## MetalSerializer

> `/System/Library/PrivateFrameworks/MetalSerializer.framework/Versions/A/MetalSerializer`

```diff

-367.6.0.0.0
-  __TEXT.__text: 0x1afc8
+368.11.4.0.0
+  __TEXT.__text: 0x1adf4
   __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_methlist: 0x22a8
+  __TEXT.__objc_methlist: 0x3734
   __TEXT.__gcc_except_tab: 0x1d4
   __TEXT.__cstring: 0x18f9
   __TEXT.__const: 0x238
   __TEXT.__oslogstring: 0x2ef
-  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__unwind_info: 0x7e0
   __TEXT.__objc_classname: 0x33b
   __TEXT.__objc_methname: 0x7e48
   __TEXT.__objc_methtype: 0x299e

   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1930
+  __DATA_CONST.__objc_selrefs: 0x1bd0
   __DATA_CONST.__objc_superrefs: 0x78
   __AUTH_CONST.__auth_got: 0x200
   __AUTH_CONST.__const: 0x260
   __AUTH_CONST.__cfstring: 0x940
-  __AUTH_CONST.__objc_const: 0x7678
+  __AUTH_CONST.__objc_const: 0x4e70
   __AUTH.__objc_data: 0x4b0
   __DATA.__objc_ivar: 0x170
   __DATA.__data: 0x600

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5600E6C8-6F2D-3435-AF31-D75E937F13D5
-  Functions: 861
-  Symbols:   1965
+  UUID: F10DF552-4378-3FB8-A694-FF03B7306862
+  Functions: 877
+  Symbols:   1984
   CStrings:  1575
 
Symbols:
+ -[MTLSerializer newSharedTextureWithDescriptor:allocator:].cold.1
+ -[MTLSerializer newSharedTextureWithHandle:].cold.1
+ -[MTLSerializerRenderCommandEncoder setAlphaTestReferenceValue:].cold.1
+ -[MTLSerializerRenderCommandEncoder setClipPlane:p2:p3:p4:atIndex:].cold.1
+ -[MTLSerializerRenderCommandEncoder setColorResolveTexture:slice:depthPlane:level:yInvert:atIndex:].cold.1
+ -[MTLSerializerRenderCommandEncoder setDepthCleared].cold.1
+ -[MTLSerializerRenderCommandEncoder setDepthResolveTexture:slice:depthPlane:level:yInvert:].cold.1
+ -[MTLSerializerRenderCommandEncoder setFragmentSamplerState:lodMinClamp:lodMaxClamp:lodBias:atIndex:].cold.1
+ -[MTLSerializerRenderCommandEncoder setPointSize:].cold.1
+ -[MTLSerializerRenderCommandEncoder setPrimitiveRestartEnabled:].cold.1
+ -[MTLSerializerRenderCommandEncoder setPrimitiveRestartEnabled:index:].cold.1
+ -[MTLSerializerRenderCommandEncoder setProvokingVertexMode:].cold.1
+ -[MTLSerializerRenderCommandEncoder setStencilCleared].cold.1
+ -[MTLSerializerRenderCommandEncoder setStencilResolveTexture:slice:depthPlane:level:yInvert:].cold.1
+ -[MTLSerializerRenderCommandEncoder setTransformFeedbackState:].cold.1
+ -[MTLSerializerRenderCommandEncoder setTriangleFrontFillMode:backFillMode:].cold.1
+ -[MTLSerializerRenderCommandEncoder setVertexSamplerState:lodMinClamp:lodMaxClamp:lodBias:atIndex:].cold.1
+ -[MTLSerializerRenderCommandEncoder setViewportTransformEnabled:].cold.1
+ -[_MTLDeserializer initWithDevice:generateResourceRefs:objectDelegate:createQueues:].cold.1
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__15dequeIjNS_9allocatorIjEEE25__maybe_remove_back_spareB8ne190102Eb
+ __ZNSt3__15dequeIjNS_9allocatorIjEEED2B8ne190102Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__15dequeIjNS_9allocatorIjEEE25__maybe_remove_back_spareB8ne180100Eb
- __ZNSt3__15dequeIjNS_9allocatorIjEEED2B8ne180100Ev
- __ZSt28__throw_bad_array_new_lengthB8ne180100v

```
