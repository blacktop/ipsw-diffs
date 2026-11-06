## com.apple.driver.AppleSmartBatteryManager

> `com.apple.driver.AppleSmartBatteryManager`

```diff

-2043.1.1.0.0
-  __TEXT.__cstring: 0x7ee8
-  __TEXT.__const: 0x2610
-  __TEXT.__os_log: 0x2627
-  __TEXT_EXEC.__text: 0x31b94
+2043.40.52.0.2
+  __TEXT.__cstring: 0x82ad
+  __TEXT.__const: 0x2640
+  __TEXT.__os_log: 0x2694
+  __TEXT_EXEC.__text: 0x3272c
   __TEXT_EXEC.__auth_stubs: 0x790
   __DATA.__data: 0x1f0
-  __DATA.__common: 0x4c8
-  __DATA.__bss: 0x54a0
+  __DATA.__common: 0x4d8
+  __DATA.__bss: 0x5688
   __DATA_CONST.__mod_init_func: 0xa0
   __DATA_CONST.__mod_term_func: 0x78
   __DATA_CONST.__const: 0x9a78

   __DATA_CONST.__kalloc_var: 0x960
   __DATA_CONST.__auth_got: 0x3c8
   __DATA_CONST.__got: 0x100
-  Functions: 684
-  Symbols:   2252
-  CStrings:  1226
+  Functions: 685
+  Symbols:   2279
+  CStrings:  1257
 
Symbols:
+ __RawCurrentCapacitySym
+ __RawMaxCapacitySym
+ __ZL15_kIsDevFusedSym
+ __ZL24_kBatteryAgingTlcTimeSym
+ __ZL24_kBatteryFeatureFlagsSym
+ __ZL28_kLifetimeFailureCountersSym
+ __ZL31_kLifetimeFailureCounterDataSym
+ __ZL38_kLifetimeFailureCounterChgOverTempSym
+ __ZL38_kLifetimeFailureCounterDsgOverTempSym
+ __ZL38_kLifetimeFailureCounterFETOverTempSym
+ __ZL38_kLifetimeFailureCounterOverVoltageSym
+ __ZL39_kLifetimeFailureCounterChgUnderTempSym
+ __ZL39_kLifetimeFailureCounterDsgUnderTempSym
+ __ZL39_kLifetimeFailureCounterUnderVoltageSym
+ __ZL40_kLifetimeFailureCounterChargeInhibitSym
+ __ZL40_kLifetimeFailureCounterChargeSuspendSym
+ __ZL43_kLifetimeFailureCounterChgOverCurrentHWSym
+ __ZL43_kLifetimeFailureCounterChgOverCurrentL1Sym
+ __ZL43_kLifetimeFailureCounterChgOverCurrentL2Sym
+ __ZL43_kLifetimeFailureCounterDsgOverCurrentL1Sym
+ __ZL43_kLifetimeFailureCounterDsgOverCurrentL2Sym
+ __ZL43_kLifetimeFailureCounterPassedChargeLowVSym
+ __ZL44_kLifetimeFailureCounterDsgOverCurrentHW1Sym
+ __ZL44_kLifetimeFailureCounterDsgOverCurrentHW2Sym
+ __ZL44_kLifetimeFailureCounterDsgShortCircuitHWSym
+ __ZL44_kLifetimeFailureCounterPassedChargeHighVSym
+ __ZN21AppleSmartBatteryPack17_parsePackBootArgEPKcPvi
+ __ZNK21AppleSmartBatteryPack33createLifetimeFailureCountersDictEPK6OSData
+ __ZZN17AppleSmartBattery10messageSMCEPK8OSSymbolP8OSObjectmE11_os_log_fmt_4
+ __ZZN17AppleSmartBattery18initializeCommandsEvE21kalloc_type_view_2518
+ __ZZN17AppleSmartBattery18smcNotifierHandlerEPvP9IOServiceP10IONotifierE21kalloc_type_view_6488
+ __ZZN17AppleSmartBattery18smcNotifierHandlerEPvP9IOServiceP10IONotifierE21kalloc_type_view_6499
+ __ZZN17AppleSmartBattery21handlePollingFinishedEbE11_os_log_fmt_0
+ __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_538
+ __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_541
+ __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_542
+ __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_543
+ __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_544
+ __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_305
+ __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_319
+ __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_361
+ __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_383
+ __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_411
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1749
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1750
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1751
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1752
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1753
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1754
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1759
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_914
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_929
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_941
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_953
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_965
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_973
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_984
- __ZL18_RawMaxCapacitySym
- __ZL22_RawCurrentCapacitySym
- __ZN21AppleSmartBatteryPack17_parsePackBootArgEPKcPvm
- __ZZN17AppleSmartBattery18initializeCommandsEvE21kalloc_type_view_2516
- __ZZN17AppleSmartBattery18smcNotifierHandlerEPvP9IOServiceP10IONotifierE21kalloc_type_view_6417
- __ZZN17AppleSmartBattery18smcNotifierHandlerEPvP9IOServiceP10IONotifierE21kalloc_type_view_6428
- __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_531
- __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_534
- __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_535
- __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_536
- __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_537
- __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_297
- __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_311
- __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_354
- __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_376
- __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_404
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1563
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1564
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1565
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1566
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1567
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1568
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1573
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_874
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_889
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_901
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_913
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_925
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_933
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_944
CStrings:
+ "12111112122212121111111112111111122221112"
+ "AgingTlcTime"
+ "AppleSmartBatteryPack: DBG: ID: %d Gauge reports no lifetime failure counters\n"
+ "AppleSmartBatteryPack: DBG: ID: %d Lifetime failure counter mask has slots this kext does not publish:%#llx\n"
+ "AppleSmartBatteryPack: ID: %d Battery data read aborted. ltd:%d kiosk:%d carrier:%d\n"
+ "AppleSmartBatteryPack: ID: %d Battery pack is pending/missing/bad\n"
+ "AppleSmartBatteryPack: ID: %d Lifetime failure counter payload is %u bytes, expected %zu\n"
+ "AppleSmartBatteryPack: ID: %d updateRebalanceData: rebalancing not supported, ret=%d\n"
+ "BatteryInstalled=%u packs:%d\n"
+ "ChargeInhibit"
+ "ChargeSuspend"
+ "ChargingOverCurrentHW"
+ "ChargingOverCurrentLevel1"
+ "ChargingOverCurrentLevel2"
+ "ChargingOverTemperature"
+ "ChargingUnderTemperature"
+ "DischargingOverCurrentHW1"
+ "DischargingOverCurrentHW2"
+ "DischargingOverCurrentLevel1"
+ "DischargingOverCurrentLevel2"
+ "DischargingOverTemperature"
+ "DischargingShortCircuitHW"
+ "DischargingUnderTemperature"
+ "FETOverTemperature"
+ "FailureCounters"
+ "FeatureFlags"
+ "Ignoring SMC message type %#x while system is sleeping\n"
+ "IsDevFused"
+ "LTFailureCounterData"
+ "Not restarting poll type %d while system is sleeping\n"
+ "OverVoltage"
+ "PassedChargeHighVoltage"
+ "PassedChargeLowVoltage"
+ "UnderVoltage"
- "1211111212221212111111111211111112221112"
- "AppleSmartBatteryPack: ID: %d Battery pack is missing/bad\n"
- "BatteryInstalled=%u packs:%zu\n"
```
