## com.apple.driver.AppleActuatorDriver

> `com.apple.driver.AppleActuatorDriver`

```diff

-10100.44.0.0.0
+10110.3.0.0.0
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x11fc
-  __TEXT.__os_log: 0x34e
-  __TEXT_EXEC.__text: 0x945c
+  __TEXT.__cstring: 0x11ca
+  __TEXT.__os_log: 0x51d
+  __TEXT_EXEC.__text: 0x95a0
   __TEXT_EXEC.__auth_stubs: 0x470
   __DATA.__data: 0xc8
   __DATA.__common: 0xf0

   __DATA_CONST.__got: 0xa8
   Functions: 214
   Symbols:   0
-  CStrings:  157
+  CStrings:  160
 
Functions:
~ __ZN19AppleActuatorDevice26_deviceSetReportWithLookUpEP21AADDeviceReportStructh : 416 -> 740
CStrings:
+ "[HID] [%s] [Error] %s::%s [0x%llx] ERROR - Invalid length : Report struct [ID:0x%02x] length [%u] is larger than max buffer size [%zu]\n"
+ "[HID] [%s] [Error] %s::%s [0x%llx] ERROR - OVERRUN: mtReportID 0x%02x has reportLength of %d, attempting to write %d bytes\n"
+ "[HID] [%s] [Error] %s::%s [0x%llx] ERROR - UNDERRUN: mtReportID 0x%02x has reportLength of %d, attempting to write %d bytes\n"
+ "[HID] [%s] [Error] %s::%s [0x%llx] _getFeatureReportInfo returned error 0x%x\n"
- "%s::%s _getFeatureReportInfo returned error 0x%x\n"
```
