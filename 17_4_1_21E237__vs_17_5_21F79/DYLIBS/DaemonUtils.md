## DaemonUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils`

```diff

-1394.100.151.0.1
-  __TEXT.__text: 0xe088
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x10dc
+1394.120.27.0.0
+  __TEXT.__text: 0xe3c8
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_methlist: 0x10ec
   __TEXT.__const: 0x110
   __TEXT.__cstring: 0xed9
-  __TEXT.__oslogstring: 0xd84
+  __TEXT.__oslogstring: 0xdcf
   __TEXT.__gcc_except_tab: 0x1a0
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x4ec
+  __TEXT.__unwind_info: 0x4e8
   __TEXT.__objc_classname: 0x286
-  __TEXT.__objc_methname: 0x33a6
+  __TEXT.__objc_methname: 0x33d4
   __TEXT.__objc_methtype: 0x7af
-  __TEXT.__objc_stubs: 0x29e0
+  __TEXT.__objc_stubs: 0x2a00
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x4b0
+  __DATA_CONST.__const: 0x4d8
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x26a8
-  __DATA_CONST.__objc_selrefs: 0xd20
+  __DATA_CONST.__objc_selrefs: 0xd28
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x180
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__cfstring: 0xf60
-  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__objc_const: 0x940
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0x368
-  __AUTH.__objc_data: 0x1e0
+  __AUTH_CONST.__auth_got: 0x378
+  __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x178
   __DATA.__data: 0x240
   __DATA.__bss: 0x88
-  __DATA_DIRTY.__objc_data: 0x500
+  __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__bss: 0x138
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2BF790B6-2415-3B34-BAC1-D6BA25DE7511
-  Functions: 448
-  Symbols:   1808
-  CStrings:  1137
+  UUID: A8FB9F71-EDA7-374D-81A2-939FCF870A33
+  Functions: 454
+  Symbols:   1825
+  CStrings:  1139
 
Symbols:
+ +[DaemonUtils _callerDisplayNameWithPid:auditToken:bundleId:]
+ +[DaemonUtils callerDisplayNameWithPid:auditToken:bundleId:].cold.1
+ ___60+[DaemonUtils callerDisplayNameWithPid:auditToken:bundleId:]_block_invoke
+ ___60+[DaemonUtils callerDisplayNameWithPid:auditToken:bundleId:]_block_invoke.4
+ ___block_descriptor_92_e8_32bs40r48r_e5_v8?0lr40l8r48l8s32l8
+ ___block_literal_global.24
+ ___block_literal_global.29
+ ___block_literal_global.3
+ ___block_literal_global.34
+ ___block_literal_global.39
+ ___block_literal_global.44
+ ___block_literal_global.86
+ ___block_literal_global.88
+ _dispatch_block_wait
+ _dispatch_get_global_queue
+ _objc_msgSend$_callerDisplayNameWithPid:auditToken:bundleId:
- ___block_literal_global.21
- ___block_literal_global.26
- ___block_literal_global.31
- ___block_literal_global.36
- ___block_literal_global.41
- ___block_literal_global.82
- ___block_literal_global.84
CStrings:
+ "Timed out after trying to determine caller name and bundle ID for %.1f sec"
+ "_callerDisplayNameWithPid:auditToken:bundleId:"

```
