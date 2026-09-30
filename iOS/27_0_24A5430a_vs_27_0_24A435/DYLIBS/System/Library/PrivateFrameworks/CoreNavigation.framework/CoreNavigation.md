## CoreNavigation

> `/System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation`

```diff

 425.0.0.0.0
-  __TEXT.__text: 0x361f64
+  __TEXT.__text: 0x3620ec
   __TEXT.__objc_methlist: 0x198
   __TEXT.__const: 0x51fb1
   __TEXT.__cstring: 0x3839c
Functions:
~ __ZN5raven31RavenDeviceAttitudeActiveObject39UpdateDeviceVehicleAttitudeWithRotationEv : 4664 -> 4660
~ __ZN5raven14RavenEstimator23StoreHistoricalSolutionEv : 2168 -> 2184
~ sub_1d8428864 -> sub_1d76db870 : 1428 -> 1440
~ __ZNK5raven26RavenSolutionPostprocessor15ShouldBeClampedERKNS_18RavenSolutionEventE : 2404 -> 2408
~ __ZN5raven26RavenSolutionPostprocessor21PushToClampingHistoryERKNS_18RavenSolutionEventE : 2832 -> 2856
~ __ZN5raven33RavenDeltaVIOEstimateActiveObject11HandleEventERKNS_18RavenSolutionEventE : 2060 -> 2072
~ __ZN5raven34ConvertProtobufToGnssMeasDataEventERKN14CoreNavigation3CLP8LogEntry11PrivateData33MeasurementReportCallbackContentsERNS_24GnssMeasurementDataEventE : 9300 -> 9332
~ sub_1d8475ff0 -> sub_1d7729050 : 1380 -> 1384
~ sub_1d8480b38 -> sub_1d7733b9c : 3120 -> 3116
~ __ZNK5raven22GNSSUncertaintyScaling39Fire7orNewerPhoneGNSSUncertaintyWrapper29GetUncertaintyScaleFactorCoreERKNS_18GNSSObservableTypeERKNS_8GnssBandERKNS_22RavenSignalEnvironmentERKNS_18RavenActivityStateERKNSt3__14pairImmEERKfNS0_30GNSSUncertaintyScaleFactorTypeE : 2800 -> 2808
~ __ZN8trackrun26TrackRunEngineActiveObject11HandleEventERKNS_13PositionEventE : 16612 -> 16616
~ sub_1d8497f50 -> sub_1d774afbc : 12620 -> 12624
~ __ZN5raven32RavenIMUPreprocessorActiveObject11HandleEventERKNS_18AccelerometerEventE : 1568 -> 1576
~ __ZN12cnestimation18PeriodicityTracker15AddSignalSampleEd : 3172 -> 3228
~ sub_1d84a44a4 -> sub_1d7757554 : 580 -> 584
~ __ZN5raven32RavenIMUPreprocessorActiveObject11HandleEventERKNS_13RateGyroEventE : 1568 -> 1576
~ __ZN5raven34RavenPressurePrefilterActiveObject11HandleEventERKNS_14BarometerEventE : 3608 -> 3628
~ sub_1d84aa4e0 -> sub_1d775d5b0 : 580 -> 584
~ __ZN5raven31RavenDeviceAttitudeActiveObject22DetectStationaryStatusEv : 3124 -> 3108
~ __ZN5raven31RavenDeviceAttitudeActiveObject40UpdateDeviceAttitudeByLinearAccelerationERKNS_13TimeMarkEventE : 3848 -> 3852
~ __ZN5raven31RavenDeviceAttitudeActiveObject35UpdateDeviceAttitudeByWahbaSolutionERKNS_13TimeMarkEventE : 6160 -> 6168
~ sub_1d84cc970 -> sub_1d777fa40 : 3812 -> 3816
~ sub_1d84d88bc -> sub_1d778b990 : 256 -> 260
~ sub_1d84d89bc -> sub_1d778ba94 : 248 -> 252
~ sub_1d84dcfa8 -> sub_1d7790084 : 284 -> 288
~ __ZN12cnestimation18PeriodicityTracker5ResetEv : 296 -> 300
~ __ZN12cnestimation18PeriodicityTracker9ConfigureERKNS_28PeriodicityTrackerConfigArgsE : 1912 -> 1924
~ sub_1d85c3090 -> sub_1d7876180 : 128 -> 132
~ __ZNK12cnestimation18PeriodicityTracker51NumberOfSamplesToLastObservedFeatureInRecentSamplesEj : 564 -> 576
~ sub_1d85c40d0 -> sub_1d78771d0 : 256 -> 260
~ sub_1d85c4384 -> sub_1d7877488 : 572 -> 576
~ sub_1d85df654 -> sub_1d789275c : 184 -> 176
~ sub_1d85e357c -> sub_1d789667c : 284 -> 288
~ sub_1d85e7878 -> sub_1d789a97c : 252 -> 248
~ sub_1d85e7974 -> sub_1d789aa74 : 304 -> 296
~ __ZN4swan14BatchLogParser6updateERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 1648 -> 1656
~ sub_1d85ef094 -> sub_1d78a2194 : 340 -> 336
~ sub_1d85f5410 -> sub_1d78a850c : 4164 -> 4192
~ sub_1d85f6454 -> sub_1d78a956c : 792 -> 796
~ __ZNK4swan36ForwardBackwardFixedIntervalSmoother6UpdateERKNS_7details6VectorILi6EEERKNS1_6MatrixILi6ELi6EEEmRKNSt3__16vectorIdNSA_9allocatorIdEEEERKNSB_IS3_NSC_IS3_EEEERKNSB_INS2_ILi3EEENSC_ISL_EEEESP_SG_SG_bRSI_RNSB_IS7_NSC_IS7_EEEERdSQ_ST_ : 9808 -> 9820
~ __ZNK4swan26PositionVelocityDataEditor25TestNormalizedInnovationsEmRKNSt3__16vectorINS_7details6VectorILi6EEENS1_9allocatorIS5_EEEERKNS2_INS3_6MatrixILi6ELi6EEENS6_ISC_EEEEdRmRNS2_ImNS6_ImEEEE : 408 -> 420
~ __ZNK4swan18ConsistencyChecker34UpdateNormalizedInnovationsSquaredEmjRKNSt3__16vectorINS_7details6VectorILi6EEENS1_9allocatorIS5_EEEERKNS2_INS3_6MatrixILi6ELi6EEENS6_ISC_EEEERd : 1072 -> 1076
~ sub_1d86045d8 -> sub_1d78b7710 : 1180 -> 1192
~ __ZN8trackrun44ConvertProtobufToGEOMapRunningTrackDataEventERKN14CoreNavigation3CLP8LogEntry11PrivateData25GEOMapTropicalSavannaDataERNS_27GEOMapRunningTrackDataEventE : 4092 -> 4064
~ __ZN5raven33RavenDeltaVIOEstimateActiveObject11HandleEventERKNS_16VIOEstimateEventE : 3880 -> 3896
~ sub_1d8622250 -> sub_1d78d5388 : 924 -> 932
~ __ZN5raven33RavenDeltaVIOEstimateActiveObject5ResetEv : 1272 -> 1276
~ sub_1d8625584 -> sub_1d78d86c8 : 120 -> 104
~ sub_1d8625a6c -> sub_1d78d8ba0 : 320 -> 324
~ __ZN5raven31RavenDeviceAttitudeActiveObject52ComputePCABasedHorizontalDirectionOfTravelInIMUFrameERKNS_13TimeMarkEventE : 3344 -> 3348
~ __ZN5raven31RavenDeviceAttitudeActiveObject29PCAForHorizontalDOTInIMUFrameERK6CNTimeS3_RKNS_13RavenSolutionERN8cnmatrix8CNMatrixILj3ELj1EdEERdSA_ : 4136 -> 4140
~ __ZNK5raven31RavenDeviceAttitudeActiveObject13DualDirSmoothERNSt3__16vectorIdNS1_9allocatorIdEEEEd : 628 -> 644
~ __ZN5raven31RavenDeviceAttitudeActiveObject20IsDecelerationToStopEv : 852 -> 860
~ __ZN5raven31RavenDeviceAttitudeActiveObject5ResetEv : 2528 -> 2536
~ sub_1d862fc14 -> sub_1d78e2d74 : 356 -> 360
~ sub_1d86300cc -> sub_1d78e3230 : 256 -> 260
~ sub_1d86302dc -> sub_1d78e3444 : 256 -> 260
~ sub_1d8630530 -> sub_1d78e369c : 252 -> 256
~ sub_1d8632fd4 -> sub_1d78e6144 : 184 -> 180
~ __ZN5raven32RavenIMUPreprocessorActiveObject9ConfigureERKNS_42RavenIMUPreprocessorActiveObjectConfigArgsE : 1796 -> 1812
~ __ZN5raven34RavenPressurePrefilterActiveObject9ConfigureERKNS_44RavenPressurePrefilterActiveObjectConfigArgsE : 1464 -> 1468
~ __ZN5raven34RavenPressurePrefilterActiveObject5ResetEv : 356 -> 360
~ __ZN5raven32RavenUserGaitTrackerActiveObject22InitializeGaitTrackingEi : 348 -> 356
~ sub_1d8662be0 -> sub_1d7915d6c : 3796 -> 3820
~ sub_1d867dab8 -> sub_1d7930c5c : 184 -> 176
~ __ZNK5raven22GNSSUncertaintyScaling34Fire6orOlderGNSSUncertaintyWrapper29GetUncertaintyScaleFactorCoreERKNS_18GNSSObservableTypeERKNS_8GnssBandERKNS_22RavenSignalEnvironmentERKNS_18RavenActivityStateERKNSt3__14pairImmEERKfNS0_30GNSSUncertaintyScaleFactorTypeE : 4444 -> 4452
~ __ZNK5raven22GNSSUncertaintyScaling39Fire7orNewerWatchGNSSUncertaintyWrapper29GetUncertaintyScaleFactorCoreERKNS_18GNSSObservableTypeERKNS_8GnssBandERKNS_22RavenSignalEnvironmentERKNS_18RavenActivityStateERKNSt3__14pairImmEERKfNS0_30GNSSUncertaintyScaleFactorTypeE : 3184 -> 3192
~ __ZNK5raven22GNSSUncertaintyScaling29Indus25GNSSUncertaintyWrapper29GetUncertaintyScaleFactorCoreERKNS_18GNSSObservableTypeERKNS_8GnssBandERKNS_22RavenSignalEnvironmentERKNS_18RavenActivityStateERKNSt3__14pairImmEERKfNS0_30GNSSUncertaintyScaleFactorTypeE : 6008 -> 6016
~ __ZN5raven24RavenFacetVisibilityData40ConstructPointToFacetVisibilityHierarchyERKNSt3__15arrayIdLm2EEEPKN18cnbuildinggeometry12BuildingDataIdEES5_ : 1832 -> 1828
~ sub_1d86b3b4c -> sub_1d7966cfc : 392 -> 396
~ __ZN5raven15RavenNLOSEngine21RefineApproximatePathERKN18cnbuildinggeometry7RayPathIdEERK6CNTimeRKN12cnnavigation15GNSSSatelliteIDERKN8cnvector10CNVector3DIdEE : 10992 -> 10932
~ sub_1d86cb8b8 -> sub_1d797ea30 : 368 -> 372
~ sub_1d86cdea0 -> sub_1d798101c : 344 -> 356
~ sub_1d86cdff8 -> sub_1d7981180 : 464 -> 476
~ sub_1d86ce310 -> sub_1d79814a4 : 1132 -> 1144
~ sub_1d86ce77c -> sub_1d798191c : 216 -> 220
~ __ZN5raven17RavenPNTEstimator16PredictAndUpdateERKNS0_37RavenPNTEstimatorPredictAndUpdateArgsE : 5760 -> 5736
~ __ZN5raven42ConvertProtobufToAsyncTrackingInsightEventERKN14CoreNavigation3CLP8LogEntry11PrivateData20AsyncTrackingInsightERNS_41GnssMeasurementsAsyncTrackingInsightEventE : 960 -> 968
~ __ZN5raven38RavenSequentialGNSSMeasurementSelector13SortedMSRData13RegisterGroupEjRKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEb : 1376 -> 1380
~ sub_1d87514fc -> sub_1d7a04694 : 128 -> 112
```
