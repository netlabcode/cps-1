#Topology Substation 13-10-11
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
    r13 = net.addHost('r13', cls=LinuxRouter, ip='100.13.0.1/16')
    r10 = net.addHost('r10', cls=LinuxRouter, ip='100.10.0.1/16')
    r11 = net.addHost('r11', cls=LinuxRouter, ip='100.11.0.1/16')


    #Switch External Gateway
    s777 = net.addSwitch( 's777' )

    #Switch on Control Center
    s999 = net.addSwitch( 's999' )

    #Switch on Substation
    s131 = net.addSwitch( 's131' )
    s132 = net.addSwitch( 's132' )
    s133 = net.addSwitch( 's133' )
    s101 = net.addSwitch( 's101' )
    s102 = net.addSwitch( 's102' )
    s103 = net.addSwitch( 's103' )
    s111 = net.addSwitch( 's111' )
    s112 = net.addSwitch( 's112' )
    s113 = net.addSwitch( 's113' )

    # Add host-switch links in the same subnet
    net.addLink(s999, r0, intfName2='r0-eth1', params2={'ip': '100.0.0.1/16'})
    net.addLink(s131, r13, intfName2='r13-eth1', params2={'ip': '100.13.0.1/16'})
    net.addLink(s101, r10, intfName2='r10-eth1', params2={'ip': '100.10.0.1/16'})
    net.addLink(s111, r11, intfName2='r11-eth1', params2={'ip': '100.11.0.1/16'})

     # Add router-router link in a new subnet for the router-router connection
    net.addLink(r0, r13, intfName1='r0-eth3', intfName2='r13-eth2', params1={'ip': '200.13.0.1/24'}, params2={'ip': '200.13.0.2/24'})
    net.addLink(r0, r10, intfName1='r0-eth2', intfName2='r10-eth2', params1={'ip': '200.10.0.1/24'}, params2={'ip': '200.10.0.2/24'})
    net.addLink(r0, r11, intfName1='r0-eth4', intfName2='r11-eth2', params1={'ip': '200.11.0.1/24'}, params2={'ip': '200.11.0.2/24'})

    #Add Host on Control Center
    ccdb = net.addHost('ccdb', ip='100.0.0.11')
    cctl = net.addHost('cctl', ip='100.0.0.12')

    #Add Hosts on Substation 13
    s13m1 = net.addHost('s13m1', ip='100.13.0.11', cls=CPULimitedHost, cpu=.1)
    s13m2 = net.addHost('s13m2', ip='100.13.0.12', cls=CPULimitedHost, cpu=.1)
    s13m3 = net.addHost('s13m3', ip='100.13.0.13', cls=CPULimitedHost, cpu=.1)
    s13m4 = net.addHost('s13m4', ip='100.13.0.14', cls=CPULimitedHost, cpu=.1)
    s13m5 = net.addHost('s13m5', ip='100.13.0.15', cls=CPULimitedHost, cpu=.1)
    s13m6 = net.addHost('s13m6', ip='100.13.0.16', cls=CPULimitedHost, cpu=.1)
    s13m7 = net.addHost('s13m7', ip='100.13.0.17', cls=CPULimitedHost, cpu=.1)
    s13m8 = net.addHost('s13m8', ip='100.13.0.18', cls=CPULimitedHost, cpu=.1)
    s13m9 = net.addHost('s13m9', ip='100.13.0.19', cls=CPULimitedHost, cpu=.1)
    s13cpc = net.addHost('s13cpc', ip='100.13.0.21')
    s13db = net.addHost('s13db', ip='100.13.0.22')
    s13gw = net.addHost('s13gw', ip='100.13.0.23')

    #Add Hosts on Substation 10
    s10m1 = net.addHost('s10m1', ip='100.10.0.11', cls=CPULimitedHost, cpu=.1)
    s10m2 = net.addHost('s10m2', ip='100.10.0.12', cls=CPULimitedHost, cpu=.1)
    s10m3 = net.addHost('s10m3', ip='100.10.0.13', cls=CPULimitedHost, cpu=.1)
    s10m4 = net.addHost('s10m4', ip='100.10.0.14', cls=CPULimitedHost, cpu=.1)
    s10m5 = net.addHost('s10m5', ip='100.10.0.15', cls=CPULimitedHost, cpu=.1)
    s10m6 = net.addHost('s10m6', ip='100.10.0.16', cls=CPULimitedHost, cpu=.1)
    s10cpc = net.addHost('s10cpc', ip='100.10.0.21')
    s10db = net.addHost('s10db', ip='100.10.0.22')
    s10gw = net.addHost('s10gw', ip='100.10.0.23')

    #Add Hosts on Substation 17
    s11m1 = net.addHost('s11m1', ip='100.11.0.11', cls=CPULimitedHost, cpu=.1)
    s11m2 = net.addHost('s11m2', ip='100.11.0.12', cls=CPULimitedHost, cpu=.1)
    s11m3 = net.addHost('s11m3', ip='100.11.0.13', cls=CPULimitedHost, cpu=.1)
    s11m4 = net.addHost('s11m4', ip='100.11.0.14', cls=CPULimitedHost, cpu=.1)
    s11m5 = net.addHost('s11m5', ip='100.11.0.15', cls=CPULimitedHost, cpu=.1)
    s11m6 = net.addHost('s11m6', ip='100.11.0.16', cls=CPULimitedHost, cpu=.1)
    s11cpc = net.addHost('s11cpc', ip='100.11.0.21')
    s11db = net.addHost('s11db', ip='100.11.0.22')
    s11gw = net.addHost('s11gw', ip='100.11.0.23')

    # Link siwtch to switch
    net.addLink(s131,s132)
    net.addLink(s133,s132)
    net.addLink(s101,s102)
    net.addLink(s103,s102)
    net.addLink(s111,s112)
    net.addLink(s113,s112)


    # Link Control Center to Switch
    net.addLink(ccdb,s999, intfName1='ccdb-eth1', params1={'ip':'100.0.0.11/24'})
    net.addLink(cctl,s999, intfName1='cctl-eth1', params1={'ip':'100.0.0.12/24'})

    # Link Substation 13 Merging unit to Switch
    net.addLink(s13m1,s133, intfName1='s13m1-eth1', params1={'ip':'100.13.0.11/24'})
    net.addLink(s13m2,s133, intfName1='s13m2-eth1', params1={'ip':'100.13.0.12/24'})
    net.addLink(s13m3,s133, intfName1='s13m3-eth1', params1={'ip':'100.13.0.13/24'})
    net.addLink(s13m4,s133, intfName1='s13m4-eth1', params1={'ip':'100.13.0.14/24'})
    net.addLink(s13m5,s133, intfName1='s13m5-eth1', params1={'ip':'100.13.0.15/24'})
    net.addLink(s13m6,s133, intfName1='s13m6-eth1', params1={'ip':'100.13.0.16/24'})
    net.addLink(s13m7,s133, intfName1='s13m7-eth1', params1={'ip':'100.13.0.17/24'})
    net.addLink(s13m8,s133, intfName1='s13m8-eth1', params1={'ip':'100.13.0.18/24'})
    net.addLink(s13m9,s133, intfName1='s13m9-eth1', params1={'ip':'100.13.0.19/24'})  
    net.addLink(s13cpc,s132)
    net.addLink(s13db,s132)
    net.addLink(s13gw,s131, intfName1='s13gw-eth1', params1={'ip':'100.13.0.23/24'})
    
    # Link Substation 10 Merging unit to Switch
    net.addLink(s10m1,s103, intfName1='s10m1-eth1', params1={'ip':'100.10.0.11/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s10m2,s103, intfName1='s10m2-eth1', params1={'ip':'100.10.0.12/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s10m3,s103, intfName1='s10m3-eth1', params1={'ip':'100.10.0.13/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s10m4,s103, intfName1='s10m4-eth1', params1={'ip':'100.10.0.14/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s10m5,s103, intfName1='s10m5-eth1', params1={'ip':'100.10.0.15/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s10m6,s103, intfName1='s10m6-eth1', params1={'ip':'100.10.0.16/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s10cpc,s102)
    net.addLink(s10db,s102)
    net.addLink(s10gw,s101, intfName1='s10gw-eth1', params1={'ip':'100.10.0.23/24'})

    # Link Substation 11 Merging unit to Switch
    net.addLink(s11m1,s113, intfName1='s11m1-eth1', params1={'ip':'100.11.0.11/24'})
    net.addLink(s11m2,s113, intfName1='s11m2-eth1', params1={'ip':'100.11.0.12/24'})
    net.addLink(s11m3,s113, intfName1='s11m3-eth1', params1={'ip':'100.11.0.13/24'})
    net.addLink(s11m4,s113, intfName1='s11m4-eth1', params1={'ip':'100.11.0.14/24'})
    net.addLink(s11m5,s113, intfName1='s11m5-eth1', params1={'ip':'100.11.0.15/24'})
    net.addLink(s11m6,s113, intfName1='s11m6-eth1', params1={'ip':'100.11.0.16/24'}) 
    net.addLink(s11cpc,s112)
    net.addLink(s11db,s112)
    net.addLink(s11gw,s111, intfName1='s11gw-eth1', params1={'ip':'100.11.0.23/24'})


    # Link Host Control Center to External gateway
    net.addLink(ccdb,s777, intfName1='ccdb-eth0', params1={'ip':'10.0.0.11/16'})
    net.addLink(cctl,s777, intfName1='cctl-eth0', params1={'ip':'10.0.0.12/16'})

    # Link Host Substation 13 to switch to external gateway
    net.addLink(s13m1,s777, intfName1='s13m1-eth0', params1={'ip':'10.0.13.11/16'})
    net.addLink(s13m2,s777, intfName1='s13m2-eth0', params1={'ip':'10.0.13.12/16'})
    net.addLink(s13m3,s777, intfName1='s13m3-eth0', params1={'ip':'10.0.13.13/16'})
    net.addLink(s13m4,s777, intfName1='s13m4-eth0', params1={'ip':'10.0.13.14/16'})
    net.addLink(s13m5,s777, intfName1='s13m5-eth0', params1={'ip':'10.0.13.15/16'})
    net.addLink(s13m6,s777, intfName1='s13m6-eth0', params1={'ip':'10.0.13.16/16'})
    net.addLink(s13m7,s777, intfName1='s13m7-eth0', params1={'ip':'10.0.13.17/16'})
    net.addLink(s13m8,s777, intfName1='s13m8-eth0', params1={'ip':'10.0.13.18/16'})
    net.addLink(s13m9,s777, intfName1='s13m9-eth0', params1={'ip':'10.0.13.19/16'})
    net.addLink(s13gw,s777, intfName1='s13gw-eth0', params1={'ip':'10.0.13.23/16'})
    
    # Link Host Substation 10 to switch to external gateway
    net.addLink(s10m1,s777, intfName1='s10m1-eth0', params1={'ip':'10.0.10.11/16'})
    net.addLink(s10m2,s777, intfName1='s10m2-eth0', params1={'ip':'10.0.10.12/16'})
    net.addLink(s10m3,s777, intfName1='s10m3-eth0', params1={'ip':'10.0.10.13/16'})
    net.addLink(s10m4,s777, intfName1='s10m4-eth0', params1={'ip':'10.0.10.14/16'})
    net.addLink(s10m5,s777, intfName1='s10m5-eth0', params1={'ip':'10.0.10.15/16'})
    net.addLink(s10m6,s777, intfName1='s10m6-eth0', params1={'ip':'10.0.10.16/16'})
    net.addLink(s10gw,s777, intfName1='s10gw-eth0', params1={'ip':'10.0.10.23/16'})

    # Link Host Substation 11 to switch to external gateway
    net.addLink(s11m1,s777, intfName1='s11m1-eth0', params1={'ip':'10.0.11.11/16'})
    net.addLink(s11m2,s777, intfName1='s11m2-eth0', params1={'ip':'10.0.11.12/16'})
    net.addLink(s11m3,s777, intfName1='s11m3-eth0', params1={'ip':'10.0.11.13/16'})
    net.addLink(s11m4,s777, intfName1='s11m4-eth0', params1={'ip':'10.0.11.14/16'})
    net.addLink(s11m5,s777, intfName1='s11m5-eth0', params1={'ip':'10.0.11.15/16'})
    net.addLink(s11m6,s777, intfName1='s11m6-eth0', params1={'ip':'10.0.11.16/16'})
    net.addLink(s11gw,s777, intfName1='s11gw-eth0', params1={'ip':'10.0.11.23/16'})

    


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
    info( net[ 'r0' ].cmd( 'ip route add 100.13.0.0/24 via 200.13.0.2 dev r0-eth3' ) )
    info( net[ 'r13' ].cmd( 'ip route add 100.0.0.0/24 via 200.13.0.1 dev r13-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.10.0.0/24 via 200.10.0.2 dev r0-eth2' ) )
    info( net[ 'r10' ].cmd( 'ip route add 100.0.0.0/24 via 200.10.0.1 dev r10-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.11.0.0/24 via 200.11.0.2 dev r0-eth4' ) )
    info( net[ 'r11' ].cmd( 'ip route add 100.0.0.0/24 via 200.11.0.1 dev r11-eth2' ) )

    info( net[ 's13m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.13.0.1 dev s13m1-eth1' ) )
    info( net[ 's13m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.13.0.1 dev s13m2-eth1' ) )
    info( net[ 's13m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.13.0.1 dev s13m3-eth1' ) )
    info( net[ 's13m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.13.0.1 dev s13m4-eth1' ) )
    info( net[ 's13m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.13.0.1 dev s13m5-eth1' ) )
    info( net[ 's13m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.13.0.1 dev s13m6-eth1' ) )
    info( net[ 's13m7' ].cmd( 'ip route add 100.0.0.0/24 via 100.13.0.1 dev s13m7-eth1' ) )
    info( net[ 's13m8' ].cmd( 'ip route add 100.0.0.0/24 via 100.13.0.1 dev s13m8-eth1' ) )
    info( net[ 's13m9' ].cmd( 'ip route add 100.0.0.0/24 via 100.13.0.1 dev s13m9-eth1' ) )

    info( net[ 's10m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.10.0.1 dev s10m1-eth1' ) )
    info( net[ 's10m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.10.0.1 dev s10m2-eth1' ) )
    info( net[ 's10m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.10.0.1 dev s10m3-eth1' ) )
    info( net[ 's10m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.10.0.1 dev s10m4-eth1' ) )
    info( net[ 's10m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.10.0.1 dev s10m5-eth1' ) )
    info( net[ 's10m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.10.0.1 dev s10m6-eth1' ) )

    info( net[ 's11m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.11.0.1 dev s11m1-eth1' ) )
    info( net[ 's11m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.11.0.1 dev s11m2-eth1' ) )
    info( net[ 's11m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.11.0.1 dev s11m3-eth1' ) )
    info( net[ 's11m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.11.0.1 dev s11m4-eth1' ) )
    info( net[ 's11m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.11.0.1 dev s11m5-eth1' ) )
    info( net[ 's11m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.11.0.1 dev s11m6-eth1' ) )
    
    info( net[ 'ccdb' ].cmd( 'ip route add 100.13.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.10.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.11.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )

    info( net[ 'cctl' ].cmd( 'ip route add 100.13.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.10.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.11.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    
    info(os.system('ip addr add 100.0.0.99/24 dev s999'))
    info(os.system('ip link set s999 up'))

    #time.sleep(5)

    #info( net[ 's06db' ].cmd( 'python3 ascdb.py &amp' ) )


    CLI( net )
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()