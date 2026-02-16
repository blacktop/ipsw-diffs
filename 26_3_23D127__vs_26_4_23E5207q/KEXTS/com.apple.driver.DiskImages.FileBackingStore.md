## com.apple.driver.DiskImages.FileBackingStore

> `com.apple.driver.DiskImages.FileBackingStore`

```diff

-681.60.1.0.0
+683.100.3.0.0
+  __TEXT.__const: 0x10
   __TEXT.__cstring: 0x237
-  __TEXT_EXEC.__text: 0x1404
+  __TEXT_EXEC.__text: 0x12e0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x38

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x678
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 570F3B01-A102-34D5-953D-50CDF714C4AF
+  UUID: 24B159A1-6C62-37B6-B398-49EFDBCDF73C
   Functions: 32
   Symbols:   0
   CStrings:  20
Functions:
~ sub_fffffe000a637128 -> sub_fffffe0009d05e88 : 36 -> 32
~ __ZN19KDIFileBackingStore5probeEP9IOServicePi -> sub_fffffe0009d05ea8 : 208 -> 192
~ __ZN19KDIFileBackingStore12getUserVnodeEP8OSObjectP11vfs_context -> sub_fffffe0009d05f68 : 260 -> 248
~ __ZN19KDIFileBackingStore12_handleStartEP9IOService -> sub_fffffe0009d06090 : 1576 -> 1344
~ __ZN19KDIFileBackingStore11_handleStopEP9IOService -> sub_fffffe0009d065d0 : 256 -> 248
~ sub_fffffe000a637aa8 -> sub_fffffe0009d066f8 : 444 -> 448
~ sub_fffffe000a637c64 -> sub_fffffe0009d068b8 : 584 -> 576
~ sub_fffffe000a637eac -> sub_fffffe0009d06af8 : 596 -> 588
~ sub_fffffe000a638100 -> sub_fffffe0009d06d44 : 200 -> 192

```
