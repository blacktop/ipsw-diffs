## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

```diff

 1592.40.6.0.0
-  __TEXT.__text: 0x2d2d20
+  __TEXT.__text: 0x2d2e2c
   __TEXT.__auth_stubs: 0x2f10
   __TEXT.__objc_methlist: 0x14f80
   __TEXT.__const: 0xbb98
-  __TEXT.__gcc_except_tab: 0x5eb0
-  __TEXT.__cstring: 0x88a8b
+  __TEXT.__gcc_except_tab: 0x5eac
+  __TEXT.__cstring: 0x88a8f
   __TEXT.__oslogstring: 0xa5db
   __TEXT.__dlopen_cstrs: 0x313
   __TEXT.__runtimeheader: 0xda3c

   __TEXT.__eh_frame: 0x208
   __TEXT.__objc_classname: 0x2a59
   __TEXT.__objc_methname: 0x204ad
-  __TEXT.__objc_methtype: 0x66c9
+  __TEXT.__objc_methtype: 0x66e5
   __TEXT.__objc_stubs: 0x10520
   __DATA_CONST.__got: 0xa78
   __DATA_CONST.__const: 0x7500

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CCD76CC1-9B87-3500-8DB4-261C37109975
+  UUID: A473A64F-0E5E-328B-A7E0-E619B44FDD8A
   Functions: 14022
   Symbols:   43382
   CStrings:  18051
Symbols:
+ ___block_descriptor_40_e8_32b_e113_{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}{?=^{CGRect}}}44?0i8{CGRect={CGPoint=dd}{CGSize=dd}}12ls32l8
+ ___block_descriptor_48_e8_32o40o_e113_{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}{?=^{CGRect}}}44?0i8{CGRect={CGPoint=dd}{CGSize=dd}}12ls32l8s40l8
- ___block_descriptor_40_e8_32b_e109_{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}^{CGRect}}44?0i8{CGRect={CGPoint=dd}{CGSize=dd}}12ls32l8
- ___block_descriptor_48_e8_32o40o_e109_{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}^{CGRect}}44?0i8{CGRect={CGPoint=dd}{CGSize=dd}}12ls32l8s40l8
Functions:
~ __ZN2CI21SoftwareDAGDescriptor12ArgumentInfo3addENS_18SWArgumentInfoTypeEm : 448 -> 452
~ __ZNSt3__16vectorIN2CI27SWRendererFunctionInputNodeENS_9allocatorIS2_EEE11__vallocateB8nn200100Em : 76 -> 80
~ __ZNSt3__16vectorIN2CI21SoftwareDAGDescriptor12ArgumentInfoENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRmEEEPS3_DpOT_ : 268 -> 272
~ __ZNSt3__16vectorIN2CI22SWRendererFunctionNodeENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRNS1_10SWFunctionERPNS0_INS1_27SWRendererFunctionInputNodeENS3_IS9_EEEEEEEPS2_DpOT_ : 280 -> 292
~ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZNSt3__16vectorIN2CI22SWRendererFunctionNodeENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKNS1_10SWFunctionERPNS0_INS1_27SWRendererFunctionInputNodeENS3_ISA_EEEEEEEPS2_DpOT_ : 280 -> 292
~ __ZN2CI21SoftwareDAGDescriptor23add_set_destcoord_nodesEv : 1656 -> 1660
~ __ZNSt3__16vectorIN2CI22SWRendererFunctionNodeENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 328 -> 332
~ __ZNSt3__16vectorIN2CI22SWRendererFunctionNodeENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKNS1_10SWFunctionERNS0_INS1_27SWRendererFunctionInputNodeENS3_ISA_EEEEEEEPS2_DpOT_ : 280 -> 292
~ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_4.120 : 944 -> 948
~ +[TiledHistogram processWithInputs:arguments:output:error:] : 548 -> 568
~ __ZNSt3__16vectorINS0_INS_4pairIdiEENS_9allocatorIS2_EEEENS3_IS5_EEE11__vallocateB8nn200100Em : 76 -> 80
~ __ZNSt3__16vectorI5IRectNS_9allocatorIS1_EEE11__vallocateB8nn200100Em : 76 -> 80
~ __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZN18CIKernelReflection7reflectEP15CIKernelLibraryPKcPP7NSError : 5424 -> 5428
~ -[CIKernel applyWithExtent:roiCallback:arguments:options:] : 2280 -> 2284
~ __ZNSt3__16vectorIN2CI18KernelArgumentTypeENS_9allocatorIS2_EEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8nn200100Em : 76 -> 80
~ ____ZN16CIKLLibraryMaker17analyzeCIKLSourceEP7__sFILEPKcS3__block_invoke : 2256 -> 2260
~ __ZNSt3__16vectorIsNS_9allocatorIsEEE11__vallocateB8nn200100Em : 56 -> 60
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE18__assign_with_sizeB8nn200100IPS6_SA_EEvT_T0_l : 416 -> 420
~ -[CIPerspectiveAutoCalcV1 compute] : 1060 -> 1052
~ -[CIPerspectiveAutoCalcV1 extractLineSegments] : 1500 -> 1504
~ __ZZ46-[CIPerspectiveAutoCalcV1 clusterLineSegments]ENK3$_0clERKNSt3__16vectorIN2CI11Perspective4LineENS0_9allocatorIS4_EEEEm : 1692 -> 1704
~ -[CIPerspectiveAutoCalcV1 computeGuides] : 2268 -> 2260
~ __ZNSt3__16vectorIN2CI11Perspective4LineENS_9allocatorIS3_EEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZZ46-[CIPerspectiveAutoCalcV2 clusterLineSegments]ENK3$_0clERKNSt3__16vectorIN2CI11Perspective4LineENS0_9allocatorIS4_EEEEm : 1684 -> 1696
~ __ZN2CI11Perspective9NMSimplexIDv3_fEC2ENS0_8NMParamsEU13block_pointerFfRKS2_EPS5_m : 992 -> 996
~ __ZN2CI11Perspective9NMSimplexIDv2_fEC2ENS0_8NMParamsEU13block_pointerFfRKS2_EPS5_m : 912 -> 916
~ __ZN2CI11Perspective10EDLinesCPU12extractLinesEv : 1324 -> 1332
~ -[CIEnhancementCalculation printHistogram:downsampledTo:] : 168 -> 184
~ __ZN2CI9SWContext11render_nodeEPNS_11ProgramNodeERK6CGRectS5_PKNS_6BitmapE : 3868 -> 3872
~ ____ZN2CI19MetalTextureManager23remove_matching_textureERKNSt3__16vectorINS_7TextureENS1_9allocatorIS3_EEEE_block_invoke : 444 -> 448
~ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZNSt3__16vectorIN2CI7TextureENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 288 -> 284
~ __ZN2CI15SerialRectArray7restoreEiRKNS_9parentROIE : 452 -> 456
~ __ZN2CI15SerialRectArray16recurseSubdivideERK6CGRectiRNSt3__16vectorIS1_NS4_9allocatorIS1_EEEE : 472 -> 476
~ __ZNSt3__16vectorIPKN2CI14intermediate_tENS_9allocatorIS4_EEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN2CI13ProgramDigestENS2_11ObjectCacheINS2_11MainProgramES3_Lb0EE5EntryEEENS_22__unordered_map_hasherIS3_S8_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S8_SD_SB_Lb1EEENS_9allocatorIS8_EEE21__emplace_unique_implIJRKNS_21piecewise_construct_tENS_5tupleIJRKS3_EEENSO_IJRKPS5_RyRKjEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEEDpOT_ : 188 -> 196
~ __ZNSt3__16vectorINS_4pairI6CGRectmEENS_9allocatorIS3_EEE11__vallocateB8nn200100Em : 76 -> 80
~ __ZN2CI19LegacyDAGDescriptor20create_argument_infoEm : 280 -> 284
~ __ZN2CI31StitchableFunctionDAGDescriptor20create_argument_infoEm : 340 -> 348
~ __ZN2CI17UberDAGDescriptor15create_pipelineEv : 4944 -> 4836
~ ____ZN2CI15ColorKernelNode14append_to_treeEPKNS_6KernelEPNS_20SerialObjectPtrArrayE6CGRectU13block_pointerFS6_iS6_EbbNS_11PixelFormatE_block_invoke : 400 -> 404
~ __ZNSt3__16vectorIP11__IOSurfaceNS_9allocatorIS2_EEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZNSt3__16vectorIbNS_9allocatorIbEEE11__vallocateB8nn200100Em : 68 -> 72
~ __ZNSt3__16vectorIN2CI9parentROIENS_9allocatorIS2_EEE11__vallocateB8nn200100Em : 76 -> 80
~ __ZNK2CI12ProviderNode13surfaceForROIEPKNS_7ContextERK6CGRectRNS_8Tileable5StatsE : 1468 -> 1472
~ __ZNSt3__16vectorIN2CI15SerialRectArray7roiDataENS_9allocatorIS3_EEE18__assign_with_sizeB8nn200100IPS3_S8_EEvT_T0_l : 340 -> 344
~ __ZNSt3__16vectorIN2CI15SerialRectArray7roiDataENS_9allocatorIS3_EEE11__vallocateB8nn200100Em : 76 -> 80
~ __ZNSt3__16vectorIN2CI15SerialRectArray7roiDataENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_ : 296 -> 308
~ __ZN2CI11GraphObject27traverse_preorder_stoppableEPS0_S1_iiU13block_pointerFbS1_S1_iiE : 780 -> 804
~ __ZN2CI11GraphObject27traverse_preorder_stoppableEPKS0_S2_iiU13block_pointerFbS2_S2_iiE : 780 -> 804
~ __ZN2CI11GraphObject18traverse_stoppableEPS0_S1_iiU13block_pointerFbS1_S1_iiEU13block_pointerFvS1_S1_iiE : 680 -> 688
~ __ZN2CI11GraphObject18traverse_stoppableEPKS0_S2_iiU13block_pointerFbS2_S2_iiEU13block_pointerFvS2_S2_iiE : 680 -> 688
~ __ZNSt3__16vectorIN2CI13TraverseVisitENS_9allocatorIS2_EEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZNSt3__16vectorIN2CI18ConstTraverseVisitENS_9allocatorIS2_EEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZN2CIL17recurseGraphStatsEPNS_4NodeES1_iRNSt3__16vectorIPKS0_NS2_9allocatorIS5_EEEEiPNS2_3mapIS5_NS_13useCountDepthENS2_4lessIS5_EENS6_INS2_4pairIKS5_SB_EEEEEE : 1132 -> 1136
~ __ZN2CI15SerialRectArray18updateSubGraphLoadEimj : 404 -> 408
~ __ZN2CIL23_traverse_program_graphENS_6roiKeyERNS_8liveROIsES2_ : 904 -> 908
~ __ZNSt3__16vectorIN2CI8roiTupleENS_9allocatorIS2_EEE11__vallocateB8nn200100Em : 76 -> 80
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_11ProgramNodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE21__emplace_unique_implIJRKNS_21piecewise_construct_tENS_5tupleIJRKyEEENSN_IJRKPS4_RyRKjEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEEbEEDpOT_ : 188 -> 196
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_4NodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE21__emplace_unique_implIJRKNS_21piecewise_construct_tENS_5tupleIJRKyEEENSN_IJRKPS4_RyRKjEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEEbEEDpOT_ : 188 -> 196
~ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZNSt3__15dequeIPN2CI17SurfaceCacheEntryENS_9allocatorIS3_EEE19__add_back_capacityEv : 372 -> 376
~ __ZNSt3__114__split_bufferIPPN2CI17SurfaceCacheEntryENS_9allocatorIS4_EEE13emplace_frontIJS4_EEEvDpOT_ : 268 -> 272
~ __ZN2CI10RenderTask11addTileTaskEPNS_8TileTaskE : 276 -> 280
CStrings:
+ "@136@0:8{CIKernelReflection=ii***{vector<CI::KernelArgumentType, std::allocator<CI::KernelArgumentType>>=^i^i{?=^i}}{vector<std::string, std::allocator<std::string>>=^v^v{?=^v}}@IiQQBB}16"
+ "@152@0:8{CIKernelReflection=ii***{vector<CI::KernelArgumentType, std::allocator<CI::KernelArgumentType>>=^i^i{?=^i}}{vector<std::string, std::allocator<std::string>>=^v^v{?=^v}}@IiQQBB}16@136@144"
+ "{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}{?=^{CGRect}}}44@?0i8{CGRect={CGPoint=dd}{CGSize=dd}}12"
+ "{vector<CI::Perspective::Line, std::allocator<CI::Perspective::Line>>=\"__begin_\"^{?}\"__end_\"^{?}\"\"{?=\"__cap_\"^{?}}}"
+ "{vector<LineCostProxy, std::allocator<LineCostProxy>>=\"__begin_\"^{LineCostProxy}\"__end_\"^{LineCostProxy}\"\"{?=\"__cap_\"^{LineCostProxy}}}"
- "@136@0:8{CIKernelReflection=ii***{vector<CI::KernelArgumentType, std::allocator<CI::KernelArgumentType>>=^i^i^i}{vector<std::string, std::allocator<std::string>>=^v^v^v}@IiQQBB}16"
- "@152@0:8{CIKernelReflection=ii***{vector<CI::KernelArgumentType, std::allocator<CI::KernelArgumentType>>=^i^i^i}{vector<std::string, std::allocator<std::string>>=^v^v^v}@IiQQBB}16@136@144"
- "{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}^{CGRect}}44@?0i8{CGRect={CGPoint=dd}{CGSize=dd}}12"
- "{vector<CI::Perspective::Line, std::allocator<CI::Perspective::Line>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
- "{vector<LineCostProxy, std::allocator<LineCostProxy>>=\"__begin_\"^{LineCostProxy}\"__end_\"^{LineCostProxy}\"__cap_\"^{LineCostProxy}}"

```
