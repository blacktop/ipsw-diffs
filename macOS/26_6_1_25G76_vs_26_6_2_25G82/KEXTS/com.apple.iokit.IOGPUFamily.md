## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

   __TEXT.__cstring: 0x64ea
   __TEXT.__os_log: 0x4fa2
   __TEXT.__const: 0xcc
-  __TEXT_EXEC.__text: 0x46a40
+  __TEXT_EXEC.__text: 0x46b98
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x460
   __DATA.__common: 0x8e8

   __DATA_CONST.__kalloc_type: 0x1240
   __DATA_CONST.__kalloc_var: 0x1090
   __DATA_CONST.__assert: 0x28
-  Functions: 2145
-  Symbols:   3628
+  Functions: 2146
+  Symbols:   3629
   CStrings:  936
 
Symbols:
+ __ZNK14IOGPUSysMemory22retainMemoryDescriptorEv
Functions:
~ __ZN13IOGPUResource12setOwnershipEP4task : 120 -> 128
~ __ZN11IOGPUDevice22set_resource_purgeableEj23eIOGPUResourcePurgeablePS0_ : 828 -> 864
~ __ZN11IOGPUDevice12new_resourceEP20IOGPUNewResourceArgsP26IOGPUNewResourceReturnDatayPj : 2432 -> 2472
~ __ZN11IOGPUDevice25create_resource_iosurfaceEjyyPj : 1160 -> 1216
+ __ZNK14IOGPUSysMemory22retainMemoryDescriptorEv
~ __ZN14IOGPUSysMemory18describeAllocationEP12OSDictionary : 576 -> 628
~ __ZN14IOGPUSysMemory22get_memory_descriptorsEjjPj : 724 -> 788
```
