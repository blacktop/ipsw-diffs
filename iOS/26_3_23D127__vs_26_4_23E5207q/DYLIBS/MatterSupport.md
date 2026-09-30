## MatterSupport

> `/System/Library/Frameworks/MatterSupport.framework/MatterSupport`

```diff

-1388.4.13.0.0
-  __TEXT.__text: 0x30e6c
-  __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_methlist: 0x1eb0
-  __TEXT.__const: 0x31f0
-  __TEXT.__cstring: 0x181e
-  __TEXT.__swift5_typeref: 0x979
+1418.5.4.0.0
+  __TEXT.__text: 0x2f788
+  __TEXT.__auth_stubs: 0x1060
+  __TEXT.__objc_methlist: 0x1cc0
+  __TEXT.__const: 0x3240
+  __TEXT.__swift5_typeref: 0x985
   __TEXT.__constg_swiftt: 0x74c
   __TEXT.__swift5_reflstr: 0x2ea
   __TEXT.__swift5_fieldmd: 0x78c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_proto: 0x2b8
+  __TEXT.__cstring: 0x1159
+  __TEXT.__swift5_proto: 0x2c0
   __TEXT.__swift5_types: 0xb8
   __TEXT.__swift5_capture: 0x254
-  __TEXT.__oslogstring: 0x22b5
+  __TEXT.__oslogstring: 0x1d44
   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x48
-  __TEXT.__gcc_except_tab: 0x170
-  __TEXT.__unwind_info: 0x1058
-  __TEXT.__eh_frame: 0x1120
-  __TEXT.__objc_classname: 0x694
-  __TEXT.__objc_methname: 0x304f
-  __TEXT.__objc_methtype: 0xedd
-  __TEXT.__objc_stubs: 0x1ee0
-  __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0x328
-  __DATA_CONST.__objc_classlist: 0x120
+  __TEXT.__gcc_except_tab: 0x168
+  __TEXT.__unwind_info: 0x1000
+  __TEXT.__eh_frame: 0x1178
+  __TEXT.__objc_classname: 0x756
+  __TEXT.__objc_methname: 0x2d19
+  __TEXT.__objc_methtype: 0xe20
+  __TEXT.__objc_stubs: 0x1cc0
+  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__const: 0x2f8
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x140
+  __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9c0
+  __DATA_CONST.__objc_selrefs: 0x908
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x878
-  __AUTH_CONST.__const: 0x1a20
-  __AUTH_CONST.__cfstring: 0x13e0
-  __AUTH_CONST.__objc_const: 0x3aa8
-  __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH.__objc_data: 0x9d8
+  __DATA_CONST.__objc_superrefs: 0xd8
+  __AUTH_CONST.__auth_got: 0x840
+  __AUTH_CONST.__const: 0x1a00
+  __AUTH_CONST.__cfstring: 0x11e0
+  __AUTH_CONST.__objc_const: 0x3770
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH.__objc_data: 0x938
   __AUTH.__data: 0x358
-  __DATA.__objc_ivar: 0x158
-  __DATA.__data: 0x14e8
-  __DATA.__bss: 0x5760
+  __DATA.__objc_ivar: 0x140
+  __DATA.__data: 0x13d0
+  __DATA.__bss: 0x5870
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FD9F3C67-2735-3D87-BA8D-BD51AD7E70C4
-  Functions: 1417
-  Symbols:   2424
-  CStrings:  1194
+  UUID: F520B745-48C9-3EB8-9FD0-A635748F9DE1
+  Functions: 1366
+  Symbols:   2284
+  CStrings:  1078
 
Symbols:
+ -[MTSSystemCommissionerPairing initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:]
+ GCC_except_table335
+ GCC_except_table405
+ GCC_except_table406
+ GCC_except_table438
+ GCC_except_table442
+ ___block_literal_global.1732
+ ___block_literal_global.2174
+ ___block_literal_global.2306
+ ___block_literal_global.394
+ ___block_literal_global.471
+ ___block_literal_global.564
+ ___block_literal_global.806
+ _logCategory._hmf_once_t13.2181
+ _logCategory._hmf_once_t16
+ _logCategory._hmf_once_v14.2182
+ _logCategory._hmf_once_v17
+ _objc_msgSend$initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:
+ _objectdestroy.35Tm
+ _symbolic _____Sg_ABt 13MatterSupport0A16AddDeviceRequestV0D8CriteriaO
- +[MTSNetworkCredentialManager logCategory]
- +[MTSNetworkCredentialManager threadCredentialManagementEndpoint:]
- +[MTSNetworkCredentialManager threadCredentialManagementImplicitlyEnabledForDeviceType:]
- +[MTSNetworkCredentialManager threadCredentialManagementSupportedForCommissionee:]
- +[MTSThreadNetworkCredential supportsSecureCoding]
- -[MTSNetworkCredentialManager .cxx_destruct]
- -[MTSNetworkCredentialManager dealloc]
- -[MTSNetworkCredentialManager initWithServerProxy:]
- -[MTSNetworkCredentialManager init]
- -[MTSNetworkCredentialManager retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]
- -[MTSNetworkCredentialManager retrievePreferredThreadCredentialsWithCompletionHandler:]
- -[MTSNetworkCredentialManager serverProxy]
- -[MTSNetworkCredentialManager setThreadCredentialManagementEnabled:forPairingWithUUID:completionHandler:]
- -[MTSSystemCommissionerPairing initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:threadCredentialManagementEnabled:]
- -[MTSSystemCommissionerPairing threadCredentialManagementEnabled]
- -[MTSThreadNetworkCredential .cxx_destruct]
- -[MTSThreadNetworkCredential borderAgentEUI]
- -[MTSThreadNetworkCredential borderAgentID]
- -[MTSThreadNetworkCredential copyWithZone:]
- -[MTSThreadNetworkCredential dataset]
- -[MTSThreadNetworkCredential encodeWithCoder:]
- -[MTSThreadNetworkCredential hash]
- -[MTSThreadNetworkCredential initWithCoder:]
- -[MTSThreadNetworkCredential initWithDataset:borderAgentEUI:borderAgentID:]
- -[MTSThreadNetworkCredential isEqual:]
- -[MTSXPCClientProxy hasThreadCredentialsEntitlement]
- -[MTSXPCClientProxy retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]
- -[MTSXPCClientProxy updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]
- -[MTSXPCServer clientProxy:retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]
- -[MTSXPCServer clientProxy:updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]
- -[MTSXPCServer networkCredentialServer]
- -[MTSXPCServer setNetworkCredentialServer:]
- -[MTSXPCServerProxy retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]
- -[MTSXPCServerProxy updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]
- GCC_except_table366
- GCC_except_table477
- GCC_except_table479
- GCC_except_table480
- GCC_except_table481
- _MTSXPCEntitlementNameThreadCredentials
- _OBJC_CLASS_$_MTSNetworkCredentialManager
- _OBJC_CLASS_$_MTSThreadNetworkCredential
- _OBJC_IVAR_$_MTSNetworkCredentialManager._serverProxy
- _OBJC_IVAR_$_MTSSystemCommissionerPairing._threadCredentialManagementEnabled
- _OBJC_IVAR_$_MTSThreadNetworkCredential._borderAgentEUI
- _OBJC_IVAR_$_MTSThreadNetworkCredential._borderAgentID
- _OBJC_IVAR_$_MTSThreadNetworkCredential._dataset
- _OBJC_IVAR_$_MTSXPCServer._networkCredentialServer
- _OBJC_METACLASS_$_MTSNetworkCredentialManager
- _OBJC_METACLASS_$_MTSThreadNetworkCredential
- __OBJC_$_CLASS_METHODS_MTSNetworkCredentialManager
- __OBJC_$_CLASS_METHODS_MTSThreadNetworkCredential
- __OBJC_$_CLASS_PROP_LIST_MTSThreadNetworkCredential
- __OBJC_$_INSTANCE_METHODS_MTSNetworkCredentialManager
- __OBJC_$_INSTANCE_METHODS_MTSThreadNetworkCredential
- __OBJC_$_INSTANCE_VARIABLES_MTSNetworkCredentialManager
- __OBJC_$_INSTANCE_VARIABLES_MTSThreadNetworkCredential
- __OBJC_$_PROP_LIST_MTSNetworkCredentialManager
- __OBJC_$_PROP_LIST_MTSThreadNetworkCredential
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTSNetworkCredentialServerInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTSXPCNetworkCredentialClientProxyDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_MTSNetworkCredentialServerInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_MTSXPCNetworkCredentialClientProxyDelegate
- __OBJC_CLASS_PROTOCOLS_$_MTSNetworkCredentialManager
- __OBJC_CLASS_PROTOCOLS_$_MTSThreadNetworkCredential
- __OBJC_CLASS_RO_$_MTSNetworkCredentialManager
- __OBJC_CLASS_RO_$_MTSThreadNetworkCredential
- __OBJC_LABEL_PROTOCOL_$_MTSNetworkCredentialClientInterface
- __OBJC_LABEL_PROTOCOL_$_MTSNetworkCredentialServerInterface
- __OBJC_LABEL_PROTOCOL_$_MTSXPCNetworkCredentialClientProxyDelegate
- __OBJC_METACLASS_RO_$_MTSNetworkCredentialManager
- __OBJC_METACLASS_RO_$_MTSThreadNetworkCredential
- __OBJC_PROTOCOL_$_MTSNetworkCredentialClientInterface
- __OBJC_PROTOCOL_$_MTSNetworkCredentialServerInterface
- __OBJC_PROTOCOL_$_MTSXPCNetworkCredentialClientProxyDelegate
- ___103-[MTSNetworkCredentialManager retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]_block_invoke
- ___105-[MTSNetworkCredentialManager setThreadCredentialManagementEnabled:forPairingWithUUID:completionHandler:]_block_invoke
- ___112-[MTSXPCServerProxy updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]_block_invoke
- ___42+[MTSNetworkCredentialManager logCategory]_block_invoke
- ___87-[MTSNetworkCredentialManager retrievePreferredThreadCredentialsWithCompletionHandler:]_block_invoke
- ___93-[MTSXPCServerProxy retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]_block_invoke
- ___block_descriptor_56_e8_32s40s48bs_e48_v24?0"MTSThreadNetworkCredential"8"NSError"16ls32l8s40l8s48l8
- ___block_literal_global.1430
- ___block_literal_global.1953
- ___block_literal_global.2403
- ___block_literal_global.2535
- ___block_literal_global.406
- ___block_literal_global.483
- ___block_literal_global.573
- ___block_literal_global.824
- _logCategory._hmf_once_t15.2409
- _logCategory._hmf_once_t18
- _logCategory._hmf_once_t9
- _logCategory._hmf_once_v10
- _logCategory._hmf_once_v16.2410
- _logCategory._hmf_once_v19
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$borderAgentEUI
- _objc_msgSend$borderAgentID
- _objc_msgSend$children
- _objc_msgSend$clientProxy:retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:
- _objc_msgSend$clientProxy:updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:
- _objc_msgSend$dataset
- _objc_msgSend$deviceTypeID
- _objc_msgSend$deviceTypes
- _objc_msgSend$endpointID
- _objc_msgSend$hasThreadCredentialsEntitlement
- _objc_msgSend$initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:threadCredentialManagementEnabled:
- _objc_msgSend$networkCredentialServer
- _objc_msgSend$numberWithBool:
- _objc_msgSend$retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:
- _objc_msgSend$rootEndpoint
- _objc_msgSend$threadCredentialManagementEnabled
- _objc_msgSend$threadCredentialManagementEndpoint:
- _objc_msgSend$updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
- _objectdestroy.31Tm
CStrings:
+ "MTDeviceSetupRequestFactory"
+ "S"
+ "initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:"
- "\t"
- "!borderAgentEUI || isValidBorderAgentEUI(borderAgentEUI)"
- "!borderAgentID || isValidBorderAgentID(borderAgentID)"
- "%{public}@Disallowing retrieve preferred Thread credentials because %@"
- "%{public}@Disallowing update Thread credential management status request because %@"
- "%{public}@Failed to decode MTSThreadNetworkCredentialBorderAgentEUICodingKey"
- "%{public}@Failed to decode MTSThreadNetworkCredentialBorderAgentIDCodingKey"
- "%{public}@Failed to decode MTSThreadNetworkCredentialOperationalDatasetCodingKey"
- "%{public}@Failed to obtain remote object proxy for retrieve preferred Thread credentials: %@"
- "%{public}@Failed to obtain remote object proxy for set Thread credential management state: %@"
- "%{public}@Missing endpoint information, MTRCommissioningParameters.readEndpointInformation == NO?"
- "%{public}@[%{public}@] %@ Thread credential management for system commissioner pairing with UUID: %@"
- "%{public}@[%{public}@] Failed to retrieve or create preferred Thread credentials: %@"
- "%{public}@[%{public}@] Failed to retrieve preferred Thread credentials: %@"
- "%{public}@[%{public}@] Failed to update Thread credential management status: %@"
- "%{public}@[%{public}@] Retrieving or creating preferred Thread credentials"
- "%{public}@[%{public}@] Retrieving preferred Thread credentials"
- "%{public}@[%{public}@] Successfully retrieved or created preferred Thread credentials"
- "%{public}@[%{public}@] Successfully retrieved preferred Thread credentials"
- "%{public}@[%{public}@] Successfully update Thread credential management status"
- "@\"<MTSNetworkCredentialServerInterface>\""
- "@88@0:8@16@24@32@40@48@56@64@72@80"
- "Disabling"
- "Enabling"
- "I"
- "MTSNetworkCredentialClientInterface"
- "MTSNetworkCredentialManager"
- "MTSNetworkCredentialServerInterface"
- "MTSSCP.threadCM"
- "MTSThreadNetworkCredential"
- "MTSXPCNetworkCredentialClientProxyDelegate"
- "Retrieve or create preferred Thread credentials"
- "Retrieve preferred Thread credentials"
- "T@\"<MTSNetworkCredentialServerInterface>\",W,V_networkCredentialServer"
- "T@\"NSData\",R,C,V_borderAgentEUI"
- "T@\"NSData\",R,C,V_borderAgentID"
- "T@\"NSData\",R,C,V_dataset"
- "T@\"NSNumber\",R,V_threadCredentialManagementEnabled"
- "Thread Credential Management"
- "Update Thread credential management status"
- "_borderAgentEUI"
- "_borderAgentID"
- "_dataset"
- "_networkCredentialServer"
- "_threadCredentialManagementEnabled"
- "ba"
- "borderAgentEUI"
- "borderAgentID"
- "c"
- "children"
- "clientProxy:retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:"
- "clientProxy:updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:"
- "com.apple.matter.support.xpc.thread-credentials"
- "dataset"
- "deviceTypeID"
- "deviceTypes"
- "ds"
- "endpointID"
- "hasThreadCredentialsEntitlement"
- "id"
- "initWithDataset:borderAgentEUI:borderAgentID:"
- "initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:threadCredentialManagementEnabled:"
- "networkCredentialServer"
- "numberWithBool:"
- "retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:"
- "retrievePreferredThreadCredentialsWithCompletionHandler:"
- "rootEndpoint"
- "setNetworkCredentialServer:"
- "setThreadCredentialManagementEnabled:forPairingWithUUID:completionHandler:"
- "system.commissioner.network.credential.manager"
- "systemCommissionerPairingUUID"
- "threadCredentialManagementEnabled"
- "threadCredentialManagementEndpoint:"
- "threadCredentialManagementImplicitlyEnabledForDeviceType:"
- "threadCredentialManagementSupportedForCommissionee:"
- "updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:"
- "v24@?0@\"MTSThreadNetworkCredential\"8@\"NSError\"16"
- "v32@0:8@\"NSData\"16@?<v@?@\"MTSThreadNetworkCredential\"@\"NSError\">24"
- "v36@0:8B16@\"NSUUID\"20@?<v@?@\"NSError\">28"
- "v36@0:8B16@20@?28"
- "v40@0:8@\"MTSXPCClientProxy\"16@\"NSData\"24@?<v@?@\"MTSThreadNetworkCredential\"@\"NSError\">32"
- "v44@0:8@\"MTSXPCClientProxy\"16B24@\"NSUUID\"28@?<v@?@\"NSError\">36"
- "v44@0:8@16B24@28@?36"

```
