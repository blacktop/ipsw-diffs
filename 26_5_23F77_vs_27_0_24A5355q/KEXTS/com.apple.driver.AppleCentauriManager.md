## com.apple.driver.AppleCentauriManager

> `com.apple.driver.AppleCentauriManager`

```diff

-92.0.0.0.0
-  __TEXT.__cstring: 0x5812
-  __TEXT.__const: 0x190
-  __TEXT_EXEC.__text: 0x19e64
+123.0.0.0.1
+  __TEXT.__cstring: 0x5c00
+  __TEXT.__const: 0x180
+  __TEXT_EXEC.__text: 0x1ac24
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0xf0
-  __DATA.__bss: 0x48
-  __DATA_CONST.__auth_got: 0x368
-  __DATA_CONST.__got: 0xf8
+  __DATA.__bss: 0x50
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
-  __DATA_CONST.__const: 0x1918
+  __DATA_CONST.__const: 0x1980
   __DATA_CONST.__kalloc_type: 0x1c0
-  UUID: 8CB2CA6D-9482-3214-B72C-5394BDA1A1B4
-  Functions: 625
+  __DATA_CONST.__auth_got: 0x368
+  __DATA_CONST.__got: 0xf8
+  UUID: D75DC8F4-822F-314E-8FBC-9DAAC2A45E3F
+  Functions: 641
   Symbols:   0
-  CStrings:  698
+  CStrings:  729
 
CStrings:
+ "\"duration != nullptr\" @%s:%d"
+ "\"fErrorEventActionDict->setObject(forClient->getName(), errorAction)\" @%s:%d"
+ "\"non-built-in client %s on %s; use centauri-builtin-disable=1 boot-arg\" @%s:%d"
+ "\"unexpected link down - no recovery path\" @%s:%d"
+ "\"unexpected link down with error detect - no recovery path\" @%s:%d"
+ "%s::%s: client no longer valid \n"
+ "%s::%s: failed to create OSDictionary for error actions \n"
+ "%s::%s: failed to create OSDictionary for firmware boot durations \n"
+ "%s::%s: ignoring device \n"
+ "%s::%s: kUSBProductString not found \n"
+ "%s::%s: kUSBVendorString not found \n"
+ "%s::%s: location 0x%llx, nibble 0x%x, ignore %u \n"
+ "%s::%s: locationID not found \n"
+ "%s::%s: notify client about prior completion timeout \n"
+ "%s::%s: overwriting pending error notification %s \n"
+ "%s::%s: skipping reenumeration since error recovery is underway (error %s) \n"
+ "%s::%s: start result: %d \n"
+ "12111112122212121111111111111111111111122222222212212121112222111211122222"
+ "Apple"
+ "Client Error Notify: %s\n"
+ "CompletionTimeout"
+ "DextLaunchTimeout"
+ "ErrorDetectGPIO"
+ "ErrorDetectGPIOLinkDown"
+ "Firmware Boot Durations:\n"
+ "FirmwareBootDurations"
+ "LinkDown"
+ "LinkTrainingTimeout"
+ "ManagerStartResult"
+ "WSSCB"
+ "[Fatal]Centauri-PCIeCompletionTimeout"
+ "kUSBProductString"
+ "kUSBVendorString"
+ "locationID"
+ "notifyPendingErrorEvents"
+ "setChipInfo"
+ "setManagerStartResult"
+ "shouldIgnoreDevice"
- "\"!fErrorEventAction\" @%s:%d"
- "\"[%s] Trigger panic for: %s\" @%s:%d"
- "%s::%s: not permitted \n"
- "%s::%s: skipping reenumeration since link training timeout recovery is underway \n"
- "1211111212221212111111111111111111111112222222221221212112222111211122222"
- "registerCentauriManagerErrorHandler"
- "triggerPanic"

```
