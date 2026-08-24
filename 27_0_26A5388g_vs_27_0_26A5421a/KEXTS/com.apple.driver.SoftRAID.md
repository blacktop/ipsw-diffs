## com.apple.driver.SoftRAID

> `com.apple.driver.SoftRAID`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-57.0.0.0.0
+58.0.0.0.0
   __TEXT.__const: 0x180
   __TEXT.__cstring: 0x26fb
-  __TEXT_EXEC.__text: 0x31cf8
-  __TEXT_EXEC.__auth_stubs: 0x650
+  __TEXT_EXEC.__text: 0x31ce4
+  __TEXT_EXEC.__auth_stubs: 0x660
   __DATA.__data: 0xc8
   __DATA.__common: 0x818
   __DATA_CONST.__mod_init_func: 0xf0
   __DATA_CONST.__mod_term_func: 0xf0
   __DATA_CONST.__const: 0xc028
   __DATA_CONST.__kalloc_var: 0x19f0
-  __DATA_CONST.__kalloc_type: 0xcc0
-  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__kalloc_type: 0xd40
+  __DATA_CONST.__auth_got: 0x330
   __DATA_CONST.__got: 0xd0
   Functions: 1778
-  Symbols:   2810
+  Symbols:   2813
   CStrings:  307
 
Symbols:
+ _IOFreeData
+ _IOFreeTypeImpl
+ _IOMallocData
+ _IOMallocTypeImpl
+ _IOMallocZeroData
+ __ZZN44com_softraid_driver_SoftRAID_WA_CacheManager22StoreCacheToIORegistryEvE21kalloc_type_view_1408
+ __ZZN44com_softraid_driver_SoftRAID_WA_CacheManager23LoadCacheFromIORegistryEvE21kalloc_type_view_1334
- _IOFree
- _IOMalloc
- __ZdaPv
- __Znam
Functions:
~ __Z36AllocateAndInitIORegstryEntryPathPtrP15IORegistryEntryPPc : 364 -> 352
~ __ZN44com_softraid_driver_SoftRAID_WA_CacheManager23LoadCacheFromIORegistryEv : 852 -> 868
~ __ZN44com_softraid_driver_SoftRAID_WA_CacheManager22StoreCacheToIORegistryEv : 836 -> 840
~ __ZN46com_softraid_driver_SoftRAID_DirtyBlockManager23ConvertVolumeToExtendedEP35com_softraid_driver_SoftRAID_VolumeP32ExtendedVolumePartitionStatusRec : 380 -> 352
CStrings:
+ "21:39:10"
+ "Aug 11 2026"
- "21:18:13"
- "Jul 14 2026"
```
