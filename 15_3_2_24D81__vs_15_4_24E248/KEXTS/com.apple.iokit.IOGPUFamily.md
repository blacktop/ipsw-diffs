## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-104.1.2.0.0
-  __TEXT.__cstring: 0x57cb
-  __TEXT.__os_log: 0x3c9d
+104.4.1.0.0
+  __TEXT.__cstring: 0x5806
+  __TEXT.__os_log: 0x3d1d
   __TEXT.__const: 0xd4
-  __TEXT_EXEC.__text: 0x3e228
+  __TEXT_EXEC.__text: 0x3f080
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4b0
   __DATA.__common: 0x7d0
   __DATA.__bss: 0x9
-  __DATA_CONST.__auth_got: 0x668
+  __DATA_CONST.__auth_got: 0x678
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x100

   __DATA_CONST.__const: 0xba70
   __DATA_CONST.__kalloc_type: 0x1080
   __DATA_CONST.__kalloc_var: 0xf00
-  UUID: 58A77EFF-A976-30FA-82BE-105694713FB8
-  Functions: 1907
-  Symbols:   3204
-  CStrings:  799
+  __DATA_CONST.__assert: 0x78
+  UUID: 6271BAF4-DB8A-34AC-9967-4C793D9E9A93
+  Functions: 1899
+  Symbols:   3218
+  CStrings:  803
 
Symbols:
+ _ZN16IOGPUResourceSet16releaseResourcesEv.cold.1
+ _ZN20IOGPUIOCommandBuffer15processCommandsEjyb.cold.1
+ _ZNK11IOGPUObject13taggedReleaseEPKv.cold.1
+ _ZNK11IOGPUObject13taggedReleaseEPKvi.cold.2
+ _ZNK11IOGPUObject7releaseEi.cold.2
+ _ZNK11IOGPUObject7releaseEv.cold.1
+ __ZZN13IOGPUResource10initializeEP11IOGPUDeviceP20IOGPUNewResourceArgsyE21kalloc_type_view_1054
+ __ZZN13IOGPUResource16newResourceGroupEP5IOGPUP11IOGPUDevicejE11_os_log_fmt_1
+ __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_1881
+ __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_1929
+ __ZZN16IOGPUGroupMemory22addMemoryFromResourcesEPP13IOGPUResourcejE6__desc
+ __ZZN16IOGPUGroupMemory22addMemoryFromResourcesEPP13IOGPUResourcejE6__desc_0
+ __ZZN16IOGPUGroupMemory22addMemoryFromResourcesEPP13IOGPUResourcejE6__desc_1
+ __ZZN16IOGPUGroupMemory22addMemoryFromResourcesEPP13IOGPUResourcejE6__desc_2
+ __ZZN5IOGPU4freeEvE20kalloc_type_view_847
+ __ZZN5IOGPU5startEP9IOServiceE11_os_log_fmt__21_
+ __ZZZN13IOGPUResource19add_group_resourcesEPPS_jENK3$_1clES0_E6__desc
+ __ZZZN13IOGPUResource24add_group_resources_fastEPPS_jENK3$_1clES0_E6__desc
+ _kern_allocation_name_allocate
+ _kern_allocation_name_release
+ _thread_set_allocation_name
- _Assert
- _ZN24IOGPUClientSharedMachine13alloc_handlesEv.cold.1
- _ZN5IOGPU5startEP9IOService.cold.1
- __ZZN13IOGPUResource10initializeEP11IOGPUDeviceP20IOGPUNewResourceArgsyE21kalloc_type_view_1051
- __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_1878
- __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_1926
- __ZZN5IOGPU4freeEvE20kalloc_type_view_837
CStrings:
+ "%s: API Allocation Name allocation failed\n"
+ "%s: newResourceGroup failed - initial capacity (%u) less than minimum required (%u)\n"
+ "121111121222121212111111121211121222221111112112211122211111121112112212222222222222222222222221222122"
+ "com.apple.iokit.IOGPUFamily.API"
+ "result == kIOReturnSuccess"
- "121111121222121212111111121211121222221111112112211122211111121112112212222222222222222222222221222222"

```
