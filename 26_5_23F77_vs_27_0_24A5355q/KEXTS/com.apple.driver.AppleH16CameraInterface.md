## com.apple.driver.AppleH16CameraInterface

> `com.apple.driver.AppleH16CameraInterface`

```diff

-5.504.0.0.0
+6.10.3.0.0
   __TEXT.__const: 0xa1b0
-  __TEXT.__cstring: 0x1989e
-  __TEXT.__os_log: 0x1589c
-  __TEXT_EXEC.__text: 0x9a51c
+  __TEXT.__cstring: 0x198ca
+  __TEXT.__os_log: 0x158c8
+  __TEXT_EXEC.__text: 0x9a698
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a8
   __DATA.__common: 0x4f0
   __DATA.__bss: 0x1f8
-  __DATA_CONST.__auth_got: 0x858
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0x90
   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x19770
   __DATA_CONST.__kalloc_type: 0x1200
   __DATA_CONST.__kalloc_var: 0xa50
-  UUID: 5525C5A7-EAE2-3D7D-8F2F-E0F0741752CE
+  __DATA_CONST.__auth_got: 0x868
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__auth_ptr: 0x18
+  UUID: 6CE76C82-5315-30B7-B346-1BC46123ACF4
   Functions: 1817
   Symbols:   0
-  CStrings:  3255
+  CStrings:  3257
 
Functions:
~ __ZN13AppleH16CamIn26H16ISPSharedMemorySurfaces15allocateSurfaceEyPP31H16ISPSharedMemorySurfaceParamsbjbjb -> sub_fffffe0008d72ea4 : 3780 -> 3752
~ __ZN13AppleH16CamIn28ReleaseFirmwareWorkProcessorEP8ipc_port -> sub_fffffe0008d7acfc : 2748 -> 2752
~ __ZN13AppleH16CamIn27ISP_InitializeSoCParametersE13H16ISPVersionjj -> sub_fffffe0008d7e130 : 23368 -> 23612
~ __ZN13AppleH16CamIn28ISP_InitializeClassVariablesEv -> sub_fffffe0008d841c4 : 4840 -> 4836
~ __ZN13AppleH16CamIn5startEP9IOService -> sub_fffffe0008d89bc4 : 14220 -> 14228
~ sub_fffffe0008acd37c -> sub_fffffe0008d93a2c : 452 -> 456
~ sub_fffffe0008acd540 -> sub_fffffe0008d93bf4 : 452 -> 456
~ __ZN13AppleH16CamIn37processTargetToHostBufferNotificationEyyyPv -> sub_fffffe0008d98ce0 : 2984 -> 2924
~ __ZN13AppleH16CamIn36drainIOProcessorChannelMessageQueuesEv -> sub_fffffe0008d99ce0 : 392 -> 396
~ __ZN15PSDServiceVoter4voteEb23PSDVoteLatencyToleranceP16AppleARMIODevice -> sub_fffffe0008d9b74c : 260 -> 264
~ __ZN15PSDServiceVoter8GetStateEPjP16AppleARMIODevice -> sub_fffffe0008d9b854 : 236 -> 240
~ __ZN13AppleH16CamIn21ISP_SendCommand_gatedEP25H16ISPUserFWCommandParams -> sub_fffffe0008da7bcc : 1160 -> 1344
~ __ZN13AppleH16CamIn31ReadAndPublishSensorInfoToIORegEj -> sub_fffffe0008daa8dc : 4020 -> 4044
~ __ZN13AppleH16CamIn43ISP_CompleteFirmwareWorkProcessorItem_gatedEPyPvjP4task -> sub_fffffe0008db4ebc : 1924 -> 1928
~ __ZN13AppleH16CamIn23AllocateFwMemorySurfaceEjj -> sub_fffffe0008dc53b0 : 2312 -> 2300
~ sub_fffffe0008b02bbc -> sub_fffffe0008dc930c : 160 -> 164
~ sub_fffffe0008b03178 -> sub_fffffe0008dc98cc : 740 -> 736
~ __ZN13AppleH16CamIn15ISPCoredumpInitEv -> sub_fffffe0008dca10c : 692 -> 688
~ __ZN13AppleH16CamIn17ISP_ForceShutdownEv -> sub_fffffe0008dca3bc : 552 -> 548
~ __ZN13AppleH16CamIn17ISP_StartFirmwareEv -> sub_fffffe0008dcb2bc : 10160 -> 10164
~ sub_fffffe0008b2b8d8 -> sub_fffffe0008df2024 : 228 -> 232
~ sub_fffffe0008b2c390 -> sub_fffffe0008df2ae0 : 224 -> 228
~ sub_fffffe0008b33000 -> sub_fffffe0008df9754 : 204 -> 196
CStrings:
+ "AppleCamera:%s - ISP command not permitted\n"

```
