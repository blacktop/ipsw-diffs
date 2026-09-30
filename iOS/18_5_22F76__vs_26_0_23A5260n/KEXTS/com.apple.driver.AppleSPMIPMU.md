## com.apple.driver.AppleSPMIPMU

> `com.apple.driver.AppleSPMIPMU`

```diff

-1356.100.2.0.0
+1360.0.0.0.0
   __TEXT.__cstring: 0x2584
   __TEXT.__const: 0x26
-  __TEXT_EXEC.__text: 0xc774
+  __TEXT_EXEC.__text: 0xc784
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x320
   __DATA.__common: 0xc0

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf00
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: 95635548-9EA6-394D-B8B5-A26CB5D98DAA
+  UUID: 4EDA282F-018E-3DD7-B584-0F83A4F50DA8
   Functions: 155
   Symbols:   0
   CStrings:  350
Functions:
~ __ZN18AppleDialogSPMIPMU5startEP9IOService : 3552 -> 3544
~ __ZN18AppleDialogSPMIPMU20_handlePEHaltRestartEj : 264 -> 256
~ __ZN18AppleDialogSPMIPMU20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_ : 1228 -> 1224
~ __ZN18AppleDialogSPMIPMU18_readConfigurationEP9IOService : 4196 -> 4204
~ __ZN18AppleDialogSPMIPMU18setDebugPropertiesEPK12OSDictionary : 516 -> 520
~ __ZN18AppleDialogSPMIPMU10_writeRegsEtPht : 320 -> 340
~ __ZN18AppleDialogSPMIPMU9_readRegsEtPht : 320 -> 340
~ __ZN18AppleDialogSPMIPMU6modRegEthh : 424 -> 452
~ sub_fffffff009845fc4 -> sub_fffffff009b5d380 : 288 -> 284
~ __ZN18AppleDialogSPMIPMU21_updateBootPropertiesEb : 2908 -> 2912
~ __ZN18AppleDialogSPMIPMU11_handleSOCDEv : 740 -> 752
~ __ZN18AppleDialogSPMIPMU21_updateFaultRegistersEb : 1544 -> 1540
~ __ZN18AppleDialogSPMIPMU30_updateOff2WakeSourceRegistersEv : 1396 -> 1392
~ __ZN18AppleDialogSPMIPMU14_shutdownGatedEv : 2640 -> 2636
~ sub_fffffff00984a94c -> sub_fffffff009b61d08 : 320 -> 316
~ __ZN21AppleDialogSPMIPMURTC11handleStartEP9IOService : 2124 -> 2128
~ sub_fffffff00984bfe4 -> sub_fffffff009b633a0 : 300 -> 296
~ __ZN21AppleDialogSPMIPMURTC22_handleSMCNotificationEPv : 208 -> 204
~ sub_fffffff00984cee0 -> sub_fffffff009b64294 : 172 -> 168
~ __ZN21AppleDialogSPMIPMURTC20_setClockOffsetTicksEx : 196 -> 192
~ sub_fffffff00984d218 -> sub_fffffff009b645c4 : 100 -> 96
~ sub_fffffff00984d27c -> sub_fffffff009b64624 : 120 -> 116
~ __ZN17PMURTCNVRAMHelper13nvramReadSI64EPx : 760 -> 756
~ sub_fffffff00984d788 -> sub_fffffff009b64b28 : 200 -> 196
~ sub_fffffff00984db5c -> sub_fffffff009b64ef8 : 144 -> 140
~ __ZN21AppleDialogSPMIPMURTC20_readRTCUpcountTicksEv : 976 -> 968
CStrings:
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 18:50:07 May 30 2025\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 18:50:07 May 30 2025\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 18:50:07 May 30 2025\n"
+ "%s::start: %s _pmuNub: %p built 18:50:07 May 30 2025\n"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 20:14:34 Apr 22 2025\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 20:14:34 Apr 22 2025\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 20:14:34 Apr 22 2025\n"
- "%s::start: %s _pmuNub: %p built 20:14:34 Apr 22 2025\n"

```
