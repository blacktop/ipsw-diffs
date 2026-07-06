## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

   __TEXT.__cstring: 0x690a
   __TEXT.__os_log: 0x5600
   __TEXT.__const: 0xe4
-  __TEXT_EXEC.__text: 0x48944
+  __TEXT_EXEC.__text: 0x48a5c
   __TEXT_EXEC.__auth_stubs: 0xe30
   __DATA.__data: 0x460
   __DATA.__common: 0x8e8

   __DATA_CONST.__auth_got: 0x718
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2168
-  Symbols:   3757
+  Functions: 2167
+  Symbols:   3756
   CStrings:  980
 
Sections:
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__assert : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ __ZZN13IOGPUResource10initializeEP11IOGPUDeviceP20IOGPUNewResourceArgsyE21kalloc_type_view_1253
+ __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2136
+ __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2199
+ __ZZN15IOGPUCountedSetIP11IOGPUMemory14IOGPUMemoryKey27IOGPUMemoryCountedSetBucket25IOGPUIOLibAllocatorPolicyLb0EEdlEPvmE19kalloc_type_view_39
+ __ZZN15IOGPUCountedSetIP11IOGPUMemory14IOGPUMemoryKey27IOGPUMemoryCountedSetBucket25IOGPUIOLibAllocatorPolicyLb0EEnwEmE19kalloc_type_view_39
- __ZZN13IOGPUResource10initializeEP11IOGPUDeviceP20IOGPUNewResourceArgsyE21kalloc_type_view_1245
- __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2128
- __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2191
- __ZZN15IOGPUCountedSetIP11IOGPUMemory14IOGPUMemoryKey27IOGPUMemoryCountedSetBucket25IOGPUIOLibAllocatorPolicyLb0EEdlEPvmE19kalloc_type_view_42
- __ZZN15IOGPUCountedSetIP11IOGPUMemory14IOGPUMemoryKey27IOGPUMemoryCountedSetBucket25IOGPUIOLibAllocatorPolicyLb0EEnwEmE19kalloc_type_view_42
Functions:
~ __ZN18IOGPUVirtualMemory4initEP5IOGPUyjbyyP4task : 1648 -> 1656
~ __ZN13IOGPUResource13sharedReleaseEP11IOGPUDevice : 264 -> 292
~ __ZN14IOGPUScheduler24hardware_error_interruptEP22IOInterruptEventSourcei : 820 -> 824
~ __ZN16IOGPUGroupMemory4wireEy : 3024 -> 3160
~ __ZN16IOGPUGroupMemory6unwireEv : 1580 -> 1716
- _OUTLINED_FUNCTION_0
~ __ZN22IOGPUResidentMemorySet4sortEv : 404 -> 440
~ _ZN16IOGPUGroupMemory4wireEy.cold.2 : 56 -> 44
~ _ZN16IOGPUGroupMemory6unwireEv.cold.2 : 56 -> 44

```
