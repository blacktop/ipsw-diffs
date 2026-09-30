## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/Contents/MacOS/BTAudioHALPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2700.43.0.0.0
-  __TEXT.__text: 0x92a8c
-  __TEXT.__auth_stubs: 0x1210
-  __TEXT.__objc_stubs: 0x1f00
+2700.46.1.1.0
+  __TEXT.__text: 0x93254
+  __TEXT.__auth_stubs: 0x1220
+  __TEXT.__objc_stubs: 0x1f20
   __TEXT.__init_offsets: 0xb4
   __TEXT.__objc_methlist: 0xcac
-  __TEXT.__gcc_except_tab: 0x27e0
-  __TEXT.__const: 0x1cbc
+  __TEXT.__gcc_except_tab: 0x2840
+  __TEXT.__const: 0x1cec
   __TEXT.__cstring: 0x539b
-  __TEXT.__oslogstring: 0x19b18
-  __TEXT.__objc_methname: 0x2956
+  __TEXT.__oslogstring: 0x19e35
+  __TEXT.__objc_methname: 0x2967
   __TEXT.__objc_classname: 0x112
   __TEXT.__objc_methtype: 0x7b4
-  __TEXT.__unwind_info: 0x2060
+  __TEXT.__unwind_info: 0x2090
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__const: 0x79d8
   __DATA_CONST.__cfstring: 0x1780

   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x918
+  __DATA_CONST.__auth_got: 0x920
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x1650
-  __DATA.__objc_selrefs: 0xa48
+  __DATA.__objc_selrefs: 0xa50
   __DATA.__objc_ivar: 0x130
   __DATA.__objc_data: 0x370
   __DATA.__data: 0xaa8
-  __DATA.__bss: 0x210e0
+  __DATA.__bss: 0x21120
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3273
-  Symbols:   424
-  CStrings:  3046
+  Functions: 3280
+  Symbols:   425
+  CStrings:  3048
 
