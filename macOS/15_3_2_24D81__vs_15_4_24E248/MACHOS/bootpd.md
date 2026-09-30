## bootpd

> `/usr/libexec/bootpd`

```diff

-494.80.2.0.0
-  __TEXT.__text: 0x1cbfc
-  __TEXT.__auth_stubs: 0xd40
+494.101.1.0.0
+  __TEXT.__text: 0x1c9bc
+  __TEXT.__auth_stubs: 0xd30
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x2cc9
+  __TEXT.__cstring: 0x2c68
   __TEXT.__oslogstring: 0x20a4
-  __TEXT.__unwind_info: 0x450
-  __DATA_CONST.__auth_got: 0x6a0
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__auth_ptr: 0x40
+  __TEXT.__unwind_info: 0x440
+  __DATA_CONST.__auth_got: 0x698
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__auth_ptr: 0x50
   __DATA_CONST.__const: 0x14c0
-  __DATA_CONST.__cfstring: 0x1200
+  __DATA_CONST.__cfstring: 0x1180
   __DATA.__data: 0xb8
-  __DATA.__common: 0x138
+  __DATA.__common: 0x311
   __DATA.__bss: 0x13c0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libresolv.9.dylib
-  UUID: 3A8A7D5F-E5A7-3DD8-AD9B-100D0CC2B5D7
-  Functions: 294
-  Symbols:   278
-  CStrings:  1087
+  UUID: D9F6A7CD-2C14-335C-92AE-0BE114404095
+  Functions: 290
+  Symbols:   275
+  CStrings:  1079
 
Symbols:
+ _SCNetworkInterfaceGetInterfaceType
+ ___res_9_state
+ _kSCNetworkInterfaceTypeIEEE80211
- _IOObjectRelease
- _IORegistryEntryCreateCFProperty
- _IOServiceGetMatchingService
- __res
- _kCFAllocatorDefault
- _kIOMainPortDefault
CStrings:
+ "http://"
+ "local"
- "IO80211InterfaceRole"
- "IOInterfaceName"
- "IOPropertyMatch"
- "Infrastructure"
- "label length is 0\n"
- "name missing end label\n"

```
