## AccessibilityDataMigration

> `/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration`

```diff

-3148.15.26.0.0
-  __TEXT.__text: 0x86f4
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_stubs: 0x2180
-  __TEXT.__objc_methlist: 0x374
-  __TEXT.__const: 0xb0
+3180.6.1.0.0
+  __TEXT.__text: 0x2118
+  __TEXT.__auth_stubs: 0x2b0
+  __TEXT.__objc_stubs: 0xe80
+  __TEXT.__objc_methlist: 0x134
+  __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0x13e8
-  __TEXT.__oslogstring: 0x73a
-  __TEXT.__objc_methname: 0x1f8c
+  __TEXT.__cstring: 0x7c2
+  __TEXT.__oslogstring: 0x12a
+  __TEXT.__objc_methname: 0xcd3
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methtype: 0x44
-  __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0xb8
-  __DATA_CONST.__cfstring: 0x1360
+  __TEXT.__unwind_info: 0xd8
+  __DATA_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__const: 0x50
+  __DATA_CONST.__cfstring: 0x6e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0x188
-  __DATA_CONST.__objc_dictobj: 0x140
-  __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0xd0
-  __DATA.__objc_selrefs: 0x8b8
+  __DATA.__objc_selrefs: 0x3f8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
-  - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A045A10A-A0B7-3967-82FD-F742467CE56D
-  Functions: 82
-  Symbols:   169
-  CStrings:  634
+  UUID: 43DAC3BD-53E6-3DDE-9FDA-44667635DFA3
+  Functions: 27
+  Symbols:   82
+  CStrings:  255
 
Symbols:
- _AXAssistiveTouchDefaultIconTypeForMouseButton
- _AXAssistiveTouchIconTypeDwell
- _AXAssistiveTouchIconTypeScroll
- _AXAssistiveTouchInsertIconsIntoDictionary
- _AXColorizeFormatLog
- _AXGetComponentsInOldSiriVoiceIdentifier
- _AXIsAnyPreferredLanguageRTL
- _AXIsInternalInstall
- _AXLanguageCanonicalFormToGeneralLanguage
- _AXLoggerForFacility
- _AXOSLogLevelFromAXLogLevel
- _AXSGuidedAccessAutoLockTimeMirrorSystem
- _AXSpeechSourceKeySpeechFeatures
- _AXSpeechSourceKeySwitchControl
- _AXSpeechSourceKeyVoiceOver
- _CFGetTypeID
- _CFNumberGetTypeID
- _CFPreferencesCopyAppValue
- _CFPreferencesCopyValue
- _CFPreferencesGetAppIntegerValue
- _CFRelease
- _MADisplayFilterPrefSetCategoryEnabled
- _MADisplayFilterPrefSetType
- _NSLog
- _OBJC_CLASS_$_AFLocalization
- _OBJC_CLASS_$_AVSpeechSynthesisVoice
- _OBJC_CLASS_$_AXSubsystemDataMigrator
- _OBJC_CLASS_$_HUHearingAidSettings
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_NSLocale
- _OBJC_CLASS_$_NSMutableSet
- _OBJC_CLASS_$_RTTSettings
- _OBJC_CLASS_$_TTSAlternativeVoices
- _OBJC_CLASS_$_UIKeyboardInputModeController
- _TTSGetComponentsInNamedSiriVoiceIdentifier
- _UIKeyboardInputModeGetLanguageWithRegion
- __AXDarkenSystemColors
- __AXSCopyPreferenceValue
- __AXSHearingAidsSetPaired
- __AXSHomeButtonRestingUnlock
- __AXSHomeButtonRestingUnlockPreferredForDevice
- __AXSLeftRightAudioBalance
- __AXSPointerAllowAppCustomizationSetEnabled
- __AXSPointerEffectScalingSetEnabled
- __AXSPointerIncreasedContrastSetEnabled
- __AXSQuickSpeakSetHighlightTextEnabled
- __AXSReduceMotionEnabled
- __AXSVoiceOverTouchBrailleContractionMode
- __AXSVoiceOverTouchBrailleEightDotMode
- __AXSVoiceOverTouchBrailleMasterStatusCellIndex
- __AXSVoiceOverTouchSetBrailleMasterStatusCellIndex
- __AXSVoiceOverTouchSetShouldRouteToSpeakerWithProximity
- __AXSVoiceOverTouchSetTypingMode
- __AXSetPreferenceWithNotification
- __AXStringForArgs
- __NSConcreteGlobalBlock
- __TTSIdentifierForVoiceInformation
- ___kCFBooleanFalse
- __os_log_default
- __os_log_error_impl
- _kAXSAssistiveTouchScannerSpeechEnabledPreference
- _kAXSAssistiveTouchScannerSpeechRatePreference
- _kAXSAssistiveTouchSpeedDefault
- _kAXSCustomPronunciationSubstitutionsPreference
- _kAXSHearingAidsCloudDenylistPreference
- _kAXSInvertColorsEnabledPreference
- _kAXSLeftRightBalancePreference
- _kAXSQuickSpeakHighlightTextEnabledPreference
- _kAXSRestingHomeButtonUnlockPreference
- _kAXSVoiceOverPitchPreference
- _kAXSVoiceOverPreferenceDomain
- _kAXSVoiceOverTouchRotorItemNavigationDirection
- _kAXSVoiceOverTouchShouldRouteToSpeakerWithProximityPreference
- _kTTSGryphonVoiceIdentifierPrefix
- _kTTSSystemVoiceIdentifierPrefix
- _objc_opt_isKindOfClass
- _objc_opt_respondsToSelector
- _objc_release_x26
- _objc_release_x28
- _objc_retain_x1
- _objc_retain_x22
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x27
- _objc_retain_x8
CStrings:
- "%{public}@"
- "AX: Value for %{public}@ in %{public}@ was not a number, but %@. That's extremely unexpected."
- "AX: migrating audio balance value %@ to AX domain"
- "AXSEnabledSoundDetectionState"
- "AXSEnabledSoundDetectionTypes"
- "AXSSoundDetectionSnoozeDictionary"
- "AXSSoundDetectionSupportedTypes"
- "AXSUltronEnabled"
- "AXSUltronRunningStatus"
- "Aaron"
- "Arthur"
- "Assigned \"Perform long press\" to one finger triple tap."
- "Assigned \"Secondary activate\" to one finger quadruple tap."
- "B32@?0@\"NSDictionary\"8Q16^B24"
- "Catherine"
- "Clearing existing Rest Finger to Open preference."
- "Could not determine old gender, moving on"
- "Could not find names for %@ %@"
- "Daniel"
- "Device prefers Rest Finger to Open. Currently enabled: %i"
- "DeviceMenuItemsVersion"
- "Failed to add one finger quadruple tap for VoiceOver secondary activate."
- "Failed to add one finger triple tap for VoiceOver perform long press."
- "Failed to remove one finger triple tap from VoiceOver secondary activate."
- "GesturedTextInputNextBrailleTable"
- "GesturedTextInputNextKeyboardLanguage"
- "GesturesMenuItemsVersion"
- "Gordon"
- "Hattori"
- "HearingAidsCloudBlacklist"
- "Helena"
- "Idenitified invalid siri voice: %@"
- "Idenitified selected siri voice: %@"
- "Identified selected siri voice: %@"
- "Invalid"
- "InvertColorsEnabled"
- "Li-mu"
- "MADisplayFilterReduceWhitePointIntensity"
- "Made new identifier %@ %@"
- "Marie"
- "Martha"
- "Martin"
- "Migrating emoji enabled preference from %@ to new style"
- "Migrating incorrect voice defaults: "
- "Nicky"
- "Not assigning \"Perform long press\" to one finger triple tap - already assigned to a gesture: %@"
- "Not assigning \"Perform long press\" to one finger triple tap because the gesture is used for a command other than the previous default, \"Secondary activate\": %@"
- "Not assigning \"Secondary activate\" to one finger quadruple tap because another command is assigned to that gesture: %@"
- "Not running 'incorrect voice defaults' migrator, already migrated"
- "Not running 'incorrect voice defaults' migrator, since we have no speech voice identifiers saved"
- "O-ren"
- "OneFingerQuadrupleTap"
- "OneFingerTripleTap"
- "PerformLongPress"
- "Post migrate data: %@"
- "Pre migrate data: %@"
- "PunctuationKey"
- "ReduceWhitePointEnabled"
- "SecondaryActivate"
- "SettingsMenuItemsVersion"
- "SpeakScreenIsHighlightVisible"
- "TopLevelMenuItemsVersion"
- "TwoFingerFlickUp"
- "TypingMode"
- "TypingModeStandard"
- "TypingModeTouchTyping"
- "Upgraded navigation direction rotors"
- "Upgrading navigation direction rotors..."
- "VoiceOverSoundEffectsEnabledPreference"
- "VoiceOverVerbosityEmojisEnabledPreference"
- "Yu-shu"
- "_AccessibilityMigration_ASTMigrateDefaultCustomActions_13.4"
- "_AccessibilityMigration_AXInitialSettingsForPointer_13.4"
- "_AccessibilityMigration_AlwaysShowMenu_13.4"
- "_AccessibilityMigration_BrailleTables_13.0"
- "_AccessibilityMigration_Braille_11.0"
- "_AccessibilityMigration_DisplayFilter_10.0"
- "_AccessibilityMigration_EmojiSuffix_13.0"
- "_AccessibilityMigration_GuidedAccess_13.0"
- "_AccessibilityMigration_IncorrectVoiceDefaults_13.0"
- "_AccessibilityMigration_MigrateAssistiveTouchSpeedSettings_14_3"
- "_AccessibilityMigration_MigrateCustomVoices_14_7"
- "_AccessibilityMigration_MigrateFeedbackOptions_15_0"
- "_AccessibilityMigration_MigrateRestFingerToOpen_14_0"
- "_AccessibilityMigration_MigrateSpeakScreenHighlightSettings_14_2"
- "_AccessibilityMigration_MigrateSwitchSpeechRateSettingsToNewDomain_14_0"
- "_AccessibilityMigration_MigrateVoiceOverVerbosityContainerSettings_14_3"
- "_AccessibilityMigration_MigrateVoices_14_5"
- "_AccessibilityMigration_RemoveNavigationDirectionRotorIfNeeded_9.0"
- "_AccessibilityMigration_Revert\x10_VoiceOverBrailleScreenInputTwoFingerSwipeUp_14.0"
- "_AccessibilityMigration_Speech_10.0"
- "_AccessibilityMigration_TTY_10.0"
- "_AccessibilityMigration_TouchAccommodations_12.0"
- "_AccessibilityMigration_VoiceOverBrailleScreenInputTwoFingerSwipeUp_14.0"
- "_AccessibilityMigration_VoiceOverCommandsForLongPress_13.2"
- "_AccessibilityMigration_Voices_11.0"
- "_AccessibilityMigration_YukonEEnsureInvertColorsPrefHasValidValue_13.4"
- "_AccessibilityMigration_YukonENeuralVoicePref_13.4"
- "_AccessibilityMigration__CleanupGryphonSCVoices_15"
- "_AccessibilityMigration__CleanupGryphonYushu_15"
- "_AccessibilityMigration__MigrateHearingDenylist_15.0"
- "_AccessibilityMigration__MigratePairedHearingAids_13.2"
- "_AccessibilityMigration__MigrateSoundDetection_15"
- "_AccessibilityMigration__PrimeLeftRightBalance_15"
- "__Color__.MADisplayFilterCategoryEnabled"
- "__NONE__"
- "__ReduceWhite__.MADisplayFilterCategoryEnabled"
- "__ReduceWhite__.MADisplayFilterType"
- "_azulBMigrateSpeakScreenHighlightSettings"
- "_azulCMigrateAssistiveTouchSpeedSettings"
- "_azulCMigrateVoiceOverVerbosityContainerSettings"
- "_azulEUpdatesVoicesForSiri"
- "_azulGUpdateCustomVoiceIdentifiers"
- "_azulMigrateRestFingerToOpen"
- "_azulMigrateSwitchAndVOSpeechSettingsToNewDomain"
- "_azulUnmigrateVoiceOverBrailleScreenInputTwoFingerSwipeUp"
- "_clearWhitetailMigrationSettings"
- "_domainNameForDomain:"
- "_eagleMigrateBalanceSettingFromCoreAudio"
- "_monarchClearSwitchControlMenuItemVersionPreferences"
- "_monarchRemoveNavigationDirectionRotorIfNeeded"
- "_okemoMigrateBrailleOutputMode"
- "_okemoMigrateVoiceOverGradeTwoAutoTranslate"
- "_okemoMigrateVoiceOverTypingMode"
- "_peaceMigrateTouchAccommodationsSettings"
- "_quickSpeakAltVoices"
- "_quickSpeakPrefersCompact"
- "_skyClearGryphonYushu"
- "_skyClearIrrelevantSwitchControlVoices"
- "_skyMigrateActionFeedback"
- "_skyMigrateEmojiSetting"
- "_skyMigrateFeedbackOptions"
- "_skyMigrateHearingDenylist"
- "_skyMigrateLinkFeedback"
- "_skyMigrateSoundDetectionSettingsToNewDomain"
- "_skyPrimeLeftRightBalance"
- "_speechVoiceMigrationWhitetail"
- "_speechVoicesIncludingSiri"
- "_switchControlAltVoices"
- "_switchControlPrefersCompact"
- "_switchControlScannerDefaultDialect"
- "_switchVoiceMigrationWhitetail"
- "_tigrisMigrateBrailleStatusCellSettings"
- "_tigrisMigrateSwitchSpeechSettingsToNewDomain"
- "_tigrisMigrateVoiceOverPunctuationSettings"
- "_tigrisMigrateVoicesToNewDomain"
- "_voiceOverAlternativeVoiceIdentifiers"
- "_voiceOverPrefersCompactByLanguage"
- "_voiceOverVoiceMigrationWhitetail"
- "_whitetailMigrateDisplayFilterSettings"
- "_whitetailMigrateTTYSettings"
- "_whitetailMigrateVOTShouldRouteToSpeakerWithProx"
- "_whitetailMigrateVoiceSettings"
- "_yukonBMigrateAssistiveTouchMenuForDwell"
- "_yukonBMigratePairedHearingAids"
- "_yukonBMigrateVoiceOverCommandsForLongPress"
- "_yukonBrailleTablesToMigrateWithKeyboardIdentifiers:"
- "_yukonEEnsureInvertColorsPrefHasValidValue"
- "_yukonEMigrateASTAlwaysShowMenuForDwell"
- "_yukonEMigrateASTCustomActions"
- "_yukonEMigrateNeuralVoicesForInternalInstalls"
- "_yukonESetAXSettingsForPointer"
- "_yukonMigrateBrailleTables"
- "_yukonMigrateEmojiSuffixPreference"
- "_yukonMigrateGuidedAccessSettings"
- "_yukonMigrateIncorrectVoiceDefaults"
- "allValues"
- "anyObject"
- "arrayWithObjects:count:"
- "assistiveTouchMainScreenCustomization"
- "assistiveTouchMouseCustomizedClickActions"
- "assistiveTouchMouseDwellControlEnabled"
- "assistiveTouchMouseDwellControlMutatedMenu"
- "buttonMap"
- "clearExistingValueForPreferenceWithSelector:"
- "com.apple.Accessibility.SwitchControl"
- "com.apple.coreaudio"
- "com.apple.mediaaccessibility"
- "com.apple.springboard"
- "com.apple.ttsbundle.Paulina-compact"
- "com.apple.ttsbundle.Samantha-compact"
- "com.apple.ttsbundle.gryphon_yushu_zh-CN_premium"
- "containsObject:"
- "currentLocale"
- "customActionForButtonNumber:"
- "de-DE"
- "dictionaryWithCapacity:"
- "doubleValue"
- "en"
- "en-AU"
- "en-GB"
- "en-US"
- "enabledInputModeIdentifiers"
- "es"
- "female"
- "firstObject"
- "fr-FR"
- "gestureBindingsForCommand:withResolver:"
- "guidedAccessOverrideIdleTime"
- "hasExistingValueForPreferenceWithSelector:"
- "hasPrefix:"
- "iOS11: Migrating VoiceOver punctuation level : %{public}@"
- "iOS13: Migrating Emoji suffix pref : %{public}@"
- "ignoreLogging"
- "indexOfObjectPassingTest:"
- "indexesOfObjectsPassingTest:"
- "integerValue"
- "isNeuralSiriVoiceIdentifier:"
- "isOldSiriVoiceIdentifier:"
- "isSiriVoiceIdentifier:"
- "ja-JP"
- "language"
- "laserEnabled"
- "length"
- "localeWithLocaleIdentifier:"
- "localizedName"
- "lowercaseString"
- "male"
- "numberWithInteger:"
- "pairedHearingAids"
- "pt"
- "quality"
- "removing default custom actions from %@"
- "selectedSpeechVoiceIdentifiers"
- "selectedSpeechVoiceIdentifiersForSourceKey:"
- "selectedSpeechVoiceIdentifiersWithLanguageSource"
- "set"
- "setAssistiveTouchAlwaysShowMenuEnabled:"
- "setAssistiveTouchMainScreenCustomization:"
- "setAssistiveTouchScannerSpeechEnabled:"
- "setAssistiveTouchScannerSpeechRate:"
- "setAssistiveTouchSpeed:"
- "setCustomAction:forButtonNumber:"
- "setEnabledSoundDetectionTypes:"
- "setGuidedAccessAutoLockTimeInSeconds:"
- "setLeftRightBalanceEnabled:"
- "setLeftRightBalanceValue:"
- "setObject:atIndexedSubscript:"
- "setSelectedSpeechVoiceIdentifiersWithLanguageSource:"
- "setSoundDetectionSnoozeDictionary:"
- "setSoundDetectionState:source:"
- "setSpeechVoiceIdentifier:forLanguage:sourceKey:"
- "setTTYHardwareEnabled:"
- "setTouchAccommodationsAllowsSwipeGesturesToBypass:"
- "setTouchAccommodationsSwipeGestureMinimumDistance:"
- "setUltronIsRunning:"
- "setUltronSupportEnabled:"
- "setVoiceOverActionsFeedback:"
- "setVoiceOverBrailleGradeTwoAutoTranslateEnabled:"
- "setVoiceOverContainerOutputFeedback:"
- "setVoiceOverLinkFeedback:"
- "setVoiceOverPitch:"
- "setVoiceOverPunctuationLevel:"
- "setVoiceOverRotorItems:"
- "setVoiceOverTouchBrailleDisplayOutputMode:"
- "setVoiceOverTouchBrailleShowGeneralStatus:"
- "setVoiceOverVerbosityEmojiFeedback:"
- "setVoiceOverVerbosityEmojiSuffixEnabled:"
- "sharedInputModeController"
- "speechVoiceIdentifierForLanguage:sourceKey:exists:"
- "systemLanguageID"
- "touchAccommodationsHoldDurationAllowsSwipeGesturesToBypass"
- "touchAccommodationsHoldDurationSwipeGestureSensitivity"
- "tty-enabled"
- "updateCustomizableMouse:"
- "user defined actions specified, will skip removing actions for %@"
- "userDidSelectVoiceForLanguage:sourceKey:"
- "voiceNamesForOutputLanguageCode:gender:"
- "voiceOverActionsFeedback"
- "voiceOverBrailleGradeTwoAutoTranslateEnabled"
- "voiceOverContainerOutputFeedback"
- "voiceOverLinkFeedback"
- "voiceOverNavigationDirectionMode"
- "voiceOverRotorItems"
- "voiceOverTouchBrailleDisplayOutputMode"
- "zh-CN"
- "zh_CN"
- "zh_TW"
- "zh_hans"
- "zh_hant"

```
