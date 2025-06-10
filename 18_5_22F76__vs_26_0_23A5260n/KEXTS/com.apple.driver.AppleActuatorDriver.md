## com.apple.driver.AppleActuatorDriver

> `com.apple.driver.AppleActuatorDriver`

```diff

-8140.4.0.0.0
+9100.23.0.0.0
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x1283
-  __TEXT.__os_log: 0x2f1
-  __TEXT_EXEC.__text: 0xaa98
+  __TEXT.__cstring: 0x1242
+  __TEXT.__os_log: 0x34e
+  __TEXT_EXEC.__text: 0xa75c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xf0
-  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
   __DATA_CONST.__const: 0x1880
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: 621D4B86-79EB-3420-AB17-6CAFFCAD8D7F
+  UUID: D0BBFC35-4A5E-3EB8-9BA2-2588BBD301D8
   Functions: 214
   Symbols:   0
-  CStrings:  164
+  CStrings:  159
 
Functions:
~ sub_fffffff008cc12c4 -> sub_fffffff008e35c94 : 208 -> 232
~ sub_fffffff008cc1394 -> sub_fffffff008e35d7c : 192 -> 216
~ sub_fffffff008cc147c -> sub_fffffff008e35e7c : 276 -> 344
~ sub_fffffff008cc1590 -> sub_fffffff008e35fd4 : 212 -> 236
~ __ZN19AppleActuatorDevice5startEP9IOService : 2180 -> 2176
~ sub_fffffff008cc263c -> sub_fffffff008e37094 : 528 -> 532
~ sub_fffffff008cc284c -> sub_fffffff008e372a8 : 376 -> 368
~ sub_fffffff008cc2a24 -> sub_fffffff008e37478 : 640 -> 636
~ sub_fffffff008cc30e4 -> sub_fffffff008e37b34 : 640 -> 636
~ sub_fffffff008cc354c -> sub_fffffff008e37f98 : 672 -> 668
~ __ZN19AppleActuatorDevice18registerUserClientEP29AppleActuatorDeviceUserClient : 664 -> 660
~ __ZN19AppleActuatorDevice20unregisterUserClientEP29AppleActuatorDeviceUserClient : 664 -> 660
~ __ZN19AppleActuatorDevice25addHostClickControlClientEv : 612 -> 608
~ __ZN19AppleActuatorDevice28removeHostClickControlClientEv : 612 -> 608
~ sub_fffffff008cc4874 -> sub_fffffff008e392ac : 616 -> 612
~ sub_fffffff008cc4b80 -> sub_fffffff008e395b4 : 408 -> 404
~ sub_fffffff008cc4d74 -> sub_fffffff008e397a4 : 400 -> 396
~ __ZN19AppleActuatorDevice22_cacheDevicePropertiesEv : 2732 -> 1720
~ __ZN19AppleActuatorDevice21_sendLogToUserClientsEPhj : 360 -> 356
~ __ZN19AppleActuatorDevice28_scheduleSetHostClickControlEj : 508 -> 504
~ __ZN29AppleActuatorDeviceUserClient28setHostClickControlRequestedEPv : 380 -> 384
~ sub_fffffff008cc7298 -> sub_fffffff008e3b8cc : 92 -> 100
~ __ZN29AppleActuatorDeviceUserClient11clientCloseEv : 112 -> 108
~ sub_fffffff008cc85a0 -> sub_fffffff008e3cbd8 : 52 -> 68
~ __ZN27AppleActuatorHIDEventDriver5startEP9IOService : 1240 -> 1244
~ __ZN27AppleActuatorHIDEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypejPv : 252 -> 264
~ __ZN27AppleActuatorHIDEventDriver13willTerminateEP9IOServicej : 376 -> 372
~ __ZN27AppleActuatorHIDEventDriver15simpleGetReportEhP24IOBufferMemoryDescriptorPj15IOHIDReportType : 680 -> 688
~ __ZN27AppleActuatorHIDEventDriver15simpleSetReportEhP24IOBufferMemoryDescriptorj15IOHIDReportType : 600 -> 608
~ __ZN27AppleActuatorHIDEventDriver26getActuatorReportInfoGatedEPhS0_Pj : 508 -> 520
~ __ZN27AppleActuatorHIDEventDriver14buildActDeviceEv : 1404 -> 1440
~ sub_fffffff008ccaf24 -> sub_fffffff008e3f5b8 : 144 -> 140
~ __ZN27AppleActuatorHIDEventDriver5startEP9IOService.cold.1 : 92 -> 96
CStrings:
+ "[HID] [%s] %s::%s [0x%llx] Entered\n"
+ "[HID] [%s] %s::%s [0x%llx] Successfully started\n"
+ "[HID] [%s] [Error] %s::%s [0x%llx] Could not create new MT handler\n"
+ "[HID] [%s] [Error] %s::%s [0x%llx] Could not initialize properties dictionary\n"
+ "[HID] [%s] [Error] %s::%s [0x%llx] Couldn't attach Actuator handler\n"
+ "[HID] [%s] [Error] %s::%s [0x%llx] Couldn't start Actuator handler\n"
+ "[HID] [%s] [Error] %s::%s [0x%llx] Ignoring interrupt report id = 0x%08x\n"
+ "[HID] [%s] [Error] %s::%s [0x%llx] _hidInterface->open failed\n"
+ "[HID] [%s] [Error] %s::%s [0x%llx] returned 0x%08X\n"
+ "[HID] [%s] [Error] %s::%s [0x%llx] returned 0x%08X for reportID 0x%02X\n"
+ "[HID] [%s] [Error] %s::%s [0x%llx] returned 0x%08X for reportID 0x%02X\n\n"
- "ActuatorLimits"
- "AmplitudeMax"
- "AmplitudeMin"
- "DurationMax"
- "DurationMin"
- "[HID] [%s] %s [0x%llX] Entered\n"
- "[HID] [%s] %s [0x%llX] Successfully started\n"
- "[HID] [%s] [Error] %s::%s Could not create new MT handler\n"
- "[HID] [%s] [Error] %s::%s Could not initialize properties dictionary\n"
- "[HID] [%s] [Error] %s::%s Couldn't attach Actuator handler\n"
- "[HID] [%s] [Error] %s::%s Couldn't start Actuator handler\n"
- "[HID] [%s] [Error] %s::%s Ignoring interrupt report id = 0x%08x\n"
- "[HID] [%s] [Error] %s::%s _hidInterface->open failed\n"
- "[HID] [%s] [Error] %s::%s returned 0x%08X\n"
- "[HID] [%s] [Error] %s::%s returned 0x%08X for reportID 0x%02X\n"
- "[HID] [%s] [Error] %s::%s returned 0x%08X for reportID 0x%02X\n\n"

```
