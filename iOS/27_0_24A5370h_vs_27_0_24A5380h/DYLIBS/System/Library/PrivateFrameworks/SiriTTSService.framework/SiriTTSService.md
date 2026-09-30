## SiriTTSService

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService`

```diff

-  __TEXT.__text: 0x1d41a4
-  __TEXT.__objc_methlist: 0x6758
-  __TEXT.__const: 0x10de0
+  __TEXT.__text: 0x1df898
+  __TEXT.__objc_methlist: 0x6850
+  __TEXT.__const: 0x11320
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__cstring: 0xd65d
-  __TEXT.__swift5_typeref: 0x46f1
-  __TEXT.__oslogstring: 0x6eb9
-  __TEXT.__swift5_capture: 0x39a8
-  __TEXT.__swift5_reflstr: 0x433f
-  __TEXT.__swift5_assocty: 0x608
-  __TEXT.__constg_swiftt: 0x7bf8
-  __TEXT.__swift5_fieldmd: 0x5268
-  __TEXT.__swift5_builtin: 0x348
-  __TEXT.__swift5_protos: 0x60
-  __TEXT.__swift5_proto: 0xd8c
-  __TEXT.__swift5_types: 0x584
-  __TEXT.__swift_as_entry: 0x88
-  __TEXT.__swift_as_cont: 0x18c
-  __TEXT.__swift5_mpenum: 0x60
-  __TEXT.__swift_as_ret: 0xa8
-  __TEXT.__gcc_except_tab: 0x3bb8
-  __TEXT.__unwind_info: 0x95b8
-  __TEXT.__eh_frame: 0x82c4
+  __TEXT.__cstring: 0xd90a
+  __TEXT.__swift5_typeref: 0x47c8
+  __TEXT.__oslogstring: 0x72db
+  __TEXT.__swift5_capture: 0x3b90
+  __TEXT.__swift5_reflstr: 0x4546
+  __TEXT.__swift5_assocty: 0x638
+  __TEXT.__constg_swiftt: 0x7ed0
+  __TEXT.__swift5_fieldmd: 0x542c
+  __TEXT.__swift5_builtin: 0x384
+  __TEXT.__swift5_protos: 0x64
+  __TEXT.__swift5_proto: 0xdc8
+  __TEXT.__swift5_types: 0x5a8
+  __TEXT.__swift_as_entry: 0x98
+  __TEXT.__swift_as_cont: 0x1a0
+  __TEXT.__swift5_mpenum: 0x68
+  __TEXT.__swift_as_ret: 0xb8
+  __TEXT.__gcc_except_tab: 0x3bd0
+  __TEXT.__unwind_info: 0x9818
+  __TEXT.__eh_frame: 0x8418
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15c8
-  __DATA_CONST.__objc_classlist: 0x740
+  __DATA_CONST.__const: 0x1660
+  __DATA_CONST.__objc_classlist: 0x758
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23e8
+  __DATA_CONST.__objc_selrefs: 0x2428
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x250
-  __DATA_CONST.__got: 0xb70
-  __AUTH_CONST.__const: 0x18270
+  __DATA_CONST.__got: 0xba8
+  __AUTH_CONST.__const: 0x18568
   __AUTH_CONST.__cfstring: 0x1080
-  __AUTH_CONST.__objc_const: 0x118b8
+  __AUTH_CONST.__objc_const: 0x11d08
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__auth_got: 0x1f20
-  __AUTH.__objc_data: 0x3558
-  __AUTH.__data: 0x2d08
+  __AUTH_CONST.__auth_got: 0x1f68
+  __AUTH.__objc_data: 0x3fb8
+  __AUTH.__data: 0x5c38
   __DATA.__objc_ivar: 0x2f0
-  __DATA.__data: 0x3d70
-  __DATA.__bss: 0x170c0
-  __DATA.__common: 0x3e8
-  __DATA_DIRTY.__objc_data: 0x3df8
-  __DATA_DIRTY.__data: 0x4d90
+  __DATA.__data: 0x3c38
+  __DATA.__bss: 0x17750
+  __DATA.__common: 0x330
+  __DATA_DIRTY.__objc_data: 0x3458
+  __DATA_DIRTY.__data: 0x2388
   __DATA_DIRTY.__bss: 0x480
-  __DATA_DIRTY.__common: 0xc8
+  __DATA_DIRTY.__common: 0x178
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16108
-  Symbols:   18110
-  CStrings:  2190
+  Functions: 16505
+  Symbols:   18491
+  CStrings:  2225
 
