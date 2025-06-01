## TrackingAvoidance

> `/System/Library/PrivateFrameworks/TrackingAvoidance.framework/TrackingAvoidance`

```diff

-104.0.6.0.0
-  __TEXT.__text: 0x47b64
+104.0.7.0.0
+  __TEXT.__text: 0x47fe8
   __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x41a0
+  __TEXT.__objc_methlist: 0x41e8
   __TEXT.__oslogstring: 0x68e7
-  __TEXT.__cstring: 0x2cf5
+  __TEXT.__cstring: 0x2d72
   __TEXT.__const: 0x210
   __TEXT.__gcc_except_tab: 0x554
-  __TEXT.__unwind_info: 0xd1c
-  __TEXT.__objc_classname: 0x77a
-  __TEXT.__objc_methname: 0xc8fd
-  __TEXT.__objc_methtype: 0x121e
-  __TEXT.__objc_stubs: 0x7360
+  __TEXT.__unwind_info: 0xd7c
+  __TEXT.__objc_classname: 0x779
+  __TEXT.__objc_methname: 0xc9f7
+  __TEXT.__objc_methtype: 0x1229
+  __TEXT.__objc_stubs: 0x7400
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x6f8
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x68b8
-  __DATA_CONST.__objc_selrefs: 0x20c8
+  __DATA_CONST.__objc_const: 0x6948
+  __DATA_CONST.__objc_selrefs: 0x2100
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x348
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__objc_const: 0x2108
-  __AUTH_CONST.__cfstring: 0x4540
+  __AUTH_CONST.__cfstring: 0x46c0
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x2d8
-  __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x5fc
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x608
   __DATA.__data: 0x600
-  __DATA_DIRTY.__objc_data: 0x1040
+  __DATA_DIRTY.__objc_data: 0x12c0
   __DATA_DIRTY.__bss: 0x18
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 58B8BA20-5377-379D-8787-AADCD09032E5
-  Functions: 1529
-  Symbols:   5261
-  CStrings:  3457
+  UUID: 515D84DE-7C4F-3803-A648-C09C9E0328CD
+  Functions: 1535
+  Symbols:   5281
+  CStrings:  3494
 
Symbols:
+ -[TAAccessoryInformation accessoryTypeNameWithAdvTypeString:]
+ -[TAAccessoryInformation batteryLevel]
+ -[TAAccessoryInformation batteryType]
+ -[TAAccessoryInformation initWithDeviceUUID:deviceType:productData:manufacturerName:modelName:firmwareVersion:accessoryCategory:accessoryCapabilities:serialNumber:protocolImplementation:networkID:batteryType:batteryLevel:]
+ -[TAAccessoryInformation networkID]
+ -[TAAccessoryInformation setBatteryLevel:]
+ -[TAAccessoryInformation setBatteryType:]
+ -[TAAccessoryInformation setNetworkID:]
+ -[TASPAdvertisement getLatestAdvTypeToString:]
+ -[TAUnknownBeacon initWithBeaconUUID:address:deviceType:withAccessoryInfo:isPoshAccessory:isFindMyNetwork:]
+ -[TAUnknownBeacon isFindMyNetwork]
+ _OBJC_IVAR_$_TAAccessoryInformation._batteryLevel
+ _OBJC_IVAR_$_TAAccessoryInformation._batteryType
+ _OBJC_IVAR_$_TAAccessoryInformation._networkID
+ _OBJC_IVAR_$_TAUnknownBeacon._isFindMyNetwork
+ _objc_msgSend$accessoryTypeNameWithAdvTypeString:
+ _objc_msgSend$batteryLevel
+ _objc_msgSend$batteryType
+ _objc_msgSend$getLatestAdvTypeToString:
+ _objc_msgSend$initWithBeaconUUID:address:deviceType:withAccessoryInfo:isPoshAccessory:isFindMyNetwork:
+ _objc_msgSend$initWithDeviceUUID:deviceType:productData:manufacturerName:modelName:firmwareVersion:accessoryCategory:accessoryCapabilities:serialNumber:protocolImplementation:networkID:batteryType:batteryLevel:
+ _objc_msgSend$isFindMyNetwork
+ _objc_msgSend$networkID
- -[TAAccessoryInformation accessoryTypeName]
- -[TAAccessoryInformation initWithDeviceUUID:deviceType:productData:manufacturerName:modelName:firmwareVersion:accessoryCategory:accessoryCapabilities:serialNumber:productName:protocolImplementation:]
- -[TAAccessoryInformation productName]
- -[TAAccessoryInformation setProductName:]
- -[TAUnknownBeacon initWithBeaconUUID:address:deviceType:withAccessoryInfo:isPoshAccessory:]
- _OBJC_IVAR_$_TAAccessoryInformation._productName
- _objc_msgSend$accessoryTypeName
- _objc_msgSend$initWithBeaconUUID:address:deviceType:withAccessoryInfo:isPoshAccessory:
- _objc_msgSend$initWithDeviceUUID:deviceType:productData:manufacturerName:modelName:firmwareVersion:accessoryCategory:accessoryCapabilities:serialNumber:productName:protocolImplementation:
CStrings:
+ "\x01\x17"
+ "%ld"
+ ":A"
+ ":AP"
+ ":NA"
+ ":P"
+ "@120@0:8@16Q24@32@40@48@56@64@72@80q88q96q104q112"
+ "@56@0:8@16@24Q32@40B48B52"
+ "A"
+ "NA"
+ "P"
+ "T@\"NSData\",C,N,V_serialNumber"
+ "TAUnknownBeaconIsFindMyNetwork"
+ "TAUnknownBeaconIsPosh"
+ "TB,R,N,V_isFindMyNetwork"
+ "Tq,N,V_batteryLevel"
+ "Tq,N,V_batteryType"
+ "Tq,N,V_networkID"
+ "_batteryLevel"
+ "_batteryType"
+ "_isFindMyNetwork"
+ "_networkID"
+ "accessoryTypeNameWithAdvTypeString:"
+ "batteryLevel"
+ "batteryType"
+ "getLatestAdvTypeToString:"
+ "initWithBeaconUUID:address:deviceType:withAccessoryInfo:isPoshAccessory:isFindMyNetwork:"
+ "initWithDeviceUUID:deviceType:productData:manufacturerName:modelName:firmwareVersion:accessoryCategory:accessoryCapabilities:serialNumber:protocolImplementation:networkID:batteryType:batteryLevel:"
+ "isFindMyNetwork"
+ "networkID"
+ "setBatteryLevel:"
+ "setBatteryType:"
+ "setNetworkID:"
- "\x01\x16\x12"
- "%tu"
- "@104@0:8@16Q24@32@40@48@56@64@72@80@88Q96"
- "@52@0:8@16@24Q32@40B48"
- "T@\"NSString\",C,N,V_productName"
- "T@\"NSString\",C,N,V_serialNumber"
- "_productName"
- "accessoryTypeName"
- "initWithBeaconUUID:address:deviceType:withAccessoryInfo:isPoshAccessory:"
- "initWithDeviceUUID:deviceType:productData:manufacturerName:modelName:firmwareVersion:accessoryCategory:accessoryCapabilities:serialNumber:productName:protocolImplementation:"
- "setProductName:"

```
