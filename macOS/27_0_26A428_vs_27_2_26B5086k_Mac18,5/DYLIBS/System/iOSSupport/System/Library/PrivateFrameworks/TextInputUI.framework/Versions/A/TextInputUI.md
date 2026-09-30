## TextInputUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/TextInputUI.framework/Versions/A/TextInputUI`

```diff

-9127.0.84.0.0
-  __TEXT.__text: 0x10b188
-  __TEXT.__objc_methlist: 0xf384
-  __TEXT.__const: 0x2e1e
+9127.1.6.0.0
+  __TEXT.__text: 0x11203c
+  __TEXT.__objc_methlist: 0xf49c
+  __TEXT.__const: 0x31de
   __TEXT.__dlopen_cstrs: 0x22c
-  __TEXT.__swift5_typeref: 0x1694
-  __TEXT.__constg_swiftt: 0x13e4
+  __TEXT.__swift5_typeref: 0x1a10
+  __TEXT.__constg_swiftt: 0x1518
   __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_reflstr: 0x7e5
-  __TEXT.__swift5_fieldmd: 0x9cc
-  __TEXT.__swift5_assocty: 0x270
-  __TEXT.__cstring: 0xc8a3
-  __TEXT.__swift5_proto: 0x10c
-  __TEXT.__swift5_types: 0xf8
-  __TEXT.__swift5_capture: 0x434
-  __TEXT.__swift5_protos: 0xc
-  __TEXT.__oslogstring: 0x4c00
+  __TEXT.__swift5_reflstr: 0x895
+  __TEXT.__swift5_fieldmd: 0xac0
+  __TEXT.__swift5_assocty: 0x2c0
+  __TEXT.__cstring: 0xca03
+  __TEXT.__swift5_proto: 0x120
+  __TEXT.__swift5_types: 0x108
+  __TEXT.__oslogstring: 0x4e83
+  __TEXT.__swift5_capture: 0x484
   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__swift_as_cont: 0xcc
   __TEXT.__swift5_mpenum: 0x1c
+  __TEXT.__swift5_protos: 0xc
   __TEXT.__ustring: 0x258
-  __TEXT.__unwind_info: 0x4558
-  __TEXT.__eh_frame: 0x11b4
+  __TEXT.__unwind_info: 0x46c8
+  __TEXT.__eh_frame: 0x11fc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x76e0
-  __DATA_CONST.__objc_classlist: 0x690
+  __DATA_CONST.__const: 0x7760
+  __DATA_CONST.__objc_classlist: 0x698
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9b78
+  __DATA_CONST.__objc_selrefs: 0x9ce0
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0x430
-  __DATA_CONST.__objc_arraydata: 0xa10
-  __DATA_CONST.__got: 0x1280
-  __AUTH_CONST.__const: 0x25a0
-  __AUTH_CONST.__cfstring: 0xe240
-  __AUTH_CONST.__objc_const: 0x18540
+  __DATA_CONST.__objc_superrefs: 0x428
+  __DATA_CONST.__objc_arraydata: 0xa20
+  __DATA_CONST.__got: 0x1350
+  __AUTH_CONST.__const: 0x2770
+  __AUTH_CONST.__cfstring: 0xe360
+  __AUTH_CONST.__objc_const: 0x18700
   __AUTH_CONST.__objc_intobj: 0x360
-  __AUTH_CONST.__objc_arrayobj: 0x258
+  __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_doubleobj: 0x110
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0xe0
-  __AUTH_CONST.__auth_got: 0x1620
-  __AUTH.__objc_data: 0x30f0
-  __AUTH.__data: 0x758
-  __DATA.__objc_ivar: 0x118c
-  __DATA.__data: 0x2478
+  __AUTH_CONST.__auth_got: 0x1780
+  __AUTH.__objc_data: 0x31b0
+  __AUTH.__data: 0x8f8
+  __DATA.__objc_ivar: 0x119c
+  __DATA.__data: 0x2608
   __DATA.__common: 0x168
-  __DATA_DIRTY.__objc_data: 0x20d0
-  __DATA_DIRTY.__data: 0x3c0
+  __DATA_DIRTY.__objc_data: 0x20d8
+  __DATA_DIRTY.__data: 0x3c8
   __DATA_DIRTY.__bss: 0x588
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6234
-  Symbols:   14331
-  CStrings:  2494
+  Functions: 6365
+  Symbols:   14467
+  CStrings:  2513
 
Symbols:
+ +[TUICandidateGrid isFullWidthSuggestionCandidate:]
+ +[TUIKeyplane maxRowsPerKey:variantSelectorType:]
+ +[TUIKeyplane maxVariantsPerRowForKey:layoutStyle:rowLimit:maxRows:]
+ +[TUIKeyplane variantRowLimitForKey:layoutStyle:variantSelectorType:]
+ -[TUICandidateGrid resetContentOffsetIfContentFits]
+ -[TUICandidateGrid showSiriButtonOnLeft]
+ -[TUICandidateGrid showsFullWidthSuggestionCandidate]
+ -[TUICandidateView candidateGroupArrayByRepositioningCompositionCandidates:]
+ -[TUICandidateView candidatesByRepositioningFirstCompositionCandidate:]
+ -[TUIInputSession _shouldUseSecureDisplayForCandidates:withBundleId:usesCandidateSelection:]
+ -[TUIKey updateVariantOrderForMultilineSelectorWithKeyStartingPosition:rowLimit:maxVariantsPerRow:variantCount:]
+ -[TUIKeyPopupView isNarrowLayout]
+ -[TUIKeyPopupView setIsNarrowLayout:]
+ -[TUIKeyplaneRow reservesDockCornerPadding]
+ -[TUIKeyplaneRow setReservesDockCornerPadding:]
+ -[TUIKeyplaneView setSizeClassTraitChangeRegistration:]
+ -[TUIKeyplaneView sizeClassTraitChangeRegistration]
+ -[TUIPredictionViewCell minimumNonClippingWidth]
+ -[TUIPredictionViewStackView _spacingBetweenCells]
+ -[TUIPredictionViewStackView _updateHiddenCellsToFitWidth:]
+ -[TUIPredictionViewStackView fitsCellsToMinimumWidth]
+ -[TUIPredictionViewStackView setFitsCellsToMinimumWidth:]
+ -[TUIVariantSelectorView keyDisplaysNarrowVariants:]
+ -[_TUIKeyboardCandidateContainer _arrayCountOrNilDebugDescription:]
+ OBJC_IVAR_$_TUIKeyPopupView._isNarrowLayout
+ OBJC_IVAR_$_TUIKeyplaneRow._reservesDockCornerPadding
+ OBJC_IVAR_$_TUIKeyplaneView._sizeClassTraitChangeRegistration
+ OBJC_IVAR_$_TUIPredictionViewStackView._fitsCellsToMinimumWidth
+ _CATransform3DMakeScale
+ _OBJC_CLASS_$_CAAnimation
+ _OBJC_CLASS_$_CAPackage
+ _OBJC_CLASS_$_UITraitHorizontalSizeClass
+ _OBJC_CLASS_$_UITraitVerticalSizeClass
+ _OBJC_METACLASS_$__TtC11TextInputUIP33_4E3CCC217D4507E7AD2D9EBD007764CA19GenmojiMicaHostView
+ _UIAccessibilityIsReduceMotionEnabled
+ __DATA__TtC11TextInputUIP33_4E3CCC217D4507E7AD2D9EBD007764CA19GenmojiMicaHostView
+ __INSTANCE_METHODS__TtC11TextInputUIP33_4E3CCC217D4507E7AD2D9EBD007764CA19GenmojiMicaHostView
+ __IVARS__TtC11TextInputUIP33_4E3CCC217D4507E7AD2D9EBD007764CA19GenmojiMicaHostView
+ __METACLASS_DATA__TtC11TextInputUIP33_4E3CCC217D4507E7AD2D9EBD007764CA19GenmojiMicaHostView
+ ___112-[TUIKey updateVariantOrderForMultilineSelectorWithKeyStartingPosition:rowLimit:maxVariantsPerRow:variantCount:]_block_invoke
+ ___112-[TUIKey updateVariantOrderForMultilineSelectorWithKeyStartingPosition:rowLimit:maxVariantsPerRow:variantCount:]_block_invoke_2
+ ___32-[TUIKeyplane buildSplitRowInfo]_block_invoke
+ ___45-[TUIKeyplaneView createContentViewsIfNeeded]_block_invoke_2
+ ___59-[TUIPredictionViewStackView _updateHiddenCellsToFitWidth:]_block_invoke
+ ___92-[TUIInputSession _shouldUseSecureDisplayForCandidates:withBundleId:usesCandidateSelection:]_block_invoke
+ ___92-[TUIInputSession _shouldUseSecureDisplayForCandidates:withBundleId:usesCandidateSelection:]_block_invoke_2
+ ___block_descriptor_32_e23_B32?0"TUIKey"8Q16^B24l
+ ___block_descriptor_40_e23_v32?0"UIView"8Q16^B24l
+ ___block_descriptor_48_e8_q16?0q8l
+ ___block_descriptor_56_e8_q16?0q8l
+ _associated conformance 11TextInputUI20GenmojiAnimatedGlyph33_4E3CCC217D4507E7AD2D9EBD007764CALLV05SwiftC04ViewAA4BodyAeFP_AeF
+ _associated conformance 11TextInputUI22GenmojiButtonAnimationOSHAASQ
+ _associated conformance 11TextInputUI26GenmojiButtonAnimationViewV05SwiftC00G0AA4BodyAdEP_AdE
+ _associated conformance 11TextInputUI26GenmojiButtonAnimationViewV05SwiftC019UIViewRepresentableAaD0G0
+ _kCAPackageTypeCAMLBundle
+ _objc_msgSend$URLForResource:withExtension:
+ _objc_msgSend$URLForResource:withExtension:subdirectory:
+ _objc_msgSend$_arrayCountOrNilDebugDescription:
+ _objc_msgSend$_spacingBetweenCells
+ _objc_msgSend$_updateHiddenCellsToFitWidth:
+ _objc_msgSend$candidateGroupArrayByRepositioningCompositionCandidates:
+ _objc_msgSend$candidatesByRepositioningFirstCompositionCandidate:
+ _objc_msgSend$constraintGreaterThanOrEqualToAnchor:multiplier:constant:
+ _objc_msgSend$fitsCellsToMinimumWidth
+ _objc_msgSend$foreachLayer:
+ _objc_msgSend$hasOnlyProactiveCandidates
+ _objc_msgSend$isChinaPolicyEnabledForMailReply
+ _objc_msgSend$isDecelerating
+ _objc_msgSend$isFullWidthSuggestionCandidate:
+ _objc_msgSend$isGeometryFlipped
+ _objc_msgSend$isNarrowLayout
+ _objc_msgSend$isTracking
+ _objc_msgSend$keyDisplaysNarrowVariants:
+ _objc_msgSend$listWithCorrections:
+ _objc_msgSend$mask
+ _objc_msgSend$maxRowsPerKey:variantSelectorType:
+ _objc_msgSend$maxVariantsPerRowForKey:layoutStyle:rowLimit:maxRows:
+ _objc_msgSend$minimumNonClippingWidth
+ _objc_msgSend$packageWithContentsOfURL:type:options:error:
+ _objc_msgSend$repeatCount
+ _objc_msgSend$reservesDockCornerPadding
+ _objc_msgSend$resetContentOffsetIfContentFits
+ _objc_msgSend$rootLayer
+ _objc_msgSend$setFitsCellsToMinimumWidth:
+ _objc_msgSend$setGeometryFlipped:
+ _objc_msgSend$setIsNarrowLayout:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setReservesDockCornerPadding:
+ _objc_msgSend$setSizeClassTraitChangeRegistration:
+ _objc_msgSend$setSpeed:
+ _objc_msgSend$setTimeOffset:
+ _objc_msgSend$setTypingAttributes:
+ _objc_msgSend$setWithCandidates:proactiveTriggers:
+ _objc_msgSend$showSiriButtonOnLeft
+ _objc_msgSend$showsFullWidthSuggestionCandidate
+ _objc_msgSend$sizeClassTraitChangeRegistration
+ _objc_msgSend$typingAttributes
+ _objc_msgSend$updateVariantOrderForMultilineSelectorWithKeyStartingPosition:rowLimit:maxVariantsPerRow:variantCount:
+ _objc_msgSend$variantRowLimitForKey:layoutStyle:variantSelectorType:
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithTake
+ _swift_dynamicCastClass
+ _swift_getAtKeyPath
+ _swift_getEnumCaseMultiPayload
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_stdlib_random
+ _swift_storeEnumTagMultiPayload
+ _swift_storeEnumTagSinglePayloadGeneric
+ _symbolic $s7SwiftUI19UIViewRepresentableP
+ _symbolic Sd
+ _symbolic Sdz_Xx
+ _symbolic So28TIKeyboardCandidateResultSetC
+ _symbolic So7CALayerCSg
+ _symbolic _____ 11TextInputUI19GenmojiMicaHostView33_4E3CCC217D4507E7AD2D9EBD007764CALLC
+ _symbolic _____ 11TextInputUI20GenmojiAnimatedGlyph33_4E3CCC217D4507E7AD2D9EBD007764CALLV
+ _symbolic _____ 11TextInputUI22GenmojiButtonAnimationO
+ _symbolic _____ 11TextInputUI26GenmojiButtonAnimationViewV
+ _symbolic _____ 7SwiftUI11ColorSchemeO
+ _symbolic _____ s5NeverO
+ _symbolic _____11colorScheme_Sb4boldt 7SwiftUI11ColorSchemeO
+ _symbolic _____11colorScheme_Sb4boldtSg 7SwiftUI11ColorSchemeO
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic _____Sg 11TextInputUI22GenmojiButtonAnimationO
+ _symbolic _____Sg 7SwiftUI11ColorSchemeO
+ _symbolic _____Sg 7SwiftUI16LegibilityWeightO
+ _symbolic _____Sg_ABt 7SwiftUI11ColorSchemeO
+ _symbolic _____Sg_ABt 7SwiftUI16LegibilityWeightO
+ _symbolic _____XMT 11TextInputUI19GenmojiMicaHostView33_4E3CCC217D4507E7AD2D9EBD007764CALLC
+ _symbolic _____yAAyAAy_____y_____y_____yAAy_____y_____SiG_____GAAy_____y______Qo_AHGG______yAAy__________ySiSgGG_Qo_SgQPGG_____GAWGAOy_____GG 7SwiftUI15ModifiedContentV AA6HStackV AA05TupleD0V AA012_ConditionalD0V AA6IDViewV 09TextInputB020GenmojiAnimatedGlyph33_4E3CCC217D4507E7AD2D9EBD007764CALLV AA13_OffsetEffectV AA4ViewPAAE10fontWeightyQrAA4FontV0Z0VSgFQO AA5ImageV AsAEATyQrAYFQO AA0I0V AA30_EnvironmentKeyWritingModifierV AA14_PaddingLayoutV AA15DynamicTypeSizeO
+ _symbolic _____yAAy_____y______Qo______G_____yAAy__________GGG 7SwiftUI15ModifiedContentV AA4ViewPAAE10fontWeightyQrAA4FontV0G0VSgFQO AA5ImageV AA14_OpacityEffectV AA16_OverlayModifierV 09TextInputB0022GenmojiButtonAnimationE0V AA023AccessibilityAttachmentM0V
+ _symbolic _____yAAy_____y_____y_____yAAy_____y_____SiG_____GAAy_____y______Qo_AHGG______yAAy__________ySiSgGG_Qo_SgQPGG_____GAWG 7SwiftUI15ModifiedContentV AA6HStackV AA05TupleD0V AA012_ConditionalD0V AA6IDViewV 09TextInputB020GenmojiAnimatedGlyph33_4E3CCC217D4507E7AD2D9EBD007764CALLV AA13_OffsetEffectV AA4ViewPAAE10fontWeightyQrAA4FontV0Z0VSgFQO AA5ImageV AsAEATyQrAYFQO AA0I0V AA30_EnvironmentKeyWritingModifierV AA14_PaddingLayoutV
+ _symbolic _____ySbG 7SwiftUI7BindingV
+ _symbolic _____ySbG 7SwiftUI9LazyStateV
+ _symbolic _____y_____G 7SwiftUI11EnvironmentV AA11ColorSchemeO
+ _symbolic _____y_____SgG 7SwiftUI11EnvironmentV AA16LegibilityWeightO
+ _symbolic _____y_____Sg_G 7SwiftUI11EnvironmentV7ContentO AA16LegibilityWeightO
+ _symbolic _____y_____SiG 7SwiftUI6IDViewV 09TextInputB020GenmojiAnimatedGlyph33_4E3CCC217D4507E7AD2D9EBD007764CALLV
+ _symbolic _____y______G 7SwiftUI11EnvironmentV7ContentO AA11ColorSchemeO
+ _symbolic _____y___________y_____y_____y_____y_____SiG_____GAEy_____y______Qo_AIGG______yAEy__________ySiSgGG_Qo_SgQPGG 7SwiftUI13_VariadicViewO4TreeV AA13_HStackLayoutV AA12TupleContentV AA012_ConditionalI0V AA08ModifiedI0V AA6IDViewV 09TextInputB020GenmojiAnimatedGlyph33_4E3CCC217D4507E7AD2D9EBD007764CALLV AA13_OffsetEffectV AA0D0PAAE10fontWeightyQrAA4FontV6WeightVSgFQO AA5ImageV AwAEAXyQrA1_FQO AA0M0V AA30_EnvironmentKeyWritingModifierV
+ _symbolic _____y_____y_____SiG_____G 7SwiftUI15ModifiedContentV AA6IDViewV 09TextInputB020GenmojiAnimatedGlyph33_4E3CCC217D4507E7AD2D9EBD007764CALLV AA13_OffsetEffectV
+ _symbolic _____y_____y______Qo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE10fontWeightyQrAA4FontV0G0VSgFQO AA5ImageV AA13_OffsetEffectV
+ _symbolic _____y_____y______Qo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE10fontWeightyQrAA4FontV0G0VSgFQO AA5ImageV AA14_OpacityEffectV
+ _symbolic _____y_____y__________GG 7SwiftUI16_OverlayModifierV AA15ModifiedContentV 09TextInputB026GenmojiButtonAnimationViewV AA023AccessibilityAttachmentD0V
+ _symbolic _____y_____y_____y_____SiG_____GABy_____y______Qo_AFGG 7SwiftUI19_ConditionalContentV AA08ModifiedD0V AA6IDViewV 09TextInputB020GenmojiAnimatedGlyph33_4E3CCC217D4507E7AD2D9EBD007764CALLV AA13_OffsetEffectV AA4ViewPAAE10fontWeightyQrAA4FontV0X0VSgFQO AA5ImageV
+ _symbolic _____y_____y_____y_____SiG_____GABy_____y______Qo_AFGG______yABy__________ySiSgGG_Qo_Sgt 7SwiftUI19_ConditionalContentV AA08ModifiedD0V AA6IDViewV 09TextInputB020GenmojiAnimatedGlyph33_4E3CCC217D4507E7AD2D9EBD007764CALLV AA13_OffsetEffectV AA4ViewPAAE10fontWeightyQrAA4FontV0X0VSgFQO AA5ImageV AoAEAPyQrAUFQO AA0G0V AA30_EnvironmentKeyWritingModifierV
+ _symbolic _____y_____y_____y_____SiG_____GABy_____y______Qo_AFG_G 7SwiftUI19_ConditionalContentV7StorageO AA08ModifiedD0V AA6IDViewV 09TextInputB020GenmojiAnimatedGlyph33_4E3CCC217D4507E7AD2D9EBD007764CALLV AA13_OffsetEffectV AA4ViewPAAE10fontWeightyQrAA4FontV0Y0VSgFQO AA5ImageV
+ _symbolic _____y_____y_____y_____yAAy_____y_____SiG_____GAAy_____y______Qo_AHGG______yAAy__________ySiSgGG_Qo_SgQPGG_____G 7SwiftUI15ModifiedContentV AA6HStackV AA05TupleD0V AA012_ConditionalD0V AA6IDViewV 09TextInputB020GenmojiAnimatedGlyph33_4E3CCC217D4507E7AD2D9EBD007764CALLV AA13_OffsetEffectV AA4ViewPAAE10fontWeightyQrAA4FontV0Z0VSgFQO AA5ImageV AsAEATyQrAYFQO AA0I0V AA30_EnvironmentKeyWritingModifierV AA14_PaddingLayoutV
+ _symbolic _____y_____y_____y_____y_____y_____SiG_____GADy_____y______Qo_AHGG______yADy__________ySiSgGG_Qo_SgQPGG 7SwiftUI6HStackV AA12TupleContentV AA012_ConditionalE0V AA08ModifiedE0V AA6IDViewV 09TextInputB020GenmojiAnimatedGlyph33_4E3CCC217D4507E7AD2D9EBD007764CALLV AA13_OffsetEffectV AA4ViewPAAE10fontWeightyQrAA4FontV0Z0VSgFQO AA5ImageV AsAEATyQrAYFQO AA0I0V AA30_EnvironmentKeyWritingModifierV
+ _symbolic yt
+ _type_layout_string So6CGSizeV
+ get_witness_table 7SwiftUI15ModifiedContentVyACyAA4ViewPAAE10fontWeightyQrAA4FontV0G0VSgFQOyAA5ImageV_Qo_AA14_OpacityEffectVGAA16_OverlayModifierVyACy09TextInputB0022GenmojiButtonAnimationE0VAA023AccessibilityAttachmentM0VGGGAaDHPAqaDHPqd__AaDHD2_ANHO_ApA0eM0HPyHCHC_AzAA0_HPyHCHC
+ get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA6HStackVyAA05TupleD0VyAA012_ConditionalD0VyACyAA6IDViewVy09TextInputB020GenmojiAnimatedGlyph33_4E3CCC217D4507E7AD2D9EBD007764CALLVSiGAA13_OffsetEffectVGACyAA4ViewPAAE10fontWeightyQrAA4FontV0Z0VSgFQOyAA5ImageV_Qo_ARGG_AuAEAVyQrA_FQOyACyAA0I0VAA30_EnvironmentKeyWritingModifierVySiSgGG_Qo_SgQPGGAA14_PaddingLayoutVGA17_GA8_yAA15DynamicTypeSizeOGGAaTHPA19_AaTHPA18_AaTHPA15_AaTHPyHC_A17_AA0X8ModifierHPyHCHC_A17_AAA24_HPyHCHC_A22_AAA24_HPyHCHC
- +[TUIInputSession _shouldUseSecureDisplayForCandidates:withBundleId:usesCandidateSelection:]
- -[TUIFlickVariantCell defaultFontSize]
- -[TUIFlickVariantCell initWithFrame:string:annotation:traits:]
- -[TUIKeyplane variantRowLimitForLayoutWithKey:variantSelectorType:]
- __OBJC_$_CLASS_METHODS_TUIInputSession
- ___92+[TUIInputSession _shouldUseSecureDisplayForCandidates:withBundleId:usesCandidateSelection:]_block_invoke
- ___92+[TUIInputSession _shouldUseSecureDisplayForCandidates:withBundleId:usesCandidateSelection:]_block_invoke_2
- _objc_msgSend$hideInputCandidateView
- _objc_msgSend$variantRowLimitForLayoutWithKey:variantSelectorType:
- _symbolic _____yAAyAAy_____y_____yAAy__________G______yAAy__________ySiSgGG_Qo_SgQPGG_____GAPGAHy_____GG 7SwiftUI15ModifiedContentV AA6HStackV AA05TupleD0V AA5ImageV AA13_OffsetEffectV AA4ViewPAAE10fontWeightyQrAA4FontV0L0VSgFQO AA4TextV AA30_EnvironmentKeyWritingModifierV AA14_PaddingLayoutV AA15DynamicTypeSizeO
- _symbolic _____yAAy_____y_____yAAy__________G______yAAy__________ySiSgGG_Qo_SgQPGG_____GAPG 7SwiftUI15ModifiedContentV AA6HStackV AA05TupleD0V AA5ImageV AA13_OffsetEffectV AA4ViewPAAE10fontWeightyQrAA4FontV0L0VSgFQO AA4TextV AA30_EnvironmentKeyWritingModifierV AA14_PaddingLayoutV
- _symbolic _____y__________G______yAAy__________ySiSgGG_Qo_Sgt 7SwiftUI15ModifiedContentV AA5ImageV AA13_OffsetEffectV AA4ViewPAAE10fontWeightyQrAA4FontV0J0VSgFQO AA4TextV AA30_EnvironmentKeyWritingModifierV
- _symbolic _____y___________y_____y__________G______yADy__________ySiSgGG_Qo_SgQPGG 7SwiftUI13_VariadicViewO4TreeV AA13_HStackLayoutV AA12TupleContentV AA08ModifiedI0V AA5ImageV AA13_OffsetEffectV AA0D0PAAE10fontWeightyQrAA4FontV0O0VSgFQO AA4TextV AA30_EnvironmentKeyWritingModifierV
- _symbolic _____y_____y_____yAAy__________G______yAAy__________ySiSgGG_Qo_SgQPGG_____G 7SwiftUI15ModifiedContentV AA6HStackV AA05TupleD0V AA5ImageV AA13_OffsetEffectV AA4ViewPAAE10fontWeightyQrAA4FontV0L0VSgFQO AA4TextV AA30_EnvironmentKeyWritingModifierV AA14_PaddingLayoutV
- _symbolic _____y_____y_____y__________G______yACy__________ySiSgGG_Qo_SgQPGG 7SwiftUI6HStackV AA12TupleContentV AA08ModifiedE0V AA5ImageV AA13_OffsetEffectV AA4ViewPAAE10fontWeightyQrAA4FontV0L0VSgFQO AA4TextV AA30_EnvironmentKeyWritingModifierV
- _type_layout_string So7CGPointV
- get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA6HStackVyAA05TupleD0VyACyAA5ImageVAA13_OffsetEffectVG_AA4ViewPAAE10fontWeightyQrAA4FontV0L0VSgFQOyACyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGG_Qo_SgQPGGAA14_PaddingLayoutVGA5_GAXyAA15DynamicTypeSizeOGGAaMHPA7_AaMHPA6_AaMHPA3_AaMHPyHC_A5_AA0jR0HPyHCHC_A5_AAA12_HPyHCHC_A10_AAA12_HPyHCHC
CStrings:
+ "%@ {autocorrectionList: %@}"
+ "%@ {candidate resultset: %@}"
+ "%@, predictions: %@, emojis: %@, containsProactiveTriggers: %s, containsAutofillCandidates: %s"
+ "%tu"
+ "(nil)"
+ "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
+ "Allowing smart reply generation without network access for on-device Mail replies"
+ "Autocorrection list contains candidates to be redacted.  Unsupported selector `redactedList`.  Sending empty autocorrection list instead."
+ "B32@?0@\"TUIKey\"8Q16^B24"
+ "Candidate result set contains candidates to be redacted.  Unsupported selector `redactedSet`.  Sending empty result set instead."
+ "KBD returned nil autocorrectionList for request token: %@"
+ "KBD returned nil candidate result set for request token: %@"
+ "Optional<LegibilityWeight>"
+ "Syriac-Diacritics"
+ "Thai-Accents"
+ "autocorrection: %tu, alternate correction: %tu"
+ "candidates: %@, hasOnlyProactiveCandidates: %s"
+ "could not load %{public}s.ca"
+ "q16@?0q8"
```
