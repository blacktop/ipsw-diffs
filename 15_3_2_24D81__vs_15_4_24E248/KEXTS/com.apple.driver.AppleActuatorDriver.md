## com.apple.driver.AppleActuatorDriver

> `com.apple.driver.AppleActuatorDriver`

```diff

-8420.1.0.0.0
+8440.1.0.0.0
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x125e
   __TEXT.__os_log: 0x2c3
-  __TEXT_EXEC.__text: 0xac1c
+  __TEXT_EXEC.__text: 0xad8c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xf0

   __DATA_CONST.__const: 0x2840
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: 7DCD1435-B29A-36AA-9DE3-C3AC5C78C281
-  Functions: 253
-  Symbols:   749
+  UUID: 40E7D37F-C592-3F42-9D65-BC0A880A4427
+  Functions: 254
+  Symbols:   750
   CStrings:  162
 
Symbols:
+ _ZN27AppleActuatorHIDEventDriver5startEP9IOService.cold.1
Functions:
~ __ZN29HIDMTQueueEventSourceWorkItem4initEPFvP8OSObjectPvS2_S2_S2_ES1_S2_S2_S2_S2_ : 180 -> 184
~ __ZN29HIDMTQueueEventSourceWorkItem4freeEv : 132 -> 136
~ __ZN21HIDMTQueueEventSource4initEP8OSObjectPFvS1_S1_Ejb : 248 -> 252
~ __ZN21HIDMTQueueEventSource4freeEv : 204 -> 208
~ __ZN21HIDMTQueueEventSource12checkForWorkEv : 192 -> 212
~ __ZN19AppleActuatorDevice5startEP9IOService : 2180 -> 2188
~ __ZNK19AppleActuatorDevice11getWorkLoopEv : 432 -> 452
~ __ZN19AppleActuatorDevice4stopEP9IOService : 548 -> 552
~ __ZN19AppleActuatorDevice4freeEv : 372 -> 376
~ __ZN19AppleActuatorDevice21_getFeatureReportInfoEhPhPth : 276 -> 284
~ __ZN19AppleActuatorDevice21_unregisterUserClientEP29AppleActuatorDeviceUserClient : 344 -> 348
~ __ZN19AppleActuatorDevice14setPreferencesEP12OSDictionary : 688 -> 708
~ __ZN19AppleActuatorDevice15driverLogStringEP8OSObjectPKcz : 300 -> 324
~ __ZN19AppleActuatorDevice20driverLogTransactionEP8OSObjectPhtS2_t : 324 -> 340
~ __ZN19AppleActuatorDevice21_sendLogToUserClientsEPhj : 372 -> 376
- __ZN19AppleActuatorDevice27scheduleSetHostClickControlEj
~ __ZZN19AppleActuatorDevice27scheduleSetHostClickControlEjEN3$_08__invokeEPvS1_ : 252 -> 272
~ __ZN29AppleActuatorDeviceUserClient14reservedMethodEv : 124 -> 132
~ __ZN29AppleActuatorDeviceUserClient17recachePropertiesEv : 88 -> 96
~ __ZN29AppleActuatorDeviceUserClient11clientCloseEv : 108 -> 112
~ __ZN29AppleActuatorDeviceUserClient4freeEv : 184 -> 188
~ __ZN29AppleActuatorDeviceUserClient26getTargetAndMethodForIndexEPP9IOServicej : 48 -> 68
~ __ZN27AppleActuatorHIDEventDriver4freeEv : 360 -> 364
~ __ZN27AppleActuatorHIDEventDriver5startEP9IOService : 1324 -> 1272
~ __ZN27AppleActuatorHIDEventDriver13willTerminateEP9IOServicej : 372 -> 376
~ __ZN27AppleActuatorHIDEventDriver17getActuatorReportEhPhPjh15IOHIDReportType : 136 -> 172
~ __ZN27AppleActuatorHIDEventDriver17setActuatorReportEhPhjh15IOHIDReportType : 144 -> 180
~ __ZN27AppleActuatorHIDEventDriver22setActuatorReportGatedEPNS_17AAHEDReportStructE : 412 -> 400
~ __ZN27AppleActuatorHIDEventDriver14buildActDeviceEv : 1368 -> 1412
~ __ZN27AppleActuatorHIDEventDriver15closeReportGateEv : 140 -> 144

```
