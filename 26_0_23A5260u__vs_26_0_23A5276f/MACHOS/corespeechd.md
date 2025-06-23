## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-3500.97.2.1.1
-  __TEXT.__text: 0x16fa94
+3500.104.2.0.0
+  __TEXT.__text: 0x170470
   __TEXT.__auth_stubs: 0x16f0
-  __TEXT.__objc_stubs: 0x1ea00
-  __TEXT.__objc_methlist: 0x184cc
+  __TEXT.__objc_stubs: 0x1eb20
+  __TEXT.__objc_methlist: 0x1853c
   __TEXT.__dlopen_cstrs: 0x2c5
   __TEXT.__const: 0x360
   __TEXT.__gcc_except_tab: 0x3d78
-  __TEXT.__objc_methname: 0x3e6f8
-  __TEXT.__cstring: 0x2ac6a
-  __TEXT.__oslogstring: 0x2150c
-  __TEXT.__objc_classname: 0x350d
+  __TEXT.__objc_methname: 0x3e89d
+  __TEXT.__cstring: 0x2adee
+  __TEXT.__oslogstring: 0x216ad
+  __TEXT.__objc_classname: 0x3532
   __TEXT.__objc_methtype: 0x871f
-  __TEXT.__unwind_info: 0x5610
+  __TEXT.__unwind_info: 0x5620
   __DATA_CONST.__auth_got: 0xb90
   __DATA_CONST.__got: 0x13d0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x5e40
-  __DATA_CONST.__cfstring: 0x88a0
-  __DATA_CONST.__objc_classlist: 0x978
+  __DATA_CONST.__cfstring: 0x88e0
+  __DATA_CONST.__objc_classlist: 0x980
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x4f0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_dictobj: 0x348
   __DATA_CONST.__objc_floatobj: 0x4b0
-  __DATA.__objc_const: 0x270c8
-  __DATA.__objc_selrefs: 0xb868
-  __DATA.__objc_ivar: 0x1dd8
-  __DATA.__objc_data: 0x5eb0
+  __DATA.__objc_const: 0x271b8
+  __DATA.__objc_selrefs: 0xb8c0
+  __DATA.__objc_ivar: 0x1de0
+  __DATA.__objc_data: 0x5f00
   __DATA.__data: 0x3b40
   __DATA.__bss: 0x738
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
-  UUID: 4C35348F-987B-3E99-9AF2-722C6FE9F7AD
-  Functions: 9333
-  Symbols:   1022
-  CStrings:  16677
+  UUID: C35B9E88-1B63-3EB9-9768-8EF54C9A4577
+  Functions: 9346
+  Symbols:   1018
+  CStrings:  16705
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "%s A supported notification was NOT handled: %@"
+ "%s At %llu notifying self trigger detected with audioSourceType %{public}lu : %{public}@"
+ "%s Fetched asset is nil (including default fallback), ignore notification"
+ "%s HearstRouteStatus: %d, isHearstHijackable? %@, shouldHandle: %d"
+ "%s Is BargeIn allowed: %u"
+ "%s isBargeInAllowed :%u"
+ "%s isBargeInDisabledPref:%u, isJarvisCarplayConnected:%u, isBargeInDisabledForCarplay:%u"
+ "%s isRecordRouteJarvis:%u, isBuiltInRecordRoute:%u, isPlaybackRouteCarAudio:%u, isBuiltInRecordAndPlaybackRoute:%u"
+ "%s recordRoute:%@, playbackRoute:%@"
+ "+[CSAttSiriMagusBargeInDecisionChecker isBargeInAllowedForAudioSource:withCompletion:]"
+ "+[CSAttSiriMagusBargeInDecisionChecker isBargeInAllowedForAudioSource:withCompletion:]_block_invoke"
+ "-[CSIntuitiveConvRequestHandler _handleClientDidStopWithOption:]_block_invoke_2"
+ "-[CSPDispatcher handleDarwinNotificationEventWithName:]_block_invoke"
+ "-[CSSelfTriggerDetector _processAudioChunk:]"
+ "-[CSVoiceTriggerFirstPassHearst _shouldHandleHearstActivation]"
+ "CSAttSiriMagusBargeInDecisionChecker"
+ "TB,N,V_didReceiveFirstBuffer"
+ "_didReceiveFirstBuffer"
+ "_digitalZeroChunkFromFirstAudioChunk:"
+ "_processAudioChunk:"
+ "_shouldHandleHearstActivation"
+ "_wait"
+ "com.apple.corespeechd.speechprofileassetstartup"
+ "com.apple.corespeechd.speechprofilefirstunlock"
+ "didReceiveFirstBuffer"
+ "digitalZeroChunkWithDurationInSec:startSampleCount:hostTime:"
+ "initWithRequestId:asrId:dictationInteractionId:languageCode:task:isSamplingForDictation:"
+ "initWithSpeechManager:voiceTriggerEnabledMonitor:siriClientBehaviorMonitor:phoneCallStateMonitor:otherAppRecordingStateMonitor:audioRouteChangeMonitor:"
+ "isAutomaticCompilationEnabled"
+ "isBargeInAllowedForAudioSource:withCompletion:"
+ "isFloat"
+ "isPlaybackRouteCarAudio:"
+ "sampleByteDepth"
+ "setDidReceiveFirstBuffer:"
+ "updateRequiredLocales"
- "%s BargeIn disabled:%u"
- "%s Notifying self trigger detected with audioSourceType %{public}lu : %{public}@"
- "%s RequestCtx already exists for requestId: %@"
- "-[CSPDispatcher handleDarwinNotificationEventWithName:]_block_invoke_4"
- "-[CSSelfTriggerDetector audioStreamProvider:audioBufferAvailable:]_block_invoke"
- "handleAssetUpdate"
- "handleSettingsChange"
- "initWithDictationInteractionId:asrId:languageCode:task:"
- "initWithSpeechManager:voiceTriggerEnabledMonitor:siriClientBehaviorMonitor:phoneCallStateMonitor:otherAppRecordingStateMonitor:"

```
