## RunningBoardServices

> `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices`

```diff

-1008.40.4.0.0
-  __TEXT.__text: 0x424ac
+1008.42.1.0.0
+  __TEXT.__text: 0x42424
   __TEXT.__auth_stubs: 0xe20
   __TEXT.__objc_methlist: 0x5a68
   __TEXT.__const: 0x150
   __TEXT.__cstring: 0x481a
-  __TEXT.__oslogstring: 0x27a8
+  __TEXT.__oslogstring: 0x2768
   __TEXT.__gcc_except_tab: 0x92c
   __TEXT.__dlopen_cstrs: 0x76
   __TEXT.__unwind_info: 0x1650
   __TEXT.__objc_classname: 0xf04
-  __TEXT.__objc_methname: 0x80e4
+  __TEXT.__objc_methname: 0x80cf
   __TEXT.__objc_methtype: 0x1595
   __TEXT.__objc_stubs: 0x4ae0
   __DATA_CONST.__got: 0x4d8

   __AUTH_CONST.__auth_got: 0x720
   __AUTH_CONST.__const: 0x660
   __AUTH_CONST.__cfstring: 0x5ee0
-  __AUTH_CONST.__objc_const: 0xad38
+  __AUTH_CONST.__objc_const: 0xad18
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x1680
-  __DATA.__objc_ivar: 0x5c8
+  __DATA.__objc_ivar: 0x5c4
   __DATA.__data: 0x620
   __DATA.__bss: 0x260
   __DATA_DIRTY.__objc_data: 0x1400

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0A4C0F8F-075C-393B-AE81-DC59EC49883D
+  UUID: CDD84DF0-7A5B-3A48-9B9A-9509AD5697A3
   Functions: 2257
-  Symbols:   7107
-  CStrings:  3693
+  Symbols:   7106
+  CStrings:  3691
 
Symbols:
- _OBJC_IVAR_$_RBSProcessHandle._deathCallbackCalled
Functions:
~ ___36-[RBSProcessHandle monitorForDeath:]_block_invoke : 396 -> 272
~ -[RBSProcessHandle initWithInstance:auditToken:bundleData:manageFlags:beforeTranslocationBundlePath:executablePath:cache:] : 576 -> 572
~ -[RBSProcessHandle initWithRBSXPCCoder:] : 612 -> 608
~ -[RBSProcessHandle _initWithIdentity:beforeTranslocationBundlePath:executablePath:] : 268 -> 264
CStrings:
- "Death callback already called for handle %@, ignoring duplicate"
- "_deathCallbackCalled"

```
