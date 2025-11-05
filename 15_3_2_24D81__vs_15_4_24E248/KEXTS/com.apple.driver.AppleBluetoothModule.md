## com.apple.driver.AppleBluetoothModule

> `com.apple.driver.AppleBluetoothModule`

```diff

-66.0.0.0.0
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x25a0
-  __TEXT_EXEC.__text: 0x7ddc
+72.0.0.0.0
+  __TEXT.__const: 0x20
+  __TEXT.__cstring: 0x25d5
+  __TEXT_EXEC.__text: 0x8098
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x15c0
   __DATA_CONST.__kalloc_type: 0x180
-  UUID: CA8734F2-A299-34F3-ACBE-B543C0C353AB
-  Functions: 141
+  UUID: 137EE6DB-E3B6-3EE0-A0B9-CB6E7C0B2391
+  Functions: 140
   Symbols:   556
-  CStrings:  232
+  CStrings:  234
 
Symbols:
+ __ZZN20AppleBluetoothModule15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_528
+ __ZZN20AppleBluetoothModule15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_548
+ __ZZN20AppleBluetoothModule15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_567
+ __ZZN20AppleBluetoothModule15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_575
- __ZZN20AppleBluetoothModule15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_527
- __ZZN20AppleBluetoothModule15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_547
- __ZZN20AppleBluetoothModule15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_566
- __ZZN20AppleBluetoothModule15initCoreCaptureE16CCStreamLogLevelS0_E20kalloc_type_view_574
Functions:
~ __ZN20AppleBluetoothModule5startEP9IOService : 2512 -> 2536
~ __ZN20AppleBluetoothModule19amfmServiceNotifierEPvP9IOServiceP10IONotifier : 1140 -> 1152
~ __ZN20AppleBluetoothModule9sendStatsE27AppleBluetoothStatisticTypey : 100 -> 104
~ __ZN20AppleBluetoothModule14unquiesceGatedEv : 388 -> 392
~ __ZN20AppleBluetoothModule21waitForPCIDriverGatedEv : 176 -> 168
~ __ZN20AppleBluetoothModule19coredumpModuleGatedEPKc : 72 -> 80
~ __ZN20AppleBluetoothModule15generateMacAddrEP17IOEthernetAddress : 184 -> 192
~ __ZN20AppleBluetoothModule8flrGatedEPKc : 1240 -> 1248
~ __ZN20AppleBluetoothModule21powerCycleModuleGatedEPKc : 1420 -> 1516
~ __ZN20AppleBluetoothModule13setPropertiesEP8OSObject : 2236 -> 2232
~ __ZN20AppleBluetoothModule20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_ : 632 -> 640
~ __ZN20AppleBluetoothModule14copyPrimaryPMUEv : 428 -> 404
~ __ZN20AppleBluetoothModule23amfmMessageHandlerGatedEjP9IOServicePvm : 5276 -> 5868
- sub_fffffe00095b7558
~ __ZN30AppleBluetoothModuleUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv : 328 -> 348
~ _ZN20AppleBluetoothModule8flrGatedEPKc.cold.1 : 44 -> 80
~ _ZN20AppleBluetoothModule8flrGatedEPKc.cold.3 : 80 -> 44
~ _ZN20AppleBluetoothModule21powerCycleModuleGatedEPKc.cold.1 : 44 -> 80
~ _ZN20AppleBluetoothModule21powerCycleModuleGatedEPKc.cold.4 : 80 -> 44
~ _ZN20AppleBluetoothModule23amfmMessageHandlerGatedEjP9IOServicePvm.cold.2 : 44 -> 80
~ _ZN20AppleBluetoothModule23amfmMessageHandlerGatedEjP9IOServicePvm.cold.5 : 80 -> 44
~ _ZN20AppleBluetoothModule23amfmMessageHandlerGatedEjP9IOServicePvm.cold.7 : 44 -> 80
~ _ZN20AppleBluetoothModule23amfmMessageHandlerGatedEjP9IOServicePvm.cold.15 : 80 -> 44
~ _ZN20AppleBluetoothModule23amfmMessageHandlerGatedEjP9IOServicePvm.cold.17 : 44 -> 80
~ _ZN20AppleBluetoothModule23amfmMessageHandlerGatedEjP9IOServicePvm.cold.20 : 80 -> 44
CStrings:
+ "AppleBluetoothModule::%s:lpm3 object not found\n"
+ "lpm3"

```
