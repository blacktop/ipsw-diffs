## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3403.7.3.0.0
-  __TEXT.__text: 0x1590b8
-  __TEXT.__auth_stubs: 0x1c10
-  __TEXT.__objc_methlist: 0x13348
-  __TEXT.__const: 0x5c0
-  __TEXT.__gcc_except_tab: 0x3848
-  __TEXT.__cstring: 0x27382
-  __TEXT.__oslogstring: 0x1f9da
+3404.71.4.1.1
+  __TEXT.__text: 0x157f10
+  __TEXT.__auth_stubs: 0x1bf0
+  __TEXT.__objc_methlist: 0x15444
+  __TEXT.__const: 0x5e0
   __TEXT.__dlopen_cstrs: 0x197
-  __TEXT.__unwind_info: 0x4f40
-  __TEXT.__objc_classname: 0x2ee4
-  __TEXT.__objc_methname: 0x38547
-  __TEXT.__objc_methtype: 0x7cca
-  __TEXT.__objc_stubs: 0x1c460
-  __DATA_CONST.__got: 0x1ac0
-  __DATA_CONST.__const: 0x4158
-  __DATA_CONST.__objc_classlist: 0x860
+  __TEXT.__gcc_except_tab: 0x3fc8
+  __TEXT.__cstring: 0x2710c
+  __TEXT.__oslogstring: 0x1f8cd
+  __TEXT.__unwind_info: 0x5028
+  __TEXT.__objc_classname: 0x2e97
+  __TEXT.__objc_methname: 0x383ea
+  __TEXT.__objc_methtype: 0x7c61
+  __TEXT.__objc_stubs: 0x1c500
+  __DATA_CONST.__got: 0x1ab0
+  __DATA_CONST.__const: 0x4130
+  __DATA_CONST.__objc_classlist: 0x858
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x498
+  __DATA_CONST.__objc_protolist: 0x490
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa860
+  __DATA_CONST.__objc_selrefs: 0xaa10
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x6a0
-  __DATA_CONST.__objc_arraydata: 0x440
-  __AUTH_CONST.__auth_got: 0xe20
+  __DATA_CONST.__objc_superrefs: 0x698
+  __DATA_CONST.__objc_arraydata: 0x450
+  __AUTH_CONST.__auth_got: 0xe10
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x1e40
-  __AUTH_CONST.__cfstring: 0x8f80
-  __AUTH_CONST.__objc_const: 0x25958
+  __AUTH_CONST.__const: 0x1e20
+  __AUTH_CONST.__cfstring: 0x8f40
+  __AUTH_CONST.__objc_const: 0x21b68
   __AUTH_CONST.__objc_intobj: 0xa20
   __AUTH_CONST.__objc_doubleobj: 0xb0
+  __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_floatobj: 0x4c0
-  __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x1a98
-  __DATA.__data: 0x36b0
-  __DATA.__bss: 0x660
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x1a7c
+  __DATA.__data: 0x3650
+  __DATA.__bss: 0x668
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x5050
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x198
+  __DATA_DIRTY.__bss: 0x180
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8317
-  Symbols:   10112
-  CStrings:  14592
+  Functions: 8265
+  Symbols:   10078
+  CStrings:  14559
 
