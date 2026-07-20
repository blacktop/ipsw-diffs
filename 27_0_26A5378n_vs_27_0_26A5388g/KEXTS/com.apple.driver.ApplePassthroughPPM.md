## com.apple.driver.ApplePassthroughPPM

> `com.apple.driver.ApplePassthroughPPM`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-1191.0.16.0.0
+1191.0.27.0.0
   __TEXT.__const: 0x1170
-  __TEXT.__cstring: 0xfec8
-  __TEXT.__os_log: 0x4400
-  __TEXT_EXEC.__text: 0x59dd8
+  __TEXT.__cstring: 0xff06
+  __TEXT.__os_log: 0x4476
+  __TEXT_EXEC.__text: 0x5a0e0
   __TEXT_EXEC.__auth_stubs: 0x7b0
   __DATA.__data: 0x160
   __DATA.__common: 0x578
   __DATA.__bss: 0x200
   __DATA_CONST.__mod_init_func: 0xf8
   __DATA_CONST.__mod_term_func: 0xc8
-  __DATA_CONST.__const: 0x92c8
+  __DATA_CONST.__const: 0x92e0
   __DATA_CONST.__kalloc_type: 0xa40
   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2346
-  Symbols:   2797
-  CStrings:  1914
+  Functions: 2349
+  Symbols:   2801
+  CStrings:  1917
 
Symbols:
+ __ZN31ApplePPMSystemCapabilityMonitor27getFilteredSystemCapabilityEv
+ __ZN35ApplePPMCPMSSystemCapabilityMonitor27getFilteredSystemCapabilityEv
+ __ZZN18ApplePPMUserClient21batteryIntfGetOCVDataEP22ppmbatteryIntfAPIInReqP24ppmbatteryIntfAPIOutReq1E11_os_log_fmt_7
+ __ZZN18ApplePPMUserClient27batteryIntfGetImpedanceDataEP22ppmbatteryIntfAPIInReqP24ppmbatteryIntfAPIOutReq0E11_os_log_fmt_6
+ __ZZN31ApplePPMCPMSMeasuredPowerHelperdlEPvmE20kalloc_type_view_918
+ __ZZN31ApplePPMCPMSMeasuredPowerHelpernwEmE20kalloc_type_view_918
- __ZZN31ApplePPMCPMSMeasuredPowerHelperdlEPvmE20kalloc_type_view_917
- __ZZN31ApplePPMCPMSMeasuredPowerHelpernwEmE20kalloc_type_view_917
Functions:
+ __ZN35ApplePPMCPMSSystemCapabilityMonitor27getFilteredSystemCapabilityEv
~ __ZN8ApplePPM23PPMInterfaceAPICallBackEP8OSObjectP12OSDictionaryPS3_ : 8 -> 16
~ __ZN12ApplePPMCPMS23PPMInterfaceAPICallBackEP8OSObjectP12OSDictionaryPS3_ : 496 -> 492
~ __ZN12ApplePPMCPMS24takeControlStateSnapshotEb : 2308 -> 2464
~ __ZN12ApplePPMCPMS20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_ : 1632 -> 1756
~ __ZN12ApplePPMCPMS33sendControlStateSnapshotTelemetryEP27CPMSPPMControlStateSnapshot : 2404 -> 2700
~ __ZN18ApplePPMUserClient27batteryIntfGetImpedanceDataEP22ppmbatteryIntfAPIInReqP24ppmbatteryIntfAPIOutReq0 : 1488 -> 1552
~ __ZN18ApplePPMUserClient21batteryIntfGetOCVDataEP22ppmbatteryIntfAPIInReqP24ppmbatteryIntfAPIOutReq1 : 1404 -> 1468
+ __ZN35ApplePPMCPMSSystemCapabilityMonitor27getFilteredSystemCapabilityEv
+ __ZN31ApplePPMSystemCapabilityMonitor27getFilteredSystemCapabilityEv
~ __ZN19ApplePPMARMFunction12callFunctionEPvS0_S0_ : 228 -> 260
CStrings:
+ "%s::%s:Error: PPMInterfaceAPICallBack failed with 0x%08x\n\n"
+ "ApplePPMInterfaceAPIFunction"
+ "SystemCapability%s_Battery%d"
+ "virtual IOReturn ApplePPMCPMS::PPMInterfaceAPICallBack(OSObject *, OSDictionary *, OSDictionary **)"
- "virtual void ApplePPMCPMS::PPMInterfaceAPICallBack(OSObject *, OSDictionary *, OSDictionary **)"
```
