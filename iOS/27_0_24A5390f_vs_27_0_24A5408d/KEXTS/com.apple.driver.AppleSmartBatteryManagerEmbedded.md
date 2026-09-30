## com.apple.driver.AppleSmartBatteryManagerEmbedded

> `com.apple.driver.AppleSmartBatteryManagerEmbedded`

```diff

-2043.0.31.0.0
-  __TEXT.__cstring: 0x7bf6
-  __TEXT.__const: 0x2440
-  __TEXT.__os_log: 0x2970
-  __TEXT_EXEC.__text: 0x304b8
-  __TEXT_EXEC.__auth_stubs: 0x7a0
+2043.0.45.502.1
+  __TEXT.__cstring: 0x8289
+  __TEXT.__const: 0x2630
+  __TEXT.__os_log: 0x28fb
+  __TEXT_EXEC.__text: 0x315e4
+  __TEXT_EXEC.__auth_stubs: 0x7c0
   __DATA.__data: 0x1f0
-  __DATA.__common: 0x3c0
-  __DATA.__bss: 0x5350
+  __DATA.__common: 0x4c8
+  __DATA.__bss: 0x5560
   __DATA_CONST.__mod_init_func: 0xa0
   __DATA_CONST.__mod_term_func: 0x78
   __DATA_CONST.__const: 0x5d58
   __DATA_CONST.__kalloc_type: 0x700
-  __DATA_CONST.__kalloc_var: 0x8c0
-  __DATA_CONST.__auth_got: 0x3d0
-  __DATA_CONST.__got: 0x100
-  Functions: 689
+  __DATA_CONST.__kalloc_var: 0x960
+  __DATA_CONST.__auth_got: 0x3e0
+  __DATA_CONST.__got: 0x108
+  Functions: 695
   Symbols:   0
-  CStrings:  1254
+  CStrings:  1280
 
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
+ "BatteryInstalled=%u packs:%d\n"
+ "Cell Check Fault"
+ "Charged Too Long"
+ "Charger Communication Failure"
+ "Ibatt MinFault"
+ "Ignoring SMC message type %#x while system is sleeping\n"
+ "Not restarting poll type %d while system is sleeping\n"
+ "Vbatt Fault"
+ "kPPMChemIdReq"
+ "kPPMDODInReq"
+ "kPPMInterfaceAPIReq"
+ "kPPMOutImpdDataR0"
+ "kPPMTempInReq"
- "1211111212221212111111111211111122212"
- "BatteryInstalled=%u packs:%zu\n"
- "Failed to clear shutdown data. rc:0x%x=%s\n"
- "Failed to read shutdown data error flags\n"
- "Failed to read shutdown nominal capacity\n"
- "Failed with permanent failure for cmd 0x%x\n"
- "No battery shutdown data\n"
- "failed to read shutdownData\n"
```
