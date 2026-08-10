## com.apple.driver.AppleStockholmControl

> `com.apple.driver.AppleStockholmControl`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-370.40.2.0.0
-  __TEXT.__cstring: 0x478b
+370.42.1.0.0
+  __TEXT.__cstring: 0x47a9
   __TEXT.__const: 0x50
-  __TEXT_EXEC.__text: 0x14bd8
+  __TEXT_EXEC.__text: 0x14ccc
   __TEXT_EXEC.__auth_stubs: 0x500
   __DATA.__data: 0x219
   __DATA.__common: 0x17e

   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x80
-  Functions: 239
+  Functions: 240
   Symbols:   0
   CStrings:  465
 
Functions:
~ __ZN18AppleStockholmSPMI20_setVirtualGPIOGatedEh : 776 -> 844
~ __ZN18AppleStockholmSPMI22_setStandbyEnableGatedEb : 768 -> 836
+ sub_fffffe000976de5c
CStrings:
+ "ERR: %s::%s:%d failed to write to SPMI[0x%02X]:0x%02x - 0x%x, %d attempts\n"
+ "[%llu] ERR: %s::%s:%d failed to write to SPMI[0x%02X]:0x%02x - 0x%x, %d attempts"
- "ERR: %s::%s:%d failed to write to SPMI[0x%02X]:0x%02x - %x\n"
- "[%llu] ERR: %s::%s:%d failed to write to SPMI[0x%02X]:0x%02x - %x"
```
