## com.apple.driver.ApplePassthroughPPM

> `com.apple.driver.ApplePassthroughPPM`

```diff

-1191.0.37.0.0
+1191.40.27.0.1
   __TEXT.__const: 0x1170
-  __TEXT.__cstring: 0xff06
-  __TEXT.__os_log: 0x4441
-  __TEXT_EXEC.__text: 0x5b670
+  __TEXT.__cstring: 0xffb4
+  __TEXT.__os_log: 0x4646
+  __TEXT_EXEC.__text: 0x5bf50
   __TEXT_EXEC.__auth_stubs: 0x7b0
   __DATA.__data: 0x160
   __DATA.__common: 0x578
   __DATA.__bss: 0x200
   __DATA_CONST.__mod_init_func: 0xf8
   __DATA_CONST.__mod_term_func: 0xc8
-  __DATA_CONST.__const: 0x92e0
+  __DATA_CONST.__const: 0x9370
   __DATA_CONST.__kalloc_type: 0xa40
   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x10
-  Functions: 2351
-  Symbols:   2800
-  CStrings:  1916
+  Functions: 2373
+  Symbols:   2818
+  CStrings:  1931
 
Symbols:
+ __ZN12ApplePPMCPMS21pushAsbLpemDataOnWakeEv
+ __ZN12ApplePPMCPMS33trailingBudgetFlushTimeoutHandlerEP18IOTimerEventSource
+ __ZN18ApplePPMPolicyCPMS15updateACSKDroopEf
+ __ZN18ApplePPMPolicyCPMS20resolveClientBudgetsEPjPb16UniqueClientID_tU13block_pointerFvP18CPMSPPMPowerBudgetP31DetailedThermalBudgetsForClientE
+ __ZN19ApplePassthroughPPM21pushAsbLpemDataOnWakeEv
+ __ZN19ApplePassthroughPPM24getDynamicSocVcutFeatureEv
+ __ZN31ApplePPMSystemCapabilityMonitor14getUseLpemDataEv
+ __ZN35ApplePPMCPMSSystemCapabilityMonitor14getUseLpemDataEv
+ __ZN8ApplePPM24getDynamicSocVcutFeatureEv
+ __ZNK12ApplePPMCPMS27requiresTrailingBudgetFlushEv
+ __ZNK19ApplePassthroughPPM27requiresTrailingBudgetFlushEv
+ __ZZN12ApplePPMCPMS25updatePMUVoltageThresholdEjhE11_os_log_fmt
+ __ZZN18ApplePPMPolicyCPMS20resolveClientBudgetsEPjPb16UniqueClientID_tU13block_pointerFvP18CPMSPPMPowerBudgetP31DetailedThermalBudgetsForClientEE11_os_log_fmt
+ __ZZN18ApplePPMPolicyCPMS20resolveClientBudgetsEPjPb16UniqueClientID_tU13block_pointerFvP18CPMSPPMPowerBudgetP31DetailedThermalBudgetsForClientEE11_os_log_fmt_0
+ __ZZN19ApplePassthroughPPM21pushAsbLpemDataOnWakeEvE11_os_log_fmt
+ __ZZN22ApplePPMDynamicSocVcut20readAndUpdateFromASBEvE11_os_log_fmt_5
+ __ZZN22ApplePPMDynamicSocVcut20readAndUpdateFromASBEvE11_os_log_fmt_6
+ __ZZN22ApplePPMDynamicSocVcut20readAndUpdateFromASBEvE11_os_log_fmt_7
+ __ZZN31ApplePPMCPMSMeasuredPowerHelperdlEPvmE20kalloc_type_view_927
+ __ZZN31ApplePPMCPMSMeasuredPowerHelpernwEmE20kalloc_type_view_927
+ __ZZN31ApplePPMSystemCapabilityMonitor29getTemperatureFromBatteryDictEP12OSDictionaryPfE11_os_log_fmt
+ __ZZN35ApplePPMCPMSSystemCapabilityMonitor23readBatteryInputFromASBEvE11_os_log_fmt_6
+ __ZZN35ApplePPMCPMSSystemCapabilityMonitor23readBatteryInputFromASBEvE11_os_log_fmt_7
- __ZN18ApplePPMPolicyCPMS20resolveClientBudgetsEPb16UniqueClientID_tU13block_pointerFvP18CPMSPPMPowerBudgetP31DetailedThermalBudgetsForClientE
- __ZZN18ApplePPMPolicyCPMS20resolveClientBudgetsEPb16UniqueClientID_tU13block_pointerFvP18CPMSPPMPowerBudgetP31DetailedThermalBudgetsForClientEE11_os_log_fmt
- __ZZN18ApplePPMPolicyCPMS20resolveClientBudgetsEPb16UniqueClientID_tU13block_pointerFvP18CPMSPPMPowerBudgetP31DetailedThermalBudgetsForClientEE11_os_log_fmt_0
- __ZZN31ApplePPMCPMSMeasuredPowerHelperdlEPvmE20kalloc_type_view_918
- __ZZN31ApplePPMCPMSMeasuredPowerHelpernwEmE20kalloc_type_view_918
CStrings:
+ "%s::%s:failed to get SoC1Vcut from bank %u of gPPMBatteryKey_Soc1Vcut array\n\n"
+ "%s::%s:failed to get array entry from key gPPMBatteryKey_Soc1Vcut\n"
+ "%s::%s:failed to get array from key gPPMBatteryKey_Soc1Vcut\n\n"
+ "%s::%s:failed to get data from key gPPMBatteryKey_Soc1Vcut\n\n"
+ "%s::%s:failed to get number from key gPPMBatteryKey_AlgoTemperature\n"
+ "%s::%s:failed to get number from key gPPMBatteryKey_Soc1Vcut\n"
+ "%s::%s:function-btm-vthr callFunction failed with error 0x%08x\n\n"
+ "%s::%s:gPPMBatteryKey_Soc1Vcut array is empty\n\n"
+ "%s::%s:sendAsbLpemData failed with 0x%x for battery pack=%d, bank=%d\n"
+ "12222112222222222112222222222222222222222222222222222221111222222122112"
+ "12222112222222222112222222222222222222222222222222222221111222222122112111212211122212222222211"
+ "122221122222222221122222222222222222222222222222222222211112222221221121112122111222122222222111"
+ "OverrideSoc1Voltage"
+ "UseOverrideSoc1Voltage"
+ "Vtarget-Vdroop-fallback"
+ "_trailingBudgetFlushTimer"
+ "getTemperatureFromBatteryDict"
+ "pushAsbLpemDataOnWake"
+ "updatePMUVoltageThreshold"
- "%s::%s:failed to get SoC1Vcut from key gPPMBatteryKey_Soc1Vcut\n\n"
- "1222211222222222211222222222222222222222222222222222221111222222122112"
- "1222211222222222211222222222222222222222222222222222221111222222122112111212211122212222222211"
- "12222112222222222112222222222222222222222222222222222211112222221221121112122111222122222222111"
```
