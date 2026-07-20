## com.apple.driver.DiskImages.UDIFDiskImage

> `com.apple.driver.DiskImages.UDIFDiskImage`

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

-698.0.0.0.0
+701.0.0.0.0
   __TEXT.__const: 0x3058
   __TEXT.__cstring: 0x2b0
-  __TEXT_EXEC.__text: 0xb494
+  __TEXT_EXEC.__text: 0xb514
   __TEXT_EXEC.__auth_stubs: 0x240
   __DATA.__data: 0xc4
   __DATA.__common: 0xd8
Functions:
~ __ZN16KDIUDIFDiskImage11readSectorsExxPxPvb : 1564 -> 1588
~ sub_fffffe000a0900c4 -> sub_fffffe000a0ae79c : 768 -> 780
~ sub_fffffe000a0907b8 -> sub_fffffe000a0aee9c : 876 -> 984
~ sub_fffffe000a093434 -> sub_fffffe000a0b1b84 : 1420 -> 1404
```
