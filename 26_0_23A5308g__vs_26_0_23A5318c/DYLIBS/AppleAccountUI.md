## AppleAccountUI

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI`

```diff

-548.0.0.0.0
-  __TEXT.__text: 0x230154
-  __TEXT.__auth_stubs: 0x3980
+550.0.0.0.0
+  __TEXT.__text: 0x235778
+  __TEXT.__auth_stubs: 0x3a60
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0x244
-  __TEXT.__objc_methlist: 0xb0dc
-  __TEXT.__cstring: 0x9e89
-  __TEXT.__const: 0xa5c4
-  __TEXT.__gcc_except_tab: 0x1658
-  __TEXT.__oslogstring: 0xdc0c
+  __TEXT.__objc_methlist: 0xb18c
+  __TEXT.__cstring: 0x9f99
+  __TEXT.__const: 0xa714
+  __TEXT.__gcc_except_tab: 0x16b0
+  __TEXT.__oslogstring: 0xdcfc
   __TEXT.__dlopen_cstrs: 0x526
   __TEXT.__ustring: 0x4
-  __TEXT.__constg_swiftt: 0x4858
-  __TEXT.__swift5_typeref: 0xd42e
-  __TEXT.__swift5_reflstr: 0x24b6
-  __TEXT.__swift5_fieldmd: 0x2354
-  __TEXT.__swift5_types: 0x444
-  __TEXT.__swift5_capture: 0x24f4
+  __TEXT.__constg_swiftt: 0x4924
+  __TEXT.__swift5_typeref: 0xd54a
+  __TEXT.__swift5_reflstr: 0x2516
+  __TEXT.__swift5_fieldmd: 0x23a4
+  __TEXT.__swift5_types: 0x44c
+  __TEXT.__swift5_capture: 0x2634
   __TEXT.__swift5_assocty: 0xc98
-  __TEXT.__swift5_proto: 0x5c0
+  __TEXT.__swift5_proto: 0x5e0
   __TEXT.__swift_as_entry: 0x10c
   __TEXT.__swift_as_ret: 0xf0
   __TEXT.__swift5_builtin: 0x1e0
-  __TEXT.__swift5_protos: 0x1c
+  __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x5310
+  __TEXT.__unwind_info: 0x53c8
   __TEXT.__eh_frame: 0x1548
-  __TEXT.__objc_classname: 0x2202
-  __TEXT.__objc_methname: 0x1b13b
+  __TEXT.__objc_classname: 0x221e
+  __TEXT.__objc_methname: 0x1b2b5
   __TEXT.__objc_methtype: 0x4fb9
-  __TEXT.__objc_stubs: 0x138a0
-  __DATA_CONST.__got: 0x1c18
-  __DATA_CONST.__const: 0x3138
-  __DATA_CONST.__objc_classlist: 0x7d0
-  __DATA_CONST.__objc_catlist: 0x78
+  __TEXT.__objc_stubs: 0x13960
+  __DATA_CONST.__got: 0x1c38
+  __DATA_CONST.__const: 0x3188
+  __DATA_CONST.__objc_classlist: 0x7d8
+  __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6710
+  __DATA_CONST.__objc_selrefs: 0x6758
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x1ce0
-  __AUTH_CONST.__const: 0x9010
-  __AUTH_CONST.__cfstring: 0x4b20
-  __AUTH_CONST.__objc_const: 0x3c900
+  __AUTH_CONST.__auth_got: 0x1d50
+  __AUTH_CONST.__const: 0x93a0
+  __AUTH_CONST.__cfstring: 0x4b60
+  __AUTH_CONST.__objc_const: 0x3cab0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x6740
+  __AUTH.__objc_data: 0x67d0
   __AUTH.__data: 0x28f0
