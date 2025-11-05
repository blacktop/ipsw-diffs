## com.apple.driver.AppleEffaceableBlockDevice

> `com.apple.driver.AppleEffaceableBlockDevice`

```diff

 88.0.0.0.0
   __TEXT.__cstring: 0x166
-  __TEXT_EXEC.__text: 0x1074
+  __TEXT_EXEC.__text: 0xfb0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x9b8
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: A22CE208-4755-369D-832A-3FB5FEC12381
-  Functions: 55
+  UUID: B9A1D022-51CF-358F-B986-38D6258E0AD7
+  Functions: 50
   Symbols:   381
   CStrings:  14
 
Functions:
~ _startEffaceableBDEV : 300 -> 304
~ __ZN26AppleEffaceableBlockDevice5startEP9IOService : 356 -> 364
- __Z18getStorageSizeHookP20_effaceable_bdev_hal
~ __Z9writeHookP20_effaceable_bdev_halPKvj : 48 -> 44
~ __ZN26AppleEffaceableBlockDevice9writeBDEVEPKvj : 212 -> 232
~ __Z10formatHookP20_effaceable_bdev_hal : 100 -> 96
+ __Z18getStorageSizeHookP20_effaceable_bdev_hal

```
