## com.apple.driver.AppleS8000AES

> `com.apple.driver.AppleS8000AES`

```diff

 140.0.0.0.0
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x13a4
-  __TEXT_EXEC.__text: 0x412c
+  __TEXT_EXEC.__text: 0x4270
   __TEXT_EXEC.__auth_stubs: 0x200
   __DATA.__data: 0x200
   __DATA.__common: 0x60
Functions:
~ sub_fffffe00093e5a30 -> sub_fffffe000945dba0 : 72 -> 76
~ sub_fffffe00093e5a80 -> sub_fffffe000945dbf4 : 52 -> 56
~ sub_fffffe00093e5ab4 -> sub_fffffe000945dc2c : 52 -> 56
~ sub_fffffe00093e5af8 -> sub_fffffe000945dc74 : 68 -> 72
~ sub_fffffe00093e5b64 -> sub_fffffe000945dce4 : 72 -> 76
~ sub_fffffe00093e5bac -> sub_fffffe000945dd30 : 104 -> 108
~ sub_fffffe00093e5c28 -> sub_fffffe000945ddb0 : 88 -> 92
~ sub_fffffe00093e5c80 -> sub_fffffe000945de0c : 88 -> 92
~ sub_fffffe00093e5cd8 -> sub_fffffe000945de68 : 72 -> 76
~ sub_fffffe00093e5d28 -> sub_fffffe000945debc : 52 -> 56
~ sub_fffffe00093e5d5c -> sub_fffffe000945def4 : 52 -> 56
~ sub_fffffe00093e5da0 -> sub_fffffe000945df3c : 68 -> 72
~ sub_fffffe00093e5e0c -> sub_fffffe000945dfac : 72 -> 76
~ sub_fffffe00093e5e54 -> sub_fffffe000945dff8 : 104 -> 108
~ sub_fffffe00093e5ed0 -> sub_fffffe000945e078 : 88 -> 92
~ sub_fffffe00093e5f28 -> sub_fffffe000945e0d4 : 88 -> 92
~ _OUTLINED_FUNCTION_0 : 2492 -> 2496
~ __ZN24AppleS8000AESAccelerator18_interruptOccurredEP22IOInterruptEventSourcei : 244 -> 248
~ sub_fffffe00093e6a30 -> sub_fffffe000945ebe8 : 256 -> 260
~ sub_fffffe00093e6b4c -> sub_fffffe000945ed08 : 184 -> 188
~ _OUTLINED_FUNCTION_2 : 72 -> 76
~ sub_fffffe00093e6c4c -> sub_fffffe000945ee10 : 232 -> 236
~ __ZN24AppleS8000AESAccelerator10_enableAESEb : 784 -> 788
~ __ZN24AppleS8000AESAccelerator13_configureAESEP23IOAESAcceleratorCommandj : 2596 -> 2600
~ __ZN24AppleS8000AESAccelerator16_space_availableEj : 332 -> 336
~ sub_fffffe00093e7cc8 -> sub_fffffe000945fe9c : 104 -> 108
~ __ZN24AppleS8000AESAccelerator16_distribute_dkeyEv : 164 -> 168
~ __ZN24AppleS8000AESAccelerator17performAESQuantumEP23IOAESAcceleratorCommand : 1620 -> 1624
~ __ZN24AppleS8000AESAccelerator16_prepareTransferEjjP12IODMACommandS1_yyy : 616 -> 620
~ __ZN24AppleS8000AESAccelerator15_handleIVBounceEP7IOAESIVt : 260 -> 264
~ __ZN24AppleS8000AESAccelerator12_completeAESEv : 920 -> 924
~ __ZN24AppleS8000AESAccelerator13getDTPropertyEPKcP9IOServicePj : 240 -> 244
~ __ZN24AppleS8000AESAccelerator14OverrideRegMapEP9IOService : 496 -> 500
~ __ZN24AppleS8000AESAccelerator13_push_commandEPvj : 256 -> 260
~ __GLOBAL__sub_I_AppleS8000AES.cpp : 160 -> 164
~ sub_fffffe00093e919c -> sub_fffffe0009461398 : 56 -> 60
~ _panic : 40 -> 44
~ __ZN24AppleS8000AESAccelerator5startEP9IOService.cold.2 : 40 -> 44
~ __ZN24AppleS8000AESAccelerator5startEP9IOService.cold.3 : 40 -> 44
~ __ZN24AppleS8000AESAccelerator5startEP9IOService.cold.4 : 44 -> 48
~ __ZN24AppleS8000AESAccelerator5startEP9IOService.cold.5 : 40 -> 44
~ __ZN24AppleS8000AESAccelerator5startEP9IOService.cold.6 : 40 -> 44
~ __ZN24AppleS8000AESAccelerator5startEP9IOService.cold.7 : 40 -> 44
~ __ZN24AppleS8000AESAccelerator5startEP9IOService.cold.8 : 40 -> 44
~ __ZN24AppleS8000AESAccelerator5startEP9IOService.cold.9 : 40 -> 44
~ __ZN24AppleS8000AESAccelerator5startEP9IOService.cold.10 : 40 -> 44
~ __ZN24AppleS8000AESAccelerator5startEP9IOService.cold.11 : 40 -> 44
~ __ZN24AppleS8000AESAccelerator5startEP9IOService.cold.12 : 40 -> 44
~ __ZN24AppleS8000AESAccelerator5startEP9IOService.cold.13 : 40 -> 44
~ __ZN24AppleS8000AESAccelerator5startEP9IOService.cold.14 : 40 -> 44
~ __ZN24AppleS8000AESAccelerator18_interruptOccurredEP22IOInterruptEventSourcei.cold.1 : 52 -> 56
~ __ZN24AppleS8000AESAccelerator4stopEP9IOService.cold.1 : 52 -> 56
~ __ZN24AppleS8000AESAccelerator10_enableAESEb.cold.1 : 52 -> 56
~ __ZN24AppleS8000AESAccelerator10_enableAESEb.cold.2 : 44 -> 48
~ __ZN24AppleS8000AESAccelerator10_enableAESEb.cold.3 : 44 -> 48
~ __ZN24AppleS8000AESAccelerator13_configureAESEP23IOAESAcceleratorCommandj.cold.1 : 44 -> 48
~ __ZN24AppleS8000AESAccelerator17_push_command_keyEjjPhS0_b.cold.1 : 60 -> 64
~ __ZN24AppleS8000AESAccelerator16_distribute_dkeyEv.cold.1 : 52 -> 56
~ __ZN24AppleS8000AESAccelerator17performAESQuantumEP23IOAESAcceleratorCommand.cold.1 : 52 -> 56
~ __ZN24AppleS8000AESAccelerator12_completeAESEv.cold.2 : 52 -> 56
~ sub_fffffe00093e9728 -> sub_fffffe0009461988 : 28 -> 32
~ sub_fffffe00093e9744 -> sub_fffffe00094619a8 : 28 -> 32
~ sub_fffffe00093e9760 -> sub_fffffe00094619c8 : 28 -> 32
~ __ZN24AppleS8000AESAccelerator12_completeAESEv.cold.3 : 52 -> 56
~ __ZN24AppleS8000AESAccelerator12_completeAESEv.cold.4 : 52 -> 56
~ __ZN24AppleS8000AESAccelerator12_completeAESEv.cold.6 : 52 -> 56
~ __ZN24AppleS8000AESAccelerator12_completeAESEv.cold.7 : 52 -> 56
~ __ZN24AppleS8000AESAccelerator17performAESQuantumEP23IOAESAcceleratorCommand.cold.10 : 52 -> 56
~ __ZN24AppleS8000AESAccelerator15_handleIVBounceEP7IOAESIVt.cold.1 : 52 -> 56
~ _OUTLINED_FUNCTION_1 : 52 -> 56
~ sub_fffffe00093e98e8 -> sub_fffffe0009461b70 : 52 -> 56
~ sub_fffffe00093e991c -> sub_fffffe0009461ba8 : 52 -> 56
~ sub_fffffe00093e9950 -> sub_fffffe0009461be0 : 52 -> 56
~ __ZN24AppleS8000AESAccelerator12_completeAESEv.cold.5 : 52 -> 56
~ sub_fffffe00093e99b8 -> sub_fffffe0009461c50 : 52 -> 56
~ sub_fffffe00093e99ec -> sub_fffffe0009461c88 : 52 -> 56
~ __ZN24AppleS8000AESAccelerator12_completeAESEv.cold.8 : 52 -> 56
~ __ZN24AppleS8000AESAccelerator13getDTPropertyEPKcP9IOServicePj.cold.1 : 84 -> 88
~ __ZN24AppleS8000AESAccelerator16_space_availableEj.cold.1 : 60 -> 64
~ __ZN24AppleS8000AESAccelerator13_push_commandEPvj.cold.1 : 60 -> 64
~ __ZN24AppleS8000AESAccelerator13_push_commandEPvj.cold.2 : 60 -> 64
```
