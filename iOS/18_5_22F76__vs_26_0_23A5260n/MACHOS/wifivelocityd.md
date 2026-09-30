## wifivelocityd

> `/usr/libexec/wifivelocityd`

```diff

-1100.25.0.0.0
-  __TEXT.__text: 0x9d144
-  __TEXT.__auth_stubs: 0x1390
-  __TEXT.__objc_stubs: 0xd2e0
-  __TEXT.__objc_methlist: 0x53ec
+1150.45.0.0.0
+  __TEXT.__text: 0x9bcac
+  __TEXT.__auth_stubs: 0x13d0
+  __TEXT.__objc_stubs: 0xd280
+  __TEXT.__objc_methlist: 0x53ac
   __TEXT.__dlopen_cstrs: 0x31a
   __TEXT.__const: 0x388
-  __TEXT.__objc_methname: 0xdebc
-  __TEXT.__oslogstring: 0xaf5b
-  __TEXT.__cstring: 0xc3b6
+  __TEXT.__objc_methname: 0xdd70
+  __TEXT.__oslogstring: 0xb0e0
+  __TEXT.__cstring: 0xc385
   __TEXT.__objc_classname: 0x832
-  __TEXT.__objc_methtype: 0x2404
-  __TEXT.__gcc_except_tab: 0x1884
+  __TEXT.__objc_methtype: 0x23e9
+  __TEXT.__gcc_except_tab: 0x1880
   __TEXT.__ustring: 0x8c
-  __TEXT.__unwind_info: 0x1bb8
-  __DATA_CONST.__auth_got: 0x9d8
-  __DATA_CONST.__got: 0x5b0
+  __TEXT.__unwind_info: 0x1b40
+  __DATA_CONST.__auth_got: 0x9f8
+  __DATA_CONST.__got: 0x590
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x2868
-  __DATA_CONST.__cfstring: 0xaf80
+  __DATA_CONST.__const: 0x28f0
+  __DATA_CONST.__cfstring: 0xaf20
   __DATA_CONST.__objc_classlist: 0x258
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_intobj: 0xe88
-  __DATA_CONST.__objc_arraydata: 0x23a0
+  __DATA_CONST.__objc_arraydata: 0x2390
   __DATA_CONST.__objc_dictobj: 0x14f0
-  __DATA_CONST.__objc_arrayobj: 0x14e8
+  __DATA_CONST.__objc_arrayobj: 0x14b8
   __DATA_CONST.__objc_doubleobj: 0x80
-  __DATA.__objc_const: 0x8be0
-  __DATA.__objc_selrefs: 0x3b10
-  __DATA.__objc_ivar: 0x6ec
+  __DATA.__objc_const: 0x8b70
+  __DATA.__objc_selrefs: 0x3ac8
+  __DATA.__objc_ivar: 0x6d8
   __DATA.__objc_data: 0x1770
   __DATA.__data: 0x660
-  __DATA.__bss: 0x130
+  __DATA.__bss: 0x140
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
   - @rpath/BloodhoundKit.framework/BloodhoundKit
-  UUID: 3614EB66-61DC-3993-A262-74B4F8FE3B30
-  Functions: 2372
+  UUID: 51558B5C-C20A-3991-A850-E0195BCC27AC
+  Functions: 2341
   Symbols:   508
-  CStrings:  6733
+  CStrings:  6719
 
Symbols:
+ _CWFEthernetAddressStringFromData
+ _IOServiceNameMatching
+ _OBJC_CLASS_$_CBController
+ _OBJC_CLASS_$_CBDiscovery
+ _OBJC_CLASS_$_NSManagedObject
+ _class_copyPropertyList
+ _property_getAttributes
+ _property_getName
- _BluetoothAdvertisingStateChangedNotification
- _BluetoothAvailabilityChangedNotification
- _BluetoothConnectabilityChangedNotification
- _BluetoothDiscoveryStateChangedNotification
- _BluetoothPowerChangedNotification
- _OBJC_CLASS_$_BluetoothManager
- _OBJC_CLASS_$_CBCentralManager
- _os_variant_has_internal_content
CStrings:
+ ",R"
+ "/wl"
+ "@\"CBController\""
+ "@\"CBDevice\""
+ "Faulting"
+ "T:"
+ "[wifivelocity] Activation completed for CBController (error=%@)"
+ "[wifivelocity] CBController errorHandler invoked (error=%@)"
+ "[wifivelocity] CoreCapture collection is %s"
+ "[wifivelocity] Max count exceeded, removing file from destination and skipping remaining files (aggregateSize=%luB, maxSize=%ldB, fileSize=%luB, aggregateCount=%lu, maxCount=%ld, file=%{public}@)"
+ "[wifivelocity] Max size exceeded, removing file from destination and continuing to add remaining files (aggregateSize=%luB, maxSize=%ldB, fileSize=%luB, aggregateCount=%lu, maxCount=%ld, file=%{public}@)"
+ "[wlan]"
+ "__allowCoreCapture"
+ "__bluetoothLoggingEnabledWithQueue:reply:"
+ "__controllerInfo"
+ "__sendBluetoothStatusChangeEvent"
+ "__setBluetoothLoggingEnabled:queue:reply:"
+ "_w5AllAttributes"
+ "_w5DictionaryRepresentation"
+ "bluetoothState"
+ "btAddressData"
+ "connectedServices"
+ "controllerInfoAndReturnError:"
+ "defaultCStringEncoding"
+ "deviceFlags"
+ "devicesWithDiscoveryFlags:error:"
+ "diagnosticEventAt:with:"
+ "discoverableState"
+ "entity"
+ "eventType"
+ "hardwareAddressData"
+ "initWithCBDevice:"
+ "inquiryState"
+ "isSubclassOfClass:"
+ "managedObjectContextResetAndRelease:"
+ "marconi-wifi"
+ "releaseMoc"
+ "setBluetoothStateChangedHandler:"
+ "setDesc:"
+ "setDiscoverableStateChangedHandler:"
+ "setEnabled:"
+ "setErrorHandler:"
+ "supportedServices"
+ "v16@?0@\"WADeviceAnalyticsDiagnosticStateRecord\"8"
+ "valueForKey:"
+ "vendorID"
+ "wlan"
+ "wlan_cca_get_stats.txt"
+ "wlan_curpower.txt"
- "-dbg=print_nan_avail"
- "-nan"
- "-nan_peers"
- "@\"BluetoothDevice\""
- "@\"CBCentralManager\""
- "@\"CBPeripheral\""
- "Filtered known networks for customer install without MegaWiFi profile\n"
- "T@\"W5WiFiInterface\",R,&,V_nan"
- "[wifivelocity] Max size or max count exceeded, removing file from destination (aggregateSize=%luB, maxSize=%ldB, fileSize=%luB, aggregateCount=%lu, maxCount=%ld, file=%{public}@)"
- "__deviceList"
- "__handleBTAdvertisingNotification:"
- "__handleBTAvailabilityNotification:"
- "__handleBTConnectabiliyNotification:"
- "__handleBTDiscoveryNotification:"
- "__handleBTPowerNotification:"
- "__ios_bluetoothLoggingEnabledWithQueue:reply:"
- "__ios_setBluetoothLoggingEnabled:queue:reply:"
- "__majorClass"
- "__minorClass"
- "__startNANPerfLogging"
- "__startNANQueryTimer"
- "_centralManager"
- "_nan"
- "_nanQueryFileHandle"
- "_nanQueryTimer"
- "_peripheral"
- "addEntriesFromDictionary:"
- "addObserver:selector:name:object:"
- "available"
- "cloudPaired"
- "com.apple.wifi.DiagnosticState"
- "connectable"
- "connected"
- "connectedDevices"
- "desc"
- "deviceScanningInProgress"
- "isAppleAudioDevice"
- "isConnectedToSystem"
- "isPeerCloudPaired:"
- "isPeerPaired:"
- "localAddress"
- "maskLocalDeviceEvents:"
- "nan"
- "nan_%@"
- "paired"
- "pairedDevices"
- "processWAMessageMetric:data:"
- "releaseBackgroundRawAccessMOC"
- "retrieveConnectedPeripheralsWithServices:allowAll:"
- "retrievePairedPeers"
- "setBluetoothDevice:"
- "setMajorClass:"
- "setMinorClass:"
- "setPeripheral:centralManager:"
- "setSharedInstanceQueue:"
- "sharedInstance"
- "sharedPairingAgent"
- "wl_cca_get_stats.txt"
- "wl_curpower.txt"

```
