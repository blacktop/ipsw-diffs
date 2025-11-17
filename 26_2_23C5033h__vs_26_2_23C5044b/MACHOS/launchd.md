## launchd

> `/sbin/launchd`

```diff

-3089.60.4.0.0
-  __TEXT.__text: 0x54600
+3089.60.7.0.0
+  __TEXT.__text: 0x54670
   __TEXT.__auth_stubs: 0x21f0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x20c
   __TEXT.__const: 0x340
-  __TEXT.__cstring: 0x15292
+  __TEXT.__cstring: 0x15302
   __TEXT.__launchd: 0x1
   __TEXT.__objc_methname: 0x8
   __TEXT.__objc_classname: 0x1d5

   __DATA_CONST.__auth_got: 0x10f8
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x5620
+  __DATA_CONST.__const: 0x5630
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: 6CC112FB-9AAD-322C-8635-50ECFDDB3739
+  UUID: AEDB9FBC-8269-3BFA-AF81-885B8CB060FC
   Functions: 1720
   Symbols:   598
-  CStrings:  2719
+  CStrings:  2722
 
Functions:
~ sub_10001224c : 424 -> 444
~ sub_100012b2c -> sub_100012b40 : 168 -> 208
~ sub_10002729c -> sub_1000272d8 : 468 -> 472
~ sub_10002c3e8 -> sub_10002c428 : 564 -> 612
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Tue Nov 11 23:56:04 PST 2025; root:libxpc_executables-3089.60.7~72/launchd/RELEASE_ARM64E"
+ "Darwin Bootstrapper Version 7.0.0: Tue Nov 11 23:56:04 PST 2025; root:libxpc_executables-3089.60.7~72/launchd/RELEASE_ARM64E"
+ "KSS_CHECKED_ALLOCATIONS_PREFLIGHT:Enable=1"
+ "com.apple.private.xpc.launchd.setenv-pid-domain"
+ "controlled-preflight"
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sun Nov  2 21:13:09 PST 2025; root:libxpc_executables-3089.60.4~92/launchd/RELEASE_ARM64E"
- "Darwin Bootstrapper Version 7.0.0: Sun Nov  2 21:13:09 PST 2025; root:libxpc_executables-3089.60.4~92/launchd/RELEASE_ARM64E"

```
