## com.apple.driver.AppleSPIMC

> `com.apple.driver.AppleSPIMC`

```diff

 39.0.0.0.1
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x1777
-  __TEXT_EXEC.__text: 0x7040
+  __TEXT_EXEC.__text: 0x71a4
   __TEXT_EXEC.__auth_stubs: 0x250
   __DATA.__data: 0xc4
   __DATA.__common: 0x68
Functions:
~ sub_fffffe00095fbfa0 -> sub_fffffe00096808d0 : 72 -> 76
~ sub_fffffe00095fbff0 -> sub_fffffe0009680924 : 52 -> 56
~ sub_fffffe00095fc024 -> sub_fffffe000968095c : 52 -> 56
~ sub_fffffe00095fc068 -> sub_fffffe00096809a4 : 68 -> 72
~ sub_fffffe00095fc0d4 -> sub_fffffe0009680a14 : 72 -> 76
~ sub_fffffe00095fc11c -> sub_fffffe0009680a60 : 104 -> 108
~ sub_fffffe00095fc198 -> sub_fffffe0009680ae0 : 88 -> 92
~ sub_fffffe00095fc1f0 -> sub_fffffe0009680b3c : 88 -> 92
~ __ZN20AppleSPIMCController5startEP9IOService : 2664 -> 2668
~ sub_fffffe00095fccb0 -> sub_fffffe0009681604 : 136 -> 140
~ __ZN20AppleSPIMCController22_powerOffTimerCallbackEP18IOTimerEventSource : 200 -> 204
~ sub_fffffe00095fce68 -> sub_fffffe00096817c4 : 320 -> 324
~ sub_fffffe00095fcfa8 -> sub_fffffe0009681908 : 112 -> 116
~ __ZN20AppleSPIMCController22setSPIControllerActiveEb : 1200 -> 1204
~ sub_fffffe00095fd4c8 -> sub_fffffe0009681e30 : 300 -> 304
~ __ZN20AppleSPIMCController14validSPIConfigEP17AppleARMSPIConfig : 256 -> 260
~ __ZN20AppleSPIMCController17executeSPICommandEP18AppleARMSPICommand : 524 -> 528
~ sub_fffffe00095fda10 -> sub_fffffe0009682384 : 132 -> 136
~ __ZN20AppleSPIMCController23_configureHardwareDelayEv : 1208 -> 1212
~ __ZN20AppleSPIMCController21_executeSPICommandDMAEP18AppleARMSPICommand : 2380 -> 2384
~ sub_fffffe00095fe898 -> sub_fffffe0009683218 : 84 -> 88
~ sub_fffffe00095fe8ec -> sub_fffffe0009683270 : 140 -> 144
~ __ZN20AppleSPIMCController21_executeSPICommandPIOEP18AppleARMSPICommand : 3976 -> 3980
~ __ZN20AppleSPIMCController9_dmaAbortEP18AppleARMSPICommandiPKcS3_ : 428 -> 432
~ __ZN20AppleSPIMCController8_dmaStopEP16IODMAEventSourcePjyPKc : 528 -> 532
~ __ZN20AppleSPIMCController15_dmaEventActionEP16IODMAEventSourceP12IODMACommandiy : 716 -> 720
~ __ZN20AppleSPIMCController20_interruptActionSubrEv : 732 -> 736
~ sub_fffffe0009600480 -> sub_fffffe0009684e1c : 404 -> 408
~ sub_fffffe0009600614 -> sub_fffffe0009684fb4 : 308 -> 312
~ __ZN20AppleSPIMCController14_interruptPollEj : 576 -> 580
~ sub_fffffe0009600bb4 -> sub_fffffe000968555c : 164 -> 168
~ __ZN20AppleSPIMCController18_enableDeviceClockEb : 320 -> 324
~ sub_fffffe0009600d98 -> sub_fffffe0009685748 : 64 -> 68
~ sub_fffffe0009600dd8 -> sub_fffffe000968578c : 72 -> 76
~ sub_fffffe0009600e20 -> sub_fffffe00096857d8 : 64 -> 68
~ sub_fffffe0009600e60 -> sub_fffffe000968581c : 72 -> 76
~ sub_fffffe0009600ec8 -> sub_fffffe0009685888 : 72 -> 76
~ sub_fffffe0009600f18 -> sub_fffffe00096858dc : 52 -> 56
~ sub_fffffe0009600f4c -> sub_fffffe0009685914 : 52 -> 56
~ sub_fffffe0009600f90 -> sub_fffffe000968595c : 68 -> 72
~ sub_fffffe0009600ffc -> sub_fffffe00096859cc : 72 -> 76
~ sub_fffffe0009601044 -> sub_fffffe0009685a18 : 104 -> 108
~ sub_fffffe00096010c0 -> sub_fffffe0009685a98 : 88 -> 92
~ sub_fffffe0009601118 -> sub_fffffe0009685af4 : 88 -> 92
~ sub_fffffe0009601170 -> sub_fffffe0009685b50 : 152 -> 156
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize : 2488 -> 2492
~ sub_fffffe0009601bd0 -> sub_fffffe00096865b8 : 140 -> 144
~ sub_fffffe0009601c5c -> sub_fffffe0009686648 : 56 -> 60
~ __ZN20AppleSPIMCController5startEP9IOService.cold.1 : 116 -> 120
~ __ZN20AppleSPIMCController5startEP9IOService.cold.2 : 112 -> 116
~ __ZN20AppleSPIMCController5startEP9IOService.cold.3 : 116 -> 120
~ __ZN20AppleSPIMCController5startEP9IOService.cold.4 : 128 -> 132
~ sub_fffffe0009601f80 -> sub_fffffe0009686980 : 36 -> 40
~ __ZN20AppleSPIMCController17executeSPICommandEP18AppleARMSPICommand.cold.1 : 112 -> 116
~ __ZN20AppleSPIMCController17executeSPICommandEP18AppleARMSPICommand.cold.2 : 112 -> 116
~ __ZN20AppleSPIMCController17executeSPICommandEP18AppleARMSPICommand.cold.3 : 112 -> 116
~ __ZN20AppleSPIMCController17executeSPICommandEP18AppleARMSPICommand.cold.4 : 112 -> 116
~ __ZN20AppleSPIMCController21_executeSPICommandDMAEP18AppleARMSPICommand.cold.1 : 120 -> 124
~ __ZN20AppleSPIMCController21_executeSPICommandDMAEP18AppleARMSPICommand.cold.2 : 132 -> 136
~ __ZN20AppleSPIMCController21_executeSPICommandDMAEP18AppleARMSPICommand.cold.3 : 136 -> 140
~ __ZN20AppleSPIMCController21_executeSPICommandDMAEP18AppleARMSPICommand.cold.4 : 136 -> 140
~ __ZN20AppleSPIMCController21_executeSPICommandDMAEP18AppleARMSPICommand.cold.5 : 132 -> 136
~ __ZN20AppleSPIMCController21_executeSPICommandDMAEP18AppleARMSPICommand.cold.6 : 120 -> 124
~ __ZN20AppleSPIMCController21_executeSPICommandDMAEP18AppleARMSPICommand.cold.7 : 120 -> 124
~ __ZN20AppleSPIMCController21_executeSPICommandPIOEP18AppleARMSPICommand.cold.1 : 128 -> 132
~ __ZN20AppleSPIMCController21_executeSPICommandPIOEP18AppleARMSPICommand.cold.2 : 128 -> 132
~ __ZN20AppleSPIMCController21_executeSPICommandPIOEP18AppleARMSPICommand.cold.3 : 96 -> 100
~ __ZN20AppleSPIMCController21_executeSPICommandPIOEP18AppleARMSPICommand.cold.4 : 96 -> 100
~ __ZN20AppleSPIMCController14_interruptPollEj.cold.1 : 96 -> 100
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.1 : 112 -> 116
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.2 : 112 -> 116
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.3 : 112 -> 116
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.4 : 112 -> 116
~ _OUTLINED_FUNCTION_2 : 112 -> 116
~ sub_fffffe0009602934 -> sub_fffffe000968738c : 112 -> 116
~ sub_fffffe00096029a4 -> sub_fffffe0009687400 : 112 -> 116
~ sub_fffffe0009602a14 -> sub_fffffe0009687474 : 112 -> 116
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.9 : 108 -> 112
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.10 : 108 -> 112
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.11 : 108 -> 112
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.12 : 108 -> 112
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.13 : 112 -> 116
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.14 : 112 -> 116
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.15 : 112 -> 116
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.16 : 112 -> 116
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.17 : 112 -> 116
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.18 : 112 -> 116
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.19 : 156 -> 160
~ __ZNK25AppleSPIMCControllerStats9serializeEP11OSSerialize.cold.20 : 112 -> 116
```
