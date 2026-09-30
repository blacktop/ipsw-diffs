## IOGPU

> `/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`

```diff

-124.1.0.0.0
-  __TEXT.__text: 0x28a7c
+126.0.0.0.0
+  __TEXT.__text: 0x28b28
   __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0x4cbc
+  __TEXT.__objc_methlist: 0x4cd4
   __TEXT.__cstring: 0x5f7f
   __TEXT.__const: 0x208
   __TEXT.__gcc_except_tab: 0x428
   __TEXT.__oslogstring: 0x8ae
-  __TEXT.__unwind_info: 0xcc8
+  __TEXT.__unwind_info: 0xcd0
   __TEXT.__objc_classname: 0x635
-  __TEXT.__objc_methname: 0xb4a9
+  __TEXT.__objc_methname: 0xb4bd
   __TEXT.__objc_methtype: 0x6ae0
-  __TEXT.__objc_stubs: 0x2fc0
+  __TEXT.__objc_stubs: 0x2fe0
   __DATA_CONST.__got: 0x418
   __DATA_CONST.__const: 0x768
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2798
+  __DATA_CONST.__objc_selrefs: 0x27a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x130
   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__const: 0x3f0
   __AUTH_CONST.__cfstring: 0x1300
-  __AUTH_CONST.__objc_const: 0x7cb0
+  __AUTH_CONST.__objc_const: 0x7cc8
   __AUTH.__objc_data: 0x6e0
   __DATA.__objc_ivar: 0x38c
   __DATA.__data: 0x7e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 71DDBDE0-8A47-3181-BC29-3FAD25F59B86
-  Functions: 1420
-  Symbols:   4245
-  CStrings:  2935
+  UUID: 10BC5878-8856-36DB-BD23-CA9D799C03B8
+  Functions: 1421
+  Symbols:   4248
+  CStrings:  2936
 
Symbols:
+ -[IOGPUMetal4CommandAllocator setCurrentCommandEncoder:]
+ ___39-[IOGPUMetalDevice launchMappingThread]_block_invoke.1328
+ _objc_msgSend$setCurrentCommandEncoder:
- ___39-[IOGPUMetalDevice launchMappingThread]_block_invoke.1326
Functions:
~ _IOGPUMetalCommandBufferStorageBeginSegment : 164 -> 160
~ -[IOGPUMetalCommandBuffer setCurrentCommandEncoder:] : 212 -> 220
~ -[IOGPUMetal4RenderCommandEncoder initWithCommandAllocator:] : 200 -> 236
~ -[IOGPUMetal4RenderCommandEncoder endEncoding] : 156 -> 180
~ -[IOGPUMetal4ComputeCommandEncoder initWithCommandAllocator:] : 224 -> 236
~ -[IOGPUMetal4MachineLearningCommandEncoder initWithCommandBuffer:allocator:] : 200 -> 224
~ -[IOGPUMetal4MachineLearningCommandEncoder endEncoding] : 156 -> 180
~ _IOGPUCommandQueueSupportsBackgroundAppRole : 228 -> 220
+ -[IOGPUMetal4CommandAllocator setCurrentCommandEncoder:]
CStrings:
+ "T^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}Q^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B},R,V_storage"
+ "^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}Q^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}"
+ "^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}Q^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}16@0:8"
+ "^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}Q^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}28@0:8Q16B24"
+ "supportsAtomicFloat"
+ "v28@0:8^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}Q^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}16I24"
+ "v84@0:8@16@24I32^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}Q^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}36Q44Q52I60@64@72B80"
- "T^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}@^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B},R,V_storage"
- "^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}@^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}"
- "^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}@^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}16@0:8"
- "^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}@^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}28@0:8Q16B24"
- "v28@0:8^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}@^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}16I24"
- "v84@0:8@16@24I32^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}@^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}36Q44Q52I60@64@72B80"

```
