## com.apple.driver.AppleHPM

> `com.apple.driver.AppleHPM`

```diff

-614.0.0.0.0
-  __TEXT.__cstring: 0x1d1a3
+614.0.2.0.1
+  __TEXT.__cstring: 0x1d1b9
   __TEXT.__const: 0x110
   __TEXT.__os_log: 0x1e8
-  __TEXT_EXEC.__text: 0x66fe4
+  __TEXT_EXEC.__text: 0x6723c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6d0
   __DATA.__common: 0x630

   __DATA_CONST.__mod_term_func: 0x130
   __DATA_CONST.__const: 0x15838
   __DATA_CONST.__kalloc_type: 0xcc0
-  UUID: DFA65361-C452-309F-9156-120D068D9D73
+  UUID: C2D342D1-3777-3502-94DA-1F0610B01FF5
   Functions: 1623
   Symbols:   0
-  CStrings:  1658
+  CStrings:  1659
 
Functions:
~ sub_fffffff0094d0524 -> sub_fffffff009518d64 : 252 -> 268
~ sub_fffffff0094d164c -> sub_fffffff009519e9c : 348 -> 364
~ __ZN12AppleHPMLDCM21getLDCMStatusRegisterEPhh : 408 -> 424
~ sub_fffffff0094d1bd0 -> sub_fffffff00951a440 : 252 -> 268
~ sub_fffffff0094d1d74 -> sub_fffffff00951a5f4 : 104 -> 120
~ __ZN12AppleHPMLDCM17isVoltageDetectedEv : 440 -> 456
~ __ZN17AppleHPMInterface22processInterruptEventsEv : 3944 -> 3952
~ __ZN17AppleHPMInterface19setCurrentModeFlagsEv : 4268 -> 4344
~ sub_fffffff0094e9ddc -> sub_fffffff0095326d0 : 3564 -> 3572
~ __ZN23AppleHPMInterfaceType105startEP9IOService : 412 -> 464
~ __ZN23AppleHPMInterfaceType1011tUSBTimeoutEP18IOTimerEventSource : 372 -> 448
~ __ZN23AppleHPMInterfaceType1012stopUSBTimerEv : 324 -> 400
~ __ZN23AppleHPMInterfaceType1012forceUSB23OnEv : 760 -> 832
~ __ZN23AppleHPMInterfaceType1010turnOnVbusEv : 264 -> 332
~ __ZN23AppleTCControllerType125startEP9IOService : 716 -> 784
CStrings:
+ "HPM Mode Block Active"

```
