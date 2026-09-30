## com.apple.driver.AppleEffaceableNOR

> `com.apple.driver.AppleEffaceableNOR`

```diff

 88.0.0.0.0
   __TEXT.__cstring: 0x16c
-  __TEXT_EXEC.__text: 0xf30
+  __TEXT_EXEC.__text: 0xe10
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x1398
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: A9BCF54E-826D-3A6C-998B-688614FE95FF
-  Functions: 64
+  UUID: A613C06C-87D7-3738-B44A-92D480012037
+  Functions: 58
   Symbols:   395
   CStrings:  13
 
Functions:
- __ZN26AppleVirtualNORFlashDevice30CreateAppleEffaceableNORObjectEv
~ __Z18getRegionCountHookP19_effaceable_nor_hal : 48 -> 44
~ __Z17getRegionSizeHookP19_effaceable_nor_halj : 48 -> 44
~ __Z15eraseRegionHookP19_effaceable_nor_haljj : 48 -> 44
~ __Z15writeRegionHookP19_effaceable_nor_haljPKvjj : 48 -> 44
~ __Z14readRegionHookP19_effaceable_nor_haljPvjj : 48 -> 44
+ __ZN26AppleVirtualNORFlashDevice30CreateAppleEffaceableNORObjectEv

```
