## PredictedContextAlgorithms

> `/System/Library/PrivateFrameworks/PredictedContextAlgorithms.framework/PredictedContextAlgorithms`

```diff

-37.0.0.0.0
-  __TEXT.__text: 0x8db5c
+37.0.1.0.0
+  __TEXT.__text: 0x8da1c
   __TEXT.__auth_stubs: 0x10a0
   __TEXT.__objc_methlist: 0x6b0c
-  __TEXT.__const: 0xcf4
-  __TEXT.__cstring: 0x337d
-  __TEXT.__oslogstring: 0x643d
+  __TEXT.__const: 0xce4
+  __TEXT.__cstring: 0x3374
+  __TEXT.__oslogstring: 0x6261
   __TEXT.__swift5_typeref: 0x2e0
   __TEXT.__swift5_reflstr: 0x14d
   __TEXT.__swift5_assocty: 0x30

   __TEXT.__unwind_info: 0x1930
   __TEXT.__eh_frame: 0x628
   __TEXT.__objc_classname: 0x925
-  __TEXT.__objc_methname: 0xd4fc
-  __TEXT.__objc_methtype: 0x1756
-  __TEXT.__objc_stubs: 0x8ae0
-  __DATA_CONST.__got: 0x688
+  __TEXT.__objc_methname: 0xd4e3
+  __TEXT.__objc_methtype: 0x1764
+  __TEXT.__objc_stubs: 0x8ac0
+  __DATA_CONST.__got: 0x680
   __DATA_CONST.__const: 0xb68
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f08
+  __DATA_CONST.__objc_selrefs: 0x2f00
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x298
-  __DATA_CONST.__objc_arraydata: 0xf0
+  __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0x868
   __AUTH_CONST.__const: 0x830
-  __AUTH_CONST.__cfstring: 0x42e0
+  __AUTH_CONST.__cfstring: 0x42c0
   __AUTH_CONST.__objc_const: 0xacb8
   __AUTH_CONST.__objc_doubleobj: 0x180
-  __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x860
   __AUTH.__data: 0x1b0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DC427026-96DC-3D85-A91D-8BBB1AA38E21
+  UUID: 15928D03-9C0B-3D39-90E1-AD07E8C8AF07
   Functions: 2837
-  Symbols:   9208
-  CStrings:  4096
+  Symbols:   9206
+  CStrings:  4091
 
Symbols:
+ -[PCWorkoutAnnotationManager getContextEventsForBaseEvents:sortedEvents:]
+ _objc_msgSend$getContextEventsForBaseEvents:sortedEvents:
- -[PCWorkoutAnnotationManager getContextEventsForBaseEvents:events:]
- _OBJC_CLASS_$_NSCompoundPredicate
- _objc_msgSend$andPredicateWithSubpredicates:
- _objc_msgSend$getContextEventsForBaseEvents:events:
Functions:
~ __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne200100Em : 60 -> 64
~ -[PCWorkoutAnnotationManager getContextEventsForBaseEvents:events:] -> -[PCWorkoutAnnotationManager getContextEventsForBaseEvents:sortedEvents:] : 432 -> 476
~ -[PCWorkoutAnnotationManager performAnnotationWithEventsInternal:] : 1372 -> 1496
~ +[PCEmbeddingDistanceCalculator calculateDistanceFromFeatures:withWeights:fromEmbedding:toEmbedding:] : 2148 -> 1600
~ __ZN7Hdbscan7executeEiiNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 1688 -> 1700
~ __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE18__assign_with_sizeB8ne200100IPS3_S7_EEvT_T0_l : 376 -> 380
~ __ZNSt3__16vectorI17hdbscanConstraintNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorI12outlierScoreNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZN11hdbscanStar16hdbscanAlgorithm12constructMstENSt3__16vectorINS2_IdNS1_9allocatorIdEEEENS3_IS5_EEEES5_b : 1800 -> 1804
~ __ZN11hdbscanStar16hdbscanAlgorithm32calculateNumConstraintsSatisfiedERNSt3__13setIiNS1_4lessIiEENS1_9allocatorIiEEEERNS1_6vectorIP7clusterNS5_ISB_EEEERNS9_I17hdbscanConstraintNS5_ISF_EEEERNS9_IiS6_EE : 2140 -> 2144
~ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE9push_backB8ne200100ERKS3_ : 360 -> 368
~ __ZN11hdbscanStar16hdbscanAlgorithm19findMembershipScoreENSt3__16vectorIiNS1_9allocatorIiEEEENS2_IdNS3_IdEEEE : 856 -> 860
~ __ZN15cluster_factory16createNewClusterEiP7clusterdi : 396 -> 400
CStrings:
+ "getContextEventsForBaseEvents:sortedEvents:"
+ "v40@0:8{vector<std::vector<double>, std::allocator<std::vector<double>>>=^v^v{?=^v}}16"
+ "{unique_ptr<Hdbscan, std::default_delete<Hdbscan>>=\"\"{?=\"__ptr_\"^{Hdbscan}}}"
+ "{vector<std::vector<double>, std::allocator<std::vector<double>>>=^v^v{?=^v}}24@0:8@16"
- "%K IN %@"
- "Clustering: Weights: ActivityType=%.2f,ActivityContext=%.2f,TimeContext=%.2f,DurationNorm=%.2f,TimeOfDay=%.2f,DayOfWeek=%.2f,IsWeekend=%.2f,LocationContext=%.2f,PlaceName=%.2f,CombinedPlaceType=%.2f,GeographicalProximity=%.2f"
- "Clustering: fromEmbedding,%@,toEmbedding,%@,totalDistance,%.3f,activityContext,%.3f,activity,%.3f,timeContext,%.3f,durationNorm,%.3f,timeOfDay,%.3f,dayOfWeek,%.3f,isWeekend,%.3f,locationContext,%.3f,placeName,%.3f,combinedPlaceType,%.3f,geoProx,%.3f"
- "andPredicateWithSubpredicates:"
- "getContextEventsForBaseEvents:events:"
- "v40@0:8{vector<std::vector<double>, std::allocator<std::vector<double>>>=^v^v^v}16"
- "{unique_ptr<Hdbscan, std::default_delete<Hdbscan>>=\"__ptr_\"^{Hdbscan}}"
- "{vector<std::vector<double>, std::allocator<std::vector<double>>>=^v^v^v}24@0:8@16"

```
