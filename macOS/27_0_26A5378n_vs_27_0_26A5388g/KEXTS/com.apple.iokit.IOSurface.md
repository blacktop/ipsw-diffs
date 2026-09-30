## com.apple.iokit.IOSurface

> `com.apple.iokit.IOSurface`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-402.4.0.0.0
+402.5.0.0.0
   __TEXT.__cstring: 0x32bf
   __TEXT.__os_log: 0x345e
   __TEXT.__const: 0x40
-  __TEXT_EXEC.__text: 0x34350
+  __TEXT_EXEC.__text: 0x3438c
   __TEXT_EXEC.__auth_stubs: 0x930
   __DATA.__data: 0x178
   __DATA.__common: 0x460
Symbols:
+ __ZZN13IOSurfaceRoot14client_startedEP23IOSurfaceRootUserClientP4taskE21kalloc_type_view_3178
+ __ZZN13IOSurfaceRoot14client_startedEP23IOSurfaceRootUserClientP4taskE21kalloc_type_view_3188
+ __ZZN13IOSurfaceRoot22addEventNotifierClientEPFvP8OSObjectES1_E21kalloc_type_view_3127
+ __ZZN13IOSurfaceRoot25removeEventNotifierClientEP28IOSurfaceEventNotifierClientE21kalloc_type_view_3157
- __ZZN13IOSurfaceRoot14client_startedEP23IOSurfaceRootUserClientP4taskE21kalloc_type_view_3166
- __ZZN13IOSurfaceRoot14client_startedEP23IOSurfaceRootUserClientP4taskE21kalloc_type_view_3176
- __ZZN13IOSurfaceRoot22addEventNotifierClientEPFvP8OSObjectES1_E21kalloc_type_view_3115
- __ZZN13IOSurfaceRoot25removeEventNotifierClientEP28IOSurfaceEventNotifierClientE21kalloc_type_view_3145
Functions:
~ __ZN13IOSurfaceRoot23purge_iomd_from_mappersEP18IOMemoryDescriptor : 204 -> 264
```
