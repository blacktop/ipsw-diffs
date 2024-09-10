## restoreserviced

> `/usr/libexec/restoreserviced`

```diff

 29.0.1.0.0
-  __TEXT.__text: 0x13264
-  __TEXT.__auth_stubs: 0xed0
+  __TEXT.__text: 0x13828
+  __TEXT.__auth_stubs: 0xee0
   __TEXT.__objc_stubs: 0x1760
   __TEXT.__objc_methlist: 0xc64
   __TEXT.__const: 0xb88
-  __TEXT.__cstring: 0x73b1
+  __TEXT.__cstring: 0x756e
   __TEXT.__oslogstring: 0x34d
   __TEXT.__gcc_except_tab: 0x1c4
   __TEXT.__objc_methname: 0x1707
   __TEXT.__objc_classname: 0x11e
   __TEXT.__objc_methtype: 0x76c
-  __TEXT.__unwind_info: 0x508
-  __DATA_CONST.__auth_got: 0x778
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0xc38
+  __TEXT.__unwind_info: 0x510
+  __DATA_CONST.__auth_got: 0x780
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0xc58
   __DATA_CONST.__cfstring: 0x34e0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x5b8
-  __DATA.__bss: 0xb8
+  __DATA.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 437
-  Symbols:   293
-  CStrings:  1347
+  Functions: 442
+  Symbols:   298
+  CStrings:  1358
 
Symbols:
+ _mach_error_string
+ _kAMAuthInstallApParameterApNonce
+ _kAMAuthInstallApParameterSepNonce
+ _kAMAuthInstallApParameterApNonceSlotID
+ _kAMAuthInstallApParameterSepNonceSlotID
CStrings:
+ "Failed to connect to AppleSEPManager to generate sep nonce.\n"
+ "IOServiceGetMatchingService failed\n"
+ "unable to read the SEP slot id will not set.\n"
+ "IOConnectCallMethod(%!s(MISSING),%!u(MISSING)) failed: %!s(MISSING)\n"
+ "AppleMobileApNonce"
+ "IODeviceTree:/arm-io/sep/iop-sep-nub/Sandcat"
+ "IOServiceMatching failed for %!s(MISSING)\n"
+ "unable to read the AP slot id will not set.\n"
+ "IOServiceOpen failed for class '%!s(MISSING)'\n"
+ "Failed to connect to AppleMobileApNonce to generate AP nonce slot.\n"
+ "AppleSEPManager"

```
