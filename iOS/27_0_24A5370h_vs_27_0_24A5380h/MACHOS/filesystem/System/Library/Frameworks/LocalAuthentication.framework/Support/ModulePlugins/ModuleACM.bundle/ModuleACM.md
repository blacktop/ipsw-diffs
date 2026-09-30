## ModuleACM

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/ModulePlugins/ModuleACM.bundle/ModuleACM`

```diff

-  __TEXT.__text: 0x20d18
+  __TEXT.__text: 0x20d28
   __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_stubs: 0x2680
+  __TEXT.__objc_stubs: 0x26c0
   __TEXT.__objc_methlist: 0x4ac
   __TEXT.__const: 0x2c0
   __TEXT.__gcc_except_tab: 0x3e0
   __TEXT.__cstring: 0x2cd1
-  __TEXT.__objc_methname: 0x27cb
+  __TEXT.__objc_methname: 0x280d
   __TEXT.__oslogstring: 0xb60
   __TEXT.__ustring: 0x1e
   __TEXT.__objc_classname: 0x49

   __DATA_CONST.__got: 0x298
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x518
-  __DATA.__objc_selrefs: 0xa70
+  __DATA.__objc_selrefs: 0xa80
   __DATA.__objc_ivar: 0x4c
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x2

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 636
+  Functions: 637
   Symbols:   448
-  CStrings:  1089
+  CStrings:  1091
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
Functions:
~ sub_158c : 576 -> 564
+ sub_17634
- sub_1764c
+ sub_17690
~ _LibCall_ACMContextVerifyPolicyAndCopyRequirementEx : 704 -> 716
~ _LibCall_ACMKernDoubleClickNotify : 172 -> 180
~ _LibCall_ACMContextVerifyPolicyEx : 196 -> 192
~ _LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx : 200 -> 196
~ _LibCall_ACMContextLoadFromImage : 464 -> 460
~ _LibCall_ACMSecSetBuiltinBiometry : 164 -> 172
CStrings:
+ "createContextWithExternalForm:"
+ "createContextWithFlags:contextRef:"

```
