## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-3500.122.2.0.0
-  __TEXT.__text: 0x16ea38
+3505.14.3.0.0
+  __TEXT.__text: 0x16f380
   __TEXT.__auth_stubs: 0x16e0
-  __TEXT.__objc_stubs: 0x1e7e0
-  __TEXT.__objc_methlist: 0x1841c
+  __TEXT.__objc_stubs: 0x1e860
+  __TEXT.__objc_methlist: 0x18484
   __TEXT.__dlopen_cstrs: 0x2c5
   __TEXT.__const: 0x360
   __TEXT.__gcc_except_tab: 0x3cc4
-  __TEXT.__objc_methname: 0x3e430
-  __TEXT.__cstring: 0x2a9ca
-  __TEXT.__oslogstring: 0x21572
+  __TEXT.__objc_methname: 0x3e603
+  __TEXT.__cstring: 0x2aad7
+  __TEXT.__oslogstring: 0x2169c
   __TEXT.__objc_classname: 0x34dd
-  __TEXT.__objc_methtype: 0x8634
-  __TEXT.__unwind_info: 0x55e0
+  __TEXT.__objc_methtype: 0x8671
+  __TEXT.__unwind_info: 0x55f8
   __DATA_CONST.__auth_got: 0xb88
-  __DATA_CONST.__got: 0x1380
+  __DATA_CONST.__got: 0x1398
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x5db8
-  __DATA_CONST.__cfstring: 0x8860
+  __DATA_CONST.__cfstring: 0x88a0
   __DATA_CONST.__objc_classlist: 0x978
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x4e0

   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_dictobj: 0x348
   __DATA_CONST.__objc_floatobj: 0x4b0
-  __DATA.__objc_const: 0x26fa0
-  __DATA.__objc_selrefs: 0xb7a0
-  __DATA.__objc_ivar: 0x1dc8
+  __DATA.__objc_const: 0x27008
+  __DATA.__objc_selrefs: 0xb7e0
+  __DATA.__objc_ivar: 0x1dd0
   __DATA.__objc_data: 0x5eb0
   __DATA.__data: 0x3a80
   __DATA.__bss: 0x718

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 2E1E9AE6-20D6-325D-B62D-CE2E4E550D40
-  Functions: 9309
-  Symbols:   1007
-  CStrings:  16619
+  UUID: 3D6914BD-19FE-310A-A202-42FF446447B0
+  Functions: 9320
+  Symbols:   1010
+  CStrings:  16642
 
Symbols:
+ _NSURLIsPurgeableKey
+ _OBJC_CLASS_$_CSRemoteAssetManagerFactory
+ _OBJC_CLASS_$_SSRSecureAssetProvider
+ _OBJC_CLASS_$_SSRVoiceProfileManagerXPCListener
+ _SSRVoiceRetrainingSecureAssetKey
- _OBJC_CLASS_$_CSDADataAnalyticsController
- _OBJC_CLASS_$_CSRemoteAssetManager
CStrings:
+ "%@-%@"
+ "%s Audio capture folder name %@ is too short to parse date time"
+ "%s Failed to check purgeable status for file %@"
+ "%s Failed to get secure audio capture"
+ "%s Failed to get secure audio logging directory"
+ "%s Failed to move secure audio capture file %@"
+ "%s Secure audio capture file %@ copied successfully"
+ "%s Secure audio capture file %@ skipped (likely in progress)"
+ "-[CSVoiceProfileRetrainManager _retrainingVoiceProfile:voiceProfile:asset:secureAsset:]"
+ "-[CSVoiceProfileRetrainManager _retrainingVoiceProfile:voiceProfile:asset:secureAsset:]_block_invoke"
+ "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:withSecureAsset:languageCode:]"
+ "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:withSecureAsset:languageCode:]_block_invoke"
+ "-[CSVoiceProfileRetrainManager triggerVoiceProfileRetrainingWithAsset:withSecureAsset:]_block_invoke"
+ "-[CSVoiceTriggerFileLogger _moveSecureAudioCaptureFrom:withExclaveTimestamp:]"
+ "-[CSVoiceTriggerFileLogger _syncAvailableSecureCaptures]"
+ "/var/mobile/tmp/com.apple.corespeechd/AudioCapture/siri"
+ "@\"SSRVoiceProfileManagerXPCListener\""
+ "Q32@0:8Q16Q24"
+ "T@\"SSRVoiceProfileManagerXPCListener\",&,N,V_voiceProfileManagerXPCListener"
+ "_getSecondPassRejectReasonFromExclaveKeywordResult:speakerDetectionResult:"
+ "_moveSecureAudioCaptureFrom:withExclaveTimestamp:"
+ "_retrainingVoiceProfile:voiceProfile:asset:secureAsset:"
+ "_runRetrainerWithAssets:withSecureAsset:languageCode:"
+ "_runVoiceProfileRetrainerWithAsset:withSecureAsset:withLanguageCode:"
+ "_syncAvailableSecureCaptures"
+ "_voiceProfileManagerXPCListener"
+ "audioRecorderSensorInvalidated:"
+ "fetchSecureAssetForLocale:withAsset:"
+ "getSecondPassRejectReasonFromExclaveKeywordResult:speakerDetectionResult:"
+ "needRetrainingForExclaveOnly"
+ "remoteAssetManager"
+ "setVoiceProfileManagerXPCListener:"
+ "substringFromIndex:"
+ "triggerVoiceProfileRetrainingWithAsset:withSecureAsset:"
+ "v24@0:8@\"<CSRemoteAssetManagerProtocol>\"16"
+ "voiceProfileManagerXPCListener"
- "%s asr task checking: %@"
- "%s rpiSamplingEnabled checking: %@"
- "-[CSVoiceProfileRetrainManager _retrainingVoiceProfile:voiceProfile:asset:]"
- "-[CSVoiceProfileRetrainManager _retrainingVoiceProfile:voiceProfile:asset:]_block_invoke"
- "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]"
- "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]_block_invoke"
- "-[CSVoiceProfileRetrainManager triggerVoiceProfileRetrainingWithAsset:]_block_invoke"
- "_retrainingVoiceProfile:voiceProfile:asset:"
- "_runRetrainerWithAssets:languageCode:"
- "_runVoiceProfileRetrainerWithAsset:withLanguageCode:"
- "initWithLocale:fbfBundleId:"
- "initWithRequestId:asrId:languageCode:task:rpiEnabled:"
- "shouldStartAudioLogIsVoiceTrigger:isButtonPress:"
- "triggerVoiceProfileRetrainingWithAsset:"
- "v24@0:8@\"CSRemoteAssetManager\"16"

```
