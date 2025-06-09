## AXAssetAndDataServer

> `/System/Library/AccessibilityBundles/AXAssetAndDataServer.axuiservice/AXAssetAndDataServer`

```diff

-3148.15.26.0.0
-  __TEXT.__text: 0x50f8
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_stubs: 0x1400
-  __TEXT.__objc_methlist: 0x7bc
-  __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x2d0
-  __TEXT.__oslogstring: 0x5bf
-  __TEXT.__cstring: 0x6ce
+3180.6.1.0.0
+  __TEXT.__text: 0x4604
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_stubs: 0xfa0
+  __TEXT.__objc_methlist: 0x7a4
+  __TEXT.__const: 0x58
+  __TEXT.__gcc_except_tab: 0x298
+  __TEXT.__oslogstring: 0x397
+  __TEXT.__cstring: 0x7ac
   __TEXT.__objc_classname: 0x82
-  __TEXT.__objc_methtype: 0xe64
+  __TEXT.__objc_methtype: 0xe40
   __TEXT.__dlopen_cstrs: 0x127
-  __TEXT.__objc_methname: 0x278a
-  __TEXT.__unwind_info: 0x188
-  __DATA_CONST.__auth_got: 0x2c0
-  __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x258
+  __TEXT.__objc_methname: 0x23a7
+  __TEXT.__unwind_info: 0x170
+  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0x1d8
   __DATA_CONST.__cfstring: 0x680
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x748
-  __DATA.__objc_selrefs: 0x8d8
-  __DATA.__objc_ivar: 0x24
+  __DATA.__objc_const: 0x728
+  __DATA.__objc_selrefs: 0x7c8
+  __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x68

   - /System/Library/PrivateFrameworks/AXSpeechAssetServices.framework/AXSpeechAssetServices
   - /System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport
   - /System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService
+  - /System/Library/PrivateFrameworks/AccessibilityUIShared.framework/AccessibilityUIShared
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/ClarityFoundation.framework/ClarityFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 897FF813-2EDB-3BE9-B7D4-C52F801E35E3
-  Functions: 75
-  Symbols:   154
-  CStrings:  567
+  UUID: 11D85F64-CFEC-3282-8937-BD743C0468D0
+  Functions: 69
+  Symbols:   147
+  CStrings:  521
 
Symbols:
+ _AXTeachableFeatureDisplayTextSize
+ _AXTeachableFeatureEyeTracking
+ _AXTeachableFeatureMotionCues
+ _AXTeachableFeatureMusicHaptics
+ _AXTeachableFeatureReadAndSpeak
+ _AXTeachableFeatureSoundRecognition
+ _AXTeachableFeatureVoiceControl
+ __AXSCommandAndControlEnabled
+ __AXSHapticMusicEnabled
+ __AXSLargeTextUsesExtendedRange
+ __AXSMotionCuesEnabled
+ __AXSOnDeviceEyeTrackingEnabled
+ __AXSSoundDetectionRunning
- _AXCRemapLanguageCodeToFallbackIfNeccessary
- _AXLanguageCanonicalFormToGeneralLanguage
- _AXLanguageConvertToCanonicalForm
- _AXLogSpeechAssetDownload
- _AXSpeechSourceKeySpeechFeatures
- _AXSpeechSourceKeySwitchControl
- _OBJC_CLASS_$_AXAssetsService
- _OBJC_CLASS_$_AXLanguageManager
- _OBJC_CLASS_$_AXUIServiceManager
- _OBJC_CLASS_$_NSLocale
- _OBJC_CLASS_$_SiriTTSDaemonSession
- _OBJC_CLASS_$_TTSAXResourceManager
- _OBJC_CLASS_$_TTSAlternativeVoices
- _OBJC_CLASS_$_TTSSiriAssetManager
- _OBJC_CLASS_$_TTSSpeechSynthesizer
- _TTSGetComponentsInNamedSiriVoiceIdentifier
- __AXSAssistiveTouchScannerEnabled
- __AXSQuickSpeakEnabled
- __AXSZoomSpeakUnderFingerEnabled
- _dispatch_async
CStrings:
+ "initWithIntent:moduleIdentifier:containerBundleIdentifier:moduleSize:"
+ "prefs://root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE"
+ "prefs://root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#DwellEnabledSpecifier"
+ "prefs://root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchMouseDevices"
- "-"
- "@\"AXAssetsService\""
- "@16@?0@\"TTSAXResource\"8"
- "AXAssetAndDataServer: Reset voice subscriptions."
- "AXAssetAndDataServer: Unable to reset voice subscriptions. %@"
- "Asset is installed and is in selected voices: %@"
- "Inform siri about %@"
- "Not updating default spoken content voice because no speech features are enabled."
- "Not updating default spoken content voice because switch control is not enabled."
- "Not updating default voice because the voice doesn't match our system language."
- "Switching voice from %@ to %@ for source %@ because default voice has changed, and the user hasn't selected one for language %@"
- "_"
- "_assetService"
- "_updateDefaultVoiceIfNecessaryForLanguage:sourceKey:"
- "axSafelyAddObjectsFromArray:"
- "ax_flatMappedArrayUsingBlock:"
- "beginTransactionWithIdentifier:forService:"
- "currentLocale"
- "endTransactionWithIdentifier:forService:"
- "footprint"
- "informSiriAboutVoiceUsageForIdentifier:forLanguage:add:"
- "informSiriVoiceSubscriptionsWithVoiceId:addition:"
- "initWithIntent:moduleIdentifier:containerBundleIdentifier:size:"
- "installedAssetsForLanguage:voiceType:"
- "isDefault"
- "isInstalled"
- "isNeuralSiriVoiceIdentifier:"
- "isSiriVoiceIdentifier:"
- "isVocalizerVoiceIdentifier:"
- "languageCode"
- "languages"
- "letterFeedbackEnabled"
- "migrate-siri-list"
- "phoneticFeedbackEnabled"
- "quickTypeWordFeedbackEnabled"
- "resourcesWithLanguage:type:"
- "selectedSpeechVoiceIdentifiers"
- "setSiriAutoUpdateListInitialized:"
- "setSpeechVoiceIdentifier:forLanguage:sourceKey:"
- "sharedServiceManager"
- "speakCorrectionsEnabled"
- "speechVoice"
- "speechVoiceIdentifierForLanguage:sourceKey:exists:"
- "stringByReplacingOccurrencesOfString:withString:"
- "subscribeWithVoices:reply:"
- "systemLanguageID"
- "userDidSelectVoiceForLanguage:sourceKey:"
- "v36@0:8@16@24B32"
- "voiceForIdentifier:"
- "wordFeedbackEnabled"

```
