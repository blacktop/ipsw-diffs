## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

-1833.1.0.0.0
-  __TEXT.__text: 0x150b00
+1836.0.0.0.0
+  __TEXT.__text: 0x150bc4
   __TEXT.__auth_stubs: 0x24a0
   __TEXT.__objc_stubs: 0x1dfa0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0xfdfc
-  __TEXT.__gcc_except_tab: 0x5270
+  __TEXT.__objc_methlist: 0xfe04
+  __TEXT.__gcc_except_tab: 0x5230
   __TEXT.__const: 0x18c28
-  __TEXT.__cstring: 0x4d48d
+  __TEXT.__cstring: 0x4d5cf
   __TEXT.__objc_classname: 0x104e
-  __TEXT.__objc_methname: 0x2e9f3
-  __TEXT.__objc_methtype: 0x75f0
+  __TEXT.__objc_methname: 0x2eb00
+  __TEXT.__objc_methtype: 0x75f3
   __TEXT.__dlopen_cstrs: 0x3ca
   __TEXT.__oslogstring: 0x90
-  __TEXT.__unwind_info: 0x4680
+  __TEXT.__unwind_info: 0x4688
   __DATA_CONST.__auth_got: 0x1268
   __DATA_CONST.__got: 0x700
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4d40
+  __DATA_CONST.__const: 0x4d10
   __DATA_CONST.__cfstring: 0x2c360
   __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_protolist: 0x80

   __DATA_CONST.__objc_arrayobj: 0x6db0
   __DATA_CONST.__objc_dictobj: 0x348
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x197d8
-  __DATA.__objc_selrefs: 0x8e90
-  __DATA.__objc_ivar: 0x1aa8
+  __DATA.__objc_const: 0x19938
+  __DATA.__objc_selrefs: 0x8e98
+  __DATA.__objc_ivar: 0x1ad4
   __DATA.__objc_data: 0x2fd0
   __DATA.__data: 0x700
   __DATA.__common: 0x1e1

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 60C800A2-3931-39FB-89A0-B50FADD762A1
+  UUID: 19B50C63-D69F-3E28-BD08-EFF163963CBE
   Functions: 6956
   Symbols:   814
-  CStrings:  20724
+  CStrings:  20735
 
CStrings:
+ "Coex ARI Driver:  BB power on, configure cached camera and tuner state... "
+ "Coex ARI Driver:  BB power on, configure cached camera and tuner state... completed "
+ "Coex ARI Driver:  cache BT state = %llu, useCase = %llu "
+ "Coex ARI Driver:  cache GNSS state = %llu, useCase = %llu "
+ "Coex ARI Driver:  cache HFBT state = %llu, useCase = %llu "
+ "Coex ARI Driver:  cache UWB state = %llu, useCase = %llu "
+ "Coex ARI Driver:  cache WiFi state = %llu, useCase = %llu "
+ "Coex ARI Driver: Sensor %llu has wrong data size (%llu). Expect size = 2"
+ "handleTunerState:state:useCase:SubId:"
+ "mTunerStateBT_State"
+ "mTunerStateBT_UseCase"
+ "mTunerStateGNSS_State"
+ "mTunerStateGNSS_UseCase"
+ "mTunerStateHFBT_State"
+ "mTunerStateHFBT_UseCase"
+ "mTunerStateUWB_State"
+ "mTunerStateUWB_UseCase"
+ "mTunerStateWifi_State"
+ "mTunerStateWifi_UseCase"
+ "sendBasebandCameraState:SubId:BasebandPowerOnUpdate:"
+ "updateWeightAvgLQM:txRate:"
+ "v32@0:8Q16I24B28"
+ "v44@0:8Q16Q24Q32I40"
+ "{?=\"band\"[5C]\"usecase\"[5C]}"
- "Coex ARI Driver(SubId %u): Sensor %llu has wrong data size (%llu). Expect size = 2"
- "Low5GRate Counters Reset"
- "handleTunerState:sensorData:SubId:"
- "kCameraStateEvent"
- "kTunerStateBT"
- "kTunerStateGNSS"
- "kTunerStateHFBT"
- "kTunerStateUWB"
- "kTunerStateWiFi"
- "updateWeightAvgLQM:txRate:forceReset:"
- "v28@0:8I16I20B24"
- "v36@0:8Q16@24I32"
- "{?=\"band\"[4C]\"usecase\"[4C]}"

```
