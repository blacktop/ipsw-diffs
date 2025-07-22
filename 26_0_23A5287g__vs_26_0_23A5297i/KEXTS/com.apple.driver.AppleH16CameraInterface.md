## com.apple.driver.AppleH16CameraInterface

> `com.apple.driver.AppleH16CameraInterface`

```diff

-4.18.5.0.0
-  __TEXT.__const: 0xa1e8
-  __TEXT.__cstring: 0x18435
-  __TEXT.__os_log: 0x14416
-  __TEXT_EXEC.__text: 0x9d438
+4.20.4.0.0
+  __TEXT.__const: 0xa1f8
+  __TEXT.__cstring: 0x184de
+  __TEXT.__os_log: 0x144bf
+  __TEXT_EXEC.__text: 0x9d714
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a8
   __DATA.__common: 0x4c8

   __DATA_CONST.__const: 0x18550
   __DATA_CONST.__kalloc_type: 0x11c0
   __DATA_CONST.__kalloc_var: 0xa50
-  UUID: 1E27350F-436B-32AA-BE9E-46B9FCABB5C6
+  UUID: E772FD11-C38E-37C2-80DD-7C58073E3059
   Functions: 1757
   Symbols:   0
-  CStrings:  3132
+  CStrings:  3134
 
Functions:
~ sub_fffffff0093871b4 -> sub_fffffff009390064 : 4412 -> 4420
~ sub_fffffff00938ba00 -> sub_fffffff0093948b8 : 4432 -> 4440
~ __ZN13AppleH16CamIn27ISP_InitializeSoCParametersE13H16ISPVersionjj : 18500 -> 18948
~ __ZN13AppleH16CamIn28ISP_InitializeClassVariablesEv : 5284 -> 5280
~ __ZN13AppleH16CamIn5startEP9IOService : 14836 -> 14804
~ sub_fffffff0093ac7a4 -> sub_fffffff0093b5800 : 1864 -> 1856
~ __ZN13AppleH16CamIn25ISP_LoadOverrideNVM_gatedEP27H16ISPLoadOverrideNVMParamsb : 2204 -> 2272
~ __ZN13AppleH16CamIn28powerStateWillChangeTo_gatedEmmP9IOService : 424 -> 488
~ __ZN13AppleH16CamIn31ReadAndPublishSensorInfoToIORegEj : 5124 -> 5128
~ __ZN13AppleH16CamIn27ISP_InstallFakeSensor_gatedEjj : 720 -> 780
~ __ZN13AppleH16CamIn17ISP_StartFirmwareEv : 10684 -> 10736
~ __ZN18IspAneIPCEndPoints18sendEPConfigToPeerEv : 1120 -> 1184
CStrings:
+ "AppleH16CamIn:%s - AOP RTBuddyService state will change to %lu, ret=%d, fIsPowered=%d, fPowerEvent=%d\n"
+ "AppleH16CamIn:%s - AppleH16CamIn:: ispcpuSoftwareInterruptRegisterAddress: 0x%llx, ispcpuSoftwareInterruptRegisterBitmask: 0x%x\n\n"
- "AppleH16CamIn:%s - AOP RTBuddyService state will change to %lu\n"

```
