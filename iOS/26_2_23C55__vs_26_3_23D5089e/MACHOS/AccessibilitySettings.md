## AccessibilitySettings

> `/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-1817.4.10.0.0
+1817.4.11.0.0
   __TEXT.__text: 0x197348
   __TEXT.__auth_stubs: 0x4ed0
   __TEXT.__objc_stubs: 0x252a0
-  __TEXT.__objc_methlist: 0x15a34
+  __TEXT.__objc_methlist: 0x15a4c
   __TEXT.__const: 0x34e4
   __TEXT.__gcc_except_tab: 0x3eb4
   __TEXT.__objc_methname: 0x356cb

   __TEXT.__swift5_types: 0x120
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x34
-  __TEXT.__unwind_info: 0x5eb0
+  __TEXT.__unwind_info: 0x5ec0
   __TEXT.__eh_frame: 0xb90
   __DATA_CONST.__auth_got: 0x2778
   __DATA_CONST.__got: 0x24c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 491A25CA-FFBA-3311-8475-BE5B738D0DCA
-  Functions: 8836
-  Symbols:   20033
+  UUID: F8A1AEF6-3DFD-3B91-BBC3-5E8BFE2F7824
+  Functions: 8838
+  Symbols:   20035
   CStrings:  17162
 
Symbols:
+ -[DetectorsToneController tonePickerViewController:requestsPresentingToneClassicsViewController:animated:]
+ -[GuidedAccessTimeRestrictionsTonePickerViewController tonePickerViewController:requestsPresentingToneClassicsViewController:animated:]
+ __102-[VoiceOverScreenRecognitionController assetController:didFinishRefreshingAssets:wasSuccessful:error:]_block_invoke.325
+ __104-[AXVoiceOverImageDescriptionsController assetController:didFinishRefreshingAssets:wasSuccessful:error:]_block_invoke.407
+ __135-[UIViewController(AXTripleClickConflictAvoidance) accessibilityPerformTripleClickAddingBlockConfirmingSOSConflicts:cancellationBlock:]_block_invoke.491
+ __146-[ClarityUIController _checkExistenceOfSettingsForAppSpecifier:identifier:bundleIdentifiersCheckingExistenceOfSettings:specifiersRequiringReload:]_block_invoke.566
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke.296
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke.302
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_2.297
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_2.304
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_3.298
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_3.305
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_4.299
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_4.306
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_5.300
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_5.310
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_6.301
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_6.314
+ __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_7.318
+ __28-[HandController specifiers]_block_invoke.463
+ __38-[AXHapticMusicController viewDidLoad]_block_invoke.292
+ __40-[VoiceOverAwarenessController loadView]_block_invoke.339
+ __41-[VoiceOverActivityController specifiers]_block_invoke.496
+ __41-[VoiceOverActivityController specifiers]_block_invoke.531
+ __41-[VoiceOverActivityController specifiers]_block_invoke_10.588
+ __41-[VoiceOverActivityController specifiers]_block_invoke_11.589
+ __41-[VoiceOverActivityController specifiers]_block_invoke_12.590
+ __41-[VoiceOverActivityController specifiers]_block_invoke_13.604
+ __41-[VoiceOverActivityController specifiers]_block_invoke_14.605
+ __41-[VoiceOverActivityController specifiers]_block_invoke_15.613
+ __41-[VoiceOverActivityController specifiers]_block_invoke_16.614
+ __41-[VoiceOverActivityController specifiers]_block_invoke_17.622
+ __41-[VoiceOverActivityController specifiers]_block_invoke_18.623
+ __41-[VoiceOverActivityController specifiers]_block_invoke_2.500
+ __41-[VoiceOverActivityController specifiers]_block_invoke_2.532
+ __41-[VoiceOverActivityController specifiers]_block_invoke_3.546
+ __41-[VoiceOverActivityController specifiers]_block_invoke_4.547
+ __41-[VoiceOverActivityController specifiers]_block_invoke_5.555
+ __41-[VoiceOverActivityController specifiers]_block_invoke_6.556
+ __41-[VoiceOverActivityController specifiers]_block_invoke_7.566
+ __41-[VoiceOverActivityController specifiers]_block_invoke_8.571
+ __41-[VoiceOverActivityController specifiers]_block_invoke_9.576
+ __42-[HandController setPayWithAST:specifier:]_block_invoke.661
+ __42-[HandController setPayWithAST:specifier:]_block_invoke.661.cold.1
+ __42-[HandController setPayWithAST:specifier:]_block_invoke.668
+ __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.849
+ __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.849.cold.1
+ __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.856
+ __53-[SCATController setSwitchScanningEnabled:specifier:]_block_invoke.790
+ __54-[AXPearlSettingsController setPearlUnlock:specifier:]_block_invoke.353
+ __57-[AXHapticMusicController _fetchUpdatePlayingInformation]_block_invoke.431
+ __59-[AXPronunciationEntryViewController _dictateButtonTapped:]_block_invoke.515
+ __59-[AXPronunciationEntryViewController _dictateButtonTapped:]_block_invoke.519
+ __59-[AXPronunciationEntryViewController _dictateButtonTapped:]_block_invoke.530
+ __61-[SoundDetectionController updateDetectorSpecifiersAnimated:]_block_invoke.399
+ __65-[VoiceOverCommandDetailsViewController _addGestureButtonTapped:]_block_invoke.324
+ __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.370
+ __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.370.cold.1
+ __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.376
+ __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.376.cold.1
+ __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.382
+ __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.382.cold.1
+ __75-[ClarityUIAdminPasscodeSetupController _axShowDoneControllerWithPasscode:]_block_invoke.386
+ __75-[ClarityUIAdminPasscodeSetupController _axShowDoneControllerWithPasscode:]_block_invoke_2.388
+ __83-[VoiceOverCommandsByTouchGestureListController tableView:didSelectRowAtIndexPath:]_block_invoke.285
+ __84-[VoiceOverCommandDetailsViewController _addKeyboardShortcutWithSpecifier:resolver:]_block_invoke.328
+ __88-[VoiceOverCommandDetailsViewController tableView:commitEditingStyle:forRowAtIndexPath:]_block_invoke.315
+ __88-[VoiceOverCommandDetailsViewController tableView:commitEditingStyle:forRowAtIndexPath:]_block_invoke_2.316
+ __88-[VoiceOverCommandDetailsViewController tableView:commitEditingStyle:forRowAtIndexPath:]_block_invoke_2.316.cold.1
+ __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.331
+ __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.342
+ __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.342.cold.1
+ __99-[VoiceOverCommandsByKeyboardShortcutListController _modifyKeyboardShortcutWithSpecifier:resolver:]_block_invoke.301
+ __block_literal_global.286
+ __block_literal_global.288
+ __block_literal_global.290
+ __block_literal_global.292
+ __block_literal_global.300
+ __block_literal_global.302
+ __block_literal_global.303
+ __block_literal_global.306
+ __block_literal_global.308
+ __block_literal_global.314
+ __block_literal_global.316
+ __block_literal_global.321
+ __block_literal_global.327
+ __block_literal_global.334
+ __block_literal_global.337
+ __block_literal_global.345
+ __block_literal_global.349
+ __block_literal_global.350
+ __block_literal_global.353
+ __block_literal_global.356
+ __block_literal_global.357
+ __block_literal_global.360
+ __block_literal_global.372
+ __block_literal_global.374
+ __block_literal_global.376
+ __block_literal_global.378
+ __block_literal_global.384
+ __block_literal_global.388
+ __block_literal_global.394
+ __block_literal_global.396
+ __block_literal_global.407
+ __block_literal_global.410
+ __block_literal_global.417
+ __block_literal_global.424
+ __block_literal_global.425
+ __block_literal_global.427
+ __block_literal_global.441
+ __block_literal_global.442
+ __block_literal_global.444
+ __block_literal_global.445
+ __block_literal_global.447
+ __block_literal_global.464
+ __block_literal_global.465
+ __block_literal_global.466
+ __block_literal_global.467
+ __block_literal_global.469
+ __block_literal_global.482
+ __block_literal_global.488
+ __block_literal_global.493
+ __block_literal_global.495
+ __block_literal_global.501
+ __block_literal_global.503
+ __block_literal_global.513
+ __block_literal_global.515
+ __block_literal_global.531
+ __block_literal_global.533
+ __block_literal_global.538
+ __block_literal_global.553
+ __block_literal_global.557
+ __block_literal_global.577
+ __block_literal_global.580
+ __block_literal_global.582
+ __block_literal_global.587
+ __block_literal_global.595
+ __block_literal_global.597
+ __block_literal_global.639
+ __block_literal_global.657
+ __block_literal_global.659
+ __block_literal_global.664
+ __block_literal_global.674
+ __block_literal_global.679
+ __block_literal_global.697
+ __block_literal_global.700
+ __block_literal_global.705
+ __block_literal_global.723
+ __block_literal_global.852
+ __block_literal_global.927
+ __block_literal_global.954
- __102-[VoiceOverScreenRecognitionController assetController:didFinishRefreshingAssets:wasSuccessful:error:]_block_invoke.334
- __104-[AXVoiceOverImageDescriptionsController assetController:didFinishRefreshingAssets:wasSuccessful:error:]_block_invoke.416
- __135-[UIViewController(AXTripleClickConflictAvoidance) accessibilityPerformTripleClickAddingBlockConfirmingSOSConflicts:cancellationBlock:]_block_invoke.500
- __146-[ClarityUIController _checkExistenceOfSettingsForAppSpecifier:identifier:bundleIdentifiersCheckingExistenceOfSettings:specifiersRequiringReload:]_block_invoke.575
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke.305
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke.311
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_2.306
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_2.313
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_3.307
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_3.314
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_4.308
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_4.315
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_5.309
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_5.319
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_6.310
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_6.323
- __146-[VOSCommandManager(VoiceOverCustomCommandsExtras) applyAction:toCommand:withGesture:keyboardShortcut:resolver:presentationController:completion:]_block_invoke_7.327
- __28-[HandController specifiers]_block_invoke.472
- __38-[AXHapticMusicController viewDidLoad]_block_invoke.301
- __40-[VoiceOverAwarenessController loadView]_block_invoke.348
- __41-[VoiceOverActivityController specifiers]_block_invoke.505
- __41-[VoiceOverActivityController specifiers]_block_invoke.540
- __41-[VoiceOverActivityController specifiers]_block_invoke_10.597
- __41-[VoiceOverActivityController specifiers]_block_invoke_11.598
- __41-[VoiceOverActivityController specifiers]_block_invoke_12.599
- __41-[VoiceOverActivityController specifiers]_block_invoke_13.613
- __41-[VoiceOverActivityController specifiers]_block_invoke_14.614
- __41-[VoiceOverActivityController specifiers]_block_invoke_15.622
- __41-[VoiceOverActivityController specifiers]_block_invoke_16.623
- __41-[VoiceOverActivityController specifiers]_block_invoke_17.631
- __41-[VoiceOverActivityController specifiers]_block_invoke_18.632
- __41-[VoiceOverActivityController specifiers]_block_invoke_2.509
- __41-[VoiceOverActivityController specifiers]_block_invoke_2.541
- __41-[VoiceOverActivityController specifiers]_block_invoke_3.555
- __41-[VoiceOverActivityController specifiers]_block_invoke_4.556
- __41-[VoiceOverActivityController specifiers]_block_invoke_5.564
- __41-[VoiceOverActivityController specifiers]_block_invoke_6.565
- __41-[VoiceOverActivityController specifiers]_block_invoke_7.575
- __41-[VoiceOverActivityController specifiers]_block_invoke_8.580
- __41-[VoiceOverActivityController specifiers]_block_invoke_9.585
- __42-[HandController setPayWithAST:specifier:]_block_invoke.670
- __42-[HandController setPayWithAST:specifier:]_block_invoke.670.cold.1
- __42-[HandController setPayWithAST:specifier:]_block_invoke.677
- __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.858
- __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.858.cold.1
- __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.865
- __53-[SCATController setSwitchScanningEnabled:specifier:]_block_invoke.799
- __54-[AXPearlSettingsController setPearlUnlock:specifier:]_block_invoke.362
- __57-[AXHapticMusicController _fetchUpdatePlayingInformation]_block_invoke.440
- __59-[AXPronunciationEntryViewController _dictateButtonTapped:]_block_invoke.524
- __59-[AXPronunciationEntryViewController _dictateButtonTapped:]_block_invoke.528
- __59-[AXPronunciationEntryViewController _dictateButtonTapped:]_block_invoke.539
- __61-[SoundDetectionController updateDetectorSpecifiersAnimated:]_block_invoke.408
- __65-[VoiceOverCommandDetailsViewController _addGestureButtonTapped:]_block_invoke.333
- __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.379
- __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.379.cold.1
- __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.385
- __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.385.cold.1
- __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.391
- __73-[ClarityUISettingsWrapperController _axValidateAuthenticationController]_block_invoke.391.cold.1
- __75-[ClarityUIAdminPasscodeSetupController _axShowDoneControllerWithPasscode:]_block_invoke.395
- __75-[ClarityUIAdminPasscodeSetupController _axShowDoneControllerWithPasscode:]_block_invoke_2.397
- __83-[VoiceOverCommandsByTouchGestureListController tableView:didSelectRowAtIndexPath:]_block_invoke.294
- __84-[VoiceOverCommandDetailsViewController _addKeyboardShortcutWithSpecifier:resolver:]_block_invoke.337
- __88-[VoiceOverCommandDetailsViewController tableView:commitEditingStyle:forRowAtIndexPath:]_block_invoke.324
- __88-[VoiceOverCommandDetailsViewController tableView:commitEditingStyle:forRowAtIndexPath:]_block_invoke_2.325
- __88-[VoiceOverCommandDetailsViewController tableView:commitEditingStyle:forRowAtIndexPath:]_block_invoke_2.325.cold.1
- __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.340
- __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.351
- __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.351.cold.1
- __99-[VoiceOverCommandsByKeyboardShortcutListController _modifyKeyboardShortcutWithSpecifier:resolver:]_block_invoke.310
- __block_literal_global.295
- __block_literal_global.297
- __block_literal_global.299
- __block_literal_global.301
- __block_literal_global.309
- __block_literal_global.312
- __block_literal_global.317
- __block_literal_global.323
- __block_literal_global.324
- __block_literal_global.325
- __block_literal_global.336
- __block_literal_global.338
- __block_literal_global.339
- __block_literal_global.343
- __block_literal_global.346
- __block_literal_global.354
- __block_literal_global.358
- __block_literal_global.362
- __block_literal_global.365
- __block_literal_global.368
- __block_literal_global.369
- __block_literal_global.375
- __block_literal_global.381
- __block_literal_global.383
- __block_literal_global.385
- __block_literal_global.387
- __block_literal_global.402
- __block_literal_global.403
- __block_literal_global.405
- __block_literal_global.406
- __block_literal_global.416
- __block_literal_global.426
- __block_literal_global.433
- __block_literal_global.436
- __block_literal_global.437
- __block_literal_global.443
- __block_literal_global.450
- __block_literal_global.451
- __block_literal_global.453
- __block_literal_global.454
- __block_literal_global.456
- __block_literal_global.473
- __block_literal_global.475
- __block_literal_global.483
- __block_literal_global.485
- __block_literal_global.487
- __block_literal_global.497
- __block_literal_global.500
- __block_literal_global.502
- __block_literal_global.504
- __block_literal_global.510
- __block_literal_global.512
- __block_literal_global.522
- __block_literal_global.524
- __block_literal_global.542
- __block_literal_global.547
- __block_literal_global.549
- __block_literal_global.562
- __block_literal_global.566
- __block_literal_global.586
- __block_literal_global.589
- __block_literal_global.591
- __block_literal_global.604
- __block_literal_global.605
- __block_literal_global.606
- __block_literal_global.648
- __block_literal_global.666
- __block_literal_global.668
- __block_literal_global.673
- __block_literal_global.683
- __block_literal_global.688
- __block_literal_global.706
- __block_literal_global.709
- __block_literal_global.714
- __block_literal_global.732
- __block_literal_global.861
- __block_literal_global.936
- __block_literal_global.963
Functions:
+ -[GuidedAccessTimeRestrictionsTonePickerViewController tonePickerViewController:requestsPresentingToneClassicsViewController:animated:]
+ -[DetectorsToneController tonePickerViewController:requestsPresentingToneClassicsViewController:animated:]
~ -[AXAudioController setAudioLeftRightBalance:specifier:] : 560 -> 536

```
