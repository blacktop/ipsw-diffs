## CoreAccessories

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories`

```diff

-898.80.3.0.0
-  __TEXT.__text: 0x2f444
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0xf6c
+919.100.33.0.0
+  __TEXT.__text: 0x2f630
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0xf74
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x350e
-  __TEXT.__oslogstring: 0x3a62
+  __TEXT.__cstring: 0x3694
+  __TEXT.__oslogstring: 0x3af1
   __TEXT.__gcc_except_tab: 0x618
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x874
+  __TEXT.__unwind_info: 0x878
   __TEXT.__objc_classname: 0x258
-  __TEXT.__objc_methname: 0x40ab
-  __TEXT.__objc_methtype: 0x1408
-  __TEXT.__objc_stubs: 0x2820
+  __TEXT.__objc_methname: 0x412b
+  __TEXT.__objc_methtype: 0x1478
+  __TEXT.__objc_stubs: 0x2840
   __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x1a50
+  __DATA_CONST.__const: 0x1b40
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2ac0
-  __DATA_CONST.__objc_selrefs: 0xd18
+  __DATA_CONST.__objc_const: 0x2ae0
+  __DATA_CONST.__objc_selrefs: 0xd20
+  __DATA_CONST.__objc_protorefs: 0x50
+  __DATA_CONST.__objc_classrefs: 0x100
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__cfstring: 0x3260
+  __AUTH_CONST.__cfstring: 0x3440
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__const: 0x660
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x378
-  __DATA.__objc_protorefs: 0x50
-  __DATA.__objc_classrefs: 0x100
-  __DATA.__objc_superrefs: 0x48
+  __AUTH_CONST.__auth_got: 0x370
   __DATA.__objc_ivar: 0xc8
   __DATA.__data: 0x740
   __DATA.__bss: 0xe0
-  __DATA_DIRTY.__const: 0x9c0
+  __DATA_DIRTY.__const: 0x3e0
   __DATA_DIRTY.__objc_const: 0x510
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x138

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3D25545D-0146-3493-9BC0-DBA142B2A24E
-  Functions: 1135
-  Symbols:   3649
-  CStrings:  1886
+  UUID: 388FA779-0C8D-38C4-A7EE-D49D7ED85687
+  Functions: 1137
+  Symbols:   3683
+  CStrings:  1921
 
