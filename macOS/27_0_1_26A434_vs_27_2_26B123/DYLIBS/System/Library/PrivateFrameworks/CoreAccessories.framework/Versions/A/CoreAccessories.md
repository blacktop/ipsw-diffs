## CoreAccessories

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Versions/A/CoreAccessories`

```diff

-1216.0.0.0.0
-  __TEXT.__text: 0x28bb8
-  __TEXT.__objc_methlist: 0x19ac
-  __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x3d30
-  __TEXT.__oslogstring: 0x3f32
+1219.40.10.0.0
+  __TEXT.__text: 0x292fc
+  __TEXT.__objc_methlist: 0x19d4
+  __TEXT.__const: 0x168
+  __TEXT.__cstring: 0x3d79
+  __TEXT.__oslogstring: 0x4021
   __TEXT.__gcc_except_tab: 0x82c
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0xa38
+  __TEXT.__unwind_info: 0xa58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1780
+  __DATA_CONST.__const: 0x17c0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf50
+  __DATA_CONST.__objc_selrefs: 0xf68
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xd8
   __DATA_CONST.__got: 0x138
-  __AUTH_CONST.__const: 0x14f0
-  __AUTH_CONST.__cfstring: 0x3b20
-  __AUTH_CONST.__objc_const: 0x2360
+  __AUTH_CONST.__const: 0x1510
+  __AUTH_CONST.__cfstring: 0x3b60
+  __AUTH_CONST.__objc_const: 0x2398
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0xdc
+  __DATA.__objc_ivar: 0xe0
   __DATA.__data: 0x760
-  __DATA.__bss: 0x110
+  __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x138
   __DATA_DIRTY.__bss: 0x68

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 843
-  Symbols:   2367
-  CStrings:  861
+  Functions: 855
+  Symbols:   2388
+  CStrings:  867
 
Symbols:
+ -[ACCHWComponentAuth signTouchControllerChallenge:completionHandler:componentIndex:]
+ -[_ACCExternalAccessoryInfo ppidVersionUID]
+ -[_ACCExternalAccessoryInfo setPpidVersionUID:]
+ GCC_except_table40
+ GCC_except_table46
+ OBJC_IVAR_$__ACCExternalAccessoryInfo._ppidVersionUID
+ __84-[ACCHWComponentAuth signTouchControllerChallenge:completionHandler:componentIndex:]_block_invoke
+ __84-[ACCHWComponentAuth signTouchControllerChallenge:completionHandler:componentIndex:]_block_invoke_2
+ ___84-[ACCHWComponentAuth signTouchControllerChallenge:completionHandler:componentIndex:]_block_invoke
+ ___84-[ACCHWComponentAuth signTouchControllerChallenge:completionHandler:componentIndex:]_block_invoke_2
+ ___acc_internalSettings_isInternalBuild_block_invoke
+ _acc_internalSettings_boolForKey
+ _acc_internalSettings_integerForKey
+ _acc_internalSettings_isInternalBuild
+ _kACCExternalAccessoryPPIDVersionUIDKey
+ _kACCInfo_PPIDVersionUID
+ _kCFACCExternalAccessoryPPIDVersionUIDKey
+ _kCFACCInfo_PPIDVersionUID
+ _objc_msgSend$ppidVersionUID
+ _objc_msgSend$setPpidVersionUID:
+ _objc_msgSend$signTouchControllerChallenge:completionHandler:componentIndex:
+ acc_internalSettings_boolForKey
+ acc_internalSettings_integerForKey
+ acc_internalSettings_isInternalBuild
+ acc_internalSettings_isInternalBuild.isInternalBuild
+ acc_internalSettings_isInternalBuild.onceToken
- GCC_except_table108
- GCC_except_table38
- GCC_except_table44
- GCC_except_table57
- GCC_except_table64
CStrings:
+ "<_ACCExternalAccessoryInfo>[%@ name='%@' manu='%@' model='%@' serial='%@' fw(active)='%@', fw(pending)='%@', hw='%@' ppid='%@' ppidVersionUID='%@']"
+ "ACCExternalAccessoryPPIDVersionUIDKey"
+ "PPIDVersionUID"
+ "Signing touch controller challenge... (completionHandler: %s)"
+ "acc_internalSettings: internal-only setting %{public}@ active"
+ "acc_internalSettings: internal-only setting %{public}@ active (%ld)"
+ "signed touch controller challenge authError %d"
- "<_ACCExternalAccessoryInfo>[%@ name='%@' manu='%@' model='%@' serial='%@' fw(active)='%@', fw(pending)='%@', hw='%@' ppid='%@']"
```