Sections:
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
Symbols:
+ -[SiriTTSSpeechRequest(SwiftProxy) setVoiceExpressivityPreset:]
+ -[SiriTTSSpeechRequest(SwiftProxy) setVoicePacePreset:]
+ -[SiriTTSSpeechRequest(SwiftProxy) voiceExpressivityPreset]
+ -[SiriTTSSpeechRequest(SwiftProxy) voicePacePreset]
+ -[SiriTTSSynthesisEngine usingGryphonFrontend]
+ -[SiriTTSSynthesisRequest(SwiftProxy) setVoiceExpressivityPreset:]
+ -[SiriTTSSynthesisRequest(SwiftProxy) setVoicePacePreset:]
+ -[SiriTTSSynthesisRequest(SwiftProxy) voiceExpressivityPreset]
+ -[SiriTTSSynthesisRequest(SwiftProxy) voicePacePreset]
+ GCC_except_table1016
+ GCC_except_table1021
+ GCC_except_table1032
+ GCC_except_table1037
+ GCC_except_table1050
+ GCC_except_table1056
+ GCC_except_table1058
+ GCC_except_table1065
+ GCC_except_table1071
+ GCC_except_table1073
+ GCC_except_table1085
+ GCC_except_table1087
+ GCC_except_table1089
+ GCC_except_table1091
+ GCC_except_table1095
+ GCC_except_table1102
+ GCC_except_table1114
+ GCC_except_table1121
+ GCC_except_table1123
+ GCC_except_table1128
+ GCC_except_table1136
+ GCC_except_table1142
+ GCC_except_table1144
+ GCC_except_table1153
+ GCC_except_table1155
+ GCC_except_table1164
+ GCC_except_table1171
+ GCC_except_table1173
+ GCC_except_table1181
+ GCC_except_table1187
+ GCC_except_table1189
+ GCC_except_table1192
+ GCC_except_table1195
+ GCC_except_table1199
+ GCC_except_table1202
+ GCC_except_table1204
+ GCC_except_table1208
+ GCC_except_table1211
+ GCC_except_table1215
+ GCC_except_table1282
+ GCC_except_table1313
+ GCC_except_table1319
+ GCC_except_table1487
+ GCC_except_table1488
+ GCC_except_table1489
+ GCC_except_table1493
+ GCC_except_table1494
+ GCC_except_table1495
+ GCC_except_table195
+ GCC_except_table204
+ GCC_except_table218
+ GCC_except_table220
+ GCC_except_table222
+ GCC_except_table224
+ GCC_except_table226
+ GCC_except_table228
+ GCC_except_table232
+ GCC_except_table234
+ GCC_except_table238
+ GCC_except_table240
+ GCC_except_table244
+ GCC_except_table250
+ GCC_except_table252
+ GCC_except_table256
+ GCC_except_table278
+ GCC_except_table282
+ GCC_except_table286
+ GCC_except_table291
+ GCC_except_table293
+ GCC_except_table297
+ GCC_except_table299
+ GCC_except_table303
+ GCC_except_table307
+ GCC_except_table309
+ GCC_except_table311
+ GCC_except_table313
+ GCC_except_table315
+ GCC_except_table326
+ GCC_except_table332
+ GCC_except_table338
+ GCC_except_table340
+ GCC_except_table347
+ GCC_except_table367
+ GCC_except_table369
+ GCC_except_table371
+ GCC_except_table375
+ GCC_except_table377
+ GCC_except_table379
+ GCC_except_table381
+ GCC_except_table383
+ GCC_except_table385
+ GCC_except_table387
+ GCC_except_table389
+ GCC_except_table391
+ GCC_except_table395
+ GCC_except_table397
+ GCC_except_table403
+ GCC_except_table405
+ GCC_except_table407
+ GCC_except_table409
+ GCC_except_table411
+ GCC_except_table415
+ GCC_except_table417
+ GCC_except_table449
+ GCC_except_table453
+ GCC_except_table455
+ GCC_except_table457
+ GCC_except_table459
+ GCC_except_table461
+ GCC_except_table463
+ GCC_except_table465
+ GCC_except_table467
+ GCC_except_table469
+ GCC_except_table473
+ GCC_except_table475
+ GCC_except_table481
+ GCC_except_table483
+ GCC_except_table485
+ GCC_except_table487
+ GCC_except_table489
+ GCC_except_table491
+ GCC_except_table495
+ GCC_except_table497
+ GCC_except_table503
+ GCC_except_table505
+ GCC_except_table507
+ GCC_except_table511
+ GCC_except_table513
+ GCC_except_table517
+ GCC_except_table519
+ GCC_except_table523
+ GCC_except_table525
+ GCC_except_table528
+ GCC_except_table532
+ GCC_except_table534
+ GCC_except_table538
+ GCC_except_table540
+ GCC_except_table546
+ GCC_except_table548
+ GCC_except_table552
+ GCC_except_table554
+ GCC_except_table559
+ GCC_except_table566
+ GCC_except_table569
+ GCC_except_table571
+ GCC_except_table573
+ GCC_except_table580
+ GCC_except_table583
+ GCC_except_table587
+ GCC_except_table594
+ GCC_except_table609
+ GCC_except_table616
+ GCC_except_table618
+ GCC_except_table629
+ GCC_except_table638
+ GCC_except_table640
+ GCC_except_table644
+ GCC_except_table650
+ GCC_except_table654
+ GCC_except_table656
+ GCC_except_table662
+ GCC_except_table664
+ GCC_except_table669
+ GCC_except_table675
+ GCC_except_table677
+ GCC_except_table687
+ GCC_except_table689
+ GCC_except_table691
+ GCC_except_table695
+ GCC_except_table702
+ GCC_except_table705
+ GCC_except_table712
+ GCC_except_table714
+ GCC_except_table717
+ GCC_except_table723
+ GCC_except_table736
+ GCC_except_table742
+ GCC_except_table744
+ GCC_except_table754
+ GCC_except_table757
+ GCC_except_table764
+ GCC_except_table766
+ GCC_except_table773
+ GCC_except_table776
+ GCC_except_table782
+ GCC_except_table788
+ GCC_except_table791
+ GCC_except_table797
+ GCC_except_table799
+ GCC_except_table805
+ GCC_except_table810
+ GCC_except_table813
+ GCC_except_table819
+ GCC_except_table821
+ GCC_except_table825
+ GCC_except_table831
+ GCC_except_table833
+ GCC_except_table836
+ GCC_except_table842
+ GCC_except_table844
+ GCC_except_table863
+ GCC_except_table868
+ GCC_except_table873
+ GCC_except_table878
+ GCC_except_table883
+ GCC_except_table886
+ GCC_except_table895
+ GCC_except_table901
+ GCC_except_table907
+ GCC_except_table909
+ GCC_except_table911
+ GCC_except_table915
+ GCC_except_table921
+ GCC_except_table923
+ GCC_except_table930
+ GCC_except_table933
+ GCC_except_table939
+ GCC_except_table941
+ GCC_except_table947
+ GCC_except_table953
+ GCC_except_table955
+ GCC_except_table957
+ GCC_except_table961
+ GCC_except_table967
+ GCC_except_table977
+ GCC_except_table983
+ GCC_except_table985
+ GCC_except_table988
+ GCC_except_table990
+ GCC_except_table996
+ GCC_except_table998
+ _OUTLINED_FUNCTION_470
+ _OUTLINED_FUNCTION_471
+ _OUTLINED_FUNCTION_472
+ _OUTLINED_FUNCTION_473
+ _OUTLINED_FUNCTION_474
+ _OUTLINED_FUNCTION_475
+ _OUTLINED_FUNCTION_476
+ _OUTLINED_FUNCTION_477
+ _OUTLINED_FUNCTION_478
+ _OUTLINED_FUNCTION_479
+ _OUTLINED_FUNCTION_480
+ _OUTLINED_FUNCTION_481
+ _OUTLINED_FUNCTION_482
+ _OUTLINED_FUNCTION_483
+ _OUTLINED_FUNCTION_484
+ _OUTLINED_FUNCTION_485
+ _OUTLINED_FUNCTION_486
+ _OUTLINED_FUNCTION_487
+ _OUTLINED_FUNCTION_488
+ _OUTLINED_FUNCTION_489
+ _OUTLINED_FUNCTION_490
+ _OUTLINED_FUNCTION_491
+ _OUTLINED_FUNCTION_492
+ _OUTLINED_FUNCTION_493
+ _OUTLINED_FUNCTION_494
+ _OUTLINED_FUNCTION_495
+ _OUTLINED_FUNCTION_496
+ _OUTLINED_FUNCTION_497
+ _OUTLINED_FUNCTION_498
+ _OUTLINED_FUNCTION_499
+ _OUTLINED_FUNCTION_500
+ _OUTLINED_FUNCTION_501
+ _OUTLINED_FUNCTION_502
+ _OUTLINED_FUNCTION_503
+ _OUTLINED_FUNCTION_504
+ _OUTLINED_FUNCTION_505
+ _OUTLINED_FUNCTION_506
+ _OUTLINED_FUNCTION_507
+ _OUTLINED_FUNCTION_508
+ _OUTLINED_FUNCTION_509
+ _OUTLINED_FUNCTION_510
+ _OUTLINED_FUNCTION_511
+ _OUTLINED_FUNCTION_512
+ _OUTLINED_FUNCTION_513
+ _OUTLINED_FUNCTION_514
+ _OUTLINED_FUNCTION_515
+ _OUTLINED_FUNCTION_516
+ _OUTLINED_FUNCTION_517
+ _OUTLINED_FUNCTION_518
+ _OUTLINED_FUNCTION_519
+ _OUTLINED_FUNCTION_520
+ _OUTLINED_FUNCTION_521
+ _OUTLINED_FUNCTION_522
+ _OUTLINED_FUNCTION_523
+ _OUTLINED_FUNCTION_524
+ _OUTLINED_FUNCTION_525
+ _OUTLINED_FUNCTION_526
+ _OUTLINED_FUNCTION_527
+ _OUTLINED_FUNCTION_528
+ _OUTLINED_FUNCTION_529
+ _OUTLINED_FUNCTION_530
+ _OUTLINED_FUNCTION_531
+ __DATA__TtC14SiriTTSService12PCMConverter
+ __DATA__TtC14SiriTTSService24AudioNormalizationAction
+ __DATA__TtC14SiriTTSService26FrontendToolCachingService
+ __IVARS__TtC14SiriTTSService12PCMConverter
+ __IVARS__TtC14SiriTTSService24AudioNormalizationAction
+ __IVARS__TtC14SiriTTSService26FrontendToolCachingService
+ __METACLASS_DATA__TtC14SiriTTSService12PCMConverter
+ __METACLASS_DATA__TtC14SiriTTSService24AudioNormalizationAction
+ __METACLASS_DATA__TtC14SiriTTSService26FrontendToolCachingService
+ __ZN14TTSSynthesizer22using_gryphon_frontendEv
+ ___swift_closure_destructor.112Tm
+ ___swift_closure_destructor.1145Tm
+ ___swift_closure_destructor.1166Tm
+ ___swift_closure_destructor.1169Tm
+ ___swift_closure_destructor.1172Tm
+ ___swift_closure_destructor.388Tm
+ ___swift_closure_destructor.404Tm
+ ___swift_closure_destructor.44Tm
+ ___swift_closure_destructor.50Tm
+ ___swift_closure_destructor.78Tm
+ ___swift_closure_destructor.835Tm
+ ___swift_deallocate_boxed_opaque_existential_1
+ ___swift_memcpy34_8
+ ___swift_memcpy88_8
+ ___swift_memcpy89_8
+ _associated conformance 14SiriTTSService10AFMVersionVSLAASQ
+ _associated conformance 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO05EndOfG10CodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLOs0K3KeyAAs23CustomStringConvertible
+ _associated conformance 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO05EndOfG10CodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLOs0K3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO10CodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLOSHAASQ
+ _associated conformance 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO10CodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO10CodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLOs0I3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO14TextCodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLOSHAASQ
+ _associated conformance 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO14TextCodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLOs0J3KeyAAs23CustomStringConvertible
+ _associated conformance 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO14TextCodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLOs0J3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO19UtteranceCodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLOSHAASQ
+ _associated conformance 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO19UtteranceCodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLOs0J3KeyAAs23CustomStringConvertible
+ _associated conformance 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO19UtteranceCodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLOs0J3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 14SiriTTSService16SynthesisContextC19ObjCVoicePacePresetOSHAASQ
+ _associated conformance 14SiriTTSService16SynthesisContextC27ObjCVoiceExpressivityPresetOSHAASQ
+ _get_enum_tag_for_layout_string 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO
+ _objc_msgSend$appendStreamTaskWithId:tokenData:reply:
+ _objc_msgSend$setVoiceExpressivityPreset:
+ _objc_msgSend$setVoicePacePreset:
+ _objc_msgSend$startStreamWithSynthesisRequestData:reply:
+ _objc_msgSend$usingGryphonFrontend
+ _objc_msgSend$voiceExpressivityPreset
+ _objc_msgSend$voicePacePreset
+ _symbolic $s14SiriTTSService0A20OutputVoiceProvidingP
+ _symbolic SDySOypG
+ _symbolic SDySOypycG
+ _symbolic SDySSSaySo19SiriTTSFrontendToolCGG
+ _symbolic SDySS_____G 14SiriTTSService14AcousticValuesV
+ _symbolic SDySS_____GSg 14SiriTTSService14AcousticValuesV
+ _symbolic SS3key______5valuet 14SiriTTSService14AcousticValuesV
+ _symbolic SaySo19SiriTTSFrontendToolCG
+ _symbolic SbSg
+ _symbolic So16AVAudioPCMBufferCSg
+ _symbolic _____ 14SiriTTSService0A22OutputVoiceWithPresetsV
+ _symbolic _____ 14SiriTTSService10AFMVersionV
+ _symbolic _____ 14SiriTTSService12PCMConverterC
+ _symbolic _____ 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO05EndOfG10CodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLO
+ _symbolic _____ 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO10CodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLO
+ _symbolic _____ 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO14TextCodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLO
+ _symbolic _____ 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO19UtteranceCodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLO
+ _symbolic _____ 14SiriTTSService16SynthesisContextC19ObjCVoicePacePresetO
+ _symbolic _____ 14SiriTTSService16SynthesisContextC27ObjCVoiceExpressivityPresetO
+ _symbolic _____ 14SiriTTSService18VoicePresetPayloadV
+ _symbolic _____ 14SiriTTSService19AFMModelVersionGateO
+ _symbolic _____ 14SiriTTSService24AudioNormalizationActionC
+ _symbolic _____ 14SiriTTSService26FrontendToolCachingServiceC
+ _symbolic _____Iegn_ 14SiriTTSService18VoicePresetPayloadV
+ _symbolic _____Sg 14SiriTTSService12PCMConverterC
+ _symbolic _____SgXw 14SiriTTSService18GMSSynthesisActionC
+ _symbolic _____SgXwz_Xx 14SiriTTSService22SpeechGenerationActionC
+ _symbolic ______p 12ModelCatalog0B8ResourceP
+ _symbolic ______p 12ModelCatalog19AssetBackedResourceP
+ _symbolic ______p 14SiriTTSService0A20OutputVoiceProvidingP
+ _symbolic ______pSg 12ModelCatalog0B13AssetProtocolP
+ _symbolic ______pSg 12ModelCatalog0B8ResourceP
+ _symbolic ______pSg 14SiriTTSService0A20OutputVoiceProvidingP
+ _symbolic ______pm 14SiriTTSService0A20OutputVoiceProvidingP
+ _symbolic _____ySDySSSaySo19SiriTTSFrontendToolCGGG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____ySDyxq_GG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____ySOypG s17_NativeDictionaryV
+ _symbolic _____ySOypycG s17_NativeDictionaryV
+ _symbolic _____ySSSaySo19SiriTTSFrontendToolCGG s17_NativeDictionaryV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO05EndOfJ10CodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO10CodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO14TextCodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO19UtteranceCodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO05EndOfJ10CodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO10CodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO14TextCodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenO19UtteranceCodingKeys33_C4D12866C26F0D8333B9FCE3CA50A7F7LLO
+ _symbolic _____y______G 14SiriTTSService16InternalSettingsC7DefaultV s5Int32V
+ _type_layout_string 14SiriTTSService0A22OutputVoiceWithPresetsV
+ _type_layout_string 14SiriTTSService10AFMVersionV
+ _type_layout_string 14SiriTTSService18VoicePresetPayloadV
+ _type_layout_string So11CMTimeFlagsV
- GCC_except_table1007
- GCC_except_table1017
- GCC_except_table1031
- GCC_except_table1036
- GCC_except_table1049
- GCC_except_table1055
- GCC_except_table1057
- GCC_except_table1064
- GCC_except_table1070
- GCC_except_table1072
- GCC_except_table1076
- GCC_except_table1086
- GCC_except_table1088
- GCC_except_table1090
- GCC_except_table1094
- GCC_except_table1099
- GCC_except_table1113
- GCC_except_table1120
- GCC_except_table1122
- GCC_except_table1125
- GCC_except_table1135
- GCC_except_table1141
- GCC_except_table1143
- GCC_except_table1148
- GCC_except_table1154
- GCC_except_table1163
- GCC_except_table1170
- GCC_except_table1172
- GCC_except_table1180
- GCC_except_table1186
- GCC_except_table1188
- GCC_except_table1191
- GCC_except_table1194
- GCC_except_table1198
- GCC_except_table1201
- GCC_except_table1203
- GCC_except_table1205
- GCC_except_table1210
- GCC_except_table1214
- GCC_except_table1281
- GCC_except_table1312
- GCC_except_table1318
- GCC_except_table1478
- GCC_except_table1479
- GCC_except_table1480
- GCC_except_table1484
- GCC_except_table1485
- GCC_except_table1486
- GCC_except_table191
- GCC_except_table196
- GCC_except_table211
- GCC_except_table219
- GCC_except_table221
- GCC_except_table223
- GCC_except_table225
- GCC_except_table227
- GCC_except_table229
- GCC_except_table233
- GCC_except_table235
- GCC_except_table239
- GCC_except_table241
- GCC_except_table245
- GCC_except_table251
- GCC_except_table253
- GCC_except_table257
- GCC_except_table279
- GCC_except_table283
- GCC_except_table287
- GCC_except_table292
- GCC_except_table294
- GCC_except_table298
- GCC_except_table300
- GCC_except_table304
- GCC_except_table308
- GCC_except_table310
- GCC_except_table312
- GCC_except_table314
- GCC_except_table316
- GCC_except_table327
- GCC_except_table333
- GCC_except_table339
- GCC_except_table341
- GCC_except_table348
- GCC_except_table368
- GCC_except_table370
- GCC_except_table372
- GCC_except_table376
- GCC_except_table378
- GCC_except_table380
- GCC_except_table382
- GCC_except_table384
- GCC_except_table386
- GCC_except_table388
- GCC_except_table390
- GCC_except_table392
- GCC_except_table396
- GCC_except_table398
- GCC_except_table404
- GCC_except_table406
- GCC_except_table408
- GCC_except_table410
- GCC_except_table412
- GCC_except_table416
- GCC_except_table418
- GCC_except_table450
- GCC_except_table454
- GCC_except_table456
- GCC_except_table458
- GCC_except_table460
- GCC_except_table462
- GCC_except_table464
- GCC_except_table466
- GCC_except_table468
- GCC_except_table470
- GCC_except_table474
- GCC_except_table476
- GCC_except_table482
- GCC_except_table484
- GCC_except_table486
- GCC_except_table488
- GCC_except_table490
- GCC_except_table492
- GCC_except_table496
- GCC_except_table498
- GCC_except_table504
- GCC_except_table506
- GCC_except_table508
- GCC_except_table512
- GCC_except_table514
- GCC_except_table518
- GCC_except_table520
- GCC_except_table524
- GCC_except_table526
- GCC_except_table529
- GCC_except_table533
- GCC_except_table535
- GCC_except_table539
- GCC_except_table541
- GCC_except_table547
- GCC_except_table549
- GCC_except_table553
- GCC_except_table555
- GCC_except_table560
- GCC_except_table567
- GCC_except_table570
- GCC_except_table572
- GCC_except_table574
- GCC_except_table582
- GCC_except_table586
- GCC_except_table593
- GCC_except_table608
- GCC_except_table615
- GCC_except_table617
- GCC_except_table628
- GCC_except_table637
- GCC_except_table639
- GCC_except_table643
- GCC_except_table649
- GCC_except_table651
- GCC_except_table655
- GCC_except_table661
- GCC_except_table663
- GCC_except_table668
- GCC_except_table674
- GCC_except_table676
- GCC_except_table686
- GCC_except_table688
- GCC_except_table690
- GCC_except_table694
- GCC_except_table699
- GCC_except_table704
- GCC_except_table711
- GCC_except_table713
- GCC_except_table716
- GCC_except_table722
- GCC_except_table735
- GCC_except_table741
- GCC_except_table743
- GCC_except_table750
- GCC_except_table756
- GCC_except_table763
- GCC_except_table765
- GCC_except_table769
- GCC_except_table775
- GCC_except_table781
- GCC_except_table783
- GCC_except_table790
- GCC_except_table796
- GCC_except_table798
- GCC_except_table804
- GCC_except_table806
- GCC_except_table812
- GCC_except_table818
- GCC_except_table820
- GCC_except_table824
- GCC_except_table830
- GCC_except_table832
- GCC_except_table835
- GCC_except_table841
- GCC_except_table843
- GCC_except_table859
- GCC_except_table864
- GCC_except_table869
- GCC_except_table874
- GCC_except_table879
- GCC_except_table885
- GCC_except_table894
- GCC_except_table900
- GCC_except_table906
- GCC_except_table908
- GCC_except_table910
- GCC_except_table914
- GCC_except_table920
- GCC_except_table922
- GCC_except_table926
- GCC_except_table932
- GCC_except_table938
- GCC_except_table940
- GCC_except_table946
- GCC_except_table952
- GCC_except_table954
- GCC_except_table956
- GCC_except_table960
- GCC_except_table966
- GCC_except_table976
- GCC_except_table982
- GCC_except_table984
- GCC_except_table986
- GCC_except_table989
- GCC_except_table995
- GCC_except_table997
- ___swift_closure_destructor.1054Tm
- ___swift_closure_destructor.118Tm
- ___swift_closure_destructor.41Tm
- ___swift_closure_destructor.47Tm
- ___swift_closure_destructor.75Tm
- ___swift_closure_destructor.821Tm
- ___swift_memcpy73_8
- _associated conformance 14SiriTTSService10PaceValuesV10CodingKeys33_0B43D254CF689D0E612ACC3CA0A0D62ELLOSHAASQ
- _associated conformance 14SiriTTSService10PaceValuesV10CodingKeys33_0B43D254CF689D0E612ACC3CA0A0D62ELLOs0E3KeyAAs23CustomStringConvertible
- _associated conformance 14SiriTTSService10PaceValuesV10CodingKeys33_0B43D254CF689D0E612ACC3CA0A0D62ELLOs0E3KeyAAs28CustomDebugStringConvertible
- _associated conformance 14SiriTTSService13DaemonSessionC20SynthesisInputStreamV5TokenOs25LosslessStringConvertibleAAs06CustomjK0
- _associated conformance 14SiriTTSService18ExpressivityValuesV10CodingKeys33_0B43D254CF689D0E612ACC3CA0A0D62ELLOSHAASQ
- _associated conformance 14SiriTTSService18ExpressivityValuesV10CodingKeys33_0B43D254CF689D0E612ACC3CA0A0D62ELLOs0E3KeyAAs23CustomStringConvertible
- _associated conformance 14SiriTTSService18ExpressivityValuesV10CodingKeys33_0B43D254CF689D0E612ACC3CA0A0D62ELLOs0E3KeyAAs28CustomDebugStringConvertible
- _get_type_metadata 15Synchronization5MutexVy10Foundation3URLVSgG noncopyable
- _get_type_metadata 15Synchronization5MutexVy14SiriTTSService19AudioPowerProviding_pSgG noncopyable
- _get_type_metadata 15Synchronization5MutexVy14SiriTTSService25AudioPlaybackServiceStateOG noncopyable
- _get_type_metadata 15Synchronization5MutexVySSSgG noncopyable
- _get_type_metadata 15Synchronization5MutexVySaySSGSgG noncopyable
- _get_type_metadata 15Synchronization5MutexVySbG noncopyable
- _get_type_metadata 15Synchronization5MutexVySiG noncopyable
- _get_type_metadata 15Synchronization5MutexVySo12TTSAssetTypeCSgG noncopyable
- _get_type_metadata 15Synchronization5MutexVySo8NSNumberCSgG noncopyable
- _get_type_metadata SHRzr0_l15Synchronization5MutexVySDyxq_GG noncopyable
- _objc_msgSend$appendStreamTaskWithId:tokenString:reply:
- _swift_runtimeSupportsNoncopyableTypes
- _symbolic SDySS_____G 14SiriTTSService10PaceValuesV
- _symbolic SDySS_____G 14SiriTTSService18ExpressivityValuesV
- _symbolic SDySS_____GSg 14SiriTTSService10PaceValuesV
- _symbolic SDySS_____GSg 14SiriTTSService18ExpressivityValuesV
- _symbolic SDySSypycG
- _symbolic So13NSProcessInfoCmm
- _symbolic So19SiriTTSFrontendToolCSg
- _symbolic So20NSNotificationCenterCmm
- _symbolic _____ 14SiriTTSService10PaceValuesV
- _symbolic _____ 14SiriTTSService10PaceValuesV10CodingKeys33_0B43D254CF689D0E612ACC3CA0A0D62ELLO
- _symbolic _____ 14SiriTTSService18ExpressivityValuesV
- _symbolic _____ 14SiriTTSService18ExpressivityValuesV10CodingKeys33_0B43D254CF689D0E612ACC3CA0A0D62ELLO
- _symbolic ______pmm 14SiriTTSService15GMSAPIProvidingP
- _symbolic ______pmm 14SiriTTSService21OspreyConfigProvidingP
- _symbolic ______pmm 14SiriTTSService24SynthesisConfigProvidingP
- _symbolic ______pmm 14SiriTTSService37SpeechGeneratorCachingServiceProtocolP
- _symbolic ______pmm 14SiriTTSService39GMSTokenGeneratorCachingServiceProtocolP
- _symbolic _____mm 14SiriTTSService11NeuralUtilsC
- _symbolic _____mm 14SiriTTSService12CacheStorageC
- _symbolic _____mm 14SiriTTSService12EntitlementsV
- _symbolic _____mm 14SiriTTSService12OspreyClientC
- _symbolic _____mm 14SiriTTSService16InternalSettingsC
- _symbolic _____mm 14SiriTTSService18LocalAssetProviderC
- _symbolic _____mm 14SiriTTSService20BuiltInVoiceProviderC
- _symbolic _____mm 14SiriTTSService20EngineCachingServiceC
- _symbolic _____mm 14SiriTTSService22InlineStreamingStorageC
- _symbolic _____mm 14SiriTTSService24PreinstalledAudioStorageC
- _symbolic _____mm 14SiriTTSService24TTSAssetUAFAssetProviderC
- _symbolic _____mm 14SiriTTSService24TranscriptContextStorageC
- _symbolic _____mm 14SiriTTSService25PreinstalledVoiceProviderC
- _symbolic _____mm 14SiriTTSService28VocalizerCustomVoiceProviderC
- _symbolic _____mm 14SiriTTSService8TTSAssetC18AssistantVoiceMapsC
- _symbolic _____ySSypycG s17_NativeDictionaryV
- _symbolic _____y_____G s22KeyedDecodingContainerV 14SiriTTSService10PaceValuesV10CodingKeys33_0B43D254CF689D0E612ACC3CA0A0D62ELLO
- _symbolic _____y_____G s22KeyedDecodingContainerV 14SiriTTSService18ExpressivityValuesV10CodingKeys33_0B43D254CF689D0E612ACC3CA0A0D62ELLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 14SiriTTSService10PaceValuesV10CodingKeys33_0B43D254CF689D0E612ACC3CA0A0D62ELLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 14SiriTTSService18ExpressivityValuesV10CodingKeys33_0B43D254CF689D0E612ACC3CA0A0D62ELLO
- _type_layout_string 14SiriTTSService10PaceValuesV
- _type_layout_string 14SiriTTSService18ExpressivityValuesV
- _type_layout_string So16os_unfair_lock_sV
CStrings:
+ "\",\n \"voice_preset\": \"expressivity="
+ "# AFMModelVersionGate UAF namespace update received, invalidating cache"
+ "# AFMModelVersionGate base=%s adapter=%s → %{bool}d"
+ "# AFMModelVersionGate missing version → false"
+ "# AFMModelVersionGate no asset for %s variant=%s"
+ "# FrontendOverrideAction: Failed to execute stitch pipeline for locale %{public}s"
+ "# SpeechGenerationAction final rate:%f, low: 0.5, high: 4.0"
+ "# SpeechGenerationAction settings rate:%f, wsola:%f"
+ "# SynthesisPrewarmAction Missing request"
+ "# VoiceEmbeddingLoader No embedding plist for '%s' (UAF or built-in)"
+ "# VoiceEmbeddingLoader Resolved '%s' embeddings from UAF: %s"
+ "# VoiceEmbeddingLoader Resolved '%s' embeddings from built-in: %s"
+ "#FrontendToolCachingService Created stitch pipeline for locale %{public}s"
+ "#FrontendToolCachingService Failed to create stitch pipeline for locale %{public}s"
+ "#GMSSynthesisAction Sending GMS call with text: %s%s, request id: %llu"
+ "14.3.0.13.102949,0"
+ "14.5.81930.13.204414,0"
+ "AFMModelVersionGate.callbacks"
+ "AudioNormalizationAction: no audio found"
+ "AudioTrack: dropping audio with mismatched ASBD — track %f Hz vs incoming %f Hz. Upstream normalisation should have prevented this (rdar://178171278)."
+ "Failed to execute stitch pipeline for locale "
+ "Failed ttsfrontend_stitch_execute for %@ with error: %s\n"
+ "Missing sample count: %f, duration: %f"
+ "PCMConverter: convert error "
+ "PCMConverter: invalid destination asbd "
+ "PCMConverter: invalid source asbd "
+ "PCMConverter: unable to create converter from "
+ "PCMConverter: unable to create input buffer"
+ "PCMConverter: unable to create output buffer"
+ "SiriTTSService.Event.voicePresetResolved"
+ "Stream synthesis request error: %s"
+ "Streaming #SynthesisRequest %{public}s"
+ "TTSAudioStall"
+ "VoicePresetPayload"
+ "Workflow: wait() timed out unexpectedly"
+ "Workflow: wait() timed out unexpectedly on %s"
+ "com.apple.fm.language.instruct_3b.base"
+ "disableInferenceRetry"
+ "fmVoiceThermalThreshold"
+ "forceNeuralThermalState"
+ "isFmPlatform: %{bool}d, isNaturalPlatform: %{bool}d, isNeuralPlatform: %{bool}d, thermal level: %s, low power mode: %{bool}d"
+ "m11"
+ "stream(synthesisRequest:inputHandler:)"
+ "voice_expressivity_preset"
+ "voice_pace_preset"
- "# FrontendOverrideAction: Created new stitch pipeline for locale %{public}s"
- "# FrontendOverrideAction: Failed to create stitch pipeline for locale %{public}s"
- "# FrontendOverrideAction: Failed to execute stitch pipeline"
- "# SpeechGenerationAction Missing voiceExpressivityPreset for request "
- "#GMSSynthesisAction Sending GMS call with text: %s, request id: %llu"
- "Failed to create stitch pipeline for locale "
- "Failed to execute stitch pipeline"
- "disableDeviceRacing"
- "disableOspreyStreaming"
- "isNaturalPlatform: %{bool}d, isNeuralPlatform: %{bool}d, thermal level: %s, low power mode: %{bool}d"

```
