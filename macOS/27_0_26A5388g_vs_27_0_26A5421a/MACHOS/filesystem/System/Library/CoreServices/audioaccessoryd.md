## audioaccessoryd

> `/System/Library/CoreServices/audioaccessoryd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`

```diff

-40.36.1.0.0
-  __TEXT.__text: 0x2404e4
-  __TEXT.__auth_stubs: 0x3700
-  __TEXT.__objc_stubs: 0x1b020
-  __TEXT.__objc_methlist: 0xcd34
-  __TEXT.__const: 0x4ed0
+40.41.1.0.1
+  __TEXT.__text: 0x242310
+  __TEXT.__auth_stubs: 0x3760
+  __TEXT.__objc_stubs: 0x1b180
+  __TEXT.__objc_methlist: 0xce4c
+  __TEXT.__const: 0x4f30
   __TEXT.__gcc_except_tab: 0x4ff4
-  __TEXT.__cstring: 0x4c1c3
-  __TEXT.__objc_classname: 0xf43
-  __TEXT.__objc_methname: 0x27205
-  __TEXT.__objc_methtype: 0x3d49
-  __TEXT.__oslogstring: 0x9fba
+  __TEXT.__cstring: 0x4c7e3
+  __TEXT.__objc_classname: 0xf93
+  __TEXT.__objc_methname: 0x273a5
+  __TEXT.__objc_methtype: 0x3e22
+  __TEXT.__oslogstring: 0xa02a
   __TEXT.__ustring: 0x10
-  __TEXT.__swift5_typeref: 0x1ee4
-  __TEXT.__constg_swiftt: 0x2104
-  __TEXT.__swift5_reflstr: 0x1bbb
-  __TEXT.__swift5_fieldmd: 0x1998
+  __TEXT.__swift5_typeref: 0x1ef6
+  __TEXT.__constg_swiftt: 0x2100
+  __TEXT.__swift5_reflstr: 0x1bab
+  __TEXT.__swift5_fieldmd: 0x19a8
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_assocty: 0x228
-  __TEXT.__swift5_capture: 0x1f94
+  __TEXT.__swift5_capture: 0x1f98
   __TEXT.__swift5_proto: 0x3a4
-  __TEXT.__swift5_types: 0x120
+  __TEXT.__swift5_types: 0x124
   __TEXT.__swift_as_entry: 0x7c
   __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift_as_cont: 0xe8
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x6770
+  __TEXT.__unwind_info: 0x67e0
   __TEXT.__eh_frame: 0x2d78
-  __DATA_CONST.__const: 0xc818
-  __DATA_CONST.__cfstring: 0xb000
-  __DATA_CONST.__objc_classlist: 0x368
+  __DATA_CONST.__const: 0xc920
+  __DATA_CONST.__cfstring: 0xb120
+  __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_intobj: 0x300
   __DATA_CONST.__objc_arraydata: 0x368
   __DATA_CONST.__objc_dictobj: 0x5c8
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA_CONST.__auth_got: 0x1b90
-  __DATA_CONST.__got: 0xe08
-  __DATA_CONST.__auth_ptr: 0x7b8
-  __DATA.__objc_const: 0x1c970
-  __DATA.__objc_selrefs: 0x7eb8
-  __DATA.__objc_ivar: 0x14ec
-  __DATA.__objc_data: 0x3258
-  __DATA.__data: 0x52b0
-  __DATA.__bss: 0x7630
+  __DATA_CONST.__auth_got: 0x1bc0
+  __DATA_CONST.__got: 0xe30
+  __DATA_CONST.__auth_ptr: 0x7c0
+  __DATA.__objc_const: 0x1cf18
+  __DATA.__objc_selrefs: 0x7f08
+  __DATA.__objc_ivar: 0x1508
+  __DATA.__objc_data: 0x32c0
+  __DATA.__data: 0x5360
+  __DATA.__bss: 0x7640
   __DATA.__common: 0x3a8
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10873
-  Symbols:   1519
-  CStrings:  14385
+  Functions: 10924
+  Symbols:   1529
+  CStrings:  14446
 
Symbols:
+ _CFDictionaryCreateMutable
+ _CFDictionarySetValue
+ _CFRunLoopAddSource
+ _CFRunLoopGetMain
+ _CFRunLoopRemoveSource
+ _CFUserNotificationCreateRunLoopSource
+ _kCFRunLoopCommonModes
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _kCFUserNotificationOtherButtonTitleKey
CStrings:
+ "!"
+ "-[AccessoryDiagnosticsMonitor _fileRadarForDevice:]"
+ "-[AccessoryDiagnosticsMonitor _handleBobbleAlertResponseForNotification:flags:]_block_invoke"
+ "-[AccessoryDiagnosticsMonitor _logPropertyChangesFrom:to:]"
+ "-[AccessoryDiagnosticsMonitor _showBobbleTurnedOffNotificationForDevice:]"
+ "1540729"
+ "@\"AccessoryDiagnosticsPendingAlert\""
+ "@40@0:8^{__CFUserNotification=}16^{__CFRunLoopSource=}24@32"
+ "AccessoryDiagnosticsMonitor"
+ "AccessoryDiagnosticsPendingAlert"
+ "AirPods Head Gestures Turned Off"
+ "Bobble Turned Off - File Radar tapped for device: %@"
+ "Bobble alert cancelled without File Radar. deviceId: %@"
+ "Bobble alert create failed. deviceId: %@, error: %d"
+ "Bobble alert dismissed via Do Not Ask Again. deviceId: %@"
+ "Bobble alert presented. deviceId: %@"
+ "Bobble alert runloop source create failed. deviceId: %@"
+ "Bobble alert suppressed by user preference. deviceId: %@"
+ "Bobble alert suppressed, another alert is already pending. deviceId: %@"
+ "Bobble unexpectedly turned off on %@ at %@"
+ "BobbleAlertDisabledByUser"
+ "BobbleDebugAlert"
+ "Bug"
+ "Cancel"
+ "Connected Audio - Cloud Sync | All"
+ "Count"
+ "Do Not Ask Again"
+ "Head gesture toggle changed for device: %@, from: %s, to: %s"
+ "Head gesture unexpectedly turned off for device: %@"
+ "Head gestures were unexpectedly disabled on %@? Please file a radar."
+ "Missing deviceConfiguration"
+ "No device found for identifier: %@"
+ "No matching reader for writer UUID %s; dropping sensor data"
+ "No pending Bobble alert found for notification response"
+ "Press Hold"
+ "Press Once"
+ "Received write sensor data message with %ld bytes from writer UUID %s"
+ "Registered read connection for device configuration: %s"
+ "SaveAllDevicesToPreference: Failed to unarchive existing devices: %@"
+ "SideToSide"
+ "T@\"NSString\",R,C,N,V_deviceIdentifier"
+ "T^{__CFRunLoopSource=},R,N,V_runLoopSource"
+ "T^{__CFUserNotification=},R,N,V_notification"
+ "UpAndDown"
+ "^{__CFRunLoopSource=}"
+ "^{__CFRunLoopSource=}16@0:8"
+ "^{__CFUserNotification=}16@0:8"
+ "_deviceIdentifier"
+ "_dismissPendingBobbleAlert"
+ "_fileRadarForDevice:"
+ "_handleBobbleAlertResponseForNotification:flags:"
+ "_logPropertyChangesFrom:to:"
+ "_notification"
+ "_pendingBobbleAlert"
+ "_runLoopSource"
+ "_showBobbleTurnedOffNotificationForDevice:"
+ "acceptReplyPlayPauseConfig changed for device: %@, from: %s, to: %s"
+ "addEntriesFromDictionary:"
+ "audiogramEnrolledTimestamp changed for device: %@, from: %@, to: %@"
+ "chargingReminderEnabled changed for device: %@, from: %s, to: %s"
+ "declineDismissSkipConfig changed for device: %@, from: %s, to: %s"
+ "healthKitDataWriteAllowed changed for device: %@, from: %s, to: %s"
+ "heartRateMonitorCapability changed for device: %@, from: %s, to: %s"
+ "initWithNotification:runLoopSource:deviceIdentifier:"
+ "listeningModeOffAllowed changed for device: %@, from: %s, to: %s"
+ "remoteCameraControlConfig changed for device: %@, from: %s, to: %s"
+ "runLoopSource"
+ "sharedDiagnosticsMonitor"
+ "v32@0:8^{__CFUserNotification=}16Q24"
- "IsSRConnectEligible: allowing low activity iPhone source to connect to Wx %@ which has no source connected and out of case > 5s"
- "IsSRConnectEligible: skip, iPhone source activity low and Wx already connected to a source, Wx %@"
- "IsSRConnectEligible: skip, low activity iPhone source but Wx %@ out of case <= 5s"
- "Received write sensor data message with %ld bytes"
- "Write = %s Reader = %s"
- "currentReaderConfiguration"
- "currentWriterConfiguration"
- "dataAvailable"
```
