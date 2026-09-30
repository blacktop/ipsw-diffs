## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-3403.7.3.0.0
-  __TEXT.__text: 0x174364
-  __TEXT.__auth_stubs: 0x1750
-  __TEXT.__objc_stubs: 0x1eb40
-  __TEXT.__objc_methlist: 0x17100
-  __TEXT.__const: 0x360
-  __TEXT.__gcc_except_tab: 0x39e4
-  __TEXT.__cstring: 0x2a5ab
-  __TEXT.__objc_methname: 0x3ec43
-  __TEXT.__oslogstring: 0x21bbd
-  __TEXT.__objc_classname: 0x3566
-  __TEXT.__objc_methtype: 0x8798
+3404.79.2.0.0
+  __TEXT.__text: 0x173cb8
+  __TEXT.__auth_stubs: 0x17a0
+  __TEXT.__objc_stubs: 0x1ef80
+  __TEXT.__objc_methlist: 0x194bc
   __TEXT.__dlopen_cstrs: 0x2c5
-  __TEXT.__unwind_info: 0x56a0
-  __DATA_CONST.__auth_got: 0xbc0
-  __DATA_CONST.__got: 0x13e8
+  __TEXT.__const: 0x390
+  __TEXT.__gcc_except_tab: 0x41d0
+  __TEXT.__objc_methname: 0x3f1d8
+  __TEXT.__cstring: 0x2a5df
+  __TEXT.__oslogstring: 0x21b2e
+  __TEXT.__objc_classname: 0x3521
+  __TEXT.__objc_methtype: 0x8762
+  __TEXT.__unwind_info: 0x58a0
+  __DATA_CONST.__auth_got: 0xbe8
+  __DATA_CONST.__got: 0x13d8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x5cc8
-  __DATA_CONST.__cfstring: 0x83c0
-  __DATA_CONST.__objc_classlist: 0x988
+  __DATA_CONST.__const: 0x5df8
+  __DATA_CONST.__cfstring: 0x8540
+  __DATA_CONST.__objc_classlist: 0x980
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x4f8
+  __DATA_CONST.__objc_protolist: 0x4f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xf0
-  __DATA_CONST.__objc_superrefs: 0x7d0
+  __DATA_CONST.__objc_superrefs: 0x7c8
   __DATA_CONST.__objc_intobj: 0xc90
   __DATA_CONST.__objc_doubleobj: 0x80
-  __DATA_CONST.__objc_arraydata: 0x270
+  __DATA_CONST.__objc_arraydata: 0x280
   __DATA_CONST.__objc_arrayobj: 0x150
-  __DATA_CONST.__objc_dictobj: 0x320
+  __DATA_CONST.__objc_dictobj: 0x348
   __DATA_CONST.__objc_floatobj: 0x4b0
-  __DATA.__objc_const: 0x2c6d8
-  __DATA.__objc_selrefs: 0xb890
-  __DATA.__objc_ivar: 0x1f48
-  __DATA.__objc_data: 0x5f50
-  __DATA.__data: 0x3ba0
-  __DATA.__bss: 0x758
+  __DATA.__objc_const: 0x28598
+  __DATA.__objc_selrefs: 0xbb10
+  __DATA.__objc_ivar: 0x1f34
+  __DATA.__objc_data: 0x5f00
+  __DATA.__data: 0x3b40
+  __DATA.__bss: 0x748
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis
   - /System/Library/Frameworks/Speech.framework/Speech
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9685
-  Symbols:   1027
-  CStrings:  15798
+  Functions: 9657
+  Symbols:   1028
+  CStrings:  15827
 
