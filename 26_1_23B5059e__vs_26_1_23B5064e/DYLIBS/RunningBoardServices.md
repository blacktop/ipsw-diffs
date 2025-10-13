## RunningBoardServices

> `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices`

```diff

-1008.40.2.0.0
-  __TEXT.__text: 0x423cc
+1008.40.4.0.0
+  __TEXT.__text: 0x424ac
   __TEXT.__auth_stubs: 0xe20
   __TEXT.__objc_methlist: 0x5a68
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x4808
-  __TEXT.__oslogstring: 0x2768
+  __TEXT.__cstring: 0x481a
+  __TEXT.__oslogstring: 0x27a8
   __TEXT.__gcc_except_tab: 0x92c
   __TEXT.__dlopen_cstrs: 0x76
   __TEXT.__unwind_info: 0x1650
   __TEXT.__objc_classname: 0xf04
-  __TEXT.__objc_methname: 0x80cf
+  __TEXT.__objc_methname: 0x80e4
   __TEXT.__objc_methtype: 0x1595
   __TEXT.__objc_stubs: 0x4ae0
   __DATA_CONST.__got: 0x4d8

   __DATA_CONST.__objc_superrefs: 0x2d8
   __AUTH_CONST.__auth_got: 0x720
   __AUTH_CONST.__const: 0x660
-  __AUTH_CONST.__cfstring: 0x5ec0
-  __AUTH_CONST.__objc_const: 0xad18
+  __AUTH_CONST.__cfstring: 0x5ee0
+  __AUTH_CONST.__objc_const: 0xad38
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x1680
-  __DATA.__objc_ivar: 0x5c4
+  __DATA.__objc_ivar: 0x5c8
   __DATA.__data: 0x620
   __DATA.__bss: 0x260
   __DATA_DIRTY.__objc_data: 0x1400

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F9A8B6C8-3C0C-366A-828C-1FB4D37646A2
+  UUID: DDB8A617-9CE6-3012-BEB6-8E1A5621A678
   Functions: 2257
-  Symbols:   7106
-  CStrings:  3689
+  Symbols:   7107
+  CStrings:  3693
 
Symbols:
+ _OBJC_IVAR_$_RBSProcessHandle._deathCallbackCalled
Functions:
~ -[RBSXPCServiceProcessIdentity _initWithXPCServiceID:pid:auid:] : 696 -> 784
~ ___36-[RBSProcessHandle monitorForDeath:]_block_invoke : 272 -> 396
~ -[RBSProcessHandle initWithInstance:auditToken:bundleData:manageFlags:beforeTranslocationBundlePath:executablePath:cache:] : 572 -> 576
~ -[RBSProcessHandle initWithRBSXPCCoder:] : 608 -> 612
~ -[RBSProcessHandle _initWithIdentity:beforeTranslocationBundlePath:executablePath:] : 264 -> 268
CStrings:
+ "%@{definition:%@}"
+ "Death callback already called for handle %@, ignoring duplicate"
+ "_deathCallbackCalled"

```
