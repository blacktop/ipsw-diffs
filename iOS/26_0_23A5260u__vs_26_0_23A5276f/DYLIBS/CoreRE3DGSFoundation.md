## CoreRE3DGSFoundation

> `/System/Library/PrivateFrameworks/CoreRE3DGSFoundation.framework/CoreRE3DGSFoundation`

```diff

-1.2.2.0.0
-  __TEXT.__text: 0x6c870
+1.3.0.0.0
+  __TEXT.__text: 0x6dd9c
   __TEXT.__auth_stubs: 0x1030
   __TEXT.__objc_methlist: 0x8fc
-  __TEXT.__gcc_except_tab: 0x6d68
-  __TEXT.__const: 0x2ea9
-  __TEXT.__cstring: 0x2763
+  __TEXT.__gcc_except_tab: 0x6e8c
+  __TEXT.__const: 0x2ee2
+  __TEXT.__cstring: 0x2820
   __TEXT.__oslogstring: 0xcf9
-  __TEXT.__unwind_info: 0x1c68
+  __TEXT.__unwind_info: 0x1cc0
   __TEXT.__objc_classname: 0x9a
-  __TEXT.__objc_methname: 0x1fec
+  __TEXT.__objc_methname: 0x1efc
   __TEXT.__objc_methtype: 0x16c8
-  __TEXT.__objc_stubs: 0x1680
-  __DATA_CONST.__got: 0x278
+  __TEXT.__objc_stubs: 0x15c0
+  __DATA_CONST.__got: 0x248
   __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa28
+  __DATA_CONST.__objc_selrefs: 0x9f8
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x830
   __AUTH_CONST.__const: 0x1898
-  __AUTH_CONST.__cfstring: 0x640
+  __AUTH_CONST.__cfstring: 0x600
   __AUTH_CONST.__objc_const: 0xb40
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x2d0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B5F54A78-8353-36EC-9083-BDAFC80D9321
-  Functions: 1168
-  Symbols:   3793
-  CStrings:  998
+  UUID: E7AFF6B5-DFF9-35CE-8AFC-F08E26ED68B3
+  Functions: 1176
+  Symbols:   3795
+  CStrings:  996
 
Symbols:
+ __ZN9apple3dgs11RadixSorter11ClearBufferEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU19objcproto9MTLBuffer11objc_objectjj
+ __ZN9apple3dgs11RadixSorter11InitIndicesEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU19objcproto9MTLBuffer11objc_objectj
+ __ZN9apple3dgs11RadixSorter16ComputeHistogramEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU19objcproto9MTLBuffer11objc_objectS4_jj
+ __ZN9apple3dgs11RadixSorter22CheckInternalDataAllocEj
+ __ZN9apple3dgs11RadixSorter4SortEPU27objcproto16MTLCommandBuffer11objc_objectPU19objcproto9MTLBuffer11objc_objectS4_j
+ __ZN9apple3dgs11RadixSorter7ReorderEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU19objcproto9MTLBuffer11objc_objectS4_S4_S4_S4_jj
+ __ZN9apple3dgs11RadixSorter9PrefixSumEPU35objcproto24MTLComputeCommandEncoder11objc_objectPU19objcproto9MTLBuffer11objc_objectS4_S4_S4_j
+ __ZN9apple3dgs11RadixSorterC1EPU19objcproto9MTLDevice11objc_objectjbb
+ __ZN9apple3dgs11RadixSorterC2EPU19objcproto9MTLDevice11objc_objectjbb
+ __ZN9apple3dgs11RadixSorterD1Ev
+ __ZN9apple3dgs13MinAreaFilterER12MetalContextPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_i
+ __ZN9apple3dgs23ComputePrimitiveIndicesER12MetalContextPU27objcproto16MTLCommandBuffer11objc_objectPU19objcproto9MTLBuffer11objc_objectS5_j
+ __ZN9apple3dgs23ComputeRefinementWeightER12MetalContextPU27objcproto16MTLCommandBuffer11objc_objectPU21objcproto10MTLTexture11objc_objectS5_S5_RKN4simd8float3x3E
+ __ZN9apple3dgs9BoxFilterER12MetalContextPU35objcproto24MTLComputeCommandEncoder11objc_objectPU21objcproto10MTLTexture11objc_objectS5_i
+ _objc_msgSend$dispatchThreadgroups:threadsPerThreadgroup:
+ _objc_msgSend$newBufferWithBytesNoCopy:length:options:deallocator:
- _OBJC_CLASS_$_MPSCommandBuffer
- _OBJC_CLASS_$_MPSGraph
- _OBJC_CLASS_$_MPSGraphTensorData
- _OBJC_CLASS_$_MPSImageAreaMin
- _OBJC_CLASS_$_MPSImageBox
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_CLASS_$_NSNumber
- __ZN9apple3dgs23ComputePrimitiveIndicesER12MetalContextPU27objcproto16MTLCommandBuffer11objc_objectPU19objcproto9MTLBuffer11objc_objectS5_S5_j
- __ZN9apple3dgs23ComputeRefinementWeightER12MetalContextPU27objcproto16MTLCommandBuffer11objc_objectPU21objcproto10MTLTexture11objc_objectS5_RKN4simd8float3x3E
- __ZN9apple3dgs9MPSSorterC1E11MPSDataTypeb
- __ZN9apple3dgs9MPSSorterC2E11MPSDataTypeb
- __ZN9apple3dgs9MPSSorterD1Ev
- __ZNK9apple3dgs9MPSSorter7ArgSortEPU27objcproto16MTLCommandBuffer11objc_objectPU19objcproto9MTLBuffer11objc_objectS4_j
- _objc_msgSend$argSortWithTensor:axis:descending:name:
- _objc_msgSend$encodeToCommandBuffer:feeds:targetOperations:resultsDictionary:executionDescriptor:
- _objc_msgSend$encodeToCommandBuffer:sourceTexture:destinationTexture:
- _objc_msgSend$initWithCommandBuffer:
- _objc_msgSend$initWithDevice:kernelWidth:kernelHeight:
- _objc_msgSend$initWithMTLBuffer:shape:dataType:
- _objc_msgSend$numberWithUnsignedInt:
- _objc_msgSend$placeholderWithShape:dataType:name:
CStrings:
+ "ClearBuffer"
+ "InitIndices"
+ "PrefixExclusiveSumKernel_uint_false"
+ "PrefixExclusiveSumKernel_uint_true"
+ "RadixSortMakeHistogramKernel%d_uint"
+ "RadixSortReorderKernel%d_uint"
+ "ReduceSumKernel_uint"
+ "SeparableBoxFilter"
+ "SeparableMinFilter"
+ "[A3DGSR /MultiLayerRenderer.mm:423] Number of layers should be larger than 0"
+ "[A3DGSR /MultiLayerRenderer.mm:429] Number of layers should be divisible by number of passes."
+ "[A3DGSR /MultiLayerRenderer.mm:436] Image size should be larger than 0"
+ "[A3DGSR /MultiLayerRenderer.mm:464] Provided option's near far plane are invalid: near %.2f, far %.2f"
+ "[A3DGSR /SortWorker.mm:975] MPI (%lux%lu) should have the same aspect ratio as GT image (%lux%lu)."
+ "dispatchThreadgroups:threadsPerThreadgroup:"
+ "newBufferWithBytesNoCopy:length:options:deallocator:"
- "[A3DGSR /MultiLayerRenderer.mm:415] Number of layers should be larger than 0"
- "[A3DGSR /MultiLayerRenderer.mm:421] Number of layers should be divisible by number of passes."
- "[A3DGSR /MultiLayerRenderer.mm:428] Image size should be larger than 0"
- "[A3DGSR /MultiLayerRenderer.mm:456] Provided option's near far plane are invalid: near %.2f, far %.2f"
- "[A3DGSR /SortWorker.mm:940] MPI (%lux%lu) should have the same aspect ratio as GT image (%lux%lu)."
- "argSortWithTensor:axis:descending:name:"
- "encodeToCommandBuffer:feeds:targetOperations:resultsDictionary:executionDescriptor:"
- "encodeToCommandBuffer:sourceTexture:destinationTexture:"
- "gather_indices"
- "i"
- "initWithCommandBuffer:"
- "initWithDevice:kernelWidth:kernelHeight:"
- "initWithMTLBuffer:shape:dataType:"
- "keys_unsorted"
- "numberWithUnsignedInt:"
- "placeholderWithShape:dataType:name:"

```
