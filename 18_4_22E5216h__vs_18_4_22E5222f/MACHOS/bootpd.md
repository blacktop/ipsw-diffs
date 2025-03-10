## bootpd

> `/usr/libexec/bootpd`

```diff

-494.100.6.502.1
-  __TEXT.__text: 0x10160
-  __TEXT.__auth_stubs: 0x8f0
+494.100.7.502.1
+  __TEXT.__text: 0x10054
+  __TEXT.__auth_stubs: 0x8d0
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x1e88
+  __TEXT.__cstring: 0x1e44
   __TEXT.__oslogstring: 0x114f
   __TEXT.__unwind_info: 0x2d8
-  __DATA_CONST.__auth_got: 0x478
-  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__auth_got: 0x468
+  __DATA_CONST.__got: 0x98
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x1300
-  __DATA_CONST.__cfstring: 0xbe0
+  __DATA_CONST.__cfstring: 0xb60
   __DATA.__data: 0xa8
   __DATA.__common: 0x311
   __DATA.__bss: 0x1350

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libresolv.9.dylib
   Functions: 195
-  Symbols:   185
-  CStrings:  644
+  Symbols:   182
+  CStrings:  640
 
Symbols:
+ _SCNetworkInterfaceGetInterfaceType
+ _kSCNetworkInterfaceTypeIEEE80211
- _IOObjectRelease
- _IORegistryEntryCreateCFProperty
- _IOServiceGetMatchingService
- _kCFAllocatorDefault
- _kIOMainPortDefault
CStrings:
- "IO80211InterfaceRole"
- "IOInterfaceName"
- "IOPropertyMatch"
- "Infrastructure"

```
