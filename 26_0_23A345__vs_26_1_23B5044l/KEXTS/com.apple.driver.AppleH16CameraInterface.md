## com.apple.driver.AppleH16CameraInterface

> `com.apple.driver.AppleH16CameraInterface`

```diff

-4.31.0.0.0
+4.105.0.0.0
   __TEXT.__const: 0xa1f8
-  __TEXT.__cstring: 0x1858f
-  __TEXT.__os_log: 0x1457a
-  __TEXT_EXEC.__text: 0x9da94
+  __TEXT.__cstring: 0x18647
+  __TEXT.__os_log: 0x145f2
+  __TEXT_EXEC.__text: 0x9dfa0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a8
   __DATA.__common: 0x4c8

   __DATA_CONST.__const: 0x18560
   __DATA_CONST.__kalloc_type: 0x11c0
   __DATA_CONST.__kalloc_var: 0xa50
-  UUID: 7C90949E-C0F4-3EA4-811D-9E81B0BDC738
+  UUID: 6FAF56FF-4957-39BE-AA31-A86B274960B2
   Functions: 1761
   Symbols:   0
-  CStrings:  3141
+  CStrings:  3146
 
Functions:
~ sub_fffffe0009305344 -> sub_fffffe00093c5f04 : 6908 -> 6956
~ sub_fffffe0009306e40 -> sub_fffffe00093c7a30 : 6908 -> 6956
~ sub_fffffe0009309cc0 -> sub_fffffe00093ca8e0 : 136 -> 148
~ __ZN13AppleH16CamIn26H16ISPSharedMemorySurfaces15allocateSurfaceEyPP31H16ISPSharedMemorySurfaceParamsbjbjb : 4100 -> 4316
~ __ZN13AppleH16CamIn37ISP_ShowSharedMemoryAllocations_gatedEby : 19712 -> 19728
~ __ZN13AppleH16CamIn26H16ISPSharedMemorySurfaces41targetPhysicalAddressToHostVirtualAddressEyPP31H16ISPSharedMemorySurfaceParamsPjy : 1224 -> 1228
~ __ZN13AppleH16CamIn28ISP_InitializeClassVariablesEv : 5280 -> 5348
~ __ZN13AppleH16CamIn26processSharedMallocRequestEyyyPv : 1180 -> 1184
~ __ZN13AppleH16CamIn24ISP_PowerOffCamera_gatedEPv : 2024 -> 2188
~ __ZN13AppleH16CamIn23ISP_PowerOnCamera_gatedEPvj : 2200 -> 2264
~ sub_fffffe0009343bc0 -> sub_fffffe0009404a04 : 920 -> 1136
~ sub_fffffe0009344028 -> sub_fffffe0009404f44 : 616 -> 724
~ sub_fffffe0009344484 -> sub_fffffe000940540c : 920 -> 1136
~ sub_fffffe0009344880 -> sub_fffffe00094058e0 : 616 -> 724
CStrings:
+ "AppleH16CamIn:%s -  %s (fPowerEvent=%d, fOutstandingPowerUpRequests=%d)\n"
+ "AppleH16CamIn:%s -  %s (fPowerEvent=%d, fOutstandingPowerUpRequests=%d, fSystemSleepInProgress=%d)\n"
+ "AppleH16CamIn:%s - Client %s is requesting ISP power down\n"
+ "AppleH16CamIn:%s - Client %s is requesting ISP power up\n"
+ "AppleH16CamIn:%s - Didn't initiate HW power down. powerRefCnt=%d, fPowerEvent=%d, fOutstandingPowerUpRequests = %d, isPowered: %d\n"
+ "AppleH16CamIn::H16ISPSharedMemorySurfaces:%s - remap allowed surface\n"
+ "IOSurfaceHostOnly"
- "AppleH16CamIn:%s - (fPowerEvent=%d, fOutstandingPowerUpRequests=%d)\n"
- "AppleH16CamIn:%s - (fPowerEvent=%d, fOutstandingPowerUpRequests=%d, fSystemSleepInProgress=%d)\n"
- "AppleH16CamIn:%s - Didn't initiate HW power down. fPowerEvent=%d, fOutstandingPowerUpRequests = %d, isPowered: %d\n"
- "AppleH16CamIn:%s - requesting ISP power up\n"

```
