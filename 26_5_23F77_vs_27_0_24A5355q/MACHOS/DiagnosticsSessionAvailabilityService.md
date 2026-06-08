## DiagnosticsSessionAvailabilityService

> `/System/Library/PrivateFrameworks/DiagnosticsSessionAvailability.framework/XPCServices/DiagnosticsSessionAvailabilityService.xpc/DiagnosticsSessionAvailabilityService`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0xb2a8
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_stubs: 0x1dc0
-  __TEXT.__objc_methlist: 0xef4
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x9de
-  __TEXT.__objc_classname: 0x21e
-  __TEXT.__objc_methname: 0x242b
-  __TEXT.__objc_methtype: 0x58a
-  __TEXT.__oslogstring: 0x7bd
-  __TEXT.__gcc_except_tab: 0x4bc
-  __TEXT.__unwind_info: 0x488
-  __DATA_CONST.__auth_got: 0x280
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x440
-  __DATA_CONST.__cfstring: 0x980
-  __DATA_CONST.__objc_classlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x48
+1351.0.0.0.0
+  __TEXT.__text: 0xb738
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_stubs: 0x1fc0
+  __TEXT.__objc_methlist: 0x1104
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0x448
+  __TEXT.__cstring: 0x9f1
+  __TEXT.__oslogstring: 0x9fc
+  __TEXT.__objc_classname: 0x24c
+  __TEXT.__objc_methname: 0x27b4
+  __TEXT.__objc_methtype: 0x700
+  __TEXT.__unwind_info: 0x428
+  __DATA_CONST.__const: 0x478
+  __DATA_CONST.__cfstring: 0x9a0
+  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_intobj: 0x1c8
+  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_intobj: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x2e38
-  __DATA.__objc_selrefs: 0x9a8
-  __DATA.__objc_ivar: 0x10c
-  __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0x360
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x178
+  __DATA.__objc_const: 0x3490
+  __DATA.__objc_selrefs: 0xab0
+  __DATA.__objc_ivar: 0x12c
+  __DATA.__objc_data: 0x500
+  __DATA.__data: 0x420
   __DATA.__bss: 0x40
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/HomeKit.framework/HomeKit
   - /System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit
-  - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
-  - /System/Library/PrivateFrameworks/EnhancedLoggingState.framework/EnhancedLoggingState
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D08D5091-0E56-3146-A1BC-C69F049637DD
-  Functions: 305
-  Symbols:   199
-  CStrings:  751
+  UUID: D6F90D4C-5430-3835-A388-3D62D69113C2
+  Functions: 331
+  Symbols:   202
+  CStrings:  820
 
