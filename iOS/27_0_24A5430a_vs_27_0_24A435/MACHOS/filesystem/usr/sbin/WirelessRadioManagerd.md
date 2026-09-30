## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1939.3.0.0.0
-  __TEXT.__text: 0x17172c
-  __TEXT.__auth_stubs: 0x26f0
-  __TEXT.__objc_stubs: 0x21740
+  __TEXT.__text: 0x1772a4
+  __TEXT.__auth_stubs: 0x2790
+  __TEXT.__objc_stubs: 0x21920
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0x11bfc
-  __TEXT.__const: 0x11e08
-  __TEXT.__gcc_except_tab: 0x6364
-  __TEXT.__cstring: 0x5a227
-  __TEXT.__objc_methname: 0x346f4
+  __TEXT.__objc_methlist: 0x11cac
+  __TEXT.__const: 0x11f10
+  __TEXT.__gcc_except_tab: 0x65a0
+  __TEXT.__cstring: 0x5a831
+  __TEXT.__objc_methname: 0x347ee
   __TEXT.__objc_classname: 0x11e2
-  __TEXT.__objc_methtype: 0x8b17
+  __TEXT.__objc_methtype: 0x8bea
   __TEXT.__dlopen_cstrs: 0x43e
   __TEXT.__oslogstring: 0x109
-  __TEXT.__unwind_info: 0x50e8
-  __DATA_CONST.__const: 0x5888
-  __DATA_CONST.__cfstring: 0x32f80
+  __TEXT.__unwind_info: 0x51b0
+  __DATA_CONST.__const: 0x59f8
+  __DATA_CONST.__cfstring: 0x33400
   __DATA_CONST.__objc_classlist: 0x538
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x550
-  __DATA_CONST.__objc_intobj: 0x47b8
-  __DATA_CONST.__objc_arraydata: 0x10130
-  __DATA_CONST.__objc_dictobj: 0x848
-  __DATA_CONST.__objc_arrayobj: 0x6780
+  __DATA_CONST.__objc_superrefs: 0x558
+  __DATA_CONST.__objc_intobj: 0x4980
+  __DATA_CONST.__objc_arraydata: 0x10c98
+  __DATA_CONST.__objc_dictobj: 0xa50
+  __DATA_CONST.__objc_arrayobj: 0x6d38
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x1390
-  __DATA_CONST.__got: 0x8b0
+  __DATA_CONST.__auth_got: 0x13e0
+  __DATA_CONST.__got: 0x8e0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x1cf78
-  __DATA.__objc_selrefs: 0xa040
-  __DATA.__objc_ivar: 0x1e88
+  __DATA.__objc_const: 0x1d038
+  __DATA.__objc_selrefs: 0xa080
+  __DATA.__objc_ivar: 0x1e9c
   __DATA.__objc_data: 0x3430
   __DATA.__data: 0x838
   __DATA.__common: 0x63a

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7811
-  Symbols:   874
-  CStrings:  16876
+  Functions: 7862
+  Symbols:   890
+  CStrings:  16934
 
