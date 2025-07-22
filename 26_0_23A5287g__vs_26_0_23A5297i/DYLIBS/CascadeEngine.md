## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-197.0.0.0.0
-  __TEXT.__text: 0x1f6c4
+198.0.0.0.0
+  __TEXT.__text: 0x1f744
   __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x17cc
-  __TEXT.__const: 0x110
+  __TEXT.__objc_methlist: 0x17dc
+  __TEXT.__const: 0x118
   __TEXT.__gcc_except_tab: 0x69c
   __TEXT.__cstring: 0x107c
-  __TEXT.__oslogstring: 0x3b51
+  __TEXT.__oslogstring: 0x3bbb
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__unwind_info: 0x848
   __TEXT.__objc_classname: 0x46e
-  __TEXT.__objc_methname: 0x5207
+  __TEXT.__objc_methname: 0x523e
   __TEXT.__objc_methtype: 0xfcb
-  __TEXT.__objc_stubs: 0x4460
+  __TEXT.__objc_stubs: 0x4480
   __DATA_CONST.__got: 0x288
   __DATA_CONST.__const: 0xb88
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1388
+  __DATA_CONST.__objc_selrefs: 0x1390
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0xb8
   __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0xf40
-  __AUTH_CONST.__objc_const: 0x3120
+  __AUTH_CONST.__objc_const: 0x3150
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x258
+  __DATA.__objc_ivar: 0x25c
   __DATA.__data: 0x720
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x5f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BE4D1276-56AC-38C2-A05C-DCBB013898C3
-  Functions: 694
-  Symbols:   2767
-  CStrings:  1586
+  UUID: 6A5FE258-ADA9-319A-907F-73E78ECF2EEB
+  Functions: 695
+  Symbols:   2771
+  CStrings:  1590
 
Symbols:
+ -[CCDifferentialUpdater clientFinished]
+ GCC_except_table59
+ _OBJC_IVAR_$_CCDifferentialUpdater._clientFinished
+ _objc_msgSend$clientFinished
- GCC_except_table58
- GCC_except_table63
- GCC_except_table65
Functions:
~ __recursivelyWaitForTransactionProgress : 636 -> 748
~ -[CCDifferentialUpdater finishUpdateWithRevisionToken:designateAsFullSet:] : 56 -> 64
+ -[CCDifferentialUpdater clientFinished]
CStrings:
+ "Client progress check-in after ~%.2lf seconds:\t {%u items added or updated, %u removed}\t[CLIENT FINISHED]"
+ "TB,R,N,V_clientFinished"
+ "_clientFinished"
+ "clientFinished"

```
