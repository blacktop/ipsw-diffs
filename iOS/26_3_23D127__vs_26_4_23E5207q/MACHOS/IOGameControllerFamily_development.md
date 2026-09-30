## IOGameControllerFamily_development

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily_development`

```diff

-13.3.1.0.0
+13.4.8.0.0
   __TEXT.__const: 0x480
-  __TEXT.__cstring: 0x21ec
+  __TEXT.__cstring: 0x242d
   __TEXT.__os_log: 0x85e6
-  __TEXT_EXEC.__text: 0x2c294
+  __TEXT_EXEC.__text: 0x27748
   __TEXT_EXEC.__auth_stubs: 0x520
   __DATA.__data: 0xc8
   __DATA.__common: 0x268

   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x5578
   __DATA_CONST.__kalloc_type: 0x800
-  UUID: 37B15133-0FA6-3154-990E-83A80B3A3E44
-  Functions: 891
-  Symbols:   1993
+  UUID: 5F016090-54BD-327A-9F12-834110556368
+  Functions: 912
+  Symbols:   2016
   CStrings:  576
 
Symbols:
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ __ZZL39_IOHIDDevice_getReport_completion_thunkPvS_ijE20kalloc_type_view_563
+ __ZZL39_IOHIDDevice_setReport_completion_thunkPvS_ijE20kalloc_type_view_716
+ __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_584
+ __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_615
+ __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_737
+ __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_767
- __ZZL39_IOHIDDevice_getReport_completion_thunkPvS_ijE20kalloc_type_view_544
- __ZZL39_IOHIDDevice_setReport_completion_thunkPvS_ijE20kalloc_type_view_686
- __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_569
- __ZZN13IOHIDGCDevice9getReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_604
- __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_711
- __ZZN13IOHIDGCDevice9setReportE15IOHIDReportTypehP18IOMemoryDescriptorjP8OSObjectPvPFvS4_S5_S2_iEE20kalloc_type_view_745
CStrings:
+ "/Library/Caches/com.apple.xbs/CBACDC36-2DDE-4421-897D-28D3F3FB17C9/TemporaryDirectory.zAfJCo/Sources/CoreController_kext/GameControllerDrivers/Sony/PSVR2/Kernel/PSVR2SenseDevice.cpp"
+ "/Library/Caches/com.apple.xbs/CBACDC36-2DDE-4421-897D-28D3F3FB17C9/TemporaryDirectory.zAfJCo/Sources/CoreController_kext/GameControllerDrivers/Sony/PSVR2/Kernel/PSVR2SenseDeviceFastPathUserClient.cpp"
+ "/Library/Caches/com.apple.xbs/CBACDC36-2DDE-4421-897D-28D3F3FB17C9/TemporaryDirectory.zAfJCo/Sources/CoreController_kext/GameControllerDrivers/Sony/PSVR2/Kernel/PSVR2SenseDeviceFastPathUserClientQueue.cpp"
+ "/Library/Caches/com.apple.xbs/CBACDC36-2DDE-4421-897D-28D3F3FB17C9/TemporaryDirectory.zAfJCo/Sources/CoreController_kext/GameControllerDrivers/Sony/PSVR2/Kernel/PSVR2SenseDeviceHIDEventServerUserClient.cpp"
+ "/Library/Caches/com.apple.xbs/CBACDC36-2DDE-4421-897D-28D3F3FB17C9/TemporaryDirectory.zAfJCo/Sources/CoreController_kext/IOGameControllerFamily/IOGCResource.cpp"
+ "/Library/Caches/com.apple.xbs/CBACDC36-2DDE-4421-897D-28D3F3FB17C9/TemporaryDirectory.zAfJCo/Sources/CoreController_kext/IOGameControllerFamily/Service/IOHIDGCDevice.cpp"
+ "/Library/Caches/com.apple.xbs/CBACDC36-2DDE-4421-897D-28D3F3FB17C9/TemporaryDirectory.zAfJCo/Sources/CoreController_kext/IOGameControllerFamily/Utility/ControlQueue/IOGCCircularControlQueueMemory.c"
+ "/Library/Caches/com.apple.xbs/CBACDC36-2DDE-4421-897D-28D3F3FB17C9/TemporaryDirectory.zAfJCo/Sources/CoreController_kext/IOGameControllerFamily/Utility/DataQueue/IOGCCircularDataQueue.cpp"
+ "/Library/Caches/com.apple.xbs/CBACDC36-2DDE-4421-897D-28D3F3FB17C9/TemporaryDirectory.zAfJCo/Sources/CoreController_kext/IOGameControllerFamily/Utility/IOGCCommandQueue.cpp"
+ "2111111"
+ "22111111"
+ "site.struct GetReportContinuation"
+ "site.struct SetReportContinuation"
- "/Library/Caches/com.apple.xbs/Sources/CoreController_kext/GameControllerDrivers/Sony/PSVR2/Kernel/PSVR2SenseDevice.cpp"
- "/Library/Caches/com.apple.xbs/Sources/CoreController_kext/GameControllerDrivers/Sony/PSVR2/Kernel/PSVR2SenseDeviceFastPathUserClient.cpp"
- "/Library/Caches/com.apple.xbs/Sources/CoreController_kext/GameControllerDrivers/Sony/PSVR2/Kernel/PSVR2SenseDeviceFastPathUserClientQueue.cpp"
- "/Library/Caches/com.apple.xbs/Sources/CoreController_kext/GameControllerDrivers/Sony/PSVR2/Kernel/PSVR2SenseDeviceHIDEventServerUserClient.cpp"
- "/Library/Caches/com.apple.xbs/Sources/CoreController_kext/IOGameControllerFamily/IOGCResource.cpp"
- "/Library/Caches/com.apple.xbs/Sources/CoreController_kext/IOGameControllerFamily/Service/IOHIDGCDevice.cpp"
- "/Library/Caches/com.apple.xbs/Sources/CoreController_kext/IOGameControllerFamily/Utility/ControlQueue/IOGCCircularControlQueueMemory.c"
- "/Library/Caches/com.apple.xbs/Sources/CoreController_kext/IOGameControllerFamily/Utility/DataQueue/IOGCCircularDataQueue.cpp"
- "/Library/Caches/com.apple.xbs/Sources/CoreController_kext/IOGameControllerFamily/Utility/IOGCCommandQueue.cpp"
- "1112"
- "11122"
- "site.struct GetReportCompletion"
- "site.struct SetReportCompletion"

```
