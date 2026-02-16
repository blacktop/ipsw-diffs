## KeyboardSettings

> `/System/Library/PrivateFrameworks/KeyboardSettings.framework/KeyboardSettings`

```diff

-123.0.0.0.0
-  __TEXT.__text: 0x28e3c
-  __TEXT.__auth_stubs: 0xad0
+123.4.0.0.0
+  __TEXT.__text: 0x29440
+  __TEXT.__auth_stubs: 0xa90
   __TEXT.__objc_methlist: 0x2998
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x2fc
-  __TEXT.__cstring: 0x3645
+  __TEXT.__cstring: 0x3617
   __TEXT.__oslogstring: 0x3
   __TEXT.__dlopen_cstrs: 0x117
   __TEXT.__ustring: 0x52
-  __TEXT.__unwind_info: 0x900
+  __TEXT.__unwind_info: 0x8f8
   __TEXT.__objc_classname: 0x5c7
-  __TEXT.__objc_methname: 0x8a3f
+  __TEXT.__objc_methname: 0x8a33
   __TEXT.__objc_methtype: 0x17f1
-  __TEXT.__objc_stubs: 0x6680
+  __TEXT.__objc_stubs: 0x6660
   __DATA_CONST.__got: 0x740
   __DATA_CONST.__const: 0x798
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22f8
+  __DATA_CONST.__objc_selrefs: 0x22f0
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x2b8
-  __AUTH_CONST.__auth_got: 0x578
-  __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x33a0
+  __AUTH_CONST.__auth_got: 0x558
+  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__cfstring: 0x3360
   __AUTH_CONST.__objc_const: 0x3458
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_intobj: 0x2e8

   __AUTH.__objc_data: 0xaa0
   __DATA.__objc_ivar: 0x1d4
   __DATA.__data: 0x540
-  __DATA.__bss: 0xd8
+  __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3C8AD87C-41DC-3FF6-9F48-DE3A5FF31D9C
-  Functions: 855
-  Symbols:   3463
-  CStrings:  2489
+  UUID: FA624487-8DD4-38BC-9A1A-868B654D61D2
+  Functions: 853
+  Symbols:   3451
+  CStrings:  2484
 
Symbols:
+ GCC_except_table68
+ ___block_literal_global.389
+ ___block_literal_global.729
+ _objc_retainAutoreleasedReturnValue
- -[KSKeyboardController feedbackFeatureEnabled].cold.2
- GCC_except_table69
- ___46-[KSKeyboardController feedbackFeatureEnabled]_block_invoke
- ___block_literal_global.237
- ___block_literal_global.401
- ___block_literal_global.741
- _feedbackFeatureEnabled.is_internal_install
- _feedbackFeatureEnabled.once_token
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$boolForKey:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[KSKeyboardController setKeyboardPreferenceValue:forSpecifier:] : 1552 -> 1560
~ -[KSKeyboardController feedbackFeatureEnabled] : 172 -> 76
- ___46-[KSKeyboardController feedbackFeatureEnabled]_block_invoke
~ -[KSKeyboardController loadPreferenceForInputModeIdentifier:keyboardInputMode:addNewPreferencesToArray:defaultPreferenceIdentifiers:additionalPreferenceIdentifiers:mapPreferenceToInputMode:] : 1480 -> 1464
~ -[KSAddExtensionKeyboardController newSpecifiers] : 696 -> 700
~ -[KSHardwareKeyboardKeyboardTypeRemapController specifiers] : 92 -> 104
~ -[KSHardwareKeyboardKeyboardTypeRemapController reloadSpecifiersWithAnimation] : 116 -> 120
~ -[KSHardwareKeyboardKeyboardTypeRemapController loadKeyboards] : 1844 -> 1892
~ -[KSHardwareKeyboardKeyboardTypeRemapController newSpecifiers] : 160 -> 168
~ -[KSHardwareKeyboardKeyboardTypeRemapController keyboardsSectionSpecifiers] : 1368 -> 1412
~ -[KSHardwareKeyboardKeyboardTypeRemapController keyboardTypeSectionSpecifiers] : 528 -> 544
~ -[KSHardwareKeyboardKeyboardTypeRemapController tableView:cellForRowAtIndexPath:] : 360 -> 372
~ -[KSHardwareKeyboardKeyboardTypeRemapController tableView:didSelectRowAtIndexPath:] : 304 -> 312
~ _IsTrialAssetDeliveryEnabled : 184 -> 192
~ -[KSDictationOfflineStatusObserver updateOfflineDictationStatus] : 144 -> 148
~ ___64-[KSDictationOfflineStatusObserver updateOfflineDictationStatus]_block_invoke_2 : 84 -> 88
~ -[KSAddMultilingualLanguageListController viewWillAppear:] : 188 -> 200
~ -[KSAddMultilingualLanguageListController specifiers] : 92 -> 104
~ -[KSAddMultilingualLanguageListController newSpecifiers] : 532 -> 568
~ ___56-[KSAddMultilingualLanguageListController newSpecifiers]_block_invoke : 112 -> 120
~ -[KSAddMultilingualLanguageListController multilingualSet] : 116 -> 128
~ -[KSAddMultilingualLanguageListController addLanguage:] : 576 -> 620
~ -[KSAddMultilingualLanguageListController reloadKeyboardSpecifiers] : 104 -> 112
~ -[KSAddMultilingualLanguageListController setMultilingualSet:] : 20 -> 80
~ -[KSHardwareKeyboardModifierRemapController specifiers] : 92 -> 104
~ -[KSHardwareKeyboardModifierRemapController subtitleForSpecifier:] : 152 -> 164
~ _attributedTitleForKey : 568 -> 584
~ -[KSHardwareKeyboardModifierRemapController reloadSpecifiersWithAnimation] : 116 -> 120
~ -[KSHardwareKeyboardModifierRemapController loadKeyboards] : 1496 -> 1536
~ -[KSHardwareKeyboardModifierRemapController loadRemapping] : 628 -> 640
~ -[KSHardwareKeyboardModifierRemapController saveRemapping] : 1280 -> 1316
~ -[KSHardwareKeyboardModifierRemapController valueForRemappingKey:] : 104 -> 108
~ -[KSHardwareKeyboardModifierRemapController newSpecifiers] : 372 -> 396
~ -[KSHardwareKeyboardModifierRemapController keyboardsSectionSpecifiers] : 1384 -> 1428
~ -[KSHardwareKeyboardModifierRemapController keysSectionSpecifiers] : 1128 -> 1168
~ -[KSHardwareKeyboardModifierRemapController tableView:cellForRowAtIndexPath:] : 432 -> 460
~ -[KSHardwareKeyboardModifierRemapController tableView:didSelectRowAtIndexPath:] : 256 -> 260
~ -[TIHardwareKeyboardModifierRemapDetailController specifiers] : 92 -> 104
~ -[TIHardwareKeyboardModifierRemapDetailController newSpecifiers] : 808 -> 844
~ -[TIHardwareKeyboardModifierRemapDetailController tableView:cellForRowAtIndexPath:] : 876 -> 940
~ -[TIHardwareKeyboardModifierRemapDetailController tableView:didSelectRowAtIndexPath:] : 256 -> 272
~ ___initializeDictionaries_block_invoke : 936 -> 964
~ -[KSEditUserWordController _unpackTextReplacementError:] : 224 -> 220
~ -[KSEditUserWordController textField:shouldChangeCharactersInRange:replacementString:] : 556 -> 552
~ -[KSListUserWordsController tableView:sectionForSectionIndexTitle:atIndex:] : 256 -> 252
~ _TIUIGetMultilingualIDFromInputMode : 84 -> 92
~ _TIUIInputModeGetMultilingualSetFromInputModes : 444 -> 464
~ _TIUIGetMultlingualSetsAreEqual : 540 -> 568
~ _TIUIGetLanguagesForMultilingualSet : 92 -> 100
~ _TIUIGetOrderedLanguagesForMultilingualSet : 328 -> 340
~ _TIUIKeyboardInputModeGetIdentifierFromComponents : 432 -> 476
~ _TIUIKeyboardGetSupportedSoftwareMultiscriptLayouts : 104 -> 124
~ _TIUIGetPairedInputModesForInputMode : 108 -> 112
~ _TIUICanAddInputModeToMultilingualSet : 500 -> 508
~ _GetDependentMultilingualInputModes : 68 -> 84
~ _TIUIMultilingualSetIsMonoscriptInput : 416 -> 436
~ _TIUIMultilingualSetIsMultiscriptInput : 160 -> 172
~ _TIUIGetAddableInputModesForMultilingualSet : 1276 -> 1316
~ _GetMultilingualInputModes : 108 -> 120
~ _GetRequiredInputModesForDependentInputMode : 128 -> 124
~ _GetBilingualInputModes : 68 -> 84
~ ___TIUIGetAddableInputModesForMultilingualSet_block_invoke : 324 -> 332
~ _TIUIGetProposedMultilingualSetsForAddingInputMode : 3424 -> 3676
~ _GetInputModeIdentifierByMatchingLayoutsAndAddingMultilingualID : 552 -> 596
~ _TIUIGetProposedMultilingualSetByAddingInputMode : 1140 -> 1232
~ _TIUIGetProposedInputModeIsValid : 440 -> 476
~ _TIUIProposedInputModeGetMultilingualSet : 152 -> 172
~ _TIUIGetInputModesByAddingProposedInputMode : 712 -> 744
~ __TIUIMultilingualSetIsMultiscriptInputInOrder : 420 -> 472
~ _TIUIGetCountOfUserVisibleInputModes : 388 -> 404
~ _TIUIGetLocalizedConcatenatedLanguageNamesForInputModesWithStyle : 1080 -> 1168
~ _TIUIMultilingualSetGetLanguageCount : 256 -> 260
~ _TIUIMultilingualSetContainsTransliterationInputModes : 284 -> 292
~ ___GetBilingualInputModes_block_invoke : 440 -> 464
~ +[KSAddKeyboardController shouldShowAddKeyboardControllerForInputModes:] : 348 -> 340
~ -[KSAddKeyboardController koreanEnglishBilingualInputModeIdentifier:enabledInputModes:] : 564 -> 556
~ -[KSKeyboardController feedbackFeatureEnabled].cold.1 : 20 -> 184
- -[KSKeyboardController feedbackFeatureEnabled].cold.2
CStrings:
+ "%s Feedback %@: RC_SEED_BUILD: 1 enabled: %d"
- "%s Feedback %@: RC_SEED_BUILD: 0 enabled: %d"
- "apple-internal-install"
- "boolForKey:"

```
