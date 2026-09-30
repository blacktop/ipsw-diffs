## com.apple.driver.AppleIOPADMAStream

> `com.apple.driver.AppleIOPADMAStream`

```diff

-240.2.0.0.0
+300.8.0.0.0
   __TEXT.__const: 0xf9
-  __TEXT.__cstring: 0x3125
-  __TEXT_EXEC.__text: 0x10298
+  __TEXT.__cstring: 0x338d
+  __TEXT_EXEC.__text: 0x10a40
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0xb0

   __DATA_CONST.__const: 0x1228
   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__kalloc_var: 0x50
-  UUID: 97353207-3964-36FE-A9EB-68E9F611D697
-  Functions: 234
+  UUID: 117338CD-71C4-3F03-897B-D8FB7064DA04
+  Functions: 231
   Symbols:   0
-  CStrings:  356
+  CStrings:  367
 
CStrings:
+ "%s::%s@%d: %s: Unexpected error reading IOPDeviceNode property id(%#x), %s(%x)\n"
+ "%s::%s@%d: %s: Unexpected error reading node state: %s(%x)\n"
+ "%s::%s@%d: Unable to get node state while attempting to set active mode = %x: %s(%x)\n"
+ "%s::%s@%d: Unable to get node state while attempting to start device %x(%s%s): %s(%x)\n"
+ "%s::%s@%d: Unable to get node state while attempting to stop device: %s(%x)\n"
+ "%s::%s@%d: Unable to read kCMRegistersOnStateID from iopNode: %s(%#x)\n"
+ "%s::%s@%d: Unable to read kCMStartIOStateID from iopNode: %s(%#x)\n"
+ "%s::%s@%d: Unexpected error getting current value from IOPDeviceNode(%#x), %s(%x)\n"
+ "%s::%s@%d: setConfigSwitch request failed %s(%x)\n"
+ "1211112222"
+ "control-only"
+ "device_type"
+ "getNodeState"
- "\"%s::%s:\" \"%s: Unexpected error reading IOPDeviceNode state id(%#x), %s(%x)\" @%s:%d"
- "121111222"

```
