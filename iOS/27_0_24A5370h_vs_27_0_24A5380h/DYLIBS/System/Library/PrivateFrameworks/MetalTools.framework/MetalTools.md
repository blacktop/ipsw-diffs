## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`

```diff

-  __TEXT.__text: 0x145004
-  __TEXT.__objc_methlist: 0x1a674
-  __TEXT.__gcc_except_tab: 0x31c4
-  __TEXT.__cstring: 0x35230
-  __TEXT.__const: 0x590
+  __TEXT.__text: 0x146170
+  __TEXT.__objc_methlist: 0x1a71c
+  __TEXT.__gcc_except_tab: 0x32ec
+  __TEXT.__cstring: 0x35270
+  __TEXT.__const: 0x5a0
   __TEXT.__oslogstring: 0x28d1
-  __TEXT.__unwind_info: 0x5710
+  __TEXT.__unwind_info: 0x5770
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1bd8
+  __DATA_CONST.__const: 0x1c00
   __DATA_CONST.__objc_classlist: 0x7a8
   __DATA_CONST.__objc_protolist: 0x4f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x6a68
+  __DATA_CONST.__objc_selrefs: 0x6ac0
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x6a8
-  __DATA_CONST.__got: 0xb90
+  __DATA_CONST.__got: 0xbb8
   __AUTH_CONST.__const: 0x2b0
-  __AUTH_CONST.__cfstring: 0xf500
-  __AUTH_CONST.__objc_const: 0x48fb8
+  __AUTH_CONST.__cfstring: 0xf640
+  __AUTH_CONST.__objc_const: 0x490c8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__auth_got: 0x6d0
-  __AUTH.__objc_data: 0x1e0
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x1
-  __DATA.__objc_ivar: 0x10e0
+  __DATA.__objc_ivar: 0x10f8
   __DATA.__data: 0x3b70
   __DATA.__bss: 0xa0
-  __DATA_DIRTY.__objc_data: 0x4ab0
+  __DATA_DIRTY.__objc_data: 0x4c90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8172
-  Symbols:   25989
-  CStrings:  5628
+  Functions: 8190
+  Symbols:   26050
+  CStrings:  5650
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__thread_vars : content changed
~ __DATA.__data : content changed
Symbols:
+ -[MTL4ToolsComputeCommandEncoder flushCompressionMetadata]
+ -[MTLGPUDebugBufferErrorLog bufferGPUAddress]
+ -[MTLGPUDebugBufferErrorLog bufferIsResolved]
+ -[MTLGPUDebugBufferErrorLog bufferLabel]
+ -[MTLGPUDebugBufferErrorLog bufferLength]
+ -[MTLGPUDebugBufferErrorLog setBufferGPUAddress:]
+ -[MTLGPUDebugBufferErrorLog setBufferIsResolved:]
+ -[MTLGPUDebugBufferErrorLog setBufferLabel:]
+ -[MTLGPUDebugBufferErrorLog setBufferLength:]
+ -[MTLGPUDebugDevice resetBVHResidencyCursorForAccelerationStructure:]
+ -[MTLToolsCommandQueue internalResidencySets]
+ -[MTLToolsCommandQueue residencySets]
+ -[MTLToolsTexture compressionMetadata]
+ GCC_except_table102
+ GCC_except_table107
+ GCC_except_table111
+ GCC_except_table153
+ GCC_except_table237
+ GCC_except_table240
+ GCC_except_table246
+ GCC_except_table249
+ GCC_except_table256
+ GCC_except_table260
+ GCC_except_table263
+ OBJC_IVAR_$_MTLGPUDebugDevice.bvhResidencyCounterTable
+ _OBJC_IVAR_$_MTL4GPUDebugCommandBuffer._deallocated
+ _OBJC_IVAR_$_MTLGPUDebugBufferErrorLog._bufferGPUAddress
+ _OBJC_IVAR_$_MTLGPUDebugBufferErrorLog._bufferIsResolved
+ _OBJC_IVAR_$_MTLGPUDebugBufferErrorLog._bufferLabel
+ _OBJC_IVAR_$_MTLGPUDebugBufferErrorLog._bufferLength
+ __Z37validateMTL4ComputePipelineDescriptorP29MTL4ComputePipelineDescriptorP18_MTLMessageContext
+ __ZL29validateLibraryFunctionLookupP22MTL4FunctionDescriptorP8NSStringP18_MTLMessageContext
+ __ZL35validateMTL4StaticLinkingDescriptorP27MTL4StaticLinkingDescriptorP8NSStringP18_MTLMessageContext
+ __ZN18ResourceUsageTableD2Ev
+ __ZN28GPUDebugBufferDescriptorHeap19reportInfoForHandleEy
+ ____ZL35validateMTL4StaticLinkingDescriptorP27MTL4StaticLinkingDescriptorP8NSStringP18_MTLMessageContext_block_invoke
+ ___block_descriptor_128_e8_32o40o48o56o64o72o_e8_v16?0Q8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_48_e5_v8?0ls40l8
+ ___block_descriptor_48_e8_32o_e34_v32?0"NSString"8"NSArray"16^B24ls32l8
+ _objc_msgSend$bufferIsResolved
+ _objc_msgSend$compressionMetadata
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$flushCompressionMetadata
+ _objc_msgSend$internalResidencySets
+ _objc_msgSend$resetBVHResidencyCursorForAccelerationStructure:
+ _objc_msgSend$residencySets
+ _objc_msgSend$setBufferGPUAddress:
+ _objc_msgSend$setBufferIsResolved:
+ _objc_msgSend$setBufferLabel:
+ _objc_msgSend$setBufferLength:
- -[MTLToolsCommandQueue internalResidencySetsArray]
- GCC_except_table100
- GCC_except_table151
- GCC_except_table231
- GCC_except_table235
- GCC_except_table238
- GCC_except_table242
- GCC_except_table243
- GCC_except_table254
- GCC_except_table258
- GCC_except_table75
- GCC_except_table78
- GCC_except_table95
- ___block_descriptor_120_e8_32o40o48o56o64o72o_e8_v16?0Q8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_40_e5_v8?0ls32l8
- _objc_msgSend$internalResidencySetsArray
- _objc_msgSend$setWithArray:
- _objc_msgSend$setWithSet:
- _objc_msgSend$usedInternalResidencySets
CStrings:
+ "\n=================================================================\nInvalid Metal usage: %@\n================================================================="
+ "\n=================================================================\nInvalid Metal usage: %@\n=================================================================\n"
+ " 0"
+ "%@.functionDescriptors at index %lu"
+ "%@.groups['%@'] at index %lu"
+ "%@.privateFunctionDescriptors at index %lu"
+ "%@: function '%@' not found in library"
+ "Tensor data (offset %lu + size %lu = %lu) exceeds buffer length (%lu)."
+ "Tensor offset (%lu) must be < buffer length (%lu)."
+ "descriptor.computeFunctionDescriptor"
+ "descriptor.fragmentFunctionDescriptor"
+ "descriptor.fragmentStaticLinkingDescriptor"
+ "descriptor.meshFunctionDescriptor"
+ "descriptor.meshStaticLinkingDescriptor"
+ "descriptor.objectFunctionDescriptor"
+ "descriptor.objectStaticLinkingDescriptor"
+ "descriptor.staticLinkingDescriptor"
+ "descriptor.tileFunctionDescriptor"
+ "descriptor.vertexFunctionDescriptor"
+ "descriptor.vertexStaticLinkingDescriptor"
+ "v32@?0@\"NSString\"8@\"NSArray\"16^B24"
- "\n=================================================================\nInvalid metal usage: %@\n================================================================="
- "\n=================================================================\nInvalid metal usage: %@\n=================================================================\n"
- "Base: %llX End: %llX"
- "The command buffer (at index %lu) requires %lu Metal internal residency sets which exceeds the maximum (%lu)."
- "The command buffer (at index %lu) requires %lu residency sets which exceeds the maximum (%lu)."
- "The command buffer requires %lu Metal internal residency sets which exceeds the maximum (%lu)."
- "The command buffer requires %lu residency sets which exceeds the maximum (%lu)."
- "The command buffers (from index %lu to index %lu) require %lu Metal internal residency sets which exceeds the maximum (%lu)."
- "The command buffers (from index %lu to index %lu) require %lu residency sets which exceeds the maximum (%lu)."
- "invalid metal usage:\n%s\n"

```
