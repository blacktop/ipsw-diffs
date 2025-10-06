## HomeKit

> `/System/Library/Frameworks/HomeKit.framework/HomeKit`

```diff

-1054.1.7.1.4
-  __TEXT.__text: 0x2513f4
+1076.2.8.1.1
+  __TEXT.__text: 0x25d8d0
   __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_methlist: 0x1f004
-  __TEXT.__const: 0x274
-  __TEXT.__gcc_except_tab: 0x3e90
-  __TEXT.__cstring: 0x24e66
-  __TEXT.__oslogstring: 0x24d42
+  __TEXT.__objc_methlist: 0x1fe04
+  __TEXT.__const: 0x290
+  __TEXT.__gcc_except_tab: 0x3f6c
+  __TEXT.__cstring: 0x256ce
+  __TEXT.__oslogstring: 0x24f52
   __TEXT.__dlopen_cstrs: 0x3a2
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x8ff8
-  __TEXT.__objc_classname: 0x4800
-  __TEXT.__objc_methname: 0x3cfe3
-  __TEXT.__objc_methtype: 0x71c3
-  __TEXT.__objc_stubs: 0x22b80
+  __TEXT.__unwind_info: 0x9298
+  __TEXT.__objc_classname: 0x4a29
+  __TEXT.__objc_methname: 0x3eb11
+  __TEXT.__objc_methtype: 0x74a6
+  __TEXT.__objc_stubs: 0x23560
   __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0x6bb0
-  __DATA_CONST.__objc_classlist: 0x1030
-  __DATA_CONST.__objc_catlist: 0xd8
+  __DATA_CONST.__const: 0x6d00
+  __DATA_CONST.__objc_classlist: 0x1090
+  __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x470
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x302f0
-  __DATA_CONST.__objc_selrefs: 0xb470
+  __DATA_CONST.__objc_const: 0x316b0
+  __DATA_CONST.__objc_selrefs: 0xb998
   __DATA_CONST.__objc_arraydata: 0x1330
-  __AUTH_CONST.__cfstring: 0x22a20
-  __AUTH_CONST.__objc_const: 0xef58
-  __AUTH_CONST.__const: 0x18e0
-  __AUTH_CONST.__objc_intobj: 0x780
+  __AUTH_CONST.__cfstring: 0x232c0
+  __AUTH_CONST.__objc_const: 0xf3c8
+  __AUTH_CONST.__const: 0x1920
+  __AUTH_CONST.__objc_intobj: 0x798
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x540
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_got: 0x688
-  __AUTH.__objc_data: 0x7940
+  __AUTH.__objc_data: 0x7d00
   __DATA.__objc_protorefs: 0x98
-  __DATA.__objc_classrefs: 0x12c0
-  __DATA.__objc_superrefs: 0xd88
-  __DATA.__objc_ivar: 0x2004
+  __DATA.__objc_classrefs: 0x1330
+  __DATA.__objc_superrefs: 0xde0
+  __DATA.__objc_ivar: 0x211c
   __DATA.__data: 0x3608
   __DATA.__common: 0x18
-  __DATA.__bss: 0x7e0
+  __DATA.__bss: 0x7f0
   __DATA_DIRTY.__objc_data: 0x28a0
-  __DATA_DIRTY.__bss: 0x1f0
+  __DATA_DIRTY.__bss: 0x1e0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AC988A81-DED9-3459-9A65-37A2CE4CCEE5
-  Functions: 12168
-  Symbols:   39199
-  CStrings:  22461
+  UUID: 91181732-E42D-3DFC-B6B7-623908CACFF5
+  Functions: 12493
+  Symbols:   40112
+  CStrings:  22917
 
Symbols:
+ +[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo visibleAccessoriesInfoType]
+ +[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo visibleIDSDevicesType]
+ +[HMExecuteTurnOffRequest executeRequestWithActionSet:]
+ +[HMFWiFiNetworkInfo(WifiInfoSerialization) wifiNetworkInfoFromProto:]
+ +[HMRemoteEventRouterProtoServerDiagnosticInfo connectedClientsType]
+ -[HMAccessoryDiagnosticInfo .cxx_destruct]
+ -[HMAccessoryDiagnosticInfo cdpStatusGood]
+ -[HMAccessoryDiagnosticInfo cloudkitAccountStatusGood]
+ -[HMAccessoryDiagnosticInfo connectedClientsDescription]
+ -[HMAccessoryDiagnosticInfo currentAccessoryUUID]
+ -[HMAccessoryDiagnosticInfo currrentAccessoryMediaRouteId]
+ -[HMAccessoryDiagnosticInfo description]
+ -[HMAccessoryDiagnosticInfo firstCloudImportDone]
+ -[HMAccessoryDiagnosticInfo idsIdentifier]
+ -[HMAccessoryDiagnosticInfo idsStatusGood]
+ -[HMAccessoryDiagnosticInfo initWithProtoData:]
+ -[HMAccessoryDiagnosticInfo isEventRouterServerConnected]
+ -[HMAccessoryDiagnosticInfo isPrimaryResident]
+ -[HMAccessoryDiagnosticInfo isRunningHH2]
+ -[HMAccessoryDiagnosticInfo manufacturer]
+ -[HMAccessoryDiagnosticInfo model]
+ -[HMAccessoryDiagnosticInfo numHomes]
+ -[HMAccessoryDiagnosticInfo serialNumber]
+ -[HMAccessoryDiagnosticInfo serverLastConnected]
+ -[HMAccessoryDiagnosticInfo softwareVersion]
+ -[HMAccessoryDiagnosticInfo version]
+ -[HMAccessoryDiagnosticInfo wifiInfo]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo .cxx_destruct]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo cloudInfo]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo copyTo:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo copyWithZone:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo currentAccessoryInfo]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo description]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo dictionaryRepresentation]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo eventRouterServerInfo]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo generationTime]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasCloudInfo]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasCurrentAccessoryInfo]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasEventRouterServerInfo]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasGenerationTime]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasIdsInfo]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasManufacturer]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasMediaRouteIdString]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasModelIdentifier]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasRegionInfo]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasSerialNumber]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasSoftwareVersion]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasWifiInfo]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hash]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo idsInfo]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo isEqual:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo manufacturer]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo mediaRouteIdString]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo mergeFrom:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo modelIdentifier]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo readFrom:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo regionInfo]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo serialNumber]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setCloudInfo:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setCurrentAccessoryInfo:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setEventRouterServerInfo:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setGenerationTime:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setHasGenerationTime:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setIdsInfo:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setManufacturer:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setMediaRouteIdString:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setModelIdentifier:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setRegionInfo:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setSerialNumber:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setSoftwareVersion:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setWifiInfo:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo softwareVersion]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo wifiInfo]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo writeTo:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo StringAsCloudState:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo StringAsOctagonState:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo cloudStateAsString:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo cloudState]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo copyTo:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo copyWithZone:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo description]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo dictionaryRepresentation]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo firstCloudImportComplete]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo hasCloudState]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo hasFirstCloudImportComplete]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo hasOctagonState]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo hash]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo isEqual:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo mergeFrom:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo octagonStateAsString:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo octagonState]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo readFrom:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo setCloudState:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo setFirstCloudImportComplete:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo setHasCloudState:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo setHasFirstCloudImportComplete:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo setHasOctagonState:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo setOctagonState:]
+ -[HMAccessoryDiagnosticInfoProtoCloudInfo writeTo:]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo .cxx_destruct]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo copyTo:]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo copyWithZone:]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo description]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo dictionaryRepresentation]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo hasPublicPairingIdentity]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo hasUuidString]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo hash]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo isEqual:]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo mergeFrom:]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo publicPairingIdentity]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo readFrom:]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo setPublicPairingIdentity:]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo setUuidString:]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo uuidString]
+ -[HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo writeTo:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo .cxx_destruct]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo appleMediaAccessoryDiagnosticInfo]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo copyTo:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo copyWithZone:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo description]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo dictionaryRepresentation]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo generationTime]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo hasAppleMediaAccessoryDiagnosticInfo]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo hasGenerationTime]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo hasHomeHubVersion]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo hasNumHomes]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo hasPrimaryResidentDiagnosticInfo]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo hasVersion]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo hash]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo homeHubVersion]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo isEqual:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo mergeFrom:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo numHomes]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo primaryResidentDiagnosticInfo]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo readFrom:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo setAppleMediaAccessoryDiagnosticInfo:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo setGenerationTime:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo setHasGenerationTime:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo setHasHomeHubVersion:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo setHasNumHomes:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo setHasVersion:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo setHomeHubVersion:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo setNumHomes:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo setPrimaryResidentDiagnosticInfo:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo setVersion:]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo version]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo writeTo:]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo .cxx_destruct]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo StringAsIdsState:]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo copyTo:]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo copyWithZone:]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo description]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo dictionaryRepresentation]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo hasIdsIdentifierString]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo hasIdsState]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo hash]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo idsIdentifierString]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo idsStateAsString:]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo idsState]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo isEqual:]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo mergeFrom:]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo readFrom:]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo setHasIdsState:]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo setIdsIdentifierString:]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo setIdsState:]
+ -[HMAccessoryDiagnosticInfoProtoIdsInfo writeTo:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo .cxx_destruct]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo addVisibleAccessoriesInfo:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo addVisibleIDSDevices:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo clearVisibleAccessoriesInfos]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo clearVisibleIDSDevices]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo copyTo:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo copyWithZone:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo description]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo dictionaryRepresentation]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo eventRouterServerInfo]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo hasEventRouterServerInfo]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo hasWifiInfo]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo hash]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo isEqual:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo mergeFrom:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo readFrom:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo setEventRouterServerInfo:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo setVisibleAccessoriesInfos:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo setVisibleIDSDevices:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo setWifiInfo:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo visibleAccessoriesInfoAtIndex:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo visibleAccessoriesInfosCount]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo visibleAccessoriesInfos]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo visibleIDSDevicesAtIndex:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo visibleIDSDevicesCount]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo visibleIDSDevices]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo wifiInfo]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo writeTo:]
+ -[HMAccessoryInfoProtoWifiNetworkInfoEvent hasNetworkBSSID]
+ -[HMAccessoryInfoProtoWifiNetworkInfoEvent hasNetworkGatewayIPAddress]
+ -[HMAccessoryInfoProtoWifiNetworkInfoEvent hasNetworkGatewayMacAddress]
+ -[HMAccessoryInfoProtoWifiNetworkInfoEvent hasNetworkRSSI]
+ -[HMAccessoryInfoProtoWifiNetworkInfoEvent networkBSSID]
+ -[HMAccessoryInfoProtoWifiNetworkInfoEvent networkGatewayIPAddress]
+ -[HMAccessoryInfoProtoWifiNetworkInfoEvent networkGatewayMacAddress]
+ -[HMAccessoryInfoProtoWifiNetworkInfoEvent networkRSSI]
+ -[HMAccessoryInfoProtoWifiNetworkInfoEvent setHasNetworkRSSI:]
+ -[HMAccessoryInfoProtoWifiNetworkInfoEvent setNetworkBSSID:]
+ -[HMAccessoryInfoProtoWifiNetworkInfoEvent setNetworkGatewayIPAddress:]
+ -[HMAccessoryInfoProtoWifiNetworkInfoEvent setNetworkGatewayMacAddress:]
+ -[HMAccessoryInfoProtoWifiNetworkInfoEvent setNetworkRSSI:]
+ -[HMDeviceSetupOperation initWithSession:setupSession:]
+ -[HMFWifiNetworkAssociation(WifiInfoSerialization) protoPayload]
+ -[HMHomeManager addEphemeralContainer:completion:]
+ -[HMHomeManager deactivateEphemeralContainer:completion:]
+ -[HMHomeManager deleteCountersBeforeDate:afterDate:completion:]
+ -[HMHomeManager deleteEphemeralContainer:completion:]
+ -[HMHomeManager fetchAppleMediaAccesoryDiagnosticInfo:options:completion:]
+ -[HMHomeManager fetchDiagnosticInfoWithCompletionHandler:]
+ -[HMHomeManager initWithUUID:configuration:context:xpcEventRouterClient:lastEventStore:timerFactory:darwinNotificationProvider:privacySettingsProvider:]
+ -[HMHomeManager listEphemeralContainersWithCompletion:]
+ -[HMHomeManager privacySettingsProvider]
+ -[HMHomeManager readCountersForGroup:homeUUIDString:accessoryUUIDString:counter:statistics:datePartition:ephemeralContainer:completion:]
+ -[HMHomeManager saveCountersWithCompletion:]
+ -[HMHomeManager startupEphemeralContainer:completion:]
+ -[HMHomeManagerConfiguration canWriteToCache]
+ -[HMProtoResidentCapabilities hasSupportsMatterTTU]
+ -[HMProtoResidentCapabilities setHasSupportsMatterTTU:]
+ -[HMProtoResidentCapabilities setSupportsMatterTTU:]
+ -[HMProtoResidentCapabilities supportsMatterTTU]
+ -[HMRemoteEventRouterProtoConnectedClientInfo .cxx_destruct]
+ -[HMRemoteEventRouterProtoConnectedClientInfo connectedClientIdentifierString]
+ -[HMRemoteEventRouterProtoConnectedClientInfo copyTo:]
+ -[HMRemoteEventRouterProtoConnectedClientInfo copyWithZone:]
+ -[HMRemoteEventRouterProtoConnectedClientInfo description]
+ -[HMRemoteEventRouterProtoConnectedClientInfo dictionaryRepresentation]
+ -[HMRemoteEventRouterProtoConnectedClientInfo hasConnectedClientIdentifierString]
+ -[HMRemoteEventRouterProtoConnectedClientInfo hash]
+ -[HMRemoteEventRouterProtoConnectedClientInfo isEqual:]
+ -[HMRemoteEventRouterProtoConnectedClientInfo mergeFrom:]
+ -[HMRemoteEventRouterProtoConnectedClientInfo readFrom:]
+ -[HMRemoteEventRouterProtoConnectedClientInfo setConnectedClientIdentifierString:]
+ -[HMRemoteEventRouterProtoConnectedClientInfo writeTo:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo .cxx_destruct]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo StringAsConnectionState:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo StringAsMode:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo addConnectedClients:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo clearConnectedClients]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo connectedClientsAtIndex:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo connectedClientsCount]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo connectedClients]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo connectionStateAsString:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo connectionState]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo copyTo:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo copyWithZone:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo description]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo dictionaryRepresentation]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo hasConnectionState]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo hasLastConnected]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo hasMode]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo hasVersion]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo hash]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo isEqual:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo lastConnected]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo mergeFrom:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo modeAsString:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo mode]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo readFrom:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo setConnectedClients:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo setConnectionState:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo setHasConnectionState:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo setHasLastConnected:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo setHasMode:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo setHasVersion:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo setLastConnected:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo setMode:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo setVersion:]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo version]
+ -[HMRemoteEventRouterProtoServerDiagnosticInfo writeTo:]
+ -[HMResidentCapabilities supportsMatterTTU]
+ -[HMWidgetManager fetchStateForActionSets:completion:]
+ -[HMWidgetManager monitorAndFetchStateForActionSets:widgetIdentifier:kind:completion:]
+ -[HMWidgetManager performRequests:forKind:completion:]
+ -[HMWidgetManagerFetchStateForActionSetsResponse .cxx_destruct]
+ -[HMWidgetManagerFetchStateForActionSetsResponse didExecutionFailByActionSetUniqueIdentifier]
+ -[HMWidgetManagerFetchStateForActionSetsResponse initWithIsOnByActionSetsUniqueIdentifier:didExecutionFailByActionSetUniqueIdentifier:]
+ -[HMWidgetManagerFetchStateForActionSetsResponse isOnByActionSetUniqueIdentifier]
+ -[HMWidgetManagerMonitorActionSetsResponse .cxx_destruct]
+ -[HMWidgetManagerMonitorActionSetsResponse didExecutionFailByActionSetUniqueIdentifier]
+ -[HMWidgetManagerMonitorActionSetsResponse initWithIsOnByActionSetsUniqueIdentifier:didExecutionFailByActionSetUniqueIdentifier:]
+ -[HMWidgetManagerMonitorActionSetsResponse isOnByActionSetUniqueIdentifier]
+ -[_HMPrivacySettingsProvider requestHomeKitAccessWithQueue:completion:]
+ -[_HMPrivacySettingsProvider requestMicrophoneAccessWithQueue:completion:]
+ GCC_except_table1005
+ GCC_except_table10187
+ GCC_except_table10189
+ GCC_except_table10191
+ GCC_except_table10192
+ GCC_except_table10222
+ GCC_except_table10224
+ GCC_except_table10226
+ GCC_except_table10232
+ GCC_except_table10233
+ GCC_except_table10234
+ GCC_except_table10341
+ GCC_except_table10342
+ GCC_except_table10369
+ GCC_except_table10371
+ GCC_except_table10375
+ GCC_except_table10376
+ GCC_except_table10450
+ GCC_except_table10463
+ GCC_except_table10487
+ GCC_except_table10491
+ GCC_except_table10532
+ GCC_except_table10533
+ GCC_except_table10534
+ GCC_except_table10535
+ GCC_except_table10536
+ GCC_except_table10537
+ GCC_except_table10538
+ GCC_except_table10539
+ GCC_except_table10540
+ GCC_except_table10541
+ GCC_except_table10542
+ GCC_except_table10543
+ GCC_except_table10544
+ GCC_except_table10545
+ GCC_except_table10546
+ GCC_except_table10563
+ GCC_except_table10590
+ GCC_except_table10697
+ GCC_except_table10698
+ GCC_except_table10701
+ GCC_except_table10763
+ GCC_except_table10765
+ GCC_except_table10773
+ GCC_except_table10779
+ GCC_except_table10780
+ GCC_except_table10786
+ GCC_except_table10788
+ GCC_except_table10793
+ GCC_except_table10794
+ GCC_except_table10795
+ GCC_except_table11023
+ GCC_except_table1120
+ GCC_except_table11202
+ GCC_except_table11205
+ GCC_except_table11210
+ GCC_except_table11214
+ GCC_except_table11220
+ GCC_except_table11225
+ GCC_except_table11227
+ GCC_except_table11232
+ GCC_except_table11233
+ GCC_except_table11235
+ GCC_except_table11318
+ GCC_except_table11320
+ GCC_except_table11339
+ GCC_except_table11340
+ GCC_except_table11341
+ GCC_except_table11342
+ GCC_except_table11347
+ GCC_except_table11361
+ GCC_except_table11367
+ GCC_except_table11372
+ GCC_except_table1142
+ GCC_except_table11452
+ GCC_except_table11454
+ GCC_except_table11457
+ GCC_except_table11465
+ GCC_except_table11466
+ GCC_except_table11471
+ GCC_except_table11479
+ GCC_except_table11481
+ GCC_except_table11483
+ GCC_except_table11485
+ GCC_except_table11487
+ GCC_except_table11621
+ GCC_except_table11676
+ GCC_except_table11677
+ GCC_except_table11678
+ GCC_except_table11689
+ GCC_except_table11690
+ GCC_except_table11714
+ GCC_except_table11715
+ GCC_except_table11769
+ GCC_except_table11794
+ GCC_except_table11797
+ GCC_except_table11929
+ GCC_except_table12049
+ GCC_except_table12050
+ GCC_except_table12051
+ GCC_except_table12099
+ GCC_except_table12100
+ GCC_except_table12102
+ GCC_except_table12105
+ GCC_except_table12107
+ GCC_except_table12109
+ GCC_except_table12141
+ GCC_except_table12184
+ GCC_except_table12189
+ GCC_except_table1219
+ GCC_except_table12192
+ GCC_except_table1222
+ GCC_except_table12252
+ GCC_except_table12337
+ GCC_except_table12344
+ GCC_except_table1236
+ GCC_except_table12398
+ GCC_except_table12400
+ GCC_except_table12409
+ GCC_except_table12412
+ GCC_except_table12432
+ GCC_except_table12434
+ GCC_except_table12435
+ GCC_except_table1371
+ GCC_except_table1440
+ GCC_except_table1443
+ GCC_except_table1512
+ GCC_except_table1514
+ GCC_except_table1588
+ GCC_except_table1589
+ GCC_except_table1637
+ GCC_except_table1866
+ GCC_except_table1869
+ GCC_except_table1872
+ GCC_except_table1877
+ GCC_except_table1890
+ GCC_except_table1892
+ GCC_except_table1895
+ GCC_except_table1905
+ GCC_except_table1907
+ GCC_except_table1908
+ GCC_except_table1913
+ GCC_except_table1914
+ GCC_except_table1915
+ GCC_except_table1916
+ GCC_except_table2100
+ GCC_except_table2102
+ GCC_except_table2106
+ GCC_except_table2108
+ GCC_except_table2110
+ GCC_except_table2112
+ GCC_except_table2118
+ GCC_except_table2341
+ GCC_except_table2344
+ GCC_except_table2358
+ GCC_except_table2390
+ GCC_except_table2406
+ GCC_except_table2407
+ GCC_except_table2410
+ GCC_except_table2433
+ GCC_except_table2435
+ GCC_except_table2437
+ GCC_except_table2439
+ GCC_except_table2599
+ GCC_except_table2617
+ GCC_except_table2618
+ GCC_except_table2674
+ GCC_except_table2676
+ GCC_except_table2679
+ GCC_except_table2704
+ GCC_except_table2706
+ GCC_except_table2714
+ GCC_except_table2716
+ GCC_except_table2723
+ GCC_except_table2724
+ GCC_except_table2725
+ GCC_except_table2727
+ GCC_except_table2728
+ GCC_except_table2729
+ GCC_except_table2730
+ GCC_except_table2731
+ GCC_except_table2783
+ GCC_except_table2807
+ GCC_except_table2810
+ GCC_except_table2813
+ GCC_except_table2816
+ GCC_except_table2819
+ GCC_except_table2822
+ GCC_except_table2825
+ GCC_except_table2890
+ GCC_except_table2891
+ GCC_except_table2935
+ GCC_except_table2942
+ GCC_except_table2943
+ GCC_except_table2944
+ GCC_except_table2947
+ GCC_except_table2948
+ GCC_except_table2949
+ GCC_except_table2951
+ GCC_except_table2967
+ GCC_except_table2968
+ GCC_except_table2986
+ GCC_except_table2993
+ GCC_except_table2997
+ GCC_except_table3000
+ GCC_except_table3003
+ GCC_except_table3046
+ GCC_except_table3050
+ GCC_except_table3055
+ GCC_except_table3063
+ GCC_except_table3067
+ GCC_except_table3076
+ GCC_except_table3078
+ GCC_except_table3310
+ GCC_except_table3316
+ GCC_except_table3319
+ GCC_except_table3323
+ GCC_except_table3324
+ GCC_except_table3327
+ GCC_except_table3333
+ GCC_except_table3340
+ GCC_except_table3364
+ GCC_except_table3366
+ GCC_except_table3368
+ GCC_except_table3371
+ GCC_except_table3372
+ GCC_except_table3374
+ GCC_except_table3377
+ GCC_except_table3459
+ GCC_except_table3464
+ GCC_except_table3476
+ GCC_except_table3479
+ GCC_except_table3481
+ GCC_except_table3484
+ GCC_except_table3491
+ GCC_except_table3544
+ GCC_except_table3610
+ GCC_except_table3625
+ GCC_except_table3628
+ GCC_except_table3742
+ GCC_except_table3743
+ GCC_except_table3745
+ GCC_except_table3750
+ GCC_except_table3754
+ GCC_except_table3757
+ GCC_except_table3759
+ GCC_except_table3767
+ GCC_except_table3965
+ GCC_except_table3968
+ GCC_except_table3980
+ GCC_except_table4052
+ GCC_except_table4071
+ GCC_except_table4158
+ GCC_except_table4273
+ GCC_except_table4278
+ GCC_except_table4279
+ GCC_except_table4287
+ GCC_except_table4289
+ GCC_except_table4314
+ GCC_except_table4315
+ GCC_except_table4317
+ GCC_except_table4377
+ GCC_except_table4387
+ GCC_except_table4452
+ GCC_except_table4454
+ GCC_except_table4456
+ GCC_except_table4498
+ GCC_except_table4501
+ GCC_except_table4502
+ GCC_except_table4576
+ GCC_except_table4662
+ GCC_except_table4663
+ GCC_except_table4669
+ GCC_except_table4671
+ GCC_except_table4700
+ GCC_except_table4702
+ GCC_except_table4721
+ GCC_except_table4767
+ GCC_except_table4816
+ GCC_except_table4899
+ GCC_except_table4919
+ GCC_except_table4920
+ GCC_except_table4921
+ GCC_except_table4923
+ GCC_except_table4926
+ GCC_except_table4927
+ GCC_except_table4929
+ GCC_except_table5135
+ GCC_except_table5141
+ GCC_except_table5143
+ GCC_except_table5153
+ GCC_except_table5154
+ GCC_except_table5401
+ GCC_except_table5507
+ GCC_except_table5513
+ GCC_except_table5520
+ GCC_except_table5601
+ GCC_except_table5607
+ GCC_except_table5609
+ GCC_except_table5746
+ GCC_except_table5903
+ GCC_except_table5904
+ GCC_except_table5929
+ GCC_except_table5931
+ GCC_except_table5937
+ GCC_except_table5945
+ GCC_except_table5967
+ GCC_except_table5984
+ GCC_except_table5989
+ GCC_except_table6025
+ GCC_except_table6042
+ GCC_except_table6046
+ GCC_except_table6054
+ GCC_except_table6059
+ GCC_except_table6073
+ GCC_except_table6078
+ GCC_except_table6086
+ GCC_except_table6088
+ GCC_except_table6091
+ GCC_except_table6096
+ GCC_except_table6103
+ GCC_except_table6108
+ GCC_except_table6112
+ GCC_except_table613
+ GCC_except_table6146
+ GCC_except_table616
+ GCC_except_table617
+ GCC_except_table6171
+ GCC_except_table6176
+ GCC_except_table618
+ GCC_except_table6180
+ GCC_except_table619
+ GCC_except_table620
+ GCC_except_table6209
+ GCC_except_table6213
+ GCC_except_table6215
+ GCC_except_table6216
+ GCC_except_table622
+ GCC_except_table623
+ GCC_except_table630
+ GCC_except_table631
+ GCC_except_table6354
+ GCC_except_table6360
+ GCC_except_table6440
+ GCC_except_table6462
+ GCC_except_table6467
+ GCC_except_table6475
+ GCC_except_table6520
+ GCC_except_table6522
+ GCC_except_table6534
+ GCC_except_table6545
+ GCC_except_table6571
+ GCC_except_table6580
+ GCC_except_table6587
+ GCC_except_table6590
+ GCC_except_table6593
+ GCC_except_table6596
+ GCC_except_table6599
+ GCC_except_table6607
+ GCC_except_table6617
+ GCC_except_table6641
+ GCC_except_table6644
+ GCC_except_table6647
+ GCC_except_table6650
+ GCC_except_table6656
+ GCC_except_table6659
+ GCC_except_table6662
+ GCC_except_table6665
+ GCC_except_table6668
+ GCC_except_table6671
+ GCC_except_table6674
+ GCC_except_table6677
+ GCC_except_table6680
+ GCC_except_table6683
+ GCC_except_table6686
+ GCC_except_table6689
+ GCC_except_table6693
+ GCC_except_table6705
+ GCC_except_table6706
+ GCC_except_table6714
+ GCC_except_table6731
+ GCC_except_table6733
+ GCC_except_table6758
+ GCC_except_table6772
+ GCC_except_table6774
+ GCC_except_table6794
+ GCC_except_table6798
+ GCC_except_table6921
+ GCC_except_table7123
+ GCC_except_table7217
+ GCC_except_table7321
+ GCC_except_table7332
+ GCC_except_table7426
+ GCC_except_table7432
+ GCC_except_table7434
+ GCC_except_table7436
+ GCC_except_table7437
+ GCC_except_table7568
+ GCC_except_table7571
+ GCC_except_table7582
+ GCC_except_table7585
+ GCC_except_table7587
+ GCC_except_table7590
+ GCC_except_table7621
+ GCC_except_table7623
+ GCC_except_table7641
+ GCC_except_table7649
+ GCC_except_table7651
+ GCC_except_table7653
+ GCC_except_table7660
+ GCC_except_table7666
+ GCC_except_table7668
+ GCC_except_table7670
+ GCC_except_table7671
+ GCC_except_table7681
+ GCC_except_table7682
+ GCC_except_table7683
+ GCC_except_table7694
+ GCC_except_table7696
+ GCC_except_table7698
+ GCC_except_table7739
+ GCC_except_table7741
+ GCC_except_table7749
+ GCC_except_table7751
+ GCC_except_table7753
+ GCC_except_table7755
+ GCC_except_table7757
+ GCC_except_table7763
+ GCC_except_table7779
+ GCC_except_table7781
+ GCC_except_table7783
+ GCC_except_table7785
+ GCC_except_table7804
+ GCC_except_table7954
+ GCC_except_table7956
+ GCC_except_table7957
+ GCC_except_table7958
+ GCC_except_table7960
+ GCC_except_table7962
+ GCC_except_table7963
+ GCC_except_table7964
+ GCC_except_table8000
+ GCC_except_table8003
+ GCC_except_table8004
+ GCC_except_table8007
+ GCC_except_table8010
+ GCC_except_table8011
+ GCC_except_table8055
+ GCC_except_table8056
+ GCC_except_table8057
+ GCC_except_table8064
+ GCC_except_table8065
+ GCC_except_table8067
+ GCC_except_table8129
+ GCC_except_table8131
+ GCC_except_table8168
+ GCC_except_table8350
+ GCC_except_table8351
+ GCC_except_table8355
+ GCC_except_table836
+ GCC_except_table8410
+ GCC_except_table843
+ GCC_except_table8431
+ GCC_except_table8502
+ GCC_except_table8508
+ GCC_except_table8510
+ GCC_except_table8512
+ GCC_except_table8514
+ GCC_except_table8522
+ GCC_except_table8571
+ GCC_except_table8572
+ GCC_except_table8574
+ GCC_except_table8599
+ GCC_except_table8627
+ GCC_except_table866
+ GCC_except_table875
+ GCC_except_table8785
+ GCC_except_table8844
+ GCC_except_table8854
+ GCC_except_table8858
+ GCC_except_table8871
+ GCC_except_table8874
+ GCC_except_table8877
+ GCC_except_table8879
+ GCC_except_table8909
+ GCC_except_table8929
+ GCC_except_table8930
+ GCC_except_table8931
+ GCC_except_table8968
+ GCC_except_table8969
+ GCC_except_table8973
+ GCC_except_table8975
+ GCC_except_table8977
+ GCC_except_table9036
+ GCC_except_table9063
+ GCC_except_table9066
+ GCC_except_table9068
+ GCC_except_table9070
+ GCC_except_table9072
+ GCC_except_table9074
+ GCC_except_table9080
+ GCC_except_table9082
+ GCC_except_table9088
+ GCC_except_table9092
+ GCC_except_table9095
+ GCC_except_table9103
+ GCC_except_table9107
+ GCC_except_table9113
+ GCC_except_table9119
+ GCC_except_table9122
+ GCC_except_table9130
+ GCC_except_table9131
+ GCC_except_table9158
+ GCC_except_table9369
+ GCC_except_table9382
+ GCC_except_table943
+ GCC_except_table9431
+ GCC_except_table9432
+ GCC_except_table9434
+ GCC_except_table9438
+ GCC_except_table9442
+ GCC_except_table945
+ GCC_except_table948
+ GCC_except_table9498
+ GCC_except_table950
+ GCC_except_table9501
+ GCC_except_table9502
+ GCC_except_table952
+ GCC_except_table956
+ GCC_except_table9812
+ GCC_except_table9851
+ GCC_except_table9864
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._cloudInfo
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._currentAccessoryInfo
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._eventRouterServerInfo
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._generationTime
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._has
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._idsInfo
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._manufacturer
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._mediaRouteIdString
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._modelIdentifier
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._regionInfo
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._serialNumber
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._softwareVersion
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._wifiInfo
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoCloudInfo._cloudState
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoCloudInfo._firstCloudImportComplete
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoCloudInfo._has
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoCloudInfo._octagonState
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo._publicPairingIdentity
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo._uuidString
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoDiagnosticInfo._appleMediaAccessoryDiagnosticInfo
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoDiagnosticInfo._generationTime
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoDiagnosticInfo._has
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoDiagnosticInfo._homeHubVersion
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoDiagnosticInfo._numHomes
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoDiagnosticInfo._primaryResidentDiagnosticInfo
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoDiagnosticInfo._version
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoIdsInfo._has
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoIdsInfo._idsIdentifierString
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoIdsInfo._idsState
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo._eventRouterServerInfo
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo._visibleAccessoriesInfos
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo._visibleIDSDevices
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo._wifiInfo
+ OBJC_IVAR_$_HMAccessoryInfoProtoWifiNetworkInfoEvent._has
+ OBJC_IVAR_$_HMAccessoryInfoProtoWifiNetworkInfoEvent._networkBSSID
+ OBJC_IVAR_$_HMAccessoryInfoProtoWifiNetworkInfoEvent._networkGatewayIPAddress
+ OBJC_IVAR_$_HMAccessoryInfoProtoWifiNetworkInfoEvent._networkGatewayMacAddress
+ OBJC_IVAR_$_HMAccessoryInfoProtoWifiNetworkInfoEvent._networkRSSI
+ OBJC_IVAR_$_HMProtoResidentCapabilities._supportsMatterTTU
+ OBJC_IVAR_$_HMRemoteEventRouterProtoConnectedClientInfo._connectedClientIdentifierString
+ OBJC_IVAR_$_HMRemoteEventRouterProtoServerDiagnosticInfo._connectedClients
+ OBJC_IVAR_$_HMRemoteEventRouterProtoServerDiagnosticInfo._connectionState
+ OBJC_IVAR_$_HMRemoteEventRouterProtoServerDiagnosticInfo._has
+ OBJC_IVAR_$_HMRemoteEventRouterProtoServerDiagnosticInfo._lastConnected
+ OBJC_IVAR_$_HMRemoteEventRouterProtoServerDiagnosticInfo._mode
+ OBJC_IVAR_$_HMRemoteEventRouterProtoServerDiagnosticInfo._version
+ _CoreAnalyticsLibraryCore.frameworkLibrary.35568
+ _HHMHomeManagerDiagnosticInfoAccessoryUUIDMessageKey
+ _HHMHomeManagerDiagnosticInfoDataKey
+ _HHMHomeManagerDiagnosticInfoFetchOptionsMessageKey
+ _HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfoReadFrom
+ _HMAccessoryDiagnosticInfoProtoCloudInfoReadFrom
+ _HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfoReadFrom
+ _HMAccessoryDiagnosticInfoProtoDiagnosticInfoReadFrom
+ _HMAccessoryDiagnosticInfoProtoIdsInfoReadFrom
+ _HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfoReadFrom
+ _HMAccessoryDiagnosticInfoRequestMessage
+ _HMAccessorySetupManagerPerformAccessorySetupTimeout
+ _HMDeviceSetupConfiguringStateKey
+ _HMHomeManagerDeviceSetupConfiguringStateRequestMessageKey
+ _HMHomeManagerFetchAccessoryDiagnosticInfoMessage
+ _HMHomeManagerFetchCurrentDeviceDiagnosticInfoMessage
+ _HMHomeManagerSetAppDataRequestKey
+ _HMMultiuserSettingsFetchRequestMessage
+ _HMRemoteEventRouterProtoConnectedClientInfoReadFrom
+ _HMRemoteEventRouterProtoServerDiagnosticInfoReadFrom
+ _HMWidgetManagerMessageKeyActionSetUUID
+ _HMWidgetManagerMessageKeyActionSets
+ _HMWidgetManagerMessageKeyActionSetsDidExecuteFail
+ _HMWidgetManagerMessageKeyActionSetsIsOn
+ _HMWidgetManagerMessageKeyCharacteristicUUID
+ _HMWidgetManagerMessageKeyCharacteristicValue
+ _HMWidgetManagerMessageKeyRequestType
+ _HMWidgetManagerMessageKeyRequests
+ _HMWidgetManagerMessageNameFetchStateForActionSets
+ _HMWidgetManagerMessageNameMonitorActionSetsForWidget
+ _HMWidgetManagerMessageNamePerformRequests
+ _IDSFoundationLibraryCore.39158
+ _IDSFoundationLibraryCore.frameworkLibrary.39160
+ _OBJC_CLASS_$_HMAccessoryDiagnosticInfo
+ _OBJC_CLASS_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo
+ _OBJC_CLASS_$_HMAccessoryDiagnosticInfoProtoCloudInfo
+ _OBJC_CLASS_$_HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo
+ _OBJC_CLASS_$_HMAccessoryDiagnosticInfoProtoDiagnosticInfo
+ _OBJC_CLASS_$_HMAccessoryDiagnosticInfoProtoIdsInfo
+ _OBJC_CLASS_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo
+ _OBJC_CLASS_$_HMExecuteTurnOffRequest
+ _OBJC_CLASS_$_HMFWifiNetworkAssociation
+ _OBJC_CLASS_$_HMRemoteEventRouterProtoConnectedClientInfo
+ _OBJC_CLASS_$_HMRemoteEventRouterProtoServerDiagnosticInfo
+ _OBJC_CLASS_$_HMWidgetManagerFetchStateForActionSetsResponse
+ _OBJC_CLASS_$_HMWidgetManagerMonitorActionSetsResponse
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._cdpStatusGood
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._cloudkitAccountStatusGood
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._connectedClientsDescription
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._currentAccessoryUUID
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._currrentAccessoryMediaRouteId
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._firstCloudImportDone
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._idsIdentifier
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._idsStatusGood
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._isEventRouterServerConnected
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._isPrimaryResident
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._isRunningHH2
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._manufacturer
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._model
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._numHomes
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._serialNumber
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._serverLastConnected
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._softwareVersion
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._version
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._wifiInfo
+ _OBJC_IVAR_$_HMHomeManager._privacySettingsProvider
+ _OBJC_IVAR_$_HMWidgetManagerFetchStateForActionSetsResponse._didExecutionFailByActionSetUniqueIdentifier
+ _OBJC_IVAR_$_HMWidgetManagerFetchStateForActionSetsResponse._isOnByActionSetUniqueIdentifier
+ _OBJC_IVAR_$_HMWidgetManagerMonitorActionSetsResponse._didExecutionFailByActionSetUniqueIdentifier
+ _OBJC_IVAR_$_HMWidgetManagerMonitorActionSetsResponse._isOnByActionSetUniqueIdentifier
+ _OBJC_METACLASS_$_HMAccessoryDiagnosticInfo
+ _OBJC_METACLASS_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo
+ _OBJC_METACLASS_$_HMAccessoryDiagnosticInfoProtoCloudInfo
+ _OBJC_METACLASS_$_HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo
+ _OBJC_METACLASS_$_HMAccessoryDiagnosticInfoProtoDiagnosticInfo
+ _OBJC_METACLASS_$_HMAccessoryDiagnosticInfoProtoIdsInfo
+ _OBJC_METACLASS_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo
+ _OBJC_METACLASS_$_HMExecuteTurnOffRequest
+ _OBJC_METACLASS_$_HMRemoteEventRouterProtoConnectedClientInfo
+ _OBJC_METACLASS_$_HMRemoteEventRouterProtoServerDiagnosticInfo
+ _OBJC_METACLASS_$_HMWidgetManagerFetchStateForActionSetsResponse
+ _OBJC_METACLASS_$_HMWidgetManagerMonitorActionSetsResponse
+ _UIKitLibrary.39393
+ _UIKitLibraryCore.39387
+ _UIKitLibraryCore.frameworkLibrary.39402
+ __OBJC_$_CATEGORY_HMFWiFiNetworkInfo_$_WifiInfoSerialization
+ __OBJC_$_CATEGORY_HMFWifiNetworkAssociation_$_WifiInfoSerialization
+ __OBJC_$_CLASS_METHODS_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo
+ __OBJC_$_CLASS_METHODS_HMExecuteTurnOffRequest
+ __OBJC_$_CLASS_METHODS_HMFWiFiNetworkInfo(WifiInfoSerialization)
+ __OBJC_$_CLASS_METHODS_HMRemoteEventRouterProtoServerDiagnosticInfo
+ __OBJC_$_INSTANCE_METHODS_HMAccessoryDiagnosticInfo
+ __OBJC_$_INSTANCE_METHODS_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo
+ __OBJC_$_INSTANCE_METHODS_HMAccessoryDiagnosticInfoProtoCloudInfo
+ __OBJC_$_INSTANCE_METHODS_HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo
+ __OBJC_$_INSTANCE_METHODS_HMAccessoryDiagnosticInfoProtoDiagnosticInfo
+ __OBJC_$_INSTANCE_METHODS_HMAccessoryDiagnosticInfoProtoIdsInfo
+ __OBJC_$_INSTANCE_METHODS_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo
+ __OBJC_$_INSTANCE_METHODS_HMFWifiNetworkAssociation(WifiInfoSerialization)
+ __OBJC_$_INSTANCE_METHODS_HMRemoteEventRouterProtoConnectedClientInfo
+ __OBJC_$_INSTANCE_METHODS_HMRemoteEventRouterProtoServerDiagnosticInfo
+ __OBJC_$_INSTANCE_METHODS_HMWidgetManagerFetchStateForActionSetsResponse
+ __OBJC_$_INSTANCE_METHODS_HMWidgetManagerMonitorActionSetsResponse
+ __OBJC_$_INSTANCE_VARIABLES_HMAccessoryDiagnosticInfo
+ __OBJC_$_INSTANCE_VARIABLES_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo
+ __OBJC_$_INSTANCE_VARIABLES_HMAccessoryDiagnosticInfoProtoCloudInfo
+ __OBJC_$_INSTANCE_VARIABLES_HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo
+ __OBJC_$_INSTANCE_VARIABLES_HMAccessoryDiagnosticInfoProtoDiagnosticInfo
+ __OBJC_$_INSTANCE_VARIABLES_HMAccessoryDiagnosticInfoProtoIdsInfo
+ __OBJC_$_INSTANCE_VARIABLES_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo
+ __OBJC_$_INSTANCE_VARIABLES_HMRemoteEventRouterProtoConnectedClientInfo
+ __OBJC_$_INSTANCE_VARIABLES_HMRemoteEventRouterProtoServerDiagnosticInfo
+ __OBJC_$_INSTANCE_VARIABLES_HMWidgetManagerFetchStateForActionSetsResponse
+ __OBJC_$_INSTANCE_VARIABLES_HMWidgetManagerMonitorActionSetsResponse
+ __OBJC_$_PROP_LIST_HMAccessoryDiagnosticInfo
+ __OBJC_$_PROP_LIST_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo
+ __OBJC_$_PROP_LIST_HMAccessoryDiagnosticInfoProtoCloudInfo
+ __OBJC_$_PROP_LIST_HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo
+ __OBJC_$_PROP_LIST_HMAccessoryDiagnosticInfoProtoDiagnosticInfo
+ __OBJC_$_PROP_LIST_HMAccessoryDiagnosticInfoProtoIdsInfo
+ __OBJC_$_PROP_LIST_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo
+ __OBJC_$_PROP_LIST_HMApplicationData.11105
+ __OBJC_$_PROP_LIST_HMRemoteEventRouterProtoConnectedClientInfo
+ __OBJC_$_PROP_LIST_HMRemoteEventRouterProtoServerDiagnosticInfo
+ __OBJC_$_PROP_LIST_HMResidentCapabilities.196
+ __OBJC_$_PROP_LIST_HMWidgetManagerFetchStateForActionSetsResponse
+ __OBJC_$_PROP_LIST_HMWidgetManagerMonitorActionSetsResponse
+ __OBJC_$_PROP_LIST__HMPrivacySettingsProvider.51
+ __OBJC_CLASS_PROTOCOLS_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo
+ __OBJC_CLASS_PROTOCOLS_$_HMAccessoryDiagnosticInfoProtoCloudInfo
+ __OBJC_CLASS_PROTOCOLS_$_HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo
+ __OBJC_CLASS_PROTOCOLS_$_HMAccessoryDiagnosticInfoProtoDiagnosticInfo
+ __OBJC_CLASS_PROTOCOLS_$_HMAccessoryDiagnosticInfoProtoIdsInfo
+ __OBJC_CLASS_PROTOCOLS_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo
+ __OBJC_CLASS_PROTOCOLS_$_HMRemoteEventRouterProtoConnectedClientInfo
+ __OBJC_CLASS_PROTOCOLS_$_HMRemoteEventRouterProtoServerDiagnosticInfo
+ __OBJC_CLASS_RO_$_HMAccessoryDiagnosticInfo
+ __OBJC_CLASS_RO_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo
+ __OBJC_CLASS_RO_$_HMAccessoryDiagnosticInfoProtoCloudInfo
+ __OBJC_CLASS_RO_$_HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo
+ __OBJC_CLASS_RO_$_HMAccessoryDiagnosticInfoProtoDiagnosticInfo
+ __OBJC_CLASS_RO_$_HMAccessoryDiagnosticInfoProtoIdsInfo
+ __OBJC_CLASS_RO_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo
+ __OBJC_CLASS_RO_$_HMExecuteTurnOffRequest
+ __OBJC_CLASS_RO_$_HMRemoteEventRouterProtoConnectedClientInfo
+ __OBJC_CLASS_RO_$_HMRemoteEventRouterProtoServerDiagnosticInfo
+ __OBJC_CLASS_RO_$_HMWidgetManagerFetchStateForActionSetsResponse
+ __OBJC_CLASS_RO_$_HMWidgetManagerMonitorActionSetsResponse
+ __OBJC_METACLASS_RO_$_HMAccessoryDiagnosticInfo
+ __OBJC_METACLASS_RO_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo
+ __OBJC_METACLASS_RO_$_HMAccessoryDiagnosticInfoProtoCloudInfo
+ __OBJC_METACLASS_RO_$_HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo
+ __OBJC_METACLASS_RO_$_HMAccessoryDiagnosticInfoProtoDiagnosticInfo
+ __OBJC_METACLASS_RO_$_HMAccessoryDiagnosticInfoProtoIdsInfo
+ __OBJC_METACLASS_RO_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo
+ __OBJC_METACLASS_RO_$_HMExecuteTurnOffRequest
+ __OBJC_METACLASS_RO_$_HMRemoteEventRouterProtoConnectedClientInfo
+ __OBJC_METACLASS_RO_$_HMRemoteEventRouterProtoServerDiagnosticInfo
+ __OBJC_METACLASS_RO_$_HMWidgetManagerFetchStateForActionSetsResponse
+ __OBJC_METACLASS_RO_$_HMWidgetManagerMonitorActionSetsResponse
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.723
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.725
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.726
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.729
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.733
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.735
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.728
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.731
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.734
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.736
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.732
+ ___136-[HMHomeManager readCountersForGroup:homeUUIDString:accessoryUUIDString:counter:statistics:datePartition:ephemeralContainer:completion:]_block_invoke
+ ___136-[HMHomeManager readCountersForGroup:homeUUIDString:accessoryUUIDString:counter:statistics:datePartition:ephemeralContainer:completion:]_block_invoke_2
+ ___152-[HMHomeManager initWithUUID:configuration:context:xpcEventRouterClient:lastEventStore:timerFactory:darwinNotificationProvider:privacySettingsProvider:]_block_invoke
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.299
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.302
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.304
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.307
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.310
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.313
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.316
+ ___29-[HMUser mergeFromNewObject:]_block_invoke_2.300
+ ___29-[HMUser mergeFromNewObject:]_block_invoke_2.303
+ ___29-[HMUser mergeFromNewObject:]_block_invoke_2.305
+ ___29-[HMUser mergeFromNewObject:]_block_invoke_2.308
+ ___29-[HMUser mergeFromNewObject:]_block_invoke_2.311
+ ___29-[HMUser mergeFromNewObject:]_block_invoke_2.314
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1088
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1089
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1091
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1095
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1093
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1096
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.1094
+ ___30-[HMAccessory _mergeServices:]_block_invoke.909
+ ___30-[HMAccessory _mergeServices:]_block_invoke.911
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1064
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1066
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1068
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1069
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1071
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1074
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1076
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1077
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1078
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1079
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1080
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1081
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1083
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1085
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1086
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.913
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.914
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.918
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.921
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.924
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.927
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.930
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.933
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.936
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.938
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.943
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.947
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1065
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1067
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1072
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1075
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1084
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.915
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.919
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.922
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.925
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.928
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.931
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.934
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.937
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.939
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.944
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.948
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.940
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.945
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.950
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.951
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.952
+ ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.483
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.738
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.740
+ ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke.148
+ ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke.152
+ ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke.156
+ ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke_2.149
+ ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke_2.153
+ ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke_2.157
+ ___44-[HMHomeManager saveCountersWithCompletion:]_block_invoke
+ ___44-[HMHomeManager saveCountersWithCompletion:]_block_invoke_2
+ ___44-[HMUser _mergeWithNewAccessoryInvitations:]_block_invoke.296
+ ___45-[HMAccessory _handleCharacteristicsUpdated:]_block_invoke.1107
+ ___45-[HMResidentDevice handleRuntimeStateUpdate:]_block_invoke.158
+ ___45-[HMResidentDevice handleRuntimeStateUpdate:]_block_invoke.159
+ ___45-[HMResidentDevice handleRuntimeStateUpdate:]_block_invoke.160
+ ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.647
+ ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1108
+ ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1109
+ ___50-[HMHomeManager addEphemeralContainer:completion:]_block_invoke
+ ___50-[HMHomeManager addEphemeralContainer:completion:]_block_invoke_2
+ ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.707
+ ___53-[HMHomeManager deleteEphemeralContainer:completion:]_block_invoke
+ ___53-[HMHomeManager deleteEphemeralContainer:completion:]_block_invoke_2
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.576
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.577
+ ___54-[HMHomeManager startupEphemeralContainer:completion:]_block_invoke
+ ___54-[HMHomeManager startupEphemeralContainer:completion:]_block_invoke_2
+ ___54-[HMWidgetManager fetchStateForActionSets:completion:]_block_invoke
+ ___54-[HMWidgetManager fetchStateForActionSets:completion:]_block_invoke.122
+ ___54-[HMWidgetManager fetchStateForActionSets:completion:]_block_invoke.123
+ ___54-[HMWidgetManager fetchStateForActionSets:completion:]_block_invoke.124
+ ___54-[HMWidgetManager fetchStateForActionSets:completion:]_block_invoke.126
+ ___54-[HMWidgetManager performRequests:forKind:completion:]_block_invoke
+ ___54-[HMWidgetManager performRequests:forKind:completion:]_block_invoke.108
+ ___55-[HMHomeManager listEphemeralContainersWithCompletion:]_block_invoke
+ ___55-[HMHomeManager listEphemeralContainersWithCompletion:]_block_invoke_2
+ ___57-[HMHomeManager deactivateEphemeralContainer:completion:]_block_invoke
+ ___57-[HMHomeManager deactivateEphemeralContainer:completion:]_block_invoke_2
+ ___58-[HMHomeManager __resolveAccountHandle:completionHandler:]_block_invoke.634
+ ___58-[HMHomeManager fetchDiagnosticInfoWithCompletionHandler:]_block_invoke
+ ___59-[HMWidgetManager fetchStateForCharacteristics:completion:]_block_invoke.94
+ ___59-[HMWidgetManager fetchStateForCharacteristics:completion:]_block_invoke.95
+ ___59-[HMWidgetManager fetchStateForCharacteristics:completion:]_block_invoke.96
+ ___59-[HMWidgetManager fetchStateForCharacteristics:completion:]_block_invoke.98
+ ___61-[HMAccessory _notifyClientsOfSymptomsHandlerAddedOrRemoved:]_block_invoke.1123
+ ___61-[HMHomeManager __removeAccountWithHandle:completionHandler:]_block_invoke.636
+ ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.843
+ ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.845
+ ___63-[HMHomeManager deleteCountersBeforeDate:afterDate:completion:]_block_invoke
+ ___63-[HMHomeManager deleteCountersBeforeDate:afterDate:completion:]_block_invoke_2
+ ___65-[HMHomeManager __removeAccountWithIdentifier:completionHandler:]_block_invoke.635
+ ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.665
+ ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.669
+ ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.671
+ ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.673
+ ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke_2.674
+ ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.792
+ ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.644
+ ___74-[HMHomeManager fetchAppleMediaAccesoryDiagnosticInfo:options:completion:]_block_invoke
+ ___86-[HMWidgetManager monitorAndFetchStateForActionSets:widgetIdentifier:kind:completion:]_block_invoke
+ ___86-[HMWidgetManager monitorAndFetchStateForActionSets:widgetIdentifier:kind:completion:]_block_invoke.115
+ ___86-[HMWidgetManager monitorAndFetchStateForActionSets:widgetIdentifier:kind:completion:]_block_invoke.116
+ ___86-[HMWidgetManager monitorAndFetchStateForActionSets:widgetIdentifier:kind:completion:]_block_invoke.117
+ ___86-[HMWidgetManager monitorAndFetchStateForActionSets:widgetIdentifier:kind:completion:]_block_invoke.119
+ ___91-[HMWidgetManager monitorAndFetchStateForCharacteristics:widgetIdentifier:kind:completion:]_block_invoke.84
+ ___91-[HMWidgetManager monitorAndFetchStateForCharacteristics:widgetIdentifier:kind:completion:]_block_invoke.85
+ ___91-[HMWidgetManager monitorAndFetchStateForCharacteristics:widgetIdentifier:kind:completion:]_block_invoke.87
+ ___91-[HMWidgetManager monitorAndFetchStateForCharacteristics:widgetIdentifier:kind:completion:]_block_invoke.88
+ ___91-[HMWidgetManager monitorAndFetchStateForCharacteristics:widgetIdentifier:kind:completion:]_block_invoke.90
+ ___93-[HMHomeManager _pingDeviceWithUUID:monitor:secure:restrictToLocalNetwork:completionHandler:]_block_invoke.637
+ ___Block_byref_object_copy_.14048
+ ___Block_byref_object_copy_.14357
+ ___Block_byref_object_copy_.21027
+ ___Block_byref_object_copy_.23116
+ ___Block_byref_object_copy_.27137
+ ___Block_byref_object_copy_.28823
+ ___Block_byref_object_copy_.35455
+ ___Block_byref_object_copy_.38312
+ ___Block_byref_object_copy_.39388
+ ___Block_byref_object_copy_.59774
+ ___Block_byref_object_dispose_.14049
+ ___Block_byref_object_dispose_.14358
+ ___Block_byref_object_dispose_.21028
+ ___Block_byref_object_dispose_.23117
+ ___Block_byref_object_dispose_.27138
+ ___Block_byref_object_dispose_.28824
+ ___Block_byref_object_dispose_.35456
+ ___Block_byref_object_dispose_.38313
+ ___Block_byref_object_dispose_.39389
+ ___Block_byref_object_dispose_.59775
+ ___CoreAnalyticsLibraryCore_block_invoke.35569
+ ___IDSFoundationLibraryCore_block_invoke.39161
+ ___UIKitLibraryCore_block_invoke.39403
+ _____HMHomeManagerRegisterForNotifications_block_invoke.1350
+ _____processNextArchivedData_block_invoke.307
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_32_e29_"NSUUID"16?0"HMActionSet"8l
+ ___block_literal_global.101.35576
+ ___block_literal_global.10180
+ ___block_literal_global.11166
+ ___block_literal_global.114
+ ___block_literal_global.12.45313
+ ___block_literal_global.121.48239
+ ___block_literal_global.12126
+ ___block_literal_global.12273
+ ___block_literal_global.12727
+ ___block_literal_global.128
+ ___block_literal_global.12919
+ ___block_literal_global.13483
+ ___block_literal_global.13814
+ ___block_literal_global.14132
+ ___block_literal_global.14721
+ ___block_literal_global.15782
+ ___block_literal_global.16309
+ ___block_literal_global.16500
+ ___block_literal_global.16632
+ ___block_literal_global.16794
+ ___block_literal_global.17.17425
+ ___block_literal_global.17432
+ ___block_literal_global.18099
+ ___block_literal_global.18502
+ ___block_literal_global.19.13799
+ ___block_literal_global.19053
+ ___block_literal_global.192.22341
+ ___block_literal_global.19377
+ ___block_literal_global.1962
+ ___block_literal_global.20410
+ ___block_literal_global.21065
+ ___block_literal_global.21338
+ ___block_literal_global.21823
+ ___block_literal_global.22042
+ ___block_literal_global.22347
+ ___block_literal_global.22481
+ ___block_literal_global.22727
+ ___block_literal_global.22978
+ ___block_literal_global.23139
+ ___block_literal_global.23231
+ ___block_literal_global.25723
+ ___block_literal_global.25858
+ ___block_literal_global.26331
+ ___block_literal_global.27020
+ ___block_literal_global.27266
+ ___block_literal_global.27605
+ ___block_literal_global.27817
+ ___block_literal_global.28095
+ ___block_literal_global.28169
+ ___block_literal_global.29021
+ ___block_literal_global.29346
+ ___block_literal_global.29617
+ ___block_literal_global.30.17415
+ ___block_literal_global.30.7383
+ ___block_literal_global.30446
+ ___block_literal_global.30984
+ ___block_literal_global.32158
+ ___block_literal_global.32968
+ ___block_literal_global.33.59117
+ ___block_literal_global.33199
+ ___block_literal_global.33422
+ ___block_literal_global.3397
+ ___block_literal_global.34372
+ ___block_literal_global.35563
+ ___block_literal_global.35813
+ ___block_literal_global.3592
+ ___block_literal_global.36149
+ ___block_literal_global.36781
+ ___block_literal_global.3683
+ ___block_literal_global.37583
+ ___block_literal_global.37708
+ ___block_literal_global.37983
+ ___block_literal_global.39223
+ ___block_literal_global.39319
+ ___block_literal_global.40028
+ ___block_literal_global.40217
+ ___block_literal_global.40849
+ ___block_literal_global.41474
+ ___block_literal_global.41890
+ ___block_literal_global.42210
+ ___block_literal_global.42883
+ ___block_literal_global.43767
+ ___block_literal_global.45035
+ ___block_literal_global.45325
+ ___block_literal_global.45591
+ ___block_literal_global.45785
+ ___block_literal_global.46012
+ ___block_literal_global.46704
+ ___block_literal_global.468
+ ___block_literal_global.46824
+ ___block_literal_global.473
+ ___block_literal_global.47556
+ ___block_literal_global.47993
+ ___block_literal_global.48326
+ ___block_literal_global.4852
+ ___block_literal_global.49239
+ ___block_literal_global.51788
+ ___block_literal_global.5243
+ ___block_literal_global.52491
+ ___block_literal_global.5379
+ ___block_literal_global.53927
+ ___block_literal_global.54567
+ ___block_literal_global.55097
+ ___block_literal_global.55408
+ ___block_literal_global.55905
+ ___block_literal_global.56077
+ ___block_literal_global.56462
+ ___block_literal_global.56706
+ ___block_literal_global.58355
+ ___block_literal_global.58521
+ ___block_literal_global.5873
+ ___block_literal_global.58858
+ ___block_literal_global.59123
+ ___block_literal_global.59483
+ ___block_literal_global.59772
+ ___block_literal_global.60065
+ ___block_literal_global.6345
+ ___block_literal_global.6614
+ ___block_literal_global.686
+ ___block_literal_global.688
+ ___block_literal_global.7049
+ ___block_literal_global.7166
+ ___block_literal_global.73.21316
+ ___block_literal_global.7401
+ ___block_literal_global.75.35766
+ ___block_literal_global.76.25490
+ ___block_literal_global.7852
+ ___block_literal_global.796
+ ___block_literal_global.8335
+ ___block_literal_global.85.59786
+ ___block_literal_global.8613
+ ___block_literal_global.8789
+ ___block_literal_global.9216
+ ___block_literal_global.93
+ ___block_literal_global.9470
+ ___getAnalyticsSendEventLazySymbolLoc_block_invoke.35566
+ ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.39398
+ ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.39392
+ __unnamed_array_storage.14065
+ __unnamed_array_storage.22254
+ __unnamed_array_storage.227.25637
+ __unnamed_array_storage.239.25636
+ __unnamed_array_storage.251.25640
+ __unnamed_array_storage.25713
+ __unnamed_array_storage.28682
+ __unnamed_array_storage.54043
+ __unnamed_array_storage.55533
+ __unnamed_array_storage.58974
+ _audit_stringCoreAnalytics.35572
+ _audit_stringIDSFoundation.39163
+ _audit_stringUIKit.39405
+ _getAnalyticsSendEventLazySymbolLoc.ptr.35565
+ _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.39397
+ _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.39391
+ _logCategory._hmf_once_t0.12272
+ _logCategory._hmf_once_t0.21337
+ _logCategory._hmf_once_t0.27816
+ _logCategory._hmf_once_t0.28168
+ _logCategory._hmf_once_t0.40027
+ _logCategory._hmf_once_t0.40216
+ _logCategory._hmf_once_t0.40848
+ _logCategory._hmf_once_t0.56705
+ _logCategory._hmf_once_t1.16631
+ _logCategory._hmf_once_t1.18501
+ _logCategory._hmf_once_t1.35789
+ _logCategory._hmf_once_t1.41473
+ _logCategory._hmf_once_t1.45312
+ _logCategory._hmf_once_t1.46823
+ _logCategory._hmf_once_t1.51787
+ _logCategory._hmf_once_t15.56461
+ _logCategory._hmf_once_t16.33198
+ _logCategory._hmf_once_t16.58520
+ _logCategory._hmf_once_t17.37575
+ _logCategory._hmf_once_t19.12945
+ _logCategory._hmf_once_t2.25857
+ _logCategory._hmf_once_t2.29345
+ _logCategory._hmf_once_t20.5378
+ _logCategory._hmf_once_t22.22726
+ _logCategory._hmf_once_t24.36143
+ _logCategory._hmf_once_t25.22977
+ _logCategory._hmf_once_t25.59482
+ _logCategory._hmf_once_t26.48074
+ _logCategory._hmf_once_t27.47555
+ _logCategory._hmf_once_t27.55407
+ _logCategory._hmf_once_t3.37707
+ _logCategory._hmf_once_t3.59116
+ _logCategory._hmf_once_t31.21064
+ _logCategory._hmf_once_t31.58354
+ _logCategory._hmf_once_t33.48351
+ _logCategory._hmf_once_t337
+ _logCategory._hmf_once_t34.14127
+ _logCategory._hmf_once_t34.18098
+ _logCategory._hmf_once_t35.34371
+ _logCategory._hmf_once_t4.5242
+ _logCategory._hmf_once_t50.37982
+ _logCategory._hmf_once_t57
+ _logCategory._hmf_once_t6.30445
+ _logCategory._hmf_once_t6.32967
+ _logCategory._hmf_once_t6.46703
+ _logCategory._hmf_once_t6.52490
+ _logCategory._hmf_once_t64.53926
+ _logCategory._hmf_once_t7.23230
+ _logCategory._hmf_once_t8.33421
+ _logCategory._hmf_once_t8.42882
+ _logCategory._hmf_once_t8.45803
+ _logCategory._hmf_once_t85
+ _logCategory._hmf_once_v1.12274
+ _logCategory._hmf_once_v1.21339
+ _logCategory._hmf_once_v1.27818
+ _logCategory._hmf_once_v1.28170
+ _logCategory._hmf_once_v1.40029
+ _logCategory._hmf_once_v1.40218
+ _logCategory._hmf_once_v1.40850
+ _logCategory._hmf_once_v1.56707
+ _logCategory._hmf_once_v16.56463
+ _logCategory._hmf_once_v17.33200
+ _logCategory._hmf_once_v17.58522
+ _logCategory._hmf_once_v18.37576
+ _logCategory._hmf_once_v2.16633
+ _logCategory._hmf_once_v2.18503
+ _logCategory._hmf_once_v2.35790
+ _logCategory._hmf_once_v2.41475
+ _logCategory._hmf_once_v2.45314
+ _logCategory._hmf_once_v2.46825
+ _logCategory._hmf_once_v2.51789
+ _logCategory._hmf_once_v20.12946
+ _logCategory._hmf_once_v21.5380
+ _logCategory._hmf_once_v23.22728
+ _logCategory._hmf_once_v25.36144
+ _logCategory._hmf_once_v26.22979
+ _logCategory._hmf_once_v26.59484
+ _logCategory._hmf_once_v27.48075
+ _logCategory._hmf_once_v28.47557
+ _logCategory._hmf_once_v28.55409
+ _logCategory._hmf_once_v3.25859
+ _logCategory._hmf_once_v3.29347
+ _logCategory._hmf_once_v32.21066
+ _logCategory._hmf_once_v32.58356
+ _logCategory._hmf_once_v338
+ _logCategory._hmf_once_v34.48352
+ _logCategory._hmf_once_v35.14128
+ _logCategory._hmf_once_v35.18100
+ _logCategory._hmf_once_v36.34373
+ _logCategory._hmf_once_v4.37709
+ _logCategory._hmf_once_v4.59118
+ _logCategory._hmf_once_v5.5244
+ _logCategory._hmf_once_v51.37984
+ _logCategory._hmf_once_v58
+ _logCategory._hmf_once_v65.53928
+ _logCategory._hmf_once_v7.30447
+ _logCategory._hmf_once_v7.32969
+ _logCategory._hmf_once_v7.46705
+ _logCategory._hmf_once_v7.52492
+ _logCategory._hmf_once_v8.23232
+ _logCategory._hmf_once_v86
+ _logCategory._hmf_once_v9.33423
+ _logCategory._hmf_once_v9.42884
+ _logCategory._hmf_once_v9.45804
+ _objc_msgSend$BSSID
+ _objc_msgSend$addConnectedClients:
+ _objc_msgSend$addVisibleAccessoriesInfo:
+ _objc_msgSend$addVisibleIDSDevices:
+ _objc_msgSend$appleMediaAccessoryDiagnosticInfo
+ _objc_msgSend$canWriteToCache
+ _objc_msgSend$cdpStatusGood
+ _objc_msgSend$clearConnectedClients
+ _objc_msgSend$clearVisibleAccessoriesInfos
+ _objc_msgSend$clearVisibleIDSDevices
+ _objc_msgSend$cloudInfo
+ _objc_msgSend$cloudState
+ _objc_msgSend$cloudkitAccountStatusGood
+ _objc_msgSend$connectedClientIdentifierString
+ _objc_msgSend$connectedClients
+ _objc_msgSend$connectedClientsAtIndex:
+ _objc_msgSend$connectedClientsCount
+ _objc_msgSend$connectedClientsDescription
+ _objc_msgSend$connectionState
+ _objc_msgSend$currentAccessoryInfo
+ _objc_msgSend$currentAccessoryUUID
+ _objc_msgSend$currrentAccessoryMediaRouteId
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$eventRouterServerInfo
+ _objc_msgSend$firstCloudImportComplete
+ _objc_msgSend$firstCloudImportDone
+ _objc_msgSend$gatewayIPAddress
+ _objc_msgSend$gatewayMACAddress
+ _objc_msgSend$hasAppleMediaAccessoryDiagnosticInfo
+ _objc_msgSend$hasLastConnected
+ _objc_msgSend$hasPrimaryResidentDiagnosticInfo
+ _objc_msgSend$hasSoftwareVersion
+ _objc_msgSend$hasWifiInfo
+ _objc_msgSend$homeHubVersion
+ _objc_msgSend$idsIdentifierString
+ _objc_msgSend$idsInfo
+ _objc_msgSend$idsState
+ _objc_msgSend$idsStatusGood
+ _objc_msgSend$initWithIsOnByActionSetsUniqueIdentifier:didExecutionFailByActionSetUniqueIdentifier:
+ _objc_msgSend$initWithMACAddress:SSID:BSSID:gatewayIPAddress:gatewayMACAddress:
+ _objc_msgSend$initWithSession:setupSession:
+ _objc_msgSend$initWithUUID:configuration:context:xpcEventRouterClient:lastEventStore:timerFactory:darwinNotificationProvider:privacySettingsProvider:
+ _objc_msgSend$isEventRouterServerConnected
+ _objc_msgSend$isPrimaryResident
+ _objc_msgSend$isRunningHH2
+ _objc_msgSend$lastConnected
+ _objc_msgSend$mediaRouteIdString
+ _objc_msgSend$modelIdentifier
+ _objc_msgSend$networkBSSID
+ _objc_msgSend$networkGatewayIPAddress
+ _objc_msgSend$networkGatewayMacAddress
+ _objc_msgSend$numHomes
+ _objc_msgSend$octagonState
+ _objc_msgSend$privacySettingsProvider
+ _objc_msgSend$requestHomeKitAccessWithQueue:completion:
+ _objc_msgSend$serverLastConnected
+ _objc_msgSend$setAppleMediaAccessoryDiagnosticInfo:
+ _objc_msgSend$setCloudInfo:
+ _objc_msgSend$setConnectedClientIdentifierString:
+ _objc_msgSend$setCurrentAccessoryInfo:
+ _objc_msgSend$setEventRouterServerInfo:
+ _objc_msgSend$setIdsIdentifierString:
+ _objc_msgSend$setIdsInfo:
+ _objc_msgSend$setMediaRouteIdString:
+ _objc_msgSend$setModelIdentifier:
+ _objc_msgSend$setNetworkBSSID:
+ _objc_msgSend$setNetworkGatewayIPAddress:
+ _objc_msgSend$setNetworkGatewayMacAddress:
+ _objc_msgSend$setPrimaryResidentDiagnosticInfo:
+ _objc_msgSend$setPublicPairingIdentity:
+ _objc_msgSend$setRegionInfo:
+ _objc_msgSend$setSupportsMatterTTU:
+ _objc_msgSend$setTimeout:
+ _objc_msgSend$setWifiInfo:
+ _objc_msgSend$supportsMatterTTU
+ _objc_msgSend$visibleAccessoriesInfoAtIndex:
+ _objc_msgSend$visibleAccessoriesInfosCount
+ _objc_msgSend$visibleIDSDevicesAtIndex:
+ _objc_msgSend$visibleIDSDevicesCount
+ _objc_msgSend$wifiInfo
+ _objc_msgSend$wifiNetworkInfoFromProto:
+ _sharedInstance.onceToken.37582
+ _sharedManager.onceToken.55550
+ _supportedValueClasses.onceToken.45590
+ _supportedValueClasses.onceToken.53889
+ _supportedValueClasses.supportedValueClasses.45592
+ _supportedValueClasses.supportedValueClasses.53890
+ _unconfigureQueue.onceToken.36148
+ _unconfigureQueue.unconfigureQueue.36150
- -[HMHomeManager initWithUUID:configuration:context:xpcEventRouterClient:lastEventStore:timerFactory:darwinNotificationProvider:]
- -[HMHomeManager initWithUUID:configuration:context:xpcEventRouterClient:timerFactory:darwinNotificationProvider:]
- -[HMWidgetManager performWriteRequests:forKind:completion:]
- -[_HMPrivacySettingsProvider requestAccessWithQueue:completion:]
- GCC_except_table10085
- GCC_except_table10086
- GCC_except_table10113
- GCC_except_table10115
- GCC_except_table10119
- GCC_except_table10120
- GCC_except_table10168
- GCC_except_table10194
- GCC_except_table10207
- GCC_except_table10231
- GCC_except_table10235
- GCC_except_table10276
- GCC_except_table10277
- GCC_except_table10278
- GCC_except_table10279
- GCC_except_table10280
- GCC_except_table10281
- GCC_except_table10282
- GCC_except_table10283
- GCC_except_table10284
- GCC_except_table10285
- GCC_except_table10286
- GCC_except_table10287
- GCC_except_table10288
- GCC_except_table10289
- GCC_except_table10290
- GCC_except_table10307
- GCC_except_table10334
- GCC_except_table10420
- GCC_except_table10421
- GCC_except_table10486
- GCC_except_table10488
- GCC_except_table10496
- GCC_except_table10502
- GCC_except_table10503
- GCC_except_table10509
- GCC_except_table10511
- GCC_except_table10516
- GCC_except_table10517
- GCC_except_table10518
- GCC_except_table10702
- GCC_except_table10703
- GCC_except_table1086
- GCC_except_table10882
- GCC_except_table10885
- GCC_except_table10890
- GCC_except_table10894
- GCC_except_table10900
- GCC_except_table10905
- GCC_except_table10907
- GCC_except_table10912
- GCC_except_table10913
- GCC_except_table10915
- GCC_except_table10998
- GCC_except_table11000
- GCC_except_table11019
- GCC_except_table11020
- GCC_except_table11021
- GCC_except_table11027
- GCC_except_table11041
- GCC_except_table11047
- GCC_except_table11050
- GCC_except_table11052
- GCC_except_table1108
- GCC_except_table11132
- GCC_except_table11134
- GCC_except_table11137
- GCC_except_table11145
- GCC_except_table11146
- GCC_except_table11151
- GCC_except_table11157
- GCC_except_table11159
- GCC_except_table11161
- GCC_except_table11163
- GCC_except_table11165
- GCC_except_table11167
- GCC_except_table11301
- GCC_except_table11356
- GCC_except_table11357
- GCC_except_table11358
- GCC_except_table11369
- GCC_except_table11394
- GCC_except_table11395
- GCC_except_table11449
- GCC_except_table11474
- GCC_except_table11609
- GCC_except_table11729
- GCC_except_table11730
- GCC_except_table11731
- GCC_except_table11778
- GCC_except_table11779
- GCC_except_table11781
- GCC_except_table11784
- GCC_except_table11786
- GCC_except_table11788
- GCC_except_table11820
- GCC_except_table1185
- GCC_except_table11863
- GCC_except_table11868
- GCC_except_table11871
- GCC_except_table1188
- GCC_except_table11931
- GCC_except_table12016
- GCC_except_table1202
- GCC_except_table12023
- GCC_except_table12077
- GCC_except_table12079
- GCC_except_table12088
- GCC_except_table12091
- GCC_except_table12111
- GCC_except_table12113
- GCC_except_table12114
- GCC_except_table1337
- GCC_except_table1406
- GCC_except_table1409
- GCC_except_table1478
- GCC_except_table1480
- GCC_except_table1554
- GCC_except_table1555
- GCC_except_table1603
- GCC_except_table1832
- GCC_except_table1835
- GCC_except_table1838
- GCC_except_table1843
- GCC_except_table1847
- GCC_except_table1856
- GCC_except_table1858
- GCC_except_table1861
- GCC_except_table1871
- GCC_except_table1873
- GCC_except_table1874
- GCC_except_table1879
- GCC_except_table1880
- GCC_except_table1882
- GCC_except_table2066
- GCC_except_table2068
- GCC_except_table2072
- GCC_except_table2074
- GCC_except_table2076
- GCC_except_table2078
- GCC_except_table2084
- GCC_except_table2307
- GCC_except_table2310
- GCC_except_table2324
- GCC_except_table2356
- GCC_except_table2369
- GCC_except_table2372
- GCC_except_table2373
- GCC_except_table2376
- GCC_except_table2399
- GCC_except_table2401
- GCC_except_table2405
- GCC_except_table2565
- GCC_except_table2583
- GCC_except_table2584
- GCC_except_table2640
- GCC_except_table2642
- GCC_except_table2645
- GCC_except_table2646
- GCC_except_table2670
- GCC_except_table2672
- GCC_except_table2682
- GCC_except_table2689
- GCC_except_table2690
- GCC_except_table2691
- GCC_except_table2693
- GCC_except_table2694
- GCC_except_table2695
- GCC_except_table2696
- GCC_except_table2697
- GCC_except_table2749
- GCC_except_table2773
- GCC_except_table2776
- GCC_except_table2779
- GCC_except_table2782
- GCC_except_table2785
- GCC_except_table2788
- GCC_except_table2791
- GCC_except_table2856
- GCC_except_table2857
- GCC_except_table2901
- GCC_except_table2908
- GCC_except_table2909
- GCC_except_table2910
- GCC_except_table2913
- GCC_except_table2914
- GCC_except_table2915
- GCC_except_table2917
- GCC_except_table2925
- GCC_except_table2933
- GCC_except_table2934
- GCC_except_table2952
- GCC_except_table2963
- GCC_except_table2966
- GCC_except_table2969
- GCC_except_table3008
- GCC_except_table3012
- GCC_except_table3016
- GCC_except_table3021
- GCC_except_table3029
- GCC_except_table3033
- GCC_except_table3044
- GCC_except_table3274
- GCC_except_table3280
- GCC_except_table3283
- GCC_except_table3287
- GCC_except_table3288
- GCC_except_table3291
- GCC_except_table3297
- GCC_except_table3300
- GCC_except_table3304
- GCC_except_table3328
- GCC_except_table3330
- GCC_except_table3332
- GCC_except_table3335
- GCC_except_table3338
- GCC_except_table3341
- GCC_except_table3423
- GCC_except_table3428
- GCC_except_table3440
- GCC_except_table3443
- GCC_except_table3445
- GCC_except_table3448
- GCC_except_table3455
- GCC_except_table3508
- GCC_except_table3574
- GCC_except_table3589
- GCC_except_table3592
- GCC_except_table3692
- GCC_except_table3693
- GCC_except_table3695
- GCC_except_table3700
- GCC_except_table3704
- GCC_except_table3707
- GCC_except_table3709
- GCC_except_table3717
- GCC_except_table3914
- GCC_except_table3917
- GCC_except_table3929
- GCC_except_table4001
- GCC_except_table4020
- GCC_except_table4107
- GCC_except_table4202
- GCC_except_table4207
- GCC_except_table4208
- GCC_except_table4216
- GCC_except_table4218
- GCC_except_table4243
- GCC_except_table4244
- GCC_except_table4245
- GCC_except_table4246
- GCC_except_table4306
- GCC_except_table4381
- GCC_except_table4383
- GCC_except_table4385
- GCC_except_table4427
- GCC_except_table4430
- GCC_except_table4431
- GCC_except_table4505
- GCC_except_table4591
- GCC_except_table4592
- GCC_except_table4598
- GCC_except_table4600
- GCC_except_table4629
- GCC_except_table4631
- GCC_except_table4650
- GCC_except_table4696
- GCC_except_table4745
- GCC_except_table4828
- GCC_except_table4848
- GCC_except_table4849
- GCC_except_table4850
- GCC_except_table4852
- GCC_except_table4855
- GCC_except_table4856
- GCC_except_table4858
- GCC_except_table5060
- GCC_except_table5066
- GCC_except_table5068
- GCC_except_table5078
- GCC_except_table5079
- GCC_except_table5326
- GCC_except_table5431
- GCC_except_table5437
- GCC_except_table5444
- GCC_except_table5449
- GCC_except_table5531
- GCC_except_table5533
- GCC_except_table5670
- GCC_except_table580
- GCC_except_table5827
- GCC_except_table5828
- GCC_except_table583
- GCC_except_table584
- GCC_except_table585
- GCC_except_table5853
- GCC_except_table5855
- GCC_except_table586
- GCC_except_table5861
- GCC_except_table5869
- GCC_except_table587
- GCC_except_table5884
- GCC_except_table589
- GCC_except_table5891
- GCC_except_table5894
- GCC_except_table590
- GCC_except_table5908
- GCC_except_table5913
- GCC_except_table5949
- GCC_except_table5966
- GCC_except_table597
- GCC_except_table5978
- GCC_except_table598
- GCC_except_table5983
- GCC_except_table5997
- GCC_except_table6002
- GCC_except_table6010
- GCC_except_table6012
- GCC_except_table6015
- GCC_except_table6020
- GCC_except_table6027
- GCC_except_table6032
- GCC_except_table6064
- GCC_except_table6070
- GCC_except_table6095
- GCC_except_table6100
- GCC_except_table6104
- GCC_except_table6133
- GCC_except_table6137
- GCC_except_table6139
- GCC_except_table6278
- GCC_except_table6284
- GCC_except_table6363
- GCC_except_table6381
- GCC_except_table6386
- GCC_except_table6394
- GCC_except_table6437
- GCC_except_table6439
- GCC_except_table6441
- GCC_except_table6453
- GCC_except_table6464
- GCC_except_table6490
- GCC_except_table6499
- GCC_except_table6506
- GCC_except_table6509
- GCC_except_table6512
- GCC_except_table6515
- GCC_except_table6526
- GCC_except_table6536
- GCC_except_table6560
- GCC_except_table6563
- GCC_except_table6566
- GCC_except_table6569
- GCC_except_table6572
- GCC_except_table6575
- GCC_except_table6578
- GCC_except_table6581
- GCC_except_table6584
- GCC_except_table6588
- GCC_except_table6600
- GCC_except_table6601
- GCC_except_table6609
- GCC_except_table6626
- GCC_except_table6628
- GCC_except_table6667
- GCC_except_table6669
- GCC_except_table6690
- GCC_except_table6694
- GCC_except_table6769
- GCC_except_table6971
- GCC_except_table7065
- GCC_except_table7147
- GCC_except_table7158
- GCC_except_table7234
- GCC_except_table7252
- GCC_except_table7258
- GCC_except_table7260
- GCC_except_table7262
- GCC_except_table7263
- GCC_except_table7394
- GCC_except_table7397
- GCC_except_table7411
- GCC_except_table7413
- GCC_except_table7416
- GCC_except_table7447
- GCC_except_table7449
- GCC_except_table7467
- GCC_except_table7475
- GCC_except_table7477
- GCC_except_table7479
- GCC_except_table7486
- GCC_except_table7492
- GCC_except_table7494
- GCC_except_table7496
- GCC_except_table7497
- GCC_except_table7507
- GCC_except_table7508
- GCC_except_table7509
- GCC_except_table7520
- GCC_except_table7522
- GCC_except_table7524
- GCC_except_table7565
- GCC_except_table7567
- GCC_except_table7575
- GCC_except_table7577
- GCC_except_table7579
- GCC_except_table7581
- GCC_except_table7583
- GCC_except_table7589
- GCC_except_table7593
- GCC_except_table7605
- GCC_except_table7607
- GCC_except_table7609
- GCC_except_table7611
- GCC_except_table7630
- GCC_except_table7769
- GCC_except_table7770
- GCC_except_table7771
- GCC_except_table7773
- GCC_except_table7775
- GCC_except_table7776
- GCC_except_table7777
- GCC_except_table7813
- GCC_except_table7816
- GCC_except_table7817
- GCC_except_table7820
- GCC_except_table7823
- GCC_except_table7824
- GCC_except_table7868
- GCC_except_table7869
- GCC_except_table7870
- GCC_except_table7877
- GCC_except_table7878
- GCC_except_table7880
- GCC_except_table7942
- GCC_except_table7943
- GCC_except_table7944
- GCC_except_table798
- GCC_except_table7981
- GCC_except_table802
- GCC_except_table809
- GCC_except_table8124
- GCC_except_table8125
- GCC_except_table8126
- GCC_except_table8185
- GCC_except_table8206
- GCC_except_table8277
- GCC_except_table8283
- GCC_except_table8285
- GCC_except_table8287
- GCC_except_table8289
- GCC_except_table8297
- GCC_except_table8346
- GCC_except_table8347
- GCC_except_table8374
- GCC_except_table8402
- GCC_except_table841
- GCC_except_table8560
- GCC_except_table8619
- GCC_except_table8624
- GCC_except_table8629
- GCC_except_table8633
- GCC_except_table8646
- GCC_except_table8649
- GCC_except_table8652
- GCC_except_table8654
- GCC_except_table8684
- GCC_except_table8704
- GCC_except_table8705
- GCC_except_table8706
- GCC_except_table8743
- GCC_except_table8744
- GCC_except_table8748
- GCC_except_table8750
- GCC_except_table8752
- GCC_except_table8811
- GCC_except_table8838
- GCC_except_table8841
- GCC_except_table8843
- GCC_except_table8845
- GCC_except_table8847
- GCC_except_table8855
- GCC_except_table8857
- GCC_except_table8863
- GCC_except_table8867
- GCC_except_table8870
- GCC_except_table8878
- GCC_except_table8882
- GCC_except_table8888
- GCC_except_table8894
- GCC_except_table8897
- GCC_except_table8905
- GCC_except_table8906
- GCC_except_table8919
- GCC_except_table8933
- GCC_except_table909
- GCC_except_table911
- GCC_except_table914
- GCC_except_table9157
- GCC_except_table916
- GCC_except_table918
- GCC_except_table9206
- GCC_except_table9207
- GCC_except_table9209
- GCC_except_table9213
- GCC_except_table9217
- GCC_except_table922
- GCC_except_table9273
- GCC_except_table9276
- GCC_except_table9277
- GCC_except_table9556
- GCC_except_table9595
- GCC_except_table9608
- GCC_except_table971
- GCC_except_table9931
- GCC_except_table9933
- GCC_except_table9935
- GCC_except_table9936
- GCC_except_table9966
- GCC_except_table9968
- GCC_except_table9970
- GCC_except_table9976
- GCC_except_table9977
- GCC_except_table9978
- _CoreAnalyticsLibraryCore.frameworkLibrary.34868
- _HMWidgetManagerMessageNamePerformWriteRequests
- _IDSFoundationLibraryCore.38455
- _IDSFoundationLibraryCore.frameworkLibrary.38457
- _UIKitLibrary.38689
- _UIKitLibraryCore.38683
- _UIKitLibraryCore.frameworkLibrary.38698
- __OBJC_$_PROP_LIST_HMApplicationData.10985
- __OBJC_$_PROP_LIST_HMResidentCapabilities.194
- __OBJC_$_PROP_LIST__HMPrivacySettingsProvider.50
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.674
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.676
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.677
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.680
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.684
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.686
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.679
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.682
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.685
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.687
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.683
- ___128-[HMHomeManager initWithUUID:configuration:context:xpcEventRouterClient:lastEventStore:timerFactory:darwinNotificationProvider:]_block_invoke
- ___29-[HMUser mergeFromNewObject:]_block_invoke.303
- ___29-[HMUser mergeFromNewObject:]_block_invoke.306
- ___29-[HMUser mergeFromNewObject:]_block_invoke.308
- ___29-[HMUser mergeFromNewObject:]_block_invoke.311
- ___29-[HMUser mergeFromNewObject:]_block_invoke.314
- ___29-[HMUser mergeFromNewObject:]_block_invoke.317
- ___29-[HMUser mergeFromNewObject:]_block_invoke.320
- ___29-[HMUser mergeFromNewObject:]_block_invoke_2.304
- ___29-[HMUser mergeFromNewObject:]_block_invoke_2.307
- ___29-[HMUser mergeFromNewObject:]_block_invoke_2.309
- ___29-[HMUser mergeFromNewObject:]_block_invoke_2.312
- ___29-[HMUser mergeFromNewObject:]_block_invoke_2.315
- ___29-[HMUser mergeFromNewObject:]_block_invoke_2.318
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.992
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.993
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.995
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.999
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1000
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.997
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.998
- ___30-[HMAccessory _mergeServices:]_block_invoke.813
- ___30-[HMAccessory _mergeServices:]_block_invoke.815
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.817
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.818
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.822
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.825
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.828
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.831
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.834
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.837
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.840
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.842
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.847
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.851
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.968
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.970
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.972
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.973
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.975
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.978
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.980
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.981
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.982
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.983
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.984
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.985
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.987
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.989
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.990
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.819
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.823
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.826
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.829
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.832
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.835
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.838
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.841
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.843
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.848
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.852
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.969
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.971
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.976
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.979
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.988
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.844
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.849
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.854
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.855
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.856
- ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.458
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.689
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.691
- ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke.145
- ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke.149
- ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke.153
- ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke_2.146
- ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke_2.150
- ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke_2.154
- ___44-[HMUser _mergeWithNewAccessoryInvitations:]_block_invoke.300
- ___45-[HMAccessory _handleCharacteristicsUpdated:]_block_invoke.1011
- ___45-[HMResidentDevice handleRuntimeStateUpdate:]_block_invoke.155
- ___45-[HMResidentDevice handleRuntimeStateUpdate:]_block_invoke.156
- ___45-[HMResidentDevice handleRuntimeStateUpdate:]_block_invoke.157
- ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.598
- ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1012
- ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1013
- ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.658
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.551
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.552
- ___58-[HMHomeManager __resolveAccountHandle:completionHandler:]_block_invoke.585
- ___59-[HMWidgetManager fetchStateForCharacteristics:completion:]_block_invoke.64
- ___59-[HMWidgetManager fetchStateForCharacteristics:completion:]_block_invoke.65
- ___59-[HMWidgetManager fetchStateForCharacteristics:completion:]_block_invoke.66
- ___59-[HMWidgetManager fetchStateForCharacteristics:completion:]_block_invoke.68
- ___59-[HMWidgetManager performWriteRequests:forKind:completion:]_block_invoke
- ___59-[HMWidgetManager performWriteRequests:forKind:completion:]_block_invoke.73
- ___61-[HMAccessory _notifyClientsOfSymptomsHandlerAddedOrRemoved:]_block_invoke.1027
- ___61-[HMHomeManager __removeAccountWithHandle:completionHandler:]_block_invoke.587
- ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.745
- ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.747
- ___65-[HMHomeManager __removeAccountWithIdentifier:completionHandler:]_block_invoke.586
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.616
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.620
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.622
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.624
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke_2.625
- ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.742
- ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.595
- ___91-[HMWidgetManager monitorAndFetchStateForCharacteristics:widgetIdentifier:kind:completion:]_block_invoke.54
- ___91-[HMWidgetManager monitorAndFetchStateForCharacteristics:widgetIdentifier:kind:completion:]_block_invoke.55
- ___91-[HMWidgetManager monitorAndFetchStateForCharacteristics:widgetIdentifier:kind:completion:]_block_invoke.57
- ___91-[HMWidgetManager monitorAndFetchStateForCharacteristics:widgetIdentifier:kind:completion:]_block_invoke.58
- ___91-[HMWidgetManager monitorAndFetchStateForCharacteristics:widgetIdentifier:kind:completion:]_block_invoke.60
- ___93-[HMHomeManager _pingDeviceWithUUID:monitor:secure:restrictToLocalNetwork:completionHandler:]_block_invoke.588
- ___Block_byref_object_copy_.13931
- ___Block_byref_object_copy_.14238
- ___Block_byref_object_copy_.20780
- ___Block_byref_object_copy_.22865
- ___Block_byref_object_copy_.26874
- ___Block_byref_object_copy_.28541
- ___Block_byref_object_copy_.34755
- ___Block_byref_object_copy_.37611
- ___Block_byref_object_copy_.38684
- ___Block_byref_object_copy_.58735
- ___Block_byref_object_dispose_.13932
- ___Block_byref_object_dispose_.14239
- ___Block_byref_object_dispose_.20781
- ___Block_byref_object_dispose_.22866
- ___Block_byref_object_dispose_.26875
- ___Block_byref_object_dispose_.28542
- ___Block_byref_object_dispose_.34756
- ___Block_byref_object_dispose_.37612
- ___Block_byref_object_dispose_.38685
- ___Block_byref_object_dispose_.58736
- ___CoreAnalyticsLibraryCore_block_invoke.34869
- ___IDSFoundationLibraryCore_block_invoke.38458
- ___UIKitLibraryCore_block_invoke.38699
- _____HMHomeManagerRegisterForNotifications_block_invoke.1286
- _____processNextArchivedData_block_invoke.304
- ___block_literal_global.10060
- ___block_literal_global.101.34876
- ___block_literal_global.11046
- ___block_literal_global.12.44514
- ___block_literal_global.12007
- ___block_literal_global.12154
- ___block_literal_global.12607
- ___block_literal_global.12799
- ___block_literal_global.13366
- ___block_literal_global.13696
- ___block_literal_global.14015
- ___block_literal_global.14600
- ___block_literal_global.15660
- ___block_literal_global.16187
- ___block_literal_global.16378
- ___block_literal_global.16510
- ___block_literal_global.16672
- ___block_literal_global.17.17304
- ___block_literal_global.17311
- ___block_literal_global.17931
- ___block_literal_global.18333
- ___block_literal_global.1847
- ___block_literal_global.18884
- ___block_literal_global.19.13681
- ___block_literal_global.192.22091
- ___block_literal_global.19208
- ___block_literal_global.20163
- ___block_literal_global.20818
- ___block_literal_global.21091
- ___block_literal_global.21576
- ___block_literal_global.21795
- ___block_literal_global.22097
- ___block_literal_global.22231
- ___block_literal_global.22477
- ___block_literal_global.22728
- ___block_literal_global.22888
- ___block_literal_global.22980
- ___block_literal_global.25463
- ___block_literal_global.25597
- ___block_literal_global.26068
- ___block_literal_global.26757
- ___block_literal_global.27003
- ___block_literal_global.27342
- ___block_literal_global.27555
- ___block_literal_global.27833
- ___block_literal_global.27907
- ___block_literal_global.28703
- ___block_literal_global.28863
- ___block_literal_global.29134
- ___block_literal_global.29963
- ___block_literal_global.30.17294
- ___block_literal_global.30.7263
- ___block_literal_global.30501
- ___block_literal_global.31662
- ___block_literal_global.32417
- ___block_literal_global.32648
- ___block_literal_global.3280
- ___block_literal_global.32871
- ___block_literal_global.33.58078
- ___block_literal_global.33810
- ___block_literal_global.3475
- ___block_literal_global.34863
- ___block_literal_global.35113
- ___block_literal_global.35449
- ___block_literal_global.3566
- ___block_literal_global.36081
- ___block_literal_global.36883
- ___block_literal_global.37008
- ___block_literal_global.37282
- ___block_literal_global.38521
- ___block_literal_global.38615
- ___block_literal_global.39324
- ___block_literal_global.39513
- ___block_literal_global.40146
- ___block_literal_global.40771
- ___block_literal_global.41188
- ___block_literal_global.41507
- ___block_literal_global.42085
- ___block_literal_global.42968
- ___block_literal_global.44236
- ___block_literal_global.443
- ___block_literal_global.44526
- ___block_literal_global.44792
- ___block_literal_global.448
- ___block_literal_global.44986
- ___block_literal_global.45213
- ___block_literal_global.45905
- ___block_literal_global.46025
- ___block_literal_global.46757
- ___block_literal_global.47194
- ___block_literal_global.4734
- ___block_literal_global.47448
- ___block_literal_global.48369
- ___block_literal_global.50733
- ___block_literal_global.5125
- ___block_literal_global.51436
- ___block_literal_global.5261
- ___block_literal_global.52868
- ___block_literal_global.53531
- ___block_literal_global.54062
- ___block_literal_global.54374
- ___block_literal_global.54871
- ___block_literal_global.55043
- ___block_literal_global.55429
- ___block_literal_global.55673
- ___block_literal_global.57319
- ___block_literal_global.57486
- ___block_literal_global.5761
- ___block_literal_global.57819
- ___block_literal_global.58084
- ___block_literal_global.58444
- ___block_literal_global.58733
- ___block_literal_global.59026
- ___block_literal_global.6232
- ___block_literal_global.63
- ___block_literal_global.637
- ___block_literal_global.639
- ___block_literal_global.6494
- ___block_literal_global.6929
- ___block_literal_global.7046
- ___block_literal_global.7281
- ___block_literal_global.73.21069
- ___block_literal_global.746
- ___block_literal_global.75.35066
- ___block_literal_global.75.47480
- ___block_literal_global.76.25227
- ___block_literal_global.7732
- ___block_literal_global.8213
- ___block_literal_global.8492
- ___block_literal_global.85.58747
- ___block_literal_global.8668
- ___block_literal_global.9095
- ___block_literal_global.9350
- ___getAnalyticsSendEventLazySymbolLoc_block_invoke.34866
- ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.38694
- ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.38688
- __unnamed_array_storage.13948
- __unnamed_array_storage.22007
- __unnamed_array_storage.227.25374
- __unnamed_array_storage.239.25373
- __unnamed_array_storage.251.25377
- __unnamed_array_storage.25453
- __unnamed_array_storage.28366
- __unnamed_array_storage.52987
- __unnamed_array_storage.54499
- __unnamed_array_storage.57935
- _audit_stringCoreAnalytics.34872
- _audit_stringIDSFoundation.38460
- _audit_stringUIKit.38701
- _getAnalyticsSendEventLazySymbolLoc.ptr.34865
- _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.38693
- _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.38687
- _logCategory._hmf_once_t0.12153
- _logCategory._hmf_once_t0.21090
- _logCategory._hmf_once_t0.27554
- _logCategory._hmf_once_t0.27906
- _logCategory._hmf_once_t0.39323
- _logCategory._hmf_once_t0.39512
- _logCategory._hmf_once_t0.40145
- _logCategory._hmf_once_t0.55672
- _logCategory._hmf_once_t1.16509
- _logCategory._hmf_once_t1.18332
- _logCategory._hmf_once_t1.35089
- _logCategory._hmf_once_t1.40770
- _logCategory._hmf_once_t1.44513
- _logCategory._hmf_once_t1.46024
- _logCategory._hmf_once_t1.50732
- _logCategory._hmf_once_t15.55428
- _logCategory._hmf_once_t16.32647
- _logCategory._hmf_once_t16.57485
- _logCategory._hmf_once_t17.36875
- _logCategory._hmf_once_t17.47479
- _logCategory._hmf_once_t19.12825
- _logCategory._hmf_once_t2.25596
- _logCategory._hmf_once_t2.28862
- _logCategory._hmf_once_t20.5260
- _logCategory._hmf_once_t22.22476
- _logCategory._hmf_once_t24.35443
- _logCategory._hmf_once_t25.22727
- _logCategory._hmf_once_t25.58443
- _logCategory._hmf_once_t26.47275
- _logCategory._hmf_once_t27.46756
- _logCategory._hmf_once_t27.54373
- _logCategory._hmf_once_t3.37007
- _logCategory._hmf_once_t3.58077
- _logCategory._hmf_once_t31.20817
- _logCategory._hmf_once_t31.57318
- _logCategory._hmf_once_t324
- _logCategory._hmf_once_t34.14010
- _logCategory._hmf_once_t34.17930
- _logCategory._hmf_once_t35.33809
- _logCategory._hmf_once_t4.5124
- _logCategory._hmf_once_t50.37281
- _logCategory._hmf_once_t56
- _logCategory._hmf_once_t6.29962
- _logCategory._hmf_once_t6.32416
- _logCategory._hmf_once_t6.45904
- _logCategory._hmf_once_t6.51435
- _logCategory._hmf_once_t64.52867
- _logCategory._hmf_once_t7.22979
- _logCategory._hmf_once_t8.32870
- _logCategory._hmf_once_t8.42084
- _logCategory._hmf_once_t8.45004
- _logCategory._hmf_once_t87
- _logCategory._hmf_once_v1.12155
- _logCategory._hmf_once_v1.21092
- _logCategory._hmf_once_v1.27556
- _logCategory._hmf_once_v1.27908
- _logCategory._hmf_once_v1.39325
- _logCategory._hmf_once_v1.39514
- _logCategory._hmf_once_v1.40147
- _logCategory._hmf_once_v1.55674
- _logCategory._hmf_once_v16.55430
- _logCategory._hmf_once_v17.32649
- _logCategory._hmf_once_v17.57487
- _logCategory._hmf_once_v18.36876
- _logCategory._hmf_once_v18.47481
- _logCategory._hmf_once_v2.16511
- _logCategory._hmf_once_v2.18334
- _logCategory._hmf_once_v2.35090
- _logCategory._hmf_once_v2.40772
- _logCategory._hmf_once_v2.44515
- _logCategory._hmf_once_v2.46026
- _logCategory._hmf_once_v2.50734
- _logCategory._hmf_once_v20.12826
- _logCategory._hmf_once_v21.5262
- _logCategory._hmf_once_v23.22478
- _logCategory._hmf_once_v25.35444
- _logCategory._hmf_once_v26.22729
- _logCategory._hmf_once_v26.58445
- _logCategory._hmf_once_v27.47276
- _logCategory._hmf_once_v28.46758
- _logCategory._hmf_once_v28.54375
- _logCategory._hmf_once_v3.25598
- _logCategory._hmf_once_v3.28864
- _logCategory._hmf_once_v32.20819
- _logCategory._hmf_once_v32.57320
- _logCategory._hmf_once_v325
- _logCategory._hmf_once_v35.14011
- _logCategory._hmf_once_v35.17932
- _logCategory._hmf_once_v36.33811
- _logCategory._hmf_once_v4.37009
- _logCategory._hmf_once_v4.58079
- _logCategory._hmf_once_v5.5126
- _logCategory._hmf_once_v51.37283
- _logCategory._hmf_once_v57
- _logCategory._hmf_once_v65.52869
- _logCategory._hmf_once_v7.29964
- _logCategory._hmf_once_v7.32418
- _logCategory._hmf_once_v7.45906
- _logCategory._hmf_once_v7.51437
- _logCategory._hmf_once_v8.22981
- _logCategory._hmf_once_v88
- _logCategory._hmf_once_v9.32872
- _logCategory._hmf_once_v9.42086
- _logCategory._hmf_once_v9.45005
- _objc_msgSend$cachedAuthorizationStatus
- _objc_msgSend$initWithUUID:configuration:context:xpcEventRouterClient:lastEventStore:timerFactory:darwinNotificationProvider:
- _sharedInstance.onceToken.36882
- _sharedManager.onceToken.54516
- _supportedValueClasses.onceToken.44791
- _supportedValueClasses.onceToken.52832
- _supportedValueClasses.supportedValueClasses.44793
- _supportedValueClasses.supportedValueClasses.52833
- _unconfigureQueue.onceToken.35448
- _unconfigureQueue.unconfigureQueue.35450
CStrings:
+ "\x12\x13\x11S1/\x01G"
+ "\x1b"
+ "%{public}@%{public}@Action set isOn statuses are unexpectedly missing in the response"
+ "%{public}@%{public}@Failed to fetch action sets with error: %@"
+ "%{public}@%{public}@Failed to monitor action sets with error: %@"
+ "%{public}@%{public}@Failed to perform requests with error: %@"
+ "%{public}@%{public}@No requests to process"
+ "%{public}@%{public}@Request is not a supported type: %@"
+ "%{public}@%{public}@Successfully fetched action sets"
+ "%{public}@%{public}@Successfully monitored action sets"
+ "%{public}@%{public}@Successfully performed requests"
+ "%{public}@%{public}@[%@] Fetching action sets: %@"
+ "%{public}@%{public}@[%@] Monitoring action sets for widget (%@, %@): %@"
+ "%{public}@%{public}@[%@] Performing requests: %@"
+ "%{public}@Cannot refresh before date %fs in the past: %@"
+ "%{public}@Could not determine accessory UUID"
+ "%{public}@Missing asset properties from asset info: %@"
+ "%{public}@Not starting new download in state: %@"
+ "%{public}@The bundle parameter is required"
+ ")\x11"
+ "-[HMHomeManager addEphemeralContainer:completion:]"
+ "-[HMHomeManager deactivateEphemeralContainer:completion:]"
+ "-[HMHomeManager deleteCountersBeforeDate:afterDate:completion:]"
+ "-[HMHomeManager deleteEphemeralContainer:completion:]"
+ "-[HMHomeManager fetchAppleMediaAccesoryDiagnosticInfo:options:completion:]"
+ "-[HMHomeManager fetchDiagnosticInfoWithCompletionHandler:]"
+ "-[HMHomeManager listEphemeralContainersWithCompletion:]"
+ "-[HMHomeManager readCountersForGroup:homeUUIDString:accessoryUUIDString:counter:statistics:datePartition:ephemeralContainer:completion:]"
+ "-[HMHomeManager saveCountersWithCompletion:]"
+ "-[HMHomeManager startupEphemeralContainer:completion:]"
+ "<%@ [cloudkit=> accountStatus: %d, cdp: %d, firstImport: %d>] [ids=> status: %d identifier: %@ ] [device=> %@ - %@ - %@, s/w: %@] hh2: %d, numHomes: %lu, uuid: %@, mediaRouteID: %@, isPrimary: %d, wifi: %@, [eventrouter=> connected: %d date: %@, clients: %@] >"
+ "@\"<_HMPrivacySettingsProvider>\""
+ "@\"HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo\""
+ "@\"HMAccessoryDiagnosticInfoProtoCloudInfo\""
+ "@\"HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo\""
+ "@\"HMAccessoryDiagnosticInfoProtoIdsInfo\""
+ "@\"HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo\""
+ "@\"HMAccessoryInfoProtoPublicPairingIdentity\""
+ "@\"HMAccessoryInfoProtoWifiNetworkInfoEvent\""
+ "@\"HMRemoteEventRouterProtoServerDiagnosticInfo\""
+ "@\"NSUUID\"16@?0@\"HMActionSet\"8"
+ "@28@0:8@16{_HMResidentCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}24"
+ "@80@0:8@16@24@32@40@48@?56@64@72"
+ "BSSID"
+ "Connected"
+ "Disconnected"
+ "HMAccessoryDiagnosticInfo"
+ "HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo"
+ "HMAccessoryDiagnosticInfoProtoCloudInfo"
+ "HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo"
+ "HMAccessoryDiagnosticInfoProtoDiagnosticInfo"
+ "HMAccessoryDiagnosticInfoProtoIdsInfo"
+ "HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo"
+ "HMAccessoryDiagnosticInfoRequestMessage"
+ "HMDeviceSetupConfiguringStateKey"
+ "HMExecuteTurnOffRequest"
+ "HMHM.accessoryDiagnosticInfo"
+ "HMHM.currentDeviceDiagnosticInfo"
+ "HMHM.dscs"
+ "HMRemoteEventRouterProtoConnectedClientInfo"
+ "HMRemoteEventRouterProtoServerDiagnosticInfo"
+ "HMWM.actionSetUUID"
+ "HMWM.actionSets"
+ "HMWM.actionSetsDidExecuteFail"
+ "HMWM.actionSetsIsOn"
+ "HMWM.characteristicUUID"
+ "HMWM.characteristicValue"
+ "HMWM.fetchStateForActionSets"
+ "HMWM.monitorActionSets"
+ "HMWM.performRequests"
+ "HMWM.requestType"
+ "HMWM.requests"
+ "HMWidgetManagerFetchStateForActionSetsResponse"
+ "HMWidgetManagerMonitorActionSetsResponse"
+ "Primary"
+ "Resident"
+ "StringAsCloudState:"
+ "StringAsConnectionState:"
+ "StringAsIdsState:"
+ "StringAsMode:"
+ "StringAsOctagonState:"
+ "T@\"<_HMPrivacySettingsProvider>\",R,N,V_privacySettingsProvider"
+ "T@\"HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo\",&,N,V_appleMediaAccessoryDiagnosticInfo"
+ "T@\"HMAccessoryDiagnosticInfoProtoCloudInfo\",&,N,V_cloudInfo"
+ "T@\"HMAccessoryDiagnosticInfoProtoCurrentAccessoryInfo\",&,N,V_currentAccessoryInfo"
+ "T@\"HMAccessoryDiagnosticInfoProtoIdsInfo\",&,N,V_idsInfo"
+ "T@\"HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo\",&,N,V_primaryResidentDiagnosticInfo"
+ "T@\"HMAccessoryInfoProtoPublicPairingIdentity\",&,N,V_publicPairingIdentity"
+ "T@\"HMAccessoryInfoProtoWifiNetworkInfoEvent\",&,N,V_wifiInfo"
+ "T@\"HMFSoftwareVersion\",R,C,N,V_softwareVersion"
+ "T@\"HMFWiFiNetworkInfo\",R,N,V_wifiInfo"
+ "T@\"HMRemoteEventRouterProtoServerDiagnosticInfo\",&,N,V_eventRouterServerInfo"
+ "T@\"NSDate\",R,N,V_serverLastConnected"
+ "T@\"NSDictionary\",R,C,V_didExecutionFailByActionSetUniqueIdentifier"
+ "T@\"NSDictionary\",R,C,V_isOnByActionSetUniqueIdentifier"
+ "T@\"NSMutableArray\",&,N,V_connectedClients"
+ "T@\"NSMutableArray\",&,N,V_visibleAccessoriesInfos"
+ "T@\"NSMutableArray\",&,N,V_visibleIDSDevices"
+ "T@\"NSString\",&,N,V_connectedClientIdentifierString"
+ "T@\"NSString\",&,N,V_idsIdentifierString"
+ "T@\"NSString\",&,N,V_manufacturer"
+ "T@\"NSString\",&,N,V_mediaRouteIdString"
+ "T@\"NSString\",&,N,V_modelIdentifier"
+ "T@\"NSString\",&,N,V_networkBSSID"
+ "T@\"NSString\",&,N,V_networkGatewayIPAddress"
+ "T@\"NSString\",&,N,V_networkGatewayMacAddress"
+ "T@\"NSString\",&,N,V_regionInfo"
+ "T@\"NSString\",&,N,V_serialNumber"
+ "T@\"NSString\",&,N,V_softwareVersion"
+ "T@\"NSString\",R,C,N,V_manufacturer"
+ "T@\"NSString\",R,C,N,V_model"
+ "T@\"NSString\",R,C,N,V_serialNumber"
+ "T@\"NSString\",R,N,V_connectedClientsDescription"
+ "T@\"NSString\",R,N,V_currrentAccessoryMediaRouteId"
+ "T@\"NSString\",R,N,V_idsIdentifier"
+ "T@\"NSUUID\",R,N,V_currentAccessoryUUID"
+ "TB,N,V_firstCloudImportComplete"
+ "TB,N,V_supportsMatterTTU"
+ "TB,R,N,V_cdpStatusGood"
+ "TB,R,N,V_cloudkitAccountStatusGood"
+ "TB,R,N,V_firstCloudImportDone"
+ "TB,R,N,V_idsStatusGood"
+ "TB,R,N,V_isEventRouterServerConnected"
+ "TB,R,N,V_isPrimaryResident"
+ "TB,R,N,V_isRunningHH2"
+ "TQ,N,V_version"
+ "TQ,R,N,V_numHomes"
+ "TQ,R,N,V_version"
+ "Td,N,V_generationTime"
+ "Td,N,V_lastConnected"
+ "Ti,N,V_cloudState"
+ "Ti,N,V_connectionState"
+ "Ti,N,V_homeHubVersion"
+ "Ti,N,V_idsState"
+ "Ti,N,V_mode"
+ "Ti,N,V_networkRSSI"
+ "Ti,N,V_numHomes"
+ "Ti,N,V_octagonState"
+ "T{_HMResidentCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},R,N,V_capabilities"
+ "WifiInfoSerialization"
+ "WriteOnly"
+ "_appleMediaAccessoryDiagnosticInfo"
+ "_cdpStatusGood"
+ "_cloudInfo"
+ "_cloudState"
+ "_cloudkitAccountStatusGood"
+ "_connectedClientIdentifierString"
+ "_connectedClients"
+ "_connectedClientsDescription"
+ "_connectionState"
+ "_currentAccessoryInfo"
+ "_currentAccessoryUUID"
+ "_currrentAccessoryMediaRouteId"
+ "_didExecutionFailByActionSetUniqueIdentifier"
+ "_eventRouterServerInfo"
+ "_firstCloudImportComplete"
+ "_firstCloudImportDone"
+ "_generationTime"
+ "_homeHubVersion"
+ "_idsIdentifierString"
+ "_idsInfo"
+ "_idsState"
+ "_idsStatusGood"
+ "_isEventRouterServerConnected"
+ "_isOnByActionSetUniqueIdentifier"
+ "_isPrimaryResident"
+ "_isRunningHH2"
+ "_lastConnected"
+ "_mediaRouteIdString"
+ "_mode"
+ "_modelIdentifier"
+ "_networkBSSID"
+ "_networkGatewayIPAddress"
+ "_networkGatewayMacAddress"
+ "_networkRSSI"
+ "_numHomes"
+ "_octagonState"
+ "_primaryResidentDiagnosticInfo"
+ "_privacySettingsProvider"
+ "_publicPairingIdentity"
+ "_regionInfo"
+ "_serverLastConnected"
+ "_supportsMatterTTU"
+ "_visibleAccessoriesInfos"
+ "_visibleIDSDevices"
+ "_wifiInfo"
+ "accessoryDiagnosticData"
+ "addConnectedClients:"
+ "addEphemeralContainer"
+ "addEphemeralContainer:completion:"
+ "addVisibleAccessoriesInfo:"
+ "addVisibleIDSDevices:"
+ "afterDate"
+ "appleMediaAccessoryDiagnosticInfo"
+ "beforeDate"
+ "canWriteToCache"
+ "cdpStatusGood"
+ "clearConnectedClients"
+ "clearVisibleAccessoriesInfos"
+ "clearVisibleIDSDevices"
+ "cloudInfo"
+ "cloudState"
+ "cloudStateAsString:"
+ "cloudkitAccountStatusGood"
+ "connectedClientIdentifierString"
+ "connectedClients"
+ "connectedClientsAtIndex:"
+ "connectedClientsCount"
+ "connectedClientsDescription"
+ "connectedClientsType"
+ "connectionState"
+ "connectionStateAsString:"
+ "counter"
+ "currentAccessoryInfo"
+ "currentAccessoryUUID"
+ "currrentAccessoryMediaRouteId"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "deactivateEphemeralContainer"
+ "deactivateEphemeralContainer:completion:"
+ "deleteCounters"
+ "deleteCountersBeforeDate:afterDate:completion:"
+ "deleteEphemeralContainer"
+ "deleteEphemeralContainer:completion:"
+ "didExecutionFailByActionSetUniqueIdentifier"
+ "ephemeralContainer"
+ "eventRouterServerInfo"
+ "fetchAppleMediaAccesoryDiagnosticInfo:options:completion:"
+ "fetchDiagnosticInfoWithCompletionHandler:"
+ "fetchEventCounters"
+ "fetchStateForActionSets:completion:"
+ "firstCloudImportComplete"
+ "firstCloudImportDone"
+ "gatewayIPAddress"
+ "gatewayMACAddress"
+ "generationTime"
+ "hasAppleMediaAccessoryDiagnosticInfo"
+ "hasCloudInfo"
+ "hasCloudState"
+ "hasConnectedClientIdentifierString"
+ "hasConnectionState"
+ "hasCurrentAccessoryInfo"
+ "hasEventRouterServerInfo"
+ "hasFirstCloudImportComplete"
+ "hasGenerationTime"
+ "hasHomeHubVersion"
+ "hasIdsIdentifierString"
+ "hasIdsInfo"
+ "hasIdsState"
+ "hasLastConnected"
+ "hasManufacturer"
+ "hasMediaRouteIdString"
+ "hasMode"
+ "hasModelIdentifier"
+ "hasNetworkBSSID"
+ "hasNetworkGatewayIPAddress"
+ "hasNetworkGatewayMacAddress"
+ "hasNetworkRSSI"
+ "hasNumHomes"
+ "hasOctagonState"
+ "hasPrimaryResidentDiagnosticInfo"
+ "hasPublicPairingIdentity"
+ "hasRegionInfo"
+ "hasSerialNumber"
+ "hasSoftwareVersion"
+ "hasSupportsMatterTTU"
+ "hasWifiInfo"
+ "homeHubVersion"
+ "idsIdentifierString"
+ "idsInfo"
+ "idsState"
+ "idsStateAsString:"
+ "idsStatusGood"
+ "initWithIsOnByActionSetsUniqueIdentifier:didExecutionFailByActionSetUniqueIdentifier:"
+ "initWithMACAddress:SSID:BSSID:gatewayIPAddress:gatewayMACAddress:"
+ "initWithSession:setupSession:"
+ "initWithUUID:configuration:context:xpcEventRouterClient:lastEventStore:timerFactory:darwinNotificationProvider:privacySettingsProvider:"
+ "isEventRouterServerConnected"
+ "isOnByActionSetUniqueIdentifier"
+ "isPrimaryResident"
+ "isRunningHH2"
+ "lastConnected"
+ "listEphemeralContainers"
+ "listEphemeralContainersWithCompletion:"
+ "logEventDailySchedulerRequestStatus"
+ "logEventDailySchedulerRunRegisteredBlocks"
+ "matterTTU"
+ "mediaRouteIdString"
+ "modeAsString:"
+ "modelIdentifier"
+ "monitorAndFetchStateForActionSets:widgetIdentifier:kind:completion:"
+ "networkBSSID"
+ "networkGatewayIPAddress"
+ "networkGatewayMacAddress"
+ "networkRSSI"
+ "numHomes"
+ "octagonState"
+ "octagonStateAsString:"
+ "partition"
+ "performRequests:forKind:completion:"
+ "presentTTRDialog"
+ "primaryResidentDiagnosticInfo"
+ "privacySettingsProvider"
+ "readCounters"
+ "readCountersForGroup:homeUUIDString:accessoryUUIDString:counter:statistics:datePartition:ephemeralContainer:completion:"
+ "regionInfo"
+ "requestHomeKitAccessWithQueue:completion:"
+ "requestMicrophoneAccessWithQueue:completion:"
+ "resetEventCounters"
+ "resetLastTTRTime"
+ "saveCounters"
+ "saveCountersWithCompletion:"
+ "serverLastConnected"
+ "setAppleMediaAccessoryDiagnosticInfo:"
+ "setCloudInfo:"
+ "setCloudState:"
+ "setConnectedClientIdentifierString:"
+ "setConnectedClients:"
+ "setConnectionState:"
+ "setCurrentAccessoryInfo:"
+ "setEventRouterServerInfo:"
+ "setFirstCloudImportComplete:"
+ "setGenerationTime:"
+ "setHasCloudState:"
+ "setHasConnectionState:"
+ "setHasFirstCloudImportComplete:"
+ "setHasGenerationTime:"
+ "setHasHomeHubVersion:"
+ "setHasIdsState:"
+ "setHasLastConnected:"
+ "setHasMode:"
+ "setHasNetworkRSSI:"
+ "setHasNumHomes:"
+ "setHasOctagonState:"
+ "setHasSupportsMatterTTU:"
+ "setHomeHubVersion:"
+ "setIdsIdentifierString:"
+ "setIdsInfo:"
+ "setIdsState:"
+ "setLastConnected:"
+ "setMediaRouteIdString:"
+ "setMode:"
+ "setModelIdentifier:"
+ "setNetworkBSSID:"
+ "setNetworkGatewayIPAddress:"
+ "setNetworkGatewayMacAddress:"
+ "setNetworkRSSI:"
+ "setNumHomes:"
+ "setOctagonState:"
+ "setPrimaryResidentDiagnosticInfo:"
+ "setPublicPairingIdentity:"
+ "setRegionInfo:"
+ "setSupportsMatterTTU:"
+ "setTimeout:"
+ "setVisibleAccessoriesInfos:"
+ "setVisibleIDSDevices:"
+ "setWifiInfo:"
+ "startupEphemeralContainer"
+ "startupEphemeralContainer:completion:"
+ "statistics"
+ "supportsMatterTTU"
+ "v80@0:8@16@24@32@40@48@56@64@?72"
+ "visibleAccessoriesInfo"
+ "visibleAccessoriesInfoAtIndex:"
+ "visibleAccessoriesInfoType"
+ "visibleAccessoriesInfos"
+ "visibleAccessoriesInfosCount"
+ "visibleIDSDevices"
+ "visibleIDSDevicesAtIndex:"
+ "visibleIDSDevicesCount"
+ "visibleIDSDevicesType"
+ "wifiInfo"
+ "wifiNetworkInfoFromProto:"
+ "{?=\"cloudState\"b1\"octagonState\"b1\"firstCloudImportComplete\"b1}"
+ "{?=\"generationTime\"b1\"version\"b1\"homeHubVersion\"b1\"numHomes\"b1}"
+ "{?=\"generationTime\"b1}"
+ "{?=\"idsState\"b1}"
+ "{?=\"lastConnected\"b1\"version\"b1\"connectionState\"b1\"mode\"b1}"
+ "{?=\"networkRSSI\"b1}"
+ "{?=\"supports40e39e789f11ed6f1738\"b1\"supports5348b248a25f84b0c83e\"b1\"supportsAccessCodes\"b1\"supportsAnnounce\"b1\"supportsCHIP\"b1\"supportsCameraActivityZones\"b1\"supportsCameraPackageDetection\"b1\"supportsCameraRecording\"b1\"supportsCameraRecordingReachabilityNotifications\"b1\"supportsCameraSignificantEventNotifications\"b1\"supportsCustomMediaApplicationDestination\"b1\"supportsFaceClassification\"b1\"supportsFirmwareUpdate\"b1\"supportsHomeHub\"b1\"supportsLockNotificationContext\"b1\"supportsMatterTTU\"b1\"supportsMediaActions\"b1\"supportsNaturalLighting\"b1\"supportsResidentFirmwareUpdate\"b1\"supportsResidentFirstAccessoryCommunication\"b1\"supportsRouterManagement\"b1\"supportsShortcutActions\"b1\"supportsSiriEndpointSetup\"b1\"supportsThreadBorderRouter\"b1\"supportsThreadNetworkCredentialSharing\"b1\"supportsUnifiedMediaNotifications\"b1\"supportsWakeOnLAN\"b1\"supportsWalletKey\"b1}"
+ "{_HMResidentCapabilitiesStruct=\"supportsCameraRecording\"b1\"supportsRouterManagement\"b1\"supportsShortcutActions\"b1\"supportsMediaActions\"b1\"supportsCameraSignificantEventNotifications\"b1\"supportsFirmwareUpdate\"b1\"supportsResidentFirmwareUpdate\"b1\"supportsCameraActivityZones\"b1\"supportsFaceClassification\"b1\"supportsNaturalLighting\"b1\"supportsCameraRecordingReachabilityNotifications\"b1\"supportsAnnounce\"b1\"supportsWakeOnLAN\"b1\"supportsLockNotificationContext\"b1\"supportsWalletKey\"b1\"supportsCameraPackageDetection\"b1\"supportsAccessCodes\"b1\"supportsCHIP\"b1\"supportsThreadBorderRouter\"b1\"supportsSiriEndpointSetup\"b1\"supportsCustomMediaApplicationDestination\"b1\"supportsUnifiedMediaNotifications\"b1\"supportsHomeHub\"b1\"supportsResidentFirstAccessoryCommunication\"b1\"supportsThreadNetworkCredentialSharing\"b1\"supportsMatterSharedAdminPairing\"b1\"supportsEventLog\"b1\"supportsMatterTTU\"b1}"
+ "{_HMResidentCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"
- "\x12\x13\x11S1/G"
- "%{public}@%{public}@Failed to write characteristic requests with error: %@"
- "%{public}@%{public}@Successfully performed write requests"
- "%{public}@%{public}@[%@] Performing write requests for characteristics: %@"
- "%{public}@Missing asset properites from asset info: %@"
- "%{public}@The bundle paramter is required"
- "%{public}@The request timeout is invalid"
- "%{public}@messaging entitlement 'com.apple.private.homekit.messaging' is missing"
- "@28@0:8@16{_HMResidentCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}24"
- "@64@0:8@16@24@32@40@?48@56"
- "@72@0:8@16@24@32@40@48@?56@64"
- "HMWM.writeRequests"
- "T{_HMResidentCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},R,N,V_capabilities"
- "com.apple.private.homekit.messaging"
- "initWithUUID:configuration:context:xpcEventRouterClient:lastEventStore:timerFactory:darwinNotificationProvider:"
- "initWithUUID:configuration:context:xpcEventRouterClient:timerFactory:darwinNotificationProvider:"
- "kFetchEventCounters"
- "kLogEventDailySchedulerRequestStatus"
- "kLogEventDailySchedulerRunRegisteredBlocks"
- "kPresentTTRDialog"
- "kResetEventCounters"
- "kResetLastTTRTime"
- "performWriteRequests:forKind:completion:"
- "requestAccessWithQueue:completion:"
- "writeRequests"
- "{?=\"supports40e39e789f11ed6f1738\"b1\"supports5348b248a25f84b0c83e\"b1\"supportsAccessCodes\"b1\"supportsAnnounce\"b1\"supportsCHIP\"b1\"supportsCameraActivityZones\"b1\"supportsCameraPackageDetection\"b1\"supportsCameraRecording\"b1\"supportsCameraRecordingReachabilityNotifications\"b1\"supportsCameraSignificantEventNotifications\"b1\"supportsCustomMediaApplicationDestination\"b1\"supportsFaceClassification\"b1\"supportsFirmwareUpdate\"b1\"supportsHomeHub\"b1\"supportsLockNotificationContext\"b1\"supportsMediaActions\"b1\"supportsNaturalLighting\"b1\"supportsResidentFirmwareUpdate\"b1\"supportsResidentFirstAccessoryCommunication\"b1\"supportsRouterManagement\"b1\"supportsShortcutActions\"b1\"supportsSiriEndpointSetup\"b1\"supportsThreadBorderRouter\"b1\"supportsThreadNetworkCredentialSharing\"b1\"supportsUnifiedMediaNotifications\"b1\"supportsWakeOnLAN\"b1\"supportsWalletKey\"b1}"
- "{_HMResidentCapabilitiesStruct=\"supportsCameraRecording\"b1\"supportsRouterManagement\"b1\"supportsShortcutActions\"b1\"supportsMediaActions\"b1\"supportsCameraSignificantEventNotifications\"b1\"supportsFirmwareUpdate\"b1\"supportsResidentFirmwareUpdate\"b1\"supportsCameraActivityZones\"b1\"supportsFaceClassification\"b1\"supportsNaturalLighting\"b1\"supportsCameraRecordingReachabilityNotifications\"b1\"supportsAnnounce\"b1\"supportsWakeOnLAN\"b1\"supportsLockNotificationContext\"b1\"supportsWalletKey\"b1\"supportsCameraPackageDetection\"b1\"supportsAccessCodes\"b1\"supportsCHIP\"b1\"supportsThreadBorderRouter\"b1\"supportsSiriEndpointSetup\"b1\"supportsCustomMediaApplicationDestination\"b1\"supportsUnifiedMediaNotifications\"b1\"supportsHomeHub\"b1\"supportsResidentFirstAccessoryCommunication\"b1\"supportsThreadNetworkCredentialSharing\"b1\"supportsMatterSharedAdminPairing\"b1\"supportsEventLog\"b1}"
- "{_HMResidentCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"

```
