## TrackingAvoidance

> `/System/Library/PrivateFrameworks/TrackingAvoidance.framework/TrackingAvoidance`

```diff

-104.0.1.0.0
-  __TEXT.__text: 0x46ed0
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_methlist: 0x40f0
-  __TEXT.__oslogstring: 0x6737
-  __TEXT.__cstring: 0x2c08
-  __TEXT.__const: 0x200
+104.0.6.0.0
+  __TEXT.__text: 0x47b64
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_methlist: 0x41a0
+  __TEXT.__oslogstring: 0x68e7
+  __TEXT.__cstring: 0x2cf5
+  __TEXT.__const: 0x210
   __TEXT.__gcc_except_tab: 0x554
-  __TEXT.__unwind_info: 0xd10
-  __TEXT.__objc_classname: 0x776
-  __TEXT.__objc_methname: 0xc56d
-  __TEXT.__objc_methtype: 0x1199
-  __TEXT.__objc_stubs: 0x71a0
+  __TEXT.__unwind_info: 0xd1c
+  __TEXT.__objc_classname: 0x77a
+  __TEXT.__objc_methname: 0xc8fd
+  __TEXT.__objc_methtype: 0x121e
+  __TEXT.__objc_stubs: 0x7360
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x6f8
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6798
-  __DATA_CONST.__objc_selrefs: 0x2030
-  __DATA_CONST.__objc_arraydata: 0x30
+  __DATA_CONST.__objc_const: 0x68b8
+  __DATA_CONST.__objc_selrefs: 0x20c8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x348
+  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__objc_const: 0x2108
-  __AUTH_CONST.__cfstring: 0x4400
+  __AUTH_CONST.__cfstring: 0x4540
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x2c8
+  __AUTH_CONST.__auth_got: 0x2d8
   __AUTH.__objc_data: 0x500
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x348
-  __DATA.__objc_superrefs: 0x1d8
-  __DATA.__objc_ivar: 0x5e4
+  __DATA.__objc_ivar: 0x5fc
   __DATA.__data: 0x600
   __DATA_DIRTY.__objc_data: 0x1040
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1511
-  Symbols:   5203
-  CStrings:  2848
+  Functions: 1529
+  Symbols:   5261
+  CStrings:  2903
 
Symbols:
+ -[TAAccessoryInformation initWithDeviceUUID:deviceType:productData:manufacturerName:modelName:firmwareVersion:accessoryCategory:accessoryCapabilities:serialNumber:productName:protocolImplementation:]
+ -[TAAccessoryInformation productName]
+ -[TAAccessoryInformation protocolImplementation]
+ -[TAAccessoryInformation serialNumber]
+ -[TAAccessoryInformation setProductName:]
+ -[TAAccessoryInformation setProtocolImplementation:]
+ -[TAAccessoryInformation setSerialNumber:]
+ -[TASPAdvertisement detailsBitmask]
+ -[TASPAdvertisement initWithAddress:advertisementData:status:reserved:rssi:scanDate:detailsBitmask:uuid:protocolID:]
+ -[TASPAdvertisement isApple]
+ -[TASPAdvertisement isNearOwner]
+ -[TASPAdvertisement isPosh]
+ -[TASPAdvertisement protocolID]
+ -[TASingleDeviceRecord _isAISFetchComplete].cold.2
+ -[TASingleDeviceRecord _isAISFetchComplete].cold.3
+ -[TATrackingAvoidanceService debugForceSurfaceStagedDetections:deviceType:detailsBitmask:]
+ -[TATrackingAvoidanceService debugStageTADetection:deviceType:detailsBitmask:]
+ -[TATrackingAvoidanceService debugStageTADetection:deviceType:detailsBitmask:].cold.1
+ -[TATrackingAvoidanceServiceManager debugForceSurfaceStagedDetections:deviceType:detailsBitmask:]
+ -[TATrackingAvoidanceServiceManager debugForceSurfaceStagedDetections:deviceType:detailsBitmask:].cold.1
+ -[TATrackingAvoidanceServiceManager debugStageTADetection:deviceType:detailsBitmask:]
+ -[TATrackingAvoidanceServiceManager debugStageTADetection:deviceType:detailsBitmask:].cold.1
+ -[TAUnknownBeacon initWithBeaconUUID:address:deviceType:withAccessoryInfo:isPoshAccessory:]
+ -[TAUnknownBeacon isPoshAccessory]
+ _NSSelectorFromString
+ _OBJC_IVAR_$_TAAccessoryInformation._productName
+ _OBJC_IVAR_$_TAAccessoryInformation._protocolImplementation
+ _OBJC_IVAR_$_TAAccessoryInformation._serialNumber
+ _OBJC_IVAR_$_TASPAdvertisement._detailsBitmask
+ _OBJC_IVAR_$_TASPAdvertisement._protocolID
+ _OBJC_IVAR_$_TAUnknownBeacon._isPoshAccessory
+ __os_feature_enabled_impl
+ __unnamed_array_storage.72
+ __unnamed_array_storage.73
+ _objc_msgSend$debugForceSurfaceStagedDetections:deviceType:detailsBitmask:
+ _objc_msgSend$debugStageTADetection:deviceType:detailsBitmask:
+ _objc_msgSend$decodeIntForKey:
+ _objc_msgSend$detailsBitmask
+ _objc_msgSend$encodeInt:forKey:
+ _objc_msgSend$initWithAddress:advertisementData:status:reserved:rssi:scanDate:detailsBitmask:uuid:protocolID:
+ _objc_msgSend$initWithBeaconUUID:address:deviceType:withAccessoryInfo:isPoshAccessory:
+ _objc_msgSend$initWithDeviceUUID:deviceType:productData:manufacturerName:modelName:firmwareVersion:accessoryCategory:accessoryCapabilities:serialNumber:productName:protocolImplementation:
+ _objc_msgSend$instancesRespondToSelector:
+ _objc_msgSend$intValue
+ _objc_msgSend$isApple
+ _objc_msgSend$isNearOwner
+ _objc_msgSend$isPosh
+ _objc_msgSend$isPoshAccessory
+ _objc_msgSend$protocolID
+ _objc_msgSend$protocolImplementation
+ _objc_msgSend$serialNumber
+ _objc_msgSend$stringValue
- -[TATrackingAvoidanceService debugForceSurfaceStagedDetections:deviceType:]
- -[TATrackingAvoidanceService debugStageTADetection:deviceType:]
- -[TATrackingAvoidanceService debugStageTADetection:deviceType:].cold.1
- -[TATrackingAvoidanceServiceManager debugForceSurfaceStagedDetections:deviceType:]
- -[TATrackingAvoidanceServiceManager debugForceSurfaceStagedDetections:deviceType:].cold.1
- -[TATrackingAvoidanceServiceManager debugStageTADetection:deviceType:]
- -[TATrackingAvoidanceServiceManager debugStageTADetection:deviceType:].cold.1
- __unnamed_array_storage.70
- __unnamed_array_storage.71
- _objc_msgSend$debugForceSurfaceStagedDetections:deviceType:
- _objc_msgSend$debugStageTADetection:deviceType:
- _objc_msgSend$initWithAddress:advertisementData:status:reserved:rssi:scanDate:
- _objc_msgSend$initWithDeviceUUID:deviceType:productData:manufacturerName:modelName:firmwareVersion:accessoryCategory:accessoryCapabilities:
CStrings:
+ "\x01\x16\x12"
+ "\x12\x11"
+ "\x13\x13"
+ "#TASingleDeviceRecord receiving _isAISFetchComplete for a non-posh accessory"
+ "#TASingleDeviceRecord receiving _isAISFetchComplete for a posh accessory, but feature isn't enabled"
+ "#TATrackingAvoidanceService forceSurfaceStagedDetections for address: %{private}@"
+ "#TATrackingAvoidanceService start stageTADetection for address: %{private}@ "
+ "%tu"
+ "0"
+ "@104@0:8@16Q24@32@40@48@56@64@72@80@88Q96"
+ "@52@0:8@16@24Q32@40B48"
+ "@80@0:8@16@24C32@36q44@52I60@64@72"
+ "CoreLocation"
+ "DetailsBitmask"
+ "DetailsBitmaskString"
+ "I"
+ "ProtocolIDString"
+ "StandardUT"
+ "T@\"NSNumber\",R,C,N,V_protocolID"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_productName"
+ "T@\"NSString\",C,N,V_serialNumber"
+ "TB,R,N,V_isPoshAccessory"
+ "TI,R,N,V_detailsBitmask"
+ "Tq,N,V_protocolImplementation"
+ "YES"
+ "_detailsBitmask"
+ "_isPoshAccessory"
+ "_productName"
+ "_protocolID"
+ "_protocolImplementation"
+ "_serialNumber"
+ "debugForceSurfaceStagedDetections:deviceType:detailsBitmask:"
+ "debugStageTADetection:deviceType:detailsBitmask:"
+ "decodeIntForKey:"
+ "detailsBitmask"
+ "encodeInt:forKey:"
+ "initWithAddress:advertisementData:status:reserved:rssi:scanDate:detailsBitmask:uuid:protocolID:"
+ "initWithBeaconUUID:address:deviceType:withAccessoryInfo:isPoshAccessory:"
+ "initWithDeviceUUID:deviceType:productData:manufacturerName:modelName:firmwareVersion:accessoryCategory:accessoryCapabilities:serialNumber:productName:protocolImplementation:"
+ "instancesRespondToSelector:"
+ "intValue"
+ "isApple"
+ "isNearOwner"
+ "isPosh"
+ "isPosh, %@, isApple, %@, isNearOwner, %@"
+ "isPoshAccessory"
+ "protocolID"
+ "protocolImplementation"
+ "serialNumber"
+ "setProductName:"
+ "setProtocolImplementation:"
+ "setSerialNumber:"
+ "stringValue"
+ "v24@0:8q16"
+ "v36@0:8@\"NSData\"16Q24I32"
+ "v36@0:8@16Q24I32"
+ "{\"msg%{public}.0s\":\"#TADeviceRecord skip request AIS fetch - non-posh durian type\", \"address\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#TADeviceRecord skip request AIS fetch for posh type - feature isn't enabled\", \"address\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#TATrackingAvoidanceService skip adv ff not enabled\", \"adv\":\"%{private}@\"}"
- "\x01\x16"
- "\x13\x12"
- "#TATrackingAvoidanceService forceSurfaceStagedDetections %{private}@"
- "#TATrackingAvoidanceService start stageTADetection %{private}@"
- "debugForceSurfaceStagedDetections:deviceType:"
- "debugStageTADetection:deviceType:"
- "v32@0:8@\"NSData\"16Q24"
- "{\"msg%{public}.0s\":\"#TADeviceRecord skip request AIS fetch - durian type\", \"address\":\"%{private}@\"}"

```
