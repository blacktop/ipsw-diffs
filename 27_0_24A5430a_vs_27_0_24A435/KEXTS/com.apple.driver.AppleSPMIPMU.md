## com.apple.driver.AppleSPMIPMU

> `com.apple.driver.AppleSPMIPMU`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

 1372.0.3.0.0
   __TEXT.__const: 0x16
   __TEXT.__cstring: 0x2bf8
-  __TEXT_EXEC.__text: 0xcb7c
+  __TEXT_EXEC.__text: 0xcd88
   __TEXT_EXEC.__auth_stubs: 0x4d0
   __DATA.__data: 0x320
   __DATA.__common: 0xe8
Functions:
~ sub_fffffe000960e920 -> sub_fffffe0009693590 : 72 -> 76
~ sub_fffffe000960e970 -> sub_fffffe00096935e4 : 124 -> 128
~ sub_fffffe000960ea04 -> sub_fffffe000969367c : 68 -> 72
~ sub_fffffe000960ea70 -> sub_fffffe00096936ec : 72 -> 76
~ sub_fffffe000960eab8 -> sub_fffffe0009693738 : 52 -> 56
~ sub_fffffe000960eb08 -> sub_fffffe000969378c : 160 -> 164
~ __ZN18AppleDialogSPMIPMU5startEP9IOService : 3512 -> 3516
~ __ZN18AppleDialogSPMIPMU25_initUpsiFailureInjectionEv : 240 -> 244
~ __ZN18AppleDialogSPMIPMU16_interruptActionEP22IOInterruptEventSourcei : 192 -> 196
~ sub_fffffe000960fb10 -> sub_fffffe00096947a4 : 204 -> 208
~ sub_fffffe000960fbdc -> sub_fffffe0009694874 : 1008 -> 1012
~ __ZN18AppleDialogSPMIPMU23_resetLpemInRestoreModeEv : 368 -> 372
~ __ZN18AppleDialogSPMIPMU26_checkUpsiFailureInjectionEh : 188 -> 192
~ __ZN18AppleDialogSPMIPMU20_handlePEHaltRestartEj : 248 -> 252
~ sub_fffffe00096102f0 -> sub_fffffe0009694f98 : 480 -> 484
~ sub_fffffe00096104d0 -> sub_fffffe000969517c : 112 -> 116
~ __ZN18AppleDialogSPMIPMU15updatePMSettingEhh : 356 -> 360
~ sub_fffffe00096106a4 -> sub_fffffe0009695358 : 204 -> 208
~ __ZN18AppleDialogSPMIPMU18registerPMCallbackEv : 352 -> 356
~ __ZN18AppleDialogSPMIPMU20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_ : 1156 -> 1160
~ sub_fffffe0009610dc0 -> sub_fffffe0009695a80 : 88 -> 92
~ sub_fffffe0009610e18 -> sub_fffffe0009695adc : 204 -> 208
~ __ZN18AppleDialogSPMIPMU18_readConfigurationEP9IOService : 3412 -> 3416
~ sub_fffffe0009611d80 -> sub_fffffe0009696a4c : 140 -> 144
~ __ZN18AppleDialogSPMIPMU17copyDebugPropertyEPKc : 296 -> 300
~ __ZN18AppleDialogSPMIPMU18setDebugPropertiesEPK12OSDictionary : 472 -> 476
~ __ZN18AppleDialogSPMIPMU16_handleSpmiErrorEij : 296 -> 300
~ __ZN18AppleDialogSPMIPMU10_writeRegsEtPht : 312 -> 316
~ __ZN18AppleDialogSPMIPMU9_readRegsEtPht : 312 -> 316
~ __ZN18AppleDialogSPMIPMU6modRegEthh : 408 -> 412
~ __ZN18AppleDialogSPMIPMU9_writeMemEbtPht : 604 -> 608
~ __ZN18AppleDialogSPMIPMU8_readMemEbtPht : 604 -> 608
~ sub_fffffe0009612af4 -> sub_fffffe00096977e4 : 208 -> 212
~ sub_fffffe0009612bc4 -> sub_fffffe00096978b8 : 152 -> 156
~ sub_fffffe0009612c5c -> sub_fffffe0009697954 : 284 -> 288
~ __ZN18AppleDialogSPMIPMU12_readBootKeyEhPhh : 208 -> 212
~ __ZN18AppleDialogSPMIPMU13_writeBootKeyEhPhh : 208 -> 212
~ __ZN18AppleDialogSPMIPMU13_readFaultLogEPhhb : 488 -> 492
~ __ZN18AppleDialogSPMIPMU19_readOff2WakeSourceEPhhb : 268 -> 272
~ __ZN18AppleDialogSPMIPMU13setPropertiesEP8OSObject : 4148 -> 4152
~ __ZN18AppleDialogSPMIPMU13_setLpemStateEhhhhhhh : 420 -> 424
~ __ZN18AppleDialogSPMIPMU21_setLpemBluetoothFWOKEh : 360 -> 364
~ __ZN18AppleDialogSPMIPMU21_updateBootPropertiesEb : 2148 -> 2152
~ __ZN18AppleDialogSPMIPMU13_getLpemStateEPhS0_S0_ : 192 -> 196
~ _panic : 276 -> 280
~ sub_fffffe0009615078 -> sub_fffffe0009699d9c : 772 -> 776
~ __ZN18AppleDialogSPMIPMU21_populateSOCDPropertyEv : 460 -> 464
~ __ZN18AppleDialogSPMIPMU17_writeLpemLogDataEv : 488 -> 492
~ sub_fffffe0009615730 -> sub_fffffe000969a460 : 132 -> 136
~ __ZN18AppleDialogSPMIPMU21_updateFaultRegistersEb : 1276 -> 1280
~ __ZN18AppleDialogSPMIPMU30_updateOff2WakeSourceRegistersEv : 1176 -> 1180
~ sub_fffffe0009616148 -> sub_fffffe000969ae84 : 80 -> 84
~ __ZN18AppleDialogSPMIPMU14_shutdownGatedEv : 2404 -> 2408
~ sub_fffffe0009616b08 -> sub_fffffe000969b84c : 308 -> 312
~ __ZN18AppleDialogSPMIPMU14_enterTestModeEv : 148 -> 152
~ __ZN18AppleDialogSPMIPMU13_exitTestModeEv : 148 -> 152
~ sub_fffffe0009616dbc -> sub_fffffe000969bb0c : 72 -> 76
~ sub_fffffe0009616e0c -> sub_fffffe000969bb60 : 52 -> 56
~ sub_fffffe0009616e40 -> sub_fffffe000969bb98 : 52 -> 56
~ sub_fffffe0009616e84 -> sub_fffffe000969bbe0 : 68 -> 72
~ sub_fffffe0009616ef0 -> sub_fffffe000969bc50 : 72 -> 76
~ sub_fffffe0009616f38 -> sub_fffffe000969bc9c : 104 -> 108
~ sub_fffffe0009616fa0 -> sub_fffffe000969bd08 : 88 -> 92
~ __ZN26AppleDialogSPMIPMUFunction12callFunctionEPvS0_S0_ : 484 -> 488
~ __ZN26AppleDialogSPMIPMUFunction27initWithTargetDataAndSymbolEP9IOServicePK6OSDataPK8OSSymbol : 236 -> 240
~ __GLOBAL__sub_I_AppleDialogSPMIPMU.cpp : 360 -> 364
~ sub_fffffe0009617458 -> sub_fffffe000969c1d0 : 56 -> 60
~ _IOLog : 316 -> 320
~ __ZN22AppleDialogSPMIPMUSOCD12readAndClearEP6OSDataRtS2_tPPh : 456 -> 460
~ sub_fffffe00096177c4 -> sub_fffffe000969c548 : 336 -> 340
~ sub_fffffe0009617924 -> sub_fffffe000969c6ac : 188 -> 192
~ __ZN22AppleDialogSPMIPMUSOCD19readContainerDataV0EP6OSDataRtS2_ : 292 -> 296
~ __ZN22AppleDialogSPMIPMUSOCD19readContainerDataV1EP6OSDataRtS2_ : 284 -> 288
~ __ZN22AppleDialogSPMIPMUSOCD17getSOCDContainersEP7OSArray : 484 -> 488
~ sub_fffffe0009617e54 -> sub_fffffe000969cbec : 72 -> 76
~ sub_fffffe0009617ea4 -> sub_fffffe000969cc40 : 56 -> 60
~ sub_fffffe0009617edc -> sub_fffffe000969cc7c : 56 -> 60
~ sub_fffffe0009617f24 -> sub_fffffe000969ccc8 : 68 -> 72
~ sub_fffffe0009617f90 -> sub_fffffe000969cd38 : 72 -> 76
~ sub_fffffe0009617fd8 -> sub_fffffe000969cd84 : 108 -> 112
~ sub_fffffe0009618058 -> sub_fffffe000969ce08 : 92 -> 96
~ sub_fffffe00096180b4 -> sub_fffffe000969ce68 : 92 -> 96
~ __ZN21AppleDialogSPMIPMURTC11handleStartEP9IOService : 1952 -> 1956
~ sub_fffffe00096188b0 -> sub_fffffe000969d66c : 108 -> 112
~ sub_fffffe000961891c -> sub_fffffe000969d6dc : 368 -> 372
~ sub_fffffe0009618a8c -> sub_fffffe000969d850 : 288 -> 292
~ sub_fffffe0009618bac -> sub_fffffe000969d974 : 420 -> 424
~ __ZN21AppleDialogSPMIPMURTC22_handleSMCNotificationEPv : 196 -> 200
~ __ZN21AppleDialogSPMIPMURTC25_sysctlNVRAMOffsetHandlerEP10sysctl_oidPviP10sysctl_req : 324 -> 328
~ __ZN21AppleDialogSPMIPMURTC18_readConfigurationEP9IOService : 1496 -> 1500
~ __ZN21AppleDialogSPMIPMURTC23_readCurrentOffsetTicksEPx : 492 -> 496
~ sub_fffffe0009619738 -> sub_fffffe000969e514 : 284 -> 288
~ sub_fffffe0009619854 -> sub_fffffe000969e634 : 168 -> 172
~ __ZN17PMURTCNVRAMHelper14nvramWriteSI64Exb : 356 -> 360
~ __ZN21AppleDialogSPMIPMURTC20_setClockOffsetTicksEx : 184 -> 188
~ sub_fffffe0009619b50 -> sub_fffffe000969e93c : 88 -> 92
~ sub_fffffe0009619ba8 -> sub_fffffe000969e998 : 108 -> 112
~ sub_fffffe0009619cb0 -> sub_fffffe000969eaa4 : 152 -> 156
~ __ZN17PMURTCNVRAMHelper13nvramReadSI64EPx : 620 -> 624
~ sub_fffffe0009619fb4 -> sub_fffffe000969edb0 : 180 -> 184
~ sub_fffffe000961a068 -> sub_fffffe000969ee68 : 120 -> 124
~ __ZN21AppleDialogSPMIPMURTC15programRTCAlarmEj : 612 -> 616
~ sub_fffffe000961a344 -> sub_fffffe000969f14c : 132 -> 136
~ sub_fffffe000961a3e0 -> sub_fffffe000969f1ec : 60 -> 64
~ __ZN21AppleDialogSPMIPMURTC20_readRTCUpcountTicksEv : 836 -> 840
~ __ZN21AppleDialogSPMIPMURTC20scheduleRTCWakeAlarmEb : 416 -> 420
~ __ZN21AppleDialogSPMIPMURTC20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_ : 228 -> 232
~ sub_fffffe000961a9e4 -> sub_fffffe000969f800 : 128 -> 132
~ sub_fffffe000961aa6c -> sub_fffffe000969f88c : 116 -> 120
~ sub_fffffe000961aae0 -> sub_fffffe000969f904 : 80 -> 84
~ sub_fffffe000961ab40 -> sub_fffffe000969f968 : 72 -> 76
~ sub_fffffe000961ab90 -> sub_fffffe000969f9bc : 52 -> 56
~ sub_fffffe000961abc4 -> sub_fffffe000969f9f4 : 52 -> 56
~ sub_fffffe000961ac08 -> sub_fffffe000969fa3c : 68 -> 72
~ sub_fffffe000961ac74 -> sub_fffffe000969faac : 72 -> 76
~ sub_fffffe000961acbc -> sub_fffffe000969faf8 : 104 -> 108
~ sub_fffffe000961ad38 -> sub_fffffe000969fb78 : 88 -> 92
~ sub_fffffe000961ad90 -> sub_fffffe000969fbd4 : 88 -> 92
~ sub_fffffe000961ade8 -> sub_fffffe000969fc30 : 172 -> 176
~ sub_fffffe000961ae94 -> sub_fffffe000969fce0 : 128 -> 132
~ sub_fffffe000961af14 -> sub_fffffe000969fd64 : 200 -> 204
~ sub_fffffe000961afdc -> sub_fffffe000969fe30 : 200 -> 204
~ sub_fffffe000961b0ac -> sub_fffffe000969ff04 : 80 -> 84
~ __ZN18AppleDialogSPMIPMU20_handlePEHaltRestartEj.cold.1 : 116 -> 120
~ __ZN18AppleDialogSPMIPMU20_handlePEHaltRestartEj.cold.2 : 188 -> 192
~ __ZN18AppleDialogSPMIPMU28_updateLpemLogDataPropertiesEPh.cold.1 : 44 -> 48
~ __ZN18AppleDialogSPMIPMU14_shutdownGatedEv.cold.1 : 44 -> 48
~ __ZN18AppleDialogSPMIPMU14_shutdownGatedEv.cold.2 : 44 -> 48
~ __ZN18AppleDialogSPMIPMU14_shutdownGatedEv.cold.3 : 204 -> 208
~ __ZN21AppleDialogSPMIPMURTC18getCurrentDateTimeEP11RTCDateTime : 44 -> 48
~ __ZN21AppleDialogSPMIPMURTC18setCurrentDateTimeEPK11RTCDateTime : 44 -> 48
CStrings:
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 21:25:33 Aug 13 2026\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 21:25:33 Aug 13 2026\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 21:25:33 Aug 13 2026\n"
+ "%s::start: %s _pmuNub: %p built 21:25:33 Aug 13 2026\n"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 22:11:26 Aug 13 2026\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 22:11:26 Aug 13 2026\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 22:11:27 Aug 13 2026\n"
- "%s::start: %s _pmuNub: %p built 22:11:27 Aug 13 2026\n"
```
