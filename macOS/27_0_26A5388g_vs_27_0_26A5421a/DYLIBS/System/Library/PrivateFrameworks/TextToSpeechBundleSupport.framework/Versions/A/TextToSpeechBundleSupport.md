## TextToSpeechBundleSupport

> `/System/Library/PrivateFrameworks/TextToSpeechBundleSupport.framework/Versions/A/TextToSpeechBundleSupport`

```diff

-720.0.0.0.0
-  __TEXT.__text: 0x1cba0
-  __TEXT.__objc_methlist: 0x4d8
-  __TEXT.__const: 0xc38
-  __TEXT.__cstring: 0x49b
-  __TEXT.__oslogstring: 0xbb6
-  __TEXT.__swift5_typeref: 0x308
+723.1.0.0.0
+  __TEXT.__text: 0x1cbbc
+  __TEXT.__objc_methlist: 0x2cc
+  __TEXT.__const: 0xb80
+  __TEXT.__cstring: 0x48f
+  __TEXT.__oslogstring: 0xa6e
+  __TEXT.__swift5_typeref: 0x320
   __TEXT.__swift5_capture: 0xd0
-  __TEXT.__swift5_reflstr: 0x255
+  __TEXT.__swift5_reflstr: 0x265
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__constg_swiftt: 0x3d4
-  __TEXT.__swift5_fieldmd: 0x1f0
+  __TEXT.__constg_swiftt: 0x3fc
+  __TEXT.__swift5_fieldmd: 0x1fc
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift_as_entry: 0x54
-  __TEXT.__swift_as_ret: 0x54
-  __TEXT.__swift_as_cont: 0xb8
-  __TEXT.__gcc_except_tab: 0x9cc
-  __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x6f0
-  __TEXT.__eh_frame: 0xc48
+  __TEXT.__swift_as_ret: 0x58
+  __TEXT.__swift_as_cont: 0xd4
+  __TEXT.__gcc_except_tab: 0x67c
+  __TEXT.__unwind_info: 0x688
+  __TEXT.__eh_frame: 0xe28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x138
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__const: 0xc0
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x448
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0x2a0
-  __AUTH_CONST.__const: 0x738
+  __DATA_CONST.__objc_selrefs: 0x280
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__got: 0x270
+  __AUTH_CONST.__const: 0x5f8
   __AUTH_CONST.__cfstring: 0x200
-  __AUTH_CONST.__objc_const: 0xcc0
+  __AUTH_CONST.__objc_const: 0x8c0
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0x950
-  __AUTH.__objc_data: 0x190
+  __AUTH_CONST.__auth_got: 0x900
+  __AUTH.__objc_data: 0x140
   __AUTH.__data: 0xb0
-  __DATA.__objc_ivar: 0x80
-  __DATA.__data: 0x128
+  __DATA.__objc_ivar: 0x44
+  __DATA.__data: 0x148
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x780
-  __DATA_DIRTY.__objc_data: 0x188
-  __DATA_DIRTY.__data: 0x238
+  __DATA.__bss: 0x790
+  __DATA_DIRTY.__objc_data: 0x138
+  __DATA_DIRTY.__data: 0x248
   __DATA_DIRTY.__common: 0x38
   __DATA_DIRTY.__bss: 0x1c0
-  - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 457
-  Symbols:   728
-  CStrings:  104
+  Functions: 409
+  Symbols:   548
+  CStrings:  93
 
Symbols:
+ -[TTSSynthesizerWrapper .cxx_construct]
+ -[TTSSynthesizerWrapper loadVoiceResourceData:mimeType:error:]
+ -[TTSSynthesizerWrapper unloadAllVoiceResourcesWithError:]
+ GCC_except_table11
+ GCC_except_table13
+ GCC_except_table45
+ GCC_except_table46
+ GCC_except_table53
+ GCC_except_table56
+ GCC_except_table68
+ GCC_except_table7
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table78
+ GCC_except_table79
+ OBJC_IVAR_$_TTSSynthesizerWrapper._loadedResources
+ __ZNSt3__110shared_ptrIN7SiriTTS13VoiceResourceEED2B9nqe220106Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN7SiriTTS13VoiceResourceEEENS_9allocatorIS4_EEE20__throw_length_errorB9nqe220106Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN7SiriTTS13VoiceResourceEEENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJRKS4_EEEPS4_DpOT_
+ _objc_msgSend$initWithContentsOfURL:
+ _objc_msgSend$loadVoiceResourceData:mimeType:error:
+ _objc_msgSend$unloadAllVoiceResourcesWithError:
+ _symbolic SDyS2SG
+ _symbolic SaySSG
+ _symbolic _____Sg 12TextToSpeech15CoreSynthesizerC5VoiceV0F4TypeO
- -[TTSSiriSynthWrapper .cxx_destruct]
- -[TTSSiriSynthWrapper _neuralStyles]
- -[TTSSiriSynthWrapper _rawLiteralCharacterRegexForCurrentLanguage]
- -[TTSSiriSynthWrapper _setProsodyParameters]
- -[TTSSiriSynthWrapper bufferConverter]
- -[TTSSiriSynthWrapper currentNeuralStyle]
- -[TTSSiriSynthWrapper dealloc]
- -[TTSSiriSynthWrapper delegate]
- -[TTSSiriSynthWrapper engineFormat]
- -[TTSSiriSynthWrapper initWithVoicePath:language:dynamicStylePrompt:censorPlainText:delegate:feResourcePath:]
- -[TTSSiriSynthWrapper language]
- -[TTSSiriSynthWrapper loadVoiceResource:]
- -[TTSSiriSynthWrapper neuralStyles]
- -[TTSSiriSynthWrapper outputFormat]
- -[TTSSiriSynthWrapper setBufferConverter:]
- -[TTSSiriSynthWrapper setCurrentNeuralStyle:]
- -[TTSSiriSynthWrapper setDelegate:]
- -[TTSSiriSynthWrapper setEngineFormat:]
- -[TTSSiriSynthWrapper setLanguage:]
- -[TTSSiriSynthWrapper setNeuralStyles:]
- -[TTSSiriSynthWrapper setOutputFormat:]
- -[TTSSiriSynthWrapper setSynthesisQueue:]
- -[TTSSiriSynthWrapper setSynthesizer:]
- -[TTSSiriSynthWrapper setSynthesizing:]
- -[TTSSiriSynthWrapper setVoiceResources:]
- -[TTSSiriSynthWrapper stopSynthesis]
- -[TTSSiriSynthWrapper synthesisQueue]
- -[TTSSiriSynthWrapper synthesizeString:]
- -[TTSSiriSynthWrapper synthesizer]
- -[TTSSiriSynthWrapper synthesizing]
- -[TTSSiriSynthWrapper unloadAllVoiceResources]
- -[TTSSiriSynthWrapper unloadVoiceResource:]
- -[TTSSiriSynthWrapper voiceResources]
- -[TTSSiriVoiceResource .cxx_construct]
- -[TTSSiriVoiceResource .cxx_destruct]
- -[TTSSiriVoiceResource resourceData]
- -[TTSSiriVoiceResource resourceName]
- -[TTSSiriVoiceResource resourceString]
- -[TTSSiriVoiceResource setResourceData:]
- -[TTSSiriVoiceResource setResourceName:]
- -[TTSSiriVoiceResource setResourceString:]
- -[TTSSiriVoiceResource setSiriVoiceResource:]
- -[TTSSiriVoiceResource setType:]
- -[TTSSiriVoiceResource siriVoiceResource]
- -[TTSSiriVoiceResource type]
- GCC_except_table110
- GCC_except_table111
- GCC_except_table113
- GCC_except_table119
- GCC_except_table120
- GCC_except_table125
- GCC_except_table138
- GCC_except_table140
- GCC_except_table141
- GCC_except_table142
- GCC_except_table143
- GCC_except_table144
- GCC_except_table31
- GCC_except_table33
- GCC_except_table36
- GCC_except_table41
- GCC_except_table48
- GCC_except_table50
- GCC_except_table54
- GCC_except_table55
- GCC_except_table60
- GCC_except_table74
- OBJC_IVAR_$_TTSSiriSynthWrapper._bufferConverter
- OBJC_IVAR_$_TTSSiriSynthWrapper._currentNeuralStyle
- OBJC_IVAR_$_TTSSiriSynthWrapper._delegate
- OBJC_IVAR_$_TTSSiriSynthWrapper._engineFormat
- OBJC_IVAR_$_TTSSiriSynthWrapper._language
- OBJC_IVAR_$_TTSSiriSynthWrapper._neuralStyles
- OBJC_IVAR_$_TTSSiriSynthWrapper._outputFormat
- OBJC_IVAR_$_TTSSiriSynthWrapper._synthesisQueue
- OBJC_IVAR_$_TTSSiriSynthWrapper._synthesizer
- OBJC_IVAR_$_TTSSiriSynthWrapper._synthesizing
- OBJC_IVAR_$_TTSSiriSynthWrapper._voiceResources
- OBJC_IVAR_$_TTSSiriVoiceResource._resourceData
- OBJC_IVAR_$_TTSSiriVoiceResource._resourceName
- OBJC_IVAR_$_TTSSiriVoiceResource._resourceString
- OBJC_IVAR_$_TTSSiriVoiceResource._siriVoiceResource
- OBJC_IVAR_$_TTSSiriVoiceResource._type
- _OBJC_CLASS_$_AVAudioConverter
- _OBJC_CLASS_$_AVAudioFormat
- _OBJC_CLASS_$_AVAudioPCMBuffer
- _OBJC_CLASS_$_NSMutableOrderedSet
- _OBJC_CLASS_$_TTSRegexCache
- _OBJC_CLASS_$_TTSSiriSynthWrapper
- _OBJC_CLASS_$_TTSSiriVoiceResource
- _OBJC_CLASS_$_TTSUnicodeUtils
- _OBJC_METACLASS_$_TTSSiriSynthWrapper
- _OBJC_METACLASS_$_TTSSiriVoiceResource
- __DefaultRuneLocale
- __NSConcreteGlobalBlock
- __OBJC_$_INSTANCE_METHODS_TTSSiriSynthWrapper
- __OBJC_$_INSTANCE_METHODS_TTSSiriVoiceResource
- __OBJC_$_INSTANCE_VARIABLES_TTSSiriSynthWrapper
- __OBJC_$_INSTANCE_VARIABLES_TTSSiriVoiceResource
- __OBJC_$_PROP_LIST_TTSSiriSynthWrapper
- __OBJC_$_PROP_LIST_TTSSiriVoiceResource
- __OBJC_CLASS_RO_$_TTSSiriSynthWrapper
- __OBJC_CLASS_RO_$_TTSSiriVoiceResource
- __OBJC_METACLASS_RO_$_TTSSiriSynthWrapper
- __OBJC_METACLASS_RO_$_TTSSiriVoiceResource
- __ZNKSt11logic_error4whatEv
- __ZNKSt3__110__function6__funcIZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_E3$_0FiN14TTSSynthesizer15CallbackMessageEEE11target_typeEv
- __ZNKSt3__110__function6__funcIZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_E3$_0FiN14TTSSynthesizer15CallbackMessageEEE6targetERKSt9type_info
- __ZNKSt3__110__function6__funcIZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_E3$_0FiN14TTSSynthesizer15CallbackMessageEEE7__cloneEPNS0_6__baseIS5_EE
- __ZNKSt3__110__function6__funcIZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_E3$_0FiN14TTSSynthesizer15CallbackMessageEEE7__cloneEv
- __ZNSt11logic_errorC1ERKS_
- __ZNSt11logic_errorD1Ev
- __ZNSt3__110__function6__funcIZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_E3$_0FiN14TTSSynthesizer15CallbackMessageEEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_E3$_0FiN14TTSSynthesizer15CallbackMessageEEE7destroyEv
- __ZNSt3__110__function6__funcIZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_E3$_0FiN14TTSSynthesizer15CallbackMessageEEED0Ev
- __ZNSt3__110__function6__funcIZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_E3$_0FiN14TTSSynthesizer15CallbackMessageEEED1Ev
- __ZNSt3__110__function6__funcIZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_E3$_0FiN14TTSSynthesizer15CallbackMessageEEEclEOS4_
- __ZNSt3__110shared_ptrIN7SiriTTS13VoiceResourceEED1B9nqe220106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_externalEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_externalEPKcm
- __ZNSt3__16vectorI13SiriTTSMarkerNS_9allocatorIS1_EEE20__throw_length_errorB9nqe220106Ev
- __ZNSt3__16vectorI13SiriTTSMarkerNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEED2B9nqe220106Ev
- __ZSt9terminatev
- __ZTINSt3__110__function6__funcIZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_E3$_0FiN14TTSSynthesizer15CallbackMessageEEEE
- __ZTISt11logic_error
- __ZTIZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_E3$_0
- __ZTSNSt3__110__function6__funcIZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_E3$_0FiN14TTSSynthesizer15CallbackMessageEEEE
- __ZTSZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_E3$_0
- __ZTVNSt3__110__function6__funcIZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_E3$_0FiN14TTSSynthesizer15CallbackMessageEEEE
- ___36-[TTSSiriSynthWrapper _neuralStyles]_block_invoke
- ___36-[TTSSiriSynthWrapper stopSynthesis]_block_invoke
- ___40-[TTSSiriSynthWrapper synthesizeString:]_block_invoke
- ____ZZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_ENK3$_0clEN14TTSSynthesizer15CallbackMessageE_block_invoke
- ____ZZZ40-[TTSSiriSynthWrapper synthesizeString:]EUb_ENK3$_0clEN14TTSSynthesizer15CallbackMessageE_block_invoke_2
- ___block_descriptor_32_e31_B32?0"TTSNeuralStyle"8Q16^B24l
- ___block_descriptor_32_e49_v16?0r^{AudioBufferList=I[1{AudioBuffer=II^v}]}8l
- ___block_descriptor_32_e5_v8?0l
- ___block_descriptor_48_ea8_32s40r_e27_"AVAudioBuffer"20?0I8^q12l
- ___block_descriptor_48_ea8_32s40s_e5_v8?0l
- ___block_literal_global
- ___clang_call_terminate
- ___copy_helper_block_ea8_32s40r
- ___copy_helper_block_ea8_32s40s
- ___cxa_begin_catch
- ___cxa_end_catch
- ___cxa_get_exception_ptr
- ___destroy_helper_block_ea8_32s40r
- ___destroy_helper_block_ea8_32s40s
- ___gxx_personality_v0
- ___toupper
- __block_literal_global
- __os_log_error_impl
- _dispatch_sync
- _objc_alloc
- _objc_destroyWeak
- _objc_loadWeakRetained
- _objc_msgSend$UTF8String
- _objc_msgSend$_neuralStyles
- _objc_msgSend$_setProsodyParameters
- _objc_msgSend$bufferConverter
- _objc_msgSend$cStringUsingEncoding:
- _objc_msgSend$convertToBuffer:error:withInputFromBlock:
- _objc_msgSend$currentNeuralStyle
- _objc_msgSend$delegate
- _objc_msgSend$engineFormat
- _objc_msgSend$hasPrefix:
- _objc_msgSend$indexOfObjectPassingTest:
- _objc_msgSend$initFromFormat:toFormat:
- _objc_msgSend$initStandardFormatWithSampleRate:channels:
- _objc_msgSend$initWithCommonFormat:sampleRate:channels:interleaved:
- _objc_msgSend$initWithName:vector:
- _objc_msgSend$initWithPCMFormat:bufferListNoCopy:deallocator:
- _objc_msgSend$initWithPCMFormat:frameCapacity:
- _objc_msgSend$insertObject:atIndex:
- _objc_msgSend$isEqualToString:
- _objc_msgSend$language
- _objc_msgSend$lengthOfBytesUsingEncoding:
- _objc_msgSend$numberWithBool:
- _objc_msgSend$objectAtIndexedSubscript:
- _objc_msgSend$orderedSet
- _objc_msgSend$outputFormat
- _objc_msgSend$regexForString:atStart:
- _objc_msgSend$removeObject:
- _objc_msgSend$removeObjectAtIndex:
- _objc_msgSend$reset
- _objc_msgSend$resourceData
- _objc_msgSend$resourceString
- _objc_msgSend$setCurrentNeuralStyle:
- _objc_msgSend$setNeuralStyles:
- _objc_msgSend$setPrimeMethod:
- _objc_msgSend$setSiriVoiceResource:
- _objc_msgSend$setSynthesizer:
- _objc_msgSend$setSynthesizing:
- _objc_msgSend$siri:didGenerateBuffer:
- _objc_msgSend$siri:didGenerateMarkers:count:
- _objc_msgSend$siriDidEndSynthesis:successfully:
- _objc_msgSend$siriDidStartSynthesis:
- _objc_msgSend$siriVoiceResource
- _objc_msgSend$synthesisQueue
- _objc_msgSend$synthesizer
- _objc_msgSend$unloadVoiceResource:
- _objc_msgSend$utf16RangeFromUTF8Range:chars:size:
- _objc_msgSend$voiceResources
- _objc_storeWeak
CStrings:
+ "Exception loading voice resource"
+ "Exception unloading voice resources"
+ "Failed to load voice resource"
+ "Failed to unload voice resources"
+ "Q"
+ "ax_gryphon_resource_order"
+ "loadResourceAsset: failed to load resource %s: %@"
+ "loadResourceAsset: failed to read resource file %s"
+ "voice_configs.plist"
- ""
- "!"
- "@\"AVAudioBuffer\"20@?0I8^q12"
- "B32@?0@\"TTSNeuralStyle\"8Q16^B24"
- "Failed to set dynamic prompt on TTSSynthesizer. prompt=%@"
- "Siri resource load exception."
- "Siri returned invalid word marker [%@,%@], skipping."
- "Siri returned style %s for which we have no localization."
- "Siri threw an exception instead of reporting an error via callback: %s"
- "SiriTTSSynthesizer initialization error: %@"
- "SiriTTSSynthesizer initialization exception"
- "Will set dynamic prompt on TTSSynthesizer. prompt=%@"
- "[æøå]"
- "application/edct-text-dictionary"
- "application/x-vocalizer-rettt+text"
- "com.siri.synthesis"
- "da"
- "init TTSSiriSynthWrapper. censorPlainText=%@"
- "siri"
- "v16@?0r^{AudioBufferList=I[1{AudioBuffer=II^v}]}8"
```
