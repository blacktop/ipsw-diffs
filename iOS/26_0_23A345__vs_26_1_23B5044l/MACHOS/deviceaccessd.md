## deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

-320.40.0.0.0
-  __TEXT.__text: 0x33308
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_stubs: 0x49e0
-  __TEXT.__objc_methlist: 0x1a28
-  __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x1df8
-  __TEXT.__objc_methname: 0x660a
+321.4.1.0.0
+  __TEXT.__text: 0x35cc4
+  __TEXT.__auth_stubs: 0xe10
+  __TEXT.__objc_stubs: 0x4cc0
+  __TEXT.__objc_methlist: 0x1aa0
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0x1fe0
+  __TEXT.__objc_methname: 0x68d6
   __TEXT.__objc_classname: 0x1ff
-  __TEXT.__objc_methtype: 0x14bc
-  __TEXT.__cstring: 0xba82
-  __TEXT.__unwind_info: 0xa88
-  __DATA_CONST.__auth_got: 0x710
-  __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0xee8
-  __DATA_CONST.__cfstring: 0x1000
+  __TEXT.__objc_methtype: 0x145b
+  __TEXT.__cstring: 0xc147
+  __TEXT.__unwind_info: 0xad0
+  __DATA_CONST.__auth_got: 0x718
+  __DATA_CONST.__got: 0x370
+  __DATA_CONST.__const: 0xf60
+  __DATA_CONST.__cfstring: 0x1080
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0xd8
-  __DATA.__objc_const: 0x2320
-  __DATA.__objc_selrefs: 0x1848
+  __DATA.__objc_const: 0x2318
+  __DATA.__objc_selrefs: 0x1908
   __DATA.__objc_ivar: 0x234
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x6e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 059EE755-62F7-3482-96B7-3255AD0DB6E9
-  Functions: 945
-  Symbols:   342
-  CStrings:  2475
+  UUID: 62AD639C-495E-3F01-97CA-B4781ED2A9D2
+  Functions: 973
+  Symbols:   345
+  CStrings:  2542
 
Symbols:
+ _CBConnectionEventMatchingOptionPeripheralUUIDs
+ _CUXPCDecodeNSArrayOfNSString
+ _OBJC_CLASS_$_DADeviceAccessoryServiceInfo
CStrings:
+ "### SetDeviceAccessoryServiceInfo failed: %@ from %@"
+ "### _refreshRegistrationForBTConnectionEvents"
+ "### _refreshRegistrationForBTConnectionEvents adding %@ to monitoring list"
+ "### _refreshRegistrationForBTConnectionEvents calling registerForConnectionEventsWithOptions with %@"
+ "### connectionEventDidOccur %@"
+ "### connectionEventDidOccur %@ %s transport=%d"
+ "### connectionEventDidOccur DADevice %@ for %@"
+ "### connectionEventDidOccur getDevicesWithFlags %@ %@"
+ "### reportDeviceConnectionStatusChanged %@ flags:%@ %@"
+ "### runMigrationWithDiscovery found ASK record %@"
+ "### saveDeviceAccessoryServiceInfo, Using containerized path %s"
+ "-[DADaemonServer _refreshRegistrationForBTConnectionEvents]"
+ "-[DADaemonServer _refreshRegistrationForBTConnectionEvents]_block_invoke"
+ "-[DADaemonServer centralManager:connectionEventDidOccur:forPeripheral:]"
+ "-[DADaemonServer centralManager:connectionEventDidOccur:forPeripheral:]_block_invoke"
+ "-[DADaemonServer getDevicesWithFlags:appID:]_block_invoke_4"
+ "-[DADaemonServer runMigrationWithDiscovery:fromPostOnboarding:]"
+ "-[DADaemonServer runMigrationWithDiscovery:fromPostOnboarding:]_block_invoke"
+ "-[DADaemonServer saveDeviceAccessoryServiceInfo:device:error:]"
+ "-[DADaemonXPCConnection _xpcSetDeviceAccessoryServiceInfo:]"
+ "-[DADaemonXPCConnection _xpcSetDeviceAccessoryServiceInfo:]_block_invoke"
+ "-[DADaemonXPCConnection reportDeviceConnectionStatusChanged:]"
+ "AccessoryServiceInfos"
+ "Connected"
+ "Disconnected"
+ "Invalid access or missing entitlement"
+ "No associated bundle ID"
+ "No service info"
+ "RPDs"
+ "SASi"
+ "Serialize accessory services info data failed"
+ "SetDeviceAccessoryServiceInfo: %@, %@, from %@"
+ "[Device Decoding Error] %@"
+ "[ServiceInfo Decoding Error] %@"
+ "_findDADeviceWithMigrationConfig:"
+ "_refreshRegistrationForBTConnectionEvents"
+ "_reportDeviceAccessoryServicesChanged:"
+ "_reportDeviceConnectionStatusChanged:"
+ "_xpcRequestPermissionsForDevice:"
+ "_xpcSetDeviceAccessoryServiceInfo:"
+ "accessoryServicesInternalMap"
+ "accessoryServicesMap"
+ "arrayByAddingObjectsFromArray:"
+ "associatedBundleID"
+ "authorizationLevel"
+ "connectedTransport"
+ "connectionStatus"
+ "dAsI"
+ "daserviceInfodata"
+ "deviceFlags"
+ "initWithPersistentDictionaryRepresentation:deviceID:error:"
+ "registerForConnectionEventsWithOptions:"
+ "reportAccessoryServicesChanged:"
+ "reportDeviceConnectionStatusChanged:"
+ "reportDiscoveryEvent:appID:filterDiscoveryInApp:"
+ "runMigrationWithDiscovery:fromPostOnboarding:"
+ "saveDeviceAccessoryServiceInfo: changed, %@"
+ "saveDeviceAccessoryServiceInfo: no changes, %@"
+ "saveDeviceAccessoryServiceInfo: remove, %@"
+ "saveDeviceAccessoryServiceInfo:device:error:"
+ "services"
+ "setAccessoryServicesInternalMap:"
+ "setAuthorizationLevel:"
+ "setBluetoothAdvertisementData:"
+ "setBluetoothRSSI:"
+ "setConnectionStatus:"
+ "svcs"
+ "v28@0:8@16B24"
+ "v32@?0@\"NSString\"8@\"DADeviceAccessoryServiceInfo\"16^B24"
- "### runMigrationWithDiscovery found %@"
- "-[DADaemonServer runMigrationWithDiscovery:]"
- "-[DADaemonServer runMigrationWithDiscovery:]_block_invoke"
- "[Decoding Error] %@"
- "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:"
- "runMigrationWithDiscovery:"
- "v48@0:8@\"WiFiAwareDataSession\"16@\"WiFiMACAddress\"24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"32@\"NSUUID\"40"

```
