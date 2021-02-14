#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Node, Controller, RemoteController, OVSSwitch, OVSKernelSwitch, Host
from mininet.cli import CLI
from mininet.link import Intf, TCLink
from mininet.log import setLogLevel, info
from mininet.node import Node, CPULimitedHost
from mininet.util import irange,dumpNodeConnections
import time
import os



class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()

def emptyNet():

    NODE2_IP='192.168.56.1'
    CONTROLLER_IP='127.0.0.1'

    net = Mininet( topo=None,
                   build=False)

    #c0 = net.addController( 'c0',controller=RemoteController,ip=CONTROLLER_IP,port=6633)
    net.addController('c0', port=6633)

    r0 = net.addHost('r0', cls=LinuxRouter, ip='100.0.0.1/16')
    r6 = net.addHost('r6', cls=LinuxRouter, ip='100.6.0.1/16')
    r7 = net.addHost('r7', cls=LinuxRouter, ip='100.7.0.1/16')

    #Switch External Gateway
    s777 = net.addSwitch( 's777' )

    #Switch on Control Center
    s999 = net.addSwitch( 's999' )

    #Switch on Substation
    s61 = net.addSwitch( 's61' )
    s62 = net.addSwitch( 's62' )
    s63 = net.addSwitch( 's63' )
    s71 = net.addSwitch( 's71' )
    s72 = net.addSwitch( 's72' )
    s73 = net.addSwitch( 's73' )

    # Add host-switch links in the same subnet
    net.addLink(s999, r0, intfName2='r0-eth1', params2={'ip': '100.0.0.1/16'})
    net.addLink(s61, r6, intfName2='r6-eth1', params2={'ip': '100.6.0.1/16'})
    net.addLink(s71, r7, intfName2='r7-eth1', params2={'ip': '100.7.0.1/16'})

     # Add router-router link in a new subnet for the router-router connection
    net.addLink(r0, r6, intfName1='r0-eth2', intfName2='r6-eth2', params1={'ip': '200.6.0.1/24'}, params2={'ip': '200.6.0.2/24'})
    net.addLink(r0, r7, intfName1='r0-eth3', intfName2='r7-eth2', params1={'ip': '200.7.0.1/24'}, params2={'ip': '200.7.0.2/24'})

    #Add Host on Control Center
    ccdb = net.addHost('ccdb', ip='100.0.0.11')
    cctl = net.addHost('cctl', ip='100.0.0.12')

    #Add Hosts on Substation 6
    s06m1 = net.addHost('s06m1', ip='100.6.0.11', cls=CPULimitedHost, cpu=.1)
    s06cpc = net.addHost('s06cpc', ip='100.6.0.21')
    s06db = net.addHost('s06db', ip='100.6.0.22')
    s06gw = net.addHost('s06gw', ip='100.6.0.23')
    hacker = net.addHost('hacker', ip='100.6.0.99')

    #Add Hosts on Substation 7
    s07m1 = net.addHost('s07m1', ip='100.7.0.11', cls=CPULimitedHost, cpu=.1)
    s07cpc = net.addHost('s07cpc', ip='100.7.0.21')
    s07db = net.addHost('s07db', ip='100.7.0.22')
    s07gw = net.addHost('s07gw', ip='100.7.0.23')

    # Link siwtch to switch
    net.addLink(s61,s62)
    net.addLink(s63,s62)
    net.addLink(s71,s72)
    net.addLink(s73,s72)
    #net.addLink(s61,s999)
    #net.addLink(s71,s999)

    # Link Control Center to Switch
    net.addLink(ccdb,s999, intfName1='ccdb-eth1', params1={'ip':'100.0.0.11/24'})
    net.addLink(cctl,s999, intfName1='cctl-eth1', params1={'ip':'100.0.0.12/24'})

    # Link Substation 06 Merging unit to Switch
    net.addLink(s06m1,s63, intfName1='s06m1-eth1', params1={'ip':'100.6.0.11/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s06cpc,s62)
    net.addLink(s06db,s62)
    net.addLink(s06gw,s61, intfName1='s06gw-eth1', params1={'ip':'100.6.0.23/24'})
    net.addLink(hacker,s61)

    # Link Substation 07 Merging unit to Switch
    net.addLink(s07m1,s73, intfName1='s07m1-eth1', params1={'ip':'100.7.0.11/24'})  
    net.addLink(s07cpc,s72)
    net.addLink(s07db,s72)
    net.addLink(s07gw,s71, intfName1='s07gw-eth1', params1={'ip':'100.7.0.23/24'})

    # Link Host Control Center to External gateway
    net.addLink(ccdb,s777, intfName1='ccdb-eth0', params1={'ip':'10.0.0.11/16'})
    net.addLink(cctl,s777, intfName1='cctl-eth0', params1={'ip':'10.0.0.12/16'})

    # Link Host Substation 6 to switch to external gateway
    net.addLink(s06m1,s777, intfName1='s06m1-eth0', params1={'ip':'10.0.6.11/16'})
    net.addLink(s06gw,s777, intfName1='s06gw-eth0', params1={'ip':'10.0.6.23/16'})

    # Link Host Substation 7 to switch to external gateway
    net.addLink(s07m1,s777, intfName1='s07m1-eth0', params1={'ip':'10.0.7.11/16'})
    net.addLink(s07gw,s777, intfName1='s07gw-eth0', params1={'ip':'10.0.7.23/16'})


    #Build and start Network ============================================================================
    net.build()
    net.addNAT(ip='10.0.0.250').configDefault()
    net.start()

    #Configure GRE Tunnel
    #s777.cmdPrint('ovs-vsctl add-port s777 s777-gre1 -- set interface s777-gre1 type=gre ofport_request=5 options:remote_ip='+NODE2_IP)
    #s777.cmdPrint('ovs-vsctl show')
    nat = net.get('nat0')
    nat.cmdPrint('ip link set mtu 1454 dev nat0-eth0')

    # Add routing for reaching networks that aren't directly connected
    info( net[ 'r0' ].cmd( 'ip route add 100.6.0.0/24 via 200.6.0.2 dev r0-eth2' ) )
    info( net[ 'r6' ].cmd( 'ip route add 100.0.0.0/24 via 200.6.0.1 dev r6-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.7.0.0/24 via 200.7.0.2 dev r0-eth3' ) )
    info( net[ 'r7' ].cmd( 'ip route add 100.0.0.0/24 via 200.7.0.1 dev r7-eth2' ) )

    info( net[ 's06m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m1-eth1' ) )
    info( net[ 's07m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m1-eth1' ) )

    info( net[ 'ccdb' ].cmd( 'ip route add 100.6.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.7.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )

    info( net[ 'cctl' ].cmd( 'ip route add 100.6.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.7.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )

    info(os.system('ip addr add 100.0.0.99/24 dev s999'))
    info(os.system('ip link set s999 up'))


    
 
    

    #time.sleep(5)

    #info( net[ 's06db' ].cmd( 'python3 ascdb.py &amp' ) )


    CLI( net )
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()