## AccessibilitySettings

> `/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-1726.2.17.0.0
-  __TEXT.__text: 0x143c58
-  __TEXT.__auth_stubs: 0x3610
-  __TEXT.__objc_stubs: 0x210c0
-  __TEXT.__objc_methlist: 0x110fc
+1726.15.0.0.0
+  __TEXT.__text: 0x14496c
+  __TEXT.__auth_stubs: 0x35f0
+  __TEXT.__objc_stubs: 0x21480
+  __TEXT.__objc_methlist: 0x1120c
   __TEXT.__const: 0xfa4
-  __TEXT.__gcc_except_tab: 0x2ad8
-  __TEXT.__objc_methname: 0x2eb5f
-  __TEXT.__cstring: 0x14f38
-  __TEXT.__oslogstring: 0x2c9b
-  __TEXT.__objc_classname: 0x3de4
-  __TEXT.__objc_methtype: 0x5b7a
+  __TEXT.__gcc_except_tab: 0x2adc
+  __TEXT.__objc_methname: 0x2ef25
+  __TEXT.__cstring: 0x15398
+  __TEXT.__oslogstring: 0x2f16
+  __TEXT.__objc_classname: 0x3e07
+  __TEXT.__objc_methtype: 0x5bb7
   __TEXT.__dlopen_cstrs: 0x186
   __TEXT.__ustring: 0x2e
   __TEXT.__constg_swiftt: 0x668

   __TEXT.__swift5_capture: 0x80
   __TEXT.__swift5_proto: 0x64
   __TEXT.__swift5_types: 0x64
-  __TEXT.__unwind_info: 0x4ad8
-  __DATA_CONST.__auth_got: 0x1b18
-  __DATA_CONST.__got: 0x1348
+  __TEXT.__unwind_info: 0x4b18
+  __DATA_CONST.__auth_got: 0x1b08
+  __DATA_CONST.__got: 0x1350
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x4910
-  __DATA_CONST.__cfstring: 0x17640
+  __DATA_CONST.__const: 0x4980
+  __DATA_CONST.__cfstring: 0x17d00
   __DATA_CONST.__objc_classlist: 0xcf0
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x268
+  __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x1568
+  __DATA_CONST.__objc_superrefs: 0xa40
   __DATA_CONST.__objc_intobj: 0x15c0
-  __DATA_CONST.__objc_arraydata: 0x11c0
-  __DATA_CONST.__objc_arrayobj: 0x708
-  __DATA_CONST.__objc_dictobj: 0x870
+  __DATA_CONST.__objc_arraydata: 0x1188
+  __DATA_CONST.__objc_arrayobj: 0x6f0
   __DATA_CONST.__objc_doubleobj: 0x1b0
   __DATA_CONST.__objc_floatobj: 0x20
-  __DATA.__objc_const: 0x1e628
-  __DATA.__objc_selrefs: 0xad58
-  __DATA.__objc_classrefs: 0x1548
-  __DATA.__objc_superrefs: 0xa40
-  __DATA.__objc_ivar: 0xce0
+  __DATA_CONST.__objc_dictobj: 0x848
+  __DATA.__objc_const: 0x1e6e8
+  __DATA.__objc_selrefs: 0xae50
+  __DATA.__objc_ivar: 0xce8
   __DATA.__objc_data: 0x8318
-  __DATA.__data: 0x259a
+  __DATA.__data: 0x25fa
   __DATA.__bss: 0xf55
   __DATA.__common: 0x38
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI
+  - /System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI
   - /System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/RTTUI.framework/RTTUI

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ED9FB7E0-14FE-342E-9DFB-B53F77503A97
-  Functions: 7188
-  Symbols:   17705
-  CStrings:  14801
+  UUID: E80030D7-2AFC-3279-AE71-99BC5735BD51
+  Functions: 7206
+  Symbols:   17765
+  CStrings:  14953
 
Symbols:
+ +[SecureIntentViewController authStorageKeyForRequestSource:]
+ +[SecureIntentViewController isEnrolledWithRequestSource:]
+ -[AccessibilitySettingsController _customGraphicIconWithSymbol:systemColor:]
+ -[AccessibilitySettingsController _graphicIconForBundleIdentifier:]
+ -[AccessibilitySettingsController _iconImageFromISIcon:]
+ -[AccessibilitySettingsController _predefinedGraphicIconNamed:]
+ -[AccessibilitySettingsController _shouldUseGraphicsRecipes]
+ -[AccessibilitySettingsController showPersonalVoiceController:]
+ -[DetectorsController _eligibleForApplePay]
+ -[DetectorsController _presentKShotOnboardingController:]
+ -[DetectorsController _presentKShotOnboardingControllerWithCategory:]
+ -[DetectorsController _presentKShotOnboardingControllerWithDetector:]
+ -[DetectorsController _presentKShotSecureIntent]
+ -[DetectorsController _shouldUseKShotEnrollment]
+ -[DetectorsController localAuthContext]
+ -[DetectorsController secureIntentViewControllerDidCancel:]
+ -[DetectorsController secureIntentViewControllerDidFinish:]
+ -[DetectorsController setLocalAuthContext:]
+ -[DetectorsDetailsController _updateSoundDetectionState]
+ -[HandController secureIntentViewControllerDidCancel:]
+ -[SCATController secureIntentViewControllerDidCancel:]
+ -[SecureIntentViewController _authStorageKey]
+ -[SecureIntentViewController _logger]
+ -[SecureIntentViewController authStorageKeyDescription:]
+ -[SecureIntentViewController isEnrolled]
+ -[SecureIntentViewController requestSourceDescription]
+ GCC_except_table30
+ GCC_except_table57
+ OBJC_IVAR_$_DetectorsController._cachedSpecifier
+ OBJC_IVAR_$_DetectorsController._localAuthContext
+ _AXResizeImageWithSize
+ _IOHIDDeviceGetProperty
+ _OBJC_CLASS_$_IFColor
+ _OBJC_CLASS_$_IFGraphicSymbolDescriptor
+ _OBJC_CLASS_$_IFSymbol
+ _OBJC_CLASS_$_ISIcon
+ __102-[VoiceOverScreenRecognitionController assetController:didFinishRefreshingAssets:wasSuccessful:error:]_block_invoke.280
+ __104-[AXVoiceOverImageDescriptionsController assetController:didFinishRefreshingAssets:wasSuccessful:error:]_block_invoke.368
+ __135-[UIViewController(AXTripleClickConflictAvoidance) accessibilityPerformTripleClickAddingBlockConfirmingSOSConflicts:cancellationBlock:]_block_invoke.428
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke.251
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke.257
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_2.252
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_2.259
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_3.253
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_3.260
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_4.254
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_4.261
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_5.255
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_5.265
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_6.256
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_6.269
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_7.273
+ __28-[HandController specifiers]_block_invoke.367
+ __39-[AccessibilitySettingsController init]_block_invoke.299
+ __41-[VoiceOverActivityController specifiers]_block_invoke.416
+ __41-[VoiceOverActivityController specifiers]_block_invoke.452
+ __41-[VoiceOverActivityController specifiers]_block_invoke_10.505
+ __41-[VoiceOverActivityController specifiers]_block_invoke_11.509
+ __41-[VoiceOverActivityController specifiers]_block_invoke_12.521
+ __41-[VoiceOverActivityController specifiers]_block_invoke_13.522
+ __41-[VoiceOverActivityController specifiers]_block_invoke_14.523
+ __41-[VoiceOverActivityController specifiers]_block_invoke_15.537
+ __41-[VoiceOverActivityController specifiers]_block_invoke_16.538
+ __41-[VoiceOverActivityController specifiers]_block_invoke_17.546
+ __41-[VoiceOverActivityController specifiers]_block_invoke_18.547
+ __41-[VoiceOverActivityController specifiers]_block_invoke_19.584
+ __41-[VoiceOverActivityController specifiers]_block_invoke_2.420
+ __41-[VoiceOverActivityController specifiers]_block_invoke_2.453
+ __41-[VoiceOverActivityController specifiers]_block_invoke_20.588
+ __41-[VoiceOverActivityController specifiers]_block_invoke_3.467
+ __41-[VoiceOverActivityController specifiers]_block_invoke_4.468
+ __41-[VoiceOverActivityController specifiers]_block_invoke_5.476
+ __41-[VoiceOverActivityController specifiers]_block_invoke_6.477
+ __41-[VoiceOverActivityController specifiers]_block_invoke_7.488
+ __41-[VoiceOverActivityController specifiers]_block_invoke_8.490
+ __41-[VoiceOverActivityController specifiers]_block_invoke_9.501
+ __42-[HandController setPayWithAST:specifier:]_block_invoke.519
+ __42-[HandController setPayWithAST:specifier:]_block_invoke.519.cold.1
+ __42-[HandController setPayWithAST:specifier:]_block_invoke.526
+ __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.714
+ __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.714.cold.1
+ __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.721
+ __53-[SCATController setSwitchScanningEnabled:specifier:]_block_invoke.657
+ __54-[AXPearlSettingsController setPearlUnlock:specifier:]_block_invoke.309
+ __59-[AXPronunciationEntryViewController _dictateButtonTapped:]_block_invoke.458
+ __59-[AXPronunciationEntryViewController _dictateButtonTapped:]_block_invoke.462
+ __59-[AXPronunciationEntryViewController _dictateButtonTapped:]_block_invoke.473
+ __65-[VoiceOverCommandDetailsViewController _addGestureButtonTapped:]_block_invoke.279
+ __68-[VoiceOverActivitySpeechVoiceSelector _showUnifiedSpeechSelection:]_block_invoke.242
+ __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.307
+ __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.307.cold.1
+ __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.313
+ __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.313.cold.1
+ __75-[ClarityUIAdminPasscodeSetupController _axShowDoneControllerWithPasscode:]_block_invoke.341
+ __75-[ClarityUIAdminPasscodeSetupController _axShowDoneControllerWithPasscode:]_block_invoke_2.343
+ __83-[VoiceOverCommandsByTouchGestureListController tableView:didSelectRowAtIndexPath:]_block_invoke.240
+ __84-[VoiceOverCommandDetailsViewController _addKeyboardShortcutWithSpecifier:resolver:]_block_invoke.283
+ __88-[VoiceOverCommandDetailsViewController tableView:commitEditingStyle:forRowAtIndexPath:]_block_invoke.270
+ __88-[VoiceOverCommandDetailsViewController tableView:commitEditingStyle:forRowAtIndexPath:]_block_invoke_2.271
+ __88-[VoiceOverCommandDetailsViewController tableView:commitEditingStyle:forRowAtIndexPath:]_block_invoke_2.271.cold.1
+ __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.291
+ __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.303
+ __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.303.cold.1
+ __99-[VoiceOverCommandsByKeyboardShortcutListController _modifyKeyboardShortcutWithSpecifier:resolver:]_block_invoke.257
+ __OBJC_$_CLASS_METHODS_SecureIntentViewController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SecureIntentViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SecureIntentViewControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_SecureIntentViewControllerDelegate
+ __OBJC_PROTOCOL_$_SecureIntentViewControllerDelegate
+ ___54-[HandController secureIntentViewControllerDidCancel:]_block_invoke
+ ___54-[SCATController secureIntentViewControllerDidCancel:]_block_invoke
+ ___63-[AccessibilitySettingsController showPersonalVoiceController:]_block_invoke
+ ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ __block_literal_global.241
+ __block_literal_global.243
+ __block_literal_global.255
+ __block_literal_global.257
+ __block_literal_global.258
+ __block_literal_global.263
+ __block_literal_global.266
+ __block_literal_global.271
+ __block_literal_global.274
+ __block_literal_global.280
+ __block_literal_global.283
+ __block_literal_global.289
+ __block_literal_global.292
+ __block_literal_global.293
+ __block_literal_global.294
+ __block_literal_global.296
+ __block_literal_global.299
+ __block_literal_global.300
+ __block_literal_global.305
+ __block_literal_global.306
+ __block_literal_global.308
+ __block_literal_global.309
+ __block_literal_global.310
+ __block_literal_global.312
+ __block_literal_global.327
+ __block_literal_global.331
+ __block_literal_global.335
+ __block_literal_global.337
+ __block_literal_global.339
+ __block_literal_global.348
+ __block_literal_global.352
+ __block_literal_global.357
+ __block_literal_global.360
+ __block_literal_global.362
+ __block_literal_global.364
+ __block_literal_global.367
+ __block_literal_global.371
+ __block_literal_global.372
+ __block_literal_global.385
+ __block_literal_global.392
+ __block_literal_global.394
+ __block_literal_global.397
+ __block_literal_global.398
+ __block_literal_global.402
+ __block_literal_global.404
+ __block_literal_global.417
+ __block_literal_global.419
+ __block_literal_global.432
+ __block_literal_global.437
+ __block_literal_global.453
+ __block_literal_global.455
+ __block_literal_global.465
+ __block_literal_global.476
+ __block_literal_global.482
+ __block_literal_global.503
+ __block_literal_global.505
+ __block_literal_global.508
+ __block_literal_global.509
+ __block_literal_global.517
+ __block_literal_global.522
+ __block_literal_global.537
+ __block_literal_global.623
+ __block_literal_global.626
+ __block_literal_global.629
+ __block_literal_global.634
+ __block_literal_global.672
+ __block_literal_global.717
+ __block_literal_global.736
+ _calloc
+ _objc_msgSend$_authStorageKey
+ _objc_msgSend$_customGraphicIconWithSymbol:systemColor:
+ _objc_msgSend$_eligibleForApplePay
+ _objc_msgSend$_iconImageFromISIcon:
+ _objc_msgSend$_logger
+ _objc_msgSend$_predefinedGraphicIconNamed:
+ _objc_msgSend$_presentKShotOnboardingController:
+ _objc_msgSend$_presentKShotOnboardingControllerWithCategory:
+ _objc_msgSend$_presentKShotOnboardingControllerWithDetector:
+ _objc_msgSend$_presentKShotSecureIntent
+ _objc_msgSend$_shouldUseGraphicsRecipes
+ _objc_msgSend$_shouldUseKShotEnrollment
+ _objc_msgSend$_startKShotOnboarding:
+ _objc_msgSend$_updateSoundDetectionState
+ _objc_msgSend$authStorageKeyDescription:
+ _objc_msgSend$authStorageKeyForRequestSource:
+ _objc_msgSend$getUserPreferredVoiceTriggerPhraseTypeForDeviceType:endpointId:error:
+ _objc_msgSend$imageForGraphicSymbolDescriptor:
+ _objc_msgSend$imageForImageDescriptor:
+ _objc_msgSend$imageWithCGImage:
+ _objc_msgSend$initWithSize:scale:
+ _objc_msgSend$initWithSymbolName:bundleURL:
+ _objc_msgSend$initWithSystemColor:
+ _objc_msgSend$invalidateIntrinsicContentSize
+ _objc_msgSend$isEnrolled
+ _objc_msgSend$isEnrolledWithRequestSource:
+ _objc_msgSend$localizedCompactTriggerPhraseForLanguageCode:
+ _objc_msgSend$requestSourceDescription
+ _objc_msgSend$secureIntentViewControllerDidCancel:
+ _objc_msgSend$setEnclosureColors:
+ _objc_msgSend$setRenderingMode:
+ _objc_msgSend$setSymbolColors:
+ _unnamed_array_storage.260
+ _unnamed_array_storage.261
+ _unnamed_array_storage.263
+ _unnamed_array_storage.266
+ _unnamed_array_storage.269
+ _unnamed_array_storage.270
+ _unnamed_array_storage.271
+ _unnamed_array_storage.272
+ _unnamed_array_storage.279
+ _unnamed_array_storage.281
+ _unnamed_array_storage.291
+ _unnamed_array_storage.292
+ _unnamed_array_storage.301
+ _unnamed_array_storage.302
+ _unnamed_array_storage.309
+ _unnamed_array_storage.322
+ _unnamed_array_storage.329
+ _unnamed_array_storage.330
+ _unnamed_array_storage.336
+ _unnamed_array_storage.337
+ _unnamed_array_storage.343
+ _unnamed_array_storage.344
+ _unnamed_array_storage.350
+ _unnamed_array_storage.351
+ _unnamed_array_storage.357
+ _unnamed_array_storage.358
+ _unnamed_array_storage.364
+ _unnamed_array_storage.365
+ _unnamed_array_storage.372
+ _unnamed_array_storage.376
+ _unnamed_array_storage.379
+ _unnamed_array_storage.380
+ _unnamed_array_storage.383
+ _unnamed_array_storage.385
+ _unnamed_array_storage.386
+ _unnamed_array_storage.387
+ _unnamed_array_storage.391
+ _unnamed_array_storage.392
+ _unnamed_array_storage.393
+ _unnamed_array_storage.395
+ _unnamed_array_storage.398
+ _unnamed_array_storage.401
+ _unnamed_array_storage.402
+ _unnamed_array_storage.413
+ _unnamed_array_storage.421
+ _unnamed_array_storage.432
+ _unnamed_array_storage.435
+ _unnamed_array_storage.438
+ _unnamed_array_storage.441
+ _unnamed_array_storage.442
+ _unnamed_array_storage.444
+ _unnamed_array_storage.448
+ _unnamed_array_storage.450
+ _unnamed_array_storage.451
+ _unnamed_array_storage.452
+ _unnamed_array_storage.455
+ _unnamed_array_storage.458
+ _unnamed_array_storage.461
+ _unnamed_array_storage.464
+ _unnamed_array_storage.467
+ _unnamed_array_storage.470
+ _unnamed_array_storage.578
+ _unnamed_array_storage.579
+ _unnamed_array_storage.590
+ _unnamed_array_storage.591
+ _unnamed_array_storage.604
+ _unnamed_array_storage.605
+ _unnamed_array_storage.616
+ _unnamed_array_storage.617
+ _unnamed_array_storage.620
+ _unnamed_array_storage.631
+ _unnamed_array_storage.632
+ _unnamed_array_storage.638
+ _unnamed_array_storage.645
+ _unnamed_array_storage.646
+ _unnamed_array_storage.652
+ _unnamed_array_storage.653
+ _unnamed_array_storage.659
+ _unnamed_array_storage.660
+ _unnamed_array_storage.663
+ _unnamed_array_storage.713
+ _unnamed_array_storage.714
+ _unnamed_array_storage.726
+ _unnamed_array_storage.727
+ _unnamed_array_storage.730
+ get_witness_table 7SwiftUI15ModifiedContentVyAA6ZStackVyAA9TupleViewVyACy21AccessibilitySettings40ClarityOnboardingPreviewRoundedRectangleVAA13_ShadowEffectVG_ACyAA09_VariadicG0O4TreeVy_AA11_LayoutRootVyAA03AnyS0VGAGyACyAjA012_AspectRatioS0VG_ACyAjA010_FlexFrameS0VGtGGAA08_PaddingS0VGtGGA_GAA0G0HPA7_AAA9_HPyHC_A_AA0G8ModifierHPyHCHC.26
+ get_witness_table 7SwiftUI15ModifiedContentVyAA6ZStackVyAA9TupleViewVyACyACy21AccessibilitySettings40ClarityOnboardingPreviewRoundedRectangleVAA13_ShadowEffectVGAA14_PaddingLayoutVG_ACyAjA010_FlexFrameR0VGtGGARGAA0G0HPAuaWHPyHC_ArA0G8ModifierHPyHCHC.27
+ get_witness_table 7SwiftUI15ModifiedContentVyACy21AccessibilitySettings33ClarityOnboardingDeviceLockScreenVAA12_FrameLayoutVGAA0E18AttachmentModifierVGAA4ViewHPAiaMHPAfaMHPyHC_AhA0pO0HPyHCHC_AkaNHPyHCHC.12
+ get_witness_table 7SwiftUI15ModifiedContentVyACy21AccessibilitySettings40ClarityOnboardingDeviceBackgroundAndAppsVAA12_FrameLayoutVGAA0E18AttachmentModifierVGAA4ViewHPAiaMHPAfaMHPyHC_AhA0qP0HPyHCHC_AkaNHPyHCHC.11
+ get_witness_table 7SwiftUI15ModifiedContentVyACyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA11_ClipEffectVyAA07RoundedE0VGGAA4ViewHPAkaRHPAeaRHPyHC_AjA0mH0HPyHCHC_ApaSHPyHCHC.28
+ get_witness_table 7SwiftUI6ZStackVyAA9TupleViewVyAA15ModifiedContentVyAGyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA11_ClipEffectVyAA07RoundedH0VGG_AGyAGyAGyAA5ImageVAA18_AspectRatioLayoutVGAA06_FrameS0VGATGSgAA6VStackVyAEyAGyAA6SpacerVA0_G_AGy21AccessibilitySettings024ClarityOnboardingPreviewoH0VAA05_FlextS0VGA7_A9_0Y23LockScreenPreviewButtonVtGGtGGAA0E0HPyHC.25
+ get_witness_table 7SwiftUI6ZStackVyAA9TupleViewVyAA15ModifiedContentVyAGyAGyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA11_ClipEffectVyAA07RoundedH0VGGAA07_ShadowN0VG_AGyAGyAA6VStackVyAEyAGyAA6SpacerVAA12_FrameLayoutVG_AA7ForEachVySnySiGSi21AccessibilitySettings33ClarityOnboardingPreviewAppButtonVGtGGAA08_PaddingT0VGAA08_OpacityN0VGAGyAZyAEyA3__AGyAA9LazyVGridVyA10_GA14_GtGGA17_GtGGAA0E0HPyHC.24
- -[AccessibilitySettingsController tableView:didSelectRowAtIndexPath:]
- -[HandController _eligibleForApplePayWithAST]
- -[SCATController _eligibleForApplePayWithSwitchControl]
- -[SecureIntentViewController viewDidDisappear:]
- GCC_except_table52
- _AXDeviceSupportsVoiceBankingSpeech
- _AXDeviceSupportsVoiceBankingTraining
- _CGRectGetMinY
- __102-[VoiceOverScreenRecognitionController assetController:didFinishRefreshingAssets:wasSuccessful:error:]_block_invoke.256
- __104-[AXVoiceOverImageDescriptionsController assetController:didFinishRefreshingAssets:wasSuccessful:error:]_block_invoke.344
- __135-[UIViewController(AXTripleClickConflictAvoidance) accessibilityPerformTripleClickAddingBlockConfirmingSOSConflicts:cancellationBlock:]_block_invoke.404
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke.227
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke.233
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_2.228
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_2.235
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_3.229
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_3.236
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_4.230
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_4.237
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_5.231
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_5.241
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_6.232
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_6.245
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_7.249
- __28-[HandController specifiers]_block_invoke.343
- __39-[AccessibilitySettingsController init]_block_invoke.272
- __41-[VoiceOverActivityController specifiers]_block_invoke.392
- __41-[VoiceOverActivityController specifiers]_block_invoke.428
- __41-[VoiceOverActivityController specifiers]_block_invoke_10.481
- __41-[VoiceOverActivityController specifiers]_block_invoke_11.485
- __41-[VoiceOverActivityController specifiers]_block_invoke_12.497
- __41-[VoiceOverActivityController specifiers]_block_invoke_13.498
- __41-[VoiceOverActivityController specifiers]_block_invoke_14.499
- __41-[VoiceOverActivityController specifiers]_block_invoke_15.513
- __41-[VoiceOverActivityController specifiers]_block_invoke_16.514
- __41-[VoiceOverActivityController specifiers]_block_invoke_17.522
- __41-[VoiceOverActivityController specifiers]_block_invoke_18.523
- __41-[VoiceOverActivityController specifiers]_block_invoke_19.560
- __41-[VoiceOverActivityController specifiers]_block_invoke_2.396
- __41-[VoiceOverActivityController specifiers]_block_invoke_2.429
- __41-[VoiceOverActivityController specifiers]_block_invoke_20.564
- __41-[VoiceOverActivityController specifiers]_block_invoke_3.443
- __41-[VoiceOverActivityController specifiers]_block_invoke_4.444
- __41-[VoiceOverActivityController specifiers]_block_invoke_5.452
- __41-[VoiceOverActivityController specifiers]_block_invoke_6.453
- __41-[VoiceOverActivityController specifiers]_block_invoke_7.464
- __41-[VoiceOverActivityController specifiers]_block_invoke_8.466
- __41-[VoiceOverActivityController specifiers]_block_invoke_9.477
- __42-[HandController setPayWithAST:specifier:]_block_invoke.493
- __42-[HandController setPayWithAST:specifier:]_block_invoke.493.cold.1
- __42-[HandController setPayWithAST:specifier:]_block_invoke.500
- __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.675
- __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.675.cold.1
- __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.682
- __53-[SCATController setSwitchScanningEnabled:specifier:]_block_invoke.618
- __54-[AXPearlSettingsController setPearlUnlock:specifier:]_block_invoke.285
- __59-[AXPronunciationEntryViewController _dictateButtonTapped:]_block_invoke.434
- __59-[AXPronunciationEntryViewController _dictateButtonTapped:]_block_invoke.438
- __59-[AXPronunciationEntryViewController _dictateButtonTapped:]_block_invoke.449
- __65-[VoiceOverCommandDetailsViewController _addGestureButtonTapped:]_block_invoke.255
- __68-[VoiceOverActivitySpeechVoiceSelector _showUnifiedSpeechSelection:]_block_invoke.218
- __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.283
- __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.283.cold.1
- __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.289
- __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.289.cold.1
- __75-[ClarityUIAdminPasscodeSetupController _axShowDoneControllerWithPasscode:]_block_invoke.317
- __75-[ClarityUIAdminPasscodeSetupController _axShowDoneControllerWithPasscode:]_block_invoke_2.319
- __83-[VoiceOverCommandsByTouchGestureListController tableView:didSelectRowAtIndexPath:]_block_invoke.216
- __84-[VoiceOverCommandDetailsViewController _addKeyboardShortcutWithSpecifier:resolver:]_block_invoke.259
- __88-[VoiceOverCommandDetailsViewController tableView:commitEditingStyle:forRowAtIndexPath:]_block_invoke.246
- __88-[VoiceOverCommandDetailsViewController tableView:commitEditingStyle:forRowAtIndexPath:]_block_invoke_2.247
- __88-[VoiceOverCommandDetailsViewController tableView:commitEditingStyle:forRowAtIndexPath:]_block_invoke_2.247.cold.1
- __92-[SecureIntentViewController paymentAuthorizationController:didAuthorizeContextWithHandler:]_block_invoke.cold.1
- __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.267
- __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.279
- __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.279.cold.1
- __99-[VoiceOverCommandsByKeyboardShortcutListController _modifyKeyboardShortcutWithSpecifier:resolver:]_block_invoke.233
- ___69-[AccessibilitySettingsController tableView:didSelectRowAtIndexPath:]_block_invoke
- ___AXStringForVariables
- __block_literal_global.217
- __block_literal_global.219
- __block_literal_global.221
- __block_literal_global.223
- __block_literal_global.231
- __block_literal_global.233
- __block_literal_global.234
- __block_literal_global.239
- __block_literal_global.242
- __block_literal_global.246
- __block_literal_global.250
- __block_literal_global.256
- __block_literal_global.259
- __block_literal_global.261
- __block_literal_global.265
- __block_literal_global.268
- __block_literal_global.272
- __block_literal_global.275
- __block_literal_global.276
- __block_literal_global.281
- __block_literal_global.282
- __block_literal_global.284
- __block_literal_global.286
- __block_literal_global.287
- __block_literal_global.288
- __block_literal_global.291
- __block_literal_global.303
- __block_literal_global.307
- __block_literal_global.313
- __block_literal_global.314
- __block_literal_global.319
- __block_literal_global.324
- __block_literal_global.328
- __block_literal_global.333
- __block_literal_global.336
- __block_literal_global.340
- __block_literal_global.346
- __block_literal_global.347
- __block_literal_global.359
- __block_literal_global.361
- __block_literal_global.368
- __block_literal_global.373
- __block_literal_global.374
- __block_literal_global.378
- __block_literal_global.380
- __block_literal_global.393
- __block_literal_global.395
- __block_literal_global.405
- __block_literal_global.408
- __block_literal_global.413
- __block_literal_global.436
- __block_literal_global.441
- __block_literal_global.452
- __block_literal_global.458
- __block_literal_global.479
- __block_literal_global.481
- __block_literal_global.485
- __block_literal_global.491
- __block_literal_global.496
- __block_literal_global.511
- __block_literal_global.599
- __block_literal_global.602
- __block_literal_global.605
- __block_literal_global.610
- __block_literal_global.648
- __block_literal_global.655
- __block_literal_global.678
- _objc_msgSend$_eligibleForApplePayWithAST
- _objc_msgSend$_eligibleForApplePayWithSwitchControl
- _swift_bridgeObjectRelease_n
- _unnamed_array_storage.218
- _unnamed_array_storage.223
- _unnamed_array_storage.234
- _unnamed_array_storage.236
- _unnamed_array_storage.237
- _unnamed_array_storage.239
- _unnamed_array_storage.245
- _unnamed_array_storage.246
- _unnamed_array_storage.248
- _unnamed_array_storage.249
- _unnamed_array_storage.254
- _unnamed_array_storage.255
- _unnamed_array_storage.257
- _unnamed_array_storage.264
- _unnamed_array_storage.267
- _unnamed_array_storage.268
- _unnamed_array_storage.274
- _unnamed_array_storage.277
- _unnamed_array_storage.284
- _unnamed_array_storage.285
- _unnamed_array_storage.286
- _unnamed_array_storage.287
- _unnamed_array_storage.294
- _unnamed_array_storage.295
- _unnamed_array_storage.296
- _unnamed_array_storage.297
- _unnamed_array_storage.304
- _unnamed_array_storage.305
- _unnamed_array_storage.307
- _unnamed_array_storage.313
- _unnamed_array_storage.314
- _unnamed_array_storage.317
- _unnamed_array_storage.324
- _unnamed_array_storage.325
- _unnamed_array_storage.326
- _unnamed_array_storage.327
- _unnamed_array_storage.333
- _unnamed_array_storage.339
- _unnamed_array_storage.340
- _unnamed_array_storage.346
- _unnamed_array_storage.347
- _unnamed_array_storage.353
- _unnamed_array_storage.354
- _unnamed_array_storage.360
- _unnamed_array_storage.361
- _unnamed_array_storage.367
- _unnamed_array_storage.368
- _unnamed_array_storage.374
- _unnamed_array_storage.389
- _unnamed_array_storage.404
- _unnamed_array_storage.407
- _unnamed_array_storage.411
- _unnamed_array_storage.416
- _unnamed_array_storage.417
- _unnamed_array_storage.420
- _unnamed_array_storage.424
- _unnamed_array_storage.426
- _unnamed_array_storage.427
- _unnamed_array_storage.434
- _unnamed_array_storage.437
- _unnamed_array_storage.443
- _unnamed_array_storage.446
- _unnamed_array_storage.494
- _unnamed_array_storage.506
- _unnamed_array_storage.507
- _unnamed_array_storage.518
- _unnamed_array_storage.540
- _unnamed_array_storage.580
- _unnamed_array_storage.581
- _unnamed_array_storage.592
- _unnamed_array_storage.593
- _unnamed_array_storage.596
- _unnamed_array_storage.607
- _unnamed_array_storage.608
- _unnamed_array_storage.614
- _unnamed_array_storage.615
- _unnamed_array_storage.621
- _unnamed_array_storage.622
- _unnamed_array_storage.628
- _unnamed_array_storage.629
- _unnamed_array_storage.635
- _unnamed_array_storage.636
- _unnamed_array_storage.665
- _unnamed_array_storage.666
- _unnamed_array_storage.678
- _unnamed_array_storage.679
- _unnamed_array_storage.706
- get_witness_table 7SwiftUI15ModifiedContentVyAA6ZStackVyAA9TupleViewVyACy21AccessibilitySettings40ClarityOnboardingPreviewRoundedRectangleVAA13_ShadowEffectVG_ACyAA09_VariadicG0O4TreeVy_AA11_LayoutRootVyAA03AnyS0VGAGyACyAjA012_AspectRatioS0VG_ACyAjA010_FlexFrameS0VGtGGAA08_PaddingS0VGtGGA_GAA0G0HPA7_AAA9_HPyHC_A_AA0G8ModifierHPyHCHC.27
- get_witness_table 7SwiftUI15ModifiedContentVyAA6ZStackVyAA9TupleViewVyACyACy21AccessibilitySettings40ClarityOnboardingPreviewRoundedRectangleVAA13_ShadowEffectVGAA14_PaddingLayoutVG_ACyAjA010_FlexFrameR0VGtGGARGAA0G0HPAuaWHPyHC_ArA0G8ModifierHPyHCHC.28
- get_witness_table 7SwiftUI15ModifiedContentVyACy21AccessibilitySettings33ClarityOnboardingDeviceLockScreenVAA12_FrameLayoutVGAA0E18AttachmentModifierVGAA4ViewHPAiaMHPAfaMHPyHC_AhA0pO0HPyHCHC_AkaNHPyHCHC.13
- get_witness_table 7SwiftUI15ModifiedContentVyACy21AccessibilitySettings40ClarityOnboardingDeviceBackgroundAndAppsVAA12_FrameLayoutVGAA0E18AttachmentModifierVGAA4ViewHPAiaMHPAfaMHPyHC_AhA0qP0HPyHCHC_AkaNHPyHCHC.12
- get_witness_table 7SwiftUI15ModifiedContentVyACyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA11_ClipEffectVyAA07RoundedE0VGGAA4ViewHPAkaRHPAeaRHPyHC_AjA0mH0HPyHCHC_ApaSHPyHCHC.29
- get_witness_table 7SwiftUI6ZStackVyAA9TupleViewVyAA15ModifiedContentVyAGyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA11_ClipEffectVyAA07RoundedH0VGG_AGyAGyAGyAA5ImageVAA18_AspectRatioLayoutVGAA06_FrameS0VGATGSgAA6VStackVyAEyAGyAA6SpacerVA0_G_AGy21AccessibilitySettings024ClarityOnboardingPreviewoH0VAA05_FlextS0VGA7_A9_0Y23LockScreenPreviewButtonVtGGtGGAA0E0HPyHC.26
- get_witness_table 7SwiftUI6ZStackVyAA9TupleViewVyAA15ModifiedContentVyAGyAGyAA9RectangleVAA24_ForegroundStyleModifierVyAA5ColorVGGAA11_ClipEffectVyAA07RoundedH0VGGAA07_ShadowN0VG_AGyAGyAA6VStackVyAEyAGyAA6SpacerVAA12_FrameLayoutVG_AA7ForEachVySnySiGSi21AccessibilitySettings33ClarityOnboardingPreviewAppButtonVGtGGAA08_PaddingT0VGAA08_OpacityN0VGAGyAZyAEyA3__AGyAA9LazyVGridVyA10_GA14_GtGGA17_GtGGAA0E0HPyHC.25
CStrings:
+ "%@\n\n%@"
+ "AXVoiceBanking"
+ "AX_ASSET_STATUS_INFO_CELL"
+ "AllowSiri"
+ "Applications"
+ "B24@0:8Q16"
+ "BackTap"
+ "BottomLeft"
+ "BottomRight"
+ "ClarityUIStart"
+ "ConfirmWith"
+ "InitialDelay"
+ "LAStorageKeyDoublePressDisabled"
+ "LAStorageKeySoundEnrollment"
+ "MaximumSpeed"
+ "OptionKeyToggle"
+ "Options"
+ "PasscodeSettings"
+ "ProductID"
+ "Reachability"
+ "SECURE_INTENT_CUSTOM_SOUND_DETAIL"
+ "SECURE_INTENT_CUSTOM_SOUND_ENROLLMENT_LABEL"
+ "SECURE_INTENT_CUSTOM_SOUND_ERROR"
+ "SECURE_INTENT_CUSTOM_SOUND_TITLE"
+ "SIRI_SETTINGS_VOICE_ACTIVATION_HS"
+ "SIRI_SETTINGS_VOICE_ACTIVATION_HS_JS"
+ "SPEECH_RATE_SLIDER"
+ "SWITCH_CONTROL_CANT_USE_WITH_AST"
+ "SWITCH_CONTROL_CANT_USE_WITH_FKA"
+ "SWITCH_CONTROL_CANT_USE_WITH_VOICEOVER"
+ "SecureIntent: KShot Secure Enrollment is enabled."
+ "SecureIntent: Secure Intent did finish but still not authenticated. Will not present training view."
+ "SecureIntent: Secure Intent did finish. Continue training with cached specifier: %@"
+ "SecureIntent: Secure Intent view was cancelled."
+ "SecureIntent: Secure Intent will auto dismiss since device is not setup for Apple Pay. Add a password, touchID, or FaceID to continue."
+ "SecureIntent: Successfully set LAStorageKey: %@ for request source: %@."
+ "SecureIntent: Unable to set LAStorageKey: %@ for request source: %@. Error: %@"
+ "SecureIntent: User has not opted-in to Custom Sound Recognition. Caching specifier: %@ and presenting Secure Intent."
+ "SecureIntentRequestSourceAssistiveTouch"
+ "SecureIntentRequestSourceCustomSoundRecognition"
+ "SecureIntentRequestSourceSwitchControl"
+ "SecureIntentViewControllerDelegate"
+ "ShowBattery"
+ "ShowNotification"
+ "ShowTime"
+ "T@\"NSString\",?,R,C"
+ "TopLeft"
+ "TopRight"
+ "UsePrimaryKeyboard"
+ "Vibration"
+ "VolumeButtons"
+ "Wallpaper"
+ "_authStorageKey"
+ "_customGraphicIconWithSymbol:systemColor:"
+ "_eligibleForApplePay"
+ "_graphicIconForBundleIdentifier:"
+ "_iconImageFromISIcon:"
+ "_logger"
+ "_predefinedGraphicIconNamed:"
+ "_presentKShotOnboardingController:"
+ "_presentKShotOnboardingControllerWithCategory:"
+ "_presentKShotOnboardingControllerWithDetector:"
+ "_presentKShotSecureIntent"
+ "_shouldUseGraphicsRecipes"
+ "_shouldUseKShotEnrollment"
+ "_updateSoundDetectionState"
+ "airpodspro"
+ "arrowtriangles.up.right.down.left.magnifyingglass"
+ "authStorageKeyDescription:"
+ "authStorageKeyForRequestSource:"
+ "captions.bubble.fill"
+ "com.apple.graphic-icon.accessibility"
+ "com.apple.graphic-icon.keyboard"
+ "detectorStore:didFinishPurgingDetectors:wasSuccessful:error:"
+ "dot.square"
+ "ear"
+ "getUserPreferredVoiceTriggerPhraseTypeForDeviceType:endpointId:error:"
+ "hand.point.up.left.fill"
+ "imageForGraphicSymbolDescriptor:"
+ "imageForImageDescriptor:"
+ "imageWithCGImage:"
+ "initWithSize:scale:"
+ "initWithSymbolName:bundleURL:"
+ "initWithSystemColor:"
+ "invalidateIntrinsicContentSize"
+ "isEnrolled"
+ "isEnrolledWithRequestSource:"
+ "localizedCompactTriggerPhraseForLanguageCode:"
+ "q24@0:8Q16"
+ "quote.bubble.fill"
+ "rectangle.3.group.bubble.fill"
+ "requestSourceDescription"
+ "secureIntentViewControllerDidCancel:"
+ "setEnclosureColors:"
+ "setRenderingMode:"
+ "setSymbolColors:"
+ "showPersonalVoiceController:"
+ "speaker.eye.fill"
+ "square.grid.2x2"
+ "textformat.size"
+ "v24@0:8@\"SecureIntentViewController\"16"
+ "voice.control"
+ "waveform.badge.magnifyingglass"
- "/9luHerXthRoPoNt/PVkTg"
- "Unable to set LAStorageKeyDoublePressDisabled: %@"
- "__AXStringForVariablesSentinel"
- "_eligibleForApplePayWithAST"
- "_eligibleForApplePayWithSwitchControl"

```
