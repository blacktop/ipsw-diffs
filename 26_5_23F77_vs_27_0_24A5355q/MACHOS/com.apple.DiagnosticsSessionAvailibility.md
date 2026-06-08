## com.apple.DiagnosticsSessionAvailibility

> `/System/Library/PrivateFrameworks/iOSDiagnostics.framework/XPCServices/com.apple.DiagnosticsSessionAvailibility.xpc/com.apple.DiagnosticsSessionAvailibility`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0xb6bc
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_stubs: 0x1ec0
-  __TEXT.__objc_methlist: 0xfe4
-  __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x494
-  __TEXT.__cstring: 0xa59
-  __TEXT.__oslogstring: 0x935
-  __TEXT.__objc_methname: 0x25a9
-  __TEXT.__objc_classname: 0x229
-  __TEXT.__objc_methtype: 0x5cf
-  __TEXT.__unwind_info: 0x4c0
-  __DATA_CONST.__auth_got: 0x2c0
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x528
-  __DATA_CONST.__cfstring: 0xc60
-  __DATA_CONST.__objc_classlist: 0x80
+1351.0.0.0.0
+  __TEXT.__text: 0xbefc
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_stubs: 0x2120
+  __TEXT.__objc_methlist: 0x1214
+  __TEXT.__objc_classname: 0x257
+  __TEXT.__objc_methname: 0x29ef
+  __TEXT.__objc_methtype: 0x76b
+  __TEXT.__cstring: 0xaea
+  __TEXT.__const: 0x60
+  __TEXT.__gcc_except_tab: 0x460
+  __TEXT.__oslogstring: 0xb8e
+  __TEXT.__unwind_info: 0x468
+  __DATA_CONST.__const: 0x570
+  __DATA_CONST.__cfstring: 0xca0
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_intobj: 0x180
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x2fa8
-  __DATA.__objc_selrefs: 0xa28
-  __DATA.__objc_ivar: 0x10c
-  __DATA.__objc_data: 0x500
-  __DATA.__data: 0x378
+  __DATA_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__got: 0x1a0
+  __DATA.__objc_const: 0x3650
+  __DATA.__objc_selrefs: 0xb48
+  __DATA.__objc_ivar: 0x130
+  __DATA.__objc_data: 0x550
+  __DATA.__data: 0x438
   __DATA.__bss: 0x50
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/HomeKit.framework/HomeKit
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit
   - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
-  - /System/Library/PrivateFrameworks/EnhancedLoggingState.framework/EnhancedLoggingState
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0AF3BFF0-CFAA-3505-95A0-56C2A6F53192
-  Functions: 316
-  Symbols:   230
-  CStrings:  821
+  UUID: F576B2CD-C1C4-3089-B080-3ECD8DB0C6AE
+  Functions: 349
+  Symbols:   240
+  CStrings:  902
 
Symbols:
+ _DAProductClassHomePod
+ _HMAccessoryCategoryTypeHomePod
+ _OBJC_CLASS_$_CBDiscovery
+ _OBJC_CLASS_$_DADeviceObserverHomePod
+ _OBJC_CLASS_$_HMHomeManager
+ _OBJC_CLASS_$_HMMutableHomeManagerConfiguration
+ _OBJC_METACLASS_$_DADeviceObserverHomePod
+ __os_feature_enabled_impl
+ _dispatch_after
+ _dispatch_group_notify
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _BluetoothAvailabilityChangedNotification
- _BluetoothPairedStatusChangedNotification
- _OBJC_CLASS_$_BluetoothManager
- _OBJC_CLASS_$_ELSManager
- _dispatch_group_wait
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x25
CStrings:
+ "@\"CBDiscovery\""
+ "@\"HMHomeManager\""
+ "@\"NSObject<OS_dispatch_group>\""
+ "Activated bluetooth paired device discovery with error %@"
+ "BluetoothDevice (%@) is servicable: (%d) isAppleAirPodsDevice: (%d) allowed: (%d)"
+ "Checking for availability..."
+ "DADeviceAirPodsDeviceKey"
+ "DADeviceHomePodProxy"
+ "DADeviceObserverHomePod"
+ "Diagnostics"
+ "Failed to force discover paired bluetooth devices with error %@"
+ "Found new bluetooth device %@ while observing for AirPods"
+ "HMAccessoryDelegate"
+ "HMHomeManagerDelegate"
+ "HomePod"
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
+ "IncludeHomePods"
+ "Lost bluetooth device %@ is a supported AirPods device. Removing."
+ "Lost bluetooth device %@ while observing for AirPods"
+ "New bluetooth device %@ is a supported AirPods device. Adding."
+ "Removing Bluetooth device: %@"
+ "T@\"CBDiscovery\",&,N,V_btPairedDeviceDiscovery"
+ "T@\"HMHomeManager\",&,N,V_homeManager"
+ "T@\"NSObject<OS_dispatch_group>\",&,N,V_resultsFoundGroup"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_workQueue"
+ "TB,N,V_discoveryComplete"
+ "[DADiagnosticsSessionAvailability] Discovering devices..."
+ "_bluetoothDeviceFound:"
+ "_bluetoothDeviceLost:"
+ "_btPairedDeviceDiscovery"
+ "_createDeviceWithHMAccessory:"
+ "_discoveryComplete"
+ "_homeManager"
+ "_isDiagnosticsCheckupDaemon"
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
+ "checkAvailabilityWithTicketNumber:timeout:exitWhenDone:isDiagnosticsCheckupDaemon:completion:"
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
+ "invalidate"
+ "productID"
+ "resultsFoundGroup"
+ "serialNumberLeft"
+ "serialNumberRight"
+ "service:devicesChanged:"
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
+ "v32@0:8@16Q24"
+ "v40@0:8@\"HMAccessory\"16@\"HMService\"24@\"HMCharacteristic\"32"
+ "v40@0:8@16@24@32"
+ "v48@0:8@16d24B32B36@?40"
+ "workQueue"
- "@\"BluetoothManager\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "AACPVersionInfo"
- "BluetoothDevice (%@) is servicable: (%d) appleAudioDevice: (%d) tempPaired: (%d) allowed: (%d)"
- "Checking for Enhanced Logging Session response"
- "DADeviceObserverAirpods recieved notification that bluetooth statuses have changed. Looking for any new devices..."
- "Discovering devices…"
- "ENHANCED_LOGGING_STATE"
- "No ELS response. Getting session ID"
- "Removing Airpods device %@"
- "Sending ELSResponse %@ in reply to checkAvailabilityWithReply"
- "T@\"BluetoothManager\",&,N,V_btManager"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_btManagerAvailableSemaphore"
- "_bluetoothPairingStatusChanged:"
- "_btManager"
- "_btManagerAvailable"
- "_btManagerAvailableSemaphore"
- "_purgeUnpairedDevices"
- "accessoryInfo"
- "airpodsDevice"
- "available"
- "btManager"
- "btManagerAvailableSemaphore"
- "checkAvailabilityWithTicketNumber:timeout:exitWhenDone:completion:"
- "checkEnhancedLoggingStateWithReply:"
- "isAppleAudioDevice"
- "isTemporaryPaired"
- "objectAtIndexedSubscript:"
- "paired"
- "pairedDevices"
- "productId"
- "refreshWithCompletion:"
- "removeObserver:name:object:"
- "setBtManager:"
- "setBtManagerAvailableSemaphore:"
- "setSharedInstanceQueue:"
- "sharedManager"
- "v16@?0@\"NSString\"8"
- "v24@?0@\"ELSSnapshot\"8B16B20"

```
