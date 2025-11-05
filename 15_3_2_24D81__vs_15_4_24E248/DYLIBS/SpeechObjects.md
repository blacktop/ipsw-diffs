## SpeechObjects

> `/System/Library/PrivateFrameworks/SpeechObjects.framework/Versions/A/SpeechObjects`

```diff

 9.0.72.0.0
-  __TEXT.__text: 0x19374
+  __TEXT.__text: 0x19490
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x17b8
+  __TEXT.__objc_methlist: 0x1958
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x357f
   __TEXT.__dlopen_cstrs: 0x72

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13d0
+  __DATA_CONST.__objc_selrefs: 0x14a0
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x358
   __AUTH_CONST.__const: 0x1d0
   __AUTH_CONST.__cfstring: 0x3120
-  __AUTH_CONST.__objc_const: 0x3618
+  __AUTH_CONST.__objc_const: 0x3320
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x870

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 01155048-16A8-374A-8E6F-FA327F112B96
-  Functions: 511
-  Symbols:   1705
+  UUID: 9A8FA653-AC2D-3E24-85FC-358F19F0F579
+  Functions: 519
+  Symbols:   1714
   CStrings:  1844
 
Symbols:
+ +[SOSpeechInstallationManager sharedManager].cold.1
+ +[SOSpeechItem componentsFromLocaleIdentifier:].cold.1
+ +[SOSystemBehaviorManager sharedSOSystemBehaviorManager].cold.1
+ -[NSLocale(DisplayName) displayNameForKey:value:options:].cold.1
+ -[NSLocale(DisplayName) displayNameForKey:value:options:].cold.2
+ -[SOSpeechItem _conversionLocale].cold.1
+ -[SOVoiceObject _conversionLocale].cold.1
+ -[SOVoiceObject _voiceNamesEntryFromSpeechSynthesisFrameworkForVoiceName:].cold.1
+ SOOSLog.cold.1
Functions:
~ -[VoiceSettingsWindowController setUpWindowWithVoiceSettings:modalDelegate:] : 1180 -> 1168
~ -[VoiceSettingsWindowController saveVoiceSettings:] : 204 -> 200
~ -[NSSpeechSynthesizer(NSSpeechSynthesizerExtensions) speechPitch] : 92 -> 80
~ -[SOSRSimpleLanguagePopUpButton buildPopUpButtonAndSelectLocaleIdentifier:supportedLocaleIdentifiers:] : 1696 -> 1688
~ ___36-[SOVoicePopUpButton initWithCoder:]_block_invoke : 964 -> 972
~ -[SOVoicePopUpButton sendAction:to:] : 496 -> 492
~ -[SOVoicePopUpButton buildPopUpButtonWithSelectVoiceIdentifier:] : 2452 -> 2464
~ -[SOVoicePopUpButton selectedVoiceAttributes] : 428 -> 440
~ -[SOVoicePopUpButton isSelectedVoiceAppropriateForCurrentLanguageWithUserConfirmation:parentWindowForSheet:] : 932 -> 956
~ -[SODownloadDisplayManager timeRemainingForActiveInstallations:withTagPrefix:] : 756 -> 764
~ -[CustomizeVoicesWindowController _rebuildVoiceList] : 1056 -> 1064
~ -[CustomizeVoicesWindowController _propagateCheckboxSelection:] : 1008 -> 1012
~ -[CustomizeVoicesWindowController _updateRowDownloadStatus] : 700 -> 704
~ -[CustomizeVoicesWindowController tableView:viewForTableColumn:row:] : 880 -> 884
~ _SOOSLog : 68 -> 56
~ +[SOVoiceObject visibleVoicesForLocaleIdentifier:additionalRequiredVoices:allowAllVoices:] : 800 -> 804
~ -[SOVoiceObject _displayLocalizedVoiceNameForString:] : 348 -> 340
~ -[SOVoiceObject compare:] : 160 -> 152
~ -[SOVoiceObject _conversionLocale] : 68 -> 56
~ -[SOVoiceObject _voiceNamesEntryFromSpeechSynthesisFrameworkForVoiceName:] : 112 -> 96
~ -[VoiceTableRow description] : 24 -> 28
~ -[SOCustomizeSRLanguagesWindowController showSheetForWindow:networkSupportedLocaleIdentifiers:requiredLocaleIdentifier:supportDownloads:showOnlyNetworkSupportedItems:] : 488 -> 492
~ -[SOCustomizeSRLanguagesWindowController acceptSelection:] : 1488 -> 1500
~ -[SOCustomizeSRLanguagesWindowController _propagateCheckboxSelection:] : 684 -> 688
~ -[SOCustomizeSRLanguagesWindowController _updateRowDownloadStatus] : 744 -> 760
~ -[SOCustomizeSRLanguagesWindowController _setRowStatusFieldView:variantPopUpButton:speechItem:isSelected:] : 812 -> 816
~ +[SOSystemBehaviorManager sharedSOSystemBehaviorManager] : 68 -> 56
~ -[SOSRLanguagePopUpButton buildPopUpButtonAndSelectLocaleIdentifier:networkSupportedLocaleIdentifiers:offlineSupportedLocaleIdentifiers:] : 1712 -> 1740
~ -[SOSRLanguageRow description] : 24 -> 28
~ +[SOSpeechItem componentsFromLocaleIdentifier:] : 200 -> 184
~ -[SOSpeechItem displayTitle] : 196 -> 200
~ -[SOSpeechItem _conversionLocale] : 68 -> 56
~ +[SOSpeechInstallationManager sharedManager] : 68 -> 56
~ -[SOSpeechInstallationManager _startDownloadingHighestQualityIfNecessaryForVoiceIdentifier:requireACPower:initiator:] : 1700 -> 1696
~ -[SOSpeechInstallationManager bundleForRemovableLanguage:passingBackTagName:] : 244 -> 248
~ -[NSLocale(DisplayName) displayNameForKey:value:options:] : 1076 -> 992
- sub_1c8ce6e9c

```