Symbols:
+ _objc_autorelease
CStrings:
+ " %{private, mask.hash}@ : Injecting silent Audio allowed to stop [%llu  %d]"
+ "%{private, mask.hash}@ : Injecting silent Audio started"
+ "%{public}s Ownership Status : device %{private, mask.hash}s. Device Stream Status %{public}s"
+ "%{public}s sync mismatch warning:device %{private, mask.hash}s"
+ "A2DP : Volume received from bluetoothd: volume %f Device %{private, mask.hash}@"
+ "Add BTDevice to UnifiedAudioDevice : %{private, mask.hash}s "
+ "Asked to take ownership for %{private, mask.hash}s, but device no longer exists"
+ "Audio layer set volume %f, mScalarVolume %f, mScalarRemoteVolume %f, IsVolumeSupported %d, mIsAbsoluteVolume %d L/R : %f/%f Device %{private, mask.hash}@"
+ "Audio layer set volume Update %f, mScalarVolume %f, IsVolumeSupported %d, mIsAbsoluteVolume %d Device %{private, mask.hash}@"
+ "BT Virtual Device Starting IO on profile %{public}s, %llu to %{private, mask.hash}@ mAudioObjectID: %u Wait IO Start false, notify mode:%d, timestamp: %llu"
+ "BTAudioInputShimDevice: StopIO activeIO:%llu [%d] Transfering to Device  %{private, mask.hash}s"
+ "BTUnifiedAudioDevice: No profile/reason change [%{private, mask.hash}@ ] , profile %{public}s => %{public}s reason %{public}s = > %{public}s "
+ "BTUnifiedAudioDevice: No profile/reason change for AMP [%{private, mask.hash}@ ] , profile %{public}s => %{public}s reason %{public}s = > %{public}s "
+ "BTUnifiedAudioDevice: StartIO activeIO:%llu [%d] delegate to current Device  %{private, mask.hash}@"
+ "BTUnifiedAudioDevice: StopIO activeIO:%llu [%d] delegate Current Device  %{private, mask.hash}@"
+ "BTUnifiedAudioDevice: [%{private, mask.hash}@ ] Is route change pending ? %{public}s Current profile %{public}s "
+ "BTUnifiedAudioDevice: [%{private, mask.hash}@ ] Perform Route change for AMP, profile %{public}s => %{public}s reason %{public}s = > %{public}s "
+ "BTUnifiedAudioDevice: [%{private, mask.hash}@ ] Perform Route change, profile %{public}s => %{public}s reason %{public}s = > %{public}s "
+ "Current active USB-C device %{private, mask.hash}@ stream state changed to %@"
+ "Deleting BTUnifiedAudioDevice [%{private, mask.hash}@] ID = %d From Unified device list"
+ "Dropping Volume update becuase there is one already in flight %{private, mask.hash}@: manualVolumeUpdate: %@ Adaptive Volume: %@"
+ "Got stream state for non-routed device %{private, mask.hash}@  current routed device is %{private, mask.hash}@ stream state changed to %@"
+ "HFPInputShimDevice: StartIO activeIO:%llu [%d] transfering to device  %{private, mask.hash}@ Config Pending %d"
+ "LEAInputShimDevice: StartIO activeIO:%llu [%d] transfering to device  %{private}@"
+ "LECAInputShimDevice: StartIO activeIO:%llu [%d] transfering to device  %{private}@"
+ "LECAInputShimDevice: StopIO activeIO:%llu [%d] Transfering to Device  %{private}@"
+ "Notify Spatial Audio Mode via NowPlaying App changed: %{private, mask.hash}@"
+ "Ownership requested on disconnected device %{private, mask.hash}s"
+ "Post Publish UnifiedAudioDevice : %{private, mask.hash}@, %s"
+ "Publish UnifiedAudioDevice : %{private, mask.hash}@"
+ "Remote device set volume %f, mScalarVolume %f steps = [ %d ] , mDBVolume %f Notify Up : %{public}s Device %{private, mask.hash}@"
+ "Request For route Change: [%{private, mask.hash}@ ] profile %{public}s => %{public}s reason %{public}s = > %{public}s Calculated Transition:  %{public}s "
+ "Request Out of Band Audio : [%{private, mask.hash}@ ] profile %{public}s reason %{public}s "
+ "Sending relinquishing of ownership for %{private, mask.hash}s. Device is %{public}s streaming. TiPi Connection: %{public}s"
+ "SetProperty kBluetoothAudioDeviceWirelessSplitterAggregation creating aggregate device %{private, mask.hash}@"
+ "Starting IO on profile %{public}s, activeIO:%llu to %{private, mask.hash}@ mAudioObjectID: %u Wait IO Start %d"
+ "Taking ownership for %{private, mask.hash}s"
+ "Telling audioaccessoryd USB-C Device is PUBLISHED with UID %{private, mask.hash}@ is connected with BT address %{private, mask.hash}@"
+ "Telling audioaccessoryd USB-C Device is UNPUBLISHED with UID %{private, mask.hash}@ is with BT address %{private, mask.hash}@"
+ "Wireless Splitter Updating individual volume from MV [%f -> %f] MV = %f device %{private, mask.hash}@"
+ "Wireless Splitter stop for Audio Device %{private, mask.hash}@"
+ "Wireless Splitter, mAggregateDevices AudioObjectIDUser1 = %u User1UID = %{private, mask.hash}@ AudioObjectIDUser2 = %u User2UID = %{private, mask.hash}@"
+ "[%{private, mask.hash}@ ]  %{public}s, Profile Transport operation completed operaton type = %{public}s"
+ "[%{private, mask.hash}@ ] Request block Scheduling transport update"
+ "[%{private, mask.hash}@ ] Transport schedule already running"
+ "[%{private, mask.hash}@ ] Wait for transport update"
+ "[%{private, mask.hash}@ ] transport Update Completed"
+ "[%{private, mask.hash}@ ] transport update: timed out"
+ "[%{private, mask.hash}@] Can Unified Device be released : %{public}s"
+ "[%{private, mask.hash}@] Deleting BTAudioDevice %{private, mask.hash}s"
+ "[%{private, mask.hash}@] Deleting Internal BTAudioDevice %{private, mask.hash}s"
+ "[%{private, mask.hash}@] Received Status update from bluetoothd Status %d %d -> %d Notify HAL %@"
+ "[%{private, mask.hash}@] Update ownership state notification for %{private, mask.hash}s Bluetoothd as %{public}s"
+ "[%{private, mask.hash}@] UpdateSpatialConfigChange called with nil bundleID, ignoring spatial config update"
+ "[%{private, mask.hash}@] UpdateSpatialConfigChange called with null accessory device"
+ "getBundleIDFromPid: RBS lookup returned nil for pid %d, falling back to clientPIDTrackingMap"
+ "isEqualToNumber:"
- " %{public}@ : Injecting silent Audio allowed to stop [%llu  %d]"
- "%{public}@ : Injecting silent Audio started"
- "%{public}s Ownership Status : device %{public}s. Device Stream Status %{public}s"
- "%{public}s sync mismatch warning:device %{public}s"
- "A2DP : Volume received from bluetoothd: volume %f Device %{public}@"
- "Add BTDevice to UnifiedAudioDevice : %{public}s "
- "Asked to take ownership for %{public}s, but device no longer exists"
- "Audio layer set volume %f, mScalarVolume %f, mScalarRemoteVolume %f, IsVolumeSupported %d, mIsAbsoluteVolume %d L/R : %f/%f Device %{public}@"
- "Audio layer set volume Update %f, mScalarVolume %f, IsVolumeSupported %d, mIsAbsoluteVolume %d Device %{public}@"
- "BT Virtual Device Starting IO on profile %{public}s, %llu to %{public}@ mAudioObjectID: %u Wait IO Start false, notify mode:%d, timestamp: %llu"
- "BTAudioInputShimDevice: StopIO activeIO:%llu [%d] Transfering to Device  %{public}s"
- "BTUnifiedAudioDevice: No profile/reason change [%{public}@ ] , profile %{public}s => %{public}s reason %{public}s = > %{public}s "
- "BTUnifiedAudioDevice: No profile/reason change for AMP [%{public}@ ] , profile %{public}s => %{public}s reason %{public}s = > %{public}s "
- "BTUnifiedAudioDevice: StartIO activeIO:%llu [%d] delegate to current Device  %{public}@"
- "BTUnifiedAudioDevice: StopIO activeIO:%llu [%d] delegate Current Device  %{public}@"
- "BTUnifiedAudioDevice: [%{public}@ ] Is route change pending ? %{public}s Current profile %{public}s "
- "BTUnifiedAudioDevice: [%{public}@ ] Perform Route change for AMP, profile %{public}s => %{public}s reason %{public}s = > %{public}s "
- "BTUnifiedAudioDevice: [%{public}@ ] Perform Route change, profile %{public}s => %{public}s reason %{public}s = > %{public}s "
- "Current active USB-C device %{private}@ stream state changed to %@"
- "Deleting BTUnifiedAudioDevice [%{public}@] ID = %d From Unified device list"
- "Dropping Volume update becuase there is one already in flight %{public}@: manualVolumeUpdate: %@ Adaptive Volume: %@"
- "Got stream state for non-routed device %{private}@  current routed device is %{private}@ stream state changed to %@"
- "HFPInputShimDevice: StartIO activeIO:%llu [%d] transfering to device  %{public}@ Config Pending %d"
- "LEAInputShimDevice: StartIO activeIO:%llu [%d] transfering to device  %{public}@"
- "LECAInputShimDevice: StartIO activeIO:%llu [%d] transfering to device  %{public}@"
- "LECAInputShimDevice: StopIO activeIO:%llu [%d] Transfering to Device  %{public}@"
- "Notify Spatial Audio Mode via NowPlaying App changed: %{public}@"
- "Ownership requested on disconnected device %{public}s"
- "Post Publish UnifiedAudioDevice : %{public}@, %s"
- "Publish UnifiedAudioDevice : %{public}@"
- "Remote device set volume %f, mScalarVolume %f steps = [ %d ] , mDBVolume %f Notify Up : %{public}s Device %{public}@"
- "Request For route Change: [%{public}@ ] profile %{public}s => %{public}s reason %{public}s = > %{public}s Calculated Transition:  %{public}s "
- "Request Out of Band Audio : [%{public}@ ] profile %{public}s reason %{public}s "
- "Sending relinquishing of ownership for %{public}s. Device is %{public}s streaming. TiPi Connection: %{public}s"
- "SetProperty kBluetoothAudioDeviceWirelessSplitterAggregation creating aggregate device %{public}@"
- "Starting IO on profile %{public}s, activeIO:%llu to %{public}@ mAudioObjectID: %u Wait IO Start %d"
- "Taking ownership for %{public}s"
- "Telling audioaccessoryd USB-C Device is PUBLISHED with UID %{private}@ is connected with BT address %{private}@"
- "Telling audioaccessoryd USB-C Device is UNPUBLISHED with UID %{private}@ is with BT address %{private}@"
- "Wireless Splitter Updating individual volume from MV [%f -> %f] MV = %f device %{public}@"
- "Wireless Splitter stop for Audio Device %{public}@"
- "Wireless Splitter, mAggregateDevices AudioObjectIDUser1 = %u User1UID = %{public}@ AudioObjectIDUser2 = %u User2UID = %{public}@"
- "[%{public}@ ]  %{public}s, Profile Transport operation completed operaton type = %{public}s"
- "[%{public}@ ] Request block Scheduling transport update"
- "[%{public}@ ] Transport schedule already running"
- "[%{public}@ ] Wait for transport update"
- "[%{public}@ ] transport Update Completed"
- "[%{public}@ ] transport update: timed out"
- "[%{public}@] Can Unified Device be released : %{public}s"
- "[%{public}@] Deleting BTAudioDevice %{public}s"
- "[%{public}@] Deleting Internal BTAudioDevice %{public}s"
- "[%{public}@] Received Status update from bluetoothd Status %d %d -> %d Notify HAL %@"
- "[%{public}@] Update ownership state notification for %{public}s Bluetoothd as %{public}s"
- "[%{public}@] UpdateSpatialConfigChange called with nil bundleID, ignoring spatial config update"
- "[%{public}@] UpdateSpatialConfigChange called with null accessory device"
```
