## DisembarkUI

> `/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI`

```diff

-224.0.0.0.0
-  __TEXT.__text: 0x161ec
+226.0.0.0.0
+  __TEXT.__text: 0x16400
   __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0x17ec
+  __TEXT.__objc_methlist: 0x184c
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x1443
+  __TEXT.__cstring: 0x1466
   __TEXT.__gcc_except_tab: 0x158
   __TEXT.__oslogstring: 0xad9
-  __TEXT.__unwind_info: 0x598
-  __TEXT.__objc_classname: 0x4d4
-  __TEXT.__objc_methname: 0x5a40
-  __TEXT.__objc_methtype: 0x11dd
-  __TEXT.__objc_stubs: 0x44e0
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0xaf8
-  __DATA_CONST.__objc_classlist: 0x108
+  __TEXT.__unwind_info: 0x594
+  __TEXT.__objc_classname: 0x4ed
+  __TEXT.__objc_methname: 0x5b74
+  __TEXT.__objc_methtype: 0x1240
+  __TEXT.__objc_stubs: 0x4580
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__const: 0xb20
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3b80
-  __DATA_CONST.__objc_selrefs: 0x1450
+  __DATA_CONST.__objc_const: 0x3d48
+  __DATA_CONST.__objc_selrefs: 0x1480
   __AUTH_CONST.__cfstring: 0x1120
-  __AUTH_CONST.__objc_const: 0xaa8
+  __AUTH_CONST.__objc_const: 0xaf0
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__auth_got: 0x278
-  __AUTH.__objc_data: 0xa50
-  __DATA.__objc_classrefs: 0x330
+  __AUTH.__objc_data: 0xaa0
+  __DATA.__objc_classrefs: 0x338
   __DATA.__objc_superrefs: 0xa8
-  __DATA.__objc_ivar: 0x220
-  __DATA.__data: 0x840
+  __DATA.__objc_ivar: 0x22c
+  __DATA.__data: 0x8a0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/StorageData.framework/StorageData
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 199011E4-3FBB-3611-A88F-16A55AA81D92
-  Functions: 650
-  Symbols:   2601
-  CStrings:  1590
+  UUID: 0061B94A-3169-3917-A9C7-38D19614183A
+  Functions: 659
+  Symbols:   2641
+  CStrings:  1610
 
Symbols:
+ -[DKEraseFlow eraseDataPlan]
+ -[DKEraseFlow setEraseDataPlan:]
+ -[DKIntroViewController confirmErase]
+ -[DKIntroViewController setConfirmErase:]
+ -[DKNotableUserDataProvider fetchNotableUserData:].cold.6
+ -[DKNotableUserDataProvider restrictionsProvider]
+ -[DKNotableUserDataProvider setRestrictionsProvider:]
+ -[DKRestrictionsProvider isPreserveESIMOnEraseEnforced]
+ _OBJC_CLASS_$_DKRestrictionsProvider
+ _OBJC_IVAR_$_DKEraseFlow._eraseDataPlan
+ _OBJC_IVAR_$_DKIntroViewController._confirmErase
+ _OBJC_IVAR_$_DKNotableUserDataProvider._restrictionsProvider
+ _OBJC_METACLASS_$_DKRestrictionsProvider
+ __OBJC_$_INSTANCE_METHODS_DKRestrictionsProvider
+ __OBJC_$_PROP_LIST_DKNotableUserDataProvider.149
+ __OBJC_$_PROP_LIST_DKRestrictionsProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DKRestrictionsProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DKRestrictionsProvider
+ __OBJC_$_PROTOCOL_REFS_DKRestrictionsProvider
+ __OBJC_CLASS_PROTOCOLS_$_DKRestrictionsProvider
+ __OBJC_CLASS_RO_$_DKRestrictionsProvider
+ __OBJC_LABEL_PROTOCOL_$_DKRestrictionsProvider
+ __OBJC_METACLASS_RO_$_DKRestrictionsProvider
+ __OBJC_PROTOCOL_$_DKRestrictionsProvider
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_14
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_15
+ ___41-[DKIntroViewController _continueTapped:]_block_invoke_4
+ ___50-[DKNotableUserDataProvider fetchNotableUserData:]_block_invoke.43
+ ___NSArray0__struct
+ ___block_descriptor_40_e8_32s_e14_v16?0?<v?>8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e11_v16?0B8B12ls32l8s40l8
+ _objc_msgSend$confirmErase
+ _objc_msgSend$eraseDataPlan
+ _objc_msgSend$isPreserveESIMOnEraseEnforced
+ _objc_msgSend$restrictionsProvider
+ _objc_msgSend$setConfirmErase:
- __OBJC_$_PROP_LIST_DKNotableUserDataProvider.138
- ___27-[DKEraseFlow _eraseDevice]_block_invoke.145
- ___27-[DKEraseFlow _eraseDevice]_block_invoke_2.149
- ___50-[DKNotableUserDataProvider fetchNotableUserData:]_block_invoke.37
- ___block_descriptor_48_e8_32s40bs_e11_v16?0B8B12ls40l8s32l8
CStrings:
+ "\x06"
+ "/\x04\x12"
+ "@\"<DKRestrictionsProvider>\""
+ "@\"<DKRestrictionsProvider>\"16@0:8"
+ "Confirmation"
+ "DKRestrictionsProvider"
+ "T@\"<DKRestrictionsProvider>\",&,N"
+ "T@\"<DKRestrictionsProvider>\",&,N,V_restrictionsProvider"
+ "T@?,C,N,V_confirmErase"
+ "TB,N,V_eraseDataPlan"
+ "_confirmErase"
+ "_eraseDataPlan"
+ "_restrictionsProvider"
+ "confirmErase"
+ "eraseDataPlan"
+ "isPreserveESIMOnEraseEnforced"
+ "restrictionsProvider"
+ "self.restrictionsProvider"
+ "setConfirmErase:"
+ "setRestrictionsProvider:"
+ "v16@?0@?<v@?>8"
+ "v24@0:8@\"<DKRestrictionsProvider>\"16"
- "\x1f\x04\x12"
- "Final Confirmation"

```
