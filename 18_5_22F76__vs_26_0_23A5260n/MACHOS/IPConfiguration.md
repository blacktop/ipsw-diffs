## IPConfiguration

> `/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration`

```diff

-494.120.6.0.0
-  __TEXT.__text: 0x59ee4
-  __TEXT.__auth_stubs: 0xf90
-  __TEXT.__const: 0x300
-  __TEXT.__oslogstring: 0x63bc
-  __TEXT.__cstring: 0x3c92
-  __TEXT.__unwind_info: 0xbd8
-  __DATA_CONST.__auth_got: 0x7c8
-  __DATA_CONST.__got: 0x370
+521.0.0.0.0
+  __TEXT.__text: 0x5a248
+  __TEXT.__auth_stubs: 0x1030
+  __TEXT.__const: 0x2f0
+  __TEXT.__oslogstring: 0x5ea9
+  __TEXT.__cstring: 0x4072
+  __TEXT.__unwind_info: 0xbf0
+  __DATA_CONST.__auth_got: 0x818
+  __DATA_CONST.__got: 0x3a8
   __DATA_CONST.__auth_ptr: 0xf8
-  __DATA_CONST.__const: 0x1d30
-  __DATA_CONST.__cfstring: 0x27c0
+  __DATA_CONST.__const: 0x1d60
+  __DATA_CONST.__cfstring: 0x29e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0x110
-  __DATA.__bss: 0x1e0
+  __DATA.__data: 0x118
+  __DATA.__bss: 0x1f0
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: B8A85D39-345B-34B6-8C9D-FBB34E3C5940
-  Functions: 989
-  Symbols:   466
-  CStrings:  1989
+  UUID: 74619A4C-BA49-3C71-8980-34C740966AD5
+  Functions: 1006
+  Symbols:   482
+  CStrings:  2036
 
Symbols:
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _CFArrayAppendArray
+ _CFDataFind
+ _CFNumberCompare
+ _CFSetAddValue
+ _CFSetContainsValue
+ _CFSetCreateMutable
+ _CFStringCreateExternalRepresentation
+ _kCFTypeSetCallBacks
+ _kIPConfigurationServiceOptionEnableL4S
+ _kSCPropNetDNSEncryptedServerAddresses
+ _kSCPropNetDNSEncryptedServerAuthenticationDomainName
+ _kSCPropNetDNSEncryptedServerServiceParameters
+ _kSCPropNetDNSEncryptedServerServicePriority
+ _kSCPropNetDNSEncryptedServers
- _PvDEntityCreateWithInfo
CStrings:
+ "\n}"
+ "%hu"
+ "%s(%s)"
+ "%s: %s success"
+ "%s: %s, forcing link timer expired"
+ "%s: bad DNS servers array"
+ "%s: changing L4S mode from '%s' to '%s'"
+ "%s: reported address acquisition success (cancel) symptom"
+ "(null)"
+ ", addrs: "
+ ", authentication domain name: "
+ ", priority "
+ ", service parameters: "
+ "<truncated>"
+ "DNSEntityCreateWithDHCPInfo"
+ "DNS_ENCRYPTED_SERVERS"
+ "Default"
+ "Disable"
+ "Enable"
+ "EncryptedServerAddresses"
+ "EncryptedServerName"
+ "EncryptedServerParameters"
+ "EncryptedServerPriority"
+ "IPConfiguration: %s Router is invalid"
+ "IPv6.Prefix=%@/%@;IPv6.RouterHardwareAddress="
+ "NetworkSignatureHash"
+ "SIOCAIFADDR"
+ "SIOCAIFADDR_IN6"
+ "SIOCARPIPLL"
+ "SIOCAUTOADDR"
+ "SIOCAUTOCONF_START"
+ "SIOCAUTOCONF_STOP"
+ "SIOCCLAT46_START"
+ "SIOCCLAT46_STOP"
+ "SIOCDIFADDR"
+ "SIOCDIFADDR_IN6"
+ "SIOCGIFAFLAG_IN6"
+ "SIOCGIFALIFETIME_IN6"
+ "SIOCGIFEFLAGS"
+ "SIOCGIFFLAGS"
+ "SIOCGIFINFO_FLAGS"
+ "SIOCGIFINFO_IN6"
+ "SIOCGIFL4S"
+ "SIOCGIFNAT64PREFIX"
+ "SIOCGIFPROTOLIST"
+ "SIOCGIFSTAT_IN6"
+ "SIOCLL_CGASTART"
+ "SIOCLL_START"
+ "SIOCLL_STOP"
+ "SIOCPROTOATTACH"
+ "SIOCPROTOATTACH_IN6"
+ "SIOCPROTODETACH"
+ "SIOCPROTODETACH_IN6"
+ "SIOCSIFCGAPREP_IN6"
+ "SIOCSIFFLAGS"
+ "SIOCSIFL4S"
+ "SIOCSIFMTU"
+ "SIOCSIFNAT64PREFIX"
+ "SIOCSPFXFLUSH_IN6"
+ "SIOCSRTRFLUSH_IN6"
+ "com.apple.IPConfiguration.get-information"
+ "dnr"
+ "dns_dnr_data"
+ "encrypted_dns_server"
+ "inet socket closed %d"
+ "inet socket opened %d"
+ "inet6 socket closed %d"
+ "inet6 socket opened %d"
+ "inet6_flush_prefixes"
+ "inet6_flush_routes"
+ "interface reattached"
+ "ioctl(%s, %s) failed status, %s"
+ "link address changed"
+ "perform_async_work_requiring_store"
+ "socket(AF_INET, SOCK_DGRAM, 0) failed, %s"
+ "socket(AF_INET6, SOCK_DGRAM, 0) failed, %s"
+ "sockets need to be closed"
+ "v16@?0^{ServiceInfo=^{__CFString}^{__CFString}^{IFState}iiiii^{__CFString}^{__CFString}^{dispatch_source_s}ii^v(?={?={?={in_addr=I}{in_addr=I}{in_addr=I}}{?={in_addr=I}{in_addr=I}{in_addr=I}{in_addr=I}}{?=I{in_addr=I}[16C]}ddi}{?={?={in6_addr=(?=[16C][8S][4I])}i}{in6_addr=(?=[16C][8S][4I])}iii})}8"
+ "{\n"
+ "{ %@ (%@)\n%@\n'%@'\n}"
- "%s(%s): socket() failed, %s (%d)"
- "%s: SIOCSIFNAT64PREFIX(%d) failed, %s (%d)"
- "%s: SIOCSIFNAT64PREFIX(%d) success"
- "%s: interface reattached, forcing link timer expired"
- "DHCPv6ClientRemoveAddress(%s):socket() failed, %s (%d)"
- "IPv6.Prefix=%s/%d;IPv6.RouterHardwareAddress="
- "RTADV %s: failed to open socket, %s"
- "SIOCGIFINFO_IN6(%s) failed, %s"
- "SIOCGIFPROTOLIST failed#2: %s (%d)"
- "SIOCGIFPROTOLIST failed: %s (%d)"
- "SIOCGIFSTAT_IN6(%s) failed, %s"
- "SIOCSIFINFO_FLAGS(%s) failed, %s"
- "S_remove_ip_address(%s) socket() failed, %s (%d)"
- "ServiceRemoveIPv6Address(%s): socket() failed, %s (%d)"
- "ServiceSetIPv6Address(%s): socket() failed, %s (%d)"
- "inet6_attach_interface(%s): socket() failed, %s (%d)"
- "inet6_detach_interface(%s): socket() failed, %s (%d)"
- "inet6_flush_prefixes(%s)"
- "inet6_flush_routes(%s)"
- "inet6_has_nat64_prefixlist"
- "inet6_linklocal_start(%s): socket() failed, %s (%d)"
- "inet6_linklocal_stop(%s): socket() failed, %s (%d)"
- "inet6_rtadv_disable(%s): socket() failed, %s (%d)"
- "inet6_rtadv_enable(%s): socket() failed, %s (%d)"
- "inet6_set_nat64_prefixlist"
- "inet_set_autoaddr(%s, %d) failed, %s (%d)"
- "inet_set_autoaddr(%s, %d): socket() failed, %s (%d)"
- "ioctl(%s, SIOCCLAT46_START)"
- "ioctl(%s, SIOCCLAT46_START), failed, %s (%d)"
- "ioctl(%s, SIOCCLAT46_STOP)"
- "ioctl(%s, SIOCCLAT46_STOP), failed, %s (%d)"
- "ioctl(%s, SIOCLL_STOP)"
- "option_162"
- "perform_async_work"
- "protolist_copy: socket failed, %s (%d)"
- "service_set_address(%s): socket() failed, %s (%d)"
- "set_arp_linklocal(%s) SIOCARPIPLL %d failed, %s"
- "set_arp_linklocal(%s) socket() failed, %s"
- "set_loopback(): socket() failed, %s (%d)"
- "siocautoconf_start(%s) failed, %s (%d)"
- "siocautoconf_stop(%s) failed, %s (%d)"
- "siocll_stop(%s) failed, %s (%d)"
- "siocprotoattach(%s) failed, %s (%d)"
- "siocprotoattach_in6(%s) failed, %s (%d)"
- "siocprotodetach(%s) failed, %s (%d)"
- "siocsifcgaprep_in6(%s) failed, %s (%d)"
- "siocsifmtu(%s, %d) failed, %s (%d)"
- "socket failed, %s (%d)"
- "socket(%s) failed, %s"
- "v16@?0^{ServiceInfo=^{__CFString}^{__CFString}^{IFState}iiiii^{__CFString}^{__CFString}^{dispatch_source_s}i^v(?={?={?={in_addr=I}{in_addr=I}{in_addr=I}}{?={in_addr=I}{in_addr=I}{in_addr=I}{in_addr=I}}{?=I{in_addr=I}[16C]}ddi}{?={?={in6_addr=(?=[16C][8S][4I])}i}ii})}8"

```
