## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/Versions/A/MetalTools`

```diff

-  __TEXT.__text: 0x14e924
-  __TEXT.__objc_methlist: 0x1b22c
-  __TEXT.__gcc_except_tab: 0x32a8
-  __TEXT.__cstring: 0x361b5
+  __TEXT.__text: 0x14ef08
+  __TEXT.__objc_methlist: 0x1b29c
+  __TEXT.__gcc_except_tab: 0x32e8
+  __TEXT.__cstring: 0x361a2
   __TEXT.__const: 0x5b0
   __TEXT.__oslogstring: 0x28d1
-  __TEXT.__unwind_info: 0x5910
+  __TEXT.__unwind_info: 0x5938
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x508
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x6dc8
+  __DATA_CONST.__objc_selrefs: 0x6e08
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x6c0
-  __DATA_CONST.__got: 0xbb8
-  __AUTH_CONST.__const: 0x1120
-  __AUTH_CONST.__cfstring: 0xfa60
-  __AUTH_CONST.__objc_const: 0x4b290
+  __DATA_CONST.__got: 0xbe0
+  __AUTH_CONST.__const: 0x1150
+  __AUTH_CONST.__cfstring: 0xfb80
+  __AUTH_CONST.__objc_const: 0x4b350
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__auth_got: 0x650
-  __AUTH.__objc_data: 0x1e0
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x1
-  __DATA.__objc_ivar: 0x1114
+  __DATA.__objc_ivar: 0x1124
   __DATA.__data: 0x3c90
   __DATA.__bss: 0xa8
-  __DATA_DIRTY.__objc_data: 0x4c40
+  __DATA_DIRTY.__objc_data: 0x4e20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8392
-  Symbols:   17892
-  CStrings:  5734
+  Functions: 8406
+  Symbols:   17918
+  CStrings:  5753
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __DATA.__data : content changed
Symbols:
+ -[MTLGPUDebugBufferErrorLog bufferGPUAddress]
+ -[MTLGPUDebugBufferErrorLog bufferIsResolved]
+ -[MTLGPUDebugBufferErrorLog bufferLabel]
+ -[MTLGPUDebugBufferErrorLog bufferLength]
+ -[MTLGPUDebugBufferErrorLog setBufferGPUAddress:]
+ -[MTLGPUDebugBufferErrorLog setBufferIsResolved:]
+ -[MTLGPUDebugBufferErrorLog setBufferLabel:]
+ -[MTLGPUDebugBufferErrorLog setBufferLength:]
+ -[MTLToolsCommandQueue internalResidencySets]
+ -[MTLToolsCommandQueue residencySets]
+ GCC_except_table107
+ GCC_except_table110
+ GCC_except_table114
+ GCC_except_table255
+ GCC_except_table258
+ GCC_except_table265
+ GCC_except_table267
+ GCC_except_table274
+ GCC_except_table278
+ GCC_except_table281
+ OBJC_IVAR_$_MTLGPUDebugBufferErrorLog._bufferGPUAddress
+ OBJC_IVAR_$_MTLGPUDebugBufferErrorLog._bufferIsResolved
+ OBJC_IVAR_$_MTLGPUDebugBufferErrorLog._bufferLabel
+ OBJC_IVAR_$_MTLGPUDebugBufferErrorLog._bufferLength
+ __Z37validateMTL4ComputePipelineDescriptorP29MTL4ComputePipelineDescriptorP18_MTLMessageContext
+ __ZL29validateLibraryFunctionLookupP22MTL4FunctionDescriptorP8NSStringP18_MTLMessageContext
+ __ZL35validateMTL4StaticLinkingDescriptorP27MTL4StaticLinkingDescriptorP8NSStringP18_MTLMessageContext
+ __ZN28GPUDebugBufferDescriptorHeap19reportInfoForHandleEy
+ ____ZL35validateMTL4StaticLinkingDescriptorP27MTL4StaticLinkingDescriptorP8NSStringP18_MTLMessageContext_block_invoke
+ ___block_descriptor_48_e8_32o_e34_v32?0"NSString"8"NSArray"16^B24l
+ _objc_msgSend$bufferIsResolved
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$internalResidencySets
+ _objc_msgSend$residencySets
+ _objc_msgSend$setBufferGPUAddress:
+ _objc_msgSend$setBufferIsResolved:
+ _objc_msgSend$setBufferLabel:
+ _objc_msgSend$setBufferLength:
- -[MTLToolsCommandQueue internalResidencySetsArray]
- GCC_except_table162
- GCC_except_table254
- GCC_except_table257
- GCC_except_table261
- GCC_except_table266
- GCC_except_table273
- GCC_except_table277
- GCC_except_table280
- GCC_except_table66
- GCC_except_table95
- GCC_except_table99
- _objc_msgSend$internalResidencySetsArray
- _objc_msgSend$setWithArray:
- _objc_msgSend$setWithSet:
- _objc_msgSend$usedInternalResidencySets
CStrings:
+ "%@.functionDescriptors at index %lu"
+ "%@.groups['%@'] at index %lu"
+ "%@.privateFunctionDescriptors at index %lu"
+ "%@: function '%@' not found in library"
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
- "The command buffer (at index %lu) requires %lu Metal internal residency sets which exceeds the maximum (%lu)."
- "The command buffer (at index %lu) requires %lu residency sets which exceeds the maximum (%lu)."
- "The command buffer requires %lu Metal internal residency sets which exceeds the maximum (%lu)."
- "The command buffer requires %lu residency sets which exceeds the maximum (%lu)."
- "The command buffers (from index %lu to index %lu) require %lu Metal internal residency sets which exceeds the maximum (%lu)."
- "The command buffers (from index %lu to index %lu) require %lu residency sets which exceeds the maximum (%lu)."

```
