## com.apple.iokit.IOUSBDeviceFamily

> `com.apple.iokit.IOUSBDeviceFamily`

```diff

-818.100.6.0.0
-  __TEXT.__cstring: 0x29ba
-  __TEXT.__const: 0xa0
-  __TEXT.__os_log: 0x199c
-  __TEXT_EXEC.__text: 0x2a150
+847.0.3.0.0
+  __TEXT.__cstring: 0x2bc0
+  __TEXT.__const: 0x280
+  __TEXT.__os_log: 0x1b09
+  __TEXT_EXEC.__text: 0x2bc18
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x1f0
+  __DATA.__common: 0x218
   __DATA.__bss: 0x28
-  __DATA_CONST.__auth_got: 0x320
+  __DATA_CONST.__auth_got: 0x378
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0x3688
+  __DATA_CONST.__const: 0x3730
   __DATA_CONST.__kalloc_type: 0x6c0
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: 709A19F1-25FB-3951-93B4-4A1D4BA81A3A
-  Functions: 698
+  UUID: CECF10B0-00A1-345C-B4B2-01DA3FA875B8
+  Functions: 718
   Symbols:   0
-  CStrings:  465
+  CStrings:  489
 
CStrings:
+ "\"unexpected power state %ld\" @%s:%d"
+ "%s@%s: %s::%s: \n"
+ "%s@%s: %s::%s: %s -> %s\n"
+ "%s@%s: %s::%s: Got new configuration descriptor from \"%s\"\n"
+ "%s@%s: %s::%s: IOUSBDeviceController::hardwareException: Type: 0x%08x %s"
+ "%s@%s: %s::%s: IOUSBDeviceController::joinPowerPlane\n"
+ "%s@%s: %s::%s: forcing device off USB due to \"%s\"\n"
+ "%s@%s: %s::%s: ignoring kIOUSBDeviceCommandForceOffBusDisable from \"%s\" as we are already off bus\n"
+ "%s@%s: %s::%s: no longer forcing device off USB due to \"%s\"\n"
+ "%s@%s: %s::%s: received kIOUSBDeviceCommandGoOffAndOnBus from \"%s\"\n"
+ "%s@%s: %s::%s: thread_call_t failure\n"
+ "1211111212221212111212212222221221222211212111111121222221222222222222222222222222222222222222222222222222222222222222222112222222222"
+ "enable-acsleep"
+ "hardwareException"
+ "joinPowerPlane"
+ "kPowerStateOff"
+ "kPowerStateOn"
+ "kPowerStateSleep"
+ "kPowerStateSuspended"
+ "kPowerStateUsable"
+ "setPowerStateGated"
+ "stop"
+ "stopThreadCall"
+ "stopThreadCallGated"
+ "usb-device-slp-ddr"
- "\"IOUSBDeviceController::hardwareException: Type: 0x%08x %s\" @%s:%d"
- "%s@%s: %s::%s: cable connected, but device has been explicitly forced off bus\n"
- "%s@%s: %s::%s: forcing device off USB\n"
- "%s@%s: %s::%s: no longer forcing device off USB\n"
- "%s@%s: %s::%s: not connected\n"
- "1211111212221212111212222222122122221121211111112122222122211222222222"

```
