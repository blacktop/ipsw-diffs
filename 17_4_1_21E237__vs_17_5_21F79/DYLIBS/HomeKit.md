## HomeKit

> `/System/Library/Frameworks/HomeKit.framework/HomeKit`

```diff

-1124.5.8.1.1
-  __TEXT.__text: 0x273638
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x1ff74
+1124.6.30.0.1
+  __TEXT.__text: 0x27e31c
+  __TEXT.__auth_stubs: 0xd30
+  __TEXT.__objc_methlist: 0x20ce4
   __TEXT.__const: 0x290
-  __TEXT.__gcc_except_tab: 0x403c
-  __TEXT.__cstring: 0x25b30
-  __TEXT.__oslogstring: 0x256ef
+  __TEXT.__gcc_except_tab: 0x40ac
+  __TEXT.__cstring: 0x261a7
+  __TEXT.__oslogstring: 0x25d4f
   __TEXT.__dlopen_cstrs: 0x3ee
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x92b8
-  __TEXT.__objc_classname: 0x49ee
-  __TEXT.__objc_methname: 0x3fead
-  __TEXT.__objc_methtype: 0x7913
-  __TEXT.__objc_stubs: 0x230e0
+  __TEXT.__unwind_info: 0x9484
+  __TEXT.__objc_classname: 0x4ae3
+  __TEXT.__objc_methname: 0x422d7
+  __TEXT.__objc_methtype: 0x7d28
+  __TEXT.__objc_stubs: 0x23700
   __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0x6e78
-  __DATA_CONST.__objc_classlist: 0x1078
+  __DATA_CONST.__const: 0x6ee0
+  __DATA_CONST.__objc_classlist: 0x10a8
   __DATA_CONST.__objc_catlist: 0xe8
-  __DATA_CONST.__objc_protolist: 0x470
+  __DATA_CONST.__objc_protolist: 0x478
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x31a28
-  __DATA_CONST.__objc_selrefs: 0xbc98
+  __DATA_CONST.__objc_const: 0x32980
+  __DATA_CONST.__objc_selrefs: 0xc1b8
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_classrefs: 0x1318
-  __DATA_CONST.__objc_superrefs: 0xdf0
+  __DATA_CONST.__objc_classrefs: 0x1348
+  __DATA_CONST.__objc_superrefs: 0xe18
   __DATA_CONST.__objc_arraydata: 0x1330
-  __AUTH_CONST.__cfstring: 0x23820
-  __AUTH_CONST.__objc_const: 0xf1d0
-  __AUTH_CONST.__const: 0x1980
+  __AUTH_CONST.__cfstring: 0x23e00
+  __AUTH_CONST.__objc_const: 0xf4e8
+  __AUTH_CONST.__const: 0x19c0
   __AUTH_CONST.__objc_intobj: 0x798
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x540
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x6a0
-  __AUTH.__objc_data: 0x7c10
-  __DATA.__objc_ivar: 0x2180
-  __DATA.__data: 0x3630
+  __AUTH_CONST.__auth_got: 0x6a8
+  __AUTH.__objc_data: 0x7df0
+  __DATA.__objc_ivar: 0x2260
+  __DATA.__data: 0x36c0
   __DATA.__common: 0x18
   __DATA.__bss: 0x818
   __DATA_DIRTY.__objc_data: 0x28a0
-  __DATA_DIRTY.__bss: 0x1d0
+  __DATA_DIRTY.__bss: 0x1c0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 12547
-  Symbols:   40214
-  CStrings:  18631
+  Functions: 12840
+  Symbols:   40968
+  CStrings:  18956
 
Symbols:
+ +[HMAccessory(HMDoorbellChimeProfile) _doorbellProfilesForAccessoryProfiles:]
+ +[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo networkInfoType]
+ +[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo networkServiceInfoType]
+ +[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo networkVisibleDeviceInfosType]
+ +[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo proximityVisibleDeviceInfosType]
+ +[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo networkInfoType]
+ +[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo networkServiceInfoType]
+ +[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo networkVisibleDeviceInfosType]
+ +[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo proximityVisibleDeviceInfosType]
+ +[HMAccessoryInfoProtoNetworkInfoEvent ipv4AddressesType]
+ +[HMAccessoryInfoProtoNetworkInfoEvent ipv6AddressesType]
+ +[HMAccessoryInfoProtoNetworkServiceEvent ipv4AddressesType]
+ +[HMAccessoryInfoProtoNetworkServiceEvent ipv6AddressesType]
+ +[HMDoorbellChimeProfile logCategory]
+ +[_HMDoorbellChimeProfile logCategory]
+ +[_HMDoorbellChimeProfile supportsSecureCoding]
+ -[HMAccessory _handleSupportsCompanionInitiatedObliterateUpdatedMessage:]
+ -[HMAccessory _notifyClientsOfSupportsCompanionInitiatedObliterateUpdate]
+ -[HMAccessory setSupportsCompanionInitiatedObliterate:]
+ -[HMAccessory supportsCompanionInitiatedObliterate]
+ -[HMAccessory(HMDoorbellChimeProfile) doorbellChimeProfile]
+ -[HMAccessoryCapabilities supportsCompanionInitiatedObliterate]
+ -[HMAccessoryCapabilities supportsCoordinationFreeDoorbellChime]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo addNetworkInfo:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo addNetworkServiceInfo:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo addNetworkVisibleDeviceInfos:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo addProximityVisibleDeviceInfos:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo clearNetworkInfos]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo clearNetworkServiceInfos]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo clearNetworkVisibleDeviceInfos]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo clearProximityVisibleDeviceInfos]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo networkInfoAtIndex:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo networkInfosCount]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo networkInfos]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo networkServiceInfoAtIndex:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo networkServiceInfosCount]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo networkServiceInfos]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo networkVisibleDeviceInfosAtIndex:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo networkVisibleDeviceInfosCount]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo networkVisibleDeviceInfos]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo proximityVisibleDeviceInfosAtIndex:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo proximityVisibleDeviceInfosCount]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo proximityVisibleDeviceInfos]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setNetworkInfos:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setNetworkServiceInfos:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setNetworkVisibleDeviceInfos:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setProximityVisibleDeviceInfos:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo addNetworkInfo:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo addNetworkServiceInfo:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo addNetworkVisibleDeviceInfos:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo addProximityVisibleDeviceInfos:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo clearNetworkInfos]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo clearNetworkServiceInfos]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo clearNetworkVisibleDeviceInfos]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo clearProximityVisibleDeviceInfos]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo networkInfoAtIndex:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo networkInfosCount]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo networkInfos]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo networkServiceInfoAtIndex:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo networkServiceInfosCount]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo networkServiceInfos]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo networkVisibleDeviceInfosAtIndex:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo networkVisibleDeviceInfosCount]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo networkVisibleDeviceInfos]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo proximityVisibleDeviceInfosAtIndex:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo proximityVisibleDeviceInfosCount]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo proximityVisibleDeviceInfos]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo setNetworkInfos:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo setNetworkServiceInfos:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo setNetworkVisibleDeviceInfos:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo setProximityVisibleDeviceInfos:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo controllerSetupSessionIdentifier]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo currentDeviceConfirmedPrimaryResidentINT]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo firstCoreDataContainerSetupDurationMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo firstCoreDataContainerSetupErrorCodeHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo firstCoreDataContainerSetupErrorDomainHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo firstCoreDataContainerSetupUnderlyingErrorCodeHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo firstCoreDataContainerSetupUnderlyingErrorDomainHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasControllerSetupSessionIdentifier]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasCurrentDeviceConfirmedPrimaryResidentINT]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasFirstCoreDataContainerSetupDurationMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasFirstCoreDataContainerSetupErrorCodeHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasFirstCoreDataContainerSetupErrorDomainHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasFirstCoreDataContainerSetupUnderlyingErrorCodeHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasFirstCoreDataContainerSetupUnderlyingErrorDomainHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasLastPrimaryClientConnectMessageFailErrorCodeHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasLastPrimaryClientConnectMessageFailErrorDomainHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasLastPrimaryClientConnectMessageFailUnderlyingErrorCodeHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasLastPrimaryClientConnectMessageFailUnderlyingErrorDomainHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasLastPrimaryClientConnectedTimeHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasNumberOfTimesPrimaryClientConnectMessageFailedHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasNumberOfTimesPrimaryClientConnectedHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasNumberOfTimesPrimaryClientDisconnectedHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasNumberOfTimesPrimaryResidentChangedHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasPrimaryResidentElectionFirstCloudKitImportFutureResolvedMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasPrimaryResidentElectionJoinMeshMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasPrimaryResidentElectionModernTransportStartedFutureResolvedMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasPrimaryResidentElectionPeerDeviceFutureResolvedMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo lastPrimaryClientConnectMessageFailErrorCodeHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo lastPrimaryClientConnectMessageFailErrorDomainHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo lastPrimaryClientConnectMessageFailUnderlyingErrorCodeHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo lastPrimaryClientConnectMessageFailUnderlyingErrorDomainHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo lastPrimaryClientConnectedTimeHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo numberOfTimesPrimaryClientConnectMessageFailedHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo numberOfTimesPrimaryClientConnectedHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo numberOfTimesPrimaryClientDisconnectedHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo numberOfTimesPrimaryResidentChangedHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo primaryResidentElectionFirstCloudKitImportFutureResolvedMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo primaryResidentElectionJoinMeshMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo primaryResidentElectionModernTransportStartedFutureResolvedMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo primaryResidentElectionPeerDeviceFutureResolvedMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setControllerSetupSessionIdentifier:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setCurrentDeviceConfirmedPrimaryResidentINT:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setFirstCoreDataContainerSetupDurationMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setFirstCoreDataContainerSetupErrorCodeHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setFirstCoreDataContainerSetupErrorDomainHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setFirstCoreDataContainerSetupUnderlyingErrorCodeHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setFirstCoreDataContainerSetupUnderlyingErrorDomainHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasCurrentDeviceConfirmedPrimaryResidentINT:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasFirstCoreDataContainerSetupDurationMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasFirstCoreDataContainerSetupErrorCodeHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasFirstCoreDataContainerSetupUnderlyingErrorCodeHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasLastPrimaryClientConnectMessageFailErrorCodeHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasLastPrimaryClientConnectMessageFailUnderlyingErrorCodeHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasLastPrimaryClientConnectedTimeHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasNumberOfTimesPrimaryClientConnectMessageFailedHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasNumberOfTimesPrimaryClientConnectedHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasNumberOfTimesPrimaryClientDisconnectedHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasNumberOfTimesPrimaryResidentChangedHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasPrimaryResidentElectionFirstCloudKitImportFutureResolvedMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasPrimaryResidentElectionJoinMeshMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasPrimaryResidentElectionModernTransportStartedFutureResolvedMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasPrimaryResidentElectionPeerDeviceFutureResolvedMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setLastPrimaryClientConnectMessageFailErrorCodeHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setLastPrimaryClientConnectMessageFailErrorDomainHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setLastPrimaryClientConnectMessageFailUnderlyingErrorCodeHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setLastPrimaryClientConnectMessageFailUnderlyingErrorDomainHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setLastPrimaryClientConnectedTimeHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setNumberOfTimesPrimaryClientConnectMessageFailedHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setNumberOfTimesPrimaryClientConnectedHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setNumberOfTimesPrimaryClientDisconnectedHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setNumberOfTimesPrimaryResidentChangedHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setPrimaryResidentElectionFirstCloudKitImportFutureResolvedMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setPrimaryResidentElectionJoinMeshMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setPrimaryResidentElectionModernTransportStartedFutureResolvedMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setPrimaryResidentElectionPeerDeviceFutureResolvedMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo .cxx_destruct]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo copyTo:]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo copyWithZone:]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo description]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo dictionaryRepresentation]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo hasIdsIdentifierString]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo hasMediaRouteIdString]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo hash]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo idsIdentifierString]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo isEqual:]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo mediaRouteIdString]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo mergeFrom:]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo readFrom:]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo setIdsIdentifierString:]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo setMediaRouteIdString:]
+ -[HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo writeTo:]
+ -[HMAccessoryInfoProtoAirportInfoEvent .cxx_destruct]
+ -[HMAccessoryInfoProtoAirportInfoEvent bssid]
+ -[HMAccessoryInfoProtoAirportInfoEvent copyTo:]
+ -[HMAccessoryInfoProtoAirportInfoEvent copyWithZone:]
+ -[HMAccessoryInfoProtoAirportInfoEvent description]
+ -[HMAccessoryInfoProtoAirportInfoEvent dictionaryRepresentation]
+ -[HMAccessoryInfoProtoAirportInfoEvent hasBssid]
+ -[HMAccessoryInfoProtoAirportInfoEvent hasSsid]
+ -[HMAccessoryInfoProtoAirportInfoEvent hash]
+ -[HMAccessoryInfoProtoAirportInfoEvent isEqual:]
+ -[HMAccessoryInfoProtoAirportInfoEvent mergeFrom:]
+ -[HMAccessoryInfoProtoAirportInfoEvent readFrom:]
+ -[HMAccessoryInfoProtoAirportInfoEvent setBssid:]
+ -[HMAccessoryInfoProtoAirportInfoEvent setSsid:]
+ -[HMAccessoryInfoProtoAirportInfoEvent ssid]
+ -[HMAccessoryInfoProtoAirportInfoEvent writeTo:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent .cxx_destruct]
+ -[HMAccessoryInfoProtoNetworkInfoEvent addIpv4Addresses:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent addIpv6Addresses:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent clearIpv4Addresses]
+ -[HMAccessoryInfoProtoNetworkInfoEvent clearIpv6Addresses]
+ -[HMAccessoryInfoProtoNetworkInfoEvent copyTo:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent copyWithZone:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent description]
+ -[HMAccessoryInfoProtoNetworkInfoEvent dictionaryRepresentation]
+ -[HMAccessoryInfoProtoNetworkInfoEvent hasIfaceName]
+ -[HMAccessoryInfoProtoNetworkInfoEvent hasMacAddress]
+ -[HMAccessoryInfoProtoNetworkInfoEvent hasType]
+ -[HMAccessoryInfoProtoNetworkInfoEvent hasWifiInfo]
+ -[HMAccessoryInfoProtoNetworkInfoEvent hash]
+ -[HMAccessoryInfoProtoNetworkInfoEvent ifaceName]
+ -[HMAccessoryInfoProtoNetworkInfoEvent ipv4AddressesAtIndex:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent ipv4AddressesCount]
+ -[HMAccessoryInfoProtoNetworkInfoEvent ipv4Addresses]
+ -[HMAccessoryInfoProtoNetworkInfoEvent ipv6AddressesAtIndex:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent ipv6AddressesCount]
+ -[HMAccessoryInfoProtoNetworkInfoEvent ipv6Addresses]
+ -[HMAccessoryInfoProtoNetworkInfoEvent isEqual:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent macAddress]
+ -[HMAccessoryInfoProtoNetworkInfoEvent mergeFrom:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent readFrom:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent setIfaceName:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent setIpv4Addresses:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent setIpv6Addresses:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent setMacAddress:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent setType:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent setWifiInfo:]
+ -[HMAccessoryInfoProtoNetworkInfoEvent type]
+ -[HMAccessoryInfoProtoNetworkInfoEvent wifiInfo]
+ -[HMAccessoryInfoProtoNetworkInfoEvent writeTo:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent .cxx_destruct]
+ -[HMAccessoryInfoProtoNetworkServiceEvent addIpv4Addresses:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent addIpv6Addresses:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent clearIpv4Addresses]
+ -[HMAccessoryInfoProtoNetworkServiceEvent clearIpv6Addresses]
+ -[HMAccessoryInfoProtoNetworkServiceEvent confirmedIfaceName]
+ -[HMAccessoryInfoProtoNetworkServiceEvent copyTo:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent copyWithZone:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent description]
+ -[HMAccessoryInfoProtoNetworkServiceEvent dictionaryRepresentation]
+ -[HMAccessoryInfoProtoNetworkServiceEvent hasConfirmedIfaceName]
+ -[HMAccessoryInfoProtoNetworkServiceEvent hasIfaceName]
+ -[HMAccessoryInfoProtoNetworkServiceEvent hasIsPrimary]
+ -[HMAccessoryInfoProtoNetworkServiceEvent hasMacAddress]
+ -[HMAccessoryInfoProtoNetworkServiceEvent hasNetworkSignatureV4]
+ -[HMAccessoryInfoProtoNetworkServiceEvent hasNetworkSignatureV6]
+ -[HMAccessoryInfoProtoNetworkServiceEvent hasRouterIPv4]
+ -[HMAccessoryInfoProtoNetworkServiceEvent hasRouterIPv6]
+ -[HMAccessoryInfoProtoNetworkServiceEvent hash]
+ -[HMAccessoryInfoProtoNetworkServiceEvent ifaceName]
+ -[HMAccessoryInfoProtoNetworkServiceEvent ipv4AddressesAtIndex:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent ipv4AddressesCount]
+ -[HMAccessoryInfoProtoNetworkServiceEvent ipv4Addresses]
+ -[HMAccessoryInfoProtoNetworkServiceEvent ipv6AddressesAtIndex:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent ipv6AddressesCount]
+ -[HMAccessoryInfoProtoNetworkServiceEvent ipv6Addresses]
+ -[HMAccessoryInfoProtoNetworkServiceEvent isEqual:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent isPrimary]
+ -[HMAccessoryInfoProtoNetworkServiceEvent macAddress]
+ -[HMAccessoryInfoProtoNetworkServiceEvent mergeFrom:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent networkSignatureV4]
+ -[HMAccessoryInfoProtoNetworkServiceEvent networkSignatureV6]
+ -[HMAccessoryInfoProtoNetworkServiceEvent readFrom:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent routerIPv4]
+ -[HMAccessoryInfoProtoNetworkServiceEvent routerIPv6]
+ -[HMAccessoryInfoProtoNetworkServiceEvent setConfirmedIfaceName:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent setHasIsPrimary:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent setIfaceName:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent setIpv4Addresses:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent setIpv6Addresses:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent setIsPrimary:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent setMacAddress:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent setNetworkSignatureV4:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent setNetworkSignatureV6:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent setRouterIPv4:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent setRouterIPv6:]
+ -[HMAccessoryInfoProtoNetworkServiceEvent writeTo:]
+ -[HMDoorbellChimeProfile .cxx_destruct]
+ -[HMDoorbellChimeProfile delegate]
+ -[HMDoorbellChimeProfile didReceiveDoorbellChimeMessage:]
+ -[HMDoorbellChimeProfile initWithDoorbellChimeProfile:]
+ -[HMDoorbellChimeProfile setDelegate:]
+ -[HMHomeManager currentUserPairingIdentityForHomeContainingAccessoryWithUniqueIdentifier:completionHandler:]
+ -[HMProtoAccessoryCapabilities hasSupportsCompanionInitiatedObliterate]
+ -[HMProtoAccessoryCapabilities hasSupportsCoordinationFreeDoorbellChime]
+ -[HMProtoAccessoryCapabilities setHasSupportsCompanionInitiatedObliterate:]
+ -[HMProtoAccessoryCapabilities setHasSupportsCoordinationFreeDoorbellChime:]
+ -[HMProtoAccessoryCapabilities setSupportsCompanionInitiatedObliterate:]
+ -[HMProtoAccessoryCapabilities setSupportsCoordinationFreeDoorbellChime:]
+ -[HMProtoAccessoryCapabilities supportsCompanionInitiatedObliterate]
+ -[HMProtoAccessoryCapabilities supportsCoordinationFreeDoorbellChime]
+ -[_HMDoorbellChimeProfile .cxx_destruct]
+ -[_HMDoorbellChimeProfile _handleDoorbellChimeMessage:]
+ -[_HMDoorbellChimeProfile _registerNotificationHandlers]
+ -[_HMDoorbellChimeProfile delegate]
+ -[_HMDoorbellChimeProfile setDelegate:]
+ GCC_except_table10175
+ GCC_except_table10214
+ GCC_except_table10227
+ GCC_except_table1047
+ GCC_except_table1051
+ GCC_except_table10564
+ GCC_except_table10566
+ GCC_except_table10569
+ GCC_except_table1058
+ GCC_except_table10600
+ GCC_except_table10602
+ GCC_except_table10604
+ GCC_except_table10610
+ GCC_except_table10611
+ GCC_except_table10612
+ GCC_except_table10720
+ GCC_except_table10721
+ GCC_except_table10747
+ GCC_except_table10749
+ GCC_except_table10753
+ GCC_except_table10754
+ GCC_except_table10828
+ GCC_except_table10841
+ GCC_except_table10865
+ GCC_except_table10869
+ GCC_except_table10910
+ GCC_except_table10911
+ GCC_except_table10912
+ GCC_except_table10913
+ GCC_except_table10914
+ GCC_except_table10915
+ GCC_except_table10916
+ GCC_except_table10917
+ GCC_except_table10918
+ GCC_except_table10919
+ GCC_except_table10920
+ GCC_except_table10921
+ GCC_except_table10922
+ GCC_except_table10923
+ GCC_except_table10924
+ GCC_except_table10941
+ GCC_except_table10968
+ GCC_except_table11075
+ GCC_except_table11076
+ GCC_except_table11079
+ GCC_except_table11143
+ GCC_except_table11145
+ GCC_except_table11153
+ GCC_except_table11159
+ GCC_except_table11160
+ GCC_except_table11166
+ GCC_except_table11168
+ GCC_except_table11173
+ GCC_except_table11174
+ GCC_except_table11175
+ GCC_except_table1131
+ GCC_except_table11378
+ GCC_except_table11379
+ GCC_except_table1140
+ GCC_except_table11549
+ GCC_except_table11552
+ GCC_except_table11557
+ GCC_except_table11561
+ GCC_except_table11567
+ GCC_except_table11572
+ GCC_except_table11574
+ GCC_except_table11579
+ GCC_except_table11580
+ GCC_except_table11582
+ GCC_except_table11665
+ GCC_except_table11667
+ GCC_except_table11686
+ GCC_except_table11687
+ GCC_except_table11688
+ GCC_except_table11689
+ GCC_except_table11694
+ GCC_except_table11708
+ GCC_except_table11714
+ GCC_except_table11717
+ GCC_except_table11719
+ GCC_except_table11801
+ GCC_except_table11803
+ GCC_except_table11806
+ GCC_except_table11814
+ GCC_except_table11815
+ GCC_except_table11820
+ GCC_except_table11826
+ GCC_except_table11828
+ GCC_except_table11830
+ GCC_except_table11832
+ GCC_except_table11834
+ GCC_except_table11836
+ GCC_except_table11838
+ GCC_except_table11972
+ GCC_except_table12028
+ GCC_except_table12029
+ GCC_except_table12030
+ GCC_except_table12031
+ GCC_except_table12042
+ GCC_except_table12043
+ GCC_except_table12067
+ GCC_except_table12068
+ GCC_except_table1208
+ GCC_except_table1210
+ GCC_except_table12121
+ GCC_except_table1213
+ GCC_except_table12144
+ GCC_except_table12147
+ GCC_except_table1215
+ GCC_except_table1217
+ GCC_except_table1221
+ GCC_except_table12279
+ GCC_except_table12391
+ GCC_except_table12392
+ GCC_except_table12393
+ GCC_except_table12441
+ GCC_except_table12442
+ GCC_except_table12444
+ GCC_except_table12447
+ GCC_except_table12449
+ GCC_except_table12451
+ GCC_except_table12483
+ GCC_except_table12526
+ GCC_except_table12531
+ GCC_except_table12534
+ GCC_except_table12594
+ GCC_except_table12679
+ GCC_except_table12687
+ GCC_except_table1270
+ GCC_except_table12740
+ GCC_except_table12742
+ GCC_except_table12751
+ GCC_except_table12754
+ GCC_except_table12774
+ GCC_except_table12776
+ GCC_except_table12777
+ GCC_except_table1402
+ GCC_except_table1423
+ GCC_except_table1500
+ GCC_except_table1503
+ GCC_except_table1521
+ GCC_except_table1656
+ GCC_except_table1725
+ GCC_except_table1728
+ GCC_except_table1797
+ GCC_except_table1799
+ GCC_except_table1873
+ GCC_except_table1874
+ GCC_except_table1922
+ GCC_except_table2151
+ GCC_except_table2154
+ GCC_except_table2157
+ GCC_except_table2162
+ GCC_except_table2166
+ GCC_except_table2175
+ GCC_except_table2177
+ GCC_except_table2180
+ GCC_except_table2190
+ GCC_except_table2192
+ GCC_except_table2193
+ GCC_except_table2198
+ GCC_except_table2199
+ GCC_except_table2200
+ GCC_except_table2201
+ GCC_except_table2591
+ GCC_except_table2596
+ GCC_except_table2622
+ GCC_except_table2625
+ GCC_except_table2639
+ GCC_except_table2677
+ GCC_except_table2694
+ GCC_except_table2697
+ GCC_except_table2698
+ GCC_except_table2701
+ GCC_except_table2724
+ GCC_except_table2726
+ GCC_except_table2728
+ GCC_except_table2730
+ GCC_except_table2890
+ GCC_except_table2908
+ GCC_except_table2909
+ GCC_except_table2973
+ GCC_except_table2976
+ GCC_except_table3001
+ GCC_except_table3003
+ GCC_except_table3011
+ GCC_except_table3013
+ GCC_except_table3020
+ GCC_except_table3021
+ GCC_except_table3022
+ GCC_except_table3024
+ GCC_except_table3025
+ GCC_except_table3026
+ GCC_except_table3027
+ GCC_except_table3028
+ GCC_except_table3080
+ GCC_except_table3110
+ GCC_except_table3113
+ GCC_except_table3116
+ GCC_except_table3119
+ GCC_except_table3122
+ GCC_except_table3187
+ GCC_except_table3188
+ GCC_except_table3233
+ GCC_except_table3240
+ GCC_except_table3241
+ GCC_except_table3242
+ GCC_except_table3245
+ GCC_except_table3246
+ GCC_except_table3247
+ GCC_except_table3249
+ GCC_except_table3257
+ GCC_except_table3265
+ GCC_except_table3266
+ GCC_except_table3284
+ GCC_except_table3291
+ GCC_except_table3295
+ GCC_except_table3298
+ GCC_except_table3301
+ GCC_except_table3342
+ GCC_except_table3346
+ GCC_except_table3350
+ GCC_except_table3355
+ GCC_except_table3363
+ GCC_except_table3367
+ GCC_except_table3376
+ GCC_except_table3378
+ GCC_except_table3611
+ GCC_except_table3615
+ GCC_except_table3619
+ GCC_except_table3622
+ GCC_except_table3627
+ GCC_except_table3630
+ GCC_except_table3636
+ GCC_except_table3639
+ GCC_except_table3668
+ GCC_except_table3670
+ GCC_except_table3672
+ GCC_except_table3675
+ GCC_except_table3676
+ GCC_except_table3678
+ GCC_except_table3681
+ GCC_except_table3763
+ GCC_except_table3768
+ GCC_except_table3780
+ GCC_except_table3783
+ GCC_except_table3785
+ GCC_except_table3788
+ GCC_except_table3795
+ GCC_except_table3848
+ GCC_except_table3914
+ GCC_except_table3929
+ GCC_except_table3932
+ GCC_except_table4025
+ GCC_except_table4026
+ GCC_except_table4028
+ GCC_except_table4033
+ GCC_except_table4037
+ GCC_except_table4040
+ GCC_except_table4042
+ GCC_except_table4050
+ GCC_except_table4254
+ GCC_except_table4257
+ GCC_except_table4269
+ GCC_except_table4344
+ GCC_except_table4363
+ GCC_except_table4553
+ GCC_except_table4558
+ GCC_except_table4559
+ GCC_except_table4567
+ GCC_except_table4569
+ GCC_except_table4594
+ GCC_except_table4595
+ GCC_except_table4596
+ GCC_except_table4597
+ GCC_except_table4657
+ GCC_except_table4667
+ GCC_except_table4732
+ GCC_except_table4734
+ GCC_except_table4736
+ GCC_except_table4778
+ GCC_except_table4779
+ GCC_except_table4852
+ GCC_except_table4939
+ GCC_except_table4940
+ GCC_except_table4946
+ GCC_except_table4948
+ GCC_except_table4977
+ GCC_except_table4979
+ GCC_except_table4998
+ GCC_except_table5044
+ GCC_except_table506
+ GCC_except_table509
+ GCC_except_table5094
+ GCC_except_table511
+ GCC_except_table517
+ GCC_except_table5180
+ GCC_except_table519
+ GCC_except_table5200
+ GCC_except_table5201
+ GCC_except_table5202
+ GCC_except_table5204
+ GCC_except_table5207
+ GCC_except_table5208
+ GCC_except_table521
+ GCC_except_table5210
+ GCC_except_table5424
+ GCC_except_table5430
+ GCC_except_table5432
+ GCC_except_table5442
+ GCC_except_table5443
+ GCC_except_table5690
+ GCC_except_table5798
+ GCC_except_table5804
+ GCC_except_table5811
+ GCC_except_table5816
+ GCC_except_table5899
+ GCC_except_table5905
+ GCC_except_table5907
+ GCC_except_table6045
+ GCC_except_table6205
+ GCC_except_table6230
+ GCC_except_table6244
+ GCC_except_table6259
+ GCC_except_table6266
+ GCC_except_table6269
+ GCC_except_table6283
+ GCC_except_table6288
+ GCC_except_table6322
+ GCC_except_table6333
+ GCC_except_table6339
+ GCC_except_table6343
+ GCC_except_table6351
+ GCC_except_table6356
+ GCC_except_table6370
+ GCC_except_table6375
+ GCC_except_table6383
+ GCC_except_table6385
+ GCC_except_table6388
+ GCC_except_table6393
+ GCC_except_table6400
+ GCC_except_table6405
+ GCC_except_table6409
+ GCC_except_table6437
+ GCC_except_table6443
+ GCC_except_table6468
+ GCC_except_table6473
+ GCC_except_table6477
+ GCC_except_table6502
+ GCC_except_table6506
+ GCC_except_table6508
+ GCC_except_table6509
+ GCC_except_table659
+ GCC_except_table662
+ GCC_except_table6644
+ GCC_except_table6650
+ GCC_except_table667
+ GCC_except_table670
+ GCC_except_table671
+ GCC_except_table6728
+ GCC_except_table6750
+ GCC_except_table6755
+ GCC_except_table6757
+ GCC_except_table6765
+ GCC_except_table6810
+ GCC_except_table6812
+ GCC_except_table6824
+ GCC_except_table6836
+ GCC_except_table6863
+ GCC_except_table6879
+ GCC_except_table6882
+ GCC_except_table6885
+ GCC_except_table6888
+ GCC_except_table6891
+ GCC_except_table6900
+ GCC_except_table6910
+ GCC_except_table693
+ GCC_except_table6930
+ GCC_except_table6933
+ GCC_except_table6936
+ GCC_except_table6942
+ GCC_except_table6945
+ GCC_except_table6948
+ GCC_except_table6951
+ GCC_except_table6954
+ GCC_except_table6957
+ GCC_except_table6960
+ GCC_except_table6963
+ GCC_except_table6966
+ GCC_except_table6969
+ GCC_except_table6972
+ GCC_except_table6975
+ GCC_except_table6978
+ GCC_except_table6982
+ GCC_except_table6994
+ GCC_except_table6995
+ GCC_except_table7004
+ GCC_except_table7021
+ GCC_except_table7023
+ GCC_except_table7048
+ GCC_except_table7062
+ GCC_except_table7064
+ GCC_except_table7084
+ GCC_except_table7088
+ GCC_except_table710
+ GCC_except_table7249
+ GCC_except_table727
+ GCC_except_table7463
+ GCC_except_table7533
+ GCC_except_table7637
+ GCC_except_table7642
+ GCC_except_table7653
+ GCC_except_table7729
+ GCC_except_table7747
+ GCC_except_table7753
+ GCC_except_table7758
+ GCC_except_table7892
+ GCC_except_table7895
+ GCC_except_table7905
+ GCC_except_table7908
+ GCC_except_table7910
+ GCC_except_table7913
+ GCC_except_table7944
+ GCC_except_table7946
+ GCC_except_table7964
+ GCC_except_table7972
+ GCC_except_table7974
+ GCC_except_table7976
+ GCC_except_table7978
+ GCC_except_table7985
+ GCC_except_table7991
+ GCC_except_table7993
+ GCC_except_table7995
+ GCC_except_table7996
+ GCC_except_table8005
+ GCC_except_table8063
+ GCC_except_table8065
+ GCC_except_table8073
+ GCC_except_table8075
+ GCC_except_table8077
+ GCC_except_table8079
+ GCC_except_table8081
+ GCC_except_table8103
+ GCC_except_table8105
+ GCC_except_table8107
+ GCC_except_table8109
+ GCC_except_table8128
+ GCC_except_table8278
+ GCC_except_table8280
+ GCC_except_table8281
+ GCC_except_table8282
+ GCC_except_table8284
+ GCC_except_table8286
+ GCC_except_table8287
+ GCC_except_table8288
+ GCC_except_table8324
+ GCC_except_table8327
+ GCC_except_table8328
+ GCC_except_table8331
+ GCC_except_table8334
+ GCC_except_table8335
+ GCC_except_table835
+ GCC_except_table8379
+ GCC_except_table838
+ GCC_except_table8380
+ GCC_except_table8381
+ GCC_except_table8388
+ GCC_except_table8389
+ GCC_except_table839
+ GCC_except_table8391
+ GCC_except_table840
+ GCC_except_table841
+ GCC_except_table842
+ GCC_except_table844
+ GCC_except_table845
+ GCC_except_table8453
+ GCC_except_table8454
+ GCC_except_table8455
+ GCC_except_table8492
+ GCC_except_table852
+ GCC_except_table853
+ GCC_except_table8674
+ GCC_except_table8675
+ GCC_except_table8676
+ GCC_except_table8680
+ GCC_except_table8735
+ GCC_except_table8756
+ GCC_except_table8827
+ GCC_except_table8833
+ GCC_except_table8835
+ GCC_except_table8837
+ GCC_except_table8839
+ GCC_except_table8847
+ GCC_except_table8896
+ GCC_except_table8897
+ GCC_except_table8899
+ GCC_except_table8924
+ GCC_except_table8952
+ GCC_except_table9127
+ GCC_except_table9179
+ GCC_except_table9186
+ GCC_except_table9191
+ GCC_except_table9196
+ GCC_except_table9213
+ GCC_except_table9219
+ GCC_except_table9221
+ GCC_except_table9251
+ GCC_except_table9271
+ GCC_except_table9272
+ GCC_except_table9273
+ GCC_except_table9310
+ GCC_except_table9311
+ GCC_except_table9315
+ GCC_except_table9317
+ GCC_except_table9319
+ GCC_except_table9378
+ GCC_except_table9405
+ GCC_except_table9408
+ GCC_except_table9410
+ GCC_except_table9412
+ GCC_except_table9414
+ GCC_except_table9416
+ GCC_except_table9422
+ GCC_except_table9424
+ GCC_except_table9430
+ GCC_except_table9434
+ GCC_except_table9437
+ GCC_except_table9444
+ GCC_except_table9448
+ GCC_except_table9454
+ GCC_except_table9460
+ GCC_except_table9463
+ GCC_except_table9471
+ GCC_except_table9472
+ GCC_except_table9485
+ GCC_except_table9495
+ GCC_except_table9699
+ GCC_except_table9712
+ GCC_except_table9761
+ GCC_except_table9762
+ GCC_except_table9764
+ GCC_except_table9768
+ GCC_except_table9776
+ GCC_except_table9832
+ GCC_except_table9835
+ GCC_except_table9836
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._networkInfos
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._networkServiceInfos
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._networkVisibleDeviceInfos
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._proximityVisibleDeviceInfos
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo._networkInfos
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo._networkServiceInfos
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo._networkVisibleDeviceInfos
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo._proximityVisibleDeviceInfos
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._controllerSetupSessionIdentifier
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._currentDeviceConfirmedPrimaryResidentINT
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._firstCoreDataContainerSetupDurationMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._firstCoreDataContainerSetupErrorCodeHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._firstCoreDataContainerSetupErrorDomainHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._firstCoreDataContainerSetupUnderlyingErrorCodeHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._firstCoreDataContainerSetupUnderlyingErrorDomainHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._lastPrimaryClientConnectMessageFailErrorCodeHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._lastPrimaryClientConnectMessageFailErrorDomainHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._lastPrimaryClientConnectMessageFailUnderlyingErrorCodeHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._lastPrimaryClientConnectMessageFailUnderlyingErrorDomainHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._lastPrimaryClientConnectedTimeHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._numberOfTimesPrimaryClientConnectMessageFailedHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._numberOfTimesPrimaryClientConnectedHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._numberOfTimesPrimaryClientDisconnectedHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._numberOfTimesPrimaryResidentChangedHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._primaryResidentElectionFirstCloudKitImportFutureResolvedMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._primaryResidentElectionJoinMeshMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._primaryResidentElectionModernTransportStartedFutureResolvedMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._primaryResidentElectionPeerDeviceFutureResolvedMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo._idsIdentifierString
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo._mediaRouteIdString
+ OBJC_IVAR_$_HMAccessoryInfoProtoAirportInfoEvent._bssid
+ OBJC_IVAR_$_HMAccessoryInfoProtoAirportInfoEvent._ssid
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkInfoEvent._ifaceName
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkInfoEvent._ipv4Addresses
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkInfoEvent._ipv6Addresses
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkInfoEvent._macAddress
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkInfoEvent._type
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkInfoEvent._wifiInfo
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkServiceEvent._confirmedIfaceName
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkServiceEvent._has
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkServiceEvent._ifaceName
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkServiceEvent._ipv4Addresses
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkServiceEvent._ipv6Addresses
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkServiceEvent._isPrimary
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkServiceEvent._macAddress
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkServiceEvent._networkSignatureV4
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkServiceEvent._networkSignatureV6
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkServiceEvent._routerIPv4
+ OBJC_IVAR_$_HMAccessoryInfoProtoNetworkServiceEvent._routerIPv6
+ OBJC_IVAR_$_HMProtoAccessoryCapabilities._supportsCompanionInitiatedObliterate
+ OBJC_IVAR_$_HMProtoAccessoryCapabilities._supportsCoordinationFreeDoorbellChime
+ _CoreAnalyticsLibraryCore.frameworkLibrary.36699
+ _CoreHAPLibraryCore.frameworkLibrary.29869
+ _HMAccessoryDiagnosticInfoProtoVisibleDeviceInfoReadFrom
+ _HMAccessoryInfoProtoAirportInfoEventReadFrom
+ _HMAccessoryInfoProtoNetworkInfoEventReadFrom
+ _HMAccessoryInfoProtoNetworkServiceEventReadFrom
+ _HMAccessorySupportsCompanionInitiatedObliterateCodingKey
+ _HMDoorbellChimeDateMessagePayloadKey
+ _HMDoorbellChimeMessageName
+ _HMDoorbellChimeModeMessagePayloadKey
+ _HMDoorbellChimePersonIdentificationTextMessagePayloadKey
+ _HMHomeManagerFetchCurrentUserPairingIdentityForHomeContainingAccessoryRequestMessage
+ _HMHomeManagerIsDemoModeActive
+ _HMHomePreferredResidentIDSIdentifierKey
+ _HMHomeSetPreferredPrimaryMessageKeyResidentName
+ _IDSFoundationLibraryCore.40392
+ _IDSFoundationLibraryCore.frameworkLibrary.40394
+ _OBJC_CLASS_$_HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo
+ _OBJC_CLASS_$_HMAccessoryInfoProtoAirportInfoEvent
+ _OBJC_CLASS_$_HMAccessoryInfoProtoNetworkInfoEvent
+ _OBJC_CLASS_$_HMAccessoryInfoProtoNetworkServiceEvent
+ _OBJC_CLASS_$_HMDoorbellChimeProfile
+ _OBJC_CLASS_$__HMDoorbellChimeProfile
+ _OBJC_IVAR_$_HMAccessory._supportsCompanionInitiatedObliterate
+ _OBJC_IVAR_$_HMDoorbellChimeProfile._delegate
+ _OBJC_IVAR_$_HMDoorbellChimeProfile._lock
+ _OBJC_IVAR_$__HMDoorbellChimeProfile._delegate
+ _OBJC_IVAR_$__HMDoorbellChimeProfile._lock
+ _OBJC_METACLASS_$_HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo
+ _OBJC_METACLASS_$_HMAccessoryInfoProtoAirportInfoEvent
+ _OBJC_METACLASS_$_HMAccessoryInfoProtoNetworkInfoEvent
+ _OBJC_METACLASS_$_HMAccessoryInfoProtoNetworkServiceEvent
+ _OBJC_METACLASS_$_HMDoorbellChimeProfile
+ _OBJC_METACLASS_$__HMDoorbellChimeProfile
+ _PBDataWriterWriteUint32Field
+ _UIKitLibrary.40624
+ _UIKitLibraryCore.40620
+ _UIKitLibraryCore.frameworkLibrary.40633
+ __OBJC_$_CLASS_METHODS_HMAccessory(SiriEndpoint|Television|WoL|LightInternal|HMDoorbellChimeProfile|NetworkRouter|NetworkRouterInternal|Private|PendingConfiguration|CUPeerIdentifier|Shortcuts|Camera|CHIP|NetworkConfiguration|Light|Media)
+ __OBJC_$_CLASS_METHODS_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo
+ __OBJC_$_CLASS_METHODS_HMAccessoryInfoProtoNetworkInfoEvent
+ __OBJC_$_CLASS_METHODS_HMAccessoryInfoProtoNetworkServiceEvent
+ __OBJC_$_CLASS_METHODS_HMDoorbellChimeProfile
+ __OBJC_$_CLASS_METHODS__HMDoorbellChimeProfile
+ __OBJC_$_INSTANCE_METHODS_HMAccessory(SiriEndpoint|Television|WoL|LightInternal|HMDoorbellChimeProfile|NetworkRouter|NetworkRouterInternal|Private|PendingConfiguration|CUPeerIdentifier|Shortcuts|Camera|CHIP|NetworkConfiguration|Light|Media)
+ __OBJC_$_INSTANCE_METHODS_HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo
+ __OBJC_$_INSTANCE_METHODS_HMAccessoryInfoProtoAirportInfoEvent
+ __OBJC_$_INSTANCE_METHODS_HMAccessoryInfoProtoNetworkInfoEvent
+ __OBJC_$_INSTANCE_METHODS_HMAccessoryInfoProtoNetworkServiceEvent
+ __OBJC_$_INSTANCE_METHODS_HMDoorbellChimeProfile
+ __OBJC_$_INSTANCE_METHODS__HMDoorbellChimeProfile
+ __OBJC_$_INSTANCE_VARIABLES_HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo
+ __OBJC_$_INSTANCE_VARIABLES_HMAccessoryInfoProtoAirportInfoEvent
+ __OBJC_$_INSTANCE_VARIABLES_HMAccessoryInfoProtoNetworkInfoEvent
+ __OBJC_$_INSTANCE_VARIABLES_HMAccessoryInfoProtoNetworkServiceEvent
+ __OBJC_$_INSTANCE_VARIABLES_HMDoorbellChimeProfile
+ __OBJC_$_INSTANCE_VARIABLES__HMDoorbellChimeProfile
+ __OBJC_$_PROP_LIST_HMAccessoryCapabilities.138
+ __OBJC_$_PROP_LIST_HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo
+ __OBJC_$_PROP_LIST_HMAccessoryInfoProtoAirportInfoEvent
+ __OBJC_$_PROP_LIST_HMAccessoryInfoProtoNetworkInfoEvent
+ __OBJC_$_PROP_LIST_HMAccessoryInfoProtoNetworkServiceEvent
+ __OBJC_$_PROP_LIST_HMApplicationData.11820
+ __OBJC_$_PROP_LIST_HMDoorbellChimeProfile
+ __OBJC_$_PROP_LIST_HMResidentCapabilities.202
+ __OBJC_$_PROP_LIST__HMDoorbellChimeProfile
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__HMDoorbellChimeProfileDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__HMDoorbellChimeProfileDelegate
+ __OBJC_CLASS_PROTOCOLS_$_HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo
+ __OBJC_CLASS_PROTOCOLS_$_HMAccessoryInfoProtoAirportInfoEvent
+ __OBJC_CLASS_PROTOCOLS_$_HMAccessoryInfoProtoNetworkInfoEvent
+ __OBJC_CLASS_PROTOCOLS_$_HMAccessoryInfoProtoNetworkServiceEvent
+ __OBJC_CLASS_PROTOCOLS_$_HMDoorbellChimeProfile
+ __OBJC_CLASS_PROTOCOLS_$__HMDoorbellChimeProfile
+ __OBJC_CLASS_RO_$_HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo
+ __OBJC_CLASS_RO_$_HMAccessoryInfoProtoAirportInfoEvent
+ __OBJC_CLASS_RO_$_HMAccessoryInfoProtoNetworkInfoEvent
+ __OBJC_CLASS_RO_$_HMAccessoryInfoProtoNetworkServiceEvent
+ __OBJC_CLASS_RO_$_HMDoorbellChimeProfile
+ __OBJC_CLASS_RO_$__HMDoorbellChimeProfile
+ __OBJC_LABEL_PROTOCOL_$__HMDoorbellChimeProfileDelegate
+ __OBJC_METACLASS_RO_$_HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo
+ __OBJC_METACLASS_RO_$_HMAccessoryInfoProtoAirportInfoEvent
+ __OBJC_METACLASS_RO_$_HMAccessoryInfoProtoNetworkInfoEvent
+ __OBJC_METACLASS_RO_$_HMAccessoryInfoProtoNetworkServiceEvent
+ __OBJC_METACLASS_RO_$_HMDoorbellChimeProfile
+ __OBJC_METACLASS_RO_$__HMDoorbellChimeProfile
+ __OBJC_PROTOCOL_$__HMDoorbellChimeProfileDelegate
+ ___108-[HMHomeManager currentUserPairingIdentityForHomeContainingAccessoryWithUniqueIdentifier:completionHandler:]_block_invoke
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.782
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.786
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.790
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.792
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.791
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.793
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.789
+ ___22-[HMHome _mergeRooms:]_block_invoke.766
+ ___22-[HMHome _mergeRooms:]_block_invoke.768
+ ___22-[HMHome _mergeRooms:]_block_invoke_2.770
+ ___22-[HMHome _mergeRooms:]_block_invoke_3.771
+ ___22-[HMHome _mergeUsers:]_block_invoke.812
+ ___22-[HMHome _mergeUsers:]_block_invoke.814
+ ___22-[HMHome _mergeUsers:]_block_invoke_2.816
+ ___22-[HMHome _mergeUsers:]_block_invoke_3.817
+ ___22-[HMHome _mergeZones:]_block_invoke.774
+ ___22-[HMHome _mergeZones:]_block_invoke.776
+ ___22-[HMHome _mergeZones:]_block_invoke_2.778
+ ___22-[HMHome _mergeZones:]_block_invoke_3.779
+ ___25-[HMHome _mergeTriggers:]_block_invoke.807
+ ___25-[HMHome _mergeTriggers:]_block_invoke.809
+ ___27-[HMHome _mergeActionSets:]_block_invoke.799
+ ___27-[HMHome _mergeActionSets:]_block_invoke.801
+ ___27-[HMHome _mergeActionSets:]_block_invoke_2.803
+ ___27-[HMHome _mergeActionSets:]_block_invoke_3.804
+ ___28-[HMHome _mergeAccessories:]_block_invoke.785
+ ___28-[HMHome _mergeAccessories:]_block_invoke.787
+ ___28-[HMHome _mergeAccessories:]_block_invoke_2.788
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.546
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.550
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.554
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.558
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.560
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.564
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.568
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.580
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.584
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.588
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.592
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.735
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.747
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.761
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.547
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.551
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.555
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.559
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.561
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.565
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.569
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.581
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.585
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.589
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.593
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.736
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.748
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.762
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_3.750
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_4.751
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_5.752
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_6.753
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1117
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1118
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1120
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1124
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1122
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1125
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.1123
+ ___30-[HMAccessory _mergeServices:]_block_invoke.934
+ ___30-[HMAccessory _mergeServices:]_block_invoke.936
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke.791
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke.793
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke_2.795
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke_3.796
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke.820
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke.822
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke_2.824
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke_3.825
+ ___32-[HMService mergeFromNewObject:]_block_invoke.303
+ ___32-[HMService mergeFromNewObject:]_block_invoke.305
+ ___32-[HMService mergeFromNewObject:]_block_invoke.307
+ ___32-[HMService mergeFromNewObject:]_block_invoke.309
+ ___32-[HMService mergeFromNewObject:]_block_invoke.311
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1093
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1095
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1107
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1108
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1109
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1110
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1112
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1114
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1115
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.939
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.943
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.946
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.949
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.952
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.961
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.963
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.970
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.974
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1094
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1096
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1101
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1113
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.940
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.944
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.947
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.950
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.953
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.962
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.964
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.971
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.975
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.972
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.977
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.978
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.979
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_6.1087
+ ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.827
+ ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.829
+ ___37+[HMDoorbellChimeProfile logCategory]_block_invoke
+ ___38+[_HMDoorbellChimeProfile logCategory]_block_invoke
+ ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.532
+ ___39-[HMCharacteristic mergeFromNewObject:]_block_invoke.141
+ ___39-[HMHome _mergeTriggerOwnedActionSets:]_block_invoke.805
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.795
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.797
+ ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1152
+ ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1154
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.832
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.834
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.836
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke_2.835
+ ___43-[HMHome fetchPresenceForUsers:completion:]_block_invoke.845
+ ___43-[HMHome fetchPresenceForUsers:completion:]_block_invoke.847
+ ___44-[HMHome _handleAccessoryAddedNotification:]_block_invoke.916
+ ___45-[HMAccessory _handleCharacteristicsUpdated:]_block_invoke.1138
+ ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.704
+ ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1139
+ ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1140
+ ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.764
+ ___52-[HMHome(HMUser) _manageUsersWithCompletionHandler:]_block_invoke.1731
+ ___54-[HMHome _notifyDelegateOfAccessControlUpdateForUser:]_block_invoke.949
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.626
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.627
+ ___57-[HMDoorbellChimeProfile didReceiveDoorbellChimeMessage:]_block_invoke
+ ___57-[HMDoorbellChimeProfile didReceiveDoorbellChimeMessage:]_block_invoke.79
+ ___58-[HMHomeManager __resolveAccountHandle:completionHandler:]_block_invoke.691
+ ___61-[HMHomeManager __removeAccountWithHandle:completionHandler:]_block_invoke.693
+ ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.873
+ ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.875
+ ___64-[HMHome(HMMediaProfile) updateMediaPassword:completionHandler:]_block_invoke.1809
+ ___65-[HMHomeManager __removeAccountWithIdentifier:completionHandler:]_block_invoke.692
+ ___67-[HMHome _addEventTriggerFromResponse:withEventTrigger:completion:]_block_invoke.909
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.722
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.726
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.728
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.730
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke_2.731
+ ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.848
+ ___73-[HMAccessory _notifyClientsOfSupportsCompanionInitiatedObliterateUpdate]_block_invoke
+ ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.701
+ ___75-[HMHome(HMAccessory) addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.1594
+ ___80-[HMDeviceSetupOperation setupSession:didReceiveExchangeData:completionHandler:]_block_invoke.34
+ ___88-[HMHome(HMAccessory) addAccessoryWithAccessorySetupPayload:progress:completionHandler:]_block_invoke.1605
+ ___88-[HMHome(HMAccessory) addAndSetUpNewAccessoriesWithSuggestedRoomName:completionHandler:]_block_invoke.1596
+ ___88-[HMHome(HomeLocationFeedback) retrieveHomeKitLocationForFeedbackWithCompletionHandler:]_block_invoke.1894
+ ___89-[HMHome(NetworkRouter) updateAccessoryNetworkProtectionGroup:protectionMode:completion:]_block_invoke.1864
+ ___93-[HMHomeManager _pingDeviceWithUUID:monitor:secure:restrictToLocalNetwork:completionHandler:]_block_invoke.694
+ ___Block_byref_object_copy_.14863
+ ___Block_byref_object_copy_.15166
+ ___Block_byref_object_copy_.21895
+ ___Block_byref_object_copy_.23973
+ ___Block_byref_object_copy_.28193
+ ___Block_byref_object_copy_.29959
+ ___Block_byref_object_copy_.36586
+ ___Block_byref_object_copy_.39518
+ ___Block_byref_object_copy_.61067
+ ___Block_byref_object_dispose_.14864
+ ___Block_byref_object_dispose_.15167
+ ___Block_byref_object_dispose_.21896
+ ___Block_byref_object_dispose_.23974
+ ___Block_byref_object_dispose_.28194
+ ___Block_byref_object_dispose_.29960
+ ___Block_byref_object_dispose_.36587
+ ___Block_byref_object_dispose_.39519
+ ___Block_byref_object_dispose_.61068
+ ___CoreAnalyticsLibraryCore_block_invoke.36700
+ ___CoreHAPLibraryCore_block_invoke.29870
+ ___IDSFoundationLibraryCore_block_invoke.40395
+ ___UIKitLibraryCore_block_invoke.40634
+ _____HMHomeManagerRegisterForNotifications_block_invoke.1403
+ ___block_descriptor_80_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.10027
+ ___block_literal_global.101.36707
+ ___block_literal_global.10725
+ ___block_literal_global.1133
+ ___block_literal_global.11753
+ ___block_literal_global.11881
+ ___block_literal_global.12.46592
+ ___block_literal_global.121.49537
+ ___block_literal_global.1270
+ ___block_literal_global.12862
+ ___block_literal_global.13003
+ ___block_literal_global.13075
+ ___block_literal_global.13530
+ ___block_literal_global.13724
+ ___block_literal_global.14291
+ ___block_literal_global.14626
+ ___block_literal_global.14945
+ ___block_literal_global.15534
+ ___block_literal_global.156
+ ___block_literal_global.1613
+ ___block_literal_global.16615
+ ___block_literal_global.17.18285
+ ___block_literal_global.17151
+ ___block_literal_global.17344
+ ___block_literal_global.17477
+ ___block_literal_global.17640
+ ___block_literal_global.1783
+ ___block_literal_global.1806
+ ___block_literal_global.18292
+ ___block_literal_global.18947
+ ___block_literal_global.19.14611
+ ___block_literal_global.19372
+ ___block_literal_global.19925
+ ___block_literal_global.20264
+ ___block_literal_global.21276
+ ___block_literal_global.21933
+ ___block_literal_global.22206
+ ___block_literal_global.2240
+ ___block_literal_global.22679
+ ___block_literal_global.22900
+ ___block_literal_global.23207
+ ___block_literal_global.23338
+ ___block_literal_global.23586
+ ___block_literal_global.23836
+ ___block_literal_global.23998
+ ___block_literal_global.24092
+ ___block_literal_global.26680
+ ___block_literal_global.26813
+ ___block_literal_global.27293
+ ___block_literal_global.28055
+ ___block_literal_global.28352
+ ___block_literal_global.28700
+ ___block_literal_global.28904
+ ___block_literal_global.29185
+ ___block_literal_global.29261
+ ___block_literal_global.30.18275
+ ___block_literal_global.30.8017
+ ___block_literal_global.30171
+ ___block_literal_global.30585
+ ___block_literal_global.30857
+ ___block_literal_global.31704
+ ___block_literal_global.32075
+ ___block_literal_global.33.60407
+ ___block_literal_global.33176
+ ___block_literal_global.34087
+ ___block_literal_global.34319
+ ___block_literal_global.34544
+ ___block_literal_global.35499
+ ___block_literal_global.3609
+ ___block_literal_global.36694
+ ___block_literal_global.36944
+ ___block_literal_global.37286
+ ___block_literal_global.37916
+ ___block_literal_global.38783
+ ___block_literal_global.38910
+ ___block_literal_global.39
+ ___block_literal_global.39187
+ ___block_literal_global.3950
+ ___block_literal_global.4042
+ ___block_literal_global.40456
+ ___block_literal_global.40552
+ ___block_literal_global.41261
+ ___block_literal_global.41451
+ ___block_literal_global.42074
+ ___block_literal_global.42700
+ ___block_literal_global.43146
+ ___block_literal_global.43465
+ ___block_literal_global.44197
+ ___block_literal_global.45085
+ ___block_literal_global.46313
+ ___block_literal_global.46604
+ ___block_literal_global.467
+ ___block_literal_global.46870
+ ___block_literal_global.47065
+ ___block_literal_global.47294
+ ___block_literal_global.48001
+ ___block_literal_global.48121
+ ___block_literal_global.48854
+ ___block_literal_global.4898
+ ___block_literal_global.49290
+ ___block_literal_global.49624
+ ___block_literal_global.50538
+ ___block_literal_global.51
+ ___block_literal_global.513
+ ___block_literal_global.518
+ ___block_literal_global.53128
+ ___block_literal_global.5338
+ ___block_literal_global.53836
+ ___block_literal_global.55163
+ ___block_literal_global.55857
+ ___block_literal_global.56392
+ ___block_literal_global.56704
+ ___block_literal_global.57218
+ ___block_literal_global.57395
+ ___block_literal_global.5774
+ ___block_literal_global.57759
+ ___block_literal_global.57999
+ ___block_literal_global.5909
+ ___block_literal_global.59641
+ ___block_literal_global.59809
+ ___block_literal_global.60147
+ ___block_literal_global.60413
+ ___block_literal_global.60775
+ ___block_literal_global.61065
+ ___block_literal_global.61361
+ ___block_literal_global.6444
+ ___block_literal_global.6928
+ ___block_literal_global.7209
+ ___block_literal_global.73.22184
+ ___block_literal_global.73.37279
+ ___block_literal_global.743
+ ___block_literal_global.745
+ ___block_literal_global.76.26448
+ ___block_literal_global.7681
+ ___block_literal_global.7798
+ ___block_literal_global.8035
+ ___block_literal_global.81.36916
+ ___block_literal_global.8506
+ ___block_literal_global.852
+ ___block_literal_global.9043
+ ___block_literal_global.914
+ ___block_literal_global.9325
+ ___block_literal_global.935
+ ___block_literal_global.9501
+ ___block_literal_global.980
+ ___block_literal_global.985
+ ___getAnalyticsSendEventLazySymbolLoc_block_invoke.36697
+ ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.40629
+ ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.40623
+ __unnamed_array_storage.143.26598
+ __unnamed_array_storage.14880
+ __unnamed_array_storage.227.26595
+ __unnamed_array_storage.23099
+ __unnamed_array_storage.239.26594
+ __unnamed_array_storage.251.26599
+ __unnamed_array_storage.254.26593
+ __unnamed_array_storage.26670
+ __unnamed_array_storage.29868
+ __unnamed_array_storage.55286
+ __unnamed_array_storage.56829
+ __unnamed_array_storage.60263
+ _audit_stringCoreAnalytics.36703
+ _audit_stringCoreHAP.29872
+ _audit_stringIDSFoundation.40397
+ _audit_stringUIKit.40636
+ _getAnalyticsSendEventLazySymbolLoc.ptr.36696
+ _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.40628
+ _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.40622
+ _kHMDDemoModeStatusKey
+ _logCategory._hmf_once_t0.13074
+ _logCategory._hmf_once_t0.22205
+ _logCategory._hmf_once_t0.28903
+ _logCategory._hmf_once_t0.29260
+ _logCategory._hmf_once_t0.41260
+ _logCategory._hmf_once_t0.41450
+ _logCategory._hmf_once_t0.42073
+ _logCategory._hmf_once_t0.57998
+ _logCategory._hmf_once_t1.17476
+ _logCategory._hmf_once_t1.19371
+ _logCategory._hmf_once_t1.36920
+ _logCategory._hmf_once_t1.42699
+ _logCategory._hmf_once_t1.46591
+ _logCategory._hmf_once_t1.48120
+ _logCategory._hmf_once_t1.53127
+ _logCategory._hmf_once_t14.57758
+ _logCategory._hmf_once_t15.12861
+ _logCategory._hmf_once_t16.34318
+ _logCategory._hmf_once_t16.59808
+ _logCategory._hmf_once_t19.13750
+ _logCategory._hmf_once_t19.27292
+ _logCategory._hmf_once_t2.23997
+ _logCategory._hmf_once_t2.26812
+ _logCategory._hmf_once_t2.30584
+ _logCategory._hmf_once_t20.5908
+ _logCategory._hmf_once_t22.23585
+ _logCategory._hmf_once_t24.37278
+ _logCategory._hmf_once_t25.60774
+ _logCategory._hmf_once_t27.49371
+ _logCategory._hmf_once_t27.56703
+ _logCategory._hmf_once_t28.61360
+ _logCategory._hmf_once_t3.38909
+ _logCategory._hmf_once_t3.60406
+ _logCategory._hmf_once_t31.21932
+ _logCategory._hmf_once_t31.59640
+ _logCategory._hmf_once_t318
+ _logCategory._hmf_once_t33.49647
+ _logCategory._hmf_once_t34.18946
+ _logCategory._hmf_once_t344
+ _logCategory._hmf_once_t35.35498
+ _logCategory._hmf_once_t38.8051
+ _logCategory._hmf_once_t4.1281
+ _logCategory._hmf_once_t4.5773
+ _logCategory._hmf_once_t42.55856
+ _logCategory._hmf_once_t5.17150
+ _logCategory._hmf_once_t6.31703
+ _logCategory._hmf_once_t6.34086
+ _logCategory._hmf_once_t6.53835
+ _logCategory._hmf_once_t64.55162
+ _logCategory._hmf_once_t7.24091
+ _logCategory._hmf_once_t7.48000
+ _logCategory._hmf_once_t8.34543
+ _logCategory._hmf_once_t8.44196
+ _logCategory._hmf_once_t8.47083
+ _logCategory._hmf_once_t87
+ _logCategory._hmf_once_v1.13076
+ _logCategory._hmf_once_v1.22207
+ _logCategory._hmf_once_v1.28905
+ _logCategory._hmf_once_v1.29262
+ _logCategory._hmf_once_v1.41262
+ _logCategory._hmf_once_v1.41452
+ _logCategory._hmf_once_v1.42075
+ _logCategory._hmf_once_v1.58000
+ _logCategory._hmf_once_v15.57760
+ _logCategory._hmf_once_v16.12863
+ _logCategory._hmf_once_v17.34320
+ _logCategory._hmf_once_v17.59810
+ _logCategory._hmf_once_v2.17478
+ _logCategory._hmf_once_v2.19373
+ _logCategory._hmf_once_v2.36921
+ _logCategory._hmf_once_v2.42701
+ _logCategory._hmf_once_v2.46593
+ _logCategory._hmf_once_v2.48122
+ _logCategory._hmf_once_v2.53129
+ _logCategory._hmf_once_v20.13751
+ _logCategory._hmf_once_v20.27294
+ _logCategory._hmf_once_v21.5910
+ _logCategory._hmf_once_v23.23587
+ _logCategory._hmf_once_v25.37280
+ _logCategory._hmf_once_v26.60776
+ _logCategory._hmf_once_v28.49372
+ _logCategory._hmf_once_v28.56705
+ _logCategory._hmf_once_v29.61362
+ _logCategory._hmf_once_v3.23999
+ _logCategory._hmf_once_v3.26814
+ _logCategory._hmf_once_v3.30586
+ _logCategory._hmf_once_v319
+ _logCategory._hmf_once_v32.21934
+ _logCategory._hmf_once_v32.59642
+ _logCategory._hmf_once_v34.49648
+ _logCategory._hmf_once_v345
+ _logCategory._hmf_once_v35.18948
+ _logCategory._hmf_once_v36.35500
+ _logCategory._hmf_once_v39.8052
+ _logCategory._hmf_once_v4.38911
+ _logCategory._hmf_once_v4.60408
+ _logCategory._hmf_once_v43.55858
+ _logCategory._hmf_once_v5.1282
+ _logCategory._hmf_once_v5.5775
+ _logCategory._hmf_once_v6.17152
+ _logCategory._hmf_once_v65.55164
+ _logCategory._hmf_once_v7.31705
+ _logCategory._hmf_once_v7.34088
+ _logCategory._hmf_once_v7.53837
+ _logCategory._hmf_once_v8.24093
+ _logCategory._hmf_once_v8.48002
+ _logCategory._hmf_once_v88
+ _logCategory._hmf_once_v9.34545
+ _logCategory._hmf_once_v9.44198
+ _logCategory._hmf_once_v9.47084
+ _objc_msgSend$_doorbellProfilesForAccessoryProfiles:
+ _objc_msgSend$_notifyClientsOfSupportsCompanionInitiatedObliterateUpdate
+ _objc_msgSend$accessoryDidUpdateSupportsCompanionInitiatedObliterate:
+ _objc_msgSend$addIpv4Addresses:
+ _objc_msgSend$addIpv6Addresses:
+ _objc_msgSend$addNetworkInfo:
+ _objc_msgSend$addNetworkServiceInfo:
+ _objc_msgSend$addNetworkVisibleDeviceInfos:
+ _objc_msgSend$addProximityVisibleDeviceInfos:
+ _objc_msgSend$clearIpv4Addresses
+ _objc_msgSend$clearIpv6Addresses
+ _objc_msgSend$clearNetworkInfos
+ _objc_msgSend$clearNetworkServiceInfos
+ _objc_msgSend$clearNetworkVisibleDeviceInfos
+ _objc_msgSend$clearProximityVisibleDeviceInfos
+ _objc_msgSend$didReceiveDoorbellChimeMessage:
+ _objc_msgSend$doorbellChimeProfile:didChimeWithMode:chimeDate:
+ _objc_msgSend$doorbellChimeProfile:didChimeWithMode:chimeDate:personIdentificationText:
+ _objc_msgSend$initWithDoorbellChimeProfile:
+ _objc_msgSend$ipv4AddressesAtIndex:
+ _objc_msgSend$ipv4AddressesCount
+ _objc_msgSend$ipv6AddressesAtIndex:
+ _objc_msgSend$ipv6AddressesCount
+ _objc_msgSend$networkInfoAtIndex:
+ _objc_msgSend$networkInfosCount
+ _objc_msgSend$networkServiceInfoAtIndex:
+ _objc_msgSend$networkServiceInfosCount
+ _objc_msgSend$networkVisibleDeviceInfosAtIndex:
+ _objc_msgSend$networkVisibleDeviceInfosCount
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$proximityVisibleDeviceInfosAtIndex:
+ _objc_msgSend$proximityVisibleDeviceInfosCount
+ _objc_msgSend$setBssid:
+ _objc_msgSend$setConfirmedIfaceName:
+ _objc_msgSend$setControllerSetupSessionIdentifier:
+ _objc_msgSend$setFirstCoreDataContainerSetupErrorDomainHH2:
+ _objc_msgSend$setFirstCoreDataContainerSetupUnderlyingErrorDomainHH2:
+ _objc_msgSend$setIfaceName:
+ _objc_msgSend$setLastPrimaryClientConnectMessageFailErrorDomainHH2:
+ _objc_msgSend$setLastPrimaryClientConnectMessageFailUnderlyingErrorDomainHH2:
+ _objc_msgSend$setNetworkSignatureV4:
+ _objc_msgSend$setNetworkSignatureV6:
+ _objc_msgSend$setRouterIPv4:
+ _objc_msgSend$setRouterIPv6:
+ _objc_msgSend$setSsid:
+ _objc_msgSend$setSupportsCompanionInitiatedObliterate:
+ _objc_msgSend$setSupportsCoordinationFreeDoorbellChime:
+ _objc_msgSend$supportsCompanionInitiatedObliterate
+ _objc_msgSend$supportsCoordinationFreeDoorbellChime
+ _sharedInstance.onceToken.38782
+ _sharedManager.onceToken.56846
+ _supportedValueClasses.onceToken.46869
+ _supportedValueClasses.onceToken.55128
+ _supportedValueClasses.supportedValueClasses.46871
+ _supportedValueClasses.supportedValueClasses.55129
+ _unconfigureQueue.onceToken.37285
+ _unconfigureQueue.unconfigureQueue.37287
- GCC_except_table1006
- GCC_except_table1015
- GCC_except_table10291
- GCC_except_table10293
- GCC_except_table10295
- GCC_except_table10296
- GCC_except_table10327
- GCC_except_table10329
- GCC_except_table10331
- GCC_except_table10337
- GCC_except_table10338
- GCC_except_table10339
- GCC_except_table10447
- GCC_except_table10448
- GCC_except_table10474
- GCC_except_table10476
- GCC_except_table10480
- GCC_except_table10481
- GCC_except_table10529
- GCC_except_table10555
- GCC_except_table10592
- GCC_except_table10596
- GCC_except_table10637
- GCC_except_table10638
- GCC_except_table10639
- GCC_except_table10640
- GCC_except_table10641
- GCC_except_table10642
- GCC_except_table10643
- GCC_except_table10644
- GCC_except_table10645
- GCC_except_table10646
- GCC_except_table10647
- GCC_except_table10648
- GCC_except_table10649
- GCC_except_table10650
- GCC_except_table10651
- GCC_except_table10668
- GCC_except_table10695
- GCC_except_table10803
- GCC_except_table10806
- GCC_except_table1083
- GCC_except_table1085
- GCC_except_table10870
- GCC_except_table10872
- GCC_except_table1088
- GCC_except_table10880
- GCC_except_table10886
- GCC_except_table10887
- GCC_except_table10893
- GCC_except_table10895
- GCC_except_table1090
- GCC_except_table10900
- GCC_except_table10901
- GCC_except_table10902
- GCC_except_table1092
- GCC_except_table1096
- GCC_except_table11105
- GCC_except_table11106
- GCC_except_table11259
- GCC_except_table11262
- GCC_except_table11267
- GCC_except_table11271
- GCC_except_table11277
- GCC_except_table11282
- GCC_except_table11284
- GCC_except_table11289
- GCC_except_table11290
- GCC_except_table11292
- GCC_except_table11375
- GCC_except_table11377
- GCC_except_table11396
- GCC_except_table11397
- GCC_except_table11398
- GCC_except_table11399
- GCC_except_table11404
- GCC_except_table11418
- GCC_except_table11424
- GCC_except_table11427
- GCC_except_table11429
- GCC_except_table1145
- GCC_except_table11511
- GCC_except_table11513
- GCC_except_table11516
- GCC_except_table11524
- GCC_except_table11525
- GCC_except_table11530
- GCC_except_table11536
- GCC_except_table11538
- GCC_except_table11540
- GCC_except_table11542
- GCC_except_table11544
- GCC_except_table11546
- GCC_except_table11548
- GCC_except_table11682
- GCC_except_table11738
- GCC_except_table11739
- GCC_except_table11740
- GCC_except_table11741
- GCC_except_table11752
- GCC_except_table11753
- GCC_except_table11777
- GCC_except_table11778
- GCC_except_table11831
- GCC_except_table11854
- GCC_except_table11857
- GCC_except_table11989
- GCC_except_table12101
- GCC_except_table12102
- GCC_except_table12103
- GCC_except_table12151
- GCC_except_table12152
- GCC_except_table12154
- GCC_except_table12157
- GCC_except_table12159
- GCC_except_table12161
- GCC_except_table12193
- GCC_except_table12236
- GCC_except_table12241
- GCC_except_table12244
- GCC_except_table12304
- GCC_except_table12389
- GCC_except_table12397
- GCC_except_table12450
- GCC_except_table12452
- GCC_except_table12461
- GCC_except_table12464
- GCC_except_table12484
- GCC_except_table12486
- GCC_except_table12487
- GCC_except_table1260
- GCC_except_table1281
- GCC_except_table1358
- GCC_except_table1361
- GCC_except_table1379
- GCC_except_table1514
- GCC_except_table1583
- GCC_except_table1586
- GCC_except_table1655
- GCC_except_table1657
- GCC_except_table1731
- GCC_except_table1732
- GCC_except_table1780
- GCC_except_table2009
- GCC_except_table2012
- GCC_except_table2015
- GCC_except_table2020
- GCC_except_table2024
- GCC_except_table2033
- GCC_except_table2035
- GCC_except_table2038
- GCC_except_table2048
- GCC_except_table2050
- GCC_except_table2051
- GCC_except_table2056
- GCC_except_table2057
- GCC_except_table2058
- GCC_except_table2059
- GCC_except_table2449
- GCC_except_table2454
- GCC_except_table2480
- GCC_except_table2483
- GCC_except_table2497
- GCC_except_table2535
- GCC_except_table2552
- GCC_except_table2555
- GCC_except_table2556
- GCC_except_table2559
- GCC_except_table2582
- GCC_except_table2584
- GCC_except_table2586
- GCC_except_table2588
- GCC_except_table2748
- GCC_except_table2766
- GCC_except_table2767
- GCC_except_table2829
- GCC_except_table2831
- GCC_except_table2834
- GCC_except_table2835
- GCC_except_table2859
- GCC_except_table2861
- GCC_except_table2869
- GCC_except_table2871
- GCC_except_table2878
- GCC_except_table2879
- GCC_except_table2880
- GCC_except_table2882
- GCC_except_table2883
- GCC_except_table2884
- GCC_except_table2885
- GCC_except_table2886
- GCC_except_table2938
- GCC_except_table2962
- GCC_except_table2965
- GCC_except_table2968
- GCC_except_table2974
- GCC_except_table2980
- GCC_except_table3045
- GCC_except_table3046
- GCC_except_table3091
- GCC_except_table3098
- GCC_except_table3099
- GCC_except_table3100
- GCC_except_table3103
- GCC_except_table3105
- GCC_except_table3115
- GCC_except_table3123
- GCC_except_table3124
- GCC_except_table3142
- GCC_except_table3149
- GCC_except_table3153
- GCC_except_table3156
- GCC_except_table3159
- GCC_except_table3200
- GCC_except_table3204
- GCC_except_table3208
- GCC_except_table3213
- GCC_except_table3221
- GCC_except_table3225
- GCC_except_table3234
- GCC_except_table3236
- GCC_except_table3469
- GCC_except_table3473
- GCC_except_table3477
- GCC_except_table3480
- GCC_except_table3484
- GCC_except_table3485
- GCC_except_table3488
- GCC_except_table3494
- GCC_except_table3497
- GCC_except_table3501
- GCC_except_table3526
- GCC_except_table3528
- GCC_except_table3530
- GCC_except_table3533
- GCC_except_table3534
- GCC_except_table3536
- GCC_except_table3539
- GCC_except_table3621
- GCC_except_table3638
- GCC_except_table3641
- GCC_except_table3646
- GCC_except_table3653
- GCC_except_table3706
- GCC_except_table3772
- GCC_except_table3787
- GCC_except_table3790
- GCC_except_table3883
- GCC_except_table3884
- GCC_except_table3886
- GCC_except_table3891
- GCC_except_table3895
- GCC_except_table3898
- GCC_except_table3900
- GCC_except_table3908
- GCC_except_table4108
- GCC_except_table4111
- GCC_except_table4123
- GCC_except_table4198
- GCC_except_table4217
- GCC_except_table4304
- GCC_except_table431
- GCC_except_table434
- GCC_except_table436
- GCC_except_table4407
- GCC_except_table4412
- GCC_except_table4413
- GCC_except_table442
- GCC_except_table4421
- GCC_except_table4423
- GCC_except_table444
- GCC_except_table4448
- GCC_except_table4449
- GCC_except_table4451
- GCC_except_table446
- GCC_except_table4511
- GCC_except_table4521
- GCC_except_table4586
- GCC_except_table4588
- GCC_except_table4590
- GCC_except_table4632
- GCC_except_table4633
- GCC_except_table4705
- GCC_except_table4792
- GCC_except_table4793
- GCC_except_table4799
- GCC_except_table4801
- GCC_except_table4830
- GCC_except_table4832
- GCC_except_table4851
- GCC_except_table4897
- GCC_except_table4947
- GCC_except_table5033
- GCC_except_table5053
- GCC_except_table5054
- GCC_except_table5055
- GCC_except_table5057
- GCC_except_table5060
- GCC_except_table5061
- GCC_except_table5063
- GCC_except_table5277
- GCC_except_table5283
- GCC_except_table5285
- GCC_except_table5295
- GCC_except_table5296
- GCC_except_table5543
- GCC_except_table5651
- GCC_except_table5657
- GCC_except_table5664
- GCC_except_table5669
- GCC_except_table5752
- GCC_except_table5758
- GCC_except_table5760
- GCC_except_table584
- GCC_except_table587
- GCC_except_table5898
- GCC_except_table592
- GCC_except_table595
- GCC_except_table596
- GCC_except_table6057
- GCC_except_table6058
- GCC_except_table6081
- GCC_except_table6083
- GCC_except_table6089
- GCC_except_table6097
- GCC_except_table6112
- GCC_except_table6119
- GCC_except_table6122
- GCC_except_table6136
- GCC_except_table6141
- GCC_except_table6175
- GCC_except_table618
- GCC_except_table6186
- GCC_except_table6192
- GCC_except_table6196
- GCC_except_table6209
- GCC_except_table6223
- GCC_except_table6238
- GCC_except_table6241
- GCC_except_table6246
- GCC_except_table6253
- GCC_except_table6258
- GCC_except_table6262
- GCC_except_table6290
- GCC_except_table6296
- GCC_except_table6321
- GCC_except_table6326
- GCC_except_table6330
- GCC_except_table635
- GCC_except_table6355
- GCC_except_table6359
- GCC_except_table6361
- GCC_except_table6362
- GCC_except_table6497
- GCC_except_table6503
- GCC_except_table652
- GCC_except_table6581
- GCC_except_table6603
- GCC_except_table6608
- GCC_except_table6616
- GCC_except_table6659
- GCC_except_table6661
- GCC_except_table6663
- GCC_except_table6675
- GCC_except_table6687
- GCC_except_table6714
- GCC_except_table6723
- GCC_except_table6730
- GCC_except_table6733
- GCC_except_table6736
- GCC_except_table6739
- GCC_except_table6742
- GCC_except_table6751
- GCC_except_table6761
- GCC_except_table6781
- GCC_except_table6784
- GCC_except_table6787
- GCC_except_table6790
- GCC_except_table6793
- GCC_except_table6796
- GCC_except_table6799
- GCC_except_table6802
- GCC_except_table6805
- GCC_except_table6811
- GCC_except_table6814
- GCC_except_table6817
- GCC_except_table6820
- GCC_except_table6823
- GCC_except_table6826
- GCC_except_table6829
- GCC_except_table6833
- GCC_except_table6845
- GCC_except_table6846
- GCC_except_table6855
- GCC_except_table6874
- GCC_except_table6899
- GCC_except_table691
- GCC_except_table6913
- GCC_except_table6915
- GCC_except_table6935
- GCC_except_table694
- GCC_except_table695
- GCC_except_table7072
- GCC_except_table7278
- GCC_except_table7348
- GCC_except_table7452
- GCC_except_table7457
- GCC_except_table7468
- GCC_except_table7541
- GCC_except_table7559
- GCC_except_table7565
- GCC_except_table7567
- GCC_except_table7569
- GCC_except_table7570
- GCC_except_table760
- GCC_except_table763
- GCC_except_table764
- GCC_except_table765
- GCC_except_table767
- GCC_except_table7703
- GCC_except_table7706
- GCC_except_table7716
- GCC_except_table7719
- GCC_except_table7721
- GCC_except_table7724
- GCC_except_table777
- GCC_except_table7775
- GCC_except_table778
- GCC_except_table7783
- GCC_except_table7785
- GCC_except_table7787
- GCC_except_table7789
- GCC_except_table7796
- GCC_except_table7802
- GCC_except_table7804
- GCC_except_table7806
- GCC_except_table7807
- GCC_except_table7816
- GCC_except_table7872
- GCC_except_table7874
- GCC_except_table7882
- GCC_except_table7884
- GCC_except_table7886
- GCC_except_table7888
- GCC_except_table7890
- GCC_except_table7896
- GCC_except_table7900
- GCC_except_table7912
- GCC_except_table7914
- GCC_except_table7916
- GCC_except_table7918
- GCC_except_table7937
- GCC_except_table8089
- GCC_except_table8090
- GCC_except_table8093
- GCC_except_table8095
- GCC_except_table8096
- GCC_except_table8097
- GCC_except_table8133
- GCC_except_table8136
- GCC_except_table8137
- GCC_except_table8140
- GCC_except_table8143
- GCC_except_table8144
- GCC_except_table8188
- GCC_except_table8189
- GCC_except_table8190
- GCC_except_table8197
- GCC_except_table8198
- GCC_except_table8200
- GCC_except_table8262
- GCC_except_table8263
- GCC_except_table8264
- GCC_except_table8301
- GCC_except_table8483
- GCC_except_table8484
- GCC_except_table8485
- GCC_except_table8489
- GCC_except_table8544
- GCC_except_table8565
- GCC_except_table8636
- GCC_except_table8642
- GCC_except_table8644
- GCC_except_table8646
- GCC_except_table8648
- GCC_except_table8656
- GCC_except_table8705
- GCC_except_table8706
- GCC_except_table8708
- GCC_except_table8733
- GCC_except_table8761
- GCC_except_table8919
- GCC_except_table8971
- GCC_except_table8978
- GCC_except_table8983
- GCC_except_table8988
- GCC_except_table8992
- GCC_except_table9005
- GCC_except_table9008
- GCC_except_table9011
- GCC_except_table9013
- GCC_except_table9043
- GCC_except_table9063
- GCC_except_table9064
- GCC_except_table9065
- GCC_except_table9102
- GCC_except_table9103
- GCC_except_table9107
- GCC_except_table9109
- GCC_except_table9111
- GCC_except_table9170
- GCC_except_table9197
- GCC_except_table9202
- GCC_except_table9204
- GCC_except_table9206
- GCC_except_table9208
- GCC_except_table9214
- GCC_except_table9222
- GCC_except_table9226
- GCC_except_table9229
- GCC_except_table9236
- GCC_except_table9240
- GCC_except_table9246
- GCC_except_table9252
- GCC_except_table9255
- GCC_except_table9263
- GCC_except_table9264
- GCC_except_table9277
- GCC_except_table9287
- GCC_except_table9491
- GCC_except_table9504
- GCC_except_table9553
- GCC_except_table9554
- GCC_except_table9556
- GCC_except_table9560
- GCC_except_table9568
- GCC_except_table9624
- GCC_except_table9627
- GCC_except_table9628
- GCC_except_table972
- GCC_except_table976
- GCC_except_table983
- GCC_except_table9939
- GCC_except_table9978
- GCC_except_table9991
- _CoreAnalyticsLibraryCore.frameworkLibrary.36114
- _CoreHAPLibraryCore.frameworkLibrary.29360
- _HMHomeSetPreferredPrimaryMessageKeyIdentifier
- _IDSFoundationLibraryCore.39694
- _IDSFoundationLibraryCore.frameworkLibrary.39696
- _UIKitLibrary.39925
- _UIKitLibraryCore.39921
- _UIKitLibraryCore.frameworkLibrary.39934
- __OBJC_$_CLASS_METHODS_HMAccessory(SiriEndpoint|Television|WoL|LightInternal|NetworkRouter|NetworkRouterInternal|Private|PendingConfiguration|CUPeerIdentifier|Shortcuts|Camera|CHIP|NetworkConfiguration|Light|Media)
- __OBJC_$_INSTANCE_METHODS_HMAccessory(SiriEndpoint|Television|WoL|LightInternal|NetworkRouter|NetworkRouterInternal|Private|PendingConfiguration|CUPeerIdentifier|Shortcuts|Camera|CHIP|NetworkConfiguration|Light|Media)
- __OBJC_$_PROP_LIST_HMAccessoryCapabilities.134
- __OBJC_$_PROP_LIST_HMApplicationData.11377
- __OBJC_$_PROP_LIST_HMResidentCapabilities.198
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.777
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.779
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.787
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.789
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.782
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.790
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.786
- ___22-[HMHome _mergeRooms:]_block_invoke.762
- ___22-[HMHome _mergeRooms:]_block_invoke.763
- ___22-[HMHome _mergeRooms:]_block_invoke_2.767
- ___22-[HMHome _mergeRooms:]_block_invoke_3.768
- ___22-[HMHome _mergeUsers:]_block_invoke.808
- ___22-[HMHome _mergeUsers:]_block_invoke.809
- ___22-[HMHome _mergeUsers:]_block_invoke_2.813
- ___22-[HMHome _mergeUsers:]_block_invoke_3.814
- ___22-[HMHome _mergeZones:]_block_invoke.770
- ___22-[HMHome _mergeZones:]_block_invoke.771
- ___22-[HMHome _mergeZones:]_block_invoke_2.775
- ___22-[HMHome _mergeZones:]_block_invoke_3.776
- ___25-[HMHome _mergeTriggers:]_block_invoke.804
- ___25-[HMHome _mergeTriggers:]_block_invoke.806
- ___27-[HMHome _mergeActionSets:]_block_invoke.795
- ___27-[HMHome _mergeActionSets:]_block_invoke.796
- ___27-[HMHome _mergeActionSets:]_block_invoke_2.800
- ___27-[HMHome _mergeActionSets:]_block_invoke_3.801
- ___28-[HMHome _mergeAccessories:]_block_invoke.778
- ___28-[HMHome _mergeAccessories:]_block_invoke.779
- ___28-[HMHome _mergeAccessories:]_block_invoke_2.785
- ___29-[HMHome mergeFromNewObject:]_block_invoke.543
- ___29-[HMHome mergeFromNewObject:]_block_invoke.547
- ___29-[HMHome mergeFromNewObject:]_block_invoke.551
- ___29-[HMHome mergeFromNewObject:]_block_invoke.555
- ___29-[HMHome mergeFromNewObject:]_block_invoke.557
- ___29-[HMHome mergeFromNewObject:]_block_invoke.561
- ___29-[HMHome mergeFromNewObject:]_block_invoke.565
- ___29-[HMHome mergeFromNewObject:]_block_invoke.577
- ___29-[HMHome mergeFromNewObject:]_block_invoke.581
- ___29-[HMHome mergeFromNewObject:]_block_invoke.585
- ___29-[HMHome mergeFromNewObject:]_block_invoke.589
- ___29-[HMHome mergeFromNewObject:]_block_invoke.732
- ___29-[HMHome mergeFromNewObject:]_block_invoke.741
- ___29-[HMHome mergeFromNewObject:]_block_invoke.752
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.544
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.548
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.552
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.556
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.558
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.562
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.566
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.578
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.582
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.586
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.590
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.733
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.742
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.753
- ___29-[HMHome mergeFromNewObject:]_block_invoke_3.747
- ___29-[HMHome mergeFromNewObject:]_block_invoke_4.748
- ___29-[HMHome mergeFromNewObject:]_block_invoke_5.749
- ___29-[HMHome mergeFromNewObject:]_block_invoke_6.750
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1108
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1109
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1111
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1115
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1113
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1116
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.1114
- ___30-[HMAccessory _mergeServices:]_block_invoke.926
- ___30-[HMAccessory _mergeServices:]_block_invoke.928
- ___30-[HMHome _mergeServiceGroups:]_block_invoke.787
- ___30-[HMHome _mergeServiceGroups:]_block_invoke.788
- ___30-[HMHome _mergeServiceGroups:]_block_invoke_2.792
- ___30-[HMHome _mergeServiceGroups:]_block_invoke_3.793
- ___32-[HMHome _mergeResidentDevices:]_block_invoke.816
- ___32-[HMHome _mergeResidentDevices:]_block_invoke.817
- ___32-[HMHome _mergeResidentDevices:]_block_invoke_2.821
- ___32-[HMHome _mergeResidentDevices:]_block_invoke_3.822
- ___32-[HMService mergeFromNewObject:]_block_invoke.302
- ___32-[HMService mergeFromNewObject:]_block_invoke.304
- ___32-[HMService mergeFromNewObject:]_block_invoke.306
- ___32-[HMService mergeFromNewObject:]_block_invoke.308
- ___32-[HMService mergeFromNewObject:]_block_invoke.310
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1084
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1086
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1088
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1089
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1091
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1094
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1096
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1099
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1101
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.930
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.931
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.935
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.941
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.944
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.947
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.950
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.953
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.962
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1085
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1087
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1092
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1095
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.932
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.936
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.939
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.942
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.945
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.948
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.951
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.954
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.963
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.964
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.969
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.970
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.971
- ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.824
- ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.826
- ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.529
- ___39-[HMCharacteristic mergeFromNewObject:]_block_invoke.140
- ___39-[HMHome _mergeTriggerOwnedActionSets:]_block_invoke.802
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.792
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.794
- ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1143
- ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1145
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.828
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.829
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.830
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke_2.832
- ___43-[HMHome fetchPresenceForUsers:completion:]_block_invoke.842
- ___43-[HMHome fetchPresenceForUsers:completion:]_block_invoke.844
- ___44-[HMHome _handleAccessoryAddedNotification:]_block_invoke.913
- ___45-[HMAccessory _handleCharacteristicsUpdated:]_block_invoke.1129
- ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.701
- ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1130
- ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1131
- ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.761
- ___52-[HMHome(HMUser) _manageUsersWithCompletionHandler:]_block_invoke.1728
- ___54-[HMHome _notifyDelegateOfAccessControlUpdateForUser:]_block_invoke.946
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.623
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.624
- ___58-[HMHomeManager __resolveAccountHandle:completionHandler:]_block_invoke.688
- ___61-[HMHomeManager __removeAccountWithHandle:completionHandler:]_block_invoke.690
- ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.865
- ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.867
- ___64-[HMHome(HMMediaProfile) updateMediaPassword:completionHandler:]_block_invoke.1806
- ___65-[HMHomeManager __removeAccountWithIdentifier:completionHandler:]_block_invoke.689
- ___67-[HMHome _addEventTriggerFromResponse:withEventTrigger:completion:]_block_invoke.906
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.719
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.723
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.725
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.727
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke_2.728
- ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.845
- ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.698
- ___75-[HMHome(HMAccessory) addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.1591
- ___80-[HMDeviceSetupOperation setupSession:didReceiveExchangeData:completionHandler:]_block_invoke_2
- ___88-[HMHome(HMAccessory) addAccessoryWithAccessorySetupPayload:progress:completionHandler:]_block_invoke.1602
- ___88-[HMHome(HMAccessory) addAndSetUpNewAccessoriesWithSuggestedRoomName:completionHandler:]_block_invoke.1593
- ___88-[HMHome(HomeLocationFeedback) retrieveHomeKitLocationForFeedbackWithCompletionHandler:]_block_invoke.1891
- ___89-[HMHome(NetworkRouter) updateAccessoryNetworkProtectionGroup:protectionMode:completion:]_block_invoke.1861
- ___93-[HMHomeManager _pingDeviceWithUUID:monitor:secure:restrictToLocalNetwork:completionHandler:]_block_invoke.691
- ___Block_byref_object_copy_.14411
- ___Block_byref_object_copy_.14722
- ___Block_byref_object_copy_.21439
- ___Block_byref_object_copy_.23537
- ___Block_byref_object_copy_.27702
- ___Block_byref_object_copy_.29449
- ___Block_byref_object_copy_.36001
- ___Block_byref_object_copy_.38874
- ___Block_byref_object_copy_.60100
- ___Block_byref_object_dispose_.14412
- ___Block_byref_object_dispose_.14723
- ___Block_byref_object_dispose_.21440
- ___Block_byref_object_dispose_.23538
- ___Block_byref_object_dispose_.27703
- ___Block_byref_object_dispose_.29450
- ___Block_byref_object_dispose_.36002
- ___Block_byref_object_dispose_.38875
- ___Block_byref_object_dispose_.60101
- ___CoreAnalyticsLibraryCore_block_invoke.36115
- ___CoreHAPLibraryCore_block_invoke.29361
- ___IDSFoundationLibraryCore_block_invoke.39697
- ___UIKitLibraryCore_block_invoke.39935
- _____HMHomeManagerRegisterForNotifications_block_invoke.1399
- ___block_literal_global.101.36122
- ___block_literal_global.10283
- ___block_literal_global.1124
- ___block_literal_global.11310
- ___block_literal_global.11438
- ___block_literal_global.1180
- ___block_literal_global.12.45718
- ___block_literal_global.121.48665
- ___block_literal_global.12414
- ___block_literal_global.12554
- ___block_literal_global.12626
- ___block_literal_global.13081
- ___block_literal_global.13275
- ___block_literal_global.13840
- ___block_literal_global.14175
- ___block_literal_global.14493
- ___block_literal_global.15089
- ___block_literal_global.153
- ___block_literal_global.1610
- ___block_literal_global.16191
- ___block_literal_global.16723
- ___block_literal_global.16916
- ___block_literal_global.17.17849
- ___block_literal_global.17049
- ___block_literal_global.1716
- ___block_literal_global.17210
- ___block_literal_global.17856
- ___block_literal_global.1803
- ___block_literal_global.18511
- ___block_literal_global.18916
- ___block_literal_global.19.14160
- ___block_literal_global.19469
- ___block_literal_global.19808
- ___block_literal_global.20820
- ___block_literal_global.21477
- ___block_literal_global.21750
- ___block_literal_global.2177
- ___block_literal_global.22223
- ___block_literal_global.22440
- ___block_literal_global.22773
- ___block_literal_global.22904
- ___block_literal_global.23152
- ___block_literal_global.23402
- ___block_literal_global.23561
- ___block_literal_global.23654
- ___block_literal_global.26194
- ___block_literal_global.26327
- ___block_literal_global.26803
- ___block_literal_global.27562
- ___block_literal_global.27859
- ___block_literal_global.28208
- ___block_literal_global.28412
- ___block_literal_global.28693
- ___block_literal_global.28769
- ___block_literal_global.29658
- ___block_literal_global.30.17839
- ___block_literal_global.30.7684
- ___block_literal_global.30011
- ___block_literal_global.30283
- ___block_literal_global.31127
- ___block_literal_global.31498
- ___block_literal_global.32589
- ___block_literal_global.33.59440
- ___block_literal_global.33504
- ___block_literal_global.33736
- ___block_literal_global.33961
- ___block_literal_global.34913
- ___block_literal_global.3544
- ___block_literal_global.36
- ___block_literal_global.36109
- ___block_literal_global.36357
- ___block_literal_global.36699
- ___block_literal_global.37329
- ___block_literal_global.3747
- ___block_literal_global.38140
- ___block_literal_global.38267
- ___block_literal_global.3839
- ___block_literal_global.38545
- ___block_literal_global.39758
- ___block_literal_global.39853
- ___block_literal_global.40563
- ___block_literal_global.40753
- ___block_literal_global.41374
- ___block_literal_global.42000
- ___block_literal_global.42441
- ___block_literal_global.42760
- ___block_literal_global.43437
- ___block_literal_global.442
- ___block_literal_global.44325
- ___block_literal_global.45439
- ___block_literal_global.45730
- ___block_literal_global.45996
- ___block_literal_global.46191
- ___block_literal_global.46420
- ___block_literal_global.47129
- ___block_literal_global.47249
- ___block_literal_global.47983
- ___block_literal_global.48.46480
- ___block_literal_global.48419
- ___block_literal_global.48752
- ___block_literal_global.49666
- ___block_literal_global.5019
- ___block_literal_global.510
- ___block_literal_global.515
- ___block_literal_global.52231
- ___block_literal_global.52939
- ___block_literal_global.54207
- ___block_literal_global.5457
- ___block_literal_global.54890
- ___block_literal_global.55422
- ___block_literal_global.55734
- ___block_literal_global.5591
- ___block_literal_global.56249
- ___block_literal_global.56426
- ___block_literal_global.56792
- ___block_literal_global.57032
- ___block_literal_global.58674
- ___block_literal_global.58842
- ___block_literal_global.59180
- ___block_literal_global.59446
- ___block_literal_global.59808
- ___block_literal_global.60098
- ___block_literal_global.60393
- ___block_literal_global.6137
- ___block_literal_global.630
- ___block_literal_global.6621
- ___block_literal_global.6900
- ___block_literal_global.73.21728
- ___block_literal_global.73.36692
- ___block_literal_global.7351
- ___block_literal_global.740
- ___block_literal_global.7468
- ___block_literal_global.76.25963
- ___block_literal_global.7702
- ___block_literal_global.8165
- ___block_literal_global.844
- ___block_literal_global.849
- ___block_literal_global.8700
- ___block_literal_global.8981
- ___block_literal_global.911
- ___block_literal_global.9157
- ___block_literal_global.9585
- ___block_literal_global.977
- ___block_literal_global.979
- ___getAnalyticsSendEventLazySymbolLoc_block_invoke.36112
- ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.39930
- ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.39924
- __unnamed_array_storage.140
- __unnamed_array_storage.14428
- __unnamed_array_storage.22665
- __unnamed_array_storage.227.26110
- __unnamed_array_storage.239.26109
- __unnamed_array_storage.251.26113
- __unnamed_array_storage.254.26108
- __unnamed_array_storage.26184
- __unnamed_array_storage.29359
- __unnamed_array_storage.54327
- __unnamed_array_storage.55860
- __unnamed_array_storage.59296
- _audit_stringCoreAnalytics.36118
- _audit_stringCoreHAP.29363
- _audit_stringIDSFoundation.39699
- _audit_stringUIKit.39937
- _getAnalyticsSendEventLazySymbolLoc.ptr.36111
- _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.39929
- _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.39923
- _logCategory._hmf_once_t0.12625
- _logCategory._hmf_once_t0.21749
- _logCategory._hmf_once_t0.28411
- _logCategory._hmf_once_t0.28768
- _logCategory._hmf_once_t0.40562
- _logCategory._hmf_once_t0.40752
- _logCategory._hmf_once_t0.41373
- _logCategory._hmf_once_t0.57031
- _logCategory._hmf_once_t1.17048
- _logCategory._hmf_once_t1.18915
- _logCategory._hmf_once_t1.36333
- _logCategory._hmf_once_t1.41999
- _logCategory._hmf_once_t1.45717
- _logCategory._hmf_once_t1.47248
- _logCategory._hmf_once_t1.52230
- _logCategory._hmf_once_t14.56791
- _logCategory._hmf_once_t16.33735
- _logCategory._hmf_once_t16.58841
- _logCategory._hmf_once_t17.38132
- _logCategory._hmf_once_t19.13301
- _logCategory._hmf_once_t2.26326
- _logCategory._hmf_once_t2.30010
- _logCategory._hmf_once_t20.5590
- _logCategory._hmf_once_t22.23151
- _logCategory._hmf_once_t24.36691
- _logCategory._hmf_once_t25.59807
- _logCategory._hmf_once_t26.48499
- _logCategory._hmf_once_t27.47982
- _logCategory._hmf_once_t27.55733
- _logCategory._hmf_once_t3.38266
- _logCategory._hmf_once_t3.59439
- _logCategory._hmf_once_t31.21476
- _logCategory._hmf_once_t31.58673
- _logCategory._hmf_once_t315
- _logCategory._hmf_once_t33.48775
- _logCategory._hmf_once_t337
- _logCategory._hmf_once_t34.18510
- _logCategory._hmf_once_t35.34912
- _logCategory._hmf_once_t38.7718
- _logCategory._hmf_once_t4.1191
- _logCategory._hmf_once_t4.5456
- _logCategory._hmf_once_t42.54889
- _logCategory._hmf_once_t5.16722
- _logCategory._hmf_once_t6.31126
- _logCategory._hmf_once_t6.33503
- _logCategory._hmf_once_t6.52938
- _logCategory._hmf_once_t64.54206
- _logCategory._hmf_once_t7.23653
- _logCategory._hmf_once_t7.47128
- _logCategory._hmf_once_t8.33960
- _logCategory._hmf_once_t8.43436
- _logCategory._hmf_once_t8.46209
- _logCategory._hmf_once_t85
- _logCategory._hmf_once_v1.12627
- _logCategory._hmf_once_v1.21751
- _logCategory._hmf_once_v1.28413
- _logCategory._hmf_once_v1.28770
- _logCategory._hmf_once_v1.40564
- _logCategory._hmf_once_v1.40754
- _logCategory._hmf_once_v1.41375
- _logCategory._hmf_once_v1.57033
- _logCategory._hmf_once_v15.56793
- _logCategory._hmf_once_v17.33737
- _logCategory._hmf_once_v17.58843
- _logCategory._hmf_once_v18.38133
- _logCategory._hmf_once_v2.17050
- _logCategory._hmf_once_v2.18917
- _logCategory._hmf_once_v2.36334
- _logCategory._hmf_once_v2.42001
- _logCategory._hmf_once_v2.45719
- _logCategory._hmf_once_v2.47250
- _logCategory._hmf_once_v2.52232
- _logCategory._hmf_once_v20.13302
- _logCategory._hmf_once_v21.5592
- _logCategory._hmf_once_v23.23153
- _logCategory._hmf_once_v25.36693
- _logCategory._hmf_once_v26.59809
- _logCategory._hmf_once_v27.48500
- _logCategory._hmf_once_v28.47984
- _logCategory._hmf_once_v28.55735
- _logCategory._hmf_once_v3.26328
- _logCategory._hmf_once_v3.30012
- _logCategory._hmf_once_v316
- _logCategory._hmf_once_v32.21478
- _logCategory._hmf_once_v32.58675
- _logCategory._hmf_once_v338
- _logCategory._hmf_once_v34.48776
- _logCategory._hmf_once_v35.18512
- _logCategory._hmf_once_v36.34914
- _logCategory._hmf_once_v39.7719
- _logCategory._hmf_once_v4.38268
- _logCategory._hmf_once_v4.59441
- _logCategory._hmf_once_v43.54891
- _logCategory._hmf_once_v5.1192
- _logCategory._hmf_once_v5.5458
- _logCategory._hmf_once_v6.16724
- _logCategory._hmf_once_v65.54208
- _logCategory._hmf_once_v7.31128
- _logCategory._hmf_once_v7.33505
- _logCategory._hmf_once_v7.52940
- _logCategory._hmf_once_v8.23655
- _logCategory._hmf_once_v8.47130
- _logCategory._hmf_once_v86
- _logCategory._hmf_once_v9.33962
- _logCategory._hmf_once_v9.43438
- _logCategory._hmf_once_v9.46210
- _sharedInstance.onceToken.38139
- _sharedManager.onceToken.55877
- _supportedValueClasses.onceToken.45995
- _supportedValueClasses.onceToken.54170
- _supportedValueClasses.supportedValueClasses.45997
- _supportedValueClasses.supportedValueClasses.54171
- _unconfigureQueue.onceToken.36698
- _unconfigureQueue.unconfigureQueue.36700
CStrings:
+ "%{public}@Accessories are not supported for stereo pair as they have same serial number: %@"
+ "%{public}@Failed to unarchive pairing identity a user in the home with accessory from encoded pairing identity: %@, %@"
+ "%{public}@HM: Fetched pairing identity [%@] for a user in the home with accessory : %@"
+ "%{public}@HomeKitDaemon did not send any pairing identity a user in the home with accessory : %@"
+ "%{public}@No chime mode (%ld) or date (%@) in chime message"
+ "%{public}@No message payload for chime message"
+ "%{public}@No person identification text in spoken message, mode: %ld, date: %@"
+ "%{public}@Notified delegate: %@ of chime"
+ "%{public}@Notified delegate: %@ of chime (%ld) with person identification text"
+ "%{public}@Notifying delegate of supports companion initiated obliterate update: %@"
+ "%{public}@Notifying delegate: %@ of chime"
+ "%{public}@Notifying delegate: %@ of chime (%ld) with person identification text"
+ "%{public}@Received message to chime (mode %ld) on %@"
+ "%{public}@Sending device setup session open message"
+ "%{public}@Sending exchange data using TRSession: %@"
+ "%{public}@TRSession is unexpectedly nil"
+ "%{public}@There was an error while retrieving pairing identity for a user in the home with accessory %@ : %@"
+ "%{public}@Unknown chime mode (%ld)"
+ "%{public}@allPairingIdentitiesInRankOrderWithError returning empty array because demo mode is on."
+ "%{public}@fetchAllPairingIdentitiesWithCompletionHandler completing with empty array because demo mode is on."
+ "%{public}@pairingIdentityWithCompletionHandler completing with nil because demo mode is on."
+ "%{public}@pairingIdentityWithPrivateKey completing with nil because demo mode is on."
+ "-[HMHomeManager currentUserPairingIdentityForHomeContainingAccessoryWithUniqueIdentifier:completionHandler:]"
+ "/\x02"
+ "@\"<HMDoorbellChimeProfileDelegate>\""
+ "@\"<_HMDoorbellChimeProfileDelegate>\""
+ "@\"HMAccessoryInfoProtoAirportInfoEvent\""
+ "@32@0:8@16{_HMAccessoryCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}24"
+ "CoordinationFreeDoorbell"
+ "HM.doorbell.chime"
+ "HM.doorbell.chime.date"
+ "HM.doorbell.chime.mode"
+ "HM.doorbell.chime.personText"
+ "HMA.supportsCompanionInitiatedObliterate"
+ "HMAccessoryDiagnosticInfoProtoVisibleDeviceInfo"
+ "HMAccessoryInfoProtoAirportInfoEvent"
+ "HMAccessoryInfoProtoNetworkInfoEvent"
+ "HMAccessoryInfoProtoNetworkServiceEvent"
+ "HMAccessorySupportsCompanionInitiatedObliterateMessageKey"
+ "HMDoorbellChimeProfile"
+ "HMHM.cuacpi"
+ "HMHomePreferredResidentIDSKey"
+ "T@\"<HMDoorbellChimeProfileDelegate>\",W,V_delegate"
+ "T@\"<_HMDoorbellChimeProfileDelegate>\",W,V_delegate"
+ "T@\"HMAccessoryInfoProtoAirportInfoEvent\",&,N,V_wifiInfo"
+ "T@\"HMDoorbellChimeProfile\",R"
+ "T@\"NSData\",&,N,V_bssid"
+ "T@\"NSData\",&,N,V_ssid"
+ "T@\"NSMutableArray\",&,N,V_ipv4Addresses"
+ "T@\"NSMutableArray\",&,N,V_ipv6Addresses"
+ "T@\"NSMutableArray\",&,N,V_networkInfos"
+ "T@\"NSMutableArray\",&,N,V_networkServiceInfos"
+ "T@\"NSMutableArray\",&,N,V_networkVisibleDeviceInfos"
+ "T@\"NSMutableArray\",&,N,V_proximityVisibleDeviceInfos"
+ "T@\"NSString\",&,N,V_confirmedIfaceName"
+ "T@\"NSString\",&,N,V_controllerSetupSessionIdentifier"
+ "T@\"NSString\",&,N,V_firstCoreDataContainerSetupErrorDomainHH2"
+ "T@\"NSString\",&,N,V_firstCoreDataContainerSetupUnderlyingErrorDomainHH2"
+ "T@\"NSString\",&,N,V_ifaceName"
+ "T@\"NSString\",&,N,V_lastPrimaryClientConnectMessageFailErrorDomainHH2"
+ "T@\"NSString\",&,N,V_lastPrimaryClientConnectMessageFailUnderlyingErrorDomainHH2"
+ "T@\"NSString\",&,N,V_networkSignatureV4"
+ "T@\"NSString\",&,N,V_networkSignatureV6"
+ "T@\"NSString\",&,N,V_routerIPv4"
+ "T@\"NSString\",&,N,V_routerIPv6"
+ "T@\"NSString\",&,N,V_type"
+ "TB,N,V_isPrimary"
+ "TB,N,V_supportsCompanionInitiatedObliterate"
+ "TB,N,V_supportsCoordinationFreeDoorbellChime"
+ "TI,N,V_currentDeviceConfirmedPrimaryResidentINT"
+ "TI,N,V_numberOfTimesPrimaryClientConnectMessageFailedHH2"
+ "TI,N,V_numberOfTimesPrimaryClientConnectedHH2"
+ "TI,N,V_numberOfTimesPrimaryClientDisconnectedHH2"
+ "TI,N,V_numberOfTimesPrimaryResidentChangedHH2"
+ "Tq,N,V_firstCoreDataContainerSetupDurationMSHH2"
+ "Tq,N,V_firstCoreDataContainerSetupErrorCodeHH2"
+ "Tq,N,V_firstCoreDataContainerSetupUnderlyingErrorCodeHH2"
+ "Tq,N,V_lastPrimaryClientConnectMessageFailErrorCodeHH2"
+ "Tq,N,V_lastPrimaryClientConnectMessageFailUnderlyingErrorCodeHH2"
+ "Tq,N,V_lastPrimaryClientConnectedTimeHH2"
+ "Tq,N,V_primaryResidentElectionFirstCloudKitImportFutureResolvedMSHH2"
+ "Tq,N,V_primaryResidentElectionJoinMeshMSHH2"
+ "Tq,N,V_primaryResidentElectionModernTransportStartedFutureResolvedMSHH2"
+ "Tq,N,V_primaryResidentElectionPeerDeviceFutureResolvedMSHH2"
+ "T{_HMAccessoryCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},R,N,V_capabilities"
+ "_HMDoorbellChimeProfile"
+ "_HMDoorbellChimeProfileDelegate"
+ "_bssid"
+ "_confirmedIfaceName"
+ "_controllerSetupSessionIdentifier"
+ "_currentDeviceConfirmedPrimaryResidentINT"
+ "_doorbellProfilesForAccessoryProfiles:"
+ "_firstCoreDataContainerSetupDurationMSHH2"
+ "_firstCoreDataContainerSetupErrorCodeHH2"
+ "_firstCoreDataContainerSetupErrorDomainHH2"
+ "_firstCoreDataContainerSetupUnderlyingErrorCodeHH2"
+ "_firstCoreDataContainerSetupUnderlyingErrorDomainHH2"
+ "_handleDoorbellChimeMessage:"
+ "_handleSupportsCompanionInitiatedObliterateUpdatedMessage:"
+ "_ifaceName"
+ "_ipv4Addresses"
+ "_ipv6Addresses"
+ "_isPrimary"
+ "_lastPrimaryClientConnectMessageFailErrorCodeHH2"
+ "_lastPrimaryClientConnectMessageFailErrorDomainHH2"
+ "_lastPrimaryClientConnectMessageFailUnderlyingErrorCodeHH2"
+ "_lastPrimaryClientConnectMessageFailUnderlyingErrorDomainHH2"
+ "_lastPrimaryClientConnectedTimeHH2"
+ "_networkInfos"
+ "_networkServiceInfos"
+ "_networkSignatureV4"
+ "_networkSignatureV6"
+ "_networkVisibleDeviceInfos"
+ "_notifyClientsOfSupportsCompanionInitiatedObliterateUpdate"
+ "_numberOfTimesPrimaryClientConnectMessageFailedHH2"
+ "_numberOfTimesPrimaryClientConnectedHH2"
+ "_numberOfTimesPrimaryClientDisconnectedHH2"
+ "_numberOfTimesPrimaryResidentChangedHH2"
+ "_primaryResidentElectionFirstCloudKitImportFutureResolvedMSHH2"
+ "_primaryResidentElectionJoinMeshMSHH2"
+ "_primaryResidentElectionModernTransportStartedFutureResolvedMSHH2"
+ "_primaryResidentElectionPeerDeviceFutureResolvedMSHH2"
+ "_proximityVisibleDeviceInfos"
+ "_routerIPv4"
+ "_routerIPv6"
+ "_ssid"
+ "_supportsCompanionInitiatedObliterate"
+ "_supportsCoordinationFreeDoorbellChime"
+ "accessoryDidUpdateSupportsCompanionInitiatedObliterate:"
+ "addIpv4Addresses:"
+ "addIpv6Addresses:"
+ "addNetworkInfo:"
+ "addNetworkServiceInfo:"
+ "addNetworkVisibleDeviceInfos:"
+ "addProximityVisibleDeviceInfos:"
+ "bssid"
+ "clearIpv4Addresses"
+ "clearIpv6Addresses"
+ "clearNetworkInfos"
+ "clearNetworkServiceInfos"
+ "clearNetworkVisibleDeviceInfos"
+ "clearProximityVisibleDeviceInfos"
+ "confirmedIfaceName"
+ "controllerSetupSessionIdentifier"
+ "currentDeviceConfirmedPrimaryResidentINT"
+ "currentDeviceConfirmedPrimaryResident_INT"
+ "currentUserPairingIdentityForHomeContainingAccessoryWithUniqueIdentifier:completionHandler:"
+ "didReceiveDoorbellChimeMessage:"
+ "doorbellChimeProfile"
+ "doorbellChimeProfile:didChimeWithMode:chimeDate:"
+ "doorbellChimeProfile:didChimeWithMode:chimeDate:personIdentificationText:"
+ "firstCoreDataContainerSetupDurationMSHH2"
+ "firstCoreDataContainerSetupDurationMS_HH2"
+ "firstCoreDataContainerSetupErrorCodeHH2"
+ "firstCoreDataContainerSetupErrorCode_HH2"
+ "firstCoreDataContainerSetupErrorDomainHH2"
+ "firstCoreDataContainerSetupErrorDomain_HH2"
+ "firstCoreDataContainerSetupUnderlyingErrorCodeHH2"
+ "firstCoreDataContainerSetupUnderlyingErrorCode_HH2"
+ "firstCoreDataContainerSetupUnderlyingErrorDomainHH2"
+ "firstCoreDataContainerSetupUnderlyingErrorDomain_HH2"
+ "hasBssid"
+ "hasConfirmedIfaceName"
+ "hasControllerSetupSessionIdentifier"
+ "hasCurrentDeviceConfirmedPrimaryResidentINT"
+ "hasFirstCoreDataContainerSetupDurationMSHH2"
+ "hasFirstCoreDataContainerSetupErrorCodeHH2"
+ "hasFirstCoreDataContainerSetupErrorDomainHH2"
+ "hasFirstCoreDataContainerSetupUnderlyingErrorCodeHH2"
+ "hasFirstCoreDataContainerSetupUnderlyingErrorDomainHH2"
+ "hasIfaceName"
+ "hasIsPrimary"
+ "hasLastPrimaryClientConnectMessageFailErrorCodeHH2"
+ "hasLastPrimaryClientConnectMessageFailErrorDomainHH2"
+ "hasLastPrimaryClientConnectMessageFailUnderlyingErrorCodeHH2"
+ "hasLastPrimaryClientConnectMessageFailUnderlyingErrorDomainHH2"
+ "hasLastPrimaryClientConnectedTimeHH2"
+ "hasNetworkSignatureV4"
+ "hasNetworkSignatureV6"
+ "hasNumberOfTimesPrimaryClientConnectMessageFailedHH2"
+ "hasNumberOfTimesPrimaryClientConnectedHH2"
+ "hasNumberOfTimesPrimaryClientDisconnectedHH2"
+ "hasNumberOfTimesPrimaryResidentChangedHH2"
+ "hasPrimaryResidentElectionFirstCloudKitImportFutureResolvedMSHH2"
+ "hasPrimaryResidentElectionJoinMeshMSHH2"
+ "hasPrimaryResidentElectionModernTransportStartedFutureResolvedMSHH2"
+ "hasPrimaryResidentElectionPeerDeviceFutureResolvedMSHH2"
+ "hasRouterIPv4"
+ "hasRouterIPv6"
+ "hasSsid"
+ "hasSupportsCompanionInitiatedObliterate"
+ "hasSupportsCoordinationFreeDoorbellChime"
+ "hm.doorbell.chime"
+ "ifaceName"
+ "initWithDoorbellChimeProfile:"
+ "ipv4Addresses"
+ "ipv4AddressesAtIndex:"
+ "ipv4AddressesCount"
+ "ipv4AddressesType"
+ "ipv6Addresses"
+ "ipv6AddressesAtIndex:"
+ "ipv6AddressesCount"
+ "ipv6AddressesType"
+ "kHMDDemoModeStatusKey"
+ "lastPrimaryClientConnectMessageFailErrorCodeHH2"
+ "lastPrimaryClientConnectMessageFailErrorCode_HH2"
+ "lastPrimaryClientConnectMessageFailErrorDomainHH2"
+ "lastPrimaryClientConnectMessageFailErrorDomain_HH2"
+ "lastPrimaryClientConnectMessageFailUnderlyingErrorCodeHH2"
+ "lastPrimaryClientConnectMessageFailUnderlyingErrorCode_HH2"
+ "lastPrimaryClientConnectMessageFailUnderlyingErrorDomainHH2"
+ "lastPrimaryClientConnectMessageFailUnderlyingErrorDomain_HH2"
+ "lastPrimaryClientConnectedTimeHH2"
+ "lastPrimaryClientConnectedTime_HH2"
+ "networkInfo"
+ "networkInfoAtIndex:"
+ "networkInfoType"
+ "networkInfos"
+ "networkInfosCount"
+ "networkServiceInfo"
+ "networkServiceInfoAtIndex:"
+ "networkServiceInfoType"
+ "networkServiceInfos"
+ "networkServiceInfosCount"
+ "networkSignatureV4"
+ "networkSignatureV6"
+ "networkVisibleDeviceInfos"
+ "networkVisibleDeviceInfosAtIndex:"
+ "networkVisibleDeviceInfosCount"
+ "networkVisibleDeviceInfosType"
+ "numberOfTimesPrimaryClientConnectMessageFailedHH2"
+ "numberOfTimesPrimaryClientConnectMessageFailed_HH2"
+ "numberOfTimesPrimaryClientConnectedHH2"
+ "numberOfTimesPrimaryClientConnected_HH2"
+ "numberOfTimesPrimaryClientDisconnectedHH2"
+ "numberOfTimesPrimaryClientDisconnected_HH2"
+ "numberOfTimesPrimaryResidentChangedHH2"
+ "numberOfTimesPrimaryResidentChanged_HH2"
+ "numberWithUnsignedInt:"
+ "preferred.primary.name"
+ "primaryResidentElectionFirstCloudKitImportFutureResolvedMSHH2"
+ "primaryResidentElectionFirstCloudKitImportFutureResolvedMS_HH2"
+ "primaryResidentElectionJoinMeshMSHH2"
+ "primaryResidentElectionJoinMeshMS_HH2"
+ "primaryResidentElectionModernTransportStartedFutureResolvedMSHH2"
+ "primaryResidentElectionModernTransportStartedFutureResolvedMS_HH2"
+ "primaryResidentElectionPeerDeviceFutureResolvedMSHH2"
+ "primaryResidentElectionPeerDeviceFutureResolvedMS_HH2"
+ "proximityVisibleDeviceInfos"
+ "proximityVisibleDeviceInfosAtIndex:"
+ "proximityVisibleDeviceInfosCount"
+ "proximityVisibleDeviceInfosType"
+ "routerIPv4"
+ "routerIPv6"
+ "setBssid:"
+ "setConfirmedIfaceName:"
+ "setControllerSetupSessionIdentifier:"
+ "setCurrentDeviceConfirmedPrimaryResidentINT:"
+ "setFirstCoreDataContainerSetupDurationMSHH2:"
+ "setFirstCoreDataContainerSetupErrorCodeHH2:"
+ "setFirstCoreDataContainerSetupErrorDomainHH2:"
+ "setFirstCoreDataContainerSetupUnderlyingErrorCodeHH2:"
+ "setFirstCoreDataContainerSetupUnderlyingErrorDomainHH2:"
+ "setHasCurrentDeviceConfirmedPrimaryResidentINT:"
+ "setHasFirstCoreDataContainerSetupDurationMSHH2:"
+ "setHasFirstCoreDataContainerSetupErrorCodeHH2:"
+ "setHasFirstCoreDataContainerSetupUnderlyingErrorCodeHH2:"
+ "setHasIsPrimary:"
+ "setHasLastPrimaryClientConnectMessageFailErrorCodeHH2:"
+ "setHasLastPrimaryClientConnectMessageFailUnderlyingErrorCodeHH2:"
+ "setHasLastPrimaryClientConnectedTimeHH2:"
+ "setHasNumberOfTimesPrimaryClientConnectMessageFailedHH2:"
+ "setHasNumberOfTimesPrimaryClientConnectedHH2:"
+ "setHasNumberOfTimesPrimaryClientDisconnectedHH2:"
+ "setHasNumberOfTimesPrimaryResidentChangedHH2:"
+ "setHasPrimaryResidentElectionFirstCloudKitImportFutureResolvedMSHH2:"
+ "setHasPrimaryResidentElectionJoinMeshMSHH2:"
+ "setHasPrimaryResidentElectionModernTransportStartedFutureResolvedMSHH2:"
+ "setHasPrimaryResidentElectionPeerDeviceFutureResolvedMSHH2:"
+ "setHasSupportsCompanionInitiatedObliterate:"
+ "setHasSupportsCoordinationFreeDoorbellChime:"
+ "setIfaceName:"
+ "setIpv4Addresses:"
+ "setIpv6Addresses:"
+ "setIsPrimary:"
+ "setLastPrimaryClientConnectMessageFailErrorCodeHH2:"
+ "setLastPrimaryClientConnectMessageFailErrorDomainHH2:"
+ "setLastPrimaryClientConnectMessageFailUnderlyingErrorCodeHH2:"
+ "setLastPrimaryClientConnectMessageFailUnderlyingErrorDomainHH2:"
+ "setLastPrimaryClientConnectedTimeHH2:"
+ "setNetworkInfos:"
+ "setNetworkServiceInfos:"
+ "setNetworkSignatureV4:"
+ "setNetworkSignatureV6:"
+ "setNetworkVisibleDeviceInfos:"
+ "setNumberOfTimesPrimaryClientConnectMessageFailedHH2:"
+ "setNumberOfTimesPrimaryClientConnectedHH2:"
+ "setNumberOfTimesPrimaryClientDisconnectedHH2:"
+ "setNumberOfTimesPrimaryResidentChangedHH2:"
+ "setPrimaryResidentElectionFirstCloudKitImportFutureResolvedMSHH2:"
+ "setPrimaryResidentElectionJoinMeshMSHH2:"
+ "setPrimaryResidentElectionModernTransportStartedFutureResolvedMSHH2:"
+ "setPrimaryResidentElectionPeerDeviceFutureResolvedMSHH2:"
+ "setProximityVisibleDeviceInfos:"
+ "setRouterIPv4:"
+ "setRouterIPv6:"
+ "setSsid:"
+ "setSupportsCompanionInitiatedObliterate:"
+ "setSupportsCoordinationFreeDoorbellChime:"
+ "ssid"
+ "supportsCompanionInitiatedObliterate"
+ "supportsCoordinationFreeDoorbellChime"
+ "{?=\"accessoryAddMSHH2\"b1\"accountSettleWaitMSHH2\"b1\"controllerKeyExchangeMSHH1\"b1\"currentDeviceIDSWaitMSHH2\"b1\"eventRouterFirstEventPushMSHH2\"b1\"eventRouterServerConnectionMSHH2\"b1\"firstCoreDataContainerSetupDurationMSHH2\"b1\"firstCoreDataContainerSetupErrorCodeHH2\"b1\"firstCoreDataContainerSetupUnderlyingErrorCodeHH2\"b1\"firstCoreDataImportMSHH2\"b1\"homeManagerReadyMSHH2\"b1\"lastKnownStageErrorCode\"b1\"lastKnownStageUnderlyingErrorCode\"b1\"lastPrimaryClientConnectMessageFailErrorCodeHH2\"b1\"lastPrimaryClientConnectMessageFailUnderlyingErrorCodeHH2\"b1\"lastPrimaryClientConnectedTimeHH2\"b1\"newAccessoryTransferMSHH1\"b1\"pairingIdentityCreationMSHH2\"b1\"primaryResidentElectionFirstCloudKitImportFutureResolvedMSHH2\"b1\"primaryResidentElectionJoinMeshMSHH2\"b1\"primaryResidentElectionMSHH2\"b1\"primaryResidentElectionModernTransportStartedFutureResolvedMSHH2\"b1\"primaryResidentElectionPeerDeviceFutureResolvedMSHH2\"b1\"savedEventState\"b1\"sentinelZoneFetchMSHH1\"b1\"sessionSetupCloseMSHH1\"b1\"sessionSetupOpenMSHH1\"b1\"settingsCreationMSHH2\"b1\"siriReadyMSHH2\"b1\"totalDurationMSHH1\"b1\"totalDurationMSHH2\"b1\"version\"b1\"currentDeviceConfirmedPrimaryResidentINT\"b1\"iCloudAvailableINT\"b1\"iDSAvailableINT\"b1\"lastKnownControllerHH2Mode\"b1\"lastKnownControllerSentinelZoneExistence\"b1\"manateeAvailableINT\"b1\"networkAvailableINT\"b1\"numberOfTimesPrimaryClientConnectMessageFailedHH2\"b1\"numberOfTimesPrimaryClientConnectedHH2\"b1\"numberOfTimesPrimaryClientDisconnectedHH2\"b1\"numberOfTimesPrimaryResidentChangedHH2\"b1}"
+ "{?=\"isPrimary\"b1}"
+ "{?=\"supports2c25465bb0b47366\"b1\"supports89024c1cadcb8b00\"b1\"supports90bb069d6bx54e7\"b1\"supportsAnnounce\"b1\"supportsAssistantAccessControl\"b1\"supportsAudioReturnChannel\"b1\"supportsCaptiveNetworks\"b1\"supportsCloudDataSync\"b1\"supportsCompanionInitiatedObliterate\"b1\"supportsCompanionInitiatedRestart\"b1\"supportsCoordinationDoorbellChime\"b1\"supportsCoordinationFreeDoorbellChime\"b1\"supportsDeviceSetup\"b1\"supportsDoorbellChime\"b1\"supportsHomeHub\"b1\"supportsHomeInvitation\"b1\"supportsHomeLevelAnalyticsAndImprovementSetting\"b1\"supportsHomeLevelLocationServiceSetting\"b1\"supportsInstallManagedConfigurationProfile\"b1\"supportsKeyTransferClient\"b1\"supportsKeyTransferServer\"b1\"supportsKeychainSync\"b1\"supportsManagedConfigurationProfile\"b1\"supportsMediaActions\"b1\"supportsMessagedHomePodSettings\"b1\"supportsMultiUser\"b1\"supportsMusicAlarm\"b1\"supportsPreferredMediaUser\"b1\"supportsStandaloneMode\"b1\"supportsTargetControl\"b1\"supportsThirdPartyMusic\"b1\"supportsThreadBorderRouter\"b1\"supportsUserMediaSettings\"b1\"supportsWholeHouseAudio\"b1\"supportsf9cc0d9d6aa54e7\"b1}"
+ "{_HMAccessoryCapabilitiesStruct=\"supportsKeychainSync\"b1\"supportsDeviceSetup\"b1\"supportsKeyTransferClient\"b1\"supportsKeyTransferServer\"b1\"supportsStandaloneMode\"b1\"supportsCloudDataSync\"b1\"supportsWholeHouseAudio\"b1\"supportsAssistantAccessControl\"b1\"supportsHomeInvitation\"b1\"supportsTargetControl\"b1\"supportsMultiUser\"b1\"supportsHomeLevelLocationServiceSetting\"b1\"supportsCompanionInitiatedRestart\"b1\"supportsMusicAlarm\"b1\"supportsAnnounce\"b1\"supportsAudioAnalysis\"b1\"supportsThirdPartyMusic\"b1\"supportsPreferredMediaUser\"b1\"supportsThreadBorderRouter\"b1\"supportsDoorbellChime\"b1\"supportsUserMediaSettings\"b1\"supportsCoordinationDoorbellChime\"b1\"supportsHomeHub\"b1\"supportsAudioReturnChannel\"b1\"supportsManagedConfigurationProfile\"b1\"supportsCaptiveNetworks\"b1\"supportsMessagedHomePodSettings\"b1\"supportsMediaActions\"b1\"supportsDropIn\"b1\"supportsRMVonAppleTV\"b1\"supportsJustSiri\"b1\"supportsInstallManagedConfigurationProfile\"b1\"supportsCoordinationFreeDoorbellChime\"b1\"supportsCompanionInitiatedObliterate\"b1}"
+ "{_HMAccessoryCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"
+ "\xf0\xf0!\x12%"
- "@28@0:8@16{_HMAccessoryCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}24"
- "T{_HMAccessoryCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},R,N,V_capabilities"
- "preferred.primary.identifier"
- "{?=\"accessoryAddMSHH2\"b1\"accountSettleWaitMSHH2\"b1\"controllerKeyExchangeMSHH1\"b1\"currentDeviceIDSWaitMSHH2\"b1\"eventRouterFirstEventPushMSHH2\"b1\"eventRouterServerConnectionMSHH2\"b1\"firstCoreDataImportMSHH2\"b1\"homeManagerReadyMSHH2\"b1\"lastKnownStageErrorCode\"b1\"lastKnownStageUnderlyingErrorCode\"b1\"newAccessoryTransferMSHH1\"b1\"pairingIdentityCreationMSHH2\"b1\"primaryResidentElectionMSHH2\"b1\"savedEventState\"b1\"sentinelZoneFetchMSHH1\"b1\"sessionSetupCloseMSHH1\"b1\"sessionSetupOpenMSHH1\"b1\"settingsCreationMSHH2\"b1\"siriReadyMSHH2\"b1\"totalDurationMSHH1\"b1\"totalDurationMSHH2\"b1\"version\"b1\"iCloudAvailableINT\"b1\"iDSAvailableINT\"b1\"lastKnownControllerHH2Mode\"b1\"lastKnownControllerSentinelZoneExistence\"b1\"manateeAvailableINT\"b1\"networkAvailableINT\"b1}"
- "{?=\"supports2c25465bb0b47366\"b1\"supports89024c1cadcb8b00\"b1\"supports90bb069d6bx54e7\"b1\"supportsAnnounce\"b1\"supportsAssistantAccessControl\"b1\"supportsAudioReturnChannel\"b1\"supportsCaptiveNetworks\"b1\"supportsCloudDataSync\"b1\"supportsCompanionInitiatedRestart\"b1\"supportsCoordinationDoorbellChime\"b1\"supportsDeviceSetup\"b1\"supportsDoorbellChime\"b1\"supportsHomeHub\"b1\"supportsHomeInvitation\"b1\"supportsHomeLevelAnalyticsAndImprovementSetting\"b1\"supportsHomeLevelLocationServiceSetting\"b1\"supportsInstallManagedConfigurationProfile\"b1\"supportsKeyTransferClient\"b1\"supportsKeyTransferServer\"b1\"supportsKeychainSync\"b1\"supportsManagedConfigurationProfile\"b1\"supportsMediaActions\"b1\"supportsMessagedHomePodSettings\"b1\"supportsMultiUser\"b1\"supportsMusicAlarm\"b1\"supportsPreferredMediaUser\"b1\"supportsStandaloneMode\"b1\"supportsTargetControl\"b1\"supportsThirdPartyMusic\"b1\"supportsThreadBorderRouter\"b1\"supportsUserMediaSettings\"b1\"supportsWholeHouseAudio\"b1\"supportsf9cc0d9d6aa54e7\"b1}"
- "{_HMAccessoryCapabilitiesStruct=\"supportsKeychainSync\"b1\"supportsDeviceSetup\"b1\"supportsKeyTransferClient\"b1\"supportsKeyTransferServer\"b1\"supportsStandaloneMode\"b1\"supportsCloudDataSync\"b1\"supportsWholeHouseAudio\"b1\"supportsAssistantAccessControl\"b1\"supportsHomeInvitation\"b1\"supportsTargetControl\"b1\"supportsMultiUser\"b1\"supportsHomeLevelLocationServiceSetting\"b1\"supportsCompanionInitiatedRestart\"b1\"supportsMusicAlarm\"b1\"supportsAnnounce\"b1\"supportsAudioAnalysis\"b1\"supportsThirdPartyMusic\"b1\"supportsPreferredMediaUser\"b1\"supportsThreadBorderRouter\"b1\"supportsDoorbellChime\"b1\"supportsUserMediaSettings\"b1\"supportsCoordinationDoorbellChime\"b1\"supportsHomeHub\"b1\"supportsAudioReturnChannel\"b1\"supportsManagedConfigurationProfile\"b1\"supportsCaptiveNetworks\"b1\"supportsMessagedHomePodSettings\"b1\"supportsMediaActions\"b1\"supportsDropIn\"b1\"supportsRMVonAppleTV\"b1\"supportsJustSiri\"b1\"supportsInstallManagedConfigurationProfile\"b1}"
- "{_HMAccessoryCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"
- "\xf0\x93"

```
