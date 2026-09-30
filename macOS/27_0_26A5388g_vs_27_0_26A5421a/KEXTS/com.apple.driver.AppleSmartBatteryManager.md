## com.apple.driver.AppleSmartBatteryManager

> `com.apple.driver.AppleSmartBatteryManager`

```diff

-2043.0.31.0.0
-  __TEXT.__cstring: 0x784c
-  __TEXT.__const: 0x2420
-  __TEXT.__os_log: 0x2709
-  __TEXT_EXEC.__text: 0x30468
-  __TEXT_EXEC.__auth_stubs: 0x770
+2043.0.47.0.3
+  __TEXT.__cstring: 0x7ee8
+  __TEXT.__const: 0x2610
+  __TEXT.__os_log: 0x2627
+  __TEXT_EXEC.__text: 0x314ec
+  __TEXT_EXEC.__auth_stubs: 0x790
   __DATA.__data: 0x1f0
-  __DATA.__common: 0x3c0
-  __DATA.__bss: 0x5270
+  __DATA.__common: 0x4c8
+  __DATA.__bss: 0x54a0
   __DATA_CONST.__mod_init_func: 0xa0
   __DATA_CONST.__mod_term_func: 0x78
   __DATA_CONST.__const: 0x9a78
   __DATA_CONST.__kalloc_type: 0x700
-  __DATA_CONST.__kalloc_var: 0x8c0
-  __DATA_CONST.__auth_got: 0x3b8
-  __DATA_CONST.__got: 0xf8
-  Functions: 678
-  Symbols:   2244
-  CStrings:  1201
+  __DATA_CONST.__kalloc_var: 0x960
+  __DATA_CONST.__auth_got: 0x3c8
+  __DATA_CONST.__got: 0x100
+  Functions: 684
+  Symbols:   2252
+  CStrings:  1226
 
Symbols:
+ __ZL13_kIPDRatioSym
+ __ZL22shutdownDataSystemKeys
+ __ZL24shutdownDataKeysTemplate
+ __ZL26shutdownDataKeysTemplate1D
+ __ZN17AppleSmartBattery22readSystemShutdownDataEv
+ __ZN21AppleSmartBatteryPack16readShutdownDataEv
+ __ZN21AppleSmartBatteryPack18cpmsArrivalHandlerEPvP9IOServiceP10IONotifier
+ __ZN21AppleSmartBatteryPack19updateRebalanceDataEv
+ __ZN21AppleSmartBatteryPack20updateErrorConditionEv
+ __ZN21AppleSmartBatteryPack23cpmsArrivalHandlerGatedEP9IOService
+ __ZN8OSNumber10withDoubleEd
+ __ZNK8OSNumber10floatValueEv
+ __ZNK8OSNumber11doubleValueEv
+ __ZZN17AppleSmartBattery18initializeCommandsEvE21kalloc_type_view_2516
+ __ZZN17AppleSmartBattery18smcNotifierHandlerEPvP9IOServiceP10IONotifierE21kalloc_type_view_6417
+ __ZZN17AppleSmartBattery18smcNotifierHandlerEPvP9IOServiceP10IONotifierE21kalloc_type_view_6428
+ __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_531
+ __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_537
+ __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_297
+ __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_311
+ __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_354
+ __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_376
+ __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_404
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1563
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1564
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1565
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1566
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1567
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1568
+ __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1573
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_874
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_889
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_901
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_913
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_925
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_933
+ __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_944
+ __kShutdownDataAverageCurrentSym
+ __kShutdownDataCriticalFlagsSym
+ __kShutdownDataDOD0Sym
+ __kShutdownDataDataErrorSym
+ __kShutdownDataFilteredCurrentSym
+ __kShutdownDataFullChargeCapacitySym
+ __kShutdownDataLpemModeSym
+ __kShutdownDataMaxDischargeCurrentSym
+ __kShutdownDataNominalChargeCapacitySym
+ __kShutdownDataPassedChargeSym
+ __kShutdownDataPresentDODSym
+ __kShutdownDataPrevAverageCurrentSym
+ __kShutdownDataPrevFullChargeCapacitySym
+ __kShutdownDataPrevNominalChargeCapacitySym
+ __kShutdownDataPrevRemainingCapacitySym
+ __kShutdownDataPrevVoltageSym
+ __kShutdownDataRSSSym
+ __kShutdownDataRaTableRawSym
+ __kShutdownDataRemainingCapacitySym
+ __kShutdownDataResScaleSym
+ __kShutdownDataRestartTimestampSym
+ __kShutdownDataShutdownSocSym
+ __kShutdownDataShutdownVoltageSym
+ __kShutdownDataSoc1vcutSym
+ __kShutdownDataSocAlarmSym
+ __kShutdownDataSocSoc2Sym
+ __kShutdownDataSocfThresSym
+ __kShutdownDataSwFccSym
+ __kShutdownDataSwRemCapSym
+ __kShutdownDataTemperatureSym
+ __kShutdownDataUiSocSym
+ __kShutdownDataUnexpectedRestartSym
+ __kShutdownDataVoltageSym
+ _gIOFirstMatchNotification
- __ZL16shutdownDataKeys
- __ZL20_kShutdownDataRSSSym
- __ZL21_kShutdownDataDOD0Sym
- __ZL22_kShutdownDataSwFccSym
- __ZL22_kShutdownDataUiSocSym
- __ZL24_kShutdownDataSocSoc2Sym
- __ZL24_kShutdownDataVoltageSym
- __ZL25_kShutdownDataLpemModeSym
- __ZL25_kShutdownDataResScaleSym
- __ZL25_kShutdownDataSoc1vcutSym
- __ZL25_kShutdownDataSocAlarmSym
- __ZL25_kShutdownDataSwRemCapSym
- __ZL26_kShutdownDataDataErrorSym
- __ZL26_kShutdownDataSocfThresSym
- __ZL27_kShutdownDataPresentDODSym
- __ZL27_kShutdownDataRaTableRawSym
- __ZL28_kShutdownDataPrevVoltageSym
- __ZL28_kShutdownDataShutdownSocSym
- __ZL28_kShutdownDataTemperatureSym
- __ZL29_kShutdownDataPassedChargeSym
- __ZL30_kShutdownDataCriticalFlagsSym
- __ZL31_kShutdownDataAverageCurrentSym
- __ZL32_kShutdownDataFilteredCurrentSym
- __ZL32_kShutdownDataShutdownVoltageSym
- __ZL33_kShutdownDataRestartTimestampSym
- __ZL34_kShutdownDataRemainingCapacitySym
- __ZL34_kShutdownDataUnexpectedRestartSym
- __ZL35_kShutdownDataFullChargeCapacitySym
- __ZL35_kShutdownDataPrevAverageCurrentSym
- __ZL36_kShutdownDataMaxDischargeCurrentSym
- __ZL38_kShutdownDataNominalChargeCapacitySym
- __ZL38_kShutdownDataPrevRemainingCapacitySym
- __ZL39_kShutdownDataPrevFullChargeCapacitySym
- __ZL42_kShutdownDataPrevNominalChargeCapacitySym
- __ZN15IOPMPowerSource17setErrorConditionEP8OSSymbol
- __ZZN17AppleSmartBattery16readShutdownDataEvE11_os_log_fmt
- __ZZN17AppleSmartBattery16readShutdownDataEvE11_os_log_fmt_0
- __ZZN17AppleSmartBattery16readShutdownDataEvE11_os_log_fmt_1
- __ZZN17AppleSmartBattery16readShutdownDataEvE11_os_log_fmt_2
- __ZZN17AppleSmartBattery16readShutdownDataEvE11_os_log_fmt_3
- __ZZN17AppleSmartBattery18initializeCommandsEvE21kalloc_type_view_2589
- __ZZN17AppleSmartBattery18smcNotifierHandlerEPvP9IOServiceP10IONotifierE21kalloc_type_view_6565
- __ZZN17AppleSmartBattery18smcNotifierHandlerEPvP9IOServiceP10IONotifierE21kalloc_type_view_6576
- __ZZN17AppleSmartBattery26transactionCompletionGatedEP30transactionCompletionGatedArgsE11_os_log_fmt__15_
- __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_530
- __ZZN21AppleSmartBatteryBank4freeEvE20kalloc_type_view_533
- __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_296
- __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_310
- __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_353
- __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_375
- __ZZN21AppleSmartBatteryBank5startEP9IOServiceE20kalloc_type_view_403
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1353
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1354
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1355
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1356
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1357
- __ZZN21AppleSmartBatteryPack4freeEvE21kalloc_type_view_1362
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_794
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_809
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_821
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_833
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_845
- __ZZN21AppleSmartBatteryPack5startEP9IOServiceE20kalloc_type_view_853
CStrings:
+ "1211111212221212111111111211111112221112"
+ "ApplePPMCPMS"
+ "ApplePPMInterfaceAPIFunction"
+ "AppleSmartBatteryPack: ID: %d Failed to clear shutdown data. rc:0x%x=%s\n"
+ "AppleSmartBatteryPack: ID: %d Failed to create shutdown reason symbol\n"
+ "AppleSmartBatteryPack: ID: %d Failed to read shutdown data error flags\n"
+ "AppleSmartBatteryPack: ID: %d Failed to read shutdown nominal capacity\n"
+ "AppleSmartBatteryPack: ID: %d Failed to update Error Condition\n"
+ "AppleSmartBatteryPack: ID: %d No battery shutdown data for pack %d\n"
+ "AppleSmartBatteryPack: ID: %d failed to read shutdownData for pack %d\n"
+ "AppleSmartBatteryPack: ID: %d updateRebalanceData: PPM API call failed, ret=%d\n"
+ "AppleSmartBatteryPack: ID: %d updateRebalanceData: PPM returned all-zero impedance array, skipping SMC write\n"
+ "AppleSmartBatteryPack: ID: %d updateRebalanceData: failed to allocate dataIn\n"
+ "AppleSmartBatteryPack: ID: %d updateRebalanceData: failed to get impedance array from PPM output\n"
+ "AppleSmartBatteryPack: ID: %d updateRebalanceData: failed to get impedence key (%c%c%c%c) data, ret=%d\n"
+ "AppleSmartBatteryPack: ID: %d updateRebalanceData: failed to read DOD key, ret=%d\n"
+ "AppleSmartBatteryPack: ID: %d updateRebalanceData: failed to read temp key, ret=%d\n"
+ "AppleSmartBatteryPack: ID: %d updateRebalanceData: failed to write impedence key (%c%c%c%c), raw=%d,ret=%d\n"
+ "AppleSmartBatteryPack: ID: %d updateRebalanceData: no Algo chem ID in bank batteryData\n"
+ "AppleSmartBatteryPack: ID: %d updateRebalanceData: no bank instance\n"
+ "AppleSmartBatteryPack: ID: %d updateRebalanceData: no batteryData in bank\n"
+ "Cell Check Fault"
+ "Charged Too Long"
+ "Charger Communication Failure"
+ "IPDRatio"
+ "Ibatt MinFault"
+ "Vbatt Fault"
+ "kPPMChemIdReq"
+ "kPPMDODInReq"
+ "kPPMInterfaceAPIReq"
+ "kPPMOutImpdDataR0"
+ "kPPMTempInReq"
- "1211111212221212111111111211111122212"
- "Failed to clear shutdown data. rc:0x%x=%s\n"
- "Failed to read shutdown data error flags\n"
- "Failed to read shutdown nominal capacity\n"
- "Failed with permanent failure for cmd 0x%x\n"
- "No battery shutdown data\n"
- "failed to read shutdownData\n"
```
