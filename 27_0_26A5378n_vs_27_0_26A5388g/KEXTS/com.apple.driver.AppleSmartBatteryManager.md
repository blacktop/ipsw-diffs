## com.apple.driver.AppleSmartBatteryManager

> `com.apple.driver.AppleSmartBatteryManager`

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

-2043.0.13.0.2
-  __TEXT.__cstring: 0x77be
-  __TEXT.__const: 0x23f0
-  __TEXT.__os_log: 0x26d0
-  __TEXT_EXEC.__text: 0x3011c
+2043.0.31.0.0
+  __TEXT.__cstring: 0x784c
+  __TEXT.__const: 0x2420
+  __TEXT.__os_log: 0x2709
+  __TEXT_EXEC.__text: 0x30468
   __TEXT_EXEC.__auth_stubs: 0x770
   __DATA.__data: 0x1f0
   __DATA.__common: 0x3c0
-  __DATA.__bss: 0x5200
+  __DATA.__bss: 0x5270
   __DATA_CONST.__mod_init_func: 0xa0
   __DATA_CONST.__mod_term_func: 0x78
   __DATA_CONST.__const: 0x9a78

   __DATA_CONST.__auth_got: 0x3b8
   __DATA_CONST.__got: 0xf8
   Functions: 678
-  Symbols:   2238
-  CStrings:  1194
+  Symbols:   2244
+  CStrings:  1201
 
Symbols:
+ __ZL12_kVmaxNccSym
+ __ZL15_kIlimFrzRsnSym
+ __ZL18_kRxPwrLimitRsnSym
+ __ZL25_kShipChargeLimitUiSocSym
+ __ZL42_kShipChargeLimitComplianceStatePendingSym
+ __ZZN17AppleSmartBattery18initializeCommandsEvE21kalloc_type_view_2589
+ __ZZN17AppleSmartBattery18smcNotifierHandlerEPvP9IOServiceP10IONotifierE21kalloc_type_view_6565
+ __ZZN17AppleSmartBattery18smcNotifierHandlerEPvP9IOServiceP10IONotifierE21kalloc_type_view_6576
+ __ZZN17AppleSmartBattery27readShippingChargeLimitDataEvE11_os_log_fmt_2
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1353
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1354
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1355
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1356
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1357
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1362
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_794
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_809
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_821
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_833
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_845
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_853
- __ZZN17AppleSmartBattery18initializeCommandsEvE21kalloc_type_view_2584
- __ZZN17AppleSmartBattery18smcNotifierHandlerEPvP9IOServiceP10IONotifierE21kalloc_type_view_6549
- __ZZN17AppleSmartBattery18smcNotifierHandlerEPvP9IOServiceP10IONotifierE21kalloc_type_view_6560
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1341
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1342
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1343
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1344
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1345
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1350
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_792
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_807
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_819
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_831
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_843
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_851
Functions:
~ __ZN21AppleSmartBatteryPack17updateBatteryDataEv : 2608 -> 2876
~ _GLOBAL__sub_I_AppleSmartBatteryPack.cpp : 9108 -> 9160
~ __ZN17AppleSmartBattery27readShippingChargeLimitDataEv : 788 -> 1080
~ _GLOBAL__sub_I_AppleSmartBattery.cpp : 13716 -> 13856
~ __ZN21AppleSmartBatteryBank20handleLpemPropsGatedEP12OSDictionary : 3648 -> 3740
CStrings:
+ "AppleSmartBatteryPack: ID: %d Battery pack is missing/bad\n"
+ "Failed to read shipping charge limit UISOC smcResult:%d\n"
+ "IlimFrzReason"
+ "RxPwrLimitReason"
+ "ShipChargeLimitComplianceStatePending"
+ "UISoc"
+ "VmaxNcc"
```
