## SceneKit

> `/System/Library/Frameworks/SceneKit.framework/SceneKit`

```diff

 608.100.0.0.0
-  __TEXT.__text: 0x36c370
+  __TEXT.__text: 0x36c458
   __TEXT.__auth_stubs: 0x2f00
   __TEXT.__objc_methlist: 0x17924
   __TEXT.__const: 0x262a8

   __TEXT.__unwind_info: 0xaf60
   __TEXT.__objc_classname: 0x1d04
   __TEXT.__objc_methname: 0x248d5
-  __TEXT.__objc_methtype: 0x121c5
+  __TEXT.__objc_methtype: 0x12213
   __TEXT.__objc_stubs: 0x1d5e0
   __DATA_CONST.__got: 0xbf0
   __DATA_CONST.__const: 0x7b18

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CDC76820-336D-35D8-B610-E9A79648FECF
+  UUID: E37AC958-3BFC-3EB4-93C7-5F7AE95C8ACC
   Functions: 19167
   Symbols:   56932
   CStrings:  20410
Functions:
~ __ZN15ShaderConverter5ParseEb : 1356 -> 1348
~ __ZNSt3__16vectorIP9StatementNS_9allocatorIS2_EEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_19__map_value_compareIS7_S8_NS_4lessIS7_EELb1EEENS5_IS8_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJOS7_EEENSJ_IJEEEEEENS_4pairINS_15__tree_iteratorIS8_PNS_11__tree_nodeIS8_PvEElEEbEERKT_DpOT0_ : 204 -> 208
~ __ZNSt3__16vectorI8VariableNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_ : 384 -> 388
~ __Z29_createIndexedGeometryElementItEP18SCNGeometryElementP10MDLSubmesh : 812 -> 816
~ __Z29_createIndexedGeometryElementIjEP18SCNGeometryElementP10MDLSubmesh : 820 -> 824
~ __ZN12_GLOBAL__N_111_findMeshesEP9MDLObjectRK13simd_float4x4P14NSMutableArrayIP7MDLMeshERNSt3__16vectorIS2_NSA_9allocatorIS2_EEEE : 652 -> 656
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZN18__C3DCullingSystem10_newHandleEj : 272 -> 276
~ __ZN21WireframeMeshRenderer11AddInstanceEP9__C3DMesh9C3DColor412C3DMatrix4x4 : 280 -> 284
~ __ZNSt3__16vectorIN5vmesh8TriangleENS_9allocatorIS2_EEE11__vallocateB8nn200100Em : 76 -> 80
~ __ZNSt3__16vectorIN10OpenSubdiv6v3_1_13Osd10PatchArrayENS_9allocatorIS4_EEE11__vallocateB8nn200100Em : 60 -> 64
~ __ZNSt3__16vectorINS0_INS0_I7CFRangeNS_9allocatorIS1_EEEENS2_IS4_EEEENS2_IS6_EEE11__vallocateB8nn200100Em : 76 -> 80
~ __ZNSt3__16vectorI27C3DSubdivisionOsdGPURefinerNS_9allocatorIS1_EEE11__vallocateB8nn200100Em : 80 -> 84
~ __ZN10OpenSubdiv6v3_1_13Osd15EvaluatorCacheTINS1_19MTLComputeEvaluatorEE12GetEvaluatorINS1_10MTLContextEEEPS3_RKNS1_16BufferDescriptorESA_SA_SA_PT_ : 784 -> 788
~ __ZNSt3__16vectorI30C3DSubdivisionOsdGPUPatchTableNS_9allocatorIS1_EEE11__vallocateB8nn200100Em : 80 -> 84
~ +[SCNGeometry geometryWithSources:elements:sourceChannels:] : 692 -> 712
~ -[SCNGeometry _customDecodingOfSCNGeometry:] : 1284 -> 1304
~ ____Z41C3DGeometryInitSubdivTopologyInfoIfNeededP13__C3DGeometry_block_invoke : 332 -> 336
~ ____Z30C3DSubdivInitCPUPrimvarContextP26C3DSubdivCPUPrimvarContextPK26C3DGeometrySubdivisionInfoP9__C3DMesh_block_invoke : 476 -> 480
~ ____Z33C3DSubdivInitGPUPrimvarDescriptorP29C3DSubdivGPUPrimvarDescriptorPK26C3DGeometrySubdivisionInfoP9__C3DMesh_block_invoke : 568 -> 572
~ __ZNSt3__16vectorI23C3DSubdivCPUPrimvarDataIDv4_fENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_ : 280 -> 292
~ __ZNSt3__16vectorIbNS_9allocatorIbEEE11__vallocateB8nn200100Em : 68 -> 72
~ __ZNSt3__16vectorI27C3DSubdivCPUFVarPrimvarInfoNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_ : 252 -> 264
~ __ZNSt3__16vectorI28C3DSubdivCPUPrimvarDataGroupNS_9allocatorIS1_EEE8__appendEm : 416 -> 424
~ __ZNSt3__16vectorI27C3DSubdivGPUFVarPrimvarDataNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_ : 292 -> 304
~ __ZN15USDKitConverter18processSCNGeometryEP7USKNodeP8NSStringP11SCNGeometry : 4688 -> 4692
~ __ZNSt3__16vectorI11MaterialMapNS_9allocatorIS1_EEE7reserveEm : 220 -> 236
~ __ZNSt3__16vectorI11MaterialMapNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_ : 336 -> 340
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRKS6_EEEPS6_DpOT_ : 320 -> 316
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE18__assign_with_sizeB8nn200100IPS6_SA_EEvT_T0_l : 416 -> 420
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8nn200100Em : 76 -> 80
~ __ZN15USDKitConverter25processSkeletonAnimationsEP8Skeleton : 3156 -> 3160
~ __ZNSt3__16vectorIP19CAKeyframeAnimationNS_9allocatorIS2_EEE11__vallocateB8nn200100Em : 60 -> 64
~ -[SCNMTLShaderBindingsGenerator addPassResourceBindingsForArgument:] : 1600 -> 1604
~ -[SCNGeometryVDMCDeformerInstance initWithNode:deformer:outputs:computeVertexCount:context:] : 4092 -> 4096
~ __Z31newUInt32BufferFromUInt16BufferPU19objcproto9MTLBuffer11objc_objectjP21SCNMTLResourceManagerPU32objcproto21MTLBlitCommandEncoder11objc_object : 400 -> 408
~ ___92-[SCNGeometryVDMCDeformerInstance initWithNode:deformer:outputs:computeVertexCount:context:]_block_invoke : 596 -> 600
~ __ZN18__C3DTransformTree10_newHandleE19C3DTransformIndexes : 260 -> 264
~ __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB8nn200100Em : 56 -> 60
~ __ZN10OpenSubdiv6v3_1_13Far17PatchTableFactory23identifyAdaptivePatchesERNS2_14BuilderContextE : 792 -> 788
~ __ZNSt3__16vectorIN10OpenSubdiv6v3_1_13Far10PatchTable16FVarPatchChannelENS_9allocatorIS5_EEE8__appendEm : 416 -> 424
~ __ZN10OpenSubdiv6v3_1_13Far30EndCapGregoryBasisPatchFactory14GetPatchPointsEPKNS0_3Vtr8internal5LevelEiPKNS5_5VSpanEii : 1044 -> 1048
~ __ZNSt3__16vectorIN10OpenSubdiv6v3_1_13Far13TopologyLevelENS_9allocatorIS4_EEE8__appendEm : 352 -> 360
~ __ZNSt3__15dequeIiNS_9allocatorIiEEE19__add_back_capacityEv : 372 -> 376
~ __ZNSt3__114__split_bufferIPiNS_9allocatorIS1_EEE13emplace_frontIJS1_EEEvDpOT_ : 268 -> 272
~ -[SCNMTLDeformerStack updateDataForAuthoringEnvironment:transforms:context:] : 144 -> 140
~ -[SCNMTLDeformerStack drawAuthoringEnvironment:context:] : 120 -> 116
~ -[SCNMTLResourceManager removeAllShaders] : 68 -> 76
~ -[SCNMTLResourceManager resetRasterizerStates] : 80 -> 88
~ -[SCNMTLResourceManager newConstantBufferWithLength:options:] : 80 -> 76
~ -[SCNMTLResourceManager newBufferWithBytes:length:options:] : 64 -> 60
~ -[SCNMTLResourceManager newBufferWithLength:options:] : 60 -> 56
~ -[SCNMTLResourceManager dispatchForTexture:computeEncoder:pipelineState:] : 188 -> 184
~ -[SCNMTLResourceManager dispatchForCubemap:computeEncoder:pipelineState:] : 180 -> 176
~ -[SCNMTLResourceManager depthAndStencilStateWithReadWriteDepthDisabled] : 160 -> 156
~ -[SCNMTLRenderContext setPreferredFramesPerSecond:] : 152 -> 148
~ -[SCNMTLRenderContext setWantsWideGamut:] : 112 -> 120
~ -[SCNMTLRenderContext setDisableLinearRendering:] : 128 -> 136
~ -[SCNMTLRenderContext setReverseZ:] : 124 -> 132
~ -[SCNMTLRenderContext setIsOpaque:] : 128 -> 136
~ -[SCNMTLRenderContext setSampleCount:] : 52 -> 48
~ -[SCNMTLRenderContext endFrameSceneSpecifics] : 64 -> 72
~ -[SCNMTLRenderContext _commitResourceCommandBufferIfNeeded] : 88 -> 84
~ -[SCNMTLRenderContext endFrameWaitingUntilCompleted:status:error:] : 756 -> 752
~ -[SCNMTLRenderContext _finalRenderTexture] : 332 -> 328
~ -[SCNMTLRenderContext resourceCommandBuffer] : 88 -> 84
~ -[SCNMTLRenderContext beginRenderPass:renderEncoder:parameters:] : 172 -> 168
~ -[SCNMTLRenderContext endRenderPass] : 164 -> 160
~ -[SCNMTLRenderContext authoring_drawPrimitives:vertexCount:instanceCount:vertexBuffers:offsets:range:vertexDescriptor:withProgram:uniforms:uniformsLength:rasterizerStates:blendStates:] : 464 -> 460
~ -[SCNMTLRenderContext stopProcessingRendererElements:] : 196 -> 192
~ -[SCNMTLRenderContext unmapVolatileMeshElement:] : 100 -> 108
~ -[SCNMTLRenderContext currentRenderPassDescriptor] : 40 -> 36
~ -[SCNMTLRenderContext _drawFullScreenTexture:over:] : 560 -> 556
~ -[SCNMTLRenderContext discardPendingCommandBufferScheduledHandlers] : 72 -> 80
~ -[SCNMTLRenderContext discardPendingCommandBufferCompletedHandlers] : 72 -> 80
~ -[SCNMTLRenderContext discardPendingDrawablePresentedHandlers] : 72 -> 80
~ -[SCNMTLMesh setVertexDescriptor:] : 84 -> 80
~ -[SCNMTLMesh tessellationVertexDescriptor] : 48 -> 44
~ -[SCNMTLMesh tessellationVertexDescriptorHash] : 48 -> 44
~ -[SCNPhysicsWorld removeBehavior_unsafe:] : 148 -> 144
~ -[SCNDisplayLink _displayLinkCallbackWaitingOnFrameCompletionWithTime:] : 256 -> 252
CStrings:
+ "Welcome to SceneKit 608.100 (Nov  1 2025 03:22:39)"
+ "{?=\"currentLightingSet\"{?=\"lights\"[8C]}\"currentShadowMaps\"[8@\"<MTLTexture>\"]\"currentGoboMaps\"[8@\"<MTLTexture>\"]\"frameLightingSetDatas\"{unordered_map<unsigned long long, SCNMTLLightSetData, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, SCNMTLLightSetData>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, SCNMTLLightSetData>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, SCNMTLLightSetData>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, SCNMTLLightSetData>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, SCNMTLLightSetData>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, SCNMTLLightSetData>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, SCNMTLLightSetData>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, SCNMTLLightSetData>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, SCNMTLLightSetData>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}\"currentLightingHashKey\"Q\"currentLightingDesc\"{?=\"count\"q\"lights\"[8^{__C3DLight}]\"lightsData\"[8^{__C3DLightRuntimeData}]}\"currentLightingSpace\"{?=\"columns\"[4]}\"currentLightingSpaceShadow\"{?=\"columns\"[4]}\"needLightingSpaceTransformation\"B\"clusterSystem\"{SCNMTLClusterSystem=\"clustersCount\"\"tileSize\"\"selectedDebugClusterIndex\"\"_debugClusterTilesPipeline\"@\"SCNMTLRenderPipeline\"\"_debugLightIndicesBufferPipeline\"@\"SCNMTLRenderPipeline\"\"_debugClusterSlicesPipeline\"@\"SCNMTLRenderPipeline\"\"_debugProgram\"[7^{__C3DFXMetalProgram}]\"_debugShapes\"[7^{__C3DMesh}]}\"clusterInfo\"{Info=\"clusterBuffer\"{?=\"memory\"*\"buffer\"@\"<MTLBuffer>\"\"offset\"Q}\"clusterTexture\"@\"<MTLTexture>\"\"lightIndicesTexture\"@\"<MTLTexture>\"\"cellSize\"\"clusterScale\"\"cellPixelSize\"\"omniLightsRange\"\"spotLightsRange\"\"probeLightsRange\"\"lightsBuffer\"{?=\"memory\"*\"buffer\"@\"<MTLBuffer>\"\"offset\"Q}\"lightsBufferLightCount\"I\"shadowTextures\"[8@\"<MTLTexture>\"]\"iesOrGoboTextures\"[8@\"<MTLTexture>\"]\"samplerStates\"[8@\"<MTLSamplerState>\"]\"areaBuffer\"@\"<MTLBuffer>\"\"areaBufferOffset\"Q\"areaBufferOffsets\"[8Q]}\"reflectionProbesTextureArray\"@\"<MTLTexture>\"}"
+ "{?=\"lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"keyCodeConfiguration\"@\"NSDictionary\"\"keyDown\"{set<unsigned short, std::less<unsigned short>, std::allocator<unsigned short>>=\"__tree_\"{__tree<unsigned short, std::less<unsigned short>, std::allocator<unsigned short>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}\"forward\"{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"\"{?=\"__cap_\"^S}}\"backward\"{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"\"{?=\"__cap_\"^S}}\"left\"{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"\"{?=\"__cap_\"^S}}\"right\"{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"\"{?=\"__cap_\"^S}}}"
+ "{c3dAether=\"_fields\"{vector<c3dPhysicsField *, std::allocator<c3dPhysicsField *>>=\"__begin_\"^^{c3dPhysicsField}\"__end_\"^^{c3dPhysicsField}\"\"{?=\"__cap_\"^^{c3dPhysicsField}}}\"_activeFields\"{vector<c3dPhysicsField *, std::allocator<c3dPhysicsField *>>=\"__begin_\"^^{c3dPhysicsField}\"__end_\"^^{c3dPhysicsField}\"\"{?=\"__cap_\"^^{c3dPhysicsField}}}\"_lastOverrideIndex\"I}"
- "Welcome to SceneKit 608.100 (Oct 18 2025 10:57:21)"
- "{?=\"currentLightingSet\"{?=\"lights\"[8C]}\"currentShadowMaps\"[8@\"<MTLTexture>\"]\"currentGoboMaps\"[8@\"<MTLTexture>\"]\"frameLightingSetDatas\"{unordered_map<unsigned long long, SCNMTLLightSetData, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, SCNMTLLightSetData>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long long, SCNMTLLightSetData>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, SCNMTLLightSetData>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, SCNMTLLightSetData>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, SCNMTLLightSetData>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, SCNMTLLightSetData>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, SCNMTLLightSetData>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, SCNMTLLightSetData>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, SCNMTLLightSetData>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}\"currentLightingHashKey\"Q\"currentLightingDesc\"{?=\"count\"q\"lights\"[8^{__C3DLight}]\"lightsData\"[8^{__C3DLightRuntimeData}]}\"currentLightingSpace\"{?=\"columns\"[4]}\"currentLightingSpaceShadow\"{?=\"columns\"[4]}\"needLightingSpaceTransformation\"B\"clusterSystem\"{SCNMTLClusterSystem=\"clustersCount\"\"tileSize\"\"selectedDebugClusterIndex\"\"_debugClusterTilesPipeline\"@\"SCNMTLRenderPipeline\"\"_debugLightIndicesBufferPipeline\"@\"SCNMTLRenderPipeline\"\"_debugClusterSlicesPipeline\"@\"SCNMTLRenderPipeline\"\"_debugProgram\"[7^{__C3DFXMetalProgram}]\"_debugShapes\"[7^{__C3DMesh}]}\"clusterInfo\"{Info=\"clusterBuffer\"{?=\"memory\"*\"buffer\"@\"<MTLBuffer>\"\"offset\"Q}\"clusterTexture\"@\"<MTLTexture>\"\"lightIndicesTexture\"@\"<MTLTexture>\"\"cellSize\"\"clusterScale\"\"cellPixelSize\"\"omniLightsRange\"\"spotLightsRange\"\"probeLightsRange\"\"lightsBuffer\"{?=\"memory\"*\"buffer\"@\"<MTLBuffer>\"\"offset\"Q}\"lightsBufferLightCount\"I\"shadowTextures\"[8@\"<MTLTexture>\"]\"iesOrGoboTextures\"[8@\"<MTLTexture>\"]\"samplerStates\"[8@\"<MTLSamplerState>\"]\"areaBuffer\"@\"<MTLBuffer>\"\"areaBufferOffset\"Q\"areaBufferOffsets\"[8Q]}\"reflectionProbesTextureArray\"@\"<MTLTexture>\"}"
- "{?=\"lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"keyCodeConfiguration\"@\"NSDictionary\"\"keyDown\"{set<unsigned short, std::less<unsigned short>, std::allocator<unsigned short>>=\"__tree_\"{__tree<unsigned short, std::less<unsigned short>, std::allocator<unsigned short>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}\"forward\"{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"__cap_\"^S}\"backward\"{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"__cap_\"^S}\"left\"{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"__cap_\"^S}\"right\"{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"__cap_\"^S}}"
- "{c3dAether=\"_fields\"{vector<c3dPhysicsField *, std::allocator<c3dPhysicsField *>>=\"__begin_\"^^{c3dPhysicsField}\"__end_\"^^{c3dPhysicsField}\"__cap_\"^^{c3dPhysicsField}}\"_activeFields\"{vector<c3dPhysicsField *, std::allocator<c3dPhysicsField *>>=\"__begin_\"^^{c3dPhysicsField}\"__end_\"^^{c3dPhysicsField}\"__cap_\"^^{c3dPhysicsField}}\"_lastOverrideIndex\"I}"

```
