## com.apple.driver.ApplePPMCPMS

> `com.apple.driver.ApplePPMCPMS`

```diff

-1191.0.27.0.0
+1191.0.37.0.0
   __TEXT.__const: 0x1150
   __TEXT.__cstring: 0xf888
-  __TEXT.__os_log: 0x3eb3
-  __TEXT_EXEC.__text: 0x5326c
+  __TEXT.__os_log: 0x3e7e
+  __TEXT_EXEC.__text: 0x53280
   __TEXT_EXEC.__auth_stubs: 0x7b0
   __DATA.__data: 0x164
   __DATA.__common: 0x500

   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__auth_ptr: 0x10
   Functions: 2170
   Symbols:   0
-  CStrings:  1858
+  CStrings:  1857
 
Functions:
~ __ZN12ApplePPMCPMS36updateTimestampsTracesAndShimBudgetsE16UniqueClientID_tP18CPMSPPMPowerBudgetP31DetailedThermalBudgetsForClientPj : 424 -> 484
~ __ZN12ApplePPMCPMS14triggerLoggingEy : 364 -> 396
~ __ZN12ApplePPMCPMS38prepareAndSendControlSnapshotTelemetryEv : 552 -> 452
~ sub_fffffe0009364dbc -> sub_fffffe000934e164 : 204 -> 208
~ sub_fffffe0009388a24 -> sub_fffffe0009371dd0 : 2320 -> 2328
~ sub_fffffe000938a38c -> sub_fffffe0009373740 : 1624 -> 1632
~ sub_fffffe000938a9e4 -> sub_fffffe0009373da0 : 1900 -> 1908
CStrings:
- "%s::%s:%s: Failed to allocate local snapshot rings\n\n"
```
