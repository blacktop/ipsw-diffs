## wifivelocityd

> `/usr/libexec/wifivelocityd`

```diff

-1035.4.0.0.0
-  __TEXT.__text: 0xa2198
-  __TEXT.__auth_stubs: 0x1260
-  __TEXT.__objc_stubs: 0xd560
-  __TEXT.__objc_methlist: 0x4cb0
-  __TEXT.__const: 0x390
-  __TEXT.__objc_methname: 0xde3a
-  __TEXT.__oslogstring: 0xab8e
-  __TEXT.__cstring: 0xc160
-  __TEXT.__objc_classname: 0x835
-  __TEXT.__objc_methtype: 0x2354
-  __TEXT.__gcc_except_tab: 0x1838
+1050.25.0.0.0
+  __TEXT.__text: 0xa3884
+  __TEXT.__auth_stubs: 0x1250
+  __TEXT.__objc_stubs: 0xd420
+  __TEXT.__objc_methlist: 0x53f4
   __TEXT.__dlopen_cstrs: 0x2c2
+  __TEXT.__const: 0x398
+  __TEXT.__objc_methname: 0xdf29
+  __TEXT.__oslogstring: 0xadd1
+  __TEXT.__cstring: 0xc2a5
+  __TEXT.__objc_classname: 0x832
+  __TEXT.__objc_methtype: 0x2412
+  __TEXT.__gcc_except_tab: 0x188c
   __TEXT.__ustring: 0x8c
-  __TEXT.__unwind_info: 0x1b70
-  __DATA_CONST.__auth_got: 0x940
-  __DATA_CONST.__got: 0x588
+  __TEXT.__unwind_info: 0x1be8
+  __DATA_CONST.__auth_got: 0x938
+  __DATA_CONST.__got: 0x5a8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x2af8
-  __DATA_CONST.__cfstring: 0xb140
+  __DATA_CONST.__const: 0x2b28
+  __DATA_CONST.__cfstring: 0xb040
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x238
-  __DATA_CONST.__objc_intobj: 0xe58
+  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__objc_intobj: 0xe88
   __DATA_CONST.__objc_arraydata: 0x2470
   __DATA_CONST.__objc_dictobj: 0x14c8
   __DATA_CONST.__objc_arrayobj: 0x16b0
   __DATA_CONST.__objc_doubleobj: 0x80
-  __DATA.__objc_const: 0x9788
-  __DATA.__objc_selrefs: 0x3af8
-  __DATA.__objc_ivar: 0x6e0
+  __DATA.__objc_const: 0x8ba0
+  __DATA.__objc_selrefs: 0x3b70
+  __DATA.__objc_ivar: 0x6e4
   __DATA.__objc_data: 0x1770
   __DATA.__data: 0x660
-  __DATA.__bss: 0x138
+  __DATA.__bss: 0x130
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /System/Library/Frameworks/UserNotifications.framework/Versions/A/UserNotifications
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/Versions/A/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/BluetoothManager.framework/Versions/A/BluetoothManager
   - /System/Library/PrivateFrameworks/Bom.framework/Versions/A/Bom
   - /System/Library/PrivateFrameworks/ConfigurationProfiles.framework/Versions/A/ConfigurationProfiles
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
   - @rpath/BloodhoundKit.framework/Versions/A/BloodhoundKit
-  UUID: 411E3BE1-DDB8-3933-A87A-6A08A96F11E9
-  Functions: 2463
-  Symbols:   484
-  CStrings:  6753
+  UUID: B253E7F6-D508-3550-A6BA-8AD336F6D232
+  Functions: 2484
+  Symbols:   487
+  CStrings:  6749
 
Symbols:
+ _BluetoothAdvertisingStateChangedNotification
+ _BluetoothAvailabilityChangedNotification
+ _BluetoothConnectabilityChangedNotification
+ _BluetoothDiscoveryStateChangedNotification
+ _BluetoothPowerChangedNotification
+ _OBJC_CLASS_$_BluetoothManager
+ _OBJC_CLASS_$_CWFAssocParameters
+ _OBJC_CLASS_$_W5FeatureAvailability
- _NSPersistentStoreRemoteChangeNotification
- _OBJC_CLASS_$_IOBluetoothDevice
- _OBJC_CLASS_$_IOBluetoothHostController
- _OBJC_CLASS_$_NSDistributedNotificationCenter
- _notify_post
CStrings:
+ "-[W5DatabaseManager performFetch:]"
+ "-[W5Engine xpcConnection:associateToNetworkOnPeer:scanResult:configuration:reply:]_block_invoke_2"
+ "-[W5Engine xpcConnection:startNetworkDiscoveryOnPeer:configuration:reply:]_block_invoke_2"
+ "-[W5PeerInfraManager _requestHandler]_block_invoke"
+ "-[W5PeerInfraManager initWithPeerManager:statusManager:]"
+ "-[W5StatusManager associateToNetwork:configuration:reply:]_block_invoke"
+ "-[W5StatusManager scanForNetworksWithConfiguration:handler:]_block_invoke"
+ "-[W5WiFiInterface performScanWithParams:error:]"
+ "@\"BluetoothDevice\""
+ "@\"W5PeerInfraManager\""
+ "@\"WADeviceAnalyticsClient\""
+ "@48@0:8@16@24@32@?40"
+ "Class getWADeviceAnalyticsClientClass(void)_block_invoke"
+ "JoinError"
+ "JoinPassword"
+ "JoinTarget"
+ "ScanError"
+ "T@\"W5PeerGenericRequestListener\",R,N,V_listener"
+ "W5PeerInfraManager"
+ "W5PeerInfraManager.m"
+ "WADeviceAnalyticsClient"
+ "[wifivelocity] %s (%s:%u) Association request completed. Error: %@"
+ "[wifivelocity] %s (%s:%u) Association request on peer: %@ completed. Error: %@"
+ "[wifivelocity] %s (%s:%u) Attempting association to: %@ with parameters: %@"
+ "[wifivelocity] %s (%s:%u) CoreWiFi Scan failed. Error: %@"
+ "[wifivelocity] %s (%s:%u) Directed scan did not find network: %@"
+ "[wifivelocity] %s (%s:%u) Directed scan with pararmeters: %@ failed!"
+ "[wifivelocity] %s (%s:%u) Initiating a directed scan with parameters: %@"
+ "[wifivelocity] %s (%s:%u) Initiating scan with parameters: %@"
+ "[wifivelocity] %s (%s:%u) Scan request completed. Error: %@"
+ "[wifivelocity] %s (%s:%u) Scan request on peer: %@ completed. Error: %@"
+ "[wifivelocity] %s (%s:%u) Unsupported requested type"
+ "[wifivelocity] %s (%s:%u) W5InfraManager: Handle Request Type: %@"
+ "[wifivelocity] %s: failed to fetch %@ with %@"
+ "__deviceList"
+ "__handleBTAdvertisingNotification:"
+ "__handleBTAvailabilityNotification:"
+ "__handleBTConnectabiliyNotification:"
+ "__handleBTDiscoveryNotification:"
+ "__handleBTPowerNotification:"
+ "_deviceAnalyticsClient"
+ "_getWADeviceAnalyticsClient"
+ "_infraManager"
+ "addPersistentStoreRemoteChangeNotificationObserver:selector:"
+ "associateToNetwork:configuration:reply:"
+ "associateToNetwork:peer:configuration:reply:"
+ "associateToNetworkOnPeer:scanResult:configuration:reply:"
+ "associateWithParameters:reply:"
+ "available"
+ "cloudPaired"
+ "com.apple.wifi.peer.infra"
+ "connectable"
+ "connected"
+ "deviceScanningInProgress"
+ "initWithPeerManager:statusManager:"
+ "isAppleAudioDevice"
+ "localAddress"
+ "maskLocalDeviceEvents:"
+ "nil InfraManager"
+ "paired"
+ "performFetch:error:"
+ "performScanWithParams:error:"
+ "releaseBackgroundRawAccessMOC"
+ "scanForNetworksWithConfiguration:handler:"
+ "setAcceptableCacheAge:"
+ "setBluetoothDevice:"
+ "setForceBSSID:"
+ "setPassword:"
+ "setRememberUponSuccessfulAssociation:"
+ "setSSID:"
+ "setScanResult:"
+ "setSharedInstanceQueue:"
+ "sharedDeviceAnalyticsClient"
+ "sharedInstance"
+ "startNetworkDiscovery:reply:"
+ "startNetworkDiscoveryOnPeer:configuration:reply:"
+ "v48@0:8@\"W5Peer\"16@\"W5WiFiScanResult\"24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
+ "v56@0:8@\"W5XPCConnection\"16@\"W5Peer\"24@\"W5WiFiScanResult\"32@\"NSDictionary\"40@?<v@?@\"NSError\">48"
+ "xpcConnection:associateToNetworkOnPeer:scanResult:configuration:reply:"
+ "xpcConnection:startNetworkDiscoveryOnPeer:configuration:reply:"
- "%llx"
- "%x"
- "-[W5DatabaseManager _performFetch:error:]"
- "@\"IOBluetoothDevice\""
- "@\"IOBluetoothHostController\""
- "@\"WAAnalyticsAccess\""
- "AnalyticsProcessor"
- "BluetoothHCILEReadChannelMap:channelMap:"
- "BluetoothHCIReadAFHChannelMap:outAFHMode:outAFHChannelMap:"
- "BluetoothHCIReadScanEnable:"
- "BluetoothHCIRoleDiscovery:outCurrentRole:"
- "Class getAnalyticsProcessorClass(void)_block_invoke"
- "Class getWAAnalyticsAccessClass(void)_block_invoke"
- "DISCOVERABLE"
- "HID_OPERATION_HISTORY"
- "OPERATION_TYPE"
- "PAGEABLE"
- "PAGE_END"
- "PAGE_START"
- "REMAINING_PAGE_DURATION"
- "W5DatabaseManager.m"
- "W5FeatureAvailability"
- "WAAnalyticsAccess"
- "[wifivelocity] %s: entityName %@ doesn't (yet) exist"
- "[wifivelocity] Error with countForFetchRequest %@. %@ %@"
- "[wifivelocity] Error with executeFetchRequest %@. %@ %@"
- "[wifivelocity] Will return error %@"
- "[wifivelocity] retrieving %lu entries from request.entityName %@"
- "__macos_afhMap"
- "__macos_role"
- "__osx__deviceList"
- "__osx__handleBTStatusNotification:"
- "_analyticsAccess"
- "_bt"
- "_featureAvailabilityDefaults"
- "_getWAAnalyticsAccess"
- "_isPaging"
- "_lastStatusNotification"
- "_performFetch:error:"
- "accessWithOptions:"
- "addressAsString"
- "addressString"
- "com.apple.bluetooth.status"
- "com.apple.wifivelocity.features"
- "configuredDevices"
- "connectionHandle"
- "countForFetchRequest:error:"
- "defaultController"
- "deviceClassMajor"
- "deviceClassMinor"
- "diagnostics-mode"
- "entitiesByName"
- "entityName"
- "executeFetchRequest:error:"
- "getRemoteVersionInfo:lmpVersion:lmpSubversion:"
- "isA2DPSink"
- "isInitiator"
- "isLowEnergyDevice"
- "isiCloudPaired"
- "localizedDescription"
- "mainObjectContext"
- "managedObjectModel"
- "performBlockAndWait:"
- "persistentStoreCoordinator"
- "rawRSSI"
- "setAfhMap:"
- "setConnectionMode:"
- "setConnectionModeInterval:"
- "setIOBluetoothDevice:"
- "setLmpSubversion:"
- "setLmpVersion:"
- "setManufacturer:"
- "setRole:"
- "sharedAnalyticsProcessor"
- "userInfo"

```
