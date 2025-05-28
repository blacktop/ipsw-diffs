## nearbyd

> `/usr/libexec/nearbyd`

```diff

-413.0.6.0.0
-  __TEXT.__text: 0x44ffd0
-  __TEXT.__auth_stubs: 0x2450
-  __TEXT.__objc_stubs: 0xf100
+415.0.7.0.1
+  __TEXT.__text: 0x452e90
+  __TEXT.__auth_stubs: 0x2480
+  __TEXT.__objc_stubs: 0xf440
   __TEXT.__init_offsets: 0x5c0
-  __TEXT.__objc_methlist: 0x81a8
-  __TEXT.__gcc_except_tab: 0x3d1c4
-  __TEXT.__const: 0x238e40
-  __TEXT.__cstring: 0x2ba89
-  __TEXT.__objc_methname: 0x16161
-  __TEXT.__oslogstring: 0x46a0a
-  __TEXT.__objc_classname: 0x14ea
-  __TEXT.__objc_methtype: 0x1a143
-  __TEXT.__unwind_info: 0x184ec
+  __TEXT.__objc_methlist: 0x8350
+  __TEXT.__gcc_except_tab: 0x3d6d0
+  __TEXT.__const: 0x238f00
+  __TEXT.__cstring: 0x2bc0c
+  __TEXT.__objc_methname: 0x166a5
+  __TEXT.__oslogstring: 0x46ce6
+  __TEXT.__objc_classname: 0x1531
+  __TEXT.__objc_methtype: 0x1a417
+  __TEXT.__unwind_info: 0x185b4
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x1240
-  __DATA_CONST.__got: 0x550
+  __DATA_CONST.__auth_got: 0x1258
+  __DATA_CONST.__got: 0x558
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x1f740
-  __DATA_CONST.__cfstring: 0xd9a0
-  __DATA_CONST.__objc_classlist: 0x3d0
+  __DATA_CONST.__const: 0x1f860
+  __DATA_CONST.__cfstring: 0xda60
+  __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x230
+  __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x2c8
   __DATA_CONST.__objc_arrayobj: 0x138
   __DATA_CONST.__objc_intobj: 0x468
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x13be0
-  __DATA.__objc_selrefs: 0x4520
+  __DATA.__objc_const: 0x140c8
+  __DATA.__objc_selrefs: 0x4608
   __DATA.__objc_protorefs: 0x70
-  __DATA.__objc_classrefs: 0x6d8
-  __DATA.__objc_superrefs: 0x398
-  __DATA.__objc_ivar: 0xfcc
-  __DATA.__objc_data: 0x2620
-  __DATA.__data: 0x2e24
-  __DATA.__bss: 0xcda0
+  __DATA.__objc_classrefs: 0x6e8
+  __DATA.__objc_superrefs: 0x3a0
+  __DATA.__objc_ivar: 0x1014
+  __DATA.__objc_data: 0x26c0
+  __DATA.__data: 0x2ea4
+  __DATA.__bss: 0xcdd0
   __DATA.__common: 0xec8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 20827
-  Symbols:   876
-  CStrings:  14947
+  Functions: 20885
+  Symbols:   880
+  CStrings:  15028
 
Symbols:
+ _XPC_ACTIVITY_CHECK_IN
+ _sleep
+ _xpc_activity_copy_criteria
+ _xpc_activity_set_criteria
CStrings:
+ "\x04"
+ "\x14"
+ "\x16\x11\x12Z%"
+ "!\x12\xd1\x12"
+ "!\x12\xf0!a\xa2\xf0\xe1"
+ "#bt-accessory,AddServiceListener: existing listener [%@] for peer [%@]"
+ "#bt-accessory,AddServiceListener: new listener [%@] for existing peer [%@]. State: %s. Result: %s. Previous listener count: %d"
+ "#bt-accessory,AddServiceListener: new listener [%@] for new peer [%@]"
+ "#bt-accessory,BackgroundAuthorization: listener [%@] for peer [%@] NOT authorized"
+ "#bt-accessory,BackgroundAuthorization: listener [%@] for peer [%@] NOT authorized. Re-discover services"
+ "#bt-accessory,BackgroundAuthorization: listener [%@] for peer [%@] authorized"
+ "#bt-accessory,ConnectToPeer [%@]: BT not available"
+ "#bt-accessory,ConnectToPeer [%@]: Paired and connected. Establishing a local connection"
+ "#bt-accessory,ConnectToPeer [%@]: already finished"
+ "#bt-accessory,ConnectToPeer [%@]: not already connected"
+ "#bt-accessory,ConnectToPeer [%@]: not paired"
+ "#bt-accessory,ConnectToPeer [%@]: wait for CBManager state update"
+ "#bt-accessory,RemoveServiceListener: listener [%@] for peer [%@]. Listener count after removal: %d"
+ "#bt-accessory,centralManager:didConnectPeripheral [%@]: No matching peer"
+ "#bt-accessory,centralManager:didConnectPeripheral [%@]: Success"
+ "#bt-accessory,centralManager:didConnectPeripheral [%@]: Unexpected connection success"
+ "#bt-accessory,centralManager:didDisconnectPeripheral [%@]: Error: %@"
+ "#bt-accessory,centralManager:didDisconnectPeripheral [%@]: No matching peer. Error: %@"
+ "#bt-accessory,centralManager:didFailToConnectPeripheral [%@]: Error: %@"
+ "#bt-accessory,centralManager:didFailToConnectPeripheral [%@]: No matching peer. Error: %@"
+ "#bt-accessory,centralManager:didFailToConnectPeripheral [%@]: Unexpected connection failure: %@"
+ "#bt-accessory,centralManagerDidUpdateState: %s"
+ "#bt-accessory,peripheral:didDiscoverCharacteristics [%@]: %d characteristics discovered"
+ "#bt-accessory,peripheral:didDiscoverCharacteristics [%@]: Characteristics not discovered"
+ "#bt-accessory,peripheral:didDiscoverCharacteristics [%@]: Error discovering characteristics: %@"
+ "#bt-accessory,peripheral:didDiscoverCharacteristics [%@]: No matching peer. Error: %@"
+ "#bt-accessory,peripheral:didDiscoverCharacteristics [%@]: Unexpected characteristic discovery. Error: %@"
+ "#bt-accessory,peripheral:didDiscoverServices [%@]: Error discovering service: %@"
+ "#bt-accessory,peripheral:didDiscoverServices [%@]: No matching peer. Error: %@"
+ "#bt-accessory,peripheral:didDiscoverServices [%@]: Service not discovered"
+ "#bt-accessory,peripheral:didDiscoverServices [%@]: Success"
+ "#bt-accessory,peripheral:didDiscoverServices [%@]: Unexpected service discovery. Error: %@"
+ "#bt-accessory,peripheral:didUpdateValueForCharacteristic [%@]: Error: %@"
+ "#bt-accessory,peripheral:didUpdateValueForCharacteristic [%@]: No matching peer. Error: %@"
+ "#bt-accessory,peripheral:didUpdateValueForCharacteristic [%@]: Read %d characteristics, %d left to go"
+ "#bt-accessory,peripheral:didUpdateValueForCharacteristic [%@]: Unexpected characteristic update. Error: %@"
+ "#find-range,#crypto Reset state. Failures: %{public}d. Reset: %{public}d"
+ "#find-ses,%{public}@"
+ "#find-ses,Add observer to relay: %{public}@"
+ "#find-ses,Configure [%{public}@]: %{public}@"
+ "#find-ses,Dealloc [%{public}@]"
+ "#find-ses,Delivered first update [%{public}@]. Range: %{public}0.2f"
+ "#find-ses,FindingServicePool provide service for token: %{public}@"
+ "#find-ses,FindingServicePool remove service for token: %{public}@"
+ "#find-ses,FindingServicePool replace nil service for token: %{public}@. Race condition (OK)"
+ "#find-ses,FindingServicePool replace non-nil service for token: %{public}@. Race condition (probably not OK)"
+ "#find-ses,Invalidate [%{public}@]"
+ "#find-ses,Pause [%{public}@]"
+ "#find-ses,Remove observer from relay: %{public}@"
+ "#find-ses,Remove stale observer from relay: %{public}@"
+ "#find-ses,Run [%{public}@]. Process: %{private}@"
+ "#find-ses,Service [%{public}@] canceled pending pause"
+ "#find-ses,Service add client %{public}@ (%{public}d previous clients)"
+ "#find-ses,Service client %{public}@ updated its run state to %{public}d (previous %{public}d). Service state: %{public}s. Is any client running %{public}d"
+ "#find-ses,Service deallocated (%{public}@)"
+ "#find-ses,Service initialized (%{public}@)"
+ "#find-ses,Service removing client %{public}@ (%{public}d clients before removal)"
+ "#find-ses,Update configuration [%{public}@]\nOld: %{public}@\nNew: %{public}@"
+ "#find-ses,Update service after removing client %{public}@. Service state: %{public}s. Is any client running %{public}d"
+ "#findalgs-findee, Clearing step history because motion activity changed to stationary"
+ "#findalgs-peoplefinder,#convergence_blending, Insufficient Displacement: SA: %d, PF: %d, SAVIO: %d, Blended: %d"
+ "#findalgs-peoplefinder,#convergence_blending, Insufficient Horizontal Displacement: SA: %d, PF: %d, SAVIO: %d, Blended: %d"
+ "#gri,%s,tracked_ratio,%.1lf,has_good_gnss_conditions,%d"
+ "#halt-exec-PRRose halt PRRose execution due to HaltPRRoseOnFatalError override"
+ "#halt-exec-PRRose halt PRRose execution due to HaltPRRoseOnFatalErrorReason override: %@"
+ "#nrby-eng,Finding range result latency report. measDelta: %{public}0.3f [s]. processDelta: %{public}0.3f [s]. Excess ms: %{public}d. Accumulated excess ms: %{public}d"
+ "#nrby-eng,Overriding GRI parameter, minSvTrackedToAvailableRatioForFavorableGnssConditions: %.2lf"
+ "#ota,%s bool override. Config file key: %@. Defaults key: %@. Value: %d"
+ "#sa_algo_batchfilter,SyntheticApertureBatchFilter constructed. Strict box span requirement %d, third party behavior %d"
+ "#sa_algo_batchfilter_with,SyntheticApertureBatchFilterWithFindeeVIO constructed. Strict box span requirement %d, third party behavior %d"
+ "#ses-container,Unable to run session due to activation failure. Activation error code: %ld"
+ "#ses-ecosystem,Bluetooth device %@. BG authorized? %s"
+ "%{public}@"
+ "-[NIServerAccessoryGATTServiceManager _connectToPeer:]"
+ "-[NIServerAccessoryGATTServiceManager _isListener:backgroundAuthorizedForPeer:]"
+ "-[NIServerAccessoryGATTServiceManager peripheral:didDiscoverCharacteristicsForService:error:]"
+ "-[NIServerAccessoryGATTServiceManager peripheral:didUpdateValueForCharacteristic:error:]"
+ "-[NIServerHomeDeviceSession _calculateMagneticFieldBias]"
+ "-[NIServerNearbyAccessorySession accessoryFailedWithError:]"
+ "-[NIServerNearbyAccessorySession accessoryUpdatedBackgroundAuthorization:]"
+ "/AppleInternal/Library/BuildRoots/5ae9d77c-6742-11ee-a800-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/5ae9d77c-6742-11ee-a800-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "@\"<NIServerAccessoryGATTServiceListener>\""
+ "AlishaTestMode_R1"
+ "AlishaTestMode_R2"
+ "BluetoothNotAvailable"
+ "ConfigCharacteristicsRead"
+ "DidFindeeChangeFloors"
+ "DidFinderChangeFloors"
+ "FMSTARFGC"
+ "Failure"
+ "FindeeIsPhone"
+ "FindeeMinSvTrackedToAvailableRatioForFavorableGnssConditions"
+ "FinderIsPhone"
+ "HaltPRRoseOnFatalError"
+ "HaltPRRoseOnFatalErrorReason"
+ "Initial"
+ "ListenerTracking"
+ "Log Collection Error"
+ "NIServerAccessoryGATTServiceListener"
+ "NIServerAccessoryGATTServiceManager"
+ "NIServerAccessoryGATTServiceManager.mm"
+ "PMSTARFGC"
+ "PRRose Reconfigured. Reenter deep sleep"
+ "PRRose UWB not allowed. Power off rose"
+ "PRRose power down Rose after regulatory disallowment"
+ "PRRose reconfigure Rose from deep sleep"
+ "PRRose waking Rose from DSLP to properly power down"
+ "PeerTracking"
+ "PeopleFinderMinSvTrackedToAvailableRatioForFavorableGnssConditions"
+ "T#,&,N,V_exportedObjectClass"
+ "T@\"<NIServerAccessoryGATTServiceListener>\",W,N,V_listener"
+ "T@\"CBPeripheral\",&,N,V_peripheral"
+ "T@\"NIConfiguration\",&,N,V_configuration"
+ "T@\"NSError\",&,N,V_resultError"
+ "T@\"NSMutableSet\",&,N,V_listeners"
+ "T@\"NSMutableSet\",&,N,V_resultConfigCharacteristics"
+ "T@\"NSUUID\",&,N,V_peerIdentifier"
+ "T@,W,N,V_exportedObject"
+ "TC,N,V_connectionResult"
+ "TC,N,V_connectionState"
+ "Ti,N,V_numCharacteristicsLeftToRead"
+ "TimeToFirstPeerLocationFromFMF"
+ "TimeToFirstPeerLocationFromFindeeData"
+ "Triggering crashlog failed"
+ "WaitingForManagerStateUpdate"
+ "WaitingToConnect"
+ "WaitingToDiscoverNICharacteristics"
+ "WaitingToDiscoverNIService"
+ "WaitingToReadNIConfigCharacteristic"
+ "_activationError"
+ "_bleProviderSessionIRK"
+ "_bleProviderSessionIdentifier"
+ "_calMFbuf"
+ "_calculateMagneticFieldBias"
+ "_connectToPeer:"
+ "_connectionResult"
+ "_connectionState"
+ "_didFindeeChangeFloor"
+ "_didFinderChangeFloor"
+ "_estMagneticFieldBias"
+ "_exportedObjectClass"
+ "_isListener:backgroundAuthorizedForPeer:"
+ "_lastDisplacementSourceFindee"
+ "_listener"
+ "_maxYCoordinateFindee"
+ "_maxYCoordinateFinder"
+ "_minYCoordinateFindee"
+ "_minYCoordinateFinder"
+ "_numCharacteristicsLeftToRead"
+ "_peer:didFailWithError:"
+ "_peerDevices"
+ "_peerDevices[peerIdentifier].connectionResult == ConnectionResult::ConfigCharacteristicsRead"
+ "_peerDevices[peerIdentifier].connectionState == ConnectionState::Finished"
+ "_rawMFbuf"
+ "_resultConfigCharacteristics"
+ "_resultError"
+ "accessoryFailedWithError:"
+ "accessoryUpdatedBackgroundAuthorization:"
+ "activateWithDelegate:delegateQueue:sessionIRK:sessionIdentifier:controlFlags:tokenFlags:"
+ "addServiceListener:withIdentifier:forBluetoothPeer:withConfiguration:"
+ "cancelPeripheralConnection:"
+ "cbState == CBManagerStatePoweredOn"
+ "com.apple.CarKeysTests"
+ "com.apple.CarKeysTests.watchkitapp"
+ "com.apple.nearbyd.accessory.gatt-service"
+ "connectionResult"
+ "connectionState"
+ "didReceiveMagnetometerData:at:"
+ "exportedObjectClass"
+ "forwardInvocation:"
+ "instanceMethodSignatureForSelector:"
+ "latestCalMagneticFieldTime.has_value()"
+ "latestRawMagneticFieldTime.has_value()"
+ "listener"
+ "listeners"
+ "magneticField.size() == timestamps.size()"
+ "methodSignatureForSelector:"
+ "numCharacteristicsLeftToRead"
+ "peripheral"
+ "pushSample"
+ "removeServiceListenerWithIdentifier:"
+ "resultConfigCharacteristics"
+ "resultError"
+ "setConfiguration:"
+ "setConnectionResult:"
+ "setConnectionState:"
+ "setExportedObjectClass:"
+ "setListener:"
+ "setListeners:"
+ "setNumCharacteristicsLeftToRead:"
+ "setPeerIdentifier:"
+ "setPeripheral:"
+ "setResultConfigCharacteristics:"
+ "setResultError:"
+ "setService:forToken:"
+ "size"
+ "startDeviceMotionUpdatesUsingReferenceFrame:toQueue:withHandler:"
+ "timestamps.size() == magneticField.size()"
+ "v24@0:8#16"
+ "v24@?0@\"NSString\"8^B16"
+ "v32@0:8r^16d24"
+ "v32@?0@\"NSUUID\"8@\"PeerTracking\"16^B24"
+ "v54@0:8@\"<PRBLEDiscoveryConsuming>\"16@\"NSObject<OS_dispatch_queue>\"24@\"NSData\"32@\"NSData\"40{NIBluetoothDiscoveryControlFlags=BB}48I50"
+ "v54@0:8@16@24@32@40{NIBluetoothDiscoveryControlFlags=BB}48I50"
+ "{FindeeAlgorithmConfig={GnssReliabilityIndicatorConfig=dd}}16@0:8"
+ "{MagneticFieldDataBuffer=\"magneticField\"{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=\"__begin_\"^\"__end_\"^\"__end_cap_\"{__compressed_pair<float * __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=\"__value_\"^}}\"timestamps\"{vector<double, std::allocator<double>>=\"__begin_\"^d\"__end_\"^d\"__end_cap_\"{__compressed_pair<double *, std::allocator<double>>=\"__value_\"^d}}}"
+ "{PeopleFinderAlgorithmConfig=BBBBBBBddddd{ParticleFilterConfig=BBdqdddddddd}B{GnssReliabilityIndicatorConfig=dd}BdB}16@0:8"
+ "{optional<MagneticFieldBias>=\"\"(?=\"__null_state_\"c\"__val_\"{MagneticFieldBias=\"value\"\"time\"d})\"__engaged_\"B}"
+ "{optional<nearby::algorithms::finding::DisplacementSource>=\"\"(?=\"__null_state_\"c\"__val_\"i)\"__engaged_\"B}"
+ "\xf0\xf0B"
- "\x03\x14"
- "\x17i%"
- "!\x12\xd1\x13"
- "!\x12\xf0!a\xa2\xb1"
- "#bt-accessory,Cannot verify - CBManager not available"
- "#bt-accessory,Device: %@. Another config already being checked for background auth"
- "#bt-accessory,Device: %@. Check config for background auth."
- "#bt-accessory,Device: %@. Only Nearby Accessory supports background auth"
- "#bt-accessory,Discovered NI service. Discovering NI characteristics"
- "#bt-accessory,Discovered and triggered reads on %d configuration characteristics"
- "#bt-accessory,Failed to discover characteristics. Error: %@"
- "#bt-accessory,Failed to discover services. Error: %@"
- "#bt-accessory,Failed to locally connect"
- "#bt-accessory,Failed to update characteristic value. Error: %@"
- "#bt-accessory,Initialized CBManager, wait for state update"
- "#bt-accessory,Locally connected. Discovering NI service"
- "#bt-accessory,NI config characteristic: config matched"
- "#bt-accessory,NI config characteristic: config not matched"
- "#bt-accessory,NI config characteristic: length: %d bytes"
- "#bt-accessory,NI configuration characteristic NOT discovered"
- "#bt-accessory,NI service NOT discovered"
- "#bt-accessory,No CBManager - unexpected state update"
- "#bt-accessory,No CBManager or peripheral - unexpected characteristic discovery"
- "#bt-accessory,No CBManager or peripheral - unexpected characteristic update"
- "#bt-accessory,No CBManager or peripheral - unexpected connection failure"
- "#bt-accessory,No CBManager or peripheral - unexpected connection success"
- "#bt-accessory,No CBManager or peripheral - unexpected disconnection"
- "#bt-accessory,No CBManager or peripheral - unexpected service discovery"
- "#bt-accessory,None of the characteristics contained the session configuration data."
- "#bt-accessory,Not verifying auth - ignoring state update"
- "#bt-accessory,Not waiting for connection - unexpected connection failure"
- "#bt-accessory,Not waiting for connection - unexpected connection success"
- "#bt-accessory,Not waiting to discover NI characteristics - unexpected service characteristics"
- "#bt-accessory,Not waiting to discover NI service - unexpected service discovery"
- "#bt-accessory,Not waiting to read NI configuration characteristic - ignoring characteristic update"
- "#bt-accessory,Paired peripheral background setting enabled"
- "#bt-accessory,Peripheral %@ is NOT connected"
- "#bt-accessory,Peripheral %@ is NOT paired"
- "#bt-accessory,Peripheral %@ is already connected. Establishing a local connection"
- "#bt-accessory,Peripheral %@ is paired"
- "#bt-accessory,Peripheral disconnected"
- "#bt-accessory,Success! Configuration authorized with background operation."
- "#bt-accessory,This characteristic did not contain the session configuration data. %d left to read"
- "#bt-accessory,Wait for imminent CBManager state update"
- "#bt-accessory,centralManager:didConnectPeripheral: %@"
- "#bt-accessory,centralManager:didDisconnectPeripheral: %@ error: %@"
- "#bt-accessory,centralManager:didFailToConnectPeripheral: %@ error: %@"
- "#bt-accessory,centralManagerDidUpdateState: state %ld"
- "#bt-accessory,peripheral: %@ didDiscoverCharacteristicsForService: %@ error: %@"
- "#bt-accessory,peripheral: %@ didDiscoverServices: %@"
- "#bt-accessory,peripheral: %@ didUpdateValueForCharacteristic: %@ error: %@"
- "#find-range,#auth Never allowed to disable"
- "#find-range,#crypto Never allowed to disable"
- "#find-range,#crypto Reset state. Failures: %d. Reset: %d"
- "#find-ses,%@"
- "#find-ses,Add observer to relay: %@"
- "#find-ses,Configure [%@]: %@"
- "#find-ses,Dealloc [%@]"
- "#find-ses,Delivered first update [%@]. Range: %0.2f"
- "#find-ses,FindingServicePool provide service for token: %{private}@"
- "#find-ses,FindingServicePool remove service for token: %{private}@"
- "#find-ses,Invalidate [%@]"
- "#find-ses,Pause [%@]"
- "#find-ses,Remove observer from relay: %@"
- "#find-ses,Remove stale observer from relay: %@"
- "#find-ses,Run [%@]. Process: %{private}@"
- "#find-ses,Service [%{private}@] canceled pending pause"
- "#find-ses,Service add client %@ (%d previous clients)"
- "#find-ses,Service client %@ updated its run state to %d (previous %d). Service state: %s. Is any client running %d"
- "#find-ses,Service deallocated (%@)"
- "#find-ses,Service initialized (%@)"
- "#find-ses,Service removing client %@ (%d clients before removal)"
- "#find-ses,Update configuration [%@]\nOld: %@\nNew: %@"
- "#find-ses,Update service after removing client %@. Service state: %s. Is any client running %d"
- "#findalgs-peoplefinder,#convergence_blending, Insufficient Displacement: SA: %d, PF: %d, Blended: %d"
- "#findalgs-peoplefinder,#convergence_blending, Insufficient Horizontal Displacement: SA: %d, PF: %d, Blended: %d"
- "#gri,%s,num_svs,%ld,has_good_gnss_conditions,%d"
- "#ni-ca,Not calculating user moved distance with pose because of a VIO reset"
- "#nrby-eng,Finding range result latency report. measDelta: %0.3f [s]. processDelta: %0.3f [s]. Excess ms: %d. Accumulated excess ms: %d"
- "#nrby-eng,Overriding GRI parameter, minNumSatellitesForFavorableGnssConditions: %d"
- "#ota,%s bool override. Config file key: %@. Defaults key: %@. Value: %@"
- "#sa_algo_batchfilter,SyntheticApertureBatchFilter constructed. Strict box span requirement %d"
- "#sa_algo_batchfilter_with,SyntheticApertureBatchFilterWithFindeeVIO constructed. Strict box span requirement %d"
- "#ses-ecosystem,Bluetooth device %@. BG authorized? %s. Finalize running session..."
- "#ses-ecosystem,Could not create Bluetooth accessory manager"
- "-[NIServerBluetoothPairedAccessoryManager centralManager:didConnectPeripheral:]"
- "-[NIServerBluetoothPairedAccessoryManager centralManager:didDisconnectPeripheral:error:]"
- "-[NIServerBluetoothPairedAccessoryManager centralManager:didFailToConnectPeripheral:error:]"
- "-[NIServerBluetoothPairedAccessoryManager centralManagerDidUpdateState:]"
- "-[NIServerBluetoothPairedAccessoryManager checkBackgroundAuthorizationForConfiguration:authHandler:]"
- "-[NIServerBluetoothPairedAccessoryManager peripheral:didDiscoverCharacteristicsForService:error:]"
- "-[NIServerBluetoothPairedAccessoryManager peripheral:didDiscoverServices:]"
- "-[NIServerBluetoothPairedAccessoryManager peripheral:didUpdateValueForCharacteristic:error:]"
- "-[NIServerNearbyAccessorySession _handleBluetoothPairedAccessoryBackgroundAuth:]"
- "-[NIServerNearbyAccessorySession _handleBluetoothPairedAccessoryError:]"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "@\"NIServerBluetoothPairedAccessoryManager\""
- "@40@0:8@16@24@?32"
- "AlishaTestMode"
- "FMNSFGC"
- "Fatal crashlog callback not received"
- "FindeeMinNumSatellitesForFavorableGnssConditions"
- "IsFindeeAPhone"
- "NIServerBluetoothPairedAccessoryManager"
- "NIServerBluetoothPairedAccessoryManager.mm"
- "NonFatal crashlog callback not received"
- "PMNSFGC"
- "PeopleFinderMinNumSatellitesForFavorableGnssConditions"
- "T@,W,V_exportedObject"
- "Triggering crashlog collection failed"
- "_authVerificationState"
- "_bluetoothAccessoryManager"
- "_cbManager == central"
- "_cbManager.state == CBManagerStatePoweredOn"
- "_configData"
- "_errorHandler"
- "_handleBluetoothPairedAccessoryBackgroundAuth:"
- "_handleBluetoothPairedAccessoryError:"
- "_numberOfConfigCharacteristicsToRead"
- "_peripheral == peripheral"
- "activateWithDelegate:delegateQueue:controlFlags:tokenFlags:"
- "checkBackgroundAuthorizationForConfiguration:authHandler:"
- "configCharacteristicValue:doesContainConfigData:"
- "errorHandler"
- "initWithPeerIdentifier:queue:errorHandler:"
- "isFinderAPhone"
- "onActivity:withIdentifier:"
- "removeServiceForToken:"
- "v38@0:8@\"<PRBLEDiscoveryConsuming>\"16@\"NSObject<OS_dispatch_queue>\"24{NIBluetoothDiscoveryControlFlags=BB}32I34"
- "v38@0:8@16@24{NIBluetoothDiscoveryControlFlags=BB}32I34"
- "{FindeeAlgorithmConfig={GnssReliabilityIndicatorConfig=id}}16@0:8"
- "{PeopleFinderAlgorithmConfig=BBBBBBBddddd{ParticleFilterConfig=BBdqdddddddd}B{GnssReliabilityIndicatorConfig=id}Bd}16@0:8"

```
