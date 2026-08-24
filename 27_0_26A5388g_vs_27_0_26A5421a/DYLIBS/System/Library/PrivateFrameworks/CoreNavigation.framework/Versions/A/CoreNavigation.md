## CoreNavigation

> `/System/Library/PrivateFrameworks/CoreNavigation.framework/Versions/A/CoreNavigation`

```diff

-424.0.0.0.0
-  __TEXT.__text: 0x35f1f0
+425.0.0.0.0
+  __TEXT.__text: 0x35f2b8
   __TEXT.__objc_methlist: 0x198
-  __TEXT.__const: 0x52011
-  __TEXT.__cstring: 0x385dc
+  __TEXT.__const: 0x51fb1
+  __TEXT.__cstring: 0x3863c
   __TEXT.__oslogstring: 0x51
   __TEXT.__gcc_except_tab: 0x1673c
   __TEXT.__unwind_info: 0xea50

   - /usr/lib/libobjc.A.dylib
   Functions: 15550
   Symbols:   13547
-  CStrings:  3915
+  CStrings:  3917
 
Functions:
~ __ZN5raven31RavenDeviceAttitudeActiveObject35UpdateDeviceAttitudeByWahbaSolutionERKNS_13TimeMarkEventE : 6096 -> 6100
~ __ZN5raven31RavenDeviceAttitudeActiveObject9ConfigureERKNS_41RavenDeviceAttitudeActiveObjectConfigArgsE : 1260 -> 1256
~ __ZNK5raven25RavenSolutionActiveObject28WriteRavenSolutionToProtobufERKNS_18RavenSolutionEventE : 660 -> 668
~ __ZN5raven15RavenSupervisorD2Ev : 1304 -> 1308
~ sub_1c7d6a3f0 -> sub_1c73ed3fc : 744 -> 728
~ __ZN5raven15RavenSupervisor9ConfigureEv : 51296 -> 51292
~ sub_1c7d7e2f4 -> sub_1c74012ec : 2852 -> 2824
~ __ZNK5raven27GnssMeasurementPreprocessor19FormAveragedDopplerERKNS_15GnssMeasurementENS_22GnssMultipathIndicatorEdRKNSt3__18optionalIdEERKNS_24GnssSvAndMeasurementDataE : 512 -> 572
~ __ZN5raven27GnssMeasurementPreprocessor36FormAveragedDopplerFromPhaseTrackingERKNS_15GnssMeasurementERKN12cnnavigation15GNSSSatelliteIDENS_22GnssMultipathIndicatorEdRKNSt3__18optionalIdEERKNS_24GnssSvAndMeasurementDataE : 728 -> 764
~ __ZN5raven25RavenConvergenceEstimator9ConfigureERKNS_24RavenEstimatorConfigArgsE : 1452 -> 1460
~ __ZNK5raven25RavenConvergenceEstimator37GetEstimatorPredictAndUpdateArgumentsERK6CNTimeS3_RNS0_45RavenConvergenceEstimatorPredictAndUpdateArgsE : 280 -> 276
~ __ZNK5raven24RavenIonosphereEstimator37GetEstimatorPredictAndUpdateArgumentsERK6CNTimeS3_RNS0_35RavenIonosphereEstimatorPredictArgsE : 352 -> 344
~ __ZNK5raven9MSRLogger14LogEpochFooterERKNSt3__14listINS_7MSRDataENS1_9allocatorIS3_EEEERKNS_28MeasurementEvaluationContextERKNS_9RavenTimeERKNS0_17PVTLoggingHistoryEPKN13referencedata18ReferenceDataStore15GMATDataCaptureE : 136 -> 144
~ __ZNK5raven9MSRLogger10LogMSRDataERKNSt3__14listINS_7MSRDataENS1_9allocatorIS3_EEEERKNS_28MeasurementEvaluationContextERKNS_9RavenTimeE : 10276 -> 10284
~ __ZN5raven15RavenParameters22ParseConfigurationFileEv : 32764 -> 32876
~ __ZN5raven15RavenParametersC2ERKNS_17RavenPlatformInfoE : 4480 -> 4504
~ __ZNK5raven15RavenParameters38GetDebugMsrLoggingFilenameForEstimatorERKNS_18RavenEstimatorTypeE : 720 -> 724
~ __ZN5raven25RavenLineOfSightEstimator7PredictERKNS0_11PredictArgsE : 1524 -> 1520
~ __ZN5raven17RavenPNTEstimator9ConfigureERKNS_24RavenEstimatorConfigArgsE : 2588 -> 2596
~ __ZNK5raven17RavenPNTEstimator37GetEstimatorPredictAndUpdateArgumentsERK6CNTimeS3_RNS0_37RavenPNTEstimatorPredictAndUpdateArgsE : 1168 -> 1160
~ __ZNK5raven17RavenPNTEstimator43GetSimplifiedEightStateEstimatorPredictArgsERK6CNTimeS3_RNS0_45RavenSimplifiedEightStateEstimatorPredictArgsE : 280 -> 276
~ __ZN5raven38RavenSequentialGNSSMeasurementSelector18SelectMeasurementsERKNS_33GnssPreprocessedMeasurementsEventERNSt3__14listINS_7MSRDataENS4_9allocatorIS6_EEEERNS4_8optionalIdEE : 1028 -> 1036
~ __ZN5raven29RavenPositionContextEstimator19HmmPredictAndUpdateERKNS_12GnssEvidenceE : 1228 -> 1224
~ __ZN5raven29RavenPositionContextEstimator19HmmPredictAndUpdateERKNS_21ActivityStateEvidenceE : 808 -> 804
~ __ZN5raven29RavenPositionContextEstimator19HmmPredictAndUpdateERKNS_20AvailabilityEvidenceE : 792 -> 788
CStrings:
+ "gnss_preprocessor_avg_doppler_min_unc_mps"
+ "gnss_preprocessor_disable_avg_doppler_when_driving"
```
