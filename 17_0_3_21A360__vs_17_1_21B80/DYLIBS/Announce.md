## Announce

> `/System/Library/PrivateFrameworks/Announce.framework/Announce`

```diff

-217.0.0.0.0
-  __TEXT.__text: 0x1dc5c
-  __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_methlist: 0x1d00
-  __TEXT.__const: 0x24a
-  __TEXT.__cstring: 0x3c39
-  __TEXT.__oslogstring: 0xc21
+217.10.3.0.0
+  __TEXT.__text: 0x1c620
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x1c50
+  __TEXT.__const: 0x222
+  __TEXT.__cstring: 0x3be9
+  __TEXT.__oslogstring: 0xa48
   __TEXT.__gcc_except_tab: 0x21c
   __TEXT.__swift5_typeref: 0x1c3
   __TEXT.__swift5_capture: 0x50

   __TEXT.__swift5_reflstr: 0x112
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x8bc
+  __TEXT.__unwind_info: 0x880
   __TEXT.__eh_frame: 0x110
-  __TEXT.__objc_classname: 0x56b
-  __TEXT.__objc_methname: 0x4b36
-  __TEXT.__objc_methtype: 0x1214
-  __TEXT.__objc_stubs: 0x37e0
+  __TEXT.__objc_classname: 0x54f
+  __TEXT.__objc_methname: 0x44dc
+  __TEXT.__objc_methtype: 0xe24
+  __TEXT.__objc_stubs: 0x3400
   __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0xb38
+  __DATA_CONST.__const: 0xad0
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0xc8
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x37f8
-  __DATA_CONST.__objc_selrefs: 0x12b8
-  __AUTH_CONST.__cfstring: 0x2d80
+  __DATA_CONST.__objc_const: 0x34f0
+  __DATA_CONST.__objc_selrefs: 0x1180
+  __AUTH_CONST.__cfstring: 0x2d00
   __AUTH_CONST.__objc_const: 0x11c8
-  __AUTH_CONST.__const: 0x548
+  __AUTH_CONST.__const: 0x508
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x110
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x590
+  __AUTH_CONST.__auth_got: 0x570
   __AUTH.__objc_data: 0x7d0
   __DATA.__objc_protorefs: 0x68
-  __DATA.__objc_classrefs: 0x220
+  __DATA.__objc_classrefs: 0x200
   __DATA.__objc_superrefs: 0xa8
-  __DATA.__objc_ivar: 0x1e8
+  __DATA.__objc_ivar: 0x1d8
   __DATA.__objc_data: 0x78
-  __DATA.__data: 0x8d0
-  __DATA.__bss: 0x350
+  __DATA.__data: 0x870
+  __DATA.__bss: 0x330
   __DATA_DIRTY.__objc_data: 0x530
   __DATA_DIRTY.__data: 0x80
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 817
-  Symbols:   2997
-  CStrings:  1651
+  Functions: 796
+  Symbols:   2893
+  CStrings:  1559
 
Symbols:
- +[ANSpeechUtil _pcmAudioDataFromOpusAudio:]
- -[ANSpeechUtil .cxx_destruct]
- -[ANSpeechUtil _fileNameGeneratorWithFileExtension:]
- -[ANSpeechUtil _handleCompletedSpeechRequest:error:]
- -[ANSpeechUtil audioSession]
- -[ANSpeechUtil queue]
- -[ANSpeechUtil requests]
- -[ANSpeechUtil setAudioSession:]
- -[ANSpeechUtil setRequests:]
- -[ANSpeechUtil setSynthesizer:]
- -[ANSpeechUtil speechSynthesizer:didFinishSpeakingRequest:withInstrumentMetrics:]
- -[ANSpeechUtil speechSynthesizer:didFinishSynthesisRequest:withInstrumentMetrics:error:]
- -[ANSpeechUtil speechSynthesizer:didStartSpeakingRequest:]
- -[ANSpeechUtil speechSynthesizer:withSynthesisRequest:didGenerateAudioChunk:]
- -[ANSpeechUtil synthesizer]
- _ANLogHandleSpeechUtil
- _ANLogHandleSpeechUtil.logger
- _ANLogHandleSpeechUtil.once
- _AudioFileClose
- _AudioFileCreateWithURL
- _AudioFileWriteBytes
- _OBJC_CLASS_$_VSAudioData
- _OBJC_CLASS_$_VSOpusDecoder
- _OBJC_CLASS_$_VSSpeechRequest
- _OBJC_CLASS_$_VSSpeechSynthesizer
- _OBJC_IVAR_$_ANSpeechUtil._audioSession
- _OBJC_IVAR_$_ANSpeechUtil._queue
- _OBJC_IVAR_$_ANSpeechUtil._requests
- _OBJC_IVAR_$_ANSpeechUtil._synthesizer
- __OBJC_$_INSTANCE_VARIABLES_ANSpeechUtil
- __OBJC_$_PROP_LIST_ANSpeechUtil
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_VSSpeechSynthesizerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_VSSpeechSynthesizerDelegate
- __OBJC_$_PROTOCOL_REFS_VSSpeechSynthesizerDelegate
- __OBJC_CLASS_PROTOCOLS_$_ANSpeechUtil
- __OBJC_LABEL_PROTOCOL_$_VSSpeechSynthesizerDelegate
- __OBJC_PROTOCOL_$_VSSpeechSynthesizerDelegate
- ___52-[ANSpeechUtil _fileNameGeneratorWithFileExtension:]_block_invoke
- ___65-[ANSpeechUtil synthesizeSpeechToFileFromText:completionHandler:]_block_invoke
- ___77-[ANSpeechUtil speechSynthesizer:withSynthesisRequest:didGenerateAudioChunk:]_block_invoke
- ___88-[ANSpeechUtil speechSynthesizer:didFinishSynthesisRequest:withInstrumentMetrics:error:]_block_invoke
- ___ANLogHandleSpeechUtil_block_invoke
- ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_literal_global.159
- __fileNameGeneratorWithFileExtension:.dateFormatter
- __fileNameGeneratorWithFileExtension:.onceToken
- _kANSUAudioData
- _kANSUHandler
- _kANSUUUIDString
- _objc_msgSend$_fileNameGeneratorWithFileExtension:
- _objc_msgSend$_handleCompletedSpeechRequest:error:
- _objc_msgSend$asbd
- _objc_msgSend$audioData
- _objc_msgSend$audioSession
- _objc_msgSend$auxiliarySession
- _objc_msgSend$bytes
- _objc_msgSend$concatenateWithAudio:
- _objc_msgSend$contextInfo
- _objc_msgSend$dataWithBytes:length:
- _objc_msgSend$decodeChunks:streamDescription:outError:
- _objc_msgSend$dictionaryWithObject:forKey:
- _objc_msgSend$getBytes:range:
- _objc_msgSend$numberWithUnsignedInt:
- _objc_msgSend$opaqueSessionID
- _objc_msgSend$outputPath
- _objc_msgSend$packetCount
- _objc_msgSend$packetDescriptions
- _objc_msgSend$requests
- _objc_msgSend$setAsbd:
- _objc_msgSend$setAudioData:
- _objc_msgSend$setAudioSessionID:
- _objc_msgSend$setCategory:error:
- _objc_msgSend$setContextInfo:
- _objc_msgSend$setLanguageCode:
- _objc_msgSend$setShouldCache:
- _objc_msgSend$setText:
- _objc_msgSend$setVolume:
- _objc_msgSend$startSpeakingRequest:
- _objc_msgSend$startSynthesizingRequest:
- _objc_msgSend$synthesizer
- _objc_retainBlock
CStrings:
- "%@/out-%@.%@"
- "%@Did Finish Speaking Request %@"
- "%@Did Start Speaking Request %@"
- "%@Error AudioFileClose: '%@', code: %@"
- "%@Error AudioFileCreateWithURL: '%@', code: %@"
- "%@Error AudioFileWriteBytes: '%@', code: %@"
- "%@Failed to set aux audio session for TTS. %@"
- "%@Failed to start speaking request: %@"
- "%@Speech Synthesizer Did Finish Synthesis Request: %@, Error = %@"
- "%@Speech Synthesizer Did Generate Audio Chunk For Request: %@, Audio = %@"
- "%@Unsupported audio format %u"
- "%@Wrote %@ bytes to %@"
- "@\"AVAudioSession\""
- "@\"VSSpeechSynthesizer\""
- "AudioData"
- "Handler"
- "SpeechUtil"
- "T@\"AVAudioSession\",&,N,V_audioSession"
- "T@\"NSMutableDictionary\",&,N,V_requests"
- "T@\"VSSpeechSynthesizer\",&,N,V_synthesizer"
- "VSSpeechSynthesizerDelegate"
- "_audioSession"
- "_fileNameGeneratorWithFileExtension:"
- "_handleCompletedSpeechRequest:error:"
- "_pcmAudioDataFromOpusAudio:"
- "_requests"
- "_synthesizer"
- "asbd"
- "audioData"
- "audioSession"
- "auxiliarySession"
- "bytes"
- "com.apple.announce.speechUtil"
- "concatenateWithAudio:"
- "contextInfo"
- "dataWithBytes:length:"
- "decodeChunks:streamDescription:outError:"
- "dictionaryWithObject:forKey:"
- "getBytes:range:"
- "numberWithUnsignedInt:"
- "opaqueSessionID"
- "outputPath"
- "packetCount"
- "packetDescriptions"
- "requests"
- "setAsbd:"
- "setAudioData:"
- "setAudioSession:"
- "setAudioSessionID:"
- "setCategory:error:"
- "setContextInfo:"
- "setLanguageCode:"
- "setRequests:"
- "setShouldCache:"
- "setSynthesizer:"
- "setText:"
- "setVolume:"
- "speechSynthesizer:didContinueSpeakingRequest:"
- "speechSynthesizer:didFinishPresynthesizedAudioRequest:withInstrumentMetrics:error:"
- "speechSynthesizer:didFinishPrewarmRequest:withError:"
- "speechSynthesizer:didFinishSpeakingRequest:successfully:phonemesSpoken:withError:"
- "speechSynthesizer:didFinishSpeakingRequest:withInstrumentMetrics:"
- "speechSynthesizer:didFinishSynthesisRequest:withInstrumentMetrics:error:"
- "speechSynthesizer:didPauseSpeakingRequest:"
- "speechSynthesizer:didStartPlayingPreviewRequest:"
- "speechSynthesizer:didStartPresynthesizedAudioRequest:"
- "speechSynthesizer:didStartSpeakingRequest:"
- "speechSynthesizer:didStopPresynthesizedAudioRequest:atEnd:error:"
- "speechSynthesizer:willSpeakRangeOfSpeechString:forRequest:"
- "speechSynthesizer:withRequest:didReceiveTimingInfo:"
- "speechSynthesizer:withSynthesisRequest:didGenerateAudioChunk:"
- "startSpeakingRequest:"
- "startSynthesizingRequest:"
- "synthesizer"
- "v32@0:8@\"VSSpeechSynthesizer\"16@\"VSPresynthesizedAudioRequest\"24"
- "v32@0:8@\"VSSpeechSynthesizer\"16@\"VSPreviewRequest\"24"
- "v32@0:8@\"VSSpeechSynthesizer\"16@\"VSSpeechRequest\"24"
- "v40@0:8@\"VSSpeechSynthesizer\"16@\"VSSpeechRequest\"24@\"NSArray\"32"
- "v40@0:8@\"VSSpeechSynthesizer\"16@\"VSSpeechRequest\"24@\"NSError\"32"
- "v40@0:8@\"VSSpeechSynthesizer\"16@\"VSSpeechRequest\"24@\"VSAudioData\"32"
- "v40@0:8@\"VSSpeechSynthesizer\"16@\"VSSpeechRequest\"24@\"VSInstrumentMetrics\"32"
- "v40@0:8@16@24@32"
- "v44@0:8@\"VSSpeechSynthesizer\"16@\"VSPresynthesizedAudioRequest\"24B32@\"NSError\"36"
- "v44@0:8@16@24B32@36"
- "v48@0:8@\"VSSpeechSynthesizer\"16@\"VSPresynthesizedAudioRequest\"24@\"VSInstrumentMetrics\"32@\"NSError\"40"
- "v48@0:8@\"VSSpeechSynthesizer\"16@\"VSSpeechRequest\"24@\"VSInstrumentMetrics\"32@\"NSError\"40"
- "v48@0:8@\"VSSpeechSynthesizer\"16{_NSRange=QQ}24@\"VSSpeechRequest\"40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16{_NSRange=QQ}24@40"
- "v52@0:8@\"VSSpeechSynthesizer\"16@\"VSSpeechRequest\"24B32@\"NSString\"36@\"NSError\"44"
- "v52@0:8@16@24B32@36@44"

```
