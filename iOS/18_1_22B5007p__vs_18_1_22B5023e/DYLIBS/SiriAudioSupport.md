## SiriAudioSupport

> `/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport`

```diff

-3400.139.1.0.0
-  __TEXT.__text: 0x218410
-  __TEXT.__auth_stubs: 0x37d0
+3401.3.1.0.0
+  __TEXT.__text: 0x21a89c
+  __TEXT.__auth_stubs: 0x3840
   __TEXT.__objc_methlist: 0x808
-  __TEXT.__const: 0x9278
-  __TEXT.__cstring: 0xbcd5
-  __TEXT.__swift5_typeref: 0x3f3d
-  __TEXT.__swift5_fieldmd: 0x41d4
-  __TEXT.__constg_swiftt: 0x5818
-  __TEXT.__swift5_builtin: 0x2e4
-  __TEXT.__swift5_reflstr: 0x45cc
+  __TEXT.__const: 0x93b8
+  __TEXT.__cstring: 0xb0f5
+  __TEXT.__swift5_typeref: 0x3fa5
+  __TEXT.__swift5_fieldmd: 0x4268
+  __TEXT.__constg_swiftt: 0x5944
+  __TEXT.__swift5_builtin: 0x2f8
+  __TEXT.__swift5_reflstr: 0x461c
   __TEXT.__swift5_assocty: 0x570
-  __TEXT.__swift5_protos: 0x114
-  __TEXT.__swift5_proto: 0x53c
-  __TEXT.__swift5_types: 0x3f8
-  __TEXT.__swift5_capture: 0x54c4
-  __TEXT.__oslogstring: 0x1f26e
+  __TEXT.__swift5_protos: 0x118
+  __TEXT.__swift5_proto: 0x548
+  __TEXT.__swift5_types: 0x408
+  __TEXT.__swift5_capture: 0x54e4
+  __TEXT.__oslogstring: 0x1fc0e
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4558
-  __TEXT.__eh_frame: 0x274c
+  __TEXT.__unwind_info: 0x45f0
+  __TEXT.__eh_frame: 0x2564
   __TEXT.__objc_classname: 0x180
-  __TEXT.__objc_methname: 0x614b
+  __TEXT.__objc_methname: 0x61b8
   __TEXT.__objc_methtype: 0x5c5
-  __DATA_CONST.__got: 0x10b0
-  __DATA_CONST.__const: 0x7c0
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __DATA_CONST.__got: 0x10f0
+  __DATA_CONST.__const: 0x810
+  __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ca8
+  __DATA_CONST.__objc_selrefs: 0x1cc0
   __DATA_CONST.__objc_protorefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x1be8
-  __AUTH_CONST.__auth_ptr: 0x15d8
-  __AUTH_CONST.__const: 0x14ce8
-  __AUTH_CONST.__cfstring: 0x6a0
-  __AUTH_CONST.__objc_const: 0xac60
+  __AUTH_CONST.__auth_got: 0x1c20
+  __AUTH_CONST.__auth_ptr: 0x15f0
+  __AUTH_CONST.__const: 0x14ec8
+  __AUTH_CONST.__cfstring: 0x20
+  __AUTH_CONST.__objc_const: 0xb198
   __AUTH.__objc_data: 0xfb8
-  __AUTH.__data: 0x5888
-  __DATA.__data: 0x2b50
-  __DATA.__bss: 0x6e38
+  __AUTH.__data: 0x5a00
+  __DATA.__data: 0x2c08
+  __DATA.__bss: 0x6f38
   __DATA.__common: 0x270
   __DATA_DIRTY.__objc_data: 0xd0
   __DATA_DIRTY.__data: 0x28

   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal

   - /System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers
   - /System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals
   - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities
-  - /System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8337
-  Symbols:   986
-  CStrings:  4089
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 8431
+  Symbols:   1009
+  CStrings:  4084
 
Symbols:
+ _OBJC_CLASS_$_MCProfileConnection
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _TCCAccessCopyInformationForBundleId
+ _TCCAccessSetForBundleId
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _kTCCInfoGranted
+ _kTCCInfoService
+ _kTCCServiceSiri
- _OBJC_CLASS_$_DESRecordStore
- _OBJC_CLASS_$_SSRVoiceProfile
- _OBJC_CLASS_$_SSRVoiceProfileManager
- _swift_continuation_await
- _swift_continuation_init
- _swift_taskGroup_destroy
- _swift_taskGroup_initialize
CStrings:
+ "ClassicalTCCRejectedCounter"
+ "Default_TTR_Config_Factor"
+ "Error downloading levels for factor: %!s(MISSING) in namespace: %!s(MISSING). Error: %!s(MISSING)"
+ "ErrorFilingProvider#TrialClientManager downloadLevels"
+ "ErrorFilingProvider#TrialClientManager unable to load latest data policy"
+ "ErrorFilingProvider#TrialClientManager update handler called with %!s(MISSING)"
+ "ErrorFilingProvider#TrialClientManager#init"
+ "ErrorFilingProvider#TrialClientManager#loadLatest level path: %!s(MISSING)"
+ "ErrorFilingProvider#TrialClientManager#loadLatest..."
+ "ErrorFilingProvider#setTrialPolicy... policy is %!l(MISSING)d bytes"
+ "ErrorFilingProvider#setupTrialClient..."
+ "ErrorFilingProvider#trialQueue"
+ "MediaPlaybackProvider#doesCurrentHPPolicyAllowTimeoutErrorsForTailspin denyAll, returning false"
+ "MediaPlaybackProvider#doesCurrentHPPolicyAllowTimeoutErrorsForTailspin invalid policy, returning false"
+ "MediaPlaybackProvider#doesCurrentHPPolicyAllowTimeoutErrorsForTailspin no error denyList, returning true"
+ "MediaPlaybackProvider#doesCurrentHPPolicyAllowTimeoutErrorsForTailspin no policy for %!s(MISSING)"
+ "MediaPlaybackProvider#doesCurrentHPPolicyAllowTimeoutErrorsForTailspin no policy, returning false"
+ "MediaPlaybackProvider#fileRadarWithTailSpins count: %!l(MISSING)d"
+ "MediaPlaybackProvider#fileRadarWithTailSpins notification received: %!{(MISSING)bool}d"
+ "MediaPlaybackProvider#fileRadarWithTailSpins waiting up to %!l(MISSING)d seconds for tailspin file creation to complete"
+ "MediaPlaybackProvider#generateTailSpinIfIsCommandDidNotProvideAStatusError createTailSpinFile generated: %!s(MISSING)"
+ "MediaPlaybackProvider#generateTailSpinIfIsCommandDidNotProvideAStatusError failed to create tailspin file"
+ "Music-6044-Error-V4"
+ "SIRI_AUDIO_TAPTORADAR_CONFIGURATION"
+ "SiriAudio#isMakeFlowFromParse#get %!{(MISSING)bool}d"
+ "SiriAudio#isMakeFlowFromParse#reset makeFlow(from:) did not finish within %!l(MISSING)dms."
+ "SiriAudio#isMakeFlowFromParse#set %!{(MISSING)bool}d"
+ "SiriAudioDomainExecutionLogger#deinit Error event wasn't logged successfully. Make sure that you called send(event:) for: %!s(MISSING)."
+ "SiriAudioDomainExecutionLogger#send sending %!s(MISSING) event with domainExecutionType: %!s(MISSING)"
+ "SiriAudioDomainExecutionLogger#send sent %!s(MISSING) event with domainExecutionType: %!s(MISSING)"
+ "SiriAudioDomainExecutionLogger#startDomainExecution Couldn't initialize FLOWSchemaFLOWDomainExecutionStarted"
+ "SiriAudioDomainExecutionLogger#startDomainExecution Couldn't initialize start FLOWSchemaFLOWDomainExecutionContext"
+ "SiriAudioDomainExecutionLogger#startDomainExecution..."
+ "SiriAudioState.reset"
+ "SiriEnvironmentWrapper called from warmup or makeFlow(from: Parse). This will result in the wrong SiriEnvironment"
+ "SiriEnvironmentWrapper#retrieve Removing old context with refId: %!{(MISSING)public}s"
+ "SiriEnvironmentWrapper#retrieve SiriEnvironment.forCurrentTask: %!s(MISSING)"
+ "Successfully downloaded levels for factor: %!s(MISSING) in namespace: %!s(MISSING)"
+ "SystemApertureCachedValue#isSystemApertureEnabled returning cached Value"
+ "SystemApertureCachedValue#isSystemApertureEnabled returning value from current request."
+ "SystemApertureCachedValue#start persisting value for the next request as: %!{(MISSING)bool}d"
+ "SystemApertureCachedValue#update count is now: %!l(MISSING)d"
+ "SystemApertureCachedValue#update updating SystemAperture cached value."
+ "SystemApertureCachedValue#update value expired"
+ "TCCProvider#getSiriTCCStatusForBundle bundle:%!s(MISSING), TCC info:%!s(MISSING)"
+ "TCCProvider#getSiriTCCStatusForBundle failed to access TCC strings"
+ "TCCProvider#getSiriTCCStatusForBundle failed to pull TCC info for %!s(MISSING)"
+ "TCCProvider#rejectTCC explicitly denying TCC access for %!s(MISSING)"
+ "TCCProvider#rejectTCC failed to access kTCCServiceSiri string"
+ "TTRErrorCodeInfo"
+ "TTRErrorInfoAirPlayNotResponding"
+ "TTRErrorTitleInfo"
+ "_TtC16SiriAudioSupport21FlowClientEventSender"
+ "_TtCC16SiriAudioSupport19ErrorFilingProviderP33_35DCE3D6F0D64029689780897F5B807018TrialClientManager"
+ "domainPerfContextEventSender"
+ "downloadLevelsForFactors:withNamespace:queue:options:progress:completion:"
+ "endEventSent"
+ "fileValue"
+ "isDiagnosticSubmissionAllowed"
+ "objectForKeyedSubscript:"
+ "propertyListWithData:options:format:error:"
+ "refresh"
+ "sharedConnection"
+ "sirikitEventSender"
+ "startEventSent"
+ "taskType"
+ "v20@?0B8@\"NSError\"12"
- "\nUsers in the Home: "
- "FLOWDOMAINEXECUTIONTYPE_HOME_AUTOMATION_BLOCKING_INTENT"
- "FLOWDOMAINEXECUTIONTYPE_HOME_AUTOMATION_ININTENT_CONVERTER"
- "FLOWDOMAINEXECUTIONTYPE_HOME_AUTOMATION_INTENT_SELECTION"
- "FLOWDOMAINEXECUTIONTYPE_HOME_AUTOMATION_MODIFYING_INTENT"
- "FLOWDOMAINEXECUTIONTYPE_HOME_AUTOMATION_NATIVE_HOME_STORE_INITIALIZATION"
- "FLOWDOMAINEXECUTIONTYPE_HOME_AUTOMATION_NL_INTENT_CONVERTER"
- "FLOWDOMAINEXECUTIONTYPE_HOME_AUTOMATION_SEND_HOMEKIT_COMMAND_ACE"
- "FLOWDOMAINEXECUTIONTYPE_HOME_AUTOMATION_SEND_HOMEKIT_COMMAND_CONFIGURE"
- "FLOWDOMAINEXECUTIONTYPE_HOME_AUTOMATION_SEND_HOMEKIT_COMMAND_CONTROL"
- "FLOWDOMAINEXECUTIONTYPE_LIVE_ACTIVITY_WAIT"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_AIRPLAY_DEVICE_SEARCH"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_AIRPLAY_SET_AUDIO_SESSION_CATEGORY"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_AIRPLAY_SET_OUTPUT_DEVICES"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_AMS_PURCHASE"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_BOLT_ENABLED_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_CLIENT_CONTEXT_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_COMPOUND_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_ENTITY_SEARCH_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_FOREGROUP_APP_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_FREE_MEDIA_CONTENT_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_INTENT_MEDIA_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_LAST_NOW_PLAYING_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_MEGA_MODEL_LAST_NOW_PLAYING_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_MEGA_MODEL_NOW_PLAYING_COUNT_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_MEGA_MODEL_NOW_PLAYING_RECENCY_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_NOW_PLAYING_APP_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_NOW_PLAYING_STATE_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_NOW_PLAYING_USAGE_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_PIRENE_REQUEST_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_PRIVATE_INTENT_DATA_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_SELECTED_APP_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_SUPPORTED_MEDIA_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_USER_CONTEXT_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_USER_RECOGNIZED_SIGNAL"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_MEDIAREMOTE_PLAY"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_MEDIAREMOTE_SEND_QUEUE"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_RECON_SESSION_CREATE_W_ENDPOINT_FEATURES"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_RECON_SESSION_SET_TARGET_AUDIO_SESSION_ID"
- "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_SHAZAM_PERFORM_MATCH"
- "FLOWDOMAINEXECUTIONTYPE_MESSAGE_NOW_PLAYING_QUEUE_FETCH"
- "FLOWDOMAINEXECUTIONTYPE_MESSAGE_ONE_SHOT_AUTO_PUNCTUATION_CESRFORMATTER"
- "FLOWDOMAINEXECUTIONTYPE_MESSAGE_READ_ACTION_SPEECH_API"
- "FLOWDOMAINEXECUTIONTYPE_MESSAGE_SHARING_LINK_PRESENTATION"
- "FLOWDOMAINEXECUTIONTYPE_MESSAGE_WFON_SCREEN_CONTENT_EXTRACTION"
- "FLOWDOMAINEXECUTIONTYPE_PHONE_FACETIME_MESSAGE"
- "FLOWDOMAINEXECUTIONTYPE_PHONE_RESOLVE_CRR"
- "FLOWDOMAINEXECUTIONTYPE_PHONE_RESOLVE_SRR"
- "FLOWDOMAINEXECUTIONTYPE_TIMER_ALARM_COORDINATION_WAIT"
- "FLOWDOMAINEXECUTIONTYPE_TIMER_ALARM_MOBILE_TIMER_WAIT"
- "FLOWDOMAINEXECUTIONTYPE_UNKNOWN"
- "FLOWDOMAINEXECUTIONTYPE_VOICESHORTCUTS_LINK_EVENT_WAIT"
- "FLOWDOMAINEXECUTIONTYPE_VOICESHORTCUTS_SHORTCUT_EVENT_WAIT"
- "FirstPartyFailure"
- "MediaPlaybackProvider#fileTTRWithTailSpins count: %!l(MISSING)d"
- "MediaPlaybackProvider#fileTTRWithTailSpins currently ignoring this error signature: %!s(MISSING)"
- "SiriAudioDomainExecutionLogger#deinit Error event wasn't logged successfully. Make sure that you called sendSirikitEvents() for: "
- "SiriAudioDomainExecutionLogger#init Couldn't initialize FLOWSchemaFLOWDomainExecutionStarted"
- "SiriAudioDomainExecutionLogger#init Couldn't initialize start FLOWSchemaFLOWDomainExecutionContext"
- "SiriAudioDomainExecutionLogger#init Initialized SELFPerformanceLogger: startEventDomainExecutionContext: %!@(MISSING) contextId: %!@(MISSING)"
- "SiriAudioDomainExecutionLogger#sendSirikitEvents sending endDomainExecutionContext with domainExecutionType: %!s(MISSING)"
- "SiriAudioDomainExecutionLogger#sendSirikitEvents sending startEventDomainExecutionContext with domainExecutionType: %!s(MISSING)"
- "SiriAudioDomainExecutionLogger#sendSirikitEvents sent endDomainExecutionContext with domainExecutionType: %!s(MISSING)"
- "SiriAudioDomainExecutionLogger#sendSirikitEvents sent startEventDomainExecutionContext with domainExecutionType: %!s(MISSING)"
- "SiriAudioDomainExecutionLogger#sendSirikitEvents..."
- "SiriMusic failed due to "
- "VoiceProfileProvider#getVoiceProfileCount Found %!s(MISSING) voice profiles"
- "domainExecutionType"
- "eventLoggedSuccessfully"
- "isPermitted"
- "provisionedVoiceProfilesForAppDomain:withLocale:"
- "startEventDomainExecutionContext"
- "startedOrChanged"

```
