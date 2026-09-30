## wifivelocityd

> `/usr/libexec/wifivelocityd`

```diff

-1075.2.0.0.0
-  __TEXT.__text: 0x9b938
-  __TEXT.__auth_stubs: 0x1390
-  __TEXT.__objc_stubs: 0xd240
-  __TEXT.__objc_methlist: 0x4cc0
-  __TEXT.__const: 0x380
-  __TEXT.__objc_methname: 0xdce3
-  __TEXT.__oslogstring: 0xadd9
-  __TEXT.__cstring: 0xc1a2
-  __TEXT.__objc_classname: 0x835
-  __TEXT.__objc_methtype: 0x2342
-  __TEXT.__gcc_except_tab: 0x1830
+1100.25.0.0.0
+  __TEXT.__text: 0x9c0a4
+  __TEXT.__auth_stubs: 0x1380
+  __TEXT.__objc_stubs: 0xd280
+  __TEXT.__objc_methlist: 0x53cc
   __TEXT.__dlopen_cstrs: 0x31a
+  __TEXT.__const: 0x388
+  __TEXT.__objc_methname: 0xde47
+  __TEXT.__oslogstring: 0xaf5b
+  __TEXT.__cstring: 0xc343
+  __TEXT.__objc_classname: 0x832
+  __TEXT.__objc_methtype: 0x2404
+  __TEXT.__gcc_except_tab: 0x1884
   __TEXT.__ustring: 0x8c
-  __TEXT.__unwind_info: 0x1b60
-  __DATA_CONST.__auth_got: 0x9d8
-  __DATA_CONST.__got: 0x5a8
+  __TEXT.__unwind_info: 0x1b68
+  __DATA_CONST.__auth_got: 0x9d0
+  __DATA_CONST.__got: 0x5b0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x2840
-  __DATA_CONST.__cfstring: 0xaf40
+  __DATA_CONST.__const: 0x2868
+  __DATA_CONST.__cfstring: 0xaee0
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x238
-  __DATA_CONST.__objc_intobj: 0xe58
-  __DATA_CONST.__objc_arraydata: 0x23a0
+  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__objc_intobj: 0xe88
+  __DATA_CONST.__objc_arraydata: 0x2390
   __DATA_CONST.__objc_dictobj: 0x14f0
-  __DATA_CONST.__objc_arrayobj: 0x14e8
+  __DATA_CONST.__objc_arrayobj: 0x14b8
   __DATA_CONST.__objc_doubleobj: 0x80
-  __DATA.__objc_const: 0x9768
-  __DATA.__objc_selrefs: 0x3a40
-  __DATA.__objc_ivar: 0x6dc
+  __DATA.__objc_const: 0x8b70
+  __DATA.__objc_selrefs: 0x3af8
+  __DATA.__objc_ivar: 0x6e0
   __DATA.__objc_data: 0x1770
   __DATA.__data: 0x660
-  __DATA.__bss: 0x138
+  __DATA.__bss: 0x130
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
   - @rpath/BloodhoundKit.framework/BloodhoundKit
-  Functions: 2355
+  Functions: 2351
   Symbols:   507
-  CStrings:  5320
+  CStrings:  5334
 
Symbols:
+ _OBJC_CLASS_$_CWFAssocParameters
+ _OBJC_CLASS_$_W5FeatureAvailability
- _NSPersistentStoreRemoteChangeNotification
- _os_variant_has_internal_content
CStrings:
+ "-[W5DatabaseManager performFetch:]"
+ "-[W5Engine xpcConnection:associateToNetworkOnPeer:scanResult:configuration:reply:]_block_invoke_2"
+ "-[W5Engine xpcConnection:startNetworkDiscoveryOnPeer:configuration:reply:]_block_invoke_2"
+ "-[W5PeerInfraManager _requestHandler]_block_invoke"
+ "-[W5PeerInfraManager _requestHandler]_block_invoke_3"
+ "-[W5PeerInfraManager initWithPeerManager:statusManager:]"
+ "-[W5StatusManager associateToNetwork:configuration:reply:]_block_invoke"
+ "-[W5StatusManager associateToNetwork:configuration:reply:]_block_invoke_2"
+ "-[W5StatusManager scanForNetworksWithConfiguration:handler:]_block_invoke"
+ "-[W5WiFiInterface performScanWithParams:error:]"
+ "@\"W5PeerInfraManager\""
+ "@48@0:8@16@24@32@?40"
+ "Class getWADeviceAnalyticsClientClass(void)_block_invoke"
+ "JoinError"
+ "JoinPassword"
+ "JoinTarget"
+ "ScanError"
+ "T@\"W5PeerGenericRequestListener\",R,N,V_listener"
+ "W5PeerInfraManager"
+ "W5PeerInfraManager.m"
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
+ "[wifivelocity] Creating _waDeviceAnalyticsClient"
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
+ "com.apple.wifi.peer.infra"
+ "initWithPeerManager:statusManager:"
+ "nil InfraManager"
+ "performFetch:error:"
+ "performScanWithParams:error:"
+ "releaseBackgroundRawAccessMOC"
+ "scanForNetworksWithConfiguration:handler:"
+ "setAcceptableCacheAge:"
+ "setForceBSSID:"
+ "setPassword:"
+ "setRememberUponSuccessfulAssociation:"
+ "setSSID:"
+ "setScanResult:"
+ "sharedDeviceAnalyticsClient"
+ "startNetworkDiscovery:reply:"
+ "startNetworkDiscoveryOnPeer:configuration:reply:"
+ "v48@0:8@\"W5Peer\"16@\"W5WiFiScanResult\"24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
+ "v56@0:8@\"W5XPCConnection\"16@\"W5Peer\"24@\"W5WiFiScanResult\"32@\"NSDictionary\"40@?<v@?@\"NSError\">48"
+ "xpcConnection:associateToNetworkOnPeer:scanResult:configuration:reply:"
+ "xpcConnection:startNetworkDiscoveryOnPeer:configuration:reply:"
- "-[W5DatabaseManager _performFetch:error:]"
- "-dbg=print_nan_avail"
- "-nan"
- "-nan_peers"
- "@\"WAAnalyticsAccess\""
- "AnalyticsProcessor"
- "Class getAnalyticsProcessorClass(void)_block_invoke"
- "Class getWAAnalyticsAccessClass(void)_block_invoke"
- "Filtered known networks for customer install without MegaWiFi profile\n"
- "HND_AnalyticsProcessor"
- "T@\"W5WiFiInterface\",R,&,V_nan"
- "W5DatabaseManager.m"
- "W5FeatureAvailability"
- "WAAnalyticsAccess"
- "WiFiPolicy"
- "[wifivelocity] %s: entityName %@ doesn't (yet) exist"
- "[wifivelocity] Creating _waDeviceAnalyticsClient with [WADeviceAnalyticsClient_SOFT sharedDeviceAnalyticsClientWithSharedServerTypeAndXPCStore]"
- "[wifivelocity] Creating _waDeviceAnalyticsClient with [[WADeviceAnalyticsClient_SOFT alloc] init]"
- "[wifivelocity] Error with countForFetchRequest %@. %@ %@"
- "[wifivelocity] Error with executeFetchRequest %@. %@ %@"
- "[wifivelocity] Will return error %@"
- "[wifivelocity] retrieving %lu entries from request.entityName %@"
- "__ios__deviceList"
- "__ios__handleBTAdvertisingNotification:"
- "__ios__handleBTAvailabilityNotification:"
- "__ios__handleBTConnectabiliyNotification:"
- "__ios__handleBTDiscoveryNotification:"
- "__ios__handleBTPowerNotification:"
- "__startNANPerfLogging"
- "__startNANQueryTimer"
- "_analyticsAccess"
- "_featureAvailabilityDefaults"
- "_getWAAnalyticsAccess"
- "_nan"
- "_nanQueryFileHandle"
- "_nanQueryTimer"
- "_performFetch:error:"
- "accessWithOptions:"
- "com.apple.wifivelocity.features"
- "countForFetchRequest:error:"
- "diagnostics-mode"
- "entitiesByName"
- "entityName"
- "executeFetchRequest:error:"
- "mainObjectContext"
- "managedObjectModel"
- "nan"
- "nan_%@"
- "performBlockAndWait:"
- "persistentStoreCoordinator"
- "sharedAnalyticsProcessor"
- "sharedDeviceAnalyticsClientWithPersist"
- "userInfo"

```
