## libAudioDSP.dylib

> `/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib`

```diff

-819.301.0.0.0
-  __TEXT.__text: 0x508468
+819.302.0.0.0
+  __TEXT.__text: 0x508858
   __TEXT.__auth_stubs: 0x3f70
   __TEXT.__objc_methlist: 0x37c
   __TEXT.__const: 0x9ab70

   __TEXT.__eh_frame: 0xf0
   __TEXT.__objc_classname: 0xc9
   __TEXT.__objc_methname: 0xe45
-  __TEXT.__objc_methtype: 0x76f
+  __TEXT.__objc_methtype: 0x789
   __TEXT.__objc_stubs: 0x10e0
   __DATA_CONST.__got: 0x3f8
   __DATA_CONST.__const: 0xd5e0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: AC8A7565-10EE-34D6-ADFF-46F585C78F29
+  UUID: 5E2C1DBE-00CF-3E4C-9461-4E21B802C27C
   Functions: 12578
   Symbols:   33016
   CStrings:  15549
Functions:
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN6DspLib6Biquad7SectionENS_9allocatorIS3_EEE11__vallocateB8ne200100Em : 72 -> 76
~ __ZNSt3__16vectorIN6DspLib3RMSENS_9allocatorIS2_EEE8__appendEm : 500 -> 508
~ __ZNSt3__16vectorIN6DspLib14PeakPowerGuard24AdmittanceFilterCoeffSet6PresetENS_9allocatorIS4_EEE8__appendEm : 396 -> 412
~ __ZNSt3__16vectorIN6DspLib14PeakPowerGuard24AdmittanceFilterCoeffSet9FIRfilterENS_9allocatorIS4_EEE8__appendEm : 296 -> 304
~ __ZNSt3__16vectorIN6DspLib11PilotToneV29PilotToneENS_9allocatorIS3_EEE8__appendEm : 596 -> 604
~ __ZNSt3__16vectorIN6DspLib6Biquad14SDomainSectionENS_9allocatorIS3_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorIN6DspLib13CircularDelayENS_9allocatorIS2_EEE8__appendEm : 296 -> 304
~ __ZNSt3__16vectorIN6DspLib6Biquad16ParametricFilterENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJEEEPS3_DpOT_ : 320 -> 332
~ __ZNSt3__16vectorIbNS_9allocatorIbEEE11__vallocateB8ne200100Em : 68 -> 72
~ __ZNSt3__16vectorIN6DspLib6Biquad16ParametricFilterENS_9allocatorIS3_EEE8__appendEm : 412 -> 428
~ __ZNSt3__16vectorIN6DspLib13ComplexVectorENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRmEEEPS2_DpOT_ : 308 -> 312
~ __ZN6DspLib16LoudspeakerModel9Algorithm13setParametersENSt3__14spanIKfLm18446744073709551615EEE : 4004 -> 4028
~ __ZN6DspLib16LoudspeakerModelL43inversePressurFilterForSdomain_1_ParametersERNSt3__16vectorINS2_I10DSPComplexNS1_9allocatorIS3_EEEENS4_IS6_EEEES9_NS1_4spanIKfLm18446744073709551615EEEjdddRNS2_INS2_INS_6Biquad7SectionENS4_ISE_EEEENS4_ISG_EEEEd : 1940 -> 1956
~ __ZNSt3__16vectorINS0_I10DSPComplexNS_9allocatorIS1_EEEENS2_IS4_EEE24__emplace_back_slow_pathIJRS4_EEEPS4_DpOT_ : 304 -> 300
~ __ZNSt3__16vectorINS0_IN6DspLib6Biquad7SectionENS_9allocatorIS3_EEEENS4_IS6_EEE24__emplace_back_slow_pathIJiRKS3_EEEPS6_DpOT_ : 296 -> 292
~ __ZNSt3__16vectorIN6DspLib21LoudspeakerSystemIDV28SystemIDENS_9allocatorIS3_EEE8__appendEm : 432 -> 452
~ __ZNSt3__16vectorIN6DspLib13ComplexVectorENS_9allocatorIS2_EEE18__assign_with_sizeB8ne200100IPS2_S7_EEvT_T0_l : 412 -> 416
~ __ZNSt3__16vectorIN6DspLib13ComplexVectorENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorIN6DspLib3FFT19BufferedForwardSTFTENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRNS0_IfNS4_IfEEEERmRNS2_4ModeEEEEPS3_DpOT_ : 360 -> 364
~ __ZNSt3__16vectorIN6DspLib3FFT19BufferedInverseSTFTENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRNS0_IfNS4_IfEEEERmRNS2_4ModeEEEEPS3_DpOT_ : 336 -> 340
~ __ZNSt3__16vectorIN6DspLib13ComplexVectorENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJmEEEPS2_DpOT_ : 308 -> 312
~ __ZNSt3__16vectorIN6DspLib24ThermalSpeakerProtection12SpeakerModelENS_9allocatorIS3_EEE8__appendEmRKS3_ : 492 -> 500
~ __ZNSt3__16vectorIN6DspLib21LoudspeakerController9Algorithm13ChannelModuleENS_9allocatorIS4_EEE8__appendEm : 456 -> 464
~ __ZNSt3__16vectorIN6DspLib11LinearDelayENS_9allocatorIS2_EEE8__appendEm : 396 -> 412
~ __ZNSt3__16vectorINS0_IN6DspLib6Biquad7SectionENS_9allocatorIS3_EEEENS4_IS6_EEE24__emplace_back_slow_pathIJRS6_EEEPS6_DpOT_ : 316 -> 312
~ __ZNSt3__16vectorINS0_INS0_IN6DspLib6Biquad7SectionENS_9allocatorIS3_EEEENS4_IS6_EEEENS4_IS8_EEE24__emplace_back_slow_pathIJRS8_EEEPS8_DpOT_ : 316 -> 312
~ __ZNSt3__16vectorINS0_IN6DspLib6Biquad7SectionENS_9allocatorIS3_EEEENS4_IS6_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorIN6DspLib13ComplexVectorENS_9allocatorIS2_EEE8__appendEm : 392 -> 412
~ __ZNSt3__16vectorIN6DspLib9GainStateENS_9allocatorIS2_EEE8__appendEm : 444 -> 452
~ __ZN6DspLib26AlgorithmBaseNewParametersC2ERKNS_26SystemParametersDefinitionE : 628 -> 632
~ __ZNSt3__16vectorIN6DspLib13MovingAverageENS_9allocatorIS2_EEE8__appendEm : 388 -> 396
~ __ZN6DspLib13MeisterStueck10Automation25setAutomationForParameterENS_28PiecewiseLinearInterpolation9SetPointsEm : 568 -> 576
~ __ZNSt3__16vectorIN6DspLib28PiecewiseLinearInterpolation9SetPointsENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRS3_EEEPS3_DpOT_ : 320 -> 324
~ __ZN7PPUtils17ContiguousArray2DIfE6resizeEjj : 304 -> 312
~ __ZNSt3__16vectorIfNS_9allocatorIfEEE13shrink_to_fitEv : 212 -> 208
~ __ZN7PPUtils17ContiguousArray3DINSt3__17complexIfEEE6resizeEjjj : 1164 -> 1160
~ __ZN7PPUtils17ContiguousArray3DIfE6resizeEjjj : 976 -> 972
~ __ZN7PPUtils14findERBindicesENSt3__14spanIKfLm18446744073709551615EEEjfRNS0_6vectorIjNS0_9allocatorIjEEEE : 1124 -> 1132
~ __ZNSt3__16vectorIN7PPUtils23SphericalCoordinateTree25sphericalCoordinateBranchENS_9allocatorIS3_EEE9push_backB8ne200100ERKS3_ : 684 -> 692
~ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS0_IjNS_9allocatorIjEEEENS1_IS3_EEE8__appendEm : 360 -> 376
~ __ZNSt3__16vectorIPfNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZN10applesauce2CF7details15make_CFArrayRefIfPfEEDaT0_S5_NS1_15counterpart_tagE : 388 -> 392
~ __ZN10applesauce2CF7details15make_CFArrayRefIjPKjEEDaT0_S6_NS1_15counterpart_tagE : 388 -> 392
~ __ZN10applesauce2CF7details15make_CFArrayRefIfEEDaRKNSt3__16vectorIT_NS4_9allocatorIS6_EEEENS1_15counterpart_tagE : 408 -> 412
~ __ZNSt3__16vectorIN10applesauce2CF9NumberRefENS_9allocatorIS3_EEE7reserveEm : 128 -> 132
~ __ZN8AUDspLib30allocateStatusQueueForInstanceEjPKN6DspLib18AlgorithmInterfaceE : 828 -> 844
~ __ZN8AUDspLib10InitializeEv : 1416 -> 1412
~ __ZN32ParametricProcessorV2SynthesiserC2EP33ParametricProcessorV2GlobalConfigRKN7PPUtils17ContiguousArray3DIfEENSt3__14spanIfLm18446744073709551615EEEjbNS_22BinauralDecoderOptionsEbb : 14252 -> 14248
~ __ZN29ParametricProcessorV2AnalyserC1EP33ParametricProcessorV2GlobalConfigNS_13DoAEstimatorsE : 3672 -> 3644
~ __ZN10applesauce2CF7details15make_CFArrayRefIjEEDaRKNSt3__16vectorIT_NS4_9allocatorIS6_EEEENS1_15counterpart_tagE : 408 -> 412
~ __ZNSt3__16vectorINS0_INS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEEENS1_IS7_EEE16__init_with_sizeB8ne200100IPS7_SB_EEvT_T0_m : 236 -> 240
~ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE18__assign_with_sizeB8ne200100IPS5_S9_EEvT_T0_l : 364 -> 368
~ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE18__assign_with_sizeB8ne200100IPS3_S7_EEvT_T0_l : 364 -> 368
~ __ZNSt3__16vectorINS_10unique_ptrI19VPTimeFreqConverterNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE6resizeEm : 304 -> 308
~ __ZN10applesauce2CF7details15make_CFArrayRefIPKcEEDaRKSt16initializer_listIT_ENS1_15counterpart_tagE : 392 -> 396
~ __ZNSt3__16vectorIN10applesauce2CF9StringRefENS_9allocatorIS3_EEE7reserveEm : 128 -> 132
~ __ZN22AUReferenceSignalMixer10InitializeEv : 15864 -> 15872
~ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE6resizeEm : 400 -> 404
~ __ZN8nlohmann10basic_jsonINSt3__13mapENS1_6vectorENS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEbxydS7_NS_14adl_serializerENS3_IhNS7_IhEEEEE6createINS3_ISD_NS7_ISD_EEEEJNS1_11__wrap_iterIPKxEESK_EEEPT_DpOT0_ : 264 -> 268
~ __ZNSt3__16vectorIN8nlohmann10basic_jsonINS_3mapES0_NS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbxydS7_NS1_14adl_serializerENS0_IhNS7_IhEEEEEENS7_ISD_EEE7reserveEm : 192 -> 204
~ __ZNSt3__16vectorIN8nlohmann10basic_jsonINS_3mapES0_NS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbxydS7_NS1_14adl_serializerENS0_IhNS7_IhEEEEEENS7_ISD_EEE24__emplace_back_slow_pathIJSD_EEEPSD_DpOT_ : 292 -> 296
~ __ZN10applesauce2CF10convert_asINSt3__16vectorIfNS2_9allocatorIfEEEELi0EEENS2_8optionalIT_EEPK9__CFArray : 452 -> 456
~ __ZN19ParametricProcessorC2ERKNS_4parsE : 27388 -> 27392
~ __ZNSt3__16vectorIN2IR17FixedIntegerDelayIfEENS_9allocatorIS3_EEE6resizeEmRKS3_ : 468 -> 472
~ __ZNSt3__16vectorIN10applesauce2CF13DictionaryRefENS_9allocatorIS3_EEE9push_backB8ne200100EOS3_ : 216 -> 224
~ __ZN10applesauce2CF7details15make_CFArrayRefIfEEDaRKSt16initializer_listIT_ENS1_15counterpart_tagE : 392 -> 396
~ __ZN10applesauce2CF7details15make_CFArrayRefIjEEDaRKSt16initializer_listIT_ENS1_15counterpart_tagE : 392 -> 396
~ __ZN16AUSpatialMixerV211GetPropertyEjjjPv : 12540 -> 12544
~ __ZN10applesauce2CF7details20make_CFDictionaryRefINS0_9StringRefENS0_7TypeRefEEEDaRKNSt3__13mapIT_T0_NS6_4lessIS8_EENS6_9allocatorINS6_4pairIKS8_S9_EEEEEE : 460 -> 464
~ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE7reserveEm : 172 -> 184
~ __ZN16AUSpatialMixerV210InitializeEv : 17036 -> 17040
~ __ZN10applesauce2CF7details20make_CFDictionaryRefINSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS3_6vectorIfNS7_IfEEEEEEDaRKNS3_3mapIT_T0_NS3_4lessISF_EENS7_INS3_4pairIKSF_SG_EEEEEE : 488 -> 492
~ __ZNSt3__16vectorIN7Shoebox10ReflectionENS_9allocatorIS2_EEE6resizeEm : 628 -> 636
~ __ZN13ERSpatializer10initializeEfjj : 6988 -> 6996
~ __ZN14AUTemplateBaseI14AUCPMSVolumeV1NSt3__15tupleIJN4cpms8VolumeV110Parameters18TC_smoother_attackENS5_19TC_smoother_releaseENS5_11VolumeLevelENS5_10OutputGainEEEENS2_IJN9AUGeneric10Properties6BypassENS4_10Properties9LUTSystemEEEENS2_IJNSE_11PowerBudgetEEEEE11GetPropertyEjjjPv : 3388 -> 3400
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_22__unordered_map_hasherIS7_S8_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S8_SD_SB_Lb1EEENS5_IS8_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJOS7_EEENSN_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEERKT_DpOT0_ : 648 -> 644
~ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKNS_12basic_stringIcNS_11char_traitsIcEENS4_IcEEEESE_EEEPS3_DpOT_ : 276 -> 288
~ __ZNSt3__16vectorINS0_IjNS_9allocatorIjEEEENS1_IS3_EEE7reserveEm : 172 -> 176
~ __ZN18HRTFXTCSpatializer10initializeEfjj : 4752 -> 4732
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE18__assign_with_sizeB8ne200100IPS6_SA_EEvT_T0_l : 420 -> 424
~ __ZN16AUSpatialCapture10InitializeEv : 16864 -> 16932
~ __ZN20AUSpatialProbability35InitializeSpatialProbabilityClassesEv : 8164 -> 8092
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE24PiecewiseLinearTransformEENS_19__map_value_compareIS7_S9_NS_4lessIS7_EELb1EEENS5_IS9_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRKS7_EEENSK_IJEEEEEENS_4pairINS_15__tree_iteratorIS9_PNS_11__tree_nodeIS9_PvEElEEbEERKT_DpOT0_ : 244 -> 248
~ __ZN15CircArrayKernelC2EjjjffRKNSt3__16vectorIjNS0_9allocatorIjEEEERKNS1_IfNS2_IfEEEERKNS1_IS8_NS2_IS8_EEEESE_RKNS1_ISC_NS2_ISC_EEEERKNS1_IdNS2_IdEEEERKNS1_ISK_NS2_ISK_EEEERKNS1_IhNS2_IhEEEEPKN5CALog5ScopeE : 11868 -> 12072
~ __ZNSt3__16vectorI19FreqDomainConvolverNS_9allocatorIS1_EEE7reserveEm : 208 -> 220
~ __ZNSt3__16vectorI19FreqDomainConvolverNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKjEEEPS1_DpOT_ : 324 -> 328
~ __ZN18StringArrayDecoder22BlobToStringArray_PrivERKNSt3__111__wrap_iterIPKfEERNS0_6vectorINS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENSB_ISD_EEEE : 424 -> 428
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE9push_backB8ne200100ERKS6_ : 392 -> 400
~ __ZN17HRTFNFSpatializer10initializeEfjj : 4052 -> 4072
~ __ZN32AUSpatialMixerV2ChannelProcessor34setDecorrFilterLengthsOnReverbSendERKNSt3__16vectorIjNS0_9allocatorIjEEEE : 884 -> 896
~ __ZN4AUSM9MatrixMix17createHOADecodersEbj : 6368 -> 6380
~ __ZNSt3__16vectorIdNS_9allocatorIdEEE7reserveEm : 136 -> 148
~ __ZN17AUChannelSelector10InitializeEv : 3384 -> 3408
~ __ZN17AUFIREngineKernel13SetMatrixFIRsERKNSt3__16vectorINS1_INS1_INS1_IfNS0_9allocatorIfEEEENS2_IS4_EEEENS2_IS6_EEEENS2_IS8_EEEE : 3476 -> 3496
~ __ZN15CartesianPanner10initializeEjN4AUSM13ExclusionZone7ePresetE : 9500 -> 9512
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE18__assign_with_sizeB8ne200100IPKS6_SB_EEvT_T0_l : 400 -> 412
~ __ZN11AUFIRFilter11GetPropertyEjjjPv : 836 -> 840
~ __ZNKSt3__111basic_regexIcNS_12regex_traitsIcEEE16__match_at_startINS_9allocatorINS_9sub_matchIPKcEEEEEEbS8_S8_RNS_13match_resultsIS8_T_EENS_15regex_constants15match_flag_typeEb : 4136 -> 4148
~ __ZNSt3__15dequeINS_7__stateIcEENS_9allocatorIS2_EEE9push_backEOS2_ : 820 -> 824
~ __ZN10applesauce2CF7details15make_CFArrayRefINSt3__13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS0_7TypeRefENS3_4lessISA_EENS8_INS3_4pairIKSA_SB_EEEEEEEEDaRKNS3_6vectorIT_NS8_ISL_EEEENS1_15counterpart_tagE : 832 -> 836
~ __ZN10applesauce2CF10convert_toINSt3__16vectorINS2_3mapINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS0_7TypeRefENS2_4lessISA_EENS8_INS2_4pairIKSA_SB_EEEEEENS8_ISI_EEEELi0EEET_PK9__CFArray : 1380 -> 1388
~ __ZNSt3__16vectorIN10applesauce2CF13DictionaryRefENS_9allocatorIS3_EEE7reserveEm : 128 -> 132
~ __ZN10applesauce2CF7details20make_CFDictionaryRefINSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS0_7TypeRefEEEDaRKNS3_3mapIT_T0_NS3_4lessISD_EENS7_INS3_4pairIKSD_SE_EEEEEE : 488 -> 492
~ __ZN13AUDSPGraph_v110InitializeEv : 28428 -> 28504
~ __ZN10applesauce2CF7details15make_CFArrayRefIPKcPKS4_EEDaT0_S8_NS1_15counterpart_tagE : 388 -> 392
~ __ZN10applesauce2CF7details15make_CFArrayRefIfNSt3__111__wrap_iterIPKfEEEEDaT0_S9_NS1_15counterpart_tagE : 388 -> 392
~ __ZN28AUSpatialMixerV2InputElement27InitializeChannelProcessorsEv : 9152 -> 9160
~ __ZNK28AUSpatialMixerV2InputElement11GetGeometryEv : 2544 -> 2560
~ __ZN28AUSpatialMixerV2InputElement7ProcessERjRK14AudioTimeStampRN4AUSM13SharedBuffersEPNS4_10ReverbSendES8_S8_S8_jj : 19780 -> 19800
~ __ZN17ScottySTFTUpmixer27calculate_smoothing_windowsEfffb : 1868 -> 1872
~ __ZN15AUMeisterStueck14loadAutomationEP12NSDictionary : 1340 -> 1320
~ __ZN6ecMIMO14ec_state_resetEv : 1804 -> 1808
~ __ZN10applesauce2CF7details15make_CFArrayRefINSt3__16vectorINS4_IfNS3_9allocatorIfEEEENS5_IS7_EEEEEEDaRKNS4_IT_NS5_ISB_EEEENS1_15counterpart_tagE : 480 -> 484
~ __ZN10applesauce2CF7details15make_CFArrayRefINSt3__16vectorIfNS3_9allocatorIfEEEEEEDaRKNS4_IT_NS5_IS9_EEEENS1_15counterpart_tagE : 460 -> 464
~ __ZNSt3__16vectorIN10applesauce2CF8ArrayRefENS_9allocatorIS3_EEE7reserveEm : 128 -> 132
~ __ZN11AUCircArray12CreateKernelEv : 3036 -> 3060
~ __ZN26SincKernelFactorySingleton19ReferenceSincKernelEiidd : 2376 -> 2384
~ __ZNSt3__16vectorINS_10unique_ptrI19VPTimeFreqConverterNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE9push_backB8ne200100EOS5_ : 248 -> 256
~ __ZN8MIL2BNNS9loadModelEPK14__CFDictionary : 5608 -> 5592
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE13shrink_to_fitEv : 212 -> 208
~ __ZN4AUSM14RoomCongruence9Processor27computeTargetMatchingParamsERKNS0_10RoomTargetEN2IR8IRPresetERKNS0_8UserDataE : 7104 -> 7108
~ __ZN4AUSM14RoomCongruence9ProcessorC2ERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE : 8920 -> 8840
~ __ZN2IR5Cache10initializeEf : 1716 -> 1720
~ __ZN18CASmartPreferences10AddHandlerIbEEvPK10__CFStringS3_PFT_PKvRbENSt3__18functionIFvS4_EEE : 1156 -> 1164
~ __ZN21AUSpeakerProtectionV321InitParamsFromPlistV9ER14CACFDictionary : 59260 -> 59284
~ __ZNSt3__16vectorINS_10unique_ptrIN4clsp28SpeakerCalibrationPropertiesENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE9push_backB8ne200100EOS6_ : 248 -> 256
~ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKNS2_9StringRefERKfEEEPS3_DpOT_ : 276 -> 288
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN10applesauce2CF9StringRefEfEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIS4_JRKNS_21piecewise_construct_tENS_5tupleIJOS4_EEENSL_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_ : 1116 -> 1108
~ __ZNSt3__16vectorIN10applesauce2CF13DictionaryRefENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRNS_13unordered_mapINS2_9StringRefENS2_9NumberRefENS_4hashIS9_EENS_8equal_toIS9_EENS4_INS_4pairIKS9_SA_EEEEEEEEEPS3_DpOT_ : 364 -> 368
~ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKNS2_9StringRefERKNS2_9NumberRefEEEEPS3_DpOT_ : 252 -> 264
~ __ZNSt3__16vectorIN4clsp9telemetry4ItemENS_9allocatorIS3_EEE7reserveEm : 124 -> 128
~ __ZNSt3__16vectorIN4clsp9telemetry4ItemENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_ : 192 -> 196
~ __Z21FetchAndInterpretSpTSv : 3812 -> 3816
~ __ZN4cpms11controllers5PowerIfNS_9smoothers11ExponentialEN4clsp13AttackReleaseEE9GainGroupC2EfNS6_17SmoothingStrategyERKNSt3__16vectorIjNS9_9allocatorIjEEEERKNSA_INS_9TimeScaleIfEENSB_ISH_EEEESF_ : 2960 -> 2976
~ __ZN28ParametricProcessorV2Wrapper18recreateAllObjectsEv : 2460 -> 2404
~ __ZN23EndpointVADViterbiModel33parseObservationTransitionFloat32ERPKhRNSt3__16vectorINS4_INS4_IfNS3_9allocatorIfEEEENS5_IS7_EEEENS5_IS9_EEEERKNS4_IjNS5_IjEEEE : 1384 -> 1388
~ __ZN17AULoudnessInNoise11GetPropertyEjjjPv : 1964 -> 1968
~ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE7reserveEm : 192 -> 196
~ __ZL15GetFilterMatrixRKN10applesauce2CF13DictionaryRefE : 3228 -> 3288
~ __ZN10applesauce2CF10convert_asINSt3__16vectorINS3_INS3_INS3_IfNS2_9allocatorIfEEEENS4_IS6_EEEENS4_IS8_EEEENS4_ISA_EEEELi0EEENS2_8optionalIT_EEPK9__CFArray : 1676 -> 1712
~ __ZN10applesauce2CF7details15make_CFArrayRefINSt3__16vectorINS4_INS4_IfNS3_9allocatorIfEEEENS5_IS7_EEEENS5_IS9_EEEEEEDaRKNS4_IT_NS5_ISD_EEEENS1_15counterpart_tagE : 480 -> 484
~ __ZN11AUFIREngine10InitializeEv : 1748 -> 1752
~ __ZN4AUSM10SoundStage20setWarpingParametersEjRKNSt3__16vectorI21AUSMChannelParametersNS1_9allocatorIS3_EEEERKNS1_12basic_stringIcNS1_11char_traitsIcEENS4_IcEEEE : 5720 -> 5680
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE6resizeEm : 404 -> 408
~ __ZN11LeanSpatial17LSFilterProcessorIDF16_E10initializeEmNS_8BankModeE : 5424 -> 5416
~ __ZN4VBAP10initializeERKNSt3__16vectorIfNS0_9allocatorIfEEEES6_RKNS1_IiNS2_IiEEEERKNS1_INS0_4listIiS7_EENS2_ISC_EEEE : 15532 -> 15536
~ __ZNSt3__16vectorINS_4listIiNS_9allocatorIiEEEENS2_IS4_EEE18__construct_at_endIPS4_S8_EEvT_T0_m : 280 -> 284
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CBcKugDhIL-NiJH4a1pEdcQ0VWSs85Hv5mucj9Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
+ "/AppleInternal/Library/BuildRoots/4~CBcKugDhIL-NiJH4a1pEdcQ0VWSs85Hv5mucj9Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
+ "22:56:55"
+ "22:57:00"
+ "22:57:03"
+ "22:57:14"
+ "@24@0:8{unique_ptr<NeuralNetImpl, std::default_delete<NeuralNetImpl>>={?=^{NeuralNetImpl}}}16"
+ "Nov  2 2025"
+ "{optional<AUProcessingBlock_DSPGraph>=\"\"(?=\"__null_state_\"c\"__val_\"{AUProcessingBlock_DSPGraph=\"_vptr$AUProcessingBlockBase\"^^?\"mName\"^{__CFString}\"mPBRef\"^{OpaqueAUPB}\"mUnitVector\"{vector<AUPBUnit, std::allocator<AUPBUnit>>=\"__begin_\"^{AUPBUnit}\"__end_\"^{AUPBUnit}\"\"{?=\"__cap_\"^{AUPBUnit}}}\"mGraph\"{shared_ptr<DSPGraph::Graph>=\"__ptr_\"^{Graph}\"__cntrl_\"^{__shared_weak_count}}\"mProfiler\"{unique_ptr<DSPGraph::Profiler, std::default_delete<DSPGraph::Profiler>>=\"\"{?=\"__ptr_\"^{Profiler}}}})\"__engaged_\"B}"
+ "{unique_ptr<NeuralNetImpl, std::default_delete<NeuralNetImpl>>=\"\"{?=\"__ptr_\"^{NeuralNetImpl}}}"
+ "{unique_ptr<NeuralNetImpl, std::default_delete<NeuralNetImpl>>={?=^{NeuralNetImpl}}}16@0:8"
- "/AppleInternal/Library/BuildRoots/4~CAo6ugCbZ2MHQsORtnmS3Gpn25gbohYUiineio8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
- "/AppleInternal/Library/BuildRoots/4~CAo6ugCbZ2MHQsORtnmS3Gpn25gbohYUiineio8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
- "01:36:19"
- "01:36:25"
- "01:36:28"
- "01:36:41"
- "@24@0:8{unique_ptr<NeuralNetImpl, std::default_delete<NeuralNetImpl>>=^{NeuralNetImpl}}16"
- "Oct 23 2025"
- "{optional<AUProcessingBlock_DSPGraph>=\"\"(?=\"__null_state_\"c\"__val_\"{AUProcessingBlock_DSPGraph=\"_vptr$AUProcessingBlockBase\"^^?\"mName\"^{__CFString}\"mPBRef\"^{OpaqueAUPB}\"mUnitVector\"{vector<AUPBUnit, std::allocator<AUPBUnit>>=\"__begin_\"^{AUPBUnit}\"__end_\"^{AUPBUnit}\"__cap_\"^{AUPBUnit}}\"mGraph\"{shared_ptr<DSPGraph::Graph>=\"__ptr_\"^{Graph}\"__cntrl_\"^{__shared_weak_count}}\"mProfiler\"{unique_ptr<DSPGraph::Profiler, std::default_delete<DSPGraph::Profiler>>=\"__ptr_\"^{Profiler}}})\"__engaged_\"B}"
- "{unique_ptr<NeuralNetImpl, std::default_delete<NeuralNetImpl>>=\"__ptr_\"^{NeuralNetImpl}}"
- "{unique_ptr<NeuralNetImpl, std::default_delete<NeuralNetImpl>>=^{NeuralNetImpl}}16@0:8"

```
