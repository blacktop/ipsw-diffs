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
+3404.71.4.1.1
+  __TEXT.__text: 0x1736a8
+  __TEXT.__auth_stubs: 0x1760
+  __TEXT.__objc_stubs: 0x1ef20
+  __TEXT.__objc_methlist: 0x19444
   __TEXT.__dlopen_cstrs: 0x2c5
-  __TEXT.__unwind_info: 0x56a0
-  __DATA_CONST.__auth_got: 0xbc0
-  __DATA_CONST.__got: 0x13e8
+  __TEXT.__const: 0x380
+  __TEXT.__gcc_except_tab: 0x4250
+  __TEXT.__cstring: 0x2a429
+  __TEXT.__objc_methname: 0x3f076
+  __TEXT.__oslogstring: 0x21b93
+  __TEXT.__objc_classname: 0x3520
+  __TEXT.__objc_methtype: 0x8745
+  __TEXT.__unwind_info: 0x5878
+  __DATA_CONST.__auth_got: 0xbc8
+  __DATA_CONST.__got: 0x13f8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x5cc8
-  __DATA_CONST.__cfstring: 0x83c0
-  __DATA_CONST.__objc_classlist: 0x988
+  __DATA_CONST.__const: 0x5d18
+  __DATA_CONST.__cfstring: 0x84a0
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
+  __DATA.__objc_const: 0x28568
+  __DATA.__objc_selrefs: 0xbad8
+  __DATA.__objc_ivar: 0x1f30
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
+  Functions: 9640
+  Symbols:   1028
+  CStrings:  15814
 