-  __DATA.__objc_ivar: 0xbe0
-  __DATA.__data: 0x54b0
-  __DATA.__bss: 0xc170
+  __DATA.__objc_ivar: 0xbec
+  __DATA.__data: 0x5520
+  __DATA.__bss: 0xc470
   __DATA.__common: 0x4d0
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x48

   - /System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI
   - /System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI
   - /System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation
+  - /System/Library/PrivateFrameworks/Settings.framework/Settings
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 32D45C19-F5F6-35D3-8FA8-8A1C59C93FA9
-  Functions: 11178
-  Symbols:   17303
-  CStrings:  7972
+  UUID: 75FB0841-046A-3C12-B665-74DB9BA26F02
+  Functions: 11294
+  Symbols:   17359
+  CStrings:  8002
 
Symbols:
+ -[AAUIAppleAccountDeferredURL .cxx_destruct]
+ -[AAUIAppleAccountDeferredURL resourcesDictionary]
+ -[AAUIAppleAccountDeferredURL setResourcesDictionary:]
+ -[AAUICDPCustodianHook setIsInternalBuild:]
+ -[AAUICDPCustodianHook setIsOSUpgradeFlow:]
+ -[AAUICustodianSetupFlowController _beginAddRecoveryContactAfterSelectFlow:ifIsVerified:andNoError:]
+ -[AAUICustodianSetupFlowController _beginAddRecoveryContactAfterSelectFlow:ifIsVerified:andNoError:].cold.1
+ GCC_except_table54
+ GCC_except_table65
+ GCC_except_table70
+ GCC_except_table77
+ GCC_except_table82
+ GCC_except_table98
+ _AAUIAppleAccountDeferredURLKey
+ _OBJC_CLASS_$_AAUIAppleAccountDeferredURL
+ _OBJC_IVAR_$_AAUIAppleAccountDeferredURL._resourcesDictionary
+ _OBJC_IVAR_$_AAUICDPCustodianHook._isInternalBuild
+ _OBJC_IVAR_$_AAUICDPCustodianHook._isOSUpgradeFlow
+ _OBJC_METACLASS_$_AAUIAppleAccountDeferredURL
+ __CATEGORY_INSTANCE_METHODS_UIViewController_$_AppleAccountUI
+ __CATEGORY_UIViewController_$_AppleAccountUI
+ __OBJC_$_INSTANCE_METHODS_AAUIAppleAccountDeferredURL
+ __OBJC_$_INSTANCE_METHODS_UINavigationController(AAUIContactSetupNavigationController|AppleAccountUI)
+ __OBJC_$_INSTANCE_VARIABLES_AAUIAppleAccountDeferredURL
+ __OBJC_$_PROP_LIST_AAUIAppleAccountDeferredURL
+ __OBJC_CLASS_RO_$_AAUIAppleAccountDeferredURL
+ __OBJC_METACLASS_RO_$_AAUIAppleAccountDeferredURL
+ __PROTOCOLS_AAUISignInDataclassActionModel.11
+ ___100-[AAUICustodianSetupFlowController _beginAddRecoveryContactAfterSelectFlow:ifIsVerified:andNoError:]_block_invoke
+ ___100-[AAUICustodianSetupFlowController _beginAddRecoveryContactAfterSelectFlow:ifIsVerified:andNoError:]_block_invoke.94
+ ___100-[AAUICustodianSetupFlowController _beginAddRecoveryContactAfterSelectFlow:ifIsVerified:andNoError:]_block_invoke_2
+ ___51-[AAUICustodianSetupFlowController _inviteContact:]_block_invoke.165.cold.1
+ ___51-[AAUICustodianSetupFlowController _inviteContact:]_block_invoke.165.cold.2
+ ___51-[AAUICustodianSetupFlowController _inviteContact:]_block_invoke.165.cold.3
+ ___51-[AAUICustodianSetupFlowController _inviteContact:]_block_invoke.169
+ ___55-[AAUICustodianSetupFlowController _dismissCFUIfNeeded]_block_invoke.178
+ ___55-[AAUICustodianSetupFlowController _dismissCFUIfNeeded]_block_invoke.178.cold.1
+ ___58-[AAUICustodianSetupFlowController _cancelCustodianInvite]_block_invoke.171
+ ___67-[AAUICustodianSetupFlowController _continueAddRecoveryContactFlow]_block_invoke.98
+ ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.100
+ ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.100.cold.1
+ ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.100.cold.2
+ ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.101
+ ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.101.cold.1
+ ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.102
+ ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.102.cold.1
+ ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.103
+ ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.103.cold.1
+ ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.99
+ ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.99.cold.1
+ ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.99.cold.2
+ ___72-[AAUICDPCustodianHook custodianSetupFlowControllerDidFinish:withError:]_block_invoke.73
+ ___72-[AAUICDPCustodianHook custodianSetupFlowControllerDidFinish:withError:]_block_invoke.73.cold.1
+ ___72-[AAUICDPCustodianHook custodianSetupFlowControllerDidFinish:withError:]_block_invoke.73.cold.2
+ ___76-[AAUICustodianSetupFlowController _beginAddRecoveryContactAfterSelectFlow:]_block_invoke.95
+ ___76-[AAUICustodianSetupFlowController _beginAddRecoveryContactAfterSelectFlow:]_block_invoke.95.cold.1
+ ___76-[AAUICustodianSetupFlowController _beginAddRecoveryContactAfterSelectFlow:]_block_invoke.96
+ ___76-[AAUICustodianSetupFlowController _beginAddRecoveryContactAfterSelectFlow:]_block_invoke.97
+ ___76-[AAUICustodianSetupFlowController _beginAddRecoveryContactAfterSelectFlow:]_block_invoke.97.cold.1
+ ___block_descriptor_48_e8_32s40w_e20_v20?0B8"NSError"12lw40l8s32l8
+ ___block_literal_global.180
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyACyACyAA6VStackVyAA9TupleViewVyACy012AppleAccountB0013CustodianIconG0VAA31AccessibilityAttachmentModifierVG_AEyAGyACyAA4TextVALG_APtGGAA012_ConditionalD0VyATyAA05EmptyG0VAEyAGyAA7DividerV_AA10LabelGroupVyAGyAA6HStackVyAGyAO_ATyATyACyACyAA5ImageVAA022_EnvironmentKeyWritingN0VyAA4FontVSgGGA4_yAA5ColorVSgGGACyACyA2_A13_GA8_GGATyA16_AVGGtGG_AOtGGtGGGATyATyA0_yAGyACyACyACyACyAA6ButtonVyAOGAA16_FlexFrameLayoutVGAA016_BackgroundStyleN0VyA11_GGAA11_ClipEffectVyAA16RoundedRectangleVGGAA01_d5ShapeN0VyAA9RectangleVGG_A48_tGGA25_GAEyAGyAX_AZyAGyA0_yAGyAO_A16_tGG_AOtGGtGGGGtGGAA14_PaddingLayoutVGA63_GA63_GA31_GAA0G0HPA66_AAA68_HPA65_AAA68_HPA64_AAA68_HPA61_AAA68_HPyHC_A63_AA0gN0HPyHCHC_A63_AAA69_HPyHCHC_A63_AAA69_HPyHCHC_A31_AAA69_HPyHCHC.32
+ _get_witness_table 7SwiftUI6ButtonVyAA15ModifiedContentVyAEyAA6HStackVyAA9TupleViewVyAA4TextV_AA5ImageVtGGAA30_EnvironmentKeyWritingModifierVyAA4FontVSgGGAQyAA5ColorVSgGGGAA0H0HPyHC.39
+ _get_witness_table 7SwiftUI6HStackVyAA9TupleViewVyAA15ModifiedContentVyAA5ImageVAA12_FrameLayoutVG_AA6SpacerVAA6ButtonVyAGyAGyACyAEyAA4TextV_AItGGAA30_EnvironmentKeyWritingModifierVyAA4FontVSgGGAVyAA5ColorVSgGGGSgtGGAA0E0HPyHC.38
+ _objc_msgSend$_beginAddRecoveryContactAfterSelectFlow:ifIsVerified:andNoError:
+ _objc_msgSend$aaui_pushViewController:animated:
+ _objc_msgSend$aaui_removeLastViewControllerAnimated:
+ _objc_msgSend$aaui_showViewController:sender:
+ _objc_msgSend$isInternalBuild
+ _objc_msgSend$updateTaskResultWithError:
+ _swift_getMetatypeMetadata
+ _symbolic $s14AppleAccountUI24TraitCollectionProvidingP
+ _symbolic $s14AppleAccountUI32SettingsNavigationProxyProvidingP
+ _symbolic So16UIViewControllerCXDXMT
+ _symbolic _____yAAy_____y_____y___________tGG_____y_____SgGGAHy_____SgGG 7SwiftUI15ModifiedContentV AA6HStackV AA9TupleViewV AA4TextV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
+ _symbolic _____y__________G___________yAAyAAy_____y_____y______ABtGG_____y_____SgGGALy_____SgGGGSgt 7SwiftUI15ModifiedContentV AA5ImageV AA12_FrameLayoutV AA6SpacerV AA6ButtonV AA6HStackV AA9TupleViewV AA4TextV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
+ _symbolic _____y___________tG 7SwiftUI9TupleViewV AA4TextV AA5ImageV
+ _symbolic _____y___________y_____y__________G___________yADyADy_____yACy______AEtGG_____y_____SgGGANy_____SgGGGSgtGG 7SwiftUI13_VariadicViewO4TreeV AA13_HStackLayoutV AA05TupleD0V AA15ModifiedContentV AA5ImageV AA06_FrameG0V AA6SpacerV AA6ButtonV AA0F0V AA4TextV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
+ _symbolic _____y_____yABy_____y_____y___________tGG_____y_____SgGGAIy_____SgGGG 7SwiftUI6ButtonV AA15ModifiedContentV AA6HStackV AA9TupleViewV AA4TextV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
+ _symbolic _____y_____yABy_____y_____y___________tGG_____y_____SgGGAIy_____SgGGGSg 7SwiftUI6ButtonV AA15ModifiedContentV AA6HStackV AA9TupleViewV AA4TextV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
+ _symbolic _____y_____y__________G___________yAByABy_____yAAy______ACtGG_____y_____SgGGALy_____SgGGGSgtG 7SwiftUI9TupleViewV AA15ModifiedContentV AA5ImageV AA12_FrameLayoutV AA6SpacerV AA6ButtonV AA6HStackV AA4TextV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
+ _symbolic _____y_____y___________tGG 7SwiftUI6HStackV AA9TupleViewV AA4TextV AA5ImageV
+ _symbolic _____y_____y_____y__________G___________yACyACyAAyABy______ADtGG_____y_____SgGGALy_____SgGGGSgtGG 7SwiftUI6HStackV AA9TupleViewV AA15ModifiedContentV AA5ImageV AA12_FrameLayoutV AA6SpacerV AA6ButtonV AA4TextV AA30_EnvironmentKeyWritingModifierV AA4FontV AA5ColorV
+ _symbolic _____y_____y_____y___________tGG_____y_____SgGG 7SwiftUI15ModifiedContentV AA6HStackV AA9TupleViewV AA4TextV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV
+ _type_layout_string 14AppleAccountUI17CustodianIconViewV
- GCC_except_table33
- GCC_except_table50
- GCC_except_table61
- GCC_except_table73
- GCC_except_table78
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UINavigationController_$_AAUIContactSetupNavigationController
- __PROTOCOLS_AAUISignInDataclassActionModel.9
- ___51-[AAUICustodianSetupFlowController _inviteContact:]_block_invoke.160
- ___51-[AAUICustodianSetupFlowController _inviteContact:]_block_invoke.160.cold.1
- ___51-[AAUICustodianSetupFlowController _inviteContact:]_block_invoke.160.cold.2
- ___51-[AAUICustodianSetupFlowController _inviteContact:]_block_invoke.160.cold.3
- ___55-[AAUICustodianSetupFlowController _dismissCFUIfNeeded]_block_invoke.174
- ___55-[AAUICustodianSetupFlowController _dismissCFUIfNeeded]_block_invoke.174.cold.1
- ___58-[AAUICustodianSetupFlowController _cancelCustodianInvite]_block_invoke.167
- ___67-[AAUICustodianSetupFlowController _continueAddRecoveryContactFlow]_block_invoke.85
- ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.86
- ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.86.cold.1
- ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.86.cold.2
- ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.87
- ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.87.cold.1
- ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.87.cold.2
- ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.88
- ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.88.cold.1
- ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.89
- ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.89.cold.1
- ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.90
- ___70-[AAUICustodianSetupFlowController _beginAddRecoveryContactUpsellFlow]_block_invoke.90.cold.1
- ___72-[AAUICDPCustodianHook custodianSetupFlowControllerDidFinish:withError:]_block_invoke.69
- ___72-[AAUICDPCustodianHook custodianSetupFlowControllerDidFinish:withError:]_block_invoke.69.cold.1
- ___72-[AAUICDPCustodianHook custodianSetupFlowControllerDidFinish:withError:]_block_invoke.69.cold.2
- ___76-[AAUICustodianSetupFlowController _beginAddRecoveryContactAfterSelectFlow:]_block_invoke.82
- ___76-[AAUICustodianSetupFlowController _beginAddRecoveryContactAfterSelectFlow:]_block_invoke.82.cold.1
- ___76-[AAUICustodianSetupFlowController _beginAddRecoveryContactAfterSelectFlow:]_block_invoke.83
- ___76-[AAUICustodianSetupFlowController _beginAddRecoveryContactAfterSelectFlow:]_block_invoke.84
- ___76-[AAUICustodianSetupFlowController _beginAddRecoveryContactAfterSelectFlow:]_block_invoke.84.cold.1
- ___swift_memcpy64_8
- _get_witness_table 7SwiftUI15ModifiedContentVyACyACyACyACyAA6VStackVyAA9TupleViewVyACy012AppleAccountB0013CustodianIconG0VAA31AccessibilityAttachmentModifierVG_AEyAGyACyAA4TextVALG_APtGGAA012_ConditionalD0VyATyAA05EmptyG0VAEyAGyAA7DividerV_AA10LabelGroupVyAGyAA6HStackVyAGyAO_ATyATyACyACyAA5ImageVAA022_EnvironmentKeyWritingN0VyAA4FontVSgGGA4_yAA5ColorVSgGGACyACyA2_A13_GA8_GGATyA16_AVGGtGG_AOtGGtGGGATyATyA0_yAGyACyACyACyACyAA6ButtonVyAOGAA16_FlexFrameLayoutVGAA016_BackgroundStyleN0VyA11_GGAA11_ClipEffectVyAA16RoundedRectangleVGGAA01_d5ShapeN0VyAA9RectangleVGG_A48_tGGA25_GAEyAGyAX_AZyAGyA0_yAGyAO_A16_tGG_AOtGGtGGGGtGGAA14_PaddingLayoutVGA63_GA63_GA31_GA35_GAA0G0HPA67_AAA69_HPA66_AAA69_HPA65_AAA69_HPA64_AAA69_HPA61_AAA69_HPyHC_A63_AA0gN0HPyHCHC_A63_AAA70_HPyHCHC_A63_AAA70_HPyHCHC_A31_AAA70_HPyHCHC_A35_AAA70_HPyHCHC.32
- _get_witness_table 7SwiftUI6HStackVyAA9TupleViewVyAA15ModifiedContentVyAA5ImageVAA12_FrameLayoutVG_AA6SpacerVAA6ButtonVyAA4TextVGtGGAA0E0HPyHC.38
- _symbolic _____yAAyAAyAAyAAy_____y_____yAAy__________G_AByACyAAy_____AEG_AHtGG_____yAKy_____AByACy___________yACy_____yACyAG_AKyAKyAAyAAy__________y_____SgGGAQy_____SgGGAAyAAyApXGATGGAKyA_ALGGtGG_AGtGGtGGGAKyAKyAOyACyAAyAAyAAyAAy_____yAGG_____G_____yAVGG_____y_____GG_____y_____GG_A24_tGGA8_GAByACyAM_ANyACyAOyACyAG_A_tGG_AGtGGtGGGGtGG_____GA38_GA38_GA12_GA15_G 7SwiftUI15ModifiedContentV AA6VStackV AA9TupleViewV 012AppleAccountB0013CustodianIconG0V AA31AccessibilityAttachmentModifierV AA4TextV AA012_ConditionalD0V AA05EmptyG0V AA7DividerV AA10LabelGroupV AA6HStackV AA5ImageV AA022_EnvironmentKeyWritingN0V AA4FontV AA5ColorV AA6ButtonV AA16_FlexFrameLayoutV AA016_BackgroundStyleN0V AA11_ClipEffectV AA16RoundedRectangleV AA01_d5ShapeN0V AA9RectangleV AA14_PaddingLayoutV
- _symbolic _____y__________G___________y_____Gt 7SwiftUI15ModifiedContentV AA5ImageV AA12_FrameLayoutV AA6SpacerV AA6ButtonV AA4TextV
- _symbolic _____y___________y_____y__________G___________y_____GtGG 7SwiftUI13_VariadicViewO4TreeV AA13_HStackLayoutV AA05TupleD0V AA15ModifiedContentV AA5ImageV AA06_FrameG0V AA6SpacerV AA6ButtonV AA4TextV
- _symbolic _____y_____y__________G___________y_____GtG 7SwiftUI9TupleViewV AA15ModifiedContentV AA5ImageV AA12_FrameLayoutV AA6SpacerV AA6ButtonV AA4TextV
- _symbolic _____y_____y_____y__________G___________y_____GtGG 7SwiftUI6HStackV AA9TupleViewV AA15ModifiedContentV AA5ImageV AA12_FrameLayoutV AA6SpacerV AA6ButtonV AA4TextV
CStrings:
+ "%s: navigation controller was nil, unable to show view controller %s"
+ "AAUIAppleAccountDeferredURL"
+ "AAUIAppleAccountDeferredURLKey"
+ "RC_SETUP_UPGRADE_DEVICE_MESSAGE"
+ "SIGN_IN_MERGE_DATACLASS_LINK"
+ "SettingsNavigationProxy available for %s. Using state-driven navigation."
+ "SettingsNavigationProxy not available for %s. Falling back to UIKit navigation."
+ "T@\"NSDictionary\",C,N,V_resourcesDictionary"
+ "_beginAddRecoveryContactAfterSelectFlow:ifIsVerified:andNoError:"
+ "_isInternalBuild"
+ "_isOSUpgradeFlow"
+ "_resourcesDictionary"
+ "aaui_pushViewController:animated:"
+ "aaui_removeLastViewControllerAnimated:"
+ "aaui_showViewController:sender:"
+ "chevron.right"
+ "https://support.apple.com/108306?cid=mc-ols-icloud-article_108306-SigningOut-07092025"
+ "isInternalBuild"
+ "pushViewController"
+ "removeViewController"
+ "resourcesDictionary"
+ "setIsInternalBuild:"
+ "setIsOSUpgradeFlow:"
+ "setResourcesDictionary:"
+ "showViewController"
+ "updateTaskResultWithError:"
- "https://support.apple.com/122682?cid=mc-ols-iCloud-article_122682-SigningOut-04282025"
- "systemGray5Color"

```
