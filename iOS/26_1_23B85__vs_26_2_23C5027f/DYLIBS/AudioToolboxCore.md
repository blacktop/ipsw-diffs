## AudioToolboxCore

> `/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`

```diff

-1556.224.0.0.0
-  __TEXT.__text: 0x3193a0
+1556.303.0.0.0
+  __TEXT.__text: 0x319640
   __TEXT.__auth_stubs: 0x3790
   __TEXT.__objc_methlist: 0x376c
   __TEXT.__const: 0x2065d
   __TEXT.__dlopen_cstrs: 0x50a
   __TEXT.__gcc_except_tab: 0x2649c
-  __TEXT.__cstring: 0x1c241
+  __TEXT.__cstring: 0x1c282
   __TEXT.__oslogstring: 0x14bee
   __TEXT.__dof_AudioTool: 0x4f1
   __TEXT.__dof_AUHosting: 0x23c

   __TEXT.__unwind_info: 0xda20
   __TEXT.__eh_frame: 0x88
   __TEXT.__objc_classname: 0x7a8
-  __TEXT.__objc_methname: 0x72cf
-  __TEXT.__objc_methtype: 0x5115
+  __TEXT.__objc_methname: 0x72d7
+  __TEXT.__objc_methtype: 0x51c7
   __TEXT.__objc_stubs: 0x59e0
   __DATA_CONST.__got: 0x578
   __DATA_CONST.__const: 0x8f10

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 79C9BD3B-0341-3C1B-BF10-2B86C9494CF3
+  UUID: A66DA9E9-45A0-355F-AC80-3B2E23CE40E8
   Functions: 11319
   Symbols:   29809
-  CStrings:  9308
+  CStrings:  9309
 
Symbols:
+ __ZL13CheckPropertyjjPKv.14166
+ __ZL27selectAudioConverterServiceb.14188
+ __ZL29ParameterListPropertyListenerPvP28OpaqueAudioComponentInstancejjj.14757
+ __ZTI3$_0.15257
+ __ZTI3$_0.15434
+ __ZTS3$_0.15268
+ __ZTS3$_0.15436
+ __ZZL16isPlatformBinaryvE14platformBinary.14193
+ __ZZL16isPlatformBinaryvE4once.14191
+ ___Block_byref_object_copy_.14621
+ ___Block_byref_object_copy_.15570
+ ___Block_byref_object_dispose_.14622
+ ___Block_byref_object_dispose_.15571
+ ____ZL16isPlatformBinaryv_block_invoke.14200
+ ____ZN8DSPGraph6getLogEv_block_invoke.15696
+ ___block_descriptor_tmp.13979
+ ___block_descriptor_tmp.14198
+ ___block_descriptor_tmp.15694
+ ___block_descriptor_tmp.31.13972
+ ___block_literal_global.13286
+ ___block_literal_global.13962
+ ___block_literal_global.14192
+ ___block_literal_global.14624
+ ___block_literal_global.15208
+ ___block_literal_global.15680
+ ___block_literal_global.15899
+ ___block_literal_global.24.13963
+ ___block_literal_global.34.14631
+ ___block_literal_global.37.14632
- __ZL13CheckPropertyjjPKv.14165
- __ZL27selectAudioConverterServiceb.14187
- __ZL29ParameterListPropertyListenerPvP28OpaqueAudioComponentInstancejjj.14756
- __ZTI3$_0.15256
- __ZTI3$_0.15433
- __ZTS3$_0.15267
- __ZTS3$_0.15435
- __ZZL16isPlatformBinaryvE14platformBinary.14192
- __ZZL16isPlatformBinaryvE4once.14190
- ___Block_byref_object_copy_.14620
- ___Block_byref_object_copy_.15569
- ___Block_byref_object_dispose_.14621
- ___Block_byref_object_dispose_.15570
- ____ZL16isPlatformBinaryv_block_invoke.14199
- ____ZN8DSPGraph6getLogEv_block_invoke.15695
- ___block_descriptor_tmp.13978
- ___block_descriptor_tmp.14197
- ___block_descriptor_tmp.15693
- ___block_descriptor_tmp.31.13971
- ___block_literal_global.13285
- ___block_literal_global.13961
- ___block_literal_global.14191
- ___block_literal_global.14623
- ___block_literal_global.15207
- ___block_literal_global.15679
- ___block_literal_global.15898
- ___block_literal_global.24.13962
- ___block_literal_global.34.14630
- ___block_literal_global.37.14631
Functions:
~ __ZN4acv219PCMConverterFactory19BuildConverterChainERKNS_14StreamDescPairERKNS_18ChainBuildSettingsERNS_19AudioConverterChainERS0_ : 3624 -> 3636
~ __ZN4acv219PCMConverterFactory20AddDownReinterleaverERNS_14StreamDescPairERNS_17ChannelLayoutPairERKNS_18ChainBuildSettingsERNSt3__16vectorINS8_10unique_ptrINS_18AudioConverterBaseENS8_14default_deleteISB_EEEENS8_9allocatorISE_EEEERb : 696 -> 704
~ __ZN4acv219PCMConverterFactory12AddPCMToGoalERKN2CA17StreamDescriptionERNS_14StreamDescPairERKNS_18ChainBuildSettingsERNSt3__16vectorINSA_10unique_ptrINS_18AudioConverterBaseENSA_14default_deleteISD_EEEENSA_9allocatorISG_EEEEb : 3668 -> 3680
~ __ZN4acv219PCMConverterFactory31BuildSampleFormatConverterChainERKNS_14StreamDescPairERN2CA17StreamDescriptionERNSt3__16vectorINS7_10unique_ptrINS_18AudioConverterBaseENS7_14default_deleteISA_EEEENS7_9allocatorISD_EEEE : 1588 -> 1596
~ __ZN4acv219PCMConverterFactory18AddUpReinterleaverERNS_14StreamDescPairERNS_17ChannelLayoutPairERKNS_18ChainBuildSettingsERNSt3__16vectorINS8_10unique_ptrINS_18AudioConverterBaseENS8_14default_deleteISB_EEEENS8_9allocatorISE_EEEEb : 684 -> 692
~ __ZN26AudioMetadataMemoryPool_APC2Ev : 484 -> 492
~ __ZN5auoop21WorkgroupManager_Base5State12addWorkgroupEjP15OS_os_workgroup : 964 -> 972
~ __ZN20AudioComponentVector12insertSortedENSt3__111__wrap_iterIPNS0_10shared_ptrI11APComponentEEEERKS4_ : 656 -> 676
~ __ZNSt3__16vectorINS_10shared_ptrI11APComponentEENS_9allocatorIS3_EEE18__assign_with_sizeB8ne200100IPS3_S8_EEvT_T0_l : 268 -> 280
~ __ZNSt3__16vectorINS_10shared_ptrIN2CA9ADMObjectEEENS_9allocatorIS4_EEE9push_backB8ne200100ERKS4_ : 272 -> 280
~ __ZN20AudioComponentVector8subtractERS_ : 640 -> 644
~ __ZN8DSPGraph11Interpreter11compileTextEPKcRKNSt3__113unordered_mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEESA_NS3_4hashISA_EENS3_8equal_toISA_EENS8_INS3_4pairIKSA_SA_EEEEEERKNS3_6vectorISA_NS8_ISA_EEEE : 9208 -> 9264
~ __ZNSt3__112__hash_tableINS_10unique_ptrIN8DSPGraph8IsoGroupENS_14default_deleteIS3_EEEENS_4hashIS6_EENS_8equal_toIS6_EENS_9allocatorIS6_EEE25__emplace_unique_key_argsIS6_JS6_EEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_ : 1100 -> 1104
~ __ZN8DSPGraph14NewBoxRegistry3addERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERK25AudioComponentDescriptionRKNS1_8functionIFPNS_3BoxEjjEEE : 1648 -> 1620
~ __ZN8DSPGraph5Graph19initializeWithFlagsEj : 3864 -> 3852
~ __ZN8DSPGraph3Box10initializeEv : 3316 -> 3320
~ __ZN4acv219PCMConverterFactory6AddSRCERNS_14StreamDescPairERKNS_18ChainBuildSettingsERNSt3__16vectorINS6_10unique_ptrINS_18AudioConverterBaseENS6_14default_deleteIS9_EEEENS6_9allocatorISC_EEEE : 1092 -> 1100
~ __ZN4acv219SampleRateConverter16ReplaceResamplerEv : 2424 -> 2452
~ __ZNSt3__16vectorIN22ACRendererSharedMemory7ElementENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJPN2CA17StreamDescriptionEjRjRPhSC_EEEPS2_DpOT_ : 548 -> 552
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_6vectorIPN8DSPGraph6BufferENS_9allocatorIS5_EEEEEENS_22__unordered_map_hasherIjS9_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS9_SE_SC_Lb1EEENS6_IS9_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSO_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS9_PvEEEEbEERKT_DpOT0_ : 1048 -> 1052
~ __ZN8DSPGraph3BoxC2Ejj : 2048 -> 2072
~ __ZN8DSPGraph5Graph6addBoxEPNS_3BoxERKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS3_8optionalIyEE : 3360 -> 3356
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8DSPGraph18FormatAndBlockSizeEEENS_22__unordered_map_hasherIS7_SA_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SA_SF_SD_Lb1EEENS5_ISA_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRKS7_EEENSP_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeISA_PvEEEEbEERKT_DpOT0_ : 1136 -> 1132
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjN8DSPGraph5Graph14GraphParameterEEENS_22__unordered_map_hasherIjS5_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSL_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_ : 1056 -> 1060
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjN8DSPGraph5Graph13GraphPropertyEEENS_22__unordered_map_hasherIjS5_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSL_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_ : 1064 -> 1068
~ __ZN4acv217Resampler2Wrapper23GetNumberOfSourceFramesEj : 52 -> 44
~ __ZN8DSPGraph6SRCBox10initializeEv : 1708 -> 1700
~ __ZN12_GLOBAL__N_122encode_channel_formatsERKNS_13PacketBuilderEN2CA33AudioMetadataSerializedPacketTypeEPhRmmddd : 1812 -> 1824
~ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12CADeprecated10TSingletonI11IPCAUClientE8instanceEvEUlvE_EEEEEvPv : 1288 -> 1292
~ __ZNSt3__16vectorIN17CAFStringsWrapper16CAFStringWrapperENS_9allocatorIS2_EEE9push_backB8ne200100ERKS2_ : 500 -> 508
~ __ZNSt3__16vectorINS_4pairIN10applesauce2CF9StringRefES4_EENS_9allocatorIS5_EEE7reserveEm : 164 -> 172
~ __ZN13VorbisComment14AddUserCommentERKN10applesauce2CF9StringRefES4_ : 404 -> 408
~ __ZN10applesauce2CF7details11parse_arrayIN8minijson20const_buffer_contextEEENS0_7TypeRefERT_ : 1904 -> 1908
~ __ZN21AudioMetadataTimeline8addEventENSt3__110shared_ptrI27AudioMetadataFormatExtendedEEd : 36028 -> 36228
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE9push_backB8ne200100EOS6_ : 300 -> 308
~ __ZN2CA10ADMBuilder5buildEv : 6516 -> 6520
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIN2CA16ADMChannelFormatEEEEENS_22__unordered_map_hasherIS7_SC_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SC_SH_SF_Lb1EEENS5_ISC_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRKS7_EEENSR_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeISC_PvEEEEbEERKT_DpOT0_ : 1156 -> 1148
~ __ZNSt3__16vectorIN2CA14ADMBlockFormatENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 328 -> 332
~ __ZN2CA10ADMBuilder4Impl25build_common_track_formatENS1_14ADMChannelTypeEm : 2168 -> 2140
~ __ZN2CA10ADMBuilder4Impl26build_common_stream_formatENS1_14ADMChannelTypeEm : 2680 -> 2656
~ __ZNSt3__16vectorINS_10shared_ptrIN2CA15ADMStreamFormatEEENS_9allocatorIS4_EEE12emplace_backIJS4_EEERS4_DpOT_ : 240 -> 248
~ __ZN8DSPGraph8ProfilerC2ERKNSt3__110shared_ptrINS_5GraphEEEd : 1972 -> 1896
~ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJPKcNS2_13DictionaryRefEEEEPS3_DpOT_ : 276 -> 288
~ __ZNSt3__16vectorI15ISOLoudnessInfoNS_9allocatorIS1_EEE6resizeEm : 556 -> 560
~ __ZN13KVOAggregator4findEP8NSObjectP8NSStringb : 1216 -> 1224
~ __ZN17AUOOPSharedMemory5init2ERKNS_20InitializationParamsENSt3__14spanIhLm18446744073709551615EEE : 1128 -> 1132
~ ____ZN23NotifyDStateDumpManager17registerSubsystemE27CACentralStateDumpSubsystemPK10__CFStringU13block_pointerFvP7__sFILEE_block_invoke : 1076 -> 1072
~ ____ZN18OSStateDumpManager17registerSubsystemE27CACentralStateDumpSubsystemPK10__CFStringU13block_pointerFvP7__sFILEE_block_invoke : 1380 -> 1376
~ __ZN3HOA13createDecoderERKNSt3__16vectorIfNS0_9allocatorIfEEEES6_NS_16DecoderAlgorithmENS_16DecoderWeightingE : 12620 -> 12624
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeItNS_6vectorItNS_9allocatorItEEEEEENS_22__unordered_map_hasherItS6_NS_4hashItEENS_8equal_toItEELb1EEENS_21__unordered_map_equalItS6_SB_S9_Lb1EEENS3_IS6_EEE25__emplace_unique_key_argsItJRKNS_21piecewise_construct_tENS_5tupleIJRKtEEENSL_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_ : 1052 -> 1056
~ __ZNSt3__113unordered_mapIN12_GLOBAL__N_18FormatIDENS_6vectorIS2_NS_9allocatorIS2_EEEENS_4hashIS2_EENS_8equal_toIS2_EENS4_INS_4pairIKS2_S6_EEEEEC1ERKSF_ : 800 -> 804
~ __ZNSt3__113unordered_mapIN12_GLOBAL__N_18FormatIDENS_6vectorIS2_NS_9allocatorIS2_EEEENS_4hashIS2_EENS_8equal_toIS2_EENS4_INS_4pairIKS2_S6_EEEEEixERSC_ : 616 -> 620
~ __ZNSt3__16vectorIN16AUv3InstanceBase17ScopeElementIDObjENS_9allocatorIS2_EEE7reserveEm : 192 -> 196
~ __ZNSt3__16vectorIN16AUv3InstanceBase17ScopeElementIDObjENS_9allocatorIS2_EEE9push_backB8ne200100ERKS2_ : 364 -> 372
~ -[AUAudioUnit_XPC allocateRenderResourcesAndReturnError:] : 6856 -> 6860
~ __ZN8nlohmann10basic_jsonINSt3__13mapENS1_6vectorENS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEbxydS7_NS_14adl_serializerENS3_IhNS7_IhEEEEEixEm : 1336 -> 1360
~ __ZN8nlohmann10basic_jsonINSt3__13mapENS1_6vectorENS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEbxydS7_NS_14adl_serializerENS3_IhNS7_IhEEEEEC2ERKSD_ : 1020 -> 1024
~ __ZNSt3__16vectorIN8nlohmann10basic_jsonINS_3mapES0_NS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbxydS7_NS1_14adl_serializerENS0_IhNS7_IhEEEEEENS7_ISD_EEE7reserveEm : 192 -> 204
~ __ZNSt3__16vectorIN8nlohmann10basic_jsonINS_3mapES0_NS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbxydS7_NS1_14adl_serializerENS0_IhNS7_IhEEEEEENS7_ISD_EEE24__emplace_back_slow_pathIJSD_EEEPSD_DpOT_ : 292 -> 296
~ __ZN4VBAP35calculateVirtualLoudspeakersPolygonERKNSt3__16vectorIfNS0_9allocatorIfEEEERNS1_IS4_NS2_IS4_EEEERNS1_INS1_IjNS2_IjEEEENS2_ISB_EEEE : 2772 -> 2780
~ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE6resizeEm : 412 -> 416
~ __ZNSt3__16vectorINS0_IjNS_9allocatorIjEEEENS1_IS3_EEE6resizeEm : 412 -> 416
~ __ZN2CA10ADMBuilder4Impl33parse_block_format_zone_exclusionEPKhPS3_ : 2392 -> 2368
~ __ZN20AudioComponentVector6appendERKS_ : 436 -> 444
~ __ZNSt3__16vectorINS0_INS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEEENS4_IS8_EEE9push_backB8ne200100EOS8_ : 316 -> 324
~ __ZNSt3__16vectorINS_10unique_ptrIvN10applesauce4raii2v16detail23opaque_deletion_functorIPvXadL_Z27VPTimeFreqConverter_DisposeEEEEEENS_9allocatorIS9_EEE7reserveEm : 152 -> 156
~ __ZN2CA15extractMetadataER23AudioMetadataMemoryPoolRKNS_3ADME : 15832 -> 15836
~ __ZNSt3__16vectorI19BusPropertyObserverNS_9allocatorIS1_EEE18__assign_with_sizeB8ne200100IPS1_S6_EEvT_T0_l : 272 -> 288
~ __ZNSt3__16vectorI19BusPropertyObserverNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_ : 436 -> 444
~ __ZN2CA10ADMBuilder4Impl11parse_modelEPKhPS3_ : 10144 -> 10180
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIN2CA13ADMPackFormatEEEEENS_22__unordered_map_hasherIS7_SC_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SC_SH_SF_Lb1EEENS5_ISC_EEE25__emplace_unique_key_argsIS7_JNS_4pairIKS7_SB_EEEEENSO_INS_15__hash_iteratorIPNS_11__hash_nodeISC_PvEEEEbEERKT_DpOT0_ : 680 -> 676
~ __ZNSt3__16vectorINS0_INS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEEENS4_IS8_EEE24__emplace_back_slow_pathIJS8_EEEPS8_DpOT_ : 268 -> 272
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIN2CA14ADMTrackFormatEEEEENS_22__unordered_map_hasherIS7_SC_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SC_SH_SF_Lb1EEENS5_ISC_EEE25__emplace_unique_key_argsIS7_JNS_4pairIKS7_SB_EEEEENSO_INS_15__hash_iteratorIPNS_11__hash_nodeISC_PvEEEEbEERKT_DpOT0_ : 680 -> 676
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIN2CA15ADMStreamFormatEEEEENS_22__unordered_map_hasherIS7_SC_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SC_SH_SF_Lb1EEENS5_ISC_EEE25__emplace_unique_key_argsIS7_JNS_4pairIKS7_SB_EEEEENSO_INS_15__hash_iteratorIPNS_11__hash_nodeISC_PvEEEEbEERKT_DpOT0_ : 680 -> 676
~ __ZN8DSPGraph11InterpreterC2ERKNS_14NewBoxRegistryE : 1812 -> 1816
~ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJPKcdEEEPS3_DpOT_ : 276 -> 288
~ -[AUAudioUnitV2Bridge _createParameterTree] : 3332 -> 3344
~ __ZNSt3__16vectorIN20ParameterTreeBuilder14ClumpableParamENS_9allocatorIS2_EEE9push_backB8ne200100EOS2_ : 292 -> 300
~ -[AUHALOutputUnit tokenByAddingRenderObserver:] : 1204 -> 1196
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRKS6_EEEPS6_DpOT_ : 320 -> 324
~ _AudioSampleRateConverterCreate : 2704 -> 2680
~ __ZNSt3__16vectorI15ISOLoudnessInfoNS_9allocatorIS1_EEE16__init_with_sizeB8ne200100IPS1_S6_EEvT_T0_m : 360 -> 364
~ __ZNSt3__16vectorI18ISOLoudnessInfoBoxNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRS1_EEEPS1_DpOT_ : 436 -> 440
~ __ZN8DSPGraph3Box17addRenderCallbackENSt3__18functionIFvPS0_jEEENS_18RenderCallbackTypeENS_19RenderCallbackOrderE : 1920 -> 1924
~ __ZN8DSPGraph3Box14addPropertyTapERKNS_11PropertyTapE : 512 -> 516
~ __ZN4APAC23MetadataBitStreamParser31parseParametricRadiationPatternERNS_8Metadata12RendererData16RadiationPattern26ParametricRadiationPatternEbRN2AT16TBitstreamReaderIjEE : 3136 -> 3276
~ __ZN13VorbisCommentaSERKS_ : 384 -> 396
~ __ZN8DSPGraph5Graph17addRenderCallbackENSt3__18functionIFvPS0_jEEENS_18RenderCallbackTypeENS_19RenderCallbackOrderE : 1872 -> 1876
~ __ZNSt3__16vectorIN8DSPGraph5Graph11GraphBridgeENS_9allocatorIS3_EEE9push_backB8ne200100ERKS3_ : 680 -> 688
~ __ZNSt3__16vectorIN8DSPGraph5Graph11GraphBridge15BridgedPropertyENS_9allocatorIS4_EEE9push_backB8ne200100EOS4_ : 452 -> 460
~ __ZNSt3__16vectorIN8DSPGraph5Graph11GraphBridge15BridgedPropertyENS_9allocatorIS4_EEE16__init_with_sizeB8ne200100IPS4_S9_EEvT_T0_m : 264 -> 268
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8DSPGraph4JackEEENS_22__unordered_map_hasherIS7_SA_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SA_SF_SD_Lb1EEENS5_ISA_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRKS7_EEENSP_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeISA_PvEEEEbEERKT_DpOT0_ : 1116 -> 1112
CStrings:
+ "@68@0:8{unique_ptr<AUHostingServiceClient, std::default_delete<AUHostingServiceClient>>={?=^{AUHostingServiceClient}}}16{AudioComponentDescription=IIIII}24^{OpaqueAudioComponentInstance=}44@52^@60"
+ "T{vector<AddressToParameter, std::allocator<AddressToParameter>>=^{AddressToParameter}^{AddressToParameter}{?=^{AddressToParameter}}},N,V_addrToParamIndex"
+ "T{vector<BusPropertyObserver, std::allocator<BusPropertyObserver>>=^{BusPropertyObserver}^{BusPropertyObserver}{?=^{BusPropertyObserver}}},N,V_observers"
+ "error in parsing parseParametricRadiationPattern"
+ "v40@0:8{vector<AddressToParameter, std::allocator<AddressToParameter>>=^{AddressToParameter}^{AddressToParameter}{?=^{AddressToParameter}}}16"
+ "v40@0:8{vector<BusPropertyObserver, std::allocator<BusPropertyObserver>>=^{BusPropertyObserver}^{BusPropertyObserver}{?=^{BusPropertyObserver}}}16"
+ "{AudioComponentVector=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}\"mSorted\"B}"
+ "{AudioComponentVector=^v^v{?=^v}B}20@0:8B16"
+ "{AudioComponentVector=^v^v{?=^v}B}24@0:8@16"
+ "{KVOAggregator=\"mRecords\"{vector<KVOAggregator::Record, std::allocator<KVOAggregator::Record>>=\"__begin_\"^{Record}\"__end_\"^{Record}\"\"{?=\"__cap_\"^{Record}}}}"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"\"{?=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"
+ "{map<unsigned int, AUProcessingBlock, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, AUProcessingBlock>>>=\"__tree_\"{__tree<std::__value_type<unsigned int, AUProcessingBlock>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, AUProcessingBlock>, std::less<unsigned int>>, std::allocator<std::__value_type<unsigned int, AUProcessingBlock>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{map<unsigned int, RemoteAUHandleInfo, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, RemoteAUHandleInfo>>>=\"__tree_\"{__tree<std::__value_type<unsigned int, RemoteAUHandleInfo>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, RemoteAUHandleInfo>, std::less<unsigned int>>, std::allocator<std::__value_type<unsigned int, RemoteAUHandleInfo>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{unique_ptr<AUAudioUnitV2Bridge_Renderer, std::default_delete<AUAudioUnitV2Bridge_Renderer>>=\"\"{?=\"__ptr_\"^{AUAudioUnitV2Bridge_Renderer}}}"
+ "{unique_ptr<AUHostingServiceClient, std::default_delete<AUHostingServiceClient>>=\"\"{?=\"__ptr_\"^{AUHostingServiceClient}}}"
+ "{unique_ptr<AUProcAndUserData, std::default_delete<AUProcAndUserData>>=\"\"{?=\"__ptr_\"^{AUProcAndUserData}}}"
+ "{unique_ptr<TestAUProcessingBlock, std::default_delete<TestAUProcessingBlock>>=\"\"{?=\"__ptr_\"^{TestAUProcessingBlock}}}"
+ "{unique_ptr<XOSTransactor, std::default_delete<XOSTransactor>>=\"\"{?=\"__ptr_\"^{XOSTransactor}}}"
+ "{unique_ptr<caulk::mach::unfair_recursive_lock, std::default_delete<caulk::mach::unfair_recursive_lock>>=\"\"{?=\"__ptr_\"^{unfair_recursive_lock}}}"
+ "{unordered_map<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking)), std::hash<long>, std::equal_to<long>, std::allocator<std::pair<const long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>>>=\"__table_\"{__hash_table<std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>, std::__unordered_map_hasher<long, std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>, std::hash<long>, std::equal_to<long>>, std::__unordered_map_equal<long, std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>, std::equal_to<long>, std::hash<long>>, std::allocator<std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{vector<AUAudioUnit_XPC_PropListener, std::allocator<AUAudioUnit_XPC_PropListener>>=\"__begin_\"^{AUAudioUnit_XPC_PropListener}\"__end_\"^{AUAudioUnit_XPC_PropListener}\"\"{?=\"__cap_\"^{AUAudioUnit_XPC_PropListener}}}"
+ "{vector<AURemoteMessageChannel *, std::allocator<AURemoteMessageChannel *>>=\"__begin_\"^@\"__end_\"^@\"\"{?=\"__cap_\"^@}}"
+ "{vector<AddressToParameter, std::allocator<AddressToParameter>>=\"__begin_\"^{AddressToParameter}\"__end_\"^{AddressToParameter}\"\"{?=\"__cap_\"^{AddressToParameter}}}"
+ "{vector<AddressToParameter, std::allocator<AddressToParameter>>=^{AddressToParameter}^{AddressToParameter}{?=^{AddressToParameter}}}16@0:8"
+ "{vector<BusPropertyObserver, std::allocator<BusPropertyObserver>>=\"__begin_\"^{BusPropertyObserver}\"__end_\"^{BusPropertyObserver}\"\"{?=\"__cap_\"^{BusPropertyObserver}}}"
+ "{vector<BusPropertyObserver, std::allocator<BusPropertyObserver>>=^{BusPropertyObserver}^{BusPropertyObserver}{?=^{BusPropertyObserver}}}16@0:8"
+ "{vector<NSObject<OS_dispatch_semaphore> *, std::allocator<NSObject<OS_dispatch_semaphore> *>>=\"__begin_\"^@\"__end_\"^@\"\"{?=\"__cap_\"^@}}"
+ "{vector<NewServerListener, std::allocator<NewServerListener>>=\"__begin_\"^{NewServerListener}\"__end_\"^{NewServerListener}\"\"{?=\"__cap_\"^{NewServerListener}}}"
+ "{vector<PropertyListener, std::allocator<PropertyListener>>=\"__begin_\"^{PropertyListener}\"__end_\"^{PropertyListener}\"\"{?=\"__cap_\"^{PropertyListener}}}"
- "@68@0:8{unique_ptr<AUHostingServiceClient, std::default_delete<AUHostingServiceClient>>=^{AUHostingServiceClient}}16{AudioComponentDescription=IIIII}24^{OpaqueAudioComponentInstance=}44@52^@60"
- "T{vector<AddressToParameter, std::allocator<AddressToParameter>>=^{AddressToParameter}^{AddressToParameter}^{AddressToParameter}},N,V_addrToParamIndex"
- "T{vector<BusPropertyObserver, std::allocator<BusPropertyObserver>>=^{BusPropertyObserver}^{BusPropertyObserver}^{BusPropertyObserver}},N,V_observers"
- "v40@0:8{vector<AddressToParameter, std::allocator<AddressToParameter>>=^{AddressToParameter}^{AddressToParameter}^{AddressToParameter}}16"
- "v40@0:8{vector<BusPropertyObserver, std::allocator<BusPropertyObserver>>=^{BusPropertyObserver}^{BusPropertyObserver}^{BusPropertyObserver}}16"
- "{AudioComponentVector=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v\"mSorted\"B}"
- "{AudioComponentVector=^v^v^vB}20@0:8B16"
- "{AudioComponentVector=^v^v^vB}24@0:8@16"
- "{KVOAggregator=\"mRecords\"{vector<KVOAggregator::Record, std::allocator<KVOAggregator::Record>>=\"__begin_\"^{Record}\"__end_\"^{Record}\"__cap_\"^{Record}}}"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}"
- "{map<unsigned int, AUProcessingBlock, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, AUProcessingBlock>>>=\"__tree_\"{__tree<std::__value_type<unsigned int, AUProcessingBlock>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, AUProcessingBlock>, std::less<unsigned int>>, std::allocator<std::__value_type<unsigned int, AUProcessingBlock>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{map<unsigned int, RemoteAUHandleInfo, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, RemoteAUHandleInfo>>>=\"__tree_\"{__tree<std::__value_type<unsigned int, RemoteAUHandleInfo>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, RemoteAUHandleInfo>, std::less<unsigned int>>, std::allocator<std::__value_type<unsigned int, RemoteAUHandleInfo>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{unique_ptr<AUAudioUnitV2Bridge_Renderer, std::default_delete<AUAudioUnitV2Bridge_Renderer>>=\"__ptr_\"^{AUAudioUnitV2Bridge_Renderer}}"
- "{unique_ptr<AUHostingServiceClient, std::default_delete<AUHostingServiceClient>>=\"__ptr_\"^{AUHostingServiceClient}}"
- "{unique_ptr<AUProcAndUserData, std::default_delete<AUProcAndUserData>>=\"__ptr_\"^{AUProcAndUserData}}"
- "{unique_ptr<TestAUProcessingBlock, std::default_delete<TestAUProcessingBlock>>=\"__ptr_\"^{TestAUProcessingBlock}}"
- "{unique_ptr<XOSTransactor, std::default_delete<XOSTransactor>>=\"__ptr_\"^{XOSTransactor}}"
- "{unique_ptr<caulk::mach::unfair_recursive_lock, std::default_delete<caulk::mach::unfair_recursive_lock>>=\"__ptr_\"^{unfair_recursive_lock}}"
- "{unordered_map<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking)), std::hash<long>, std::equal_to<long>, std::allocator<std::pair<const long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>>>=\"__table_\"{__hash_table<std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>, std::__unordered_map_hasher<long, std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>, std::hash<long>, std::equal_to<long>>, std::__unordered_map_equal<long, std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>, std::equal_to<long>, std::hash<long>>, std::allocator<std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<long, void (^)(unsigned int, const AudioTimeStamp *, unsigned int, long) __attribute__((nonblocking))>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{vector<AUAudioUnit_XPC_PropListener, std::allocator<AUAudioUnit_XPC_PropListener>>=\"__begin_\"^{AUAudioUnit_XPC_PropListener}\"__end_\"^{AUAudioUnit_XPC_PropListener}\"__cap_\"^{AUAudioUnit_XPC_PropListener}}"
- "{vector<AURemoteMessageChannel *, std::allocator<AURemoteMessageChannel *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}"
- "{vector<AddressToParameter, std::allocator<AddressToParameter>>=\"__begin_\"^{AddressToParameter}\"__end_\"^{AddressToParameter}\"__cap_\"^{AddressToParameter}}"
- "{vector<AddressToParameter, std::allocator<AddressToParameter>>=^{AddressToParameter}^{AddressToParameter}^{AddressToParameter}}16@0:8"
- "{vector<BusPropertyObserver, std::allocator<BusPropertyObserver>>=\"__begin_\"^{BusPropertyObserver}\"__end_\"^{BusPropertyObserver}\"__cap_\"^{BusPropertyObserver}}"
- "{vector<BusPropertyObserver, std::allocator<BusPropertyObserver>>=^{BusPropertyObserver}^{BusPropertyObserver}^{BusPropertyObserver}}16@0:8"
- "{vector<NSObject<OS_dispatch_semaphore> *, std::allocator<NSObject<OS_dispatch_semaphore> *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}"
- "{vector<NewServerListener, std::allocator<NewServerListener>>=\"__begin_\"^{NewServerListener}\"__end_\"^{NewServerListener}\"__cap_\"^{NewServerListener}}"
- "{vector<PropertyListener, std::allocator<PropertyListener>>=\"__begin_\"^{PropertyListener}\"__end_\"^{PropertyListener}\"__cap_\"^{PropertyListener}}"

```
