## com.apple.driver.ApplePassthroughPPM

> `com.apple.driver.ApplePassthroughPPM`

```diff

-1191.0.27.0.0
+1191.0.37.0.0
   __TEXT.__const: 0x1170
   __TEXT.__cstring: 0xff06
-  __TEXT.__os_log: 0x4476
-  __TEXT_EXEC.__text: 0x5a0e0
+  __TEXT.__os_log: 0x4441
+  __TEXT_EXEC.__text: 0x5a0f4
   __TEXT_EXEC.__auth_stubs: 0x7b0
   __DATA.__data: 0x160
   __DATA.__common: 0x578

   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__auth_ptr: 0x10
   Functions: 2349
-  Symbols:   2801
-  CStrings:  1917
+  Symbols:   2800
+  CStrings:  1916
 
Symbols:
+ __ZN12ApplePPMCPMS38prepareAndSendControlSnapshotTelemetryE36CPMSPPMControlStateSnapshotRingIndex
+ __ZN8ApplePPM38prepareAndSendControlSnapshotTelemetryE36CPMSPPMControlStateSnapshotRingIndex
+ __ZZN12ApplePPMCPMS38prepareAndSendControlSnapshotTelemetryE36CPMSPPMControlStateSnapshotRingIndexE11_os_log_fmt
+ __ZZN12ApplePPMCPMS38prepareAndSendControlSnapshotTelemetryE36CPMSPPMControlStateSnapshotRingIndexE11_os_log_fmt_0
+ __ZZN12ApplePPMCPMS38prepareAndSendControlSnapshotTelemetryE36CPMSPPMControlStateSnapshotRingIndexE11_os_log_fmt_1
- __ZN12ApplePPMCPMS38prepareAndSendControlSnapshotTelemetryEv
- __ZN8ApplePPM38prepareAndSendControlSnapshotTelemetryEv
- __ZZN12ApplePPMCPMS38prepareAndSendControlSnapshotTelemetryEvE11_os_log_fmt
- __ZZN12ApplePPMCPMS38prepareAndSendControlSnapshotTelemetryEvE11_os_log_fmt_0
- __ZZN12ApplePPMCPMS38prepareAndSendControlSnapshotTelemetryEvE11_os_log_fmt_1
- __ZZN12ApplePPMCPMS38prepareAndSendControlSnapshotTelemetryEvE11_os_log_fmt_2
Functions:
~ __ZN12ApplePPMCPMS36updateTimestampsTracesAndShimBudgetsE16UniqueClientID_tP18CPMSPPMPowerBudgetP31DetailedThermalBudgetsForClientPj : 424 -> 484
~ __ZN12ApplePPMCPMS14triggerLoggingEy : 364 -> 396
~ __ZN12ApplePPMCPMS38prepareAndSendControlSnapshotTelemetryEv -> __ZN12ApplePPMCPMS38prepareAndSendControlSnapshotTelemetryE36CPMSPPMControlStateSnapshotRingIndex : 552 -> 452
~ __ZN18ApplePPMUserClient17telemetryDonationEv : 204 -> 208
~ __ZN23ApplePPMBatteryModel4RC16calculateMaxPuVFEPfffbfbfffS0_S0_bbffff : 2320 -> 2328
~ __ZN23ApplePPMBatteryModel4RC31calculatePredictiveVoltageDroopEPfffbbffS0_S0_bfff : 1616 -> 1624
~ __ZN23ApplePPMBatteryModel4RC31calculatePredictiveVoltageDroopEPfffbbffS0_S0_bfffff : 1892 -> 1900
CStrings:
- "%s::%s:%s: Failed to allocate local snapshot rings\n\n"
```
