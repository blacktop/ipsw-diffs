## com.apple.driver.AppleStockholmControl

> `com.apple.driver.AppleStockholmControl`

```diff

-  __TEXT.__cstring: 0x45e9
+  __TEXT.__cstring: 0x4585
   __TEXT.__const: 0x30
-  __TEXT_EXEC.__text: 0x14a98
+  __TEXT_EXEC.__text: 0x148cc
   __TEXT_EXEC.__auth_stubs: 0x500
   __DATA.__data: 0x219
   __DATA.__common: 0x17e

   __DATA_CONST.__got: 0x80
   Functions: 239
   Symbols:   743
-  CStrings:  454
+  CStrings:  452
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ __ZN18AppleStockholmSPMI16_vGPIOWriteGatedEhi
- __ZN18AppleStockholmSPMI16_vGPIOWriteGatedEh
Functions:
~ __ZN18AppleStockholmSPMI22_setStandbyEnableGatedEb : 924 -> 768
~ __ZN18AppleStockholmSPMI20_setVirtualGPIOGatedEh : 924 -> 776
~ __ZN18AppleStockholmSPMI16_vGPIOWriteGatedEh -> __ZN18AppleStockholmSPMI16_vGPIOWriteGatedEhi : 716 -> 560
CStrings:
+ "[%llu] %s::%s:%d write to SPMI[0x%02X] - %02x, attempt %d"
- "[%llu] %s::%s:%d attempt %d"
- "[%llu] %s::%s:%d second write to SPMI was NACKed, ignore NACK since this is a reset"
- "[%llu] %s::%s:%d write to SPMI[0x%02X] - %02x"

```