Symbols:
+ _OBJC_CLASS_$_CSAudioProviderSelectingProxy
+ _OBJC_CLASS_$_CSFHashUtils
- _AVAudioSessionCategoryPlayback
- _AVAudioSessionModeDefault
- _AudioQueueNewOutput
- _CC_SHA256
- _OBJC_CLASS_$_CSAudioInjectionProviderExclave
- _OBJC_METACLASS_$_CSAudioInjectionProviderExclave
- _kCFRunLoopCommonModes
CStrings:
+ "\t"
+ "%s AOP trigger timestamp was 4 seconds the current time. Ignoring AOP trigger due to trigger time CONSTRAINT check"
+ "%s Asset Provider:%ld, Asset Variant: %ld, attemptAssetMapping:%d"
+ "%s Failed retrying to map asset with error %@"
+ "%s Failed retrying to map asset with version:%@"
+ "%s Fetched installed voicetrigger asset %@"
+ "%s Magus is not supported since locale is coupled with SAE and is ineligible"
+ "%s Mapping asset failed. Falling back to preinstalled asset with version:%@"
+ "%s Mapping is not supported hardware with no exclaves"
+ "%s Mapping is not supported hardware with no exclaves. Aborting retries."
+ "%s New task string: %{public}@, current task string: %{public}@"
+ "%s Should retry mapping asset? %@"
+ "%s SpeechController to receive data from VoiceIsolation Channel: %{public}tu"
+ "%s Successfully mapped asset with version:%@"
+ "%s Unable to find endpointer model for default task %{public}@"
+ "%s isSupported=%@: Is request during active call? %@, isDeviceSupported: %@, isFFEnabledOnDevice: %@, isSupportedRequestType: %@, isFFUserDisabled: %@, isTypeToSiriEnabled: %@, isLocaleInDenyList:%@, isSAEEnabled:%@, isLocaleUnsupportedWithSAE:%@ isLocaleCoupledWithSAE:%@"
+ "%s languageCode:  %{public}@ -voiceProfileArray: %{public}@, _currentAssets:%@"
+ "-[CSBuiltInVoiceTrigger _setAsset:]"
+ "-[CSBuiltInVoiceTrigger _setAsset:]_block_invoke"
+ "-[CSSpeechManager _mapAssetToExclaveKit:completion:]_block_invoke"
+ "-[CSSpeechManager _mapAssetToExclaveKit:completion:]_block_invoke_2"
+ "-[CSSpeechManager _retryMapAssetToExclaveKit:]_block_invoke"
+ "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]"
+ "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]_block_invoke"
+ "-[CSVoiceTriggerAssetHandler mapAssetToExclaveKit:completion:]_block_invoke"
+ "-[CSVoiceTriggerAssetHandler retryMappingAssetToExclaveKit:completion:]_block_invoke"
+ "Failed retrying to map asset with version:%@"
+ "Fallback_Secure_PreinstalledAsset"
+ "Mapping asset failed. Falling back to preinstalled asset with version:%@"
+ "Mapping_Secure_Asset_Succeeded"
+ "Retry_Mapping_Secure_Asset_Failed"
+ "Successfully mapped asset with version:%@"
+ "T@\"NSString\",&,N,V_currentTaskString"
+ "_currentTaskString"
+ "_isTaskStringAccessible:"
+ "_mapAssetToExclaveKit:completion:"
+ "_retryMapAssetToExclaveKit:"
+ "_runRetrainerWithAssets:languageCode:"
+ "_shouldUseVoiceIsolationChannel"
+ "addAudioSync:"
+ "ay12!Rd"
+ "channelForVoiceIsolation"
+ "cleanupVoiceProfileModelFilesForLocale:withAssets:"
+ "currentTaskString"
+ "enforceAutomaticEndpointing"
+ "installedCompactAssetOfType:language:"
+ "isCompactVersion"
+ "isMagusRestrictedWithSAEForLanguageCode:"
+ "resetForNewRequestSync"
+ "retryMappingAssetToExclaveKit:completion:"
+ "setAudioProviderImp:"
+ "setCurrentTaskString:"
+ "sha1StringFromInputData:"
+ "sha256DataFromInputData:"
+ "sharedContollerProxy"
+ "supportsPersonalizedHeySiri"
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
- "%s Fetched exclave audio injection enabled : %d"
- "%s Got Trial rollout for assetType: %lu for locale: %@ version: %@"
- "%s Setting exclave audio injection enabled : %d"
- "%s Successfully activate audioSession"
- "%s Successfully deactivate audioSession"
- "%s Successfully start the audio queue"
- "%s Unable to alloc AudioQueue AudioBuffer with OSStatus: %d"
- "%s Unable to find endpointer model for default task type %{public}@"
- "%s injection is ended at time: %llu"
- "%s isSupported=%@: Is request during active call? %@, isDeviceSupported: %@, isFFEnabledOnDevice: %@, isSupportedRequestType: %@, isFFUserDisabled: %@, isTypeToSiriEnabled: %@, isLocaleInDenyList:%@, isSAEEnabled:%@"
- "%s languageCode:  %{public}@ -voiceProfileArray: %{public}@, _currentAsset:%@"
- "-[CSAudioInjectionProviderExclave _createAudioQueueIfNeeded]"
- "-[CSAudioInjectionProviderExclave _defaultBufferRef]"
- "-[CSAudioInjectionProviderExclave _prepareAndStartAudioQueue]"
- "-[CSAudioInjectionProviderExclave _readAudioBufferAndFeedIntoAudioQueue]_block_invoke"
- "-[CSAudioInjectionProviderExclave _setAudioSessionActive:]"
- "-[CSAudioInjectionProviderExclave speakAudioInExclave:withCompletion:]_block_invoke"
- "-[CSBuiltInVoiceTrigger _setAsset:forceExclaveToUsePreInstalledAsset:]"
- "-[CSBuiltInVoiceTrigger _setAsset:forceExclaveToUsePreInstalledAsset:]_block_invoke"
- "-[CSBuiltInVoiceTrigger setAsset:forceExclaveToUsePreInstalledAsset:]"
- "-[CSSpeechManager _setAssetForBuiltInVoiceTrigger:completion:]_block_invoke_4"
- "-[CSTrialAssetManager _getSiriAttAssetsForType:forLocale:completion:]_block_invoke"
- "-[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]"
- "-[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]_block_invoke"
- "-[CSVoiceTriggerAssetHandlerMac mapAssetToExclaveKit:completion:]_block_invoke"
- "CSAudioInjectionProviderExclave"
- "CSVoiceTriggerAssetHandlerExclaveProtocol"
- "Mismatch between Current locale: %@ & Trial rollout locale: %@"
- "T@?,C,N,V_injectionCompletion"
- "TB,N,V_isAudioQueueStarted"
- "TQ,N,V_injectionEndTime"
- "TQ,N,V_injectionStartTime"
- "T^{OpaqueAudioQueue=},N,V_exclaveAudioQueue"
- "Trial asset bypass is set"
- "UAFLevelForFactor:withNamespaceName:withLanguage:"
- "Unable to get Trial factor: %@"
- "^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16@0:8"
- "_createAudioQueueIfNeeded"
- "_defaultBufferRef"
- "_exclaveAudioQueue"
- "_getSiriAttAssetsForType:forLocale:completion:"
- "_injectionCompletion"
- "_injectionEndTime"
- "_injectionStartTime"
- "_isAudioQueueStarted"
- "_prepareAndStartAudioQueue"
- "_readAudioBufferAndFeedIntoAudioQueue"
- "_setAsset:forceExclaveToUsePreInstalledAsset:"
- "_setAudioSessionActive:"
- "_sha256:"
- "addAudio:"
- "ay12!Rc"
- "bypassTrialAssets"
- "cleanupVoiceProfileModelFilesForLocale:withAsset:"
- "enableExclaveAudioInjection:"
- "exclaveAudioInjectionEnabled"
- "exclaveAudioQueue"
- "injectionCompletion"
- "injectionEndTime"
- "injectionStartTime"
- "isAudioQueueStarted"
- "metadata"
- "setAsset:forceExclaveToUsePreInstalledAsset:"
- "setCategory:mode:options:error:"
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
