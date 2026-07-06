## com.apple.accessoryd.matching

> `/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching`

```diff

-  __TEXT.__text: 0x37c3c
+  __TEXT.__text: 0x37c8c
   __TEXT.__auth_stubs: 0x1000
   __TEXT.__objc_stubs: 0x5080
   __TEXT.__objc_methlist: 0x23ac
-  __TEXT.__cstring: 0x4f5a
+  __TEXT.__cstring: 0x4f8e
   __TEXT.__objc_methname: 0x6ebf
   __TEXT.__objc_classname: 0x27f
   __TEXT.__objc_methtype: 0xaeb

   __TEXT.__oslogstring: 0x3f4f
   __TEXT.__gcc_except_tab: 0x404
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0xa50
-  __DATA.__const: 0x10c0
-  __DATA.__cfstring: 0x3960
+  __TEXT.__unwind_info: 0xa58
+  __DATA.__const: 0x10e0
+  __DATA.__cfstring: 0x39a0
   __DATA.__objc_classlist: 0xb0
   __DATA.__objc_catlist: 0x10
   __DATA.__objc_protolist: 0x48

   __DATA.__data: 0x39e
   __DATA.__objc_dictobj: 0x28
   __DATA.__auth_got: 0x810
-  __DATA.__got: 0x358
+  __DATA.__got: 0x380
   __DATA.__auth_ptr: 0x18
   __DATA.__bss: 0x1e8
   __DATA.__common: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1495
-  Symbols:   8402
-  CStrings:  2980
+  Functions: 1496
+  Symbols:   8410
+  CStrings:  2984
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA.__objc_classlist : content changed
~ __DATA.__objc_catlist : content changed
~ __DATA.__objc_protolist : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_protorefs : content changed
~ __DATA.__objc_superrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__objc_arraydata : content changed
~ __DATA.__objc_arrayobj : content changed
~ __DATA.__objc_intobj : content changed
~ __DATA.__data : content changed
~ __DATA.__objc_dictobj : content changed
~ __DATA.__bss : content changed
~ __DATA.__common : content changed
Symbols:
+ _ACCUserDefaultsKey_EnableManager2ForTransport
+ _ACCUserDefaultsKey_OverrideMPPAuthSupported
+ _CFDictionaryCopyKeys
+ _kCFACCUserDefaultsKey_EnableManager2ForTransport
+ _kCFACCUserDefaultsKey_OverrideMPPAuthSupported
- _CFDictionaryGetKeys
Functions:
~ -[NSData(CKUtilsAdditions) CKHexString] : 416 -> 420
~ _acc_userNotifications_unlockToUseAccessories : 308 -> 324
~ _OUTLINED_FUNCTION_12 : 12 -> 16
~ _OUTLINED_FUNCTION_13 : 16 -> 12
~ _OUTLINED_FUNCTION_16 : 16 -> 20
~ _OUTLINED_FUNCTION_17 : 20 -> 16
+ _OUTLINED_FUNCTION_57
~ _OUTLINED_FUNCTION_59 : 20 -> 12
~ _systemInfo_copyProductType : 72 -> 96
~ _systemInfo_copyProductVersion : 72 -> 96
~ -[accessorydMatchingPlugin initWithModule:] : 2264 -> 2248
~ _LibCall_ACMContextVerifyPolicyAndCopyRequirementEx : 704 -> 716
~ _LibCall_ACMKernDoubleClickNotify : 172 -> 180
~ _LibCall_ACMContextVerifyPolicyEx : 196 -> 192
~ _LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx : 200 -> 196
~ _LibCall_ACMContextLoadFromImage : 464 -> 460
~ _LibCall_ACMSecSetBuiltinBiometry : 164 -> 172
CStrings:
+ "EnableManager2ForTransport"
+ "OverrideMPPAuthSupported"

```
