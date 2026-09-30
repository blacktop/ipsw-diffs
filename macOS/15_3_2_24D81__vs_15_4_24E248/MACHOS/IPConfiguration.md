## IPConfiguration

> `/System/Library/SystemConfiguration/IPConfiguration.bundle/Contents/MacOS/IPConfiguration`

```diff

-494.80.2.0.0
-  __TEXT.__text: 0x59d64
-  __TEXT.__auth_stubs: 0x1050
-  __TEXT.__const: 0x300
-  __TEXT.__cstring: 0x3c8b
-  __TEXT.__oslogstring: 0x638b
-  __TEXT.__unwind_info: 0xbb0
-  __DATA_CONST.__auth_got: 0x828
+494.101.1.0.0
+  __TEXT.__text: 0x5acf0
+  __TEXT.__auth_stubs: 0x1060
+  __TEXT.__const: 0x2f0
+  __TEXT.__cstring: 0x3d3d
+  __TEXT.__oslogstring: 0x64d6
+  __TEXT.__unwind_info: 0xb60
+  __DATA_CONST.__auth_got: 0x830
   __DATA_CONST.__got: 0x3c8
-  __DATA_CONST.__auth_ptr: 0xf0
-  __DATA_CONST.__const: 0x1d40
-  __DATA_CONST.__cfstring: 0x2880
+  __DATA_CONST.__auth_ptr: 0xf8
+  __DATA_CONST.__const: 0x1d90
+  __DATA_CONST.__cfstring: 0x2920
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x110
-  __DATA.__bss: 0x1f8
+  __DATA.__bss: 0x200
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 480FB930-8F32-369F-BB27-138EFA0E9F68
-  Functions: 1012
-  Symbols:   496
-  CStrings:  1992
+  UUID: E73E7BF3-2F43-30D0-9936-847F6E301845
+  Functions: 999
+  Symbols:   498
+  CStrings:  2017
 
Symbols:
+ _SCNetworkInterfaceGetInterfaceType
+ _kSCNetworkInterfaceTypeIEEE80211
+ _memcmp
- _IORegistryEntryCreateCFProperty
CStrings:
+ " CLIENT_FQDN flags 0x%x"
+ " CLIENT_FQDN option is too short %d < %d\n"
+ " N"
+ " O"
+ " S"
+ " ["
+ " domain-name %@"
+ " domain-name bad, raw bytes <"
+ "%s(%s): address still assigned %d.%d.%d.%d"
+ "%s: %s() invalid mode '%s'"
+ "%s: %s() saved information is not valid"
+ ">"
+ "CLIENT_FQDN"
+ "DHCP %s: hostname is NULL"
+ "DHCPv6 %s: added FQDN option for '%s'"
+ "DHCPv6 %s: failed to convert '%s'"
+ "DHCPv6 %s: no hostname available"
+ "DHCPv6 %s: privacy disallows sharing hostname"
+ "DHCPv6Client: failed to add CLIENT_FQDN, %s"
+ "DHCPv6ClientRelease"
+ "IPv6.Prefix=%@/%@;IPv6.RouterHardwareAddress="
+ "LENGTH %d\n"
+ "attempt to set offset 0x%x at index %d\n"
+ "failed to add %s\n"
+ "name %@\n"
+ "service_set_address"
+ "trying to set used to %d\n"
- "IO80211InterfaceRole"
- "IOInterfaceName"
- "IOPropertyMatch"
- "IPv6.Prefix=%s/%d;IPv6.RouterHardwareAddress="
- "Infrastructure"
- "name missing end label\n"
- "no domains "

```
