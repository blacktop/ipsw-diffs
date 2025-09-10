## Metal

> `/System/Library/Frameworks/Metal.framework/Metal`

```diff

 370.63.0.0.0
-  __TEXT.__text: 0x1d8d6c
+  __TEXT.__text: 0x1da6b4
   __TEXT.__auth_stubs: 0x1d00
-  __TEXT.__objc_methlist: 0x1d6ac
+  __TEXT.__objc_methlist: 0x1df7c
   __TEXT.__gcc_except_tab: 0xb3d4
-  __TEXT.__cstring: 0x22098
-  __TEXT.__const: 0x2cde0
+  __TEXT.__cstring: 0x2240c
+  __TEXT.__const: 0x2d160
   __TEXT.__oslogstring: 0x1e66
   __TEXT.__ustring: 0x1be
   __TEXT.text_env: 0x2574
-  __TEXT.__unwind_info: 0x82e8
+  __TEXT.__unwind_info: 0x8330
   __TEXT.__eh_frame: 0x78
-  __TEXT.__objc_classname: 0x3ef5
-  __TEXT.__objc_methname: 0x355a5
-  __TEXT.__objc_methtype: 0x176c8
-  __TEXT.__objc_stubs: 0x155a0
+  __TEXT.__objc_classname: 0x3f94
+  __TEXT.__objc_methname: 0x3615e
+  __TEXT.__objc_methtype: 0x17b6c
+  __TEXT.__objc_stubs: 0x159e0
   __DATA_CONST.__got: 0x9a8
-  __DATA_CONST.__const: 0x3040
-  __DATA_CONST.__objc_classlist: 0xcc8
+  __DATA_CONST.__const: 0x3090
+  __DATA_CONST.__objc_classlist: 0xcf8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x480
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x87b0
+  __DATA_CONST.__objc_selrefs: 0x8a90
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0xbc8
+  __DATA_CONST.__objc_superrefs: 0xbd8
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0xe98
   __AUTH_CONST.__const: 0x4f80
-  __AUTH_CONST.__cfstring: 0x124a0
-  __AUTH_CONST.__objc_const: 0x449e8
+  __AUTH_CONST.__cfstring: 0x12760
+  __AUTH_CONST.__objc_const: 0x45788
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x3d90
-  __DATA.__objc_ivar: 0x20c8
-  __DATA.__data: 0x43d0
+  __AUTH.__objc_data: 0x3f70
+  __DATA.__objc_ivar: 0x215c
+  __DATA.__data: 0x43e8
   __DATA.__bss: 0x334
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x4240

   - /usr/lib/libcompression.dylib
   - /usr/lib/libllvm-flatbuffers.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A192972D-E383-3909-B074-60081D375D0D
-  Functions: 12807
-  Symbols:   40362
-  CStrings:  15666
+  UUID: C9D32402-C05D-30C8-ABBA-D9E2F03CB05D
+  Functions: 12951
+  Symbols:   40767
+  CStrings:  15876
 
Symbols:
+ -[MTLDepthStencilDescriptorInternal resourceIndex]
+ -[MTLDepthStencilDescriptorInternal setResourceIndex:]
+ -[MTLDeviceFeatureQueries familySupportsConditionalTileDispatch]
+ -[MTLDeviceFeatureQueries familySupportsDepthBoundsTesting]
+ -[MTLDeviceFeatureQueries familySupportsExtendedIndirectRenderCommand]
+ -[MTLDeviceFeatureQueries familySupportsFP8]
+ -[MTLDeviceFeatureQueries familySupportsMXU]
+ -[MTLDeviceFeatureQueries familySupportsSamplerReductionMode]
+ -[MTLDeviceFeatureQueries familySupportsTextureAccessPatterns]
+ -[MTLDeviceFeatureQueries supportsConditionalTileDispatch]
+ -[MTLDeviceFeatureQueries supportsDepthBoundsTesting]
+ -[MTLDeviceFeatureQueries supportsExtendedIndirectRenderCommand]
+ -[MTLDeviceFeatureQueries supportsFP8]
+ -[MTLDeviceFeatureQueries supportsMXU]
+ -[MTLDeviceFeatureQueries supportsSamplerReductionMode]
+ -[MTLDeviceFeatureQueries supportsTextureAccessPatterns]
+ -[MTLIndirectCommandBufferDescriptor allowOverrideRenderStates]
+ -[MTLIndirectCommandBufferDescriptor inheritBlendColor]
+ -[MTLIndirectCommandBufferDescriptor inheritCullMode]
+ -[MTLIndirectCommandBufferDescriptor inheritDepthBias]
+ -[MTLIndirectCommandBufferDescriptor inheritDepthClipMode]
+ -[MTLIndirectCommandBufferDescriptor inheritDepthStencilState]
+ -[MTLIndirectCommandBufferDescriptor inheritDepthTestBounds]
+ -[MTLIndirectCommandBufferDescriptor inheritFrontFacingWinding]
+ -[MTLIndirectCommandBufferDescriptor inheritScissorRects]
+ -[MTLIndirectCommandBufferDescriptor inheritStencilReferenceValues]
+ -[MTLIndirectCommandBufferDescriptor inheritTriangleFillMode]
+ -[MTLIndirectCommandBufferDescriptor inheritViewports]
+ -[MTLIndirectCommandBufferDescriptor maxScissorRectCount]
+ -[MTLIndirectCommandBufferDescriptor maxViewportCount]
+ -[MTLIndirectCommandBufferDescriptor setAllowOverrideRenderStates:]
+ -[MTLIndirectCommandBufferDescriptor setInheritBlendColor:]
+ -[MTLIndirectCommandBufferDescriptor setInheritCullMode:]
+ -[MTLIndirectCommandBufferDescriptor setInheritDepthBias:]
+ -[MTLIndirectCommandBufferDescriptor setInheritDepthClipMode:]
+ -[MTLIndirectCommandBufferDescriptor setInheritDepthStencilState:]
+ -[MTLIndirectCommandBufferDescriptor setInheritDepthTestBounds:]
+ -[MTLIndirectCommandBufferDescriptor setInheritFrontFacingWinding:]
+ -[MTLIndirectCommandBufferDescriptor setInheritScissorRects:]
+ -[MTLIndirectCommandBufferDescriptor setInheritStencilReferenceValues:]
+ -[MTLIndirectCommandBufferDescriptor setInheritTriangleFillMode:]
+ -[MTLIndirectCommandBufferDescriptor setInheritViewports:]
+ -[MTLIndirectCommandBufferDescriptor setMaxScissorRectCount:]
+ -[MTLIndirectCommandBufferDescriptor setMaxViewportCount:]
+ -[MTLSamplerDescriptorInternal reductionMode]
+ -[MTLSamplerDescriptorInternal setReductionMode:]
+ -[MTLTextureDescriptorInternal setWriteAccessPattern:]
+ -[MTLTextureDescriptorInternal writeAccessPattern]
+ -[MTLTextureViewDescriptor setWriteAccessPattern:]
+ -[MTLTextureViewDescriptor writeAccessPattern]
+ -[_MTL4RenderCommandEncoder setDepthTestMinBound:maxBound:]
+ -[_MTLCommandEncoder optimizeContentsForCPUAccess:]
+ -[_MTLCommandEncoder optimizeContentsForCPUAccess:slice:level:]
+ -[_MTLCommandEncoder optimizeContentsForGPUAccess:]
+ -[_MTLCommandEncoder optimizeContentsForGPUAccess:slice:level:]
+ -[_MTLCommandEncoder optimizeContentsForTexture:readAccessPattern:]
+ -[_MTLCommandEncoder optimizeContentsForTexture:readAccessPattern:readAccessor:]
+ -[_MTLCommandEncoder optimizeContentsForTexture:readAccessPattern:readAccessor:slice:level:]
+ -[_MTLCommandEncoder optimizeContentsForTexture:readAccessPattern:slice:level:]
+ -[_MTLDepthStencilState gpuResourceID]
+ -[_MTLDepthStencilState resourceIndex]
+ -[_MTLDepthStencilState uniqueIdentifier]
+ -[_MTLDevice samplerReductionModeSupport]
+ -[_MTLDevice supportsConditionalTileDispatch]
+ -[_MTLDevice supportsDepthBoundsTesting]
+ -[_MTLDevice supportsExtendedIndirectRenderCommand]
+ -[_MTLDevice supportsFP8]
+ -[_MTLDevice supportsMXU]
+ -[_MTLDevice supportsSamplerReductionMode]
+ -[_MTLDevice supportsTextureAccessPatterns]
+ -[_MTLDeviceFeatureQueries familySupportsConditionalTileDispatch]
+ -[_MTLDeviceFeatureQueries familySupportsDepthBoundsTesting]
+ -[_MTLDeviceFeatureQueries familySupportsExtendedIndirectRenderCommand]
+ -[_MTLDeviceFeatureQueries familySupportsFP8]
+ -[_MTLDeviceFeatureQueries familySupportsMXU]
+ -[_MTLDeviceFeatureQueries familySupportsSamplerReductionMode]
+ -[_MTLDeviceFeatureQueries familySupportsTextureAccessPatterns]
+ -[_MTLIndirectArgumentBufferLayout uniqueIdentifierForDepthStencilStateAtIndex:inIndirectArgumentBuffer:atOffset:]
+ -[_MTLIndirectArgumentEncoder setDepthStencilState:atIndex:]
+ -[_MTLIndirectArgumentEncoder setDepthStencilStates:withRange:]
+ -[_MTLIndirectBlendColor alpha]
+ -[_MTLIndirectBlendColor blue]
+ -[_MTLIndirectBlendColor green]
+ -[_MTLIndirectBlendColor red]
+ -[_MTLIndirectBlendColor setAlpha:]
+ -[_MTLIndirectBlendColor setBlue:]
+ -[_MTLIndirectBlendColor setGreen:]
+ -[_MTLIndirectBlendColor setRed:]
+ -[_MTLIndirectDepthBiasInfo clamp]
+ -[_MTLIndirectDepthBiasInfo depthBias]
+ -[_MTLIndirectDepthBiasInfo setClamp:]
+ -[_MTLIndirectDepthBiasInfo setDepthBias:]
+ -[_MTLIndirectDepthBiasInfo setSlopeScale:]
+ -[_MTLIndirectDepthBiasInfo slopeScale]
+ -[_MTLIndirectDepthTestBounds maxBounds]
+ -[_MTLIndirectDepthTestBounds minBounds]
+ -[_MTLIndirectDepthTestBounds setMaxBounds:]
+ -[_MTLIndirectDepthTestBounds setMinBounds:]
+ -[_MTLIndirectRenderCommand getBlendColor]
+ -[_MTLIndirectRenderCommand getCullMode]
+ -[_MTLIndirectRenderCommand getDepthBiasInfo]
+ -[_MTLIndirectRenderCommand getDepthClipMode]
+ -[_MTLIndirectRenderCommand getDepthStencilStateUniqueIdentifier]
+ -[_MTLIndirectRenderCommand getDepthStencilState]
+ -[_MTLIndirectRenderCommand getDepthTestBounds]
+ -[_MTLIndirectRenderCommand getFrontFacingWinding]
+ -[_MTLIndirectRenderCommand getScissorRects]
+ -[_MTLIndirectRenderCommand getStencilReferenceValues]
+ -[_MTLIndirectRenderCommand getTriangleFillMode]
+ -[_MTLIndirectRenderCommand getViewports]
+ -[_MTLIndirectRenderCommand setBlendColorRed:green:blue:alpha:]
+ -[_MTLIndirectRenderCommand setCullMode:]
+ -[_MTLIndirectRenderCommand setDepthBias:slopeScale:clamp:]
+ -[_MTLIndirectRenderCommand setDepthClipMode:]
+ -[_MTLIndirectRenderCommand setDepthStencilState:]
+ -[_MTLIndirectRenderCommand setDepthTestMinBound:maxBound:]
+ -[_MTLIndirectRenderCommand setFrontFacingWinding:]
+ -[_MTLIndirectRenderCommand setScissorRect:]
+ -[_MTLIndirectRenderCommand setScissorRects:count:]
+ -[_MTLIndirectRenderCommand setStencilFrontReferenceValue:backReferenceValue:]
+ -[_MTLIndirectRenderCommand setStencilReferenceValue:]
+ -[_MTLIndirectRenderCommand setToolsDispatchBufferSPI:atIndex:stages:]
+ -[_MTLIndirectRenderCommand setTriangleFillMode:]
+ -[_MTLIndirectRenderCommand setViewport:]
+ -[_MTLIndirectRenderCommand setViewports:count:]
+ -[_MTLIndirectScissorRects count]
+ -[_MTLIndirectScissorRects dealloc]
+ -[_MTLIndirectScissorRects initWithCount:]
+ -[_MTLIndirectScissorRects scissorRects]
+ -[_MTLIndirectScissorRects setCount:]
+ -[_MTLIndirectScissorRects setScissorRects:]
+ -[_MTLIndirectStencilReferenceValues backReferenceValue]
+ -[_MTLIndirectStencilReferenceValues frontReferenceValue]
+ -[_MTLIndirectStencilReferenceValues setBackReferenceValue:]
+ -[_MTLIndirectStencilReferenceValues setFrontReferenceValue:]
+ -[_MTLIndirectViewports count]
+ -[_MTLIndirectViewports dealloc]
+ -[_MTLIndirectViewports initWithCount:]
+ -[_MTLIndirectViewports setCount:]
+ -[_MTLIndirectViewports setViewports:]
+ -[_MTLIndirectViewports viewports]
+ GCC_except_table307
+ GCC_except_table381
+ GCC_except_table415
+ GCC_except_table417
+ GCC_except_table428
+ GCC_except_table462
+ GCC_except_table465
+ GCC_except_table718
+ GCC_except_table719
+ GCC_except_table759
+ GCC_except_table806
+ GCC_except_table818
+ GCC_except_table823
+ GCC_except_table824
+ GCC_except_table828
+ OBJC_IVAR_$__MTLIndirectBlendColor.alpha
+ OBJC_IVAR_$__MTLIndirectBlendColor.blue
+ OBJC_IVAR_$__MTLIndirectBlendColor.green
+ OBJC_IVAR_$__MTLIndirectBlendColor.red
+ OBJC_IVAR_$__MTLIndirectDepthBiasInfo.clamp
+ OBJC_IVAR_$__MTLIndirectDepthBiasInfo.depthBias
+ OBJC_IVAR_$__MTLIndirectDepthBiasInfo.slopeScale
+ OBJC_IVAR_$__MTLIndirectDepthTestBounds.maxBounds
+ OBJC_IVAR_$__MTLIndirectDepthTestBounds.minBounds
+ OBJC_IVAR_$__MTLIndirectScissorRects.count
+ OBJC_IVAR_$__MTLIndirectScissorRects.scissorRects
+ OBJC_IVAR_$__MTLIndirectStencilReferenceValues.backReferenceValue
+ OBJC_IVAR_$__MTLIndirectStencilReferenceValues.frontReferenceValue
+ OBJC_IVAR_$__MTLIndirectViewports.count
+ OBJC_IVAR_$__MTLIndirectViewports.viewports
+ _MTLPipelinePerformanceKeyNonSmashableAtomicInstructionCount
+ _MTLPipelinePerformanceKeySmashableAtomicInstructionCount
+ _MTLTextureAccessPatternString
+ _OBJC_CLASS_$__MTLIndirectBlendColor
+ _OBJC_CLASS_$__MTLIndirectDepthBiasInfo
+ _OBJC_CLASS_$__MTLIndirectDepthTestBounds
+ _OBJC_CLASS_$__MTLIndirectScissorRects
+ _OBJC_CLASS_$__MTLIndirectStencilReferenceValues
+ _OBJC_CLASS_$__MTLIndirectViewports
+ _OBJC_IVAR_$_MTLDeviceFeatureQueries._familySupportsConditionalTileDispatch
+ _OBJC_IVAR_$_MTLDeviceFeatureQueries._familySupportsDepthBoundsTesting
+ _OBJC_IVAR_$_MTLDeviceFeatureQueries._familySupportsExtendedIndirectRenderCommand
+ _OBJC_IVAR_$_MTLDeviceFeatureQueries._familySupportsFP8
+ _OBJC_IVAR_$_MTLDeviceFeatureQueries._familySupportsMXU
+ _OBJC_IVAR_$_MTLDeviceFeatureQueries._familySupportsSamplerReductionMode
+ _OBJC_IVAR_$_MTLDeviceFeatureQueries._familySupportsTextureAccessPatterns
+ _OBJC_IVAR_$__MTLIndirectBlendColor._alpha
+ _OBJC_IVAR_$__MTLIndirectBlendColor._blue
+ _OBJC_IVAR_$__MTLIndirectBlendColor._green
+ _OBJC_IVAR_$__MTLIndirectBlendColor._red
+ _OBJC_IVAR_$__MTLIndirectDepthBiasInfo._clamp
+ _OBJC_IVAR_$__MTLIndirectDepthBiasInfo._depthBias
+ _OBJC_IVAR_$__MTLIndirectDepthBiasInfo._slopeScale
+ _OBJC_IVAR_$__MTLIndirectDepthTestBounds._maxBounds
+ _OBJC_IVAR_$__MTLIndirectDepthTestBounds._minBounds
+ _OBJC_IVAR_$__MTLIndirectScissorRects._count
+ _OBJC_IVAR_$__MTLIndirectScissorRects._scissorRects
+ _OBJC_IVAR_$__MTLIndirectStencilReferenceValues._backReferenceValue
+ _OBJC_IVAR_$__MTLIndirectStencilReferenceValues._frontReferenceValue
+ _OBJC_IVAR_$__MTLIndirectViewports._count
+ _OBJC_IVAR_$__MTLIndirectViewports._viewports
+ _OBJC_METACLASS_$__MTLIndirectBlendColor
+ _OBJC_METACLASS_$__MTLIndirectDepthBiasInfo
+ _OBJC_METACLASS_$__MTLIndirectDepthTestBounds
+ _OBJC_METACLASS_$__MTLIndirectScissorRects
+ _OBJC_METACLASS_$__MTLIndirectStencilReferenceValues
+ _OBJC_METACLASS_$__MTLIndirectViewports
+ __OBJC_$_INSTANCE_METHODS__MTLIndirectBlendColor
+ __OBJC_$_INSTANCE_METHODS__MTLIndirectDepthBiasInfo
+ __OBJC_$_INSTANCE_METHODS__MTLIndirectDepthTestBounds
+ __OBJC_$_INSTANCE_METHODS__MTLIndirectScissorRects
+ __OBJC_$_INSTANCE_METHODS__MTLIndirectStencilReferenceValues
+ __OBJC_$_INSTANCE_METHODS__MTLIndirectViewports
+ __OBJC_$_INSTANCE_VARIABLES__MTLIndirectBlendColor
+ __OBJC_$_INSTANCE_VARIABLES__MTLIndirectDepthBiasInfo
+ __OBJC_$_INSTANCE_VARIABLES__MTLIndirectDepthTestBounds
+ __OBJC_$_INSTANCE_VARIABLES__MTLIndirectScissorRects
+ __OBJC_$_INSTANCE_VARIABLES__MTLIndirectStencilReferenceValues
+ __OBJC_$_INSTANCE_VARIABLES__MTLIndirectViewports
+ __OBJC_$_PROP_LIST__MTLIndirectBlendColor
+ __OBJC_$_PROP_LIST__MTLIndirectDepthBiasInfo
+ __OBJC_$_PROP_LIST__MTLIndirectDepthTestBounds
+ __OBJC_$_PROP_LIST__MTLIndirectScissorRects
+ __OBJC_$_PROP_LIST__MTLIndirectStencilReferenceValues
+ __OBJC_$_PROP_LIST__MTLIndirectViewports
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MTLIndirectRenderCommandSPI
+ __OBJC_CLASS_RO_$__MTLIndirectBlendColor
+ __OBJC_CLASS_RO_$__MTLIndirectDepthBiasInfo
+ __OBJC_CLASS_RO_$__MTLIndirectDepthTestBounds
+ __OBJC_CLASS_RO_$__MTLIndirectScissorRects
+ __OBJC_CLASS_RO_$__MTLIndirectStencilReferenceValues
+ __OBJC_CLASS_RO_$__MTLIndirectViewports
+ __OBJC_METACLASS_RO_$__MTLIndirectBlendColor
+ __OBJC_METACLASS_RO_$__MTLIndirectDepthBiasInfo
+ __OBJC_METACLASS_RO_$__MTLIndirectDepthTestBounds
+ __OBJC_METACLASS_RO_$__MTLIndirectScissorRects
+ __OBJC_METACLASS_RO_$__MTLIndirectStencilReferenceValues
+ __OBJC_METACLASS_RO_$__MTLIndirectViewports
+ __Z29MTLSamplerReductionModeString23MTLSamplerReductionMode
+ __ZNK13AirReflection4Node28node_as_DepthStencilStateArgEv
+ ___block_literal_global.1292
+ ___block_literal_global.1372
+ ___block_literal_global.1720
+ ___block_literal_global.1834
+ ___block_literal_global.1837
+ ___block_literal_global.198
+ ___block_literal_global.1998
+ ___block_literal_global.201
+ ___block_literal_global.204
+ ___block_literal_global.2123
+ ___block_literal_global.2343
+ ___block_literal_global.2346
+ ___block_literal_global.2348
+ ___block_literal_global.293
+ _kMetalTextureWriteAccessPattern
+ _objc_msgSend$allowOverrideRenderStates
+ _objc_msgSend$familySupportsConditionalTileDispatch
+ _objc_msgSend$familySupportsDepthBoundsTesting
+ _objc_msgSend$familySupportsExtendedIndirectRenderCommand
+ _objc_msgSend$familySupportsFP8
+ _objc_msgSend$familySupportsMXU
+ _objc_msgSend$familySupportsSamplerReductionMode
+ _objc_msgSend$familySupportsTextureAccessPatterns
+ _objc_msgSend$inheritBlendColor
+ _objc_msgSend$inheritCullMode
+ _objc_msgSend$inheritDepthBias
+ _objc_msgSend$inheritDepthClipMode
+ _objc_msgSend$inheritDepthStencilState
+ _objc_msgSend$inheritDepthTestBounds
+ _objc_msgSend$inheritFrontFacingWinding
+ _objc_msgSend$inheritScissorRects
+ _objc_msgSend$inheritStencilReferenceValues
+ _objc_msgSend$inheritTriangleFillMode
+ _objc_msgSend$inheritViewports
+ _objc_msgSend$maxScissorRectCount
+ _objc_msgSend$maxViewportCount
+ _objc_msgSend$optimizeContentsForTexture:readAccessPattern:readAccessor:
+ _objc_msgSend$optimizeContentsForTexture:readAccessPattern:readAccessor:slice:level:
+ _objc_msgSend$reductionMode
+ _objc_msgSend$setReductionMode:
+ _objc_msgSend$setWriteAccessPattern:
+ _objc_msgSend$supportsConditionalTileDispatch
+ _objc_msgSend$supportsDepthBoundsTesting
+ _objc_msgSend$supportsExtendedIndirectRenderCommand
+ _objc_msgSend$supportsFP8
+ _objc_msgSend$supportsMXU
+ _objc_msgSend$supportsSamplerReductionMode
+ _objc_msgSend$supportsTextureAccessPatterns
+ _objc_msgSend$writeAccessPattern
- GCC_except_table210
- GCC_except_table218
- GCC_except_table300
- GCC_except_table377
- GCC_except_table408
- GCC_except_table410
- GCC_except_table448
- GCC_except_table451
- GCC_except_table453
- GCC_except_table710
- GCC_except_table749
- GCC_except_table751
- GCC_except_table798
- GCC_except_table801
- GCC_except_table820
- ___block_literal_global.1276
- ___block_literal_global.1356
- ___block_literal_global.1698
- ___block_literal_global.1815
- ___block_literal_global.185
- ___block_literal_global.188
- ___block_literal_global.191
- ___block_literal_global.1975
- ___block_literal_global.2100
- ___block_literal_global.2320
- ___block_literal_global.2323
- ___block_literal_global.2325
- ___block_literal_global.290
CStrings:
+ "21:18:06"
+ "@\"<MTLDepthStencilState>\"16@0:8"
+ "@\"_MTLIndirectBlendColor\"16@0:8"
+ "@\"_MTLIndirectDepthBiasInfo\"16@0:8"
+ "@\"_MTLIndirectDepthTestBounds\"16@0:8"
+ "@\"_MTLIndirectScissorRects\"16@0:8"
+ "@\"_MTLIndirectStencilReferenceValues\"16@0:8"
+ "@\"_MTLIndirectViewports\"16@0:8"
+ "Aug  2 2025"
+ "Aug  2 2025 21:18:06"
+ "Conditional Tile Dispatch"
+ "Depth Bounds Testing"
+ "DepthStencilStateArg"
+ "DepthStencilStateType"
+ "Extended Indirect Render Command"
+ "MTLDataTypeDepthStencilState"
+ "MTLGPUFamilyApple10"
+ "MTLPixelFormatR12Uint_PACKED"
+ "MTLPixelFormatR12Uint_X4"
+ "MTLPixelFormatRG12Uint_PACKED"
+ "MTLPixelFormatRG12Uint_X8"
+ "MTLPixelFormatRGB10A8Uint_2P"
+ "MTLSamplerReductionModeMaximum"
+ "MTLSamplerReductionModeMinimum"
+ "MTLSamplerReductionModeWeightedAverage"
+ "MTLTextureAccessPatternCoherent"
+ "MTLTextureAccessPatternDefault"
+ "MTLTextureAccessPatternIncoherent"
+ "MXU"
+ "Non-smashable device atomic instruction count"
+ "Sampler reduction mode support"
+ "Smashable device atomic instruction count"
+ "Support for 8-bit floating types"
+ "TB,R,N,V_familySupportsConditionalTileDispatch"
+ "TB,R,N,V_familySupportsDepthBoundsTesting"
+ "TB,R,N,V_familySupportsExtendedIndirectRenderCommand"
+ "TB,R,N,V_familySupportsFP8"
+ "TB,R,N,V_familySupportsMXU"
+ "TB,R,N,V_familySupportsSamplerReductionMode"
+ "TB,R,N,V_familySupportsTextureAccessPatterns"
+ "TI,N,V_backReferenceValue"
+ "TI,N,V_frontReferenceValue"
+ "T^{?=QQQQ},N,V_scissorRects"
+ "T^{?=dddddd},N,V_viewports"
+ "Texture Access Patterns"
+ "Tf,N,V_alpha"
+ "Tf,N,V_blue"
+ "Tf,N,V_clamp"
+ "Tf,N,V_depthBias"
+ "Tf,N,V_green"
+ "Tf,N,V_maxBounds"
+ "Tf,N,V_minBounds"
+ "Tf,N,V_red"
+ "Tf,N,V_slopeScale"
+ "Tq,?,R"
+ "Tr^{MTLDepthStencilDescriptorPrivate=@@QB@Q},R"
+ "Tr^{MTLDepthStencilDescriptorPrivate=@@QB@Q},R,D"
+ "VertexValueType"
+ "[231{?=\"name\"@\"NSString\"\"requirement\"q\"supported\"B}]"
+ "^{?=QQQQ}"
+ "^{?=QQQQ}16@0:8"
+ "^{?=dddddd}"
+ "^{?=dddddd}16@0:8"
+ "_MTLIndirectBlendColor"
+ "_MTLIndirectDepthBiasInfo"
+ "_MTLIndirectDepthTestBounds"
+ "_MTLIndirectScissorRects"
+ "_MTLIndirectStencilReferenceValues"
+ "_MTLIndirectViewports"
+ "_alpha"
+ "_backReferenceValue"
+ "_blue"
+ "_clamp"
+ "_depthBias"
+ "_familySupportsConditionalTileDispatch"
+ "_familySupportsDepthBoundsTesting"
+ "_familySupportsExtendedIndirectRenderCommand"
+ "_familySupportsFP8"
+ "_familySupportsMXU"
+ "_familySupportsSamplerReductionMode"
+ "_familySupportsTextureAccessPatterns"
+ "_frontReferenceValue"
+ "_green"
+ "_maxBounds"
+ "_minBounds"
+ "_red"
+ "_scissorRects"
+ "_slopeScale"
+ "_viewports"
+ "allowOverrideRenderStates"
+ "alpha"
+ "applegpu_g18p"
+ "backReferenceValue"
+ "blue"
+ "clamp"
+ "count (%lu) is not a supported sample count for custom positions. count must be 0, 2, 4 or 8."
+ "depthBias"
+ "familySupportsConditionalTileDispatch"
+ "familySupportsDepthBoundsTesting"
+ "familySupportsExtendedIndirectRenderCommand"
+ "familySupportsFP8"
+ "familySupportsMXU"
+ "familySupportsSamplerReductionMode"
+ "familySupportsTextureAccessPatterns"
+ "frontReferenceValue"
+ "getBlendColor"
+ "getCullMode"
+ "getDepthBiasInfo"
+ "getDepthClipMode"
+ "getDepthStencilState"
+ "getDepthStencilStateUniqueIdentifier"
+ "getDepthTestBounds"
+ "getFrontFacingWinding"
+ "getScissorRects"
+ "getStencilReferenceValues"
+ "getTriangleFillMode"
+ "getViewports"
+ "green"
+ "inheritBlendColor"
+ "inheritCullMode"
+ "inheritDepthBias"
+ "inheritDepthClipMode"
+ "inheritDepthStencilState"
+ "inheritDepthTestBounds"
+ "inheritFrontFacingWinding"
+ "inheritScissorRects"
+ "inheritStencilReferenceValues"
+ "inheritTriangleFillMode"
+ "inheritViewports"
+ "invalid writeAccessPattern (%lu)"
+ "kMetalTextureWriteAccessPattern"
+ "maxBounds"
+ "maxScissorRectCount"
+ "minBounds"
+ "optimizeContentsForTexture:readAccessPattern:"
+ "optimizeContentsForTexture:readAccessPattern:readAccessor:"
+ "optimizeContentsForTexture:readAccessPattern:readAccessor:slice:level:"
+ "optimizeContentsForTexture:readAccessPattern:slice:level:"
+ "r^{MTLDepthStencilDescriptorPrivate=@@QB@Q}16@0:8"
+ "r^{MTLRenderPassDescriptorPrivate=@@QQQBBBBQQQ(?=QQ)QQ[8{?=ff}]Q@@BqB}16@0:8"
+ "r^{MTLSamplerDescriptorPrivate=(?={?=b2b2b2b3b3b3b1b2b1b3b1b2b1b1}I)(?=If)(?=If)(?=If)Q@Q[4I]Q}16@0:8"
+ "r^{MTLTextureDescriptorPrivate=QQQQQQQQBQBBIBQ(?=QQ)QQBBQQQqQqqQQQ}16@0:8"
+ "red"
+ "reductionMode"
+ "reductionMode ="
+ "reductionMode is not a valid MTLSamplerReductionMode."
+ "samplerReductionModeSupport"
+ "scissorRects"
+ "setAllowOverrideRenderStates:"
+ "setAlpha:"
+ "setBackReferenceValue:"
+ "setBlue:"
+ "setClamp:"
+ "setDepthBias:"
+ "setDepthStencilState:atIndex:"
+ "setDepthStencilStates:withRange:"
+ "setDepthTestMinBound:maxBound:"
+ "setFrontReferenceValue:"
+ "setGreen:"
+ "setInheritBlendColor:"
+ "setInheritCullMode:"
+ "setInheritDepthBias:"
+ "setInheritDepthClipMode:"
+ "setInheritDepthStencilState:"
+ "setInheritDepthTestBounds:"
+ "setInheritFrontFacingWinding:"
+ "setInheritScissorRects:"
+ "setInheritStencilReferenceValues:"
+ "setInheritTriangleFillMode:"
+ "setInheritViewports:"
+ "setMaxBounds:"
+ "setMaxScissorRectCount:"
+ "setMaxViewportCount:"
+ "setMinBounds:"
+ "setRed:"
+ "setReductionMode:"
+ "setScissorRects:"
+ "setSlopeScale:"
+ "setViewports:"
+ "setWriteAccessPattern:"
+ "slopeScale"
+ "supportsConditionalTileDispatch"
+ "supportsDepthBoundsTesting"
+ "supportsExtendedIndirectRenderCommand"
+ "supportsFP8"
+ "supportsMXU"
+ "supportsSamplerReductionMode"
+ "supportsTextureAccessPatterns"
+ "uniqueIdentifierForDepthStencilStateAtIndex:inIndirectArgumentBuffer:atOffset:"
+ "v24@0:8^{?=QQQQ}16"
+ "v24@0:8^{?=dddddd}16"
+ "v24@0:8f16f20"
+ "v32@0:8@\"<MTLDepthStencilState>\"16Q24"
+ "v40@0:8@16q24q32"
+ "v48@0:8@16q24Q32Q40"
+ "v56@0:8@16q24q32Q40Q48"
+ "viewports"
+ "writeAccessPattern"
+ "writeAccessPattern ="
+ "{MTLDepthStencilDescriptorPrivate=\"frontFaceStencil\"@\"MTLStencilDescriptorInternal\"\"backFaceStencil\"@\"MTLStencilDescriptorInternal\"\"depthCompareFunction\"Q\"depthWriteEnabled\"B\"label\"@\"NSString\"\"resourceIndex\"Q}"
+ "{MTLIndirectCommandBufferDescriptorState=\"commandTypes\"Q\"inheritPipelineState\"B\"inheritBuffers\"B\"maxVertexBufferBindCount\"Q\"maxFragmentBufferBindCount\"Q\"maxKernelBufferBindCount\"Q\"maxKernelThreadgroupMemoryBindCount\"Q\"maxObjectBufferBindCount\"Q\"maxMeshBufferBindCount\"Q\"maxObjectThreadgroupMemoryBindCount\"Q\"supportRayTracing\"B\"supportDynamicAttributeStride\"B\"maxScissorRectCount\"C\"maxViewportCount\"C\"inheritDepthStencilState\"B\"inheritDepthBias\"B\"inheritStencilReferenceValues\"B\"inheritDepthClipMode\"B\"inheritCullMode\"B\"inheritFrontFacingWinding\"B\"inheritTriangleFillMode\"B\"inheritDepthTestBounds\"B\"inheritScissorRects\"B\"inheritViewports\"B\"inheritBlendColor\"B\"allowOverrideRenderStates\"q\"resourceIndex\"Q\"maxToolsDispatchBindings\"I\"supportColorAttachmentMapping\"B}"
+ "{MTLIndirectCommandBufferHeader=\"headerSize\"Q\"commandTypes\"I\"inheritPipelineState\"B\"inheritBuffers\"B\"maxVertexBufferBindCount\"C\"maxFragmentBufferBindCount\"C\"maxKernelBufferBindCount\"C\"maxObjectBufferBindCount\"C\"maxMeshBufferBindCount\"C\"supportRayTracing\"B\"supportDynamicAttributeStride\"B\"maxKernelThreadgroupMemoryBindCount\"C\"maxObjectThreadgroupMemoryBindCount\"C\"maxScissorRectCount\"C\"maxViewportCount\"C\"inheritDepthStencilState\"B\"inheritDepthBias\"B\"inheritStencilReferenceValues\"B\"inheritDepthClipMode\"B\"inheritCullMode\"B\"inheritFrontFacingWinding\"B\"inheritTriangleFillMode\"B\"inheritDepthTestBounds\"B\"inheritScissorRects\"B\"inheritViewports\"B\"inheritBlendColor\"B\"allowOverrideRenderStates\"q\"size\"Q}"
+ "{MTLRenderPassDescriptorPrivate=\"attachments\"@\"MTLRenderPassColorAttachmentDescriptorArrayInternal\"\"visibilityResultBuffer\"@\"<MTLBuffer>\"\"renderTargetWidth\"Q\"renderTargetHeight\"Q\"defaultColorSampleCount\"Q\"fineGrainedBackgroundVisibilityEnabled\"B\"skipEmptyTilesOnClearEnabled\"B\"ditherEnabled\"B\"openGLModeEnabled\"B\"renderTargetArrayLength\"Q\"tileWidth\"Q\"tileHeight\"Q\"\"(?=\"defaultSampleCount\"Q\"defaultRasterSampleCount\"Q)\"imageBlockSampleLength\"Q\"threadgroupMemoryLength\"Q\"customSamplePositions\"[8{?=\"x\"f\"y\"f}]\"numCustomSamplePositions\"Q\"rasterizationRateMap\"@\"<MTLRasterizationRateMap>\"\"sampleBufferAttachments\"@\"MTLRenderPassSampleBufferAttachmentDescriptorArrayInternal\"\"pointCoordYFlipEnabled\"B\"visibilityResultType\"q\"supportColorAttachmentMapping\"B}"
+ "{MTLSamplerDescriptorPrivate=\"\"(?=\"\"{?=\"minFilter\"b2\"magFilter\"b2\"mipFilter\"b2\"sAddressMode\"b3\"tAddressMode\"b3\"rAddressMode\"b3\"normalizedCoords\"b1\"borderColor\"b2\"lodAverage\"b1\"compareFunction\"b3\"supportArgumentBuffers\"b1\"reductionMode\"b2\"forceResourceIndex\"b1\"forceSeamsOnCubemapFiltering\"b1}\"miscHash\"I)\"\"(?=\"lodMinClampHash\"I\"lodMinClamp\"f)\"\"(?=\"lodMaxClampHash\"I\"lodMaxClamp\"f)\"\"(?=\"lodBiasHash\"I\"lodBias\"f)\"maxAnisotropy\"Q\"label\"@\"NSString\"\"resourceIndex\"Q\"customBorderColorValue\"[4I]\"pixelFormat\"Q}"
+ "{MTLTextureDescriptorPrivate=\"textureType\"Q\"pixelFormat\"Q\"width\"Q\"height\"Q\"depth\"Q\"mipmapLevelCount\"Q\"sampleCount\"Q\"arrayLength\"Q\"zeroFill\"B\"rotation\"Q\"framebufferOnly\"B\"isDrawable\"B\"swizzle\"I\"writeSwizzleEnabled\"B\"compressionMode\"Q\"\"(?=\"textureUsage\"Q\"usage\"Q)\"resourceOptions\"Q\"sparseSurfaceDefaultValue\"Q\"allowGPUOptimizedContents\"B\"forceResourceIndex\"B\"resourceIndex\"Q\"protectionOptions\"Q\"compressionFootprint\"Q\"compressionType\"q\"colorSpaceConversionMatrix\"Q\"writeAccessPattern\"q\"placementSparsePageSize\"q\"resolvedUsage\"Q\"cpuCacheMode\"Q\"storageMode\"Q}"
+ "{MTLTextureViewDescriptorPrivate=\"pixelFormat\"Q\"textureType\"Q\"levels\"{_NSRange=\"location\"Q\"length\"Q}\"slices\"{_NSRange=\"location\"Q\"length\"Q}\"writeAccessPattern\"q\"swizzle\"I\"resourceIndex\"Q}"
- "21:29:55"
- "Aug 27 2025"
- "Aug 27 2025 21:29:55"
- "Tr^{MTLDepthStencilDescriptorPrivate=@@QB@},R"
- "Tr^{MTLDepthStencilDescriptorPrivate=@@QB@},R,D"
- "[224{?=\"name\"@\"NSString\"\"requirement\"q\"supported\"B}]"
- "count (%lu) is not a supported sample count for custom positions. count must be 0, 2 or 4."
- "r^{MTLDepthStencilDescriptorPrivate=@@QB@}16@0:8"
- "r^{MTLRenderPassDescriptorPrivate=@@QQQBBBBQQQ(?=QQ)QQ[4{?=ff}]Q@@BqB}16@0:8"
- "r^{MTLSamplerDescriptorPrivate=(?={?=b2b2b2b3b3b3b1b2b1b3b1b1b1}I)(?=If)(?=If)(?=If)Q@Q[4I]Q}16@0:8"
- "r^{MTLTextureDescriptorPrivate=QQQQQQQQBQBBIBQ(?=QQ)QQBBQQQqQqQQQ}16@0:8"
- "{MTLDepthStencilDescriptorPrivate=\"frontFaceStencil\"@\"MTLStencilDescriptorInternal\"\"backFaceStencil\"@\"MTLStencilDescriptorInternal\"\"depthCompareFunction\"Q\"depthWriteEnabled\"B\"label\"@\"NSString\"}"
- "{MTLIndirectCommandBufferDescriptorState=\"commandTypes\"Q\"inheritPipelineState\"B\"inheritBuffers\"B\"maxVertexBufferBindCount\"Q\"maxFragmentBufferBindCount\"Q\"maxKernelBufferBindCount\"Q\"maxKernelThreadgroupMemoryBindCount\"Q\"maxObjectBufferBindCount\"Q\"maxMeshBufferBindCount\"Q\"maxObjectThreadgroupMemoryBindCount\"Q\"supportRayTracing\"B\"supportDynamicAttributeStride\"B\"resourceIndex\"Q\"maxToolsDispatchBindings\"I\"supportColorAttachmentMapping\"B}"
- "{MTLIndirectCommandBufferHeader=\"headerSize\"Q\"commandTypes\"I\"inheritPipelineState\"B\"inheritBuffers\"B\"maxVertexBufferBindCount\"C\"maxFragmentBufferBindCount\"C\"maxKernelBufferBindCount\"C\"maxObjectBufferBindCount\"C\"maxMeshBufferBindCount\"C\"supportRayTracing\"B\"supportDynamicAttributeStride\"B\"maxKernelThreadgroupMemoryBindCount\"C\"maxObjectThreadgroupMemoryBindCount\"C\"size\"Q}"
- "{MTLRenderPassDescriptorPrivate=\"attachments\"@\"MTLRenderPassColorAttachmentDescriptorArrayInternal\"\"visibilityResultBuffer\"@\"<MTLBuffer>\"\"renderTargetWidth\"Q\"renderTargetHeight\"Q\"defaultColorSampleCount\"Q\"fineGrainedBackgroundVisibilityEnabled\"B\"skipEmptyTilesOnClearEnabled\"B\"ditherEnabled\"B\"openGLModeEnabled\"B\"renderTargetArrayLength\"Q\"tileWidth\"Q\"tileHeight\"Q\"\"(?=\"defaultSampleCount\"Q\"defaultRasterSampleCount\"Q)\"imageBlockSampleLength\"Q\"threadgroupMemoryLength\"Q\"customSamplePositions\"[4{?=\"x\"f\"y\"f}]\"numCustomSamplePositions\"Q\"rasterizationRateMap\"@\"<MTLRasterizationRateMap>\"\"sampleBufferAttachments\"@\"MTLRenderPassSampleBufferAttachmentDescriptorArrayInternal\"\"pointCoordYFlipEnabled\"B\"visibilityResultType\"q\"supportColorAttachmentMapping\"B}"
- "{MTLSamplerDescriptorPrivate=\"\"(?=\"\"{?=\"minFilter\"b2\"magFilter\"b2\"mipFilter\"b2\"sAddressMode\"b3\"tAddressMode\"b3\"rAddressMode\"b3\"normalizedCoords\"b1\"borderColor\"b2\"lodAverage\"b1\"compareFunction\"b3\"supportArgumentBuffers\"b1\"forceResourceIndex\"b1\"forceSeamsOnCubemapFiltering\"b1}\"miscHash\"I)\"\"(?=\"lodMinClampHash\"I\"lodMinClamp\"f)\"\"(?=\"lodMaxClampHash\"I\"lodMaxClamp\"f)\"\"(?=\"lodBiasHash\"I\"lodBias\"f)\"maxAnisotropy\"Q\"label\"@\"NSString\"\"resourceIndex\"Q\"customBorderColorValue\"[4I]\"pixelFormat\"Q}"
- "{MTLTextureDescriptorPrivate=\"textureType\"Q\"pixelFormat\"Q\"width\"Q\"height\"Q\"depth\"Q\"mipmapLevelCount\"Q\"sampleCount\"Q\"arrayLength\"Q\"zeroFill\"B\"rotation\"Q\"framebufferOnly\"B\"isDrawable\"B\"swizzle\"I\"writeSwizzleEnabled\"B\"compressionMode\"Q\"\"(?=\"textureUsage\"Q\"usage\"Q)\"resourceOptions\"Q\"sparseSurfaceDefaultValue\"Q\"allowGPUOptimizedContents\"B\"forceResourceIndex\"B\"resourceIndex\"Q\"protectionOptions\"Q\"compressionFootprint\"Q\"compressionType\"q\"colorSpaceConversionMatrix\"Q\"placementSparsePageSize\"q\"resolvedUsage\"Q\"cpuCacheMode\"Q\"storageMode\"Q}"
- "{MTLTextureViewDescriptorPrivate=\"pixelFormat\"Q\"textureType\"Q\"levels\"{_NSRange=\"location\"Q\"length\"Q}\"slices\"{_NSRange=\"location\"Q\"length\"Q}\"swizzle\"I\"resourceIndex\"Q}"

```
