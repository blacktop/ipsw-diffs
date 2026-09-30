## CommunicationsSetupUI

> `/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI`

```diff

-1543.200.41.0.0
-  __TEXT.__text: 0x86708
-  __TEXT.__auth_stubs: 0x11a0
-  __TEXT.__objc_methlist: 0x859c
-  __TEXT.__cstring: 0xb127
+1543.200.51.0.0
+  __TEXT.__text: 0x86d98
+  __TEXT.__auth_stubs: 0x11b0
+  __TEXT.__objc_methlist: 0x860c
+  __TEXT.__cstring: 0xb267
   __TEXT.__const: 0x4c4
-  __TEXT.__gcc_except_tab: 0x4908
-  __TEXT.__oslogstring: 0x5aaf
+  __TEXT.__gcc_except_tab: 0x4980
+  __TEXT.__oslogstring: 0x5b77
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__ustring: 0x40
   __TEXT.__swift5_typeref: 0x304

   __TEXT.__swift5_fieldmd: 0xd8
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x2760
+  __TEXT.__unwind_info: 0x2790
   __TEXT.__objc_classname: 0x108f
-  __TEXT.__objc_methname: 0x15142
-  __TEXT.__objc_methtype: 0x39e0
-  __TEXT.__objc_stubs: 0x103e0
-  __DATA_CONST.__got: 0xb28
+  __TEXT.__objc_methname: 0x1531a
+  __TEXT.__objc_methtype: 0x3a3e
+  __TEXT.__objc_stubs: 0x10480
+  __DATA_CONST.__got: 0xb30
   __DATA_CONST.__const: 0x1200
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5810
+  __DATA_CONST.__objc_selrefs: 0x5868
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x8e0
+  __AUTH_CONST.__auth_got: 0x8e8
   __AUTH_CONST.__const: 0x960
-  __AUTH_CONST.__cfstring: 0xad80
-  __AUTH_CONST.__objc_const: 0xd0c8
+  __AUTH_CONST.__cfstring: 0xae40
+  __AUTH_CONST.__objc_const: 0xd120
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1e78
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x564
+  __DATA.__objc_ivar: 0x56c
   __DATA.__data: 0xe68
   __DATA.__bss: 0x668
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x140
+  - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BD4C4E7F-A9FC-3520-B6F3-BB8F9B98D90C
-  Functions: 2884
-  Symbols:   10282
-  CStrings:  7324
+  UUID: 258F6C46-D41A-356E-BA19-F74409AD437F
+  Functions: 2893
+  Symbols:   10312
+  CStrings:  7355
 
Symbols:
+ -[CNFRegSettingsController _updateAVCUserDefaults]
+ -[CNFRegSettingsController deviceHWSupportsAlwaysFullBleed]
+ -[CNFRegSettingsController getAlwaysFullBleedEnabledForSpecifier:]
+ -[CNFRegSettingsController refreshAlwaysFullBleedSettingsAnimated:]
+ -[CNFRegSettingsController setAlwaysFullBleedEnabled:specifier:]
+ -[CNFRegSettingsController setVideoConferenceDefaults:]
+ -[CNFRegSettingsController shouldShowAlwaysFullBleedSpecifiers]
+ -[CNFRegSettingsController showAlwaysFullBleedSpecifiers:animated:]
+ -[CNFRegSettingsController videoConferenceDefaults]
+ GCC_except_table102
+ GCC_except_table114
+ GCC_except_table116
+ GCC_except_table120
+ GCC_except_table125
+ GCC_except_table143
+ GCC_except_table150
+ GCC_except_table153
+ GCC_except_table158
+ GCC_except_table163
+ GCC_except_table164
+ GCC_except_table169
+ GCC_except_table173
+ GCC_except_table174
+ GCC_except_table185
+ GCC_except_table195
+ GCC_except_table208
+ GCC_except_table211
+ GCC_except_table214
+ GCC_except_table227
+ GCC_except_table230
+ GCC_except_table231
+ GCC_except_table232
+ GCC_except_table233
+ GCC_except_table245
+ GCC_except_table246
+ GCC_except_table247
+ GCC_except_table56
+ GCC_except_table87
+ GCC_except_table99
+ _AVGQCB54MH3XAXNGTVD2SAMOV5WWOQ
+ _AVGestaltGetBoolAnswer
+ _OBJC_IVAR_$_CNFRegSettingsController._alwaysFullBleedGroupSpecifiers
+ _OBJC_IVAR_$_CNFRegSettingsController._videoConferenceDefaults
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.896
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.900
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.920
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_2.922
+ ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_3.924
+ ___69-[CNFRegSettingsController _setupAccountHandlersForDisabledOperation]_block_invoke.889
+ ___Block_byref_object_copy_.917
+ ___Block_byref_object_dispose_.918
+ ___block_literal_global.392
+ ___block_literal_global.547
+ ___block_literal_global.576
+ ___block_literal_global.584
+ _objc_msgSend$_updateAVCUserDefaults
+ _objc_msgSend$deviceHWSupportsAlwaysFullBleed
+ _objc_msgSend$deviceType
+ _objc_msgSend$shouldShowAlwaysFullBleedSpecifiers
+ _objc_msgSend$showAlwaysFullBleedSpecifiers:animated:
- GCC_except_table113
- GCC_except_table134
- GCC_except_table148
- GCC_except_table152
- GCC_except_table156
- GCC_except_table161
- GCC_except_table166
- GCC_except_table167
- GCC_except_table178
- GCC_except_table188
- GCC_except_table200
- GCC_except_table201
- GCC_except_table204
- GCC_except_table210
- GCC_except_table215
- GCC_except_table220
- GCC_except_table223
- GCC_except_table224
- GCC_except_table226
- GCC_except_table238
- GCC_except_table239
- GCC_except_table240
- GCC_except_table77
- GCC_except_table86
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.877
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.881
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke.882
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_2.903
- ___67-[CNFRegSettingsController _setupAccountHandlersForNormalOperation]_block_invoke_3.905
- ___69-[CNFRegSettingsController _setupAccountHandlersForDisabledOperation]_block_invoke.870
- ___Block_byref_object_copy_.914
- ___Block_byref_object_dispose_.915
- ___block_literal_global.386
- ___block_literal_global.537
- ___block_literal_global.573
- ___block_literal_global.581
CStrings:
+ "@\"NSUserDefaults\""
+ "FACETIME_ALWAYS_FULL_BLEED_GROUP_ID"
+ "FACETIME_ALWAYS_FULL_BLEED_SWITCH_ID"
+ "FaceTime AlwaysFullBleed availability is %d since deviceIsiPhone = %d and deviceSupportsDynamicAspectRatio = %d"
+ "FaceTime AlwaysFullBleed enabled changing to: %d"
+ "FaceTime AlwaysFullBleed enabled is %d"
+ "T@\"NSUserDefaults\",&,N,V_videoConferenceDefaults"
+ "_alwaysFullBleedGroupSpecifiers"
+ "_updateAVCUserDefaults"
+ "_videoConferenceDefaults"
+ "deviceHWSupportsAlwaysFullBleed"
+ "deviceType"
+ "getAlwaysFullBleedEnabledForSpecifier:"
+ "refreshAlwaysFullBleedSettingsAnimated:"
+ "service:account:inviteDroppedForSessionID:fromID:error:"
+ "setAlwaysFullBleedEnabled:specifier:"
+ "setVideoConferenceDefaults:"
+ "shouldShowAlwaysFullBleedSpecifiers"
+ "showAlwaysFullBleedSpecifiers:animated:"
+ "userPreferTxAlwaysFullBleedDisabled"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"
+ "videoConferenceDefaults"

```
