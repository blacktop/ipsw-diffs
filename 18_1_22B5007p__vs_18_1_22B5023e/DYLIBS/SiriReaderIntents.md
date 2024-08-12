## SiriReaderIntents

> `/System/Library/PrivateFrameworks/SiriReaderIntents.framework/SiriReaderIntents`

```diff

 3400.5.1.0.0
-  __TEXT.__text: 0x11fb0
-  __TEXT.__auth_stubs: 0xe00
+  __TEXT.__text: 0x11b4c
+  __TEXT.__auth_stubs: 0xdf0
   __TEXT.__objc_methlist: 0x80
   __TEXT.__const: 0x7f2
   __TEXT.__cstring: 0x7e6
-  __TEXT.__swift5_typeref: 0x468
+  __TEXT.__swift5_typeref: 0x466
   __TEXT.__constg_swiftt: 0x358
   __TEXT.__swift5_reflstr: 0x297
   __TEXT.__swift5_fieldmd: 0x2e0

   __TEXT.__swift5_assocty: 0x60
   __TEXT.__oslogstring: 0x91d
   __TEXT.__swift5_capture: 0x88
-  __TEXT.__unwind_info: 0x590
-  __TEXT.__eh_frame: 0x918
+  __TEXT.__unwind_info: 0x5b0
+  __TEXT.__eh_frame: 0x958
   __TEXT.__objc_classname: 0xb7
   __TEXT.__objc_methname: 0x6b0
   __TEXT.__objc_methtype: 0x433
   __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf8
   __DATA_CONST.__objc_protorefs: 0x68
-  __AUTH_CONST.__auth_got: 0x700
+  __AUTH_CONST.__auth_got: 0x6f8
   __AUTH_CONST.__auth_ptr: 0x2d8
   __AUTH_CONST.__const: 0x458
   __AUTH_CONST.__objc_const: 0x1840

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 482
-  Symbols:   296
-  CStrings:  206
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 477
+  Symbols:   298
+  CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _objc_retain_x27
CStrings:
- "OBJC_CLASS_$_SiriTTSSynthesisEngineWordTimings"
- "SessionManager"
- "_AFAnalyticsEventTypeGetName"
- "_AFAssistantRestricted"
- "_AFAudioSessionAssertionGetCurrentAcquisitionService"
- "_AFDeviceRingerSwitchStateGetName"
- "_AFDeviceSupportsHybridUOD"
- "_AFDeviceSupportsSiriMUX"
- "_AFDeviceSupportsSiriUOD"
- "_AFDictationRestricted"
- "_AFErrorEnumerate"
- "_AFErrorSetUnderlyingError"
- "_AFHasUnlockedSinceBoot"
- "_AFIsCustomerInstall"
- "_AFLogDirectory"
- "_AFLogInitIfNeeded"
- "_AFNavigationStateIsNavigating"
- "_AFOfflineDictationCapable"
- "_AFPreferencesATVStopRecordingDelay"
- "_AFPreferencesAlwaysEyesFreeEnabled"
- "_AFPreferencesAssistantEnabled"
- "_AFPreferencesLanguageIsSupported"
- "_AFPreferencesMobileUserSessionLanguage"
- "_AFPreferencesMultiUserCompanionNotificationLanguageCodesForHomePodVersion"
- "_AFPreferencesStartAlertEnabled"
- "_AFPreferencesStreamingDictationEnabled"
- "_AFPreferencesSupportedDictationLanguages"
- "_AFPreferencesSupportedLanguages"
- "_AFPreferencesSupportedLanguagesForRemote"
- "_AFPreferencesSupportedMultiUserLanguages"
- "_AFPreferencesTypeToSiriEnabled"
- "_AFRecordCoreDuetEvent"
- "_AFRecordCoreDuetEventWithStream"
- "_AFSiriActivationSourceGetName"
- "_AFSiriUserNotificationAnnouncementSpeakingStateGetName"
- "_AFSpeechEndpointerOperationModeGetIsValid"
- "_AFSpeechEndpointerOperationModeGetName"
- "_AFSpeechEventGetDescription"
- "_AFSpeechEventIsHardwareTrigger"
- "_AFSpeechEventIsTVRemote"
- "_AFSpeechEventIsVoiceTrigger"
- "_AFSpeechLogsDirectory"
- "_AFSpeechRecordingEventListenerGetXPCInterface"
- "_AFSupportPreferencesSynchronize"
- "_AFTurnIdentifierGenerate"
- "_AFTurnIdentifierGetBytes"
- "_AFTurnIdentifierGetString"
- "_AFVoiceGenderGetName"
- "_MTTimer"
- "_OBJC_CLASS_$_DistributedNotificationPoster"
- "_OBJC_CLASS_$_MTAgentNotification"
- "_OBJC_CLASS_$_MTAlarm"
- "_OBJC_CLASS_$_MTAlarmCache"
- "_OBJC_CLASS_$_MTAlarmManager"
- "_OBJC_CLASS_$_MTAlarmManagerExportedObject"
- "_OBJC_CLASS_$_MTBaseAlarmWidgetProvider"
- "_OBJC_CLASS_$_MTCFUserNotificationPoster"
- "_OBJC_CLASS_$_MTChange"
- "_OBJC_CLASS_$_MTChangeSet"
- "_OBJC_CLASS_$_MTCityResolutionResult"
- "_OBJC_CLASS_$_MTCompanionSyncRequest"
- "_OBJC_CLASS_$_MTCompanionSyncSession"
- "_OBJC_CLASS_$_MTCreateAlarmIntentResponse"
- "_OBJC_CLASS_$_MTCreateSingleTimerIntentHandler"
- "_OBJC_CLASS_$_MTDateFormatting"
- "_OBJC_CLASS_$_MTDictionaryDeserializer"
- "_OBJC_CLASS_$_MTDictionarySerializer"
- "_OBJC_CLASS_$_MTExpiringFuture"
- "_OBJC_CLASS_$_MTGCDTimer"
- "_OBJC_CLASS_$_MTGetAlarmsIntentHandler"
- "_OBJC_CLASS_$_MTInMemorySyncChangeStore"
- "_OBJC_CLASS_$_MTMetrics"
- "_OBJC_CLASS_$_MTNextAlarm"
- "_OBJC_CLASS_$_MTNextAlarmManager"
- "_OBJC_CLASS_$_MTPBAlarmState"
- "_OBJC_CLASS_$_MTPBAlarmUpdate"
- "_OBJC_CLASS_$_MTPBDismissAction"
- "_OBJC_CLASS_$_MTPairedDevicePreferences"
- "_OBJC_CLASS_$_MTPowerAssertion"
- "_OBJC_CLASS_$_MTResetTimerIntentHandler"
- "_OBJC_CLASS_$_MTScheduledObject"
- "_OBJC_CLASS_$_MTSearchTimerIntentHandler"
- "_OBJC_CLASS_$_MTSessionManager"
- "_OBJC_CLASS_$_MTSessionManagerExportedObject"
- "_OBJC_CLASS_$_MTSessionServer"
- "_OBJC_CLASS_$_MTSessionsCoordinator"
- "_OBJC_CLASS_$_MTSleepCoordinatorStateMachineDisabledState"
- "_OBJC_CLASS_$_MTSleepModeStateMachineOnState"
- "_OBJC_CLASS_$_MTSleepModeStateMachineState"
- "_OBJC_CLASS_$_MTSleepModeStateMachineWaitingState"
- "_OBJC_CLASS_$_MTSleepUtilities"
- "_OBJC_CLASS_$_MTSound"
- "_OBJC_CLASS_$_MTStateMachine"
- "_OBJC_CLASS_$_MTStateMachineState"
- "_OBJC_CLASS_$_MTTask"
- "_OBJC_CLASS_$_MTTaskGroup"
- "_OBJC_CLASS_$_MTTimerDataSource"
- "_OBJC_CLASS_$_MTTimerDurationManager"
- "_OBJC_CLASS_$_MTTimerIntentHandler"
- "_OBJC_CLASS_$_MTUpdateTimerIntentHandler"
- "_OBJC_CLASS_$_MTWidgetProvider"
- "_OBJC_CLASS_$_MTWorldClock"
- "_OBJC_CLASS_$_MTWorldClockResolutionResult"
- "_OBJC_CLASS_$_MTXPCConnectionInfo"
- "_OBJC_CLASS_$_MTXPCConnectionProvider"
- "_OBJC_CLASS_$_NotificationRelay"
- "_OBJC_CLASS_$_SiriTTSAudioHintRequest"
- "_OBJC_CLASS_$_SiriTTSDaemonSession"
- "_OBJC_CLASS_$_SiriTTSPreviewRequest"
- "_OBJC_CLASS_$_SiriTTSSpeechRequest"
- "_OBJC_CLASS_$_SiriTTSSynthesisEngine"
- "_OBJC_CLASS_$_SiriTTSSynthesisEngineRequest"
- "_OBJC_CLASS_$_SiriTTSSynthesisEngineResource"
- "_OBJC_CLASS_$_SiriTTSSynthesisRequest"
- "_OBJC_CLASS_$_TTSAsset"
- "_OBJC_CLASS_$_TTSAssetQuality"
- "_OBJC_CLASS_$_TTSAssetSource"
- "_OBJC_CLASS_$_TTSAssetTechnology"
- "_OBJC_CLASS_$_TTSAssetType"
- "_OBJC_CLASS_$_TTSStringEnum"
- "_OBJC_CLASS_$_WorldClockCity"
- "_OBJC_METACLASS_$_DistributedNotificationPoster"
- "_OBJC_METACLASS_$_MTAgentNotification"
- "_OBJC_METACLASS_$_MTAlarm"
- "_OBJC_METACLASS_$_MTAlarmCache"
- "_OBJC_METACLASS_$_MTAlarmManager"
- "_OBJC_METACLASS_$_MTAlarmManagerExportedObject"
- "_OBJC_METACLASS_$_MTBaseAlarmWidgetProvider"
- "_OBJC_METACLASS_$_MTCFUserNotificationPoster"
- "_OBJC_METACLASS_$_MTChange"
- "_OBJC_METACLASS_$_MTChangeSet"
- "_OBJC_METACLASS_$_MTCityResolutionResult"
- "_OBJC_METACLASS_$_MTCompanionSyncSession"
- "_OBJC_METACLASS_$_MTCreateAlarmIntentResponse"
- "_OBJC_METACLASS_$_MTCreateSingleTimerIntentHandler"
- "_OBJC_METACLASS_$_MTDateFormatting"
- "_OBJC_METACLASS_$_MTDictionaryDeserializer"
- "_OBJC_METACLASS_$_MTDictionarySerializer"
- "_OBJC_METACLASS_$_MTExpiringFuture"
- "_OBJC_METACLASS_$_MTGCDTimer"
- "_OBJC_METACLASS_$_MTGetAlarmsIntentHandler"
- "_OBJC_METACLASS_$_MTInMemorySyncChangeStore"
- "_OBJC_METACLASS_$_MTIntentAlarm"
- "_OBJC_METACLASS_$_MTMetrics"
- "_OBJC_METACLASS_$_MTNextAlarm"
- "_OBJC_METACLASS_$_MTNextAlarmManager"
- "_OBJC_METACLASS_$_MTPBAlarmState"
- "_OBJC_METACLASS_$_MTPBAlarmUpdate"
- "_OBJC_METACLASS_$_MTPBDismissAction"
- "_OBJC_METACLASS_$_MTPairedDevicePreferences"
- "_OBJC_METACLASS_$_MTPowerAssertion"
- "_OBJC_METACLASS_$_MTResetTimerIntentHandler"
- "_OBJC_METACLASS_$_MTScheduledObject"
- "_OBJC_METACLASS_$_MTSearchTimerIntentHandler"
- "_OBJC_METACLASS_$_MTSessionManager"
- "_OBJC_METACLASS_$_MTSessionManagerExportedObject"
- "_OBJC_METACLASS_$_MTSessionServer"
- "_OBJC_METACLASS_$_MTSessionsCoordinator"
- "_OBJC_METACLASS_$_MTSleepCoordinatorStateMachineDisabledState"
- "_OBJC_METACLASS_$_MTSleepModeStateMachineOnState"
- "_OBJC_METACLASS_$_MTSleepModeStateMachineState"
- "_OBJC_METACLASS_$_MTSleepModeStateMachineWaitingState"
- "_OBJC_METACLASS_$_MTSleepSessionManager"
- "_OBJC_METACLASS_$_MTSleepUtilities"
- "_OBJC_METACLASS_$_MTSound"
- "_OBJC_METACLASS_$_MTStateMachine"
- "_OBJC_METACLASS_$_MTStateMachineState"
- "_OBJC_METACLASS_$_MTTask"
- "_OBJC_METACLASS_$_MTTaskGroup"
- "_OBJC_METACLASS_$_MTTimer"
- "_OBJC_METACLASS_$_MTTimerDataSource"
- "_OBJC_METACLASS_$_MTTimerDurationManager"
- "_OBJC_METACLASS_$_MTTimerIntentHandler"
- "_OBJC_METACLASS_$_MTUpdateTimerIntentHandler"
- "_OBJC_METACLASS_$_MTWidgetProvider"
- "_OBJC_METACLASS_$_MTWorldClock"
- "_OBJC_METACLASS_$_MTWorldClockResolutionResult"
- "_OBJC_METACLASS_$_MTXPCConnectionInfo"
- "_OBJC_METACLASS_$_MTXPCConnectionProvider"
- "_OBJC_METACLASS_$_NotificationRelay"
- "_OBJC_METACLASS_$_SiriTTSSynthesisEngine"
- "_OBJC_METACLASS_$_SiriTTSSynthesisEngineRequest"
- "_OBJC_METACLASS_$_SiriTTSSynthesisEngineResource"
- "_OBJC_METACLASS_$_SiriTTSSynthesisEngineWordTimings"
- "_OBJC_METACLASS_$_TTSAsset"
- "_OBJC_METACLASS_$_TTSAssetQuality"
- "_OBJC_METACLASS_$_TTSAssetSource"
- "_OBJC_METACLASS_$_TTSAssetTechnology"
- "_OBJC_METACLASS_$_TTSAssetType"
- "_OBJC_METACLASS_$_TTSStringEnum"
- "_OBJC_METACLASS_$_WorldClockCity"
- "__AFBackedUpPreferencesValueForKey"
- "__AFPreferencesBoolFromValueWithDefault"
- "__AFPreferencesBoolValueForKeyWithContext"
- "__AFPreferencesDictationLanguageDetectorEnabled"
- "__AFPreferencesForceOnDeviceOnlyDictationEnabled"
- "__AFPreferencesKeepRecorededAudioFiles"
- "__AFPreferencesLanguageCode"
- "__AFPreferencesReplacementLanguageForLocalRecognizerLanguageCode"
- "__AFPreferencesShowAllDialogVariantsEnabled"
- "__AFPreferencesValueForKey"
- "__AFPreferencesValueForKeyWithContext"
- "__AFServiceLog"
- "__AFSupportPreferencesBoolForKeyWithDefault"
- "ionEventGetDescription"
- "riTTSPhonemeRequest"

```
