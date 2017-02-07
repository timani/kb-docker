---
title: How to snoop traffic going through an application in Diego cell
template: break-fix
id: 221514427
locale: en-us
<span class="wysiwyg-font-size-large">**Environment** </span>

<table style="height: 111px;" border="y" width="367">

<tbody>

<tr style="background-color: grey;">

<td><span class="wysiwyg-color-black10">Product</span></td>

<td><span class="wysiwyg-color-black10">Version</span></td>

</tr>

<tr>

<td>Pivotal Cloud Foundry® (PCF)</td>

<td>1.6.x, 1.7.x</td>

</tr>

<tr>

<td>Component</td>

<td>Diego Cell on Linux</td>

</tr>

</tbody>

</table>

<span class="wysiwyg-font-size-large">**Purpose**</span>

This article explains how you can snoop packets going through applications running on your Pivotal Cloud Foundry deployment. It explains how you find out the Linux network interface that is connected to an application of your interest so that you can execute the tcpdump command to snoop packets. Besides tcpdump, you can also execute whatever you can do with standard Linux commands that operate on the network interface, such as ip, netstat, etc. This should be useful when you want to debug or troubleshoot applications at the network traffic level. 

Note that this requires administrative access to your PCF deployment. 

**<span class="wysiwyg-font-size-large">Procedure</span>**

1.  Follow the procedure in the article **<span class="wysiwyg-font-size-medium wysiwyg-color-black">[How to login an app's container as root?](/hc/en-us/articles/220866207)</span> **up to step 2 to identify the process running on the Diego Cell for the application you are interested in.
2.  Copy the string after `/var/vcap/data/garden/depot/`. This string identifies the container and is referred to as its handle. In the example in the article, ib2acg2jbnr is the handle. 
3.  Find out the network interface attached to the container by ip link |grep <handle>.
4.  Now, you can use tcpdump -i <interface> to snoop the traffic. 
5.  Besides tcpdump, you can do whatever you can do with standard Linux commands that operate on the network interface, such as ip, netstat, etc. 

## <span class="wysiwyg-font-size-large">**Impact/Risks **</span>

*   You might inadvertently view sensitive information going through the application's traffic that you are snooping on.
*   This information is based on implementation details of the Diego Cell, which may change at any time without formal notice.  

## <span class="wysiwyg-font-size-large">Additional Information</span>

*   <span class="wysiwyg-color-black">[How to login an app's container as root?](/hc/en-us/articles/220866207)</span>
