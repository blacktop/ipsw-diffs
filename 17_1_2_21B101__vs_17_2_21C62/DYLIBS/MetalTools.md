## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`

```diff

-341.29.1.0.0
-  __TEXT.__text: 0xc93cc
+341.35.0.0.0
+  __TEXT.__text: 0xc9a90
   __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0xc198
+  __TEXT.__objc_methlist: 0xc200
   __TEXT.__cstring: 0x238ca
-  __TEXT.__gcc_except_tab: 0x1400
+  __TEXT.__gcc_except_tab: 0x140c
   __TEXT.__const: 0x279
   __TEXT.__oslogstring: 0x271d
-  __TEXT.__unwind_info: 0x345c
+  __TEXT.__unwind_info: 0x348c
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_classname: 0x176a
-  __TEXT.__objc_methname: 0x16a82
-  __TEXT.__objc_methtype: 0x151f0
-  __TEXT.__objc_stubs: 0x11620
+  __TEXT.__objc_methname: 0x16b32
+  __TEXT.__objc_methtype: 0x15235
+  __TEXT.__objc_stubs: 0x11680
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__const: 0x15c8
   __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x355c0
-  __DATA_CONST.__objc_selrefs: 0x4a70
+  __DATA_CONST.__objc_const: 0x356b0
+  __DATA_CONST.__objc_selrefs: 0x4a88
   __AUTH_CONST.__cfstring: 0xa940
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__const: 0x20

   __DATA.__objc_protorefs: 0x78
   __DATA.__objc_classrefs: 0x688
   __DATA.__objc_superrefs: 0x3e0
-  __DATA.__objc_ivar: 0x95c
+  __DATA.__objc_ivar: 0x964
   __DATA.__data: 0x2288
   __DATA.__thread_vars: 0x18
   __DATA.__thread_bss: 0x1

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9964138B-1236-344D-9A39-A7CB0EB4687E
-  Functions: 4792
-  Symbols:   14967
-  CStrings:  8151
+  UUID: 46953174-01B7-37B1-A0B0-C6404691DD6E
+  Functions: 4805
+  Symbols:   14999
+  CStrings:  8158
 
Symbols:
+ -[MTLCountersDevice areWritableHeapsEnabled]
+ -[MTLCountersDevice setWritableHeapsEnabled:]
+ -[MTLDebugDevice areWritableHeapsEnabled]
+ -[MTLDebugDevice setWritableHeapsEnabled:]
+ -[MTLGPUDebugDevice areWritableHeapsEnabled]
+ -[MTLGPUDebugDevice setWritableHeapsEnabled:]
+ -[MTLGPUDebugHeap enumerateAccelerationStructureIndices:]
+ -[MTLToolsDevice areWritableHeapsEnabled]
+ -[MTLToolsDevice setWritableHeapsEnabled:]
+ GCC_except_table177
+ GCC_except_table182
+ _OBJC_IVAR_$_MTLGPUDebugCommandBuffer._deviceOptions
+ _OBJC_IVAR_$_MTLGPUDebugCommandQueue._deviceOptions
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3__block_invoke_10
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3__block_invoke_11
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3__block_invoke_12
+ ____ZN14HeapUsageTable5applyER16BufferUsageTableS1_S1_S1_R17TextureUsageTableS3_S3_S3__block_invoke_9
+ ___block_descriptor_48_e12_v20?0^I8I16l
+ _objc_msgSend$areWritableHeapsEnabled
+ _objc_msgSend$enumerateAccelerationStructureIndices:
+ _objc_msgSend$setWritableHeapsEnabled:
- GCC_except_table175
- GCC_except_table180
- GCC_except_table184
- ___block_descriptor_40_e12_v20?0^I8I16l
CStrings:
+ "TB,GareWritableHeapsEnabled,SsetWritableHeapsEnabled:"
+ "^{GPUDebugDeviceOptions=b1b1b1b1}"
+ "_deviceOptions"
+ "areWritableHeapsEnabled"
+ "enumerateAccelerationStructureIndices:"
+ "setWritableHeapsEnabled:"
+ "writableHeapsEnabled"
+ "{GPUDebugDeviceOptions=\"retainReflection\"b1\"retainPSOFunctions\"b1\"abortOnFault\"b1\"enableDumpToStderr\"b1}"
+ "{HeapUsageTable=\"_heapUsage\"Q\"_heapStages\"{vector<std::pair<MTLGPUDebugHeap *, unsigned long>, std::allocator<std::pair<MTLGPUDebugHeap *, unsigned long>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::pair<MTLGPUDebugHeap *, unsigned long> *, std::allocator<std::pair<MTLGPUDebugHeap *, unsigned long>>>=\"__value_\"^v}}}"
- "{GPUDebugDeviceOptions=\"retainReflection\"b1\"retainPSOFunctions\"b1\"abortOnFault\"b1}"
- "{HeapUsageTable=\"_heapStages\"{vector<std::pair<MTLGPUDebugHeap *, unsigned long>, std::allocator<std::pair<MTLGPUDebugHeap *, unsigned long>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::pair<MTLGPUDebugHeap *, unsigned long> *, std::allocator<std::pair<MTLGPUDebugHeap *, unsigned long>>>=\"__value_\"^v}}}"

```
