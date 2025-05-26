## AppStoreDaemon

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon`

```diff

-10.3.4.0.0
-  __TEXT.__text: 0x75ae8
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x8cb4
-  __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x4f94
-  __TEXT.__oslogstring: 0x4056
-  __TEXT.__gcc_except_tab: 0x960
+10.4.34.2.1
+  __TEXT.__text: 0x78cb8
+  __TEXT.__auth_stubs: 0xba0
+  __TEXT.__objc_methlist: 0x8ebc
+  __TEXT.__const: 0x150
+  __TEXT.__cstring: 0x51c2
+  __TEXT.__swift5_typeref: 0xe
+  __TEXT.__constg_swiftt: 0x28
+  __TEXT.__swift5_reflstr: 0x31
+  __TEXT.__swift5_fieldmd: 0x28
+  __TEXT.__swift5_proto: 0xc
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__oslogstring: 0x414c
+  __TEXT.__gcc_except_tab: 0x99c
   __TEXT.__dlopen_cstrs: 0xb1
-  __TEXT.__unwind_info: 0x22dc
-  __TEXT.__objc_classname: 0x17ea
-  __TEXT.__objc_methname: 0x12954
-  __TEXT.__objc_methtype: 0x2f44
-  __TEXT.__objc_stubs: 0x7fa0
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x2558
-  __DATA_CONST.__objc_classlist: 0x5b0
+  __TEXT.__unwind_info: 0x24e0
+  __TEXT.__objc_classname: 0x1868
+  __TEXT.__objc_methname: 0x12d72
+  __TEXT.__objc_methtype: 0x3099
+  __TEXT.__objc_stubs: 0x8120
+  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__const: 0x2578
+  __DATA_CONST.__objc_classlist: 0x5c8
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x208
+  __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x110c8
-  __DATA_CONST.__objc_selrefs: 0x3c60
+  __DATA_CONST.__objc_const: 0x114a0
+  __DATA_CONST.__objc_selrefs: 0x3d58
+  __DATA_CONST.__objc_protorefs: 0x150
+  __DATA_CONST.__objc_classrefs: 0x5a8
+  __DATA_CONST.__objc_superrefs: 0x460
   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__objc_const: 0x5ac8
-  __AUTH_CONST.__cfstring: 0x62e0
-  __AUTH_CONST.__const: 0x740
+  __AUTH_CONST.__const: 0x820
+  __AUTH_CONST.__objc_const: 0x5c30
+  __AUTH_CONST.__cfstring: 0x6440
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x560
-  __AUTH.__objc_data: 0x18b0
-  __DATA.__objc_protorefs: 0x140
-  __DATA.__objc_classrefs: 0x590
-  __DATA.__objc_superrefs: 0x458
-  __DATA.__objc_ivar: 0xc0c
-  __DATA.__data: 0x1878
-  __DATA.__bss: 0x10
+  __AUTH_CONST.__auth_got: 0x5e0
+  __AUTH.__objc_data: 0x19a0
+  __DATA.__objc_ivar: 0xc28
+  __DATA.__data: 0x1940
+  __DATA.__bss: 0x190
   __DATA_DIRTY.__objc_ivar: 0x1ac
   __DATA_DIRTY.__objc_data: 0x2030
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x270
-  __DATA_DIRTY.__common: 0x150
+  __DATA_DIRTY.__bss: 0x280
+  __DATA_DIRTY.__common: 0x158
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/Bom.framework/Bom
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDarwin.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3932
-  Symbols:   12327
-  CStrings:  5192
+  Functions: 4093
+  Symbols:   12590
+  CStrings:  5273
 
