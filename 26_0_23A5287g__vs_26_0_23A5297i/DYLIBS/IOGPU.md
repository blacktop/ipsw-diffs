## IOGPU

> `/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`

```diff

-128.0.0.0.0
-  __TEXT.__text: 0x28bf4
+128.1.0.0.0
+  __TEXT.__text: 0x28bdc
   __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_methlist: 0x4cd4
-  __TEXT.__cstring: 0x5f7f
+  __TEXT.__cstring: 0x5f8c
   __TEXT.__const: 0x208
   __TEXT.__gcc_except_tab: 0x428
   __TEXT.__oslogstring: 0x8ae
   __TEXT.__unwind_info: 0xcc8
   __TEXT.__objc_classname: 0x635
-  __TEXT.__objc_methname: 0xb4bd
-  __TEXT.__objc_methtype: 0x6ae9
+  __TEXT.__objc_methname: 0xb4dc
+  __TEXT.__objc_methtype: 0x6aec
   __TEXT.__objc_stubs: 0x2fe0
   __DATA_CONST.__got: 0x418
   __DATA_CONST.__const: 0x768

   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__const: 0x3f0
   __AUTH_CONST.__cfstring: 0x1300
-  __AUTH_CONST.__objc_const: 0x7cc8
+  __AUTH_CONST.__objc_const: 0x7ce8
   __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x38c
+  __DATA.__objc_ivar: 0x390
   __DATA.__data: 0x7e0
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x780

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CB45AC5F-A339-3F2E-92D2-E517F4DDF721
+  UUID: FFB1B817-D108-3408-A034-358127BFEF95
   Functions: 1421
-  Symbols:   4248
-  CStrings:  2936
+  Symbols:   4249
+  CStrings:  2937
 
Symbols:
+ -[IOGPUMetal4CommandQueue commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:submissionID:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:]
+ -[IOGPUMetal4CommandQueue commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:submissionID:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:].cold.1
+ OBJC_IVAR_$_IOGPUMetal4CommandQueue._lastSubmissionID
+ ___block_descriptor_85_e8_32o40o48o56o_e17_v36?0Q8Q16I24Q28ls32l8s40l8s48l8s56l8
+ _objc_msgSend$commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:submissionID:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:
- -[IOGPUMetal4CommandQueue commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:]
- -[IOGPUMetal4CommandQueue commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:].cold.1
- ___block_descriptor_77_e8_32o40o48o56o_e17_v36?0Q8Q16I24Q28ls32l8s40l8s48l8s56l8
- _objc_msgSend$commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:
Functions:
~ -[IOGPUMetal4CommandQueue preCommit:count:options:] : 268 -> 300
~ -[IOGPUMetal4CommandQueue commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:] -> -[IOGPUMetal4CommandQueue commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:submissionID:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:] : 248 -> 252
~ -[IOGPUMetal4CommandQueue commitFillArgs:count:args:argsSize:commitFeedback:] : 300 -> 316
~ -[IOGPUMetal4CommandQueue _commit:count:commitFeedback:] : 272 -> 288
~ __ZL20submitCommandBuffersPv : 800 -> 708
CStrings:
+ "-[IOGPUMetal4CommandQueue commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:submissionID:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:]"
+ "_lastSubmissionID"
+ "commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:submissionID:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:"
+ "v92@0:8@16@24I32^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}Q^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}36Q44Q52Q60I68@72@80B88"
- "-[IOGPUMetal4CommandQueue commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:]"
- "commandBufferComplete:commandAllocator:commandAllocatorGeneration:storage:startTime:completionTime:kernelError:error:commitFeedback:commitComplete:"
- "v84@0:8@16@24I32^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}Q^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B}36Q44Q52I60@64@72B80"

```
