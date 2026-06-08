## SplashBoard

> `/System/Library/PrivateFrameworks/SplashBoard.framework/SplashBoard`

```diff

-308.4.1.0.0
-  __TEXT.__text: 0x29b64
-  __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_methlist: 0x2588
+318.100.0.0.0
+  __TEXT.__text: 0x2823c
+  __TEXT.__objc_methlist: 0x2678
   __TEXT.__const: 0x1b0
-  __TEXT.__cstring: 0x26a7
-  __TEXT.__gcc_except_tab: 0xb64
-  __TEXT.__oslogstring: 0x2fc6
+  __TEXT.__cstring: 0x277d
+  __TEXT.__gcc_except_tab: 0xa38
+  __TEXT.__oslogstring: 0x307f
   __TEXT.__ustring: 0x2a
-  __TEXT.__unwind_info: 0xd68
-  __TEXT.__objc_classname: 0x4e5
-  __TEXT.__objc_methname: 0x6208
-  __TEXT.__objc_methtype: 0xe77
-  __TEXT.__objc_stubs: 0x4d20
-  __DATA_CONST.__got: 0x460
-  __DATA_CONST.__const: 0xdc8
-  __DATA_CONST.__objc_classlist: 0x108
+  __TEXT.__unwind_info: 0xd78
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xe58
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1718
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xd0
-  __AUTH_CONST.__auth_got: 0x648
-  __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__cfstring: 0x2da0
-  __AUTH_CONST.__objc_const: 0x6ae8
+  __DATA_CONST.__objc_selrefs: 0x17e8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0xd8
+  __DATA_CONST.__got: 0x490
+  __AUTH_CONST.__const: 0x460
+  __AUTH_CONST.__cfstring: 0x2dc0
+  __AUTH_CONST.__objc_const: 0x6f70
   __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x284
-  __DATA.__data: 0x4e8
+  __DATA.__objc_ivar: 0x290
+  __DATA.__data: 0x5a8
   __DATA.__bss: 0x38
-  __DATA_DIRTY.__objc_data: 0x910
-  __DATA_DIRTY.__bss: 0x140
+  __DATA_DIRTY.__objc_data: 0x960
+  __DATA_DIRTY.__bss: 0x150
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B11FEB5B-A4DA-3CFB-8D43-C0898846D087
-  Functions: 1126
-  Symbols:   4036
-  CStrings:  2201
+  UUID: E3AEAA93-4688-3FC0-9091-99F7B02BB0A8
+  Functions: 1152
+  Symbols:   4133
+  CStrings:  980
 
Symbols:
+ +[XBApplicationSnapshotManifestImpl _queue_noteManifestInvalidated:]
+ +[XBApplicationSnapshotManifestImpl _queue_noteManifestInvalidated:].cold.1
+ +[XBLaunchImageProviderClient preheatServiceWithTimeout:connection:serviceInterface:activationHandler:activationWaitHandler:invalidationHandler:]
+ +[XBLaunchImageProviderClient preheatServiceWithTimeout:connection:serviceInterface:activationHandler:activationWaitHandler:invalidationHandler:].cold.1
+ -[XBApplicationController configureVolumeMaintenance]
+ -[XBApplicationSnapshot imageGeneratorWrapper]
+ -[XBApplicationSnapshot setImageGeneratorWrapper:]
+ -[XBApplicationSnapshotManifestImpl _access_queue_reapExpiredAndInvalidSnapshots]
+ -[XBApplicationSnapshotManifestImpl _access_queue_reapExpiredAndInvalidSnapshots].cold.1
+ -[XBApplicationSnapshotManifestImpl _access_queue_reapExpiredAndInvalidSnapshots].cold.2
+ -[XBApplicationSnapshotManifestImpl _queue_checkClientCount]
+ -[XBApplicationSnapshotManifestImpl _queue_decrementClientCount]
+ -[XBApplicationSnapshotManifestImpl _queue_incrementClientCount]
+ -[XBApplicationSnapshotManifestImpl _queue_reallyCheckClientCount]
+ -[XBApplicationSnapshotManifestImpl _queue_reallyCheckClientCount].cold.1
+ -[XBLaunchImageProviderClient _createDefaultConnection]
+ -[XBLaunchImageProviderClient _createDefaultConnection].cold.1
+ -[XBLaunchImageProviderClient activateWithHandler:]
+ -[XBLaunchImageProviderClient activate]
+ -[XBLaunchImageProviderClient connection]
+ -[XBLaunchImageProviderClient initWithApplicationInfo:connection:serviceInterface:]
+ -[XBLaunchImageProviderClient initWithApplicationInfo:connection:serviceInterface:].cold.1
+ -[XBLaunchImageProviderClient invalidate]
+ -[XBLaunchImageProviderClient shouldValidateApplicationInfo:error:]
+ -[_XBImageGeneratorWrapper .cxx_destruct]
+ -[_XBImageGeneratorWrapper _objc_initiateDealloc]
+ -[_XBImageGeneratorWrapper generator]
+ -[_XBImageGeneratorWrapper init]
+ -[_XBImageGeneratorWrapper init].cold.1
+ -[_XBImageGeneratorWrapper setGenerator:]
+ GCC_except_table12
+ GCC_except_table29
+ GCC_except_table30
+ GCC_except_table31
+ GCC_except_table32
+ GCC_except_table34
+ GCC_except_table43
+ GCC_except_table46
+ GCC_except_table50
+ GCC_except_table51
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table66
+ GCC_except_table69
+ GCC_except_table71
+ GCC_except_table8
+ GCC_except_table81
+ GCC_except_table84
+ GCC_except_table85
+ GCC_except_table86
+ GCC_except_table9
+ GCC_except_table94
+ _OBJC_CLASS_$_BSObjCProtocol
+ _OBJC_CLASS_$_BSServiceConnectionEndpoint
+ _OBJC_CLASS_$_BSServiceInitiatingConnection
+ _OBJC_CLASS_$_BSServiceInterface
+ _OBJC_CLASS_$_BSServiceQuality
+ _OBJC_CLASS_$__XBImageGeneratorWrapper
+ _OBJC_IVAR_$_XBApplicationController._didConfigureVolumeMaintenance
+ _OBJC_IVAR_$_XBApplicationSnapshot._imageGeneratorWrapper
+ _OBJC_IVAR_$_XBLaunchImageProviderClient._connection
+ _OBJC_IVAR_$__XBImageGeneratorWrapper._generator
+ _OBJC_METACLASS_$__XBImageGeneratorWrapper
+ _XBApplicationLaunchImageDomainName
+ _XBApplicationLaunchImageMachName
+ _XBServiceLaunchImageInterface
+ _XBServiceLaunchImageInterface.__interface
+ _XBServiceLaunchImageInterface.cold.1
+ _XBServiceLaunchImageInterface.onceToken
+ __OBJC_$_INSTANCE_METHODS__XBImageGeneratorWrapper
+ __OBJC_$_INSTANCE_VARIABLES__XBImageGeneratorWrapper
+ __OBJC_$_PROP_LIST_XBLaunchImageProviderClient
+ __OBJC_$_PROP_LIST__XBImageGeneratorWrapper
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSInvalidatable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_XBServiceLaunchImageClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSInvalidatable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_XBServiceLaunchImageClientInterface
+ __OBJC_$_PROTOCOL_REFS_BSInvalidatable
+ __OBJC_CLASS_PROTOCOLS_$_XBLaunchImageProviderClient
+ __OBJC_CLASS_RO_$__XBImageGeneratorWrapper
+ __OBJC_LABEL_PROTOCOL_$_BSInvalidatable
+ __OBJC_LABEL_PROTOCOL_$_XBServiceLaunchImageClientInterface
+ __OBJC_METACLASS_RO_$__XBImageGeneratorWrapper
+ __OBJC_PROTOCOL_$_BSInvalidatable
+ __OBJC_PROTOCOL_$_XBServiceLaunchImageClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_XBServiceLaunchImageClientInterface
+ ___145+[XBLaunchImageProviderClient preheatServiceWithTimeout:connection:serviceInterface:activationHandler:activationWaitHandler:invalidationHandler:]_block_invoke
+ ___171-[XBApplicationSnapshotManifestImpl _didGenerateImageData:forSnapshot:imageWasGenerated:imageDataGenerationSignal:logIdentifier:didSaveHandler:qos:writeToFileIfSupported:]_block_invoke.251
+ ___171-[XBApplicationSnapshotManifestImpl _didGenerateImageData:forSnapshot:imageWasGenerated:imageDataGenerationSignal:logIdentifier:didSaveHandler:qos:writeToFileIfSupported:]_block_invoke.251.cold.1
+ ___171-[XBApplicationSnapshotManifestImpl _didGenerateImageData:forSnapshot:imageWasGenerated:imageDataGenerationSignal:logIdentifier:didSaveHandler:qos:writeToFileIfSupported:]_block_invoke.251.cold.2
+ ___32+[XBVolumeMaintainer configure:]_block_invoke.1
+ ___32+[XBVolumeMaintainer configure:]_block_invoke_2.3
+ ___32-[_XBImageGeneratorWrapper init]_block_invoke
+ ___51-[XBLaunchImageProviderClient activateWithHandler:]_block_invoke
+ ___51-[XBLaunchImageProviderClient activateWithHandler:]_block_invoke_2
+ ___55-[XBLaunchImageProviderClient _createDefaultConnection]_block_invoke
+ ___60-[XBApplicationSnapshotManifestImpl _queue_checkClientCount]_block_invoke
+ ___60-[XBApplicationSnapshotManifestImpl _queue_checkClientCount]_block_invoke_2
+ ___66-[XBApplicationSnapshotManifestImpl _queue_reallyCheckClientCount]_block_invoke
+ ___71-[XBApplicationSnapshotManifestImpl snapshotsForGroupIDs:fetchRequest:]_block_invoke.233
+ ___71-[XBApplicationSnapshotManifestImpl snapshotsForGroupIDs:fetchRequest:]_block_invoke.236
+ ___74-[XBLaunchImageProviderClient generateImageWithContext:captureInfo:error:]_block_invoke.46
+ ___74-[XBLaunchImageProviderClient generateImageWithContext:captureInfo:error:]_block_invoke.cold.1
+ ___81-[XBApplicationSnapshotManifestImpl _access_queue_reapExpiredAndInvalidSnapshots]_block_invoke
+ ___81-[XBApplicationSnapshotManifestImpl _access_queue_reapExpiredAndInvalidSnapshots]_block_invoke.288
+ ___81-[XBApplicationSnapshotManifestImpl _access_queue_reapExpiredAndInvalidSnapshots]_block_invoke.cold.1
+ ___83-[XBLaunchImageProviderClient initWithApplicationInfo:connection:serviceInterface:]_block_invoke
+ ___83-[XBLaunchImageProviderClient initWithApplicationInfo:connection:serviceInterface:]_block_invoke.2
+ ___83-[XBLaunchImageProviderClient initWithApplicationInfo:connection:serviceInterface:]_block_invoke.2.cold.1
+ ___83-[XBLaunchImageProviderClient initWithApplicationInfo:connection:serviceInterface:]_block_invoke_2
+ ___83-[XBLaunchImageProviderClient initWithApplicationInfo:connection:serviceInterface:]_block_invoke_2.cold.1
+ ___XBServiceLaunchImageInterface_block_invoke
+ ___XBServiceLaunchImageInterface_block_invoke_2
+ ___block_descriptor_32_e35_v16?0"BSMutableServiceInterface"8l
+ ___block_descriptor_32_e48_v16?0"<BSServiceConnectionInitiatingOptions>"8l
+ ___block_descriptor_40_e8_32bs_e42_v16?0"<BSServiceConnectionConfiguring>"8ls32l8
+ ___block_descriptor_40_e8_32bs_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8ls32l8
+ ___block_descriptor_40_e8_32s_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e42_v16?0"<BSServiceConnectionConfiguring>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e72_v32?0"NSNumber"8"XBLaunchCaptureInformation"16"XBLaunchImageError"24ls32l8r48l8r56l8r64l8s40l8
+ ___block_literal_global.185
+ ___block_literal_global.23
+ ___block_literal_global.232
+ ___block_literal_global.235
+ ___block_literal_global.240
+ ___block_literal_global.26
+ ___block_literal_global.272
+ ___block_literal_global.279
+ ___block_literal_global.29
+ ___block_literal_global.308
+ ___block_literal_global.445
+ ___block_literal_global.67
+ __class_setCustomDeallocInitiation
+ __objc_deallocOnMainThreadHelper
+ _dispatch_async_f
+ _init.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_access_queue_reapExpiredAndInvalidSnapshots
+ _objc_msgSend$_createDefaultConnection
+ _objc_msgSend$_queue_checkClientCount
+ _objc_msgSend$_queue_decrementClientCount
+ _objc_msgSend$_queue_incrementClientCount
+ _objc_msgSend$_queue_noteManifestInvalidated:
+ _objc_msgSend$_queue_reallyCheckClientCount
+ _objc_msgSend$activate
+ _objc_msgSend$activateWithHandler:
+ _objc_msgSend$configureConnection:
+ _objc_msgSend$configureVolumeMaintenance
+ _objc_msgSend$connection
+ _objc_msgSend$endpointForMachName:service:instance:
+ _objc_msgSend$generator
+ _objc_msgSend$getLaunchImageForApp:launchRequest:createCaptureInfo:withTimeout:reply:
+ _objc_msgSend$initWithApplicationInfo:connection:serviceInterface:
+ _objc_msgSend$initWithEndpoint:options:
+ _objc_msgSend$interfaceWithIdentifier:configurator:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$preheat
+ _objc_msgSend$preheatServiceWithTimeout:connection:serviceInterface:activationHandler:activationWaitHandler:invalidationHandler:
+ _objc_msgSend$protocolForProtocol:
+ _objc_msgSend$remoteTarget
+ _objc_msgSend$setActivationHandler:
+ _objc_msgSend$setClientMessagingExpectation:
+ _objc_msgSend$setGenerator:
+ _objc_msgSend$setInterface:
+ _objc_msgSend$setInterfaceTarget:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setServer:
+ _objc_msgSend$setServiceQuality:
+ _objc_msgSend$shouldValidateApplicationInfo:error:
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$userInitiated
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x6
+ _pthread_main_np
- +[XBApplicationSnapshotManifestImpl _workloop_noteManifestInvalidated:]
- +[XBApplicationSnapshotManifestImpl _workloop_noteManifestInvalidated:].cold.1
- +[XBLaunchImageProviderClient preheatServiceWithTimeout:].cold.1
- -[XBApplicationSnapshot setImageGenerator:]
- -[XBApplicationSnapshotManifestImpl _access_workloop_reapExpiredAndInvalidSnapshots]
- -[XBApplicationSnapshotManifestImpl _access_workloop_reapExpiredAndInvalidSnapshots].cold.1
- -[XBApplicationSnapshotManifestImpl _access_workloop_reapExpiredAndInvalidSnapshots].cold.2
- -[XBApplicationSnapshotManifestImpl _workloop_checkClientCount]
- -[XBApplicationSnapshotManifestImpl _workloop_decrementClientCount]
- -[XBApplicationSnapshotManifestImpl _workloop_incrementClientCount]
- -[XBApplicationSnapshotManifestImpl _workloop_reallyCheckClientCount]
- -[XBApplicationSnapshotManifestImpl _workloop_reallyCheckClientCount].cold.1
- -[XBLaunchImageProviderClient init]
- GCC_except_table167
- GCC_except_table168
- GCC_except_table169
- GCC_except_table170
- GCC_except_table20
- GCC_except_table22
- GCC_except_table23
- GCC_except_table25
- GCC_except_table37
- GCC_except_table40
- GCC_except_table44
- GCC_except_table45
- GCC_except_table47
- GCC_except_table49
- GCC_except_table52
- GCC_except_table56
- GCC_except_table60
- GCC_except_table65
- GCC_except_table72
- GCC_except_table75
- GCC_except_table76
- GCC_except_table79
- GCC_except_table80
- _BSDeserializeDataFromXPCDictionaryWithKey
- _OBJC_CLASS_$_BSBaseXPCClient
- _OBJC_IVAR_$_XBApplicationSnapshot._imageGenerator
- _OBJC_METACLASS_$_BSBaseXPCClient
- _OUTLINED_FUNCTION_21
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_24
- _XBLaunchImageProviderMessageKeyCaptureInfo
- _XBLaunchImageProviderMessageKeyCompatibilityInfo
- _XBLaunchImageProviderMessageKeyContextID
- _XBLaunchImageProviderMessageKeyCreateCaptureInfo
- _XBLaunchImageProviderMessageKeyError
- _XBLaunchImageProviderMessageKeyLaunchRequest
- _XBLaunchImageProviderMessageKeyMessageType
- _XBLaunchImageProviderMessageKeyWithTimeout
- ___171-[XBApplicationSnapshotManifestImpl _didGenerateImageData:forSnapshot:imageWasGenerated:imageDataGenerationSignal:logIdentifier:didSaveHandler:qos:writeToFileIfSupported:]_block_invoke.253
- ___171-[XBApplicationSnapshotManifestImpl _didGenerateImageData:forSnapshot:imageWasGenerated:imageDataGenerationSignal:logIdentifier:didSaveHandler:qos:writeToFileIfSupported:]_block_invoke.253.cold.1
- ___171-[XBApplicationSnapshotManifestImpl _didGenerateImageData:forSnapshot:imageWasGenerated:imageDataGenerationSignal:logIdentifier:didSaveHandler:qos:writeToFileIfSupported:]_block_invoke.253.cold.2
- ___32+[XBVolumeMaintainer configure:]_block_invoke_3
- ___57+[XBLaunchImageProviderClient preheatServiceWithTimeout:]_block_invoke
- ___57+[XBLaunchImageProviderClient preheatServiceWithTimeout:]_block_invoke_2
- ___63-[XBApplicationSnapshotManifestImpl _workloop_checkClientCount]_block_invoke
- ___63-[XBApplicationSnapshotManifestImpl _workloop_checkClientCount]_block_invoke_2
- ___69-[XBApplicationSnapshotManifestImpl _workloop_reallyCheckClientCount]_block_invoke
- ___71-[XBApplicationSnapshotManifestImpl snapshotsForGroupIDs:fetchRequest:]_block_invoke.235
- ___71-[XBApplicationSnapshotManifestImpl snapshotsForGroupIDs:fetchRequest:]_block_invoke.240
- ___74-[XBLaunchImageProviderClient generateImageWithContext:captureInfo:error:]_block_invoke.38
- ___74-[XBLaunchImageProviderClient generateImageWithContext:captureInfo:error:]_block_invoke.38.cold.1
- ___74-[XBLaunchImageProviderClient generateImageWithContext:captureInfo:error:]_block_invoke.43
- ___74-[XBLaunchImageProviderClient generateImageWithContext:captureInfo:error:]_block_invoke_2
- ___84-[XBApplicationSnapshotManifestImpl _access_workloop_reapExpiredAndInvalidSnapshots]_block_invoke
- ___84-[XBApplicationSnapshotManifestImpl _access_workloop_reapExpiredAndInvalidSnapshots]_block_invoke.290
- ___84-[XBApplicationSnapshotManifestImpl _access_workloop_reapExpiredAndInvalidSnapshots]_block_invoke.cold.1
- ___ManifestWorkloop
- ___block_descriptor_32_e33_v16?0"NSObject<OS_xpc_object>"8l
- ___block_descriptor_57_e8_32s40s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8r48l8r56l8r64l8s40l8
- ___block_literal_global.189
- ___block_literal_global.234
- ___block_literal_global.237
- ___block_literal_global.24
- ___block_literal_global.242
- ___block_literal_global.27
- ___block_literal_global.274
- ___block_literal_global.281
- ___block_literal_global.30
- ___block_literal_global.310
- ___block_literal_global.447
- ___block_literal_global.53
- __xpc_type_dictionary
- _objc_msgSend$_access_workloop_reapExpiredAndInvalidSnapshots
- _objc_msgSend$_connection
- _objc_msgSend$_sendMessage:
- _objc_msgSend$_sendMessage:withReplyHandler:waitForReply:waitDuration:
- _objc_msgSend$_workloop_checkClientCount
- _objc_msgSend$_workloop_decrementClientCount
- _objc_msgSend$_workloop_incrementClientCount
- _objc_msgSend$_workloop_noteManifestInvalidated:
- _objc_msgSend$_workloop_reallyCheckClientCount
- _objc_msgSend$bs_secureDecodedFromData:
- _objc_msgSend$initWithServiceName:
- _xpc_get_type
CStrings:
+ "Connection for %@ (%@) interrupted. Re-activating."
+ "Connection for %@ (%@) invalidated."
+ "DeviceSupportsASTC"
+ "HasExtendedColorDisplay"
+ "The request failed %@"
+ "XBSplashBoardServices"
+ "cannot get endpoint for mach %{public}@ service: %{public}@"
+ "unable to find a connection to server"
+ "v16@?0@\"<BSServiceConnectionConfiguring>\"8"
+ "v16@?0@\"<BSServiceConnectionInitiatingOptions>\"8"
+ "v16@?0@\"BSMutableServiceInterface\"8"
+ "v16@?0@\"BSServiceConnection<BSServiceConnectionContext>\"8"
+ "v32@?0@\"NSNumber\"8@\"XBLaunchCaptureInformation\"16@\"XBLaunchImageError\"24"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<BSInvalidatable>\""
- "@\"<XBApplicationLaunchRequestProviding>\""
- "@\"<XBApplicationProviding>\""
- "@\"<XBApplicationSnapshotImageGenerationScheduling>\""
- "@\"<XBApplicationSnapshotManifestDelegate>\""
- "@\"<XBSnapshotDataProvider>\""
- "@\"<XBSnapshotDataProvider>\"16@0:8"
- "@\"<XBSnapshotManifestStore>\""
- "@\"BSAtomicFlag\""
- "@\"BSAtomicSignal\""
- "@\"BSContinuousMachTimer\""
- "@\"BSDescriptionBuilder\"16@0:8"
- "@\"BSDescriptionBuilder\"24@0:8@\"NSString\"16"
- "@\"BSMutableSettings\""
- "@\"FBSDisplayConfiguration\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSCountedSet\""
- "@\"NSData\"24@0:8@\"NSString\"16"
- "@\"NSData\"24@0:8o^{CGAffineTransform=dddddd}16"
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSFileManager\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_workloop>\""
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSOrderedSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@\"NSString\"24@0:8Q16"
- "@\"NSString\"32@0:8@\"BSSettings\"16Q24"
- "@\"NSString\"40@0:8q16@24Q32"
- "@\"NSString\"48@0:8@\"BSSettings\"16q24@32Q40"
- "@\"UIImage\""
- "@\"UIImage\"16@0:8"
- "@\"UIImage\"24@0:8q16"
- "@\"XBApplicationLaunchCompatibilityInfo\""
- "@\"XBApplicationSnapshot\""
- "@\"XBApplicationSnapshotGenerationContext\""
- "@\"XBApplicationSnapshotManifestImpl\""
- "@\"XBApplicationSnapshotPredicate\""
- "@\"XBDisplayEdgeInsetsWrapper\""
- "@\"XBLaunchInterface\""
- "@\"XBLaunchInterfaceConfiguration\""
- "@\"XBLaunchStateRequest\""
- "@\"XBSnapshotContainerIdentity\""
- "@\"XBSnapshotDataProviderContext\""
- "@\"XBSnapshotDataProviderContext\"16@0:8"
- "@\"XBSnapshotManifestIdentity\""
- "@\"XBStatusBarSettings\""
- "@\"_FBSSnapshot\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSObject<OS_xpc_object>\"16"
- "@24@0:8@16"
- "@24@0:8B16B20"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8o^{CGAffineTransform=dddddd}16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16I24B28"
- "@32@0:8@16Q24"
- "@32@0:8@16^q24"
- "@32@0:8@16q24"
- "@32@0:8Q16^B24"
- "@32@0:8q16Q24"
- "@36@0:8@16@24B32"
- "@36@0:8Q16B24@?28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@24d32"
- "@40@0:8q16@24Q32"
- "@44@0:8@16@24@32B40"
- "@44@0:8q16@24@32B40"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16q24@32Q40"
- "@48@0:8d16d24d32d40"
- "@48@0:8{UIEdgeInsets=dddd}16"
- "@52@0:8Q16@24@32@40B48"
- "@72@0:8@16@24@32q40@48@?56@?64"
- "@?"
- "@?16@0:8"
- "@?36@0:8@16B24^@28"
- "Aixt/MEN2O2B7f+8m4TxUA"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B24@0:8^@16"
- "B24@0:8q16"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B40@0:8@16@24^@32"
- "B48@0:8@\"BSDescriptionBuilder\"16q24@32Q40"
- "B48@0:8@16q24@32Q40"
- "B56@0:8@\"BSSettings\"16@\"BSDescriptionBuilder\"24q32@40Q48"
- "B56@0:8@16@24q32@40Q48"
- "BSDescriptionProviding"
- "BSSettingDescriptionProvider"
- "BSXPCCoding"
- "CGImage"
- "CGSizeValue"
- "EventStreamWrapper"
- "I40@0:8@16^@24^@32"
- "IOSurface"
- "NSCoding"
- "NSCopying"
- "NSMutableCopying"
- "NSObject"
- "NSSecureCoding"
- "NSSortDescriptor"
- "NSSortDescriptors"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "SortingSupport"
- "T#,R"
- "T@\"<XBApplicationProviding>\",R,N,V_applicationProvider"
- "T@\"<XBApplicationSnapshotManifestDelegate>\",W,N,V_delegate"
- "T@\"<XBSnapshotManifestStore>\",R,C,N,V_store"
- "T@\"<XBSnapshotManifestStore>\",R,N,G_store,V_store"
- "T@\"FBSDisplayConfiguration\",&,N,V_displayConfiguration"
- "T@\"NSArray\",&,N,V_urlSchemes"
- "T@\"NSArray\",C,N,V_sortDescriptors"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,C,N,V_launchInterfaces"
- "T@\"NSArray\",R,N,V_bars"
- "T@\"NSDate\",&,D,N"
- "T@\"NSDate\",&,N,V_lastUsedDate"
- "T@\"NSDate\",R,N,V_creationDate"
- "T@\"NSDictionary\",C,V_extendedData"
- "T@\"NSOrderedSet\",R,N,V_launchRequests"
- "T@\"NSSet\",C,N"
- "T@\"NSSet\",R,C,N,V_snapshots"
- "T@\"NSSortDescriptor\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,G_relativePath,S_setRelativePath:,V_relativePath"
- "T@\"NSString\",C,N,Gfilename,S_setFilename:,V_filename"
- "T@\"NSString\",C,N,S_setPath:,V_path"
- "T@\"NSString\",C,N,V_bundleContainerPath"
- "T@\"NSString\",C,N,V_bundleIdentifier"
- "T@\"NSString\",C,N,V_bundlePath"
- "T@\"NSString\",C,N,V_caarFilePath"
- "T@\"NSString\",C,N,V_dataProviderClassName"
- "T@\"NSString\",C,N,V_defaultGroupIdentifier"
- "T@\"NSString\",C,N,V_groupID"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",C,N,V_launchInterfaceIdentifier"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_requiredOSVersion"
- "T@\"NSString\",C,N,V_sandboxPath"
- "T@\"NSString\",C,N,V_scheme"
- "T@\"NSString\",C,N,V_urlSchemeName"
- "T@\"NSString\",C,N,V_variantID"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,D,N"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_bundleContainerPath"
- "T@\"NSString\",R,C,N,V_bundleIdentifier"
- "T@\"NSString\",R,C,N,V_bundlePath"
- "T@\"NSString\",R,C,N,V_colorName"
- "T@\"NSString\",R,C,N,V_dataContainerPath"
- "T@\"NSString\",R,C,N,V_groupID"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,N,V_imageName"
- "T@\"NSString\",R,C,N,V_navigationBarImageName"
- "T@\"NSString\",R,C,N,V_snapshotContainerPath"
- "T@\"NSString\",R,C,N,V_tabBarImageName"
- "T@\"NSString\",R,C,N,V_toolbarImageName"
- "T@\"NSString\",R,N"
- "T@\"XBApplicationLaunchCompatibilityInfo\",R,N,V_applicationCompatibilityInfo"
- "T@\"XBApplicationSnapshotGenerationContext\",&,N,V_fallbackGenerationContext"
- "T@\"XBApplicationSnapshotGenerationContext\",R,N,V_generationContext"
- "T@\"XBApplicationSnapshotManifestImpl\",R,W,N,V_manifestImpl"
- "T@\"XBApplicationSnapshotPredicate\",&,N,V_predicate"
- "T@\"XBDisplayEdgeInsetsWrapper\",&,N,V_customSafeAreaInsets"
- "T@\"XBDisplayEdgeInsetsWrapper\",C,N"
- "T@\"XBLaunchInterface\",R,C,N"
- "T@\"XBLaunchInterfaceConfiguration\",R,N,V_configuration"
- "T@\"XBLaunchStateRequest\",R,C,N,V_launchRequest"
- "T@\"XBSnapshotContainerIdentity\",C,V_containerIdentity"
- "T@\"XBSnapshotContainerIdentity\",R,C,N,V_containerIdentity"
- "T@\"XBSnapshotDataProviderContext\",R,&,N"
- "T@\"XBSnapshotDataProviderContext\",R,&,N,V_context"
- "T@\"XBSnapshotManifestIdentity\",R,C,N,V_identity"
- "T@\"XBStatusBarSettings\",C,N,V_statusBarSettings"
- "T@\"XBStatusBarSettings\",R,&,N"
- "T@?,C,N,V_comparator"
- "T@?,C,N,V_imageGenerator"
- "TB,D,N,GisBackgroundActivityEnabled"
- "TB,D,N,GisHidden"
- "TB,N,G_isDefault,V_default"
- "TB,N,GisFullScreen"
- "TB,N,GisFullScreen,V_fullScreen"
- "TB,N,GisImageOpaque,V_imageOpaque"
- "TB,N,GisOpaque,V_opaque"
- "TB,N,V_ascending"
- "TB,N,V_hasKnownBadLaunchImage"
- "TB,N,V_launchesOpaque"
- "TB,R"
- "TB,R,GisFatal,V_fatal"
- "TB,R,N"
- "TB,R,N,GisBackgroundActivityEnabled"
- "TB,R,N,GisExpired"
- "TB,R,N,GisHidden"
- "TB,R,N,V_imageRespectsSafeAreaInsets"
- "TB,R,V_shouldDeny"
- "TQ,N"
- "TQ,N,V_estimatedMemoryImpact"
- "TQ,N,V_key"
- "TQ,N,V_statusBarState"
- "TQ,N,V_type"
- "TQ,R"
- "TQ,R,N"
- "T^{__FSEventStream=},N,V_stream"
- "Td,N"
- "Td,N,V_imageScale"
- "Td,N,V_scale"
- "Td,R,N,V_bottomInset"
- "Td,R,N,V_leftInset"
- "Td,R,N,V_rightInset"
- "Td,R,N,V_timeout"
- "Td,R,N,V_topInset"
- "The request failed"
- "Tq,D,N"
- "Tq,N"
- "Tq,N,V_backgroundStyle"
- "Tq,N,V_badLaunchImageCandidateCount"
- "Tq,N,V_classicMode"
- "Tq,N,V_compatibilityMode"
- "Tq,N,V_contentType"
- "Tq,N,V_fileLocation"
- "Tq,N,V_imageOrientation"
- "Tq,N,V_interfaceOrientation"
- "Tq,N,V_userInterfaceStyle"
- "Tq,R,N"
- "Tq,R,N,V_fileFormat"
- "Tq,R,N,V_interfaceOrientation"
- "T{CGAffineTransform=dddddd},N,V_imageTransform"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N"
- "T{CGSize=dd},N"
- "T{CGSize=dd},N,V_naturalSize"
- "T{CGSize=dd},N,V_referenceSize"
- "T{CGSize=dd},R,N"
- "URL"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "XBApplicationCaptureInformation"
- "XBApplicationController"
- "XBApplicationDataStore"
- "XBApplicationManifestWorkloop"
- "XBApplicationProviding"
- "XBApplicationSnapshotFetchRequest"
- "XBApplicationSnapshotGenerationContext"
- "XBApplicationSnapshotGenerationScheduler"
- "XBApplicationSnapshotGroup"
- "XBApplicationSnapshotImage"
- "XBApplicationSnapshotImageGenerationScheduling"
- "XBApplicationSnapshotImageGenerator"
- "XBApplicationSnapshotManifestDelegate"
- "XBApplicationSnapshotManifestImpl"
- "XBApplicationSnapshotPredicate"
- "XBApplicationSnapshotSortDescriptor"
- "XBDefaultApplicationProvider"
- "XBDisplayEdgeInsetsWrapper"
- "XBLaunchCaptureInformation"
- "XBLaunchImageDataProvider"
- "XBLaunchImageError"
- "XBLaunchImageProvider"
- "XBLaunchImageProviderClient"
- "XBLaunchInterface"
- "XBLaunchInterfaceConfiguration"
- "XBLaunchStateRequest"
- "XBMutableStatusBarSettings"
- "XBSnapshotContainerIdentity"
- "XBSnapshotDataProvider"
- "XBSnapshotDataProviderContext"
- "XBSnapshotManifestIdentity"
- "XBSnapshotManifestStore"
- "XBStatusBarSettings"
- "XBVolumeMaintainer"
- "^{CGImage=}32@0:8@16^{CGImage=}24"
- "^{_NSZone=}16@0:8"
- "^{__FSEventStream=}"
- "^{__FSEventStream=}16@0:8"
- "_accessLock"
- "_access_accessSnapshotsWithBlock:completion:"
- "_access_addSnapshotToGroup:"
- "_access_allSnapshotGroups"
- "_access_deletePaths:"
- "_access_deleteSnapshots:"
- "_access_doArchiveWithCompletions:"
- "_access_gatherPaths:forSnapshot:"
- "_access_purgeSnapshotsWithProtectedContent"
- "_access_snapshotGroupForID:creatingIfNeeded:"
- "_access_snapshotsConsideredUnpurgableByAPFS"
- "_access_snapshotsForGroupIDs:"
- "_access_snapshotsForGroupIDs:matchingPredicate:"
- "_access_snapshotsMatchingPredicate:"
- "_access_updateSnapshotsAPFSPurgability:"
- "_access_validateWithContainerIdentity:"
- "_access_workloop_reapExpiredAndInvalidSnapshots"
- "_addBadLaunchInterfaceToDenyList:forError:"
- "_addBundleIdentifierToLaunchInterfaceDenyList:"
- "_addSnapshotToGroup:"
- "_allApplicationsFilteredBySystem:bySplashBoard:"
- "_allSecureCodingClassesIncludingDefaultAndClientSpecified"
- "_allSnapshotGroups"
- "_appInfo"
- "_applicationCompatibilityInfo"
- "_applicationProvider"
- "_applicationTypeForProxy:"
- "_archiveSchedulingQueue_dirty"
- "_archiveSchedulingQueue_scheduled"
- "_archiveSchedulingQueue_synchronizeCompletions"
- "_ascending"
- "_backgroundStyle"
- "_backgroundStyleForString:"
- "_badLaunchImageCandidateCount"
- "_bars"
- "_baseLogIdentifier"
- "_beginPreHeatImageAccess"
- "_bottomInset"
- "_bundleContainerPath"
- "_bundleIdentifier"
- "_bundleIdentifierDeniedLaunchInterfaceCount:"
- "_bundleIdentifierHasDeniedLaunchInterface:"
- "_bundlePath"
- "_caarFilePath"
- "_cacheImage:"
- "_cacheableBundleIdentifiers"
- "_cachedImageTransaction"
- "_cachedStoresByBundleIdentifier"
- "_captureInfos"
- "_captureOrUpdateLaunchImagesForApplications:firstImageIsReady:completionWithCaptureInfo:"
- "_captureOrUpdateLaunchImagesForApplications:firstImageIsReady:createCaptureInfo:completionWithCaptureInfo:"
- "_classicMode"
- "_clearCompatibilityInfoForBundleIdentifier:"
- "_clientCount"
- "_clientObjectForKey:"
- "_clientSettings"
- "_colorName"
- "_commonInit"
- "_commonInitWithIdentifier:"
- "_comparator"
- "_compatibilityMode"
- "_configuration"
- "_configureDefaultPathWithinGroupForFormat:"
- "_configureSnapshot:withCompatibilityInfo:forLaunchRequest:"
- "_configureWithPath:"
- "_connection"
- "_containerIdentity"
- "_contentFrame"
- "_contentType"
- "_context"
- "_createCGImageWithPreferredOptions:fromCGImage:"
- "_createSnapshotWithGroupID:generationContext:"
- "_createVariantWithIdentifier:"
- "_creationDate"
- "_customSafeAreaInsets"
- "_dataContainerPath"
- "_dataGenerationWorkloop"
- "_dataProvider"
- "_dataProviderClassName"
- "_dataProviderFetchType"
- "_default"
- "_defaultGroupIdentifier"
- "_defaultInterface"
- "_delegate"
- "_deleteLegacyCachesSnapshotPathsIfNeeded"
- "_descriptionBuilderWithMultilinePrefix:includeVariants:"
- "_descriptionForStateCaptureWithMultilinePrefix:"
- "_determineRelativePathForPath:location:"
- "_didGenerateImage:imageGenerationSignal:logIdentifier:imageGeneratedHandler:qos:"
- "_didGenerateImageData:forSnapshot:imageWasGenerated:imageDataGenerationSignal:logIdentifier:didSaveHandler:qos:writeToFileIfSupported:"
- "_didGenerateImageDataHandler"
- "_didGenerateImageHandler"
- "_displayConfiguration"
- "_endPreHeatImageAccess"
- "_estimatedMemoryImpact"
- "_expirationDate"
- "_extendedData"
- "_fallbackGenerationContext"
- "_fatal"
- "_fileFormat"
- "_fileLocation"
- "_filename"
- "_fullScreen"
- "_generatableSnapshotForGroupID:generationContext:"
- "_generate"
- "_generateImageForSnapshot:inManifest:withContext:asyncImageData:dataProvider:scheduleAsyncGeneration:completion:"
- "_generateImageIfPossible"
- "_generate_handled_request"
- "_generate_imageFromLegacyDataProvider:forSnapshot:imageDataHandler:"
- "_generate_imageFromNewDataProvider:forSnapshot:imageDataHandler:"
- "_generate_lock"
- "_generate_lock_shouldGenerateForSnapshot:reason:"
- "_generationContext"
- "_groupID"
- "_handleMemoryPressure"
- "_hasClientObjectForKey:"
- "_hasGenerationContext"
- "_hasKnownBadLaunchImage"
- "_hasProtectedContent"
- "_identifier"
- "_identity"
- "_imageAccessCount"
- "_imageAccessFileManger"
- "_imageAccessQueue_saveData:forSnapshot:"
- "_imageDataRequest"
- "_imageGenerationQueue"
- "_imageGenerationWorkloop"
- "_imageGenerator"
- "_imageName"
- "_imageOpaque"
- "_imageOrientation"
- "_imageRespectsSafeAreaInsets"
- "_imageScale"
- "_imageTransform"
- "_init"
- "_initWithBSSettings:"
- "_initWithBundleIdentifier:bundlePath:dataContainerPath:bundleContainerPath:"
- "_initWithContainerIdentity:"
- "_initWithContainerIdentity:store:groupID:generationContext:"
- "_initWithIOSurface:scale:orientation:"
- "_initWithIdentifier:containerIdentity:"
- "_interfaceOrientation"
- "_invalidate"
- "_invalidated"
- "_invalidatedSignal"
- "_isDefault"
- "_isInvalidated"
- "_keepImageAccessForPreHeat"
- "_keepImageAccessUntilExpiration"
- "_key"
- "_lastUsedDate"
- "_launchImagePaths"
- "_launchInterfaceIdentifier"
- "_launchInterfaces"
- "_launchRequest"
- "_launchRequestProvider"
- "_launchRequests"
- "_launchRequestsForApplication:withCompatibilityInfo:"
- "_launchesOpaque"
- "_leftInset"
- "_loadCompatibilityInfoForBundleIdentifier:"
- "_loadImageLock"
- "_locked_loadImageViaGenerationContext:options:"
- "_locked_loadImageViaGeneratorFunction:"
- "_locked_synchronized_loadImageViaFile"
- "_logContainerIdentifierDirty"
- "_logIdentifier"
- "_loggingPrefix"
- "_mainDisplayConfiguration"
- "_manifestImpl"
- "_manifestQueueDecode_setStore:"
- "_manifestsByIdentity"
- "_name"
- "_naturalSize"
- "_navigationBarImageName"
- "_noteDirtied"
- "_opaque"
- "_outputFormatForSnapshot:"
- "_path"
- "_path:isRelativeToPath:outRelativePath:"
- "_pendingOperations"
- "_performImageDataGeneration:withHandler:"
- "_persistCompatibilityInfo:forBundleIdentifier:"
- "_predicate"
- "_propertyKeyForSnapshotKey:overriddenForNil:"
- "_purgeCachedImageIfAppropriate:"
- "_queue"
- "_reapExpiredAndInvalidSnapshots"
- "_reapingTimer"
- "_referenceBounds"
- "_referenceSize"
- "_relativePath"
- "_removeAllGeneratedLaunchImagesAndSnapshots"
- "_removeBundleIdentifierFromLaunchInterfaceDenyList:"
- "_removeClientObjectForKey:"
- "_removeLaunchImagesMatchingPredicate:forApplications:forgettingApps:"
- "_requiredOSVersion"
- "_resetBadLaunchInterfaceCount:"
- "_rightInset"
- "_sandboxPath"
- "_sanitizedPathForPath:"
- "_scale"
- "_scheduleArchivingIfNecessaryWithCompletion:"
- "_scheduleArchivingIfNecessaryWithDelay:completion:"
- "_scheduler"
- "_scheme"
- "_sendMessage:"
- "_sendMessage:withReplyHandler:waitForReply:waitDuration:"
- "_setClientObject:forKey:"
- "_setContainerIdentity:"
- "_setFileLocation:"
- "_setFilename:"
- "_setHasProtectedContent:"
- "_setLaunchInterfaces:"
- "_setPath:"
- "_setRelativePath:"
- "_settings"
- "_shouldDeleteFileOnPurge:"
- "_shouldDeny"
- "_shouldGenerateForSnapshot:reason:"
- "_snapshot"
- "_snapshotContainerPath"
- "_snapshotGroupsByID"
- "_snapshotPredicateForRequest:"
- "_snapshots"
- "_sortDescriptors"
- "_stateCaptureAssertion"
- "_statusBarOrientation"
- "_statusBarSettings"
- "_statusBarState"
- "_store"
- "_storeForBundleIdentifier:"
- "_stream"
- "_stringForBackgroundStyle:"
- "_stringForKey:"
- "_synchronizeDataStoreWithCompletion:"
- "_synchronized_evaluateImageAccessUntilExpirationEnablingIfNecessary:"
- "_synchronized_hasCachedImage:"
- "_synchronized_isExpired"
- "_tabBarImageName"
- "_timeout"
- "_toolbarImageName"
- "_topInset"
- "_type"
- "_updateStatusBarOrientation"
- "_urlSchemeName"
- "_urlSchemes"
- "_userInterfaceStyle"
- "_validateWithContainerIdentity:"
- "_variantID"
- "_variantsByID"
- "_weak_snapshot"
- "_workQueue"
- "_workloop_checkClientCount"
- "_workloop_decrementClientCount"
- "_workloop_incrementClientCount"
- "_workloop_noteManifestInvalidated:"
- "_workloop_reallyCheckClientCount"
- "acquireManifestForContainerIdentity:store:creatingIfNecessary:"
- "activeMultilinePrefix"
- "addEntriesFromDictionary:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addSnapshot:"
- "allInstalledApplications"
- "allKeys"
- "allKeysForObject:"
- "allObjects"
- "allSplashBoardApplications"
- "allValues"
- "allocWithZone:"
- "allocationSize"
- "allowsKeyedCoding"
- "allowsSavingLaunchImages"
- "andPredicateWithSubpredicates:"
- "appUsageStream"
- "appendArraySection:withName:multilinePrefix:skipIfEmpty:"
- "appendArraySection:withName:skipIfEmpty:"
- "appendBodySectionWithName:multilinePrefix:block:"
- "appendBool:"
- "appendBool:withName:"
- "appendDescriptionToBuilder:forFlag:object:ofSetting:"
- "appendDictionarySection:withName:skipIfEmpty:"
- "appendDouble:withName:decimalPrecision:"
- "appendEqualsBlocks:"
- "appendFloat:withName:"
- "appendFloat:withName:decimalPrecision:"
- "appendInt64:withName:"
- "appendInteger:"
- "appendInteger:withName:"
- "appendObject:"
- "appendObject:counterpart:"
- "appendObject:withName:"
- "appendObject:withName:skipIfNil:"
- "appendPointer:withName:"
- "appendRect:withName:"
- "appendSize:withName:"
- "appendString:counterpart:"
- "appendString:withName:"
- "appendString:withName:skipIfEmpty:"
- "appendUInt64:withName:"
- "appendUnsignedInteger:withName:"
- "applicationProvider"
- "archive"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayByAddingObject:"
- "arrayByApplyingSelector:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "autorelease"
- "badLaunchImageCandidateCount"
- "beginAccessBlockForBundleIdentifier:"
- "beginImageAccess"
- "beginImageAccessUntilExpiration"
- "beginSnapshotAccessTransaction:completion:"
- "beginTrackingImageDeletions"
- "boolForKey:"
- "boolForSetting:"
- "boolValue"
- "bounds"
- "bs_compactMap:"
- "bs_firstObjectPassingTest:"
- "bs_map:"
- "bs_secureDecodedFromData:"
- "build"
- "builder"
- "builderWithObject:"
- "builderWithObject:ofExpectedClass:"
- "bundleContainerURL"
- "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
- "bundleURL"
- "bundleWithPath:"
- "bytes"
- "caarFilePath"
- "caarPathForLaunchRequest:"
- "cachedImageForInterfaceOrientation:"
- "captureInfo"
- "captureLaunchImageForManifest:withCompatibilityInfo:launchRequests:createCaptureInfo:firstImageIsReady:withCompletionHandler:"
- "captureOrUpdateLaunchImagesForApplications:firstImageIsReady:completion:"
- "caseInsensitiveCompare:"
- "characterSetWithCharactersInString:"
- "class"
- "clearImageGenerator"
- "clearManifestDataForBundleIdentifier:"
- "code"
- "comparator"
- "compare:options:"
- "compatibilityInfoForAppInfo:"
- "compatibilityObject"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "configure:"
- "conformsToProtocol:"
- "containerPath"
- "containsObject:"
- "contextID"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createCaptureInfo"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createLaunchImageGeneratorWithContext:asyncImageData:error:"
- "createSnapshotWithGroupID:"
- "createVariantForSnapshot:withIdentifier:"
- "currentDevice"
- "currentHandler"
- "currentStyle"
- "d"
- "d16@0:8"
- "dataContainerURL"
- "dataForImage:withFormat:"
- "dataProviderClassName"
- "date"
- "dateByAddingTimeInterval:"
- "dateWithTimeIntervalSinceNow:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeCGRectForKey:"
- "decodeCGSizeForKey:"
- "decodeDoubleForKey:"
- "decodeInt64ForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCenter"
- "defaultGroupIdentifier"
- "defaultLaunchInterface"
- "defaultManager"
- "delegate"
- "deleteAllSnapshots"
- "deleteAllSnapshotsIfScreenSizeChanged"
- "deleteAllSystemSnapshots"
- "deleteSnapshot:"
- "deleteSnapshots:"
- "deleteSnapshotsForGroupID:"
- "deleteSnapshotsForGroupID:matchingPredicate:"
- "deleteSnapshotsForGroupID:predicateBuilder:"
- "deleteSnapshotsMatchingPredicate:"
- "deleteSnapshotsUsingPredicateBuilder:"
- "description"
- "descriptionBuilderWithMultilinePrefix:"
- "descriptionForObject:"
- "descriptionForStateCaptureWithMultilinePrefix:"
- "descriptionWithMultilinePrefix:"
- "descriptionWithoutVariants"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "distantPast"
- "domain"
- "doubleValue"
- "edgeInsets"
- "encodeBool:forKey:"
- "encodeCGRect:forKey:"
- "encodeCGSize:forKey:"
- "encodeDouble:forKey:"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodeWithXPCDictionary:"
- "endAccessBlockForBundleIdentifier:"
- "endImageAccess"
- "endTrackingImageDeletions"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumeratorAtPath:"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "enumeratorWithOptions:"
- "error"
- "estimatedMemoryImpact"
- "estimatedMemoryImpactForLaunchRequest:"
- "evaluateWithObject:"
- "eventQueryWithPredicate:eventStreams:offset:limit:sortDescriptors:"
- "executeQuery:error:"
- "expired"
- "extensionHostIdentifier"
- "fallbackSnapshotDataProvider"
- "fallbackXPCEncodableClass"
- "fetchImage"
- "fetchImageData:"
- "fetchImageForFormat:"
- "fetchRequest"
- "fileAttributes"
- "fileExists"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "fileSystemRepresentation"
- "fileSystemRepresentationWithPath:"
- "fileType"
- "fileURLWithPath:"
- "findRecentlyUsedOfApplications:"
- "firstObject"
- "flagForSetting:"
- "generate"
- "generateImageForSnapshot:dataProvider:options:imageGeneratedHandler:imageDataSavedHandler:"
- "generateImageForSnapshot:dataProvider:writeToFile:completion:"
- "generateImageForSnapshot:dataProvider:writeToFile:didGenerateImage:didSaveImage:"
- "generateImageForSnapshot:dataProvider:writeToFile:imageGeneratedHandler:imageDataSavedHandler:"
- "generateImageWithContext:captureInfo:error:"
- "getFlag"
- "getResourceValue:forKey:error:"
- "handleFailureInFunction:file:lineNumber:description:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handleTrackingStateChange"
- "hasBeenSignalled"
- "hasCachedImage"
- "hasFullSizedContent"
- "hasZeroInsets"
- "hash"
- "identityForApplicationInfo:"
- "identityForApplicationRecord:"
- "identityForBundleProxy:"
- "identityForCompatibilityInfo:"
- "identityWithBundleIdentifier:store:"
- "imageForInterfaceOrientation:"
- "imageForInterfaceOrientation:generationOptions:"
- "imageGenerator"
- "imageTransform"
- "indexOfObject:"
- "indexOfObjectIdenticalTo:"
- "indexesOfObjectsPassingTest:"
- "infoDictionary"
- "init"
- "initWithApplicationCompatibilityInfo:launchRequest:timeout:"
- "initWithApplicationInfo:"
- "initWithApplicationProxy:"
- "initWithArray:"
- "initWithBundle:"
- "initWithBundleIdentifier:store:"
- "initWithCGImage:scale:orientation:"
- "initWithCapacity:"
- "initWithCode:bundleID:reason:fatal:"
- "initWithCoder:"
- "initWithConfiguration:identifier:urlSchemes:isDefault:"
- "initWithConfigurationDictionary:"
- "initWithContainerIdentity:store:"
- "initWithContentsOfFile:options:error:"
- "initWithContextID:baseTransform:"
- "initWithData:scale:"
- "initWithDisplayConfiguration:layers:"
- "initWithDomain:code:userInfo:"
- "initWithFormat:"
- "initWithIOSurface:"
- "initWithIdentifier:"
- "initWithKey:ascending:comparator:"
- "initWithLaunchRequests:captureInfos:launchImagePaths:"
- "initWithMainDisplayConfiguration:applicationProvider:launchRequestProvider:"
- "initWithMainDisplayConfiguration:applicationProvider:launchRequestProvider:configureCacheDelete:"
- "initWithMainDisplayConfiguration:applicationProvider:launchRequestProvider:configureVolumeMaintenance:"
- "initWithObjects:count:"
- "initWithObjects:forKeys:count:"
- "initWithObjectsAndKeys:"
- "initWithPath:"
- "initWithRequest:contextID:opaque:"
- "initWithScheduler:snapshot:dataProvider:imageDataRequest:loggingPrefix:imageGenerationHandler:imageDataGenerationHandler:"
- "initWithServiceName:"
- "initWithServiceName:endpoint:"
- "initWithSnapshot:interfaceOrientation:"
- "initWithSnapshotContext:"
- "initWithTop:left:bottom:right:"
- "initWithType:name:identifier:urlSchemes:isDefault:"
- "initWithXPCDictionary:"
- "initialize"
- "insertObject:atIndex:"
- "integerValue"
- "interfaceOrientationMask"
- "invalidate"
- "invalidateImage"
- "ioSurface"
- "isAfterDate:"
- "isConfiguration"
- "isDeletableSystemApplication"
- "isEqual"
- "isEqual:"
- "isEqualToString:"
- "isExpired"
- "isExternal"
- "isFatal"
- "isFullScreen"
- "isHidden"
- "isImageOpaque"
- "isKindOfClass:"
- "isMainDisplay"
- "isMemberOfClass:"
- "isOpaque"
- "isProxy"
- "isStoryboard"
- "isUnderMemoryPressure"
- "isValid"
- "isValidImageFileExtension:"
- "isValidWithReason:"
- "isXIB"
- "ji56BO1mUeT7Qg9RO7Er9w"
- "keyDescriptionForSetting:"
- "knowledgeStore"
- "lastObject"
- "lastPathComponent"
- "launchImagePathForLaunchRequest:"
- "launchInterfaceExistsForScheme:"
- "launchInterfaceIdentifierForRequest:"
- "launchInterfaceWithIdentifier:"
- "launchRequestsForApplication:withCompatibilityInfo:defaultLaunchRequests:"
- "layer"
- "length"
- "loadImage"
- "loadImageForPreHeat"
- "loadImageWithGenerationOptions:"
- "loadManifestDataForBundleIdentifier:"
- "localizedInfoDictionary"
- "localizedStringFromDate:dateStyle:timeStyle:"
- "logIdentifier"
- "mainBundle"
- "makeWithEdgeInsets:"
- "manifest:didPurgeProtectedContentSnapshotsWithGroupIdentifiers:"
- "manifestImpl"
- "message"
- "mutableCopy"
- "mutableCopyWithZone:"
- "normalizeSnapshotName:"
- "notPredicateWithSubpredicate:"
- "now"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKey:ofClass:"
- "objectForKeyedSubscript:"
- "objectForSetting:"
- "objectsAtIndexes:"
- "objectsForKeys:"
- "orderedSetWithObject:"
- "pathExtension"
- "pathForResource:ofType:"
- "pathForResource:ofType:inDirectory:"
- "performAsync:"
- "performImageDataGenerationAsync:withHandler:"
- "performImageDataGenerationAsyncAndWait:withHandler:"
- "performImageGenerationAsync:"
- "performImageGenerationAsyncAndWait:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistManifestData:forBundleIdentifier:"
- "predicateForEventsWithStartInDateRangeFrom:to:"
- "predicateForObjectsWithMetadataKey:"
- "preheatServiceWithTimeout:"
- "processIdentifier"
- "processInfo"
- "processName"
- "purgeImage"
- "purgeSnapshotsWithProtectedContent"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "q24@0:8q16"
- "rangeOfString:"
- "recentlyUsedBundleIDs"
- "recursiveDescription"
- "release"
- "relinquishManifest:"
- "removeAllObjects"
- "removeCachedLaunchImagesForApplications:forgettingApps:"
- "removeItemAtPath:error:"
- "removeObject:"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "removeObserver:"
- "removeSnapshot:"
- "replaceObjectAtIndex:withObject:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "safeArchivedObjectForKey:ofType:"
- "safeObjectForKey:ofType:"
- "saveSnapshot:atPath:withContext:"
- "scheduleGeneration"
- "scheduleWithFireInterval:leewayInterval:queue:handler:"
- "secureCodableCustomExtendedDataClasses"
- "sentinelWithQueue:signalCount:completion:"
- "set"
- "setArchivedObject:forKey:"
- "setAscending:"
- "setBackgroundActivityEnabled:"
- "setBackgroundStyle:"
- "setBadLaunchImageCandidateCount:"
- "setBundleContainerPath:"
- "setBundleIdentifier:"
- "setBundlePath:"
- "setCaarFilePath:"
- "setClass:forClassName:"
- "setClassicMode:"
- "setComparator:"
- "setCompatibilityMode:"
- "setContainerIdentity:"
- "setContentFrame:"
- "setContentType:"
- "setContentTypeMask:"
- "setCustomSafeAreaInsets:"
- "setDataProviderClassName:"
- "setDefaultGroupIdentifier:"
- "setDelegate:"
- "setDescriptionProvider:"
- "setDisplayConfiguration:"
- "setEstimatedMemoryImpact:"
- "setExpirationDate:"
- "setExtendedData:"
- "setFallbackGenerationContext:"
- "setFileLocation:"
- "setFlag:"
- "setFlag:forSetting:"
- "setFullScreen:"
- "setGroupID:"
- "setHasKnownBadLaunchImage:"
- "setHidden:"
- "setIdentifier:"
- "setImageGeneratingByProvider:withBlockingImageGenerator:"
- "setImageGenerator:"
- "setImageOpaque:"
- "setImageOrientation:"
- "setImageScale:"
- "setImageTransform:"
- "setInterfaceOrientation:"
- "setInterfaceOrientationMask:"
- "setKey:"
- "setLastUsedDate:"
- "setLaunchInterfaceIdentifier:"
- "setLaunchesOpaque:"
- "setName:"
- "setNaturalSize:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setObject:forSetting:"
- "setOpaque:"
- "setPredicate:"
- "setReferenceSize:"
- "setRequiredOSVersion:"
- "setSandboxPath:"
- "setScale:"
- "setScheme:"
- "setSecureCodableCustomExtendedDataClasses:"
- "setSnapshotSize:"
- "setSortDescriptors:"
- "setStatusBarSettings:"
- "setStatusBarState:"
- "setStatusBarStateMask:"
- "setStream:"
- "setStyle:"
- "setType:"
- "setUrlSchemeName:"
- "setUrlSchemes:"
- "setUseDebugDescription:"
- "setUserInterfaceStyle:"
- "setVariantID:"
- "setWithArray:"
- "setWithObjects:"
- "set_default:"
- "settings:appendDescriptionToBuilder:forFlag:object:ofSetting:"
- "settings:keyDescriptionForSetting:"
- "settings:valueDescriptionForFlag:object:ofSetting:"
- "sharedApplication"
- "sharedInstance"
- "shouldDeny"
- "signal"
- "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
- "snapshotContainerPath"
- "snapshotContainerPathForGroupID:"
- "snapshotContainerPathForSnapshot:"
- "snapshotWithSignature:duration:events:payload:actions:reply:"
- "snapshotsConsideredUnpurgableByAPFS"
- "snapshotsForGroupID:"
- "snapshotsForGroupID:fetchRequest:"
- "snapshotsForGroupID:matchingPredicate:"
- "snapshotsForGroupIDs:"
- "snapshotsForGroupIDs:fetchRequest:"
- "snapshotsForGroupIDs:matchingPredicate:"
- "sortDescriptorWithKey:ascending:"
- "sortDescriptorWithKey:ascending:comparator:"
- "sortUsingDescriptors:"
- "splashBoardSystemApplications"
- "standardUserDefaults"
- "statusBarHiddenForInterfaceOrientation:onDisplay:"
- "statusBarOrientation"
- "storeForApplication:"
- "stream"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByDeletingLastPathComponent"
- "stringByDeletingPathExtension"
- "stringByTrimmingCharactersInSet:"
- "stringForKey:"
- "stringForStatusBarStyle:"
- "stringValue"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "substringFromIndex:"
- "succinctDescription"
- "succinctDescriptionBuilder"
- "superclass"
- "supportedUserInterfaceStyle"
- "supportsInterfaceOrientation:"
- "supportsSecureCoding"
- "synchronize"
- "synchronizeForBundleIdentifier:withCompletion:"
- "synchronizeWithCompletion:"
- "tags"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "unarchivedObjectOfClass:fromData:error:"
- "unionSet:"
- "unsignedIntegerValue"
- "updateSnapshotsAPFSPurgability:"
- "use initWithDefaultService"
- "userInterfaceIdiom"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSObject<OS_xpc_object>\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8Q16"
- "v24@0:8^{__FSEventStream=}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v32@0:8@\"NSData\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?>24"
- "v32@0:8@\"XBApplicationSnapshotManifest\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@?16@?24"
- "v32@0:8@?<v@?>16@?<v@?>24"
- "v32@0:8d16@?24"
- "v32@0:8{CGSize=dd}16"
- "v36@0:8@16@24B32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@?24@?32"
- "v44@0:8@16@24B32@?36"
- "v44@0:8@16@?24B32@?36"
- "v48@0:8B16@20@28@?36I44"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v52@0:8@16@24B32@?36@?44"
- "v56@0:8@16@24Q32@?40@?48"
- "v60@0:8@16@24@32B40@?44@?52"
- "v64@0:8@16@24@32B40@44B52@?56"
- "v64@0:8{CGAffineTransform=dddddd}16"
- "v68@0:8@16@24B32@36@44@?52I60B64"
- "valueDescriptionForFlag:object:ofSetting:"
- "valueForKey:"
- "valueWithCGSize:"
- "variantWithIdentifier:"
- "willDeleteVariant:"
- "withTimeout"
- "xb_supportsUserInterfaceStyle:"
- "xb_userInterfaceStyleForRequestedUserInterfaceStyle:"
- "zone"
- "{CGAffineTransform=\"a\"d\"b\"d\"c\"d\"d\"d\"tx\"d\"ty\"d}"
- "{CGAffineTransform=dddddd}16@0:8"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{UIEdgeInsets=dddd}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
