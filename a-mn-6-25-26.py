#Topology Substation 6-25-26
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
    r25 = net.addHost('r25', cls=LinuxRouter, ip='100.25.0.1/16')
    r26 = net.addHost('r26', cls=LinuxRouter, ip='100.26.0.1/16')


    #Switch External Gateway
    s777 = net.addSwitch( 's777' )

    #Switch on Control Center
    s999 = net.addSwitch( 's999' )

    #Switch on Substation
    s61 = net.addSwitch( 's61' )
    s62 = net.addSwitch( 's62' )
    s63 = net.addSwitch( 's63' )
    s251 = net.addSwitch( 's251' )
    s252 = net.addSwitch( 's252' )
    s253 = net.addSwitch( 's253' )
    s261 = net.addSwitch( 's261' )
    s262 = net.addSwitch( 's262' )
    s263 = net.addSwitch( 's263' )

    # Add host-switch links in the same subnet
    net.addLink(s999, r0, intfName2='r0-eth1', params2={'ip': '100.0.0.1/16'})
    net.addLink(s61, r6, intfName2='r6-eth1', params2={'ip': '100.6.0.1/16'})
    net.addLink(s251, r25, intfName2='r25-eth1', params2={'ip': '100.25.0.1/16'})
    net.addLink(s261, r26, intfName2='r26-eth1', params2={'ip': '100.26.0.1/16'})

     # Add router-router link in a new subnet for the router-router connection
    net.addLink(r0, r6, intfName1='r0-eth3', intfName2='r6-eth2', params1={'ip': '200.6.0.1/24'}, params2={'ip': '200.6.0.2/24'})
    net.addLink(r0, r25, intfName1='r0-eth2', intfName2='r25-eth2', params1={'ip': '200.25.0.1/24'}, params2={'ip': '200.25.0.2/24'})
    net.addLink(r0, r26, intfName1='r0-eth4', intfName2='r26-eth2', params1={'ip': '200.26.0.1/24'}, params2={'ip': '200.26.0.2/24'})

    #Add Host on Control Center
    ccdb = net.addHost('ccdb', ip='100.0.0.11')
    cctl = net.addHost('cctl', ip='100.0.0.12')

    #Add Hosts on Substation 6
    s06m1 = net.addHost('s06m1', ip='100.6.0.11', cls=CPULimitedHost, cpu=.1)
    s06m2 = net.addHost('s06m2', ip='100.6.0.12', cls=CPULimitedHost, cpu=.1)
    s06m3 = net.addHost('s06m3', ip='100.6.0.13', cls=CPULimitedHost, cpu=.1)
    s06m4 = net.addHost('s06m4', ip='100.6.0.14', cls=CPULimitedHost, cpu=.1)
    s06m5 = net.addHost('s06m5', ip='100.6.0.15', cls=CPULimitedHost, cpu=.1)
    s06m6 = net.addHost('s06m6', ip='100.6.0.16', cls=CPULimitedHost, cpu=.1)
    s06m7 = net.addHost('s06m7', ip='100.6.0.17', cls=CPULimitedHost, cpu=.1)
    s06m8 = net.addHost('s06m8', ip='100.6.0.18', cls=CPULimitedHost, cpu=.1)
    s06m9 = net.addHost('s06m9', ip='100.6.0.19', cls=CPULimitedHost, cpu=.1)
    s06cpc = net.addHost('s06cpc', ip='100.6.0.21')
    s06db = net.addHost('s06db', ip='100.6.0.22')
    s06gw = net.addHost('s06gw', ip='100.6.0.23')

    #Add Hosts on Substation 25
    s25m1 = net.addHost('s25m1', ip='100.25.0.11', cls=CPULimitedHost, cpu=.1)
    s25m2 = net.addHost('s25m2', ip='100.25.0.12', cls=CPULimitedHost, cpu=.1)
    s25m3 = net.addHost('s25m3', ip='100.25.0.13', cls=CPULimitedHost, cpu=.1)
    s25m4 = net.addHost('s25m4', ip='100.25.0.14', cls=CPULimitedHost, cpu=.1)
    s25m5 = net.addHost('s25m5', ip='100.25.0.15', cls=CPULimitedHost, cpu=.1)
    s25m6 = net.addHost('s25m6', ip='100.25.0.16', cls=CPULimitedHost, cpu=.1)
    s25cpc = net.addHost('s25cpc', ip='100.25.0.21')
    s25db = net.addHost('s25db', ip='100.25.0.22')
    s25gw = net.addHost('s25gw', ip='100.25.0.23')

    #Add Hosts on Substation 17
    s26m1 = net.addHost('s26m1', ip='100.26.0.11', cls=CPULimitedHost, cpu=.1)
    s26m2 = net.addHost('s26m2', ip='100.26.0.12', cls=CPULimitedHost, cpu=.1)
    s26m3 = net.addHost('s26m3', ip='100.26.0.13', cls=CPULimitedHost, cpu=.1)
    s26m4 = net.addHost('s26m4', ip='100.26.0.14', cls=CPULimitedHost, cpu=.1)
    s26m5 = net.addHost('s26m5', ip='100.26.0.15', cls=CPULimitedHost, cpu=.1)
    s26m6 = net.addHost('s26m6', ip='100.26.0.16', cls=CPULimitedHost, cpu=.1)
    s26cpc = net.addHost('s26cpc', ip='100.26.0.21')
    s26db = net.addHost('s26db', ip='100.26.0.22')
    s26gw = net.addHost('s26gw', ip='100.26.0.23')

    # Link siwtch to switch
    net.addLink(s61,s62)
    net.addLink(s63,s62)
    net.addLink(s251,s252)
    net.addLink(s253,s252)
    net.addLink(s261,s262)
    net.addLink(s263,s262)

    # Link Control Center to Switch
    net.addLink(ccdb,s999, intfName1='ccdb-eth1', params1={'ip':'100.0.0.11/24'})
    net.addLink(cctl,s999, intfName1='cctl-eth1', params1={'ip':'100.0.0.12/24'})

    # Link Substation 06 Merging unit to Switch
    net.addLink(s06m1,s63, intfName1='s06m1-eth1', params1={'ip':'100.6.0.11/24'})
    net.addLink(s06m2,s63, intfName1='s06m2-eth1', params1={'ip':'100.6.0.12/24'})
    net.addLink(s06m3,s63, intfName1='s06m3-eth1', params1={'ip':'100.6.0.13/24'})
    net.addLink(s06m4,s63, intfName1='s06m4-eth1', params1={'ip':'100.6.0.14/24'})
    net.addLink(s06m5,s63, intfName1='s06m5-eth1', params1={'ip':'100.6.0.15/24'})
    net.addLink(s06m6,s63, intfName1='s06m6-eth1', params1={'ip':'100.6.0.16/24'})
    net.addLink(s06m7,s63, intfName1='s06m7-eth1', params1={'ip':'100.6.0.17/24'})
    net.addLink(s06m8,s63, intfName1='s06m8-eth1', params1={'ip':'100.6.0.18/24'})
    net.addLink(s06m9,s63, intfName1='s06m9-eth1', params1={'ip':'100.6.0.19/24'})  
    net.addLink(s06cpc,s62)
    net.addLink(s06db,s62)
    net.addLink(s06gw,s61, intfName1='s06gw-eth1', params1={'ip':'100.6.0.23/24'})
    
    # Link Substation 25 Merging unit to Switch
    net.addLink(s25m1,s253, intfName1='s25m1-eth1', params1={'ip':'100.25.0.11/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s25m2,s253, intfName1='s25m2-eth1', params1={'ip':'100.25.0.12/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s25m3,s253, intfName1='s25m3-eth1', params1={'ip':'100.25.0.13/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s25m4,s253, intfName1='s25m4-eth1', params1={'ip':'100.25.0.14/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s25m5,s253, intfName1='s25m5-eth1', params1={'ip':'100.25.0.15/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s25m6,s253, intfName1='s25m6-eth1', params1={'ip':'100.25.0.16/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s25cpc,s252)
    net.addLink(s25db,s252)
    net.addLink(s25gw,s251, intfName1='s25gw-eth1', params1={'ip':'100.25.0.23/24'})

    # Link Substation 26 Merging unit to Switch
    net.addLink(s26m1,s263, intfName1='s26m1-eth1', params1={'ip':'100.26.0.11/24'})
    net.addLink(s26m2,s263, intfName1='s26m2-eth1', params1={'ip':'100.26.0.12/24'})
    net.addLink(s26m3,s263, intfName1='s26m3-eth1', params1={'ip':'100.26.0.13/24'})
    net.addLink(s26m4,s263, intfName1='s26m4-eth1', params1={'ip':'100.26.0.14/24'})
    net.addLink(s26m5,s263, intfName1='s26m5-eth1', params1={'ip':'100.26.0.15/24'})
    net.addLink(s26m6,s263, intfName1='s26m6-eth1', params1={'ip':'100.26.0.16/24'}) 
    net.addLink(s26cpc,s262)
    net.addLink(s26db,s262)
    net.addLink(s26gw,s261, intfName1='s26gw-eth1', params1={'ip':'100.26.0.23/24'})


    # Link Host Control Center to External gateway
    net.addLink(ccdb,s777, intfName1='ccdb-eth0', params1={'ip':'10.0.0.11/16'})
    net.addLink(cctl,s777, intfName1='cctl-eth0', params1={'ip':'10.0.0.12/16'})

    # Link Host Substation 13 to switch to external gateway
    net.addLink(s06m1,s777, intfName1='s06m1-eth0', params1={'ip':'10.0.6.11/16'})
    net.addLink(s06m2,s777, intfName1='s06m2-eth0', params1={'ip':'10.0.6.12/16'})
    net.addLink(s06m3,s777, intfName1='s06m3-eth0', params1={'ip':'10.0.6.13/16'})
    net.addLink(s06m4,s777, intfName1='s06m4-eth0', params1={'ip':'10.0.6.14/16'})
    net.addLink(s06m5,s777, intfName1='s06m5-eth0', params1={'ip':'10.0.6.15/16'})
    net.addLink(s06m6,s777, intfName1='s06m6-eth0', params1={'ip':'10.0.6.16/16'})
    net.addLink(s06m7,s777, intfName1='s06m7-eth0', params1={'ip':'10.0.6.17/16'})
    net.addLink(s06m8,s777, intfName1='s06m8-eth0', params1={'ip':'10.0.6.18/16'})
    net.addLink(s06m9,s777, intfName1='s06m9-eth0', params1={'ip':'10.0.6.19/16'})
    net.addLink(s06gw,s777, intfName1='s06gw-eth0', params1={'ip':'10.0.6.23/16'})
    
    # Link Host Substation 10 to switch to external gateway
    net.addLink(s25m1,s777, intfName1='s25m1-eth0', params1={'ip':'10.0.25.11/16'})
    net.addLink(s25m2,s777, intfName1='s25m2-eth0', params1={'ip':'10.0.25.12/16'})
    net.addLink(s25m3,s777, intfName1='s25m3-eth0', params1={'ip':'10.0.25.13/16'})
    net.addLink(s25m4,s777, intfName1='s25m4-eth0', params1={'ip':'10.0.25.14/16'})
    net.addLink(s25m5,s777, intfName1='s25m5-eth0', params1={'ip':'10.0.25.15/16'})
    net.addLink(s25m6,s777, intfName1='s25m6-eth0', params1={'ip':'10.0.25.16/16'})
    net.addLink(s25gw,s777, intfName1='s25gw-eth0', params1={'ip':'10.0.25.23/16'})

    # Link Host Substation 11 to switch to external gateway
    net.addLink(s26m1,s777, intfName1='s26m1-eth0', params1={'ip':'10.0.26.11/16'})
    net.addLink(s26m2,s777, intfName1='s26m2-eth0', params1={'ip':'10.0.26.12/16'})
    net.addLink(s26m3,s777, intfName1='s26m3-eth0', params1={'ip':'10.0.26.13/16'})
    net.addLink(s26m4,s777, intfName1='s26m4-eth0', params1={'ip':'10.0.26.14/16'})
    net.addLink(s26m5,s777, intfName1='s26m5-eth0', params1={'ip':'10.0.26.15/16'})
    net.addLink(s26m6,s777, intfName1='s26m6-eth0', params1={'ip':'10.0.26.16/16'})
    net.addLink(s26gw,s777, intfName1='s26gw-eth0', params1={'ip':'10.0.26.23/16'})

    


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
    info( net[ 'r0' ].cmd( 'ip route add 100.6.0.0/24 via 200.6.0.2 dev r0-eth3' ) )
    info( net[ 'r6' ].cmd( 'ip route add 100.0.0.0/24 via 200.6.0.1 dev r6-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.25.0.0/24 via 200.25.0.2 dev r0-eth2' ) )
    info( net[ 'r25' ].cmd( 'ip route add 100.0.0.0/24 via 200.25.0.1 dev r25-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.26.0.0/24 via 200.26.0.2 dev r0-eth4' ) )
    info( net[ 'r26' ].cmd( 'ip route add 100.0.0.0/24 via 200.26.0.1 dev r26-eth2' ) )

    info( net[ 's06m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m1-eth1' ) )
    info( net[ 's06m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m2-eth1' ) )
    info( net[ 's06m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m3-eth1' ) )
    info( net[ 's06m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m4-eth1' ) )
    info( net[ 's06m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m5-eth1' ) )
    info( net[ 's06m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m6-eth1' ) )
    info( net[ 's06m7' ].cmd( 'ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m7-eth1' ) )
    info( net[ 's06m8' ].cmd( 'ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m8-eth1' ) )
    info( net[ 's06m9' ].cmd( 'ip route add 100.0.0.0/24 via 100.6.0.1 dev s06m9-eth1' ) )

    info( net[ 's25m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.25.0.1 dev s25m1-eth1' ) )
    info( net[ 's25m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.25.0.1 dev s25m2-eth1' ) )
    info( net[ 's25m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.25.0.1 dev s25m3-eth1' ) )
    info( net[ 's25m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.25.0.1 dev s25m4-eth1' ) )
    info( net[ 's25m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.25.0.1 dev s25m5-eth1' ) )
    info( net[ 's25m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.25.0.1 dev s25m6-eth1' ) )

    info( net[ 's26m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.26.0.1 dev s26m1-eth1' ) )
    info( net[ 's26m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.26.0.1 dev s26m2-eth1' ) )
    info( net[ 's26m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.26.0.1 dev s26m3-eth1' ) )
    info( net[ 's26m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.26.0.1 dev s26m4-eth1' ) )
    info( net[ 's26m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.26.0.1 dev s26m5-eth1' ) )
    info( net[ 's26m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.26.0.1 dev s26m6-eth1' ) )
    
    info( net[ 'ccdb' ].cmd( 'ip route add 100.6.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.25.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.26.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )

    info( net[ 'cctl' ].cmd( 'ip route add 100.6.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.25.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.26.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    
    info(os.system('ip addr add 100.0.0.99/24 dev s999'))
    info(os.system('ip link set s999 up'))

    #time.sleep(5)

    #info( net[ 's06db' ].cmd( 'python3 ascdb.py &amp' ) )


    CLI( net )
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()