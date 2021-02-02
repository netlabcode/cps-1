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

    NODE2_IP='131.180.165.16'
    CONTROLLER_IP='127.0.0.1'

    net = Mininet( topo=None,
                   build=False)

    #c0 = net.addController( 'c0',controller=RemoteController,ip=CONTROLLER_IP,port=6633)
    net.addController('c0', port=6633)

    #Switch External Gateway
    s777 = net.addSwitch( 's777' )

    #Switch on Control Center
    s999 = net.addSwitch( 's999' )

    #Switch on Substation
 
    s11 = net.addSwitch( 's11' )
    s12 = net.addSwitch( 's12' )
    s13 = net.addSwitch( 's13' )


    """
    s31 = net.addSwitch( 's31' )
    s32 = net.addSwitch( 's32' )
    s33 = net.addSwitch( 's33' )
    s41 = net.addSwitch( 's41' )
    s42 = net.addSwitch( 's42' )
    s43 = net.addSwitch( 's43' )
    s51 = net.addSwitch( 's51' )
    s52 = net.addSwitch( 's52' )
    s53 = net.addSwitch( 's53' )
    """

    s61 = net.addSwitch( 's61' )
    s62 = net.addSwitch( 's62' )
    s63 = net.addSwitch( 's63' )
    s71 = net.addSwitch( 's71' )
    s72 = net.addSwitch( 's72' )
    s73 = net.addSwitch( 's73' )
    s21 = net.addSwitch( 's21' )
    s22 = net.addSwitch( 's22' )
    s23 = net.addSwitch( 's23' )

    #Add Hosts on Substation 6
    s06m1 = net.addHost('s06m1', ip='100.6.0.11', cls=CPULimitedHost, cpu=.1, mac='00:00:00:00:00:01')
    s06m2 = net.addHost('s06m2', ip='100.6.0.12', cls=CPULimitedHost, cpu=.1, mac='00:00:00:00:00:02')
    s06m3 = net.addHost('s06m3', ip='100.6.0.13', cls=CPULimitedHost, cpu=.1, mac='00:00:00:00:00:03')
    s06m4 = net.addHost('s06m4', ip='100.6.0.14', cls=CPULimitedHost, cpu=.1, mac='00:00:00:00:00:04')
    s06m5 = net.addHost('s06m5', ip='100.6.0.15', cls=CPULimitedHost, cpu=.1, mac='00:00:00:00:00:05')
    s06m6 = net.addHost('s06m6', ip='100.6.0.16', cls=CPULimitedHost, cpu=.1, mac='00:00:00:00:00:06')
    s06cpc = net.addHost('s06cpc', ip='100.6.0.21', mac='00:00:00:00:00:0a')
    s06db = net.addHost('s06db', ip='100.6.0.22', mac='00:00:00:00:00:0b')
    s06gw = net.addHost('s06gw', ip='100.6.0.23', mac='00:00:00:00:00:0c')

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
    s07m10 = net.addHost('s07m10', ip='100.7.0.20', cls=CPULimitedHost, cpu=.1)
    s07cpc = net.addHost('s07cpc', ip='100.7.0.21')
    s07db = net.addHost('s07db', ip='100.7.0.22')
    s07gw = net.addHost('s07gw', ip='100.7.0.23')

    """
    #Add Host on Substaion 1
    s01m1 = net.addHost('s01m1', ip='100.1.0.11', cls=CPULimitedHost, cpu=.1)
    s01gw = net.addHost('s01gw', ip='100.1.0.23')
    
    s01cpc = net.addHost('s01cpc', ip='100.1.0.21')
    s01db = net.addHost('s01db', ip='100.1.0.22')
    s01gw = net.addHost('s01gw', ip='100.1.0.23')
    """

    #Add Host on Substaion 2
    s02m1 = net.addHost('s02m1', ip='100.2.0.11', cls=CPULimitedHost, cpu=.1)
    s02m2 = net.addHost('s02m2', ip='100.2.0.12', cls=CPULimitedHost, cpu=.1)
    s02m3 = net.addHost('s02m3', ip='100.2.0.13', cls=CPULimitedHost, cpu=.1)
    s02m4 = net.addHost('s02m4', ip='100.2.0.14', cls=CPULimitedHost, cpu=.1)
    s02m5 = net.addHost('s02m5', ip='100.2.0.15', cls=CPULimitedHost, cpu=.1)
    s02m6 = net.addHost('s02m6', ip='100.2.0.16', cls=CPULimitedHost, cpu=.1)
    s02cpc = net.addHost('s02cpc', ip='100.2.0.21')
    s02db = net.addHost('s02db', ip='100.2.0.22')
    s02gw = net.addHost('s02gw', ip='100.2.0.23')

    """
    #Add Hosts on Substation 3
    s03m1 = net.addHost('s03m1', ip='100.3.0.11', cls=CPULimitedHost, cpu=.1)
    s03m2 = net.addHost('s03m2', ip='100.3.0.12', cls=CPULimitedHost, cpu=.1)
    s03m3 = net.addHost('s03m3', ip='100.3.0.13', cls=CPULimitedHost, cpu=.1)
    s03m4 = net.addHost('s03m4', ip='100.3.0.14', cls=CPULimitedHost, cpu=.1)
    s03m5 = net.addHost('s03m5', ip='100.3.0.15', cls=CPULimitedHost, cpu=.1)
    s03m6 = net.addHost('s03m6', ip='100.3.0.16', cls=CPULimitedHost, cpu=.1)
    s03cpc = net.addHost('s03cpc', ip='100.3.0.21')
    s03db = net.addHost('s03db', ip='100.3.0.22')
    s03gw = net.addHost('s03gw', ip='100.3.0.23')

    #Add Hosts on Substation 4
    s04m1 = net.addHost('s04m1', ip='100.4.0.11', cls=CPULimitedHost, cpu=.1)
    s04m2 = net.addHost('s04m2', ip='100.4.0.12', cls=CPULimitedHost, cpu=.1)
    s04m3 = net.addHost('s04m3', ip='100.4.0.13', cls=CPULimitedHost, cpu=.1)
    s04m4 = net.addHost('s04m4', ip='100.4.0.14', cls=CPULimitedHost, cpu=.1)
    s04m5 = net.addHost('s04m5', ip='100.4.0.15', cls=CPULimitedHost, cpu=.1)
    s04m6 = net.addHost('s04m6', ip='100.4.0.16', cls=CPULimitedHost, cpu=.1)
    s04cpc = net.addHost('s04cpc', ip='100.4.0.21')
    s04db = net.addHost('s04db', ip='100.4.0.22')
    s04gw = net.addHost('s04gw', ip='100.4.0.23')

    #Add Hosts on Substation 5
    s05m1 = net.addHost('s05m1', ip='100.5.0.11', cls=CPULimitedHost, cpu=.1)
    s05m2 = net.addHost('s05m2', ip='100.5.0.12', cls=CPULimitedHost, cpu=.1)
    s05m3 = net.addHost('s05m3', ip='100.5.0.13', cls=CPULimitedHost, cpu=.1)
    s05m4 = net.addHost('s05m4', ip='100.5.0.14', cls=CPULimitedHost, cpu=.1)
    s05m5 = net.addHost('s05m5', ip='100.5.0.15', cls=CPULimitedHost, cpu=.1)
    s05m6 = net.addHost('s05m6', ip='100.5.0.16', cls=CPULimitedHost, cpu=.1)
    s05cpc = net.addHost('s05cpc', ip='100.5.0.21')
    s05db = net.addHost('s05db', ip='100.5.0.22')
    s05gw = net.addHost('s05gw', ip='100.5.0.23')
    """

    # Link siwtch to switch
    net.addLink(s61,s62)
    net.addLink(s63,s62)
    net.addLink(s71,s72)
    net.addLink(s73,s72)
    net.addLink(s21,s22)
    net.addLink(s23,s22)


    net.addLink(s13,s12)
    net.addLink(s11,s12)
    net.addLink(s13,s12)
 

    """
    net.addLink(s33,s32)
    net.addLink(s31,s32)
    net.addLink(s33,s32)
    net.addLink(s43,s42)
    net.addLink(s41,s42)
    net.addLink(s43,s42)
    net.addLink(s53,s52)
    net.addLink(s51,s52)
    net.addLink(s53,s52)
    """

    net.addLink(s61,s999)
    net.addLink(s71,s999)
    net.addLink(s21,s999)
    net.addLink(s11,s999)
    

    """
    
    net.addLink(s31,s999)
    net.addLink(s41,s999)
    net.addLink(s51,s999)
    """

    # Link Substation 06 Merging unit to Switch
    net.addLink(s06m1,s63, intfName1='s06m1-eth1', params1={'ip':'100.6.0.11/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s06m2,s63, intfName1='s06m2-eth1', params1={'ip':'100.6.0.12/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s06m3,s63, intfName1='s06m3-eth1', params1={'ip':'100.6.0.13/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s06m4,s63, intfName1='s06m4-eth1', params1={'ip':'100.6.0.14/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s06m5,s63, intfName1='s06m5-eth1', params1={'ip':'100.6.0.15/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s06m6,s63, intfName1='s06m6-eth1', params1={'ip':'100.6.0.16/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s06cpc,s62)
    net.addLink(s06db,s62)
    net.addLink(s06gw,s61, intfName1='s06gw-eth1', params1={'ip':'100.6.0.23/24'})

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
    net.addLink(s07m10,s73, intfName1='s07m10-eth1', params1={'ip':'100.7.0.20/24'})   
    net.addLink(s07cpc,s72)
    net.addLink(s07db,s72)
    net.addLink(s07gw,s71, intfName1='s07gw-eth1', params1={'ip':'100.7.0.23/24'})

    # Link Substation 02 Merging unit to Switch
    net.addLink(s02m1,s23, intfName1='s02m1-eth1', params1={'ip':'100.2.0.11/24'})
    net.addLink(s02m2,s23, intfName1='s02m2-eth1', params1={'ip':'100.2.0.12/24'})
    net.addLink(s02m3,s23, intfName1='s02m3-eth1', params1={'ip':'100.2.0.13/24'})
    net.addLink(s02m4,s23, intfName1='s02m4-eth1', params1={'ip':'100.2.0.14/24'})
    net.addLink(s02m5,s23, intfName1='s02m5-eth1', params1={'ip':'100.2.0.15/24'})
    net.addLink(s02m6,s23, intfName1='s02m6-eth1', params1={'ip':'100.2.0.16/24'})
    net.addLink(s02cpc,s22)
    net.addLink(s02db,s22)
    net.addLink(s02gw,s21, intfName1='s02gw-eth1', params1={'ip':'100.2.0.23/24'})

    """
    # Link Substation 01 Merging unit to Switch
    net.addLink(s01m1,s13, intfName1='s01m1-eth1', params1={'ip':'100.1.0.11/24'})
    net.addLink(s01gw,s11, intfName1='s01gw-eth1', params1={'ip':'100.1.0.23/24'})
    
    net.addLink(s01cpc,s12)
    net.addLink(s01db,s12)
    """

    """
    # Link Substation 03 Merging unit to Switch
    net.addLink(s03m1,s33, intfName1='s03m1-eth1', params1={'ip':'100.3.0.11/24'})
    net.addLink(s03m2,s33, intfName1='s03m2-eth1', params1={'ip':'100.3.0.12/24'})
    net.addLink(s03m3,s33, intfName1='s03m3-eth1', params1={'ip':'100.3.0.13/24'})
    net.addLink(s03m4,s33, intfName1='s03m4-eth1', params1={'ip':'100.3.0.14/24'})
    net.addLink(s03m5,s33, intfName1='s03m5-eth1', params1={'ip':'100.3.0.15/24'})
    net.addLink(s03m6,s33, intfName1='s03m6-eth1', params1={'ip':'100.3.0.16/24'})
    net.addLink(s03cpc,s32)
    net.addLink(s03db,s32)
    net.addLink(s03gw,s31, intfName1='s03gw-eth1', params1={'ip':'100.3.0.23/24'})

    # Link Substation 04 Merging unit to Switch
    net.addLink(s04m1,s43, intfName1='s04m1-eth1', params1={'ip':'100.4.0.11/24'})
    net.addLink(s04m2,s43, intfName1='s04m2-eth1', params1={'ip':'100.4.0.12/24'})
    net.addLink(s04m3,s43, intfName1='s04m3-eth1', params1={'ip':'100.4.0.13/24'})
    net.addLink(s04m4,s43, intfName1='s04m4-eth1', params1={'ip':'100.4.0.14/24'})
    net.addLink(s04m5,s43, intfName1='s04m5-eth1', params1={'ip':'100.4.0.15/24'})
    net.addLink(s04m6,s43, intfName1='s04m6-eth1', params1={'ip':'100.4.0.16/24'})
    net.addLink(s04cpc,s42)
    net.addLink(s04db,s42)
    net.addLink(s04gw,s41, intfName1='s04gw-eth1', params1={'ip':'100.4.0.23/24'})

    # Link Substation 05 Merging unit to Switch
    net.addLink(s05m1,s53, intfName1='s05m1-eth1', params1={'ip':'100.5.0.11/24'})
    net.addLink(s05m2,s53, intfName1='s05m2-eth1', params1={'ip':'100.5.0.12/24'})
    net.addLink(s05m3,s53, intfName1='s05m3-eth1', params1={'ip':'100.5.0.13/24'})
    net.addLink(s05m4,s53, intfName1='s05m4-eth1', params1={'ip':'100.5.0.14/24'})
    net.addLink(s05m5,s53, intfName1='s05m5-eth1', params1={'ip':'100.5.0.15/24'})
    net.addLink(s05m6,s53, intfName1='s05m6-eth1', params1={'ip':'100.5.0.16/24'})
    net.addLink(s05cpc,s52)
    net.addLink(s05db,s52)
    net.addLink(s05gw,s51, intfName1='s05gw-eth1', params1={'ip':'100.5.0.23/24'})

    """

    # Link Host Substation 6 to switch to external gateway
    net.addLink(s06m1,s777, intfName1='s06m1-eth0', params1={'ip':'10.0.6.11/16'})
    net.addLink(s06m2,s777, intfName1='s06m2-eth0', params1={'ip':'10.0.6.12/16'})
    net.addLink(s06m3,s777, intfName1='s06m3-eth0', params1={'ip':'10.0.6.13/16'})
    net.addLink(s06m4,s777, intfName1='s06m4-eth0', params1={'ip':'10.0.6.14/16'})
    net.addLink(s06m5,s777, intfName1='s06m5-eth0', params1={'ip':'10.0.6.15/16'})
    net.addLink(s06m6,s777, intfName1='s06m6-eth0', params1={'ip':'10.0.6.16/16'})
    net.addLink(s06gw,s777, intfName1='s06gw-eth0', params1={'ip':'10.0.6.23/16'})

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
    net.addLink(s07m10,s777, intfName1='s07m10-eth0', params1= {'ip':'10.0.7.20/16'})
    net.addLink(s07gw,s777, intfName1='s07gw-eth0', params1={'ip':'10.0.7.23/16'})

    # Link Host Substation 2 to switch to external gateway
    net.addLink(s02m1,s777, intfName1='s02m1-eth0', params1={'ip':'10.0.2.11/16'})
    net.addLink(s02m2,s777, intfName1='s02m2-eth0', params1={'ip':'10.0.2.12/16'})
    net.addLink(s02m3,s777, intfName1='s02m3-eth0', params1={'ip':'10.0.2.13/16'})
    net.addLink(s02m4,s777, intfName1='s02m4-eth0', params1={'ip':'10.0.2.14/16'})
    net.addLink(s02m5,s777, intfName1='s02m5-eth0', params1={'ip':'10.0.2.15/16'})
    net.addLink(s02m6,s777, intfName1='s02m6-eth0', params1={'ip':'10.0.2.16/16'})
    net.addLink(s02gw,s777, intfName1='s02gw-eth0', params1={'ip':'10.0.2.23/16'})

    """
    # Link Host Substation 1 to switch to external gateway
    net.addLink(s01m1,s777, intfName1='s01m1-eth0', params1={'ip':'10.0.1.11/16'})
    net.addLink(s01gw,s777, intfName1='s01gw-eth0', params1={'ip':'10.0.1.23/16'})
    

    
    # Link Host Substation 3 to switch to external gateway
    net.addLink(s03m1,s777, intfName1='s03m1-eth0', params1={'ip':'10.0.3.11/16'})
    net.addLink(s03m2,s777, intfName1='s03m2-eth0', params1={'ip':'10.0.3.12/16'})
    net.addLink(s03m3,s777, intfName1='s03m3-eth0', params1={'ip':'10.0.3.13/16'})
    net.addLink(s03m4,s777, intfName1='s03m4-eth0', params1={'ip':'10.0.3.14/16'})
    net.addLink(s03m5,s777, intfName1='s03m5-eth0', params1={'ip':'10.0.3.15/16'})
    net.addLink(s03m6,s777, intfName1='s03m6-eth0', params1={'ip':'10.0.3.16/16'})
    net.addLink(s03gw,s777, intfName1='s03gw-eth0', params1={'ip':'10.0.3.23/16'})

    # Link Host Substation 4 to switch to external gateway
    net.addLink(s04m1,s777, intfName1='s04m1-eth0', params1={'ip':'10.0.4.11/16'})
    net.addLink(s04m2,s777, intfName1='s04m2-eth0', params1={'ip':'10.0.4.12/16'})
    net.addLink(s04m3,s777, intfName1='s04m3-eth0', params1={'ip':'10.0.4.13/16'})
    net.addLink(s04m4,s777, intfName1='s04m4-eth0', params1={'ip':'10.0.4.14/16'})
    net.addLink(s04m5,s777, intfName1='s04m5-eth0', params1={'ip':'10.0.4.15/16'})
    net.addLink(s04m6,s777, intfName1='s04m6-eth0', params1={'ip':'10.0.4.16/16'})
    net.addLink(s04gw,s777, intfName1='s04gw-eth0', params1={'ip':'10.0.4.23/16'})

    # Link Host Substation 5 to switch to external gateway
    net.addLink(s05m1,s777, intfName1='s05m1-eth0', params1={'ip':'10.0.5.11/16'})
    net.addLink(s05m2,s777, intfName1='s05m2-eth0', params1={'ip':'10.0.5.12/16'})
    net.addLink(s05m3,s777, intfName1='s05m3-eth0', params1={'ip':'10.0.5.13/16'})
    net.addLink(s05m4,s777, intfName1='s05m4-eth0', params1={'ip':'10.0.5.14/16'})
    net.addLink(s05m5,s777, intfName1='s05m5-eth0', params1={'ip':'10.0.5.15/16'})
    net.addLink(s05m6,s777, intfName1='s05m6-eth0', params1={'ip':'10.0.5.16/16'})
    net.addLink(s05gw,s777, intfName1='s05gw-eth0', params1={'ip':'10.0.5.23/16'})
    """


    #Build and start Network ============================================================================
    net.build()
    net.addNAT(ip='10.0.0.250').configDefault()
    net.start()

    #Configure GRE Tunnel
    s777.cmdPrint('ovs-vsctl add-port s777 s777-gre1 -- set interface s777-gre1 type=gre ofport_request=5 options:remote_ip='+NODE2_IP)
    s777.cmdPrint('ovs-vsctl show')
    nat = net.get('nat0')
    nat.cmdPrint('ip link set mtu 1454 dev nat0-eth0')

    info(os.system('ip addr add 10.0.99.1/16 dev s777'))
    info(os.system('ip link set s777 up'))

    """
    info( net[ 's06m1' ].cmd( 'python3 as06m1.py &amp' ) )
    info( net[ 's06m2' ].cmd( 'python3 as06m2.py &amp' ) )
    info( net[ 's06m3' ].cmd( 'python3 as06m3.py &amp' ) )
    info( net[ 's06m4' ].cmd( 'python3 as06m4.py &amp' ) )
    info( net[ 's06m5' ].cmd( 'python3 as06m5.py &amp' ) )
    info( net[ 's06m6' ].cmd( 'python3 as06m6.py &amp' ) )

    info( net[ 's07m1' ].cmd( 'python3 as07m1.py &amp' ) )
    info( net[ 's07m2' ].cmd( 'python3 as07m2.py &amp' ) )
    info( net[ 's07m3' ].cmd( 'python3 as07m3.py &amp' ) )
    info( net[ 's07m4' ].cmd( 'python3 as07m4.py &amp' ) )
    info( net[ 's07m5' ].cmd( 'python3 as07m5.py &amp' ) )
    info( net[ 's07m6' ].cmd( 'python3 as07m6.py &amp' ) )
    info( net[ 's07m7' ].cmd( 'python3 as07m7.py &amp' ) )
    info( net[ 's07m8' ].cmd( 'python3 as07m8.py &amp' ) )
    info( net[ 's07m9' ].cmd( 'python3 as07m9.py &amp' ) )
    info( net[ 's07m10' ].cmd( 'python3 as07m10.py &amp' ) )
    """
 
    
 
    

    #time.sleep(5)

    #info( net[ 's06db' ].cmd( 'python3 ascdb.py &amp' ) )


    CLI( net )
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()

    
