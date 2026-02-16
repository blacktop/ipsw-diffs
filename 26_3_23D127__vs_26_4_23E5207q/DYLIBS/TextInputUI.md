## TextInputUI

> `/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI`

```diff

-9126.3.5.0.0
-  __TEXT.__text: 0xdb068
-  __TEXT.__auth_stubs: 0x2bc0
-  __TEXT.__objc_methlist: 0xc594
+9126.4.20.0.0
+  __TEXT.__text: 0xe9e28
+  __TEXT.__auth_stubs: 0x2b60
+  __TEXT.__objc_methlist: 0xc62c
   __TEXT.__const: 0x2170
   __TEXT.__dlopen_cstrs: 0x1c4
-  __TEXT.__cstring: 0xa217
-  __TEXT.__swift5_typeref: 0xe7a
-  __TEXT.__oslogstring: 0x2db1
-  __TEXT.__swift5_capture: 0x2a8
+  __TEXT.__swift5_typeref: 0xe12
+  __TEXT.__oslogstring: 0x2dce
+  __TEXT.__swift5_capture: 0x2a0
+  __TEXT.__cstring: 0x97fd
   __TEXT.__constg_swiftt: 0xb44
   __TEXT.__swift5_reflstr: 0x468
   __TEXT.__swift5_fieldmd: 0x4cc

   __TEXT.__swift_as_ret: 0x34
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__ustring: 0x78
-  __TEXT.__unwind_info: 0x2e38
-  __TEXT.__eh_frame: 0xc6c
-  __TEXT.__objc_classname: 0x15b5
-  __TEXT.__objc_methname: 0x23d4c
-  __TEXT.__objc_methtype: 0x4f8f
-  __TEXT.__objc_stubs: 0x1bf00
-  __DATA_CONST.__got: 0x1180
-  __DATA_CONST.__const: 0x72d0
+  __TEXT.__unwind_info: 0x36c0
+  __TEXT.__eh_frame: 0xd14
+  __TEXT.__objc_classname: 0x187b
+  __TEXT.__objc_methname: 0x24580
+  __TEXT.__objc_methtype: 0x5149
+  __TEXT.__objc_stubs: 0x1c520
+  __DATA_CONST.__got: 0x1188
+  __DATA_CONST.__const: 0x72c8
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x86e8
+  __DATA_CONST.__objc_selrefs: 0x8770
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x360
-  __DATA_CONST.__objc_arraydata: 0x568
-  __AUTH_CONST.__auth_got: 0x15e8
+  __DATA_CONST.__objc_arraydata: 0x588
+  __AUTH_CONST.__auth_got: 0x15b8
   __AUTH_CONST.__const: 0x1628
-  __AUTH_CONST.__cfstring: 0xb640
-  __AUTH_CONST.__objc_const: 0x13898
+  __AUTH_CONST.__cfstring: 0xb6e0
+  __AUTH_CONST.__objc_const: 0x13938
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0xe0
-  __AUTH.__objc_data: 0x2160
-  __AUTH.__data: 0x5d0
-  __DATA.__objc_ivar: 0xed8
-  __DATA.__data: 0x1930
-  __DATA.__bss: 0x1648
+  __AUTH.__objc_data: 0x1f98
+  __AUTH.__data: 0x5a8
+  __DATA.__objc_ivar: 0xee4
+  __DATA.__data: 0x1890
+  __DATA.__bss: 0x1630
   __DATA.__common: 0x168
-  __DATA_DIRTY.__objc_data: 0x19f0
-  __DATA_DIRTY.__data: 0xd8
-  __DATA_DIRTY.__bss: 0x100
+  __DATA_DIRTY.__objc_data: 0x1bb8
+  __DATA_DIRTY.__data: 0x190
+  __DATA_DIRTY.__bss: 0x110
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D0ABD99E-DB80-39D7-A2D2-7FEBC2A0EEE3
-  Functions: 4893
-  Symbols:   16294
-  CStrings:  10181
+  UUID: ADEA9D5A-4675-39F0-861F-3B80418FE460
+  Functions: 4902
+  Symbols:   16361
+  CStrings:  10177
 
Symbols:
+ +[TUIKeyboardAnimationInfo infoForUnanimatedChange]
+ +[TUIKeyboardState stateForReloading]
+ -[TUIButtonBarItemView secureDictationSlotView]
+ -[TUIButtonBarItemView setSecureDictationSlotView:]
+ -[TUICandidateGrid needsReload]
+ -[TUIKBKeyView _setupDictationSlotView]
+ -[TUIKBKeyView dictationSlotView]
+ -[TUIKBKeyView setDictationSlotView:]
+ -[TUIKeyboardState reloadForPinnedInputViews]
+ -[TUIKeyboardState setReloadForPinnedInputViews:]
+ -[TUIKeyboardTrackingProvider trackingCoordinatorSpace]
+ -[TUIKeyplaneView resetKeySizeConstraints]
+ _OBJC_IVAR_$_TUIButtonBarItemView._secureDictationSlotView
+ _OBJC_IVAR_$_TUIKBKeyView._dictationSlotView
+ _OBJC_IVAR_$_TUIKeyboardState._reloadForPinnedInputViews
+ _UIKitLibrary.2894
+ _UIKitLibraryCore.frameworkLibrary.2897
+ _UIKitLibraryCore.frameworkLibrary.3583
+ __PROTOCOLS_TUISmartActionGenerator.5
+ __TUIKeyboardTrackingLogger.8550
+ __TUIKeyboardTrackingLogger.log.8556
+ __TUIKeyboardTrackingLogger.onceToken.8554
+ ___Block_byref_object_copy_.12836
+ ___Block_byref_object_copy_.2891
+ ___Block_byref_object_copy_.3340
+ ___Block_byref_object_copy_.5547
+ ___Block_byref_object_copy_.5882
+ ___Block_byref_object_copy_.8291
+ ___Block_byref_object_copy_.9919
+ ___Block_byref_object_dispose_.12837
+ ___Block_byref_object_dispose_.2892
+ ___Block_byref_object_dispose_.3341
+ ___Block_byref_object_dispose_.5548
+ ___Block_byref_object_dispose_.5883
+ ___Block_byref_object_dispose_.8292
+ ___Block_byref_object_dispose_.9920
+ ___UIKitLibraryCore_block_invoke.2898
+ ___UIKitLibraryCore_block_invoke.3584
+ ____TUIKeyboardTrackingLogger_block_invoke.8559
+ ___block_literal_global.10.10878
+ ___block_literal_global.10021
+ ___block_literal_global.10555
+ ___block_literal_global.10883
+ ___block_literal_global.11068
+ ___block_literal_global.11409
+ ___block_literal_global.11566
+ ___block_literal_global.11842
+ ___block_literal_global.12846
+ ___block_literal_global.13086
+ ___block_literal_global.13601
+ ___block_literal_global.18.8346
+ ___block_literal_global.20.10018
+ ___block_literal_global.20.9481
+ ___block_literal_global.22.9483
+ ___block_literal_global.2935
+ ___block_literal_global.3013
+ ___block_literal_global.3195
+ ___block_literal_global.3342
+ ___block_literal_global.3835
+ ___block_literal_global.4.13109
+ ___block_literal_global.4097
+ ___block_literal_global.4248
+ ___block_literal_global.4493
+ ___block_literal_global.5370
+ ___block_literal_global.5580
+ ___block_literal_global.5992
+ ___block_literal_global.6.11070
+ ___block_literal_global.61.13084
+ ___block_literal_global.6679
+ ___block_literal_global.6801
+ ___block_literal_global.685
+ ___block_literal_global.7064
+ ___block_literal_global.7334
+ ___block_literal_global.767
+ ___block_literal_global.771
+ ___block_literal_global.7731
+ ___block_literal_global.7902
+ ___block_literal_global.8350
+ ___block_literal_global.8555
+ ___block_literal_global.8757
+ ___block_literal_global.9207
+ ___block_literal_global.9394
+ ___block_literal_global.9474
+ ___block_literal_global.9556
+ ___block_literal_global.9928
+ _audit_stringUIKit.2901
+ _audit_stringUIKit.3589
+ _get_underlying_type_ref 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOQr.2
+ _get_underlying_witness 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOqd__AaBHC.3
+ _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAC6TipKitE07popoverI0_11isPresented16attachmentAnchor9arrowEdge6actionQrAJ0I0_pSg_AA7BindingVySbGSgAA017PopoverAttachmentO0OAA0Q0OSgyAJ4TipsO6ActionVctFQOyAA6SpacerV_Qo__Qo_HO.37
+ _objc_msgSend$_emojiSetForIdentifier:
+ _objc_msgSend$_isMultiPersonFamilySkinToneEmoji:
+ _objc_msgSend$_normalizeMultiPersonGroupToLongFormEncoding:
+ _objc_msgSend$_setupDictationSlotView
+ _objc_msgSend$_supportsCoupleSkinToneSelection:
+ _objc_msgSend$actionText
+ _objc_msgSend$actionType
+ _objc_msgSend$actionsResponse
+ _objc_msgSend$bundleWithIdentifier:
+ _objc_msgSend$description
+ _objc_msgSend$detailControllerClass
+ _objc_msgSend$dictationSlotView
+ _objc_msgSend$dictationSlotViewWithFrame:onRemoteContentLoad:
+ _objc_msgSend$didObserveNetworkAvailabilityChange:
+ _objc_msgSend$emojiTokenRef
+ _objc_msgSend$emojiTokenWithString:localeData:
+ _objc_msgSend$enableDictationSecureTouch
+ _objc_msgSend$extractFinalResult:
+ _objc_msgSend$followUp
+ _objc_msgSend$generatedCandidateType
+ _objc_msgSend$init
+ _objc_msgSend$initWithBool:
+ _objc_msgSend$initWithInput:
+ _objc_msgSend$initWithTitle:options:
+ _objc_msgSend$loadSpecifiersFromPlistName:target:bundle:
+ _objc_msgSend$needsReload
+ _objc_msgSend$nextToken
+ _objc_msgSend$objectForInfoDictionaryKey:
+ _objc_msgSend$performGetter
+ _objc_msgSend$pollOptions
+ _objc_msgSend$prepareSecureTouchWithAuthenticationMessage:
+ _objc_msgSend$propertyForKey:
+ _objc_msgSend$reloadForPinnedInputViews
+ _objc_msgSend$repliesResponse
+ _objc_msgSend$requiresFollowUp
+ _objc_msgSend$resetKeySizeConstraints
+ _objc_msgSend$responses
+ _objc_msgSend$secureDictationSlotView
+ _objc_msgSend$setDictationSlotView:
+ _objc_msgSend$setEditing:animated:
+ _objc_msgSend$setInsetsLayoutMarginsFromSafeArea:
+ _objc_msgSend$setProperty:forKey:
+ _objc_msgSend$setReloadForPinnedInputViews:
+ _objc_msgSend$setSecureDictationSlotView:
+ _objc_msgSend$setSemanticContentAttribute:
+ _objc_msgSend$setShouldSuggestTitle:
+ _objc_msgSend$setSpecifier:
+ _objc_msgSend$specifier
+ _objc_msgSend$tiInputContextHistory
+ _objc_msgSend$trackingCoordinatorSpace
+ _sharedInstance.__instance.10879
+ _sharedInstance.onceToken.10017
+ _sharedInstance.onceToken.10877
+ _sharedInstance.onceToken.6800
+ _shouldGenerateCandidateForContext:.onceToken.9934
+ _symbolic _____y_____y______Qo__Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AC6TipKitE07popoverI0_11isPresented16attachmentAnchor9arrowEdge6actionQrAJ0I0_pSg_AA7BindingVySbGSgAA017PopoverAttachmentO0OAA0Q0OSgyAJ4TipsO6ActionVctFQO AA6SpacerV
- _UIKitLibrary.2893
- _UIKitLibraryCore.frameworkLibrary.2896
- _UIKitLibraryCore.frameworkLibrary.3582
- __PROTOCOLS_TUISmartActionGenerator.8
- __TUIKeyboardTrackingLogger.8610
- __TUIKeyboardTrackingLogger.log.8616
- __TUIKeyboardTrackingLogger.onceToken.8614
- ___Block_byref_object_copy_.12851
- ___Block_byref_object_copy_.2890
- ___Block_byref_object_copy_.3339
- ___Block_byref_object_copy_.5568
- ___Block_byref_object_copy_.5937
- ___Block_byref_object_copy_.8352
- ___Block_byref_object_copy_.9940
- ___Block_byref_object_dispose_.12852
- ___Block_byref_object_dispose_.2891
- ___Block_byref_object_dispose_.3340
- ___Block_byref_object_dispose_.5569
- ___Block_byref_object_dispose_.5938
- ___Block_byref_object_dispose_.8353
- ___Block_byref_object_dispose_.9941
- ___UIKitLibraryCore_block_invoke.2897
- ___UIKitLibraryCore_block_invoke.3583
- ____TUIKeyboardTrackingLogger_block_invoke.8619
- ___block_literal_global.10.10896
- ___block_literal_global.10042
- ___block_literal_global.10583
- ___block_literal_global.10901
- ___block_literal_global.11086
- ___block_literal_global.11426
- ___block_literal_global.11584
- ___block_literal_global.11857
- ___block_literal_global.12861
- ___block_literal_global.13102
- ___block_literal_global.13609
- ___block_literal_global.18.8407
- ___block_literal_global.20.10039
- ___block_literal_global.20.9501
- ___block_literal_global.22.9503
- ___block_literal_global.2934
- ___block_literal_global.3012
- ___block_literal_global.3194
- ___block_literal_global.3341
- ___block_literal_global.3834
- ___block_literal_global.4.13125
- ___block_literal_global.4096
- ___block_literal_global.4279
- ___block_literal_global.4502
- ___block_literal_global.5391
- ___block_literal_global.5601
- ___block_literal_global.6.11088
- ___block_literal_global.6053
- ___block_literal_global.61.13100
- ___block_literal_global.667
- ___block_literal_global.6744
- ___block_literal_global.6866
- ___block_literal_global.7130
- ___block_literal_global.7399
- ___block_literal_global.766
- ___block_literal_global.770
- ___block_literal_global.7796
- ___block_literal_global.7963
- ___block_literal_global.8411
- ___block_literal_global.8615
- ___block_literal_global.8817
- ___block_literal_global.9232
- ___block_literal_global.9414
- ___block_literal_global.9494
- ___block_literal_global.9576
- ___block_literal_global.9949
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_TextInputUI
- _audit_stringUIKit.2900
- _audit_stringUIKit.3588
- _get_underlying_type_ref 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line6actionQrSSSg_ScPSSSiyyYaYAcntFQOQr.5
- _get_underlying_witness 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line6actionQrSSSg_ScPSSSiyyYaYAcntFQOqd__AaBHC.6
- _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE4task4name8priority4file4line6actionQrSSSg_ScPSSSiyyYaYAcntFQOyAC6TipKitE07popoverJ0_11isPresented16attachmentAnchor9arrowEdgeAIQrAK0J0_pSg_AA7BindingVySbGSgAA017PopoverAttachmentP0OAA0R0OSgyAK4TipsO6ActionVctFQOyAA6SpacerV_Qo__Qo_HO.37
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$userInterfaceLayoutDirectionForSemanticContentAttribute:
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _sharedInstance.__instance.10897
- _sharedInstance.onceToken.10038
- _sharedInstance.onceToken.10895
- _sharedInstance.onceToken.6865
- _shouldGenerateCandidateForContext:.onceToken.9955
- _symbolic _____yAAyAAyAAyAAyAAyAAy__________G_____G_____G_____ySbGG_____G_____G_____G 7SwiftUI15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV AA12_ScaleEffectV AA09_RotationJ0V AA18_AnimationModifierV AA017_AppearanceActionM0V AA010_BlendModeJ0V AA023AccessibilityAttachmentM0V
- _symbolic _____y_____y______Qo__Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line6actionQrSSSg_ScPSSSiyyYaYAcntFQO AC6TipKitE07popoverJ0_11isPresented16attachmentAnchor9arrowEdgeAIQrAK0J0_pSg_AA7BindingVySbGSgAA017PopoverAttachmentP0OAA0R0OSgyAK4TipsO6ActionVctFQO AA6SpacerV
- _symbolic _____y_____y______Qo______G 7SwiftUI15ModifiedContentV AA4ViewP6TipKitE07popoverF0_11isPresented16attachmentAnchor9arrowEdge6actionQrAF0F0_pSg_AA7BindingVySbGSgAA017PopoverAttachmentL0OAA0N0OSgyAF4TipsO6ActionVctFQO AA6SpacerV AA13_TaskModifierV
CStrings:
+ "@\"_UISlotView\""
+ "Dynamic-Inuktitut"
+ "Inuktitut-Alternate-Letters-Finals-Keyplane-Switch-Key"
+ "Inuktitut-Letters-Finals-Keyplane-Switch-Key"
+ "Inuktitut-Shift-Alternate-Letters-Finals-Keyplane-Switch-Key"
+ "Inuktitut-Shift-Letters-Finals-Keyplane-Switch-Key"
+ "T@\"_UISlotView\",&,N,V_dictationSlotView"
+ "T@\"_UISlotView\",&,N,V_secureDictationSlotView"
+ "TB,N,V_reloadForPinnedInputViews"
+ "TUIGenerativeModelsAvailability"
+ "Updated tracking window via state update to %@; offset to %@; from %@; for %@"
+ "_dictationSlotView"
+ "_reloadForPinnedInputViews"
+ "_secureDictationSlotView"
+ "_setupDictationSlotView"
+ "assistantDictation"
+ "dictationSlotView"
+ "dictationSlotViewWithFrame:onRemoteContentLoad:"
+ "enableDictationSecureTouch"
+ "infoForUnanimatedChange"
+ "needsReload"
+ "prepareSecureTouchWithAuthenticationMessage:"
+ "reloadForPinnedInputViews"
+ "resetKeySizeConstraints"
+ "secureDictationSlotView"
+ "setDictationSlotView:"
+ "setInsetsLayoutMarginsFromSafeArea:"
+ "setReloadForPinnedInputViews:"
+ "setSecureDictationSlotView:"
+ "setSemanticContentAttribute:"
+ "stateForReloading"
+ "trackingCoordinatorSpace"
+ "{"
- "Update size to %@; offset to %@; from %@; for %@"
- "userInterfaceLayoutDirectionForSemanticContentAttribute:"
- "z"

```