Symbols:
+ _AFDeviceSupportsSiriMUX
+ _AFIsUODCapableHorsemanDevice
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_CESAContextualEntityRetriever
+ _OBJC_CLASS_$_CESRSpeechProfileConfig
+ _OBJC_CLASS_$_CSAudioProviderSelectingProxy
+ _OBJC_CLASS_$_CSFHashUtils
+ __AFPreferencesValueForKeyWithContext
- _AVAudioSessionCategoryPlayback
- _AVAudioSessionModeDefault
- _AudioQueueNewOutput
- _CC_SHA256
- _OBJC_CLASS_$_CESRSpeechProfileSiteManager
- _XPC_ACTIVITY_INTERVAL_5_MIN
- _XPC_ACTIVITY_POST_INSTALL
- _XPC_ACTIVITY_PRIORITY_UTILITY
- _kCFRunLoopCommonModes
CStrings:
+ "%s AOP trigger timestamp was 4 seconds the current time. Ignoring AOP trigger due to trigger time CONSTRAINT check"
+ "%s ASR Contextual Entity Retrieval: triggering collection warm-up during preheat"
+ "%s Asset Provider:%ld, Asset Variant: %ld, attemptAssetMapping:%d"
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
+ "%s On-Device ASR: BGST: ExpirationHandler called."
+ "%s On-Device ASR: BGST: Failed to expire task with error: %@"
+ "%s On-Device ASR: BGST: Failed to submit task %@. Error: %@"
+ "%s On-Device ASR: BGST: Skipping submission of existing task %@."
+ "%s On-Device ASR: BGST: Starting submission of task %@."
+ "%s On-Device ASR: BGST: Successfully submitted task %@"
+ "%s On-Device ASR: BGST: Task completed before expiration."
+ "%s Should retry mapping asset? %@"
+ "%s Successfully mapped asset with version:%@"
+ "%s Unable to find endpointer model for default task %{public}@"
+ "%s client is null"
+ "%s event is nil"
+ "%s isSupported=%@: Is request during active call? %@, isDeviceSupported: %@, isFFEnabledOnDevice: %@, isSupportedRequestType: %@, isFFUserDisabled: %@, isTypeToSiriEnabled: %@, isLocaleInDenyList:%@, isSAEEnabled:%@, isLocaleUnsupportedWithSAE:%@ isLocaleCoupledWithSAE:%@"
+ "%s languageCode:  %{public}@ -voiceProfileArray: %{public}@, _currentAssets:%@"
+ "%s reply is nil"
+ "%s result is BOOL"
+ "%s type of result %s"
+ "-[CSAttSiriBridgeMessageHandler sendVisualContextAndCorrectionsInfo:interactionIdentifier:]"
+ "-[CSAttSiriSpeechRecognitionNode preheatWithLanguage:source:shouldDownloadMissingAsset:]"
+ "-[CSAudioStreamProvidingProxy _handleStartAudioStreamMessage:messageBody:client:]_block_invoke"
+ "-[CSAudioStreamProvidingProxy _sendReply:client:result:error:]"
+ "-[CSBuiltInVoiceTrigger _setAsset:]"
+ "-[CSBuiltInVoiceTrigger _setAsset:]_block_invoke"
+ "-[CSSpeechManager _mapAssetToExclaveKit:completion:]_block_invoke"
+ "-[CSSpeechManager _mapAssetToExclaveKit:completion:]_block_invoke_2"
+ "-[CSSpeechManager _retryMapAssetToExclaveKit:]_block_invoke"
+ "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]"
+ "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]_block_invoke"
+ "-[CSVoiceTriggerAssetHandler mapAssetToExclaveKit:completion:]_block_invoke"
+ "-[CSVoiceTriggerAssetHandler retryMappingAssetToExclaveKit:completion:]_block_invoke"
+ "@\"BGSystemTaskRequest\"16@?0@\"NSString\"8"
+ "@\"CESRBackgroundSystemTask\""
+ "@\"CESRSpeechProfileConfig\""
+ "@\"CESRSpeechProfileSiteResolver\""
+ "C)\x11\x12\x12\x14\x13!\x11B"
+ "CESRBackgroundSystemTask"
+ "CSPRegisterAndSubmitPostInstallMigrationTask_block_invoke"
+ "Enable ASR Periodic Preheat"
+ "Failed retrying to map asset with version:%@"
+ "Fallback_Secure_PreinstalledAsset"
+ "Mapping asset failed. Falling back to preinstalled asset with version:%@"
+ "Mapping_Secure_Asset_Succeeded"
+ "NLDAClassifier_Create"
+ "NLDAClassifier_ProcessSpeechPackage"
+ "Retry_Mapping_Secure_Asset_Failed"
+ "Successfully mapped asset with version:%@"
+ "T@\"CESRBackgroundSystemTask\",&,N,V_cesrBGSTScheduler"
+ "T@\"CESRSpeechProfileConfig\",&,N,V_speechProfileConfig"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_contextualEntityRetrievalQueue"
+ "T@\"NSString\",&,N,V_currentTaskString"
+ "UresMitigator_processResultCandidateStart"
+ "Vv32@0:8@\"AFSpeechVisualContextAndCorrectionsInfo\"16@\"NSString\"24"
+ "_buildLaunchHandlerWithFunction_block_invoke"
+ "_cesrBGSTScheduler"
+ "_contextualEntityRetrievalQueue"
+ "_currentTaskString"
+ "_isANECapableDevice"
+ "_isPeriodicPreheatEnabled"
+ "_isTaskStringAccessible:"
+ "_mapAssetToExclaveKit:completion:"
+ "_retryMapAssetToExclaveKit:"
+ "_runDailyANECompilation"
+ "_runPostUpgradeANECompilation"
+ "_runPostUpgradeSubscriptions"
+ "_runRetrainerWithAssets:languageCode:"
+ "_runSubscriptionCleanup"
+ "_speechProfileConfig"
+ "_submitBGSTRequest"
+ "activeUserInfo"
+ "addAudioSync:"
+ "ay12!Rd"
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
+ "contextualEntityConfig"
+ "contextualEntityRetrievalQueue"
+ "contextualEntityRetrievalQueue Queue"
+ "currentTaskString"
+ "defaultResolver"
+ "enablementConfig"
+ "enforceAutomaticEndpointing"
+ "initWithIdentifier:"
+ "initWithLanguage:requestIdentifier:dictationUIInteractionIdentifier:task:loggingContext:applicationName:profile:overrides:modelOverrideURL:originalAudioFileURL:codec:narrowband:detectUtterances:censorSpeech:farField:secureOfflineOnly:shouldStoreAudioOnDevice:continuousListening:shouldHandleCapitalization:isSpeechAPIRequest:maximumRecognitionDuration:endpointStart:inputOrigin:location:jitGrammar:deliverEagerPackage:disableDeliveringAsrFeatures:enableEmojiRecognition:enableAutoPunctuation:enableVoiceCommands:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:recognitionStart:shouldGenerateVoiceCommandCandidates:asrId:activeUserInfo:"
+ "installedCompactAssetOfType:language:"
+ "isCompactVersion"
+ "isMagusRestrictedWithSAEForLanguageCode:"
+ "registerAndSubmitBGSystemTasks"
+ "registerBackgroundSystemTasks"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
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
+ "v16@?0@\"BGSystemTask\"8"
+ "v44@?0Q8d16I24Q28Q36"
+ "v52@?0Q8Q16d24I32Q36Q44"
- "\n"
- "\x11\""
- "%s %@ - %@"
- "%s Asset handler %@ does not support mapping asset to EK. This is a critical error"
- "%s AudioQueue call back is asking for audio, injected file has been found"
- "%s AudioQueue call back is asking for audio, injected file is not available, injecting digital 1s"
- "%s Client request to speak audio into exclave with URL: %@ at time: %llu"
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
- "%s Successfully activate audioSession"
- "%s Successfully deactivate audioSession"
- "%s Successfully start the audio queue"
- "%s Tried to defer activity but failed"
- "%s Unable to alloc AudioQueue AudioBuffer with OSStatus: %d"
- "%s Unable to find endpointer model for default task type %{public}@"
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
- "-[CSSpeechManager _setAssetForBuiltInVoiceTrigger:completion:]_block_invoke_4"
- "-[CSTrialAssetManager _getSiriAttAssetsForType:forLocale:completion:]_block_invoke"
- "-[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]"
- "-[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]_block_invoke"
- "-[CSVoiceTriggerAssetHandlerMac mapAssetToExclaveKit:completion:]_block_invoke"
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
- "UAFLevelForFactor:withNamespaceName:withLanguage:"
- "Unable to get Trial factor: %@"
- "Vv32@0:8@\"KVProfile\"16@?<v@?q>24"
- "^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16@0:8"
- "_RegisterDailyANECompilationActivity_block_invoke_2"
- "_RegisterDailySubscriptionCleanupActivity_block_invoke_2"
- "_RegisterPostUpgradeANECompilationActivity_block_invoke_2"
- "_RegisterPostUpgradeSubscriptionActivity_block_invoke_2"
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
- "_prepareAndStartAudioQueue"
- "_readAudioBufferAndFeedIntoAudioQueue"
- "_setAsset:forceExclaveToUsePreInstalledAsset:"
- "_setAudioSessionActive:"
- "_sha256:"
- "ay12!Rc"
- "beginEvaluation:completion:"
- "bypassTrialAssets"
- "cesrXPCActvity"
- "cleanupVoiceProfileModelFilesForLocale:withAsset:"
- "com.apple.siri.xpc_activity.daily-speech-ane-compilation"
- "com.apple.siri.xpc_activity.daily-speech-profile-maintenance"
- "com.apple.siri.xpc_activity.daily-subscription-cleanup"
- "com.apple.siri.xpc_activity.post-install-speech-profile-migration"
- "com.apple.siri.xpc_activity.post-upgrade-speech-ane-compilation"
- "com.apple.siri.xpc_activity.post-upgrade-subscriptions"
- "exclaveAudioQueue"
- "injectionCompletion"
- "injectionEndTime"
- "injectionStartTime"
- "isAudioQueueStarted"
- "registerDailyANECompilationActivity"
- "registerDailySubscriptionCleanupActivity"
- "registerPeriodicPreheatActivity"
- "registerPostUpgradeANECompilationActivity"
- "registerPostUpgradeSubscriptionActivity"
- "setAsset:forceExclaveToUsePreInstalledAsset:"
- "setCategory:mode:options:error:"
- "setCesrXPCActvity:"
- "setExclaveAudioQueue:"
- "setInjectionCompletion:"
- "setInjectionEndTime:"
- "setInjectionStartTime:"
- "setIsAudioQueueStarted:"
- "speakAudioInExclave:withCompletion:"
- "v32@0:8@\"CSAsset\"16@?<v@?@\"NSError\">24"
- "v56@?0Q8d16f24f28I32f36Q40Q48"
- "v64@?0Q8Q16d24f32f36I40f44Q48Q56"

```
