## com.apple.driver.ApplePassthroughPPM

> `com.apple.driver.ApplePassthroughPPM`

```diff

-  __TEXT.__const: 0x1150
-  __TEXT.__cstring: 0xf9e1
-  __TEXT.__os_log: 0x3fa4
-  __TEXT_EXEC.__text: 0x5839c
+  __TEXT.__const: 0x1170
+  __TEXT.__cstring: 0xfec8
+  __TEXT.__os_log: 0x4400
+  __TEXT_EXEC.__text: 0x59dd8
   __TEXT_EXEC.__auth_stubs: 0x7b0
   __DATA.__data: 0x160
   __DATA.__common: 0x578
   __DATA.__bss: 0x200
   __DATA_CONST.__mod_init_func: 0xf8
   __DATA_CONST.__mod_term_func: 0xc8
-  __DATA_CONST.__const: 0x9240
-  __DATA_CONST.__kalloc_type: 0xa00
+  __DATA_CONST.__const: 0x92c8
+  __DATA_CONST.__kalloc_type: 0xa40
   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2326
-  Symbols:   3427
-  CStrings:  1870
+  Functions: 2346
+  Symbols:   3457
+  CStrings:  1914
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ _ZN19ApplePassthroughPPM18setBattModelParamsEPK7ParamRC
+ _ZN19ApplePassthroughPPM29createSystemCapabilityMonitorEhh
+ _ZN20ApplePPMBatteryModel30updateRCParamsInMemoryWRdcOnlyEPK7ParamRC
+ _ZN31ApplePPMSystemCapabilityMonitor14initWithParentEP8ApplePPMhh
+ _ZN35ApplePPMCPMSSystemCapabilityMonitor10withParentEP8ApplePPMhh
+ _ZN35ApplePPMCPMSSystemCapabilityMonitor14initWithParentEP8ApplePPMhh
+ _ZN42ApplePassthroughPPMSystemCapabilityMonitor10withParentEP8ApplePPMhh
+ _ZN42ApplePassthroughPPMSystemCapabilityMonitor21setBatteryModelParamsEPK7ParamRC
+ _ZN42ApplePassthroughPPMSystemCapabilityMonitor28startSystemCapabilityMonitorEv
+ _ZN42ApplePassthroughPPMSystemCapabilityMonitor32batteryPackServiceArrivalHandlerEPvP9IOServiceP10IONotifier
+ _ZN8ApplePPM26getSystemCapabilityMonitorEhh
+ __ZN12ApplePPMCPMS29createSystemCapabilityMonitorEhh
+ __ZN19ApplePassthroughPPM18setBattModelParamsEPK7ParamRC
+ __ZN19ApplePassthroughPPM29createSystemCapabilityMonitorEhh
+ __ZN20ApplePPMBatteryModel30updateRCParamsInMemoryWRdcOnlyEPK7ParamRC
+ __ZN23GradientUpdateAlgorithm6updateEffff
+ __ZN31ApplePPMSystemCapabilityMonitor14initWithParentEP8ApplePPMhh
+ __ZN35ApplePPMCPMSSystemCapabilityMonitor10withParentEP8ApplePPMhh
+ __ZN35ApplePPMCPMSSystemCapabilityMonitor14initWithParentEP8ApplePPMhh
+ __ZN42ApplePassthroughPPMSystemCapabilityMonitor10withParentEP8ApplePPMhh
+ __ZN42ApplePassthroughPPMSystemCapabilityMonitor18sendLPEMPropertiesEP12OSDictionary
+ __ZN42ApplePassthroughPPMSystemCapabilityMonitor21setBatteryModelParamsEPK7ParamRC
+ __ZN42ApplePassthroughPPMSystemCapabilityMonitor23readBatteryInputFromASBEv
+ __ZN42ApplePassthroughPPMSystemCapabilityMonitor25batteryModelHandlerHelperEv
+ __ZN42ApplePassthroughPPMSystemCapabilityMonitor28startSystemCapabilityMonitorEv
+ __ZN42ApplePassthroughPPMSystemCapabilityMonitor32batteryPackServiceArrivalHandlerEPvP9IOServiceP10IONotifier
+ __ZN8ApplePPM26getSystemCapabilityMonitorEhh
+ __ZZN19ApplePassthroughPPM18setBattModelParamsEPK7ParamRCE11_os_log_fmt
+ __ZZN19ApplePassthroughPPM18setBattModelParamsEPK7ParamRCE11_os_log_fmt_0
+ __ZZN19ApplePassthroughPPM18setBattModelParamsEPK7ParamRCE11_os_log_fmt_1
+ __ZZN20ApplePPMBatteryModel30updateRCParamsInMemoryWRdcOnlyEPK7ParamRCE11_os_log_fmt
+ __ZZN20ApplePPMBatteryModel30updateRCParamsInMemoryWRdcOnlyEPK7ParamRCE11_os_log_fmt_0
+ __ZZN23ApplePPMBatteryModel4RCnwEmE20kalloc_type_view_390
+ __ZZN31ApplePPMCPMSMeasuredPowerHelperdlEPvmE20kalloc_type_view_917
+ __ZZN31ApplePPMCPMSMeasuredPowerHelpernwEmE20kalloc_type_view_917
+ __ZZN35ApplePPMCPMSSystemCapabilityMonitor14initWithParentEP8ApplePPMhhE11_os_log_fmt
+ __ZZN42ApplePassthroughPPMSystemCapabilityMonitor18sendLPEMPropertiesEP12OSDictionaryE11_os_log_fmt
+ __ZZN42ApplePassthroughPPMSystemCapabilityMonitor18sendLPEMPropertiesEP12OSDictionaryE11_os_log_fmt_0
+ __ZZN42ApplePassthroughPPMSystemCapabilityMonitor21setBatteryModelParamsEPK7ParamRCE11_os_log_fmt
+ __ZZN42ApplePassthroughPPMSystemCapabilityMonitor23readBatteryInputFromASBEvE11_os_log_fmt
+ __ZZN42ApplePassthroughPPMSystemCapabilityMonitor23readBatteryInputFromASBEvE11_os_log_fmt_0
+ __ZZN42ApplePassthroughPPMSystemCapabilityMonitor23readBatteryInputFromASBEvE11_os_log_fmt_1
+ __ZZN42ApplePassthroughPPMSystemCapabilityMonitor23readBatteryInputFromASBEvE11_os_log_fmt_2
+ __ZZN42ApplePassthroughPPMSystemCapabilityMonitor23readBatteryInputFromASBEvE11_os_log_fmt_3
+ __ZZN42ApplePassthroughPPMSystemCapabilityMonitor23readBatteryInputFromASBEvE11_os_log_fmt_4
+ __ZZN42ApplePassthroughPPMSystemCapabilityMonitor23readBatteryInputFromASBEvE11_os_log_fmt_5
+ __ZZN42ApplePassthroughPPMSystemCapabilityMonitor23readBatteryInputFromASBEvE11_os_log_fmt_6
+ __ZZN42ApplePassthroughPPMSystemCapabilityMonitor32batteryPackServiceArrivalHandlerEPvP9IOServiceP10IONotifierE11_os_log_fmt
- _ZN31ApplePPMSystemCapabilityMonitor14initWithParentEP8ApplePPMh
- _ZN35ApplePPMCPMSSystemCapabilityMonitor10withParentEP8ApplePPMh
- _ZN35ApplePPMCPMSSystemCapabilityMonitor14initWithParentEP8ApplePPMh
- _ZN42ApplePassthroughPPMSystemCapabilityMonitor10withParentEP8ApplePPMh
- _ZN8ApplePPM16loadTGraphPacketEv
- _ZN8ApplePPM26getSystemCapabilityMonitorEi
- __ZN12ApplePPMCPMS29createSystemCapabilityMonitorEh
- __ZN19ApplePassthroughPPM29createSystemCapabilityMonitorEh
- __ZN31ApplePPMSystemCapabilityMonitor14initWithParentEP8ApplePPMh
- __ZN35ApplePPMCPMSSystemCapabilityMonitor10withParentEP8ApplePPMh
- __ZN35ApplePPMCPMSSystemCapabilityMonitor14initWithParentEP8ApplePPMh
- __ZN42ApplePassthroughPPMSystemCapabilityMonitor10withParentEP8ApplePPMh
- __ZN8ApplePPM26getSystemCapabilityMonitorEi
- __ZZN23ApplePPMBatteryModel4RCnwEmE20kalloc_type_view_389
- __ZZN31ApplePPMCPMSMeasuredPowerHelperdlEPvmE20kalloc_type_view_916
- __ZZN31ApplePPMCPMSMeasuredPowerHelpernwEmE20kalloc_type_view_916
- __ZZN35ApplePPMCPMSSystemCapabilityMonitor14initWithParentEP8ApplePPMhE11_os_log_fmt
CStrings:
+ "%s::%s:%s: Failed to enqueue and send Pmax telemetry, batteryPackIndex %d\n\n"
+ "%s::%s:%s: createPmaxDictionary returned 0x%x, batteryPackIndex %d\n\n"
+ "%s::%s:%s: ppmDaemonMsg is NULL, batteryPackIndex %d\n\n"
+ "%s::%s:ApplePPMBatteryModel::updateRCParamsInMemoryWRdcOnly: baselineWRdc %f out of range [%f, %f]\n\n"
+ "%s::%s:ApplePPMBatteryModel::updateRCParamsInMemoryWRdcOnly: null params\n\n"
+ "%s::%s:ApplePassthroughPPMSystemCapabilityMonitor::readBatteryInputFromASB: failed to read ChemId (success=%d, chemId=%u)\n\n"
+ "%s::%s:ApplePassthroughPPMSystemCapabilityMonitor::readBatteryInputFromASB: no ASB provider, returning false\n\n"
+ "%s::%s:ApplePassthroughPPMSystemCapabilityMonitor::readBatteryInputFromASB: no battery model, returning false\n\n"
+ "%s::%s:AppleSmartBatteryLPEM arrival success bankId=%u\n\n"
+ "%s::%s:Error: Invalid batteryPackIndex %d (max: %d)\n\n"
+ "%s::%s:Error: data is NULL\n"
+ "%s::%s:Error: failed to get _sysCapMonitorLock\n"
+ "%s::%s:Error: params is NULL\n"
+ "%s::%s:Filtering out data: powerMean (%.3f W) < %.1f W and powerMax (%.3f W) < %.1f W\n\n"
+ "%s::%s:batteryPackIndex=%d, systemCapability[CPMSPPMTimeScale100ms]=%d mW, pmax[%d]=%f W \n\n"
+ "%s::%s:failed to get BatteryData from bank\n"
+ "%s::%s:failed to get LpemMode from LPEM dict\n"
+ "%s::%s:failed to get LpemSoc from LPEM dict\n"
+ "%s::%s:setBattModelParams: failed to find chemID match\n"
+ "%s::%s:setBattModelParams: failed to setBatteryModelParams for pack=%d, bank=%d, ret=0x%x\n"
+ "%s::%s:setBattModelParams: null params\n"
+ "1211111212221212111111111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122222222222222222222222222112222222222222222222222222222221111111111111121"
+ "121222222222222222222222222222222222222222222222222222222212"
+ "1212222222222222222222222222222222222222222222222222222222122222222"
+ "12222112222222222112222222222222222222222222222222222211112222221221121112122111222122222222111"
+ "ApplePPMSystemCapabilityMonitor *ApplePPM::getSystemCapabilityMonitor(uint8_t, uint8_t)"
+ "BankID"
+ "OverrideHFEFastImpedanceMaxDeltaTheta"
+ "OverrideHFEFastImpedanceThetaLowerBound"
+ "OverrideHFEFastImpedanceThetaUpperBound"
+ "OverrideHFESlowImpedanceMaxDeltaTheta"
+ "OverrideHFESlowImpedanceThetaLowerBound"
+ "OverrideHFESlowImpedanceThetaUpperBound"
+ "PPMVector%d"
+ "_numberOfBatteryBanks > 0 && _numberOfBatteryBanks <= MAX_NUMBER_BATTERY_BANKS"
+ "_numberOfBatteryPacks > 0 && _numberOfBatteryPacks < MAX_NUMBER_BATTERY_PACKS"
+ "_sysCapIndex < MAX_NUMBER_BATTERY_PACKS"
+ "bankIdx >= 0 && bankIdx < getNumBatteryBanks()"
+ "batteryPackIndex"
+ "batteryPackIndex < MAX_NUMBER_BATTERY_PACKS"
+ "batteryPackServiceArrivalHandler"
+ "data != nullptr"
+ "data->getCount() == _numBatteryPacks"
+ "hfe-fast-impedance-max-delta"
+ "hfe-fast-impedance-theta-hi"
+ "hfe-fast-impedance-theta-lo"
+ "hfe-slow-impedance-max-delta"
+ "hfe-slow-impedance-theta-hi"
+ "hfe-slow-impedance-theta-lo"
+ "index < _numberOfBatteryPacks"
+ "monitor"
+ "notifier"
+ "number-of-battery-banks"
+ "number-of-battery-packs"
+ "packIdx >= 0 && packIdx < getNumBatteryPacks()"
+ "sendLPEMProperties"
+ "sendLPEMProperties kret=%x\n"
+ "static ApplePPMCPMSSystemCapabilityMonitor *ApplePPMCPMSSystemCapabilityMonitor::withParent(ApplePPM *, uint8_t, uint8_t)"
+ "static ApplePassthroughPPMSystemCapabilityMonitor *ApplePassthroughPPMSystemCapabilityMonitor::withParent(ApplePPM *, uint8_t, uint8_t)"
+ "updateRCParamsInMemoryWRdcOnly"
+ "virtual ApplePPMSystemCapabilityMonitor *ApplePassthroughPPM::createSystemCapabilityMonitor(uint8_t, uint8_t)"
+ "virtual IOReturn ApplePassthroughPPMSystemCapabilityMonitor::setBatteryModelParams(const ParamRC *)"
+ "virtual bool ApplePPMCPMSSystemCapabilityMonitor::initWithParent(ApplePPM *, uint8_t, uint8_t)"
+ "virtual bool ApplePPMSystemCapabilityMonitor::initWithParent(ApplePPM *, uint8_t, uint8_t)"
+ "virtual bool ApplePassthroughPPMSystemCapabilityMonitor::startSystemCapabilityMonitor()"
+ "void ApplePassthroughPPMSystemCapabilityMonitor::batteryPackServiceArrivalHandler(void *, IOService *, IONotifier *)"
- "%s::%s:%s: Failed to enqueue and send Pmax telemetry, batteryIndex %d\n\n"
- "%s::%s:%s: createPmaxDictionary returned 0x%x, batteryIndex %d\n\n"
- "%s::%s:%s: ppmDaemonMsg is NULL, batteryIndex %d\n\n"
- "%s::%s:Error: Invalid batteryIndex %d (max: %d)\n\n"
- "%s::%s:Filtering out data: powerMean (%.3f W) is less than %.1f W\n\n"
- "%s::%s:batteryIndex=%d, systemCapability[CPMSPPMTimeScale100ms]=%d mW, pmax[%d]=%f W \n\n"
- "121111121222121211111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122222222222222222222222222112222222222222222222222222222221111111111111121"
- "121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212"
- "1212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122222222"
- "ApplePPMSystemCapabilityMonitor *ApplePPM::getSystemCapabilityMonitor(int)"
- "BatteryIndex"
- "_numberOfBatteries > 0 && _numberOfBatteries < MAX_NUMBER_BATTERIES"
- "_sysCapIndex < MAX_NUMBER_BATTERIES"
- "batteryIndex < MAX_NUMBER_BATTERIES"
- "data->getCount() == _numBatteries"
- "idx >= 0 && idx < MAX_NUMBER_BATTERIES"
- "index < _numberOfBatteries"
- "number-of-batteries"
- "static ApplePPMCPMSSystemCapabilityMonitor *ApplePPMCPMSSystemCapabilityMonitor::withParent(ApplePPM *, uint8_t)"
- "static ApplePassthroughPPMSystemCapabilityMonitor *ApplePassthroughPPMSystemCapabilityMonitor::withParent(ApplePPM *, uint8_t)"
- "virtual bool ApplePPMCPMSSystemCapabilityMonitor::initWithParent(ApplePPM *, uint8_t)"
- "virtual bool ApplePPMSystemCapabilityMonitor::initWithParent(ApplePPM *, uint8_t)"

```
