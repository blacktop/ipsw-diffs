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
-  __TEXT_EXEC.__text: 0xafe4
+  __TEXT_EXEC.__text: 0xb0a4
   __TEXT_EXEC.__auth_stubs: 0x240
   __DATA.__data: 0xc4
   __DATA.__common: 0xd8
Symbols:
+ __ZZN16KDIUDIFDiskImage20_analyzeBackingStoreEvE21kalloc_type_view_1040
+ __ZZN16KDIUDIFDiskImage20_analyzeBackingStoreEvE21kalloc_type_view_1107
- __ZZN16KDIUDIFDiskImage20_analyzeBackingStoreEvE21kalloc_type_view_1036
- __ZZN16KDIUDIFDiskImage20_analyzeBackingStoreEvE21kalloc_type_view_1103
Functions:
~ __ZN16KDIUDIFDiskImage11readSectorsExxPxPvb : 1564 -> 1588
~ __ZN16KDIUDIFDiskImage15readSectorChunkExPxS0_PPvb : 768 -> 780
~ __ZN16KDIUDIFDiskImage19_generateGlobalBLKXEP14UDIFFileHeaderPP6OSDatas : 884 -> 1000
~ _lzvnDecode : 1176 -> 1216
```
