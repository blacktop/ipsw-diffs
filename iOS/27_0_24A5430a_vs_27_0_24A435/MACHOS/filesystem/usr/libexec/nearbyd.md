## nearbyd

> `/usr/libexec/nearbyd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`

```diff

 569.0.0.0.0
-  __TEXT.__text: 0x554e78
+  __TEXT.__text: 0x55aab0
   __TEXT.__auth_stubs: 0x30d0
-  __TEXT.__objc_stubs: 0x170c0
-  __TEXT.__init_offsets: 0x6f8
-  __TEXT.__objc_methlist: 0xf694
-  __TEXT.__gcc_except_tab: 0x54f8c
-  __TEXT.__const: 0x3fa840
-  __TEXT.__cstring: 0x38a7c
-  __TEXT.__objc_methname: 0x23545
-  __TEXT.__oslogstring: 0x632a5
-  __TEXT.__objc_classname: 0x204e
-  __TEXT.__objc_methtype: 0x22c2d
+  __TEXT.__objc_stubs: 0x17500
+  __TEXT.__init_offsets: 0x6fc
+  __TEXT.__objc_methlist: 0xf85c
+  __TEXT.__gcc_except_tab: 0x55600
+  __TEXT.__const: 0x3fa9b0
+  __TEXT.__cstring: 0x38c82
+  __TEXT.__objc_methname: 0x23925
+  __TEXT.__oslogstring: 0x63a1a
+  __TEXT.__objc_classname: 0x20be
+  __TEXT.__objc_methtype: 0x22ded
   __TEXT.__ustring: 0x60
   __TEXT.__swift5_typeref: 0x7ec
   __TEXT.__swift5_capture: 0x574

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift_as_cont: 0x80
-  __TEXT.__unwind_info: 0x1cd80
+  __TEXT.__unwind_info: 0x1d068
   __TEXT.__eh_frame: 0x5a0
-  __DATA_CONST.__const: 0x1f258
-  __DATA_CONST.__cfstring: 0x17420
-  __DATA_CONST.__objc_classlist: 0x630
+  __DATA_CONST.__const: 0x1f4b8
+  __DATA_CONST.__cfstring: 0x17520
+  __DATA_CONST.__objc_classlist: 0x640
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x318
+  __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0x530
+  __DATA_CONST.__objc_protorefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0x538
   __DATA_CONST.__objc_arraydata: 0x480
   __DATA_CONST.__objc_arrayobj: 0x228
   __DATA_CONST.__objc_intobj: 0x990
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__auth_got: 0x1880
-  __DATA_CONST.__got: 0xe50
+  __DATA_CONST.__got: 0xe60
   __DATA_CONST.__auth_ptr: 0x300
-  __DATA.__objc_const: 0x1b4a0
-  __DATA.__objc_selrefs: 0x7080
-  __DATA.__objc_ivar: 0x19f0
-  __DATA.__objc_data: 0x4978
-  __DATA.__data: 0x41ac
-  __DATA.__common: 0xe70
+  __DATA.__objc_const: 0x1b800
+  __DATA.__objc_selrefs: 0x7180
+  __DATA.__objc_ivar: 0x1a1c
+  __DATA.__objc_data: 0x4a18
+  __DATA.__data: 0x42cc
+  __DATA.__common: 0xe80
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 23450
-  Symbols:   1307
-  CStrings:  19828
+  Functions: 23573
+  Symbols:   1309
+  CStrings:  19939
 
Symbols:
+ _OBJC_CLASS_$_CMAngleManager
+ _OBJC_CLASS_$_NSValue
CStrings:
+ "#btproximitydatabase #devicestate, OTA device-state offset read: scanner=%s advClass=%d state=%s offset=%.1fdB"
+ "#btproximitydatabase #devicestate, angle-state offset selected: scanner=%s advClass=%d state=%s offset=%.1fdB rssiThreshold %.1f -> %.1f"
+ "#dma,CMAngleManager is not available on this device"
+ "#dma,CMAngleManager started"
+ "#dma,CMAngleManager stopped"
+ "#dma,Failed to create CMAngleManager"
+ "#dma,first client added (degree), starting monitoring"
+ "#dma,first client added (state), starting monitoring"
+ "#dma,last client removed, stopping monitoring"
+ "#dma,received angle update: state=%s, mechanicalAngleDegrees=%.1f"
+ "#dma,received invalid angle update"
+ "#dma,updated angle degrees: %.4f"
+ "#dma,updated angle state: %s"
+ "#findalgs,NRBYFindingContainer::process(const common::BodyState& bodyState) unexpectedly called but not overridden"
+ "#findalgs-channelsoundingitemfinder,process(const common::BodyState &bodyState)"
+ "#findalgs-findee, process(const common::BodyState &bodyState)"
+ "#findalgs-itemfinder,process(const common::BodyState &bodyState)"
+ "#findalgs-peoplefinder,process(const common::BodyState &bodyState)"
+ "#nrby-eng,#devicestate, cached device angle state index: %u"
+ "#nrby-eng,Get update interface angle: %.4f interfaceAngle, body uuid: %@, angleDegrees: %.4f"
+ "#nrby-eng,acceptBodyStateUpdate"
+ "#roseprovider,onCMDAStateChange,index,%u"
+ "#ses-container,Debug inject UUID: %{private}@, degrees: %.1f"
+ "#ses-container,Enable the inject device state debug path"
+ "#ses-container,Session should suspend - device angle %.4f > %.4f, suspending session"
+ "#ses-container,Suspension should end - device angle %.4f < %.4f, resuming session"
+ "#ses-container,Suspension should end, resuming session"
+ "#ses-container,UWB ranging for phone auto unlock not enable yet, return"
+ "99BD6B06-60F8-4C84-87E9-DC00E52EE31B"
+ "@\"<NIBodyIdentifiable>\""
+ "@\"CMAngleManager\""
+ "@\"NIBodyToken\""
+ "Antenna state response not of expected size"
+ "B306BF46-7EBA-48D3-A730-C667BF9799C0"
+ "Body updated: %{private}@, interfaceAngle = %{public}.0f°"
+ "BtThresholdScannerModelAdvertiserClassDeviceStateOffset"
+ "D6A60FD6-4DFA-466A-8F53-0929EF56D20B"
+ "DMA"
+ "Debug inject UUID: %{private}@, angleDegrees: %{public}.1f°"
+ "Device1,8240"
+ "Device1,8242"
+ "Device1,8245"
+ "Device1,8246"
+ "Device1,8247"
+ "Device1,8248"
+ "DeviceAngleNotSupported"
+ "NIBodyIdentifiable"
+ "NIBodyToken"
+ "NIDebugInjectDeviceAngleState"
+ "NIDeviceAngleSuspensionEndThreshold"
+ "NIDeviceAngleSuspensionStartThreshold"
+ "NIUUIDBodyIdentifiable"
+ "NIViewBodyIdentifiable"
+ "PRDeviceAngleStateMonitor"
+ "Set originBody: %{private}p"
+ "StateA"
+ "StateB"
+ "T@\"<NIBodyIdentifiable>\",&,N"
+ "T@\"NISession\",W,N,V_session"
+ "T@\"NSUUID\",R,N"
+ "Td,R,N"
+ "_angleManager"
+ "_bodyToken"
+ "_computeDeviceAngleAndViewBodyState"
+ "_currentDeviceViewBodyAngleState"
+ "_debugInjectFakeUUID:degrees:"
+ "_degreeHandlers"
+ "_didUpdateBody is called with an unknown body"
+ "_didUpdateBody:"
+ "_didUpdateBodyInternal:"
+ "_hasRealState"
+ "_init"
+ "_interfaceAngle"
+ "_motionBodyID"
+ "_notifyDegreeHandlersWithDegrees:"
+ "_notifyStateHandlersWithIndex:"
+ "_originBody"
+ "_session"
+ "_startUpdatingBodyToken:"
+ "_stateHandlers"
+ "_stopUpdatingBodyToken:"
+ "_systemAngelDegrees"
+ "_updateDeviceAngleDegrees:"
+ "_updateInterfaceAngle:forBodyWithUUID:"
+ "acceptBodyStateUpdate:"
+ "acceptDeviceState:"
+ "addAngleDegreesHandler:forClient:queue:deliverInitialState:"
+ "addAngleStateHandler:forClient:queue:deliverInitialState:"
+ "angleStateToIndex:"
+ "com.apple.proximity.device-angle-state-monitor"
+ "iPhone19,4"
+ "initDeviceAngleStateListener"
+ "isAngleValid"
+ "mechanicalAngleDegrees"
+ "originBody"
+ "removeHandlersForClient:"
+ "setOriginBody:"
+ "setSession:"
+ "sharedMonitor"
+ "startAngleUpdatesToQueue:handler:"
+ "stopAngleUpdates"
+ "teardownDeviceAngleStateListener"
+ "updateInterfaceAngle:forBodyWithUUID:angleDegrees:"
+ "v12@?0f8"
+ "v16@?0@\"CMAngle\"8"
+ "v24@0:8@\"NIBodyToken\"16"
+ "v28@0:8@\"NSUUID\"16f24"
+ "v32@0:8d16@\"NSUUID\"24"
+ "v36@0:8d16@24f32"
+ "v44@0:8@?16@24@32B40"
+ "valueWithNonretainedObject:"
+ "{optional<DeviceViewBodyAngleState>=\"\"(?=\"__null_state_\"c\"__val_\"{DeviceViewBodyAngleState=\"interfaceAngle\"{optional<double>=\"\"(?=\"__null_state_\"c\"__val_\"d)\"__engaged_\"B}\"bodyUUID\"@\"NSUUID\"\"angleDegrees\"{optional<float>=\"\"(?=\"__null_state_\"c\"__val_\"f)\"__engaged_\"B}})\"__engaged_\"B}"
+ "\xf0\xf0Q1"
+ "\xf0\xf0\xf4"
- "#roseprovider,CMAM is disabled"
- "\xf0\xf0!1"
- "\xf0\xf0\x94"
```
