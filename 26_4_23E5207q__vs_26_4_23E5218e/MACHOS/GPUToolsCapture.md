## GPUToolsCapture

> `/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture`

```diff

-314.9.0.0.0
-  __TEXT.__text: 0x2638ac
+314.10.0.0.0
+  __TEXT.__text: 0x268784
   __TEXT.__auth_stubs: 0x1780
-  __TEXT.__objc_stubs: 0x16dc0
+  __TEXT.__objc_stubs: 0x17120
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x128a4
-  __TEXT.__const: 0x46d0
-  __TEXT.__cstring: 0x27647
-  __TEXT.__gcc_except_tab: 0x8f4
-  __TEXT.__objc_methname: 0x1a372
-  __TEXT.__objc_classname: 0x1570
-  __TEXT.__objc_methtype: 0xa900
-  __TEXT.__oslogstring: 0x11c5
+  __TEXT.__objc_methlist: 0x12adc
+  __TEXT.__const: 0x46e0
+  __TEXT.__cstring: 0x27cc1
+  __TEXT.__gcc_except_tab: 0xd38
+  __TEXT.__objc_methname: 0x1a81e
+  __TEXT.__objc_classname: 0x15f1
+  __TEXT.__objc_methtype: 0xab28
+  __TEXT.__oslogstring: 0x16fa
   __TEXT.__ustring: 0x20a
-  __TEXT.__unwind_info: 0x4300
+  __TEXT.__unwind_info: 0x43d8
   __DATA_CONST.__auth_got: 0xbd8
   __DATA_CONST.__got: 0x7f8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1d98
-  __DATA_CONST.__cfstring: 0x3fe0
-  __DATA_CONST.__objc_classlist: 0x318
+  __DATA_CONST.__const: 0x1dd8
+  __DATA_CONST.__cfstring: 0x4360
+  __DATA_CONST.__objc_classlist: 0x340
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x428
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x308
+  __DATA_CONST.__objc_superrefs: 0x320
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x1a030
-  __DATA.__objc_selrefs: 0x6be0
-  __DATA.__objc_ivar: 0xadc
-  __DATA.__objc_data: 0x1ef0
-  __DATA.__data: 0x3470
+  __DATA.__objc_const: 0x1a660
+  __DATA.__objc_selrefs: 0x6cb8
+  __DATA.__objc_ivar: 0xb30
+  __DATA.__objc_data: 0x2080
+  __DATA.__data: 0x3488
   __DATA.__thread_vars: 0x48
   __DATA.__thread_bss: 0x1018
   __DATA.__bss: 0x558

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E379BE03-1AE9-30FE-AA30-E41B15C92635
-  Functions: 7878
-  Symbols:   46790
-  CStrings:  9261
+  UUID: 142F10CA-D09D-35F5-AC4A-9997167E7BC7
+  Functions: 7925
+  Symbols:   47148
+  CStrings:  9412
 
Symbols:
+ +[SparseTexturePageTable computeRequiredBufferByteCountWithDevice:descriptor:]
+ +[SparseTexturePageTable sliceCountForDescriptor:]
+ -[CaptureMTLDevice sparsePageTables]
+ -[GTMTLBufferResource .cxx_destruct]
+ -[GTMTLBufferResource inUse]
+ -[GTMTLBufferResource object]
+ -[GTMTLBufferResource setInUse:]
+ -[GTMTLBufferResource setObject:]
+ -[GTMTLCaptureResourcePool .cxx_destruct]
+ -[GTMTLCaptureResourcePool acquireBufferWithByteCount:]
+ -[GTMTLCaptureResourcePool acquireCommandAllocator]
+ -[GTMTLCaptureResourcePool initWithDevice:]
+ -[GTMTLCaptureResourcePool releaseBuffer:]
+ -[GTMTLCaptureResourcePool releaseCommandAllocator:]
+ -[GTMTLCaptureSparsePageTables .cxx_destruct]
+ -[GTMTLCaptureSparsePageTables copyTextureMappings:source:destination:operations:count:]
+ -[GTMTLCaptureSparsePageTables dumpTextureMappingsWithCallback:texture:userdata:]
+ -[GTMTLCaptureSparsePageTables heaps]
+ -[GTMTLCaptureSparsePageTables initWithDevice:]
+ -[GTMTLCaptureSparsePageTables purge]
+ -[GTMTLCaptureSparsePageTables registerTexture:descriptor:]
+ -[GTMTLCaptureSparsePageTables unregisterTexture:]
+ -[GTMTLCaptureSparsePageTables updateTextureMappings:texture:heap:operations:count:]
+ -[GTMTLCommandAllocatorResource .cxx_destruct]
+ -[GTMTLCommandAllocatorResource inUse]
+ -[GTMTLCommandAllocatorResource object]
+ -[GTMTLCommandAllocatorResource setInUse:]
+ -[GTMTLCommandAllocatorResource setObject:]
+ -[SparseTexturePageTable .cxx_destruct]
+ -[SparseTexturePageTable arraySizeWithCopyOps:fromTexture:apiOpCount:]
+ -[SparseTexturePageTable arraySizeWithUpdateOps:apiOpCount:]
+ -[SparseTexturePageTable buffer]
+ -[SparseTexturePageTable decomposePageIndex:outRegion:outLevel:outSlice:]
+ -[SparseTexturePageTable descriptor]
+ -[SparseTexturePageTable dumpPageTableWithLabel:waitOnQueue:timeoutMS:]
+ -[SparseTexturePageTable fillArrayWithCopyOps:fromTexture:apiOpCount:gpuOps:]
+ -[SparseTexturePageTable fillArrayWithUpdateOps:apiOpCount:gpuOps:]
+ -[SparseTexturePageTable initWithBuffer:descriptor:]
+ -[SparseTexturePageTable setBuffer:]
+ -[SparseTexturePageTable setDescriptor:]
+ -[SparseTexturePageTable setTextureStream:]
+ -[SparseTexturePageTable textureStream]
+ /Library/Caches/com.apple.xbs/EC5DAD33-C7A6-479B-B9F7-2785559D39E5/TemporaryDirectory.7DxQry/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/DerivedSources/
+ /Library/Caches/com.apple.xbs/EC5DAD33-C7A6-479B-B9F7-2785559D39E5/TemporaryDirectory.7DxQry/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/Objects-normal/arm64e/GPUToolsCapture_lto.o
+ GCC_except_table1551
+ GCC_except_table1576
+ GCC_except_table1681
+ GCC_except_table1682
+ GCC_except_table1686
+ GCC_except_table1687
+ GCC_except_table1688
+ GCC_except_table1689
+ GCC_except_table1690
+ GCC_except_table1898
+ GCC_except_table1899
+ GCC_except_table1901
+ GCC_except_table1903
+ GCC_except_table1911
+ GCC_except_table2055
+ GCC_except_table2091
+ GCC_except_table2905
+ GCC_except_table2913
+ GCC_except_table3050
+ GCC_except_table3201
+ GCC_except_table3208
+ GCC_except_table3217
+ GCC_except_table3315
+ GCC_except_table4033
+ GCC_except_table4205
+ GCC_except_table4206
+ GCC_except_table4207
+ GCC_except_table4209
+ GCC_except_table4211
+ GCC_except_table4212
+ GCC_except_table4213
+ GCC_except_table4379
+ GCC_except_table4380
+ GCC_except_table4381
+ GCC_except_table4382
+ GTAccelerationStructureDescriptorDownloader_processCopy.7920
+ GTAccelerationStructureDescriptorDownloader_processRefit.7921
+ GetStream.20270
+ OBJC_IVAR_$_CaptureMTLDevice._sparsePageTables
+ OBJC_IVAR_$_GTMTLBufferResource._inUse
+ OBJC_IVAR_$_GTMTLBufferResource._object
+ OBJC_IVAR_$_GTMTLCaptureResourcePool._buffers
+ OBJC_IVAR_$_GTMTLCaptureResourcePool._commandAllocators
+ OBJC_IVAR_$_GTMTLCaptureResourcePool._device
+ OBJC_IVAR_$_GTMTLCaptureSparsePageTables._argumentTable
+ OBJC_IVAR_$_GTMTLCaptureSparsePageTables._commandBuffer
+ OBJC_IVAR_$_GTMTLCaptureSparsePageTables._copyTextureMappingsPipeline
+ OBJC_IVAR_$_GTMTLCaptureSparsePageTables._deallocatedTextures
+ OBJC_IVAR_$_GTMTLCaptureSparsePageTables._device
+ OBJC_IVAR_$_GTMTLCaptureSparsePageTables._heaps
+ OBJC_IVAR_$_GTMTLCaptureSparsePageTables._residencySet
+ OBJC_IVAR_$_GTMTLCaptureSparsePageTables._resourcePool
+ OBJC_IVAR_$_GTMTLCaptureSparsePageTables._textureTables
+ OBJC_IVAR_$_GTMTLCaptureSparsePageTables._updateTextureMappingsPipeline
+ OBJC_IVAR_$_GTMTLCommandAllocatorResource._inUse
+ OBJC_IVAR_$_GTMTLCommandAllocatorResource._object
+ OBJC_IVAR_$_SparseTexturePageTable._buffer
+ OBJC_IVAR_$_SparseTexturePageTable._descriptor
+ OBJC_IVAR_$_SparseTexturePageTable._textureStream
+ RetainObjectForDescriptorDownloader.9572
+ StoreMTLCompileOptionsUsingEncode.16696
+ _GTMTLCaptureSparsePageTables_dumpTextureMappings
+ _GTMTLCaptureSparsePageTables_getPlacementSparseHeaps
+ _OBJC_CLASS_$_GTMTLBufferResource
+ _OBJC_CLASS_$_GTMTLCaptureResourcePool
+ _OBJC_CLASS_$_GTMTLCaptureSparsePageTables
+ _OBJC_CLASS_$_GTMTLCommandAllocatorResource
+ _OBJC_CLASS_$_SparseTexturePageTable
+ _OBJC_METACLASS_$_GTMTLBufferResource
+ _OBJC_METACLASS_$_GTMTLCaptureResourcePool
+ _OBJC_METACLASS_$_GTMTLCaptureSparsePageTables
+ _OBJC_METACLASS_$_GTMTLCommandAllocatorResource
+ _OBJC_METACLASS_$_SparseTexturePageTable
+ __Block_byref_object_copy_.11692
+ __Block_byref_object_copy_.4006
+ __Block_byref_object_copy_.4509
+ __Block_byref_object_copy_.7173
+ __Block_byref_object_copy_.8386
+ __Block_byref_object_dispose_.11693
+ __Block_byref_object_dispose_.4007
+ __Block_byref_object_dispose_.4510
+ __Block_byref_object_dispose_.7174
+ __Block_byref_object_dispose_.8387
+ __OBJC_$_CLASS_METHODS_SparseTexturePageTable
+ __OBJC_$_INSTANCE_METHODS_GTMTLBufferResource
+ __OBJC_$_INSTANCE_METHODS_GTMTLCaptureResourcePool
+ __OBJC_$_INSTANCE_METHODS_GTMTLCaptureSparsePageTables
+ __OBJC_$_INSTANCE_METHODS_GTMTLCommandAllocatorResource
+ __OBJC_$_INSTANCE_METHODS_SparseTexturePageTable
+ __OBJC_$_INSTANCE_VARIABLES_GTMTLBufferResource
+ __OBJC_$_INSTANCE_VARIABLES_GTMTLCaptureResourcePool
+ __OBJC_$_INSTANCE_VARIABLES_GTMTLCaptureSparsePageTables
+ __OBJC_$_INSTANCE_VARIABLES_GTMTLCommandAllocatorResource
+ __OBJC_$_INSTANCE_VARIABLES_SparseTexturePageTable
+ __OBJC_$_PROP_LIST_GTMTLBufferResource
+ __OBJC_$_PROP_LIST_GTMTLCommandAllocatorResource
+ __OBJC_$_PROP_LIST_SparseTexturePageTable
+ __OBJC_CLASS_RO_$_GTMTLBufferResource
+ __OBJC_CLASS_RO_$_GTMTLCaptureResourcePool
+ __OBJC_CLASS_RO_$_GTMTLCaptureSparsePageTables
+ __OBJC_CLASS_RO_$_GTMTLCommandAllocatorResource
+ __OBJC_CLASS_RO_$_SparseTexturePageTable
+ __OBJC_METACLASS_RO_$_GTMTLBufferResource
+ __OBJC_METACLASS_RO_$_GTMTLCaptureResourcePool
+ __OBJC_METACLASS_RO_$_GTMTLCaptureSparsePageTables
+ __OBJC_METACLASS_RO_$_GTMTLCommandAllocatorResource
+ __OBJC_METACLASS_RO_$_SparseTexturePageTable
+ ___84-[GTMTLCaptureSparsePageTables updateTextureMappings:texture:heap:operations:count:]_block_invoke
+ ___88-[GTMTLCaptureSparsePageTables copyTextureMappings:source:destination:operations:count:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56s_e30_v16?0"<MTL4CommitFeedback>"8ls32l8s40l8s48l8s56l8
+ __block_descriptor_tmp.15389
+ __block_literal_global.10428
+ __block_literal_global.10924
+ __block_literal_global.11696
+ __block_literal_global.12138
+ __block_literal_global.15250
+ __block_literal_global.15488
+ __block_literal_global.15558
+ __block_literal_global.15572
+ __block_literal_global.1698
+ __block_literal_global.20655
+ __block_literal_global.275
+ __block_literal_global.3054
+ __block_literal_global.4336
+ __block_literal_global.4521
+ __block_literal_global.8106
+ __block_literal_global.8542
+ __block_literal_global.9549
+ _objc_msgSend$acquireBufferWithByteCount:
+ _objc_msgSend$acquireCommandAllocator
+ _objc_msgSend$arraySizeWithCopyOps:fromTexture:apiOpCount:
+ _objc_msgSend$arraySizeWithUpdateOps:apiOpCount:
+ _objc_msgSend$computeRequiredBufferByteCountWithDevice:descriptor:
+ _objc_msgSend$copyTextureMappings:source:destination:operations:count:
+ _objc_msgSend$decomposePageIndex:outRegion:outLevel:outSlice:
+ _objc_msgSend$descriptor
+ _objc_msgSend$dumpTextureMappingsWithCallback:texture:userdata:
+ _objc_msgSend$fillArrayWithCopyOps:fromTexture:apiOpCount:gpuOps:
+ _objc_msgSend$fillArrayWithUpdateOps:apiOpCount:gpuOps:
+ _objc_msgSend$heaps
+ _objc_msgSend$inUse
+ _objc_msgSend$initWithBuffer:descriptor:
+ _objc_msgSend$object
+ _objc_msgSend$purge
+ _objc_msgSend$registerTexture:descriptor:
+ _objc_msgSend$releaseBuffer:
+ _objc_msgSend$releaseCommandAllocator:
+ _objc_msgSend$setInUse:
+ _objc_msgSend$setObject:
+ _objc_msgSend$setTextureStream:
+ _objc_msgSend$sliceCountForDescriptor:
+ _objc_msgSend$sparsePageTables
+ _objc_msgSend$textureStream
+ _objc_msgSend$unregisterTexture:
+ _objc_msgSend$updateTextureMappings:texture:heap:operations:count:
+ _sparseMappingsCallback
+ name_array.16641
+ newHeapWithDescriptor:.onceToken.273
+ s_accelerationStructureDescriptorDownloaderPipelinesToken.7896
+ s_downloaderPipelines.0.7902
+ s_downloaderPipelines.1.7903
+ s_downloaderPipelines.2.7904
+ s_downloaderPipelines.3.7905
+ s_downloaderPipelines.4.7906
+ waitUntilSignaledValue:timeoutMS:.onceToken.13702
- /Library/Caches/com.apple.xbs/EB5EB1E5-3E70-4CA5-90D9-62F5C0E2D199/TemporaryDirectory.Kab9YK/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/DerivedSources/
- /Library/Caches/com.apple.xbs/EB5EB1E5-3E70-4CA5-90D9-62F5C0E2D199/TemporaryDirectory.Kab9YK/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/Objects-normal/arm64e/GPUToolsCapture_lto.o
- GCC_except_table1532
- GCC_except_table1557
- GCC_except_table1662
- GCC_except_table1663
- GCC_except_table1667
- GCC_except_table1668
- GCC_except_table1669
- GCC_except_table1670
- GCC_except_table1671
- GCC_except_table1879
- GCC_except_table1880
- GCC_except_table1882
- GCC_except_table1884
- GCC_except_table1892
- GCC_except_table2036
- GCC_except_table2072
- GCC_except_table2886
- GCC_except_table2894
- GCC_except_table3031
- GCC_except_table3182
- GCC_except_table3189
- GCC_except_table3198
- GCC_except_table3296
- GCC_except_table4014
- GTAccelerationStructureDescriptorDownloader_processCopy.7906
- GTAccelerationStructureDescriptorDownloader_processRefit.7907
- GetStream.20086
- RetainObjectForDescriptorDownloader.9554
- StoreMTLCompileOptionsUsingEncode.16515
- __Block_byref_object_copy_.11679
- __Block_byref_object_copy_.3994
- __Block_byref_object_copy_.4493
- __Block_byref_object_copy_.7158
- __Block_byref_object_copy_.8370
- __Block_byref_object_dispose_.11680
- __Block_byref_object_dispose_.3995
- __Block_byref_object_dispose_.4494
- __Block_byref_object_dispose_.7159
- __Block_byref_object_dispose_.8371
- __block_descriptor_tmp.15205
- __block_literal_global.10413
- __block_literal_global.10911
- __block_literal_global.11683
- __block_literal_global.12124
- __block_literal_global.15066
- __block_literal_global.15304
- __block_literal_global.15373
- __block_literal_global.15387
- __block_literal_global.1699
- __block_literal_global.20471
- __block_literal_global.274
- __block_literal_global.3046
- __block_literal_global.4323
- __block_literal_global.4505
- __block_literal_global.8092
- __block_literal_global.8527
- __block_literal_global.9531
- name_array.16460
- newHeapWithDescriptor:.onceToken.272
- s_accelerationStructureDescriptorDownloaderPipelinesToken.7882
- s_downloaderPipelines.0.7888
- s_downloaderPipelines.1.7889
- s_downloaderPipelines.2.7890
- s_downloaderPipelines.3.7891
- s_downloaderPipelines.4.7892
- waitUntilSignaledValue:timeoutMS:.onceToken.13566
CStrings:
+ "%-8llu %-8llu %-8llu (%llu,%llu)          0x%-14llx 0x%-14llx"
+ "%-8s %-8s %-8s %-16s %-16s %-16s"
+ "------------------------------------------------------------------------"
+ "/AppleInternal/Library/BuildRoots/4~CJInugDz3Hivhcv6JwAyROPneKktez0TvG7LEXg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJInugDz3Hivhcv6JwAyROPneKktez0TvG7LEXg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "@\"<MTL4CommandBuffer>\""
+ "@\"GTMTLCaptureResourcePool\""
+ "@\"GTMTLCaptureSparsePageTables\""
+ "@\"MTLTextureDescriptor\""
+ "B40@0:8^?16Q24^v32"
+ "DownloadLegacySparseTextureMappingBuffer[slice = %lu, level = %lu]"
+ "Failed to allocate sparse page table buffer of size %llu"
+ "Failed to create shadow state object for sparse page table."
+ "GTMTLBufferResource"
+ "GTMTLCaptureResourcePool"
+ "GTMTLCaptureSparsePageTables"
+ "GTMTLCaptureSparsePageTables_copyMappings"
+ "GTMTLCaptureSparsePageTables_updateMappings"
+ "GTMTLCommandAllocatorResource"
+ "HeapID"
+ "HeapOffset"
+ "Level"
+ "Malformed operation: depth of region must be 1 for non-3D texture."
+ "Mip Levels: %llu"
+ "Page"
+ "Page table buffer is nil"
+ "Q32@0:8@16@24"
+ "Q32@0:8r^{?=Q{?={?=QQQ}{?=QQQ}}QQQ}16Q24"
+ "Q40@0:8r^{?=Q{?={?=QQQ}{?=QQQ}}QQQ}16Q24^{SparsePageTableUpdateOpGPU=QQQ}32"
+ "Q40@0:8r^{?={?={?=QQQ}{?=QQQ}}QQ{?=QQQ}QQ}16@24Q32"
+ "Q48@0:8r^{?={?={?=QQQ}{?=QQQ}}QQ{?=QQQ}QQ}16@24Q32^{SparsePageTableCopyOpGPU=QQ}40"
+ "Slice"
+ "Sparse Texture Page Table"
+ "Sparse Texture Page Table: %@"
+ "SparseResources"
+ "SparseTexturePageTable"
+ "T@\"<MTL4CommandAllocator>\",&,N,V_object"
+ "T@\"<MTLBuffer>\",&,N,V_object"
+ "T@\"GTMTLCaptureSparsePageTables\",R,N,V_sparsePageTables"
+ "T@\"MTLTextureDescriptor\",C,N,V_descriptor"
+ "TB,N,V_inUse"
+ "TQ,N,V_textureStream"
+ "Texture Size: %llux%llux%llu"
+ "Tile(x,y)"
+ "Total Pages: %llu"
+ "_argumentTable"
+ "_commandAllocators"
+ "_commandBuffer"
+ "_copyTextureMappingsPipeline"
+ "_deallocatedTextures"
+ "_heaps"
+ "_inUse"
+ "_object"
+ "_residencySet"
+ "_resourcePool"
+ "_sparsePageTables"
+ "_textureStream"
+ "_textureTables"
+ "_updateTextureMappingsPipeline"
+ "acquireBufferWithByteCount:"
+ "acquireCommandAllocator"
+ "arraySizeWithCopyOps:fromTexture:apiOpCount:"
+ "arraySizeWithUpdateOps:apiOpCount:"
+ "com.apple.gputools.GTResourceDownloader.DownloadLegacySparseTextureMappingBuffer[name=%lu, ref=%llu]"
+ "com.apple.gputools.SparsePageTable"
+ "com.apple.gputools.SparsePageTableCopyOps"
+ "com.apple.gputools.SparsePageTableKernelArgs"
+ "com.apple.gputools.SparsePageTableUpdateOps"
+ "computeRequiredBufferByteCountWithDevice:descriptor:"
+ "copyTextureMappings:source:destination:operations:count:"
+ "decomposePageIndex:outRegion:outLevel:outSlice:"
+ "dumpPageTableWithLabel:waitOnQueue:timeoutMS:"
+ "dumpTextureMappingsWithCallback:texture:userdata:"
+ "fail: GTMTLCaptureSparsePageTables - Failed creating the argument table: %s"
+ "fail: GTMTLCaptureSparsePageTables - Failed creating the residency set: %s"
+ "fail: GTMTLCaptureSparsePageTables - Failed to create MTLLibrary for sparse page tables: %s"
+ "fail: GTMTLCaptureSparsePageTables - Failed to get MSL shader for sparse page tables: copyMappings"
+ "fail: GTMTLCaptureSparsePageTables - Failed to get MSL shader for sparse page tables: updateMappings"
+ "fail: GTMTLCaptureSparsePageTables - Unable to create Metal 4 pipeline for sparse page tables (copyMappings): %s"
+ "fail: GTMTLCaptureSparsePageTables - Unable to create Metal 4 pipeline for sparse page tables (updateMappings): %s"
+ "fail: Sparse textures: unexpected texture dimensions."
+ "fillArrayWithCopyOps:fromTexture:apiOpCount:gpuOps:"
+ "fillArrayWithUpdateOps:apiOpCount:gpuOps:"
+ "inUse"
+ "initWithBuffer:descriptor:"
+ "object"
+ "purge"
+ "registerTexture:descriptor:"
+ "releaseBuffer:"
+ "releaseCommandAllocator:"
+ "setInUse:"
+ "setObject:"
+ "setTextureStream:"
+ "sliceCountForDescriptor:"
+ "sparsePageTables"
+ "textureStream"
+ "unregisterTexture:"
+ "updateTextureMappings:texture:heap:operations:count:"
+ "v32@0:8Q16@24"
+ "v44@0:8i16^{?={?=QQQ}{?=QQQ}}20^Q28^Q36"
+ "v56@0:8@16Q24Q32r^{?=Q{?={?=QQQ}{?=QQQ}}QQQ}40Q48"
+ "v56@0:8@16Q24Q32r^{?={?={?=QQQ}{?=QQQ}}QQ{?=QQQ}QQ}40Q48"
+ "warning: No sparse page table buffer found for texture %llu"
+ "warning: Sparse page table mapping not initialized"
- "/AppleInternal/Library/BuildRoots/4~CH9TugDK7NeNFXlDCJk5oGYOjZm0YEVbHWxHTo4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CH9TugDK7NeNFXlDCJk5oGYOjZm0YEVbHWxHTo4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "DownloadSparseTextureMappingBuffer[slice = %lu, level = %lu]"
- "com.apple.gputools.GTResourceDownloader.DownloadSparseTextureMappingBuffer[name=%lu, ref=%llu]"

```
