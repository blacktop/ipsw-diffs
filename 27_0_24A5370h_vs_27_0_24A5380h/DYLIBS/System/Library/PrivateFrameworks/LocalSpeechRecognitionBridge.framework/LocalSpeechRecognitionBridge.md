## LocalSpeechRecognitionBridge

> `/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/LocalSpeechRecognitionBridge`

```diff

-  __TEXT.__text: 0x1bfb8
-  __TEXT.__objc_methlist: 0x2494
+  __TEXT.__text: 0x1d314
+  __TEXT.__objc_methlist: 0x24ac
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x1d0
-  __TEXT.__cstring: 0x46e6
-  __TEXT.__oslogstring: 0x297f
-  __TEXT.__unwind_info: 0x6b0
+  __TEXT.__const: 0xb0
+  __TEXT.__gcc_except_tab: 0x208
+  __TEXT.__cstring: 0x4981
+  __TEXT.__oslogstring: 0x2c72
+  __TEXT.__unwind_info: 0x6e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x728
+  __DATA_CONST.__const: 0x858
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12e0
+  __DATA_CONST.__objc_selrefs: 0x1308
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x1e8
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x1980
-  __AUTH_CONST.__objc_const: 0x3cb8
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0x1a20
+  __AUTH_CONST.__objc_const: 0x3cc0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x5a0
   __DATA.__objc_ivar: 0x2c0
   __DATA.__data: 0x8b0
-  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x320
-  __DATA_DIRTY.__bss: 0x48
+  __DATA_DIRTY.__bss: 0x58
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 718
-  Symbols:   2539
-  CStrings:  785
+  Functions: 734
+  Symbols:   2586
+  CStrings:  811
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[LBLocalSpeechRecognitionSettings companionSettingsWithRequestId:inputOrigin:]
+ -[LBAudioStreamConsumer _serviceWithErrorHandler:]
+ -[LBLocalSpeechRecognizerClient startCompanionRequestId:withStandaloneDisabled:inputOrigin:recordType:audioDeviceId:hostTime:shouldStartCapture:]
+ GCC_except_table167
+ GCC_except_table320
+ GCC_except_table443
+ GCC_except_table447
+ GCC_except_table453
+ GCC_except_table460
+ GCC_except_table541
+ GCC_except_table657
+ GCC_except_table692
+ GCC_except_table697
+ GCC_except_table702
+ _LBSpeechRecognitionModeDescription
+ ___145-[LBLocalSpeechRecognizerClient startCompanionRequestId:withStandaloneDisabled:inputOrigin:recordType:audioDeviceId:hostTime:shouldStartCapture:]_block_invoke
+ ___145-[LBLocalSpeechRecognizerClient startCompanionRequestId:withStandaloneDisabled:inputOrigin:recordType:audioDeviceId:hostTime:shouldStartCapture:]_block_invoke_2
+ ___52-[LBAudioStreamConsumer _consumePackets:completion:]_block_invoke_2
+ ___54-[LBAudioStreamConsumer _stopConsumingWithCompletion:]_block_invoke
+ ___54-[LBAudioStreamConsumer _stopConsumingWithCompletion:]_block_invoke_2
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32bs40r48w_e5_v8?0lw48l8r40l8s32l8
+ ___block_descriptor_57_e8_32s40s48s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs48r56w_e17_v16?0"NSError"8ls32l8w56l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40bs48r56w_e20_v20?0B8"NSError"12lw56l8r48l8s40l8s32l8
+ ___block_descriptor_64_e8_32s40bs48r56w_e5_v8?0lw56l8r48l8s32l8s40l8
+ ___block_descriptor_66_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48bs56r64w_e5_v8?0lw64l8r56l8s32l8s48l8s40l8
+ ___block_descriptor_82_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ _objc_msgSend$_serviceWithErrorHandler:
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$startCompanionRequestId:withStandaloneDisabled:inputOrigin:
+ _objc_msgSend$stopConsumingForRequestId:completion:
+ _objc_msgSend$streamInfo
+ _objc_unsafeClaimAutoreleasedReturnValue
- -[LBAudioStreamConsumer _service]
- GCC_except_table163
- GCC_except_table316
- GCC_except_table437
- GCC_except_table441
- GCC_except_table448
- GCC_except_table527
- GCC_except_table641
- GCC_except_table676
- GCC_except_table681
- GCC_except_table686
- ___block_descriptor_56_e8_32s40bs48w_e20_v20?0B8"NSError"12lw48l8s40l8s32l8
- ___block_descriptor_65_e8_32s40s48bs56w_e5_v8?0lw56l8s48l8s32l8s40l8
CStrings:
+ "%s #stream XPC connection error during consumePackets: %@"
+ "%s #stream XPC connection error during startConsuming: %@"
+ "%s #stream XPC connection error during stopConsuming: %@"
+ "%s #stream XPC connection error during updateManualModeEnabled: %@"
+ "%s #stream XPC connection error during updateStoppingWithHTTMode: %@"
+ "%s #stream configuration.streamInfo is nil"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:Failed to start audio capture with error : %@"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:requestId: %@ — ignored: standaloneDisabled is NO"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:requestId: %@, shouldStartCapture: %d"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:starting audio capture with hostTime: %llu"
+ "-[LBAudioStreamConsumer _consumePackets:completion:]_block_invoke_2"
+ "-[LBAudioStreamConsumer _stopConsumingWithCompletion:]_block_invoke_2"
+ "-[LBLocalSpeechRecognizerClient startCompanionRequestId:withStandaloneDisabled:inputOrigin:recordType:audioDeviceId:hostTime:shouldStartCapture:]"
+ "-[LBLocalSpeechRecognizerClient startCompanionRequestId:withStandaloneDisabled:inputOrigin:recordType:audioDeviceId:hostTime:shouldStartCapture:]_block_invoke"
+ "-[LBLocalSpeechRecognizerClient startCompanionRequestId:withStandaloneDisabled:inputOrigin:recordType:audioDeviceId:hostTime:shouldStartCapture:]_block_invoke_2"
+ "Classic"
+ "Companion"
+ "FullUOD"
+ "Hybrid"
+ "Unknown(%lu)"
+ "[speechRecognitionMode = %@]"
+ "v16@?0@\"NSError\"8"
- "[speechRecognitionMode = %lu]"

```
