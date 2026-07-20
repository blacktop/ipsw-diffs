## com.apple.driver.AppleSmartBatteryManagerEmbedded

> `com.apple.driver.AppleSmartBatteryManagerEmbedded`

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

-2043.0.13.502.1
-  __TEXT.__cstring: 0x7b68
-  __TEXT.__const: 0x2410
-  __TEXT.__os_log: 0x2937
-  __TEXT_EXEC.__text: 0x301dc
+2043.0.31.0.0
+  __TEXT.__cstring: 0x7bf6
+  __TEXT.__const: 0x2440
+  __TEXT.__os_log: 0x2970
+  __TEXT_EXEC.__text: 0x304b8
   __TEXT_EXEC.__auth_stubs: 0x7a0
   __DATA.__data: 0x1f0
   __DATA.__common: 0x3c0
-  __DATA.__bss: 0x52e0
+  __DATA.__bss: 0x5350
   __DATA_CONST.__mod_init_func: 0xa0
   __DATA_CONST.__mod_term_func: 0x78
   __DATA_CONST.__const: 0x5d58

   __DATA_CONST.__got: 0x100
   Functions: 689
   Symbols:   0
-  CStrings:  1247
+  CStrings:  1254
 
Functions:
~ sub_fffffe00097256b4 -> sub_fffffe00097416c4 : 2428 -> 2672
~ sub_fffffe00097267a4 -> sub_fffffe00097428a8 : 9108 -> 9156
~ sub_fffffe000973d56c -> sub_fffffe00097596a0 : 696 -> 932
~ sub_fffffe0009743af8 -> sub_fffffe000975fd18 : 14004 -> 14144
~ sub_fffffe000974a5b0 -> sub_fffffe000976685c : 3188 -> 3252
CStrings:
+ "AppleSmartBatteryPack: ID: %d Battery pack is missing/bad\n"
+ "Failed to read shipping charge limit UISOC smcResult:%d\n"
+ "IlimFrzReason"
+ "RxPwrLimitReason"
+ "ShipChargeLimitComplianceStatePending"
+ "UISoc"
+ "VmaxNcc"
```
