## AudioToolboxCore

> `/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`

```diff

 1638.104.3.0.0
-  __TEXT.__text: 0x3057d0
-  __TEXT.__realtime: 0x38e00
+  __TEXT.__text: 0x305a28
+  __TEXT.__realtime: 0x3910c
   __TEXT.__objc_methlist: 0x3c94
   __TEXT.__const: 0x2462a
   __TEXT.__dlopen_cstrs: 0x50a
-  __TEXT.__gcc_except_tab: 0x26da4
+  __TEXT.__gcc_except_tab: 0x26db4
   __TEXT.__cstring: 0x212ea
   __TEXT.__oslogstring: 0x1563e
   __TEXT.__dof_AudioTool: 0x4f1

   __TEXT.__dof_AudioConv: 0x129e
   __TEXT.__dof_AUHostin0: 0x4a9
   __TEXT.__dof_IPCAudioU: 0x582
-  __TEXT.__unwind_info: 0xe600
+  __TEXT.__unwind_info: 0xe608
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
Functions:
~ _AudioFormatGetProperty : 14624 -> 14636
~ _AudioFormatGetPropertyInfo : 6832 -> 6836
~ __ZN5caulk10concurrent25guarded_lookup_hash_tableIjPN2CA12OpaqueObject4RootELNS0_33guarded_lookup_hash_table_optionsE0ENS3_12_GLOBAL__N_124OpaqueObjectIdentityHashEE3addEjS5_ : 264 -> 268
~ __ZN4acv217ConverterRegistry22FindFactoryByFormatIDsEjjNSt3__14spanIK21AudioClassDescriptionLm18446744073709551615EEE : 860 -> 864
~ __ZN20AudioComponentVector12insertSortedENSt3__111__wrap_iterIPNS0_10shared_ptrI11APComponentEEEERKS4_ : 716 -> 720
~ __ZN5caulk10concurrent25guarded_lookup_hash_tableIjPN2CA12OpaqueObject4RootELNS0_33guarded_lookup_hash_table_optionsE0ENS3_12_GLOBAL__N_124OpaqueObjectIdentityHashEE6rehashEj : 344 -> 348
~ __ZNSt3__16vectorIPN8DSPGraph3BoxENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_ : 184 -> 176
~ __ZN12CAFAudioFile20PacketToRollDistanceEP34AudioPacketRollDistanceTranslation : 548 -> 552
~ +[AVHapticEvent eventWithEventType:time:parameters:count:duration:] : 116 -> 120
~ __ZN2CA12OpaqueObject4Root10InvalidateEv : 444 -> 448
~ __ZN12ExtAudioFile19GetExistingFileInfoEj : 2252 -> 2256
~ __ZN12CAFAudioFile12WritePacketsEhjPK28AudioStreamPacketDescriptionxPjPKv : 1464 -> 1468
~ __ZN8DSPGraph5AUBox10initializeEv : 1260 -> 1268
~ __ZN8DSPGraph3Box10initializeEv : 3184 -> 3188
~ __ZN8DSPGraph3Box18initializeAnalysisEv : 2332 -> 2328
~ __ZN24AudioConverterXPC_Server37instantiateSpecificAndFetchPropertiesE27AudioStreamBasicDescriptionS0_NSt3__14spanIK21AudioClassDescriptionLm18446744073709551615EEE : 968 -> 960
~ __ZNSt3__16vectorIN2CA17StreamDescriptionENS_9allocatorIS2_EEE6resizeEm : 356 -> 360
~ __ZN8DSPGraph12Preprocessor10preprocessERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb : 12952 -> 12964
~ __ZN8DSPGraph3BoxC2Ejj : 952 -> 956
~ __ZN8DSPGraph11Interpreter11parseFormatERPKcRNS_18FormatAndBlockSizeE : 2928 -> 2948
~ __ZN8DSPGraph5Graph16setPropertyStripEPK14__CFDictionaryPK10__CFString : 14944 -> 14948
~ __ZN12CAFAudioFile12AddUserChunkEjjPKv : 940 -> 948
~ __ZNSt3__16vectorI11Chunk64InfoNS_9allocatorIS1_EEE6insertENS_11__wrap_iterIPKS1_EERS6_ : 692 -> 696
~ __ZN5auoop15WorkgroupMirror6updateERKN10applesauce3xpc4dictE : 2400 -> 2408
~ __ZN8DSPGraph12Preprocessor3defERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_ : 488 -> 504
~ __ZNSt3__15dequeINS_10unique_ptrIN8DSPGraph5MacroENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__add_front_capacityEv : 1272 -> 1280
~ __ZNK8DSPGraph12Preprocessor4findERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 248 -> 260
~ __ZN8DSPGraph14StringSubMacro5applyEPNS_12PreprocessorERKNSt3__16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA_EEEE : 1036 -> 1048
~ __ZNK4APAC23MetadataBitStreamPacker20packGroupDynamicDataERKNS_8Metadata16GroupDynamicDataERN2AT16TBitstreamWriterIjEE : 252 -> 256
~ __ZNK4APAC23MetadataBitStreamPacker16packGlobalConfigERKNS_8Metadata12GlobalConfigERN2AT16TBitstreamWriterIjEE : 1148 -> 1152
~ __ZNSt3__15dequeIhNS_9allocatorIhEEE9push_backEOh : 1220 -> 1232
~ __ZNSt3__114__split_bufferIPhNS_9allocatorIS1_EEE12emplace_backIJRS1_EEEvDpOT_ : 248 -> 252
~ __ZNSt3__16vectorItNS_9allocatorItEEE24__emplace_back_slow_pathIJRKtEEEPtDpOT_ : 180 -> 172
~ _loudnessMeasurementGenerateBlocks : 1240 -> 1244
~ __ZN10applesauce2CF7details12parse_objectIN8minijson20const_buffer_contextEEENS0_7TypeRefERT_ : 2340 -> 2344
~ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJbEEEPS3_DpOT_ : 224 -> 220
~ __ZN8minijson6detail12parse_doubleEPKc : 232 -> 236
~ __ZN21AudioMetadataTimeline8addEventENSt3__110shared_ptrI27AudioMetadataFormatExtendedEEd : 36304 -> 36500
~ __ZNKSt3__116__deque_iteratorINS_10shared_ptrIN21AudioMetadataTimeline4NodeI26AudioMetadataChannelFormatNS3_I23AudioMetadataPackFormatNS3_I19AudioMetadataObjectNS3_I20AudioMetadataContentNS3_I22AudioMetadataProgrammeNS3_I27AudioMetadataFormatExtendedDnEEEEEEEEEEEEEEPSG_RSG_PSH_lLl256EEplB9foe220106El : 76 -> 80
~ __ZN21AudioMetadataTimeline28retrieveMetadataForTimeframeERKdS1_ : 5992 -> 6040
~ __ZNSt3__15dequeINS_10shared_ptrIN21AudioMetadataTimeline4NodeI26AudioMetadataChannelFormatNS3_I23AudioMetadataPackFormatNS3_I19AudioMetadataObjectNS3_I20AudioMetadataContentNS3_I22AudioMetadataProgrammeNS3_I27AudioMetadataFormatExtendedDnEEEEEEEEEEEEEENS_9allocatorISG_EEED2B9foe220106Ev : 344 -> 356
~ __ZNSt3__114__split_bufferIPNS_10shared_ptrIN21AudioMetadataTimeline4NodeI26AudioMetadataChannelFormatNS3_I23AudioMetadataPackFormatNS3_I19AudioMetadataObjectNS3_I20AudioMetadataContentNS3_I22AudioMetadataProgrammeNS3_I27AudioMetadataFormatExtendedDnEEEEEEEEEEEEEERNS_9allocatorISH_EEE12emplace_backIJSH_EEEvDpOT_ : 248 -> 252
~ __ZNSt3__114__split_bufferIPNS_10shared_ptrIN21AudioMetadataTimeline4NodeI26AudioMetadataChannelFormatNS3_I23AudioMetadataPackFormatNS3_I19AudioMetadataObjectNS3_I20AudioMetadataContentNS3_I22AudioMetadataProgrammeNS3_I27AudioMetadataFormatExtendedDnEEEEEEEEEEEEEERNS_9allocatorISH_EEE12emplace_backIJRSH_EEEvDpOT_ : 252 -> 256
~ __ZNKSt3__116__deque_iteratorINS_10shared_ptrIN21AudioMetadataTimeline4NodeI26AudioMetadataChannelFormatNS3_I23AudioMetadataPackFormatNS3_I19AudioMetadataObjectNS3_I20AudioMetadataContentNS3_I22AudioMetadataProgrammeNS3_I27AudioMetadataFormatExtendedDnEEEEEEEEEEEEEEPSG_RSG_PSH_lLl256EEmiB9foe220106El : 80 -> 84
~ __ZN2CA10ADMBuilder4Impl22xml_start_element_stubEPvPKhS4_S4_iPS4_iiS5_ : 2828 -> 2836
~ __ZNSt3__114__split_bufferIPN2CA10ADMBuilder4Impl10ADMElementENS_9allocatorIS5_EEE12emplace_backIJRS5_EEEvDpOT_ : 256 -> 260
~ __ZN26BufferedSoundCheckAnalyzer20ReceiveBufferedBlockEPvPKhj : 584 -> 596
~ __ZNSt3__16vectorIyNS_9allocatorIyEEE24__emplace_back_slow_pathIJyEEEPyDpOT_ : 184 -> 176
~ __Z32ConvertEAC3HeaderToEAC3MP4CookiePKvjPhPj : 5792 -> 5796
~ __ZN13KVOAggregator4findEP8NSObjectP8NSStringb : 1152 -> 1156
~ __ZNSt3__16vectorIU8__strongP22AURemoteMessageChannelNS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRU8__strongKS2_EEEPS3_DpOT_ : 288 -> 276
~ __ZN21AudioFileStreamObject13SetFormatListEjPK19AudioFormatListItem : 244 -> 252
~ __ZNSt3__16vectorI19AudioFormatListItemNS_9allocatorIS1_EEE6resizeEm : 356 -> 360
~ __ZN14AMRAudioStream15GeneratePacketsER27AudioFileStreamContinuation : 1200 -> 1204
~ __ZNSt3__16vectorIN8audioipc14ExtendedFormatENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 284 -> 280
~ ____ZN23NotifyDStateDumpManager17registerSubsystemE27CACentralStateDumpSubsystemPK10__CFStringU13block_pointerFvP7__sFILEE_block_invoke : 1032 -> 1036
~ ____ZN18OSStateDumpManager17registerSubsystemE27CACentralStateDumpSubsystemPK10__CFStringU13block_pointerFvP7__sFILEE_block_invoke : 1256 -> 1260
~ __ZNK23AUFlatParameterInfoBlob14ParameterProxy19dependentParametersEv : 64 -> 68
~ __ZNSt3__116__deque_iteratorIN19AUEventListenerBase7MessageEPS2_RS2_PS3_lLl73EEpLB9foe220106El : 176 -> 188
~ __ZN12EC3AudioFile14ParseAudioFileEv : 4972 -> 4992
~ __ZN16TArrayMarshallerIfE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN16TArrayMarshallerIjE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE24__emplace_back_slow_pathIJjEEEPjDpOT_ : 184 -> 176
~ __ZN25MP413KVoiceSpecificConfig11DeserializeER16TBitstreamReaderIjE : 3412 -> 3416
~ __ZN3HOA13createDecoderERKNSt3__16vectorIfNS0_9allocatorIfEEEES6_NS_16DecoderAlgorithmENS_16DecoderWeightingE : 7688 -> 7792
~ __ZN12AMRAudioFile12WritePacketsEhjPK28AudioStreamPacketDescriptionxPjPKv : 1108 -> 1116
~ __ZN5boost9container8flat_mapINSt3__15tupleIJiidbEEENS2_8weak_ptrI14RamstadKernelDEENS2_4lessIS4_EEvE14priv_subscriptERKS4_ : 1288 -> 1284
~ __ZN5boost9container8flat_mapINSt3__15tupleIJiidbEEENS2_8weak_ptrI13RamstadKernelEENS2_4lessIS4_EEvE14priv_subscriptERKS4_ : 1288 -> 1284
~ _AudioFileStreamParseBytes : 632 -> 636
~ __ZN4APAC12MetadataJSONERKNS_8MetadataEi : 37428 -> 37476
~ __ZN8nlohmann6detail10serializerINS_10basic_jsonINSt3__13mapENS3_6vectorENS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEbxydS9_NS_14adl_serializerENS5_IhNS9_IhEEEEEEE4dumpERKSF_bbjj : 7084 -> 7088
~ __ZN15ADTSAudioStream15GeneratePacketsER27AudioFileStreamContinuation : 3100 -> 3104
~ __ZN4VBAP10initializeERKNSt3__16vectorIfNS0_9allocatorIfEEEES6_RKNS1_IiNS2_IiEEEERKNS1_INS0_4listIiS7_EENS2_ISC_EEEE : 11348 -> 11264
~ __ZN4VBAP21delaunayTriangulationERKNSt3__16vectorIfNS0_9allocatorIfEEEERKNS1_IiNS2_IiEEEERKNS1_INS0_4listIiS7_EENS2_ISC_EEEE : 16456 -> 16484
~ __ZN4VBAP35calculateVirtualLoudspeakersPolygonERKNSt3__16vectorIfNS0_9allocatorIfEEEERNS1_IS4_NS2_IS4_EEEERNS1_INS1_IjNS2_IjEEEENS2_ISB_EEEE : 5148 -> 5156
~ __ZN14EC3AudioStream13ParseOneCycleEjPKhRjS2_RS1_ : 2872 -> 2880
~ __ZN14DialogueAnchor24AADialogueAnchorAnalyzer9PushAudioEjPK15AudioBufferList : 2476 -> 2480
~ __ZNSt3__110__function6__funcIZN20AudioComponentVector20no_extensions_exceptESt16initializer_listI25AudioComponentDescriptionEE3$_0FbR11APComponentEEclES8_ : 120 -> 116
~ __ZlsR12CASerializerRKPK10__CFString : 204 -> 208
~ __ZN16TArrayMarshallerI29AudioUnitFrequencyResponseBinE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN16TArrayMarshallerI13AUChannelInfoE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN16TArrayMarshallerI19AudioUnitMeterValueE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZNSt3__16vectorI8AUPBUnitNS_9allocatorIS1_EEE6insertENS_11__wrap_iterIPKS1_EERS6_ : 692 -> 696
~ __ZN2CA15extractMetadataER23AudioMetadataMemoryPoolRKNS_3ADME : 17288 -> 17316
~ ___41-[AUAudioUnit scheduleMIDIEventListBlock]_block_invoke_2 : 3440 -> 3444
~ -[AUAudioUnit allocateRenderResourcesAndReturnError:] : 576 -> 580
~ -[AUAudioUnit internalDeallocateRenderResources] : 672 -> 676
~ __ZNSt3__16vectorI24AUExtendedParameterEventN5caulk12rt_allocatorIS1_EEE24__emplace_back_slow_pathIJRS1_EEEPS1_DpOT_ : 308 -> 316
~ __ZN5caulk10concurrent25guarded_lookup_hash_tableIPviLNS0_33guarded_lookup_hash_table_optionsE2ENS0_30guarded_lookup_default_hash_fnIS2_EEE6rehashEj : 300 -> 304
~ __ZNSt3__16vectorI18AddressToParameterNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_ : 308 -> 296
~ __ZZNSt3__16vectorI24ParameterAutomationEventNS_9allocatorIS1_EEE12emplace_backIJRyS6_RfR30AUParameterAutomationEventTypeS6_RKPvEEERS1_DpOT_ENKUlvE0_clEv : 320 -> 336
~ __ZN15ChunkyAudioFile12AddUserChunkEjjPKv : 1084 -> 1088
~ __ZNSt3__16vectorI11ChunkInfo64NS_9allocatorIS1_EEE6insertENS_11__wrap_iterIPKS1_EERS6_ : 692 -> 696
~ __ZN8DSPGraph7Metrics4stopEj : 576 -> 564
~ __ZN13FLACAudioFile5CloseEv : 1532 -> 1536
~ __ZN13FLACAudioFile12WritePacketsEhjPK28AudioStreamPacketDescriptionxPjPKv : 7080 -> 7132
~ __ZN13FLACAudioFile13GetHeaderSizeExRjb : 1344 -> 1348
~ __Z21FindCanonicalLoudnessRKNSt3__16vectorI18ISOLoudnessInfoBoxNS_9allocatorIS1_EEEER15ISOLoudnessInfo : 1104 -> 1152
~ __ZN4acv221ChannelMixerConverterC2ERKNS_14StreamDescPairERKNS_17ChannelLayoutPairE : 1208 -> 1216
~ __ZNSt3__15dequeINS_10unique_ptrIN8DSPGraph5MacroENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEED2B9foe220106Ev : 380 -> 384
~ -[AUAudioUnitV2Bridge _createParameterTree] : 3776 -> 3768
~ __ZN33MP4BoxParser_SampleToGroupCompact21GetSampleToGroupTableERNSt3__16vectorI18SampleToGroupEntryNS0_9allocatorIS2_EEEE : 1752 -> 1748
~ __ZN8DSPGraph12Preprocessor5undefEPKNS_5MacroE : 1340 -> 1360
~ __ZNKSt3__116__deque_iteratorINS_10unique_ptrIN8DSPGraph5MacroENS_14default_deleteIS3_EEEEPS6_RS6_PS7_lLl512EEplB9foe220106El : 84 -> 80
~ __ZN12CAFAudioFile24ScanForIndependentPacketEN9AudioFile24AudioPacketScanDirectionEP33AudioIndependentPacketTranslation : 836 -> 840
~ __ZN14OggAudioStream13ParseOggPagesER27AudioFileStreamContinuationMS_FbRKN3Ogg10PageHeaderEEMS_FbjyPKhjP28AudioStreamPacketDescriptionEMS_FbvE : 5628 -> 5636
~ __Z39LoudnessInfoDictionaryForISOLoudnessBoxPK8__CFDataRPK14__CFDictionary : 4636 -> 4516
~ __ZN4APAC18MetadataConfigJSONERKNS_8Metadata14MetadataConfigE : 15212 -> 15084
~ __ZN8DSPGraph8IsoGroup9addBeforeEPNS_3BoxES2_ : 652 -> 656
~ __ZN13MPEGAudioFile15SetLoudnessInfoEP14CACFDictionary : 2020 -> 2040
~ __ZN5caulk10concurrent25guarded_lookup_hash_tableImNS_4mach20os_workgroup_managedELNS0_33guarded_lookup_hash_table_optionsE0ENS0_30guarded_lookup_default_hash_fnImEEE6rehashEj : 300 -> 304
~ __ZN16TArrayMarshallerIiE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN16TArrayMarshallerIyE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN16TArrayMarshallerI15AudioValueRangeE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN16TArrayMarshallerI19AudioFormatListItemE11DeserializeER14CADeserializerRPvRj : 188 -> 192
~ __ZN16TArrayMarshallerI27AudioStreamBasicDescriptionE11DeserializeER14CADeserializerRPvRj : 188 -> 192
~ __ZN16TArrayMarshallerI31AudioStreamPacketDependencyInfoE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN16TArrayMarshallerI16ProfileLevelInfoE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN16TArrayMarshallerI10OriginInfoE11DeserializeER14CADeserializerRPvRj : 188 -> 192
~ __ZN16TArrayMarshallerI20SplicingRequirementsE11DeserializeER14CADeserializerRPvRj : 160 -> 164
~ __ZN35MP4BoxParser_SampleToGroupRunLength21GetSampleToGroupTableERNSt3__16vectorI18SampleToGroupEntryNS0_9allocatorIS2_EEEE : 1036 -> 1040
~ __ZNSt3__16vectorIN8DSPGraph9InputPortENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJPNS1_3BoxERjEEEPS2_DpOT_ : 312 -> 308
~ __ZN15FLACAudioStream20ParseFLACFrameHeaderERN2AT16TBitstreamReaderIjEEbRjR27AudioStreamBasicDescriptionS4_Pj : 3244 -> 3248
~ __ZNSt3__16vectorI11ChunkSize64NS_9allocatorIS1_EEE6resizeEm : 332 -> 336
~ __ZN15LOASAudioStream15GeneratePacketsER27AudioFileStreamContinuation : 3456 -> 3460
~ __Z9to_stringRK15AudioBufferListmPK27AudioStreamBasicDescriptionPKcb : 988 -> 980
~ __ZN13LOASAudioFile40UpdateMagicCookieAndAudioSpecificConfigsEPKvj : 1284 -> 1288
~ __ZN13LOASAudioFile31StoreAudioSpecificConfigToWriteEPhj : 216 -> 220
~ ____ZN12APMIDIRouter17handleSetPropertyEPvRK23AudioUnitPluginDispatchjjjPKvj_block_invoke_2 : 5276 -> 5192
~ __ZN4APAC23MetadataBitStreamParser21parseGroupDynamicDataERNS_8Metadata16GroupDynamicDataERN2AT16TBitstreamReaderIjEE : 552 -> 556
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE18__insert_with_sizeB9foe220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPKjEES9_EENS6_IPjEES9_T0_T1_l : 560 -> 576
~ __ZN17AudioConverterOOPC2EPK27AudioStreamBasicDescriptionS2_jPK21AudioClassDescriptionjb : 10104 -> 10088
~ __ZN17AudioConverterOOP4Impl19setUpRendererConfigEPK27AudioStreamBasicDescriptionS3_NSt3__16vectorIjNS4_9allocatorIjEEEES8_ : 772 -> 776
~ __ZN16AUParameterCache6createEP28OpaqueAudioComponentInstance : 2784 -> 2768
~ __ZNK12XAUParameter13GetParamProxyEv : 748 -> 752
~ __ZN12MP4AudioFile28WritePacketsWithDependenciesEhjPK28AudioStreamPacketDescriptionPK38AudioStreamPacketDependencyDescriptionxPjPKv : 1492 -> 1484
~ __ZN11CAFormatterC2ERK15AudioBufferList : 344 -> 352
~ _IAAReadTableOfContent : 476 -> 480
~ __ZN10Resampler211PushConvertEPKfS1_PfS2_RjS3_jjj : 1388 -> 1412
~ __ZN10Resampler229ConvertSIMD_SmallIntegerRatioEPfS0_jj : 1236 -> 1248
~ __ZN19TDeinterleaver_SIMDI14PCMSInt32_SIMDE12DeinterleaveEiPKvPPvi : 832 -> 860
~ __ZN8DSPGraph5AUBox7processEj : 1728 -> 1732
~ __ZN19TDeinterleaver_SIMDI14PCMSInt16_SIMDE12DeinterleaveEiPKvPPvi : 868 -> 896
~ __ZN8DSPGraph16ChannelJoinerBox7processEj : 2232 -> 2236
~ __ZN8DSPGraph6SumBox7processEj : 1328 -> 1332
~ _MultiChannelInterleaveFloat32ToNativeLowAlignedInt32_ARM : 720 -> 732
~ __ZN20AUOOPRenderingClient24copyEventsToSharedMemoryEPK13AURenderEventdb : 400 -> 408
~ __ZN17TInterleaver_SIMDI14PCMSInt16_SIMDE10InterleaveEiPPKvPvi : 892 -> 920
~ __ZN17TInterleaver_SIMDI14PCMSInt32_SIMDE10InterleaveEiPPKvPvi : 852 -> 880
~ __ZN17TInterleaver_SIMDI15PCMFloat64_SIMDE10InterleaveEiPPKvPvi : 812 -> 840
~ __ZN19TDeinterleaver_SIMDI15PCMFloat64_SIMDE12DeinterleaveEiPKvPPvi : 808 -> 836
~ __ZN19AUEventListenerBase11SendMessageEPvRK14AudioUnitEventf : 1848 -> 1864
~ __ZN10RamstadSRC11processMonoEPKfPfiiii : 4840 -> 4952
~ __ZN10RamstadSRC13processStereoEPKfS1_PfS2_iiii : 6892 -> 7232
~ __ZN10RamstadSRC12processMultiEPKPKfPKPfiiii : 11128 -> 11076
~ __ZN10Resampler213ConvertLinearEPfS0_jj : 224 -> 236
~ __ZN10Resampler211ConvertSIMDINS_10RampedRateEEEvPfS2_jj : 2568 -> 2580
~ __ZN10Resampler211ConvertSIMDINS_9FixedRateEEEvPfS2_jj : 2224 -> 2236
~ __ZN10Resampler213ConvertScalarINS_10RampedRateEEEvPfS2_jj : 2840 -> 2852
~ __ZN10Resampler213ConvertScalarINS_9FixedRateEEEvPfS2_jj : 2440 -> 2452
~ __ZN10Resampler28Process2EPfS0_ji : 928 -> 940
~ __ZN4acv217RamstadSRCWrapper13ProduceOutputER11ACAudioSpan16ConverterContext : 1512 -> 1532
~ __ZN8DSPGraph6MixBox7processEj : 1604 -> 1608
~ __ZN26AudioConverterRenderClient16setConfigurationEP21RendererConfiguration : 2832 -> 2840
~ __ZN4acv219UV22DitherConverter14ConvertChannelIisEEvPKT_jPT0_jj : 248 -> 256
~ __ZN4acv219UV22DitherConverter14ConvertChannelIffEEvPKT_jPT0_jj : 276 -> 284
~ __ZN21OpaqueAudioInverseFFT23RectangularWindowKernel7ProcessEPKfS2_Pf : 116 -> 120
~ __ZN21OpaqueAudioInverseFFT17MagicWindowKernel7ProcessEPKfS2_Pf : 252 -> 256
```
