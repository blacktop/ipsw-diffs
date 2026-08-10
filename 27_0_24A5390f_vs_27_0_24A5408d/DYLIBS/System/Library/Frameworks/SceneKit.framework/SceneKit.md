## SceneKit

> `/System/Library/Frameworks/SceneKit.framework/SceneKit`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-611.0.0.0.0
-  __TEXT.__text: 0x393ccc
-  __TEXT.__objc_methlist: 0x1793c
+612.0.0.0.0
+  __TEXT.__text: 0x3930dc
+  __TEXT.__objc_methlist: 0x17854
   __TEXT.__const: 0x26298
-  __TEXT.__oslogstring: 0x167ad
-  __TEXT.__cstring: 0x99c1b
-  __TEXT.__gcc_except_tab: 0x41dc
+  __TEXT.__oslogstring: 0x166fc
+  __TEXT.__cstring: 0x99c1f
+  __TEXT.__gcc_except_tab: 0x402c
   __TEXT.__ustring: 0x2e
-  __TEXT.__unwind_info: 0xd508
+  __TEXT.__unwind_info: 0xd4b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7aa0
-  __DATA_CONST.__objc_classlist: 0x6e0
+  __DATA_CONST.__const: 0x7a00
+  __DATA_CONST.__objc_classlist: 0x6c8
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9758
+  __DATA_CONST.__objc_selrefs: 0x9740
   __DATA_CONST.__objc_protorefs: 0x228
-  __DATA_CONST.__objc_superrefs: 0x600
+  __DATA_CONST.__objc_superrefs: 0x5e8
   __DATA_CONST.__objc_arraydata: 0x270
   __DATA_CONST.__got: 0xc58
   __AUTH_CONST.__const: 0x9410
-  __AUTH_CONST.__cfstring: 0x20ce0
-  __AUTH_CONST.__objc_const: 0x23448
+  __AUTH_CONST.__cfstring: 0x20c60
+  __AUTH_CONST.__objc_const: 0x23058
   __AUTH_CONST.__weak_auth_got: 0x38
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_arrayobj: 0xa8

   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x1758
-  __AUTH.__objc_data: 0x4380
+  __AUTH.__objc_data: 0x4290
   __AUTH.__data: 0x4d70
-  __DATA.__objc_ivar: 0x1c94
+  __DATA.__objc_ivar: 0x1c5c
   __DATA.__data: 0x293c
   __DATA.__bss: 0x2eb8
   __DATA.__common: 0x1d1

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 19680
-  Symbols:   28275
-  CStrings:  8045
+  Functions: 19670
+  Symbols:   28237
+  CStrings:  8037
 
