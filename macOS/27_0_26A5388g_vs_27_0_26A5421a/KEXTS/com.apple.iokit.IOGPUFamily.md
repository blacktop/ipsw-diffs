## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-162.10.0.0.0
+162.11.0.0.0
   __TEXT.__cstring: 0x690a
-  __TEXT.__os_log: 0x5600
+  __TEXT.__os_log: 0x568f
   __TEXT.__const: 0xe4
-  __TEXT_EXEC.__text: 0x48a24
+  __TEXT_EXEC.__text: 0x48c1c
   __TEXT_EXEC.__auth_stubs: 0xe30
   __DATA.__data: 0x460
   __DATA.__common: 0x8e8

   __DATA_CONST.__auth_got: 0x718
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2167
-  Symbols:   3677
-  CStrings:  979
+  Functions: 2168
+  Symbols:   3680
+  CStrings:  981
 
Symbols:
+ __ZNK14IOGPUSysMemory22retainMemoryDescriptorEv
+ __ZZN13IOGPUResource10initializeEP11IOGPUDeviceP20IOGPUNewResourceArgsyE21kalloc_type_view_1271
+ __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2162
+ __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2225
+ __ZZN13IOGPUResource31newResourceWithParentResourceIDEP5IOGPUP11IOGPUDevice13eIOGPUResTypeyyyyPyjE11_os_log_fmt_8
+ __ZZN13IOGPUResource31newResourceWithParentResourceIDEP5IOGPUP11IOGPUDevice13eIOGPUResTypeyyyyPyjE11_os_log_fmt_9
- __ZZN13IOGPUResource10initializeEP11IOGPUDeviceP20IOGPUNewResourceArgsyE21kalloc_type_view_1253
- __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2144
- __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2207
Functions:
~ __ZN13IOGPUResource31newResourceWithParentResourceIDEP5IOGPUP11IOGPUDevice13eIOGPUResTypeyyyyPyj : 1044 -> 1212
~ __ZN13IOGPUResource12setOwnershipEP4task : 120 -> 128
~ __ZN11IOGPUDevice22set_resource_purgeableEj23eIOGPUResourcePurgeablePS0_ : 876 -> 912
~ __ZN11IOGPUDevice12new_resourceEP20IOGPUNewResourceArgsP26IOGPUNewResourceReturnDatayPj : 2460 -> 2500
~ __ZN11IOGPUDevice25create_resource_iosurfaceEjyyPj : 1204 -> 1248
+ __ZNK14IOGPUSysMemory22retainMemoryDescriptorEv
~ __ZN14IOGPUSysMemory18describeAllocationEP12OSDictionary : 576 -> 628
~ __ZN14IOGPUSysMemory22get_memory_descriptorsEjjPj : 760 -> 828
CStrings:
+ "%s: child resource (offset=0x%llx, size=0x%llx) exceeds parent memory size 0x%llx.\n"
+ "%s: client_buffer (0x%llx) precedes client_base (0x%llx).\n"
```
