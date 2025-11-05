## MTLSimDriver

> `/System/Library/PrivateFrameworks/MTLSimDriver.framework/Versions/A/MTLSimDriver`

```diff

-367.6.0.0.0
-  __TEXT.__text: 0x1c120
+368.11.4.0.0
+  __TEXT.__text: 0x1bf60
   __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x1668
+  __TEXT.__objc_methlist: 0x4c6c
   __TEXT.__const: 0x23a
   __TEXT.__gcc_except_tab: 0x3fc
   __TEXT.__cstring: 0x1a00
   __TEXT.__oslogstring: 0x1af
-  __TEXT.__unwind_info: 0x728
+  __TEXT.__unwind_info: 0x750
   __TEXT.__eh_frame: 0xd0
   __TEXT.__objc_classname: 0x560
   __TEXT.__objc_methname: 0xb1dc

   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1228
+  __DATA_CONST.__objc_selrefs: 0x2780
   __DATA_CONST.__objc_superrefs: 0xb0
   __AUTH_CONST.__auth_got: 0x420
   __AUTH_CONST.__const: 0x690
   __AUTH_CONST.__cfstring: 0xaa0
-  __AUTH_CONST.__objc_const: 0x13b20
+  __AUTH_CONST.__objc_const: 0xd238
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x730
   __DATA.__objc_ivar: 0x288

   - /usr/lib/libate.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B8524C60-B4B9-3AFA-A156-34B692239F36
-  Functions: 668
-  Symbols:   2061
+  UUID: BF6A9615-D67C-3939-AA90-9FFD9D502D8F
+  Functions: 684
+  Symbols:   2082
   CStrings:  2400
 
Symbols:
+ -[MTLSimBuffer initWithDevice:bufferRef:content:pointer:length:options:heap:deallocator:].cold.1
+ -[MTLSimBuffer initWithDevice:bufferRef:content:pointer:length:options:heap:deallocator:].cold.2
+ -[MTLSimBuffer initWithDevice:bufferRef:content:pointer:length:options:heap:deallocator:].cold.3
+ -[MTLSimBuffer newTextureWithDescriptor:offset:bytesPerRow:].cold.1
+ -[MTLSimBuffer newTextureWithDescriptor:offset:bytesPerRow:].cold.2
+ -[MTLSimBuffer newTextureWithDescriptor:offset:bytesPerRow:].cold.3
+ -[MTLSimCommandBuffer setProtectionOptions:].cold.1
+ -[MTLSimDevice _fixUpSwizzleForTexture:key:].cold.1
+ -[MTLSimDevice init].cold.1
+ -[MTLSimDevice minimumLinearTextureAlignmentForPixelFormat:].cold.1
+ -[MTLSimDevice minimumTextureBufferAlignmentForPixelFormat:].cold.1
+ -[MTLSimDevice newCommandQueueWithDescriptor:].cold.1
+ -[MTLSimDevice newHeapWithDescriptor:].cold.1
+ -[MTLSimDevice newSharedTextureWithDescriptor:].cold.1
+ -[MTLSimDevice newTextureWithDescriptor:].cold.1
+ -[MTLSimDevice newTextureWithDescriptor:iosurface:plane:].cold.1
+ -[MTLSimTexture initWithDescriptor:decompressedPixelFormat:iosurface:plane:textureRef:heap:device:].cold.1
+ -[MTLSimTexture initWithDescriptor:decompressedPixelFormat:iosurface:plane:textureRef:heap:device:shareable:].cold.1
+ -[MTLSimTexture initWithTextureInternal:pixelFormat:decompressedPixelFormat:textureType:levels:slices:swizzle:compressedView:textureRef:isInternalTextureView:].cold.1
+ -[MTLSimTexture newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:].cold.1
+ _ZL15decompressBlock7GLGTypePPKjPhiii.cold.1
+ __175-[MTLSimBlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:]_block_invoke.cold.1
+ __ZNSt3__110unique_ptrI29MTLSimSharedEventNotificationNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS0_I29MTLSimSharedEventNotificationNS_14default_deleteIS3_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __ZNSt3__110unique_ptrI29MTLSimSharedEventNotificationNS_14default_deleteIS1_EEE5resetB8ne180100EPS1_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_10unique_ptrI29MTLSimSharedEventNotificationNS_14default_deleteIS3_EEEEEENS_22__unordered_map_hasherIjS7_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS7_PvEEEE
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjNS_10unique_ptrI29MTLSimSharedEventNotificationNS_14default_deleteIS5_EEEEEEPvEEEEEclB8ne180100EPSB_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
CStrings:
+ "00:10:43"
+ "Mar  8 2025"
- "02:31:07"
- "Dec 14 2024"

```
