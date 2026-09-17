## com.apple.driver.AppleActuatorDriver

> `com.apple.driver.AppleActuatorDriver`

```diff

-10400.44.0.0.0
+10410.1.0.0.0
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x11d7
-  __TEXT.__os_log: 0x320
-  __TEXT_EXEC.__text: 0x977c
+  __TEXT.__cstring: 0x11a5
+  __TEXT.__os_log: 0x4ef
+  __TEXT_EXEC.__text: 0x98c0
   __TEXT_EXEC.__auth_stubs: 0x470
   __DATA.__data: 0xc8
   __DATA.__common: 0xf0

   __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0xa8
   Functions: 254
-  Symbols:   744
-  CStrings:  155
+  Symbols:   748
+  CStrings:  158
 
Symbols:
+ __ZZN19AppleActuatorDevice26_deviceSetReportWithLookUpEP21AADDeviceReportStructhE11_os_log_fmt
+ __ZZN19AppleActuatorDevice26_deviceSetReportWithLookUpEP21AADDeviceReportStructhE11_os_log_fmt_0
+ __ZZN19AppleActuatorDevice26_deviceSetReportWithLookUpEP21AADDeviceReportStructhE11_os_log_fmt_1
+ __ZZN19AppleActuatorDevice26_deviceSetReportWithLookUpEP21AADDeviceReportStructhE11_os_log_fmt_2
+ __ZZN19AppleActuatorDevice27scheduleSetHostClickControlEjE21kalloc_type_view_1452
+ __ZZN19AppleActuatorDevice27scheduleSetHostClickControlEjE21kalloc_type_view_1477
+ __ZZZN19AppleActuatorDevice27scheduleSetHostClickControlEjENK3$_0clEPvS1_E21kalloc_type_view_1472
- __ZZN19AppleActuatorDevice27scheduleSetHostClickControlEjE21kalloc_type_view_1431
- __ZZN19AppleActuatorDevice27scheduleSetHostClickControlEjE21kalloc_type_view_1456
- __ZZZN19AppleActuatorDevice27scheduleSetHostClickControlEjENK3$_0clEPvS1_E21kalloc_type_view_1451
Functions:
~ __ZN19AppleActuatorDevice26_deviceSetReportWithLookUpEP21AADDeviceReportStructh : 416 -> 740
CStrings:
+ "[HID] [%s] [Error] %s::%s [0x%llx] ERROR - Invalid length : Report struct [ID:0x%02x] length [%u] is larger than max buffer size [%zu]\n"
+ "[HID] [%s] [Error] %s::%s [0x%llx] ERROR - OVERRUN: mtReportID 0x%02x has reportLength of %d, attempting to write %d bytes\n"
+ "[HID] [%s] [Error] %s::%s [0x%llx] ERROR - UNDERRUN: mtReportID 0x%02x has reportLength of %d, attempting to write %d bytes\n"
+ "[HID] [%s] [Error] %s::%s [0x%llx] _getFeatureReportInfo returned error 0x%x\n"
- "%s::%s _getFeatureReportInfo returned error 0x%x\n"
```
