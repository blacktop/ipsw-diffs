## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__assert`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-162.9.0.0.0
+162.10.0.0.0
   __TEXT.__cstring: 0x690a
   __TEXT.__os_log: 0x5600
   __TEXT.__const: 0xe4
-  __TEXT_EXEC.__text: 0x48a5c
+  __TEXT_EXEC.__text: 0x48a24
   __TEXT_EXEC.__auth_stubs: 0xe30
   __DATA.__data: 0x460
   __DATA.__common: 0x8e8
Symbols:
+ __ZZN11IOGPUDevice19group_add_resourcesEjPKjmE21kalloc_type_view_2394
+ __ZZN11IOGPUDevice19group_add_resourcesEjPKjmE21kalloc_type_view_2400
+ __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2144
+ __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2207
+ __ZZN14IOGPUSysMemory22get_memory_descriptorsEjjPjE21kalloc_type_view_1146
+ __ZZN14IOGPUSysMemory22get_memory_descriptorsEjjPjE21kalloc_type_view_1184
+ __ZZN22IOGPUCommandDescriptor9addMemoryEP11IOGPUMemoryE20kalloc_type_view_165
- __ZZN11IOGPUDevice19group_add_resourcesEjPKjmE21kalloc_type_view_2353
- __ZZN11IOGPUDevice19group_add_resourcesEjPKjmE21kalloc_type_view_2359
- __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2136
- __ZZN13IOGPUResource19add_group_resourcesEPPS_jE21kalloc_type_view_2199
- __ZZN14IOGPUSysMemory22get_memory_descriptorsEjjPjE21kalloc_type_view_1124
- __ZZN14IOGPUSysMemory22get_memory_descriptorsEjjPjE21kalloc_type_view_1155
- __ZZN22IOGPUCommandDescriptor9addMemoryEP11IOGPUMemoryE20kalloc_type_view_183
Functions:
~ __ZN22IOGPUCommandDescriptor9addMemoryEP11IOGPUMemory : 404 -> 348
```
