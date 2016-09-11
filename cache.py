#!/usr/bin/env python

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import RemoteController, UserSwitch
from mininet.term import makeTerm

if '__main__' == __name__:
    net = Mininet(controller=RemoteController, link=TCLink)

    c0 = net.addController('c0')

    s1 = net.addSwitch('s1', protocols='OpenFlow13', switch=UserSwitch, mac='00:00:00:11:00:00')

    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')

    net.addLink(s1, h1)
    net.addLink(s1, h2)
    net.addLink(s1, h3)
    net.addLink(s1, h4)

    net.build()
    c0.start()
    s1.start([c0])

    net.startTerms()

    CLI(net)

    net.stop()

