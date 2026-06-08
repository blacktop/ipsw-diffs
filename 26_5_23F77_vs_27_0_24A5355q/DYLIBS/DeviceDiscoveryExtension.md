## DeviceDiscoveryExtension

> `/System/Library/Frameworks/DeviceDiscoveryExtension.framework/DeviceDiscoveryExtension`

```diff

-325.15.1.3.0
-  __TEXT.__text: 0x69e8
-  __TEXT.__auth_stubs: 0x770
+2700.22.0.0.0
+  __TEXT.__text: 0x66d4
   __TEXT.__objc_methlist: 0x4fc
-  __TEXT.__cstring: 0x533
+  __TEXT.__cstring: 0x543
   __TEXT.__const: 0x1c2
   __TEXT.__swift5_typeref: 0x14c
   __TEXT.__oslogstring: 0x1bd

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1c0
-  __TEXT.__objc_classname: 0xb2
-  __TEXT.__objc_methname: 0xf11
-  __TEXT.__objc_methtype: 0x254
-  __TEXT.__objc_stubs: 0xbe0
-  __DATA_CONST.__got: 0xe0
+  __TEXT.__unwind_info: 0x1a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_selrefs: 0x428
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x3c0
+  __DATA_CONST.__got: 0xe0
   __AUTH_CONST.__const: 0x1f8
   __AUTH_CONST.__cfstring: 0x960
   __AUTH_CONST.__objc_const: 0x8c8
+  __AUTH_CONST.__auth_got: 0x408
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x388

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FE4265BB-7863-30B3-8A73-1FA677F00BC0
+  UUID: F6B63E3C-A1F1-3E8A-BA9D-ED580940D4EB
   Functions: 169
-  Symbols:   560
-  CStrings:  444
+  Symbols:   571
+  CStrings:  198
 
Symbols:
+ ___swift_closure_destructor
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x27
+ _objc_retain_x8
+ _swift_release_x20
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
- _objc_retain_x28
Functions:
~ _DDErrorF : 284 -> 276
~ _DDNestedErrorF : 356 -> 352
~ -[DDDeviceEvent createDADeviceEvent] : 140 -> 132
~ -[DDDeviceEvent initWithCoder:] : 212 -> 216
~ -[DDDeviceEvent encodeWithCoder:] : 144 -> 148
~ -[DDDeviceEvent encodeWithXPCObject:] : 168 -> 160
~ -[DDDeviceEvent descriptionWithLevel:] : 320 -> 340
~ -[DDDevice createDADevice] : 684 -> 696
~ -[DDDevice initWithDisplayName:category:protocolType:identifier:] : 200 -> 208
~ -[DDDevice initWithCoder:] : 1152 -> 1192
~ -[DDDevice encodeWithCoder:] : 668 -> 664
~ -[DDDevice initWithPersistentDictionaryRepresentation:error:] : 1280 -> 1172
~ -[DDDevice persistentDictionaryRepresentation] : 924 -> 876
~ +[DDDevice mergePersistentDictionary:into:] : 180 -> 176
~ -[DDDevice encodeWithXPCObject:] : 1068 -> 1124
~ -[DDDevice copyWithZone:] : 420 -> 380
~ -[DDDevice descriptionWithLevel:] : 1672 -> 1808
~ -[DDDevice setBluetoothIdentifier:] : 64 -> 12
~ -[DDDevice setNetworkEndpoint:] : 64 -> 12
~ -[DDDevice setProtocolType:] : 64 -> 12
~ sub_23e183590 -> sub_2421b7524 : 340 -> 148
~ sub_23e1836e4 -> sub_2421b75b8 : 360 -> 160
~ sub_23e1838a0 -> sub_2421b76ac : 252 -> 236
~ sub_23e18399c -> sub_2421b7798 : 536 -> 348
~ sub_23e183d14 -> sub_2421b7a54 : 172 -> 188
~ sub_23e183dc0 -> sub_2421b7b10 : 396 -> 188
~ sub_23e183f4c -> sub_2421b7bcc : 96 -> 88
~ sub_23e183fac -> sub_2421b7c24 : 88 -> 84
~ sub_23e184004 -> sub_2421b7c78 : 84 -> 284
~ sub_23e184058 -> sub_2421b7d94 : 300 -> 396
~ sub_23e184184 -> sub_2421b7f20 : 596 -> 96
~ sub_23e18492c -> sub_2421b84d4 : 588 -> 620
~ sub_23e184bb0 -> sub_2421b8778 : 1272 -> 1352
~ sub_23e1850a8 -> sub_2421b8cc0 : 68 -> 80
~ sub_23e1850ec -> sub_2421b8d10 : 700 -> 724
~ sub_23e1853a8 -> sub_2421b8fe4 : 816 -> 948
~ sub_23e1856d8 -> sub_2421b9398 : 724 -> 748
~ sub_23e1859ac -> sub_2421b9684 : 664 -> 688
~ sub_23e185c44 -> sub_2421b9934 : 104 -> 96
~ sub_23e185cac -> sub_2421b9994 : 992 -> 1064
~ _block_copy_helper : 20 -> 16
~ +[DDDeviceEvent allocInitWithXPCObject:error:] : 224 -> 216
~ -[DDDeviceEvent initWithXPCObject:error:] : 352 -> 348
~ -[DDDeviceEvent initWithCoder:].cold.1 : 116 -> 112
~ -[DDDevice initWithXPCObject:error:] : 1052 -> 1028
~ +[DDDevice deviceMetadataURLValid:] : 280 -> 260
~ -[DDDevice initWithPersistentDictionaryRepresentation:error:].cold.1 : 80 -> 76
CStrings:
- ".cxx_destruct"
- "@\"DDDevice\""
- "@\"NSData\""
- "@\"NSError\""
- "@\"NSObject<OS_nw_endpoint>\""
- "@\"NSString\""
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"UTType\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8@\"NSObject<OS_xpc_object>\"16^@24"
- "@32@0:8@16^@24"
- "@32@0:8q16@24"
- "@48@0:8@16q24@32@40"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "CUXPCCodable"
- "DADiscoveryExtensionXPCProtocolExtension"
- "DADiscoveryExtensionXPCProtocolHost"
- "DDDevice"
- "DDDeviceEvent"
- "DDDiscoverySession"
- "NSCoding"
- "NSCopying"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "SSID"
- "T@\"DDDevice\",R,N,V_device"
- "T@\"NSData\",C,N,V_txtRecordData"
- "T@\"NSDictionary\",R,C,N"
- "T@\"NSError\",R,C,N,V_error"
- "T@\"NSObject<OS_nw_endpoint>\",&,N,V_networkEndpoint"
- "T@\"NSString\",C,N,V_SSID"
- "T@\"NSString\",C,N,V_displayImageName"
- "T@\"NSString\",C,N,V_displayName"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",C,N,V_mediaContentSubtitle"
- "T@\"NSString\",C,N,V_mediaContentTitle"
- "T@\"NSString\",C,N,V_wifiAwareModelName"
- "T@\"NSString\",C,N,V_wifiAwareServiceName"
- "T@\"NSString\",C,N,V_wifiAwareVendorName"
- "T@\"NSURL\",C,N,V_url"
- "T@\"NSUUID\",&,N,V_bluetoothIdentifier"
- "T@\"UTType\",&,N,V_protocolType"
- "T@?,C,N,V_eventHandler"
- "TB,N,V_allowPairing"
- "TB,N,V_supportsGrouping"
- "TB,R"
- "TQ,N,V_deviceSupports"
- "Td,N,V_approveTime"
- "Tq,N,V_category"
- "Tq,N,V_mediaPlaybackState"
- "Tq,N,V_protocol"
- "Tq,N,V_state"
- "Tq,N,V_wifiAwareServiceRole"
- "Tq,R,N,V_eventType"
- "URLWithString:"
- "UTF8String"
- "UUIDString"
- "_SSID"
- "_allowPairing"
- "_approveTime"
- "_bluetoothIdentifier"
- "_category"
- "_consumedExtension"
- "_device"
- "_deviceSupports"
- "_discoveryExtension"
- "_displayImageName"
- "_displayName"
- "_error"
- "_eventHandler"
- "_eventType"
- "_extensionConfiguration"
- "_extensionSession"
- "_identifier"
- "_mediaContentSubtitle"
- "_mediaContentTitle"
- "_mediaPlaybackState"
- "_networkEndpoint"
- "_protocol"
- "_protocolType"
- "_state"
- "_supportsGrouping"
- "_txtRecordData"
- "_url"
- "_wifiAwareModelName"
- "_wifiAwareServiceName"
- "_wifiAwareServiceRole"
- "_wifiAwareVendorName"
- "_xpcConnection"
- "absoluteString"
- "allocInitWithXPCObject:error:"
- "allocWithZone:"
- "allowPairing"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "bytes"
- "category"
- "consumeToken:"
- "containsValueForKey:"
- "copy"
- "copyCEndpoint"
- "copyWithZone:"
- "createDADevice"
- "createDADeviceEvent"
- "d"
- "d16@0:8"
- "dealloc"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "description"
- "descriptionWithLevel:"
- "device"
- "deviceMetadataURLValid:"
- "deviceSupports"
- "dictionaryWithObjects:forKeys:count:"
- "didReceiveDeviceChangedEvent:"
- "displayName"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodeWithXPCObject:"
- "endpointWithCEndpoint:"
- "error"
- "eventHandler"
- "eventType"
- "failWithError:"
- "flags"
- "getUUIDBytes:"
- "host"
- "init"
- "initWithCoder:"
- "initWithDisplayName:category:protocolType:identifier:"
- "initWithDomain:code:userInfo:"
- "initWithEventType:device:"
- "initWithFormat:arguments:"
- "initWithPersistentDictionaryRepresentation:error:"
- "initWithString:compareOptions:"
- "initWithUUIDString:"
- "initWithXPCObject:error:"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidate"
- "length"
- "mediaContentArtistName"
- "mediaContentSubtitle"
- "mergePersistentDictionary:into:"
- "networkEndpoint"
- "numberOfMatchesInString:options:range:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "persistentDictionaryRepresentation"
- "processIdentifier"
- "q"
- "q16@0:8"
- "query"
- "regularExpressionWithPattern:options:error:"
- "remoteObjectProxy"
- "reportEvent:"
- "resume"
- "setAllowPairing:"
- "setApproveTime:"
- "setBluetoothIdentifier:"
- "setCategory:"
- "setDeviceSupports:"
- "setDiscoveryConfiguration:"
- "setDisplayImageName:"
- "setDisplayName:"
- "setEventHandler:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFlags:"
- "setIdentifier:"
- "setInvalidationHandler:"
- "setMediaContentArtistName:"
- "setMediaContentSubtitle:"
- "setMediaContentTitle:"
- "setMediaPlaybackState:"
- "setName:"
- "setNetworkEndpoint:"
- "setObject:forKeyedSubscript:"
- "setPendingRemoval:"
- "setProtocol:"
- "setProtocolType:"
- "setRemoteObjectInterface:"
- "setSSID:"
- "setState:"
- "setSupportsGrouping:"
- "setTxtRecordData:"
- "setType:"
- "setUrl:"
- "setWifiAwareModelName:"
- "setWifiAwareModelNameMatch:"
- "setWifiAwareServiceName:"
- "setWifiAwareServiceRole:"
- "setWifiAwareServiceType:"
- "setWifiAwareVendorName:"
- "startDiscovery"
- "state"
- "stringWithUTF8String:"
- "supportsGrouping"
- "supportsSecureCoding"
- "typeWithIdentifier:"
- "unarchivedObjectOfClass:fromData:error:"
- "v16@0:8"
- "v16@?0@\"DDDeviceEvent\"8"
- "v20@0:8B16"
- "v24@0:8*16"
- "v24@0:8@\"DADeviceEvent\"16"
- "v24@0:8@\"DAEvent\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSObject<OS_xpc_object>\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v32@0:8@16@24"
- "v8@?0"
- "wifiAwareModelName"
- "wifiAwareServiceName"
- "wifiAwareServiceRole"
- "wifiAwareVendorName"

```
