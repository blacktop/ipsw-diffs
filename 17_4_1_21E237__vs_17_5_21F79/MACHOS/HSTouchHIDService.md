## HSTouchHIDService

> `/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService`

```diff

-7140.17.0.0.0
-  __TEXT.__text: 0x1aa3d8
-  __TEXT.__auth_stubs: 0x1920
-  __TEXT.__objc_stubs: 0x46e0
+7150.1.0.0.0
+  __TEXT.__text: 0x1abce4
+  __TEXT.__auth_stubs: 0x1940
+  __TEXT.__objc_stubs: 0x4760
   __TEXT.__init_offsets: 0x1b68
-  __TEXT.__objc_methlist: 0x3634
-  __TEXT.__const: 0x4527
-  __TEXT.__gcc_except_tab: 0xd344
-  __TEXT.__cstring: 0x8ff0
-  __TEXT.__oslogstring: 0x2c19
-  __TEXT.__objc_methname: 0x4f60
+  __TEXT.__objc_methlist: 0x368c
+  __TEXT.__const: 0x45cf
+  __TEXT.__gcc_except_tab: 0xd490
+  __TEXT.__cstring: 0x90f2
+  __TEXT.__oslogstring: 0x2d12
+  __TEXT.__objc_methname: 0x4fdc
   __TEXT.__objc_classname: 0xa82
-  __TEXT.__objc_methtype: 0x6d10
-  __TEXT.__unwind_info: 0x909c
+  __TEXT.__objc_methtype: 0x6d8a
+  __TEXT.__unwind_info: 0x9114
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0xca0
+  __DATA_CONST.__auth_got: 0xcb0
   __DATA_CONST.__got: 0x208
   __DATA_CONST.__auth_ptr: 0x68
   __DATA_CONST.__const: 0x1da0
-  __DATA_CONST.__cfstring: 0x5e00
+  __DATA_CONST.__cfstring: 0x5e80
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_classrefs: 0x350
-  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_intobj: 0x360
   __DATA_CONST.__objc_arraydata: 0x268
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA.__objc_const: 0x76b0
-  __DATA.__objc_selrefs: 0x14d0
+  __DATA.__objc_selrefs: 0x14f0
   __DATA.__objc_ivar: 0x470
   __DATA.__objc_data: 0x1ea0
   __DATA.__data: 0x1438

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13143
-  Symbols:   53067
-  CStrings:  2971
+  Functions: 13160
+  Symbols:   53170
+  CStrings:  2989
 
Symbols:
+ -[EmbeddedTrackpadFirmwareManager handleSetPropertyEvent:]
+ -[HSTFrameParser _driverToHSTNotificationWithContext:]
+ -[HSTPadFirmwareManager _handleVendorEvent:]
+ -[HSTPadFirmwareManager _restoreFirmwareState]
+ -[HSTPadFirmwareManager handleConsume:]
+ -[TrackpadActuatorStage _openActuatorDevice]
+ -[TrackpadActuatorStage _updateHostClickControl]
+ -[TrackpadFirmwareManager handleSetPropertyEvent:]
+ GCC_except_table1030
+ GCC_except_table1043
+ GCC_except_table1060
+ GCC_except_table1075
+ GCC_except_table1088
+ GCC_except_table1120
+ GCC_except_table1150
+ GCC_except_table1168
+ GCC_except_table1177
+ GCC_except_table1192
+ GCC_except_table1206
+ GCC_except_table1215
+ GCC_except_table1231
+ GCC_except_table125
+ GCC_except_table126
+ GCC_except_table127
+ GCC_except_table130
+ GCC_except_table1344
+ GCC_except_table1375
+ GCC_except_table190
+ GCC_except_table203
+ GCC_except_table216
+ GCC_except_table375
+ GCC_except_table376
+ GCC_except_table396
+ GCC_except_table414
+ GCC_except_table481
+ GCC_except_table517
+ GCC_except_table533
+ GCC_except_table537
+ GCC_except_table538
+ GCC_except_table541
+ GCC_except_table542
+ GCC_except_table551
+ GCC_except_table570
+ GCC_except_table594
+ GCC_except_table612
+ GCC_except_table628
+ GCC_except_table638
+ GCC_except_table644
+ GCC_except_table648
+ GCC_except_table805
+ GCC_except_table825
+ GCC_except_table837
+ GCC_except_table848
+ GCC_except_table849
+ GCC_except_table869
+ GCC_except_table880
+ GCC_except_table881
+ GCC_except_table885
+ GCC_except_table891
+ GCC_except_table905
+ GCC_except_table911
+ GCC_except_table927
+ GCC_except_table928
+ GCC_except_table943
+ GCC_except_table953
+ GCC_except_table971
+ GCC_except_table998
+ OBJC_IVAR_$_TrackpadActuatorStage._displayState
+ _IORegistryEntrySetCFProperty
+ _MTActuatorHandoffHostClickControl
+ _MTDeviceEnableWorkIntervalNotification
+ _MTDeviceNotifyWorkInterval
+ __Block_byref_object_copy_.400
+ __Block_byref_object_dispose_.401
+ __Z4fminB8ue170006IdfENSt3__19enable_ifIXaasr3std13is_arithmeticIT_EE5valuesr3std13is_arithmeticIT0_EE5valueENS0_9__promoteIS2_S3_vEEE4type4typeES2_S3_
+ __ZL14supportsPencilP10__MTDevice
+ __ZN18MTForceManagement_10clearStateEb
+ __ZN18MTForceManagement_21appendForceStageEventEP12__IOHIDEvent21ForceStageEventStruct
+ __ZN19HSTFrameParserTypes10ReportCastIN11HSTPipeline17FirmwareInterface11InputReport24DriverNotificationHeaderEEEPKT_P6NSData
+ __ZN19HSTFrameParserTypes10ReportCastIN11HSTPipeline17FirmwareInterface11InputReport24DriverNotificationHeaderEEEPKT_PKvm
+ __ZN19HSTFrameParserTypes8TypeCastIN11HSTPipeline17FirmwareInterface11InputReport24DriverNotificationHeaderEEEPKT_PKvm
+ __ZNK20MTForceThresholding_18lastGlobalProgressEv
+ ___os_log_helper_16_2_2_8_64_8_0
+ ___os_log_helper_16_2_8_8_64_8_0_8_64_8_0_8_0_4_0_8_0_8_0
+ __cxx_global_var_init.172
+ _objc_msgSend$_driverToHSTNotificationWithContext:
+ _objc_msgSend$_openActuatorDevice
+ _objc_msgSend$_updateHostClickControl
+ _objc_msgSend$initWithFormat:
- -[TrackpadFirmwareManager _handleSetPropertyEvent:]
- GCC_except_table1014
- GCC_except_table1042
- GCC_except_table1059
- GCC_except_table1074
- GCC_except_table1087
- GCC_except_table1119
- GCC_except_table1149
- GCC_except_table1176
- GCC_except_table1191
- GCC_except_table1205
- GCC_except_table1221
- GCC_except_table128
- GCC_except_table1343
- GCC_except_table1367
- GCC_except_table189
- GCC_except_table202
- GCC_except_table205
- GCC_except_table215
- GCC_except_table373
- GCC_except_table394
- GCC_except_table416
- GCC_except_table476
- GCC_except_table507
- GCC_except_table516
- GCC_except_table523
- GCC_except_table532
- GCC_except_table535
- GCC_except_table536
- GCC_except_table540
- GCC_except_table546
- GCC_except_table565
- GCC_except_table576
- GCC_except_table589
- GCC_except_table607
- GCC_except_table633
- GCC_except_table823
- GCC_except_table826
- GCC_except_table843
- GCC_except_table844
- GCC_except_table876
- GCC_except_table878
- GCC_except_table886
- GCC_except_table889
- GCC_except_table909
- GCC_except_table925
- GCC_except_table969
- GCC_except_table989
- GCC_except_table997
- OBJC_IVAR_$_TrackpadActuatorStage._displayOff
- _MTActuatorRelinquishHostClickControl
- _MTActuatorRequestHostClickControl
- __Block_byref_object_copy_.388
- __Block_byref_object_dispose_.389
- __cxx_global_var_init.170
CStrings:
+ " buttonMask=%ld,"
+ "!header.imagePayloadLen || (header.imageFormattingOptions & FORMATTING_OPTIONS_IS_IMAGE_COMPRESSED) != 0 || header.imagePayloadLen == (_config.sensorSize.width * _config.sensorSize.height * sizeof(ImagePixel))"
+ "7150.1"
+ "@24@0:8r^{HSTSensingAlgsConfig=QQ@^{__MTDevice}}16"
+ "DeviceOpenedByEventSystem"
+ "Driver notification received: type=%x"
+ "Handing off host click control (deviceID 0x%llX)"
+ "Reclaiming host click control (deviceID 0x%llX)"
+ "Restoring firmware"
+ "S24@0:8r^{DriverNotificationHeader=CC}16"
+ "SA"
+ "TP"
+ "T{HSTSensingAlgsConfig=QQ@^{__MTDevice}},N,V_config"
+ "Work interval notification enabled"
+ "Work interval notification returned error: 0x%08X"
+ "Work interval notification unsupported"
+ "[%@] Dispatching digitizer event with %lu children,%@ _eventMask=0x%lx _childEventMask=0x%lx Cancel=%d Touching=%ld inRange=%ld"
+ "[%@] Dispatching motion gesture event with GestureType=%ld"
+ "[%@] Dispatching navigation swipe event with SwipeMask=%ld"
+ "[%@] Dispatching proximity event with ProximityDetectionMask=%ld"
+ "[HID] Skipping actuation - host click not enabled"
+ "^{__MTActuator={__CFRuntimeBase=QAQ}III^{__MTDevice}^{__CFDictionary}BQiIffff}"
+ "_displayState"
+ "_driverToHSTNotificationWithContext:"
+ "_openActuatorDevice"
+ "_updateHostClickControl"
+ "iPad handle device ready in state 0x%x"
+ "initWithFormat:"
+ "v48@0:8{HSTSensingAlgsConfig=QQ@^{__MTDevice}}16"
+ "{?=\"service\"{SendRight=\"_vptr$PortRight\"^^?\"_mp\"I}\"queue\"@\"NSObject<OS_dispatch_queue>\"\"dispatcher\"@\"<HIDEventDispatcher>\"\"cancelHandler\"@?\"device\"@\"source\"@\"NSObject<OS_dispatch_source>\"\"pipeline\"@\"HSStage\"\"recording\"@\"HSTRecordingManager\"\"sysdiagnoseNotifyToken\"i\"formatter\"@\"NSDateFormatter\"\"requestedProperties\"@\"NSArray\"\"recordedProperties\"@\"NSMutableArray\"\"recordedPropertiesCount\"@\"NSMutableDictionary\"\"cachedSetProperties\"@\"NSMutableArray\"\"debugProperties\"@\"NSMutableDictionary\"\"deviceID\"Q\"isTrackpad\"B\"supportsPencil\"B}"
+ "{HSTSensingAlgsConfig=\"maxPacketSize\"Q\"familyID\"Q\"frameworkString\"@\"NSString\"\"device\"^{__MTDevice}}"
+ "{HSTSensingAlgsConfig=QQ@^{__MTDevice}}16@0:8"
- "7140.17"
- "@24@0:8r^{HSTSensingAlgsConfig=QQ@}16"
- "Dispatching digitizer event with %lu children, _eventMask=0x%lx _childEventMask=0x%lx Cancel=%d Touching=%ld inRange=%ld"
- "Dispatching motion gesture event with GestureType=%ld"
- "Dispatching navigation swipe event with SwipeMask=%ld"
- "Dispatching proximity event with ProximityDetectionMask=%ld"
- "Display turned off - relinquishing host click control (deviceID 0x%llX)"
- "Display turned on - requesting host click control (deviceID 0x%llX)"
- "T{HSTSensingAlgsConfig=QQ@},N,V_config"
- "^{__MTActuator={__CFRuntimeBase=QAQ}III^{__MTDevice}^{__CFDictionary}BQiI}"
- "v40@0:8{HSTSensingAlgsConfig=QQ@}16"
- "{?=\"service\"{SendRight=\"_vptr$PortRight\"^^?\"_mp\"I}\"queue\"@\"NSObject<OS_dispatch_queue>\"\"dispatcher\"@\"<HIDEventDispatcher>\"\"cancelHandler\"@?\"device\"@\"source\"@\"NSObject<OS_dispatch_source>\"\"pipeline\"@\"HSStage\"\"recording\"@\"HSTRecordingManager\"\"sysdiagnoseNotifyToken\"i\"formatter\"@\"NSDateFormatter\"\"requestedProperties\"@\"NSArray\"\"recordedProperties\"@\"NSMutableArray\"\"recordedPropertiesCount\"@\"NSMutableDictionary\"\"cachedSetProperties\"@\"NSMutableArray\"\"debugProperties\"@\"NSMutableDictionary\"\"deviceID\"Q\"isTrackpad\"B}"
- "{HSTSensingAlgsConfig=\"maxPacketSize\"Q\"familyID\"Q\"frameworkString\"@\"NSString\"}"
- "{HSTSensingAlgsConfig=QQ@}16@0:8"

```
