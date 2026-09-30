## com.apple.driver.AppleStockholmControl

> `com.apple.driver.AppleStockholmControl`

```diff

-370.40.2.0.0
-  __TEXT.__cstring: 0x4585
+370.42.1.0.0
+  __TEXT.__cstring: 0x45a3
   __TEXT.__const: 0x30
-  __TEXT_EXEC.__text: 0x148cc
+  __TEXT_EXEC.__text: 0x149c0
   __TEXT_EXEC.__auth_stubs: 0x500
   __DATA.__data: 0x219
   __DATA.__common: 0x17e

   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x80
-  Functions: 239
-  Symbols:   726
+  Functions: 240
+  Symbols:   727
   CStrings:  452
 
Symbols:
+ __ZN18AppleStockholmSPMI28_shouldRetryVirtualGPIOWriteEhiPii
Functions:
~ __ZN18AppleStockholmSPMI22_setStandbyEnableGatedEb : 768 -> 836
~ __ZN18AppleStockholmSPMI20_setVirtualGPIOGatedEh : 776 -> 844
+ __ZN18AppleStockholmSPMI28_shouldRetryVirtualGPIOWriteEhiPii
CStrings:
+ "ERR: %s::%s:%d failed to write to SPMI[0x%02X]:0x%02x - 0x%x, %d attempts\n"
+ "[%llu] ERR: %s::%s:%d failed to write to SPMI[0x%02X]:0x%02x - 0x%x, %d attempts"
- "ERR: %s::%s:%d failed to write to SPMI[0x%02X]:0x%02x - %x\n"
- "[%llu] ERR: %s::%s:%d failed to write to SPMI[0x%02X]:0x%02x - %x"
```
