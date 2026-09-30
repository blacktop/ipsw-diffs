## CoreNavigation

> `/System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation`

```diff

 364.0.2.0.0
-  __TEXT.__text: 0x303798
+  __TEXT.__text: 0x303b3c
   __TEXT.__auth_stubs: 0x10a0
   __TEXT.__const: 0x4cb2f
-  __TEXT.__gcc_except_tab: 0x15300
+  __TEXT.__gcc_except_tab: 0x15304
   __TEXT.__cstring: 0x31c8f
   __TEXT.__oslogstring: 0xe
-  __TEXT.__unwind_info: 0xc880
+  __TEXT.__unwind_info: 0xc888
   __DATA_CONST.__got: 0x2e0
   __DATA_CONST.__const: 0x770
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: F787148C-36AD-395B-9E8A-7346C1E339E4
+  UUID: BD043482-27F3-3D68-A156-0D6FF2869FF5
   Functions: 13638
   Symbols:   11471
   CStrings:  3468
Functions:
~ sub_1d1761020 -> sub_1d1955020 : 468 -> 472
~ sub_1d17752e4 -> sub_1d19692e8 : 268 -> 272
~ sub_1d177ae2c -> sub_1d196ee34 : 60 -> 64
~ sub_1d177bb3c -> sub_1d196fb48 : 468 -> 472
~ __ZN5raven14RavenEstimator23StoreHistoricalSolutionEv : 2292 -> 2284
~ sub_1d179262c -> sub_1d1986634 : 60 -> 64
~ sub_1d1792668 -> sub_1d1986674 : 320 -> 324
~ sub_1d1798e34 -> sub_1d198ce44 : 212 -> 208
~ __ZNK5raven38RavenSequentialGNSSMeasurementSelector10LogMSRDataERKNSt3__14listINS0_7MSRDataENS1_9allocatorIS3_EEEE : 10500 -> 10508
~ sub_1d17c4c08 -> sub_1d19b8c1c : 352 -> 364
~ __ZN5raven17RavenPNTEstimator11HandleEventERKNS_33GnssPreprocessedMeasurementsEventE : 25100 -> 25116
~ sub_1d17e745c -> sub_1d19db48c : 468 -> 472
~ sub_1d17e78c0 -> sub_1d19db8f4 : 468 -> 472
~ sub_1d18071b0 -> sub_1d19fb1e8 : 1368 -> 1376
~ sub_1d1807760 -> sub_1d19fb7a0 : 60 -> 64
~ sub_1d180786c -> sub_1d19fb8b0 : 76 -> 80
~ __ZNK5raven14GnssSvDatabase18PopulateGnssSvDataERKNSt3__18optionalINS1_3setIN12cnnavigation15GNSSSatelliteIDENS1_4lessIS5_EENS1_9allocatorIS5_EEEEEERNS1_6vectorINS1_10shared_ptrINS_24GnssSvAndMeasurementDataEEENS8_ISH_EEEERNS4_17GNSSUTCParametersE : 1296 -> 1288
~ sub_1d180e994 -> sub_1d1a029d4 : 60 -> 64
~ __ZNK5raven27GnssMeasurementPreprocessor29EstimateCoarseReceiverTaiTimeERKNS_19GnssMeasurementDataERKNSt3__13mapIN12cnnavigation15GNSSSatelliteIDEPNS_24GnssSvAndMeasurementDataENS4_4lessIS7_EENS4_9allocatorINS4_4pairIKS7_S9_EEEEEERNS6_7TAITimeE : 2560 -> 2564
~ __ZN5raven35GNSSPreprocessedMeasurementsChecker31UpdateAndPopulateProbabilityLOSERNS_33GnssPreprocessedMeasurementsEventE : 4028 -> 3996
~ __ZN5raven35GNSSPreprocessedMeasurementsChecker22RemoveOldLOSEstimatorsERK6CNTime : 672 -> 668
~ __ZN5raven35ConvertProtobufToMapsRouteHintEventERKN14CoreNavigation3CLP8LogEntry11PrivateData20MapMatchingRouteHintERNS_18MapsRouteHintEventE : 1000 -> 1004
~ sub_1d18298c8 -> sub_1d1a1d8f0 : 268 -> 272
~ __ZN12cnnavigation24GalileoEphemerisDatabase14SetEphemeridesERKNS_18GalileoEphemeridesE : 688 -> 696
~ __ZN12cnnavigation33SphericalHarmonicsIonosphereModel16UpdateParametersERKNS_38SphericalHarmonicsIonosphereParametersE : 1644 -> 1652
~ __ZN12cnnavigation23BeiDouEphemerisDatabase14SetEphemeridesERKNS_17BeiDouEphemeridesE : 592 -> 600
~ __ZN5raven15RavenParameters40ParseAndValidateLowerLimitsOfLowPLOSBinsERNSt3__15arrayIdLm4EEEPKc : 1036 -> 1044
~ __ZN5raven15RavenParameters49ParseAndValidateLowPLOSPsrTargetSigmaScaleFactorsERNSt3__15arrayIdLm4EEEPKc : 1028 -> 1036
~ __ZN5raven15RavenParameters22ParseConfigurationFileEv : 30740 -> 30796
~ sub_1d191305c -> sub_1d1b070e8 : 764 -> 768
~ sub_1d1913358 -> sub_1d1b073e8 : 764 -> 768
~ sub_1d1913654 -> sub_1d1b076e8 : 804 -> 808
~ sub_1d1913aa0 -> sub_1d1b07b38 : 804 -> 808
~ sub_1d1913e60 -> sub_1d1b07efc : 1088 -> 1092
~ sub_1d19142a0 -> sub_1d1b08340 : 824 -> 828
~ sub_1d19145d8 -> sub_1d1b0867c : 740 -> 744
~ __ZN5raven24RavenFacetVisibilityData40ConstructFacetToFacetVisibilityHierarchyEPKN18cnbuildinggeometry13BuildingFacetIdEERKN20wireless_diagnostics6google8protobuf13RepeatedFieldIjEERKN14CoreNavigation3CLP8LogEntry18RayTracingTileData21RayTracingTilePayloadEhPKNS1_12BuildingDataIdEERKNSt3__15arrayIdLm2EEE : 2228 -> 2224
~ __ZN5raven24RavenFacetVisibilityData40ConstructPointToFacetVisibilityHierarchyERKNSt3__15arrayIdLm2EEEPKN18cnbuildinggeometry12BuildingDataIdEES5_ : 1948 -> 1952
~ sub_1d191b56c -> sub_1d1b0f614 : 160 -> 164
~ sub_1d191b7e4 -> sub_1d1b0f890 : 216 -> 220
~ sub_1d191b8bc -> sub_1d1b0f96c : 220 -> 216
~ sub_1d1955a2c -> sub_1d1b49ad8 : 332 -> 336
~ sub_1d1958f60 -> sub_1d1b4d010 : 80 -> 84
~ sub_1d19641bc -> sub_1d1b58270 : 984 -> 988
~ sub_1d1975ee0 -> sub_1d1b69f98 : 296 -> 292
~ sub_1d1978374 -> sub_1d1b6c428 : 396 -> 400
~ sub_1d1982bb4 -> sub_1d1b76c6c : 700 -> 704
~ __ZN5raven15RavenSupervisor9ConfigureEv : 73640 -> 74204
~ sub_1d1994f24 -> sub_1d1b89214 : 1192 -> 1200
~ sub_1d19953cc -> sub_1d1b896c4 : 480 -> 472
~ sub_1d19955ac -> sub_1d1b8989c : 480 -> 472
~ sub_1d199578c -> sub_1d1b89a74 : 480 -> 472
~ sub_1d199596c -> sub_1d1b89c4c : 480 -> 472
~ sub_1d1995b4c -> sub_1d1b89e24 : 480 -> 472
~ sub_1d1995d2c -> sub_1d1b89ffc : 480 -> 472
~ sub_1d1995f0c -> sub_1d1b8a1d4 : 480 -> 472
~ sub_1d199d7bc -> sub_1d1b91a7c : 668 -> 664
~ sub_1d199e9a8 -> sub_1d1b92c64 : 76 -> 80
~ sub_1d19b1c68 -> sub_1d1ba5f28 : 632 -> 644
~ __ZN5raven40ConvertProtobufToGEOMapBuildingDataEventERKN14CoreNavigation3CLP8LogEntry11PrivateData18GEOMapBuildingDataERNS_23GEOMapBuildingDataEventE : 2668 -> 2712
~ sub_1d19b9fb8 -> sub_1d1bae2b0 : 192 -> 208
~ __ZN5raven32RavenUserGaitTrackerActiveObject22InitializeGaitTrackingEi : 336 -> 340
~ __ZN5raven15RavenNLOSEngine31UpdateCandidatePointSearchSpaceERKN8cnvector10CNVector3DIdEERKN8cnmatrix8CNMatrixILj3ELj3EdEEPKN18cnbuildinggeometry12BuildingDataIdEE : 3072 -> 3088
~ __ZN5raven15RavenNLOSEngine21RefineApproximatePathERKN18cnbuildinggeometry7RayPathIdEERK6CNTimeRKN12cnnavigation15GNSSSatelliteIDERKN8cnvector10CNVector3DIdEE : 11164 -> 11168
~ sub_1d19de310 -> sub_1d1bd2630 : 860 -> 864
~ sub_1d19e146c -> sub_1d1bd5790 : 568 -> 556
~ __ZN5raven24RavenIonosphereEstimator51UpdateEstimatorParametersViaPolyfitToKlobucharModelEv : 2108 -> 2116
~ sub_1d1a065ec -> sub_1d1bfa90c : 1056 -> 1060
~ __ZN5raven33RavenDeltaVIOEstimateActiveObject5ResetEv : 1264 -> 1248
~ sub_1d1a1a314 -> sub_1d1c0e628 : 320 -> 324
~ sub_1d1a1b93c -> sub_1d1c0fc54 : 136 -> 148
~ sub_1d1a23ca4 -> sub_1d1c17fc8 : 60 -> 64
~ sub_1d1a26150 -> sub_1d1c1a478 : 3288 -> 3280
~ sub_1d1a2b5d8 -> sub_1d1c1f8f8 : 4216 -> 4180
~ sub_1d1a2c650 -> sub_1d1c2094c : 812 -> 816
~ __ZN4swan16FixedLagSmoother13ExtractOutputERNSt3__16vectorIdNS1_9allocatorIdEEEERNS2_INS_17SignalEnvironmentENS3_IS7_EEEES6_RNS2_IN8cnmatrix8CNMatrixILj6ELj1EdEENS3_ISD_EEEERNS2_INSC_ILj6ELj6EdEENS3_ISH_EEEEb : 1816 -> 1804
~ sub_1d1a33758 -> sub_1d1c27a4c : 224 -> 228
~ sub_1d1a33838 -> sub_1d1c27b30 : 220 -> 224
~ __ZN8trackrun44ConvertProtobufToGEOMapRunningTrackDataEventERKN14CoreNavigation3CLP8LogEntry11PrivateData25GEOMapTropicalSavannaDataERNS_27GEOMapRunningTrackDataEventE : 4928 -> 4932
~ sub_1d1a35898 -> sub_1d1c29b98 : 232 -> 248
~ __ZN8trackrun26TrackRunEngineActiveObject11HandleEventERKNS_27GEOMapRunningTrackDataEventE : 3792 -> 3872
~ sub_1d1a3dbac -> sub_1d1c31f0c : 528 -> 540
~ sub_1d1a3f9ac -> sub_1d1c33d18 : 80 -> 84
~ sub_1d1a3fb8c -> sub_1d1c33efc : 80 -> 84
~ sub_1d1a3fca8 -> sub_1d1c3401c : 496 -> 548
~ sub_1d1a3ffc4 -> sub_1d1c3436c : 60 -> 64
~ __ZN8trackrun18TrackRunSupervisor9ConfigureEv : 2820 -> 2812
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CBS3ugDo6h_6c8a4axt3Fo_W8VblQVUQ1eJUXt4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/boost/geometry/algorithms/centroid.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CBS3ugDo6h_6c8a4axt3Fo_W8VblQVUQ1eJUXt4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/boost/rational.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CBS3ugDo6h_6c8a4axt3Fo_W8VblQVUQ1eJUXt4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/4~CBS3ugDo6h_6c8a4axt3Fo_W8VblQVUQ1eJUXt4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "/AppleInternal/Library/BuildRoots/4~CAS1ugDhB0OQdoR4BWSlfCWy7GhcH7LoVciuU1A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/boost/geometry/algorithms/centroid.hpp"
- "/AppleInternal/Library/BuildRoots/4~CAS1ugDhB0OQdoR4BWSlfCWy7GhcH7LoVciuU1A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/boost/rational.hpp"
- "/AppleInternal/Library/BuildRoots/4~CAS1ugDhB0OQdoR4BWSlfCWy7GhcH7LoVciuU1A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/4~CAS1ugDhB0OQdoR4BWSlfCWy7GhcH7LoVciuU1A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"

```