Symbols:
+ -[SCNCaptureDeviceSource init]
+ -[SCNReplicatorConstraint dealloc]
+ _C3DShapeMeshCountsAccountForShape
+ _C3DShapeMeshCreationDestroy
+ _C3DShapeTriangulationMarkTriangles
+ _OBJC_IVAR_$_SCNCaptureDeviceOutputConsumerSource._lock
+ _OBJC_IVAR_$_SCNCaptureDeviceSource._lock
+ __C3DLightingSystem_realloc
+ __ZL25_C3DCullingSystem_reallocPvmmym
+ __ZN19C3DScratchAllocator8AllocateEmym13C3DFillMemory
+ __ZN3C3D15ScratchAllocateINS_11OverlayPassEJPNS_11RenderGraphEPNS_9FinalPassEEEEPT_PvDpOT0_
+ __ZN3C3D15ScratchAllocateINS_13JitteringPassEJPNS_11RenderGraphEPNS_9FinalPassEEEEPT_PvDpOT0_
+ __ZN3C3D15ScratchAllocateINS_14TemporalAAPassEJPNS_11RenderGraphEPNS_8MainPassEEEEPT_PvDpOT0_
+ __ZN3C3D15ScratchAllocateINS_15RenderProbePassEJPNS_11RenderGraphERPNS_4PassERP9__C3DNodeRjR14MTLPixelFormatEEEPT_PvDpOT0_
+ __ZN3C3D5ArrayINS_11RenderGraph4LinkELj0ENS_14StackAllocatorEE14GrowCapacityByEjb
+ __ZN3C3D5ArrayINS_11RenderGraph4LinkELj0ENS_16ScratchAllocatorEE14GrowCapacityByEjb
+ __ZN3C3D5ArrayINS_11RenderGraph4LinkELj16ENS_14StackAllocatorEE14GrowCapacityByEjb
+ __ZN3C3D5ArrayINS_11RenderGraph9PortsPairELj16ENS_14StackAllocatorEE14GrowCapacityByEjb
+ __ZN3C3D5ArrayINS_16PassIODescriptorELj0ENS_14StackAllocatorEE14GrowCapacityByEjb
+ __ZN3C3D5ArrayINS_18RefCountedResourceELj0ENS_16ScratchAllocatorEE14GrowCapacityByEjb
+ __ZN3C3D5ArrayIP9__C3DNodeLj0ENS_14StackAllocatorEE14GrowCapacityByEjb
+ __ZN3C3D5ArrayIP9__C3DNodeLj0ENS_16ScratchAllocatorEE14GrowCapacityByEjb
+ __ZN3C3D5ArrayIPKcLj0ENS_14StackAllocatorEE14GrowCapacityByEjb
+ __ZN3C3D5ArrayIPNS_11RenderGraph9GraphNodeELj0ENS_14StackAllocatorEE14GrowCapacityByEjb
+ __ZN3C3D5ArrayIPNS_13ShadowMapPassELj0ENS_14StackAllocatorEE14GrowCapacityByEjb
+ __ZN3C3D5ArrayIPNS_18RefCountedResourceELj0ENS_14StackAllocatorEE14GrowCapacityByEjb
+ __ZN3C3D5ArrayIPNS_4PassELj0ENS_14StackAllocatorEE14GrowCapacityByEjb
+ __ZN3C3D5ArrayIPNS_4PassELj0ENS_16ScratchAllocatorEE14GrowCapacityByEjb
+ __ZN3C3D5ArrayIPNS_9FloorPassELj0ENS_14StackAllocatorEE14GrowCapacityByEjb
+ __ZN3C3D5ArrayItLj0ENS_16ScratchAllocatorEE14GrowCapacityByEjb
- +[SCNGeometryVariableTopologySampleDeformer supportsSecureCoding]
- -[SCNDisplayLink adaptativeFrameRate]
- -[SCNDisplayLink setAdaptativeFrameRate:]
- -[SCNGeometryVariableTopologySampleDeformer dealloc]
- -[SCNGeometryVariableTopologySampleDeformer deformedMeshReliesOnTransforms]
- -[SCNGeometryVariableTopologySampleDeformer encodeWithCoder:]
- -[SCNGeometryVariableTopologySampleDeformer initWithCoder:]
- -[SCNGeometryVariableTopologySampleDeformer init]
- -[SCNGeometryVariableTopologySampleDeformer newDeformerInstanceForNode:outputs:computeVertexCount:context:]
- -[SCNGeometryVariableTopologySampleDeformer requiredInputs]
- -[SCNGeometryVariableTopologySampleDeformer requiredOutputs]
- -[SCNGeometryVariableTopologySampleDeformer supportedOutputs]
- -[SCNGeometryVariableTopologySampleDeformerInstance dealloc]
- -[SCNGeometryVariableTopologySampleDeformerInstance initWithNode:deformer:outputs:computeVertexCount:context:]
- -[SCNGeometryVariableTopologySampleDeformerInstance meshForDeformedTopology]
- -[SCNGeometryVariableTopologySampleDeformerInstance updateWithContext:]
- -[SCNGeometryVariableTopologySampleDeformerMeshElementData dealloc]
- -[SCNPhysicsWorld _physicsContact]
- GCC_except_table101
- GCC_except_table42
- _C3DShapeTriangulationTriangleMark
- _C3DSourceAccessorGetPlatformLength
- _OBJC_CLASS_$_SCNGeometryVariableTopologySampleDeformer
- _OBJC_CLASS_$_SCNGeometryVariableTopologySampleDeformerInstance
- _OBJC_CLASS_$_SCNGeometryVariableTopologySampleDeformerMeshElementData
- _OBJC_IVAR_$_SCNDisplayLink._adaptativeFrameDuration
- _OBJC_IVAR_$_SCNGeometryVariableTopologySampleDeformerInstance._deformedMesh
- _OBJC_IVAR_$_SCNGeometryVariableTopologySampleDeformerInstance._deformedPrimitiveCountBuffer
- _OBJC_IVAR_$_SCNGeometryVariableTopologySampleDeformerInstance._drawIndexedPrimitivesIndirectBuffer
- _OBJC_IVAR_$_SCNGeometryVariableTopologySampleDeformerInstance._finalizeComputePipeline
- _OBJC_IVAR_$_SCNGeometryVariableTopologySampleDeformerInstance._meshElementData
- _OBJC_IVAR_$_SCNGeometryVariableTopologySampleDeformerInstance._mode
- _OBJC_IVAR_$_SCNGeometryVariableTopologySampleDeformerInstance._positionBuffer
- _OBJC_IVAR_$_SCNGeometryVariableTopologySampleDeformerMeshElementData._computePipeline
- _OBJC_IVAR_$_SCNGeometryVariableTopologySampleDeformerMeshElementData._deformedIndexBuffer
- _OBJC_IVAR_$_SCNGeometryVariableTopologySampleDeformerMeshElementData._deformedPrimitiveCountBufferOffset
- _OBJC_IVAR_$_SCNGeometryVariableTopologySampleDeformerMeshElementData._drawIndexedPrimitivesIndirectBufferOffset
- _OBJC_IVAR_$_SCNGeometryVariableTopologySampleDeformerMeshElementData._originalIndexBuffer
- _OBJC_IVAR_$_SCNGeometryVariableTopologySampleDeformerMeshElementData._originalPrimitiveCount
- _OBJC_IVAR_$_SCNGeometryVariableTopologySampleDeformerMeshElementData._subdividedVertexStartIndex
- _OBJC_IVAR_$_SCNPhysicsWorld._contact
- _OBJC_METACLASS_$_SCNGeometryVariableTopologySampleDeformer
- _OBJC_METACLASS_$_SCNGeometryVariableTopologySampleDeformerInstance
- _OBJC_METACLASS_$_SCNGeometryVariableTopologySampleDeformerMeshElementData
- __C3DLightingSystem_realloc_typed
- __OBJC_$_CLASS_METHODS_SCNGeometryVariableTopologySampleDeformer
- __OBJC_$_INSTANCE_METHODS_SCNGeometryVariableTopologySampleDeformer
- __OBJC_$_INSTANCE_METHODS_SCNGeometryVariableTopologySampleDeformerInstance
- __OBJC_$_INSTANCE_METHODS_SCNGeometryVariableTopologySampleDeformerMeshElementData
- __OBJC_$_INSTANCE_VARIABLES_SCNGeometryVariableTopologySampleDeformerInstance
- __OBJC_$_INSTANCE_VARIABLES_SCNGeometryVariableTopologySampleDeformerMeshElementData
- __OBJC_$_PROP_LIST_SCNGeometryVariableTopologySampleDeformerInstance
- __OBJC_CLASS_PROTOCOLS_$_SCNGeometryVariableTopologySampleDeformerInstance
- __OBJC_CLASS_RO_$_SCNGeometryVariableTopologySampleDeformer
- __OBJC_CLASS_RO_$_SCNGeometryVariableTopologySampleDeformerInstance
- __OBJC_CLASS_RO_$_SCNGeometryVariableTopologySampleDeformerMeshElementData
- __OBJC_METACLASS_RO_$_SCNGeometryVariableTopologySampleDeformer
- __OBJC_METACLASS_RO_$_SCNGeometryVariableTopologySampleDeformerInstance
- __OBJC_METACLASS_RO_$_SCNGeometryVariableTopologySampleDeformerMeshElementData
- __ZL31_C3DCullingSystem_realloc_typedPvmmym
- __ZN19C3DScratchAllocator8AllocateEmm13C3DFillMemory
- ___110-[SCNGeometryVariableTopologySampleDeformerInstance initWithNode:deformer:outputs:computeVertexCount:context:]_block_invoke
- ___110-[SCNGeometryVariableTopologySampleDeformerInstance initWithNode:deformer:outputs:computeVertexCount:context:]_block_invoke_2
- ___110-[SCNGeometryVariableTopologySampleDeformerInstance initWithNode:deformer:outputs:computeVertexCount:context:]_block_invoke_3
- ___block_descriptor_113_e8_32o40o48o56o64o72r80r88r_e201_v32?0^{__C3DMeshSource={__C3DGenericSource={__C3DEntity={__CFRuntimeBase=QAQ}^v^{__CFString}^{__CFString}^{__CFDictionary}^{__C3DScene}q}^{__C3DSourceAccessor}(?=^{__CFData}^v^v)qb1b1b1}SCC}8c16q20C28lr72l8r80l8s32l8s40l8s48l8s56l8r88l8s64l8
- ___block_descriptor_48_e8_32o40r_e73_v32?0"SCNGeometryVariableTopologySampleDeformerMeshElementData"8Q16^B24lr40l8s32l8
- ___block_descriptor_56_e8_32r40r_e201_v32?0^{__C3DMeshSource={__C3DGenericSource={__C3DEntity={__CFRuntimeBase=QAQ}^v^{__CFString}^{__CFString}^{__CFDictionary}^{__C3DScene}q}^{__C3DSourceAccessor}(?=^{__CFData}^v^v)qb1b1b1}SCC}8c16q20C28lr32l8r40l8
- ___block_descriptor_80_e8_32r40r_e19_v32?0I8^I12I20^B24lr32l8r40l8
CStrings:
+ "#ifndef __SCNMetalDefines__\n#define __SCNMetalDefines__\n#if defined(C3D_EXPOSE_SCNSceneBuffer_TO_CPU_CODE)\n#define SCN_METAL_HAS_SIMD_TYPES 1\n#else\n#if defined(__METAL_VERSION__)\n#define SCN_METAL_HAS_SIMD_TYPES 1\n#else\n#define SCN_METAL_HAS_SIMD_TYPES 0\n#endif\n#endif\nenum {\n    SCNVertexSemanticPosition,\n    SCNVertexSemanticNormal,\n    SCNVertexSemanticTangent,\n    SCNVertexSemanticColor,\n    SCNVertexSemanticBoneIndices,\n    SCNVertexSemanticBoneWeights,\n    SCNVertexSemanticTexcoord0,\n    SCNVertexSemanticTexcoord1,\n    SCNVertexSemanticTexcoord2,\n    SCNVertexSemanticTexcoord3,\n    SCNVertexSemanticTexcoord4,\n    SCNVertexSemanticTexcoord5,\n    SCNVertexSemanticTexcoord6,\n    SCNVertexSemanticTexcoord7\n};\n\n#if SCN_METAL_HAS_SIMD_TYPES\n\n\n\nstruct SCNSceneBuffer {\n    float4x4    viewTransform;\n    float4x4    inverseViewTransform; \n    float4x4    projectionTransform;\n    float4x4    viewProjectionTransform;\n    float4x4    viewToCubeTransform; \n    float4x4    lastFrameViewProjectionTransform;\n    float4      ambientLightingColor;\n    float4\t\tfogColor;\n    float3\t\tfogParameters; \n    float2      inverseResolution;\n    float       time;\n    float       sinTime;\n    float       cosTime;\n    float       random01;\n    float       motionBlurIntensity;\n    \n    float       environmentIntensity;\n    float4x4    inverseProjectionTransform;\n    float4x4    inverseViewProjectionTransform;\n    \n    float2      nearFar; \n    float4      viewportSize; \n    \n    float4x4    inverseTransposeViewTransform;\n\n    \n    float4      clusterScale; \n};\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n#endif\n\n#endif \n"
+ "C3DCreateTangentsWithGeometryOptimized"
+ "Error: %s - index (%u) out of bounds (%u positions, %u uvs)"
+ "Error: Geometry source has invalid parameter"
+ "Error: SCNSkinner: bone indices has insufficient data"
+ "Error: SCNSkinner: bone indices must be either int8 or int16 (maximum of 2 bytes)"
+ "Error: SCNSkinner: bone weights has insufficient data"
+ "Welcome to SceneKit 612 (Aug  4 2026 09:38:58)"
- "#ifndef __SCNMetalDefines__\n#define __SCNMetalDefines__\n\nenum {\n    SCNVertexSemanticPosition,\n    SCNVertexSemanticNormal,\n    SCNVertexSemanticTangent,\n    SCNVertexSemanticColor,\n    SCNVertexSemanticBoneIndices,\n    SCNVertexSemanticBoneWeights,\n    SCNVertexSemanticTexcoord0,\n    SCNVertexSemanticTexcoord1,\n    SCNVertexSemanticTexcoord2,\n    SCNVertexSemanticTexcoord3,\n    SCNVertexSemanticTexcoord4,\n    SCNVertexSemanticTexcoord5,\n    SCNVertexSemanticTexcoord6,\n    SCNVertexSemanticTexcoord7\n};\n\n\n\nstruct SCNSceneBuffer {\n    float4x4    viewTransform;\n    float4x4    inverseViewTransform; \n    float4x4    projectionTransform;\n    float4x4    viewProjectionTransform;\n    float4x4    viewToCubeTransform; \n    float4x4    lastFrameViewProjectionTransform;\n    float4      ambientLightingColor;\n    float4\t\tfogColor;\n    float3\t\tfogParameters; \n    float2      inverseResolution;\n    float       time;\n    float       sinTime;\n    float       cosTime;\n    float       random01;\n    float       motionBlurIntensity;\n    \n    float       environmentIntensity;\n    float4x4    inverseProjectionTransform;\n    float4x4    inverseViewProjectionTransform;\n    \n    float2      nearFar; \n    float4      viewportSize; \n    \n    float4x4    inverseTransposeViewTransform;\n\n    \n    float4      clusterScale; \n};\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n#endif \n"
- "Assertion '%s' failed. Not enough room for the specified count & stride to read"
- "Assertion '%s' failed. Not enough room for the specified count & stride to write"
- "Assertion '%s' failed. Variable topology sample expects triangles"
- "Error: SCNSkinner: bone indices must be uint8 or uint16 (maximum of 2 bytes)"
- "Error: invalid geometry detected - skip C3DCreateTangentsWithGeometryOptimized"
- "UInt%d-UInt%d"
- "Unreachable code: Unsupported index size (%zu)"
- "Unreachable code: Unsupported semantic %@"
- "Variable topology sample deformer"
- "Welcome to SceneKit 611 (Jul  8 2026 03:33:01)"
- "count * readStride <= read_length"
- "count * writeStride <= write_length"
- "deformer_variabletopologysample_any_order"
- "deformer_variabletopologysample_any_order_finalize"
- "v32@?0@\"SCNGeometryVariableTopologySampleDeformerMeshElementData\"8Q16^B24"
```
