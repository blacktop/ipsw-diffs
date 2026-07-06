## com.apple.driver.AppleSmartBatteryManager

> `com.apple.driver.AppleSmartBatteryManager`

```diff

-  __TEXT.__cstring: 0x798a
+  __TEXT.__cstring: 0x77be
   __TEXT.__const: 0x23f0
   __TEXT.__os_log: 0x26d0
-  __TEXT_EXEC.__text: 0x3032c
+  __TEXT_EXEC.__text: 0x3011c
   __TEXT_EXEC.__auth_stubs: 0x770
   __DATA.__data: 0x1f0
   __DATA.__common: 0x3c0

   __DATA_CONST.__got: 0xf8
   Functions: 678
   Symbols:   2279
-  CStrings:  1200
+  CStrings:  1194
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ __ZZN16AppleChargerData5startEP9IOServiceE20kalloc_type_view_129
+ __ZZN21AppleBeadsBatteryAuth12authSendDataEhP6OSDataE21kalloc_type_view_1367
+ __ZZN21AppleBeadsBatteryAuth20_battAuthThreadGatedEP13batt_auth_cmdE21kalloc_type_view_1275
+ __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_530
+ __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_533
+ __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_534
+ __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_296
+ __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_310
+ __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_353
+ __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_375
+ __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_403
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1341
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1342
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1343
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1344
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1345
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1350
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_792
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_807
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_819
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_831
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_843
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_851
- __ZZN16AppleChargerData5startEP9IOServiceE20kalloc_type_view_128
- __ZZN21AppleBeadsBatteryAuth12authSendDataEhP6OSDataE21kalloc_type_view_1364
- __ZZN21AppleBeadsBatteryAuth20_battAuthThreadGatedEP13batt_auth_cmdE21kalloc_type_view_1272
- __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_532
- __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_537
- __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_538
- __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_298
- __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_312
- __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_355
- __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_377
- __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_405
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1364
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1365
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1366
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1367
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1368
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1373
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_815
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_830
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_842
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_854
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_866
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_874
Functions:
~ __ZN21AppleBeadsBatteryAuth18_getServiceVersionEv : 432 -> 480
~ __ZN16AppleBatteryAuth15_getCertificateEP13batt_auth_cmdPP6OSData : 932 -> 940
~ __ZN21AppleSmartBatteryPack11_smcReadKeyEjyPv : 328 -> 164
~ __ZN21AppleSmartBatteryPack12_smcWriteKeyEjyPv : 328 -> 164
~ __ZN21AppleSmartBatteryPack18pollDateOfFirstUseEv : 168 -> 176
~ __ZN17AppleSmartBattery18initializeCommandsEv : 2248 -> 2256
~ __ZN17AppleSmartBattery22handleSetItAndForgetItEiiPKhy : 344 -> 336
~ __ZN21AppleSmartBatteryBank12_smcWriteKeyEjyPv : 344 -> 176
~ __ZN16AppleChargerData6withIDEh : 192 -> 200
~ __ZN16AppleChargerData11_smcReadKeyEjyPv : 328 -> 164
~ __ZN16AppleChargerData20setChargerEnergyDataEP15chgPwrTelemetry : 804 -> 860
~ __ZN16AppleChargerData4freeEv : 132 -> 136
CStrings:
+ "1211111212221212112121212"
- "121111121222121211212112"
- "AppleChargerData: ID: %d failed to read key '%c%c%c%c' retry:%zu rc:%#x=%s\n"
- "AppleSmartBatteryBank: DBG: Pack ID: %d Bank ID: %d WriteSMCKey attempt %lu/%u"
- "AppleSmartBatteryBank: Pack ID: %d Bank ID: %d failed to write key '%c%c%c%c', retry:%zu\n"
- "AppleSmartBatteryPack: DBG: ID: %d WriteSMCKey attempt %lu/%u"
- "AppleSmartBatteryPack: ID: %d failed to read key '%c%c%c%c' retry:%zu rc:%#x=%s\n"
- "AppleSmartBatteryPack: ID: %d failed to write key '%c%c%c%c', retry:%zu\n"

```
