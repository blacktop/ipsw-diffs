## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__assert`

```diff

-130.16.3.0.0
+130.16.4.0.0
   __TEXT.__cstring: 0x64ea
   __TEXT.__os_log: 0x4fa2
   __TEXT.__const: 0xcc
-  __TEXT_EXEC.__text: 0x46a48
+  __TEXT_EXEC.__text: 0x46a40
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x460
   __DATA.__common: 0x8e8
Symbols:
+ __ZZN11IOGPUDevice19group_add_resourcesEjPKjmE21kalloc_type_view_2388
+ __ZZN11IOGPUDevice19group_add_resourcesEjPKjmE21kalloc_type_view_2394
+ __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2135
+ __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2198
+ __ZZN14IOGPUSysMemory22get_memory_descriptorsEjjPjE21kalloc_type_view_1091
+ __ZZN14IOGPUSysMemory22get_memory_descriptorsEjjPjE21kalloc_type_view_1129
- __ZZN11IOGPUDevice19group_add_resourcesEjPKjmE21kalloc_type_view_2354
- __ZZN11IOGPUDevice19group_add_resourcesEjPKjmE21kalloc_type_view_2360
- __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2127
- __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2190
- __ZZN14IOGPUSysMemory22get_memory_descriptorsEjjPjE21kalloc_type_view_1069
- __ZZN14IOGPUSysMemory22get_memory_descriptorsEjjPjE21kalloc_type_view_1100
Functions:
~ __ZN11IOGPUDevice25create_resource_iosurfaceEjyyPj : 1168 -> 1160
```