Symbols:
+ _HMAccessoryCategoryTypeHomePod
+ _OBJC_CLASS_$_CBDiscovery
+ _OBJC_CLASS_$_DADeviceObserverHomePod
+ _OBJC_CLASS_$_HMHomeManager
+ _OBJC_CLASS_$_HMMutableHomeManagerConfiguration
+ _OBJC_METACLASS_$_DADeviceObserverHomePod
+ _dispatch_after
+ _dispatch_group_notify
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x4
- _BluetoothAvailabilityChangedNotification
- _BluetoothPairedStatusChangedNotification
- _OBJC_CLASS_$_BluetoothManager
- _OBJC_CLASS_$_ELSManager
- __os_log_fault_impl
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_sync
- _kDSDefaultsEnhancedLoggingStatusKey
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
CStrings:
+ "@\"CBDiscovery\""
+ "@\"HMHomeManager\""
+ "@\"NSObject<OS_dispatch_group>\""
+ "Activated bluetooth paired device discovery with error %@"
+ "BluetoothDevice (%@) is servicable: (%d) isAppleAirPodsDevice: (%d) allowed: (%d)"
+ "DADeviceAirPodsDeviceKey"
+ "DADeviceHomePodProxy"
+ "DADeviceObserverHomePod"
+ "Failed to force discover paired bluetooth devices with error %@"
+ "Found new bluetooth device %@ while observing for AirPods"
+ "HMAccessoryDelegate"
+ "HMHomeManagerDelegate"
+ "HomePod: Begin discovering devices"
+ "HomePod: Begin observing"
+ "HomePod: Did find %lu devices"
+ "HomePod: End discovering devices"
+ "HomePod: End observing"
+ "HomePod: No homes configured in HomeKit"
+ "HomePod: Observer Ready"
+ "HomePod: Performing initial scan with %lu homes"
+ "HomePod: Processing home '%@' with %lu accessories"
+ "HomePod: devices changed on IDS service"
+ "HomePod: discoverAllDevices"
+ "HomePod: homeManagerDidUpdateHomes called - Status: %ld, Homes: %lu"
+ "Lost bluetooth device %@ is a supported AirPods device. Removing."
+ "Lost bluetooth device %@ while observing for AirPods"
+ "New bluetooth device %@ is a supported AirPods device. Adding."
+ "Removing Bluetooth device: %@"
+ "Returning session status active to client PID %d"
+ "T@\"CBDiscovery\",&,N,V_btPairedDeviceDiscovery"
+ "T@\"HMHomeManager\",&,N,V_homeManager"
+ "T@\"NSObject<OS_dispatch_group>\",&,N,V_resultsFoundGroup"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_workQueue"
+ "TB,N,V_discoveryComplete"
+ "[DADiagnosticsSessionAvailabilityService] Discovering devices..."
+ "_bluetoothDeviceFound:"
+ "_bluetoothDeviceLost:"
+ "_btPairedDeviceDiscovery"
+ "_createDeviceWithHMAccessory:"
+ "_discoveryComplete"
+ "_homeManager"
+ "_isHomePodAccessory:"
+ "_lookForHomePodsInHome:"
+ "_removeAirpodsDevice:"
+ "_resultsFoundGroup"
+ "_scanForHomePods"
+ "_workQueue"
+ "accessories"
+ "accessory:didAddProfile:"
+ "accessory:didRemoveProfile:"
+ "accessory:didUpdateAssociatedServiceTypeForService:"
+ "accessory:didUpdateFirmwareVersion:"
+ "accessory:didUpdateNameForService:"
+ "accessory:service:didUpdateValueForCharacteristic:"
+ "accessoryDidUpdateName:"
+ "accessoryDidUpdateReachability:"
+ "accessoryDidUpdateServices:"
+ "activateWithCompletion:"
+ "btPairedDeviceDiscovery"
+ "cancelTests"
+ "category"
+ "categoryType"
+ "com.apple.Diagnostics.AirPodsBluetoothStatusChanged"
+ "com.apple.diagnostics.homepod.discovery"
+ "defaultPrivateConfiguration"
+ "deviceFlags"
+ "devicesWithDiscoveryFlags:error:"
+ "discoveryComplete"
+ "homeManager"
+ "homeManager:didAddHome:"
+ "homeManager:didReceiveAddAccessoryRequest:"
+ "homeManager:didRemoveHome:"
+ "homeManager:didUpdateAuthorizationStatus:"
+ "homeManagerDidUpdateHomes:"
+ "homeManagerDidUpdatePrimaryHome:"
+ "homes"
+ "initWithConfiguration:"
+ "initWithHMAccessory:"
+ "productID"
+ "resultsFoundGroup"
+ "serialNumberLeft"
+ "serialNumberRight"
+ "service:devicesChanged:"
+ "sessionStatusForIdentities:ticketNumber:timeout:completionHandler:"
+ "setBtPairedDeviceDiscovery:"
+ "setCachePolicy:"
+ "setDelegateQueue:"
+ "setDeviceFoundHandler:"
+ "setDeviceLostHandler:"
+ "setDiscoveryComplete:"
+ "setDiscoveryFlags:"
+ "setDispatchQueue:"
+ "setHomeManager:"
+ "setMaxConcurrentOperationCount:"
+ "setOptions:"
+ "setResultsFoundGroup:"
+ "setUnderlyingQueue:"
+ "setWorkQueue:"
+ "v16@?0@\"CBDevice\"8"
+ "v16@?0@\"NSError\"8"
+ "v24@0:8@\"HMAccessory\"16"
+ "v24@0:8@\"HMHomeManager\"16"
+ "v32@0:8@\"HMAccessory\"16@\"HMAccessoryProfile\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMService\"24"
+ "v32@0:8@\"HMAccessory\"16@\"NSString\"24"
+ "v32@0:8@\"HMHomeManager\"16@\"HMAddAccessoryRequest\"24"
+ "v32@0:8@\"HMHomeManager\"16@\"HMHome\"24"
+ "v32@0:8@\"HMHomeManager\"16Q24"
+ "v32@0:8@16@24"
+ "v32@0:8@16Q24"
+ "v40@0:8@\"HMAccessory\"16@\"HMService\"24@\"HMCharacteristic\"32"
+ "v40@0:8@16@24@32"
+ "workQueue"
- "-[DSDiagnosticsSessionAvailabilityService _getHasActiveEnhancedLoggingSessionWithCompletionHandler:]"
- "@\"BluetoothManager\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "AACPVersionInfo"
- "Active Enhanced Logging session: %d"
- "BluetoothDevice (%@) is servicable: (%d) appleAudioDevice: (%d) tempPaired: (%d) allowed: (%d)"
- "DADeviceObserverAirpods recieved notification that bluetooth statuses have changed. Looking for any new devices..."
- "Discovering devices..."
- "ELS status: %lu"
- "Removing Airpods device %@"
- "Returning session status activeDiagnostics to client PID %d"
- "Returning status activeEnhancedLogging to client PID %d"
- "T@\"BluetoothManager\",&,N,V_btManager"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_btManagerAvailableSemaphore"
- "Unhandled ELSStatus case: %lu"
- "_bluetoothPairingStatusChanged:"
- "_btManager"
- "_btManagerAvailable"
- "_btManagerAvailableSemaphore"
- "_enhancedLoggingStatusOverride"
- "_getHasActiveEnhancedLoggingSessionWithCompletionHandler:"
- "_purgeUnpairedDevices"
- "accessoryInfo"
- "airpodsDevice"
- "available"
- "btManager"
- "btManagerAvailableSemaphore"
- "enhancedLoggingStatus"
- "getEnhancedLoggingStatusWithCompletionHandler:"
- "isAppleAudioDevice"
- "isTemporaryPaired"
- "objectAtIndexedSubscript:"
- "paired"
- "pairedDevices"
- "productId"
- "refreshWithCompletion:"
- "removeObserver:name:object:"
- "sessionStatusForIdentities:ticketNumber:timeout:requestQueuedSuiteInfo:completionHandler:"
- "setBtManager:"
- "setBtManagerAvailableSemaphore:"
- "setSharedInstanceQueue:"
- "sharedManager"
- "v12@?0B8"
- "v24@0:8@?<v@?@\"NSNumber\">16"
- "v24@?0@\"ELSSnapshot\"8B16B20"

```
