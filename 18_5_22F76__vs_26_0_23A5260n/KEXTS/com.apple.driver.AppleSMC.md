## com.apple.driver.AppleSMC

> `com.apple.driver.AppleSMC`

```diff

-728.100.9.0.0
-  __TEXT.__cstring: 0x8892
+752.0.1.0.0
+  __TEXT.__cstring: 0x8fca
   __TEXT.__const: 0x1e4
   __TEXT.__os_log: 0xd26
-  __TEXT_EXEC.__text: 0x2b218
+  __TEXT_EXEC.__text: 0x2c9dc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x4e0
   __DATA.__bss: 0x110
-  __DATA_CONST.__auth_got: 0x558
+  __DATA_CONST.__auth_got: 0x560
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0xc8
   __DATA_CONST.__mod_term_func: 0xb0
-  __DATA_CONST.__const: 0x8dd8
+  __DATA_CONST.__const: 0x8f10
   __DATA_CONST.__kalloc_type: 0x880
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: E460F474-CF4A-39DC-BED9-1FFC2890425F
-  Functions: 957
+  UUID: A67731C9-2C98-3491-A185-92A873FF2024
+  Functions: 993
   Symbols:   0
-  CStrings:  1026
+  CStrings:  1108
 
CStrings:
+ "%s:%d %s() CANNOT SLEEP HERE!!!!\n"
+ "%s:%d _activeKeyCommand=%x _idleKeyCommandCount=%d\n"
+ "121111121222121211211"
+ "19:18:56"
+ "19:18:58"
+ "AppleAOPSMCDriver"
+ "AppleSMCFamily::%s ERROR: smcTryReadKey failed (%s)\n"
+ "Error: Invalid EventBuffer Message size. Expected: %lu, got: %u\n"
+ "IOPMShutdownTime"
+ "MEST dict or key alloc failed\n"
+ "MEST key not present\n"
+ "MEST number alloc failed\n"
+ "May 30 2025"
+ "PanicMedic"
+ "Wake source flags %s: %#x\n"
+ "_waitForIdle"
+ "ap_virtual_slp_ll"
+ "battAuth.unknown"
+ "bool AppleAOPSMC::aopServiceMatched(void *, IOService *, IONotifier *)"
+ "caEvent.NovaFaultCount"
+ "caEvent.unknown"
+ "event_flags-gpio%d"
+ "hid.ButtonEvent"
+ "hid.HidEvLidStateChange"
+ "hid.PMUEvent"
+ "hid.unknown"
+ "pow.AccessoryInfoChange"
+ "pow.AdapterDetailsChange"
+ "pow.ApWakeState"
+ "pow.BatteryStateChange"
+ "pow.ChargerStateChange"
+ "pow.ContractChange"
+ "pow.ExternalPowerChange"
+ "pow.InBandCommsStateChange"
+ "pow.LDCMConnDisEvent"
+ "pow.LDCMEvent"
+ "pow.LDCMVbusEvent"
+ "pow.OverCurrentEvent"
+ "pow.PortStatusChangeEvent"
+ "pow.SharedDeviceDetected"
+ "pow.USBCPDStateChange"
+ "pow.WirelessFW"
+ "pow.WirelessLogsAvailable"
+ "pow.unknown"
+ "smc.%s(0x%02x%02x%02x%02x)"
+ "smcTryGetKeyCount"
+ "sysCtl.ReqOSReboot"
+ "sysCtl.ReqOSShutdown"
+ "sysCtl.ReqOSSleep"
+ "sysCtl.unknown"
+ "sysState.APAwake"
+ "sysState.APNVRAMStatus"
+ "sysState.APPanic"
+ "sysState.APSleep"
+ "sysState.AudioPlayback"
+ "sysState.BootRomReady"
+ "sysState.BootStatus"
+ "sysState.ClearForceDFU"
+ "sysState.DisplayState"
+ "sysState.LidStateChange"
+ "sysState.MacOSPanic"
+ "sysState.NVRAMRequest"
+ "sysState.PCIeReady"
+ "sysState.PERSTLChange"
+ "sysState.PltRstLChange"
+ "sysState.PrepareForS0"
+ "sysState.PwrBtnShutdownWarn"
+ "sysState.QuiesceComplete"
+ "sysState.QuiesceDevices"
+ "sysState.RTCAlarmChange"
+ "sysState.ResumeComplete"
+ "sysState.ResumeDevices"
+ "sysState.SMCPanicDone"
+ "sysState.SMCPanicProgress"
+ "sysState.ShutdownOS"
+ "sysState.ShutdownSystem"
+ "sysState.SystemPowerState"
+ "sysState.SystemRestart"
+ "sysState.SystemShutdown"
+ "sysState.SystemState"
+ "sysState.TimeChange"
+ "sysState.USB2PlugEvent"
+ "sysState.USB2WakeEvent"
+ "sysState.USBPlugEvent"
+ "sysState.UsbDebugRouteChange"
+ "sysState.Wake"
+ "sysState.WakeSystem"
+ "sysState.unknown"
+ "thermEvent.unknown"
- "12111112122212121211"
- "20:29:19"
- "20:29:21"
- "Apr 22 2025"
- "Error: Invalid EventBuffer Message size\n"
- "smc.%02x%02x%02x%02x"
- "virtual bool AppleAOPSMC::start(IOService *)"

```
