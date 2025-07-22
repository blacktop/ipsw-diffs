## AppStoreDaemon

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon`

```diff

-10.4.45.2.1
-  __TEXT.__text: 0x78cf8
+10.4.50.0.0
+  __TEXT.__text: 0x78d68
   __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x8ed4
+  __TEXT.__objc_methlist: 0x8eec
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x51d3
+  __TEXT.__cstring: 0x51e9
   __TEXT.__swift5_typeref: 0xe
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_reflstr: 0x31

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x114d0
+  __DATA_CONST.__objc_const: 0x11500
   __DATA_CONST.__objc_selrefs: 0x3d68
   __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_classrefs: 0x5a8

   __DATA.__objc_ivar: 0xc2c
   __DATA.__data: 0x1940
   __DATA.__bss: 0x190
-  __DATA_DIRTY.__objc_ivar: 0x1ac
+  __DATA_DIRTY.__objc_ivar: 0x1b0
   __DATA_DIRTY.__objc_data: 0x2030
   __DATA_DIRTY.__data: 0x50
   __DATA_DIRTY.__bss: 0x280

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 87763354-4045-3300-A909-464D063C563A
-  Functions: 4095
-  Symbols:   12595
+  UUID: 6D5E8B79-AFE4-3D26-ACF6-369617AC2B38
+  Functions: 4097
+  Symbols:   12599
   CStrings:  6081
 
Symbols:
+ -[ASDPurgeAppsRequestOptions setSkipLaunchCheck:]
+ -[ASDPurgeAppsRequestOptions skipLaunchCheck]
CStrings:
+ "%@ {urgency = %ld, desired = %@ volume: %@ skip launch check: %d apps: [%@]}"
- "%@ {urgency = %ld, desired = %@ volume: %@ apps: [%@]}"

```
