#Topology Substation 7-8-17
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
    r7 = net.addHost('r7', cls=LinuxRouter, ip='100.7.0.1/16')
    r8 = net.addHost('r8', cls=LinuxRouter, ip='100.8.0.1/16')
    r17 = net.addHost('r17', cls=LinuxRouter, ip='100.17.0.1/16')


    #Switch External Gateway
    s777 = net.addSwitch( 's777' )

    #Switch on Control Center
    s999 = net.addSwitch( 's999' )

    #Switch on Substation
    s71 = net.addSwitch( 's71' )
    s72 = net.addSwitch( 's72' )
    s73 = net.addSwitch( 's73' )
    s81 = net.addSwitch( 's81' )
    s82 = net.addSwitch( 's82' )
    s83 = net.addSwitch( 's83' )
    s171 = net.addSwitch( 's171' )
    s172 = net.addSwitch( 's172' )
    s173 = net.addSwitch( 's173' )

    # Add host-switch links in the same subnet
    net.addLink(s999, r0, intfName2='r0-eth1', params2={'ip': '100.0.0.1/16'})
    net.addLink(s71, r7, intfName2='r7-eth1', params2={'ip': '100.7.0.1/16'})
    net.addLink(s81, r8, intfName2='r8-eth1', params2={'ip': '100.8.0.1/16'})
    net.addLink(s171, r17, intfName2='r17-eth1', params2={'ip': '100.17.0.1/16'})

     # Add router-router link in a new subnet for the router-router connection
    net.addLink(r0, r7, intfName1='r0-eth3', intfName2='r7-eth2', params1={'ip': '200.7.0.1/24'}, params2={'ip': '200.7.0.2/24'})
    net.addLink(r0, r8, intfName1='r0-eth2', intfName2='r8-eth2', params1={'ip': '200.8.0.1/24'}, params2={'ip': '200.8.0.2/24'})
    net.addLink(r0, r17, intfName1='r0-eth4', intfName2='r17-eth2', params1={'ip': '200.17.0.1/24'}, params2={'ip': '200.17.0.2/24'})

    #Add Host on Control Center
    ccdb = net.addHost('ccdb', ip='100.0.0.11')
    cctl = net.addHost('cctl', ip='100.0.0.12')

    #Add Hosts on Substation 7
    s07m1 = net.addHost('s07m1', ip='100.7.0.11', cls=CPULimitedHost, cpu=.1)
    s07m2 = net.addHost('s07m2', ip='100.7.0.12', cls=CPULimitedHost, cpu=.1)
    s07m3 = net.addHost('s07m3', ip='100.7.0.13', cls=CPULimitedHost, cpu=.1)
    s07m4 = net.addHost('s07m4', ip='100.7.0.14', cls=CPULimitedHost, cpu=.1)
    s07m5 = net.addHost('s07m5', ip='100.7.0.15', cls=CPULimitedHost, cpu=.1)
    s07m6 = net.addHost('s07m6', ip='100.7.0.16', cls=CPULimitedHost, cpu=.1)
    s07m7 = net.addHost('s07m7', ip='100.7.0.17', cls=CPULimitedHost, cpu=.1)
    s07m8 = net.addHost('s07m8', ip='100.7.0.18', cls=CPULimitedHost, cpu=.1)
    s07m9 = net.addHost('s07m9', ip='100.7.0.19', cls=CPULimitedHost, cpu=.1)
    s07cpc = net.addHost('s07cpc', ip='100.7.0.21')
    s07db = net.addHost('s07db', ip='100.7.0.22')
    s07gw = net.addHost('s07gw', ip='100.7.0.23')

    #Add Hosts on Substation 8
    s08m1 = net.addHost('s08m1', ip='100.8.0.11', cls=CPULimitedHost, cpu=.1)
    s08m2 = net.addHost('s08m2', ip='100.8.0.12', cls=CPULimitedHost, cpu=.1)
    s08m3 = net.addHost('s08m3', ip='100.8.0.13', cls=CPULimitedHost, cpu=.1)
    s08m4 = net.addHost('s08m4', ip='100.8.0.14', cls=CPULimitedHost, cpu=.1)
    s08m5 = net.addHost('s08m5', ip='100.8.0.15', cls=CPULimitedHost, cpu=.1)
    s08m6 = net.addHost('s08m6', ip='100.8.0.16', cls=CPULimitedHost, cpu=.1)
    s08cpc = net.addHost('s08cpc', ip='100.8.0.21')
    s08db = net.addHost('s08db', ip='100.8.0.22')
    s08gw = net.addHost('s08gw', ip='100.8.0.23')

    #Add Hosts on Substation 17
    s17m1 = net.addHost('s17m1', ip='100.17.0.11', cls=CPULimitedHost, cpu=.1)
    s17m2 = net.addHost('s17m2', ip='100.17.0.12', cls=CPULimitedHost, cpu=.1)
    s17m3 = net.addHost('s17m3', ip='100.17.0.13', cls=CPULimitedHost, cpu=.1)
    s17m4 = net.addHost('s17m4', ip='100.17.0.14', cls=CPULimitedHost, cpu=.1)
    s17m5 = net.addHost('s17m5', ip='100.17.0.15', cls=CPULimitedHost, cpu=.1)
    s17m6 = net.addHost('s17m6', ip='100.17.0.16', cls=CPULimitedHost, cpu=.1)
    s17cpc = net.addHost('s17cpc', ip='100.17.0.21')
    s17db = net.addHost('s17db', ip='100.17.0.22')
    s17gw = net.addHost('s17gw', ip='100.17.0.23')

    # Link siwtch to switch
    net.addLink(s71,s72)
    net.addLink(s73,s72)
    net.addLink(s81,s82)
    net.addLink(s83,s82)
    net.addLink(s171,s172)
    net.addLink(s173,s172)


    # Link Control Center to Switch
    net.addLink(ccdb,s999, intfName1='ccdb-eth1', params1={'ip':'100.0.0.11/24'})
    net.addLink(cctl,s999, intfName1='cctl-eth1', params1={'ip':'100.0.0.12/24'})

    # Link Substation 07 Merging unit to Switch
    net.addLink(s07m1,s73, intfName1='s07m1-eth1', params1={'ip':'100.7.0.11/24'})
    net.addLink(s07m2,s73, intfName1='s07m2-eth1', params1={'ip':'100.7.0.12/24'})
    net.addLink(s07m3,s73, intfName1='s07m3-eth1', params1={'ip':'100.7.0.13/24'})
    net.addLink(s07m4,s73, intfName1='s07m4-eth1', params1={'ip':'100.7.0.14/24'})
    net.addLink(s07m5,s73, intfName1='s07m5-eth1', params1={'ip':'100.7.0.15/24'})
    net.addLink(s07m6,s73, intfName1='s07m6-eth1', params1={'ip':'100.7.0.16/24'})
    net.addLink(s07m7,s73, intfName1='s07m7-eth1', params1={'ip':'100.7.0.17/24'})
    net.addLink(s07m8,s73, intfName1='s07m8-eth1', params1={'ip':'100.7.0.18/24'})
    net.addLink(s07m9,s73, intfName1='s07m9-eth1', params1={'ip':'100.7.0.19/24'})  
    net.addLink(s07cpc,s72)
    net.addLink(s07db,s72)
    net.addLink(s07gw,s71, intfName1='s07gw-eth1', params1={'ip':'100.7.0.23/24'})
    
    # Link Substation 08 Merging unit to Switch
    net.addLink(s08m1,s83, intfName1='s08m1-eth1', params1={'ip':'100.8.0.11/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s08m2,s83, intfName1='s08m2-eth1', params1={'ip':'100.8.0.12/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s08m3,s83, intfName1='s08m3-eth1', params1={'ip':'100.8.0.13/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s08m4,s83, intfName1='s08m4-eth1', params1={'ip':'100.8.0.14/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s08m5,s83, intfName1='s08m5-eth1', params1={'ip':'100.8.0.15/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s08m6,s83, intfName1='s08m6-eth1', params1={'ip':'100.8.0.16/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s08cpc,s82)
    net.addLink(s08db,s82)
    net.addLink(s08gw,s81, intfName1='s08gw-eth1', params1={'ip':'100.8.0.23/24'})

    # Link Substation 17 Merging unit to Switch
    net.addLink(s17m1,s173, intfName1='s17m1-eth1', params1={'ip':'100.17.0.11/24'})
    net.addLink(s17m2,s173, intfName1='s17m2-eth1', params1={'ip':'100.17.0.12/24'})
    net.addLink(s17m3,s173, intfName1='s17m3-eth1', params1={'ip':'100.17.0.13/24'})
    net.addLink(s17m4,s173, intfName1='s17m4-eth1', params1={'ip':'100.17.0.14/24'})
    net.addLink(s17m5,s173, intfName1='s17m5-eth1', params1={'ip':'100.17.0.15/24'})
    net.addLink(s17m6,s173, intfName1='s17m6-eth1', params1={'ip':'100.17.0.16/24'}) 
    net.addLink(s17cpc,s172)
    net.addLink(s17db,s172)
    net.addLink(s17gw,s171, intfName1='s17gw-eth1', params1={'ip':'100.17.0.23/24'})


    # Link Host Control Center to External gateway
    net.addLink(ccdb,s777, intfName1='ccdb-eth0', params1={'ip':'10.0.0.11/16'})
    net.addLink(cctl,s777, intfName1='cctl-eth0', params1={'ip':'10.0.0.12/16'})

    # Link Host Substation 7 to switch to external gateway
    net.addLink(s07m1,s777, intfName1='s07m1-eth0', params1={'ip':'10.0.7.11/16'})
    net.addLink(s07m2,s777, intfName1='s07m2-eth0', params1={'ip':'10.0.7.12/16'})
    net.addLink(s07m3,s777, intfName1='s07m3-eth0', params1={'ip':'10.0.7.13/16'})
    net.addLink(s07m4,s777, intfName1='s07m4-eth0', params1={'ip':'10.0.7.14/16'})
    net.addLink(s07m5,s777, intfName1='s07m5-eth0', params1={'ip':'10.0.7.15/16'})
    net.addLink(s07m6,s777, intfName1='s07m6-eth0', params1={'ip':'10.0.7.16/16'})
    net.addLink(s07m7,s777, intfName1='s07m7-eth0', params1={'ip':'10.0.7.17/16'})
    net.addLink(s07m8,s777, intfName1='s07m8-eth0', params1={'ip':'10.0.7.18/16'})
    net.addLink(s07m9,s777, intfName1='s07m9-eth0', params1={'ip':'10.0.7.19/16'})
    net.addLink(s07gw,s777, intfName1='s07gw-eth0', params1={'ip':'10.0.7.23/16'})
    
    # Link Host Substation 8 to switch to external gateway
    net.addLink(s08m1,s777, intfName1='s08m1-eth0', params1={'ip':'10.0.8.11/16'})
    net.addLink(s08m2,s777, intfName1='s08m2-eth0', params1={'ip':'10.0.8.12/16'})
    net.addLink(s08m3,s777, intfName1='s08m3-eth0', params1={'ip':'10.0.8.13/16'})
    net.addLink(s08m4,s777, intfName1='s08m4-eth0', params1={'ip':'10.0.8.14/16'})
    net.addLink(s08m5,s777, intfName1='s08m5-eth0', params1={'ip':'10.0.8.15/16'})
    net.addLink(s08m6,s777, intfName1='s08m6-eth0', params1={'ip':'10.0.8.16/16'})
    net.addLink(s08gw,s777, intfName1='s08gw-eth0', params1={'ip':'10.0.8.23/16'})

    # Link Host Substation 17 to switch to external gateway
    net.addLink(s17m1,s777, intfName1='s17m1-eth0', params1={'ip':'10.0.17.11/16'})
    net.addLink(s17m2,s777, intfName1='s17m2-eth0', params1={'ip':'10.0.17.12/16'})
    net.addLink(s17m3,s777, intfName1='s17m3-eth0', params1={'ip':'10.0.17.13/16'})
    net.addLink(s17m4,s777, intfName1='s17m4-eth0', params1={'ip':'10.0.17.14/16'})
    net.addLink(s17m5,s777, intfName1='s17m5-eth0', params1={'ip':'10.0.17.15/16'})
    net.addLink(s17m6,s777, intfName1='s17m6-eth0', params1={'ip':'10.0.17.16/16'})
    net.addLink(s17gw,s777, intfName1='s17gw-eth0', params1={'ip':'10.0.17.23/16'})

    


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
    info( net[ 'r0' ].cmd( 'ip route add 100.7.0.0/24 via 200.7.0.2 dev r0-eth3' ) )
    info( net[ 'r7' ].cmd( 'ip route add 100.0.0.0/24 via 200.7.0.1 dev r7-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.8.0.0/24 via 200.8.0.2 dev r0-eth2' ) )
    info( net[ 'r8' ].cmd( 'ip route add 100.0.0.0/24 via 200.8.0.1 dev r8-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.17.0.0/24 via 200.17.0.2 dev r0-eth4' ) )
    info( net[ 'r8' ].cmd( 'ip route add 100.0.0.0/24 via 200.17.0.1 dev r17-eth2' ) )

    info( net[ 's07m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m1-eth1' ) )
    info( net[ 's07m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m2-eth1' ) )
    info( net[ 's07m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m3-eth1' ) )
    info( net[ 's07m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m4-eth1' ) )
    info( net[ 's07m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m5-eth1' ) )
    info( net[ 's07m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m6-eth1' ) )
    info( net[ 's07m7' ].cmd( 'ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m7-eth1' ) )
    info( net[ 's07m8' ].cmd( 'ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m8-eth1' ) )
    info( net[ 's07m9' ].cmd( 'ip route add 100.0.0.0/24 via 100.7.0.1 dev s07m9-eth1' ) )

    info( net[ 's08m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.8.0.1 dev s08m1-eth1' ) )
    info( net[ 's08m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.8.0.1 dev s08m2-eth1' ) )
    info( net[ 's08m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.8.0.1 dev s08m3-eth1' ) )
    info( net[ 's08m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.8.0.1 dev s08m4-eth1' ) )
    info( net[ 's08m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.8.0.1 dev s08m5-eth1' ) )
    info( net[ 's08m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.8.0.1 dev s08m6-eth1' ) )

    info( net[ 's17m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.17.0.1 dev s17m1-eth1' ) )
    info( net[ 's17m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.17.0.1 dev s17m2-eth1' ) )
    info( net[ 's17m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.17.0.1 dev s17m3-eth1' ) )
    info( net[ 's17m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.17.0.1 dev s17m4-eth1' ) )
    info( net[ 's17m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.17.0.1 dev s17m5-eth1' ) )
    info( net[ 's17m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.17.0.1 dev s17m6-eth1' ) )
    
    info( net[ 'ccdb' ].cmd( 'ip route add 100.7.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.8.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.17.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )

    info( net[ 'cctl' ].cmd( 'ip route add 100.7.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.8.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.17.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    
    info(os.system('ip addr add 100.0.0.99/24 dev s999'))
    info(os.system('ip link set s999 up'))

    #time.sleep(5)

    #info( net[ 's06db' ].cmd( 'python3 ascdb.py &amp' ) )


    CLI( net )
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()