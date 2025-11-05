## dhcp6d

> `/usr/libexec/dhcp6d`

```diff

-494.80.2.0.0
-  __TEXT.__text: 0x7508
+494.101.1.0.0
+  __TEXT.__text: 0x763c
   __TEXT.__auth_stubs: 0x690
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x92c
+  __TEXT.__cstring: 0x95e
   __TEXT.__oslogstring: 0x55b
   __TEXT.__unwind_info: 0x1b0
   __DATA_CONST.__auth_got: 0x348
-  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1c0
-  __DATA_CONST.__cfstring: 0x560
+  __DATA_CONST.__const: 0x1d0
+  __DATA_CONST.__cfstring: 0x640
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
-  UUID: B77CBA18-95FD-379F-81F3-B618F9B6DE5F
-  Functions: 99
-  Symbols:   127
-  CStrings:  226
+  UUID: 704E3A83-F662-306E-BDDE-49D5604715B1
+  Functions: 100
+  Symbols:   128
+  CStrings:  240
 
Symbols:
+ _SCNetworkInterfaceGetInterfaceType
+ _SCPrint
+ ___stdoutp
+ _kSCNetworkInterfaceTypeIEEE80211
+ _printf
- _IOObjectRelease
- _IORegistryEntryCreateCFProperty
- _IOServiceGetMatchingService
- _kIOMainPortDefault
CStrings:
+ " CLIENT_FQDN flags 0x%x"
+ " CLIENT_FQDN option is too short %d < %d\n"
+ " N"
+ " O"
+ " S"
+ " ["
+ " ]"
+ " domain-name %@"
+ " domain-name bad, raw bytes <"
+ ">"
+ "CLIENT_FQDN"
+ "LENGTH %d\n"
+ "name %@\n"
- "IO80211InterfaceRole"
- "IOInterfaceName"
- "IOPropertyMatch"
- "Infrastructure"
- "label length is 0\n"
- "name missing end label\n"

```
