## AudioCodecs

> `/System/Library/Components/AudioCodecs.component/Contents/MacOS/AudioCodecs`

```diff

-  __TEXT.__text: 0x61cb04
+  __TEXT.__text: 0x61a694
   __TEXT.__realtime: 0x3c0
   __TEXT.__auth_stubs: 0x1950
   __TEXT.__const: 0x330c98
   __TEXT.__cstring: 0xc64a
-  __TEXT.__gcc_except_tab: 0x13370
-  __TEXT.__oslogstring: 0x1b724
+  __TEXT.__gcc_except_tab: 0x1335c
+  __TEXT.__oslogstring: 0x1b778
   __TEXT.__ustring: 0x20
   __TEXT.__unwind_info: 0x9d70
   __TEXT.__eh_frame: 0x6a0

   - /usr/lib/libc++.1.dylib
   Functions: 9793
   Symbols:   17859
-  CStrings:  4091
+  CStrings:  4092
 
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__got : content changed
~ __DATA.__data : content changed
Functions:
~ __ZN16SBREncodeChannel14CreateSbrFrameEP16SBR_FRAME_RECORDP17SBR_CONFIGURATIONjj : 1936 -> 1912
~ __ZN28ACMP4AACLowComplexityDecoder11GetPropertyEjRjPv : 2340 -> 2312
~ __ZN19ACMP4AACBaseDecoder11GetPropertyEjRjPv : 6020 -> 5988
~ __ZN19ACMP4AACBaseDecoder14SetMagicCookieEPKvj : 1128 -> 1120
~ __ZN19ACMP4AACBaseDecoder23ProduceOutputBufferListEP15AudioBufferListRjP28AudioStreamPacketDescription : 1768 -> 1772
~ __ZN16TBitstreamReaderIjEC2EPKhj : 128 -> 116
~ __ZNSt3__110__list_impIN22DynamicRangeCompressor19DRCExtensionPayload8BandInfoENS_9allocatorIS3_EEE5clearEv : 104 -> 108
~ __ZN13ACUSACDecoder10InitializeEPK27AudioStreamBasicDescriptionS2_PKvj : 2316 -> 2304
~ __ZN13ACUSACDecoder11GetPropertyEjRjPv : 5020 -> 4988
~ __ZNSt3__16vectorI18MP4LoudnessMeasureNS_9allocatorIS1_EEE16__destroy_vectorclB9nqe220106Ev : 152 -> 144
~ __ZN13ACACCFDecoder23ProduceOutputBufferListEP15AudioBufferListRjP28AudioStreamPacketDescription : 6824 -> 6800
~ __ZN13ACACCFDecoder11GetPropertyEjRjPv : 2908 -> 2900
~ __ZNK11ACFLACCodec16ParseMagicCookieEPKvjP31FLAC__StreamMetadata_StreamInfo : 2484 -> 2464
~ __ZN15SACDecorrelator6createEjjjjj : 1844 -> 1740
~ __ZNSt3__16vectorIN15SACDecorrelator11cmplxVectorENS_9allocatorIS2_EEE6resizeEm : 852 -> 728
~ __ZN15SACDecorrelatorD2Ev : 252 -> 240
~ __ZNSt3__16vectorIN15SACDecorrelator11cmplxVectorENS_9allocatorIS2_EEE16__destroy_vectorclB9nqe220106Ev : 152 -> 144
~ __ZN3sbc9sbcConfig11deserializeEPKvj : 668 -> 660
~ __ZN12ACAMREncoder27WriteSpeechDataIF2ToPayloadEjR16TBitstreamWriterIhEPKh : 624 -> 612
~ __ZN3sac6matrix8resizeRCEjj : 292 -> 284
~ __ZNSt3__16vectorIN3sac7elementENS_9allocatorIS2_EEE6resizeEm : 820 -> 688
~ __ZNK3sac6matrix10get1stDataERNS_10matrixDataE : 180 -> 168
~ __ZNK3sac6matrix7getDataEjRNS_10matrixDataE : 196 -> 176
~ __ZNSt3__16vectorIN3sac7elementENS_9allocatorIS2_EEE16__destroy_vectorclB9nqe220106Ev : 152 -> 144
~ __ZN17ACDDPAtmosDecoder10InitializeEPK27AudioStreamBasicDescriptionS2_PKvj : 16364 -> 16320
~ __ZN17ACDDPAtmosDecoder23ProduceOutputBufferListEP15AudioBufferListRjP28AudioStreamPacketDescription : 10436 -> 10400
~ __ZN17ACDDPAtmosDecoder18CopyUDCOutputToABLEjP15AudioBufferList : 308 -> 300
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN17ACDDPAtmosDecoder11GetPropertyEjRjPvE3$_0PjLb0EEEvT1_S8_T0_NS_15iterator_traitsIS8_E15difference_typeEb : 2240 -> 2228
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERZN17ACDDPAtmosDecoder11GetPropertyEjRjPvE3$_0PjEEbT1_S8_T0_ : 652 -> 636
~ __ZN18ACAppleIMA4Decoder20ProduceOutputPacketsEPvRjS1_P28AudioStreamPacketDescription : 896 -> 888
~ _mix16 : 160 -> 136
~ _mix20 : 280 -> 256
~ _mix24 : 664 -> 608
~ _mix32 : 324 -> 280
~ __ZN22ACAppleLosslessDecoder20ProduceOutputPacketsEPvRjS1_P28AudioStreamPacketDescription : 7228 -> 6988
~ __ZN22ACAppleLosslessEncoder10InitializeEPK27AudioStreamBasicDescriptionS2_PKvj : 1708 -> 1688
~ __ZN22ACAppleLosslessEncoder10EncodeMonoEP9BitBufferPvjjj : 1860 -> 1824
~ __ZN22ACAppleLosslessEncoder5ResetEv : 204 -> 184
~ __ZN17APACSpeechDecoder11DeserializeEPKhj : 172 -> 164
~ __ZNSt3__113__stable_sortINS_17_ClassicAlgPolicyERPFbRK27AudioStreamBasicDescriptionS4_ENS_11__wrap_iterIP24CAStreamBasicDescriptionEEEEvT1_SC_T0_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeEl : 768 -> 760
~ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERPFbRK27AudioStreamBasicDescriptionS4_ENS_11__wrap_iterIP24CAStreamBasicDescriptionEEEEvT1_SC_SC_OT0_NS_15iterator_traitsISC_E15difference_typeESH_PNSG_10value_typeEl : 1564 -> 1580
~ __ZNSt3__18valarrayIfEC2ERKS1_ : 136 -> 120
~ __ZN10SBCDecoder6decodeEPKhjRjRNS_15outputDataFrameE : 5648 -> 5640
~ __ZN6mpddrc15UniDrcSelection18getSignalPeakLevelERKNS_12UniDrcHeaderEjjhjPfPb : 1816 -> 1768
~ __ZN6mpddrc15UniDrcSelection19initLoudnessControlERKNS_15UniDrcInterfaceERKNS_12UniDrcHeaderEjihPfS7_ : 4632 -> 4556
~ __ZN13MP4ELDDecoder11DecodeFrameEPKhjR14FrameOutRecord : 15720 -> 15708
~ __ZN21LDSACExtensionPayload11DeserializeER16TBitstreamReaderIjERi15ElementTagAndID : 1184 -> 1172
~ __ZNSt3__16vectorIN6mpddrc10GainParamsENS_9allocatorIS2_EEE6resizeEm : 360 -> 340
~ __ZNSt3__16vectorIN6mpddrc22SplitDrcCharacteristicENS_9allocatorIS2_EEE6resizeEm : 508 -> 488
~ __ZNSt3__16vectorIN6mpddrc20GainModifiersForBandENS_9allocatorIS2_EEE6resizeEm : 392 -> 372
~ __ZN6mpddrc28DrcCoefficientsParametricDrc11DeserializeER16TBitstreamReaderIjEbj : 3372 -> 3344
~ __ZN6mpddrc14EqCoefficients11DeserializeER16TBitstreamReaderIjE : 7324 -> 7304
~ __ZNSt3__16vectorIN6mpddrc21DrcCoefficientsUniDrcENS_9allocatorIS2_EEE6resizeEm : 480 -> 468
~ __ZNSt3__16vectorIN7ac_dict18LoudnessInfoV8DataENS_9allocatorIS2_EEE6resizeEm : 648 -> 636
~ __ZNSt3__16vectorIN6mpddrc18LoudnessInfoSourceENS_9allocatorIS2_EEE6resizeEm : 540 -> 512
~ __ZNK6mpddrc15LoudnessInfoSet16HasValidLoudnessEv : 156 -> 148
~ __ZN6mpddrc12UniDrcConfig5ResetEv : 396 -> 384
~ __ZN6mpddrc12UniDrcHeader11DeserializeER16TBitstreamReaderIjENS_17HeaderPayloadTypeE : 12708 -> 12696
~ __ZN6mpddrc12UniDrcConfigaSERKS0_ : 4972 -> 4924
~ __ZNSt3__16vectorI18MP4LoudnessMeasureNS_9allocatorIS1_EEE16__init_with_sizeB9nqe220106IPS1_S6_EEvT_T0_m : 180 -> 172
~ __ZNSt3__16vectorIN7ac_dict18LoudnessInfoV8DataENS_9allocatorIS2_EEE16__destroy_vectorclB9nqe220106Ev : 128 -> 116
~ __ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc13GainModifiersES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_ : 392 -> 388
~ __ZNKSt3__111__copy_implclB9nqe220106IP15MP4LoudnessInfoS3_S3_Li0EEENS_4pairIT_T1_EES5_T0_S6_ : 612 -> 560
~ __ZNSt3__16vectorI18MP4LoudnessMeasureNS_9allocatorIS1_EEE13__vdeallocateEv : 132 -> 124
~ __ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc20DrcInstructionsBasicES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_ : 148 -> 144
~ __ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc20ParametricDrcGainSetES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_ : 140 -> 136
~ __ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc25ParametricDrcInstructionsES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_ : 180 -> 176
~ __ZNSt3__1eqB9nqe220106IN6mpddrc21DrcCoefficientsUniDrcENS_9allocatorIS2_EEEEbRKNS_6vectorIT_T0_EESA_ : 924 -> 896
~ __ZNSt3__1eqB9nqe220106IN6mpddrc21DrcInstructionsUniDrcENS_9allocatorIS2_EEEEbRKNS_6vectorIT_T0_EESA_ : 732 -> 720
~ __ZNSt3__1eqB9nqe220106IN6mpddrc14EqInstructionsENS_9allocatorIS2_EEEEbRKNS_6vectorIT_T0_EESA_ : 660 -> 596
~ __ZNSt3__1eqB9nqe220106IN6mpddrc10GainParamsENS_9allocatorIS2_EEEEbRKNS_6vectorIT_T0_EESA_ : 240 -> 216
~ __ZNSt3__1eqB9nqe220106IN6mpddrc13GainModifiersENS_9allocatorIS2_EEEEbRKNS_6vectorIT_T0_EESA_ : 368 -> 344
~ __ZNK6mpddrc6LoudEqeqERKS0_ : 956 -> 932
~ __ZNK6mpddrc14EqCoefficientseqERKS0_ : 976 -> 948
~ __ZNSt3__1eqB9nqe220106IN6mpddrc14EqInstructions15TdFilterCascadeENS_9allocatorIS3_EEEEbRKNS_6vectorIT_T0_EESB_ : 224 -> 196
~ __ZNSt3__1eqB9nqe220106INS_6vectorIbNS_9allocatorIbEEEENS2_IS4_EEEEbRKNS1_IT_T0_EESA_ : 184 -> 160
~ __ZNSt3__16vectorIN6mpddrc14LoudnessInfoV8ENS_9allocatorIS2_EEE16__destroy_vectorclB9nqe220106Ev : 128 -> 116
~ __ZNSt3__16vectorIN6mpddrc14LoudnessInfoV8ENS_9allocatorIS2_EEE18__assign_with_sizeB9nqe220106INS_17_ClassicAlgPolicyEPS2_S8_EEvT0_T1_l : 444 -> 420
~ __Z5isp2aPsS_sS_ : 388 -> 384
~ _AdvanceLoopKernel : 8272 -> 8264
~ _AdvanceLoopKernel_Fast : 2640 -> 2632
~ __ZN15UniDrcEncConfig15ConfigUniDrcEncEjjjjjhjRKN6mpddrc15LoudnessInfoSetER24PreLimiterConfigurationsjj : 8824 -> 8808
~ __ZN17ACVoiceAgeDecoder20ProduceOutputPacketsEPvRjS1_P28AudioStreamPacketDescription : 7704 -> 7656
~ __ZN13ACFLACEncoderD2Ev : 508 -> 528
~ __ZN5ausdk9APFactoryI16AudioCodecLookup13ACFLACEncoderE9ConstructEPvP23ComponentInstanceRecord : 1680 -> 1652
~ __ZN7OTTData11DeserializeER16TBitstreamReaderIjERK29MP4SpatialAudioSpecificConfighRNSt3__13mapIN3sac9paramTypeENS6_6vectorINS8_10bsParamXXXENS6_9allocatorISB_EEEENS6_4lessIS9_EENSC_INS6_4pairIKS9_SE_EEEEEE : 1176 -> 1164
~ __ZN6EcData11DeserializeER16TBitstreamReaderIjEhRN3sac10bsParamXXXEjj : 920 -> 908
~ __ZNSt3__16vectorIN3sac10bsParamSetENS_9allocatorIS2_EEE18__assign_with_sizeB9nqe220106INS_17_ClassicAlgPolicyEPS2_S8_EEvT0_T1_l : 444 -> 420
~ _mp3d_BitBufEnsureBits : 416 -> 408
~ __ZN6mpddrc14ShapeFilterSet21resetShapeFilterBlockEv : 176 -> 168
~ __ZNSt3__16vectorIN6mpddrc13LoudnessEqSet15ChannelGroupLeqENS_9allocatorIS3_EEE6resizeEm : 660 -> 628
~ __ZN6mpddrc15UniDrcProcessor10InitializeERKNS_24UserGainModificationInfoERKNS_15UniDrcInterfaceERKNS_12UniDrcHeaderENS_12UniDrcDomainENS_14FeatureProfileE : 21960 -> 21948
~ __ZNSt3__16vectorI23LinkwitzRileyFilterbankNS_9allocatorIS1_EEE6resizeEm : 736 -> 644
~ __ZNK6mpddrc28DynamicRangeControlInterfaceneERKS0_ : 328 -> 300
~ __ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc17DrcFeatureRequestES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_ : 140 -> 136
~ __ZNSt3__113__stable_sortINS_17_ClassicAlgPolicyERZN19ACMP4AACBaseDecoder11GetPropertyEjRjPvE3$_0P27AudioStreamBasicDescriptionEEvT1_S9_T0_NS_15iterator_traitsIS9_E15difference_typeEPNSC_10value_typeEl : 720 -> 684
~ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERZN19ACMP4AACBaseDecoder11GetPropertyEjRjPvE3$_0P27AudioStreamBasicDescriptionEEvT1_S9_S9_OT0_NS_15iterator_traitsIS9_E15difference_typeESE_PNSD_10value_typeEl : 1044 -> 1020
~ __ZNSt3__18__rotateB9nqe220106INS_17_ClassicAlgPolicyEP27AudioStreamBasicDescriptionS3_EENS_4pairIT0_S5_EES5_S5_T1_ : 592 -> 508
~ __ZN19ACMP4AACBaseEncoder11GetPropertyEjRjPv : 6788 -> 6772
~ __ZN19ACMP4AACBaseEncoder14SetMagicCookieEPKvj : 1020 -> 1012
~ __ZNSt3__134__uninitialized_allocator_relocateB9nqe220106INS_9allocatorI18MP4LoudnessMeasureEEPS2_EEvRT_T0_S7_S7_ : 188 -> 152
~ __ZNSt3__16vectorI8DrcQuantNS_9allocatorIS1_EEE18__assign_with_sizeB9nqe220106INS_17_ClassicAlgPolicyEPS1_S7_EEvT0_T1_l : 568 -> 516
~ _analyseNextBlockForScaling : 680 -> 668
~ _analyseCurrentBlockForScaling_LowDelay : 436 -> 424
~ __ZN27MP3DecoderWrapper_SpiritDSP11DecodeFrameEPhiPii : 9168 -> 9016
~ _gsm_decode : 5012 -> 4996
~ _LARp_to_rp : 168 -> 160
~ _createAugmentedVec : 200 -> 196
~ _evo_brw_read : 216 -> 204
~ _iCBSearch : 3452 -> 3380
~ __ZN22APACPassThroughDecoder11DeserializeEPKhj : 172 -> 164
~ __ZN14iLBCDecode20MS17decInterpolateLSFEv : 188 -> 184
~ __ZN14iLBCDecode20MS25decInterpolateLSFModifiedEv : 148 -> 144
~ __ZN15MP4LoudnessInfo11DeserializeER16TBitstreamReaderIjEb : 1352 -> 1328
~ __ZNSt3__16vectorI18MP4LoudnessMeasureNS_9allocatorIS1_EEE6resizeEm : 452 -> 416
~ __ZN22LoudnessInfoDictionary5ParseEPK14__CFDictionary : 1924 -> 1916
~ __ZN15iLBCLPCAnalysis9anaFilterEPfS0_jS0_S0_S0_ : 204 -> 188
~ __ZNSt3__16vectorIN3sac10bsParamSetENS_9allocatorIS2_EEE6resizeEm : 420 -> 408
~ __ZNSt3__16vectorIN13LDMPSEncFrame7XTTDataENS_9allocatorIS2_EEE16__destroy_vectorclB9nqe220106Ev : 128 -> 116
~ __ZN12ACLC3Decoder11GetPropertyEjRjPv : 1144 -> 1136
~ _imdct36 : 536 -> 520
~ __ZN12ACEVSDecoder23ProduceOutputBufferListEP15AudioBufferListRjP28AudioStreamPacketDescription : 6736 -> 6724
~ __ZN31ACMP4AACEnhancedLowDelayDecoder11GetPropertyEjRjPv : 1624 -> 1616
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN28ACDDPAtmosPassThroughDecoder11GetPropertyEjRjPvE3$_0PjLb0EEEvT1_S8_T0_NS_15iterator_traitsIS8_E15difference_typeEb : 2232 -> 2220
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERZN28ACDDPAtmosPassThroughDecoder11GetPropertyEjRjPvE3$_0PjEEbT1_S8_T0_ : 652 -> 636
~ __ZN9SBREncode12codeEnvelopeEPiPK27ModeSBR_FrequencyResolutionP17SBR_CODE_RESOURCES0_iiih : 1032 -> 1024
~ __ZN17APACSpeechEncoder10InitializeER11ACParamList : 3704 -> 3696
~ __ZN17APACSpeechEncoder21EncodeCoreSpeechFrameEPKfPN4apac13SpeechEncoderEj : 7656 -> 7628
~ __ZN17APACSpeechEncoder18SerializePrerollBsER16TBitstreamWriterIjE : 440 -> 432
~ __ZN4apac12ACELPEncoder27AdvanceCodebookSearchNew_4tEPfS1_S1_S1_S1_RKNS_13cbSearchEntryEPt : 5020 -> 5056
~ __ZN13PSEncodeFrame12CreatePSToolEfj : 1456 -> 1428
~ __ZNSt3__16vectorIN7ac_dict19NonLanguageItemDataENS_9allocatorIS2_EEE6resizeEm : 516 -> 484
~ __ZNSt3__16vectorIN7ac_dict24LanguageSpecificItemDataENS_9allocatorIS2_EEE6resizeEm : 576 -> 524
~ __ZNSt3__16vectorIN7ac_dict24LanguageSelectionSetDataENS_9allocatorIS2_EEE6resizeEm : 524 -> 492
~ __ZNSt3__16vectorIN7ac_dict29CompositionSelectionGroupDataENS_9allocatorIS2_EEE6resizeEm : 484 -> 472
~ __ZNSt3__16vectorIN7ac_dict21PresetDescriptionDataENS_9allocatorIS2_EEE6resizeEm : 544 -> 504
~ __ZNSt3__16vectorIN7ac_dict12CategoryDataENS_9allocatorIS2_EEE6resizeEm : 640 -> 596
~ __ZNSt3__16vectorIN7ac_dict21AudioSceneControlData20SceneCompositionDataENS_9allocatorIS3_EEE6resizeEm : 612 -> 600
~ __ZNSt3__16vectorIN7ac_dict12CategoryDataENS_9allocatorIS2_EEE16__destroy_vectorclB9nqe220106Ev : 128 -> 116
~ __ZNSt3__16vectorIN7ac_dict21PresetDescriptionDataENS_9allocatorIS2_EEE16__destroy_vectorclB9nqe220106Ev : 128 -> 116
~ __ZNSt3__16vectorIN7ac_dict29CompositionSelectionGroupDataENS_9allocatorIS2_EEE16__destroy_vectorclB9nqe220106Ev : 128 -> 116
~ __ZNK4apac4stic11CodecConfig10GetNumBitsEv : 332 -> 316
~ __ZNK4apac4stic11CodecConfig9SerializeER16TBitstreamWriterIjE : 1160 -> 1148
~ __ZN4apac4stic11CodecConfig11DeserializeER16TBitstreamReaderIjE : 2716 -> 2708
~ __ZNSt3__16vectorIN4apac9TCEConfigENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 448 -> 408
~ __ZNSt3__16vectorIN4apac9TCEConfigENS_9allocatorIS2_EEE16__destroy_vectorclB9nqe220106Ev : 152 -> 144
~ __ZN22APACChannelPairElement18DeserializeSQFrameER16TBitstreamReaderIjE : 2040 -> 2024
~ __ZNK4apac4spch11CodecConfig10GetNumBitsEv : 152 -> 144
~ __ZNK4apac4spch11CodecConfig9SerializeER16TBitstreamWriterIjE : 284 -> 264
~ __ZN4apac4spch11CodecConfig11DeserializeER16TBitstreamReaderIjE : 360 -> 352
~ __ZN15STICBaseDecoder10InitializeERK11ACParamListN4apac12observer_ptrINS3_10IASCConfigEEE : 5804 -> 5932
~ __ZN15STICBaseDecoder15DecodeAPACFrameER16TBitstreamReaderIjEN4apac9FrameTypeERNSt3__16vectorIPfNS5_9allocatorIS7_EEEE : 2092 -> 2120
~ __ZN17TransientDetector10InitializeEv : 1536 -> 1492
~ __ZN17TransientDetector7ProcessERKN4apac16InputAudioBufferERKNSt3__16vectorINS4_10unique_ptrINS0_11ChanElementENS4_14default_deleteIS7_EEEENS4_9allocatorISA_EEEERNS5_INS0_11ChannelInfoENSB_ISG_EEEE : 2484 -> 2488
~ __ZN17TransientDetectorD2Ev : 160 -> 148
~ __ZN3pam10ResultData10InitializeEPKN4apac7EncDataERKNS_15SMRTuningParamsERKNS1_12observer_ptrINS_13BandwidthInfoEEE : 2292 -> 1960
~ __ZN3pam10ResultDataD2Ev : 288 -> 272
~ __ZN15APACMagicCookie11CompareBitsEPKhmS1_mm : 752 -> 736
~ __ZN4apac3drc11EnergyMeter10InitializeERK11ACParamListjNSt3__15arrayINS1_11MeterConfigELm3EEEjN6mpddrc20LoudnessRendererInfoE : 10932 -> 10860
~ __ZNSt3__16vectorI19SC_SceneCompositionNS_9allocatorIS1_EEE6resizeEm : 2992 -> 2936
~ __ZNSt3__16vectorI18SC_NonLanguageItemNS_9allocatorIS1_EEE6resizeEm : 656 -> 624
~ __ZNSt3__16vectorI20SC_PresetDescriptionNS_9allocatorIS1_EEE6resizeEm : 508 -> 496
~ __ZNSt3__16vectorI23SC_LanguageSpecificItemNS_9allocatorIS1_EEE6resizeEm : 692 -> 592
~ __ZNSt3__16vectorI23SC_LanguageSelectionSetNS_9allocatorIS1_EEE6resizeEm : 664 -> 632
~ __ZNSt3__16vectorI20SC_PresetDescriptionNS_9allocatorIS1_EEE16__destroy_vectorclB9nqe220106Ev : 128 -> 116
~ __ZNSt3__16vectorI23SC_LanguageSelectionSetNS_9allocatorIS1_EEE16__destroy_vectorclB9nqe220106Ev : 128 -> 116
~ __ZN23MixedContentDistributor10InitializeER11ACParamList : 1088 -> 1072
~ __ZN13ContentBuffer10InitializeER11ACParamList : 1800 -> 1788
~ __ZNSt3__16vectorIN4apac12ASCAudioDataENS_9allocatorIS2_EEE16__destroy_vectorclB9nqe220106Ev : 152 -> 144
~ __ZNSt3__134__uninitialized_allocator_relocateB9nqe220106INS_9allocatorIN4apac12ASCAudioDataEEEPS3_EEvRT_T0_S8_S8_ : 308 -> 260
~ __ZN15STICBaseEncoder16SetOptimumConfigERN4apac11ConfigParamE : 1876 -> 1856
~ __ZN15STICBaseEncoder19InitializeASCConfigERN4apac11ConfigParamE : 760 -> 752
~ __ZL21IsFOAplusCenterLayoutRKN2CA13ChannelLayoutE : 200 -> 192
~ __ZNSt3__111basic_regexIcNS_12regex_traitsIcEEE26__parse_bracket_expressionIPKcEET_S7_S7_ : 3276 -> 3260
~ __ZNSt3__111basic_regexIcNS_12regex_traitsIcEEE24__parse_collating_symbolIPKcEET_S7_S7_RNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE : 224 -> 212
~ __ZL26GetAvailableChanLayoutTagsR17ACAPACBaseEncoderRNSt3__16vectorIjNS1_9allocatorIjEEEEb : 364 -> 336
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZL21GetMergedObjectConfigRKN4apac15ASCCodecsConfigERKNS2_13ASCChannelMapERNS2_15ASCChannelRangeERjSB_E3$_0PS9_Lb0EEEvT1_SF_T0_NS_15iterator_traitsISF_E15difference_typeEb : 2660 -> 2648
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERZL21GetMergedObjectConfigRKN4apac15ASCCodecsConfigERKNS2_13ASCChannelMapERNS2_15ASCChannelRangeERjSB_E3$_0PS9_EEbT1_SF_T0_ : 844 -> 828
~ __ZNK4apac3hoa11CodecConfig10GetNumBitsEv : 984 -> 976
~ __ZNK4apac3hoa11CodecConfig9SerializeER16TBitstreamWriterIjE : 2092 -> 2080
~ __ZN4apac3hoa11CodecConfig11DeserializeER16TBitstreamReaderIjE : 4388 -> 4380
~ __ZN14APACObjEncoder19InitializeASCConfigERN4apac11ConfigParamE : 296 -> 288
~ __ZN18APACCoreLBREncoder18EncodeAndAllocBitsEv : 3460 -> 3452
~ __ZNSt3__16vectorIN24CD_AudioSceneControlData20SceneCompositionDataENS_9allocatorIS2_EEE6resizeEm : 592 -> 560
~ __ZNSt3__16vectorIN19SC_SceneComposition11SC_CategoryENS_9allocatorIS2_EEE6resizeEm : 844 -> 812
~ __ZN14SC_AudioScenes6ImportERKN7ac_dict15AudioScenesDataE : 3952 -> 3884
~ __ZN4apac17LoudnessDRCConfig11DeserializeER16TBitstreamReaderIjERK11ACParamListN6mpddrc17HeaderPayloadTypeE : 4896 -> 4840
~ __ZN4apac15AncillaryConfig10InitializeER11ACParamList : 11832 -> 11820
~ __ZN4apac15AncillaryConfig11DeserializeER16TBitstreamReaderIjEjjjb : 13592 -> 13556
~ __ZN4apac3drc16DRCDataGeneratorD2Ev : 932 -> 900
~ __ZNSt3__16vectorIN4apac3drc24GenericSequenceGeneratorENS_9allocatorIS3_EEE16__destroy_vectorclB9nqe220106Ev : 156 -> 148
~ __ZN4apac4chan11CodecConfig10InitializeERKNS_11ConfigParamERKNS_11ChannelDataE : 396 -> 388
~ __ZNK4apac4chan11CodecConfig9SerializeER16TBitstreamWriterIjE : 532 -> 520
~ __ZN4apac4chan11CodecConfig11DeserializeER16TBitstreamReaderIjE : 1252 -> 1244
~ __ZNK4apac4chan11CodecConfig10GetNumBitsEv : 264 -> 248
~ __ZN11HuffmanTreeC2ENSt3__14spanIKN16HOASpatialCommon20HuffmanCodebookEntryELm18446744073709551615EEE : 876 -> 868
~ __ZN7ac_dict19DrcAndSceneSettings5ParseEPKPK14__CFDictionary : 7832 -> 7796
~ __ZN13APACCoreTools10InitializeERKN4apac11ChannelDataE : 2012 -> 1996
~ __ZN14APACHOAEncoder15InitializeToolsERN4apac11ConfigParamE : 7816 -> 7804
~ __ZN19PsychoAcousticModelC2ERKN4apac12observer_ptrIKNS0_7EncDataEEE : 4432 -> 4452
~ __ZN4apac3obj18StaticMetadataBase25ParseByteArraysToMetadataER16TBitstreamReaderIjE : 10300 -> 10160
~ __ZN4apac3obj12MetadataBase13ParseMetadataEPKhj : 14388 -> 14380
~ __ZN4apac3obj20ContributionMetadata13ParseMetadataEPKhj : 904 -> 896
~ __ZNK4apac3obj11CodecConfig10GetNumBitsEv : 152 -> 144
~ __ZNK4apac3obj11CodecConfig9SerializeER16TBitstreamWriterIjE : 300 -> 280
~ __ZN4apac3obj11CodecConfig11DeserializeER16TBitstreamReaderIjE : 468 -> 460
~ __ZN4apac3obj18StaticMetadataBaseD2Ev : 356 -> 352
~ __ZNSt3__16vectorIN14metadata_bsfmt12RendererDataENS_9allocatorIS2_EEE6resizeEm : 480 -> 468
~ __ZN14metadata_bsfmt22HuffmanCodingProcessor8CompressERNSt3__16vectorIhNS1_9allocatorIhEEEER16TBitstreamWriterIjEjb : 620 -> 612
~ __ZN14metadata_bsfmt23LZWCompressionProcessor8CompressERNSt3__16vectorIhNS1_9allocatorIhEEEER16TBitstreamWriterIjEjb : 996 -> 988
~ __ZN14metadata_bsfmt25ArithmeticCodingProcessor8CompressERNSt3__16vectorIhNS1_9allocatorIhEEEER16TBitstreamWriterIjEjb : 2132 -> 2124
~ __ZN14metadata_bsfmt25ArithmeticCodingProcessor10DecompressERNSt3__16vectorIhNS1_9allocatorIhEEEER16TBitstreamReaderIjEj : 3112 -> 3104
~ __ZN13MetadataFrame10InitializeERKNSt3__110unique_ptrI14MetadataConfigNS0_14default_deleteIS2_EEEEPKN4apac16SceneGraphConfigE : 4396 -> 4288
~ __ZN13MetadataFrame23DeserializeUncompressedER16TBitstreamReaderIjEb : 3840 -> 3828
~ __ZN4apac3drc13UniDrcEncoder10InitializeER11ACParamList : 13304 -> 13188
~ __ZN19PsychoAcousticModel7ProcessERN4apac11ChannelDataERKNSt3__16vectorINS3_10unique_ptrINS0_12MDCTChanDataENS3_14default_deleteIS6_EEEENS3_9allocatorIS9_EEEERKNS5_I13APACCoreToolsNS7_ISF_EEEE : 2756 -> 2740
~ __ZN19PsychoAcousticModel19CalculateMDCTEnergyERKN4apac7EncDataERKNS0_11ChannelDataERKNSt3__16vectorINS7_10unique_ptrINS0_12MDCTChanDataENS7_14default_deleteISA_EEEENS7_9allocatorISD_EEEERKNS8_IN17TransientDetector8ChanDataENSE_ISK_EEEE : 640 -> 624
~ __ZN17ACAPACBaseDecoder11GetPropertyEjRjPv : 7580 -> 7532
~ __ZN17ACAPACBaseDecoder11SetPropertyEjjPKv : 18060 -> 18012
~ __ZN17ACAPACBaseDecoder19GetOutputBufferListEP15AudioBufferListRjP28AudioStreamPacketDescription : 1700 -> 1704
~ __ZN17ACAPACBaseDecoder14SetMagicCookieEPKvj : 1184 -> 1176
~ __ZNSt3__113__stable_sortINS_17_ClassicAlgPolicyERPFbRK27AudioStreamBasicDescriptionS4_EPS2_EEvT1_S9_T0_NS_15iterator_traitsIS9_E15difference_typeEPNSC_10value_typeEl : 744 -> 736
~ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERPFbRK27AudioStreamBasicDescriptionS4_EPS2_EEvT1_S9_S9_OT0_NS_15iterator_traitsIS9_E15difference_typeESE_PNSD_10value_typeEl : 1144 -> 1140
~ __ZN4apac12GlobalConfig11DeserializeER16TBitstreamReaderIjE : 5820 -> 5804
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN4apac12GlobalConfig11DeserializeER16TBitstreamReaderIjEE3$_0PjLb0EEEvT1_SA_T0_NS_15iterator_traitsISA_E15difference_typeEb : 2784 -> 2772
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERZN4apac12GlobalConfig11DeserializeER16TBitstreamReaderIjEE3$_0PjEEbT1_SA_T0_ : 792 -> 776
~ __ZN23BinaryMetadataContainer4PushEPKhj : 428 -> 420
~ __ZN9CACStereo7ProcessERN4apac11ChannelDataERNSt3__16vectorINS3_10unique_ptrINS0_12MDCTChanDataENS3_14default_deleteIS6_EEEENS3_9allocatorIS9_EEEERN3pam10ResultDataE : 5748 -> 5708
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIfjEELb0EEEvT1_S8_T0_NS_15iterator_traitsIS8_E15difference_typeEb : 3568 -> 3504
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIfjEEEEbT1_S8_T0_ : 1104 -> 1080
~ __ZNSt3__16vectorI17SequenceOptimizerNS_9allocatorIS1_EEE6resizeEm : 516 -> 504
~ __ZNSt3__16vectorI17SequenceOptimizerNS_9allocatorIS1_EEE16__destroy_vectorclB9nqe220106Ev : 128 -> 116
~ __ZNKSt3__111__copy_implclB9nqe220106IPN4apac3drc10ASCContentES5_S5_Li0EEENS_4pairIT_T1_EES7_T0_S8_ : 128 -> 124
~ __ZN4apac8ISFTools11QuantizeISFEPt : 1172 -> 1180
~ __ZN4apac10LPCodeBook8VQSearchEPKf : 348 -> 344
~ __ZN15APACCoreDecoder11DeserializeEPKhj : 172 -> 164
~ __ZN11APACDecoder11DecodeFrameEPKhjRN4apac14FrameOutRecordE : 1200 -> 1192
~ __ZN22APACAnalysisFilterBank10InitializeEjj : 892 -> 876
~ __ZNK18SC_SceneController16ExportDictionaryERjPv : 4072 -> 4036
~ __ZN18SC_SceneController12ProcessAudioEPKPKfPPfj : 3084 -> 3072
~ __ZN25APACAncillaryFrameEncoder11EncodeFrameEPKfj : 17544 -> 17464
~ __ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc12SceneItemMapES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_ : 132 -> 128
~ __ZN4apac3drc18DynRangeCompressor18AdjustForHostInputEv : 1156 -> 1144
~ __ZNSt3__16vectorI15MP4LoudnessInfoNS_9allocatorIS1_EEE18__insert_with_sizeB9nqe220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPS1_EES9_EES9_NS7_IPKS1_EET0_T1_l : 652 -> 624
~ __ZN14APACASPDecoder11DecodeFrameEPKhjRN4apac14FrameOutRecordE : 2096 -> 2080
~ __ZNK4apac14HuffmanTab030411GetCodeBookEPKijRj : 116 -> 108
~ __ZNK4apac14HuffmanTab050611GetCodeBookEPKijRj : 96 -> 84
~ __ZNK4apac14HuffmanTab05065CountEPKij : 88 -> 80
~ __ZNK4apac14HuffmanTab070811GetCodeBookEPKijRj : 96 -> 84
~ __ZNK4apac14HuffmanTab07085CountEPKij : 88 -> 80
~ __ZNK4apac14HuffmanTab07086EncodeER16TBitstreamWriterIjENS_8CodeBookEPKij : 292 -> 288
~ __ZNK4apac14HuffmanTab091011GetCodeBookEPKijRj : 96 -> 84
~ __ZNK4apac14HuffmanTab09105CountEPKij : 84 -> 76
~ __ZNK4apac14HuffmanTab09106EncodeER16TBitstreamWriterIjENS_8CodeBookEPKij : 300 -> 296
~ __ZNK4apac12HuffmanTab115CountEPKij : 88 -> 80
~ __ZNK4apac15HuffmanTab11ESC11GetCodeBookEPKijRj : 180 -> 168
~ __ZN17ACAPACBaseEncoder11GetPropertyEjRjPv : 8348 -> 8316
~ __ZN17ACAPACBaseEncoder14SetMagicCookieEPKvj : 1256 -> 1248
~ __ZN10LoopKernel10InitializeERKN4apac11ConfigParamE : 2824 -> 2688
~ __ZN10LoopKernel12AllocateBitsERKN4apac7EncDataERKNS0_11ChannelDataERKNSt3__16vectorINS7_10unique_ptrINS0_12MDCTChanDataENS7_14default_deleteISA_EEEENS7_9allocatorISD_EEEERKN3pam10ResultDataERNS0_14BsEncFrameDataE : 9072 -> 9104
~ __ZN7APACTNS11ChannelData15DesignTNSFilterERKN4apac7EncDataENS1_9BlockTypeEPKf : 1828 -> 1784
~ __ZN14APACASPEncoder9SerializeEPvRj : 2216 -> 2192
~ __ZN23APACSynthesisFilterBank10InitializeEjj : 904 -> 888
~ __ZN15APACLRVQDecoder15LrvqDeserializeER16TBitstreamReaderIjEbbRNSt3__16vectorIfNS3_9allocatorIfEEEERN4apac13aligned_arrayIfLm1024EEESC_RNSA_IfLm256EEERNSA_IsLm64EEEPt : 3580 -> 3568
~ __ZNSt3__16vectorIN4apac3drc15LoudnessMonitorENS_9allocatorIS3_EEE6resizeEm : 588 -> 576
~ __ZNSt3__16vectorIN4apac3drc27OfflineDRCSequenceGeneratorENS_9allocatorIS3_EEE6resizeEm : 1928 -> 1900
~ __ZNSt3__16vectorIN4apac3drc24GenericSequenceGeneratorENS_9allocatorIS3_EEE6resizeEm : 1100 -> 1000
~ __ZNSt3__16vectorIN4apac3drc24LevelerSequenceGeneratorENS_9allocatorIS3_EEE6resizeEm : 1816 -> 1696
~ __ZNSt3__16vectorIN4apac3drc24DuckingSequenceGeneratorENS_9allocatorIS3_EEE6resizeEm : 1156 -> 1012
~ __ZNSt3__16vectorIN4apac3drc23FadingSequenceGeneratorENS_9allocatorIS3_EEE6resizeEm : 1056 -> 936
~ __ZN11APACEncoder12SetParameterEiRKNSt3__13anyE : 920 -> 908
~ __ZNSt3__16vectorIN6mpddrc13GainModifiersENS_9allocatorIS2_EEE6resizeEmRKS2_ : 548 -> 512
~ __ZN10AACDecoder11DeserializeEPKhj : 172 -> 164
~ __Z8syn_filtPssS_S_sS_sS_ : 292 -> 284
~ __ZNSt3__16vectorIN6mpddrc17DrcFeatureRequestENS_9allocatorIS2_EEE6resizeEm : 404 -> 376
~ __ZN15MP4AACLDDecoder11DecodeFrameEPKhjR14FrameOutRecord : 1416 -> 1408
~ __ZN19AACSyntacticElement10CreateListERNSt3__16vectorI24InstanceTypeIDAndElementIPS_ENS0_9allocatorIS4_EEEER14InstanceConfigRK18DecoderConfigDescr : 1924 -> 1916
~ __ZN22DynamicRangeCompressor10InitializeER16DRCConfigurationR10AACDecoderjjj : 5252 -> 5196
~ __ZN15AACDRCGenerator10InitializeEjjjjRKNSt3__16vectorI15MP4LoudnessInfoNS0_9allocatorIS2_EEEERK15ITULoudnessInfohhjjjPi : 6316 -> 6308
~ __ZN15AACDRCGenerator22AACDynamicRangeControlERK18AACInputRingBufferjt : 7548 -> 7536
~ __ZN4accf20SpectralAnalysisToolC1Ev : 240 -> 232
~ __ZN4accf18InnovativeCodebook7ProcessEiNSt3__14spanIiLm18446744073709551615EEE : 5684 -> 5636
~ __ZN4accf18InnovativeCodebook9HVecCorr2ENSt3__14spanIfLm18446744073709551615EEES3_S3_h : 416 -> 412
~ __ZN4accf16AcelpDecoderImpl6DecodeENSt3__14spanIfLm18446744073709551615EEES3_S3_RNS_19ACCFBitstreamReaderE : 32448 -> 32356
~ __ZNSt3__118__visit_format_argB9sqe220106IZNS_8__format26__handle_replacement_fieldB9sqe220106IPKcNS_26basic_format_parse_contextIcEENS_20basic_format_contextINS_20back_insert_iteratorINS1_15__output_bufferIcEEEEcEEEET_SD_SD_RT0_RT1_EUlSD_E_SC_EEDcOSD_NS_16basic_format_argISE_EE : 8676 -> 8672
~ __ZNSt3__111__formatter32__write_using_decimal_separatorsB9sqe220106INS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEPccEET_S8_T0_S9_S9_ONS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEET1_NS_13__format_spec23__parsed_specificationsISH_EE : 468 -> 464
~ __ZNSt3__111__formatter29__format_locale_specific_formB9sqe220106INS_20back_insert_iteratorINS_8__format15__output_bufferIcEEEEdcEET_S7_RKNS0_14__float_bufferIT0_EERKNS0_14__float_resultENS_6localeENS_13__format_spec23__parsed_specificationsIT1_EE : 1144 -> 1140
~ __ZN4accf5LpcVQ8QuantizeEssNSt3__14spanIfLm18446744073709551615EEENS2_IsLm18446744073709551615EEEsS3_S4_NS2_IKfLm18446744073709551615EEES6_S3_S3_ : 3204 -> 3172
~ __ZN4accf13LsfAllocationC1ERKNS_7LvqModeE : 604 -> 596
~ __ZN4accf17DecodeMidFrameLsfENSt3__14spanIKfLm18446744073709551615EEES3_sNS1_IfLm18446744073709551615EEEiNS_14AcelpCoderTypeEPsbb : 580 -> 584
~ __ZNSt3__111__introsortINS_15_RangeAlgPolicyERZN4accfL25SortDescendingWithIndicesENS_4spanIfLm18446744073709551615EEENS3_IiLm18446744073709551615EEEE3$_0PiLb0EEEvT1_S9_T0_NS_15iterator_traitsIS9_E15difference_typeEb : 3476 -> 3464
~ __ZNSt3__127__insertion_sort_incompleteB9sqe220106INS_15_RangeAlgPolicyERZN4accfL25SortDescendingWithIndicesENS_4spanIfLm18446744073709551615EEENS3_IiLm18446744073709551615EEEE3$_0PiEEbT1_S9_T0_ : 976 -> 960
~ __ZN4accfL19EncodeLatticeVectorENSt3__14spanIKfLm18446744073709551615EEEi : 792 -> 768
~ __ZN4accf24LinearPredictionAnalysisC1Ev : 344 -> 328
~ __ZN4accf17ACCFEncPreProcess7ProcessENSt3__14spanIKfLm18446744073709551615EEENS2_IfLm18446744073709551615EEES5_iii : 21448 -> 21404
~ __ZN4accf12AcelpEncoder11AcelpEncodeER16TBitstreamWriterIjERKNS_22ACCFEncPreProcessStateENSt3__14spanIKfLm18446744073709551615EEESA_iNS8_IfLm18446744073709551615EEE : 16428 -> 16376
~ __ZNKSt3__122__unordered_map_hasherINS_17basic_string_viewIcNS_11char_traitsIcEEEENS_4pairIKS4_10BNNSTensorEENS_4hashIS4_EENS_8equal_toIS4_EEEclB9sqe220106ERS6_ : 1104 -> 1092
~ __ZN4agvc16BaseModelDecoder11DeserializeENSt3__14spanIKhLm18446744073709551615EEERj : 792 -> 784
~ __Z14ParseAC3HeaderPKvjP27AudioStreamBasicDescriptionPjS3_S3_S3_Pi : 2008 -> 2004
~ __Z18ParseEAC3MP4CookiePKvjPbP27AudioStreamBasicDescriptionPjS3_S4_S4_S4_jS1_S4_ : 1820 -> 1812
~ __ZNK20MP4ELDSpecificConfig14SerializeCountEj : 424 -> 444
~ _Decoder_amr_reset : 924 -> 932
~ _ddp_udc_int_bee_encddfrm : 15820 -> 15828
~ _ddp_udc_int_resolvecompr : 272 -> 240
~ _ddp_udc_int_mainprogram_process : 17244 -> 17260
~ _ddp_udc_int_BED_run : 1540 -> 1536
~ _ddp_udc_int_FED_run : 12916 -> 12860
~ __ddp_udc_int_interpol_mult_UM5 : 592 -> 568
~ _FLAC__add_metadata_block : 2244 -> 2236
~ _FLAC__stream_decoder_new : 708 -> 736
~ _FLAC__stream_decoder_delete : 160 -> 180
~ _FLAC__stream_decoder_finish : 628 -> 648
~ _FLAC__stream_decoder_process_single : 11808 -> 11780
~ _FLAC__stream_encoder_finish : 2444 -> 2408
~ _process_frame_ : 3196 -> 3064
~ _FLAC__stream_encoder_init_stream : 3948 -> 3860
~ _resize_buffers_ : 2856 -> 2816
~ _verify_write_callback_ : 756 -> 724
~ __ZN3lc315Channel_Encoder6EncodeEPKfjPh : 14712 -> 14700
~ __ZN4mdct18AnalysisFilterbank15TimeToFrequencyEPf : 816 -> 812
~ __ZN4ltpf7Encoder13PitchAnalyzer7AnalyzeEPKf : 824 -> 812
~ _silk_LPC_inverse_pred_gain : 736 -> 744
~ _silk_noise_shape_quantizer_del_dec : 4920 -> 4844
~ _silk_Decode : 4464 -> 4540
~ _silk_Encode : 7864 -> 7232
~ _silk_LPC_inverse_pred_gain_FLP : 528 -> 536
~ _nb_encode : 9452 -> 9440
~ _lsp_quant : 204 -> 208
~ _lsp_weight_quant : 228 -> 232
~ __Z21CDKhybridAnalysisInitP18CDK_ANA_HYB_FILTER15CDK_HYBRID_MODEiii : 388 -> 384
~ __ZL12extractBBEnvP17spatialDec_structiiiPfPK23SPATIAL_BS_FRAME_struct : 1004 -> 1028
~ __ZN6MPEG_D4USAC18JointStereoDecoder5ApplyERK8CIcsInfoPfS5_jj : 2332 -> 2308
~ __Z7sbr_decP7SBR_DECPfP15SBR_HEADER_DATAP14SBR_FRAME_DATAP19SBR_PREV_FRAME_DATAijiR7UsacQmfi : 13236 -> 13220
~ _aacDecoder_DecodeFrame : 13408 -> 13376
~ __Z18QmfTransposerApplyP13hbeTransposerPPfS2_S2_S2_ii23KEEP_STATES_SYNCED_MODE : 6332 -> 6292
~ __ZN6MPEG_D4USAC19SpectralDataDecoderD2Ev : 244 -> 228
~ _SpatialDecApplyFrame : 14672 -> 14596
~ __ZN6MPEG_D4USAC18DynRangeCompressor23USACDRCExtensionPayloadC2ERS1_RK16DRCConfigurationjjjjN6mpddrc12UniDrcDomainE : 15220 -> 15164
~ __ZN6MPEG_D4USAC19SpectralDataDecoder10InitializeEjjPK16SamplingRateInfob : 1512 -> 1248
~ __ZN6MPEG_D4USAC19SpectralDataDecoder11DeserializeER16TBitstreamReaderIjERKNS0_7ICSInfoEjb : 236 -> 224
~ __Z24qmfAnalysisFilteringSlotP15QMF_FILTER_BANKPfS1_PKfiS1_ : 844 -> 816
~ __ZN7avq_decL21re8_decode_base_indexEiiPi : 836 -> 828
~ __ZN7lpd_dec10lpdDecoder6DecodeEPfiRj : 2652 -> 2640
~ __ZNSt3__16vectorIN7lpd_dec10lpdDecoderENS_9allocatorIS2_EEE6resizeEm : 636 -> 584
~ __Z23CAacDecoder_DecodeFrameP20AAC_DECODER_INSTANCEjPfii : 20104 -> 20120
~ __ZN7fac_dec10facDecoder10Acelp2MdctER9mdct_t_flPfS3_iiiiPK9FLOAT_SPKiRKDv16_fRN9acelp_dec12acelpDecoderEfbbbN9lpd_enums7lpdModeEi : 2116 -> 2084
~ __ZL32deltaToLinearPcmEnvelopeDecodingP15SBR_HEADER_DATAP14SBR_FRAME_DATAP19SBR_PREV_FRAME_DATA : 464 -> 500
~ __Z3fftiPf : 8128 -> 7844
~ __Z23CDK_QmfDomain_ConfigureP14CDK_QMF_DOMAIN : 3088 -> 3072
~ _isf_decode_cols_for_nx : 472 -> 456
~ _oamdi_set_dimensional_trim_defaults : 176 -> 164
~ _ZNSt3__16vectorI15MP4LoudnessInfoNS_9allocatorIS1_EEE18__insert_with_sizeB9nqe220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPS1_EES9_EES9_NS7_IPKS1_EET0_T1_l.12009 -> _ZNSt3__16vectorI15MP4LoudnessInfoNS_9allocatorIS1_EEE18__insert_with_sizeB9nqe220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPS1_EES9_EES9_NS7_IPKS1_EET0_T1_l.12010 : 652 -> 624
~ _ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc25ParametricDrcInstructionsES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_.12158 -> _ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc25ParametricDrcInstructionsES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_.12159 : 180 -> 176
~ _ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc20ParametricDrcGainSetES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_.12171 -> _ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc20ParametricDrcGainSetES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_.12172 : 140 -> 136
~ _ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc13GainModifiersES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_.12331 -> _ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc13GainModifiersES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_.12332 : 392 -> 388
~ _ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc20DrcInstructionsBasicES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_.12373 -> _ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc20DrcInstructionsBasicES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_.12374 : 148 -> 144
~ _ZNSt3__16vectorI18MP4LoudnessMeasureNS_9allocatorIS1_EEE16__init_with_sizeB9nqe220106IPS1_S6_EEvT_T0_m.12465 -> _ZNSt3__16vectorI18MP4LoudnessMeasureNS_9allocatorIS1_EEE16__init_with_sizeB9nqe220106IPS1_S6_EEvT_T0_m.12466 : 180 -> 172
~ _ZNKSt3__111__copy_implclB9nqe220106IP15MP4LoudnessInfoS3_S3_Li0EEENS_4pairIT_T1_EES5_T0_S6_.12487 -> _ZNKSt3__111__copy_implclB9nqe220106IP15MP4LoudnessInfoS3_S3_Li0EEENS_4pairIT_T1_EES5_T0_S6_.12488 : 612 -> 560
~ _ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc17DrcFeatureRequestES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_.12514 -> _ZNKSt3__111__copy_implclB9nqe220106IPN6mpddrc17DrcFeatureRequestES4_S4_Li0EEENS_4pairIT_T1_EES6_T0_S7_.12515 : 140 -> 136
~ _ZNSt3__16vectorIN6mpddrc17DrcFeatureRequestENS_9allocatorIS2_EEE6resizeEm.12541 -> _ZNSt3__16vectorIN6mpddrc17DrcFeatureRequestENS_9allocatorIS2_EEE6resizeEm.12542 : 404 -> 376
~ _ZN6mpddrc15UniDrcProcessor10InitializeERKNS_24UserGainModificationInfoERKNS_15UniDrcInterfaceERKNS_12UniDrcHeaderENS_12UniDrcDomainENS_14FeatureProfileE.12669 -> _ZN6mpddrc15UniDrcProcessor10InitializeERKNS_24UserGainModificationInfoERKNS_15UniDrcInterfaceERKNS_12UniDrcHeaderENS_12UniDrcDomainENS_14FeatureProfileE.12670 : 20964 -> 20952
~ _ZNSt3__16vectorI23LinkwitzRileyFilterbankNS_9allocatorIS1_EEE6resizeEm.12792 -> _ZNSt3__16vectorI23LinkwitzRileyFilterbankNS_9allocatorIS1_EEE6resizeEm.12793 : 748 -> 732
CStrings:
+ "%25s:%-5d  Error: STIC render layout channel count does not match configured output"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/AACEncoderFactory.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/AACEnhancedLowDelaySBREncoder.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/AACHighEfficiencyEncoder.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/AACHighEfficiencyV2Encoder.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncode.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncodeChannel.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncodeFrame.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncodeFrame.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEldEncoderChannel.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEncode.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEncodeChannel.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEncodeFrame.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/aacencifc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/aux_func.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_aac.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_enc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_fram.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_pam.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/cm_utils.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/cod_chan.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/fifo_buf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/intensity.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/ms_chan.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/ms_stereo.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/pam.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/pam_loopmain.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/paminit.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/pns_tool.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/prconfig.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psy_chan.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psy_conf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psymain.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psyout.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psyparam.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/scaling.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/sw_cont.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/thr_chan.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/tns_enc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/toolmain.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/Speex/libspeex/ltp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxzdEL/Sources/AudioCodecs/Source/Codecs/Speex/libspeex/nb_celp.c"
+ "21:44:58"
+ "Apple LLVM 21.0.0 (clang-2100.3.25.1) [+internal-os]"
+ "Jun 26 2026"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/AACEncoderFactory.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/AACEnhancedLowDelaySBREncoder.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/AACHighEfficiencyEncoder.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/AACHighEfficiencyV2Encoder.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncode.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncodeChannel.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncodeFrame.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncodeFrame.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEldEncoderChannel.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEncode.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEncodeChannel.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEncodeFrame.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/aacencifc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/aux_func.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_aac.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_enc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_fram.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_pam.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/cm_utils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/cod_chan.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/fifo_buf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/intensity.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/ms_chan.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/ms_stereo.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/pam.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/pam_loopmain.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/paminit.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/pns_tool.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/prconfig.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psy_chan.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psy_conf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psymain.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psyout.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psyparam.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/scaling.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/sw_cont.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/thr_chan.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/tns_enc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/toolmain.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/Speex/libspeex/ltp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.lZBWfR/Sources/AudioCodecs/Source/Codecs/Speex/libspeex/nb_celp.c"
- "00:01:31"
- "Apple LLVM 21.0.0 (clang-2100.3.23.3) [+internal-os]"
- "Jun 12 2026"

```