Symbols:
+ +[ASDAppCapabilities _isCapable:method:]
+ +[ASDAppCapabilities interface]
+ +[ASDAppCapabilities isCapable:]
+ +[ASDAppCapabilities isCapableOfAction:capabilities:]
+ +[ASDAppCapabilities isCapableOfAction:capability:]
+ +[ASDAppCapabilityMetadata metadataWithAction:bundleID:capabilities:]
+ +[ASDAppCapabilityMetadata metadataWithAction:entitlements:infoPlist:]
+ +[ASDAppCapabilityMetadata supportsSecureCoding]
+ +[SKANInteropService interface]
+ +[SKANInteropService sharedInstance]
+ -[ASDApp hasUnknownDistributor]
+ -[ASDAppCapabilityMetadata .cxx_destruct]
+ -[ASDAppCapabilityMetadata action]
+ -[ASDAppCapabilityMetadata bundleID]
+ -[ASDAppCapabilityMetadata copyWithZone:]
+ -[ASDAppCapabilityMetadata description]
+ -[ASDAppCapabilityMetadata encodeWithCoder:]
+ -[ASDAppCapabilityMetadata features]
+ -[ASDAppCapabilityMetadata initWithCoder:]
+ -[ASDAppCapabilityMetadata setAction:]
+ -[ASDAppCapabilityMetadata setBundleID:]
+ -[ASDAppCapabilityMetadata setFeatures:]
+ -[ASDAppCapabilityMetadata setSupportsFeatureA:]
+ -[ASDAppCapabilityMetadata setSupportsFeatureB:]
+ -[ASDAppCapabilityMetadata setSupportsFeatureC:]
+ -[ASDAppCapabilityMetadata supportsFeatureA]
+ -[ASDAppCapabilityMetadata supportsFeatureB]
+ -[ASDAppCapabilityMetadata supportsFeatureC]
+ -[ASDInstallAttributionParamsConfig interactionType]
+ -[ASDInstallAttributionParamsConfig setInteractionType:]
+ -[ASDPurchase appCapabilities]
+ -[ASDPurchase setAppCapabilities:]
+ -[ASDPurchaseManager processPurchases:withResponseHandler:]
+ -[ASDServiceBroker getCapabilitiesServiceWithError:]
+ -[ASDServiceBroker getSKANInteropServiceWithCompletionHandler:]
+ -[ASDTestFlightAppMetadata setToken:]
+ -[ASDTestFlightAppMetadata token]
+ -[SKANInteropService .cxx_destruct]
+ -[SKANInteropService getImpressionsForApp:completionHandler:]
+ -[SKANInteropService storePostbacks:completionHandler:]
+ GCC_except_table10
+ GCC_except_table17
+ GCC_except_table23
+ GCC_except_table24
+ GCC_except_table33
+ GCC_except_table37
+ GCC_except_table43
+ GCC_except_table52
+ GCC_except_table61
+ GCC_except_table70
+ GCC_except_table86
+ GCC_except_table89
+ GCC_except_table92
+ _ASDAppCapabilitiesDidChangeNotification
+ _ASDInstallAttributionInteractionTypeClick
+ _ASDInstallAttributionInteractionTypeView
+ _ASD_LOG_ACTIVITY
+ _ASD_LOG_APPINSTALL
+ _ASD_LOG_APPUSAGE
+ _ASD_LOG_APP_CAPABILITIES
+ _ASD_LOG_ARCADE
+ _ASD_LOG_CLEANUP
+ _ASD_LOG_CLIPS
+ _ASD_LOG_DAAP
+ _ASD_LOG_DAEMON
+ _ASD_LOG_DOWNLOAD
+ _ASD_LOG_EVENTS_EXT
+ _ASD_LOG_EXTENSION
+ _ASD_LOG_FRAMEWORK
+ _ASD_LOG_GENERAL
+ _ASD_LOG_LIBRARY
+ _ASD_LOG_METRICS
+ _ASD_LOG_MIGRATE
+ _ASD_LOG_OCTANE
+ _ASD_LOG_ODR
+ _ASD_LOG_OFFLOADING
+ _ASD_LOG_OVERSIZE
+ _ASD_LOG_PERFORMANCE
+ _ASD_LOG_PRIVTASK
+ _ASD_LOG_PROGRESS
+ _ASD_LOG_PURCHASE
+ _ASD_LOG_PUSH
+ _ASD_LOG_REPAIR
+ _ASD_LOG_RESTORE
+ _ASD_LOG_SCHEDULER
+ _ASD_LOG_SIGNPOST
+ _ASD_LOG_SKADNETWORK
+ _ASD_LOG_SKANNER
+ _ASD_LOG_SOFTWAREMAP
+ _ASD_LOG_SQL
+ _ASD_LOG_STOREKIT
+ _ASD_LOG_SUB
+ _ASD_LOG_TESTFLIGHT
+ _ASD_LOG_TESTFLIGHT_EXT
+ _ASD_LOG_UPDATES
+ _ASD_LOG_VPP
+ _ASD_LOG_XDC
+ _OBJC_CLASS_$_ASDAppCapabilities
+ _OBJC_CLASS_$_ASDAppCapabilityMetadata
+ _OBJC_CLASS_$_SKANInteropService
+ _OBJC_IVAR_$_ASDAppCapabilityMetadata._action
+ _OBJC_IVAR_$_ASDAppCapabilityMetadata._bundleID
+ _OBJC_IVAR_$_ASDAppCapabilityMetadata._features
+ _OBJC_IVAR_$_ASDAppCapabilityMetadata._supportsFeatureC
+ _OBJC_IVAR_$_ASDInstallAttributionParamsConfig._interactionType
+ _OBJC_IVAR_$_ASDPurchase._appCapabilities
+ _OBJC_IVAR_$_ASDTestFlightAppMetadata._token
+ _OBJC_IVAR_$_SKANInteropService._serviceBroker
+ _OBJC_METACLASS_$_ASDAppCapabilities
+ _OBJC_METACLASS_$_ASDAppCapabilityMetadata
+ _OBJC_METACLASS_$_SKANInteropService
+ __OBJC_$_CLASS_METHODS_ASDAppCapabilities
+ __OBJC_$_CLASS_METHODS_ASDAppCapabilityMetadata
+ __OBJC_$_CLASS_METHODS_SKANInteropService
+ __OBJC_$_CLASS_PROP_LIST_ASDAppCapabilityMetadata
+ __OBJC_$_CLASS_PROP_LIST_SKANInteropService
+ __OBJC_$_INSTANCE_METHODS_ASDAppCapabilityMetadata
+ __OBJC_$_INSTANCE_METHODS_SKANInteropService
+ __OBJC_$_INSTANCE_VARIABLES_ASDAppCapabilityMetadata
+ __OBJC_$_INSTANCE_VARIABLES_SKANInteropService
+ __OBJC_$_PROP_LIST_ASDAppCapabilities
+ __OBJC_$_PROP_LIST_ASDAppCapabilityMetadata
+ __OBJC_$_PROP_LIST_SKANInteropService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASDAppCapabilitiesServiceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SKANInteropServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASDAppCapabilitiesServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SKANInteropServiceProtocol
+ __OBJC_$_PROTOCOL_REFS_ASDAppCapabilitiesServiceProtocol
+ __OBJC_CLASS_PROTOCOLS_$_ASDAppCapabilities
+ __OBJC_CLASS_PROTOCOLS_$_ASDAppCapabilityMetadata
+ __OBJC_CLASS_PROTOCOLS_$_SKANInteropService
+ __OBJC_CLASS_RO_$_ASDAppCapabilities
+ __OBJC_CLASS_RO_$_ASDAppCapabilityMetadata
+ __OBJC_CLASS_RO_$_SKANInteropService
+ __OBJC_LABEL_PROTOCOL_$_ASDAppCapabilitiesServiceProtocol
+ __OBJC_LABEL_PROTOCOL_$_SKANInteropServiceProtocol
+ __OBJC_METACLASS_RO_$_ASDAppCapabilities
+ __OBJC_METACLASS_RO_$_ASDAppCapabilityMetadata
+ __OBJC_METACLASS_RO_$_SKANInteropService
+ __OBJC_PROTOCOL_$_ASDAppCapabilitiesServiceProtocol
+ __OBJC_PROTOCOL_$_SKANInteropServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ASDAppCapabilitiesServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_SKANInteropServiceProtocol
+ ___33-[ASDJobManager _setupConnection]_block_invoke.130
+ ___36+[SKANInteropService sharedInstance]_block_invoke
+ ___40+[ASDAppCapabilities _isCapable:method:]_block_invoke
+ ___40+[ASDAppCapabilities _isCapable:method:]_block_invoke.48
+ ___40-[ASDCheckQueueRequest _setupConnection]_block_invoke.74
+ ___43-[ASDSoftwareUpdatesStore _setupConnection]_block_invoke.141
+ ___47-[ASDClaimApplicationsRequest _setupConnection]_block_invoke.71
+ ___47-[ASDDiagnosticService activeClientsWithError:]_block_invoke_2
+ ___48-[ASDManagedApplicationRequest _setupConnection]_block_invoke.71
+ ___52-[ASDServiceBroker getCapabilitiesServiceWithError:]_block_invoke
+ ___52-[ASDServiceBroker getCapabilitiesServiceWithError:]_block_invoke_2
+ ___55-[SKANInteropService storePostbacks:completionHandler:]_block_invoke
+ ___55-[SKANInteropService storePostbacks:completionHandler:]_block_invoke_2
+ ___57-[ASDFairPlayService generateKeybagRequestForDSID:error:]_block_invoke_2
+ ___59-[ASDPurchaseManager processPurchases:withResponseHandler:]_block_invoke
+ ___59-[ASDPurchaseManager processPurchases:withResponseHandler:]_block_invoke_2
+ ___59-[ASDPurchaseManager processPurchases:withResponseHandler:]_block_invoke_3
+ ___61-[SKANInteropService getImpressionsForApp:completionHandler:]_block_invoke
+ ___61-[SKANInteropService getImpressionsForApp:completionHandler:]_block_invoke_2
+ ___63-[ASDServiceBroker getSKANInteropServiceWithCompletionHandler:]_block_invoke
+ ___68+[ASDInstallApps _installApps:onPairedDevice:withCompletionHandler:]_block_invoke.84
+ ___68+[ASDInstallApps _installApps:onPairedDevice:withCompletionHandler:]_block_invoke.92
+ ___block_descriptor_48_e8_32r40r_e28_v24?0"NSData"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e77_v24?0"<ASDAppCapabilitiesServiceProtocol><NSXPCProxyCreating>"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e70_v24?0"<SKANInteropServiceProtocol><NSXPCProxyCreating>"8"NSError"16ls40l8s32l8
+ ___block_literal_global.140
+ ___block_literal_global.143
+ ___block_literal_global.18
+ ___block_literal_global.73
+ ___block_literal_global.76
+ ___swift_memcpy1_1
+ ___swift_noop_void_return
+ __unnamed_array_storage.29
+ _associated conformance 14AppStoreDaemon11FeatureFlagOSHAASQ
+ _objc_allocWithZone
+ _objc_msgSend$getAppCapabilitiesServiceWithReplyHandler:
+ _objc_msgSend$getCapabilitiesServiceWithError:
+ _objc_msgSend$getImpressionsForApp:completionHandler:
+ _objc_msgSend$getSKANInteropServiceWithCompletionHandler:
+ _objc_msgSend$getSKANInteropServiceWithReplyHandler:
+ _objc_msgSend$hasUnknownDistributor
+ _objc_msgSend$isCapable:withCompletionHandler:
+ _objc_msgSend$metadataWithAction:bundleID:capabilities:
+ _objc_msgSend$processPurchases:withReplyHandler:
+ _objc_msgSend$setAction:
+ _objc_msgSend$setFeatures:
+ _objc_msgSend$storePostbacks:completionHandler:
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_getWitnessTable
+ _symbolic _____ 14AppStoreDaemon11FeatureFlagO
- -[ASDUpdatesService hasEntitlement]
- GCC_except_table16
- GCC_except_table19
- GCC_except_table22
- GCC_except_table28
- GCC_except_table34
- GCC_except_table36
- GCC_except_table39
- GCC_except_table46
- GCC_except_table55
- GCC_except_table60
- GCC_except_table62
- GCC_except_table76
- GCC_except_table84
- GCC_except_table87
- _OBJC_IVAR_$_ASDUpdatesService._hasUpdatesEntitlement
- ___33-[ASDJobManager _setupConnection]_block_invoke.129
- ___40-[ASDCheckQueueRequest _setupConnection]_block_invoke.73
- ___43-[ASDSoftwareUpdatesStore _setupConnection]_block_invoke.140
- ___47-[ASDClaimApplicationsRequest _setupConnection]_block_invoke.70
- ___47-[ASDDiagnosticService activeClientsWithError:]_block_invoke.17
- ___48-[ASDManagedApplicationRequest _setupConnection]_block_invoke.70
- ___57-[ASDFairPlayService generateKeybagRequestForDSID:error:]_block_invoke.53
- ___68+[ASDInstallApps _installApps:onPairedDevice:withCompletionHandler:]_block_invoke.83
- ___68+[ASDInstallApps _installApps:onPairedDevice:withCompletionHandler:]_block_invoke.91
- ___block_descriptor_40_e17_v16?0"NSError"8l
- ___block_descriptor_48_e8_32r_e17_v16?0"NSError"8lr32l8
- ___block_descriptor_48_e8_32r_e28_v24?0"NSData"8"NSError"16lr32l8
- ___block_literal_global.139
- ___block_literal_global.142
- ___block_literal_global.20
- ___block_literal_global.72
- ___block_literal_global.75
- __unnamed_array_storage.31
CStrings:
+ "\x01+\x13%"
+ "\x1b"
+ "\x1f\x17\x15"
+ "%@: "
+ "%@Action: %ld Features: %ld"
+ "+[ASDAppCapabilities isCapable:]"
+ "+[ASDAppCapabilities isCapableOfAction:capabilities:]"
+ "+[ASDAppCapabilities isCapableOfAction:capability:]"
+ "@40@0:8q16@24@32"
+ "ASDAppCapabilities"
+ "ASDAppCapabilitiesDidChangeNotification"
+ "ASDAppCapabilitiesServiceProtocol"
+ "ASDAppCapabilityMetadata"
+ "AppCapabilities"
+ "B32@0:8q16@24"
+ "EphemeralAccount"
+ "Error getting skan impression service"
+ "Error getting skan impression service remote proxy: %{public}@"
+ "Error in %{public}s: %{public}@ - %{public}@"
+ "SKANInteropService"
+ "SKANInteropServiceProtocol"
+ "T@\"AMSBagKeySet\",?,R,N"
+ "T@\"NSArray\",C,N,V_appCapabilities"
+ "T@\"NSString\",&,N,V_interactionType"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_token"
+ "T@\"SKANInteropService\",R"
+ "TB,N,V_supportsFeatureC"
+ "TB,R,GhasUnknownDistributor"
+ "TK"
+ "Tq,N,V_action"
+ "Tq,N,V_features"
+ "[%{public}@] Getting skan impressions for adamID: %{public}@"
+ "[%{public}@] Storing postbacks from BD"
+ "_action"
+ "_appCapabilities"
+ "_features"
+ "_interactionType"
+ "_supportsFeatureC"
+ "action"
+ "appCapabilities"
+ "click"
+ "features"
+ "getAppCapabilitiesServiceWithReplyHandler:"
+ "getCapabilitiesServiceWithError:"
+ "getImpressionsForApp:completionHandler:"
+ "getSKANInteropServiceWithCompletionHandler:"
+ "getSKANInteropServiceWithReplyHandler:"
+ "hasUnknownDistributor"
+ "interactionType"
+ "is-custom-browser-engine-app"
+ "isCapable:"
+ "isCapable:withCompletionHandler:"
+ "isCapableOfAction:capabilities:"
+ "isCapableOfAction:capability:"
+ "metadataWithAction:bundleID:capabilities:"
+ "metadataWithAction:entitlements:infoPlist:"
+ "processPurchases:withReplyHandler:"
+ "processPurchases:withResponseHandler:"
+ "setAction:"
+ "setAppCapabilities:"
+ "setFeatures:"
+ "setInteractionType:"
+ "setSupportsFeatureA:"
+ "setSupportsFeatureB:"
+ "setSupportsFeatureC:"
+ "setToken:"
+ "storePostbacks:completionHandler:"
+ "supports-alternate-distribution"
+ "supportsFeatureA"
+ "supportsFeatureB"
+ "supportsFeatureC"
+ "token"
+ "uses-non-webkit-browser-engine"
+ "v24@0:8@?<v@?@\"<ASDAppCapabilitiesServiceProtocol><NSXPCProxyCreating>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"<SKANInteropServiceProtocol><NSXPCProxyCreating>\"@\"NSError\">16"
+ "v24@?0@\"<ASDAppCapabilitiesServiceProtocol><NSXPCProxyCreating>\"8@\"NSError\"16"
+ "v24@?0@\"<SKANInteropServiceProtocol><NSXPCProxyCreating>\"8@\"NSError\"16"
+ "v32@0:8@\"ASDAppCapabilityMetadata\"16@?<v@?B>24"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"ASDPurchaseResponse\"@\"NSError\">24"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSData\">24"
+ "view"
- "\x01*\x13%"
- "\x1f\x17\x14"
- "T@\"AMSBagKeySet\",R,N"

```
