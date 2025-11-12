## PeridotDepth

> `/System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth`

```diff

 49.0.0.0.0
-  __TEXT.__text: 0x137e78
+  __TEXT.__text: 0x137eac
   __TEXT.__auth_stubs: 0x1870
   __TEXT.__objc_methlist: 0x133c
   __TEXT.__const: 0x18d30

   __TEXT.__unwind_info: 0x1af8
   __TEXT.__eh_frame: 0xc0
   __TEXT.__objc_classname: 0x25a
-  __TEXT.__objc_methname: 0x4f6b
-  __TEXT.__objc_methtype: 0x588d
+  __TEXT.__objc_methname: 0x4f7b
+  __TEXT.__objc_methtype: 0x5909
   __TEXT.__objc_stubs: 0x2540
   __DATA_CONST.__got: 0x468
   __DATA_CONST.__const: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 123A7158-ECF1-3C8D-ABEE-09F05F803B23
+  UUID: 0EF1DE65-5F28-3D7C-89B3-4789258B5C8F
   Functions: 1494
   Symbols:   4127
   CStrings:  2513
Functions:
~ __ZN9GeomUtils9FindSpotsERKN8MathLibs10_CamParamsIdEERKNS0_7_SFOptsE11MatrixNxPtsILj3EdES9_6MatrixIdEdS9_ddddjjPS8_ILj1EdESD_SD_SD_ : 8680 -> 8696
~ __ZNSt3__16vectorI6MatrixIdENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 488 -> 492
~ __ZNSt3__16vectorIN10ImageUtils4BlobENS_9allocatorIS2_EEE8__appendEmRKS2_ : 664 -> 672
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN7peridot10DataBufferEEENS_19__map_value_compareIS7_SA_NS_4lessIS7_EELb1EEENS5_ISA_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRKS7_EEENSL_IJEEEEEENS_4pairINS_15__tree_iteratorISA_PNS_11__tree_nodeISA_PvEElEEbEERKT_DpOT0_ : 436 -> 444
~ -[GmoEngine specPhasePriOrder] : 396 -> 400
~ -[GmoController specsOut] : 444 -> 448
~ __ZNSt3__16vectorIN7peridot12ImgHistogramENS_9allocatorIS2_EEE8__appendEm : 1164 -> 1172
CStrings:
+ "T{vector<common::PeridotSpotValues<CGPoint>, std::allocator<common::PeridotSpotValues<CGPoint>>>=^v^v{?=^v}},R,N,V_localSpotsLocRefDist"
+ "T{vector<common::PeridotSpotValues<float>, std::allocator<common::PeridotSpotValues<float>>>=^v^v{?=^v}},R,N,V_localNa"
+ "T{vector<std::vector<SpecsResults>, std::allocator<std::vector<SpecsResults>>>=^v^v{?=^v}},R,N,V_specsOut"
+ "T{vector<std::vector<unsigned long>, std::allocator<std::vector<unsigned long>>>=^v^v{?=^v}},R,N,V_specPhasePriOrder"
+ "[4[8{PeridotDepth=\"spots\"[14{PeridotDepthSpot=\"HS\"{PeridotDepthSpotType=\"echos\"{vector<peridot::PeridotDepthSpotEcho, std::allocator<peridot::PeridotDepthSpotEcho>>=\"__begin_\"^{PeridotDepthSpotEcho}\"__end_\"^{PeridotDepthSpotEcho}\"\"{?=\"__cap_\"^{PeridotDepthSpotEcho}}}\"na\"f}\"HS2\"{PeridotDepthSpotType=\"echos\"{vector<peridot::PeridotDepthSpotEcho, std::allocator<peridot::PeridotDepthSpotEcho>>=\"__begin_\"^{PeridotDepthSpotEcho}\"__end_\"^{PeridotDepthSpotEcho}\"\"{?=\"__cap_\"^{PeridotDepthSpotEcho}}}\"na\"f}\"HP\"{PeridotDepthSpotType=\"echos\"{vector<peridot::PeridotDepthSpotEcho, std::allocator<peridot::PeridotDepthSpotEcho>>=\"__begin_\"^{PeridotDepthSpotEcho}\"__end_\"^{PeridotDepthSpotEcho}\"\"{?=\"__cap_\"^{PeridotDepthSpotEcho}}}\"na\"f}\"M1_wide\"{PeridotDepthSpotType=\"echos\"{vector<peridot::PeridotDepthSpotEcho, std::allocator<peridot::PeridotDepthSpotEcho>>=\"__begin_\"^{PeridotDepthSpotEcho}\"__end_\"^{PeridotDepthSpotEcho}\"\"{?=\"__cap_\"^{PeridotDepthSpotEcho}}}\"na\"f}\"M1_narrow\"{PeridotDepthSpotType=\"echos\"{vector<peridot::PeridotDepthSpotEcho, std::allocator<peridot::PeridotDepthSpotEcho>>=\"__begin_\"^{PeridotDepthSpotEcho}\"__end_\"^{PeridotDepthSpotEcho}\"\"{?=\"__cap_\"^{PeridotDepthSpotEcho}}}\"na\"f}\"SP\"{PeridotDepthSpotType=\"echos\"{vector<peridot::PeridotDepthSpotEcho, std::allocator<peridot::PeridotDepthSpotEcho>>=\"__begin_\"^{PeridotDepthSpotEcho}\"__end_\"^{PeridotDepthSpotEcho}\"\"{?=\"__cap_\"^{PeridotDepthSpotEcho}}}\"na\"f}}]\"detTh\"f}]]"
+ "{PeridotAlgo=\"_impl\"{unique_ptr<peridot::PeridotAlgo::Impl, std::default_delete<peridot::PeridotAlgo::Impl>>=\"\"{?=\"__ptr_\"^{Impl}}}}"
+ "{TimeSync=\"m_pointClouds\"{deque<TimeSync::TimestampedObject<ADJasperPointCloud *>, std::allocator<TimeSync::TimestampedObject<ADJasperPointCloud *>>>=\"__map_\"{__split_buffer<TimeSync::TimestampedObject<ADJasperPointCloud *> *, std::allocator<TimeSync::TimestampedObject<ADJasperPointCloud *> *>>=\"__first_\"^^v\"__begin_\"^^v\"__end_\"^^v\"\"{?=\"__cap_\"^^v}}\"__start_\"Q\"\"{?=\"__size_\"Q}}\"m_images\"{deque<TimeSync::TimestampedObject<TimeSync::Image>, std::allocator<TimeSync::TimestampedObject<TimeSync::Image>>>=\"__map_\"{__split_buffer<TimeSync::TimestampedObject<TimeSync::Image> *, std::allocator<TimeSync::TimestampedObject<TimeSync::Image> *>>=\"__first_\"^^v\"__begin_\"^^v\"__end_\"^^v\"\"{?=\"__cap_\"^^v}}\"__start_\"Q\"\"{?=\"__size_\"Q}}\"m_lock\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}\"m_numberOfBanksToMatch\"i}"
+ "{unique_ptr<bool[], std::default_delete<bool[]>>=\"\"{?=\"__ptr_\"^B}}"
+ "{unique_ptr<float[], std::default_delete<float[]>>=\"\"{?=\"__ptr_\"^f}}"
+ "{unique_ptr<unsigned long[], std::default_delete<unsigned long[]>>=\"\"{?=\"__ptr_\"^Q}}"
+ "{vector<common::PeridotSpotValues<CGPoint>, std::allocator<common::PeridotSpotValues<CGPoint>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
+ "{vector<common::PeridotSpotValues<CGPoint>, std::allocator<common::PeridotSpotValues<CGPoint>>>=^v^v{?=^v}}16@0:8"
+ "{vector<common::PeridotSpotValues<float>, std::allocator<common::PeridotSpotValues<float>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
+ "{vector<common::PeridotSpotValues<float>, std::allocator<common::PeridotSpotValues<float>>>=^v^v{?=^v}}16@0:8"
+ "{vector<std::vector<SpecsResults>, std::allocator<std::vector<SpecsResults>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
+ "{vector<std::vector<SpecsResults>, std::allocator<std::vector<SpecsResults>>>=^v^v{?=^v}}16@0:8"
+ "{vector<std::vector<unsigned long>, std::allocator<std::vector<unsigned long>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
+ "{vector<std::vector<unsigned long>, std::allocator<std::vector<unsigned long>>>=^v^v{?=^v}}16@0:8"
- "T{vector<common::PeridotSpotValues<CGPoint>, std::allocator<common::PeridotSpotValues<CGPoint>>>=^v^v^v},R,N,V_localSpotsLocRefDist"
- "T{vector<common::PeridotSpotValues<float>, std::allocator<common::PeridotSpotValues<float>>>=^v^v^v},R,N,V_localNa"
- "T{vector<std::vector<SpecsResults>, std::allocator<std::vector<SpecsResults>>>=^v^v^v},R,N,V_specsOut"
- "T{vector<std::vector<unsigned long>, std::allocator<std::vector<unsigned long>>>=^v^v^v},R,N,V_specPhasePriOrder"
- "[4[8{PeridotDepth=\"spots\"[14{PeridotDepthSpot=\"HS\"{PeridotDepthSpotType=\"echos\"{vector<peridot::PeridotDepthSpotEcho, std::allocator<peridot::PeridotDepthSpotEcho>>=\"__begin_\"^{PeridotDepthSpotEcho}\"__end_\"^{PeridotDepthSpotEcho}\"__cap_\"^{PeridotDepthSpotEcho}}\"na\"f}\"HS2\"{PeridotDepthSpotType=\"echos\"{vector<peridot::PeridotDepthSpotEcho, std::allocator<peridot::PeridotDepthSpotEcho>>=\"__begin_\"^{PeridotDepthSpotEcho}\"__end_\"^{PeridotDepthSpotEcho}\"__cap_\"^{PeridotDepthSpotEcho}}\"na\"f}\"HP\"{PeridotDepthSpotType=\"echos\"{vector<peridot::PeridotDepthSpotEcho, std::allocator<peridot::PeridotDepthSpotEcho>>=\"__begin_\"^{PeridotDepthSpotEcho}\"__end_\"^{PeridotDepthSpotEcho}\"__cap_\"^{PeridotDepthSpotEcho}}\"na\"f}\"M1_wide\"{PeridotDepthSpotType=\"echos\"{vector<peridot::PeridotDepthSpotEcho, std::allocator<peridot::PeridotDepthSpotEcho>>=\"__begin_\"^{PeridotDepthSpotEcho}\"__end_\"^{PeridotDepthSpotEcho}\"__cap_\"^{PeridotDepthSpotEcho}}\"na\"f}\"M1_narrow\"{PeridotDepthSpotType=\"echos\"{vector<peridot::PeridotDepthSpotEcho, std::allocator<peridot::PeridotDepthSpotEcho>>=\"__begin_\"^{PeridotDepthSpotEcho}\"__end_\"^{PeridotDepthSpotEcho}\"__cap_\"^{PeridotDepthSpotEcho}}\"na\"f}\"SP\"{PeridotDepthSpotType=\"echos\"{vector<peridot::PeridotDepthSpotEcho, std::allocator<peridot::PeridotDepthSpotEcho>>=\"__begin_\"^{PeridotDepthSpotEcho}\"__end_\"^{PeridotDepthSpotEcho}\"__cap_\"^{PeridotDepthSpotEcho}}\"na\"f}}]\"detTh\"f}]]"
- "{PeridotAlgo=\"_impl\"{unique_ptr<peridot::PeridotAlgo::Impl, std::default_delete<peridot::PeridotAlgo::Impl>>=\"__ptr_\"^{Impl}}}"
- "{TimeSync=\"m_pointClouds\"{deque<TimeSync::TimestampedObject<ADJasperPointCloud *>, std::allocator<TimeSync::TimestampedObject<ADJasperPointCloud *>>>=\"__map_\"{__split_buffer<TimeSync::TimestampedObject<ADJasperPointCloud *> *, std::allocator<TimeSync::TimestampedObject<ADJasperPointCloud *> *>>=\"__first_\"^^v\"__begin_\"^^v\"__end_\"^^v\"__cap_\"^^v}\"__start_\"Q\"__size_\"Q}\"m_images\"{deque<TimeSync::TimestampedObject<TimeSync::Image>, std::allocator<TimeSync::TimestampedObject<TimeSync::Image>>>=\"__map_\"{__split_buffer<TimeSync::TimestampedObject<TimeSync::Image> *, std::allocator<TimeSync::TimestampedObject<TimeSync::Image> *>>=\"__first_\"^^v\"__begin_\"^^v\"__end_\"^^v\"__cap_\"^^v}\"__start_\"Q\"__size_\"Q}\"m_lock\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}\"m_numberOfBanksToMatch\"i}"
- "{unique_ptr<bool[], std::default_delete<bool[]>>=\"__ptr_\"^B}"
- "{unique_ptr<float[], std::default_delete<float[]>>=\"__ptr_\"^f}"
- "{unique_ptr<unsigned long[], std::default_delete<unsigned long[]>>=\"__ptr_\"^Q}"
- "{vector<common::PeridotSpotValues<CGPoint>, std::allocator<common::PeridotSpotValues<CGPoint>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- "{vector<common::PeridotSpotValues<CGPoint>, std::allocator<common::PeridotSpotValues<CGPoint>>>=^v^v^v}16@0:8"
- "{vector<common::PeridotSpotValues<float>, std::allocator<common::PeridotSpotValues<float>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- "{vector<common::PeridotSpotValues<float>, std::allocator<common::PeridotSpotValues<float>>>=^v^v^v}16@0:8"
- "{vector<std::vector<SpecsResults>, std::allocator<std::vector<SpecsResults>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- "{vector<std::vector<SpecsResults>, std::allocator<std::vector<SpecsResults>>>=^v^v^v}16@0:8"
- "{vector<std::vector<unsigned long>, std::allocator<std::vector<unsigned long>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- "{vector<std::vector<unsigned long>, std::allocator<std::vector<unsigned long>>>=^v^v^v}16@0:8"

```
