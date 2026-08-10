## com.apple.driver.DiskImages.FileBackingStore

> `com.apple.driver.DiskImages.FileBackingStore`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-701.0.0.0.0
+704.0.0.0.0
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x237
-  __TEXT_EXEC.__text: 0x12e0
+  __TEXT_EXEC.__text: 0x132c
   __TEXT_EXEC.__auth_stubs: 0x260
   __DATA.__data: 0xc4
   __DATA.__common: 0x38
Functions:
~ __ZN19KDIFileBackingStore12_handleStartEP9IOService : 1344 -> 1420
```