Symbols:
+ _OBJC_CLASS_$_CMAngleManager
+ __ZN3abm15kRFSensingValueE
+ __ZN3abm15kTunerModeStateE
+ __ZN3abm17kRFSensingCommandE
+ __ZN3abm27kEventRFSensingStateChangedE
+ __ZN3abm34kRFSensingSubCommandQueryTunerModeE
+ __ZN3abm6client13CreateManagerERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEP16dispatch_queue_s
+ __ZN3abm6client14PerformCommandENSt3__110shared_ptrINS0_7ManagerEEERKNS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPvPSD_
+ __ZN3abm6client20RegisterEventHandlerENSt3__110shared_ptrINS0_7ManagerEEERKNS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEU13block_pointerFvPvP16dispatch_group_sE
+ __ZN3abm6client8EventsOnENSt3__110shared_ptrINS0_7ManagerEEE
+ __ZN3abm6client9EventsOffENSt3__110shared_ptrINS0_7ManagerEEE
+ __ZN3ctu5iokit10Controller26setFrontCameraRenoCallbackEN8dispatch19function_with_queueIFvNS0_34TelephonyIOKitFrontCameraRenoStateEEEE
+ __ZN3xpc19dyn_cast_or_defaultERKNS_6objectEi
+ _objc_storeWeak
+ _strlen
+ _xpc_null_create
CStrings:
+ "@\"<DeviceModeEventDelegate>\""
+ "@\"CMAngleManager\""
+ "@\"WCM_DeviceModeEventWrapper\""
+ "Ant-14"
+ "BB Power on, start HI monitor..."
+ "BT_ClockAlignment_Client"
+ "CoEx-Table-AntBlockPwrLmt-Coex066"
+ "CoEx-Table-AntBlockPwrLmt-Coex068"
+ "CoEx-Table-AntBlockPwrLmt-Coex070"
+ "CoEx-Table-CellCoex066_V8WiFiEnh"
+ "CoEx-Table-CellCoex067_V8WiFiEnh"
+ "CoEx-Table-CellCoex068A_V8WiFiEnh"
+ "CoEx-Table-CellCoex068B_V8WiFiEnh"
+ "CoEx-Table-CellCoex070_V8WiFiEnh"
+ "CoEx-Table-CellCoex075_watchV4Macro"
+ "CoEx-Table-CellCoex076_watchV4Macro"
+ "CoEx-Table-CellRC1-Coex067"
+ "CoexManager"
+ "Init: Read mode(%@) BT Clock Alignment Policy Table from Plist File %@.plist"
+ "Init: readPlatformBTClockAlignmentPolicy for mode(%@): %@"
+ "PolicyManager route FrontCameraReno to BackTele, cameraState = 0x%X"
+ "Register ABM event for mode: registerAbmDeviceModeCallback()"
+ "Register device mode event callback..."
+ "RouteFCamRenoToBackTele"
+ "T@\"<DeviceModeEventDelegate>\",W,N,V_delegate"
+ "^{dispatch_queue_s=}"
+ "^{dispatch_queue_s=}16@0:8"
+ "_abmManager"
+ "_delegate"
+ "antenna_block_policy_mav_p067"
+ "bb_CoEx-Table-CellCoex067_V8WiFiEnh"
+ "com.apple.wireradiomanager.deviceMode.queue"
+ "delegate"
+ "deviceModeUpdate:"
+ "deviceModeUpdate: PolicyManager is nil"
+ "deviceModeUpdate: mode = %d"
+ "init: BT Clock Alignment policy Plist File Found"
+ "init: No BT Clock Alignment policy Found in Plist file: %@.plist"
+ "init: No BT Clock Alignment policy Plist File Found"
+ "isAvailable"
+ "isFrontCameraRenoSupportedForCoex"
+ "listen"
+ "mAngleManager"
+ "mDeviceModeWrapper"
+ "queryDeviceMode"
+ "queryDeviceMode: PerformCommand failed"
+ "queryDeviceMode: mode = %@"
+ "queryDeviceMode: mode = A"
+ "queryDeviceMode: mode = B"
+ "queryDeviceMode: mode = Unknown"
+ "readPlatformBTClockAlignmentPolicy Row(%d), for mode %@"
+ "readPlatformBTClockAlignmentPolicy numofRow=%d"
+ "startDeviceModeMonitor"
+ "startMonitoringDeviceModeEvent"
+ "startMonitoringDeviceModeEvent: mode is not available in current platform!"
+ "startMonitoringDeviceModeEvent: mode is supported in current platform!"
+ "v24@?0^v8^{dispatch_group_s=}16"
+ "{shared_ptr<abm::client::Manager>=\"__ptr_\"^{Manager}\"__cntrl_\"^{__shared_weak_count}}"
```
