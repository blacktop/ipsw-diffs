## WiFiPeerToPeer

> `/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`

```diff

-790.3.0.0.0
-  __TEXT.__text: 0x1acfc
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_methlist: 0x2adc
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x3fd7
-  __TEXT.__oslogstring: 0x683
-  __TEXT.__gcc_except_tab: 0x218
-  __TEXT.__unwind_info: 0x798
-  __TEXT.__objc_classname: 0x6b3
-  __TEXT.__objc_methname: 0x69b7
-  __TEXT.__objc_methtype: 0x157a
-  __TEXT.__objc_stubs: 0x3880
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0xac8
-  __DATA_CONST.__objc_classlist: 0x118
-  __DATA_CONST.__objc_protolist: 0xb0
+826.84.0.0.0
+  __TEXT.__text: 0x20648
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_methlist: 0x335c
+  __TEXT.__const: 0xa0
+  __TEXT.__cstring: 0x532d
+  __TEXT.__oslogstring: 0x7e2
+  __TEXT.__gcc_except_tab: 0x2fc
+  __TEXT.__unwind_info: 0x910
+  __TEXT.__objc_classname: 0x779
+  __TEXT.__objc_methname: 0x8163
+  __TEXT.__objc_methtype: 0x1c06
+  __TEXT.__objc_stubs: 0x41a0
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0xd30
+  __DATA_CONST.__objc_classlist: 0x140
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1360
-  __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0x110
-  __AUTH_CONST.__auth_got: 0x310
+  __DATA_CONST.__objc_selrefs: 0x1710
+  __DATA_CONST.__objc_protorefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0x130
+  __AUTH_CONST.__auth_got: 0x340
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x2b80
-  __AUTH_CONST.__objc_const: 0x4b20
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x370
-  __DATA.__data: 0x840
-  __DATA_DIRTY.__objc_data: 0xa50
-  __DATA_DIRTY.__bss: 0x60
+  __AUTH_CONST.__cfstring: 0x3500
+  __AUTH_CONST.__objc_const: 0x5918
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x42c
+  __DATA.__data: 0x900
+  __DATA_DIRTY.__objc_data: 0xaa0
+  __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2ED1A597-88E8-3919-98FB-30CD013F4408
-  Functions: 852
-  Symbols:   3113
-  CStrings:  2002
+  UUID: 6814065B-90CF-3B20-9B65-AFE129985166
+  Functions: 1027
+  Symbols:   3680
+  CStrings:  2422
 
Symbols:
+ +[WiFiAwareDatapathPerformanceReport performanceFor:datapathType:]
+ +[WiFiAwareDatapathPerformanceReport supportsSecureCoding]
+ +[WiFiAwareDeviceCapabilities addorUpdateAutoPairingBootstrapBlob:]
+ +[WiFiAwareDeviceCapabilities addorUpdateAutoPairingBootstrapBlob:uuid:]
+ +[WiFiAwareDeviceCapabilities addorUpdateAutoPairingBootstrapBlobForPeer:]
+ +[WiFiAwareDeviceCapabilities deleteAutoPairingBootstrapBlobForClientUUID:]
+ +[WiFiAwareDeviceCapabilities rotateAutoPairingBootstrapBlobs]
+ +[WiFiAwarePairedDeviceInfo supportsSecureCoding]
+ +[WiFiAwarePairingInfo supportsSecureCoding]
+ +[WiFiAwarePairingMetadata supportsSecureCoding]
+ +[WiFiP2PXPCConnection wifip2pExportedXPCInterfaceFor:]
+ -[AWDLTrafficRegistrationConfiguration isKnownService]
+ -[WiFiAwareDataSession connectionMode]
+ -[WiFiAwareDataSession datapathConfirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:]
+ -[WiFiAwareDataSession datapathConfirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:]
+ -[WiFiAwareDataSession pairingMetadata]
+ -[WiFiAwareDataSession pinCode]
+ -[WiFiAwareDataSession setConnectionMode:]
+ -[WiFiAwareDataSession setPairingMetadata:]
+ -[WiFiAwareDataSession setPinCode:]
+ -[WiFiAwareDatapathConfiguration connectionMode]
+ -[WiFiAwareDatapathConfiguration initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:pairingMethod:pairingCachingEnabled:pairSetupServiceSpecificInfo:connectionMode:pairingMetadata:]
+ -[WiFiAwareDatapathConfiguration pairingMetadata]
+ -[WiFiAwareDatapathConfiguration setConnectionMode:]
+ -[WiFiAwareDatapathConfiguration setPairingCachingEnabled:]
+ -[WiFiAwareDatapathConfiguration setPairingMetadata:]
+ -[WiFiAwareDatapathConfiguration setPairingMethod:]
+ -[WiFiAwareDatapathPerformanceReport .cxx_destruct]
+ -[WiFiAwareDatapathPerformanceReport copyWithZone:]
+ -[WiFiAwareDatapathPerformanceReport description]
+ -[WiFiAwareDatapathPerformanceReport durationActive]
+ -[WiFiAwareDatapathPerformanceReport encodeWithCoder:]
+ -[WiFiAwareDatapathPerformanceReport initWithCoder:]
+ -[WiFiAwareDatapathPerformanceReport initWithTimestamp:localTimestamp:throughputCeilingMbps:throughputCapacityMbps:txLatency:signalStrength:durationActive:]
+ -[WiFiAwareDatapathPerformanceReport localTimestamp]
+ -[WiFiAwareDatapathPerformanceReport signalStrength]
+ -[WiFiAwareDatapathPerformanceReport throughputCapacityMbps]
+ -[WiFiAwareDatapathPerformanceReport throughputCeilingMbps]
+ -[WiFiAwareDatapathPerformanceReport timestamp]
+ -[WiFiAwareDatapathPerformanceReport txLatency]
+ -[WiFiAwareDeviceCapabilities initWithSupportedFeatures:operatingChannel:operatingClass:supportedCipherSuites:supportsDataTransfer:supportedBands:discoveryInterfaceName:maxPeers:maxPublishers:maxSubscribers:maxDatapaths:]
+ -[WiFiAwareDeviceCapabilities maxDatapaths]
+ -[WiFiAwareDeviceCapabilities maxPeers]
+ -[WiFiAwareDeviceCapabilities maxPublishers]
+ -[WiFiAwareDeviceCapabilities maxSubscribers]
+ -[WiFiAwareDeviceCapabilities supportedFeatures]
+ -[WiFiAwareDevicesStore .cxx_destruct]
+ -[WiFiAwareDevicesStore activate]
+ -[WiFiAwareDevicesStore addPairedDeviceFor:pairedDeviceInfo:pairingKeyStoreID:completionHandler:]
+ -[WiFiAwareDevicesStore authorizeNewPairedDeviceFor:pairingKeyStoreID:storageClass:lifetime:client:completionHandler:]
+ -[WiFiAwareDevicesStore authorizeNewPairedDeviceFor:pairingKeyStoreID:storageClass:lifetime:client:error:]
+ -[WiFiAwareDevicesStore deactivate]
+ -[WiFiAwareDevicesStore delegate]
+ -[WiFiAwareDevicesStore exportedInterface]
+ -[WiFiAwareDevicesStore exportedObject]
+ -[WiFiAwareDevicesStore init]
+ -[WiFiAwareDevicesStore pairedDeviceAdded:]
+ -[WiFiAwareDevicesStore pairedDeviceChanged:]
+ -[WiFiAwareDevicesStore pairedDeviceRemoved:]
+ -[WiFiAwareDevicesStore queryPairedDevicesInfo:]
+ -[WiFiAwareDevicesStore reauthorizePairedDeviceFor:withDeviceID:]
+ -[WiFiAwareDevicesStore reauthorizePairedDeviceFor:withDeviceID:completionHandler:]
+ -[WiFiAwareDevicesStore remoteObjectInterface]
+ -[WiFiAwareDevicesStore removeAllPairedDevicesFor:completionHandler:]
+ -[WiFiAwareDevicesStore removePairedDeviceFor:withDeviceID:]
+ -[WiFiAwareDevicesStore removePairedDeviceFor:withDeviceID:completionHandler:]
+ -[WiFiAwareDevicesStore setDelegate:]
+ -[WiFiAwareDevicesStore startConnectionUsingProxy:completionHandler:]
+ -[WiFiAwareDevicesStore uninstallPairedDeviceFor:withDeviceID:]
+ -[WiFiAwareDevicesStore uninstallPairedDeviceFor:withDeviceID:completionHandler:]
+ -[WiFiAwareDevicesStore updatePairedDeviceNameFor:withDeviceID:toNewName:]
+ -[WiFiAwareDevicesStore updatePairedDeviceNameFor:withDeviceID:toNewName:completionHandler:]
+ -[WiFiAwareDiscoveryResult initWithServiceName:serviceSpecificInfo:publishID:subscribeID:publisherAddressKey:datapathSupported:datapathCipherSuite:fsdFunction:rssi:pairSetupRequired:pairingConfiguration:pairedUUID:pairedDeviceName:signature:]
+ -[WiFiAwareDiscoveryResult pairedDeviceName]
+ -[WiFiAwareDiscoveryResult pairedUUID]
+ -[WiFiAwareDiscoveryResult signature]
+ -[WiFiAwarePairedDeviceInfo .cxx_destruct]
+ -[WiFiAwarePairedDeviceInfo attributes]
+ -[WiFiAwarePairedDeviceInfo description]
+ -[WiFiAwarePairedDeviceInfo deviceID]
+ -[WiFiAwarePairedDeviceInfo encodeWithCoder:]
+ -[WiFiAwarePairedDeviceInfo initWithCoder:]
+ -[WiFiAwarePairedDeviceInfo initWithName:pairingName:vendorName:modelName:attributes:]
+ -[WiFiAwarePairedDeviceInfo initWithName:vendorID:modelName:attributes:]
+ -[WiFiAwarePairedDeviceInfo modelName]
+ -[WiFiAwarePairedDeviceInfo name]
+ -[WiFiAwarePairedDeviceInfo pairingName]
+ -[WiFiAwarePairedDeviceInfo setDeviceID:]
+ -[WiFiAwarePairedDeviceInfo setName:]
+ -[WiFiAwarePairedDeviceInfo vendorName]
+ -[WiFiAwarePairingConfiguration initWithSupportedPairSetupMethods:pairingCachingEnabled:pairingSetupMode:]
+ -[WiFiAwarePairingConfiguration pairingSetupMode]
+ -[WiFiAwarePairingConfiguration setPairingCachingEnabled:]
+ -[WiFiAwarePairingConfiguration setPairingSetupMode:]
+ -[WiFiAwarePairingConfiguration setSupportedPairSetupMethods:]
+ -[WiFiAwarePairingInfo .cxx_destruct]
+ -[WiFiAwarePairingInfo copyWithZone:]
+ -[WiFiAwarePairingInfo encodeWithCoder:]
+ -[WiFiAwarePairingInfo initWithCoder:]
+ -[WiFiAwarePairingInfo initWithPeerDeviceName:]
+ -[WiFiAwarePairingInfo peerDeviceName]
+ -[WiFiAwarePairingInfo setPeerDeviceName:]
+ -[WiFiAwarePairingMetadata .cxx_destruct]
+ -[WiFiAwarePairingMetadata bundleID]
+ -[WiFiAwarePairingMetadata copyWithZone:]
+ -[WiFiAwarePairingMetadata description]
+ -[WiFiAwarePairingMetadata encodeWithCoder:]
+ -[WiFiAwarePairingMetadata initWithBundleID:selfPairingName:peerDeviceName:storageClass:lifetime:pairingClient:]
+ -[WiFiAwarePairingMetadata initWithCoder:]
+ -[WiFiAwarePairingMetadata lifetime]
+ -[WiFiAwarePairingMetadata pairingClient]
+ -[WiFiAwarePairingMetadata peerDeviceName]
+ -[WiFiAwarePairingMetadata selfPairingName]
+ -[WiFiAwarePairingMetadata setBundleID:]
+ -[WiFiAwarePairingMetadata setLifetime:]
+ -[WiFiAwarePairingMetadata setPairingClient:]
+ -[WiFiAwarePairingMetadata setPeerDeviceName:]
+ -[WiFiAwarePairingMetadata setSelfPairingName:]
+ -[WiFiAwarePairingMetadata setStorageClass:]
+ -[WiFiAwarePairingMetadata storageClass]
+ -[WiFiAwarePublishConfiguration allowedDeviceIDs]
+ -[WiFiAwarePublishConfiguration pairingMetadata]
+ -[WiFiAwarePublishConfiguration setAllowedDeviceIDs:]
+ -[WiFiAwarePublishConfiguration setPairingMetadata:]
+ -[WiFiAwarePublishConfiguration setTimeoutAfterSeconds:]
+ -[WiFiAwarePublishConfiguration timeoutAfterSeconds]
+ -[WiFiAwarePublishDatapathConfiguration connectionMode]
+ -[WiFiAwarePublishDatapathConfiguration initWithServiceType:securityConfiguration:connectionMode:]
+ -[WiFiAwarePublishDatapathConfiguration setConnectionMode:]
+ -[WiFiAwarePublishDatapathConfiguration setSecurityConfiguration:]
+ -[WiFiAwarePublishDatapathSecurityConfiguration initWithPairingConfiguration:usingPairingDelegate:usingPairingNFCTag:]
+ -[WiFiAwarePublishDatapathSecurityConfiguration initWithPairingConfiguration:usingPairingDelegate:usingPairingPINCode:]
+ -[WiFiAwarePublishDatapathSecurityConfiguration initWithPairingConfiguration:usingPairingDelegate:usingPairingPassphrase:]
+ -[WiFiAwarePublishDatapathSecurityConfiguration initWithPairingConfiguration:usingPairingDelegate:usingPairingQRCodeInformation:]
+ -[WiFiAwarePublishDatapathSecurityConfiguration pairingNFCTag]
+ -[WiFiAwarePublishDatapathSecurityConfiguration pairingPINCode]
+ -[WiFiAwarePublishDatapathSecurityConfiguration pairingPassphrase]
+ -[WiFiAwarePublishDatapathSecurityConfiguration pairingQRCodeInformation]
+ -[WiFiAwarePublishDatapathSecurityConfiguration pinCode]
+ -[WiFiAwarePublishDatapathSecurityConfiguration setPairingConfiguration:]
+ -[WiFiAwarePublishDatapathSecurityConfiguration setPinCode:]
+ -[WiFiAwarePublisher publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:]
+ -[WiFiAwarePublisher publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:]
+ -[WiFiAwarePublisher publishPairingApprovalForSubscriber:withPairingMethod:pairingSetupApprovalCompletion:]
+ -[WiFiAwarePublisher publishPairingApprovalForSubscriber:withPairingMethod:pairingSetupApprovalHandler:]
+ -[WiFiAwarePublisher updateTimeout:completionHandler:]
+ -[WiFiAwareSubscribeConfiguration allowedDeviceIDs]
+ -[WiFiAwareSubscribeConfiguration discoveryMode]
+ -[WiFiAwareSubscribeConfiguration initWithServiceName:discoveryMode:]
+ -[WiFiAwareSubscribeConfiguration setAllowedDeviceIDs:]
+ -[WiFiAwareSubscribeConfiguration setDiscoveryMode:]
+ -[WiFiAwareSubscribeConfiguration setTimeoutAfterSeconds:]
+ -[WiFiAwareSubscribeConfiguration timeoutAfterSeconds]
+ -[WiFiAwareSubscriber updateTimeout:completionHandler:]
+ GCC_except_table13
+ GCC_except_table19
+ GCC_except_table23
+ GCC_except_table27
+ GCC_except_table31
+ GCC_except_table43
+ _.str.26
+ _.str.27
+ _.str.28
+ _.str.29
+ _.str.30
+ _.str.31
+ _.str.4
+ _.str.5
+ _.str.6
+ _.str.7
+ _.str.8
+ _AWDLTrafficRegistrationServiceMacVirtualDisplay
+ _AWDLTrafficRegistrationServiceSpatialStreaming
+ _CFStringCompare
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_WiFiAwareDatapathPerformanceReport
+ _OBJC_CLASS_$_WiFiAwareDevicesStore
+ _OBJC_CLASS_$_WiFiAwarePairedDeviceInfo
+ _OBJC_CLASS_$_WiFiAwarePairingInfo
+ _OBJC_CLASS_$_WiFiAwarePairingMetadata
+ _OBJC_IVAR_$_WiFiAwareDataSession._connectionMode
+ _OBJC_IVAR_$_WiFiAwareDataSession._pairingMetadata
+ _OBJC_IVAR_$_WiFiAwareDataSession._pinCode
+ _OBJC_IVAR_$_WiFiAwareDatapathConfiguration._connectionMode
+ _OBJC_IVAR_$_WiFiAwareDatapathConfiguration._pairingMetadata
+ _OBJC_IVAR_$_WiFiAwareDatapathPerformanceReport._durationActive
+ _OBJC_IVAR_$_WiFiAwareDatapathPerformanceReport._localTimestamp
+ _OBJC_IVAR_$_WiFiAwareDatapathPerformanceReport._signalStrength
+ _OBJC_IVAR_$_WiFiAwareDatapathPerformanceReport._throughputCapacityMbps
+ _OBJC_IVAR_$_WiFiAwareDatapathPerformanceReport._throughputCeilingMbps
+ _OBJC_IVAR_$_WiFiAwareDatapathPerformanceReport._timestamp
+ _OBJC_IVAR_$_WiFiAwareDatapathPerformanceReport._txLatency
+ _OBJC_IVAR_$_WiFiAwareDeviceCapabilities._maxDatapaths
+ _OBJC_IVAR_$_WiFiAwareDeviceCapabilities._maxPeers
+ _OBJC_IVAR_$_WiFiAwareDeviceCapabilities._maxPublishers
+ _OBJC_IVAR_$_WiFiAwareDeviceCapabilities._maxSubscribers
+ _OBJC_IVAR_$_WiFiAwareDeviceCapabilities._supportedFeatures
+ _OBJC_IVAR_$_WiFiAwareDevicesStore._delegate
+ _OBJC_IVAR_$_WiFiAwareDevicesStore._xpcConnection
+ _OBJC_IVAR_$_WiFiAwareDiscoveryResult._pairedDeviceName
+ _OBJC_IVAR_$_WiFiAwareDiscoveryResult._pairedUUID
+ _OBJC_IVAR_$_WiFiAwareDiscoveryResult._signature
+ _OBJC_IVAR_$_WiFiAwarePairedDeviceInfo._attributes
+ _OBJC_IVAR_$_WiFiAwarePairedDeviceInfo._deviceID
+ _OBJC_IVAR_$_WiFiAwarePairedDeviceInfo._modelName
+ _OBJC_IVAR_$_WiFiAwarePairedDeviceInfo._name
+ _OBJC_IVAR_$_WiFiAwarePairedDeviceInfo._pairingName
+ _OBJC_IVAR_$_WiFiAwarePairedDeviceInfo._vendorName
+ _OBJC_IVAR_$_WiFiAwarePairingConfiguration._pairingSetupMode
+ _OBJC_IVAR_$_WiFiAwarePairingInfo._peerDeviceName
+ _OBJC_IVAR_$_WiFiAwarePairingMetadata._bundleID
+ _OBJC_IVAR_$_WiFiAwarePairingMetadata._lifetime
+ _OBJC_IVAR_$_WiFiAwarePairingMetadata._pairingClient
+ _OBJC_IVAR_$_WiFiAwarePairingMetadata._peerDeviceName
+ _OBJC_IVAR_$_WiFiAwarePairingMetadata._selfPairingName
+ _OBJC_IVAR_$_WiFiAwarePairingMetadata._storageClass
+ _OBJC_IVAR_$_WiFiAwarePublishConfiguration._allowedDeviceIDs
+ _OBJC_IVAR_$_WiFiAwarePublishConfiguration._pairingMetadata
+ _OBJC_IVAR_$_WiFiAwarePublishConfiguration._timeoutAfterSeconds
+ _OBJC_IVAR_$_WiFiAwarePublishDatapathConfiguration._connectionMode
+ _OBJC_IVAR_$_WiFiAwarePublishDatapathSecurityConfiguration._pairingNFCTag
+ _OBJC_IVAR_$_WiFiAwarePublishDatapathSecurityConfiguration._pairingPINCode
+ _OBJC_IVAR_$_WiFiAwarePublishDatapathSecurityConfiguration._pairingPassphrase
+ _OBJC_IVAR_$_WiFiAwarePublishDatapathSecurityConfiguration._pairingQRCodeInformation
+ _OBJC_IVAR_$_WiFiAwarePublishDatapathSecurityConfiguration._pinCode
+ _OBJC_IVAR_$_WiFiAwareSubscribeConfiguration._allowedDeviceIDs
+ _OBJC_IVAR_$_WiFiAwareSubscribeConfiguration._discoveryMode
+ _OBJC_IVAR_$_WiFiAwareSubscribeConfiguration._timeoutAfterSeconds
+ _OBJC_METACLASS_$_WiFiAwareDatapathPerformanceReport
+ _OBJC_METACLASS_$_WiFiAwareDevicesStore
+ _OBJC_METACLASS_$_WiFiAwarePairedDeviceInfo
+ _OBJC_METACLASS_$_WiFiAwarePairingInfo
+ _OBJC_METACLASS_$_WiFiAwarePairingMetadata
+ __OBJC_$_CLASS_METHODS_WiFiAwareDatapathPerformanceReport
+ __OBJC_$_CLASS_METHODS_WiFiAwarePairedDeviceInfo
+ __OBJC_$_CLASS_METHODS_WiFiAwarePairingInfo
+ __OBJC_$_CLASS_METHODS_WiFiAwarePairingMetadata
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareDatapathPerformanceReport
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwarePairedDeviceInfo
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwarePairingInfo
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwarePairingMetadata
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareDatapathPerformanceReport
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareDevicesStore
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePairedDeviceInfo
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePairingInfo
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePairingMetadata
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareDatapathPerformanceReport
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareDevicesStore
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePairedDeviceInfo
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePairingInfo
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePairingMetadata
+ __OBJC_$_PROP_LIST_WiFiAwareDatapathPerformanceReport
+ __OBJC_$_PROP_LIST_WiFiAwareDevicesStore
+ __OBJC_$_PROP_LIST_WiFiAwarePairedDeviceInfo
+ __OBJC_$_PROP_LIST_WiFiAwarePairingInfo
+ __OBJC_$_PROP_LIST_WiFiAwarePairingMetadata
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WiFiAwareDatapathXPCDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WiFiAwarePublisherXPCDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WiFiAwarePairedDevicesXPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WiFiAwarePairedDevicesXPCDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiAwarePairedDevicesXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiAwarePairedDevicesXPCDelegate
+ __OBJC_$_PROTOCOL_REFS_WiFiAwarePairedDevicesXPC
+ __OBJC_$_PROTOCOL_REFS_WiFiAwarePairedDevicesXPCDelegate
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareDatapathPerformanceReport
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareDevicesStore
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePairedDeviceInfo
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePairingInfo
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePairingMetadata
+ __OBJC_CLASS_RO_$_WiFiAwareDatapathPerformanceReport
+ __OBJC_CLASS_RO_$_WiFiAwareDevicesStore
+ __OBJC_CLASS_RO_$_WiFiAwarePairedDeviceInfo
+ __OBJC_CLASS_RO_$_WiFiAwarePairingInfo
+ __OBJC_CLASS_RO_$_WiFiAwarePairingMetadata
+ __OBJC_LABEL_PROTOCOL_$_WiFiAwarePairedDevicesXPC
+ __OBJC_LABEL_PROTOCOL_$_WiFiAwarePairedDevicesXPCDelegate
+ __OBJC_METACLASS_RO_$_WiFiAwareDatapathPerformanceReport
+ __OBJC_METACLASS_RO_$_WiFiAwareDevicesStore
+ __OBJC_METACLASS_RO_$_WiFiAwarePairedDeviceInfo
+ __OBJC_METACLASS_RO_$_WiFiAwarePairingInfo
+ __OBJC_METACLASS_RO_$_WiFiAwarePairingMetadata
+ __OBJC_PROTOCOL_$_WiFiAwarePairedDevicesXPC
+ __OBJC_PROTOCOL_$_WiFiAwarePairedDevicesXPCDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_WiFiAwarePairedDevicesXPC
+ __OBJC_PROTOCOL_REFERENCE_$_WiFiAwarePairedDevicesXPCDelegate
+ ___104-[WiFiAwarePublisher publishPairingApprovalForSubscriber:withPairingMethod:pairingSetupApprovalHandler:]_block_invoke
+ ___106-[WiFiAwareDevicesStore authorizeNewPairedDeviceFor:pairingKeyStoreID:storageClass:lifetime:client:error:]_block_invoke
+ ___107-[WiFiAwarePublisher publishPairingApprovalForSubscriber:withPairingMethod:pairingSetupApprovalCompletion:]_block_invoke
+ ___115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.120
+ ___115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.123
+ ___118-[WiFiAwareDevicesStore authorizeNewPairedDeviceFor:pairingKeyStoreID:storageClass:lifetime:client:completionHandler:]_block_invoke
+ ___48-[WiFiAwareDevicesStore queryPairedDevicesInfo:]_block_invoke
+ ___54-[WiFiAwarePublisher updateTimeout:completionHandler:]_block_invoke
+ ___55+[WiFiP2PXPCConnection wifip2pExportedXPCInterfaceFor:]_block_invoke
+ ___55-[WiFiAwareSubscriber updateTimeout:completionHandler:]_block_invoke
+ ___60-[WiFiAwareDevicesStore removePairedDeviceFor:withDeviceID:]_block_invoke
+ ___63-[WiFiAwareDevicesStore uninstallPairedDeviceFor:withDeviceID:]_block_invoke
+ ___65-[WiFiAwareDevicesStore reauthorizePairedDeviceFor:withDeviceID:]_block_invoke
+ ___66+[WiFiAwareDatapathPerformanceReport performanceFor:datapathType:]_block_invoke
+ ___68-[WiFiAwareDataSession generateDiversifiedPINWithCompletionHandler:]_block_invoke
+ ___68-[WiFiAwareDataSession generateDiversifiedPINWithCompletionHandler:]_block_invoke_2
+ ___68-[WiFiAwareDataSession generateDiversifiedPINWithCompletionHandler:]_block_invoke_3
+ ___69-[WiFiAwareDevicesStore removeAllPairedDevicesFor:completionHandler:]_block_invoke
+ ___74-[WiFiAwareDevicesStore updatePairedDeviceNameFor:withDeviceID:toNewName:]_block_invoke
+ ___77-[WiFiAwarePublisher generateDiversifiedPINForDataSession:completionHandler:]_block_invoke
+ ___77-[WiFiAwarePublisher generateDiversifiedPINForDataSession:completionHandler:]_block_invoke_2
+ ___77-[WiFiAwarePublisher generateDiversifiedPINForDataSession:completionHandler:]_block_invoke_3
+ ___78-[WiFiAwareDevicesStore removePairedDeviceFor:withDeviceID:completionHandler:]_block_invoke
+ ___79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.137
+ ___81-[WiFiAwareDevicesStore uninstallPairedDeviceFor:withDeviceID:completionHandler:]_block_invoke
+ ___83-[WiFiAwareDevicesStore reauthorizePairedDeviceFor:withDeviceID:completionHandler:]_block_invoke
+ ___92-[WiFiAwareDevicesStore updatePairedDeviceNameFor:withDeviceID:toNewName:completionHandler:]_block_invoke
+ ___97-[WiFiAwareDevicesStore addPairedDeviceFor:pairedDeviceInfo:pairingKeyStoreID:completionHandler:]_block_invoke
+ ___block_descriptor_40_e43_v24?0"<WiFiAwarePublisherXPC>"8?<v?q>16l
+ ___block_descriptor_40_e44_v24?0"<WiFiAwareSubscriberXPC>"8?<v?q>16l
+ ___block_descriptor_40_e8_32bs_e19_v24?0q8"NSData"16ls32l8
+ ___block_descriptor_40_e8_32bs_e33_v24?0q8"WiFiAwarePairingInfo"16ls32l8
+ ___block_descriptor_40_e8_32bs_e37_v16?0"<WiFiAwarePairedDevicesXPC>"8ls32l8
+ ___block_descriptor_41_e40_v24?0"<WiFiP2PXPCProtocol>"8?<v?>16l
+ ___block_descriptor_48_e8_32bs40bs_e21_v24?0q8"NSString"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e37_v16?0"<WiFiAwarePairedDevicesXPC>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e18_v16?0"NSString"8lr40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e37_v16?0"<WiFiAwarePairedDevicesXPC>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e20_v24?0Q8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs_e37_v16?0"<WiFiAwarePairedDevicesXPC>"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e37_v16?0"<WiFiAwarePairedDevicesXPC>"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48bs_e37_v16?0"<WiFiAwarePairedDevicesXPC>"8ls32l8s40l8s48l8
+ ___block_literal_global.105
+ ___block_literal_global.117
+ ___block_literal_global.160
+ ___block_literal_global.162
+ ___block_literal_global.200
+ ___block_literal_global.254
+ ___block_literal_global.351
+ ___block_literal_global.595
+ ___block_literal_global.597
+ __os_log_impl
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _objc_msgSend$addPairedDeviceFor:pairedDeviceInfo:pairingKeyStoreID:completionHandler:
+ _objc_msgSend$allowedDeviceIDs
+ _objc_msgSend$arrayWithObjects:
+ _objc_msgSend$authorizeNewPairedDeviceFor:pairingKeyStoreID:storageClass:lifetime:client:completionHandler:
+ _objc_msgSend$bundleID
+ _objc_msgSend$connectionMode
+ _objc_msgSend$containsObject:
+ _objc_msgSend$createPairingStore:
+ _objc_msgSend$dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:
+ _objc_msgSend$dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$deviceAdded:
+ _objc_msgSend$deviceChanged:
+ _objc_msgSend$deviceRemoved:
+ _objc_msgSend$discoveryMode
+ _objc_msgSend$durationActive
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$generateDiversifiedPINWithCompletionHandler:
+ _objc_msgSend$getDiversifiedPinCodeForDataSession:completionHandler:
+ _objc_msgSend$initWithBundleID:selfPairingName:peerDeviceName:storageClass:lifetime:pairingClient:
+ _objc_msgSend$initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:pairingMethod:pairingCachingEnabled:pairSetupServiceSpecificInfo:connectionMode:pairingMetadata:
+ _objc_msgSend$initWithName:pairingName:vendorName:modelName:attributes:
+ _objc_msgSend$initWithPeerDeviceName:
+ _objc_msgSend$initWithServiceName:serviceSpecificInfo:publishID:subscribeID:publisherAddressKey:datapathSupported:datapathCipherSuite:fsdFunction:rssi:pairSetupRequired:pairingConfiguration:pairedUUID:pairedDeviceName:signature:
+ _objc_msgSend$initWithServiceType:securityConfiguration:connectionMode:
+ _objc_msgSend$initWithSupportedFeatures:operatingChannel:operatingClass:supportedCipherSuites:supportsDataTransfer:supportedBands:discoveryInterfaceName:maxPeers:maxPublishers:maxSubscribers:maxDatapaths:
+ _objc_msgSend$initWithSupportedPairSetupMethods:pairingCachingEnabled:pairingSetupMode:
+ _objc_msgSend$initWithTimestamp:localTimestamp:throughputCeilingMbps:throughputCapacityMbps:txLatency:signalStrength:durationActive:
+ _objc_msgSend$initWithUnsignedLong:
+ _objc_msgSend$isKnownService
+ _objc_msgSend$lifetime
+ _objc_msgSend$localTimestamp
+ _objc_msgSend$maxDatapaths
+ _objc_msgSend$maxPeers
+ _objc_msgSend$maxPublishers
+ _objc_msgSend$maxSubscribers
+ _objc_msgSend$pairedDeviceName
+ _objc_msgSend$pairedUUID
+ _objc_msgSend$pairingClient
+ _objc_msgSend$pairingMetadata
+ _objc_msgSend$pairingPINCode
+ _objc_msgSend$pairingPassphrase
+ _objc_msgSend$pairingRequestApprovalRequiredByPublisher:forSubscriber:withPairingMethod:pairingSetupApprovalCompletion:
+ _objc_msgSend$pairingRequestApprovalRequiredByPublisher:forSubscriber:withPairingMethod:pairingSetupApprovalHandler:
+ _objc_msgSend$pairingSetupMode
+ _objc_msgSend$peerDeviceName
+ _objc_msgSend$publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:
+ _objc_msgSend$publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:
+ _objc_msgSend$queryPairedDevicesInfo:
+ _objc_msgSend$queryPerformanceReportFor:datapathType:completion:
+ _objc_msgSend$reauthorizePairedDeviceFor:withDeviceID:completionHandler:
+ _objc_msgSend$removeAllPairedDevicesFor:completionHandler:
+ _objc_msgSend$removePairedDeviceFor:withDeviceID:completionHandler:
+ _objc_msgSend$removePairedDeviceFor:withDeviceID:uninstall:completionHandler:
+ _objc_msgSend$selfPairingName
+ _objc_msgSend$setAllowedDeviceIDs:
+ _objc_msgSend$setConnectionMode:
+ _objc_msgSend$setDeviceID:
+ _objc_msgSend$setDiscoveryMode:
+ _objc_msgSend$setPairingMetadata:
+ _objc_msgSend$setPairingSetupMode:
+ _objc_msgSend$setPinCode:
+ _objc_msgSend$setTimeoutAfterSeconds:
+ _objc_msgSend$signalStrength
+ _objc_msgSend$signature
+ _objc_msgSend$storageClass
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$supportedFeatures
+ _objc_msgSend$throughputCapacityMbps
+ _objc_msgSend$throughputCeilingMbps
+ _objc_msgSend$timeoutAfterSeconds
+ _objc_msgSend$timestamp
+ _objc_msgSend$txLatency
+ _objc_msgSend$uninstallPairedDeviceFor:withDeviceID:completionHandler:
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSend$updatePairedDeviceNameFor:withDeviceID:toNewName:completionHandler:
+ _objc_msgSend$updateTimeout:completionHandler:
+ _protocol_isEqual
- +[WiFiAwareDeviceCapabilities addAutoPairingBootstrapBlobForPeer:]
- -[WiFiAwareDatapathConfiguration initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:pairingMethod:pairingCachingEnabled:pairSetupServiceSpecificInfo:]
- -[WiFiAwareDeviceCapabilities initWithOperatingChannel:operatingClass:supportedCipherSuites:supportsDataTransfer:supportedBands:discoveryInterfaceName:]
- -[WiFiAwareDiscoveryResult initWithServiceName:serviceSpecificInfo:publishID:subscribeID:publisherAddressKey:datapathSupported:datapathCipherSuite:fsdFunction:rssi:pairSetupRequired:pairingConfiguration:]
- -[WiFiAwareSubscribeConfiguration setTimeoutAfter:]
- -[WiFiAwareSubscribeConfiguration timeoutAfter]
- GCC_except_table38
- _.str.10
- _.str.11
- _.str.12
- _.str.13
- _.str.14
- _OBJC_IVAR_$_WiFiAwareSubscribeConfiguration._timeoutAfter
- ___115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.104
- ___115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.107
- ___79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.133
- ___block_literal_global.150
- ___block_literal_global.152
- ___block_literal_global.196
- ___block_literal_global.250
- ___block_literal_global.347
- ___block_literal_global.589
- ___block_literal_global.591
- ___block_literal_global.96
- ___block_literal_global.99
- _objc_msgSend$initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:pairingMethod:pairingCachingEnabled:pairSetupServiceSpecificInfo:
- _objc_msgSend$initWithOperatingChannel:operatingClass:supportedCipherSuites:supportsDataTransfer:supportedBands:discoveryInterfaceName:
- _objc_msgSend$initWithServiceName:serviceSpecificInfo:publishID:subscribeID:publisherAddressKey:datapathSupported:datapathCipherSuite:fsdFunction:rssi:pairSetupRequired:pairingConfiguration:
- _objc_msgSend$setTimeoutAfter:
- _objc_msgSend$timeoutAfter
CStrings:
+ "%@ is currently using Mac Virtual Display."
+ "%@ is currently using Spatial Streaming."
+ "%@ unable to connect to Mac Virtual Display while active with another device."
+ "%@ unable to connect to Spatial Streaming while active with another device."
+ "%s (%s:%u) DeviceID: %llu, Error: %@"
+ "%s (%s:%u) Error: %@"
+ "-[WiFiAwareDevicesStore authorizeNewPairedDeviceFor:pairingKeyStoreID:storageClass:lifetime:client:error:]_block_invoke"
+ "-[WiFiAwareDevicesStore reauthorizePairedDeviceFor:withDeviceID:]_block_invoke"
+ "-[WiFiAwareDevicesStore removePairedDeviceFor:withDeviceID:]_block_invoke"
+ "-[WiFiAwareDevicesStore uninstallPairedDeviceFor:withDeviceID:]_block_invoke"
+ "-[WiFiAwareDevicesStore updatePairedDeviceNameFor:withDeviceID:toNewName:]_block_invoke"
+ "0000000"
+ "<WiFiAwareDatapathConfiguration: discoveryResult=%@, serviceType=%s, passphrase=%@, pmk=%@, pmkID=%@, serviceSpecificInfo=%@, internetSharing=%@, pairingMethod=%s, pairingCaching=%s, pairSetupServiceSpecificInfo=%@>, connectionMode=%ld, pairingMetadata=%@"
+ "<WiFiAwareDeviceCapabilities supportedFeatures=%@ operatingChannel=%@, operatingClass=%@, supportedBands=%u, supportedCipherSuites=%@, maxPeers=%ld, maxPublishers=%ld, maxSubscribers=%ld, maxDatapaths=%ld>"
+ "<WiFiAwareDiscoveryResult: name=%@, serviceSpecificInfo=%@, publishID=%u, publisherAddress=%@, datapath=%s, security=%s, cipherSuite=%s, FSD=%s, rssi=%ld, pairSetup=%s, pairing=%@, UUID=%@>, pairedDeviceName=%@ Signature=0x%02lx [%ld]"
+ "<WiFiAwarePairing supportedMethods=%@, caching=%s, setupMode=%s>"
+ "<WiFiAwarePublishConfiguration: serviceName=%@, serviceSpecificInfo=%@, furtherServiceDiscoveryRequired=%s, jumboMessages=%s, dataConfig=%@, fastDiscovery=%@, internetSharing=%@>, allowedDeviceIDs=%@, timeoutAfter=%ld, channelInfo=%@, cc=%@, multicastConfiguration=%@, pairingMetadata=%@>"
+ "<WiFiAwarePublishDatapathConfiguration: serviceType=%s, securityConfig=%@, serviceSpecificInfo=%@, connectionMode=%s"
+ "<WiFiAwareSubscribeConfiguration: name=%@, serviceSpecificInfo=%@, fastDiscoveryConfiguration=%@, multicastAddress=%@, timeoutAfter=%ld>, allowedDeviceIDs=%@, channelInfo=%@, cc=%@, multicastConfiguration=%@>, discoveryMode=%ld"
+ "@\"<WiFiAwareDevicesStoreDelegate>\""
+ "@\"NSDate\""
+ "@\"NSDictionary\""
+ "@\"NSSet\""
+ "@\"NSUUID\""
+ "@\"WiFiAwarePairingMetadata\""
+ "@108@0:8@16q24@32@40@48@56@64q72B80@84q92@100"
+ "@112@0:8@16@24C32C36@40B48q52q60q68B76@80@88@96q104"
+ "@28@0:8C16q20"
+ "@32@0:8@16Q24"
+ "@32@0:8@16q24"
+ "@36@0:8@16B24q28"
+ "@40@0:8@16@24@32"
+ "@40@0:8@16Q24@32"
+ "@40@0:8q16@24q32"
+ "@56@0:8@16@24@32@40@48"
+ "@64@0:8@16@24@32q40d48q56"
+ "@72@0:8@16@24@32@40@48@56d64"
+ "@96@0:8@16@24@32@40B48C52@56q64q72q80q88"
+ "Any"
+ "Any Pairing (Paired + Pairable)"
+ "MacVirtualDisplay"
+ "Optimizing Mac Virtual Display connection."
+ "Optimizing Spatial Streaming connection."
+ "Paired Only"
+ "Process %{public}s is missing entitlement required for peer to peer Wi-Fi access: <key>com.apple.wifip2pd</key><true/> OR <key>com.apple.developer.wifi-aware</key><true/>"
+ "Publish"
+ "Q64@0:8@16@24q32d40q48^@56"
+ "Requesting for pair setup approval for subscriber with pairing method: %ld"
+ "Storing PIN code"
+ "Subscribe"
+ "T@\"<WiFiAwareDevicesStoreDelegate>\",W,N,V_delegate"
+ "T@\"NSArray\",C,N,V_supportedPairSetupMethods"
+ "T@\"NSData\",R,N,V_localTimestamp"
+ "T@\"NSData\",R,N,V_pairingNFCTag"
+ "T@\"NSData\",R,N,V_pairingQRCodeInformation"
+ "T@\"NSDate\",R,N,V_timestamp"
+ "T@\"NSDictionary\",R,C,N,V_attributes"
+ "T@\"NSDictionary\",R,N,V_txLatency"
+ "T@\"NSNumber\",R,N,V_signalStrength"
+ "T@\"NSNumber\",R,N,V_throughputCapacityMbps"
+ "T@\"NSNumber\",R,N,V_throughputCeilingMbps"
+ "T@\"NSSet\",C,N,V_allowedDeviceIDs"
+ "T@\"NSSet\",R,N,V_supportedFeatures"
+ "T@\"NSString\",&,N,V_pinCode"
+ "T@\"NSString\",C,N,V_bundleID"
+ "T@\"NSString\",C,N,V_name"
+ "T@\"NSString\",C,N,V_peerDeviceName"
+ "T@\"NSString\",C,N,V_pinCode"
+ "T@\"NSString\",C,N,V_selfPairingName"
+ "T@\"NSString\",R,C,N,V_modelName"
+ "T@\"NSString\",R,C,N,V_pairingName"
+ "T@\"NSString\",R,C,N,V_vendorName"
+ "T@\"NSString\",R,N,V_pairedDeviceName"
+ "T@\"NSString\",R,N,V_pairingPINCode"
+ "T@\"NSString\",R,N,V_pairingPassphrase"
+ "T@\"NSUUID\",R,N,V_pairedUUID"
+ "T@\"WiFiAwarePairingConfiguration\",C,N,V_pairingConfiguration"
+ "T@\"WiFiAwarePairingMetadata\",C,N,V_pairingMetadata"
+ "T@\"WiFiAwarePublishDatapathSecurityConfiguration\",&,N,V_securityConfiguration"
+ "TB,N,V_pairingCachingEnabled"
+ "TQ,N,V_deviceID"
+ "TQ,N,V_timeoutAfterSeconds"
+ "Td,N,V_lifetime"
+ "Td,R,N,V_durationActive"
+ "To connect Mac Virtual Display to another device, disconnect the previous one first."
+ "To connect Spatial Streaming to another device, disconnect the previous one first."
+ "To use AirPlay, disconnect Mac Virtual Display first."
+ "To use AirPlay, disconnect Spatial Streaming first."
+ "To use Continuity Camera, disconnect Mac Virtual Display first."
+ "To use Continuity Camera, disconnect Spatial Streaming first."
+ "To use Mac Virtual Display, disconnect AirPlay first."
+ "To use Mac Virtual Display, disconnect Continuity Camera first."
+ "To use Mac Virtual Display, disconnect Sidecar first."
+ "To use Mac Virtual Display, disconnect Spatial Streaming first."
+ "To use Mac Virtual Display, disconnect iPhone Mirroring first."
+ "To use Sidecar, disconnect Mac Virtual Display first."
+ "To use Sidecar, disconnect Spatial Streaming first."
+ "To use Spatial Streaming, disconnect AirPlay first."
+ "To use Spatial Streaming, disconnect Continuity Camera first."
+ "To use Spatial Streaming, disconnect Mac Virtual Display first."
+ "To use Spatial Streaming, disconnect Sidecar first."
+ "To use Spatial Streaming, disconnect iPhone Mirroring first."
+ "To use iPhone Mirroring, disconnect Mac Virtual Display first."
+ "To use iPhone Mirroring, disconnect Spatial Streaming first."
+ "Tq,N,V_connectionMode"
+ "Tq,N,V_discoveryMode"
+ "Tq,N,V_pairingClient"
+ "Tq,N,V_pairingMethod"
+ "Tq,N,V_pairingSetupMode"
+ "Tq,N,V_storageClass"
+ "Tq,R,N,V_maxDatapaths"
+ "Tq,R,N,V_maxPeers"
+ "Tq,R,N,V_maxPublishers"
+ "Tq,R,N,V_maxSubscribers"
+ "Tq,R,N,V_signature"
+ "Unable to Connect to Mac Virtual Display"
+ "Unable to Connect to Spatial Streaming"
+ "Unable to connect while the other device is active in a different Mac Virtual Display session."
+ "Unable to connect while the other device is active in a different Spatial Streaming session."
+ "Unable to connect while the other device is running Mac Virtual Display."
+ "Unable to connect while the other device is running Spatial Streaming."
+ "WiFiAwareDataRequest.connectionMode"
+ "WiFiAwareDataRequest.pairingMetadata"
+ "WiFiAwareDatapathPerformanceReport"
+ "WiFiAwareDatapathPerformanceReport.durationActive"
+ "WiFiAwareDatapathPerformanceReport.localTimestamp"
+ "WiFiAwareDatapathPerformanceReport.signalStrength"
+ "WiFiAwareDatapathPerformanceReport.throughputCapacity"
+ "WiFiAwareDatapathPerformanceReport.throughputCeiling"
+ "WiFiAwareDatapathPerformanceReport.timestamp"
+ "WiFiAwareDatapathPerformanceReport.txLatency"
+ "WiFiAwareDatapathPerformanceReport:\n \tTimestamp: %@\n \tLocalTimestamp: %@ \n \tThroughput Ceiling: %@ Mbps \n \tThroughput Capacity: %@ Mbps \n \tTx Latency: %@ \n \tSignal Strength: %@ \n \tDuration Active: %.2f s"
+ "WiFiAwareDeviceCapabilities.maxDatapaths"
+ "WiFiAwareDeviceCapabilities.maxPeers"
+ "WiFiAwareDeviceCapabilities.maxPublishers"
+ "WiFiAwareDeviceCapabilities.maxSubscribers"
+ "WiFiAwareDeviceCapabilities.supportedFeatures"
+ "WiFiAwareDevicesStore"
+ "WiFiAwareDevicesStore.m"
+ "WiFiAwareDiscoveryResult.pairedDeviceName"
+ "WiFiAwareDiscoveryResult.pairedUUID"
+ "WiFiAwareDiscoveryResult.signature"
+ "WiFiAwarePairedDeviceInfo"
+ "WiFiAwarePairedDeviceInfo(deviceID: %llu, name: %@, pairingName: %@, vendorName: %@, modelName: %@, attributes: %@)"
+ "WiFiAwarePairedDeviceInfo.attributes"
+ "WiFiAwarePairedDeviceInfo.deviceID"
+ "WiFiAwarePairedDeviceInfo.modelName"
+ "WiFiAwarePairedDeviceInfo.name"
+ "WiFiAwarePairedDeviceInfo.pairingName"
+ "WiFiAwarePairedDeviceInfo.vendorName"
+ "WiFiAwarePairedDevicesXPC"
+ "WiFiAwarePairedDevicesXPCDelegate"
+ "WiFiAwarePairingConfiguration.pairingSetupMode"
+ "WiFiAwarePairingInfo"
+ "WiFiAwarePairingMetadata"
+ "WiFiAwarePairingMetadata(bundleID: %@, selfPairingName: %@, peerDeviceName: %@)"
+ "WiFiAwarePairingMetadata.bundldeID"
+ "WiFiAwarePairingMetadata.lifetime"
+ "WiFiAwarePairingMetadata.pairingClient"
+ "WiFiAwarePairingMetadata.peerDeviceName"
+ "WiFiAwarePairingMetadata.selfPairingName"
+ "WiFiAwarePairingMetadata.storageClass"
+ "WiFiAwarePublishConfiguration.allowedDeviceIDs"
+ "WiFiAwarePublishConfiguration.pairingMetadata"
+ "WiFiAwarePublishConfiguration.timeout"
+ "WiFiAwareSubscribeConfiguration.allowedDeviceIDs"
+ "WiFiAwareSubscribeConfiguration.discoveryMode"
+ "[WiFiPeerToPeer] FAILED to complete operation within %{public}.1fs, continuing"
+ "_allowedDeviceIDs"
+ "_attributes"
+ "_bundleID"
+ "_connectionMode"
+ "_deviceID"
+ "_discoveryMode"
+ "_durationActive"
+ "_lifetime"
+ "_localTimestamp"
+ "_maxDatapaths"
+ "_maxPeers"
+ "_maxPublishers"
+ "_maxSubscribers"
+ "_modelName"
+ "_name"
+ "_pairedDeviceName"
+ "_pairedUUID"
+ "_pairingClient"
+ "_pairingMetadata"
+ "_pairingNFCTag"
+ "_pairingName"
+ "_pairingPINCode"
+ "_pairingPassphrase"
+ "_pairingQRCodeInformation"
+ "_pairingSetupMode"
+ "_peerDeviceName"
+ "_pinCode"
+ "_selfPairingName"
+ "_signalStrength"
+ "_signature"
+ "_storageClass"
+ "_supportedFeatures"
+ "_throughputCapacityMbps"
+ "_throughputCeilingMbps"
+ "_timeoutAfterSeconds"
+ "_timestamp"
+ "_txLatency"
+ "_vendorName"
+ "addPairedDeviceFor:pairedDeviceInfo:pairingKeyStoreID:completionHandler:"
+ "addorUpdateAutoPairingBootstrapBlob:"
+ "addorUpdateAutoPairingBootstrapBlob:uuid:"
+ "addorUpdateAutoPairingBootstrapBlobForPeer:"
+ "allowedDeviceIDs"
+ "arrayWithObjects:"
+ "ask for consent"
+ "attributes"
+ "authorizeNewPairedDeviceFor:pairingKeyStoreID:storageClass:lifetime:client:completionHandler:"
+ "authorizeNewPairedDeviceFor:pairingKeyStoreID:storageClass:lifetime:client:error:"
+ "auto-reply"
+ "bundleID"
+ "com.apple.developer.wifi-aware"
+ "com.apple.wifip2p.WiFiAwarePairedDevicesManager"
+ "connectionMode"
+ "containsObject:"
+ "createPairingStore:"
+ "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:"
+ "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
+ "datapathConfirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:"
+ "datapathConfirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
+ "deactivate"
+ "decodeDoubleForKey:"
+ "decodeObjectForKey:"
+ "deleteAutoPairingBootstrapBlobForClientUUID:"
+ "deviceAdded:"
+ "deviceChanged:"
+ "deviceID"
+ "deviceRemoved:"
+ "discoveryMode"
+ "durationActive"
+ "encodeDouble:forKey:"
+ "generateDiversifiedPINForDataSession: No completion handler provided!"
+ "getDiversifiedPinCodeForDataSession:completionHandler:"
+ "initWithBundleID:selfPairingName:peerDeviceName:storageClass:lifetime:pairingClient:"
+ "initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:pairingMethod:pairingCachingEnabled:pairSetupServiceSpecificInfo:connectionMode:pairingMetadata:"
+ "initWithName:pairingName:vendorName:modelName:attributes:"
+ "initWithName:vendorID:modelName:attributes:"
+ "initWithPairingConfiguration:usingPairingDelegate:usingPairingNFCTag:"
+ "initWithPairingConfiguration:usingPairingDelegate:usingPairingPINCode:"
+ "initWithPairingConfiguration:usingPairingDelegate:usingPairingPassphrase:"
+ "initWithPairingConfiguration:usingPairingDelegate:usingPairingQRCodeInformation:"
+ "initWithPeerDeviceName:"
+ "initWithServiceName:discoveryMode:"
+ "initWithServiceName:serviceSpecificInfo:publishID:subscribeID:publisherAddressKey:datapathSupported:datapathCipherSuite:fsdFunction:rssi:pairSetupRequired:pairingConfiguration:pairedUUID:pairedDeviceName:signature:"
+ "initWithServiceType:securityConfiguration:connectionMode:"
+ "initWithSupportedFeatures:operatingChannel:operatingClass:supportedCipherSuites:supportsDataTransfer:supportedBands:discoveryInterfaceName:maxPeers:maxPublishers:maxSubscribers:maxDatapaths:"
+ "initWithSupportedPairSetupMethods:pairingCachingEnabled:pairingSetupMode:"
+ "initWithTimestamp:localTimestamp:throughputCeilingMbps:throughputCapacityMbps:txLatency:signalStrength:durationActive:"
+ "initWithUnsignedLong:"
+ "isKnownService"
+ "lifetime"
+ "localTimestamp"
+ "maxDatapaths"
+ "maxPeers"
+ "maxPublishers"
+ "maxSubscribers"
+ "modelName"
+ "name"
+ "pairedDeviceAdded:"
+ "pairedDeviceChanged:"
+ "pairedDeviceName"
+ "pairedDeviceRemoved:"
+ "pairedUUID"
+ "pairingClient"
+ "pairingMetadata"
+ "pairingNFCTag"
+ "pairingName"
+ "pairingPINCode"
+ "pairingPassphrase"
+ "pairingQRCodeInformation"
+ "pairingRequestApprovalRequiredByPublisher:forSubscriber:withPairingMethod:pairingSetupApprovalCompletion:"
+ "pairingRequestApprovalRequiredByPublisher:forSubscriber:withPairingMethod:pairingSetupApprovalHandler:"
+ "pairingSetupMode"
+ "peerDeviceName"
+ "performanceFor:datapathType:"
+ "pinCode"
+ "publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:"
+ "publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
+ "publishPairingApprovalForSubscriber:withPairingMethod:pairingSetupApprovalCompletion:"
+ "publishPairingApprovalForSubscriber:withPairingMethod:pairingSetupApprovalHandler:"
+ "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:"
+ "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
+ "queryPairedDevicesInfo:"
+ "queryPerformanceReportFor:datapathType:completion:"
+ "reauthorizePairedDeviceFor:withDeviceID:"
+ "reauthorizePairedDeviceFor:withDeviceID:completionHandler:"
+ "removeAllPairedDevicesFor:completionHandler:"
+ "removePairedDeviceFor:withDeviceID:"
+ "removePairedDeviceFor:withDeviceID:completionHandler:"
+ "removePairedDeviceFor:withDeviceID:uninstall:completionHandler:"
+ "rotateAutoPairingBootstrapBlobs"
+ "selfPairingName"
+ "setAllowedDeviceIDs:"
+ "setBundleID:"
+ "setConnectionMode:"
+ "setDeviceID:"
+ "setDiscoveryMode:"
+ "setLifetime:"
+ "setName:"
+ "setPairingClient:"
+ "setPairingConfiguration:"
+ "setPairingMetadata:"
+ "setPairingSetupMode:"
+ "setPeerDeviceName:"
+ "setPinCode:"
+ "setSecurityConfiguration:"
+ "setSelfPairingName:"
+ "setStorageClass:"
+ "setSupportedPairSetupMethods:"
+ "setTimeoutAfterSeconds:"
+ "signalStrength"
+ "signature"
+ "spatialStreaming"
+ "storageClass"
+ "stringWithString:"
+ "supportedFeatures"
+ "throughputCapacityMbps"
+ "throughputCeilingMbps"
+ "timeoutAfterSeconds"
+ "timestamp"
+ "txLatency"
+ "uninstallPairedDeviceFor:withDeviceID:"
+ "uninstallPairedDeviceFor:withDeviceID:completionHandler:"
+ "unsignedLongValue"
+ "updatePairedDeviceNameFor:withDeviceID:toNewName:"
+ "updatePairedDeviceNameFor:withDeviceID:toNewName:completionHandler:"
+ "updateTimeout:completionHandler:"
+ "v16@?0@\"<WiFiAwarePairedDevicesXPC>\"8"
+ "v24@0:8@\"WiFiAwarePairedDeviceInfo\"16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@0:8@?<v@?q@\"NSString\">16"
+ "v24@?0Q8@\"NSError\"16"
+ "v24@?0q8@\"NSData\"16"
+ "v24@?0q8@\"NSString\"16"
+ "v24@?0q8@\"WiFiAwarePairingInfo\"16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"WiFiAwarePublisherDataSessionHandle\"16@?<v@?q@\"NSString\">24"
+ "v36@0:8C16q20@?28"
+ "v36@0:8C16q20@?<v@?@\"WiFiAwareDatapathPerformanceReport\">28"
+ "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"WiFiAwarePublishServiceSpecificInfo\"16q24@?<v@?q@\"NSData\">32"
+ "v40@0:8@\"WiFiAwarePublishServiceSpecificInfo\"16q24@?<v@?q@\"WiFiAwarePairingInfo\">32"
+ "v40@0:8@\"WiFiMACAddress\"16@\"WiFiAwarePublishDatapathServiceSpecificInfo\"24@\"NSUUID\"32"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16Q24@?32"
+ "v44@0:8@\"NSString\"16Q24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@\"WiFiAwarePublisherDataSessionHandle\"16I24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"28@\"NSUUID\"36"
+ "v44@0:8@16I24@28@36"
+ "v44@0:8@16Q24B32@?36"
+ "v48@0:8@\"NSString\"16@\"WiFiAwarePairedDeviceInfo\"24@\"NSUUID\"32@?<v@?Q@\"NSError\">40"
+ "v48@0:8@\"NSString\"16Q24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"WiFiMACAddress\"16@\"WiFiAwarePublishDatapathServiceSpecificInfo\"24@\"NSUUID\"32Q40"
+ "v48@0:8@16@24@32@?40"
+ "v48@0:8@16@24@32Q40"
+ "v48@0:8@16Q24@32@?40"
+ "v52@0:8@\"WiFiAwarePublisherDataSessionHandle\"16I24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"28@\"NSUUID\"36Q44"
+ "v52@0:8@16I24@28@36Q44"
+ "v64@0:8@\"NSString\"16@\"NSUUID\"24q32d40q48@?<v@?Q@\"NSError\">56"
+ "v64@0:8@16@24q32d40q48@?56"
+ "vendorName"
+ "wifip2pExportedXPCInterfaceFor:"
+ "\xc1Q"
- "<WiFiAwareDatapathConfiguration: discoveryResult=%@, serviceType=%s, passphrase=%@, pmk=%@, pmkID=%@, serviceSpecificInfo=%@, internetSharing=%@, pairingMethod=%s, pairingCaching=%s, pairSetupServiceSpecificInfo=%@>"
- "<WiFiAwareDeviceCapabilities operatingChannel=%@, operatingClass=%@, supportedBands=%u, supportedCipherSuites=%@>"
- "<WiFiAwareDiscoveryResult: name=%@, serviceSpecificInfo=%@, publishID=%u, publisherAddress=%@, datapath=%s, security=%s, cipherSuite=%s, FSD=%s, rssi=%ld, pairSetup=%s, pairing=%@>"
- "<WiFiAwarePairing supportedMethods=%@, caching=%s>"
- "<WiFiAwarePublishConfiguration: serviceName=%@, serviceSpecificInfo=%@, furtherServiceDiscoveryRequired=%s, jumboMessages=%s, dataConfig=%@, fastDiscovery=%@, internetSharing=%@, channelInfo=%@, cc=%@, multicastConfiguration=%@>"
- "<WiFiAwarePublishDatapathConfiguration: serviceType=%s, securityConfig=%@, serviceSpecificInfo=%@>"
- "<WiFiAwareSubscribeConfiguration: name=%@, serviceSpecificInfo=%@, fastDiscoveryConfiguration=%@, multicastAddress=%@ timeoutAfter=%ld, channelInfo=%@, cc=%@, multicastConfiguration=%@>"
- "@56@0:8@16@24@32B40C44@48"
- "@88@0:8@16@24C32C36@40B48q52q60q68B76@80"
- "@92@0:8@16q24@32@40@48@56@64q72B80@84"
- "Process %{public}s is missing entitlement required for peer to peer Wi-Fi access: <key>com.apple.wifip2pd</key><true/>"
- "T@\"NSArray\",R,N,V_supportedPairSetupMethods"
- "T@\"WiFiAwarePublishDatapathSecurityConfiguration\",R,N,V_securityConfiguration"
- "TB,R,N,V_pairingCachingEnabled"
- "TB,R,V_pairingCachingEnabled"
- "Tq,N,V_timeoutAfter"
- "Tq,R,V_pairingMethod"
- "_timeoutAfter"
- "addAutoPairingBootstrapBlobForPeer:"
- "initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:pairingMethod:pairingCachingEnabled:pairSetupServiceSpecificInfo:"
- "initWithOperatingChannel:operatingClass:supportedCipherSuites:supportsDataTransfer:supportedBands:discoveryInterfaceName:"
- "initWithServiceName:serviceSpecificInfo:publishID:subscribeID:publisherAddressKey:datapathSupported:datapathCipherSuite:fsdFunction:rssi:pairSetupRequired:pairingConfiguration:"
- "setTimeoutAfter:"
- "timeoutAfter"
- "\xc1!"

```