Symbols:
+ _AFDeviceSupportsSiriMUX
+ _AFIsInternalInstall
+ _AFIsUODCapableHorsemanDevice
+ _AVAudioSessionModeSpeechRecognition
+ _CFAbsoluteTimeGetCurrent
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_CESAContextualEntityRetriever
+ _OBJC_CLASS_$_CESRSpeechProfileConfig
+ _OBJC_CLASS_$_CSAudioProviderSelectingProxy
+ _OBJC_CLASS_$_CSFHashUtils
+ __AFPreferencesValueForKeyWithContext
+ _loadBookmark
+ _saveBookmark
- _AVAudioSessionCategoryPlayback
- _AVAudioSessionModeDefault
- _AudioQueueNewOutput
- _CC_SHA256
- _OBJC_CLASS_$_AFMyriadGoodnessScoreOverrideState
- _OBJC_CLASS_$_CESRSpeechProfileSiteManager
- _OBJC_CLASS_$_NSCoder
- _OBJC_CLASS_$_NSKeyedArchiver
- _OBJC_CLASS_$_NSKeyedUnarchiver
- _OBJC_CLASS_$_SCDAGoodnessScoreOverrideState
- _XPC_ACTIVITY_INTERVAL_5_MIN
- _XPC_ACTIVITY_POST_INSTALL
- _XPC_ACTIVITY_PRIORITY_UTILITY
- _kCFRunLoopCommonModes
CStrings:
+ "%s AOP trigger timestamp was 4 seconds the current time. Ignoring AOP trigger due to trigger time CONSTRAINT check"
+ "%s ASR Contextual Entity Retrieval: triggering collection warm-up during preheat"
+ "%s Asset Provider:%ld, Asset Variant: %ld, attemptAssetMapping:%d"
+ "%s Detected 2nd-pass trigger at %{public}llu, KeywordDetectionBucket : %@, SpeakerDetectionBucket : %@"
+ "%s Failed retrying to map asset with error %@"
+ "%s Failed retrying to map asset with version:%@"
+ "%s Fetched installed voicetrigger asset %@"
+ "%s Magus is not supported since locale is coupled with SAE and is ineligible"
+ "%s Mapping asset failed. Falling back to preinstalled asset with version:%@"
+ "%s Mapping is not supported hardware with no exclaves"
+ "%s Mapping is not supported hardware with no exclaves. Aborting retries."
+ "%s New task string: %{public}@, current task string: %{public}@"
+ "%s On-Device ASR: BGST: Done triggering ANE compilation"
+ "%s On-Device ASR: BGST: Done triggering daily subscription cleanup"
+ "%s On-Device ASR: BGST: Done triggering post-upgrade subscriptions"
+ "%s On-Device ASR: BGST: Done triggering replay record pruning"
+ "%s On-Device ASR: BGST: ExpirationHandler called."
+ "%s On-Device ASR: BGST: Failed to expire task with error: %@"
+ "%s On-Device ASR: BGST: Failed to submit task %@. Error: %@"
+ "%s On-Device ASR: BGST: Skipping submission of existing task %@."
+ "%s On-Device ASR: BGST: Starting submission of task %@."
+ "%s On-Device ASR: BGST: Successfully submitted task %@"
+ "%s On-Device ASR: BGST: Task completed before expiration."
+ "%s On-Device ASR: BGST: Triggering replay record pruning for event of age %f with timestamp %f"
+ "%s Rejected 2nd-pass KeywordDetectionBucket : %@, SpeakerDetectionBucket : %@"
+ "%s Should retry mapping asset? %@"
+ "%s Successfully mapped asset with version:%@"
+ "%s Unable to access app container group"
+ "%s Unable to find endpointer model for default task %{public}@"
+ "%s client is null"
+ "%s didReceivePartialResultWithRequestId : %{public}@, %{public}@"
+ "%s event is nil"
+ "%s isSupported=%@: Is request during active call? %@, isDeviceSupported: %@, isFFEnabledOnDevice: %@, isSupportedRequestType: %@, isFFUserDisabled: %@, isTypeToSiriEnabled: %@, isLocaleInDenyList:%@, isSAEEnabled:%@, isLocaleUnsupportedWithSAE:%@ isLocaleCoupledWithSAE:%@"
+ "%s languageCode:  %{public}@ -voiceProfileArray: %{public}@, _currentAssets:%@"
+ "%s reply is nil"
+ "%s result is BOOL"
+ "%s type of result %s"
+ "%s xpcDisconnection:%u"
+ "-[CSAttSiriBridgeMessageHandler sendVisualContextAndCorrectionsInfo:interactionIdentifier:]"
+ "-[CSAttSiriSpeechRecognitionNode preheatWithLanguage:source:shouldDownloadMissingAsset:]"
+ "-[CSAudioStreamProvidingProxy _handleStartAudioStreamMessage:messageBody:client:]_block_invoke"
+ "-[CSAudioStreamProvidingProxy _sendReply:client:result:error:]"
+ "-[CSBuiltInVoiceTrigger _setAsset:]"
+ "-[CSBuiltInVoiceTrigger _setAsset:]_block_invoke"
+ "-[CSIntuitiveConvRequestHandler _attendingExitAndDismissalWithXpcDisconnect:]"
+ "-[CSIntuitiveConvRequestHandler testDismissAttendingWithXPDisconnection:]_block_invoke"
+ "-[CSSiriLauncher notifyBuiltInVoiceTrigger:myriadPHash:completion:]_block_invoke_3"
+ "-[CSSpeechManager _mapAssetToExclaveKit:completion:]_block_invoke"
+ "-[CSSpeechManager _mapAssetToExclaveKit:completion:]_block_invoke_2"
+ "-[CSSpeechManager _retryMapAssetToExclaveKit:]_block_invoke"
+ "-[CSVoiceIdXPCClient _notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:]"
+ "-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]"
+ "-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]_block_invoke"
+ "-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]_block_invoke_2"
+ "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]"
+ "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]_block_invoke"
+ "-[CSVoiceTriggerAssetHandler mapAssetToExclaveKit:completion:]_block_invoke"
+ "-[CSVoiceTriggerAssetHandler retryMappingAssetToExclaveKit:completion:]_block_invoke"
+ "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]"
+ "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]_block_invoke"
+ ".\x11"
+ "@\"BGSystemTaskRequest\"16@?0@\"NSString\"8"
+ "@\"CESRBackgroundSystemTask\""
+ "@\"CESRSpeechProfileConfig\""
+ "@\"CESRSpeechProfileSiteResolver\""
+ "ASR"
+ "C)\x11\x12\x12\x14\x13!\x11B"
+ "CESRBackgroundSystemTask"
+ "CSPRegisterAndSubmitPostInstallMigrationTask_block_invoke"
+ "ContextualReplayRecord"
+ "Detected"
+ "Enable ASR Periodic Preheat"
+ "Failed retrying to map asset with version:%@"
+ "Fallback_Secure_PreinstalledAsset"
+ "Mapping asset failed. Falling back to preinstalled asset with version:%@"
+ "Mapping_Secure_Asset_Succeeded"
+ "NLDAClassifier_Create"
+ "NLDAClassifier_ProcessSpeechPackage"
+ "NearMiss"
+ "Rejected"
+ "Retry_Mapping_Secure_Asset_Failed"
+ "StrongAccept"
+ "StrongReject"
+ "Successfully mapped asset with version:%@"
+ "T@\"CESRBackgroundSystemTask\",&,N,V_cesrBGSTScheduler"
+ "T@\"CESRSpeechProfileConfig\",&,N,V_speechProfileConfig"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_contextualEntityRetrievalQueue"
+ "T@\"NSString\",&,N,V_currentTaskString"
+ "UresMitigator_processResultCandidateStart"
+ "Vv32@0:8@\"AFSpeechVisualContextAndCorrectionsInfo\"16@\"NSString\"24"
+ "Vv32@0:8@\"CCSerializedSetEnumerator\"16@?<v@?q>24"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSURL\">24"
+ "WeakAccept"
+ "WeakReject"
+ "_attendingExitAndDismissalWithXpcDisconnect:"
+ "_buildLaunchHandlerWithFunction_block_invoke"
+ "_cesrBGSTScheduler"
+ "_contextualEntityRetrievalQueue"
+ "_currentTaskString"
+ "_handleImplicitUtteranceMessage:client:"
+ "_isANECapableDevice"
+ "_isPeriodicPreheatEnabled"
+ "_isTaskStringAccessible:"
+ "_mapAssetToExclaveKit:completion:"
+ "_notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:"
+ "_processSecondPassInExclave:rejectBlock:"
+ "_retryMapAssetToExclaveKit:"
+ "_runDailyANECompilation"
+ "_runPostUpgradeANECompilation"
+ "_runPostUpgradeSubscriptions"
+ "_runReplayRecordPruning"
+ "_runReplayRecordPruning_block_invoke"
+ "_runRetrainerWithAssets:languageCode:"
+ "_runSubscriptionCleanup"
+ "_siriLanguageCode"
+ "_speechProfileConfig"
+ "_submitBGSTRequest"
+ "activeUserInfo"
+ "addAudioSync:"
+ "appContainerName"
+ "ay12!Rd"
+ "beginEvaluationWithSetEnumerator:completion:"
+ "cesrBGSTScheduler"
+ "cleanupVoiceProfileModelFilesForLocale:withAssets:"
+ "collect"
+ "com.apple.assistant"
+ "com.apple.siri.bg_system_task.daily-speech-ane-compilation"
+ "com.apple.siri.bg_system_task.daily-speech-profile-maintenance"
+ "com.apple.siri.bg_system_task.daily-subscription-cleanup"
+ "com.apple.siri.bg_system_task.post-install-speech-profile-migration"
+ "com.apple.siri.bg_system_task.post-upgrade-speech-ane-compilation"
+ "com.apple.siri.bg_system_task.post-upgrade-subscriptions"
+ "com.apple.siri.bg_system_task.replay-record-pruning"
+ "containerURLForSecurityApplicationGroupIdentifier:"
+ "contextualEntityConfig"
+ "contextualEntityRetrievalQueue"
+ "contextualEntityRetrievalQueue Queue"
+ "convertSecureVoiceTriggerKeywordDetectionResultTypeToString:"
+ "convertSecureVoiceTriggerSpeakerDetectionResultTypeToString:"
+ "currentTaskString"
+ "defaultResolver"
+ "enablementConfig"
+ "enforceAutomaticEndpointing"
+ "fetchCurrentRequestId"
+ "fetchDismissedRequestId"
+ "getBestSupportedSiriLanguageWithFallback:"
+ "initWithIdentifier:"
+ "initWithLanguage:requestIdentifier:dictationUIInteractionIdentifier:task:loggingContext:applicationName:profile:overrides:modelOverrideURL:originalAudioFileURL:codec:narrowband:detectUtterances:censorSpeech:farField:secureOfflineOnly:shouldStoreAudioOnDevice:continuousListening:shouldHandleCapitalization:isSpeechAPIRequest:maximumRecognitionDuration:endpointStart:inputOrigin:location:jitGrammar:deliverEagerPackage:disableDeliveringAsrFeatures:enableEmojiRecognition:enableAutoPunctuation:enableVoiceCommands:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:recognitionStart:shouldGenerateVoiceCommandCandidates:asrId:activeUserInfo:"
+ "installedCompactAssetOfType:language:"
+ "isCompactVersion"
+ "isMagusRestrictedWithSAEForLanguageCode:"
+ "notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:"
+ "registerAndSubmitBGSystemTasks"
+ "registerBackgroundSystemTasks"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "replay-record-pruning"
+ "resetForNewRequestSync"
+ "retryMappingAssetToExclaveKit:completion:"
+ "sendVisualContextAndCorrectionsInfo:interactionIdentifier:"
+ "setAudioProviderImp:"
+ "setCesrBGSTScheduler:"
+ "setContextualEntityRetrievalQueue:"
+ "setCurrentTaskString:"
+ "setEnforceAutomaticEndpointing:"
+ "setExpirationHandler:"
+ "setInterval:"
+ "setPostInstall:"
+ "setPriority:"
+ "setRequiresExternalPower:"
+ "setRequiresNetworkConnectivity:"
+ "setRequiresProtectionClass:"
+ "setRequiresUserInactivity:"
+ "setSpeechProfileConfig:"
+ "setTaskCompleted"
+ "setTaskExpiredWithRetryAfter:error:"
+ "setTrySchedulingBefore:"
+ "sha1StringFromInputData:"
+ "sha256DataFromInputData:"
+ "sharedContollerProxy"
+ "sharedScheduler"
+ "shouldRetrieve"
+ "speechProfileConfig"
+ "submitTaskRequest:error:"
+ "supportsPersonalizedHeySiri"
+ "taskRequestForIdentifier:"
+ "testDismissAttendingWithXPDisconnection:"
+ "v16@?0@\"BGSystemTask\"8"
+ "v60@?0Q8d16I24Q28Q36Q44Q52"
+ "v68@?0Q8Q16d24I32Q36Q44Q52Q60"
- "\n"
- "\x11\""
- "%s %@ - %@"
- "%s Asset handler %@ does not support mapping asset to EK. This is a critical error"
- "%s AudioQueue call back is asking for audio, injected file has been found"
- "%s AudioQueue call back is asking for audio, injected file is not available, injecting digital 1s"
- "%s Client request to speak audio into exclave with URL: %@ at time: %llu"
- "%s Detected 2nd-pass trigger at %{public}llu"
- "%s Failed to activate audioSession with error: %@"
- "%s Failed to create Exclave Audio Injection AudioQueue with OSStatus error: %d"
- "%s Failed to deactivate audioSession with error: %@"
- "%s Failed to feed audio into exclave, AQ or AQBuffer is invalid"
- "%s Failed to feed audio into exclave, unable to alloc AudioQueue AudioBuffer with OSStatus: %d"
- "%s Failed to feed audio into exclave, unable to enqueue AQ buffer with OSStatus: %d"
- "%s Failed to feed audio into exclave, unable to locate available audio queue"
- "%s Failed to feed audio into exclave, unable to start AQ buffer with OSStatus: %d"
- "%s Failed to set audioSession properties with error: %@"
- "%s Falling back to preinstalled assets for EK"
- "%s Got Trial rollout for assetType: %lu for locale: %@ version: %@"
- "%s On-Device ASR: XPC: Done triggering daily ANE compilation"
- "%s On-Device ASR: XPC: Done triggering daily subscription cleanup"
- "%s On-Device ASR: XPC: Done triggering post-upgrade ANE compilation"
- "%s On-Device ASR: XPC: Done triggering post-upgrade subscriptions"
- "%s On-Device ASR: XPC: Registering the daily ANE Compilation XPC Activity"
- "%s On-Device ASR: XPC: Registering the daily Subscription Cleanup XPC Activity"
- "%s On-Device ASR: XPC: Registering the post-upgrade ANE Compilation XPC Activity"
- "%s On-Device ASR: XPC: Registering the post-upgrade Subscription XPC Activity"
- "%s Overriding Myriad state as request was made during a ringtone"
- "%s Successfully activate audioSession"
- "%s Successfully deactivate audioSession"
- "%s Successfully start the audio queue"
- "%s Tried to defer activity but failed"
- "%s Unable to alloc AudioQueue AudioBuffer with OSStatus: %d"
- "%s Unable to find endpointer model for default task type %{public}@"
- "%s User Edit: cannot find bookmark from path %@, start enumeration from beginning"
- "%s User Edit: failed to deserialize bookmark, error: %@"
- "%s User Edit: failed to save bookmark on disk %@"
- "%s User Edit: failed to serialize bookmark, error: %@"
- "%s User Edit: invalid bookmark path %@, start enumeration from beginning"
- "%s User Edit: invalid file path for bookmark file %@"
- "%s User Edit: loaded bookmark from Biome %@"
- "%s User Edit: saved Biome bookmark on disk %@"
- "%s injection is ended at time: %llu"
- "%s isSupported=%@: Is request during active call? %@, isDeviceSupported: %@, isFFEnabledOnDevice: %@, isSupportedRequestType: %@, isFFUserDisabled: %@, isTypeToSiriEnabled: %@, isLocaleInDenyList:%@, isSAEEnabled:%@"
- "%s languageCode:  %{public}@ -voiceProfileArray: %{public}@, _currentAsset:%@"
- "%s starting the injection provider for exclave"
- "-[CESRXPCActivity registerDailyANECompilationActivity]"
- "-[CESRXPCActivity registerDailySubscriptionCleanupActivity]"
- "-[CESRXPCActivity registerPostUpgradeANECompilationActivity]"
- "-[CESRXPCActivity registerPostUpgradeSubscriptionActivity]"
- "-[CSAudioInjectionProviderExclave _createAudioQueueIfNeeded]"
- "-[CSAudioInjectionProviderExclave _defaultBufferRef]"
- "-[CSAudioInjectionProviderExclave _prepareAndStartAudioQueue]"
- "-[CSAudioInjectionProviderExclave _readAudioBufferAndFeedIntoAudioQueue]_block_invoke"
- "-[CSAudioInjectionProviderExclave _setAudioSessionActive:]"
- "-[CSAudioInjectionProviderExclave speakAudioInExclave:withCompletion:]_block_invoke"
- "-[CSAudioInjectionXPC init]"
- "-[CSBuiltInVoiceTrigger _setAsset:forceExclaveToUsePreInstalledAsset:]"
- "-[CSBuiltInVoiceTrigger _setAsset:forceExclaveToUsePreInstalledAsset:]_block_invoke"
- "-[CSBuiltInVoiceTrigger setAsset:forceExclaveToUsePreInstalledAsset:]"
- "-[CSIntuitiveConvRequestHandler _attendingDismissalAndBlockHelper]"
- "-[CSSpeechManager _setAssetForBuiltInVoiceTrigger:completion:]_block_invoke_4"
- "-[CSTrialAssetManager _getSiriAttAssetsForType:forLocale:completion:]_block_invoke"
- "-[CSVoiceIdXPCClient _notifyImplicitUtterance:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:]"
- "-[CSVoiceIdXPCConnection _handleClientMessage:client:]_block_invoke"
- "-[CSVoiceIdXPCConnection _handleClientMessage:client:]_block_invoke_2"
- "-[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]"
- "-[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]_block_invoke"
- "-[CSVoiceTriggerAssetHandlerMac mapAssetToExclaveKit:completion:]_block_invoke"
- "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]"
- "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]_block_invoke"
- "/Assistant/DictationUserEdit"
- "@\"CESRXPCActivity\""
- "@\"CSAudioInjectionProviderExclave\""
- "@\"NSObject<CESRSpeechProfileSiteManagement>\""
- "C(\x11\x12\x12\x14\x12!\x11B"
- "CESRXPCActivity"
- "CSAudioInjectionProviderExclave"
- "CSVoiceTriggerAssetHandlerExclaveProtocol"
- "Mismatch between Current locale: %@ & Trial rollout locale: %@"
- "T@\"CESRXPCActivity\",&,N,V_cesrXPCActvity"
- "T@?,C,N,V_injectionCompletion"
- "TB,N,V_isAudioQueueStarted"
- "TQ,N,V_injectionEndTime"
- "TQ,N,V_injectionStartTime"
- "T^{OpaqueAudioQueue=},N,V_exclaveAudioQueue"
- "Trial asset bypass is set"
- "Trigger was during a ringtone"
- "UAFLevelForFactor:withNamespaceName:withLanguage:"
- "Unable to get Trial factor: %@"
- "Vv32@0:8@\"KVProfile\"16@?<v@?q>24"
- "Vv32@0:8@\"NSArray\"16@?<v@?q>24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSURL\">24"
- "^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16@0:8"
- "_RegisterDailyANECompilationActivity_block_invoke_2"
- "_RegisterDailySubscriptionCleanupActivity_block_invoke_2"
- "_RegisterPostUpgradeANECompilationActivity_block_invoke_2"
- "_RegisterPostUpgradeSubscriptionActivity_block_invoke_2"
- "_attendingDismissalAndBlockHelper"
- "_cesrXPCActvity"
- "_createAudioQueueIfNeeded"
- "_defaultBufferRef"
- "_exclaveAudioQueue"
- "_getSiriAttAssetsForType:forLocale:completion:"
- "_injectionCompletion"
- "_injectionEndTime"
- "_injectionProviderExclave"
- "_injectionStartTime"
- "_isAudioQueueStarted"
- "_notifyImplicitUtterance:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:"
- "_prepareAndStartAudioQueue"
- "_processSecondPassInExclave:"
- "_readAudioBufferAndFeedIntoAudioQueue"
- "_setAsset:forceExclaveToUsePreInstalledAsset:"
- "_setAudioSessionActive:"
- "_sha256:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "ay12!Rc"
- "beginEvaluation:completion:"
- "beginEvaluationWithSerializedSets:completion:"
- "bm_allowedClassesForSecureCodingBMBookmark"
- "bookmark"
- "bypassTrialAssets"
- "cesrXPCActvity"
- "cleanupVoiceProfileModelFilesForLocale:withAsset:"
- "com.apple.siri.xpc_activity.daily-speech-ane-compilation"
- "com.apple.siri.xpc_activity.daily-speech-profile-maintenance"
- "com.apple.siri.xpc_activity.daily-subscription-cleanup"
- "com.apple.siri.xpc_activity.post-install-speech-profile-migration"
- "com.apple.siri.xpc_activity.post-upgrade-speech-ane-compilation"
- "com.apple.siri.xpc_activity.post-upgrade-subscriptions"
- "exclave-built-in"
- "exclaveAudioQueue"
- "initWithOverrideOption:reason:"
- "injectionCompletion"
- "injectionEndTime"
- "injectionStartTime"
- "isAudioQueueStarted"
- "loadBookmark"
- "registerDailyANECompilationActivity"
- "registerDailySubscriptionCleanupActivity"
- "registerPeriodicPreheatActivity"
- "registerPostUpgradeANECompilationActivity"
- "registerPostUpgradeSubscriptionActivity"
- "saveBookmark"
- "setAsset:forceExclaveToUsePreInstalledAsset:"
- "setCategory:withOptions:error:"
- "setCesrXPCActvity:"
- "setExclaveAudioQueue:"
- "setInjectionCompletion:"
- "setInjectionEndTime:"
- "setInjectionStartTime:"
- "setIsAudioQueueStarted:"
- "setOverrideState:"
- "speakAudioInExclave:withCompletion:"
- "unarchivedObjectOfClasses:fromData:error:"
- "v32@0:8@\"CSAsset\"16@?<v@?@\"NSError\">24"
- "v56@?0Q8d16f24f28I32f36Q40Q48"
- "v64@?0Q8Q16d24f32f36I40f44Q48Q56"

```
