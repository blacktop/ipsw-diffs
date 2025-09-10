## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`

```diff

 370.63.0.0.0
-  __TEXT.__text: 0x12c758
+  __TEXT.__text: 0x12eec4
   __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x18d0c
-  __TEXT.__cstring: 0x3171f
+  __TEXT.__objc_methlist: 0x19324
+  __TEXT.__cstring: 0x32d86
   __TEXT.__const: 0x2f8
-  __TEXT.__gcc_except_tab: 0x2b68
+  __TEXT.__gcc_except_tab: 0x2b8c
   __TEXT.__oslogstring: 0x282e
-  __TEXT.__unwind_info: 0x50a0
+  __TEXT.__unwind_info: 0x5168
   __TEXT.__objc_classname: 0x2520
-  __TEXT.__objc_methname: 0x1e210
-  __TEXT.__objc_methtype: 0x179ca
-  __TEXT.__objc_stubs: 0x16600
-  __DATA_CONST.__got: 0xaf0
-  __DATA_CONST.__const: 0x1b28
+  __TEXT.__objc_methname: 0x1e75d
+  __TEXT.__objc_methtype: 0x17bcc
+  __TEXT.__objc_stubs: 0x16bc0
+  __DATA_CONST.__got: 0xaf8
+  __DATA_CONST.__const: 0x1b30
   __DATA_CONST.__objc_classlist: 0x748
   __DATA_CONST.__objc_protolist: 0x4c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6120
+  __DATA_CONST.__objc_selrefs: 0x62a0
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x640
   __AUTH_CONST.__auth_got: 0x628
   __AUTH_CONST.__const: 0x1d0
-  __AUTH_CONST.__cfstring: 0xe300
-  __AUTH_CONST.__objc_const: 0x45910
+  __AUTH_CONST.__cfstring: 0xe9a0
+  __AUTH_CONST.__objc_const: 0x45e30
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x1
-  __DATA.__objc_ivar: 0xfec
+  __DATA.__objc_ivar: 0xffc
   __DATA.__data: 0x3970
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x48d0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 01049353-C57D-3ABC-B3A1-CB6844685213
-  Functions: 7667
-  Symbols:   24322
-  CStrings:  10878
+  UUID: DA6E3A3E-7A5C-37AE-8F2F-609DEDAE0EB8
+  Functions: 7747
+  Symbols:   24542
+  CStrings:  11084
 
Symbols:
+ -[MTL4DebugRenderCommandEncoder setDepthTestMinBound:maxBound:]
+ -[MTL4GPUDebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:]
+ -[MTL4GPUDebugRenderCommandEncoder resetTileCondition]
+ -[MTL4ToolsRenderCommandEncoder setDepthTestMinBound:maxBound:]
+ -[MTLDebugArgumentEncoder setDepthStencilState:atIndex:]
+ -[MTLDebugArgumentEncoder setDepthStencilStates:withRange:]
+ -[MTLDebugIndirectRenderCommand setBlendColorRed:green:blue:alpha:]
+ -[MTLDebugIndirectRenderCommand setCullMode:]
+ -[MTLDebugIndirectRenderCommand setDepthBias:slopeScale:clamp:]
+ -[MTLDebugIndirectRenderCommand setDepthClipMode:]
+ -[MTLDebugIndirectRenderCommand setDepthStencilState:]
+ -[MTLDebugIndirectRenderCommand setDepthTestMinBound:maxBound:]
+ -[MTLDebugIndirectRenderCommand setFrontFacingWinding:]
+ -[MTLDebugIndirectRenderCommand setScissorRect:]
+ -[MTLDebugIndirectRenderCommand setScissorRects:count:]
+ -[MTLDebugIndirectRenderCommand setStencilFrontReferenceValue:backReferenceValue:]
+ -[MTLDebugIndirectRenderCommand setStencilReferenceValue:]
+ -[MTLDebugIndirectRenderCommand setTriangleFillMode:]
+ -[MTLDebugIndirectRenderCommand setViewport:]
+ -[MTLDebugIndirectRenderCommand setViewports:count:]
+ -[MTLDebugRenderCommandEncoder _dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:]
+ -[MTLDebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:]
+ -[MTLDebugRenderCommandEncoder dispatchThreadsPerTile:withCondition:]
+ -[MTLDebugRenderCommandEncoder maxBound]
+ -[MTLDebugRenderCommandEncoder minBound]
+ -[MTLDebugRenderCommandEncoder resetTileCondition]
+ -[MTLDebugRenderCommandEncoder setDepthTestMinBound:maxBound:]
+ -[MTLGPUDebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:]
+ -[MTLGPUDebugRenderCommandEncoder dispatchThreadsPerTile:withCondition:]
+ -[MTLGPUDebugRenderCommandEncoder resetTileCondition]
+ -[MTLLegacySVRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:]
+ -[MTLLegacySVRenderCommandEncoder dispatchThreadsPerTile:withCondition:]
+ -[MTLLegacySVRenderCommandEncoder resetTileCondition]
+ -[MTLToolsArgumentEncoder setDepthStencilState:atIndex:]
+ -[MTLToolsArgumentEncoder setDepthStencilStates:withRange:]
+ -[MTLToolsBlitCommandEncoder optimizeContentsForTexture:readAccessPattern:readAccessor:]
+ -[MTLToolsBlitCommandEncoder optimizeContentsForTexture:readAccessPattern:readAccessor:slice:level:]
+ -[MTLToolsDepthStencilState gpuResourceID]
+ -[MTLToolsDepthStencilState resourceIndex]
+ -[MTLToolsDepthStencilState uniqueIdentifier]
+ -[MTLToolsDevice samplerReductionModeSupport]
+ -[MTLToolsDevice supportsConditionalTileDispatch]
+ -[MTLToolsDevice supportsDepthBoundsTesting]
+ -[MTLToolsDevice supportsExtendedIndirectRenderCommand]
+ -[MTLToolsDevice supportsFP8]
+ -[MTLToolsDevice supportsMXU]
+ -[MTLToolsDevice supportsSamplerReductionMode]
+ -[MTLToolsDevice supportsTextureAccessPatterns]
+ -[MTLToolsIndirectRenderCommand getBlendColor]
+ -[MTLToolsIndirectRenderCommand getCullMode]
+ -[MTLToolsIndirectRenderCommand getDepthBiasInfo]
+ -[MTLToolsIndirectRenderCommand getDepthClipMode]
+ -[MTLToolsIndirectRenderCommand getDepthStencilStateUniqueIdentifier]
+ -[MTLToolsIndirectRenderCommand getDepthStencilState]
+ -[MTLToolsIndirectRenderCommand getDepthTestBounds]
+ -[MTLToolsIndirectRenderCommand getFrontFacingWinding]
+ -[MTLToolsIndirectRenderCommand getScissorRects]
+ -[MTLToolsIndirectRenderCommand getStencilReferenceValues]
+ -[MTLToolsIndirectRenderCommand getTriangleFillMode]
+ -[MTLToolsIndirectRenderCommand getViewports]
+ -[MTLToolsIndirectRenderCommand setBlendColorRed:green:blue:alpha:]
+ -[MTLToolsIndirectRenderCommand setCullMode:]
+ -[MTLToolsIndirectRenderCommand setDepthBias:slopeScale:clamp:]
+ -[MTLToolsIndirectRenderCommand setDepthClipMode:]
+ -[MTLToolsIndirectRenderCommand setDepthStencilState:]
+ -[MTLToolsIndirectRenderCommand setDepthTestMinBound:maxBound:]
+ -[MTLToolsIndirectRenderCommand setFrontFacingWinding:]
+ -[MTLToolsIndirectRenderCommand setScissorRect:]
+ -[MTLToolsIndirectRenderCommand setScissorRects:count:]
+ -[MTLToolsIndirectRenderCommand setStencilFrontReferenceValue:backReferenceValue:]
+ -[MTLToolsIndirectRenderCommand setStencilReferenceValue:]
+ -[MTLToolsIndirectRenderCommand setTriangleFillMode:]
+ -[MTLToolsIndirectRenderCommand setViewport:]
+ -[MTLToolsIndirectRenderCommand setViewports:count:]
+ -[MTLToolsRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:]
+ -[MTLToolsRenderCommandEncoder dispatchThreadsPerTile:withCondition:]
+ -[MTLToolsRenderCommandEncoder resetTileCondition]
+ -[MTLToolsRenderCommandEncoder setDepthTestMinBound:maxBound:]
+ -[MTLToolsTexture writeAccessPattern]
+ GCC_except_table108
+ GCC_except_table109
+ GCC_except_table115
+ GCC_except_table118
+ GCC_except_table119
+ GCC_except_table120
+ GCC_except_table142
+ GCC_except_table146
+ GCC_except_table162
+ GCC_except_table164
+ GCC_except_table167
+ GCC_except_table169
+ GCC_except_table174
+ GCC_except_table177
+ GCC_except_table180
+ GCC_except_table211
+ GCC_except_table289
+ GCC_except_table295
+ GCC_except_table299
+ GCC_except_table303
+ GCC_except_table313
+ GCC_except_table40
+ GCC_except_table47
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentDepthTestMaxBound
+ _OBJC_IVAR_$_MTL4DebugRenderCommandEncoder._currentDepthTestMinBound
+ _OBJC_IVAR_$_MTLDebugRenderCommandEncoder._maxBound
+ _OBJC_IVAR_$_MTLDebugRenderCommandEncoder._minBound
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MTLIndirectRenderCommandSPI
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPU31objcproto20MTLDepthStencilState11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__16vectorIPU31objcproto20MTLDepthStencilState11objc_objectNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPU31objcproto20MTLDepthStencilState11objc_objectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPU31objcproto20MTLDepthStencilState11objc_objectNS_9allocatorIS2_EEEC2B8ne200100Em
+ ___block_literal_global.1703
+ _kMetalTextureWriteAccessPattern
+ _objc_msgSend$_dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:
+ _objc_msgSend$allowOverrideRenderStates
+ _objc_msgSend$dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:
+ _objc_msgSend$dispatchThreadsPerTile:withCondition:
+ _objc_msgSend$getBlendColor
+ _objc_msgSend$getCullMode
+ _objc_msgSend$getDepthBiasInfo
+ _objc_msgSend$getDepthClipMode
+ _objc_msgSend$getDepthStencilState
+ _objc_msgSend$getDepthStencilStateUniqueIdentifier
+ _objc_msgSend$getDepthTestBounds
+ _objc_msgSend$getFrontFacingWinding
+ _objc_msgSend$getScissorRects
+ _objc_msgSend$getStencilReferenceValues
+ _objc_msgSend$getTriangleFillMode
+ _objc_msgSend$getViewports
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
+ _objc_msgSend$integerValue
+ _objc_msgSend$maxScissorRectCount
+ _objc_msgSend$optimizeContentsForTexture:readAccessPattern:readAccessor:
+ _objc_msgSend$optimizeContentsForTexture:readAccessPattern:readAccessor:slice:level:
+ _objc_msgSend$reductionMode
+ _objc_msgSend$resetTileCondition
+ _objc_msgSend$samplerReductionModeSupport
+ _objc_msgSend$setDepthStencilState:atIndex:
+ _objc_msgSend$setDepthStencilStates:withRange:
+ _objc_msgSend$setDepthTestMinBound:maxBound:
+ _objc_msgSend$setWriteAccessPattern:
+ _objc_msgSend$supportsConditionalTileDispatch
+ _objc_msgSend$supportsDepthBoundsTesting
+ _objc_msgSend$supportsExtendedIndirectRenderCommand
+ _objc_msgSend$supportsFP8
+ _objc_msgSend$supportsMXU
+ _objc_msgSend$supportsSamplerReductionMode
+ _objc_msgSend$supportsTextureAccessPatterns
+ _objc_msgSend$writeAccessPattern
- GCC_except_table110
- GCC_except_table111
- GCC_except_table139
- GCC_except_table143
- GCC_except_table148
- GCC_except_table150
- GCC_except_table161
- GCC_except_table163
- GCC_except_table170
- GCC_except_table173
- GCC_except_table176
- GCC_except_table202
- GCC_except_table275
- GCC_except_table288
- GCC_except_table292
- GCC_except_table296
- GCC_except_table306
- ___block_literal_global.1659
CStrings:
+ "-[MTL4DebugRenderCommandEncoder setDepthTestMinBound:maxBound:]"
+ "-[MTLDebugArgumentEncoder setDepthStencilState:atIndex:]"
+ "-[MTLDebugArgumentEncoder setDepthStencilStates:withRange:]"
+ "-[MTLDebugIndirectRenderCommand setBlendColorRed:green:blue:alpha:]"
+ "-[MTLDebugIndirectRenderCommand setCullMode:]"
+ "-[MTLDebugIndirectRenderCommand setDepthBias:slopeScale:clamp:]"
+ "-[MTLDebugIndirectRenderCommand setDepthClipMode:]"
+ "-[MTLDebugIndirectRenderCommand setDepthStencilState:]"
+ "-[MTLDebugIndirectRenderCommand setDepthTestMinBound:maxBound:]"
+ "-[MTLDebugIndirectRenderCommand setFrontFacingWinding:]"
+ "-[MTLDebugIndirectRenderCommand setScissorRect:]"
+ "-[MTLDebugIndirectRenderCommand setScissorRects:count:]"
+ "-[MTLDebugIndirectRenderCommand setStencilFrontReferenceValue:backReferenceValue:]"
+ "-[MTLDebugIndirectRenderCommand setStencilReferenceValue:]"
+ "-[MTLDebugIndirectRenderCommand setTriangleFillMode:]"
+ "-[MTLDebugIndirectRenderCommand setViewport:]"
+ "-[MTLDebugIndirectRenderCommand setViewports:count:]"
+ "-[MTLDebugRenderCommandEncoder _dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:]"
+ "-[MTLDebugRenderCommandEncoder resetTileCondition]"
+ "-[MTLDebugRenderCommandEncoder setDepthTestMinBound:maxBound:]"
+ "@\"<MTLDepthStencilState>\"16@0:8"
+ "@\"_MTLIndirectBlendColor\"16@0:8"
+ "@\"_MTLIndirectDepthBiasInfo\"16@0:8"
+ "@\"_MTLIndirectDepthTestBounds\"16@0:8"
+ "@\"_MTLIndirectScissorRects\"16@0:8"
+ "@\"_MTLIndirectStencilReferenceValues\"16@0:8"
+ "@\"_MTLIndirectViewports\"16@0:8"
+ "Conditional Tile Dispatch Validation"
+ "DepthStencilState"
+ "Invalid usage because device does not support depth bounds testing."
+ "MTLSamplerDescriptor: Use of minimum or maximum reductionMode requires device support"
+ "Render Command Encoder Set Depth Test Bounds Validation"
+ "Render property inheritBlendColor cannot be set to NO with Compute Indirect Command Type"
+ "Render property inheritCullMode cannot be set to NO with Compute Indirect Command Type"
+ "Render property inheritDepthBias cannot be set to NO with Compute Indirect Command Type"
+ "Render property inheritDepthClipMode cannot be set to NO with Compute Indirect Command Type"
+ "Render property inheritDepthStencilState is set to NO, but depth stencil state must be inherited on this device"
+ "Render property inheritDepthTestBounds cannot be set to NO with Compute Indirect Command Type"
+ "Render property inheritScissorRects cannot be set to NO with Compute Indirect Command Type"
+ "Render property inheritStencilReferenceValues cannot be set to NO with Compute Indirect Command Type"
+ "Render property inheritTriangleFillMode cannot be set to NO with Compute Indirect Command Type"
+ "Render property inheritViewports cannot be set to NO with Compute Indirect Command Type"
+ "Reset Tile Condition Validation"
+ "Set Blend Color  Validation"
+ "Set Depth Bounds Validation"
+ "Set Depth Test Bounds"
+ "Set Stencil Reference Values Validation"
+ "Set Viewport Validation"
+ "Set Viewports Validation"
+ "Setting blend color on an indirect command buffer created with inheritBlendColor = YES is invalid"
+ "Setting cull mode on an indirect command buffer created with inheritCullMode = YES is invalid"
+ "Setting depth bias on a indirect command buffer created with inheritDepthBias = YES is invalid"
+ "Setting depth clip mode on an indirect command buffer created with inheritDepthClipMode = YES is invalid"
+ "Setting depth stencil state on an indirect command buffer created with inheritDepthStencilState = YES is invalid"
+ "Setting depth test bounds on an indirect command buffer created with inheritDepthTestBounds = YES is invalid"
+ "Setting front facing windning on an indirect command buffer created with inheritFrontFacingWinding = YES is invalid"
+ "Setting scissor rect on an indirect command buffer created with inheritScissorRects = YES is invalid"
+ "Setting scissor rects on an indirect command buffer created with inheritScissorRects = YES is invalid"
+ "Setting stencil reference values on an indirect command buffer created with inheritStencilReferenceValues = YES is invalid"
+ "Setting triangle fill mode on an indirect command buffer created with inheritTriangleFillMode = YES is invalid"
+ "Setting viewport on an indirect command buffer created with inheritViewport = YES is invalid"
+ "Setting viewports on an indirect command buffer created with inheritViewports = YES is invalid"
+ "Tf,R,N,V_maxBound"
+ "Tf,R,N,V_minBound"
+ "Tq,?,R"
+ "_currentDepthTestMaxBound"
+ "_currentDepthTestMinBound"
+ "_dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:"
+ "_maxBound"
+ "_minBound"
+ "allowOverrideRenderStates"
+ "count(%lu) must be <= maxScissorRectCount(%lu)."
+ "count(%lu) must be <= maxViewportCount(%lu)."
+ "depthStencilState is not a MTLDepthStencilState"
+ "depthStencilState must not be nil"
+ "device does not support conditional tile dispatch"
+ "dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:"
+ "dispatchThreadsPerTile:withCondition:"
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
+ "inheritBlendColor"
+ "inheritBlendColor is set to NO, but blend color must be inherited on this device"
+ "inheritCullMode"
+ "inheritCullMode is set to NO, but cull mode must be inherited on this device"
+ "inheritDepthBias"
+ "inheritDepthBias is set to NO, but depth bias must be inherited on this device"
+ "inheritDepthClipMode"
+ "inheritDepthStencilState"
+ "inheritDepthStencilState is set to NO, but depth stencil state must be inherited on this device"
+ "inheritDepthTestBounds"
+ "inheritDepthTestBounds is set to NO, but depth test bounds must be inherited on this device"
+ "inheritFrontFacingWinding"
+ "inheritScissorRects"
+ "inheritScissorRects is set to NO, but scissor rects must be inherited on this device"
+ "inheritStencilReferenceValues"
+ "inheritStencilReferenceValues is set to NO, but stencil reference values must be inherited on this device"
+ "inheritTriangleFillMode"
+ "inheritTriangleFillMode is set to NO, but triangle fill mode must be inherited on this device"
+ "inheritViewports"
+ "inheritViewports is set to NO, but viewports must be inherited on this device"
+ "integerValue"
+ "invalid usage because device does not support depth bounds testing."
+ "maxBound"
+ "maxBound ="
+ "maxBound(%g) must be between 0.0f and 1.0f."
+ "maxScissorRectCount"
+ "maximum scissor rect count (%lu) must be <= %lu."
+ "maximum viewport count (%lu) must be <= %lu."
+ "minBound"
+ "minBound ="
+ "minBound(%) and maxBound(%) must be between 0.0f and 1.0f and minBound <= maxBound"
+ "minBound(%g) must be <= maxBound(%g)."
+ "minBound(%g) must be between 0.0f and 1.0f."
+ "optimizeContentsForTexture:readAccessPattern:readAccessor:"
+ "optimizeContentsForTexture:readAccessPattern:readAccessor:slice:level:"
+ "reductionMode"
+ "redundant setDepthTestMinBound."
+ "resetTileCondition"
+ "samplerReductionModeSupport"
+ "setDepthStencilState:atIndex:"
+ "setDepthStencilStates:withRange:"
+ "setDepthTestMinBound:maxBound:"
+ "setWriteAccessPattern:"
+ "supportsConditionalTileDispatch"
+ "supportsDepthBoundsTesting"
+ "supportsExtendedIndirectRenderCommand"
+ "supportsFP8"
+ "supportsMXU"
+ "supportsSamplerReductionMode"
+ "supportsTextureAccessPatterns"
+ "texture view creation cannot change access pattern hint for texture with allowGPUOptimizedContents==NO"
+ "texture view creation is setting coherent access pattern hint on a texture that does not support lossless compression"
+ "texture view creation is setting incoherent access pattern hint on a texture that is only used as a render target"
+ "v100@0:8{?=QQQ}16{?={?=QQQ}{?=QQQ}}40I88q92"
+ "v24@0:8f16f20"
+ "v32@0:8@\"<MTLDepthStencilState>\"16Q24"
+ "v40@0:8@\"<MTLTexture>\"16q24q32"
+ "v40@0:8@16q24q32"
+ "v48@0:8{?=QQQ}16q40"
+ "v56@0:8@\"<MTLTexture>\"16q24q32Q40Q48"
+ "v56@0:8@16q24q32Q40Q48"
+ "v64@0:8{?=QQQ}16^{?={?=QQQ}{?=QQQ}}40^I48q56"
+ "writeAccessPattern"

```
