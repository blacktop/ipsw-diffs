## MechPasscode

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPasscode.bundle/MechPasscode`

```diff

-  __TEXT.__text: 0x143e8
+  __TEXT.__text: 0x14438
   __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0xec0
   __TEXT.__objc_methlist: 0x2b8
   __TEXT.__const: 0x190
   __TEXT.__cstring: 0x2185
-  __TEXT.__objc_methname: 0xce2
+  __TEXT.__objc_methname: 0xced
   __TEXT.__oslogstring: 0x39d
   __TEXT.__objc_classname: 0x59
   __TEXT.__objc_methtype: 0x1b1

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x498
   __DATA.__objc_selrefs: 0x440

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 499
+  Functions: 500
   Symbols:   376
   CStrings:  500
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Functions:
~ sub_3204 : 192 -> 244
+ sub_a35c
- sub_a334
+ sub_a3b8
~ _LibCall_ACMContextVerifyPolicyAndCopyRequirementEx : 704 -> 716
~ _LibCall_ACMKernDoubleClickNotify : 172 -> 180
~ _LibCall_ACMContextVerifyPolicyEx : 196 -> 192
~ _LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx : 200 -> 196
~ _LibCall_ACMContextLoadFromImage : 464 -> 460
~ _LibCall_ACMSecSetBuiltinBiometry : 164 -> 172
CStrings:
+ "allowsAuthenticationFallbacksForOptions:"
- "allowsAuthenticationFallbacks"

```
