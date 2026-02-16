## com.apple.driver.AppleActuatorDriver

> `com.apple.driver.AppleActuatorDriver`

```diff

-9130.2.0.0.0
+9140.1.0.0.0
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x1242
   __TEXT.__os_log: 0x34e
-  __TEXT_EXEC.__text: 0xa75c
+  __TEXT_EXEC.__text: 0x9e3c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xf0

   __DATA_CONST.__const: 0x1880
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: A40971C7-6841-33C3-A3CE-0F3DA529E85F
+  UUID: 5EED1887-B593-38FE-9A96-D50184783F71
   Functions: 214
   Symbols:   0
   CStrings:  159
Functions:
~ sub_fffffe0008f6a288 -> sub_fffffe00086efc08 : 284 -> 248
~ sub_fffffe0008f6a3a4 -> sub_fffffe00086efd00 : 184 -> 172
~ sub_fffffe0008f6a4cc -> sub_fffffe00086efe1c : 136 -> 124
~ sub_fffffe0008f6a864 -> sub_fffffe00086f01a8 : 260 -> 224
~ sub_fffffe0008f6a968 -> sub_fffffe00086f0288 : 252 -> 244
~ sub_fffffe0008f6aa64 -> sub_fffffe00086f037c : 232 -> 220
~ sub_fffffe0008f6ab4c -> sub_fffffe00086f0458 : 216 -> 208
~ sub_fffffe0008f6ac4c -> sub_fffffe00086f0550 : 344 -> 336
~ sub_fffffe0008f6ada4 -> sub_fffffe00086f06a0 : 236 -> 208
~ __ZN19AppleActuatorDevice4initEP12OSDictionary : 188 -> 184
~ __ZN19AppleActuatorDevice5startEP9IOService : 2176 -> 2008
~ __ZN19AppleActuatorDevice27handleInterfaceNotificationEP8OSNumber : 364 -> 340
~ __ZNK19AppleActuatorDevice11getWorkLoopEv : 444 -> 384
~ sub_fffffe0008f6be64 -> sub_fffffe00086f1644 : 532 -> 484
~ sub_fffffe0008f6c078 -> sub_fffffe00086f1828 : 368 -> 340
~ sub_fffffe0008f6c248 -> sub_fffffe00086f19dc : 636 -> 620
~ __ZN19AppleActuatorDevice26_deviceGetReportWithLookUpEP21AADDeviceReportStructh : 752 -> 692
~ sub_fffffe0008f6c904 -> sub_fffffe00086f204c : 636 -> 620
~ __ZN19AppleActuatorDevice26_deviceSetReportWithLookUpEP21AADDeviceReportStructh : 436 -> 412
~ sub_fffffe0008f6cd68 -> sub_fffffe00086f2488 : 668 -> 652
~ __ZN19AppleActuatorDevice11resetDeviceEv : 344 -> 336
~ __ZN19AppleActuatorDevice18registerUserClientEP29AppleActuatorDeviceUserClient : 660 -> 644
~ sub_fffffe0008f6d558 -> sub_fffffe00086f2c50 : 228 -> 212
~ __ZN19AppleActuatorDevice20unregisterUserClientEP29AppleActuatorDeviceUserClient : 660 -> 644
~ sub_fffffe0008f6d904 -> sub_fffffe00086f2fdc : 340 -> 316
~ __ZN19AppleActuatorDevice25addHostClickControlClientEv : 608 -> 592
~ __ZN19AppleActuatorDevice28removeHostClickControlClientEv : 608 -> 592
~ sub_fffffe0008f6e07c -> sub_fffffe00086f371c : 612 -> 596
~ sub_fffffe0008f6e384 -> sub_fffffe00086f3a14 : 404 -> 392
~ sub_fffffe0008f6e574 -> sub_fffffe00086f3bf8 : 396 -> 384
~ __ZN19AppleActuatorDevice22_cacheDevicePropertiesEv : 1720 -> 1508
~ __ZN19AppleActuatorDevice14setPreferencesEP12OSDictionary : 700 -> 588
~ sub_fffffe0008f6f0a8 -> sub_fffffe00086f45dc : 324 -> 316
~ sub_fffffe0008f6f1ec -> sub_fffffe00086f4718 : 340 -> 328
~ sub_fffffe0008f6f3d8 -> sub_fffffe00086f48f8 : 356 -> 344
~ __ZN19AppleActuatorDevice24systemPowerChangeHandlerEPvjP9IOServiceS0_m : 268 -> 260
~ __ZN19AppleActuatorDevice13setPowerStateEmP9IOService : 364 -> 332
~ __ZN19AppleActuatorDevice28_scheduleSetHostClickControlEj : 504 -> 500
~ __ZN19AppleActuatorDevice22powerStateWillChangeToEmmP9IOService : 272 -> 264
~ sub_fffffe0008f6fbc8 -> sub_fffffe00086f50a8 : 272 -> 236
~ sub_fffffe0008f6fcd8 -> sub_fffffe00086f5194 : 112 -> 104
~ sub_fffffe0008f6fdd4 -> sub_fffffe00086f5288 : 196 -> 172
~ sub_fffffe0008f6ff58 -> sub_fffffe00086f53f4 : 128 -> 120
~ sub_fffffe0008f6ffd8 -> sub_fffffe00086f546c : 128 -> 120
~ sub_fffffe0008f703c4 -> sub_fffffe00086f5850 : 368 -> 360
~ __ZN29AppleActuatorDeviceUserClient18issueDriverRequestEP21MTDriverRequestStructP27MTDriverRequestResultStructyPy : 1312 -> 1244
~ sub_fffffe0008f70c20 -> sub_fffffe00086f6060 : 316 -> 308
~ __ZN29AppleActuatorDeviceUserClient14reservedMethodEv : 132 -> 124
~ sub_fffffe0008f70f48 -> sub_fffffe00086f6378 : 96 -> 88
~ __ZN29AppleActuatorDeviceUserClient12initWithTaskEP4taskPvjP12OSDictionary : 560 -> 552
~ __ZN29AppleActuatorDeviceUserClient5startEP9IOService : 384 -> 360
~ sub_fffffe0008f71358 -> sub_fffffe00086f6760 : 108 -> 100
~ sub_fffffe0008f713e4 -> sub_fffffe00086f67e4 : 220 -> 204
~ sub_fffffe0008f714c0 -> sub_fffffe00086f68b0 : 188 -> 168
~ __ZN29AppleActuatorDeviceUserClient24registerNotificationPortEP8ipc_portjj : 224 -> 208
~ __ZN29AppleActuatorDeviceUserClient14createLogQueueEv : 324 -> 296
~ __ZN29AppleActuatorDeviceUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptor : 264 -> 248
~ __ZN29AppleActuatorDeviceUserClient10enqueueLogEPhj : 256 -> 240
~ sub_fffffe0008f71b1c -> sub_fffffe00086f6eac : 176 -> 160
~ sub_fffffe0008f71bcc -> sub_fffffe00086f6f4c : 176 -> 160
~ sub_fffffe0008f71e74 -> sub_fffffe00086f71e4 : 168 -> 156
~ sub_fffffe0008f71f1c -> sub_fffffe00086f7280 : 356 -> 312
~ __ZN27AppleActuatorHIDEventDriver5startEP9IOService : 1244 -> 1088
~ __ZN27AppleActuatorHIDEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypejPv : 264 -> 256
~ __ZN27AppleActuatorHIDEventDriver19BuildActDeviceEntryEP8OSObjectPv : 256 -> 232
~ __ZN27AppleActuatorHIDEventDriver4stopEP9IOService : 164 -> 156
~ __ZN27AppleActuatorHIDEventDriver7messageEjP9IOServicePv : 164 -> 156
~ __ZN27AppleActuatorHIDEventDriver13willTerminateEP9IOServicej : 372 -> 348
~ sub_fffffe0008f72a20 -> sub_fffffe00086f7c74 : 172 -> 164
~ sub_fffffe0008f72acc -> sub_fffffe00086f7d18 : 96 -> 88
~ __ZN27AppleActuatorHIDEventDriver20enableActuatorEventsEb : 160 -> 152
~ __ZN27AppleActuatorHIDEventDriver17getActuatorReportEhPhPjh15IOHIDReportType : 172 -> 152
~ __ZN27AppleActuatorHIDEventDriver22getActuatorReportGatedEPNS_17AAHEDReportStructE : 404 -> 380
~ __ZN27AppleActuatorHIDEventDriver15simpleGetReportEhP24IOBufferMemoryDescriptorPj15IOHIDReportType : 688 -> 632
~ __ZN27AppleActuatorHIDEventDriver17setActuatorReportEhPhjh15IOHIDReportType : 180 -> 160
~ __ZN27AppleActuatorHIDEventDriver22setActuatorReportGatedEPNS_17AAHEDReportStructE : 400 -> 376
~ __ZN27AppleActuatorHIDEventDriver15simpleSetReportEhP24IOBufferMemoryDescriptorj15IOHIDReportType : 608 -> 568
~ __ZN27AppleActuatorHIDEventDriver26getActuatorReportInfoGatedEPhS0_Pj : 520 -> 496
~ __ZN27AppleActuatorHIDEventDriver21newActuatorPropertiesEv : 688 -> 600
~ __ZN27AppleActuatorHIDEventDriver14buildActDeviceEv : 1440 -> 1300
~ sub_fffffe0008f74388 -> sub_fffffe00086f9410 : 140 -> 124
~ __ZN19AppleActuatorDevice27scheduleSetHostClickControlEj : 408 -> 384

```
