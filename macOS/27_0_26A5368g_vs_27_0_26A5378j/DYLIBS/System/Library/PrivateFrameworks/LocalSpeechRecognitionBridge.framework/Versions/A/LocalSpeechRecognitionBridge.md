## LocalSpeechRecognitionBridge

> `/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/Versions/A/LocalSpeechRecognitionBridge`

```diff

-  __TEXT.__text: 0x1dd48
-  __TEXT.__objc_methlist: 0x2494
+  __TEXT.__text: 0x1f34c
+  __TEXT.__objc_methlist: 0x24ac
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x1d0
-  __TEXT.__cstring: 0x4794
-  __TEXT.__oslogstring: 0x297f
-  __TEXT.__unwind_info: 0x6f0
+  __TEXT.__gcc_except_tab: 0x208
+  __TEXT.__cstring: 0x4a2f
+  __TEXT.__oslogstring: 0x2c72
+  __TEXT.__unwind_info: 0x730
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x200
+  __DATA_CONST.__const: 0x240
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12e0
+  __DATA_CONST.__objc_selrefs: 0x1308
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x1e8
-  __AUTH_CONST.__const: 0x6b0
-  __AUTH_CONST.__cfstring: 0x1980
-  __AUTH_CONST.__objc_const: 0x3cb8
+  __AUTH_CONST.__const: 0x810
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
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 745
-  Symbols:   1830
-  CStrings:  787
+  Functions: 766
+  Symbols:   1867
+  CStrings:  813
 
Sections:
~ __TEXT.__const : content changed
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
+ GCC_except_table185
+ GCC_except_table340
+ GCC_except_table465
+ GCC_except_table469
+ GCC_except_table478
+ GCC_except_table488
+ GCC_except_table571
+ GCC_except_table689
+ GCC_except_table724
+ GCC_except_table729
+ GCC_except_table734
+ _LBSpeechRecognitionModeDescription
+ __145-[LBLocalSpeechRecognizerClient startCompanionRequestId:withStandaloneDisabled:inputOrigin:recordType:audioDeviceId:hostTime:shouldStartCapture:]_block_invoke
+ __49-[LBAudioStreamConsumer updateManualModeEnabled:]_block_invoke
+ __51-[LBAudioStreamConsumer updateStoppingWithHTTMode:]_block_invoke
+ __52-[LBAudioStreamConsumer _consumePackets:completion:]_block_invoke
+ __54-[LBAudioStreamConsumer _stopConsumingWithCompletion:]_block_invoke
+ __54-[LBAudioStreamConsumer _stopConsumingWithCompletion:]_block_invoke_2
+ __69-[LBAudioStreamConsumer _startConsumingWithConfiguration:completion:]_block_invoke
+ __69-[LBAudioStreamConsumer _startConsumingWithConfiguration:completion:]_block_invoke_2
+ ___145-[LBLocalSpeechRecognizerClient startCompanionRequestId:withStandaloneDisabled:inputOrigin:recordType:audioDeviceId:hostTime:shouldStartCapture:]_block_invoke
+ ___145-[LBLocalSpeechRecognizerClient startCompanionRequestId:withStandaloneDisabled:inputOrigin:recordType:audioDeviceId:hostTime:shouldStartCapture:]_block_invoke_2
+ ___52-[LBAudioStreamConsumer _consumePackets:completion:]_block_invoke_2
+ ___54-[LBAudioStreamConsumer _stopConsumingWithCompletion:]_block_invoke
+ ___54-[LBAudioStreamConsumer _stopConsumingWithCompletion:]_block_invoke_2
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32bs40r48w_e5_v8?0l
+ ___block_descriptor_57_e8_32s40s48s_e20_v20?0B8"NSError"12l
+ ___block_descriptor_64_e8_32s40bs48r56w_e17_v16?0"NSError"8l
+ ___block_descriptor_64_e8_32s40bs48r56w_e20_v20?0B8"NSError"12l
+ ___block_descriptor_64_e8_32s40bs48r56w_e5_v8?0l
+ ___block_descriptor_66_e8_32s40s48s56s_e5_v8?0l
+ ___block_descriptor_73_e8_32s40s48bs56r64w_e5_v8?0l
+ ___block_descriptor_82_e8_32s40s48s56s_e5_v8?0l
+ ___copy_helper_block_e8_32b40r48w
+ ___copy_helper_block_e8_32s40b48r56w
+ ___copy_helper_block_e8_32s40s48b56r64w
+ ___copy_helper_block_e8_32s40s48s56s
+ ___destroy_helper_block_e8_32s40r48w
+ ___destroy_helper_block_e8_32s40s48r56w
+ ___destroy_helper_block_e8_32s40s48s56r64w
+ _objc_msgSend$_serviceWithErrorHandler:
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$startCompanionRequestId:withStandaloneDisabled:inputOrigin:
+ _objc_msgSend$stopConsumingForRequestId:completion:
+ _objc_msgSend$streamInfo
+ _objc_unsafeClaimAutoreleasedReturnValue
- -[LBAudioStreamConsumer _service]
- GCC_except_table180
- GCC_except_table335
- GCC_except_table458
- GCC_except_table462
- GCC_except_table471
- GCC_except_table552
- GCC_except_table668
- GCC_except_table703
- GCC_except_table708
- GCC_except_table713
- ___block_descriptor_56_e8_32s40bs48w_e20_v20?0B8"NSError"12l
- ___block_descriptor_65_e8_32s40s48bs56w_e5_v8?0l
- ___copy_helper_block_e8_32s40s48b56w
- ___destroy_helper_block_e8_32s40s48s56w
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
