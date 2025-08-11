## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2145.61.1.0.0
-  __TEXT.__text: 0x792424
+2145.62.1.2.0
+  __TEXT.__text: 0x792504
   __TEXT.__auth_stubs: 0x5600
-  __TEXT.__objc_methlist: 0x35968
+  __TEXT.__objc_methlist: 0x35980
   __TEXT.__const: 0xc760
-  __TEXT.__cstring: 0x8ef1a
-  __TEXT.__oslogstring: 0x10e57a
-  __TEXT.__gcc_except_tab: 0x2ab0
+  __TEXT.__cstring: 0x8ef02
+  __TEXT.__oslogstring: 0x10e5c4
+  __TEXT.__gcc_except_tab: 0x2a80
   __TEXT.__ustring: 0x2d4
-  __TEXT.__unwind_info: 0x10828
+  __TEXT.__unwind_info: 0x10820
   __TEXT.__objc_classname: 0x4eb2
-  __TEXT.__objc_methname: 0x7d752
+  __TEXT.__objc_methname: 0x7d75e
   __TEXT.__objc_methtype: 0x28277
   __TEXT.__objc_stubs: 0x4e9c0
   __DATA_CONST.__got: 0x1a30
-  __DATA_CONST.__const: 0x6a80
+  __DATA_CONST.__const: 0x6a30
   __DATA_CONST.__objc_classlist: 0x12e8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x488

   __AUTH_CONST.__auth_got: 0x2b18
   __AUTH_CONST.__const: 0x3bc8
   __AUTH_CONST.__cfstring: 0x261c0
-  __AUTH_CONST.__objc_const: 0x63388
+  __AUTH_CONST.__objc_const: 0x63390
   __AUTH_CONST.__objc_intobj: 0x4968
   __AUTH_CONST.__objc_arrayobj: 0x1b30
   __AUTH_CONST.__objc_floatobj: 0x30

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5516BA11-CC7A-3B3B-88C4-72E2D68714DA
+  UUID: C0B620B4-D482-3C8C-8283-1C3A5D6107DA
   Functions: 31529
-  Symbols:   97231
+  Symbols:   97233
   CStrings:  57117
 
