## FMIPCore

> `/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore`

```diff

-375.20.0.0.0
-  __TEXT.__text: 0x1f4d6c
-  __TEXT.__auth_stubs: 0x2460
+377.17.0.0.0
+  __TEXT.__text: 0x20b908
+  __TEXT.__auth_stubs: 0x2480
   __TEXT.__objc_methlist: 0x2e4
-  __TEXT.__const: 0x101c4
-  __TEXT.__cstring: 0x11a72
-  __TEXT.__swift5_typeref: 0x3abd
-  __TEXT.__swift5_fieldmd: 0x5650
-  __TEXT.__constg_swiftt: 0x5d88
-  __TEXT.__swift5_reflstr: 0x4d41
-  __TEXT.__swift5_builtin: 0x168
+  __TEXT.__const: 0x11374
+  __TEXT.__cstring: 0x12312
+  __TEXT.__swift5_typeref: 0x3f8b
+  __TEXT.__swift5_fieldmd: 0x5a70
+  __TEXT.__constg_swiftt: 0x62c0
+  __TEXT.__swift5_reflstr: 0x4f81
+  __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__swift5_assocty: 0xcf0
-  __TEXT.__swift5_capture: 0x2f7c
+  __TEXT.__swift5_capture: 0x3040
   __TEXT.__swift5_protos: 0x68
-  __TEXT.__swift5_proto: 0xcd4
-  __TEXT.__swift5_types: 0x540
-  __TEXT.__unwind_info: 0x68a4
-  __TEXT.__eh_frame: 0x4a58
+  __TEXT.__swift5_proto: 0xde4
+  __TEXT.__swift5_types: 0x5a4
+  __TEXT.__unwind_info: 0x6c8c
+  __TEXT.__eh_frame: 0x4ce0
   __TEXT.__objc_classname: 0xa2
-  __TEXT.__objc_methname: 0x58df
+  __TEXT.__objc_methname: 0x59e1
   __TEXT.__objc_methtype: 0x1078
-  __DATA_CONST.__got: 0x5e8
-  __DATA_CONST.__const: 0x480
-  __DATA_CONST.__objc_classlist: 0x300
+  __DATA_CONST.__got: 0x608
+  __DATA_CONST.__const: 0x488
+  __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc338
-  __DATA_CONST.__objc_selrefs: 0xb68
+  __DATA_CONST.__objc_const: 0xc5b0
+  __DATA_CONST.__objc_selrefs: 0xbc0
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_classrefs: 0x220
-  __AUTH_CONST.__const: 0x146a8
+  __DATA_CONST.__objc_classrefs: 0x228
+  __AUTH_CONST.__const: 0x15010
   __AUTH_CONST.__objc_const: 0x158
-  __AUTH_CONST.__auth_got: 0x1230
-  __AUTH.__data: 0x49c8
-  __AUTH.__objc_data: 0xf10
-  __DATA.__objc_data: 0x360
-  __DATA.__data: 0x5d30
-  __DATA.__bss: 0x16100
-  __DATA.__common: 0x3b0
+  __AUTH_CONST.__auth_got: 0x1240
+  __AUTH.__data: 0x4f08
+  __AUTH.__objc_data: 0xfb0
+  __DATA.__objc_data: 0x3a8
+  __DATA.__data: 0x6178
+  __DATA.__bss: 0x18300
+  __DATA.__common: 0x3d0
   __DATA_DIRTY.__objc_data: 0x5d0
-  __DATA_DIRTY.__data: 0x34f0
+  __DATA_DIRTY.__data: 0x3600
   __DATA_DIRTY.__bss: 0x3000
   __DATA_DIRTY.__common: 0x250
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0288BC60-CC68-35D9-AD46-2629CB4BE071
-  Functions: 10981
-  Symbols:   361
-  CStrings:  2822
+  UUID: BE365B66-F407-36AB-A523-ABFA2BE49C5B
+  Functions: 11444
+  Symbols:   366
+  CStrings:  2879
 
Symbols:
+ _OBJC_CLASS_$_SPDeviceEvent
+ _SPBeaconLocationSourceDeviceAttachedLocation
+ _SPBeaconLocationSourceDeviceDetachedLocation
+ _SPBeaconLocationSourceDeviceDetectedLocation
+ _SPBeaconTypeLocalFindable
CStrings:
+ "'\n    isFindMyNetwork: '"
+ "/fmipservice/device/"
+ "Attempting to start accessory discovery"
+ "Attempting to start local findable accessory discovery"
+ "Attempting to stop accessory discovery"
+ "Attempting to stop local findable accessory discovery"
+ "BTF"
+ "FMIPBeaconRefreshingController: beacons received %s"
+ "FMIPBeaconRefreshingController: deviceEventUpdate: beaconUUID: %s, deviceEvent: %s: %s)"
+ "FMIPBeaconRefreshingController: deviceEventUpdateBlock fired <%s>"
+ "FMIPBeaconRefreshingController: unhandled beacon type!"
+ "FMIPCore.FMIPConnectAction"
+ "FMIPDataManager: Trimed location because it doesn't belong to anyone %{private}s"
+ "FMIPDevice:\n    -- id: %s,\n    -- name: %s,\n    -- baId: %s\n    -- isAccessory: %{bool}d\n    -- onlineLocation: %s\n    -- offlineLocation: %s\n    -- bestLocation: %s\n    -- itemGroup: %s\n    -- itemGroupItemsId: %s\n    -- shouldDisplaySeparatedLocation: %{bool}d\n    -- beaconType: %s\n    -- deviceConnectedType: %s\n    -- deviceAssociatedWithBeacon: %s"
+ "FMIPDeviceActionsController: Calling unpair for local findable beacons"
+ "FMIPDeviceActionsController: Not calling unpair for local findable beacons"
+ "FMIPDeviceActionsController: Starting remove device request"
+ "FMIPDeviceActionsController: Starting repair device request"
+ "FMIPDeviceActionsController: Unpair finished. With error? %s"
+ "FMIPDeviceActionsController: error received for repair request: %s"
+ "FMIPDeviceActionsController: repair device action completed successfully"
+ "FMIPManager: didReceive beaconTypes: %s"
+ "FMIPManager: didReceive deviceConnectedStates: %s"
+ "FMIPManager: didReceive offline finding device states."
+ "FMIPManager: didReceive updating state: %s: %s"
+ "FMIPManager: updating merged deviceConnectedStates: %s"
+ "FMIPUnknownItem: Initialized model: %s\nFMIPUnknownItem: isFindMyNetwork: %{bool}d\nFMIPUnknownItem: taskInfo -> play sound %s\nFMIPUnknownItem: taskInfo -> stop sound %s\nFMIPUnknownItem: allTaskInfo ->  %s"
+ "Localizable-B532"
+ "PENCIL_NOT_SUPPORTED"
+ "REP"
+ "Successfully started local findable acessory discovery."
+ "Successfully stopped local findable accessory discovery."
+ "Unable to start the local findable discovery session due to error: "
+ "Unable to stop the local findable discovery session due to error: "
+ "_TtC8FMIPCore17FMIPRepairRequest"
+ "_TtC8FMIPCore18FMIPRepairResponse"
+ "_TtC8FMIPCore22FMIPRepairDeviceAction"
+ "_TtC8FMIPCore24FMIPPrewarmConnectAction"
+ "_TtC8FMIPCore27FMIPPrewarmDisconnectAction"
+ "associatedDeviceUUID"
+ "attachedToDevice"
+ "attachmentInfo"
+ "beaconEventByBeaconIdentifier"
+ "beaconType"
+ "beaconTypes"
+ "btConnected"
+ "deviceConnectedState"
+ "deviceConnectedStates"
+ "deviceConnectedWithBeacon"
+ "disableURL"
+ "discoveryType"
+ "findingCapable"
+ "isAirTag"
+ "isFindMyNetwork"
+ "isPosh"
+ "repairReady"
+ "setDeviceEventUpdateBlock:"
+ "setReportDeviceEvents:"
+ "startLocalFindableAccessoryDiscoveryWithCompletion:"
+ "stopLocalFindableAccessoryDiscoveryWithCompletion:"
+ "v16@?0@\"SPDeviceEventFetchResult\"8"
- "FMIPDataManager: Trimed location because it doesn't belong to anymore %{private}s"
- "FMIPDevice:\n    -- id: %s,\n    -- name: %s,\n    -- baId: %s\n    -- isAccessory: %{bool}d\n    -- onlineLocation: %s\n    -- offlineLocation: %s\n    -- bestLocation: %s\n    -- itemGroup: %s\n    -- itemGroupItemsId: %s\n    -- shouldDisplaySeparatedLocation: %{bool}d"
- "FMIPDiscoveredAccessory: Trying to initialize using a SPDiscoveredAccessory with nil productInformation"
- "FMIPManager: didReceive locating states %@"
- "FMIPUnknownItem: Initialized model: %s\nFMIPUnknownItem: taskInfo -> play sound %s\nFMIPUnknownItem: taskInfo -> stop sound %s\nFMIPUnknownItem: allTaskInfo ->  %s"
- "_TtC8FMIPCore20FMIPDisconnectAction"

```
