## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-1787.40.67.0.0
-  __TEXT.__text: 0xcfd14
-  __TEXT.__auth_stubs: 0x1970
-  __TEXT.__objc_methlist: 0x7b0c
+1787.60.31.0.0
+  __TEXT.__text: 0xce734
+  __TEXT.__auth_stubs: 0x1960
+  __TEXT.__objc_methlist: 0x7a5c
   __TEXT.__const: 0x14a0
-  __TEXT.__cstring: 0x33177
+  __TEXT.__cstring: 0x33159
   __TEXT.__gcc_except_tab: 0x2140
-  __TEXT.__oslogstring: 0x5ba4
-  __TEXT.__unwind_info: 0x29f4
+  __TEXT.__oslogstring: 0x5912
+  __TEXT.__unwind_info: 0x29c4
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x83e
-  __TEXT.__objc_methname: 0x11af6
-  __TEXT.__objc_methtype: 0x186a
-  __TEXT.__objc_stubs: 0xe600
+  __TEXT.__objc_classname: 0x7da
+  __TEXT.__objc_methname: 0x11794
+  __TEXT.__objc_methtype: 0x1703
+  __TEXT.__objc_stubs: 0xe380
   __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x23c0
-  __DATA_CONST.__objc_classlist: 0x300
+  __DATA_CONST.__const: 0x2348
+  __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_nlclslist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6530
-  __DATA_CONST.__objc_selrefs: 0x49f8
-  __DATA_CONST.__objc_arraydata: 0x30780
+  __DATA_CONST.__objc_const: 0x62c8
+  __DATA_CONST.__objc_selrefs: 0x4938
+  __DATA_CONST.__objc_arraydata: 0x30998
   __AUTH_CONST.__const: 0x1aa0
-  __AUTH_CONST.__cfstring: 0x4dd60
-  __AUTH_CONST.__objc_const: 0x29c0
+  __AUTH_CONST.__cfstring: 0x4e000
+  __AUTH_CONST.__objc_const: 0x2930
   __AUTH_CONST.__objc_intobj: 0x4308
-  __AUTH_CONST.__objc_doubleobj: 0xca0
+  __AUTH_CONST.__objc_doubleobj: 0xcb0
   __AUTH_CONST.__objc_arrayobj: 0xf00
-  __AUTH_CONST.__objc_dictobj: 0xc558
-  __AUTH_CONST.__auth_got: 0xcd0
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x3f0
-  __DATA.__objc_superrefs: 0x298
-  __DATA.__objc_ivar: 0x600
-  __DATA.__data: 0x4f8
-  __DATA.__bss: 0x1c01
+  __AUTH_CONST.__objc_dictobj: 0xc6c0
+  __AUTH_CONST.__auth_got: 0xcc8
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_protorefs: 0x10
+  __DATA.__objc_classrefs: 0x3e0
+  __DATA.__objc_superrefs: 0x290
+  __DATA.__objc_ivar: 0x5e8
+  __DATA.__data: 0x3d8
+  __DATA.__bss: 0x1bf9
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0xab0
+  __DATA_DIRTY.__bss: 0xaa8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4473
-  Symbols:   14552
-  CStrings:  14532
+  Functions: 4438
+  Symbols:   14422
+  CStrings:  14480
 
