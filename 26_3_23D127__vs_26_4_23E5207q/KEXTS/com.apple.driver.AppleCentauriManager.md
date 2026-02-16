## com.apple.driver.AppleCentauriManager

> `com.apple.driver.AppleCentauriManager`

```diff

-70.1.0.0.0
-  __TEXT.__cstring: 0x5282
-  __TEXT.__const: 0x1b0
-  __TEXT_EXEC.__text: 0x1b648
+89.0.0.0.0
+  __TEXT.__cstring: 0x5812
+  __TEXT.__const: 0x190
+  __TEXT_EXEC.__text: 0x19e64
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
-  __DATA.__common: 0xc0
-  __DATA_CONST.__auth_got: 0x360
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__mod_init_func: 0x20
-  __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x1310
-  __DATA_CONST.__kalloc_type: 0x180
-  UUID: D8911D0C-C5C3-3BB5-AEED-46F32D19A0D3
-  Functions: 531
+  __DATA.__common: 0xf0
+  __DATA.__bss: 0x48
+  __DATA_CONST.__auth_got: 0x368
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__mod_init_func: 0x28
+  __DATA_CONST.__mod_term_func: 0x28
+  __DATA_CONST.__const: 0x1918
+  __DATA_CONST.__kalloc_type: 0x1c0
+  UUID: 40F1254D-3DB1-3745-AD30-EF589780A411
+  Functions: 625
   Symbols:   0
-  CStrings:  659
+  CStrings:  698
 
CStrings:
+ "\"(*outMetadata)->setObject(kAppleCentauriManagerDextRelaunchProperty, relaunchReason)\" @%s:%d"
+ "\"(*outMetadata)->setObject(kAppleCentauriManagerSACFunctionProperty, fSlowAdaptiveClockingFunction ? kOSBooleanTrue : kOSBooleanFalse)\" @%s:%d"
+ "\"*outMetadata\" @%s:%d"
+ "\"Power %s request without FTDI USB wire connected\" @%s:%d"
+ "\"bridgeEntry->getProperty(\\\"manual-enable-defer-scan\\\")\" @%s:%d"
+ "\"fMaxClients && fMaxClients <= kCentauriMaxClients\" @%s:%d"
+ "\"fMaxClients > 1\" @%s:%d"
+ "\"i < kCentauriMaxClients\" @%s:%d"
+ "\"numClientsObj != nullptr\" @%s:%d"
+ "\"propData[propLen - 1] == '\\\\0'\" @%s:%d"
+ "\"propLen && propData\" @%s:%d"
+ "%s::%s: AppleCentauriManagerHelper %s started, ret = %x \n"
+ "%s::%s: Instantiating... centauri-module-factory-env %u \n"
+ "%s::%s: bridge matching unsupported without centauri-module-factory-env boot-arg \n"
+ "%s::%s: buffer filled, totalBytesPrinted: %u bufferSize: %u \n"
+ "%s::%s: error filling buffer, bytesPrinted: %d kLineLength: %u \n"
+ "%s::%s: failed to copy collection \n"
+ "%s::%s: failed to create iterator \n"
+ "%s::%s: failed to enable port hardware (ret=0x%x) \n"
+ "%s::%s: failed to find bridge device tree entry \n"
+ "%s::%s: failed to power on chip (ret=0x%x) \n"
+ "%s::%s: found unexpected key \n"
+ "%s::%s: found unexpected key type \n"
+ "%s::%s: incorrect property type \n"
+ "%s::%s: invalid bridge handle property \n"
+ "%s::%s: lost instantiating race, failing probe \n"
+ "%s::%s: platform supports deferred root port scan \n"
+ "%s::%s: port control function doesn't exist \n"
+ "%s::%s: previously instantiated, failing probe \n"
+ "%s::%s: unexpected key \n"
+ "%s::%s: wakeOnROM: %d \n"
+ "/Library/Caches/com.apple.xbs/A4EAEE90-304C-4D34-B9C5-F8057A947C0D/TemporaryDirectory.Q0Koe1/Sources/AppleCentauri_kexts/AppleCentauriManager/AppleCentauriManagerLogger.cpp"
+ "12111112122212121"
+ "1211111212221212111111111111111111111112222222221221212112222111211122222"
+ "AppleCentauriManagerHelper"
+ "AppleCentauriManagerHelper.cpp"
+ "Client Array Count: %u\n"
+ "FirmwareBootArgs"
+ "FusingConfig"
+ "ModuleVendor"
+ "NumClients"
+ "PowerTableVersions"
+ "Wake On ROM: %s\n"
+ "centauri-module-factory-env"
+ "handleOSDictionaryProperty"
+ "handleOSStringProperty"
+ "handleOSStringPropertyForCentauriNode"
+ "handleTimestampsProperty"
+ "manual-enable-defer-scan"
+ "pci-bridge"
+ "pci-bridge-handle"
+ "setWakeOnROM"
+ "site.AppleCentauriManagerHelper"
- "\"(*metadata)->setObject(kAppleCentauriManagerDextRelaunchProperty, relaunchReason)\" @%s:%d"
- "\"(*metadata)->setObject(kAppleCentauriManagerSACFunctionProperty, fSlowAdaptiveClockingFunction ? kOSBooleanTrue : kOSBooleanFalse)\" @%s:%d"
- "\"*metadata\" @%s:%d"
- "%s::%s: AppleCentauriManager already exists; fail probe \n"
- "%s::%s: error filling buffer, bytesPrinted: %d totalBytesPrinted: %u bufferSize: %u \n"
- "%s::%s: incorrect boot timestamp property type \n"
- "%s::%s: set property failed \n"
- "%s::%s: unexpected property received \n"
- "/Library/Caches/com.apple.xbs/Sources/AppleCentauri_kexts/AppleCentauriManager/AppleCentauriManagerLogger.cpp"
- "121111121222121211111111111111111111111222222222122121211222111211122222"
- "Client Array Count: %d\n"
- "RequireClient"
- "removeRequireClientProperty"
- "setRequireClientProperty"

```
