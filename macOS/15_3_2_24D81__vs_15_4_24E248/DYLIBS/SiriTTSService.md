## SiriTTSService

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/Versions/A/SiriTTSService`

```diff

-3403.2.1.0.0
-  __TEXT.__text: 0x13db34
-  __TEXT.__auth_stubs: 0x2c20
-  __TEXT.__objc_methlist: 0x5ae0
-  __TEXT.__const: 0x5093
-  __TEXT.__cstring: 0xff8f
-  __TEXT.__swift5_typeref: 0x23f0
-  __TEXT.__oslogstring: 0x4223
-  __TEXT.__swift5_capture: 0x1418
-  __TEXT.__swift5_reflstr: 0x29cf
-  __TEXT.__swift5_assocty: 0x278
-  __TEXT.__constg_swiftt: 0x51a0
-  __TEXT.__swift5_fieldmd: 0x28e0
-  __TEXT.__swift5_builtin: 0x1f4
-  __TEXT.__swift5_protos: 0x44
-  __TEXT.__swift5_proto: 0x2e4
-  __TEXT.__swift5_types: 0x2d0
-  __TEXT.__gcc_except_tab: 0x399c
+3404.73.1.0.0
+  __TEXT.__text: 0x152f30
+  __TEXT.__auth_stubs: 0x2c10
+  __TEXT.__objc_methlist: 0x61e8
+  __TEXT.__const: 0x53c3
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x6158
-  __TEXT.__eh_frame: 0x36ec
+  __TEXT.__cstring: 0x10192
+  __TEXT.__swift5_typeref: 0x2466
+  __TEXT.__oslogstring: 0x4563
+  __TEXT.__swift5_capture: 0x16f0
+  __TEXT.__swift5_reflstr: 0x2a4f
+  __TEXT.__swift5_assocty: 0x290
+  __TEXT.__constg_swiftt: 0x5498
+  __TEXT.__swift5_fieldmd: 0x29d0
+  __TEXT.__swift5_builtin: 0x208
+  __TEXT.__swift5_protos: 0x44
+  __TEXT.__swift5_proto: 0x2f8
+  __TEXT.__swift5_types: 0x2ec
+  __TEXT.__gcc_except_tab: 0x3a84
+  __TEXT.__unwind_info: 0x65b0
+  __TEXT.__eh_frame: 0x3944
   __TEXT.__objc_classname: 0xc6c
-  __TEXT.__objc_methname: 0x6640
-  __TEXT.__objc_methtype: 0x22f5
-  __TEXT.__objc_stubs: 0x23e0
-  __DATA_CONST.__got: 0x960
-  __DATA_CONST.__const: 0x1000
-  __DATA_CONST.__objc_classlist: 0x680
+  __TEXT.__objc_methname: 0x6a56
+  __TEXT.__objc_methtype: 0x2300
+  __TEXT.__objc_stubs: 0x2480
+  __DATA_CONST.__got: 0x9a8
+  __DATA_CONST.__const: 0x10c8
+  __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f00
-  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_selrefs: 0x20e0
+  __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x248
-  __AUTH_CONST.__auth_got: 0x1628
-  __AUTH_CONST.__const: 0xc798
-  __AUTH_CONST.__cfstring: 0x1120
-  __AUTH_CONST.__objc_const: 0xfe70
-  __AUTH.__objc_data: 0x5fb8
-  __AUTH.__data: 0x58f0
-  __DATA.__objc_ivar: 0x2fc
-  __DATA.__data: 0x24a8
-  __DATA.__bss: 0x34c0
-  __DATA.__common: 0x410
+  __AUTH_CONST.__auth_got: 0x1620
+  __AUTH_CONST.__const: 0xd6a8
+  __AUTH_CONST.__cfstring: 0x1200
+  __AUTH_CONST.__objc_const: 0xfe90
+  __AUTH.__objc_data: 0x6008
+  __AUTH.__data: 0x5b18
+  __DATA.__objc_ivar: 0x308
+  __DATA.__data: 0x2558
+  __DATA.__bss: 0x36c0
+  __DATA.__common: 0x468
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial
   - /System/Library/PrivateFrameworks/TrialProto.framework/Versions/A/TrialProto
+  - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/Versions/A/UnifiedAssetFramework
   - /usr/lib/libAudioStatistics.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 8ABE853B-06BB-3430-A306-1F49C8DC3AAB
-  Functions: 9481
-  Symbols:   6961
-  CStrings:  4035
+  UUID: F802B11E-E7A1-3847-8B72-7CE592ADC7B0
+  Functions: 9923
+  Symbols:   7342
+  CStrings:  4113
 
