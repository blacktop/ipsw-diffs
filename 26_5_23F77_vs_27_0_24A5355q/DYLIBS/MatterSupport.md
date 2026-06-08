## MatterSupport

> `/System/Library/Frameworks/MatterSupport.framework/MatterSupport`

```diff

-1418.6.20.0.0
-  __TEXT.__text: 0x2f7bc
-  __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_methlist: 0x1cc0
-  __TEXT.__const: 0x3240
-  __TEXT.__swift5_typeref: 0x985
+1468.5.0.0.6
+  __TEXT.__text: 0x338b0
+  __TEXT.__objc_methlist: 0x1f18
+  __TEXT.__const: 0x32c7
+  __TEXT.__swift5_typeref: 0x97d
   __TEXT.__constg_swiftt: 0x74c
   __TEXT.__swift5_reflstr: 0x2ea
   __TEXT.__swift5_fieldmd: 0x78c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__cstring: 0x1159
+  __TEXT.__cstring: 0x143c
   __TEXT.__swift5_proto: 0x2c0
   __TEXT.__swift5_types: 0xb8
-  __TEXT.__swift5_capture: 0x254
-  __TEXT.__oslogstring: 0x1d44
+  __TEXT.__swift5_capture: 0x264
+  __TEXT.__oslogstring: 0x432f
   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x48
-  __TEXT.__gcc_except_tab: 0x168
-  __TEXT.__unwind_info: 0x1000
-  __TEXT.__eh_frame: 0x1178
-  __TEXT.__objc_classname: 0x756
-  __TEXT.__objc_methname: 0x2d19
-  __TEXT.__objc_methtype: 0xe20
-  __TEXT.__objc_stubs: 0x1cc0
-  __DATA_CONST.__got: 0x368
-  __DATA_CONST.__const: 0x2f8
-  __DATA_CONST.__objc_classlist: 0x110
+  __TEXT.__swift_as_cont: 0x7c
+  __TEXT.__gcc_except_tab: 0xe4
+  __TEXT.__unwind_info: 0x1018
+  __TEXT.__eh_frame: 0x1148
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x350
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x128
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x908
+  __DATA_CONST.__objc_selrefs: 0xa08
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0xd8
-  __AUTH_CONST.__auth_got: 0x840
-  __AUTH_CONST.__const: 0x1a00
-  __AUTH_CONST.__cfstring: 0x11e0
-  __AUTH_CONST.__objc_const: 0x3770
-  __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0x938
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__got: 0x380
+  __AUTH_CONST.__const: 0x1a48
+  __AUTH_CONST.__cfstring: 0x1420
+  __AUTH_CONST.__objc_const: 0x3ac0
+  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__auth_got: 0x900
+  __AUTH.__objc_data: 0x9d8
   __AUTH.__data: 0x358
-  __DATA.__objc_ivar: 0x140
-  __DATA.__data: 0x13d0
-  __DATA.__bss: 0x5870
+  __DATA.__objc_ivar: 0x158
+  __DATA.__data: 0x14e0
+  __DATA.__bss: 0x5890
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
   - /System/Library/PrivateFrameworks/HomeKitFeatures.framework/HomeKitFeatures
-  - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2DC6038F-6DCE-35A7-8AE9-55914FD03C94
-  Functions: 1366
-  Symbols:   2284
-  CStrings:  1078
+  UUID: 235CAFAB-4614-3738-AD09-2C805907ADB5
+  Functions: 1412
+  Symbols:   2529
+  CStrings:  634
 
Symbols:
+ +[MTSNetworkCredentialManager logCategory]
+ +[MTSNetworkCredentialManager threadCredentialManagementEndpoint:]
+ +[MTSNetworkCredentialManager threadCredentialManagementImplicitlyEnabledForDeviceType:]
+ +[MTSNetworkCredentialManager threadCredentialManagementSupportedForCommissionee:]
+ +[MTSThreadNetworkCredential generateDataset]
+ +[MTSThreadNetworkCredential supportsSecureCoding]
+ -[MTSDevicePairing hmf_appendAttributeDescriptionsToString:options:]
+ -[MTSDevicePairingEcosystem hmf_appendAttributeDescriptionsToString:options:]
+ -[MTSDevicePairingFabric hmf_appendAttributeDescriptionsToString:options:]
+ -[MTSDevicePairingVendor hmf_appendAttributeDescriptionsToString:options:]
+ -[MTSNetworkCredentialManager .cxx_destruct]
+ -[MTSNetworkCredentialManager dealloc]
+ -[MTSNetworkCredentialManager initWithServerProxy:]
+ -[MTSNetworkCredentialManager init]
+ -[MTSNetworkCredentialManager retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]
+ -[MTSNetworkCredentialManager retrievePreferredThreadCredentialsWithCompletionHandler:]
+ -[MTSNetworkCredentialManager serverProxy]
+ -[MTSNetworkCredentialManager setThreadCredentialManagementEnabled:forPairingWithUUID:completionHandler:]
+ -[MTSSystemCommissionerPairing hmf_appendAttributeDescriptionsToString:options:]
+ -[MTSSystemCommissionerPairing initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:threadCredentialManagementEnabled:]
+ -[MTSSystemCommissionerPairing threadCredentialManagementEnabled]
+ -[MTSSystemCommissionerPairingManager pairWithSetupPayload:skipMFIPrompt:completionHandler:]
+ -[MTSThreadNetworkCredential .cxx_destruct]
+ -[MTSThreadNetworkCredential borderAgentEUI]
+ -[MTSThreadNetworkCredential borderAgentID]
+ -[MTSThreadNetworkCredential copyWithZone:]
+ -[MTSThreadNetworkCredential dataset]
+ -[MTSThreadNetworkCredential encodeWithCoder:]
+ -[MTSThreadNetworkCredential hash]
+ -[MTSThreadNetworkCredential initWithCoder:]
+ -[MTSThreadNetworkCredential initWithDataset:borderAgentEUI:borderAgentID:]
+ -[MTSThreadNetworkCredential isEqual:]
+ -[MTSXPCClientProxy hasThreadCredentialsEntitlement]
+ -[MTSXPCClientProxy hmf_appendAttributeDescriptionsToString:options:]
+ -[MTSXPCClientProxy pairSystemCommissionerWithSetupPayload:skipMFIPrompt:completionHandler:]
+ -[MTSXPCClientProxy retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]
+ -[MTSXPCClientProxy updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]
+ -[MTSXPCConnection hmf_appendAttributeDescriptionsToString:options:]
+ -[MTSXPCServer clientProxy:pairSystemCommissionerWithSetupPayload:skipMFIPrompt:completionHandler:]
+ -[MTSXPCServer clientProxy:retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]
+ -[MTSXPCServer clientProxy:updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]
+ -[MTSXPCServer networkCredentialServer]
+ -[MTSXPCServer setNetworkCredentialServer:]
+ -[MTSXPCServerProxy pairSystemCommissionerWithSetupPayload:skipMFIPrompt:completionHandler:]
+ -[MTSXPCServerProxy retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]
+ -[MTSXPCServerProxy updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]
+ GCC_except_table370
+ GCC_except_table445
+ GCC_except_table446
+ GCC_except_table484
+ GCC_except_table486
+ GCC_except_table487
+ GCC_except_table488
+ _HMFFormatAttributeValue
+ _MTSXPCEntitlementNameThreadCredentials
+ _OBJC_CLASS_$_MTSNetworkCredentialManager
+ _OBJC_CLASS_$_MTSThreadNetworkCredential
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_IVAR_$_MTSNetworkCredentialManager._serverProxy
+ _OBJC_IVAR_$_MTSSystemCommissionerPairing._threadCredentialManagementEnabled
+ _OBJC_IVAR_$_MTSThreadNetworkCredential._borderAgentEUI
+ _OBJC_IVAR_$_MTSThreadNetworkCredential._borderAgentID
+ _OBJC_IVAR_$_MTSThreadNetworkCredential._dataset
+ _OBJC_IVAR_$_MTSXPCServer._networkCredentialServer
+ _OBJC_METACLASS_$_MTSNetworkCredentialManager
+ _OBJC_METACLASS_$_MTSThreadNetworkCredential
+ _SecRandomCopyBytes
+ __OBJC_$_CLASS_METHODS_MTSNetworkCredentialManager
+ __OBJC_$_CLASS_METHODS_MTSThreadNetworkCredential
+ __OBJC_$_CLASS_PROP_LIST_MTSThreadNetworkCredential
+ __OBJC_$_INSTANCE_METHODS_MTSNetworkCredentialManager
+ __OBJC_$_INSTANCE_METHODS_MTSThreadNetworkCredential
+ __OBJC_$_INSTANCE_VARIABLES_MTSNetworkCredentialManager
+ __OBJC_$_INSTANCE_VARIABLES_MTSThreadNetworkCredential
+ __OBJC_$_PROP_LIST_MTSNetworkCredentialManager
+ __OBJC_$_PROP_LIST_MTSThreadNetworkCredential
+ __OBJC_$_PROP_LIST_MTSXPCConnection.106
+ __OBJC_$_PROP_LIST_MTSXPCListener.67
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTSNetworkCredentialServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTSXPCNetworkCredentialClientProxyDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTSNetworkCredentialServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTSXPCNetworkCredentialClientProxyDelegate
+ __OBJC_CLASS_PROTOCOLS_$_MTSNetworkCredentialManager
+ __OBJC_CLASS_PROTOCOLS_$_MTSThreadNetworkCredential
+ __OBJC_CLASS_RO_$_MTSNetworkCredentialManager
+ __OBJC_CLASS_RO_$_MTSThreadNetworkCredential
+ __OBJC_LABEL_PROTOCOL_$_MTSNetworkCredentialClientInterface
+ __OBJC_LABEL_PROTOCOL_$_MTSNetworkCredentialServerInterface
+ __OBJC_LABEL_PROTOCOL_$_MTSXPCNetworkCredentialClientProxyDelegate
+ __OBJC_METACLASS_RO_$_MTSNetworkCredentialManager
+ __OBJC_METACLASS_RO_$_MTSThreadNetworkCredential
+ __OBJC_PROTOCOL_$_MTSNetworkCredentialClientInterface
+ __OBJC_PROTOCOL_$_MTSNetworkCredentialServerInterface
+ __OBJC_PROTOCOL_$_MTSXPCNetworkCredentialClientProxyDelegate
+ __PROTOCOLS__TtCV13MatterSupport22MatterAddDeviceRequestP33_1A83A92E88F6D049FA318E551745945D7Wrapper.10
+ ___103-[MTSNetworkCredentialManager retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]_block_invoke
+ ___105-[MTSNetworkCredentialManager setThreadCredentialManagementEnabled:forPairingWithUUID:completionHandler:]_block_invoke
+ ___112-[MTSXPCServerProxy updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]_block_invoke
+ ___42+[MTSNetworkCredentialManager logCategory]_block_invoke
+ ___87-[MTSNetworkCredentialManager retrievePreferredThreadCredentialsWithCompletionHandler:]_block_invoke
+ ___92-[MTSSystemCommissionerPairingManager pairWithSetupPayload:skipMFIPrompt:completionHandler:]_block_invoke
+ ___92-[MTSXPCServerProxy pairSystemCommissionerWithSetupPayload:skipMFIPrompt:completionHandler:]_block_invoke
+ ___93-[MTSXPCServerProxy retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]_block_invoke
+ ___block_descriptor_32_e68_"<MTSDeviceSetupExtensionProcess>"24?0"_EXExtensionIdentity"8^16l
+ ___block_descriptor_56_e8_32s40s48bs_e48_v24?0"MTSThreadNetworkCredential"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e50_v24?0"MTSSystemCommissionerPairing"8"NSError"16ls32l8s40l8s48l8
+ ___block_literal_global.1520
+ ___block_literal_global.2065
+ ___block_literal_global.2536
+ ___block_literal_global.2690
+ ___block_literal_global.428
+ ___block_literal_global.512
+ ___block_literal_global.609
+ ___block_literal_global.884
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.106
+ ___swift_closure_destructor.110
+ ___swift_closure_destructor.115
+ ___swift_closure_destructor.16
+ ___swift_closure_destructor.16Tm
+ ___swift_closure_destructor.20
+ ___swift_closure_destructor.24
+ ___swift_closure_destructor.28
+ ___swift_closure_destructor.33
+ ___swift_closure_destructor.33Tm
+ ___swift_closure_destructor.37
+ ___swift_closure_destructor.39
+ ___swift_closure_destructor.39Tm
+ ___swift_closure_destructor.41
+ ___swift_closure_destructor.43
+ ___swift_closure_destructor.45
+ ___swift_closure_destructor.48
+ ___swift_closure_destructor.50
+ ___swift_closure_destructor.54
+ ___swift_closure_destructor.55
+ ___swift_closure_destructor.59
+ ___swift_closure_destructor.64
+ ___swift_closure_destructor.72
+ ___swift_closure_destructor.76
+ ___swift_closure_destructor.81
+ ___swift_closure_destructor.89
+ ___swift_closure_destructor.93
+ ___swift_closure_destructor.98
+ __swift_implicitisolationactor_to_executor_cast
+ _arc4random_buf
+ _arc4random_uniform
+ _generateDataset.baseDataset
+ _kSecAttrSyncViewHint
+ _kSecAttrViewHintHome
+ _kSecRandomDefault
+ _logCategory._hmf_once_t18
+ _logCategory._hmf_once_t18.1519
+ _logCategory._hmf_once_t22
+ _logCategory._hmf_once_t30
+ _logCategory._hmf_once_t30.2542
+ _logCategory._hmf_once_t34
+ _logCategory._hmf_once_t34.2698
+ _logCategory._hmf_once_v19
+ _logCategory._hmf_once_v19.1521
+ _logCategory._hmf_once_v23
+ _logCategory._hmf_once_v31
+ _logCategory._hmf_once_v31.2543
+ _logCategory._hmf_once_v35
+ _logCategory._hmf_once_v35.2699
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$borderAgentEUI
+ _objc_msgSend$borderAgentID
+ _objc_msgSend$children
+ _objc_msgSend$clientProxy:pairSystemCommissionerWithSetupPayload:skipMFIPrompt:completionHandler:
+ _objc_msgSend$clientProxy:retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:
+ _objc_msgSend$clientProxy:updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:
+ _objc_msgSend$dataset
+ _objc_msgSend$deviceTypeID
+ _objc_msgSend$deviceTypes
+ _objc_msgSend$endpointID
+ _objc_msgSend$hasThreadCredentialsEntitlement
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:threadCredentialManagementEnabled:
+ _objc_msgSend$networkCredentialServer
+ _objc_msgSend$now
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$pairSystemCommissionerWithSetupPayload:skipMFIPrompt:completionHandler:
+ _objc_msgSend$retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:
+ _objc_msgSend$rootEndpoint
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$threadCredentialManagementEnabled
+ _objc_msgSend$threadCredentialManagementEndpoint:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x7
+ _snprintf
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x8
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x26
+ _swift_retain_x27
- -[MTSDevicePairing attributeDescriptions]
- -[MTSDevicePairingEcosystem attributeDescriptions]
- -[MTSDevicePairingFabric attributeDescriptions]
- -[MTSDevicePairingVendor attributeDescriptions]
- -[MTSSystemCommissionerPairing attributeDescriptions]
- -[MTSSystemCommissionerPairing initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:]
- -[MTSXPCClientProxy attributeDescriptions]
- -[MTSXPCConnection attributeDescriptions]
- GCC_except_table335
- GCC_except_table405
- GCC_except_table406
- GCC_except_table438
- GCC_except_table440
- GCC_except_table441
- GCC_except_table442
- _OBJC_CLASS_$_HMFAttributeDescription
- _OBJC_CLASS_$_NSMutableArray
- __OBJC_$_PROP_LIST_MTSXPCConnection.107
- __OBJC_$_PROP_LIST_MTSXPCListener.68
- __PROTOCOLS__TtCV13MatterSupport22MatterAddDeviceRequestP33_1A83A92E88F6D049FA318E551745945D7Wrapper.11
- ___block_descriptor_32_e68_"<MTSDeviceSetupExtensionProcess>"24?0"_EXHostConfiguration"8^16l
- ___block_literal_global.1732
- ___block_literal_global.2174
- ___block_literal_global.2306
- ___block_literal_global.394
- ___block_literal_global.471
- ___block_literal_global.564
- ___block_literal_global.806
- _logCategory._hmf_once_t13.2181
- _logCategory._hmf_once_t15
- _logCategory._hmf_once_t16
- _logCategory._hmf_once_t20
- _logCategory._hmf_once_t3
- _logCategory._hmf_once_t8
- _logCategory._hmf_once_v14.2182
- _logCategory._hmf_once_v16
- _logCategory._hmf_once_v17
- _logCategory._hmf_once_v21
- _logCategory._hmf_once_v4
- _logCategory._hmf_once_v9
- _objc_msgSend$array
- _objc_msgSend$initWithName:value:
- _objc_msgSend$initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:
- _objectdestroy.16Tm
- _objectdestroy.35Tm
- _objectdestroy.38Tm
- _symbolic _____Sg 13MatterSupport0A16AddDeviceRequestV
CStrings:
+ "\t"
+ "!borderAgentEUI || isValidBorderAgentEUI(borderAgentEUI)"
+ "!borderAgentID || isValidBorderAgentID(borderAgentID)"
+ ", Connection: %@"
+ ", Device Type: %@"
+ ", Display Name: %@"
+ ", Ecosystem: %@"
+ ", Fabric: %@"
+ ", Identifier: %@"
+ ", Index: %@"
+ ", Name: %@"
+ ", Node ID: %@"
+ ", Process ID: %@"
+ ", Process Name: %@"
+ ", Product ID: %@"
+ ", Root Public Key: %@"
+ ", Serial Number: %@"
+ ", Setup Payload: %@"
+ ", Thread Credential Management: %@"
+ ", UUID: %@"
+ ", Vendor ID: %@"
+ ", Vendor: %@"
+ "@\"<MTSDeviceSetupExtensionProcess>\"24@?0@\"_EXExtensionIdentity\"8^@16"
+ "Accepting new client proxy: %@"
+ "Adding keychain item with attributes: %@"
+ "Client proxy invalidated: %@"
+ "Connection to daemon was interrupted"
+ "Connection to daemon was invalidated"
+ "Could not deserialize from wrappedRequestData: %ld"
+ "Could not initialize from decoded certificationDeclaration: %@, deviceAttestationCertificate: %@, productAttestationIntermediateCertificate: %@"
+ "Could not initialize from decoded extendedPANID: %@"
+ "Could not initialize from decoded homes: %@"
+ "Could not initialize from decoded identifier: %@ displayName: %@"
+ "Could not initialize from decoded identifier: %@ index: %@ displayName: %@ ecosystem: %@"
+ "Could not initialize from decoded name: %@"
+ "Could not initialize from decoded networkName: %@, panID: %@, extendedPANID: %@, channel: %@, extendedAddress: %@, rssi: %@, version: %@, lqi: %@"
+ "Could not initialize from decoded rootPublicKey: %@ vendor: %@"
+ "Could not initialize from decoded ssid: %@, credentials: %@"
+ "Could not initialize from decoded ssid: %@, rssi: %@"
+ "Could not initialize from decoded uuid: %@, nodeID: %@, vendorID: %@, productID: %@, deviceType: %@"
+ "Could not initialize from nodeID: %@, fabric: %@"
+ "Device setup XPC connection was interrupted"
+ "Disabling"
+ "Disallowing fetch device pairings request because %@"
+ "Disallowing fetch system commissioner pairings request because %@"
+ "Disallowing opening commissioning window because %@"
+ "Disallowing pair system commissioner request because %@"
+ "Disallowing reading commissioning window status because %@"
+ "Disallowing remove all device pairings because %@"
+ "Disallowing remove device pairing request because %@"
+ "Disallowing remove system commissioner pairing request because %@"
+ "Disallowing retrieve preferred Thread credentials because %@"
+ "Disallowing update Thread credential management status request because %@"
+ "Enabling"
+ "Failed to add keychain item with attributes %@: %@"
+ "Failed to create device setup request from dictionary representation; failed to deserialize data %@: %@"
+ "Failed to create device setup request from dictionary representation; missing %@ key in dictionary: %@"
+ "Failed to create extension process from identity %@: %@"
+ "Failed to decode MTSThreadNetworkCredentialBorderAgentEUICodingKey"
+ "Failed to decode MTSThreadNetworkCredentialBorderAgentIDCodingKey"
+ "Failed to decode MTSThreadNetworkCredentialOperationalDatasetCodingKey"
+ "Failed to decode encoded value %@: %@"
+ "Failed to encode value %@: %@"
+ "Failed to find identity for extension identifier: %@"
+ "Failed to make XPC connection with extension process %@: %@"
+ "Failed to obtain deviceSetupProxy to configure device: %@"
+ "Failed to obtain deviceSetupProxy to fetch rooms: %@"
+ "Failed to obtain deviceSetupProxy to pair device: %@"
+ "Failed to obtain deviceSetupProxy to select thread network: %@"
+ "Failed to obtain deviceSetupProxy to select wifi network: %@"
+ "Failed to obtain deviceSetupProxy to validate device: %@"
+ "Failed to obtain remote object proxy for checking allows restricted characteristics access: %@"
+ "Failed to obtain remote object proxy for fetch device pairings: %@"
+ "Failed to obtain remote object proxy for fetch system commissioner pairings: %@"
+ "Failed to obtain remote object proxy for opening commissioning window: %@"
+ "Failed to obtain remote object proxy for pair system commissioner: %@"
+ "Failed to obtain remote object proxy for performDeviceSetupUsingRequest: %@"
+ "Failed to obtain remote object proxy for reading commissioning window status: %@"
+ "Failed to obtain remote object proxy for remove all device pairings: %@"
+ "Failed to obtain remote object proxy for remove device pairing: %@"
+ "Failed to obtain remote object proxy for remove system commissioner pairing: %@"
+ "Failed to obtain remote object proxy for retrieve preferred Thread credentials: %@"
+ "Failed to obtain remote object proxy for set Thread credential management state: %@"
+ "Failed to obtain remote object proxy for showing warning: %@"
+ "Failed to query all keychain items: %@"
+ "Failed to query keychain item for key %@: %@"
+ "Failed to read BT Matter client developer mode preference: %@"
+ "Failed to remove all keychain items %@: %@"
+ "Failed to remove all values: %@"
+ "Failed to remove keychain item with query %@: %@"
+ "Failed to remove value for key %@: %@"
+ "Failed to serialize device setup request %@: %@"
+ "Failed to set value for key %@: %@"
+ "Failed to update keychain item with query %@ and attributes %@: %@"
+ "I"
+ "Keychain item query result for key %@ was of unexpected class %@: %@"
+ "Keychain item query result was of unexpected class %@: %@"
+ "MTSSCP.threadCM"
+ "Missing endpoint information, MTRCommissioningParameters.readEndpointInformation == NO?"
+ "MyHome%d"
+ "Not showing restricted characteristics access warning because process is missing entitlement: %@"
+ "Pair system commissioner"
+ "Received bad status from sysctl for developer mode check: %d"
+ "Removing all data"
+ "Removing all keychain items matching query: %@"
+ "Removing all values"
+ "Removing data for key: %@"
+ "Removing keychain item matching query: %@"
+ "Removing value for key: %@"
+ "Retrieve or create preferred Thread credentials"
+ "Retrieve preferred Thread credentials"
+ "Returning NO to check restricted characteristics access allowed because process is missing entitlement: %@"
+ "Sending configure device request with name: %@, room: %@"
+ "Sending fetch rooms request with home: %@"
+ "Sending pair device request with home: %@, onboardingPayload: %@, uuid: %@"
+ "Sending select WiFi network request with wifiScanResults: %@"
+ "Sending select thread network request with threadScanResults: %@"
+ "Sending validate device credential request with deviceCredential: %@"
+ "Setting data for key: %@"
+ "Setting value for key: %@"
+ "Starting device setup extension messenger"
+ "Update Thread credential management status"
+ "[%{public}@] %@ Thread credential management for system commissioner pairing with UUID: %@"
+ "[%{public}@] Accepting new client proxy: %@"
+ "[%{public}@] Adding keychain item with attributes: %@"
+ "[%{public}@] Client proxy invalidated: %@"
+ "[%{public}@] Connection to daemon was interrupted"
+ "[%{public}@] Connection to daemon was invalidated"
+ "[%{public}@] Could not deserialize from wrappedRequestData: %ld"
+ "[%{public}@] Could not initialize from decoded certificationDeclaration: %@, deviceAttestationCertificate: %@, productAttestationIntermediateCertificate: %@"
+ "[%{public}@] Could not initialize from decoded extendedPANID: %@"
+ "[%{public}@] Could not initialize from decoded homes: %@"
+ "[%{public}@] Could not initialize from decoded identifier: %@ displayName: %@"
+ "[%{public}@] Could not initialize from decoded identifier: %@ index: %@ displayName: %@ ecosystem: %@"
+ "[%{public}@] Could not initialize from decoded name: %@"
+ "[%{public}@] Could not initialize from decoded networkName: %@, panID: %@, extendedPANID: %@, channel: %@, extendedAddress: %@, rssi: %@, version: %@, lqi: %@"
+ "[%{public}@] Could not initialize from decoded rootPublicKey: %@ vendor: %@"
+ "[%{public}@] Could not initialize from decoded ssid: %@, credentials: %@"
+ "[%{public}@] Could not initialize from decoded ssid: %@, rssi: %@"
+ "[%{public}@] Could not initialize from decoded uuid: %@, nodeID: %@, vendorID: %@, productID: %@, deviceType: %@"
+ "[%{public}@] Could not initialize from nodeID: %@, fabric: %@"
+ "[%{public}@] Device setup XPC connection was interrupted"
+ "[%{public}@] Disallowing fetch device pairings request because %@"
+ "[%{public}@] Disallowing fetch system commissioner pairings request because %@"
+ "[%{public}@] Disallowing opening commissioning window because %@"
+ "[%{public}@] Disallowing pair system commissioner request because %@"
+ "[%{public}@] Disallowing reading commissioning window status because %@"
+ "[%{public}@] Disallowing remove all device pairings because %@"
+ "[%{public}@] Disallowing remove device pairing request because %@"
+ "[%{public}@] Disallowing remove system commissioner pairing request because %@"
+ "[%{public}@] Disallowing retrieve preferred Thread credentials because %@"
+ "[%{public}@] Disallowing update Thread credential management status request because %@"
+ "[%{public}@] Failed to add keychain item with attributes %@: %@"
+ "[%{public}@] Failed to create device setup request from dictionary representation; failed to deserialize data %@: %@"
+ "[%{public}@] Failed to create device setup request from dictionary representation; missing %@ key in dictionary: %@"
+ "[%{public}@] Failed to create extension process from identity %@: %@"
+ "[%{public}@] Failed to decode MTSThreadNetworkCredentialBorderAgentEUICodingKey"
+ "[%{public}@] Failed to decode MTSThreadNetworkCredentialBorderAgentIDCodingKey"
+ "[%{public}@] Failed to decode MTSThreadNetworkCredentialOperationalDatasetCodingKey"
+ "[%{public}@] Failed to decode encoded value %@: %@"
+ "[%{public}@] Failed to encode value %@: %@"
+ "[%{public}@] Failed to fetch device pairings: %@"
+ "[%{public}@] Failed to fetch system commissioner pairings: %@"
+ "[%{public}@] Failed to find identity for extension identifier: %@"
+ "[%{public}@] Failed to make XPC connection with extension process %@: %@"
+ "[%{public}@] Failed to obtain deviceSetupProxy to configure device: %@"
+ "[%{public}@] Failed to obtain deviceSetupProxy to fetch rooms: %@"
+ "[%{public}@] Failed to obtain deviceSetupProxy to pair device: %@"
+ "[%{public}@] Failed to obtain deviceSetupProxy to select thread network: %@"
+ "[%{public}@] Failed to obtain deviceSetupProxy to select wifi network: %@"
+ "[%{public}@] Failed to obtain deviceSetupProxy to validate device: %@"
+ "[%{public}@] Failed to obtain remote object proxy for checking allows restricted characteristics access: %@"
+ "[%{public}@] Failed to obtain remote object proxy for fetch device pairings: %@"
+ "[%{public}@] Failed to obtain remote object proxy for fetch system commissioner pairings: %@"
+ "[%{public}@] Failed to obtain remote object proxy for opening commissioning window: %@"
+ "[%{public}@] Failed to obtain remote object proxy for pair system commissioner: %@"
+ "[%{public}@] Failed to obtain remote object proxy for performDeviceSetupUsingRequest: %@"
+ "[%{public}@] Failed to obtain remote object proxy for reading commissioning window status: %@"
+ "[%{public}@] Failed to obtain remote object proxy for remove all device pairings: %@"
+ "[%{public}@] Failed to obtain remote object proxy for remove device pairing: %@"
+ "[%{public}@] Failed to obtain remote object proxy for remove system commissioner pairing: %@"
+ "[%{public}@] Failed to obtain remote object proxy for retrieve preferred Thread credentials: %@"
+ "[%{public}@] Failed to obtain remote object proxy for set Thread credential management state: %@"
+ "[%{public}@] Failed to obtain remote object proxy for showing warning: %@"
+ "[%{public}@] Failed to open commissioning window: %@"
+ "[%{public}@] Failed to pair device onto system commissioner fabric: %@"
+ "[%{public}@] Failed to perform Matter device setup setup: %@"
+ "[%{public}@] Failed to query all keychain items: %@"
+ "[%{public}@] Failed to query keychain item for key %@: %@"
+ "[%{public}@] Failed to read BT Matter client developer mode preference: %@"
+ "[%{public}@] Failed to read commissioning window status: %@"
+ "[%{public}@] Failed to remove all device pairings: %@"
+ "[%{public}@] Failed to remove all keychain items %@: %@"
+ "[%{public}@] Failed to remove all values: %@"
+ "[%{public}@] Failed to remove device pairing: %@"
+ "[%{public}@] Failed to remove keychain item with query %@: %@"
+ "[%{public}@] Failed to remove system commissioner pairing: %@"
+ "[%{public}@] Failed to remove value for key %@: %@"
+ "[%{public}@] Failed to retrieve or create preferred Thread credentials: %@"
+ "[%{public}@] Failed to retrieve preferred Thread credentials: %@"
+ "[%{public}@] Failed to serialize device setup request %@: %@"
+ "[%{public}@] Failed to set value for key %@: %@"
+ "[%{public}@] Failed to update Thread credential management status: %@"
+ "[%{public}@] Failed to update keychain item with query %@ and attributes %@: %@"
+ "[%{public}@] Fetched %ld device pairings"
+ "[%{public}@] Fetched %ld system commissioner pairings"
+ "[%{public}@] Fetching all device pairings"
+ "[%{public}@] Fetching system commissioner pairings"
+ "[%{public}@] Keychain item query result for key %@ was of unexpected class %@: %@"
+ "[%{public}@] Keychain item query result was of unexpected class %@: %@"
+ "[%{public}@] Missing endpoint information, MTRCommissioningParameters.readEndpointInformation == NO?"
+ "[%{public}@] Not showing restricted characteristics access warning because process is missing entitlement: %@"
+ "[%{public}@] Opening commissioning window"
+ "[%{public}@] Pairing device onto system commissioner fabric"
+ "[%{public}@] Performing Matter device setup using request: %@"
+ "[%{public}@] Reading commissioning window status"
+ "[%{public}@] Received bad status from sysctl for developer mode check: %d"
+ "[%{public}@] Removing all data"
+ "[%{public}@] Removing all device pairings"
+ "[%{public}@] Removing all keychain items matching query: %@"
+ "[%{public}@] Removing all values"
+ "[%{public}@] Removing data for key: %@"
+ "[%{public}@] Removing device pairing with UUID: %@"
+ "[%{public}@] Removing keychain item matching query: %@"
+ "[%{public}@] Removing system commissioner pairing with UUID: %@"
+ "[%{public}@] Removing value for key: %@"
+ "[%{public}@] Retrieving or creating preferred Thread credentials"
+ "[%{public}@] Retrieving preferred Thread credentials"
+ "[%{public}@] Returning NO to check restricted characteristics access allowed because process is missing entitlement: %@"
+ "[%{public}@] Sending configure device request with name: %@, room: %@"
+ "[%{public}@] Sending fetch rooms request with home: %@"
+ "[%{public}@] Sending pair device request with home: %@, onboardingPayload: %@, uuid: %@"
+ "[%{public}@] Sending select WiFi network request with wifiScanResults: %@"
+ "[%{public}@] Sending select thread network request with threadScanResults: %@"
+ "[%{public}@] Sending validate device credential request with deviceCredential: %@"
+ "[%{public}@] Setting data for key: %@"
+ "[%{public}@] Setting value for key: %@"
+ "[%{public}@] Starting device setup extension messenger"
+ "[%{public}@] Successfully opened commissioning window with setup QR code: %@, manual pairing code: %@"
+ "[%{public}@] Successfully paired device onto system commissioner fabric: %@"
+ "[%{public}@] Successfully performed Matter device setup setup"
+ "[%{public}@] Successfully read commissioning window status: %@"
+ "[%{public}@] Successfully removed all device pairings"
+ "[%{public}@] Successfully removed device pairing"
+ "[%{public}@] Successfully removed system commissioner pairing"
+ "[%{public}@] Successfully retrieved or created preferred Thread credentials"
+ "[%{public}@] Successfully retrieved preferred Thread credentials"
+ "[%{public}@] Successfully update Thread credential management status"
+ "[%{public}@] [%{public}@] %@ Thread credential management for system commissioner pairing with UUID: %@"
+ "[%{public}@] [%{public}@] Failed to fetch device pairings: %@"
+ "[%{public}@] [%{public}@] Failed to fetch system commissioner pairings: %@"
+ "[%{public}@] [%{public}@] Failed to open commissioning window: %@"
+ "[%{public}@] [%{public}@] Failed to pair device onto system commissioner fabric: %@"
+ "[%{public}@] [%{public}@] Failed to perform Matter device setup setup: %@"
+ "[%{public}@] [%{public}@] Failed to read commissioning window status: %@"
+ "[%{public}@] [%{public}@] Failed to remove all device pairings: %@"
+ "[%{public}@] [%{public}@] Failed to remove device pairing: %@"
+ "[%{public}@] [%{public}@] Failed to remove system commissioner pairing: %@"
+ "[%{public}@] [%{public}@] Failed to retrieve or create preferred Thread credentials: %@"
+ "[%{public}@] [%{public}@] Failed to retrieve preferred Thread credentials: %@"
+ "[%{public}@] [%{public}@] Failed to update Thread credential management status: %@"
+ "[%{public}@] [%{public}@] Fetched %ld device pairings"
+ "[%{public}@] [%{public}@] Fetched %ld system commissioner pairings"
+ "[%{public}@] [%{public}@] Fetching all device pairings"
+ "[%{public}@] [%{public}@] Fetching system commissioner pairings"
+ "[%{public}@] [%{public}@] Opening commissioning window"
+ "[%{public}@] [%{public}@] Pairing device onto system commissioner fabric"
+ "[%{public}@] [%{public}@] Performing Matter device setup using request: %@"
+ "[%{public}@] [%{public}@] Reading commissioning window status"
+ "[%{public}@] [%{public}@] Removing all device pairings"
+ "[%{public}@] [%{public}@] Removing device pairing with UUID: %@"
+ "[%{public}@] [%{public}@] Removing system commissioner pairing with UUID: %@"
+ "[%{public}@] [%{public}@] Retrieving or creating preferred Thread credentials"
+ "[%{public}@] [%{public}@] Retrieving preferred Thread credentials"
+ "[%{public}@] [%{public}@] Successfully opened commissioning window with setup QR code: %@, manual pairing code: %@"
+ "[%{public}@] [%{public}@] Successfully paired device onto system commissioner fabric: %@"
+ "[%{public}@] [%{public}@] Successfully performed Matter device setup setup"
+ "[%{public}@] [%{public}@] Successfully read commissioning window status: %@"
+ "[%{public}@] [%{public}@] Successfully removed all device pairings"
+ "[%{public}@] [%{public}@] Successfully removed device pairing"
+ "[%{public}@] [%{public}@] Successfully removed system commissioner pairing"
+ "[%{public}@] [%{public}@] Successfully retrieved or created preferred Thread credentials"
+ "[%{public}@] [%{public}@] Successfully retrieved preferred Thread credentials"
+ "[%{public}@] [%{public}@] Successfully update Thread credential management status"
+ "ba"
+ "c"
+ "com.apple.matter.support.xpc.thread-credentials"
+ "dataset"
+ "ds"
+ "id"
+ "setupPayloadString"
+ "system.commissioner.network.credential.manager"
+ "systemCommissionerPairingUUID"
+ "v24@?0@\"MTSSystemCommissionerPairing\"8@\"NSError\"16"
+ "v24@?0@\"MTSThreadNetworkCredential\"8@\"NSError\"16"
- "#16@0:8"
- "$defaultActor"
- "%{public}@Accepting new client proxy: %@"
- "%{public}@Adding keychain item with attributes: %@"
- "%{public}@Client proxy invalidated: %@"
- "%{public}@Connection to daemon was interrupted"
- "%{public}@Connection to daemon was invalidated"
- "%{public}@Could not deserialize from wrappedRequestData: %ld"
- "%{public}@Could not initialize from decoded certificationDeclaration: %@, deviceAttestationCertificate: %@, productAttestationIntermediateCertificate: %@"
- "%{public}@Could not initialize from decoded extendedPANID: %@"
- "%{public}@Could not initialize from decoded homes: %@"
- "%{public}@Could not initialize from decoded identifier: %@ displayName: %@"
- "%{public}@Could not initialize from decoded identifier: %@ index: %@ displayName: %@ ecosystem: %@"
- "%{public}@Could not initialize from decoded name: %@"
- "%{public}@Could not initialize from decoded networkName: %@, panID: %@, extendedPANID: %@, channel: %@, extendedAddress: %@, rssi: %@, version: %@, lqi: %@"
- "%{public}@Could not initialize from decoded rootPublicKey: %@ vendor: %@"
- "%{public}@Could not initialize from decoded ssid: %@, credentials: %@"
- "%{public}@Could not initialize from decoded ssid: %@, rssi: %@"
- "%{public}@Could not initialize from decoded uuid: %@, nodeID: %@, vendorID: %@, productID: %@, deviceType: %@"
- "%{public}@Could not initialize from nodeID: %@, fabric: %@"
- "%{public}@Device setup XPC connection was interrupted"
- "%{public}@Disallowing fetch device pairings request because %@"
- "%{public}@Disallowing fetch system commissioner pairings request because %@"
- "%{public}@Disallowing opening commissioning window because %@"
- "%{public}@Disallowing reading commissioning window status because %@"
- "%{public}@Disallowing remove all device pairings because %@"
- "%{public}@Disallowing remove device pairing request because %@"
- "%{public}@Disallowing remove system commissioner pairing request because %@"
- "%{public}@Failed to add keychain item with attributes %@: %@"
- "%{public}@Failed to create device setup request from dictionary representation; failed to deserialize data %@: %@"
- "%{public}@Failed to create device setup request from dictionary representation; missing %@ key in dictionary: %@"
- "%{public}@Failed to create extension process from configuration %@: %@"
- "%{public}@Failed to decode encoded value %@: %@"
- "%{public}@Failed to encode value %@: %@"
- "%{public}@Failed to find identity for extension identifier: %@"
- "%{public}@Failed to make XPC connection with extension process %@: %@"
- "%{public}@Failed to obtain deviceSetupProxy to configure device: %@"
- "%{public}@Failed to obtain deviceSetupProxy to fetch rooms: %@"
- "%{public}@Failed to obtain deviceSetupProxy to pair device: %@"
- "%{public}@Failed to obtain deviceSetupProxy to select thread network: %@"
- "%{public}@Failed to obtain deviceSetupProxy to select wifi network: %@"
- "%{public}@Failed to obtain deviceSetupProxy to validate device: %@"
- "%{public}@Failed to obtain remote object proxy for checking allows restricted characteristics access: %@"
- "%{public}@Failed to obtain remote object proxy for fetch device pairings: %@"
- "%{public}@Failed to obtain remote object proxy for fetch system commissioner pairings: %@"
- "%{public}@Failed to obtain remote object proxy for opening commissioning window: %@"
- "%{public}@Failed to obtain remote object proxy for performDeviceSetupUsingRequest: %@"
- "%{public}@Failed to obtain remote object proxy for reading commissioning window status: %@"
- "%{public}@Failed to obtain remote object proxy for remove all device pairings: %@"
- "%{public}@Failed to obtain remote object proxy for remove device pairing: %@"
- "%{public}@Failed to obtain remote object proxy for remove system commissioner pairing: %@"
- "%{public}@Failed to obtain remote object proxy for showing warning: %@"
- "%{public}@Failed to query all keychain items: %@"
- "%{public}@Failed to query keychain item for key %@: %@"
- "%{public}@Failed to read BT Matter client developer mode preference: %@"
- "%{public}@Failed to remove all keychain items %@: %@"
- "%{public}@Failed to remove all values: %@"
- "%{public}@Failed to remove keychain item with query %@: %@"
- "%{public}@Failed to remove value for key %@: %@"
- "%{public}@Failed to serialize device setup request %@: %@"
- "%{public}@Failed to set value for key %@: %@"
- "%{public}@Failed to update keychain item with query %@ and attributes %@: %@"
- "%{public}@Keychain item query result for key %@ was of unexpected class %@: %@"
- "%{public}@Keychain item query result was of unexpected class %@: %@"
- "%{public}@Not showing restricted characteristics access warning because process is missing entitlement: %@"
- "%{public}@Received bad status from sysctl for developer mode check: %d"
- "%{public}@Removing all data"
- "%{public}@Removing all keychain items matching query: %@"
- "%{public}@Removing all values"
- "%{public}@Removing data for key: %@"
- "%{public}@Removing keychain item matching query: %@"
- "%{public}@Removing value for key: %@"
- "%{public}@Returning NO to check restricted characteristics access allowed because process is missing entitlement: %@"
- "%{public}@Sending configure device request with name: %@, room: %@"
- "%{public}@Sending fetch rooms request with home: %@"
- "%{public}@Sending pair device request with home: %@, onboardingPayload: %@, uuid: %@"
- "%{public}@Sending select WiFi network request with wifiScanResults: %@"
- "%{public}@Sending select thread network request with threadScanResults: %@"
- "%{public}@Sending validate device credential request with deviceCredential: %@"
- "%{public}@Setting data for key: %@"
- "%{public}@Setting value for key: %@"
- "%{public}@Starting device setup extension messenger"
- "%{public}@[%{public}@] Failed to fetch device pairings: %@"
- "%{public}@[%{public}@] Failed to fetch system commissioner pairings: %@"
- "%{public}@[%{public}@] Failed to open commissioning window: %@"
- "%{public}@[%{public}@] Failed to perform Matter device setup setup: %@"
- "%{public}@[%{public}@] Failed to read commissioning window status: %@"
- "%{public}@[%{public}@] Failed to remove all device pairings: %@"
- "%{public}@[%{public}@] Failed to remove device pairing: %@"
- "%{public}@[%{public}@] Failed to remove system commissioner pairing: %@"
- "%{public}@[%{public}@] Fetched %ld device pairings"
- "%{public}@[%{public}@] Fetched %ld system commissioner pairings"
- "%{public}@[%{public}@] Fetching all device pairings"
- "%{public}@[%{public}@] Fetching system commissioner pairings"
- "%{public}@[%{public}@] Opening commissioning window"
- "%{public}@[%{public}@] Performing Matter device setup using request: %@"
- "%{public}@[%{public}@] Reading commissioning window status"
- "%{public}@[%{public}@] Removing all device pairings"
- "%{public}@[%{public}@] Removing device pairing with UUID: %@"
- "%{public}@[%{public}@] Removing system commissioner pairing with UUID: %@"
- "%{public}@[%{public}@] Successfully opened commissioning window with setup QR code: %@, manual pairing code: %@"
- "%{public}@[%{public}@] Successfully performed Matter device setup setup"
- "%{public}@[%{public}@] Successfully read commissioning window status: %@"
- "%{public}@[%{public}@] Successfully removed all device pairings"
- "%{public}@[%{public}@] Successfully removed device pairing"
- "%{public}@[%{public}@] Successfully removed system commissioner pairing"
- ".cxx_destruct"
- "@\"<MTDeviceSetupRequestSwiftWrapper>\""
- "@\"<MTSAuthorizationServerInterface>\""
- "@\"<MTSDevicePairingServerInterface>\""
- "@\"<MTSDeviceSetupExtensionProcess>\""
- "@\"<MTSDeviceSetupExtensionProcess>\"24@?0@\"_EXHostConfiguration\"8^@16"
- "@\"<MTSKeychainStoreDataSource>\""
- "@\"<MTSSystemCommissionerPairingServerInterface>\""
- "@\"<MTSXPCClientProxyDelegate>\""
- "@\"<MTSXPCConnection>\""
- "@\"<MTSXPCConnection>\"24@0:8^@16"
- "@\"<MTSXPCDeviceSetupClientProxyDelegate>\""
- "@\"<MTSXPCListener>\""
- "@\"<MTSXPCListenerDelegate>\""
- "@\"<MTSXPCListenerDelegate>\"16@0:8"
- "@\"HMFProcessInfo\"16@0:8"
- "@\"MTRSetupPayload\""
- "@\"MTRSetupPayload\"16@0:8"
- "@\"MTSDevicePairingEcosystem\""
- "@\"MTSDevicePairingFabric\""
- "@\"MTSDevicePairingVendor\""
- "@\"MTSDeviceSetupTopology\"16@0:8"
- "@\"MTSKeychainStore\""
- "@\"MTSSystemCommissionerPairing\""
- "@\"MTSXPCServerProxy\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject\"16@0:8"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSURL\"16@0:8"
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"NSXPCInterface\"16@0:8"
- "@\"NSXPCListener\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSString\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8@?<v@?@\"NSError\">16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@\"NSDictionary\"16^@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16^@24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24C32C36"
- "@40@0:8q16@24@32"
- "@48@0:8@16@24@32@40"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "@?"
- "@?16@0:8"
- "@?<v@?>16@0:8"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSXPCConnection\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8@\"<MTSXPCListener>\"16@\"<MTSXPCConnection>\"24"
- "B32@0:8@\"NSDictionary\"16^@24"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B40@0:8@\"NSDictionary\"16@\"NSDictionary\"24^@32"
- "B40@0:8@16@24^@32"
- "B48@0:8@16@24@32@40"
- "B64@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSString\"40@\"NSData\"48@\"NSNumber\"56"
- "B64@0:8@16@24@32@40@48@56"
- "C"
- "C16@0:8"
- "Connection"
- "Device Type"
- "Display Name"
- "Ecosystem"
- "Fabric"
- "HMFLogging"
- "HMFObject"
- "Identifier"
- "Index"
- "MTDeviceSetupRequestFactory"
- "MTDeviceSetupRequestSwiftWrapper"
- "MTSAuthorization"
- "MTSAuthorizationClientInterface"
- "MTSAuthorizationServerInterface"
- "MTSDeviceCredential"
- "MTSDevicePairing"
- "MTSDevicePairingClientInterface"
- "MTSDevicePairingEcosystem"
- "MTSDevicePairingFabric"
- "MTSDevicePairingManager"
- "MTSDevicePairingServerInterface"
- "MTSDevicePairingVendor"
- "MTSDeviceSetupClientInterface"
- "MTSDeviceSetupDevicePredicate"
- "MTSDeviceSetupExtensionIdentity"
- "MTSDeviceSetupExtensionMessenger"
- "MTSDeviceSetupExtensionProcess"
- "MTSDeviceSetupHome"
- "MTSDeviceSetupManager"
- "MTSDeviceSetupRequest"
- "MTSDeviceSetupRequestPairingDescription"
- "MTSDeviceSetupRoom"
- "MTSDeviceSetupServerInterface"
- "MTSDeviceSetupTopology"
- "MTSDeviceSetupXPC"
- "MTSDeviceSetupXPCInterface"
- "MTSError_Internal"
- "MTSKeyValueStore"
- "MTSKeychainStore"
- "MTSKeychainStoreDataSource"
- "MTSSystemCommissionerPairing"
- "MTSSystemCommissionerPairingClientInterface"
- "MTSSystemCommissionerPairingManager"
- "MTSSystemCommissionerPairingServerInterface"
- "MTSThreadNetworkAssociation"
- "MTSThreadScanResult"
- "MTSWiFiNetworkAssociation"
- "MTSWiFiScanResult"
- "MTSXPC"
- "MTSXPCAuthorizationClientProxyDelegate"
- "MTSXPCClientInterface"
- "MTSXPCClientProxy"
- "MTSXPCClientProxyDelegate"
- "MTSXPCConnection"
- "MTSXPCDevicePairingClientProxyDelegate"
- "MTSXPCDeviceSetupClientProxyDelegate"
- "MTSXPCListener"
- "MTSXPCListenerDelegate"
- "MTSXPCServer"
- "MTSXPCServerInterface"
- "MTSXPCServerProxy"
- "MTSXPCSystemCommissionerPairingClientProxyDelegate"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "Name"
- "Node ID"
- "Process ID"
- "Process Name"
- "Product ID"
- "Q16@0:8"
- "Root Public Key"
- "S"
- "Serial Number"
- "Setup Payload"
- "T#,R"
- "T@\"<MTDeviceSetupRequestSwiftWrapper>\",R,V_wrappedRequest"
- "T@\"<MTSAuthorizationServerInterface>\",W,V_authorizationServer"
- "T@\"<MTSDevicePairingServerInterface>\",W,V_devicePairingServer"
- "T@\"<MTSDeviceSetupExtensionProcess>\",&,V_extensionProcess"
- "T@\"<MTSKeychainStoreDataSource>\",R,V_dataSource"
- "T@\"<MTSSystemCommissionerPairingServerInterface>\",W,V_systemCommissionerPairingServer"
- "T@\"<MTSXPCClientProxyDelegate>\",W,V_delegate"
- "T@\"<MTSXPCConnection>\",&,N,V_connection"
- "T@\"<MTSXPCConnection>\",&,V_xpcConnection"
- "T@\"<MTSXPCConnection>\",R,V_connection"
- "T@\"<MTSXPCDeviceSetupClientProxyDelegate>\",W,V_deviceSetupServer"
- "T@\"<MTSXPCListener>\",R,V_listener"
- "T@\"<MTSXPCListenerDelegate>\",W"
- "T@\"<MTSXPCListenerDelegate>\",W,V_delegate"
- "T@\"HMFProcessInfo\",R"
- "T@\"MTRSetupPayload\",N,R"
- "T@\"MTRSetupPayload\",R"
- "T@\"MTRSetupPayload\",R,V_setupPayload"
- "T@\"MTSDevicePairingEcosystem\",R,C,V_ecosystem"
- "T@\"MTSDevicePairingFabric\",R,C,V_fabric"
- "T@\"MTSDevicePairingVendor\",R,C,V_vendor"
- "T@\"MTSDeviceSetupTopology\",N,R"
- "T@\"MTSDeviceSetupTopology\",R"
- "T@\"MTSKeychainStore\",R,V_keychainStore"
- "T@\"MTSSystemCommissionerPairing\",R,C,V_systemCommissionerPairing"
- "T@\"MTSXPCServerProxy\",R,V_serverProxy"
- "T@\"NSArray\",?,R,C,N"
- "T@\"NSArray\",R,C,V_homes"
- "T@\"NSData\",N,R"
- "T@\"NSData\",R"
- "T@\"NSData\",R,C,V_certificationDeclaration"
- "T@\"NSData\",R,C,V_credentials"
- "T@\"NSData\",R,C,V_deviceAttestationCertificate"
- "T@\"NSData\",R,C,V_extendedAddress"
- "T@\"NSData\",R,C,V_productAttestationIntermediateCertificate"
- "T@\"NSData\",R,C,V_rootPublicKey"
- "T@\"NSData\",R,C,V_ssid"
- "T@\"NSDictionary\",R,C"
- "T@\"NSMutableSet\",R,V_clientProxies"
- "T@\"NSNumber\",&,V_productID"
- "T@\"NSNumber\",&,V_vendorID"
- "T@\"NSNumber\",R,C,V_channel"
- "T@\"NSNumber\",R,C,V_deviceType"
- "T@\"NSNumber\",R,C,V_extendedPANID"
- "T@\"NSNumber\",R,C,V_identifier"
- "T@\"NSNumber\",R,C,V_index"
- "T@\"NSNumber\",R,C,V_lqi"
- "T@\"NSNumber\",R,C,V_nodeID"
- "T@\"NSNumber\",R,C,V_panID"
- "T@\"NSNumber\",R,C,V_productID"
- "T@\"NSNumber\",R,C,V_rssi"
- "T@\"NSNumber\",R,C,V_vendorID"
- "T@\"NSNumber\",R,C,V_version"
- "T@\"NSNumber\",R,V_nodeID"
- "T@\"NSNumber\",R,V_rssi"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,V_serialNumber"
- "T@\"NSString\",N,R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_name"
- "T@\"NSString\",R,C,V_displayName"
- "T@\"NSString\",R,C,V_name"
- "T@\"NSString\",R,C,V_networkName"
- "T@\"NSString\",R,C,V_scope"
- "T@\"NSString\",R,C,V_serialNumber"
- "T@\"NSURL\",R,C"
- "T@\"NSURL\",R,C,V_containingAppBundleURL"
- "T@\"NSUUID\",&,V_uuid"
- "T@\"NSUUID\",R,C,V_UUID"
- "T@\"NSUUID\",R,C,V_uuid"
- "T@\"NSUUID\",R,V_uuid"
- "T@\"NSXPCConnection\",R,V_xpcConnection"
- "T@\"NSXPCInterface\",&"
- "T@\"NSXPCInterface\",R"
- "T@\"NSXPCListener\",R,V_xpcListener"
- "T@,&"
- "T@,N,R"
- "T@,R"
- "T@?,C"
- "T@?,C,V_executeExtensionQueryHandler"
- "T@?,C,V_extensionProcessFactory"
- "T@?,R,V_clientProxyFactory"
- "T@?,R,V_connectionFactory"
- "TB,N,R"
- "TB,R"
- "TB,R,GisRestrictedCharacteristicsAccessAllowed"
- "TC,R,V_band"
- "TC,R,V_security"
- "TQ,R"
- "Ti,R"
- "Tq,N,R"
- "URL"
- "UUID"
- "UUIDFromIdentifier:"
- "UUIDFromIdentifier:ecosystem:"
- "UUIDFromNodeID:fabric:"
- "UUIDFromRootPublicKey:vendor:"
- "UUIDString"
- "Vendor"
- "Vendor ID"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_EXConnectionHandler"
- "_EXMainConnectionHandler"
- "_TtC13MatterSupport38MatterAddDeviceExtensionRequestHandler"
- "_TtC13MatterSupport41MatterAddDeviceExtensionConnectionHandler"
- "_TtCV13MatterSupport22MatterAddDeviceRequestP33_1A83A92E88F6D049FA318E551745945D24FirstOneWinsContinuation"
- "_TtCV13MatterSupport22MatterAddDeviceRequestP33_1A83A92E88F6D049FA318E551745945D7Wrapper"
- "_UUID"
- "_authorizationServer"
- "_band"
- "_certificationDeclaration"
- "_channel"
- "_clientProxies"
- "_clientProxyFactory"
- "_connection"
- "_connectionFactory"
- "_containingAppBundleURL"
- "_credentials"
- "_dataSource"
- "_delegate"
- "_deviceAttestationCertificate"
- "_devicePairingServer"
- "_deviceSetupServer"
- "_deviceType"
- "_displayName"
- "_ecosystem"
- "_executeExtensionQueryHandler"
- "_extendedAddress"
- "_extendedPANID"
- "_extensionProcess"
- "_extensionProcessFactory"
- "_fabric"
- "_homes"
- "_identifier"
- "_index"
- "_keychainStore"
- "_listener"
- "_lock"
- "_lqi"
- "_name"
- "_networkName"
- "_nodeID"
- "_panID"
- "_productAttestationIntermediateCertificate"
- "_productID"
- "_rootPublicKey"
- "_rssi"
- "_scope"
- "_security"
- "_serialNumber"
- "_serverProxy"
- "_setupPayload"
- "_ssid"
- "_systemCommissionerPairing"
- "_systemCommissionerPairingServer"
- "_uuid"
- "_vendor"
- "_vendorID"
- "_version"
- "_wrappedRequest"
- "_xpcConnection"
- "_xpcListener"
- "activate"
- "addItemWithAttributes:error:"
- "addObject:"
- "allDataByKey"
- "allowsRestrictedCharacteristicsAccessViaDeveloperModeProfile"
- "allowsRestrictedCharacteristicsAccessViaSkipDeveloperModeRestrictionProfile"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayWithObjects:count:"
- "attributeDescriptions"
- "attributeDictionaryForAddingData:forKey:"
- "attributeDictionaryForUpdatingData:"
- "autorelease"
- "boolValue"
- "checkRestrictedCharacteristicsAccessAllowedWithCompletionHandler:"
- "class"
- "clientProxies"
- "clientProxy:checkRestrictedCharacteristicsAccessAllowedWithCompletionHandler:"
- "clientProxy:fetchDevicePairingsForSystemCommissionerPairingUUID:completionHandler:"
- "clientProxy:fetchSystemCommissionerPairingsWithCompletionHandler:"
- "clientProxy:openCommissioningWindowForSystemCommissionerPairingUUID:duration:completionHandler:"
- "clientProxy:performDeviceSetupUsingRequest:completionHandler:"
- "clientProxy:readCommissioningWindowStatusForSystemCommissionerPairingUUID:completionHandler:"
- "clientProxy:removeAllDevicePairingsForSystemCommissionerPairingUUID:completionHandler:"
- "clientProxy:removeDevicePairingWithUUID:forSystemCommissionerPairingUUID:completionHandler:"
- "clientProxy:removeSystemCommissionerPairingWithUUID:completionHandler:"
- "code"
- "configureDeviceWithName:room:completionHandler:"
- "conformsToProtocol:"
- "containingBundleRecord"
- "continuation"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dataForKey:"
- "dataWithBytes:length:"
- "dealloc"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "delegate"
- "description"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "ecosystemName"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "executeExtensionQueryHandler"
- "executeQuery:"
- "exportedInterface"
- "exportedObject"
- "extensionProcess"
- "extensionProcessFactory"
- "extensionProcessWithConfiguration:error:"
- "extensionRequestHandler"
- "fetchDevicePairingsForSystemCommissionerPairingUUID:completionHandler:"
- "fetchPairingsWithCompletionHandler:"
- "fetchRoomsInHome:completionHandler:"
- "fetchSystemCommissionerPairingsWithCompletionHandler:"
- "hasDevicePairingEntitlement"
- "hasEntitlement:"
- "hasMatterSetupPayloadEntitlement"
- "hasPrivateHomeKitEntitlement"
- "hash"
- "hmfErrorWithCode:"
- "hmfErrorWithCode:reason:"
- "hmf_UUIDWithNamespace:data:"
- "hmf_dataForKey:"
- "i16@0:8"
- "init"
- "initWithCertificationDeclaration:deviceAttestationCertificate:productAttestationIntermediateCertificate:"
- "initWithCoder:"
- "initWithConnection:"
- "initWithConnectionFactory:"
- "initWithContainingAppBundleURL:"
- "initWithDictionaryRepresentation:"
- "initWithDomain:code:userInfo:"
- "initWithEcosystemName:homeNames:blockedDevicePairings:"
- "initWithExtendedPANID:"
- "initWithExtensionIdentity:"
- "initWithExtensionPointIdentifier:"
- "initWithHomes:"
- "initWithIdentifier:displayName:"
- "initWithIdentifier:displayName:ecosystem:"
- "initWithIdentifier:index:displayName:ecosystem:"
- "initWithKeychainStore:"
- "initWithListener:clientProxyFactory:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithName:"
- "initWithName:value:"
- "initWithNetworkName:panID:extendedPANID:channel:extendedAddress:rssi:version:lqi:"
- "initWithNodeID:fabric:"
- "initWithPrincipalObject:"
- "initWithRootPublicKey:nodeID:"
- "initWithRootPublicKey:vendor:"
- "initWithSSID:credentials:"
- "initWithSSID:rssi:security:band:"
- "initWithScope:"
- "initWithScope:dataSource:"
- "initWithSerializedRequest:"
- "initWithServerProxy:"
- "initWithSystemCommissionerPairing:"
- "initWithSystemCommissionerPairing:serverProxy:"
- "initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:"
- "initWithUUIDString:"
- "initWithWrappedRequest:"
- "initWithXPCConnection:"
- "initWithXPCListener:"
- "integerValue"
- "interfaceWithProtocol:"
- "interruptionHandler"
- "invalidate"
- "invalidationHandler"
- "isDeveloperModeEnabled"
- "isEqual:"
- "isEqualToData:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRestrictedCharacteristicsAccessAllowed"
- "keychainStore"
- "length"
- "listener:shouldAcceptNewConnection:"
- "logCategory"
- "logIdentifier"
- "makeMTSXPCConnectionWithError:"
- "makeRequestFrom:"
- "makeRequestWithEcosystemName:homes:blockedDevicePairings:"
- "makeXPCConnectionWithError:"
- "mts_clientInterface"
- "mts_deviceSetupExtensionInterface"
- "mts_errorWithCode:"
- "mts_errorWithCode:description:"
- "mts_errorWithCode:underlyingError:"
- "mts_errorWithCode:underlyingError:description:"
- "mts_serverInterface"
- "mts_stubErrorForMethod:"
- "na_dictionaryByMappingValues:"
- "na_firstObjectPassingTest:"
- "numberWithInt:"
- "numberWithUnsignedChar:"
- "objectForKeyedSubscript:"
- "openCommissioningWindowForSystemCommissionerPairingUUID:duration:completionHandler:"
- "openCommissioningWindowWithDuration:completionHandler:"
- "pairDeviceInHome:onboardingPayload:uuid:completionHandler:"
- "performDeviceSetupUsingRequest:completionHandler:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "principalObject"
- "privateDescription"
- "processIdentifier"
- "processInfo"
- "propertyDescription"
- "q16@0:8"
- "queryDictionaryForKey:isExpectingReturnData:"
- "readCommissioningWindowStatusForSystemCommissionerPairingUUID:completionHandler:"
- "readCommissioningWindowStatusWithCompletionHandler:"
- "release"
- "remoteObjectInterface"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllDataWithError:"
- "removeAllDevicePairingsForSystemCommissionerPairingUUID:completionHandler:"
- "removeAllPairingsWithCompletionHandler:"
- "removeAllStoredValuesWithError:"
- "removeDataForKey:error:"
- "removeDevicePairingWithUUID:forSystemCommissionerPairingUUID:completionHandler:"
- "removeItemsMatchingQuery:error:"
- "removeObject:"
- "removePairingWithUUID:completionHandler:"
- "removeStoredValueForKey:error:"
- "removeSystemCommissionerPairingWithUUID:completionHandler:"
- "respondsToSelector:"
- "restrictedCharacteristicsAccessAllowed"
- "resultMatchingQuery:error:"
- "resume"
- "retain"
- "retainCount"
- "selectThreadNetworkFromScanResults:completionHandler:"
- "selectWiFiNetworkFromScanResults:completionHandler:"
- "self"
- "serialNumber"
- "serializedAsData"
- "set"
- "setAuthorizationServer:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConnection:"
- "setData:forKey:error:"
- "setDelegate:"
- "setDevicePairingServer:"
- "setDeviceSetupServer:"
- "setExecuteExtensionQueryHandler:"
- "setExportedInterface:"
- "setExportedObject:"
- "setExtensionProcess:"
- "setExtensionProcessFactory:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKeyedSubscript:"
- "setProductID:"
- "setRemoteObjectInterface:"
- "setSerialNumber:"
- "setStoredValue:forKey:error:"
- "setSystemCommissionerPairingServer:"
- "setUuid:"
- "setVendorID:"
- "setWithArray:"
- "setXpcConnection:"
- "shortDescription"
- "shouldAcceptXPCConnection:"
- "shouldShowDeviceWithUUID:vendorID:productID:serialNumber:"
- "shouldShowDeviceWithUUID:vendorID:productID:serialNumber:rootPublicKey:nodeID:"
- "showRestrictedCharacteristicsAccessWarningAlert"
- "showRestrictedCharacteristicsAccessWarningAlertWithClientProxy:"
- "start"
- "startWithError:"
- "storedValueForKey:"
- "storedValuesByKey"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "unarchivedObjectOfClass:fromData:error:"
- "updateItemMatchingQuery:withAttributes:error:"
- "v16@0:8"
- "v24@0:8@\"<MTSXPCListenerDelegate>\"16"
- "v24@0:8@\"MTSXPCClientProxy\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSXPCInterface\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?B>16"
- "v32@0:8@\"MTSDeviceCredential\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"MTSDeviceSetupHome\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"MTSDeviceSetupRequest\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"MTSXPCClientProxy\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"MTSXPCClientProxy\"16@?<v@?B>24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"MTSThreadNetworkAssociation\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"MTSWiFiNetworkAssociation\"@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8d16@?24"
- "v40@0:8@\"MTSXPCClientProxy\"16@\"MTSDeviceSetupRequest\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"MTSXPCClientProxy\"16@\"NSUUID\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"MTSXPCClientProxy\"16@\"NSUUID\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"MTSXPCClientProxy\"16@\"NSUUID\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"MTSDeviceSetupRoom\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSUUID\"16d24@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16d24@?32"
- "v48@0:8@\"MTSDeviceSetupHome\"16@\"NSString\"24@\"NSUUID\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"MTSXPCClientProxy\"16@\"NSUUID\"24@\"NSUUID\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"MTSXPCClientProxy\"16@\"NSUUID\"24d32@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24d32@?40"
- "validateDeviceCredential:completionHandler:"
- "valueForEntitlement:"
- "wrappedRequest"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