Symbols:
+ -[ACCExternalAccessoryProvider sendWiredCarPlayAvailable:usbIdentifier:wirelessAvailable:bluetoothIdentifier:themeAssetsAvailable:forUUID:]
+ -[ACCExternalAccessoryProvider sendWiredCarPlayAvailable:usbIdentifier:wirelessAvailable:bluetoothIdentifier:themeAssetsAvailable:forUUID:].cold.1
+ _ACCUserDefaultsKey_ForceAccInfoUpdateRelaySupport
+ _ACCUserDefaultsKey_ForceMFi4AuthOverNFC
+ _ACCUserDefaultsKey_IgnoreAccInfoUpdateRelaySupport
+ _ACCUserDefaultsKey_IgnoreAuthReset
+ _ACCUserDefaultsKey_MFi4ECDSADisallow
+ _ACCUserDefaultsKey_MFi4ECDSAOnly
+ _ACCUserDefaultsKey_MFi4SigmaIRequired
+ _ACCUserDefaultsKey_PacketLoggingPlainTextOnly
+ _ACCUserDefaultsKey_PretendNoDeviceIdentityCerts
+ ___107-[ACCExternalAccessoryProvider createExternalAccessorySessionForProtocol:accessoryUUID:withEASessionReply:]_block_invoke.225
+ ___107-[ACCExternalAccessoryProvider createExternalAccessorySessionForProtocol:accessoryUUID:withEASessionReply:]_block_invoke.225.cold.1
+ ___138-[ACCTransportClient createEndpointWithTransportType:andProtocol:andIdentifier:andDataOutHandler:forConnectionWithUUID:publishConnection:]_block_invoke.141
+ ___138-[ACCTransportClient createEndpointWithTransportType:andProtocol:andIdentifier:andDataOutHandler:forConnectionWithUUID:publishConnection:]_block_invoke.141.cold.1
+ ___36-[ACCConnectionInfo connectToServer]_block_invoke.169
+ ___36-[ACCConnectionInfo connectToServer]_block_invoke.169.cold.1
+ ___36-[ACCConnectionInfo connectToServer]_block_invoke.169.cold.2
+ ___36-[ACCConnectionInfo connectToServer]_block_invoke.172
+ ___36-[ACCConnectionInfo connectToServer]_block_invoke.172.cold.1
+ ___36-[ACCConnectionInfo connectToServer]_block_invoke.172.cold.2
+ ___37-[ACCTransportClient connectToServer]_block_invoke.119
+ ___37-[ACCTransportClient connectToServer]_block_invoke.119.cold.1
+ ___37-[ACCTransportClient connectToServer]_block_invoke.119.cold.2
+ ___37-[ACCTransportClient connectToServer]_block_invoke.119.cold.3
+ ___46-[ACCTransportClient destroyEndpointWithUUID:]_block_invoke.154
+ ___46-[ACCTransportClient destroyEndpointWithUUID:]_block_invoke.154.cold.1
+ ___48-[ACCConnectionInfo getPairingStatus:withReply:]_block_invoke.238
+ ___48-[ACCConnectionInfo getPairingStatus:withReply:]_block_invoke.238.cold.1
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.198
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.198.cold.1
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.199
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.199.cold.1
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.199.cold.2
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.201
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.201.cold.1
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.201.cold.2
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.204
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.204.cold.1
+ ___48-[ACCTransportClient destroyConnectionWithUUID:]_block_invoke.157
+ ___48-[ACCTransportClient destroyConnectionWithUUID:]_block_invoke.157.cold.1
+ ___48-[ACCTransportClient isConnectionAuthenticated:]_block_invoke.173
+ ___48-[ACCTransportClient publishConnectionWithUUID:]_block_invoke.151
+ ___48-[ACCTransportClient publishConnectionWithUUID:]_block_invoke.151.cold.1
+ ___50-[ACCConnectionInfo copyUserPrivateKey:withReply:]_block_invoke.266
+ ___50-[ACCConnectionInfo copyUserPrivateKey:withReply:]_block_invoke.266.cold.1
+ ___51-[ACCExternalAccessoryProvider currentVehicleInfo:]_block_invoke.245
+ ___51-[ACCExternalAccessoryProvider currentVehicleInfo:]_block_invoke.245.cold.1
+ ___52-[ACCConnectionInfo accessoryInfoForConnectionSync:]_block_invoke.201
+ ___52-[ACCTransportClient identifierForEndpointWithUUID:]_block_invoke.194
+ ___52-[ACCTransportClient propertiesForEndpointWithUUID:]_block_invoke.188
+ ___54-[ACCTransportClient identifierForConnectionWithUUID:]_block_invoke.191
+ ___54-[ACCTransportClient propertiesForConnectionWithUUID:]_block_invoke.185
+ ___55-[ACCTransportClient accessoryInfoForEndpointWithUUID:]_block_invoke.182
+ ___56-[ACCTransportClient connectionUUIDForEndpointWithUUID:]_block_invoke.160
+ ___56-[ACCTransportClient setProperties:forEndpointWithUUID:]_block_invoke.145
+ ___56-[ACCTransportClient setProperties:forEndpointWithUUID:]_block_invoke.145.cold.1
+ ___56-[ACCTransportClient setProperties:forEndpointWithUUID:]_block_invoke.145.cold.2
+ ___56-[ACCTransportClient setProperties:forEndpointWithUUID:]_block_invoke.145.cold.3
+ ___57-[ACCConnectionInfo accessoryPropertySync:forConnection:]_block_invoke.215
+ ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.220
+ ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.220.cold.1
+ ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.220.cold.2
+ ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.220.cold.3
+ ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.221
+ ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.221.cold.1
+ ___57-[ACCTransportClient accessoryInfoForConnectionWithUUID:]_block_invoke.178
+ ___57-[ACCTransportClient endpointUUIDsForConnectionWithUUID:]_block_invoke.164
+ ___57-[ACCTransportClient removeProperty:forEndpointWithUUID:]_block_invoke.148
+ ___57-[ACCTransportClient removeProperty:forEndpointWithUUID:]_block_invoke.148.cold.1
+ ___58-[ACCTransportClient setProperties:forConnectionWithUUID:]_block_invoke.131
+ ___58-[ACCTransportClient setProperties:forConnectionWithUUID:]_block_invoke.131.cold.1
+ ___58-[ACCTransportClient setProperties:forConnectionWithUUID:]_block_invoke.131.cold.2
+ ___58-[ACCTransportClient setProperties:forConnectionWithUUID:]_block_invoke.131.cold.3
+ ___59-[ACCTransportClient removeProperty:forConnectionWithUUID:]_block_invoke.136
+ ___59-[ACCTransportClient removeProperty:forConnectionWithUUID:]_block_invoke.136.cold.1
+ ___59-[ACCTransportClient setAccessoryInfo:forEndpointWithUUID:]_block_invoke.144
+ ___59-[ACCTransportClient setAccessoryInfo:forEndpointWithUUID:]_block_invoke.144.cold.1
+ ___61-[ACCConnectionInfo accessoryInfoForEndpointSync:connection:]_block_invoke.205
+ ___61-[ACCConnectionInfo getInterceptCountForEndpoint:connection:]_block_invoke.225
+ ___61-[ACCTransportClient createConnectionWithType:andIdentifier:]_block_invoke.129
+ ___61-[ACCTransportClient createConnectionWithType:andIdentifier:]_block_invoke.129.cold.1
+ ___62-[ACCTransportClient processIncomingData:forEndpointWithUUID:]_block_invoke.204
+ ___62-[ACCTransportClient processIncomingData:forEndpointWithUUID:]_block_invoke.204.cold.1
+ ___62-[ACCTransportClient processIncomingData:forEndpointWithUUID:]_block_invoke.204.cold.2
+ ___63-[ACCTransportClient authStatusForConnectionWithUUID:authType:]_block_invoke.169
+ ___65-[ACCConnectionInfo getPublicNVMKeyValues:forEndpoint:withReply:]_block_invoke.248
+ ___65-[ACCConnectionInfo getPublicNVMKeyValues:forEndpoint:withReply:]_block_invoke.248.cold.1
+ ___65-[ACCConnectionInfo getPublicNVMKeyValues:forEndpoint:withReply:]_block_invoke.248.cold.2
+ ___65-[ACCConnectionInfo getPublicNVMKeyValues:forEndpoint:withReply:]_block_invoke.248.cold.3
+ ___65-[ACCConnectionInfo getPublicNVMKeyValues:forEndpoint:withReply:]_block_invoke.248.cold.4
+ ___66-[ACCConnectionInfo accessoryPropertySync:forEndpoint:connection:]_block_invoke.219
+ ___74-[ACCTransportClient processOutgoingSecureTunnelData:forEndpoint:forType:]_block_invoke.201
+ ___74-[ACCTransportClient processOutgoingSecureTunnelData:forEndpoint:forType:]_block_invoke.201.cold.1
+ ___74-[ACCTransportClient processOutgoingSecureTunnelData:forEndpoint:forType:]_block_invoke.201.cold.2
+ ___99-[ACCExternalAccessoryProvider sendOutgoingExternalAccessoryData:forEASessionIdentifier:withReply:]_block_invoke.235
+ ___99-[ACCExternalAccessoryProvider sendOutgoingExternalAccessoryData:forEASessionIdentifier:withReply:]_block_invoke.235.cold.1
+ ___block_literal_global.128
+ ___block_literal_global.135
+ ___block_literal_global.140
+ ___block_literal_global.143
+ ___block_literal_global.147
+ ___block_literal_global.150
+ ___block_literal_global.153
+ ___block_literal_global.159
+ ___block_literal_global.163
+ ___block_literal_global.168
+ ___block_literal_global.172
+ ___block_literal_global.175
+ ___block_literal_global.177
+ ___block_literal_global.181
+ ___block_literal_global.184
+ ___block_literal_global.187
+ ___block_literal_global.190
+ ___block_literal_global.194
+ ___block_literal_global.196
+ ___block_literal_global.198
+ ___block_literal_global.200
+ ___block_literal_global.208
+ ___block_literal_global.210
+ ___block_literal_global.212
+ ___block_literal_global.214
+ ___block_literal_global.218
+ ___block_literal_global.219
+ ___block_literal_global.222
+ ___block_literal_global.229
+ ___block_literal_global.231
+ ___block_literal_global.233
+ ___block_literal_global.235
+ ___block_literal_global.237
+ ___block_literal_global.241
+ ___block_literal_global.243
+ ___block_literal_global.245
+ ___block_literal_global.247
+ ___block_literal_global.251
+ ___block_literal_global.253
+ ___block_literal_global.255
+ ___block_literal_global.257
+ ___block_literal_global.259
+ ___block_literal_global.261
+ ___block_literal_global.263
+ ___block_literal_global.265
+ _kACCExternalAccessoryPlatformIDKey
+ _kACCInfo_AccessoryPlatformID
+ _kACCProperties_Endpoint_MFi4Auth_OneWayOnly
+ _kACCProperties_Endpoint_ParentEndpointUUID
+ _kACCVehicleInfoPowerForConnectorTypeNACS_ACKey
+ _kACCVehicleInfoPowerForConnectorTypeNACS_DCKey
+ _kCFACCExternalAccessoryPlatformIDKey
+ _kCFACCInfo_AccessoryPlatformID
+ _kCFACCProperties_Endpoint_MFi4Auth_OneWayOnly
+ _kCFACCProperties_Endpoint_ParentEndpointUUID
+ _kCFACCUserDefaultsKey_ForceAccInfoUpdateRelaySupport
+ _kCFACCUserDefaultsKey_ForceMFi4AuthOverNFC
+ _kCFACCUserDefaultsKey_IgnoreAccInfoUpdateRelaySupport
+ _kCFACCUserDefaultsKey_IgnoreAuthReset
+ _kCFACCUserDefaultsKey_MFi4ECDSADisallow
+ _kCFACCUserDefaultsKey_MFi4ECDSAOnly
+ _kCFACCUserDefaultsKey_MFi4SigmaIRequired
+ _kCFACCUserDefaultsKey_PacketLoggingPlainTextOnly
+ _kCFACCUserDefaultsKey_PretendNoDeviceIdentityCerts
+ _kCFACCVehicleInfoPowerForConnectorTypeNACS_ACKey
+ _kCFACCVehicleInfoPowerForConnectorTypeNACS_DCKey
+ _objc_msgSend$sendWiredCarPlayAvailable:usbIdentifier:wirelessAvailable:bluetoothIdentifier:themeAssetsAvailable:forUUID:
- ___107-[ACCExternalAccessoryProvider createExternalAccessorySessionForProtocol:accessoryUUID:withEASessionReply:]_block_invoke.221
- ___107-[ACCExternalAccessoryProvider createExternalAccessorySessionForProtocol:accessoryUUID:withEASessionReply:]_block_invoke.221.cold.1
- ___138-[ACCTransportClient createEndpointWithTransportType:andProtocol:andIdentifier:andDataOutHandler:forConnectionWithUUID:publishConnection:]_block_invoke.140
- ___138-[ACCTransportClient createEndpointWithTransportType:andProtocol:andIdentifier:andDataOutHandler:forConnectionWithUUID:publishConnection:]_block_invoke.140.cold.1
- ___36-[ACCConnectionInfo connectToServer]_block_invoke.167
- ___36-[ACCConnectionInfo connectToServer]_block_invoke.167.cold.1
- ___36-[ACCConnectionInfo connectToServer]_block_invoke.168.cold.2
- ___36-[ACCConnectionInfo connectToServer]_block_invoke.171
- ___36-[ACCConnectionInfo connectToServer]_block_invoke.171.cold.1
- ___36-[ACCConnectionInfo connectToServer]_block_invoke.171.cold.2
- ___37-[ACCTransportClient connectToServer]_block_invoke.118
- ___37-[ACCTransportClient connectToServer]_block_invoke.118.cold.1
- ___37-[ACCTransportClient connectToServer]_block_invoke.118.cold.2
- ___37-[ACCTransportClient connectToServer]_block_invoke.118.cold.3
- ___46-[ACCTransportClient destroyEndpointWithUUID:]_block_invoke.153
- ___46-[ACCTransportClient destroyEndpointWithUUID:]_block_invoke.153.cold.1
- ___48-[ACCConnectionInfo getPairingStatus:withReply:]_block_invoke.237
- ___48-[ACCConnectionInfo getPairingStatus:withReply:]_block_invoke.237.cold.1
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.194
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.194.cold.1
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.195
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.195.cold.1
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.195.cold.2
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.197
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.197.cold.1
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.197.cold.2
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.200
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.200.cold.1
- ___48-[ACCTransportClient destroyConnectionWithUUID:]_block_invoke.156
- ___48-[ACCTransportClient destroyConnectionWithUUID:]_block_invoke.156.cold.1
- ___48-[ACCTransportClient isConnectionAuthenticated:]_block_invoke.172
- ___48-[ACCTransportClient publishConnectionWithUUID:]_block_invoke.150
- ___48-[ACCTransportClient publishConnectionWithUUID:]_block_invoke.150.cold.1
- ___50-[ACCConnectionInfo copyUserPrivateKey:withReply:]_block_invoke.265
- ___50-[ACCConnectionInfo copyUserPrivateKey:withReply:]_block_invoke.265.cold.1
- ___51-[ACCExternalAccessoryProvider currentVehicleInfo:]_block_invoke.241
- ___51-[ACCExternalAccessoryProvider currentVehicleInfo:]_block_invoke.241.cold.1
- ___52-[ACCConnectionInfo accessoryInfoForConnectionSync:]_block_invoke.200
- ___52-[ACCTransportClient identifierForEndpointWithUUID:]_block_invoke.193
- ___52-[ACCTransportClient propertiesForEndpointWithUUID:]_block_invoke.187
- ___54-[ACCTransportClient identifierForConnectionWithUUID:]_block_invoke.190
- ___54-[ACCTransportClient propertiesForConnectionWithUUID:]_block_invoke.184
- ___55-[ACCTransportClient accessoryInfoForEndpointWithUUID:]_block_invoke.181
- ___56-[ACCTransportClient connectionUUIDForEndpointWithUUID:]_block_invoke.159
- ___56-[ACCTransportClient setProperties:forEndpointWithUUID:]_block_invoke.144
- ___56-[ACCTransportClient setProperties:forEndpointWithUUID:]_block_invoke.144.cold.1
- ___56-[ACCTransportClient setProperties:forEndpointWithUUID:]_block_invoke.144.cold.2
- ___56-[ACCTransportClient setProperties:forEndpointWithUUID:]_block_invoke.144.cold.3
- ___57-[ACCConnectionInfo accessoryPropertySync:forConnection:]_block_invoke.214
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.216
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.216.cold.1
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.216.cold.2
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.216.cold.3
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.217
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.217.cold.1
- ___57-[ACCTransportClient accessoryInfoForConnectionWithUUID:]_block_invoke.177
- ___57-[ACCTransportClient endpointUUIDsForConnectionWithUUID:]_block_invoke.163
- ___57-[ACCTransportClient removeProperty:forEndpointWithUUID:]_block_invoke.147
- ___57-[ACCTransportClient removeProperty:forEndpointWithUUID:]_block_invoke.147.cold.1
- ___58-[ACCTransportClient setProperties:forConnectionWithUUID:]_block_invoke.130
- ___58-[ACCTransportClient setProperties:forConnectionWithUUID:]_block_invoke.130.cold.1
- ___58-[ACCTransportClient setProperties:forConnectionWithUUID:]_block_invoke.130.cold.2
- ___58-[ACCTransportClient setProperties:forConnectionWithUUID:]_block_invoke.130.cold.3
- ___59-[ACCTransportClient removeProperty:forConnectionWithUUID:]_block_invoke.135
- ___59-[ACCTransportClient removeProperty:forConnectionWithUUID:]_block_invoke.135.cold.1
- ___59-[ACCTransportClient setAccessoryInfo:forEndpointWithUUID:]_block_invoke.143
- ___59-[ACCTransportClient setAccessoryInfo:forEndpointWithUUID:]_block_invoke.143.cold.1
- ___61-[ACCConnectionInfo accessoryInfoForEndpointSync:connection:]_block_invoke.204
- ___61-[ACCConnectionInfo getInterceptCountForEndpoint:connection:]_block_invoke.224
- ___61-[ACCTransportClient createConnectionWithType:andIdentifier:]_block_invoke.128
- ___61-[ACCTransportClient createConnectionWithType:andIdentifier:]_block_invoke.128.cold.1
- ___62-[ACCTransportClient processIncomingData:forEndpointWithUUID:]_block_invoke.203
- ___62-[ACCTransportClient processIncomingData:forEndpointWithUUID:]_block_invoke.203.cold.1
- ___62-[ACCTransportClient processIncomingData:forEndpointWithUUID:]_block_invoke.203.cold.2
- ___63-[ACCTransportClient authStatusForConnectionWithUUID:authType:]_block_invoke.168
- ___65-[ACCConnectionInfo getPublicNVMKeyValues:forEndpoint:withReply:]_block_invoke.247
- ___65-[ACCConnectionInfo getPublicNVMKeyValues:forEndpoint:withReply:]_block_invoke.247.cold.1
- ___65-[ACCConnectionInfo getPublicNVMKeyValues:forEndpoint:withReply:]_block_invoke.247.cold.2
- ___65-[ACCConnectionInfo getPublicNVMKeyValues:forEndpoint:withReply:]_block_invoke.247.cold.3
- ___65-[ACCConnectionInfo getPublicNVMKeyValues:forEndpoint:withReply:]_block_invoke.247.cold.4
- ___66-[ACCConnectionInfo accessoryPropertySync:forEndpoint:connection:]_block_invoke.218
- ___74-[ACCTransportClient processOutgoingSecureTunnelData:forEndpoint:forType:]_block_invoke.200
- ___74-[ACCTransportClient processOutgoingSecureTunnelData:forEndpoint:forType:]_block_invoke.200.cold.1
- ___74-[ACCTransportClient processOutgoingSecureTunnelData:forEndpoint:forType:]_block_invoke.200.cold.2
- ___99-[ACCExternalAccessoryProvider sendOutgoingExternalAccessoryData:forEASessionIdentifier:withReply:]_block_invoke.231
- ___99-[ACCExternalAccessoryProvider sendOutgoingExternalAccessoryData:forEASessionIdentifier:withReply:]_block_invoke.231.cold.1
- ___block_literal_global.127
- ___block_literal_global.134
- ___block_literal_global.139
- ___block_literal_global.142
- ___block_literal_global.146
- ___block_literal_global.149
- ___block_literal_global.152
- ___block_literal_global.155
- ___block_literal_global.158
- ___block_literal_global.162
- ___block_literal_global.167
- ___block_literal_global.170
- ___block_literal_global.173
- ___block_literal_global.176
- ___block_literal_global.180
- ___block_literal_global.183
- ___block_literal_global.186
- ___block_literal_global.189
- ___block_literal_global.192
- ___block_literal_global.195
- ___block_literal_global.197
- ___block_literal_global.199
- ___block_literal_global.202
- ___block_literal_global.207
- ___block_literal_global.209
- ___block_literal_global.211
- ___block_literal_global.213
- ___block_literal_global.215
- ___block_literal_global.217
- ___block_literal_global.220
- ___block_literal_global.221
- ___block_literal_global.223
- ___block_literal_global.226
- ___block_literal_global.227
- ___block_literal_global.236
- ___block_literal_global.240
- ___block_literal_global.242
- ___block_literal_global.246
- ___block_literal_global.250
- ___block_literal_global.252
- ___block_literal_global.254
- ___block_literal_global.256
- ___block_literal_global.258
- ___block_literal_global.260
- ___block_literal_global.262
- ___block_literal_global.264
- _arc4random_buf
CStrings:
+ "ACCExternalAccessoryPlatformIDKey"
+ "AccessoryPlatformID"
+ "EAVehicleInfoPowerForConnectorTypeNACS_ACKey"
+ "EAVehicleInfoPowerForConnectorTypeNACS_DCKey"
+ "ForceAccInfoUpdateRelaySupport"
+ "ForceMFi4AuthOverNFC"
+ "IgnoreAccInfoUpdateRelaySupport"
+ "IgnoreAuthReset"
+ "MFi4Auth_OneWayOnly"
+ "MFi4ECDSADisallow"
+ "MFi4ECDSAOnly"
+ "MFi4SigmaIRequired"
+ "PacketLoggingPlainTextOnly"
+ "ParentEndpointUUID"
+ "PretendNoDeviceIdentityCerts"
+ "T@\"NSString\",?,R,C"
+ "[#CarPlay] sendWiredCarPlayAvailable: %@, wiredAvailable %@, usbIdentifier %@, wirelessAvailable %@, bluetoothIdentifier %@ assetsAvailable %@"
+ "sendWiredCarPlayAvailable:usbIdentifier:wirelessAvailable:bluetoothIdentifier:themeAssetsAvailable:forUUID:"
+ "v44@0:8@\"NSData\"16@\"NSString\"24S32@?<v@?B>36"
+ "v44@0:8@16@24S32@?36"
+ "v64@0:8@\"NSNumber\"16@\"NSString\"24@\"NSNumber\"32@\"NSString\"40@\"NSNumber\"48@\"NSString\"56"
+ "v64@0:8@16@24@32@40@48@56"
- "v44@0:8@\"NSData\"16@\"NSString\"24C32@?<v@?B>36"
- "v44@0:8@16@24C32@?36"

```
