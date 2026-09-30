## libcryptex.dylib

> `/usr/lib/libcryptex.dylib`

```diff

-493.100.42.0.0
-  __TEXT.__text: 0x25c1c
-  __TEXT.__auth_stubs: 0x1370
+493.100.51.0.0
+  __TEXT.__text: 0x2515c
+  __TEXT.__auth_stubs: 0x1360
   __TEXT.__objc_methlist: 0x490
-  __TEXT.__const: 0x7c5
+  __TEXT.__const: 0x7c0
   __TEXT.__gcc_except_tab: 0xf78
   __TEXT.__oslogstring: 0x3f36
-  __TEXT.__cstring: 0x1bb7
-  __TEXT.__unwind_info: 0x5d0
+  __TEXT.__cstring: 0x1ba7
+  __TEXT.__unwind_info: 0x5b0
   __TEXT.__objc_classname: 0x140
   __TEXT.__objc_methname: 0x9da
   __TEXT.__objc_methtype: 0x360

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x9c8
+  __AUTH_CONST.__auth_got: 0x9c0
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x140

   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
   - /System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libcryptex_core.dylib
   - /usr/lib/libcryptex_interface.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 491
-  Symbols:   1014
-  CStrings:  836
+  Functions: 480
+  Symbols:   1002
+  CStrings:  835
 
Symbols:
+ _Img4EncodeCreatePayload
+ _cryptex_core_set_nonce_persistence
+ _cryptex_tss_set_info_from_file
- _calloc
- _cryptex_tss_set_c411_from_file
- _malloc
- _memcmp
CStrings:
+ "%{public}s: Performing nonce domain workaround, 0x8 mapped to 0x3"
+ "493.100.51"
+ "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Fri Feb 21 20:08:15 PST 2025; root:libcryptex-493.100.51~147/libcryptex/RELEASE_ARM64E"
+ "Darwin Cryptex Interface Version 2.0.0: Fri Feb 21 20:08:15 PST 2025; root:libcryptex-493.100.51~147/libcryptex/RELEASE_ARM64E"
- "%{public}s: Performing nonce domain workaround, 0x5 mapped to 0x3"
- "493.100.42"
- "@(#)VERSION:Darwin Cryptex Interface Version 2.0.0: Sun Feb 16 10:33:32 PST 2025; root:libcryptex-493.100.42~129/libcryptex/RELEASE_ARM64E"
- "Cryptex1,ChipId"
- "Darwin Cryptex Interface Version 2.0.0: Sun Feb 16 10:33:32 PST 2025; root:libcryptex-493.100.42~129/libcryptex/RELEASE_ARM64E"

```