Symbols:
- +[uarpRbdcClient sharedInstance]
- +[uarpRbdcClient xpcConnectionToManager]
- +[uarpRbdcClient xpcConnectionToManager].cold.1
- -[uarpRbdcClient .cxx_destruct]
- -[uarpRbdcClient assetSolicitationGroup]
- -[uarpRbdcClient dealloc]
- -[uarpRbdcClient dynamicAssetSolicitationComplete:]
- -[uarpRbdcClient dynamicAssetSolicitationComplete:].cold.1
- -[uarpRbdcClient dynamicAssetSolicitationComplete:].cold.2
- -[uarpRbdcClient dynamicAssetSolicitationComplete:].cold.3
- -[uarpRbdcClient dynamicAssetSolicitationComplete:].cold.4
- -[uarpRbdcClient init]
- -[uarpRbdcClient listener:shouldAcceptNewConnection:]
- -[uarpRbdcClient remoteObject]
- -[uarpRbdcClient remoteObject].cold.1
- -[uarpRbdcClient setAssetSolicitationGroup:]
- -[uarpRbdcClient setSolicitedAssetList:]
- -[uarpRbdcClient solicitAssetsForTag:andModelNumber:]
- -[uarpRbdcClient solicitAssetsForTag:andModelNumber:].cold.1
- -[uarpRbdcClient solicitedAssetList]
- _OBJC_CLASS_$_NSXPCListener
- _OBJC_CLASS_$_uarpRbdcClient
- _OBJC_IVAR_$_uarpRbdcClient._assetSolicitationGroup
- _OBJC_IVAR_$_uarpRbdcClient._internalQueue
- _OBJC_IVAR_$_uarpRbdcClient._log
- _OBJC_IVAR_$_uarpRbdcClient._solicitedAssetList
- _OBJC_IVAR_$_uarpRbdcClient._xpcConnection
- _OBJC_IVAR_$_uarpRbdcClient._xpcListener
- _OBJC_METACLASS_$_uarpRbdcClient
- __OBJC_$_CLASS_METHODS_uarpRbdcClient
- __OBJC_$_CLASS_PROP_LIST_uarpRbdcClient
- __OBJC_$_INSTANCE_METHODS_uarpRbdcClient
- __OBJC_$_INSTANCE_VARIABLES_uarpRbdcClient
- __OBJC_$_PROP_LIST_uarpRbdcClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UARPStandaloneCommandRequestor
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_UARPStandaloneCommandProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_UARPStandaloneCommandProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_UARPStandaloneCommandRequestor
- __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
- __OBJC_$_PROTOCOL_REFS_UARPStandaloneCommandProvider
- __OBJC_$_PROTOCOL_REFS_UARPStandaloneCommandRequestor
- __OBJC_CLASS_PROTOCOLS_$_uarpRbdcClient
- __OBJC_CLASS_RO_$_uarpRbdcClient
- __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
- __OBJC_LABEL_PROTOCOL_$_UARPStandaloneCommandProvider
- __OBJC_LABEL_PROTOCOL_$_UARPStandaloneCommandRequestor
- __OBJC_METACLASS_RO_$_uarpRbdcClient
- __OBJC_PROTOCOL_$_NSXPCListenerDelegate
- __OBJC_PROTOCOL_$_UARPStandaloneCommandProvider
- __OBJC_PROTOCOL_$_UARPStandaloneCommandRequestor
- __OBJC_PROTOCOL_REFERENCE_$_UARPStandaloneCommandProvider
- __OBJC_PROTOCOL_REFERENCE_$_UARPStandaloneCommandRequestor
- ___30-[uarpRbdcClient remoteObject]_block_invoke
- ___30-[uarpRbdcClient remoteObject]_block_invoke.cold.1
- ___32+[uarpRbdcClient sharedInstance]_block_invoke
- ___53-[uarpRbdcClient listener:shouldAcceptNewConnection:]_block_invoke
- ___53-[uarpRbdcClient listener:shouldAcceptNewConnection:]_block_invoke.64
- ___53-[uarpRbdcClient listener:shouldAcceptNewConnection:]_block_invoke_2
- ___53-[uarpRbdcClient listener:shouldAcceptNewConnection:]_block_invoke_2.cold.1
- ___53-[uarpRbdcClient solicitAssetsForTag:andModelNumber:]_block_invoke
- ___53-[uarpRbdcClient solicitAssetsForTag:andModelNumber:]_block_invoke.cold.1
- ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_e8_32s_e30_v24?0"NSNumber"8"NSError"16ls32l8
- ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
- _objc_allocWithZone
- _objc_msgSend$_setQueue:
- _objc_msgSend$anonymousListener
- _objc_msgSend$assetSolicitationGroup
- _objc_msgSend$bundleIdentifier
- _objc_msgSend$dynamicAssetSolicitation:modelNumbers:notifyService:reply:
- _objc_msgSend$endpoint
- _objc_msgSend$exportedInterface
- _objc_msgSend$getResponseURLs
- _objc_msgSend$initWithMachServiceName:options:
- _objc_msgSend$mainBundle
- _objc_msgSend$modelNumber
- _objc_msgSend$remoteObject
- _objc_msgSend$remoteObjectInterface
- _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
- _objc_msgSend$setExportedInterface:
- _objc_msgSend$setExportedObject:
- _objc_msgSend$setSolicitedAssetList:
- _objc_msgSend$setWithObjects:
- _objc_msgSend$solicitedAssetList
- _objc_msgSend$xpcConnectionToManager
- _sharedInstance.defaultInstance
CStrings:
+ "BackgroundProcessing"
+ "BlockingPolicies"
+ "CheckpointState"
+ "DisplayStateExtended"
+ "EDRHeadroom"
+ "FeatureCheckpoint"
+ "FeatureCode"
+ "FeatureState"
+ "FeatureStatus"
+ "GnssSession"
+ "GroupName"
+ "IntensiveTasksBlockingPolicies"
+ "MaxCapacityPercent"
+ "PLLocationAgent_EventForward_GnssSession"
+ "SmartCharging"
+ "StateChangedDate"
+ "TaskBlockingPolicies"
+ "TaskCheckpoint"
+ "TaskName"
+ "WorkloadInformation"
+ "WorkloadType"
+ "eventStatus"
+ "ptec"
- "\x06"
- "+[uarpRbdcClient xpcConnectionToManager]"
- "-[uarpRbdcClient dynamicAssetSolicitationComplete:]"
- "-[uarpRbdcClient remoteObject]"
- "-[uarpRbdcClient remoteObject]_block_invoke"
- "-[uarpRbdcClient solicitAssetsForTag:andModelNumber:]"
- "-[uarpRbdcClient solicitAssetsForTag:andModelNumber:]_block_invoke"
- "@\"NSObject<OS_dispatch_group>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSXPCListener\""
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "BDC_PARSER: %s"
- "BDC_PARSER: %s: Error: %@"
- "BDC_PARSER: %s: Failed to get remote object: %@"
- "BDC_PARSER: %s: Failed to get xpc connection"
- "BDC_PARSER: %s: Unexpected Error: %ld"
- "BDC_PARSER: %s: _xpcConnection is nil"
- "BDC_PARSER: %s: received assets: %@"
- "BDC_PARSER: %s: remoteObject: %@"
- "BDC_PARSER: %s: waiting"
- "BDC_PARSER: Connection from PID %d invalidated"
- "BDC_PARSER: Connection to PID %d interrupted"
- "BDC_PARSER: New connection from PID %d"
- "BDC_PARSER: Solicited %@ assets for %@"
- "BDC_PARSER: assetLocations empty for record %@ model %@"
- "BDC_PARSER: assetLocations error for record %@ model %@"
- "BDC_PARSER: modelNumber error for record %@"
- "BDC_PARSER: no error with %@"
- "LowVoltageResidency"
- "NSXPCListenerDelegate"
- "T@\"NSMutableArray\",&,V_solicitedAssetList"
- "T@\"NSObject<OS_dispatch_group>\",&,V_assetSolicitationGroup"
- "T@\"uarpRbdcClient\",R"
- "UARPStandaloneCommandProvider"
- "UARPStandaloneCommandRequestor"
- "_assetSolicitationGroup"
- "_internalQueue"
- "_log"
- "_setQueue:"
- "_solicitedAssetList"
- "_xpcListener"
- "anonymousListener"
- "assetSolicitationGroup"
- "com.apple.accessoryupdater.uarp.standaloneCommandListener"
- "dynamicAssetSolicitation:modelNumber:notifyService:reply:"
- "dynamicAssetSolicitation:modelNumbers:notifyService:reply:"
- "dynamicAssetSolicitationComplete:"
- "dynamicAssetSolicitationComplete:modelNumber:"
- "endpoint"
- "exportedInterface"
- "getResponseURLs"
- "initWithMachServiceName:options:"
- "listener:shouldAcceptNewConnection:"
- "mainBundle"
- "modelNumber"
- "remoteObject"
- "remoteObjectInterface"
- "setAssetSolicitationGroup:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setExportedInterface:"
- "setExportedObject:"
- "setSolicitedAssetList:"
- "setWithObjects:"
- "solicitAssetsForTag:andModelNumber:"
- "solicitedAssetList"
- "uarpRbdcClient"
- "v24@0:8@\"NSArray\"16"
- "v24@?0@\"NSNumber\"8@\"NSError\"16"
- "v32@0:8@\"NSArray\"16@\"NSString\"24"
- "v48@0:8@\"NSString\"16@\"NSArray\"24@\"NSXPCListenerEndpoint\"32@?<v@?@\"NSNumber\"@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSXPCListenerEndpoint\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "xpcConnectionToManager"

```
