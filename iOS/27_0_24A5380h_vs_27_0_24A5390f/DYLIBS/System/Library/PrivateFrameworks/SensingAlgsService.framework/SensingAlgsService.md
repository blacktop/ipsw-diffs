## SensingAlgsService

> `/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-68.0.0.0.0
-  __TEXT.__text: 0x20d88
+70.0.0.0.0
+  __TEXT.__text: 0x210d0
   __TEXT.__objc_methlist: 0x7f0
-  __TEXT.__gcc_except_tab: 0xe7c
-  __TEXT.__const: 0x1ccb
-  __TEXT.__cstring: 0x3de
-  __TEXT.__oslogstring: 0x17b4
+  __TEXT.__gcc_except_tab: 0xe88
+  __TEXT.__const: 0x1cdb
+  __TEXT.__cstring: 0x3df
+  __TEXT.__oslogstring: 0x1796
   __TEXT.__unwind_info: 0xad0
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x5a0
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x20c0
+  __AUTH_CONST.__const: 0x20f8
   __AUTH_CONST.__cfstring: 0x3c0
   __AUTH_CONST.__objc_const: 0xb78
   __AUTH_CONST.__weak_auth_got: 0x20

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 780
-  Symbols:   1497
+  Symbols:   1502
   CStrings:  155
 
Symbols:
+ GCC_except_table35
+ __ZN13PlainDataNodeIfED0Ev
+ __ZN13PlainDataNodeIfED1Ev
+ __ZNK13PlainDataNodeIfE12sendCallbackEPFvRK22AlgDataCallbackContentERS1_
+ __ZTV13PlainDataNodeIfE
Functions:
~ __ZN12TouchService22TouchServiceActivePlan17runBeforeChildrenEv : 528 -> 540
~ __ZN13PalmRejection17PalmRejectionTaskC2ER13PlainDataNodeIbERK9TimeStateRKS1_INS_17PalmRejectionInfoEERN12TouchService19PlainPathCollectionERKS1_I18PalmRejSurfaceInfoERK20SA1DArrayDynamicSizeIfESL_ : 2064 -> 2268
~ __ZN13PalmRejection17PalmRejectionTask20runNodeRegistrationsEv : 468 -> 500
~ __ZN28SA2DArrayDynamicSizeWithSyncIfED1Ev -> __ZN27InterpolationParamsDataNodeD1Ev : 4 -> 32
~ __ZN27InterpolationParamsDataNodeD1Ev -> __ZN28SA2DArrayDynamicSizeWithSyncIfED1Ev : 32 -> 4
~ __ZN13PalmRejection17PalmRejectionTask16runAfterChildrenEv : 936 -> 1092
~ __ZN13PalmRejection17PalmRejectionTaskD2Ev : 400 -> 448
~ __ZN13PlainDataNodeIN13PalmRejection17PalmRejTaskParamsEEC2Ey9MemType_tb : 1104 -> 1108
~ __ZN13PalmRejection40CalculateMetaClassifierProbabilitiesStep3runEv : 2072 -> 2128
~ __ZN13PalmRejection27GetClusterLevelFeaturesStep3runEv : 3120 -> 3164
~ __ZN13PalmRejection31UpdatePalmRejectionFeaturesStep24calculatePathProbabilityERNS_11PmRjPathTrkEt : 1824 -> 1892
~ __ZN13PalmRejection28UpdatePathAssignedFingerStep3runEv : 572 -> 604
~ __ZN13PalmRejection34UpdateTouchHoverDetectionFlagsStep3runEv : 264 -> 272
~ __ZN13PalmRejection33DetermineClustersForRejectionStep3runEv : 2088 -> 2052
~ __ZN13PalmRejection20ParseContactDataStep30updatePathCollectionAndExtremaEv : 564 -> 608
~ __ZN13PalmRejection20ParseContactDataStep21detectPathTransitionsERNS_11PmRjPathTrkE : 152 -> 160
~ __ZN13PalmRejection20ParseContactDataStep20detectAndSetPathMakeERNS_11PmRjPathTrkE : 76 -> 84
~ __ZN13PalmRejection35ClusterWithGaussianMixtureModelStep21GMMPathInitializationENS_12DistToWeightE : 572 -> 596
~ __ZN13PalmRejection35ClusterWithGaussianMixtureModelStep27GMMClusterCovInitializationEt : 404 -> 444
~ __ZN13PalmRejection35ClusterWithGaussianMixtureModelStep35populateAllPathGMMCovarianceObjectsEv : 236 -> 268
~ __ZN13PalmRejection35ClusterWithGaussianMixtureModelStep25updateClusterCovColLogDetERNS_16GMMCovCollectionE : 104 -> 132
~ __ZN13PalmRejection35ClusterWithGaussianMixtureModelStep12swapAndScoreERNS_20GMMClusterCollectionERKS1_RKNS_11PmRjPathTrkE : 528 -> 556
CStrings:
+ "21.0.0 (clang-2100.3.27.1) [+internal-os]"
+ "24A5380i"
+ "Edge grip (per-path): path %d mindist=%.0f pencil_cos=%.4f touch_seen_pencil=%.4f\n"
+ "SensingAlgsService-70~23"
- "21.0.0 (clang-2100.3.25.1) [+internal-os]"
- "24A375"
- "Edge grip (per-path): path %d mindist=%.0f pencil_cos=%.4f touch_seen_pencil=%.4f -> marking cluster %d as palm\n"
- "SensingAlgsService-68~214"
```
