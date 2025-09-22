## PeridotDepth

> `/System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth`

```diff

-25.0.0.0.0
-  __TEXT.__text: 0xfca58
-  __TEXT.__auth_stubs: 0x16b0
-  __TEXT.__objc_methlist: 0xf70
-  __TEXT.__const: 0x174b0
-  __TEXT.__gcc_except_tab: 0x6ab0
-  __TEXT.__cstring: 0x3774
-  __TEXT.__oslogstring: 0xb6c
-  __TEXT.__unwind_info: 0x1a0c
+28.0.0.0.0
+  __TEXT.__text: 0x105438
+  __TEXT.__auth_stubs: 0x17b0
+  __TEXT.__objc_methlist: 0xff8
+  __TEXT.__const: 0x17680
+  __TEXT.__gcc_except_tab: 0x7040
+  __TEXT.__cstring: 0x4010
+  __TEXT.__oslogstring: 0x1224
+  __TEXT.__unwind_info: 0x1c20
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_classname: 0x1e1
-  __TEXT.__objc_methname: 0x444e
-  __TEXT.__objc_methtype: 0x4f01
-  __TEXT.__objc_stubs: 0x1ce0
-  __DATA_CONST.__got: 0x290
-  __DATA_CONST.__const: 0xd8
+  __TEXT.__objc_methname: 0x48ec
+  __TEXT.__objc_methtype: 0x57a4
+  __TEXT.__objc_stubs: 0x1ea0
+  __DATA_CONST.__got: 0x2a0
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x22a8
-  __DATA_CONST.__objc_selrefs: 0xbc8
+  __DATA_CONST.__objc_const: 0x23f8
+  __DATA_CONST.__objc_selrefs: 0xc78
   __AUTH_CONST.__const: 0x3c8
-  __AUTH_CONST.__cfstring: 0x2460
+  __AUTH_CONST.__cfstring: 0x2cc0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_const: 0x798
-  __AUTH_CONST.__auth_got: 0xb58
+  __AUTH_CONST.__auth_got: 0xbd8
   __AUTH.__objc_data: 0x6e0
   __AUTH.__const_weak: 0x120
   __AUTH.__data: 0x8
   __AUTH.__got_weak: 0x10
   __DATA.__got_weak: 0xa8
-  __DATA.__objc_classrefs: 0x138
+  __DATA.__objc_classrefs: 0x140
   __DATA.__objc_superrefs: 0x70
-  __DATA.__objc_ivar: 0x254
-  __DATA.__data: 0x12758
-  __DATA.__common: 0x1
-  __DATA.__bss: 0x28a884
+  __DATA.__objc_ivar: 0x270
+  __DATA.__data: 0x12768
+  __DATA.__common: 0x3
+  __DATA.__bss: 0x28aa14
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 18B59C37-5C46-3641-A0B7-F2D62A234AE9
-  Functions: 1430
-  Symbols:   3698
-  CStrings:  1831
+  UUID: 6C99C203-4C19-3023-ABA3-A02B621872C1
+  Functions: 1501
+  Symbols:   3861
+  CStrings:  2068
 
Symbols:
+ -[Gmo gmoInitDone]
+ -[Gmo prevSessionDataLoaded]
+ -[Gmo setGmoInitDone:]
+ -[Gmo setPrevSessionDataLoaded:]
+ -[Gmo setSessionState:]
+ -[GmoController ca]
+ -[GmoController currAnchors]
+ -[GmoController hCtrlLast]
+ -[GmoController localNa]
+ -[GmoController sessionCalcState]
+ -[GmoController sessionState]
+ -[GmoController setCurrAnchors:]
+ -[GmoController setSessionPersistentData:]
+ -[GmoController solutionOKLast]
+ -[GmoDbgServices addDbgDataFor_getAnchorsWithHysteresis:currAnchors:snrHysteresisPct:anchorsWithHist:violations:numOfClippedSpots:anchorMoveIdx:spotLocationsAtRefDist:numQualifiedSpot:anchorsShift:anchorsMoved:]
+ -[GmoEngine blockSmoothing:localNa:specsOut:numOfFrames:smoothedSpotsLoc:validSpotsIndexes:numOfValidSpots:smoothedSNR:smoothedSNa:]
+ -[GmoEngine clipSpotsLocation:refSpotsLoc:clippedSpotLocations:numOfClippedSpots:]
+ -[GmoEngine homogClassifier:camCalib:smoothedSpotsLocAtRefDist:currentSpotsLocAtRefDist:factorySpotsLocAtRefDist:validSpotsIndexes:smoothedSNR:smoothedSNa:gmoMetrics:estTols:]
+ GCC_except_table1009
+ GCC_except_table1011
+ GCC_except_table1012
+ GCC_except_table1014
+ GCC_except_table1015
+ GCC_except_table1018
+ GCC_except_table1022
+ GCC_except_table1025
+ GCC_except_table1026
+ GCC_except_table1032
+ GCC_except_table1036
+ GCC_except_table1037
+ GCC_except_table1044
+ GCC_except_table1045
+ GCC_except_table1046
+ GCC_except_table1047
+ GCC_except_table1049
+ GCC_except_table105
+ GCC_except_table1050
+ GCC_except_table1056
+ GCC_except_table1057
+ GCC_except_table1058
+ GCC_except_table106
+ GCC_except_table107
+ GCC_except_table11
+ GCC_except_table1113
+ GCC_except_table1118
+ GCC_except_table1121
+ GCC_except_table1124
+ GCC_except_table1125
+ GCC_except_table1133
+ GCC_except_table1139
+ GCC_except_table1140
+ GCC_except_table115
+ GCC_except_table117
+ GCC_except_table119
+ GCC_except_table121
+ GCC_except_table123
+ GCC_except_table133
+ GCC_except_table135
+ GCC_except_table139
+ GCC_except_table143
+ GCC_except_table145
+ GCC_except_table151
+ GCC_except_table152
+ GCC_except_table155
+ GCC_except_table158
+ GCC_except_table164
+ GCC_except_table165
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table192
+ GCC_except_table193
+ GCC_except_table206
+ GCC_except_table208
+ GCC_except_table209
+ GCC_except_table217
+ GCC_except_table220
+ GCC_except_table221
+ GCC_except_table223
+ GCC_except_table231
+ GCC_except_table239
+ GCC_except_table240
+ GCC_except_table241
+ GCC_except_table249
+ GCC_except_table250
+ GCC_except_table251
+ GCC_except_table261
+ GCC_except_table264
+ GCC_except_table266
+ GCC_except_table272
+ GCC_except_table277
+ GCC_except_table279
+ GCC_except_table287
+ GCC_except_table311
+ GCC_except_table322
+ GCC_except_table323
+ GCC_except_table329
+ GCC_except_table338
+ GCC_except_table345
+ GCC_except_table346
+ GCC_except_table347
+ GCC_except_table35
+ GCC_except_table350
+ GCC_except_table351
+ GCC_except_table352
+ GCC_except_table353
+ GCC_except_table355
+ GCC_except_table367
+ GCC_except_table384
+ GCC_except_table386
+ GCC_except_table388
+ GCC_except_table406
+ GCC_except_table407
+ GCC_except_table409
+ GCC_except_table413
+ GCC_except_table416
+ GCC_except_table439
+ GCC_except_table477
+ GCC_except_table501
+ GCC_except_table516
+ GCC_except_table517
+ GCC_except_table528
+ GCC_except_table538
+ GCC_except_table54
+ GCC_except_table540
+ GCC_except_table544
+ GCC_except_table545
+ GCC_except_table560
+ GCC_except_table564
+ GCC_except_table565
+ GCC_except_table569
+ GCC_except_table57
+ GCC_except_table571
+ GCC_except_table574
+ GCC_except_table581
+ GCC_except_table642
+ GCC_except_table650
+ GCC_except_table651
+ GCC_except_table67
+ GCC_except_table690
+ GCC_except_table691
+ GCC_except_table731
+ GCC_except_table732
+ GCC_except_table734
+ GCC_except_table746
+ GCC_except_table747
+ GCC_except_table750
+ GCC_except_table756
+ GCC_except_table759
+ GCC_except_table765
+ GCC_except_table766
+ GCC_except_table767
+ GCC_except_table768
+ GCC_except_table776
+ GCC_except_table778
+ GCC_except_table784
+ GCC_except_table785
+ GCC_except_table787
+ GCC_except_table788
+ GCC_except_table790
+ GCC_except_table796
+ GCC_except_table797
+ GCC_except_table799
+ GCC_except_table800
+ GCC_except_table805
+ GCC_except_table81
+ GCC_except_table810
+ GCC_except_table811
+ GCC_except_table812
+ GCC_except_table817
+ GCC_except_table828
+ GCC_except_table829
+ GCC_except_table837
+ GCC_except_table840
+ GCC_except_table864
+ GCC_except_table869
+ GCC_except_table870
+ GCC_except_table871
+ GCC_except_table872
+ GCC_except_table874
+ GCC_except_table876
+ GCC_except_table881
+ GCC_except_table883
+ GCC_except_table884
+ GCC_except_table898
+ GCC_except_table899
+ GCC_except_table90
+ GCC_except_table900
+ GCC_except_table91
+ GCC_except_table912
+ GCC_except_table914
+ GCC_except_table916
+ GCC_except_table917
+ GCC_except_table928
+ GCC_except_table929
+ GCC_except_table93
+ GCC_except_table937
+ GCC_except_table94
+ GCC_except_table950
+ GCC_except_table951
+ GCC_except_table952
+ GCC_except_table953
+ GCC_except_table954
+ GCC_except_table959
+ GCC_except_table97
+ GCC_except_table979
+ GCC_except_table985
+ GCC_except_table995
+ GCC_except_table998
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_IVAR_$_Gmo._gmoInitDone
+ _OBJC_IVAR_$_Gmo._prevSessionDataLoaded
+ _OBJC_IVAR_$_GmoController._ca
+ _OBJC_IVAR_$_GmoController._currAnchors
+ _OBJC_IVAR_$_GmoController._hCtrlLast
+ _OBJC_IVAR_$_GmoController._localNa
+ _OBJC_IVAR_$_GmoController._sessionState
+ _OBJC_IVAR_$_GmoController._solutionOKLast
+ __Z17Interp1WithExtrapIf18LinearInterpolatorIfEEiRK11MatrixNxPtsILj1ET_ES6_S6_PS4_b
+ __ZGVZN7Filters7filtersEvE4inst
+ __ZL19spotMovementBuckets
+ __ZL23floatToStringScientificf
+ __ZN16PeridotTelemetry10endSessionEv
+ __ZN16PeridotTelemetry11reportEventEP8NSStringP12NSDictionary
+ __ZN16PeridotTelemetry12startSessionE8PDPreset
+ __ZN16PeridotTelemetry14frameProcessedERK17PeridotSuperFramePKN7peridot17PeridotUserOutputE
+ __ZN16PeridotTelemetry14printToConsoleE
+ __ZN16PeridotTelemetry15calcBankAmbientEPKN7peridot17PeridotUserOutputE
+ __ZN16PeridotTelemetry19sendToCoreAnalyticsE
+ __ZN16PeridotTelemetry20reportSpotStatisticsERK17PeridotSuperFramePKN7peridot17PeridotUserOutputEmf
+ __ZN16PeridotTelemetry21MeasurementStatistics3addEf
+ __ZN16PeridotTelemetry21reportFrameStatisticsERK17PeridotSuperFramePKN7peridot17PeridotUserOutputEm
+ __ZN16PeridotTelemetry23reportSessionStatisticsEv
+ __ZN16PeridotTelemetry24aggregateBankOutputStatsEPKN7peridot17PeridotUserOutputERNS_20UserOutputStatisticsE
+ __ZN16PeridotTelemetryC1Ev
+ __ZN16PeridotTelemetryC2Ev
+ __ZN25gmoCoreAnalyticsTelemetry11setCalibErrEff
+ __ZN25gmoCoreAnalyticsTelemetry14setAnchorMovedEm
+ __ZN25gmoCoreAnalyticsTelemetry14setHighAmbientEf
+ __ZN25gmoCoreAnalyticsTelemetry16reportHomogStatsEv
+ __ZN25gmoCoreAnalyticsTelemetry16setSpotsMovementER25PeridotCalibSpotLocationsS1_S1_
+ __ZN25gmoCoreAnalyticsTelemetry17setAnchorMovementERN7peridot9PDAnchorsES2_
+ __ZN25gmoCoreAnalyticsTelemetry19reportLongTermStatsEv
+ __ZN25gmoCoreAnalyticsTelemetry20setNumQualifiedSpotsEj
+ __ZN25gmoCoreAnalyticsTelemetry21setNumberSpotsClippedEi
+ __ZN25gmoCoreAnalyticsTelemetry25calcHomogStatsInitialDataEv
+ __ZN25gmoCoreAnalyticsTelemetry34loadDataFromPersistentDataLongTermEP35CoreAnalyticsLongTermPersistentData
+ __ZN25gmoCoreAnalyticsTelemetry35offloadDataToPersistentDataLongTermEP35CoreAnalyticsLongTermPersistentData
+ __ZN25gmoCoreAnalyticsTelemetry4initEv
+ __ZN25gmoCoreAnalyticsTelemetry6setHOkEbb
+ __ZN6common5utils7prctileIjEEfPT_jj
+ __ZN7BucketsC1ENSt3__16vectorIfNS0_9allocatorIfEEEE
+ __ZN7BucketsC2ENSt3__16vectorIfNS0_9allocatorIfEEEE
+ __ZN7BucketsD1Ev
+ __ZN7Filters7filtersEv
+ __ZN7FiltersC1Ev
+ __ZN7FiltersC2Ev
+ __ZN7peridot10PeridotDXP12macroProcessERKNS_23PeridotPreProcessOutput19PreProcessorOutSpotERKNS_13BankFramePtrsEmfffbRK17PeridotCalibPointRfSB_RbRNS_12PeridotDepthE
+ __ZN7peridot10PeridotDXP14findStrayQSPriERKNS_25PeridotDXPBaselineRemoval31PeridotDXPBaselineRemovalParamsERKNS_23PeridotPreProcessOutput19PreProcessorOutSpotERKNS_21PeridotDetectorOutput15DetectorOutSpotERf
+ __ZN7peridot10PeridotDXP15strayEstimationERKNS_15PeridotDxpMacro11DXPMacroOutES4_fffRfS5_
+ __ZN7peridot10PeridotDXP17macroProcessInnerERKNS_23PeridotPreProcessOutput19PreProcessorOutSpotERKNSt3__16vectorINS_12ImgHistogramENS5_9allocatorIS7_EEEERKNS_19FullStaticHistogramESF_fffffRKNS_22PeridotDxpMacroSpatial21PeridotMacroSpecsSpotEmbRK17PeridotCalibPointRfSN_RbRNS_16PeridotDepthSpotE
+ __ZN7peridot10PeridotDXP17macroProcess_MPDCERKNS_23PeridotPreProcessOutput19PreProcessorOutSpotERKNSt3__16vectorINS_12ImgHistogramENS5_9allocatorIS7_EEEESC_SC_SC_SC_SC_SC_fffmbRK17PeridotCalibPointRbRNS_12PeridotDepthE
+ __ZN7peridot10PeridotDXP3runERKNS_13BankFramePtrsEffRKNS_8T0OutputEPbRK29PeridotCalibBankSpotLocationsPfSB_RNS_12PeridotDepthE
+ __ZN7peridot10PeridotDXP8run_MPDCERKNSt3__16vectorINS2_INS_12ImgHistogramENS1_9allocatorIS3_EEEENS4_IS6_EEEESA_SA_SA_SA_SA_SA_ffRKNS_8T0OutputEPbRK29PeridotCalibBankSpotLocationsRNS_12PeridotDepthE
+ __ZN7peridot11OutputFlags8resetBitEm
+ __ZN7peridot11PeridotAlgo16getInternalStateEv
+ __ZN7peridot11PeridotAlgo16setInternalStateEP12NSDictionary
+ __ZN7peridot11PeridotAlgo23reportSessionStatisticsEv
+ __ZN7peridot11PeridotAlgo25startNewStatisticsSessionEv
+ __ZN7peridot11PeridotAlgo4Impl16getInternalStateEv
+ __ZN7peridot11PeridotAlgo4Impl16setInternalStateEP12NSDictionary
+ __ZN7peridot11PeridotAlgo4Impl18runBankWithT0_MPDCERKNSt3__16vectorINS3_INS_12ImgHistogramENS2_9allocatorIS4_EEEENS5_IS7_EEEESB_SB_SB_SB_SB_SB_hNS_13PeridotOpModeERKNS_8T0OutputEPKNS_19PeridotSpotRefDepthERSH_PNS_17PeridotUserOutputEPNS_12PeridotDepthE
+ __ZN7peridot11PeridotAlgo4Impl23reportSessionStatisticsEv
+ __ZN7peridot11PeridotAlgo4Impl25startNewStatisticsSessionEv
+ __ZN7peridot11PeridotAlgo4Impl4initEPK13_PeridotCalibP19ADCameraCalibration8PDPreset
+ __ZN7peridot11PeridotAlgo4Impl7prepareE8PDPreset
+ __ZN7peridot11PeridotAlgo4initEPK13_PeridotCalibP19ADCameraCalibration8PDPreset
+ __ZN7peridot11PeridotAlgo7prepareE8PDPreset
+ __ZN7peridot12Reflectivity16calcReflectivityERNS_12PeridotDepthERNS_17PeridotUserOutputERA14_A3_A9_KmPKahfbPKbPb
+ __ZN7peridot12Reflectivity23calcChannelReflectivityERKNS_12PeridotDepthEhmmfmffPKbPfS6_
+ __ZN7peridot12Reflectivity7calcPDEERKNS_15PeridotDXPCalibEff
+ __ZN7peridot12ReflectivityC1Efffffffff
+ __ZN7peridot12ReflectivityC2Efffffffff
+ __ZN7peridot15presetToRunModeE8PDPreset
+ __ZN7peridot17PeridotUserOutput11switchEchosERNS_21PeridotUserOutputSpotEmm
+ __ZN7peridot17PeridotUserOutput12fusionOutputERNS_12PeridotDepthENS_13PeridotOpModeEhbPbRKNS_8T0OutputERA14_A3_A9_mRNS_26PeridotUserOutputInvRmsEstE
+ __ZN7peridot17PeridotUserOutput14spotsFilteringEbPKfS2_S2_
+ __ZN7peridot17PeridotUserOutput4initEhPmf
+ __ZN7peridot17PeridotUserOutput8setStrayEPKfS2_S2_S2_
+ __ZN7peridot20peridotTempToCelciusEf
+ __ZNK7Buckets13getBucketNameEf
+ __ZNKSt3__16vectorIN6common17PeridotSpotValuesIfEENS_9allocatorIS3_EEE20__throw_length_errorB7v160006Ev
+ __ZNKSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE20__throw_length_errorB7v160006Ev
+ __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_out_of_rangeB7v160006Ev
+ __ZNSt3__113__nth_elementB7v160006INS_17_ClassicAlgPolicyERNS_6__lessIffEENS_11__wrap_iterIPfEEEEvT1_S8_S8_T0_
+ __ZNSt3__113__stable_sortINS_17_ClassicAlgPolicyERZN7peridot17PeridotUserOutput12fusionOutputERNS2_12PeridotDepthENS2_13PeridotOpModeEhbPbRKNS2_8T0OutputERA14_A3_A9_mRNS2_26PeridotUserOutputInvRmsEstEE3$_0PmEEvT1_SK_T0_NS_15iterator_traitsISK_E15difference_typeEPNSN_10value_typeEl
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEf
+ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERZN7peridot17PeridotUserOutput12fusionOutputERNS2_12PeridotDepthENS2_13PeridotOpModeEhbPbRKNS2_8T0OutputERA14_A3_A9_mRNS2_26PeridotUserOutputInvRmsEstEE3$_0PmEEvT1_SK_SK_OT0_NS_15iterator_traitsISK_E15difference_typeESP_PNSO_10value_typeEl
+ __ZNSt3__118__stable_sort_moveINS_17_ClassicAlgPolicyERZN7peridot17PeridotUserOutput12fusionOutputERNS2_12PeridotDepthENS2_13PeridotOpModeEhbPbRKNS2_8T0OutputERA14_A3_A9_mRNS2_26PeridotUserOutputInvRmsEstEE3$_0PmEEvT1_SK_T0_NS_15iterator_traitsISK_E15difference_typeEPNSN_10value_typeE
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B7v160006Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
+ __ZNSt3__16__sortIRNS_6__lessIjjEEPjEEvT0_S5_T_
+ __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEED1B7v160006Ev
+ __ZNSt3__19to_stringEf
+ __ZNSt3__1L19piecewise_constructE.967
+ __ZTTNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZZN7Filters7filtersEvE4inst
+ __ZZN7peridot20peridotTempToCelciusEfE14PeridotlutTemp
+ ____ZN16PeridotTelemetry11reportEventEP8NSStringP12NSDictionary_block_invoke
+ ____ZN25gmoCoreAnalyticsTelemetry16reportHomogStatsEv_block_invoke
+ ____ZN25gmoCoreAnalyticsTelemetry19reportLongTermStatsEv_block_invoke
+ ___block_descriptor_40_e30_"NSObject<OS_xpc_object>"8?0l
+ ___block_descriptor_40_ea8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_literal_global.956
+ _analytics_send_event_lazy
+ _arc4random_uniform
+ _objc_enumerationMutation
+ _objc_msgSend$addDbgDataFor_getAnchorsWithHysteresis:currAnchors:snrHysteresisPct:anchorsWithHist:violations:numOfClippedSpots:anchorMoveIdx:spotLocationsAtRefDist:numQualifiedSpot:anchorsShift:anchorsMoved:
+ _objc_msgSend$blockSmoothing:localNa:specsOut:numOfFrames:smoothedSpotsLoc:validSpotsIndexes:numOfValidSpots:smoothedSNR:smoothedSNa:
+ _objc_msgSend$clipSpotsLocation:refSpotsLoc:clippedSpotLocations:numOfClippedSpots:
+ _objc_msgSend$components:fromDate:
+ _objc_msgSend$copySessionState
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$description
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$homogClassifier:camCalib:smoothedSpotsLocAtRefDist:currentSpotsLocAtRefDist:factorySpotsLocAtRefDist:validSpotsIndexes:smoothedSNR:smoothedSNa:gmoMetrics:estTols:
+ _objc_msgSend$month
+ _objc_msgSend$now
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$sessionCalcState
+ _objc_msgSend$setSessionPersistentData:
+ _objc_msgSend$setSessionState:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$year
+ _objc_retainBlock
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x28
+ _time
+ _xpc_dictionary_create
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_double
+ _xpc_dictionary_set_int64
- -[GmoController anchors]
- -[GmoController setAnchors:]
- -[GmoDbgServices addDbgDataFor_getAnchorsWithHysteresis:currAnchors:snrHysteresisPct:anchorsWithHist:violations:anchorMoveIdx:spotLocationsAtRefDist:numQualifiedSpot:anchorsShift:anchorsMoved:]
- -[GmoEngine blockSmoothing:specsOut:numOfFrames:smoothedSpotsLoc:validSpotsIndexes:numOfValidSpots:smoothedSNR:]
- -[GmoEngine clipSpotsLocation:refSpotsLoc:clippedSpotLocations:]
- -[GmoEngine homogClassifier:camCalib:smoothedSpotsLocAtRefDist:currentSpotsLocAtRefDist:factorySpotsLocAtRefDist:validSpotsIndexes:smoothedSNR:gmoMetrics:estTols:]
- GCC_except_table100
- GCC_except_table101
- GCC_except_table102
- GCC_except_table103
- GCC_except_table1043
- GCC_except_table1054
- GCC_except_table1055
- GCC_except_table1063
- GCC_except_table1069
- GCC_except_table1070
- GCC_except_table109
- GCC_except_table110
- GCC_except_table111
- GCC_except_table112
- GCC_except_table120
- GCC_except_table122
- GCC_except_table124
- GCC_except_table126
- GCC_except_table128
- GCC_except_table138
- GCC_except_table140
- GCC_except_table149
- GCC_except_table150
- GCC_except_table153
- GCC_except_table160
- GCC_except_table174
- GCC_except_table185
- GCC_except_table186
- GCC_except_table187
- GCC_except_table188
- GCC_except_table195
- GCC_except_table196
- GCC_except_table197
- GCC_except_table198
- GCC_except_table211
- GCC_except_table213
- GCC_except_table226
- GCC_except_table229
- GCC_except_table230
- GCC_except_table236
- GCC_except_table244
- GCC_except_table245
- GCC_except_table246
- GCC_except_table253
- GCC_except_table256
- GCC_except_table258
- GCC_except_table268
- GCC_except_table269
- GCC_except_table275
- GCC_except_table283
- GCC_except_table307
- GCC_except_table315
- GCC_except_table318
- GCC_except_table325
- GCC_except_table334
- GCC_except_table341
- GCC_except_table342
- GCC_except_table343
- GCC_except_table360
- GCC_except_table361
- GCC_except_table364
- GCC_except_table382
- GCC_except_table383
- GCC_except_table389
- GCC_except_table392
- GCC_except_table415
- GCC_except_table449
- GCC_except_table45
- GCC_except_table46
- GCC_except_table469
- GCC_except_table47
- GCC_except_table476
- GCC_except_table484
- GCC_except_table485
- GCC_except_table488
- GCC_except_table496
- GCC_except_table506
- GCC_except_table512
- GCC_except_table513
- GCC_except_table524
- GCC_except_table525
- GCC_except_table529
- GCC_except_table532
- GCC_except_table539
- GCC_except_table600
- GCC_except_table608
- GCC_except_table609
- GCC_except_table62
- GCC_except_table646
- GCC_except_table683
- GCC_except_table684
- GCC_except_table686
- GCC_except_table698
- GCC_except_table699
- GCC_except_table700
- GCC_except_table701
- GCC_except_table702
- GCC_except_table703
- GCC_except_table704
- GCC_except_table706
- GCC_except_table708
- GCC_except_table711
- GCC_except_table715
- GCC_except_table716
- GCC_except_table717
- GCC_except_table718
- GCC_except_table719
- GCC_except_table720
- GCC_except_table721
- GCC_except_table728
- GCC_except_table729
- GCC_except_table730
- GCC_except_table736
- GCC_except_table737
- GCC_except_table739
- GCC_except_table740
- GCC_except_table744
- GCC_except_table753
- GCC_except_table757
- GCC_except_table76
- GCC_except_table762
- GCC_except_table780
- GCC_except_table781
- GCC_except_table789
- GCC_except_table815
- GCC_except_table816
- GCC_except_table820
- GCC_except_table821
- GCC_except_table822
- GCC_except_table823
- GCC_except_table827
- GCC_except_table831
- GCC_except_table832
- GCC_except_table834
- GCC_except_table835
- GCC_except_table85
- GCC_except_table851
- GCC_except_table852
- GCC_except_table855
- GCC_except_table86
- GCC_except_table863
- GCC_except_table867
- GCC_except_table868
- GCC_except_table87
- GCC_except_table879
- GCC_except_table88
- GCC_except_table888
- GCC_except_table89
- GCC_except_table897
- GCC_except_table902
- GCC_except_table903
- GCC_except_table905
- GCC_except_table910
- GCC_except_table911
- GCC_except_table923
- GCC_except_table930
- GCC_except_table935
- GCC_except_table936
- GCC_except_table949
- GCC_except_table962
- GCC_except_table963
- GCC_except_table970
- GCC_except_table971
- GCC_except_table973
- GCC_except_table974
- GCC_except_table975
- GCC_except_table976
- GCC_except_table977
- GCC_except_table982
- GCC_except_table983
- _OBJC_IVAR_$_GmoController._anchors
- __ZN7peridot10PeridotDXP12macroProcessERKNS_23PeridotPreProcessOutput19PreProcessorOutSpotERKNS_13BankFramePtrsEmfffbRK17PeridotCalibPointRNS_12PeridotDepthE
- __ZN7peridot10PeridotDXP15filterHighStrayERNS_12PeridotDepthE
- __ZN7peridot10PeridotDXP17macroProcessInnerERKNS_23PeridotPreProcessOutput19PreProcessorOutSpotERKNSt3__16vectorINS_12ImgHistogramENS5_9allocatorIS7_EEEERKNS_19FullStaticHistogramESF_ffffRKNS_22PeridotDxpMacroSpatial21PeridotMacroSpecsSpotEmbRK17PeridotCalibPointRNS_16PeridotDepthSpotE
- __ZN7peridot10PeridotDXP17macroProcess_MPDCERKNS_23PeridotPreProcessOutput19PreProcessorOutSpotERKNSt3__16vectorINS_12ImgHistogramENS5_9allocatorIS7_EEEESC_SC_SC_SC_SC_SC_ffmbRK17PeridotCalibPointRNS_12PeridotDepthE
- __ZN7peridot10PeridotDXP3runERKNS_13BankFramePtrsEffRKNS_8T0OutputEPbRK29PeridotCalibBankSpotLocationsRNS_12PeridotDepthE
- __ZN7peridot10PeridotDXP8run_MPDCERKNSt3__16vectorINS2_INS_12ImgHistogramENS1_9allocatorIS3_EEEENS4_IS6_EEEESA_SA_SA_SA_SA_SA_fRKNS_8T0OutputEPbRK29PeridotCalibBankSpotLocationsRNS_12PeridotDepthE
- __ZN7peridot11PeridotAlgo4Impl18runBankWithT0_MPDCERKNSt3__16vectorINS3_INS_12ImgHistogramENS2_9allocatorIS4_EEEENS5_IS7_EEEESB_SB_SB_SB_SB_SB_hNS_13PeridotOpModeERKNS_8T0OutputEPKNS_19PeridotSpotRefDepthEPNS_17PeridotUserOutputEPNS_12PeridotDepthE
- __ZN7peridot11PeridotAlgo4Impl4initEPK13_PeridotCalibP19ADCameraCalibrationNS_14PeridotRunModeE
- __ZN7peridot11PeridotAlgo4Impl7prepareENS_14PeridotRunModeE
- __ZN7peridot11PeridotAlgo4initEPK13_PeridotCalibP19ADCameraCalibrationNS_14PeridotRunModeE
- __ZN7peridot11PeridotAlgo7prepareENS_14PeridotRunModeE
- __ZN7peridot12Reflectivity16calcReflectivityERNS_12PeridotDepthERNS_17PeridotUserOutputERA14_A3_A9_KmPKahfbPb
- __ZN7peridot12Reflectivity23calcChannelReflectivityERKNS_12PeridotDepthEhmmfmffPfS4_
- __ZN7peridot12Reflectivity7calcPDEERKNS_15PeridotDXPCalibEf
- __ZN7peridot12ReflectivityC1Efffff
- __ZN7peridot12ReflectivityC2Efffff
- __ZN7peridot17PeridotUserOutput12fusionOutputERNS_12PeridotDepthENS_13PeridotOpModeEhbPbRA14_A3_A9_mRNS_26PeridotUserOutputInvRmsEstE
- __ZN7peridot17PeridotUserOutput4initEhPm
- __ZN7peridot20AggressorsClassifierC1Eb
- __ZN7peridot20AggressorsClassifierC1Ebf
- __ZN7peridot20AggressorsClassifierC2Eb
- __ZN7peridot20AggressorsClassifierC2Ebf
- __ZNSt3__113__stable_sortINS_17_ClassicAlgPolicyERZN7peridot17PeridotUserOutput12fusionOutputERNS2_12PeridotDepthENS2_13PeridotOpModeEhbPbRA14_A3_A9_mRNS2_26PeridotUserOutputInvRmsEstEE3$_0PmEEvT1_SH_T0_NS_15iterator_traitsISH_E15difference_typeEPNSK_10value_typeEl
- __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERZN7peridot17PeridotUserOutput12fusionOutputERNS2_12PeridotDepthENS2_13PeridotOpModeEhbPbRA14_A3_A9_mRNS2_26PeridotUserOutputInvRmsEstEE3$_0PmEEvT1_SH_SH_OT0_NS_15iterator_traitsISH_E15difference_typeESM_PNSL_10value_typeEl
- __ZNSt3__118__stable_sort_moveINS_17_ClassicAlgPolicyERZN7peridot17PeridotUserOutput12fusionOutputERNS2_12PeridotDepthENS2_13PeridotOpModeEhbPbRA14_A3_A9_mRNS2_26PeridotUserOutputInvRmsEstEE3$_0PmEEvT1_SH_T0_NS_15iterator_traitsISH_E15difference_typeEPNSK_10value_typeE
- __ZNSt3__1L19piecewise_constructE.889
- ___block_literal_global.878
- _objc_msgSend$addDbgDataFor_getAnchorsWithHysteresis:currAnchors:snrHysteresisPct:anchorsWithHist:violations:anchorMoveIdx:spotLocationsAtRefDist:numQualifiedSpot:anchorsShift:anchorsMoved:
- _objc_msgSend$blockSmoothing:specsOut:numOfFrames:smoothedSpotsLoc:validSpotsIndexes:numOfValidSpots:smoothedSNR:
- _objc_msgSend$clipSpotsLocation:refSpotsLoc:clippedSpotLocations:
- _objc_msgSend$homogClassifier:camCalib:smoothedSpotsLocAtRefDist:currentSpotsLocAtRefDist:factorySpotsLocAtRefDist:validSpotsIndexes:smoothedSNR:gmoMetrics:estTols:
CStrings:
+ "!!"
+ "!\"ERROR: Attempt to configure session data before GMO init\""
+ "%@ -> %@"
+ "(%@,%@]"
+ "(%@,Inf]"
+ "(-Inf,%@]"
+ ", "
+ "-[Gmo copySessionState]"
+ "-[Gmo setSessionState:]"
+ "-[GmoEngine clipSpotsLocation:refSpotsLoc:clippedSpotLocations:numOfClippedSpots:]"
+ "-[GmoEngine homogClassifier:camCalib:smoothedSpotsLocAtRefDist:currentSpotsLocAtRefDist:factorySpotsLocAtRefDist:validSpotsIndexes:smoothedSNR:smoothedSNa:gmoMetrics:estTols:]"
+ "-[GmoRecorder addRecWithObject:]"
+ "-[GmoRecorder checkStopConditionsAndStop]"
+ "-[GmoRecorder setPathWith:]"
+ "-[GmoRecorder stop]"
+ "3.3.0"
+ "@\"NSDictionary\"8@?0"
+ "@\"NSObject<OS_xpc_object>\"8@?0"
+ "AmbToNaRatio"
+ "AnchorMovement_Percentile"
+ "B96@0:8r^v16@24r^{?=[8{?=[14{?=ff}]}]fC[3C]}32r^{?=[8{?=[14{?=ff}]}]fC[3C]}40r^{?=[8{?=[14{?=ff}]}]fC[3C]}48r^v56r^v64r^v72^{GmoMetrics=fffffffff{nc=IIIIIIIII}}80^{EstTols=fffffff}88"
+ "BankID"
+ "BankId"
+ "Buckets"
+ "Confidence"
+ "ConfidenceBucket"
+ "DRfilterPercentage"
+ "Echo"
+ "EdgeOrReflectionPercentage"
+ "Event %@ contains invalid field: %@ = %@. Will not be reported"
+ "ExtremeAmbPercentage"
+ "Failed sending event %@ to CoreAnalytics"
+ "FrameId"
+ "Full"
+ "GMO: %s: ERROR: Attempt to configure session data before GMO init"
+ "GMO: %s: Failed to send the %s event into the diagnostics system with err %d"
+ "GMO: %s: GMO Core Analytics Init, ver: %d"
+ "GMO: %s: Got previous session data dict: %p"
+ "GMO: %s: Got stream shutdown notification. Providing session data for storage..."
+ "GMO: %s: Number of clipped spots is: %zu"
+ "GMO: %s: REC:ADD: recId: %d, Type: %d, recReq: %lld, recWritten: %lld, lengthReq: %ld [ms], currRecLength: %ld [ms], written %lld bytes\n"
+ "GMO: %s: REC:ReqStop: recId: %d, Type: %d, Req: %d, Actv: %d,  recsReq: %lld, recWritten: %lld, recLegthReqMs: %ld, currRecLengthMs: %ld\n"
+ "GMO: %s: REC:SETPATH: %@, recId: %d, Type: %d, Req: %d, lengthReg: %ld, Actv: %d, recWritten: %lld, error:%s\n"
+ "GMO: %s: REC:START: recId: %d, Type: %d, Req: %d, recReq: %lld, Actv: %d, recWritten: %lld\n"
+ "GMO: %s: REC:START:ERROR Error creating path: %@ for: recId: %d, Type: %d, Req: %d, recReq: %lld, Actv: %d, recWritten: %lld, error:%s\n"
+ "GMO: %s: REC:STOP: recId: %d, Type: %d, Actv: %d, recsReq: %lld, recWritten: %lld, recLegthReqMs: %ld, currRecLengthMs: %ld\n"
+ "GMO: %s: REC:file: File written, Written: %lld, Actual size: %llu, path: %@\n"
+ "GMO: %s: Sent the %s event into the diagnostics system"
+ "GMO: %s: WARNING: GMO session CoreAnalytics data size mismatch. Expected %lu, found:%lu -> ignoring & overwriting with empty data."
+ "GMO: %s: WARNING: GMO session persistent data integrity check failed. Expected pattern: 0x%08X found:  0x%08X, Expected version: %@, found: %@ -> ignoring & overwriting with empty data."
+ "GMO: %s: WARNING: No depthProcessor state data provided => Using empty session data\n"
+ "GMO: %s: WARNING: No previous GMO session data was provided. Starting from current session data."
+ "GlarePercentage"
+ "Gmo.mm"
+ "GrimaldiBaseline"
+ "GrimaldiBeta"
+ "GrimaldiBetaSNR"
+ "GroupGlareFAPercentage"
+ "HighAmbient"
+ "HighConfSpotsPercentage"
+ "HighStrayPercentage"
+ "Hok"
+ "LONGT: calibErrP50Arr: "
+ "LONGT: calibErrP95Arr: "
+ "MaxPeriscopeTemperature"
+ "MaxPeriscopeTemperatureDiff"
+ "MaxVSpad"
+ "MaxVSpadDiff"
+ "MinPeriscopeTemperature"
+ "MinVSpad"
+ "N/A"
+ "Na"
+ "NaBucket"
+ "NumDisabledMacroTwo"
+ "NumberAnchorsMoved"
+ "NumberOfFrames"
+ "NumberSpotsClipped"
+ "Number_of_qualified_spots"
+ "OperatingMode"
+ "OverallFiltered"
+ "PeridotDXP::getStrayRisingEdge Failed to find Global T0"
+ "PeridotTelemetry.mm"
+ "Preset"
+ "RangeBucket"
+ "Reflectivity"
+ "ReflectivityBucket"
+ "ReflectivityFilteredSpotsPercentage"
+ "RegularGlareFAPercentage"
+ "SNR"
+ "SSTP_Percent_success_long_term"
+ "SSTP_Spot_move_P50_long_term"
+ "SSTP_Spot_move_P95_long_term"
+ "SaturatedPercentage"
+ "SecondEchoFiltered"
+ "SessionPeriscopeTemperatureDiff"
+ "SessionTime"
+ "SessionVSpadDiff"
+ "SnrBucket"
+ "SpotId"
+ "Spots_movement_from_Factory_Percentile"
+ "Spots_movement_from_Nominal"
+ "Spots_movement_from_Operational_Percentile"
+ "TB,N,V_gmoInitDone"
+ "TB,N,V_prevSessionDataLoaded"
+ "TB,R,N,V_solutionOKLast"
+ "TempBucket"
+ "TileId"
+ "TimeOfFlight"
+ "TwoEchos"
+ "T{GlobalEstimationCtrl=BBBB},R,N,V_hCtrlLast"
+ "T{PDAnchors=[8{PDBankAnchors=[14{PDSpotAnchor=ccB}]}]},N,V_currAnchors"
+ "T{SessionState={SessionStatePersistentData=II{CoreAnalyticsPersistentData={CoreAnalyticsLongTermPersistentData=IIIII[30f][30f]}}}},R,N,V_sessionState"
+ "T{gmoCoreAnalyticsTelemetry={sCoreAnalyticsHomographyEvent=BBiiiffCCfffi}{sCoreAnalyticsLongTermEvent=Bfff}I{CoreAnalyticsLongTermPersistentData=IIIII[30f][30f]}BII},R,N,V_ca"
+ "T{vector<common::PeridotSpotValues<float>, std::allocator<common::PeridotSpotValues<float>>>=^v^v{__compressed_pair<common::PeridotSpotValues<float> *, std::allocator<common::PeridotSpotValues<float>>>=^v}},R,N,V_localNa"
+ "Unknown preset: %d"
+ "_ca"
+ "_currAnchors"
+ "_gmoInitDone"
+ "_hCtrlLast"
+ "_localNa"
+ "_longTermEventPersistentData.sessionCount < kGmoCaLongTermEventFireTriggerSessionCount"
+ "_prevSessionDataLoaded"
+ "_sessionState"
+ "_solutionOKLast"
+ "addDbgDataFor_getAnchorsWithHysteresis:currAnchors:snrHysteresisPct:anchorsWithHist:violations:numOfClippedSpots:anchorMoveIdx:spotLocationsAtRefDist:numQualifiedSpot:anchorsShift:anchorsMoved:"
+ "ambientLevel"
+ "blockSmoothing:localNa:specsOut:numOfFrames:smoothedSpotsLoc:validSpotsIndexes:numOfValidSpots:smoothedSNR:smoothedSNa:"
+ "ca"
+ "calibErrQualP50"
+ "clipSpotsLocation:refSpotsLoc:clippedSpotLocations:numOfClippedSpots:"
+ "com.apple.JasperDepth.FrameStatistics"
+ "com.apple.JasperDepth.GMO.HomographyAzul"
+ "com.apple.JasperDepth.GMO.longTerm"
+ "com.apple.JasperDepth.SessionStatistics"
+ "com.apple.JasperDepth.SpotStatistics"
+ "components:fromDate:"
+ "coreAnalyticsData"
+ "countByEnumeratingWithState:objects:count:"
+ "currentCalendar"
+ "getBytes:length:"
+ "gmoCoreAnalyticsTelemetry.mm"
+ "gmoInitDone"
+ "gmoSessionState"
+ "hCtrlLast"
+ "homogClassifier:camCalib:smoothedSpotsLocAtRefDist:currentSpotsLocAtRefDist:factorySpotsLocAtRefDist:validSpotsIndexes:smoothedSNR:smoothedSNa:gmoMetrics:estTols:"
+ "homography_Number_In_Session"
+ "i28@0:8^{GmoProcessBankInputs=QQQQQ[3f]IfdB{DXPUserOutput=[14{Spots=[2{Echos=fff}]}]}{SpotDepth=[14{Spots={HS=[2{Echos=ff}]}{HP=[2{Echos=ff}]}}]}{SuperFrameDataNormalBank={Specs=[3{PRI=[4{Phase=[14{Spots=[4[3f]]}]}]}]}{SpConfig=[14c][14c][14B]}{PRIConfigSpec=[16{PRIConfigSpecSingle=CCCCCCCC}]}}}16I24"
+ "i32@0:8r^{GmoProcessBankInputs=QQQQQ[3f]IfdB{DXPUserOutput=[14{Spots=[2{Echos=fff}]}]}{SpotDepth=[14{Spots={HS=[2{Echos=ff}]}{HP=[2{Echos=ff}]}}]}{SuperFrameDataNormalBank={Specs=[3{PRI=[4{Phase=[14{Spots=[4[3f]]}]}]}]}{SpConfig=[14c][14c][14B]}{PRIConfigSpec=[16{PRIConfigSpecSingle=CCCCCCCC}]}}}16^{GmoResult=BQ^{PDAnchors}^{?}B}24"
+ "i40@0:8r^{GmoProcessBankInputs=QQQQQ[3f]IfdB{DXPUserOutput=[14{Spots=[2{Echos=fff}]}]}{SpotDepth=[14{Spots={HS=[2{Echos=ff}]}{HP=[2{Echos=ff}]}}]}{SuperFrameDataNormalBank={Specs=[3{PRI=[4{Phase=[14{Spots=[4[3f]]}]}]}]}{SpConfig=[14c][14c][14B]}{PRIConfigSpec=[16{PRIConfigSpecSingle=CCCCCCCC}]}}}16Q24^{SpecsResults=[4[3[14f]]][14f][2[14B]]}32"
+ "i88@0:8^v16r^v24^v32Q40^{?=[8{?=[14{?=ff}]}]fC[3C]}48^v56^I64^v72^v80"
+ "localNa"
+ "longTermEventFirstInMonth"
+ "month"
+ "na"
+ "now"
+ "numOfClippedSpots"
+ "numQualSpots"
+ "numberWithInt:"
+ "pattern"
+ "prevSessionDataLoaded"
+ "reportHomogStats"
+ "reportLongTermStats"
+ "sessionCalcState"
+ "sessionState"
+ "setCalibErr"
+ "setCurrAnchors:"
+ "setGmoInitDone:"
+ "setPrevSessionDataLoaded:"
+ "setSessionPersistentData:"
+ "setSessionState:"
+ "solutionOKLast"
+ "spotMovePercentile"
+ "timeIntervalSinceDate:"
+ "trgouten flag is null - projector is off"
+ "v100@0:8r^{?=[8{?=[14{?=ff}]}]fC[3C]}16r^{PDAnchors=[8{PDBankAnchors=[14{PDSpotAnchor=ccB}]}]}24f32^{PDAnchors=[8{PDBankAnchors=[14{PDSpotAnchor=ccB}]}]}36^{spViolations=B[8[14{spViolationData=BBBB}]]}44Q52^v60^{?=[8{?=[14{?=ff}]}]fC[3C]}68Q76^{PDAnchors=[8{PDBankAnchors=[14{PDSpotAnchor=ccB}]}]}84Q92"
+ "v24@0:8^{SessionStatePersistentData=II{CoreAnalyticsPersistentData={CoreAnalyticsLongTermPersistentData=IIIII[30f][30f]}}}16"
+ "v24@0:8r^{GmoProcessBankInputs=QQQQQ[3f]IfdB{DXPUserOutput=[14{Spots=[2{Echos=fff}]}]}{SpotDepth=[14{Spots={HS=[2{Echos=ff}]}{HP=[2{Echos=ff}]}}]}{SuperFrameDataNormalBank={Specs=[3{PRI=[4{Phase=[14{Spots=[4[3f]]}]}]}]}{SpConfig=[14c][14c][14B]}{PRIConfigSpec=[16{PRIConfigSpecSingle=CCCCCCCC}]}}}16"
+ "v32@0:8r^{GmoMetrics=fffffffff{nc=IIIIIIIII}}16r^{EstTols=fffffff}24"
+ "v48@0:8r^{?=[8{?=[14{?=ff}]}]fC[3C]}16r^{?=[8{?=[14{?=ff}]}]fC[3C]}24^{?=[8{?=[14{?=ff}]}]fC[3C]}32^Q40"
+ "version"
+ "year"
+ "{GlobalEstimationCtrl=\"attemptHomog\"B\"doHomog\"B\"hDone\"B\"hOk\"B}"
+ "{GlobalEstimationCtrl=BBBB}16@0:8"
+ "{SessionState=\"persistent\"{SessionStatePersistentData=\"pattern\"I\"version\"I\"coreAnalyticsPersistentData\"{CoreAnalyticsPersistentData=\"coreAnalyticsLongTermData\"{CoreAnalyticsLongTermPersistentData=\"sessionCount\"I\"lastEventYear\"I\"lastEventMonth\"I\"hOkNoViolationsCount\"I\"homogDoneCount\"I\"calibErrP95Arr\"[30f]\"calibErrP50Arr\"[30f]}}}}"
+ "{SessionState={SessionStatePersistentData=II{CoreAnalyticsPersistentData={CoreAnalyticsLongTermPersistentData=IIIII[30f][30f]}}}}16@0:8"
+ "{gmoCoreAnalyticsTelemetry=\"_coreAnalyticsHomographyAzul\"{sCoreAnalyticsHomographyEvent=\"highAmbient\"B\"hOk\"B\"bankId\"i\"spotInBankId\"i\"numQualifiedSpots\"i\"spotsMovementFromNominal2\"f\"numAnchorMoved\"f\"prctileMoveBuckets\"C\"spotMovePercentile\"C\"spotsMovementFromFactoryPercentile\"f\"spotsMovementFromOperationalPercentile\"f\"anchorMovementPercentile\"f\"numberSpotsClipped\"i}\"_coreAnalyticsLongTerm\"{sCoreAnalyticsLongTermEvent=\"firstEventInMonthLongTerm\"B\"sstpSpotMoveP95LongTerm\"f\"sstpSpotMoveP50LongTerm\"f\"sstpPercentageSuccessLongTerm\"f}\"_homogSuccessfulTrackingCounter\"I\"_longTermEventPersistentData\"{CoreAnalyticsLongTermPersistentData=\"sessionCount\"I\"lastEventYear\"I\"lastEventMonth\"I\"hOkNoViolationsCount\"I\"homogDoneCount\"I\"calibErrP95Arr\"[30f]\"calibErrP50Arr\"[30f]}\"_isFireLongTermEvent\"B\"_homogTrackingLongTermCounter\"I\"_homogSuccessfulTrackingLongTermCounter\"I}"
+ "{gmoCoreAnalyticsTelemetry={sCoreAnalyticsHomographyEvent=BBiiiffCCfffi}{sCoreAnalyticsLongTermEvent=Bfff}I{CoreAnalyticsLongTermPersistentData=IIIII[30f][30f]}BII}16@0:8"
+ "{vector<common::PeridotSpotValues<float>, std::allocator<common::PeridotSpotValues<float>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<common::PeridotSpotValues<float> *, std::allocator<common::PeridotSpotValues<float>>>=\"__value_\"^v}}"
+ "{vector<common::PeridotSpotValues<float>, std::allocator<common::PeridotSpotValues<float>>>=^v^v{__compressed_pair<common::PeridotSpotValues<float> *, std::allocator<common::PeridotSpotValues<float>>>=^v}}16@0:8"
- "\x11!"
- "-[GmoEngine homogClassifier:camCalib:smoothedSpotsLocAtRefDist:currentSpotsLocAtRefDist:factorySpotsLocAtRefDist:validSpotsIndexes:smoothedSNR:gmoMetrics:estTols:]"
- "2"
- "3.2.0"
- "B88@0:8r^v16@24r^{?=[8{?=[14{?=ff}]}]fC[3C]}32r^{?=[8{?=[14{?=ff}]}]fC[3C]}40r^{?=[8{?=[14{?=ff}]}]fC[3C]}48r^v56r^v64^{GmoMetrics=fffffff{nc=IIIIIIIII}}72^{EstTols=fffffff}80"
- "Peridot algo preparing. Depth per pixel: %d, macro range: %d"
- "T{PDAnchors=[8{PDBankAnchors=[14{PDSpotAnchor=ccB}]}]},N,V_anchors"
- "Unknown preset passed to prepare: %d"
- "_anchors"
- "addDbgDataFor_getAnchorsWithHysteresis:currAnchors:snrHysteresisPct:anchorsWithHist:violations:anchorMoveIdx:spotLocationsAtRefDist:numQualifiedSpot:anchorsShift:anchorsMoved:"
- "blockSmoothing:specsOut:numOfFrames:smoothedSpotsLoc:validSpotsIndexes:numOfValidSpots:smoothedSNR:"
- "clipSpotsLocation:refSpotsLoc:clippedSpotLocations:"
- "homogClassifier:camCalib:smoothedSpotsLocAtRefDist:currentSpotsLocAtRefDist:factorySpotsLocAtRefDist:validSpotsIndexes:smoothedSNR:gmoMetrics:estTols:"
- "i28@0:8^{GmoProcessBankInputs=QQQQQ[3f]IfdB{DXPUserOutput=[14{Spots=[2{Echos=ff}]}]}{SpotDepth=[14{Spots={HS=[2{Echos=ff}]}{HP=[2{Echos=ff}]}}]}{SuperFrameDataNormalBank={Specs=[3{PRI=[4{Phase=[14{Spots=[4[3f]]}]}]}]}{SpConfig=[14c][14c][14B]}{PRIConfigSpec=[16{PRIConfigSpecSingle=CCCCCCCC}]}}}16I24"
- "i32@0:8r^{GmoProcessBankInputs=QQQQQ[3f]IfdB{DXPUserOutput=[14{Spots=[2{Echos=ff}]}]}{SpotDepth=[14{Spots={HS=[2{Echos=ff}]}{HP=[2{Echos=ff}]}}]}{SuperFrameDataNormalBank={Specs=[3{PRI=[4{Phase=[14{Spots=[4[3f]]}]}]}]}{SpConfig=[14c][14c][14B]}{PRIConfigSpec=[16{PRIConfigSpecSingle=CCCCCCCC}]}}}16^{GmoResult=BQ^{PDAnchors}^{?}B}24"
- "i40@0:8r^{GmoProcessBankInputs=QQQQQ[3f]IfdB{DXPUserOutput=[14{Spots=[2{Echos=ff}]}]}{SpotDepth=[14{Spots={HS=[2{Echos=ff}]}{HP=[2{Echos=ff}]}}]}{SuperFrameDataNormalBank={Specs=[3{PRI=[4{Phase=[14{Spots=[4[3f]]}]}]}]}{SpConfig=[14c][14c][14B]}{PRIConfigSpec=[16{PRIConfigSpecSingle=CCCCCCCC}]}}}16Q24^{SpecsResults=[4[3[14f]]][14f][2[14B]]}32"
- "i72@0:8^v16^v24Q32^{?=[8{?=[14{?=ff}]}]fC[3C]}40^v48^I56^v64"
- "setAnchors:"
- "v24@0:8r^{GmoProcessBankInputs=QQQQQ[3f]IfdB{DXPUserOutput=[14{Spots=[2{Echos=ff}]}]}{SpotDepth=[14{Spots={HS=[2{Echos=ff}]}{HP=[2{Echos=ff}]}}]}{SuperFrameDataNormalBank={Specs=[3{PRI=[4{Phase=[14{Spots=[4[3f]]}]}]}]}{SpConfig=[14c][14c][14B]}{PRIConfigSpec=[16{PRIConfigSpecSingle=CCCCCCCC}]}}}16"
- "v32@0:8r^{GmoMetrics=fffffff{nc=IIIIIIIII}}16r^{EstTols=fffffff}24"
- "v40@0:8r^{?=[8{?=[14{?=ff}]}]fC[3C]}16r^{?=[8{?=[14{?=ff}]}]fC[3C]}24^{?=[8{?=[14{?=ff}]}]fC[3C]}32"
- "v92@0:8r^{?=[8{?=[14{?=ff}]}]fC[3C]}16r^{PDAnchors=[8{PDBankAnchors=[14{PDSpotAnchor=ccB}]}]}24f32^{PDAnchors=[8{PDBankAnchors=[14{PDSpotAnchor=ccB}]}]}36^{spViolations=B[8[14{spViolationData=BBBB}]]}44^v52^{?=[8{?=[14{?=ff}]}]fC[3C]}60Q68^{PDAnchors=[8{PDBankAnchors=[14{PDSpotAnchor=ccB}]}]}76Q84"

```
