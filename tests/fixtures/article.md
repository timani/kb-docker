---
title: How to snoop traffic going through an application in Diego cell
template: break-fix
id: 221514427
locale: en-us
# How to snoop traffic going through an application in Diego cell – All Help & Support

**Environment** 

| ----- |
| Product |  Version |  
| Pivotal Cloud Foundry® (PCF) |  1.6.x, 1.7.x |  
| Component |  Diego Cell on Linux | 

**Purpose**

This article explains how you can snoop packets going through applications running on your Pivotal Cloud Foundry deployment. It explains how you find out the Linux network interface that is connected to an application of your interest so that you can execute the tcpdump command to snoop packets. Besides tcpdump, you can also execute whatever you can do with standard Linux commands that operate on the network interface, such as ip, netstat, etc. This should be useful when you want to debug or troubleshoot applications at the network traffic level. 

Note that this requires administrative access to your PCF deployment. 

**Procedure**

1. Follow the procedure in the article [**How to login an app's container as root?][1] **up to step 2 to identify the process running on the Diego Cell for the application you are interested in.
2. Copy the string after `/var/vcap/data/garden/depot/`. This string identifies the container and is referred to as its handle. In the example in the article, ib2acg2jbnr is the handle. 
3. Find out the network interface attached to the container by ip link |grep .
4. Now, you can use tcpdump -i  to snoop the traffic. 
5. Besides tcpdump, you can do whatever you can do with standard Linux commands that operate on the network interface, such as ip, netstat, etc. 

## **Impact/Risks **

* You might inadvertently view sensitive information going through the application's traffic that you are snooping on.
* This information is based on implementation details of the Diego Cell, which may change at any time without formal notice.  

## Additional Information
