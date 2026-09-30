## com.apple.driver.DiskImages.UDIFDiskImage

> `com.apple.driver.DiskImages.UDIFDiskImage`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

   __TEXT.__const: 0x3050
   __TEXT.__cstring: 0x2b0
-  __TEXT_EXEC.__text: 0xa8d0
+  __TEXT_EXEC.__text: 0xa950
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0xd8
Functions:
~ __ZN16KDIUDIFDiskImage11readSectorsExxPxPvb : 1564 -> 1588
~ sub_fffffe0009d00c84 -> sub_fffffe0009c6641c : 768 -> 780
~ sub_fffffe0009d0137c -> sub_fffffe0009c66b20 : 844 -> 912
~ sub_fffffe0009d03ffc -> sub_fffffe0009c697e4 : 1412 -> 1436
```
