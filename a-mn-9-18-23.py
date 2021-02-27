#Topology Substation 9-18-23
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
    r9 = net.addHost('r9', cls=LinuxRouter, ip='100.9.0.1/16')
    r18 = net.addHost('r18', cls=LinuxRouter, ip='100.18.0.1/16')
    r23 = net.addHost('r23', cls=LinuxRouter, ip='100.23.0.1/16')


    #Switch External Gateway
    s777 = net.addSwitch( 's777' )

    #Switch on Control Center
    s999 = net.addSwitch( 's999' )

    #Switch on Substation
    s91 = net.addSwitch( 's91' )
    s92 = net.addSwitch( 's92' )
    s93 = net.addSwitch( 's93' )
    s181 = net.addSwitch( 's181' )
    s182 = net.addSwitch( 's182' )
    s183 = net.addSwitch( 's183' )
    s231 = net.addSwitch( 's231' )
    s232 = net.addSwitch( 's232' )
    s233 = net.addSwitch( 's233' )

    # Add host-switch links in the same subnet
    net.addLink(s999, r0, intfName2='r0-eth1', params2={'ip': '100.0.0.1/16'})
    net.addLink(s91, r9, intfName2='r9-eth1', params2={'ip': '100.9.0.1/16'})
    net.addLink(s181, r18, intfName2='r18-eth1', params2={'ip': '100.18.0.1/16'})
    net.addLink(s231, r23, intfName2='r23-eth1', params2={'ip': '100.23.0.1/16'})

     # Add router-router link in a new subnet for the router-router connection
    net.addLink(r0, r9, intfName1='r0-eth3', intfName2='r9-eth2', params1={'ip': '200.9.0.1/24'}, params2={'ip': '200.9.0.2/24'})
    net.addLink(r0, r18, intfName1='r0-eth2', intfName2='r18-eth2', params1={'ip': '200.18.0.1/24'}, params2={'ip': '200.18.0.2/24'})
    net.addLink(r0, r23, intfName1='r0-eth4', intfName2='r23-eth2', params1={'ip': '200.23.0.1/24'}, params2={'ip': '200.23.0.2/24'})

    #Add Host on Control Center
    ccdb = net.addHost('ccdb', ip='100.0.0.11')
    cctl = net.addHost('cctl', ip='100.0.0.12')

    #Add Hosts on Substation 9
    s09m1 = net.addHost('s09m1', ip='100.9.0.11', cls=CPULimitedHost, cpu=.1)
    s09m2 = net.addHost('s09m2', ip='100.9.0.12', cls=CPULimitedHost, cpu=.1)
    s09m3 = net.addHost('s09m3', ip='100.9.0.13', cls=CPULimitedHost, cpu=.1)
    s09m4 = net.addHost('s09m4', ip='100.9.0.14', cls=CPULimitedHost, cpu=.1)
    s09m5 = net.addHost('s09m5', ip='100.9.0.15', cls=CPULimitedHost, cpu=.1)
    s09m6 = net.addHost('s09m6', ip='100.9.0.16', cls=CPULimitedHost, cpu=.1)
    s09m7 = net.addHost('s09m7', ip='100.9.0.17', cls=CPULimitedHost, cpu=.1)
    s09m8 = net.addHost('s09m8', ip='100.9.0.18', cls=CPULimitedHost, cpu=.1)
    s09m9 = net.addHost('s09m9', ip='100.9.0.19', cls=CPULimitedHost, cpu=.1)
    s09cpc = net.addHost('s09cpc', ip='100.9.0.21')
    s09db = net.addHost('s09db', ip='100.9.0.22')
    s09gw = net.addHost('s09gw', ip='100.9.0.23')

    #Add Hosts on Substation 18
    s18m1 = net.addHost('s18m1', ip='100.18.0.11', cls=CPULimitedHost, cpu=.1)
    s18m2 = net.addHost('s18m2', ip='100.18.0.12', cls=CPULimitedHost, cpu=.1)
    s18m3 = net.addHost('s18m3', ip='100.18.0.13', cls=CPULimitedHost, cpu=.1)
    s18m4 = net.addHost('s18m4', ip='100.18.0.14', cls=CPULimitedHost, cpu=.1)
    s18m5 = net.addHost('s18m5', ip='100.18.0.15', cls=CPULimitedHost, cpu=.1)
    s18m6 = net.addHost('s18m6', ip='100.18.0.16', cls=CPULimitedHost, cpu=.1)
    s18cpc = net.addHost('s18cpc', ip='100.18.0.21')
    s18db = net.addHost('s18db', ip='100.18.0.22')
    s18gw = net.addHost('s18gw', ip='100.18.0.23')

    #Add Hosts on Substation 17
    s23m1 = net.addHost('s23m1', ip='100.23.0.11', cls=CPULimitedHost, cpu=.1)
    s23m2 = net.addHost('s23m2', ip='100.23.0.12', cls=CPULimitedHost, cpu=.1)
    s23m3 = net.addHost('s23m3', ip='100.23.0.13', cls=CPULimitedHost, cpu=.1)
    s23m4 = net.addHost('s23m4', ip='100.23.0.14', cls=CPULimitedHost, cpu=.1)
    s23m5 = net.addHost('s23m5', ip='100.23.0.15', cls=CPULimitedHost, cpu=.1)
    s23m6 = net.addHost('s23m6', ip='100.23.0.16', cls=CPULimitedHost, cpu=.1)
    s23cpc = net.addHost('s23cpc', ip='100.23.0.21')
    s23db = net.addHost('s23db', ip='100.23.0.22')
    s23gw = net.addHost('s23gw', ip='100.23.0.23')

    # Link siwtch to switch
    net.addLink(s91,s92)
    net.addLink(s93,s92)
    net.addLink(s181,s182)
    net.addLink(s183,s182)
    net.addLink(s231,s232)
    net.addLink(s233,s232)

    # Link Control Center to Switch
    net.addLink(ccdb,s999, intfName1='ccdb-eth1', params1={'ip':'100.0.0.11/24'})
    net.addLink(cctl,s999, intfName1='cctl-eth1', params1={'ip':'100.0.0.12/24'})

    # Link Substation 09 Merging unit to Switch
    net.addLink(s09m1,s93, intfName1='s09m1-eth1', params1={'ip':'100.9.0.11/24'})
    net.addLink(s09m2,s93, intfName1='s09m2-eth1', params1={'ip':'100.9.0.12/24'})
    net.addLink(s09m3,s93, intfName1='s09m3-eth1', params1={'ip':'100.9.0.13/24'})
    net.addLink(s09m4,s93, intfName1='s09m4-eth1', params1={'ip':'100.9.0.14/24'})
    net.addLink(s09m5,s93, intfName1='s09m5-eth1', params1={'ip':'100.9.0.15/24'})
    net.addLink(s09m6,s93, intfName1='s09m6-eth1', params1={'ip':'100.9.0.16/24'})
    net.addLink(s09m7,s93, intfName1='s09m7-eth1', params1={'ip':'100.9.0.17/24'})
    net.addLink(s09m8,s93, intfName1='s09m8-eth1', params1={'ip':'100.9.0.18/24'})
    net.addLink(s09m9,s93, intfName1='s09m9-eth1', params1={'ip':'100.9.0.19/24'})  
    net.addLink(s09cpc,s92)
    net.addLink(s09db,s92)
    net.addLink(s09gw,s91, intfName1='s09gw-eth1', params1={'ip':'100.9.0.23/24'})
    
    # Link Substation 18 Merging unit to Switch
    net.addLink(s18m1,s183, intfName1='s18m1-eth1', params1={'ip':'100.18.0.11/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s18m2,s183, intfName1='s18m2-eth1', params1={'ip':'100.18.0.12/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s18m3,s183, intfName1='s18m3-eth1', params1={'ip':'100.18.0.13/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s18m4,s183, intfName1='s18m4-eth1', params1={'ip':'100.18.0.14/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s18m5,s183, intfName1='s18m5-eth1', params1={'ip':'100.18.0.15/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s18m6,s183, intfName1='s18m6-eth1', params1={'ip':'100.18.0.16/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s18cpc,s182)
    net.addLink(s18db,s182)
    net.addLink(s18gw,s181, intfName1='s18gw-eth1', params1={'ip':'100.18.0.23/24'})

    # Link Substation 23 Merging unit to Switch
    net.addLink(s23m1,s233, intfName1='s23m1-eth1', params1={'ip':'100.23.0.11/24'})
    net.addLink(s23m2,s233, intfName1='s23m2-eth1', params1={'ip':'100.23.0.12/24'})
    net.addLink(s23m3,s233, intfName1='s23m3-eth1', params1={'ip':'100.23.0.13/24'})
    net.addLink(s23m4,s233, intfName1='s23m4-eth1', params1={'ip':'100.23.0.14/24'})
    net.addLink(s23m5,s233, intfName1='s23m5-eth1', params1={'ip':'100.23.0.15/24'})
    net.addLink(s23m6,s233, intfName1='s23m6-eth1', params1={'ip':'100.23.0.16/24'}) 
    net.addLink(s23cpc,s232)
    net.addLink(s23db,s232)
    net.addLink(s23gw,s231, intfName1='s23gw-eth1', params1={'ip':'100.23.0.23/24'})


    # Link Host Control Center to External gateway
    net.addLink(ccdb,s777, intfName1='ccdb-eth0', params1={'ip':'10.0.0.11/16'})
    net.addLink(cctl,s777, intfName1='cctl-eth0', params1={'ip':'10.0.0.12/16'})

    # Link Host Substation 13 to switch to external gateway
    net.addLink(s09m1,s777, intfName1='s09m1-eth0', params1={'ip':'10.0.9.11/16'})
    net.addLink(s09m2,s777, intfName1='s09m2-eth0', params1={'ip':'10.0.9.12/16'})
    net.addLink(s09m3,s777, intfName1='s09m3-eth0', params1={'ip':'10.0.9.13/16'})
    net.addLink(s09m4,s777, intfName1='s09m4-eth0', params1={'ip':'10.0.9.14/16'})
    net.addLink(s09m5,s777, intfName1='s09m5-eth0', params1={'ip':'10.0.9.15/16'})
    net.addLink(s09m6,s777, intfName1='s09m6-eth0', params1={'ip':'10.0.9.16/16'})
    net.addLink(s09m7,s777, intfName1='s09m7-eth0', params1={'ip':'10.0.9.17/16'})
    net.addLink(s09m8,s777, intfName1='s09m8-eth0', params1={'ip':'10.0.9.18/16'})
    net.addLink(s09m9,s777, intfName1='s09m9-eth0', params1={'ip':'10.0.9.19/16'})
    net.addLink(s09gw,s777, intfName1='s09gw-eth0', params1={'ip':'10.0.9.23/16'})
    
    # Link Host Substation 10 to switch to external gateway
    net.addLink(s18m1,s777, intfName1='s18m1-eth0', params1={'ip':'10.0.18.11/16'})
    net.addLink(s18m2,s777, intfName1='s18m2-eth0', params1={'ip':'10.0.18.12/16'})
    net.addLink(s18m3,s777, intfName1='s18m3-eth0', params1={'ip':'10.0.18.13/16'})
    net.addLink(s18m4,s777, intfName1='s18m4-eth0', params1={'ip':'10.0.18.14/16'})
    net.addLink(s18m5,s777, intfName1='s18m5-eth0', params1={'ip':'10.0.18.15/16'})
    net.addLink(s18m6,s777, intfName1='s18m6-eth0', params1={'ip':'10.0.18.16/16'})
    net.addLink(s18gw,s777, intfName1='s18gw-eth0', params1={'ip':'10.0.18.23/16'})

    # Link Host Substation 11 to switch to external gateway
    net.addLink(s23m1,s777, intfName1='s23m1-eth0', params1={'ip':'10.0.23.11/16'})
    net.addLink(s23m2,s777, intfName1='s23m2-eth0', params1={'ip':'10.0.23.12/16'})
    net.addLink(s23m3,s777, intfName1='s23m3-eth0', params1={'ip':'10.0.23.13/16'})
    net.addLink(s23m4,s777, intfName1='s23m4-eth0', params1={'ip':'10.0.23.14/16'})
    net.addLink(s23m5,s777, intfName1='s23m5-eth0', params1={'ip':'10.0.23.15/16'})
    net.addLink(s23m6,s777, intfName1='s23m6-eth0', params1={'ip':'10.0.23.16/16'})
    net.addLink(s23gw,s777, intfName1='s23gw-eth0', params1={'ip':'10.0.23.23/16'})

    


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
    info( net[ 'r0' ].cmd( 'ip route add 100.9.0.0/24 via 200.9.0.2 dev r0-eth3' ) )
    info( net[ 'r9' ].cmd( 'ip route add 100.0.0.0/24 via 200.9.0.1 dev r9-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.18.0.0/24 via 200.18.0.2 dev r0-eth2' ) )
    info( net[ 'r18' ].cmd( 'ip route add 100.0.0.0/24 via 200.18.0.1 dev r18-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.23.0.0/24 via 200.23.0.2 dev r0-eth4' ) )
    info( net[ 'r23' ].cmd( 'ip route add 100.0.0.0/24 via 200.23.0.1 dev r23-eth2' ) )

    info( net[ 's09m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.9.0.1 dev s09m1-eth1' ) )
    info( net[ 's09m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.9.0.1 dev s09m2-eth1' ) )
    info( net[ 's09m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.9.0.1 dev s09m3-eth1' ) )
    info( net[ 's09m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.9.0.1 dev s09m4-eth1' ) )
    info( net[ 's09m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.9.0.1 dev s09m5-eth1' ) )
    info( net[ 's09m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.9.0.1 dev s09m6-eth1' ) )
    info( net[ 's09m7' ].cmd( 'ip route add 100.0.0.0/24 via 100.9.0.1 dev s09m7-eth1' ) )
    info( net[ 's09m8' ].cmd( 'ip route add 100.0.0.0/24 via 100.9.0.1 dev s09m8-eth1' ) )
    info( net[ 's09m9' ].cmd( 'ip route add 100.0.0.0/24 via 100.9.0.1 dev s09m9-eth1' ) )

    info( net[ 's18m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.18.0.1 dev s18m1-eth1' ) )
    info( net[ 's18m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.18.0.1 dev s18m2-eth1' ) )
    info( net[ 's18m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.18.0.1 dev s18m3-eth1' ) )
    info( net[ 's18m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.18.0.1 dev s18m4-eth1' ) )
    info( net[ 's18m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.18.0.1 dev s18m5-eth1' ) )
    info( net[ 's18m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.18.0.1 dev s18m6-eth1' ) )

    info( net[ 's23m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.23.0.1 dev s23m1-eth1' ) )
    info( net[ 's23m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.23.0.1 dev s23m2-eth1' ) )
    info( net[ 's23m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.23.0.1 dev s23m3-eth1' ) )
    info( net[ 's23m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.23.0.1 dev s23m4-eth1' ) )
    info( net[ 's23m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.23.0.1 dev s23m5-eth1' ) )
    info( net[ 's23m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.23.0.1 dev s23m6-eth1' ) )
    
    info( net[ 'ccdb' ].cmd( 'ip route add 100.9.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.18.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.23.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )

    info( net[ 'cctl' ].cmd( 'ip route add 100.9.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.18.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.23.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    
    info(os.system('ip addr add 100.0.0.99/24 dev s999'))
    info(os.system('ip link set s999 up'))

    #time.sleep(5)

    #info( net[ 's06db' ].cmd( 'python3 ascdb.py &amp' ) )


    CLI( net )
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()