Symbols:
+ +[SiriTTSSynthesisEngine hasWordTimingSupportWithVoicePath:]
+ +[SiriTTSSynthesisEngineRequest synthesisIssueCauseString:]
+ +[TTSAsset _hasUAFEntitlements]
+ -[SiriTTSSynthesisEngine setSupportPhaticResponseCachedValue:]
+ -[SiriTTSSynthesisEngine setSupportWordTimingCachedValue:]
+ -[SiriTTSSynthesisEngine supportPhaticResponseCachedValue]
+ -[SiriTTSSynthesisEngine supportPhaticResponse]
+ -[SiriTTSSynthesisEngine supportWordTimingCachedValue]
+ -[SiriTTSSynthesisEngine supportWordTiming]
+ -[SiriTTSSynthesisEngineRequest setWordAlignmentFailureHandler:]
+ -[SiriTTSSynthesisEngineRequest wordAlignmentFailureHandler]
+ GCC_except_table1009
+ GCC_except_table1024
+ GCC_except_table103
+ GCC_except_table1030
+ GCC_except_table1032
+ GCC_except_table1035
+ GCC_except_table1036
+ GCC_except_table1037
+ GCC_except_table1041
+ GCC_except_table1042
+ GCC_except_table1043
+ GCC_except_table1045
+ GCC_except_table1047
+ GCC_except_table1049
+ GCC_except_table1053
+ GCC_except_table1058
+ GCC_except_table1060
+ GCC_except_table1072
+ GCC_except_table1079
+ GCC_except_table1081
+ GCC_except_table1084
+ GCC_except_table1085
+ GCC_except_table1094
+ GCC_except_table1100
+ GCC_except_table1102
+ GCC_except_table1106
+ GCC_except_table1107
+ GCC_except_table1109
+ GCC_except_table1112
+ GCC_except_table112
+ GCC_except_table1121
+ GCC_except_table1128
+ GCC_except_table1130
+ GCC_except_table1138
+ GCC_except_table1146
+ GCC_except_table1149
+ GCC_except_table1156
+ GCC_except_table1159
+ GCC_except_table1161
+ GCC_except_table1163
+ GCC_except_table1164
+ GCC_except_table1165
+ GCC_except_table1168
+ GCC_except_table1172
+ GCC_except_table121
+ GCC_except_table1239
+ GCC_except_table1276
+ GCC_except_table1284
+ GCC_except_table1443
+ GCC_except_table1445
+ GCC_except_table1446
+ GCC_except_table1450
+ GCC_except_table1451
+ GCC_except_table1452
+ GCC_except_table163
+ GCC_except_table165
+ GCC_except_table167
+ GCC_except_table169
+ GCC_except_table177
+ GCC_except_table179
+ GCC_except_table195
+ GCC_except_table201
+ GCC_except_table223
+ GCC_except_table227
+ GCC_except_table231
+ GCC_except_table236
+ GCC_except_table238
+ GCC_except_table242
+ GCC_except_table244
+ GCC_except_table248
+ GCC_except_table252
+ GCC_except_table254
+ GCC_except_table260
+ GCC_except_table271
+ GCC_except_table277
+ GCC_except_table283
+ GCC_except_table285
+ GCC_except_table292
+ GCC_except_table314
+ GCC_except_table316
+ GCC_except_table320
+ GCC_except_table322
+ GCC_except_table324
+ GCC_except_table326
+ GCC_except_table328
+ GCC_except_table330
+ GCC_except_table394
+ GCC_except_table398
+ GCC_except_table400
+ GCC_except_table402
+ GCC_except_table404
+ GCC_except_table406
+ GCC_except_table408
+ GCC_except_table410
+ GCC_except_table412
+ GCC_except_table436
+ GCC_except_table442
+ GCC_except_table458
+ GCC_except_table464
+ GCC_except_table473
+ GCC_except_table477
+ GCC_except_table479
+ GCC_except_table483
+ GCC_except_table485
+ GCC_except_table491
+ GCC_except_table504
+ GCC_except_table514
+ GCC_except_table516
+ GCC_except_table518
+ GCC_except_table525
+ GCC_except_table526
+ GCC_except_table528
+ GCC_except_table529
+ GCC_except_table530
+ GCC_except_table532
+ GCC_except_table533
+ GCC_except_table535
+ GCC_except_table537
+ GCC_except_table539
+ GCC_except_table540
+ GCC_except_table541
+ GCC_except_table542
+ GCC_except_table543
+ GCC_except_table544
+ GCC_except_table547
+ GCC_except_table551
+ GCC_except_table558
+ GCC_except_table580
+ GCC_except_table593
+ GCC_except_table602
+ GCC_except_table604
+ GCC_except_table614
+ GCC_except_table616
+ GCC_except_table617
+ GCC_except_table618
+ GCC_except_table620
+ GCC_except_table626
+ GCC_except_table628
+ GCC_except_table633
+ GCC_except_table639
+ GCC_except_table641
+ GCC_except_table652
+ GCC_except_table654
+ GCC_except_table658
+ GCC_except_table663
+ GCC_except_table664
+ GCC_except_table665
+ GCC_except_table670
+ GCC_except_table677
+ GCC_except_table679
+ GCC_except_table682
+ GCC_except_table688
+ GCC_except_table707
+ GCC_except_table709
+ GCC_except_table717
+ GCC_except_table718
+ GCC_except_table721
+ GCC_except_table733
+ GCC_except_table735
+ GCC_except_table736
+ GCC_except_table739
+ GCC_except_table745
+ GCC_except_table747
+ GCC_except_table748
+ GCC_except_table749
+ GCC_except_table751
+ GCC_except_table760
+ GCC_except_table762
+ GCC_except_table772
+ GCC_except_table773
+ GCC_except_table774
+ GCC_except_table775
+ GCC_except_table784
+ GCC_except_table786
+ GCC_except_table790
+ GCC_except_table796
+ GCC_except_table798
+ GCC_except_table80
+ GCC_except_table809
+ GCC_except_table82
+ GCC_except_table825
+ GCC_except_table827
+ GCC_except_table828
+ GCC_except_table830
+ GCC_except_table831
+ GCC_except_table832
+ GCC_except_table833
+ GCC_except_table836
+ GCC_except_table837
+ GCC_except_table838
+ GCC_except_table840
+ GCC_except_table842
+ GCC_except_table843
+ GCC_except_table846
+ GCC_except_table871
+ GCC_except_table875
+ GCC_except_table881
+ GCC_except_table883
+ GCC_except_table887
+ GCC_except_table888
+ GCC_except_table889
+ GCC_except_table898
+ GCC_except_table912
+ GCC_except_table914
+ GCC_except_table920
+ GCC_except_table936
+ GCC_except_table94
+ GCC_except_table942
+ GCC_except_table944
+ GCC_except_table946
+ GCC_except_table967
+ GCC_except_table968
+ GCC_except_table969
+ GCC_except_table970
+ GCC_except_table972
+ GCC_except_table973
+ GCC_except_table974
+ GCC_except_table975
+ GCC_except_table977
+ GCC_except_table978
+ GCC_except_table979
+ GCC_except_table980
+ GCC_except_table991
+ GCC_except_table996
+ OBJC_IVAR_$_SiriTTSSynthesisEngine._supportPhaticResponseCachedValue
+ OBJC_IVAR_$_SiriTTSSynthesisEngine._supportWordTimingCachedValue
+ OBJC_IVAR_$_SiriTTSSynthesisEngineRequest._wordAlignmentFailureHandler
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_UAFAssetSetManager
+ _OBJC_CLASS_$_UAFAssetSetSubscription
+ _OBJC_CLASS_$__TtC14SiriTTSService16TTSAssetUAFAsset
+ _OBJC_CLASS_$__TtC14SiriTTSService21TTSAssetUAFVoiceAsset
+ _OBJC_CLASS_$__TtC14SiriTTSService24TTSAssetUAFResourceAsset
+ _OBJC_METACLASS_$__TtC14SiriTTSService16TTSAssetUAFAsset
+ _OBJC_METACLASS_$__TtC14SiriTTSService21TTSAssetUAFVoiceAsset
+ _OBJC_METACLASS_$__TtC14SiriTTSService24TTSAssetUAFResourceAsset
+ _PROTOCOLS_SiriTTSAudibleContext.241
+ _PROTOCOLS_SiriTTSAudioData.113
+ _PROTOCOLS_SiriTTSAudioHintRequest.415
+ _PROTOCOLS_SiriTTSAudioRequest.264
+ _PROTOCOLS_SiriTTSInlineStreamingSignal.239
+ _PROTOCOLS_SiriTTSInstrumentationMetrics.225
+ _PROTOCOLS_SiriTTSPreviewRequest.385
+ _PROTOCOLS_SiriTTSProsodyProperties.247
+ _PROTOCOLS_SiriTTSSpeechRequest.354
+ _PROTOCOLS_SiriTTSSynthesisContext.253
+ _PROTOCOLS_SiriTTSSynthesisRequest.294
+ _PROTOCOLS_SiriTTSSynthesisResource.454
+ _PROTOCOLS_SiriTTSSynthesisVoice.445
+ _PROTOCOLS_SiriTTSVoiceSubscription.233
+ _PROTOCOLS_SiriTTSWordTimingInfo.235
+ __Block_byref_object_copy_.651
+ __Block_byref_object_dispose_.652
+ __DATA__TtC14SiriTTSService16TTSAssetUAFAsset
+ __DATA__TtC14SiriTTSService19TTSAssetUAFStrategy
+ __DATA__TtC14SiriTTSService21TTSAssetUAFVoiceAsset
+ __DATA__TtC14SiriTTSService24TTSAssetUAFAssetProvider
+ __DATA__TtC14SiriTTSService24TTSAssetUAFResourceAsset
+ __INSTANCE_METHODS__TtC14SiriTTSService16TTSAssetUAFAsset
+ __INSTANCE_METHODS__TtC14SiriTTSService21TTSAssetUAFVoiceAsset
+ __INSTANCE_METHODS__TtC14SiriTTSService24TTSAssetUAFResourceAsset
+ __IVARS__TtC14SiriTTSService16TTSAssetUAFAsset
+ __IVARS__TtC14SiriTTSService22SynthesisPrewarmAction
+ __IVARS__TtC14SiriTTSService24TTSAssetUAFAssetProvider
+ __METACLASS_DATA__TtC14SiriTTSService16TTSAssetUAFAsset
+ __METACLASS_DATA__TtC14SiriTTSService19TTSAssetUAFStrategy
+ __METACLASS_DATA__TtC14SiriTTSService21TTSAssetUAFVoiceAsset
+ __METACLASS_DATA__TtC14SiriTTSService24TTSAssetUAFAssetProvider
+ __METACLASS_DATA__TtC14SiriTTSService24TTSAssetUAFResourceAsset
+ __OBJC_$_CLASS_METHODS_SiriTTSSynthesisEngineRequest
+ __OBJC_$_INSTANCE_METHODS_SiriTTSBaseRequest(SiriTTSService)
+ __OBJC_CLASS_PROTOCOLS_$_SiriTTSBaseRequest(SiriTTSService)
+ __PROPERTIES__TtC14SiriTTSService16TTSAssetUAFAsset
+ __PROPERTIES__TtC14SiriTTSService21TTSAssetUAFVoiceAsset
+ __PROPERTIES__TtC14SiriTTSService24TTSAssetUAFResourceAsset
+ __ZN10applesauce2CF9ObjectRefIPKvED1Ev
+ __ZN14TTSSynthesizer23has_word_timing_supportERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZNKSt3__110__function6__funcIZ52-[SiriTTSSynthesisEngine _unlockedSynthesize:error:]E3$_6NS_9allocatorIS2_EEFvPKvEE11target_typeEv
+ __ZNKSt3__110__function6__funcIZ52-[SiriTTSSynthesisEngine _unlockedSynthesize:error:]E3$_6NS_9allocatorIS2_EEFvPKvEE6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIZ52-[SiriTTSSynthesisEngine _unlockedSynthesize:error:]E3$_6NS_9allocatorIS2_EEFvPKvEE7__cloneEPNS0_6__baseIS7_EE
+ __ZNKSt3__110__function6__funcIZ52-[SiriTTSSynthesisEngine _unlockedSynthesize:error:]E3$_6NS_9allocatorIS2_EEFvPKvEE7__cloneEv
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10TTSPromptsEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14TTSReplacementEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14WordTimingInfoEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15TTSWordPhonemesEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb17TTSNormalizedTextEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18TTSPhonemeSequenceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TextToSpeechRequest_16ContextInfoEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24TTSNeuralPhonemeSequenceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25TextToSpeechVoiceResourceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb34StartTextToSpeechStreamingRequest_16ContextInfoEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetINS3_6StringEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_10shared_ptrI8ObserverEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIsNS_9allocatorIsEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt9type_infoeqB8ne190102ERKS_
+ __ZNSt11logic_errorC1EPKc
+ __ZNSt11logic_errorD1Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110__function12__value_funcIFvPKvEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvRKNS_6vectorIN14TTSSynthesizer6MarkerENS_9allocatorIS4_EEEEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvRKNS_6vectorIfNS_9allocatorIfEEEEEED2B8ne190102Ev
+ __ZNSt3__110__function6__funcIZ52-[SiriTTSSynthesisEngine _unlockedSynthesize:error:]E3$_6NS_9allocatorIS2_EEFvPKvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZ52-[SiriTTSSynthesisEngine _unlockedSynthesize:error:]E3$_6NS_9allocatorIS2_EEFvPKvEE7destroyEv
+ __ZNSt3__110__function6__funcIZ52-[SiriTTSSynthesisEngine _unlockedSynthesize:error:]E3$_6NS_9allocatorIS2_EEFvPKvEED0Ev
+ __ZNSt3__110__function6__funcIZ52-[SiriTTSSynthesisEngine _unlockedSynthesize:error:]E3$_6NS_9allocatorIS2_EEFvPKvEED1Ev
+ __ZNSt3__110__function6__funcIZ52-[SiriTTSSynthesisEngine _unlockedSynthesize:error:]E3$_6NS_9allocatorIS2_EEFvPKvEEclEOS6_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102EPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__114__split_bufferINS_10shared_ptrI8ObserverEERNS_9allocatorIS3_EEED2Ev
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10TTSPromptsEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14TTSReplacementEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14WordTimingInfoEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15TTSWordPhonemesEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb17TTSNormalizedTextEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18TTSPhonemeSequenceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TextToSpeechRequest_16ContextInfoEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24TTSNeuralPhonemeSequenceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25TextToSpeechVoiceResourceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb34StartTextToSpeechStreamingRequest_16ContextInfoEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetINS4_6StringEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10shared_ptrI8ObserverEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorINS_10shared_ptrI8ObserverEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ __ZTINSt3__110__function6__funcIZ52-[SiriTTSSynthesisEngine _unlockedSynthesize:error:]E3$_6NS_9allocatorIS2_EEFvPKvEEE
+ __ZTISt11logic_error
+ __ZTIZ52-[SiriTTSSynthesisEngine _unlockedSynthesize:error:]E3$_6
+ __ZTSNSt3__110__function6__funcIZ52-[SiriTTSSynthesisEngine _unlockedSynthesize:error:]E3$_6NS_9allocatorIS2_EEFvPKvEEE
+ __ZTSZ52-[SiriTTSSynthesisEngine _unlockedSynthesize:error:]E3$_6
+ __ZTVNSt3__110__function6__funcIZ52-[SiriTTSSynthesisEngine _unlockedSynthesize:error:]E3$_6NS_9allocatorIS2_EEFvPKvEEE
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ __block_literal_global.740
+ _associated conformance 14SiriTTSService16TTSAssetFeaturesOSHAASQ
+ _kUAFPolicyUseCellular
+ _keypath_getTm
+ _objc_msgSend$hasPhaticResponsesWithVoicePath:
+ _objc_msgSend$hasWordTimingSupportWithVoicePath:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$synthesisIssueCauseString:
+ _objc_msgSend$wordAlignmentFailureHandler
+ _symbolic SDySSSDySSypGG
+ _symbolic Sd_____Iegyy_ So29UAFSubscriptionDownloadStatusV
+ _symbolic _____ 14SiriTTSService16TTSAssetFeaturesO
+ _symbolic _____ 14SiriTTSService16TTSAssetUAFAssetC
+ _symbolic _____ 14SiriTTSService19TTSAssetUAFStrategyC
+ _symbolic _____ 14SiriTTSService21TTSAssetUAFIdentifierV
+ _symbolic _____ 14SiriTTSService21TTSAssetUAFVoiceAssetC
+ _symbolic _____ 14SiriTTSService24TTSAssetUAFAssetProviderC
+ _symbolic _____ 14SiriTTSService24TTSAssetUAFResourceAssetC
+ _symbolic _____ So29UAFSubscriptionDownloadStatusV
+ _symbolic _____Sg 14SiriTTSService13ResourceAssetC
+ _symbolic _____Sg 14SiriTTSService24TTSAssetUAFAssetProviderC
+ _symbolic _____SgXwz_Xx 14SiriTTSService19AudioPlaybackActionC
+ _symbolic _____XDXMT 14SiriTTSService19TTSAssetUAFStrategyC
+ _symbolic _____XDXMT 14SiriTTSService24TTSAssetUAFAssetProviderC
+ _symbolic ______p 14SiriTTSService13AudioPlaybackP
+ _symbolic ______pSg So8NSObjectP
+ _symbolic ______pSgIegg_Sg s5ErrorP
+ _symbolic _____m 14SiriTTSService24TTSAssetUAFAssetProviderC
+ _symbolic _____mm 14SiriTTSService24TTSAssetUAFAssetProviderC
+ _symbolic _____ySS_SStG s23_ContiguousArrayStorageC
+ block_copy_helper.101
+ block_copy_helper.12
+ block_copy_helper.120
+ block_copy_helper.126
+ block_copy_helper.132
+ block_copy_helper.138
+ block_copy_helper.141
+ block_copy_helper.144
+ block_copy_helper.22
+ block_copy_helper.254
+ block_copy_helper.257
+ block_copy_helper.260
+ block_copy_helper.263
+ block_copy_helper.30
+ block_copy_helper.303
+ block_copy_helper.313
+ block_copy_helper.339
+ block_copy_helper.354
+ block_copy_helper.369
+ block_copy_helper.376
+ block_copy_helper.391
+ block_copy_helper.406
+ block_copy_helper.409
+ block_copy_helper.459
+ block_copy_helper.465
+ block_copy_helper.471
+ block_copy_helper.59
+ block_copy_helper.6
+ block_copy_helper.62
+ block_copy_helper.9
+ block_copy_helper.91
+ block_descriptor.103
+ block_descriptor.11
+ block_descriptor.122
+ block_descriptor.128
+ block_descriptor.134
+ block_descriptor.14
+ block_descriptor.140
+ block_descriptor.143
+ block_descriptor.146
+ block_descriptor.24
+ block_descriptor.256
+ block_descriptor.259
+ block_descriptor.262
+ block_descriptor.265
+ block_descriptor.305
+ block_descriptor.315
+ block_descriptor.32
+ block_descriptor.341
+ block_descriptor.356
+ block_descriptor.371
+ block_descriptor.378
+ block_descriptor.393
+ block_descriptor.408
+ block_descriptor.411
+ block_descriptor.461
+ block_descriptor.467
+ block_descriptor.473
+ block_descriptor.61
+ block_descriptor.64
+ block_descriptor.8
+ block_descriptor.93
+ block_destroy_helper.10
+ block_destroy_helper.102
+ block_destroy_helper.121
+ block_destroy_helper.127
+ block_destroy_helper.13
+ block_destroy_helper.133
+ block_destroy_helper.139
+ block_destroy_helper.142
+ block_destroy_helper.145
+ block_destroy_helper.23
+ block_destroy_helper.255
+ block_destroy_helper.258
+ block_destroy_helper.261
+ block_destroy_helper.264
+ block_destroy_helper.304
+ block_destroy_helper.31
+ block_destroy_helper.314
+ block_destroy_helper.340
+ block_destroy_helper.355
+ block_destroy_helper.370
+ block_destroy_helper.377
+ block_destroy_helper.392
+ block_destroy_helper.407
+ block_destroy_helper.410
+ block_destroy_helper.460
+ block_destroy_helper.466
+ block_destroy_helper.472
+ block_destroy_helper.60
+ block_destroy_helper.63
+ block_destroy_helper.7
+ block_destroy_helper.92
+ objectdestroy.14Tm
- GCC_except_table1004
- GCC_except_table101
- GCC_except_table1010
- GCC_except_table1012
- GCC_except_table1016
- GCC_except_table1018
- GCC_except_table1019
- GCC_except_table1020
- GCC_except_table1021
- GCC_except_table1022
- GCC_except_table1023
- GCC_except_table1025
- GCC_except_table1027
- GCC_except_table1029
- GCC_except_table1033
- GCC_except_table1052
- GCC_except_table1061
- GCC_except_table1064
- GCC_except_table1065
- GCC_except_table1066
- GCC_except_table1074
- GCC_except_table1080
- GCC_except_table1082
- GCC_except_table1087
- GCC_except_table1088
- GCC_except_table1089
- GCC_except_table1090
- GCC_except_table1092
- GCC_except_table110
- GCC_except_table1101
- GCC_except_table1118
- GCC_except_table1124
- GCC_except_table1126
- GCC_except_table1129
- GCC_except_table1132
- GCC_except_table1136
- GCC_except_table1139
- GCC_except_table1141
- GCC_except_table1143
- GCC_except_table1145
- GCC_except_table1148
- GCC_except_table119
- GCC_except_table1219
- GCC_except_table1256
- GCC_except_table1264
- GCC_except_table138
- GCC_except_table140
- GCC_except_table141
- GCC_except_table1422
- GCC_except_table1424
- GCC_except_table1425
- GCC_except_table1429
- GCC_except_table143
- GCC_except_table1430
- GCC_except_table144
- GCC_except_table145
- GCC_except_table146
- GCC_except_table147
- GCC_except_table148
- GCC_except_table156
- GCC_except_table161
- GCC_except_table170
- GCC_except_table172
- GCC_except_table174
- GCC_except_table175
- GCC_except_table187
- GCC_except_table191
- GCC_except_table193
- GCC_except_table199
- GCC_except_table203
- GCC_except_table205
- GCC_except_table209
- GCC_except_table215
- GCC_except_table217
- GCC_except_table221
- GCC_except_table243
- GCC_except_table247
- GCC_except_table251
- GCC_except_table262
- GCC_except_table264
- GCC_except_table268
- GCC_except_table272
- GCC_except_table274
- GCC_except_table276
- GCC_except_table278
- GCC_except_table280
- GCC_except_table291
- GCC_except_table297
- GCC_except_table303
- GCC_except_table305
- GCC_except_table344
- GCC_except_table346
- GCC_except_table368
- GCC_except_table370
- GCC_except_table372
- GCC_except_table374
- GCC_except_table376
- GCC_except_table380
- GCC_except_table382
- GCC_except_table422
- GCC_except_table424
- GCC_except_table438
- GCC_except_table446
- GCC_except_table454
- GCC_except_table460
- GCC_except_table472
- GCC_except_table476
- GCC_except_table478
- GCC_except_table482
- GCC_except_table484
- GCC_except_table488
- GCC_except_table490
- GCC_except_table503
- GCC_except_table505
- GCC_except_table513
- GCC_except_table517
- GCC_except_table519
- GCC_except_table524
- GCC_except_table531
- GCC_except_table538
- GCC_except_table553
- GCC_except_table560
- GCC_except_table562
- GCC_except_table584
- GCC_except_table588
- GCC_except_table594
- GCC_except_table596
- GCC_except_table597
- GCC_except_table598
- GCC_except_table600
- GCC_except_table606
- GCC_except_table613
- GCC_except_table619
- GCC_except_table621
- GCC_except_table630
- GCC_except_table632
- GCC_except_table634
- GCC_except_table638
- GCC_except_table643
- GCC_except_table644
- GCC_except_table645
- GCC_except_table657
- GCC_except_table659
- GCC_except_table662
- GCC_except_table668
- GCC_except_table681
- GCC_except_table687
- GCC_except_table689
- GCC_except_table695
- GCC_except_table696
- GCC_except_table697
- GCC_except_table698
- GCC_except_table708
- GCC_except_table71
- GCC_except_table710
- GCC_except_table713
- GCC_except_table714
- GCC_except_table719
- GCC_except_table725
- GCC_except_table727
- GCC_except_table729
- GCC_except_table73
- GCC_except_table731
- GCC_except_table74
- GCC_except_table740
- GCC_except_table742
- GCC_except_table752
- GCC_except_table753
- GCC_except_table755
- GCC_except_table758
- GCC_except_table764
- GCC_except_table766
- GCC_except_table776
- GCC_except_table781
- GCC_except_table787
- GCC_except_table789
- GCC_except_table800
- GCC_except_table802
- GCC_except_table803
- GCC_except_table805
- GCC_except_table806
- GCC_except_table808
- GCC_except_table810
- GCC_except_table811
- GCC_except_table812
- GCC_except_table813
- GCC_except_table815
- GCC_except_table816
- GCC_except_table817
- GCC_except_table818
- GCC_except_table847
- GCC_except_table849
- GCC_except_table851
- GCC_except_table863
- GCC_except_table866
- GCC_except_table868
- GCC_except_table872
- GCC_except_table878
- GCC_except_table880
- GCC_except_table894
- GCC_except_table896
- GCC_except_table92
- GCC_except_table922
- GCC_except_table924
- GCC_except_table927
- GCC_except_table929
- GCC_except_table935
- GCC_except_table937
- GCC_except_table948
- GCC_except_table950
- GCC_except_table951
- GCC_except_table952
- GCC_except_table953
- GCC_except_table954
- GCC_except_table958
- GCC_except_table959
- GCC_except_table960
- GCC_except_table976
- GCC_except_table989
- GCC_except_table995
- GCC_except_table997
- _OBJC_CLASS_$__TtC14SiriTTSService35TTSAssetTrialProxyInstantiatedAsset
- _OBJC_METACLASS_$__TtC14SiriTTSService35TTSAssetTrialProxyInstantiatedAsset
- _OUTLINED_FUNCTION_171
- _OUTLINED_FUNCTION_174
- _PROTOCOLS_SiriTTSAudibleContext.227
- _PROTOCOLS_SiriTTSAudioData.99
- _PROTOCOLS_SiriTTSAudioHintRequest.401
- _PROTOCOLS_SiriTTSAudioRequest.250
- _PROTOCOLS_SiriTTSBaseRequest.245
- _PROTOCOLS_SiriTTSInlineStreamingSignal.227
- _PROTOCOLS_SiriTTSInstrumentationMetrics.213
- _PROTOCOLS_SiriTTSPreviewRequest.371
- _PROTOCOLS_SiriTTSProsodyProperties.233
- _PROTOCOLS_SiriTTSSpeechRequest.340
- _PROTOCOLS_SiriTTSSynthesisContext.239
- _PROTOCOLS_SiriTTSSynthesisRequest.280
- _PROTOCOLS_SiriTTSSynthesisResource.440
- _PROTOCOLS_SiriTTSSynthesisVoice.431
- _PROTOCOLS_SiriTTSVoiceSubscription.221
- _PROTOCOLS_SiriTTSWordTimingInfo.221
- __Block_byref_object_copy_.629
- __Block_byref_object_dispose_.630
- __DATA__TtC14SiriTTSService35TTSAssetTrialProxyInstantiatedAsset
- __INSTANCE_METHODS_SiriTTSBaseRequest
- __METACLASS_DATA__TtC14SiriTTSService35TTSAssetTrialProxyInstantiatedAsset
- __PROTOCOLS_SiriTTSBaseRequest
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10TTSPromptsEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14TTSReplacementEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14WordTimingInfoEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15TTSWordPhonemesEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb17TTSNormalizedTextEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18TTSPhonemeSequenceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TextToSpeechRequest_16ContextInfoEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24TTSNeuralPhonemeSequenceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25TextToSpeechVoiceResourceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb34StartTextToSpeechStreamingRequest_16ContextInfoEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetINS3_6StringEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_10shared_ptrI8ObserverEENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIsNS_9allocatorIsEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt9type_infoeqB8ne180100ERKS_
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__110__function12__value_funcIFvPKvEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvRKNS_6vectorIN14TTSSynthesizer6MarkerENS_9allocatorIS4_EEEEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvRKNS_6vectorIfNS_9allocatorIfEEEEEED2B8ne180100Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100EPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ILi0EEEPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10TTSPromptsEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14TTSReplacementEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14WordTimingInfoEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15TTSWordPhonemesEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb17TTSNormalizedTextEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18TTSPhonemeSequenceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TextToSpeechRequest_16ContextInfoEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24TTSNeuralPhonemeSequenceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25TextToSpeechVoiceResourceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb34StartTextToSpeechStreamingRequest_16ContextInfoEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetINS4_6StringEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne180100Ev
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__16vectorINS_10shared_ptrI8ObserverEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_10shared_ptrI8ObserverEENS_9allocatorIS3_EEE9push_backB8ne180100ERKS3_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __block_literal_global.716
- _symbolic SS3key_yp5valuetSg
- _symbolic _____ 14SiriTTSService35TTSAssetTrialProxyInstantiatedAssetC
- _symbolic _____3key_yp5valuetSg So16TTSAssetPropertyV
- _symbolic _____3key_yp5valuetSg So8TTSAssetC14SiriTTSServiceE14VoiceAttributeO
- _symbolic _____ySS_SaySSGtG s23_ContiguousArrayStorageC
- block_copy_helper.23
- block_copy_helper.242
- block_copy_helper.245
- block_copy_helper.248
- block_copy_helper.251
- block_copy_helper.287
- block_copy_helper.297
- block_copy_helper.323
- block_copy_helper.338
- block_copy_helper.353
- block_copy_helper.360
- block_copy_helper.375
- block_copy_helper.390
- block_copy_helper.393
- block_copy_helper.445
- block_copy_helper.451
- block_copy_helper.457
- block_copy_helper.74
- block_copy_helper.77
- block_descriptor.244
- block_descriptor.247
- block_descriptor.25
- block_descriptor.250
- block_descriptor.253
- block_descriptor.289
- block_descriptor.299
- block_descriptor.325
- block_descriptor.340
- block_descriptor.355
- block_descriptor.362
- block_descriptor.377
- block_descriptor.392
- block_descriptor.395
- block_descriptor.447
- block_descriptor.453
- block_descriptor.459
- block_descriptor.76
- block_descriptor.79
- block_destroy_helper.24
- block_destroy_helper.243
- block_destroy_helper.246
- block_destroy_helper.249
- block_destroy_helper.252
- block_destroy_helper.288
- block_destroy_helper.298
- block_destroy_helper.324
- block_destroy_helper.339
- block_destroy_helper.354
- block_destroy_helper.361
- block_destroy_helper.376
- block_destroy_helper.391
- block_destroy_helper.394
- block_destroy_helper.446
- block_destroy_helper.452
- block_destroy_helper.458
- block_destroy_helper.75
- block_destroy_helper.78
CStrings:
+ "#PrewarmRequest %llu finished prewarming engine."
+ "#PrewarmRequest %llu is prewarming engine in background."
+ "#UAF listing assets for class '%s', types: '%{public}s', filter: '%{public}s'"
+ "#UAF updating %ld subscriptions for %s"
+ "#queyrWordTimingSupport voice: %{public}@"
+ "/Library/UnifiedAssetFramework/"
+ "/System/Library/AssetsV2/com_apple_MobileAsset_UAF_Siri_TextToSpeech/"
+ "@24@0:8^v16"
+ "@24@0:8q16"
+ "AudioClick"
+ "B16@?0q8"
+ "BNNSCorruptedInference"
+ "Can't determine asset matching subscription: %@"
+ "Collecting tailspin for %llu"
+ "Encountered synthesis issue, cause: %@"
+ "Encountered word alignment failure, word timing info will be ignored"
+ "Factor %s does not have expected prefix."
+ "Falling back to vi-VN buildInVoiceAsset for vi-VN-u-sd-vnct"
+ "Get namespace update, refreshing uaf client"
+ "Missing name on TRIFactor."
+ "Missing name on TRIFactorLevel."
+ "Proxy asset [%@] already locally available, no download necessary"
+ "Proxy asset [%@] cancelling download."
+ "Proxy asset [%@] download cancellation failed."
+ "Proxy asset [%@] download cancelled."
+ "Proxy asset [%@] download failed."
+ "Proxy asset [%@] download starting."
+ "Proxy asset [%@] download succeeded."
+ "Proxy asset [%@] not downloading, unable to cancel"
+ "Proxy asset download cancellation failed, unable to establish server connection"
+ "Proxy asset download failed, unable to establish server connection"
+ "Proxy asset download status check failed, unable to establish server connection"
+ "Proxy asset query purge condition failed, unable to establish server connection"
+ "Proxy asset set purge condition failed, unable to establish server connection"
+ "Refreshing stale uaf client"
+ "SiriAnalyticsHandler: High Customer Perceived Latency detected during synthesis."
+ "SiriTTSService.TTSAssetUAFAsset"
+ "SiriTTSService/CommonSession.swift"
+ "SiriTTSService/TTSAssetUAFStrategy.swift"
+ "SynthesisPreheatQueue"
+ "T@\"NSNumber\",&,N,V_supportPhaticResponseCachedValue"
+ "T@\"NSNumber\",&,N,V_supportWordTimingCachedValue"
+ "T@?,C,N,V_wordAlignmentFailureHandler"
+ "TTSAsset UAF Callbacks"
+ "Throttle tailspin to avoid performance degradation"
+ "Tq,N,V_profile"
+ "Trial assets %{public}@ deferred removal failed with error %@"
+ "Trial assets %{public}@ deferred removal succeeded"
+ "Trial assets %{public}@ immediate removal failed with error %@"
+ "Trial assets %{public}@ immediate removal succeeded"
+ "UAF asset %{public}@ already downloaded, unable to cancel"
+ "UAF asset %{public}@ download cancellation failed with error %@"
+ "UAF asset %{public}@ download cancelled"
+ "UAF asset %{public}@ download failed"
+ "UAF asset %{public}@ download succeeded"
+ "UAF asset %{public}@ not downloading, unable to cancel"
+ "UAF asset %{public}@ removal failed with error %@"
+ "UAF asset %{public}@ removal succeeded"
+ "UAF asset %{public}@ start download with policies %{public}@"
+ "UAF asset %{public}@ subscribe failed with error %@"
+ "UAF download %u%% done, %.2fs left %d written status %d"
+ "UAF/TrialXP (by Proxy)"
+ "UAFAssetDownloadProgress"
+ "UAFAssetProvider"
+ "UAFAssetSetManager"
+ "Unable to cancel download of non-TTSAssetUAFAsset asset"
+ "Unable to fetch TTS engine for prewarming, error: %@"
+ "Unable to get bundle path for factor identifier %s"
+ "Unable to start AudioQueue, error: %s"
+ "Unavailable UAF download size for %@, asset will be skipped."
+ "Unexpected non UAF/Trial asset %{public}@"
+ "UnhandledReason"
+ "Unknown"
+ "Word timing isn't supported"
+ "_TtC14SiriTTSService16TTSAssetUAFAsset"
+ "_TtC14SiriTTSService19TTSAssetUAFStrategy"
+ "_TtC14SiriTTSService21TTSAssetUAFVoiceAsset"
+ "_TtC14SiriTTSService24TTSAssetUAFAssetProvider"
+ "_TtC14SiriTTSService24TTSAssetUAFResourceAsset"
+ "_hasUAFEntitlements"
+ "_supportPhaticResponseCachedValue"
+ "_supportWordTimingCachedValue"
+ "_wordAlignmentFailureHandler"
+ "assetNamed:withUsage:"
+ "assetSize-generic"
+ "assetSize-iPhone"
+ "audioPlayback is nil."
+ "com.apple.security.exception.mach-lookup.global-name"
+ "com.apple.siri.uaf.service"
+ "downloadStatusForSubscriber:subscriptionName:"
+ "factorIdentifier"
+ "hasFactor"
+ "hasName"
+ "hasWordTimingSupportWithVoicePath:"
+ "initWithName:assetSets:usageAliases:"
+ "location"
+ "numberWithBool:"
+ "observeAssetSet:queue:handler:"
+ "propertyListWithData:options:format:error:"
+ "queryWordTimingSupportWithVoice:reply:"
+ "retrieveAssetSet:usages:"
+ "setSupportPhaticResponseCachedValue:"
+ "setSupportWordTimingCachedValue:"
+ "setWordAlignmentFailureHandler:"
+ "sharedManager"
+ "subscribe:subscriptions:queue:completion:"
+ "subscriptionsForSubscriber:"
+ "supportPhaticResponse"
+ "supportPhaticResponseCachedValue"
+ "supportWordTiming"
+ "supportWordTimingCachedValue"
+ "synthesisIssueCauseString:"
+ "tts.errors.word_alignment_failure"
+ "uaf"
+ "uafAssetProvider"
+ "unsubscribe:subscriptionNames:queue:completion:"
+ "updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:"
+ "use_F24Voices_enAU"
+ "use_F24Voices_frFR"
+ "use_F24Voices_itIT"
+ "use_uaf"
+ "wordAlignmentFailureHandler"
- "#SubscribedVoices not entitled to impersonate arbitrary clients"
- "#SubscribedVoices not entitled to impersonate clientId: %{public}s"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "SiriAnalyticsHandler: High Customer Percieved Latency detected during synthesis."
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "TQ,N,V_profile"
- "Trial asset %{public}@ deferred removal failed with error %@"
- "Trial asset %{public}@ deferred removal succeeded"
- "Trial asset %{public}@ immediate removal failed with error %@"
- "Trial asset %{public}@ immediate removal succeeded"
- "Trial proxy asset [%@] already locally available, no download necessary"
- "Trial proxy asset [%@] cancelling download."
- "Trial proxy asset [%@] download cancellation failed."
- "Trial proxy asset [%@] download cancelled."
- "Trial proxy asset [%@] download failed."
- "Trial proxy asset [%@] download starting."
- "Trial proxy asset [%@] download succeeded."
- "Trial proxy asset [%@] not downloading, unable to cancel"
- "Trial proxy asset download cancellation failed, unable to establish server connection"
- "Trial proxy asset download failed, unable to establish server connection"
- "Trial proxy asset query purge condition failed, unable to establish server connection"
- "Trial proxy asset set purge condition failed, unable to establish server connection"
- "Trial proxy download status check failed, unable to establish server connection"
- "TrialXP (by Proxy)"
- "Unexpected non Trial asset %{public}@"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.copyMemory with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "_TtC14SiriTTSService35TTSAssetTrialProxyInstantiatedAsset"
- "enable_natural_tts"
- "invalid Collection: less than 'count' elements in collection"
- "use_F24Voices_kk"
- "use_F24Voices_lt"
- "use_F24Voices_zhCN"
- "v16@?0Q8"

```
