## com.apple.driver.AppleCallbackPowerSource

> `com.apple.driver.AppleCallbackPowerSource`

```diff

-1754.120.2.0.0
-  __TEXT.__cstring: 0xf8f
+1846.0.7.0.0
+  __TEXT.__cstring: 0xf7f
   __TEXT.__os_log: 0x76
-  __TEXT_EXEC.__text: 0x4c70
+  __TEXT_EXEC.__text: 0x4b4c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd0
   __DATA.__common: 0x190
-  __DATA.__bss: 0x1438
-  __DATA_CONST.__auth_got: 0x150
+  __DATA.__bss: 0x1468
+  __DATA_CONST.__auth_got: 0x140
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xc00
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: D3C1F9BC-1B1E-34CE-8477-5BB874ADB2CD
+  UUID: C88E2DDF-D876-34B1-A3E8-AB2D4AC76FB7
   Functions: 63
   Symbols:   0
   CStrings:  240
Functions:
~ sub_fffffff008db24ec -> sub_fffffff008fc2ecc : 960 -> 952
~ sub_fffffff008db2a58 -> sub_fffffff008fc3430 : 376 -> 372
~ __ZN24AppleCallbackPowerSource21psCallbackThreadGatedEb : 2492 -> 2480
~ sub_fffffff008db3730 -> sub_fffffff008fc40f8 : 292 -> 316
~ __ZN24AppleCallbackPowerSource12updateStatusEb : 1128 -> 1132
~ __ZN24AppleCallbackPowerSource13setPropertiesEP8OSObject -> sub_fffffff008fc541c : 416 -> 48
~ __GLOBAL__sub_I_AppleCallbackPowerSource.cpp : 8156 -> 8228
CStrings:
+ "MaximumInternalTemperature"
+ "PTATFaultCounter"
- "PropertyOverride"
- "com.apple.private.iopmps.property-override"

```
