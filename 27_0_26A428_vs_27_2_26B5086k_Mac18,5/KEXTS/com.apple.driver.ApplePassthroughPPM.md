## com.apple.driver.ApplePassthroughPPM

> `com.apple.driver.ApplePassthroughPPM`

```diff

-1191.0.37.0.0
+1191.40.25.0.0
   __TEXT.__const: 0x1170
-  __TEXT.__cstring: 0xff06
-  __TEXT.__os_log: 0x4441
-  __TEXT_EXEC.__text: 0x57c9c
+  __TEXT.__cstring: 0xff36
+  __TEXT.__os_log: 0x4487
+  __TEXT_EXEC.__text: 0x58020
   __TEXT_EXEC.__auth_stubs: 0x7b0
   __DATA.__data: 0x160
   __DATA.__common: 0x578
   __DATA_CONST.__mod_init_func: 0xf8
   __DATA_CONST.__mod_term_func: 0xc8
-  __DATA_CONST.__const: 0x92e0
+  __DATA_CONST.__const: 0x9318
   __DATA_CONST.__kalloc_type: 0xa40
   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x10
-  Functions: 2351
-  Symbols:   2800
-  CStrings:  1916
+  Functions: 2360
+  Symbols:   2808
+  CStrings:  1919
 
Symbols:
+ __ZN12ApplePPMCPMS21pushAsbLpemDataOnWakeEv
+ __ZN12ApplePPMCPMS33trailingBudgetFlushTimeoutHandlerEP18IOTimerEventSource
+ __ZN18ApplePPMPolicyCPMS20resolveClientBudgetsEPjPb16UniqueClientID_tU13block_pointerFvP18CPMSPPMPowerBudgetP31DetailedThermalBudgetsForClientE
+ __ZN19ApplePassthroughPPM21pushAsbLpemDataOnWakeEv
+ __ZN31ApplePPMSystemCapabilityMonitor14getUseLpemDataEv
+ __ZN35ApplePPMCPMSSystemCapabilityMonitor14getUseLpemDataEv
+ __ZNK12ApplePPMCPMS27requiresTrailingBudgetFlushEv
+ __ZNK19ApplePassthroughPPM27requiresTrailingBudgetFlushEv
+ __ZZN18ApplePPMPolicyCPMS20resolveClientBudgetsEPjPb16UniqueClientID_tU13block_pointerFvP18CPMSPPMPowerBudgetP31DetailedThermalBudgetsForClientEE11_os_log_fmt
+ __ZZN18ApplePPMPolicyCPMS20resolveClientBudgetsEPjPb16UniqueClientID_tU13block_pointerFvP18CPMSPPMPowerBudgetP31DetailedThermalBudgetsForClientEE11_os_log_fmt_0
+ __ZZN19ApplePassthroughPPM21pushAsbLpemDataOnWakeEvE11_os_log_fmt
+ __ZZN31ApplePPMCPMSMeasuredPowerHelperdlEPvmE20kalloc_type_view_919
+ __ZZN31ApplePPMCPMSMeasuredPowerHelpernwEmE20kalloc_type_view_919
- __ZN18ApplePPMPolicyCPMS20resolveClientBudgetsEPb16UniqueClientID_tU13block_pointerFvP18CPMSPPMPowerBudgetP31DetailedThermalBudgetsForClientE
- __ZZN18ApplePPMPolicyCPMS20resolveClientBudgetsEPb16UniqueClientID_tU13block_pointerFvP18CPMSPPMPowerBudgetP31DetailedThermalBudgetsForClientEE11_os_log_fmt
- __ZZN18ApplePPMPolicyCPMS20resolveClientBudgetsEPb16UniqueClientID_tU13block_pointerFvP18CPMSPPMPowerBudgetP31DetailedThermalBudgetsForClientEE11_os_log_fmt_0
- __ZZN31ApplePPMCPMSMeasuredPowerHelperdlEPvmE20kalloc_type_view_918
- __ZZN31ApplePPMCPMSMeasuredPowerHelpernwEmE20kalloc_type_view_918
CStrings:
+ "%s::%s:sendAsbLpemData failed with 0x%x for battery pack=%d, bank=%d\n"
+ "_trailingBudgetFlushTimer"
+ "pushAsbLpemDataOnWake"
```