Symbols:
+ -[VCAudioCaptionsSpeechAnalyzer packageAndSendTranscriberResult:withTask:final:].cold.1
+ -[VCVideoCaptureServer dispatchedStartSystemAudioForClientKey:forSource:]
+ -[VCVideoCaptureServer dispatchedStartSystemAudioForClientKey:forSource:].cold.1
+ -[VCVideoCaptureServer dispatchedStartSystemAudioForClientKey:forSource:].cold.2
+ -[VCVideoCaptureServer dispatchedStartSystemAudioForClientKey:forSource:].cold.3
+ -[VCVideoCaptureServer dispatchedStartSystemAudioForClientKey:forSource:].cold.4
+ -[VCVideoCaptureServer dispatchedStartSystemAudioForClientKey:forSource:].cold.5
+ -[VCVideoCaptureServer dispatchedStopSystemAudioForClientKey:forSource:]
+ -[VCVideoCaptureServer dispatchedStopSystemAudioForClientKey:forSource:].cold.1
+ -[VCVideoCaptureServer dispatchedStopSystemAudioForClientKey:forSource:].cold.2
+ GCC_except_table109
+ _OBJC_IVAR_$_AVCStatisticsCollector._statisticsReadCount
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_VCCaptionsSource
+ ___45-[VCCaptionsManager registerBlocksForService]_block_invoke.118
+ ___45-[VCCaptionsManager registerBlocksForService]_block_invoke.130
+ ___45-[VCCaptionsManager registerBlocksForService]_block_invoke.133
+ ___45-[VCCaptionsManager registerBlocksForService]_block_invoke.151
+ ___58-[VCSession(Messaging) setupLinkConstrainsChangedMessages]_block_invoke_2
+ ___block_literal_global.20
+ _objc_msgSend$dispatchedStartSystemAudioForClientKey:forSource:
+ _objc_msgSend$dispatchedStopSystemAudioForClientKey:forSource:
- -[VCAudioCaptions initWithDelegate:isLocal:taskIdentifier:reportingAgent:].cold.9
- -[VCAudioMachineLearningCoordinator setUpReportingAgent].cold.1
- -[VCVideoCaptureServer dispatchedStartSystemAudioForClientKey:]
- -[VCVideoCaptureServer dispatchedStartSystemAudioForClientKey:].cold.1
- -[VCVideoCaptureServer dispatchedStartSystemAudioForClientKey:].cold.2
- -[VCVideoCaptureServer dispatchedStartSystemAudioForClientKey:].cold.3
- -[VCVideoCaptureServer dispatchedStartSystemAudioForClientKey:].cold.4
- -[VCVideoCaptureServer dispatchedStartSystemAudioForClientKey:].cold.5
- -[VCVideoCaptureServer dispatchedStopSystemAudioForClientKey:]
- -[VCVideoCaptureServer dispatchedStopSystemAudioForClientKey:].cold.1
- -[VCVideoCaptureServer dispatchedStopSystemAudioForClientKey:].cold.2
- GCC_except_table105
- GCC_except_table110
- _OBJC_IVAR_$_VCAudioCaptions._analyzerAllResultsSemaphore
- ___45-[VCAudioCaptions stopWithCompletionHandler:]_block_invoke.104
- ___45-[VCCaptionsManager registerBlocksForService]_block_invoke.116
- ___45-[VCCaptionsManager registerBlocksForService]_block_invoke.128
- ___45-[VCCaptionsManager registerBlocksForService]_block_invoke.131
- ___45-[VCCaptionsManager registerBlocksForService]_block_invoke.149
- ___block_descriptor_56_e8_32o40b48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32o40b48r_e5_v8?0ls32l8s40l8r48l8
- _objc_msgSend$dispatchedStartSystemAudioForClientKey:
- _objc_msgSend$dispatchedStopSystemAudioForClientKey:
CStrings:
+ " [%s] %s:%d %@(%p) didUpdateTaskInfo=%{BOOL}d, task=%@, analyzer=%@, fetchedInfo=%@, newInfo=%@"
+ " [%s] %s:%d @:@ VCAudioMachineLearningCoordinator-invalidate (%p)"
+ " [%s] %s:%d Re-applying mute=%d"
+ " [%s] %s:%d didUpdateTaskInfo=%{BOOL}d, task=%@, analyzer=%@, fetchedInfo=%@, newInfo=%@"
+ "-[VCVideoCaptureServer dispatchedStartSystemAudioForClientKey:forSource:]"
+ "-[VCVideoCaptureServer dispatchedStopSystemAudioForClientKey:forSource:]"
+ "2145.62.1.2"
+ "@:@ VCAudioMachineLearningCoordinator-invalidate"
+ "_statisticsReadCount"
+ "dispatchedStartSystemAudioForClientKey:forSource:"
+ "dispatchedStopSystemAudioForClientKey:forSource:"
- " [%s] %s:%d %@(%p) Failed to create _analyzerAllResultsSemaphore"
- " [%s] %s:%d %@(%p) Waiting for speech analyzer all results did timeout"
- " [%s] %s:%d Failed to create _analyzerAllResultsSemaphore"
- " [%s] %s:%d Waiting for speech analyzer all results did timeout"
- "-[VCAudioCaptions stopWithCompletionHandler:]"
- "-[VCVideoCaptureServer dispatchedStartSystemAudioForClientKey:]"
- "-[VCVideoCaptureServer dispatchedStopSystemAudioForClientKey:]"
- "2145.61.1"
- "_analyzerAllResultsSemaphore"
- "dispatchedStartSystemAudioForClientKey:"
- "dispatchedStopSystemAudioForClientKey:"

```
