## com.apple.driver.AppleHapticsSupportLEAP

> `com.apple.driver.AppleHapticsSupportLEAP`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-11.2.0.0.0
-  __TEXT.__const: 0x3d0
-  __TEXT.__cstring: 0x78d3
+11.4.0.0.0
+  __TEXT.__const: 0x3e0
+  __TEXT.__cstring: 0x78b7
   __TEXT.__os_log: 0x985
-  __TEXT_EXEC.__text: 0x3b724
+  __TEXT_EXEC.__text: 0x3b780
   __TEXT_EXEC.__auth_stubs: 0x6c0
   __DATA.__data: 0x6ac
   __DATA.__common: 0x658
-  __DATA.__bss: 0xdd0
+  __DATA.__bss: 0xe60
   __DATA_CONST.__mod_init_func: 0xf8
   __DATA_CONST.__mod_term_func: 0x108
   __DATA_CONST.__const: 0x7aa0

   __DATA_CONST.__got: 0xf0
   Functions: 1201
   Symbols:   0
-  CStrings:  1302
+  CStrings:  1300
 
Functions:
~ sub_fffffe0008fa8a7c -> sub_fffffe0008fbb41c : 1852 -> 1944
CStrings:
- "HRFault"
- "hallResistanceFault"
```
