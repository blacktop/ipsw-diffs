## LocalSpeechRecognitionBridge

> `/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/LocalSpeechRecognitionBridge`

```diff

-3300.119.1.1.7
-  __TEXT.__text: 0xb4a8
+3301.20.3.0.0
+  __TEXT.__text: 0xb680
   __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_methlist: 0x98c
+  __TEXT.__objc_methlist: 0x9bc
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__cstring: 0x1f21
-  __TEXT.__oslogstring: 0xaf5
+  __TEXT.__cstring: 0x1f43
+  __TEXT.__oslogstring: 0xb1d
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0x2b4
+  __TEXT.__unwind_info: 0x2c8
   __TEXT.__objc_classname: 0x171
-  __TEXT.__objc_methname: 0x4054
-  __TEXT.__objc_methtype: 0xd55
-  __TEXT.__objc_stubs: 0x16c0
+  __TEXT.__objc_methname: 0x413c
+  __TEXT.__objc_methtype: 0xd69
+  __TEXT.__objc_stubs: 0x16e0
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x358
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2f18
-  __DATA_CONST.__objc_selrefs: 0x830
+  __DATA_CONST.__objc_const: 0x2f48
+  __DATA_CONST.__objc_selrefs: 0x848
   __AUTH_CONST.__cfstring: 0xaa0
   __AUTH_CONST.__objc_const: 0x240
   __AUTH_CONST.__const: 0x20

   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0xe0
   __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0xf8
+  __DATA.__objc_ivar: 0xfc
   __DATA.__data: 0x3d0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FA21D471-47F4-3D45-A806-385E39BDF5B3
-  Functions: 246
-  Symbols:   1020
-  CStrings:  839
+  UUID: 084A63C6-A84C-328C-BDEB-7223B184B5E3
+  Functions: 251
+  Symbols:   1032
+  CStrings:  844
 
Symbols:
+ -[LBAudioCapture _stopStreamOptionWithReason:forRequestId:]
+ -[LBAudioCapture stopAudioCaptureWithReason:requestId:completion:]
+ -[LBLocalSpeechRecognizerClient _stopSpeechRecognitionTaskWithReason:requestId:shouldInvalidateAfterStop:completion:]
+ -[LBLocalSpeechRecognizerClient requestId]
+ -[LBLocalSpeechRecognizerClient setRequestId:]
+ -[LBLocalSpeechRecognizerClient stopSpeechRecognitionTaskAndInvalidateWithReason:requestId:completion:]
+ GCC_except_table12
+ GCC_except_table141
+ GCC_except_table201
+ GCC_except_table84
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerClient._requestId
+ __OBJC_$_PROP_LIST_NSObject.139
+ __OBJC_$_PROP_LIST_NSObject.201
+ __OBJC_$_PROP_LIST_NSObject.285
+ __OBJC_$_PROP_LIST_NSObject.30
+ __OBJC_$_PROP_LIST_NSObject.569
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.570
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBAttendingStatesService.140
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBAttendingStatesServiceDelegate.141
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.142
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.202
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.286
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.31
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.571
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.572
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LBAttendingStatesServiceDelegate.143
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.144
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.203
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.287
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.32
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.573
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.574
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBAttendingStatesService.145
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBAttendingStatesServiceDelegate.146
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.147
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.204
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.288
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.33
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.575
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.576
+ __OBJC_$_PROTOCOL_REFS_LBAttendingStatesService.148
+ __OBJC_$_PROTOCOL_REFS_LBAttendingStatesServiceDelegate.149
+ ___103-[LBLocalSpeechRecognizerClient stopSpeechRecognitionTaskAndInvalidateWithReason:requestId:completion:]_block_invoke
+ ___117-[LBLocalSpeechRecognizerClient _stopSpeechRecognitionTaskWithReason:requestId:shouldInvalidateAfterStop:completion:]_block_invoke
+ ___44-[LBLocalSpeechRecognizerClient _connection]_block_invoke.41
+ ___66-[LBAudioCapture stopAudioCaptureWithReason:requestId:completion:]_block_invoke
+ ___66-[LBAudioCapture stopAudioCaptureWithReason:requestId:completion:]_block_invoke.5
+ ___66-[LBAudioCapture stopAudioCaptureWithReason:requestId:completion:]_block_invoke_2
+ ___block_descriptor_65_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ _objc_msgSend$_stopSpeechRecognitionTaskWithReason:requestId:shouldInvalidateAfterStop:completion:
+ _objc_msgSend$_stopStreamOptionWithReason:forRequestId:
+ _objc_msgSend$initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:requestId:
+ _objc_msgSend$stopAudioCaptureWithReason:requestId:completion:
- -[LBAudioCapture _stopStreamOptionWithReason:]
- -[LBAudioCapture stopAudioCaptureWithReason:completion:]
- GCC_except_table10
- GCC_except_table136
- GCC_except_table196
- GCC_except_table79
- __OBJC_$_PROP_LIST_NSObject.131
- __OBJC_$_PROP_LIST_NSObject.194
- __OBJC_$_PROP_LIST_NSObject.282
- __OBJC_$_PROP_LIST_NSObject.39
- __OBJC_$_PROP_LIST_NSObject.575
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.576
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBAttendingStatesService.132
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBAttendingStatesServiceDelegate.133
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.134
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.195
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.283
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.40
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.577
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.578
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LBAttendingStatesServiceDelegate.135
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.136
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.196
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.284
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.41
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.579
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.580
- __OBJC_$_PROTOCOL_METHOD_TYPES_LBAttendingStatesService.137
- __OBJC_$_PROTOCOL_METHOD_TYPES_LBAttendingStatesServiceDelegate.138
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.139
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.197
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.285
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.42
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.581
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.582
- __OBJC_$_PROTOCOL_REFS_LBAttendingStatesService.140
- __OBJC_$_PROTOCOL_REFS_LBAttendingStatesServiceDelegate.141
- ___44-[LBLocalSpeechRecognizerClient _connection]_block_invoke.42
- ___56-[LBAudioCapture stopAudioCaptureWithReason:completion:]_block_invoke
- ___56-[LBAudioCapture stopAudioCaptureWithReason:completion:]_block_invoke.5
- ___56-[LBAudioCapture stopAudioCaptureWithReason:completion:]_block_invoke_2
- ___90-[LBLocalSpeechRecognizerClient stopSpeechRecognitionTaskWithReason:requestId:completion:]_block_invoke.8
- ___block_descriptor_64_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
- _objc_msgSend$_stopStreamOptionWithReason:
- _objc_msgSend$initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:
- _objc_msgSend$stopAudioCaptureWithReason:completion:
CStrings:
+ "\x04#"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:reason : %{public}lu, requestId %@, shouldInvalidate %d"
+ "%s start audio capture with recordContext : %{public}@, hostTime : %llu siriSessionUUID:%@"
+ "-[LBAudioCapture stopAudioCaptureWithReason:requestId:completion:]"
+ "-[LBAudioCapture stopAudioCaptureWithReason:requestId:completion:]_block_invoke"
+ "-[LBLocalSpeechRecognizerClient _stopSpeechRecognitionTaskWithReason:requestId:shouldInvalidateAfterStop:completion:]"
+ "@32@0:8Q16@24"
+ "T@\"NSString\",&,N,V_requestId"
+ "_stopSpeechRecognitionTaskWithReason:requestId:shouldInvalidateAfterStop:completion:"
+ "_stopStreamOptionWithReason:forRequestId:"
+ "initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:requestId:"
+ "setRequestId:"
+ "stopAudioCaptureWithReason:requestId:completion:"
+ "stopSpeechRecognitionTaskAndInvalidateWithReason:requestId:completion:"
+ "v44@0:8Q16@24B32@?36"
- "\x04\""
- "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:reason : %{public}lu, requestId %@"
- "%s start audio capture with recordContext : %{public}@, hostTime : %llu"
- "-[LBAudioCapture stopAudioCaptureWithReason:completion:]"
- "-[LBAudioCapture stopAudioCaptureWithReason:completion:]_block_invoke"
- "-[LBLocalSpeechRecognizerClient stopSpeechRecognitionTaskWithReason:requestId:completion:]_block_invoke"
- "_stopStreamOptionWithReason:"
- "initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:"
- "stopAudioCaptureWithReason:completion:"
- "v32@0:8Q16@?24"

```
