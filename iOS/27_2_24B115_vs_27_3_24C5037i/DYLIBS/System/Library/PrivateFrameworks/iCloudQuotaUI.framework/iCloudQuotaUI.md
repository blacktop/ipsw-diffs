## iCloudQuotaUI

> `/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI`

```diff

-301.24.1.5.0
-  __TEXT.__text: 0x15db4c
-  __TEXT.__objc_methlist: 0x9e6c
-  __TEXT.__const: 0xac24
-  __TEXT.__gcc_except_tab: 0xeb8
-  __TEXT.__cstring: 0xae86
-  __TEXT.__oslogstring: 0xbba2
+301.24.2.4.2
+  __TEXT.__text: 0x15f5e8
+  __TEXT.__objc_methlist: 0x9eec
+  __TEXT.__const: 0xad44
+  __TEXT.__gcc_except_tab: 0xf50
+  __TEXT.__cstring: 0xb0d6
+  __TEXT.__oslogstring: 0xc082
   __TEXT.__dlopen_cstrs: 0x691
-  __TEXT.__swift5_typeref: 0x9eec
-  __TEXT.__swift5_reflstr: 0x1af0
-  __TEXT.__swift5_assocty: 0xac0
-  __TEXT.__constg_swiftt: 0x3200
-  __TEXT.__swift5_fieldmd: 0x2358
+  __TEXT.__swift5_typeref: 0x9fee
+  __TEXT.__swift5_reflstr: 0x1b30
+  __TEXT.__swift5_assocty: 0xaf8
+  __TEXT.__constg_swiftt: 0x3224
+  __TEXT.__swift5_fieldmd: 0x2374
   __TEXT.__swift5_capture: 0xcd8
-  __TEXT.__swift5_proto: 0x5e4
-  __TEXT.__swift5_types: 0x2d4
+  __TEXT.__swift5_proto: 0x5ec
+  __TEXT.__swift5_types: 0x2d8
   __TEXT.__swift_as_entry: 0x168
   __TEXT.__swift_as_ret: 0x148
   __TEXT.__swift_as_cont: 0x180
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6f50
+  __TEXT.__unwind_info: 0x6fc8
   __TEXT.__eh_frame: 0x3598
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2738
+  __DATA_CONST.__const: 0x27a0
   __DATA_CONST.__objc_classlist: 0x590
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6bd0
+  __DATA_CONST.__objc_selrefs: 0x6c68
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x578
-  __DATA_CONST.__got: 0x1d68
-  __AUTH_CONST.__const: 0x6b60
-  __AUTH_CONST.__cfstring: 0x8000
+  __DATA_CONST.__got: 0x1d88
+  __AUTH_CONST.__const: 0x6be0
+  __AUTH_CONST.__cfstring: 0x81e0
   __AUTH_CONST.__objc_const: 0x22058
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x2368
+  __AUTH_CONST.__auth_got: 0x2370
   __AUTH.__objc_data: 0x3a38
   __AUTH.__data: 0x25d8
   __DATA.__objc_ivar: 0xbe4

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8072
-  Symbols:   8220
-  CStrings:  2576
+  Functions: 8104
+  Symbols:   8255
+  CStrings:  2606
 
Symbols:
+ +[ICQInAppAlert alertForReason:placement:inOffer:]
+ +[ICQInAppMessage(Examples) _aiMessageWithReason:contentType:title:subTitle:link:]
+ +[ICQInAppMessage(Examples) aiLimitReached]
+ +[ICQInAppMessage(Examples) aiPlanUpgradeRequired]
+ +[ICQInAppMessage(Examples) approachingAILimit]
+ -[ICQInAppAlert initWithOffer:alertKey:pendingItemsCount:albumName:]
+ -[ICQInAppMessaging _actionsForBannerSpecification:offer:pendingItemsCount:albumName:]
+ -[ICQInAppMessaging _fetchSharedAlbumMessageForReason:placement:pendingItemsCount:albumName:completion:]
+ -[ICQInAppMessaging aiMessageForReason:defaultOffer:]
+ -[ICQInAppMessaging fetchMessageForReason:placement:pendingItemsCount:albumName:withCompletion:]
+ -[ICQInAppMessaging fetchMessageWithPlacement:pendingItemsCount:albumName:completion:]
+ -[ICQInAppMessaging sharedAlbumMessageForOffer:placement:pendingItemsCount:albumName:]
+ -[ICQInternetPrivacyDetailSpecifierProvider presentPrivateRelayPrivacy]
+ -[ICQLinkInAppAction addAlertFromLink:offer:pendingItemsCount:albumName:]
+ -[ICQLinkInAppAction initWithLink:inOffer:pendingItemsCount:albumName:]
+ GCC_except_table28
+ GCC_except_table47
+ GCC_except_table75
+ GCC_except_table87
+ _AAUIDataclassAttributedLinkAction
+ _ICQUIInAppMessageReasonAILimitReached
+ _ICQUIInAppMessageReasonAIPlanUpgradeRequired
+ _ICQUIInAppMessageReasonApproachingAILimit
+ _NSStringFromSelector
+ _OBJC_CLASS_$_OBBundle
+ _OBJC_CLASS_$_OBPrivacyLinkController
+ _OBJC_CLASS_$_OBPrivacyPresenter
+ __ICQIsAIReason
+ ___104-[ICQInAppMessaging _fetchSharedAlbumMessageForReason:placement:pendingItemsCount:albumName:completion:]_block_invoke
+ ___62-[ICQInAppMessaging fetchAlertForReason:placement:completion:]_block_invoke
+ ___68-[ICQInAppAlert initWithOffer:alertKey:pendingItemsCount:albumName:]_block_invoke
+ ___68-[ICQInAppAlert initWithOffer:alertKey:pendingItemsCount:albumName:]_block_invoke_2
+ ___74-[ICQInAppMessaging uploadFailureMessageForPendingItemCount:defaultOffer:]_block_invoke
+ ___74-[ICQInAppMessaging uploadFailureMessageForPendingItemCount:defaultOffer:]_block_invoke_2
+ ___86-[ICQInAppMessaging sharedAlbumMessageForOffer:placement:pendingItemsCount:albumName:]_block_invoke
+ ___86-[ICQInAppMessaging sharedAlbumMessageForOffer:placement:pendingItemsCount:albumName:]_block_invoke_2
+ ___86-[ICQInAppMessaging sharedAlbumMessageForOffer:placement:pendingItemsCount:albumName:]_block_invoke_3
+ ___block_descriptor_40_e8_32s_e28_"NSString"16?0"NSString"8ls32l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ _associated conformance 13iCloudQuotaUI25AboutPrivateRelayLinkView33_B1AE8FEA7473F77196D422B62389E5ADLLV05SwiftC00H0AA4BodyAeFP_AeF
+ _associated conformance 13iCloudQuotaUI25AboutPrivateRelayLinkView33_B1AE8FEA7473F77196D422B62389E5ADLLV05SwiftC029UIViewControllerRepresentableAaE0H0
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyAA6ToggleVyAA6HStackVyAA05TupleD0VyAA5ImageV_AA6VStackVyAIyAGyAIyACyACyAA6CircleVAA12_FrameLayoutVGAA30_EnvironmentKeyWritingModifierVyAA5ColorVSgGG_AA4TextVQPGG_A_AA012_ConditionalD0VyACy011iCloudQuotaB025AboutPrivateRelayLinkView33_B1AE8FEA7473F77196D422B62389E5ADLLVAA010_FixedSizeL0VGA_GACyACyACyA_ATyAA19SymbolRenderingModeVSgGGAA016_ForegroundStyleP0VyAA22HierarchicalShapeStyleVGGATyAA4FontVSgGGSgQPGGQPGGGAA023AccessibilityAttachmentP0VGAA01_mn9TransformP0VySbGGAA0Z0HPA36_AAA41_HPA33_AAA41_HPyHC_A35_AA0zP0HPyHCHC_A39_AAA42_HPyHCHC
+ _symbolic So23OBPrivacyLinkControllerC
+ _symbolic _____ 13iCloudQuotaUI25AboutPrivateRelayLinkView33_B1AE8FEA7473F77196D422B62389E5ADLLV
+ _symbolic ___________y_____y_____yACy_____yAEy__________G_____y_____SgGG______QPGG_AN_____yAEy__________GANGAEyAEyAEyAnIy_____SgGG_____y_____GGAIy_____SgGGSgQPGGt 7SwiftUI5ImageV AA6VStackV AA12TupleContentV AA6HStackV AA08ModifiedF0V AA6CircleV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA012_ConditionalF0V 011iCloudQuotaB025AboutPrivateRelayLinkView33_B1AE8FEA7473F77196D422B62389E5ADLLV AA010_FixedSizeK0V AA19SymbolRenderingModeV AA016_ForegroundStyleO0V AA22HierarchicalShapeStyleV AA4FontV
+ _symbolic _____yAAy_____y_____y_____y___________yADyACyADyAAyAAy__________G_____y_____SgGG______QPGG_AO_____yAAy__________GAOGAAyAAyAAyAoJy_____SgGG_____y_____GGAJy_____SgGGSgQPGGQPGGG_____G_____ySbGG 7SwiftUI15ModifiedContentV AA6ToggleV AA6HStackV AA05TupleD0V AA5ImageV AA6VStackV AA6CircleV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA012_ConditionalD0V 011iCloudQuotaB025AboutPrivateRelayLinkView33_B1AE8FEA7473F77196D422B62389E5ADLLV AA010_FixedSizeL0V AA19SymbolRenderingModeV AA016_ForegroundStyleP0V AA22HierarchicalShapeStyleV AA4FontV AA023AccessibilityAttachmentP0V AA01_mn9TransformP0V
+ _symbolic _____y___________y___________yACy_____yACy_____yAGy__________G_____y_____SgGG______QPGG_AP_____yAGy__________GAPGAGyAGyAGyApKy_____SgGG_____y_____GGAKy_____SgGGSgQPGGQPGG 7SwiftUI13_VariadicViewO4TreeV AA13_HStackLayoutV AA12TupleContentV AA5ImageV AA6VStackV AA0F0V AA08ModifiedI0V AA6CircleV AA06_FrameG0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA012_ConditionalI0V 011iCloudQuotaB0021AboutPrivateRelayLinkD033_B1AE8FEA7473F77196D422B62389E5ADLLV AA010_FixedSizeG0V AA19SymbolRenderingModeV AA016_ForegroundStyleR0V AA22HierarchicalShapeStyleV AA4FontV
+ _symbolic _____y___________y_____yACy_____yAEy__________G_____y_____SgGG______QPGG_AN_____yAEy__________GANGAEyAEyAEyAnIy_____SgGG_____y_____GGAIy_____SgGGSgQPGG 7SwiftUI13_VariadicViewO4TreeV AA13_VStackLayoutV AA12TupleContentV AA6HStackV AA08ModifiedI0V AA6CircleV AA06_FrameG0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA012_ConditionalI0V 011iCloudQuotaB0021AboutPrivateRelayLinkD033_B1AE8FEA7473F77196D422B62389E5ADLLV AA010_FixedSizeG0V AA19SymbolRenderingModeV AA016_ForegroundStyleQ0V AA22HierarchicalShapeStyleV AA4FontV
+ _symbolic _____y_____y___________yAByAAyABy_____yAEy__________G_____y_____SgGG______QPGG_AN_____yAEy__________GANGAEyAEyAEyAnIy_____SgGG_____y_____GGAIy_____SgGGSgQPGGQPGG 7SwiftUI6HStackV AA12TupleContentV AA5ImageV AA6VStackV AA08ModifiedE0V AA6CircleV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA012_ConditionalE0V 011iCloudQuotaB025AboutPrivateRelayLinkView33_B1AE8FEA7473F77196D422B62389E5ADLLV AA010_FixedSizeK0V AA19SymbolRenderingModeV AA016_ForegroundStyleO0V AA22HierarchicalShapeStyleV AA4FontV
+ _symbolic _____y_____y_____yABy_____yADy__________G_____y_____SgGG______QPGG_AM_____yADy__________GAMGADyADyADyAmHy_____SgGG_____y_____GGAHy_____SgGGSgQPGG 7SwiftUI6VStackV AA12TupleContentV AA6HStackV AA08ModifiedE0V AA6CircleV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA012_ConditionalE0V 011iCloudQuotaB025AboutPrivateRelayLinkView33_B1AE8FEA7473F77196D422B62389E5ADLLV AA010_FixedSizeJ0V AA19SymbolRenderingModeV AA016_ForegroundStyleN0V AA22HierarchicalShapeStyleV AA4FontV
+ _symbolic _____y_____y_____yACy__________G_____y_____SgGG______QPGG_AL_____yACy__________GALGACyACyACyAlGy_____SgGG_____y_____GGAGy_____SgGGSgt 7SwiftUI6HStackV AA12TupleContentV AA08ModifiedE0V AA6CircleV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA012_ConditionalE0V 011iCloudQuotaB025AboutPrivateRelayLinkView33_B1AE8FEA7473F77196D422B62389E5ADLLV AA010_FixedSizeI0V AA19SymbolRenderingModeV AA016_ForegroundStyleM0V AA22HierarchicalShapeStyleV AA4FontV
+ _symbolic _____y_____y_____y___________yACyAByACy_____yAFy__________G_____y_____SgGG______QPGG_AO_____yAFy__________GAOGAFyAFyAFyAoJy_____SgGG_____y_____GGAJy_____SgGGSgQPGGQPGGG 7SwiftUI6ToggleV AA6HStackV AA12TupleContentV AA5ImageV AA6VStackV AA08ModifiedF0V AA6CircleV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA012_ConditionalF0V 011iCloudQuotaB025AboutPrivateRelayLinkView33_B1AE8FEA7473F77196D422B62389E5ADLLV AA010_FixedSizeL0V AA19SymbolRenderingModeV AA016_ForegroundStyleP0V AA22HierarchicalShapeStyleV AA4FontV
+ _symbolic _____y_____y_____y_____y___________yADyACyADyAAyAAy__________G_____y_____SgGG______QPGG_AO_____yAAy__________GAOGAAyAAyAAyAoJy_____SgGG_____y_____GGAJy_____SgGGSgQPGGQPGGG_____G 7SwiftUI15ModifiedContentV AA6ToggleV AA6HStackV AA05TupleD0V AA5ImageV AA6VStackV AA6CircleV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA012_ConditionalD0V 011iCloudQuotaB025AboutPrivateRelayLinkView33_B1AE8FEA7473F77196D422B62389E5ADLLV AA010_FixedSizeL0V AA19SymbolRenderingModeV AA016_ForegroundStyleP0V AA22HierarchicalShapeStyleV AA4FontV AA023AccessibilityAttachmentP0V
+ _type_layout_string 13iCloudQuotaUI25AboutPrivateRelayLinkView33_B1AE8FEA7473F77196D422B62389E5ADLLV
- -[ICQInAppMessaging _actionsForBannerSpecification:offer:pendingItemsCount:]
- -[ICQInAppMessaging _fetchSharedAlbumMessageForReason:placement:pendingItemsCount:completion:]
- -[ICQInAppMessaging sharedAlbumMessageForOffer:placement:pendingItemsCount:]
- -[ICQLinkInAppAction addAlertFromLink:offer:pendingItemsCount:]
- GCC_except_table26
- GCC_except_table54
- GCC_except_table66
- ___60-[ICQInternetPrivacyDetailSpecifierProvider _switchOffAlert]_block_invoke_3
- ___94-[ICQInAppMessaging _fetchSharedAlbumMessageForReason:placement:pendingItemsCount:completion:]_block_invoke
- _get_witness_table 7SwiftUI15ModifiedContentVyACyAA6ToggleVyAA6HStackVyAA05TupleD0VyAA5ImageV_AA6VStackVyAIyAGyAIyACyACyAA6CircleVAA12_FrameLayoutVGAA30_EnvironmentKeyWritingModifierVyAA5ColorVSgGG_AA4TextVQPGG_A_A_ACyACyACyA_ATyAA19SymbolRenderingModeVSgGGAA016_ForegroundStyleP0VyAA017HierarchicalShapeW0VGGATyAA4FontVSgGGSgQPGGQPGGGAA023AccessibilityAttachmentP0VGAA01_mn9TransformP0VySbGGAA4ViewHPA26_AAA31_HPA23_AAA31_HPyHC_A25_AA04ViewP0HPyHCHC_A29_AAA32_HPyHCHC
- _symbolic ___________y_____y_____yACy_____yAEy__________G_____y_____SgGG______QPGG_A2nEyAEyAEyAnIy_____SgGG_____y_____GGAIy_____SgGGSgQPGGt 7SwiftUI5ImageV AA6VStackV AA12TupleContentV AA6HStackV AA08ModifiedF0V AA6CircleV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA19SymbolRenderingModeV AA016_ForegroundStyleO0V AA017HierarchicalShapeV0V AA4FontV
- _symbolic _____yAAy_____y_____y_____y___________yADyACyADyAAyAAy__________G_____y_____SgGG______QPGG_A2oAyAAyAAyAoJy_____SgGG_____y_____GGAJy_____SgGGSgQPGGQPGGG_____G_____ySbGG 7SwiftUI15ModifiedContentV AA6ToggleV AA6HStackV AA05TupleD0V AA5ImageV AA6VStackV AA6CircleV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA19SymbolRenderingModeV AA016_ForegroundStyleP0V AA017HierarchicalShapeW0V AA4FontV AA023AccessibilityAttachmentP0V AA01_mn9TransformP0V
- _symbolic _____y___________y___________yACy_____yACy_____yAGy__________G_____y_____SgGG______QPGG_A2pGyAGyAGyApKy_____SgGG_____y_____GGAKy_____SgGGSgQPGGQPGG 7SwiftUI13_VariadicViewO4TreeV AA13_HStackLayoutV AA12TupleContentV AA5ImageV AA6VStackV AA0F0V AA08ModifiedI0V AA6CircleV AA06_FrameG0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA19SymbolRenderingModeV AA016_ForegroundStyleR0V AA017HierarchicalShapeY0V AA4FontV
- _symbolic _____y___________y_____yACy_____yAEy__________G_____y_____SgGG______QPGG_A2nEyAEyAEyAnIy_____SgGG_____y_____GGAIy_____SgGGSgQPGG 7SwiftUI13_VariadicViewO4TreeV AA13_VStackLayoutV AA12TupleContentV AA6HStackV AA08ModifiedI0V AA6CircleV AA06_FrameG0V AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA19SymbolRenderingModeV AA016_ForegroundStyleQ0V AA017HierarchicalShapeX0V AA4FontV
- _symbolic _____y_____y___________yAByAAyABy_____yAEy__________G_____y_____SgGG______QPGG_A2nEyAEyAEyAnIy_____SgGG_____y_____GGAIy_____SgGGSgQPGGQPGG 7SwiftUI6HStackV AA12TupleContentV AA5ImageV AA6VStackV AA08ModifiedE0V AA6CircleV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA19SymbolRenderingModeV AA016_ForegroundStyleO0V AA017HierarchicalShapeV0V AA4FontV
- _symbolic _____y_____y_____yABy_____yADy__________G_____y_____SgGG______QPGG_A2mDyADyADyAmHy_____SgGG_____y_____GGAHy_____SgGGSgQPGG 7SwiftUI6VStackV AA12TupleContentV AA6HStackV AA08ModifiedE0V AA6CircleV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA19SymbolRenderingModeV AA016_ForegroundStyleN0V AA017HierarchicalShapeU0V AA4FontV
- _symbolic _____y_____y_____yACy__________G_____y_____SgGG______QPGG_A2lCyACyACyAlGy_____SgGG_____y_____GGAGy_____SgGGSgt 7SwiftUI6HStackV AA12TupleContentV AA08ModifiedE0V AA6CircleV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA19SymbolRenderingModeV AA016_ForegroundStyleM0V AA017HierarchicalShapeT0V AA4FontV
- _symbolic _____y_____y_____y___________yACyAByACy_____yAFy__________G_____y_____SgGG______QPGG_A2oFyAFyAFyAoJy_____SgGG_____y_____GGAJy_____SgGGSgQPGGQPGGG 7SwiftUI6ToggleV AA6HStackV AA12TupleContentV AA5ImageV AA6VStackV AA08ModifiedF0V AA6CircleV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA19SymbolRenderingModeV AA016_ForegroundStyleP0V AA017HierarchicalShapeW0V AA4FontV
- _symbolic _____y_____y_____y_____y___________yADyACyADyAAyAAy__________G_____y_____SgGG______QPGG_A2oAyAAyAAyAoJy_____SgGG_____y_____GGAJy_____SgGGSgQPGGQPGGG_____G 7SwiftUI15ModifiedContentV AA6ToggleV AA6HStackV AA05TupleD0V AA5ImageV AA6VStackV AA6CircleV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA5ColorV AA4TextV AA19SymbolRenderingModeV AA016_ForegroundStyleP0V AA017HierarchicalShapeW0V AA4FontV AA023AccessibilityAttachmentP0V
CStrings:
+ "%s Using mock offer"
+ "-[ICQInAppMessaging fetchAlertForReason:placement:completion:]_block_invoke"
+ "@\"NSString\"16@?0@\"NSString\"8"
+ "AILimitReached"
+ "AIPlanUpgradeRequired"
+ "ApproachingAILimit"
+ "Learn More"
+ "No %{public}@ message for bundle %{public}@ in default offer %{public}@"
+ "OBBundle returned no localizedButtonTitle for %{public}s; falling back to the hardcoded About Private Relay link"
+ "OBPrivacyLinkController returned no localizedButtonTitle for %@; falling back to the hardcoded About Private Relay link"
+ "Offer %{public}@ has no inlineAlertInfo entry for alertKey: %{public}@"
+ "Presenting Private Relay privacy splash"
+ "Returning %{public}@ server message for bundle %{public}@ (default offer: %{public}@)"
+ "Returning icqctl override message for reason %{public}@ to bundle %{public}@"
+ "Shared Collections: fetchMessageForReason:placement:pendingItemsCount:albumName: called with reason: %@, placement: %@, count: %@, albumName: %{private}@"
+ "Unable to find in-app message for reason %{public}@"
+ "Upgrade"
+ "Upgrade to iCloud+ to use this feature."
+ "You're approaching your daily limit."
+ "You've reached your daily limit. Upgrade to iCloud+ for higher limits."
+ "[icqctl] Approaching Daily Limit"
+ "[icqctl] Daily Limit Reached"
+ "[icqctl] Upgrade to iCloud+"
+ "com.apple.onboarding.privaterelay"
+ "fetchAlertForReason:%{public}@ placement:%{public}@ found no alert for bundle %{public}@ in regular offer %{public}@ or default offer %{public}@"
+ "fetchAlertForReason:%{public}@ placement:%{public}@ has no offers loaded for bundle %{public}@ (observing: %{public}@)"
+ "fetchAlertForReason:%{public}@ placement:%{public}@ returning alert from offer %{public}@: %@"
+ "fetchMessageForReason:%{public}@ for bundle %{public}@ (observing: %{public}@, default offer: %{public}@)"
+ "fetchMessageWithPlacement:pendingItemsCount:albumName: called with placement: %@, count: %@, albumName: %{private}@"
+ "https://icq.icloud.com?context=test&universalLinkAction=LAUNCH_CLOUD_FM"
+ "https://icq.icloud.com?context=test&universalLinkAction=default"
+ "https://support.apple.com/127901"
+ "none"
- "INTERNET_PRIVACY_OPEN_SYSTEM_STATUS_BUTTON_TITLE"
- "Unable to find in-app message for reason %@"
- "fetchAlertForReason:%{public}@ placement:%{public}@ not yet implemented, returning unavailable error."
```
