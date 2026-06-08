## AppleMetalGLRenderer

> `/System/Library/Extensions/AppleMetalGLRenderer.bundle/AppleMetalGLRenderer`

```diff

-104.1.0.0.0
-  __TEXT.__text: 0x18348
-  __TEXT.__auth_stubs: 0x790
+105.0.0.0.0
+  __TEXT.__text: 0x182e0
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__gcc_except_tab: 0x34c
+  __TEXT.__gcc_except_tab: 0x318
   __TEXT.__const: 0x860
   __TEXT.__cstring: 0x1939
   __TEXT.__oslogstring: 0xb9
-  __TEXT.__unwind_info: 0x788
-  __TEXT.__objc_classname: 0x1a
-  __TEXT.__objc_methname: 0x167b
-  __TEXT.__objc_methtype: 0x192
-  __TEXT.__objc_stubs: 0x1c60
-  __DATA_CONST.__got: 0xc8
+  __TEXT.__unwind_info: 0x860
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1f30
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x758
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x3d8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xac0
   __AUTH_CONST.__cfstring: 0x1320
   __AUTH_CONST.__objc_const: 0xb8
+  __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0x10
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 245FD5F9-7D38-3101-BF7A-BA45EF484BBB
+  UUID: 2432670A-420A-36F3-BBF4-9CEB18515B52
   Functions: 562
   Symbols:   1527
-  CStrings:  810
+  CStrings:  570
 
Symbols:
+ __ZNSt3__119__allocate_at_leastB9fqn220100INS_9allocatorIP17GLRBufferResourceEENS_16allocator_traitsIS4_EEEENS_19__allocation_resultINT0_7pointerENS8_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqn220100INS_9allocatorIjEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__16vectorIP17GLRBufferResourceNS_9allocatorIS2_EEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIP17GLRBufferResourceNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9fqn220100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE24__emplace_back_slow_pathIJRKjEEEPjDpOT_
+ __ZSt28__throw_bad_array_new_lengthB9fqn220100v
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- __ZNSt3__119__allocate_at_leastB9nqn210106INS_9allocatorIP17GLRBufferResourceEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB9nqn210106INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__16vectorIP17GLRBufferResourceNS_9allocatorIS2_EEE20__throw_length_errorB9nqn210106Ev
- __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9nqn210106Ev
- __ZSt28__throw_bad_array_new_lengthB9nqn210106v
CStrings:
- "@32@0:8@16@24"
- "GLRRenderPipelineStateES"
- "_internal"
- "addCompletedHandler:"
- "addEntriesFromDictionary:"
- "addObject:"
- "addScheduledHandler:"
- "array"
- "arrayLength"
- "attachVertexDescriptor:"
- "attributes"
- "backFaceStencil"
- "bitCodeHash"
- "blitCommandEncoder"
- "bundleIdentifier"
- "bundlePath"
- "cStringUsingEncoding:"
- "canGenerateMipmapLevels"
- "code"
- "colorAttachments"
- "commandBufferWithUnretainedReferences"
- "commit"
- "componentsJoinedByString:"
- "containsObject:"
- "contents"
- "copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:"
- "copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:"
- "copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:"
- "count"
- "dealloc"
- "depth"
- "depthAttachment"
- "deviceLinearTextureAlignmentBytes"
- "dictionaryWithCapacity:"
- "drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:"
- "drawPrimitives:vertexStart:vertexCount:"
- "drawPrimitives:vertexStart:vertexCount:instanceCount:"
- "endEncoding"
- "error"
- "familyName"
- "frontFaceStencil"
- "functionType"
- "generateMipmapLevel:slice:"
- "generateMipmapsForTexture:"
- "getBytes:bytesPerRow:bytesPerImage:fromRegion:mipmapLevel:slice:"
- "getBytes:length:"
- "getShaderCacheKeys"
- "height"
- "initWithArray:"
- "initWithFormat:"
- "initWithPath:"
- "initWithPipelineState:reflection:"
- "intValue"
- "iosurface"
- "iosurfaceReadOnlyTextureAlignmentBytes"
- "iosurfaceTextureAlignmentBytes"
- "isComplete"
- "layouts"
- "length"
- "level"
- "localizedDescription"
- "mainBundle"
- "mapShaderSampleBufferWithBuffer:capacity:size:"
- "maxFramebufferStorageBits"
- "methodForSelector:"
- "mipmapLevelCount"
- "name"
- "newBufferWithBytes:length:options:"
- "newBufferWithBytesNoCopy:length:options:deallocator:"
- "newBufferWithLength:options:"
- "newCommandQueueWithDescriptor:"
- "newDepthStencilStateWithDescriptor:"
- "newFragmentShaderDebugInfo"
- "newFunctionWithGLESIR:inputsDescription:functionType:"
- "newFunctionWithName:"
- "newLibraryWithFile:error:"
- "newLinearTextureWithDescriptor:offset:bytesPerRow:bytesPerImage:"
- "newRenderPipelineStateWithDescriptor:error:"
- "newRenderPipelineStateWithDescriptor:options:reflection:error:"
- "newSamplerStateWithDescriptor:"
- "newTextureViewWithPixelFormat:textureType:levels:slices:"
- "newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:"
- "newTextureWithDescriptor:"
- "newTextureWithDescriptor:iosurface:plane:"
- "newVertexShaderDebugInfo"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithLongLong:"
- "objectAtIndexedSubscript:"
- "objectForInfoDictionaryKey:"
- "objectForKey:"
- "originalObject"
- "pathForResource:ofType:"
- "pixelFormat"
- "rangeOfString:"
- "readsDepth"
- "readsStencil"
- "removeAllObjects"
- "renderCommandEncoderWithDescriptor:"
- "renderPassDescriptor"
- "replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:"
- "sampleCount"
- "sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:"
- "setAlphaBlendOperation:"
- "setAlphaTestEnabled:"
- "setAlphaTestFunction:"
- "setAlphaTestReferenceValue:"
- "setAlphaToCoverageEnabled:"
- "setAlphaToOneEnabled:"
- "setArrayLength:"
- "setBlendColorRed:green:blue:alpha:"
- "setBlendingEnabled:"
- "setBufferIndex:"
- "setClearColor:"
- "setClearDepth:"
- "setClearStencil:"
- "setClipDistanceEnableMask:"
- "setColorResolveTexture:slice:depthPlane:level:atIndex:"
- "setColorResolveTexture:slice:depthPlane:level:yInvert:atIndex:"
- "setColorStoreAction:atIndex:"
- "setCommandDataCorruptModeSPI:"
- "setCompareFunction:"
- "setCpuCacheMode:"
- "setCullMode:"
- "setDepth:"
- "setDepthAttachmentPixelFormat:"
- "setDepthBias:slopeScale:clamp:"
- "setDepthCleared"
- "setDepthCompareFunction:"
- "setDepthFailureOperation:"
- "setDepthPlane:"
- "setDepthStencilPassOperation:"
- "setDepthStencilState:"
- "setDepthStencilWriteDisabled:"
- "setDepthStoreAction:"
- "setDepthWriteEnabled:"
- "setDestinationAlphaBlendFactor:"
- "setDestinationRGBBlendFactor:"
- "setDitherEnabled:"
- "setFormat:"
- "setFragmentBuffer:offset:atIndex:"
- "setFragmentBytes:length:atIndex:"
- "setFragmentDepthCompareClampMask:"
- "setFragmentFunction:"
- "setFragmentSamplerState:atIndex:"
- "setFragmentSamplerState:lodMinClamp:lodMaxClamp:atIndex:"
- "setFragmentTexture:atIndex:"
- "setFrontFacingWinding:"
- "setGPUPriority:"
- "setHeight:"
- "setIsOpenGLQueue:"
- "setLabel:"
- "setLevel:"
- "setLineWidth:"
- "setLoadAction:"
- "setLodMaxClamp:"
- "setLodMinClamp:"
- "setLogicOperation:"
- "setLogicOperationEnabled:"
- "setMagFilter:"
- "setMaxAnisotropy:"
- "setMaxCommandBufferCount:"
- "setMinFilter:"
- "setMipFilter:"
- "setMipmapLevelCount:"
- "setNormalizedCoordinates:"
- "setObject:forKey:"
- "setOffset:"
- "setOpenGLModeEnabled:"
- "setPixelFormat:"
- "setPointCoordYFlipEnabled:"
- "setPointSmoothEnabled:"
- "setPrimitiveRestartEnabled:"
- "setProvokingVertexMode:"
- "setRAddressMode:"
- "setRasterizationEnabled:"
- "setReadMask:"
- "setRenderPipelineState:"
- "setResolveTexture:"
- "setRgbBlendOperation:"
- "setSAddressMode:"
- "setSampleCount:"
- "setSampleCoverage:"
- "setSampleCoverageInvert:"
- "setSampleMask:"
- "setScissorRect:"
- "setShaderDebugInfoCaching:"
- "setSlice:"
- "setSourceAlphaBlendFactor:"
- "setSourceRGBBlendFactor:"
- "setStencilAttachmentPixelFormat:"
- "setStencilCleared"
- "setStencilCompareFunction:"
- "setStencilFailureOperation:"
- "setStencilFrontReferenceValue:backReferenceValue:"
- "setStencilReferenceValue:"
- "setStencilStoreAction:"
- "setStepFunction:"
- "setStepRate:"
- "setStorageMode:"
- "setStoreAction:"
- "setStride:"
- "setSwizzleKey:"
- "setTAddressMode:"
- "setTexture:"
- "setTextureType:"
- "setTriangleFillMode:"
- "setUsage:"
- "setVertexBuffer:offset:atIndex:"
- "setVertexBufferOffset:atIndex:"
- "setVertexBytes:length:atIndex:"
- "setVertexDepthCompareClampMask:"
- "setVertexFunction:"
- "setVertexSamplerState:lodMinClamp:lodMaxClamp:atIndex:"
- "setVertexTexture:atIndex:"
- "setViewport:"
- "setViewportTransformEnabled:"
- "setVisibilityResultBuffer:"
- "setVisibilityResultMode:offset:"
- "setWidth:"
- "setWriteMask:"
- "setWriteSwizzleEnabled:"
- "setYInvert:"
- "stencilAttachment"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "supportsFamily:"
- "swizzleKey"
- "texture"
- "texture2DDescriptorWithPixelFormat:width:height:mipmapped:"
- "textureType"
- "unmapShaderSampleBuffer"
- "usageFlags"
- "v16@0:8"
- "waitUntilComplete"
- "width"
- "writesDepth"
- "writesStencil"
- "{?=\"renderPipelineState\"@\"<MTLRenderPipelineStateSPI>\"\"usageFlags\"{?=\"fragmentUsesDiscard\"b1\"fragmentWritesSampleMask\"b1\"fragmentWritesDepth\"b1\"vertexRegisterSpill\"b1\"fragmentRegisterSpill\"b1\"fragmentReadsFramebufferValues\"b1\"fragmentPunchThrough\"b1\"vertexWritesPointSize\"b1\"private2\"b1\"vertexThreadInvariantRegisterSpill\"b1\"fragmentThreadInvariantRegisterSpill\"b1\"reserved\"b53}}"

```
