## lockdownd

> `/usr/libexec/lockdownd`

```diff

 1319.0.7.0.0
-  __TEXT.__text: 0x1025dc
-  __TEXT.__auth_stubs: 0x2cd0
+  __TEXT.__text: 0x102b9c
+  __TEXT.__auth_stubs: 0x2ce0
   __TEXT.__objc_stubs: 0x43e0
   __TEXT.__objc_methlist: 0x3438
-  __TEXT.__cstring: 0x4cf70
+  __TEXT.__cstring: 0x4d14a
   __TEXT.__const: 0x160f0
   __TEXT.__oslogstring: 0x788
   __TEXT.__gcc_except_tab: 0x399c

   __TEXT.__objc_methname: 0x476f
   __TEXT.__objc_methtype: 0xe80
   __TEXT.__services: 0x2d8f
-  __TEXT.__unwind_info: 0x2d28
+  __TEXT.__unwind_info: 0x2d30
   __TEXT.__eh_frame: 0x10b8
-  __DATA_CONST.__auth_got: 0x1680
+  __DATA_CONST.__auth_got: 0x1688
   __DATA_CONST.__got: 0x698
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0xa948
-  __DATA_CONST.__cfstring: 0x17c20
+  __DATA_CONST.__const: 0xa988
+  __DATA_CONST.__cfstring: 0x17c60
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30

   __DATA.__objc_ivar: 0x410
   __DATA.__objc_data: 0x1900
   __DATA.__data: 0x2b68
-  __DATA.__bss: 0x1042
+  __DATA.__bss: 0x1052
   __DATA.__common: 0x1a48
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2937
-  Symbols:   925
-  CStrings:  9443
+  Functions: 2942
+  Symbols:   926
+  CStrings:  9456
 
Symbols:
+ _mach_error_string
CStrings:
+ "IOServiceGetMatchingService failed\n"
+ "unable to read the SEP slot id will not set.\n"
+ "IOServiceOpen failed for class '%!s(MISSING)'\n"
+ "ApNonceSlotID"
+ "Failed to connect to AppleSEPManager to generate sep nonce.\n"
+ "IODeviceTree:/arm-io/sep/iop-sep-nub/Sandcat"
+ "IOConnectCallMethod(%!s(MISSING),%!u(MISSING)) failed: %!s(MISSING)\n"
+ "unable to read the AP slot id will not set.\n"
+ "Failed to connect to AppleMobileApNonce to generate AP nonce slot.\n"
+ "VinylRestore-78~1097"
+ "IOServiceMatching failed for %!s(MISSING)\n"
+ "AppleSEPManager"
+ "AppleMobileApNonce"
+ "SepNonceSlotID"
- "VinylRestore-78~1088"

```
