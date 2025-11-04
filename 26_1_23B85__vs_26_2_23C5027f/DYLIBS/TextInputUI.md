## TextInputUI

> `/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI`

```diff

-9126.1.12.1.105
-  __TEXT.__text: 0xd22c0
-  __TEXT.__auth_stubs: 0x2a50
-  __TEXT.__objc_methlist: 0xc08c
-  __TEXT.__const: 0x2030
+9126.2.2.0.0
+  __TEXT.__text: 0xd6508
+  __TEXT.__auth_stubs: 0x2bc0
+  __TEXT.__objc_methlist: 0xc234
+  __TEXT.__const: 0x2170
   __TEXT.__dlopen_cstrs: 0x1c4
-  __TEXT.__cstring: 0x9fef
+  __TEXT.__cstring: 0xa162
   __TEXT.__swift5_typeref: 0xe7a
-  __TEXT.__oslogstring: 0x2a80
-  __TEXT.__swift5_capture: 0x258
-  __TEXT.__constg_swiftt: 0xa58
-  __TEXT.__swift5_reflstr: 0x403
-  __TEXT.__swift5_fieldmd: 0x454
+  __TEXT.__oslogstring: 0x2b73
+  __TEXT.__swift5_capture: 0x2a8
+  __TEXT.__constg_swiftt: 0xb44
+  __TEXT.__swift5_reflstr: 0x468
+  __TEXT.__swift5_fieldmd: 0x4cc
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_assocty: 0x158
-  __TEXT.__swift5_proto: 0x7c
-  __TEXT.__swift5_types: 0x70
-  __TEXT.__swift_as_entry: 0x30
+  __TEXT.__swift5_assocty: 0x170
+  __TEXT.__swift5_proto: 0x80
+  __TEXT.__swift5_types: 0x7c
+  __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x34
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__ustring: 0x78
-  __TEXT.__unwind_info: 0x2cc8
-  __TEXT.__eh_frame: 0xaec
-  __TEXT.__objc_classname: 0x1546
-  __TEXT.__objc_methname: 0x22ea6
-  __TEXT.__objc_methtype: 0x4ebf
-  __TEXT.__objc_stubs: 0x1b520
-  __DATA_CONST.__got: 0x1140
+  __TEXT.__unwind_info: 0x2dd0
+  __TEXT.__eh_frame: 0xc6c
+  __TEXT.__objc_classname: 0x155a
+  __TEXT.__objc_methname: 0x23131
+  __TEXT.__objc_methtype: 0x4edc
+  __TEXT.__objc_stubs: 0x1b680
+  __DATA_CONST.__got: 0x1178
   __DATA_CONST.__const: 0x7200
-  __DATA_CONST.__objc_classlist: 0x510
+  __DATA_CONST.__objc_classlist: 0x528
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8418
+  __DATA_CONST.__objc_selrefs: 0x84a8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x358
+  __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x568
-  __AUTH_CONST.__auth_got: 0x1530
-  __AUTH_CONST.__const: 0x1510
-  __AUTH_CONST.__cfstring: 0xb520
-  __AUTH_CONST.__objc_const: 0x130b8
-  __AUTH_CONST.__objc_intobj: 0x330
+  __AUTH_CONST.__auth_got: 0x15e8
+  __AUTH_CONST.__const: 0x1608
+  __AUTH_CONST.__cfstring: 0xb5e0
+  __AUTH_CONST.__objc_const: 0x13328
+  __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0xe0
-  __AUTH.__objc_data: 0x1ef0
-  __AUTH.__data: 0x580
-  __DATA.__objc_ivar: 0xe70
-  __DATA.__data: 0x1860
-  __DATA.__bss: 0x15b8
-  __DATA.__common: 0x148
+  __AUTH.__objc_data: 0x2110
+  __AUTH.__data: 0x5d0
+  __DATA.__objc_ivar: 0xe74
+  __DATA.__data: 0x18d0
+  __DATA.__bss: 0x1638
+  __DATA.__common: 0x168
   __DATA_DIRTY.__objc_data: 0x19f0
   __DATA_DIRTY.__data: 0xd8
   __DATA_DIRTY.__bss: 0x100

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/Calculate.framework/Calculate
+  - /System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji
   - /System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG
   - /System/Library/PrivateFrameworks/DefaultAppsSettings.framework/DefaultAppsSettings
   - /System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7285463D-8BA8-3FAF-B920-8A4F634925FE
-  Functions: 4715
-  Symbols:   15917
-  CStrings:  9980
+  UUID: 3F1438F3-9C27-3454-BC56-A97B7973B386
+  Functions: 4811
+  Symbols:   16016
+  CStrings:  10025
 
Symbols:
+ +[TUIGenmojiCreation showGenmojiCreationForCurrentResponderWithInputString:]
+ +[TUIInputAnalytics getIAChannelCandidateBar]
+ +[TUIInputAnalytics getIASignalCandidateBarMixmojiCombineButtonPressed]
+ +[TUIInputAnalytics getIASignalCandidateBarMixmojiCombineButtonShown]
+ +[TUIInputAnalytics sendCandidateBarSignal:threadId:payload:]
+ +[TUIMixmojiCandidate supportsSecureCoding]
+ -[TUIKeyboardCandidateMultiplexer _sendMixmojiTelemetryForCandidates:forKeyboardState:]
+ -[TUIMixmojiCandidate action]
+ -[TUIMixmojiCandidate alternativeText]
+ -[TUIMixmojiCandidate copyWithZone:]
+ -[TUIMixmojiCandidate description]
+ -[TUIMixmojiCandidate encodeWithCoder:]
+ -[TUIMixmojiCandidate hash]
+ -[TUIMixmojiCandidate initWithCoder:]
+ -[TUIMixmojiCandidate initWithInput:]
+ -[TUIMixmojiCandidate isEqual:]
+ -[TUIMixmojiCandidate label]
+ -[TUIMixmojiCandidate title]
+ -[TUIPredictionViewCell _isMixmojiCandidate:]
+ -[TUIPredictionViewCell _setMixmojiCandidate:animated:]
+ -[TUIPredictionViewCell mixmojiContentView]
+ -[TUIPredictionViewCell setMixmojiContentView:]
+ _CEMEmojiTokenCreateCopyRemovingModifiers
+ _CEMEmojiTokenGetString
+ _EMFEmojiCategoryFlags
+ _OBJC_CLASS_$_EMFEmojiToken
+ _OBJC_CLASS_$_TUIMixmojiCandidate
+ _OBJC_CLASS_$_TUIMixmojiCandidateGenerator
+ _OBJC_CLASS_$_TUIMixmojiCellContentView
+ _OBJC_IVAR_$_TUIPredictionViewCell._mixmojiContentView
+ _OBJC_METACLASS_$_TUIMixmojiCandidate
+ _OBJC_METACLASS_$_TUIMixmojiCandidateGenerator
+ _OBJC_METACLASS_$_TUIMixmojiCellContentView
+ _UIKitLibrary.2873
+ _UIKitLibraryCore.frameworkLibrary.2876
+ _UIKitLibraryCore.frameworkLibrary.3565
+ __DATA_TUIMixmojiCandidateGenerator
+ __DATA_TUIMixmojiCellContentView
+ __INSTANCE_METHODS_TUIMixmojiCandidateGenerator
+ __INSTANCE_METHODS_TUIMixmojiCellContentView
+ __IVARS_TUIMixmojiCandidateGenerator
+ __IVARS_TUIMixmojiCellContentView
+ __METACLASS_DATA_TUIMixmojiCandidateGenerator
+ __METACLASS_DATA_TUIMixmojiCellContentView
+ __OBJC_$_CLASS_METHODS_TUIMixmojiCandidate
+ __OBJC_$_CLASS_PROP_LIST_TUIMixmojiCandidate
+ __OBJC_$_INSTANCE_METHODS_TUIMixmojiCandidate
+ __OBJC_CLASS_PROTOCOLS_$_TUIMixmojiCandidate
+ __OBJC_CLASS_RO_$_TUIMixmojiCandidate
+ __OBJC_METACLASS_RO_$_TUIMixmojiCandidate
+ __PROPERTIES_TUIMixmojiCandidateGenerator
+ __PROTOCOLS_TUIMixmojiCandidateGenerator
+ __PROTOCOLS_TUIMixmojiCandidateGenerator.3
+ __TUIKeyboardTrackingLogger.8534
+ __TUIKeyboardTrackingLogger.log.8539
+ __TUIKeyboardTrackingLogger.onceToken.8537
+ ___Block_byref_object_copy_.12764
+ ___Block_byref_object_copy_.2031
+ ___Block_byref_object_copy_.2870
+ ___Block_byref_object_copy_.3321
+ ___Block_byref_object_copy_.5499
+ ___Block_byref_object_copy_.8280
+ ___Block_byref_object_copy_.9867
+ ___Block_byref_object_dispose_.12765
+ ___Block_byref_object_dispose_.2032
+ ___Block_byref_object_dispose_.2871
+ ___Block_byref_object_dispose_.3322
+ ___Block_byref_object_dispose_.5500
+ ___Block_byref_object_dispose_.8281
+ ___Block_byref_object_dispose_.9868
+ ___UIKitLibraryCore_block_invoke.2877
+ ___UIKitLibraryCore_block_invoke.3566
+ ____TUIKeyboardTrackingLogger_block_invoke.8542
+ ___block_literal_global.10.10817
+ ___block_literal_global.10504
+ ___block_literal_global.10822
+ ___block_literal_global.11008
+ ___block_literal_global.11342
+ ___block_literal_global.11497
+ ___block_literal_global.11770
+ ___block_literal_global.12774
+ ___block_literal_global.13015
+ ___block_literal_global.13468
+ ___block_literal_global.18.8335
+ ___block_literal_global.1858
+ ___block_literal_global.20.9428
+ ___block_literal_global.20.9966
+ ___block_literal_global.2062
+ ___block_literal_global.22.9430
+ ___block_literal_global.2535
+ ___block_literal_global.2806
+ ___block_literal_global.2914
+ ___block_literal_global.2992
+ ___block_literal_global.3176
+ ___block_literal_global.3323
+ ___block_literal_global.3818
+ ___block_literal_global.4.13038
+ ___block_literal_global.4080
+ ___block_literal_global.4263
+ ___block_literal_global.43.2515
+ ___block_literal_global.4479
+ ___block_literal_global.495
+ ___block_literal_global.5337
+ ___block_literal_global.6.11010
+ ___block_literal_global.61.13013
+ ___block_literal_global.6677
+ ___block_literal_global.6798
+ ___block_literal_global.7058
+ ___block_literal_global.7325
+ ___block_literal_global.7721
+ ___block_literal_global.7891
+ ___block_literal_global.8339
+ ___block_literal_global.8538
+ ___block_literal_global.8740
+ ___block_literal_global.9159
+ ___block_literal_global.9341
+ ___block_literal_global.9421
+ ___block_literal_global.9503
+ ___block_literal_global.9876
+ ___block_literal_global.9969
+ ___unnamed_4
+ __swiftEmptySetSingleton
+ _associated conformance 11TextInputUI12GenmojiLabelV05SwiftC04ViewAA4BodyAdEP_AdE
+ _audit_stringUIKit.2880
+ _audit_stringUIKit.3571
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyAA014_ViewModifier_D0Vy09TextInputB023IntelligenceLightEffect33_4E3CCC217D4507E7AD2D9EBD007764CALLVGAA08_OpacityK0VGAA011_BackgroundF0VyACyACyACyACyACyACyACyACyAA5ImageVAA18_AspectRatioLayoutVGAA06_ScaleK0VGAA09_RotationK0VGAA010_AnimationF0VySbGGAA017_AppearanceActionF0VGAA010_BlendModeK0VGAA023AccessibilityAttachmentF0VGAA05_MaskK0VyAJGGGGAA0E0HPAmAA18_HPAjAA18_HPyHC_AlA0eF0HPyHCHC_A16_AAA19_HPyHCHC.47
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA6HStackVyAA9TupleViewVyACyACyAA5ImageV09TextInputB023IntelligenceLightEffect33_4E3CCC217D4507E7AD2D9EBD007764CALLVGAA07_OffsetM0VG_ACyAA0G0PAAE10fontWeightyQrAA4FontV0X0VSgFQOyACyAA0I0VAA30_EnvironmentKeyWritingModifierVySiSgGG_Qo_AMGSgtGGAA14_PaddingLayoutVGA11_GA1_yAA15DynamicTypeSizeOGGAaRHPA13_AaRHPA12_AaRHPA9_AaRHPyHC_A11_AA0G8ModifierHPyHCHC_A11_AAA18_HPyHCHC_A16_AAA18_HPyHCHC.43
+ _get_witness_table 7SwiftUI6ButtonVy09TextInputB012GenmojiLabelVGAA4ViewHPyHC.42
+ _objc_msgSend$_isMixmojiCandidate:
+ _objc_msgSend$_sendMixmojiTelemetryForCandidates:forKeyboardState:
+ _objc_msgSend$_setMixmojiCandidate:animated:
+ _objc_msgSend$getIAChannelCandidateBar
+ _objc_msgSend$getIASignalCandidateBarMixmojiCombineButtonPressed
+ _objc_msgSend$getIASignalCandidateBarMixmojiCombineButtonShown
+ _objc_msgSend$mixmojiContentView
+ _objc_msgSend$object
+ _objc_msgSend$sendCandidateBarSignal:threadId:payload:
+ _objc_msgSend$showGenmojiCreationForCurrentResponderWithInputString:
+ _objc_msgSend$showingArrowButton
+ _sharedInstance.__instance.10818
+ _sharedInstance.onceToken.10816
+ _sharedInstance.onceToken.6797
+ _sharedInstance.onceToken.9965
+ _shouldGenerateCandidateForContext:.onceToken.9882
+ _swift_bridgeObjectRetain_n
+ _symbolic _____ 11TextInputUI12GenmojiLabelV
+ _symbolic _____ 11TextInputUI22MixmojiCellContentViewC
+ _symbolic _____ 11TextInputUI25MixmojiCandidateGeneratorC
+ _symbolic _____yAAyAAy_____y_____yAAyAAy__________G_____G_AAy_____yAAy__________ySiSgGG_Qo_AEGSgtGG_____GASGAJy_____GG 7SwiftUI15ModifiedContentV AA6HStackV AA9TupleViewV AA5ImageV 09TextInputB023IntelligenceLightEffect33_4E3CCC217D4507E7AD2D9EBD007764CALLV AA07_OffsetM0V AA0G0PAAE10fontWeightyQrAA4FontV0X0VSgFQO AA0I0V AA30_EnvironmentKeyWritingModifierV AA14_PaddingLayoutV AA15DynamicTypeSizeO
+ _symbolic _____ySJG s11_SetStorageC
+ _symbolic _____ySJG s23_ContiguousArrayStorageC
+ _symbolic _____ySaySJGG s18ReversedCollectionV
+ _symbolic _____y_____G 11TextInputUI23SecureHostingControllerC AA12GenmojiLabelV
+ _symbolic _____y_____G 7SwiftUI19UIHostingControllerC 09TextInputB012GenmojiLabelV
+ _symbolic _____y_____G 7SwiftUI6ButtonV 09TextInputB012GenmojiLabelV
+ _type_layout_string 11TextInputUI12GenmojiLabelV
- _UIKitLibrary.2872
- _UIKitLibraryCore.frameworkLibrary.2875
- _UIKitLibraryCore.frameworkLibrary.3564
- __TUIKeyboardTrackingLogger.8526
- __TUIKeyboardTrackingLogger.log.8531
- __TUIKeyboardTrackingLogger.onceToken.8529
- ___Block_byref_object_copy_.12715
- ___Block_byref_object_copy_.2030
- ___Block_byref_object_copy_.2869
- ___Block_byref_object_copy_.3320
- ___Block_byref_object_copy_.5500
- ___Block_byref_object_copy_.8277
- ___Block_byref_object_copy_.9855
- ___Block_byref_object_dispose_.12716
- ___Block_byref_object_dispose_.2031
- ___Block_byref_object_dispose_.2870
- ___Block_byref_object_dispose_.3321
- ___Block_byref_object_dispose_.5501
- ___Block_byref_object_dispose_.8278
- ___Block_byref_object_dispose_.9856
- ___UIKitLibraryCore_block_invoke.2876
- ___UIKitLibraryCore_block_invoke.3565
- ____TUIKeyboardTrackingLogger_block_invoke.8534
- ___block_literal_global.10.10830
- ___block_literal_global.10493
- ___block_literal_global.10835
- ___block_literal_global.11021
- ___block_literal_global.11355
- ___block_literal_global.11509
- ___block_literal_global.11782
- ___block_literal_global.12725
- ___block_literal_global.12952
- ___block_literal_global.13400
- ___block_literal_global.17
- ___block_literal_global.1857
- ___block_literal_global.19
- ___block_literal_global.20.9954
- ___block_literal_global.2061
- ___block_literal_global.21
- ___block_literal_global.2534
- ___block_literal_global.2805
- ___block_literal_global.2913
- ___block_literal_global.2991
- ___block_literal_global.3175
- ___block_literal_global.3322
- ___block_literal_global.3817
- ___block_literal_global.4.12975
- ___block_literal_global.4079
- ___block_literal_global.4262
- ___block_literal_global.43.2514
- ___block_literal_global.4478
- ___block_literal_global.47
- ___block_literal_global.482
- ___block_literal_global.5336
- ___block_literal_global.6.11023
- ___block_literal_global.6675
- ___block_literal_global.6796
- ___block_literal_global.7057
- ___block_literal_global.7324
- ___block_literal_global.7720
- ___block_literal_global.7890
- ___block_literal_global.8332
- ___block_literal_global.8530
- ___block_literal_global.8732
- ___block_literal_global.9151
- ___block_literal_global.9333
- ___block_literal_global.9413
- ___block_literal_global.9491
- ___block_literal_global.9864
- ___block_literal_global.9957
- _audit_stringUIKit.2879
- _audit_stringUIKit.3570
- _get_witness_table 7SwiftUI15ModifiedContentVyAA6ButtonVyACyACyAA6HStackVyAA9TupleViewVyACyACyAA5ImageV09TextInputB023IntelligenceLightEffect33_4E3CCC217D4507E7AD2D9EBD007764CALLVGAA07_OffsetN0VG_ACyAA0H0PAAE10fontWeightyQrAA4FontV0Y0VSgFQOyACyAA0J0VAA30_EnvironmentKeyWritingModifierVySiSgGG_Qo_AOGSgtGGAA14_PaddingLayoutVGA13_GGA3_yAA15DynamicTypeSizeOGGAaTHPA16_AaTHPyHC_A19_AA0H8ModifierHPyHCHC.37
- _get_witness_table 7SwiftUI15ModifiedContentVyACyAA014_ViewModifier_D0Vy09TextInputB023IntelligenceLightEffect33_4E3CCC217D4507E7AD2D9EBD007764CALLVGAA08_OpacityK0VGAA011_BackgroundF0VyACyACyACyACyACyACyACyACyAA5ImageVAA18_AspectRatioLayoutVGAA06_ScaleK0VGAA09_RotationK0VGAA010_AnimationF0VySbGGAA017_AppearanceActionF0VGAA010_BlendModeK0VGAA023AccessibilityAttachmentF0VGAA05_MaskK0VyAJGGGGAA0E0HPAmAA18_HPAjAA18_HPyHC_AlA0eF0HPyHCHC_A16_AAA19_HPyHCHC.41
- _sharedInstance.__instance.10831
- _sharedInstance.onceToken.10829
- _sharedInstance.onceToken.6795
- _sharedInstance.onceToken.9953
- _shouldGenerateCandidateForContext:.onceToken.9870
- _symbolic _____y_____yAAyAAy_____y_____yAAyAAy__________G_____G_AAy_____yAAy__________ySiSgGG_Qo_AFGSgtGG_____GATGGAKy_____GG 7SwiftUI15ModifiedContentV AA6ButtonV AA6HStackV AA9TupleViewV AA5ImageV 09TextInputB023IntelligenceLightEffect33_4E3CCC217D4507E7AD2D9EBD007764CALLV AA07_OffsetN0V AA0H0PAAE10fontWeightyQrAA4FontV0Y0VSgFQO AA0J0V AA30_EnvironmentKeyWritingModifierV AA14_PaddingLayoutV AA15DynamicTypeSizeO
- _symbolic _____y_____yABy_____y_____yAByABy__________G_____G_ABy_____yABy__________ySiSgGG_Qo_AFGSgtGG_____GATGG 7SwiftUI6ButtonV AA15ModifiedContentV AA6HStackV AA9TupleViewV AA5ImageV 09TextInputB023IntelligenceLightEffect33_4E3CCC217D4507E7AD2D9EBD007764CALLV AA07_OffsetN0V AA0H0PAAE10fontWeightyQrAA4FontV0Y0VSgFQO AA0J0V AA30_EnvironmentKeyWritingModifierV AA14_PaddingLayoutV
CStrings:
+ "<%@: input=%@ title=%@>"
+ "@\"TUIMixmojiCellContentView\""
+ "Assigning candidates of source type Mixmoji to `containerToPush` - %@ (delayed=%s)"
+ "CandidateBar"
+ "Combine"
+ "Combine Mixmoji"
+ "IsMixmojiSuggestionsEnabled"
+ "Kicking off task to generate mixmoji candidate."
+ "MixmojiCombineButtonPressed"
+ "MixmojiCombineButtonShown"
+ "Successfully created mixmoji candidate container (for autocorrection). Calling completion handler."
+ "T@\"TUIMixmojiCellContentView\",&,N,V_mixmojiContentView"
+ "TUIMixmojiCandidate"
+ "TUIMixmojiCandidateGenerator"
+ "TUIMixmojiCellContentView"
+ "TextInputUI.MixmojiCellContentView"
+ "TextInputUI/TUIMixmojiCellContentView.swift"
+ "_emojiSetForIdentifier:"
+ "_isMixmojiCandidate:"
+ "_isMultiPersonFamilySkinToneEmoji:"
+ "_mixmojiContentView"
+ "_normalizeMultiPersonGroupToLongFormEncoding:"
+ "_sendMixmojiTelemetryForCandidates:forKeyboardState:"
+ "_setMixmojiCandidate:animated:"
+ "_supportsCoupleSkinToneSelection:"
+ "emojiTokenRef"
+ "emojiTokenWithString:localeData:"
+ "getIAChannelCandidateBar"
+ "getIASignalCandidateBarMixmojiCombineButtonPressed"
+ "getIASignalCandidateBarMixmojiCombineButtonShown"
+ "initWithInput:"
+ "maxCharactersToCheck"
+ "maxEmojis"
+ "minEmojis"
+ "mixmojiContentView"
+ "object"
+ "sendCandidateBarSignal:threadId:payload:"
+ "setMixmojiContentView:"
+ "showGenmojiCreationForCurrentResponderWithInputString:"
+ "\xf0\xe1"
- "\xf0\xd1"

```
