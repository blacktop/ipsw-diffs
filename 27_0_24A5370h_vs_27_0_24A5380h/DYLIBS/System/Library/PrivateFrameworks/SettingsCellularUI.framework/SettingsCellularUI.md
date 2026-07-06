## SettingsCellularUI

> `/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI`

```diff

-  __TEXT.__text: 0x933c8
-  __TEXT.__objc_methlist: 0x9c04
+  __TEXT.__text: 0x93324
+  __TEXT.__objc_methlist: 0x9c2c
   __TEXT.__const: 0x498
   __TEXT.__dlopen_cstrs: 0x6a1
   __TEXT.__swift5_typeref: 0x196

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x10
-  __TEXT.__cstring: 0x910b
-  __TEXT.__oslogstring: 0x6c56
-  __TEXT.__gcc_except_tab: 0x1868
+  __TEXT.__cstring: 0x912e
+  __TEXT.__oslogstring: 0x6c4b
+  __TEXT.__gcc_except_tab: 0x1864
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2358
+  __TEXT.__unwind_info: 0x2370
   __TEXT.__eh_frame: 0x100
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1370
+  __DATA_CONST.__const: 0x1398
   __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5628
+  __DATA_CONST.__objc_selrefs: 0x5648
   __DATA_CONST.__objc_superrefs: 0x440
   __DATA_CONST.__objc_arraydata: 0x1b8
-  __DATA_CONST.__got: 0xa00
+  __DATA_CONST.__got: 0xac0
   __AUTH_CONST.__const: 0x5e0
-  __AUTH_CONST.__cfstring: 0x8780
-  __AUTH_CONST.__objc_const: 0x10290
-  __AUTH_CONST.__objc_intobj: 0x360
+  __AUTH_CONST.__cfstring: 0x8720
+  __AUTH_CONST.__objc_const: 0x102c8
+  __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x678
-  __AUTH.__objc_data: 0x1db0
-  __AUTH.__data: 0x270
+  __AUTH.__objc_data: 0x1718
+  __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x628
-  __DATA.__data: 0xbe8
-  __DATA.__bss: 0x1f8
-  __DATA_DIRTY.__objc_ivar: 0x5ec
-  __DATA_DIRTY.__objc_data: 0x1180
-  __DATA_DIRTY.__bss: 0x240
+  __DATA.__data: 0xb50
+  __DATA.__bss: 0xe8
+  __DATA_DIRTY.__objc_ivar: 0x5f0
+  __DATA_DIRTY.__objc_data: 0x1818
+  __DATA_DIRTY.__data: 0x270
+  __DATA_DIRTY.__bss: 0x370
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3341
-  Symbols:   11144
-  CStrings:  3151
+  Functions: 3349
+  Symbols:   11162
+  CStrings:  3146
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__objc_ivar : content changed
Symbols:
+ -[PSUIAddCellularPlanSpecifier pendingSimSetupOptions]
+ -[PSUIAddCellularPlanSpecifier setPendingSimSetupOptions:]
+ -[PSUICoreTelephonyRadioCache checkTARandomizationSupport:]
+ -[PSUICoreTelephonyRadioCache isTARandomizationRegulatoryDisabled:]
+ -[PSUICoreTelephonyRadioCache taRandomizationSupportChanged:support:]
+ _TSUserInfoIntermediateDefaultsToQuickSwitchKey
+ ___52-[EdgeSettingsController resetAllConfiguredSettings]_block_invoke_2
+ ___56-[EdgeSettingsController showCarrierSettingsEraseAlert:]_block_invoke_2
+ ___56-[EdgeSettingsController showCarrierSettingsEraseAlert:]_block_invoke_3
+ ___60-[EdgeSettingsController didChangeDeviceManagementSettings:]_block_invoke
+ ___block_descriptor_40_e8_32o_e5_v8?0ls32l8
+ _objc_msgSend$checkTARandomizationSupport:
+ _objc_msgSend$isTARandomizationRegulatoryDisabled:
+ _objc_msgSend$setPendingSimSetupOptions:
- -[PSUICoreTelephonyRadioCache checkTARandomizationSupported:]
- -[PSUICoreTelephonyRadioCache taRandomizationSupportChanged:supported:]
- _TSUserInfoIsSecondaryKey
- _TSUserInfoQuickSwitchFollowUpPhoneNumberKey
- _objc_msgSend$checkTARandomizationSupported:
CStrings:
+ "Skip query and return TA Randomization support %ld"
+ "TA Randomization support changed for descriptor: %@ to: %ld"
+ "TA_RANDOMIZATION_REGULATORY_DISABLED_FOOTER_PREFIX"
+ "addCellularPlan"
+ "default"
+ "qs"
+ "qsflow"
+ "stashing Add Cellular Plan presets for cellHighlighter-driven launch"
- "Edge"
- "Skip query and return TA Randomization support %d"
- "TA Randomization support changed for descriptor: %@ to: %d"
- "flow"
- "followUp"
- "launching Quick Switch enrollment flow"
- "launching Quick Switch follow-up info flow"
- "phoneNumber"
- "quickSwitch"
- "sliding"

```
