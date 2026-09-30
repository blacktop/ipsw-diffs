## MatterSupport

> `/System/Library/Frameworks/MatterSupport.framework/MatterSupport`

```diff

-1340.3.0.0.0
-  __TEXT.__text: 0x2e788
+1345.1.0.1.1
+  __TEXT.__text: 0x30340
   __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_methlist: 0x1cb8
+  __TEXT.__objc_methlist: 0x1ea0
   __TEXT.__const: 0x2fa0
-  __TEXT.__cstring: 0x162d
+  __TEXT.__cstring: 0x17b5
   __TEXT.__swift5_typeref: 0x979
   __TEXT.__constg_swiftt: 0x74c
   __TEXT.__swift5_reflstr: 0x2ea

   __TEXT.__swift5_proto: 0x2b8
   __TEXT.__swift5_types: 0xb8
   __TEXT.__swift5_capture: 0x254
-  __TEXT.__oslogstring: 0x1d44
+  __TEXT.__oslogstring: 0x2173
   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__gcc_except_tab: 0x170
-  __TEXT.__unwind_info: 0x1008
+  __TEXT.__unwind_info: 0x1060
   __TEXT.__eh_frame: 0x1120
-  __TEXT.__objc_classname: 0x5e8
-  __TEXT.__objc_methname: 0x2b5d
-  __TEXT.__objc_methtype: 0xd66
-  __TEXT.__objc_stubs: 0x1ca0
-  __DATA_CONST.__got: 0x368
-  __DATA_CONST.__const: 0x300
-  __DATA_CONST.__objc_classlist: 0x110
+  __TEXT.__objc_classname: 0x694
+  __TEXT.__objc_methname: 0x2fbb
+  __TEXT.__objc_methtype: 0xeee
+  __TEXT.__objc_stubs: 0x1ec0
+  __DATA_CONST.__got: 0x370
+  __DATA_CONST.__const: 0x330
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x128
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x900
+  __DATA_CONST.__objc_selrefs: 0x9b0
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0xe8
   __AUTH_CONST.__auth_got: 0x878
-  __AUTH_CONST.__const: 0x1a00
-  __AUTH_CONST.__cfstring: 0x11e0
-  __AUTH_CONST.__objc_const: 0x3770
-  __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0x938
+  __AUTH_CONST.__const: 0x1a20
+  __AUTH_CONST.__cfstring: 0x1380
+  __AUTH_CONST.__objc_const: 0x3a78
+  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH.__objc_data: 0x9d8
   __AUTH.__data: 0x358
-  __DATA.__objc_ivar: 0x140
-  __DATA.__data: 0x13c8
-  __DATA.__bss: 0x5750
+  __DATA.__objc_ivar: 0x154
+  __DATA.__data: 0x14e8
+  __DATA.__bss: 0x5780
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
+  - /System/Library/PrivateFrameworks/HomeKitFeatures.framework/HomeKitFeatures
   - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 80673B9C-A883-3235-A934-BC9268B79664
-  Functions: 1377
-  Symbols:   2288
-  CStrings:  1095
+  UUID: 0BB4FFC1-563D-3369-8509-897A56B5064F
+  Functions: 1414
+  Symbols:   2418
+  CStrings:  1182
 
Symbols:
+ +[MTSNetworkCredentialManager logCategory]
+ +[MTSNetworkCredentialManager threadCredentialManagementEndpoint:]
+ +[MTSNetworkCredentialManager threadCredentialManagementSupportedForCommissionee:]
+ +[MTSThreadNetworkCredential supportsSecureCoding]
+ -[MTSNetworkCredentialManager .cxx_destruct]
+ -[MTSNetworkCredentialManager dealloc]
+ -[MTSNetworkCredentialManager initWithServerProxy:]
+ -[MTSNetworkCredentialManager init]
+ -[MTSNetworkCredentialManager retrievePreferredThreadCredentialsWithCompletionHandler:]
+ -[MTSNetworkCredentialManager retrievePreferredThreadCredentialsWithOptions:completionHandler:]
+ -[MTSNetworkCredentialManager serverProxy]
+ -[MTSNetworkCredentialManager setThreadCredentialManagementEnabled:forPairingWithUUID:completionHandler:]
+ -[MTSSystemCommissionerPairing initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:threadCredentialManagementEnabled:]
+ -[MTSSystemCommissionerPairing threadCredentialManagementEnabled]
+ -[MTSThreadNetworkCredential .cxx_destruct]
+ -[MTSThreadNetworkCredential borderAgentEUI]
+ -[MTSThreadNetworkCredential copyWithZone:]
+ -[MTSThreadNetworkCredential dataset]
+ -[MTSThreadNetworkCredential encodeWithCoder:]
+ -[MTSThreadNetworkCredential hash]
+ -[MTSThreadNetworkCredential initWithCoder:]
+ -[MTSThreadNetworkCredential initWithDataset:borderAgentEUI:]
+ -[MTSThreadNetworkCredential isEqual:]
+ -[MTSXPCClientProxy hasEntitlement:]
+ -[MTSXPCClientProxy hasThreadCredentialsEntitlement]
+ -[MTSXPCClientProxy retrievePreferredThreadCredentialsWithOptions:completionHandler:]
+ -[MTSXPCClientProxy updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]
+ -[MTSXPCServer clientProxy:retrievePreferredThreadCredentialsWithOptions:completionHandler:]
+ -[MTSXPCServer clientProxy:updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]
+ -[MTSXPCServer networkCredentialServer]
+ -[MTSXPCServer setNetworkCredentialServer:]
+ -[MTSXPCServerProxy retrievePreferredThreadCredentialsWithOptions:completionHandler:]
+ -[MTSXPCServerProxy updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]
+ GCC_except_table363
+ GCC_except_table438
+ GCC_except_table474
+ GCC_except_table476
+ GCC_except_table477
+ GCC_except_table478
+ _MTSXPCEntitlementNameThreadCredentials
+ _OBJC_CLASS_$_MTSNetworkCredentialManager
+ _OBJC_CLASS_$_MTSThreadNetworkCredential
+ _OBJC_IVAR_$_MTSNetworkCredentialManager._serverProxy
+ _OBJC_IVAR_$_MTSSystemCommissionerPairing._threadCredentialManagementEnabled
+ _OBJC_IVAR_$_MTSThreadNetworkCredential._borderAgentEUI
+ _OBJC_IVAR_$_MTSThreadNetworkCredential._dataset
+ _OBJC_IVAR_$_MTSXPCServer._networkCredentialServer
+ _OBJC_METACLASS_$_MTSNetworkCredentialManager
+ _OBJC_METACLASS_$_MTSThreadNetworkCredential
+ __OBJC_$_CLASS_METHODS_MTSNetworkCredentialManager
+ __OBJC_$_CLASS_METHODS_MTSThreadNetworkCredential
+ __OBJC_$_CLASS_PROP_LIST_MTSThreadNetworkCredential
+ __OBJC_$_INSTANCE_METHODS_MTSNetworkCredentialManager
+ __OBJC_$_INSTANCE_METHODS_MTSThreadNetworkCredential
+ __OBJC_$_INSTANCE_VARIABLES_MTSNetworkCredentialManager
+ __OBJC_$_INSTANCE_VARIABLES_MTSThreadNetworkCredential
+ __OBJC_$_PROP_LIST_MTSNetworkCredentialManager
+ __OBJC_$_PROP_LIST_MTSThreadNetworkCredential
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
+ ___105-[MTSNetworkCredentialManager setThreadCredentialManagementEnabled:forPairingWithUUID:completionHandler:]_block_invoke
+ ___112-[MTSXPCServerProxy updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]_block_invoke
+ ___42+[MTSNetworkCredentialManager logCategory]_block_invoke
+ ___85-[MTSXPCServerProxy retrievePreferredThreadCredentialsWithOptions:completionHandler:]_block_invoke
+ ___95-[MTSNetworkCredentialManager retrievePreferredThreadCredentialsWithOptions:completionHandler:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48bs_e48_v24?0"MTSThreadNetworkCredential"8"NSError"16ls32l8s40l8s48l8
+ ___block_literal_global.1415
+ ___block_literal_global.1938
+ ___block_literal_global.2389
+ ___block_literal_global.2525
+ ___block_literal_global.401
+ ___block_literal_global.479
+ ___block_literal_global.568
+ ___block_literal_global.821
+ _logCategory._hmf_once_t15.2395
+ _logCategory._hmf_once_t18
+ _logCategory._hmf_once_t6.1414
+ _logCategory._hmf_once_v16.2396
+ _logCategory._hmf_once_v19
+ _logCategory._hmf_once_v7.1416
+ _objc_msgSend$borderAgentEUI
+ _objc_msgSend$children
+ _objc_msgSend$clientProxy:retrievePreferredThreadCredentialsWithOptions:completionHandler:
+ _objc_msgSend$clientProxy:updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:
+ _objc_msgSend$dataset
+ _objc_msgSend$deviceTypeID
+ _objc_msgSend$deviceTypes
+ _objc_msgSend$endpointID
+ _objc_msgSend$hasEntitlement:
+ _objc_msgSend$hasThreadCredentialsEntitlement
+ _objc_msgSend$initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:threadCredentialManagementEnabled:
+ _objc_msgSend$networkCredentialServer
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$retrievePreferredThreadCredentialsWithOptions:completionHandler:
+ _objc_msgSend$rootEndpoint
+ _objc_msgSend$threadCredentialManagementEnabled
+ _objc_msgSend$threadCredentialManagementEndpoint:
+ _objc_msgSend$updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:
- -[MTSSystemCommissionerPairing initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:]
- GCC_except_table334
- GCC_except_table404
- GCC_except_table405
- GCC_except_table439
- GCC_except_table440
- GCC_except_table441
- ___block_literal_global.1729
- ___block_literal_global.2170
- ___block_literal_global.2302
- ___block_literal_global.394
- ___block_literal_global.471
- ___block_literal_global.563
- ___block_literal_global.804
- _logCategory._hmf_once_t13.2177
- _logCategory._hmf_once_t16
- _logCategory._hmf_once_v14.2178
- _logCategory._hmf_once_v17
- _objc_msgSend$initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:
CStrings:
+ "\t"
+ "!borderAgentEUI || isValidBorderAgentEUI(borderAgentEUI)"
+ "%{public}@Disallowing retrieve preferred Thread credentials because %@"
+ "%{public}@Disallowing update Thread credential management status request because %@"
+ "%{public}@Failed to decode MTSThreadNetworkCredentialBorderAgentEUICodingKey"
+ "%{public}@Failed to decode MTSThreadNetworkCredentialOperationalDatasetCodingKey"
+ "%{public}@Failed to obtain remote object proxy for retrieve preferred Thread credentials: %@"
+ "%{public}@Failed to obtain remote object proxy for set Thread credential management state: %@"
+ "%{public}@Missing endpoint information, MTRCommissioningParameters.readEndpointInformation == NO?"
+ "%{public}@[%{public}@] %@ Thread credential management for system commissioner pairing with UUID: %@"
+ "%{public}@[%{public}@] Failed to retrieve preferred Thread credentials: %@"
+ "%{public}@[%{public}@] Failed to update Thread credential management status: %@"
+ "%{public}@[%{public}@] Retrieving preferred Thread credentials"
+ "%{public}@[%{public}@] Successfully retrieved preferred Thread credentials"
+ "%{public}@[%{public}@] Successfully update Thread credential management status"
+ "@\"<MTSNetworkCredentialServerInterface>\""
+ "@88@0:8@16@24@32@40@48@56@64@72@80"
+ "Disabling"
+ "Enabling"
+ "I"
+ "MTSNetworkCredentialClientInterface"
+ "MTSNetworkCredentialManager"
+ "MTSNetworkCredentialServerInterface"
+ "MTSSCP.threadCM"
+ "MTSThreadNetworkCredential"
+ "MTSXPCNetworkCredentialClientProxyDelegate"
+ "Retrieve preferred Thread credentials"
+ "T@\"<MTSNetworkCredentialServerInterface>\",W,V_networkCredentialServer"
+ "T@\"NSData\",R,C,V_borderAgentEUI"
+ "T@\"NSData\",R,C,V_dataset"
+ "T@\"NSNumber\",R,V_threadCredentialManagementEnabled"
+ "Thread Credential Management"
+ "Update Thread credential management status"
+ "_borderAgentEUI"
+ "_dataset"
+ "_networkCredentialServer"
+ "_threadCredentialManagementEnabled"
+ "ba"
+ "borderAgentEUI"
+ "c"
+ "children"
+ "clientProxy:retrievePreferredThreadCredentialsWithOptions:completionHandler:"
+ "clientProxy:updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:"
+ "com.apple.matter.support.xpc.thread-credentials"
+ "dataset"
+ "deviceTypeID"
+ "deviceTypes"
+ "ds"
+ "endpointID"
+ "hasEntitlement:"
+ "hasThreadCredentialsEntitlement"
+ "initWithDataset:borderAgentEUI:"
+ "initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:threadCredentialManagementEnabled:"
+ "networkCredentialServer"
+ "numberWithBool:"
+ "retrievePreferredThreadCredentialsWithCompletionHandler:"
+ "retrievePreferredThreadCredentialsWithOptions:completionHandler:"
+ "rootEndpoint"
+ "setNetworkCredentialServer:"
+ "setThreadCredentialManagementEnabled:forPairingWithUUID:completionHandler:"
+ "system.commissioner.network.credential.manager"
+ "systemCommissionerPairingUUID"
+ "threadCredentialManagementEnabled"
+ "threadCredentialManagementEndpoint:"
+ "threadCredentialManagementSupportedForCommissionee:"
+ "updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:"
+ "v24@?0@\"MTSThreadNetworkCredential\"8@\"NSError\"16"
+ "v32@0:8Q16@?24"
+ "v32@0:8Q16@?<v@?@\"MTSThreadNetworkCredential\"@\"NSError\">24"
+ "v36@0:8B16@\"NSUUID\"20@?<v@?@\"NSError\">28"
+ "v36@0:8B16@20@?28"
+ "v40@0:8@\"MTSXPCClientProxy\"16Q24@?<v@?@\"MTSThreadNetworkCredential\"@\"NSError\">32"
+ "v40@0:8@16Q24@?32"
+ "v44@0:8@\"MTSXPCClientProxy\"16B24@\"NSUUID\"28@?<v@?@\"NSError\">36"
+ "v44@0:8@16B24@28@?36"
- "S"
- "initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:"

```
