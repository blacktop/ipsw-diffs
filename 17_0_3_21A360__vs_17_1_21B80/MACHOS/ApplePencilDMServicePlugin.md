## ApplePencilDMServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/ApplePencilDMServicePlugin.plugin/ApplePencilDMServicePlugin`

```diff

-10.1.0.0.0
-  __TEXT.__text: 0x24c8
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_stubs: 0x400
-  __TEXT.__objc_methlist: 0x290
+10.2.0.0.0
+  __TEXT.__text: 0x5238
+  __TEXT.__auth_stubs: 0x490
+  __TEXT.__objc_stubs: 0x840
+  __TEXT.__objc_methlist: 0x514
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x54a
-  __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__objc_methname: 0x7f6
-  __TEXT.__oslogstring: 0x2d8
-  __TEXT.__objc_classname: 0x70
-  __TEXT.__objc_methtype: 0x3ff
-  __TEXT.__unwind_info: 0x110
-  __DATA_CONST.__auth_got: 0x1b0
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0xb8
-  __DATA_CONST.__cfstring: 0x400
-  __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x20
+  __TEXT.__cstring: 0x8d6
+  __TEXT.__gcc_except_tab: 0x12c
+  __TEXT.__objc_methname: 0xdea
+  __TEXT.__oslogstring: 0xa59
+  __TEXT.__objc_classname: 0xb8
+  __TEXT.__objc_methtype: 0x593
+  __TEXT.__unwind_info: 0x1a8
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__const: 0x130
+  __DATA_CONST.__cfstring: 0x620
+  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0xa50
-  __DATA.__objc_selrefs: 0x208
-  __DATA.__objc_classrefs: 0x38
-  __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x34
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x180
+  __DATA_CONST.__objc_intobj: 0x90
+  __DATA.__objc_const: 0xf98
+  __DATA.__objc_selrefs: 0x378
+  __DATA.__objc_classrefs: 0x68
+  __DATA.__objc_superrefs: 0x20
+  __DATA.__objc_ivar: 0x70
+  __DATA.__objc_data: 0x140
+  __DATA.__data: 0x1e0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 79
-  Symbols:   75
-  CStrings:  256
+  Functions: 163
+  Symbols:   109
+  CStrings:  417
 
Symbols:
+ _IOIteratorIsValid
+ _IOIteratorNext
+ _IONotificationPortCreate
+ _IONotificationPortDestroy
+ _IONotificationPortSetDispatchQueue
+ _IOObjectRelease
+ _IORegistryEntryGetParentEntry
+ _IOServiceAddMatchingNotification
+ _OBJC_CLASS_$_ACCTransportClient
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSUUID
+ _dispatch_after
+ _dispatch_async
+ _kACCInfo_AccessoryDeviceUID
+ _kACCInfo_FirmwareVersionActive
+ _kACCInfo_HardwareVersion
+ _kACCInfo_Manufacturer
+ _kACCInfo_Model
+ _kACCInfo_Name
+ _kACCInfo_ProductID
+ _kACCInfo_SerialNumber
+ _kACCInfo_VendorID
+ _objc_alloc_init
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retainAutorelease
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
CStrings:
+ "!"
+ "\"\x13"
+ "%04X"
+ "%@:%@"
+ "%s Activate pairing! (Pencil attached)"
+ "%s Added Tethered Inking module"
+ "%s Added USB Pairing module"
+ "%s Attached B482 with connection UUID %@, endpoint UUID %@: %@"
+ "%s Cancel pairing! (Pencil detached)"
+ "%s Connection %@ endpoint %@ data out: %@"
+ "%s Could not create CoreAccessories connection"
+ "%s Could not create CoreAccessories endpoint"
+ "%s Could not create notification port"
+ "%s Could not create notification port: 0x%08x (deviceIterator: 0x%08jx)"
+ "%s Could not listen for a matching DM device over BT"
+ "%s ERROR: Invalid messageID (%d) for OOBPairing transmit, endpointUUID %@"
+ "%s ERROR: Not enough bytes (%lu) for message header for OOBPairing transmit, endpointUUID %@"
+ "%s ERROR: PairingType (%d) not supported for OOBPairing transmit, endpointUUID %@"
+ "%s Error sending accessory BDADDR to accessoryd"
+ "%s Error sending accessory OOB pairing data to accessoryd"
+ "%s Failed to send host BDADDR to Pencil (retry #%u), error: %@"
+ "%s Got accessory BDADDR from Pencil: %{private}@"
+ "%s Got accessory OOB pairing data from Pencil: %{private}@"
+ "%s Invalid pairing info HID input report (%lu bytes < %lu bytes)"
+ "%s Listening for Pencil DM devices over USB"
+ "%s Matched Pencil over USB (directly connected? %s)"
+ "%s Max number of retries (%u) attempted. Give up pairing"
+ "%s Max number of retries (%u) attempted. Give up sending host BDADDR to Pencil"
+ "%s Missing serial number so I cannot match Pencil DM over USB"
+ "%s OOBPairing: endpointUUID %@ transmitData: %@"
+ "%s Pairing info HID input report received but pairing is not started. Ignore"
+ "%s Received host BD_ADDR from accessoryd: %@"
+ "%s Received host OOB pairing data from accessoryd: %@"
+ "%s Retry pairing in 3 seconds (#%lu)"
+ "%s Sending accessory BDADDR to accessoryd: %{private}@"
+ "%s Sending accessory OOB pairing data to accessoryd: %{private}@"
+ "%s Sending host BDADDR to Pencil: %@"
+ "%s Set report 0x%X error: %@"
+ "%s Start!"
+ "%s Stop!"
+ "%s Tethered inking enabled!"
+ "%s Transport client unexpectedly disconnected"
+ "-[TetheredInkingModule activate]"
+ "-[TetheredInkingModule enableTetheredInking]"
+ "-[TetheredInkingModule listenForMatchingDmOverUSB]"
+ "-[USBPairingModule activate]"
+ "-[USBPairingModule cancel]"
+ "-[USBPairingModule handleBDADDR:size:]"
+ "-[USBPairingModule handleCoreAccessoriesMessage:forConnection:forEndpoint:]"
+ "-[USBPairingModule handlePairingData:size:]"
+ "-[USBPairingModule inputReport:]"
+ "-[USBPairingModule retryPairing]"
+ "-[USBPairingModule sendBDADDR:]"
+ "-[USBPairingModule startPairing]"
+ "-[USBPairingModule transportClientServerDisconnected:]"
+ "2"
+ "@\"NSDictionary\""
+ "@\"NSString\""
+ "ACCTransportClientDelegate"
+ "Apple Inc."
+ "AppleUserUSBHostHIDDevice"
+ "B32@0:8*16Q24"
+ "Fake_B482"
+ "I"
+ "IONameMatch"
+ "IOPropertyMatch"
+ "IOService"
+ "IOServiceFirstMatch"
+ "Manufacturer"
+ "NO"
+ "PrimaryUsage"
+ "PrimaryUsagePage"
+ "Product"
+ "Q"
+ "SerialNumber"
+ "SupportedTypes"
+ "Supports2Way"
+ "T@\"NSDictionary\",&,N,V_properties"
+ "T@\"NSString\",&,N,V_connectionUUID"
+ "T@\"NSString\",&,N,V_deviceUID"
+ "T@\"NSString\",&,N,V_endpointUUID"
+ "TB,N,V_completed"
+ "TB,N,V_started"
+ "TQ,N,V_retries"
+ "TetheredInkingModule"
+ "USBPairingModule"
+ "UUID"
+ "UUIDString"
+ "VersionNumber"
+ "YES"
+ "^{IONotificationPort=}"
+ "_completed"
+ "_connectionUUID"
+ "_deviceUID"
+ "_dmMatchedIterator"
+ "_dmMatchedNotifierPortRef"
+ "_endpointUUID"
+ "_properties"
+ "_retries"
+ "_started"
+ "appendBytes:length:"
+ "appendData:"
+ "array"
+ "bytes"
+ "completed"
+ "componentsJoinedByString:"
+ "composeAccessoryInfo"
+ "connectionUUID"
+ "createConnectionWithType:andIdentifier:"
+ "createEndpointWithTransportType:andProtocol:andIdentifier:andDataOutHandler:forConnectionWithUUID:publishConnection:"
+ "dataWithBytes:length:"
+ "dataWithBytesNoCopy:length:freeWhenDone:"
+ "destroyConnectionWithUUID:"
+ "destroyEndpointWithUUID:"
+ "deviceUID"
+ "enableTetheredInking"
+ "endpointUUID"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "handleBDADDR:size:"
+ "handleCoreAccessoriesMessage:forConnection:forEndpoint:"
+ "handlePairingData:size:"
+ "length"
+ "listenForMatchingDmOverUSB"
+ "locationID"
+ "processIncomingData:forEndpointWithUUID:"
+ "properties"
+ "publishConnectionWithUUID:"
+ "retries"
+ "retryPairing"
+ "sendBDADDR:"
+ "sendPairingData:"
+ "setAccessoryInfo:forEndpointWithUUID:"
+ "setCompleted:"
+ "setConnectionUUID:"
+ "setDeviceUID:"
+ "setEndpointUUID:"
+ "setProperties:"
+ "setRetries:"
+ "setStarted:"
+ "sharedClient"
+ "startPairing"
+ "started"
+ "stopPairing"
+ "transportClient:authStatusDidChange:forConnectionWithUUID:"
+ "transportClient:propertiesDidChange:forConnectionWithUUID:previousProperties:"
+ "transportClient:propertiesDidChange:forEndpointWithUUID:previousProperties:connectionUUID:"
+ "transportClientServerDisconnected:"
+ "unsignedIntegerValue"
+ "v24@0:8@\"ACCTransportClient\"16"
+ "v24@0:8Q16"
+ "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSString\"16@\"NSData\"24"
+ "v36@0:8@\"ACCTransportClient\"16B24@\"NSString\"28"
+ "v36@0:8@16B24@28"
+ "v40@0:8@16@24@32"
+ "v48@0:8@\"ACCTransportClient\"16@\"NSDictionary\"24@\"NSString\"32@\"NSDictionary\"40"
+ "v48@0:8@16@24@32@40"
+ "v56@0:8@\"ACCTransportClient\"16@\"NSDictionary\"24@\"NSString\"32@\"NSDictionary\"40@\"NSString\"48"
+ "v56@0:8@16@24@32@40@48"
+ "void deviceManagerMatchedCallback(void *, io_iterator_t)"
+ "|"

```
