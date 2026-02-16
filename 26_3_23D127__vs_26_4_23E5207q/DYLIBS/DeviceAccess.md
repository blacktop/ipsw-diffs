## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

```diff

-323.7.0.0.0
-  __TEXT.__text: 0x3b694
-  __TEXT.__auth_stubs: 0x1530
-  __TEXT.__objc_methlist: 0x30e4
-  __TEXT.__cstring: 0x64c2
-  __TEXT.__gcc_except_tab: 0x8c8
-  __TEXT.__const: 0x5c8
-  __TEXT.__swift5_typeref: 0x258
+324.20.1.1.1
+  __TEXT.__text: 0x484dc
+  __TEXT.__auth_stubs: 0x14f0
+  __TEXT.__objc_methlist: 0x3b44
+  __TEXT.__const: 0x608
+  __TEXT.__cstring: 0x7be3
+  __TEXT.__gcc_except_tab: 0xaf8
   __TEXT.__constg_swiftt: 0x3d0
+  __TEXT.__swift5_typeref: 0x258
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__swift5_reflstr: 0x128
   __TEXT.__swift5_fieldmd: 0x164
-  __TEXT.__oslogstring: 0x30d
+  __TEXT.__oslogstring: 0x32d
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0xd98
-  __TEXT.__eh_frame: 0x5b8
-  __TEXT.__objc_classname: 0x49d
-  __TEXT.__objc_methname: 0x6072
-  __TEXT.__objc_methtype: 0x977
-  __TEXT.__objc_stubs: 0x3100
-  __DATA_CONST.__got: 0x458
-  __DATA_CONST.__const: 0x9b8
-  __DATA_CONST.__objc_classlist: 0x170
+  __TEXT.__unwind_info: 0x1168
+  __TEXT.__eh_frame: 0x570
+  __TEXT.__objc_classname: 0x5c4
+  __TEXT.__objc_methname: 0x7821
+  __TEXT.__objc_methtype: 0xac6
+  __TEXT.__objc_stubs: 0x3ce0
+  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__const: 0xc08
+  __DATA_CONST.__objc_classlist: 0x1a8
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1608
+  __DATA_CONST.__objc_selrefs: 0x1b08
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x118
-  __AUTH_CONST.__auth_got: 0xaa8
-  __AUTH_CONST.__const: 0x530
-  __AUTH_CONST.__cfstring: 0x2780
-  __AUTH_CONST.__objc_const: 0x5840
+  __DATA_CONST.__objc_superrefs: 0x150
+  __DATA_CONST.__objc_arraydata: 0x30
+  __AUTH_CONST.__auth_got: 0xa88
+  __AUTH_CONST.__const: 0x690
+  __AUTH_CONST.__cfstring: 0x2fe0
+  __AUTH_CONST.__objc_const: 0x6bc0
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH.__objc_data: 0x6b0
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0x8e0
   __AUTH.__data: 0x288
-  __DATA.__objc_ivar: 0x4b4
-  __DATA.__data: 0xb50
-  __DATA.__bss: 0x2c0
+  __DATA.__objc_ivar: 0x5ec
+  __DATA.__data: 0xc30
+  __DATA.__bss: 0x2e0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__data: 0x78

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 470A8B5E-56B1-3059-9252-8E4FE927D01A
-  Functions: 1555
-  Symbols:   4403
-  CStrings:  2644
+  UUID: 1F823DA7-0460-3C8C-9822-5C545AFA2096
+  Functions: 1963
+  Symbols:   5527
+  CStrings:  3197
 
Symbols:
+ +[DAAppAsset supportsSecureCoding]
+ +[DAAppAssetManager sharedManager]
+ +[DAAppAssetManager sharedManager].cold.1
+ +[DADeviceRegistry supportsSecureCoding]
+ +[DAExtensionSession bluetoothRestorationIDForBundleID:error:]
+ +[DAExtensionSession launchExtensionWithBundle:extensionType:]
+ +[DAExtensionSession resumeExtensionWithBundle:extensionType:]
+ +[DAExtensionSession suspendExtensionWithBundle:extensionType:]
+ +[DAExtensionSession suspendExtensionWithBundle:extensionType:extensionCapabilityFlags:]
+ +[DAIncomingMessage supportsSecureCoding]
+ +[DAOutgoingMessage supportsSecureCoding]
+ +[DASession fetchAppAssetForBundleID:error:]
+ +[DASession preflightMigrationWithConfigurations:session:error:]
+ +[DASession preflightMigrationWithConfigurations:session:error:].cold.1
+ +[DASession preflightMigrationWithConfigurations:session:error:].cold.2
+ +[DASession processAllowedWithAuditToken:error:].cold.2
+ +[DASession testProxFlow:manufacturerID:modelID:]
+ -[DAAppAsset .cxx_destruct]
+ -[DAAppAsset adamID]
+ -[DAAppAsset appName]
+ -[DAAppAsset bundleID]
+ -[DAAppAsset cachedDate]
+ -[DAAppAsset description]
+ -[DAAppAsset developerName]
+ -[DAAppAsset encodeWithCoder:]
+ -[DAAppAsset iconData]
+ -[DAAppAsset initWithBundleID:adamID:appName:developerName:iconData:]
+ -[DAAppAsset initWithCoder:]
+ -[DAAppAsset isExpired]
+ -[DAAppAssetManager .cxx_destruct]
+ -[DAAppAssetManager _cacheAsset:]
+ -[DAAppAssetManager _createCacheFileURL]
+ -[DAAppAssetManager _loadCache]
+ -[DAAppAssetManager _loadCache].cold.1
+ -[DAAppAssetManager _loadCache].cold.2
+ -[DAAppAssetManager _loadCache].cold.3
+ -[DAAppAssetManager _loadCachedAssetForBundleID:]
+ -[DAAppAssetManager _pruneCache:]
+ -[DAAppAssetManager _writeCache:]
+ -[DAAppAssetManager _writeCache:].cold.1
+ -[DAAppAssetManager _writeCache:].cold.2
+ -[DAAppAssetManager clearAllCache]
+ -[DAAppAssetManager clearAllCache].cold.1
+ -[DAAppAssetManager getAppAssetForBundleID:completion:]
+ -[DAAppAssetManager getAppAssetForBundleID:completion:].cold.1
+ -[DAAppAssetManager initInternal]
+ -[DAAppAssetManager initInternal].cold.1
+ -[DAAppAssetManager removeCacheForBundleID:]
+ -[DADevice deviceRegistry]
+ -[DADevice setDeviceRegistry:]
+ -[DADeviceAppAccessInfo devicePushToken]
+ -[DADeviceAppAccessInfo devicePushTopic]
+ -[DADeviceAppAccessInfo setDevicePushToken:]
+ -[DADeviceAppAccessInfo setDevicePushTopic:]
+ -[DADeviceRegistry .cxx_destruct]
+ -[DADeviceRegistry companionAppBundleID]
+ -[DADeviceRegistry companionAppIsOptional]
+ -[DADeviceRegistry copyWithZone:]
+ -[DADeviceRegistry description]
+ -[DADeviceRegistry encodeWithCoder:]
+ -[DADeviceRegistry encodeWithXPCObject:]
+ -[DADeviceRegistry friendlyName]
+ -[DADeviceRegistry hash]
+ -[DADeviceRegistry image2xData]
+ -[DADeviceRegistry image3xData]
+ -[DADeviceRegistry initWithCoder:]
+ -[DADeviceRegistry initWithManufacturerID:modelID:]
+ -[DADeviceRegistry initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoData:companionAppBundleID:companionAppIsOptional:]
+ -[DADeviceRegistry initWithManufacturerID:modelID:info:]
+ -[DADeviceRegistry initWithXPCObject:error:]
+ -[DADeviceRegistry isEqual:]
+ -[DADeviceRegistry manufacturerID]
+ -[DADeviceRegistry modelID]
+ -[DADeviceRegistry videoData]
+ -[DADeviceRegistryInfo .cxx_destruct]
+ -[DADeviceRegistryInfo companionAppBundleID]
+ -[DADeviceRegistryInfo companionAppIsOptional]
+ -[DADeviceRegistryInfo copyWithZone:]
+ -[DADeviceRegistryInfo description]
+ -[DADeviceRegistryInfo friendlyName]
+ -[DADeviceRegistryInfo image2xData]
+ -[DADeviceRegistryInfo image3xData]
+ -[DADeviceRegistryInfo init]
+ -[DADeviceRegistryInfo setCompanionAppBundleID:]
+ -[DADeviceRegistryInfo setCompanionAppIsOptional:]
+ -[DADeviceRegistryInfo setFriendlyName:]
+ -[DADeviceRegistryInfo setImage2xData:]
+ -[DADeviceRegistryInfo setImage3xData:]
+ -[DADeviceRegistryInfo setVideoData:]
+ -[DADeviceRegistryInfo videoData]
+ -[DAEventExtension capabilityFlag]
+ -[DAEventExtension sessionID]
+ -[DAEventExtension setCapabilityFlag:]
+ -[DAEventExtension setSessionID:]
+ -[DAExtension _activateExtension:]
+ -[DAExtension _capabilitiesEnsureStarted:]
+ -[DAExtension _handleCapabilityInterrupted:]
+ -[DAExtension _handleCapabilityInvalidated:]
+ -[DAExtension _invalidateCapabilities]
+ -[DAExtension _invalidated:]
+ -[DAExtension _invalidated:].cold.1
+ -[DAExtension _invalidated:].cold.2
+ -[DAExtension _sandboxExtensionIssueMach:]
+ -[DAExtension _sandboxExtensionIssueMach:].cold.1
+ -[DAExtension _sandboxExtensionIssueMach:].cold.2
+ -[DAExtension _sandboxExtensionIssueMach:].cold.3
+ -[DAExtension _sandboxExtensionIssueMach:].cold.4
+ -[DAExtension _sandboxExtensionIssueMach:].cold.5
+ -[DAExtension _sandboxExtensionIssueMach:].cold.6
+ -[DAExtension _sandboxExtensionIssueMach:].cold.7
+ -[DAExtension _startExtension:]
+ -[DAExtension _startExtension:].cold.1
+ -[DAExtension _startExtension:].cold.2
+ -[DAExtension _updateWithError:]
+ -[DAExtension capabilitiesForFlags:]
+ -[DAExtension capabilityWithSessionID:]
+ -[DAExtension enrolledFlags]
+ -[DAExtension invalidateDone]
+ -[DAExtension setEnrolledFlags:]
+ -[DAExtension setEnrolledFlags:].cold.1
+ -[DAExtension setInvalidateDone:]
+ -[DAExtensionCapability .cxx_destruct]
+ -[DAExtensionCapability _activateDirect]
+ -[DAExtensionCapability _activated]
+ -[DAExtensionCapability _activated].cold.1
+ -[DAExtensionCapability _interrupted]
+ -[DAExtensionCapability _interrupted].cold.1
+ -[DAExtensionCapability _invalidate]
+ -[DAExtensionCapability _invalidate].cold.1
+ -[DAExtensionCapability _invalidated]
+ -[DAExtensionCapability _invalidated].cold.1
+ -[DAExtensionCapability _invalidated].cold.2
+ -[DAExtensionCapability _reportEventType:]
+ -[DAExtensionCapability _sandboxExtensionIssueMach:]
+ -[DAExtensionCapability _sandboxExtensionIssueMach:].cold.1
+ -[DAExtensionCapability _sandboxExtensionIssueMach:].cold.2
+ -[DAExtensionCapability _sandboxExtensionIssueMach:].cold.3
+ -[DAExtensionCapability _sandboxExtensionIssueMach:].cold.4
+ -[DAExtensionCapability _sandboxExtensionIssueMach:].cold.5
+ -[DAExtensionCapability _sandboxExtensionIssueMach:].cold.6
+ -[DAExtensionCapability _sandboxExtensionIssueMach:].cold.7
+ -[DAExtensionCapability _startCapability:]
+ -[DAExtensionCapability _startCapability:].cold.1
+ -[DAExtensionCapability _startCapability:].cold.2
+ -[DAExtensionCapability activate]
+ -[DAExtensionCapability capabilityFlag]
+ -[DAExtensionCapability capabilityID]
+ -[DAExtensionCapability descriptionWithLevel:]
+ -[DAExtensionCapability description]
+ -[DAExtensionCapability encodeWithXPCObject:]
+ -[DAExtensionCapability endpoint]
+ -[DAExtensionCapability eventHandler]
+ -[DAExtensionCapability identifier]
+ -[DAExtensionCapability initWithIdentity:device:capabilityID:]
+ -[DAExtensionCapability initWithXPCObject:error:]
+ -[DAExtensionCapability invalidateWithReason:]
+ -[DAExtensionCapability invalidate]
+ -[DAExtensionCapability invalidationHandler]
+ -[DAExtensionCapability pid]
+ -[DAExtensionCapability reportEvent:]
+ -[DAExtensionCapability reportEvent:].cold.1
+ -[DAExtensionCapability reportEvent:].cold.2
+ -[DAExtensionCapability reportEventToExtension:]
+ -[DAExtensionCapability reportEventToExtension:].cold.1
+ -[DAExtensionCapability setEndpoint:]
+ -[DAExtensionCapability setEventHandler:]
+ -[DAExtensionCapability setInvalidationHandler:]
+ -[DAExtensionCapability setPid:]
+ -[DAExtensionEventData initWithDevice:data:]
+ -[DAExtensionEventData initWithDevice:data:sessionID:]
+ -[DAExtensionEventLifecycle .cxx_destruct]
+ -[DAExtensionEventLifecycle extensionCapability]
+ -[DAExtensionEventLifecycle newState]
+ -[DAExtensionEventLifecycle previousState]
+ -[DAExtensionEventLifecycle setExtensionCapability:]
+ -[DAExtensionSession _updateIfNeededWithBlock:]
+ -[DAExtensionSession _update]
+ -[DAExtensionSession _update].cold.1
+ -[DAExtensionSession _update].cold.2
+ -[DAExtensionSession getEndpointsForCapabilityFlags:completionHandler:]
+ -[DAExtensionSession hash]
+ -[DAExtensionSession isEqual:]
+ -[DAExtensionSession launch]
+ -[DAExtensionSession resume]
+ -[DAExtensionSession suspend]
+ -[DAExtensionSession terminate]
+ -[DAExtensionSession updateWithConfiguration:]
+ -[DAExtensionSession updateWithDAExtensionSession:]
+ -[DAExtensionSessionConfiguration bluetoothRestorationIdentifier]
+ -[DAExtensionSessionConfiguration capabilityFlags]
+ -[DAExtensionSessionConfiguration initWithBluetoothRestorationID:]
+ -[DAExtensionSessionConfiguration initWithBluetoothRestorationID:].cold.1
+ -[DAExtensionSessionConfiguration pid]
+ -[DAExtensionSessionConfiguration setBluetoothRestorationIdentifier:]
+ -[DAExtensionSessionConfiguration setCapabilityFlags:]
+ -[DAExtensionSessionConfiguration setPid:]
+ -[DAExtensionSessionConfiguration updateWithDAExtensionSessionConfiguration:]
+ -[DAIncomingMessage .cxx_destruct]
+ -[DAIncomingMessage copyWithZone:]
+ -[DAIncomingMessage description]
+ -[DAIncomingMessage encodeWithCoder:]
+ -[DAIncomingMessage encryptedPayloadData]
+ -[DAIncomingMessage expiresAt]
+ -[DAIncomingMessage featureID]
+ -[DAIncomingMessage initWithCoder:]
+ -[DAIncomingMessage initWithCoder:].cold.1
+ -[DAIncomingMessage initWithMessageID:encryptedPayloadData:]
+ -[DAIncomingMessage messageID]
+ -[DAIncomingMessage payloadVersion]
+ -[DAIncomingMessage receivedAt]
+ -[DAIncomingMessage setEncryptedPayloadData:]
+ -[DAIncomingMessage setExpiresAt:]
+ -[DAIncomingMessage setFeatureID:]
+ -[DAIncomingMessage setMessageID:]
+ -[DAIncomingMessage setPayloadVersion:]
+ -[DAIncomingMessage setReceivedAt:]
+ -[DAIncomingMessage setSourceDeviceID:]
+ -[DAIncomingMessage sourceDeviceID]
+ -[DAOutgoingMessage .cxx_destruct]
+ -[DAOutgoingMessage bundleID]
+ -[DAOutgoingMessage cbRestorationID]
+ -[DAOutgoingMessage copyWithZone:]
+ -[DAOutgoingMessage description]
+ -[DAOutgoingMessage destinationDeviceID]
+ -[DAOutgoingMessage encodeWithCoder:]
+ -[DAOutgoingMessage expiresAt]
+ -[DAOutgoingMessage featureID]
+ -[DAOutgoingMessage initWithCoder:]
+ -[DAOutgoingMessage initWithCoder:].cold.1
+ -[DAOutgoingMessage initWithMessageID:payloadData:]
+ -[DAOutgoingMessage initWithMessageID:payloadFilePath:]
+ -[DAOutgoingMessage lastAttemptedAt]
+ -[DAOutgoingMessage messageID]
+ -[DAOutgoingMessage originatedAt]
+ -[DAOutgoingMessage payloadData]
+ -[DAOutgoingMessage payloadFilePath]
+ -[DAOutgoingMessage payloadSize]
+ -[DAOutgoingMessage payloadVersion]
+ -[DAOutgoingMessage queueOneIdentifier]
+ -[DAOutgoingMessage retryCount]
+ -[DAOutgoingMessage setBundleID:]
+ -[DAOutgoingMessage setCbRestorationID:]
+ -[DAOutgoingMessage setDestinationDeviceID:]
+ -[DAOutgoingMessage setExpiresAt:]
+ -[DAOutgoingMessage setFeatureID:]
+ -[DAOutgoingMessage setLastAttemptedAt:]
+ -[DAOutgoingMessage setMessageID:]
+ -[DAOutgoingMessage setOriginatedAt:]
+ -[DAOutgoingMessage setPayloadData:]
+ -[DAOutgoingMessage setPayloadFilePath:]
+ -[DAOutgoingMessage setPayloadVersion:]
+ -[DAOutgoingMessage setQueueOneIdentifier:]
+ -[DAOutgoingMessage setRetryCount:]
+ -[DAOutgoingMessage setTransportPriority:]
+ -[DAOutgoingMessage transportPriority]
+ -[DASession diagnosticControl:completion:]
+ -[DASession preflightMigrationWithConfigurations:completionHandler:]
+ -[_EXCapabilityEndpoint(CUXPCCodable) encodeWithXPCObject:]
+ -[_EXCapabilityEndpoint(CUXPCCodable) initWithXPCObject:error:]
+ GCC_except_table16
+ GCC_except_table18
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table47
+ GCC_except_table51
+ GCC_except_table55
+ GCC_except_table56
+ GCC_except_table7
+ GCC_except_table76
+ GCC_except_table8
+ _DAExtensionCapabilityFlagsFromString
+ _DAExtensionCapabilityFlagsToString
+ _DAExtensionCapabilityFlagsToTCCStrings
+ _DAExtensionPointEntitlementAccessoryDataProvider
+ _DAExtensionPointEntitlementAccessoryTransportSecurity
+ _DAExtensionPointIdentifierAccessoryDataProvider
+ _DAExtensionPointIdentifierAccessoryTransportSecurity
+ _DAMessageDefaultIncomingExpirationInterval
+ _DAMessageDefaultOutgoingExpirationInterval
+ _IsAppleInternalBuild
+ _NSKeyedArchiveRootObjectKey
+ _NSStringFromClass
+ _OBJC_CLASS_$_DAAppAsset
+ _OBJC_CLASS_$_DAAppAssetManager
+ _OBJC_CLASS_$_DADeviceRegistry
+ _OBJC_CLASS_$_DADeviceRegistryInfo
+ _OBJC_CLASS_$_DAExtensionCapability
+ _OBJC_CLASS_$_DAIncomingMessage
+ _OBJC_CLASS_$_DAOutgoingMessage
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSXPCDecoder
+ _OBJC_CLASS_$_NSXPCEncoder
+ _OBJC_CLASS_$__EXCapabilityEndpoint
+ _OBJC_CLASS_$__EXCapabilityHostSession
+ _OBJC_CLASS_$__EXCapabilityHostSessionConfiguration
+ _OBJC_CLASS_$__EXCapabilitySessionIdentity
+ _OBJC_IVAR_$_DAAppAsset._adamID
+ _OBJC_IVAR_$_DAAppAsset._appName
+ _OBJC_IVAR_$_DAAppAsset._bundleID
+ _OBJC_IVAR_$_DAAppAsset._cachedDate
+ _OBJC_IVAR_$_DAAppAsset._developerName
+ _OBJC_IVAR_$_DAAppAsset._iconData
+ _OBJC_IVAR_$_DAAppAssetManager._cacheFileURL
+ _OBJC_IVAR_$_DAAppAssetManager._queue
+ _OBJC_IVAR_$_DADevice._deviceRegistry
+ _OBJC_IVAR_$_DADeviceAppAccessInfo._devicePushToken
+ _OBJC_IVAR_$_DADeviceAppAccessInfo._devicePushTopic
+ _OBJC_IVAR_$_DADeviceRegistry._companionAppBundleID
+ _OBJC_IVAR_$_DADeviceRegistry._companionAppIsOptional
+ _OBJC_IVAR_$_DADeviceRegistry._friendlyName
+ _OBJC_IVAR_$_DADeviceRegistry._image2xData
+ _OBJC_IVAR_$_DADeviceRegistry._image3xData
+ _OBJC_IVAR_$_DADeviceRegistry._manufacturerID
+ _OBJC_IVAR_$_DADeviceRegistry._modelID
+ _OBJC_IVAR_$_DADeviceRegistry._videoData
+ _OBJC_IVAR_$_DADeviceRegistryInfo._companionAppBundleID
+ _OBJC_IVAR_$_DADeviceRegistryInfo._companionAppIsOptional
+ _OBJC_IVAR_$_DADeviceRegistryInfo._friendlyName
+ _OBJC_IVAR_$_DADeviceRegistryInfo._image2xData
+ _OBJC_IVAR_$_DADeviceRegistryInfo._image3xData
+ _OBJC_IVAR_$_DADeviceRegistryInfo._videoData
+ _OBJC_IVAR_$_DAEventExtension._capabilityFlag
+ _OBJC_IVAR_$_DAEventExtension._sessionID
+ _OBJC_IVAR_$_DAExtension._capabilitesMap
+ _OBJC_IVAR_$_DAExtension._capabilityFlags
+ _OBJC_IVAR_$_DAExtension._enrolledFlags
+ _OBJC_IVAR_$_DAExtension._extensionFlags
+ _OBJC_IVAR_$_DAExtensionCapability._activateCalled
+ _OBJC_IVAR_$_DAExtensionCapability._bundleID
+ _OBJC_IVAR_$_DAExtensionCapability._capabilityFlag
+ _OBJC_IVAR_$_DAExtensionCapability._capabilityID
+ _OBJC_IVAR_$_DAExtensionCapability._clientInvalidated
+ _OBJC_IVAR_$_DAExtensionCapability._device
+ _OBJC_IVAR_$_DAExtensionCapability._dispatchQueue
+ _OBJC_IVAR_$_DAExtensionCapability._endpoint
+ _OBJC_IVAR_$_DAExtensionCapability._eventHandler
+ _OBJC_IVAR_$_DAExtensionCapability._extensionIdentity
+ _OBJC_IVAR_$_DAExtensionCapability._extensionSession
+ _OBJC_IVAR_$_DAExtensionCapability._identifier
+ _OBJC_IVAR_$_DAExtensionCapability._invalidateCalled
+ _OBJC_IVAR_$_DAExtensionCapability._invalidateDone
+ _OBJC_IVAR_$_DAExtensionCapability._invalidateReason
+ _OBJC_IVAR_$_DAExtensionCapability._invalidationHandler
+ _OBJC_IVAR_$_DAExtensionCapability._pid
+ _OBJC_IVAR_$_DAExtensionCapability._sessionUUID
+ _OBJC_IVAR_$_DAExtensionCapability._xpcConnection
+ _OBJC_IVAR_$_DAExtensionEventLifecycle._extensionCapability
+ _OBJC_IVAR_$_DAExtensionEventLifecycle._newState
+ _OBJC_IVAR_$_DAExtensionEventLifecycle._previousState
+ _OBJC_IVAR_$_DAExtensionSession._changesPending
+ _OBJC_IVAR_$_DAExtensionSession._extensionCapabilityMap
+ _OBJC_IVAR_$_DAExtensionSessionConfiguration._bluetoothRestorationIdentifier
+ _OBJC_IVAR_$_DAExtensionSessionConfiguration._capabilityFlags
+ _OBJC_IVAR_$_DAExtensionSessionConfiguration._pid
+ _OBJC_IVAR_$_DAIncomingMessage._encryptedPayloadData
+ _OBJC_IVAR_$_DAIncomingMessage._expiresAt
+ _OBJC_IVAR_$_DAIncomingMessage._featureID
+ _OBJC_IVAR_$_DAIncomingMessage._messageID
+ _OBJC_IVAR_$_DAIncomingMessage._payloadVersion
+ _OBJC_IVAR_$_DAIncomingMessage._receivedAt
+ _OBJC_IVAR_$_DAIncomingMessage._sourceDeviceID
+ _OBJC_IVAR_$_DAOutgoingMessage._bundleID
+ _OBJC_IVAR_$_DAOutgoingMessage._cbRestorationID
+ _OBJC_IVAR_$_DAOutgoingMessage._destinationDeviceID
+ _OBJC_IVAR_$_DAOutgoingMessage._expiresAt
+ _OBJC_IVAR_$_DAOutgoingMessage._featureID
+ _OBJC_IVAR_$_DAOutgoingMessage._lastAttemptedAt
+ _OBJC_IVAR_$_DAOutgoingMessage._messageID
+ _OBJC_IVAR_$_DAOutgoingMessage._originatedAt
+ _OBJC_IVAR_$_DAOutgoingMessage._payloadData
+ _OBJC_IVAR_$_DAOutgoingMessage._payloadFilePath
+ _OBJC_IVAR_$_DAOutgoingMessage._payloadVersion
+ _OBJC_IVAR_$_DAOutgoingMessage._queueOneIdentifier
+ _OBJC_IVAR_$_DAOutgoingMessage._retryCount
+ _OBJC_IVAR_$_DAOutgoingMessage._transportPriority
+ _OBJC_METACLASS_$_DAAppAsset
+ _OBJC_METACLASS_$_DAAppAssetManager
+ _OBJC_METACLASS_$_DADeviceRegistry
+ _OBJC_METACLASS_$_DADeviceRegistryInfo
+ _OBJC_METACLASS_$_DAExtensionCapability
+ _OBJC_METACLASS_$_DAIncomingMessage
+ _OBJC_METACLASS_$_DAOutgoingMessage
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ __OBJC_$_CATEGORY_INSTANCE_METHODS__EXCapabilityEndpoint_$_CUXPCCodable
+ __OBJC_$_CATEGORY__EXCapabilityEndpoint_$_CUXPCCodable
+ __OBJC_$_CLASS_METHODS_DAAppAsset
+ __OBJC_$_CLASS_METHODS_DAAppAssetManager
+ __OBJC_$_CLASS_METHODS_DADeviceRegistry
+ __OBJC_$_CLASS_METHODS_DAExtensionSession
+ __OBJC_$_CLASS_METHODS_DAIncomingMessage
+ __OBJC_$_CLASS_METHODS_DAOutgoingMessage
+ __OBJC_$_CLASS_PROP_LIST_DAAppAsset
+ __OBJC_$_CLASS_PROP_LIST_DAAppAssetManager
+ __OBJC_$_CLASS_PROP_LIST_DADeviceRegistry
+ __OBJC_$_CLASS_PROP_LIST_DAIncomingMessage
+ __OBJC_$_CLASS_PROP_LIST_DAOutgoingMessage
+ __OBJC_$_INSTANCE_METHODS_DAAppAsset
+ __OBJC_$_INSTANCE_METHODS_DAAppAssetManager
+ __OBJC_$_INSTANCE_METHODS_DADeviceRegistry(DeviceAccess)
+ __OBJC_$_INSTANCE_METHODS_DADeviceRegistryInfo
+ __OBJC_$_INSTANCE_METHODS_DAExtensionCapability
+ __OBJC_$_INSTANCE_METHODS_DAIncomingMessage
+ __OBJC_$_INSTANCE_METHODS_DAOutgoingMessage
+ __OBJC_$_INSTANCE_VARIABLES_DAAppAsset
+ __OBJC_$_INSTANCE_VARIABLES_DAAppAssetManager
+ __OBJC_$_INSTANCE_VARIABLES_DADeviceRegistry
+ __OBJC_$_INSTANCE_VARIABLES_DADeviceRegistryInfo
+ __OBJC_$_INSTANCE_VARIABLES_DAExtensionCapability
+ __OBJC_$_INSTANCE_VARIABLES_DAExtensionEventLifecycle
+ __OBJC_$_INSTANCE_VARIABLES_DAIncomingMessage
+ __OBJC_$_INSTANCE_VARIABLES_DAOutgoingMessage
+ __OBJC_$_PROP_LIST_DAAppAsset
+ __OBJC_$_PROP_LIST_DADeviceRegistry
+ __OBJC_$_PROP_LIST_DADeviceRegistryInfo
+ __OBJC_$_PROP_LIST_DAExtensionCapability
+ __OBJC_$_PROP_LIST_DAExtensionEventLifecycle
+ __OBJC_$_PROP_LIST_DAIncomingMessage
+ __OBJC_$_PROP_LIST_DAOutgoingMessage
+ __OBJC_CATEGORY_PROTOCOLS_$__EXCapabilityEndpoint_$_CUXPCCodable
+ __OBJC_CLASS_PROTOCOLS_$_DAAppAsset
+ __OBJC_CLASS_PROTOCOLS_$_DADeviceRegistry
+ __OBJC_CLASS_PROTOCOLS_$_DADeviceRegistryInfo
+ __OBJC_CLASS_PROTOCOLS_$_DAExtensionCapability
+ __OBJC_CLASS_PROTOCOLS_$_DAIncomingMessage
+ __OBJC_CLASS_PROTOCOLS_$_DAOutgoingMessage
+ __OBJC_CLASS_RO_$_DAAppAsset
+ __OBJC_CLASS_RO_$_DAAppAssetManager
+ __OBJC_CLASS_RO_$_DADeviceRegistry
+ __OBJC_CLASS_RO_$_DADeviceRegistryInfo
+ __OBJC_CLASS_RO_$_DAExtensionCapability
+ __OBJC_CLASS_RO_$_DAIncomingMessage
+ __OBJC_CLASS_RO_$_DAOutgoingMessage
+ __OBJC_METACLASS_RO_$_DAAppAsset
+ __OBJC_METACLASS_RO_$_DAAppAssetManager
+ __OBJC_METACLASS_RO_$_DADeviceRegistry
+ __OBJC_METACLASS_RO_$_DADeviceRegistryInfo
+ __OBJC_METACLASS_RO_$_DAExtensionCapability
+ __OBJC_METACLASS_RO_$_DAIncomingMessage
+ __OBJC_METACLASS_RO_$_DAOutgoingMessage
+ ___27-[DAExtension reportEvent:]_block_invoke.cold.1
+ ___27-[DAExtension reportEvent:]_block_invoke.cold.2
+ ___27-[DAExtension reportEvent:]_block_invoke.cold.3
+ ___28-[DAExtensionSession launch]_block_invoke
+ ___28-[DAExtensionSession resume]_block_invoke
+ ___29-[DAExtensionSession suspend]_block_invoke
+ ___30-[DAExtension _activateDirect]_block_invoke.cold.1
+ ___31-[DAExtension _startExtension:]_block_invoke
+ ___31-[DAExtension _startExtension:]_block_invoke.cold.1
+ ___31-[DAExtensionSession terminate]_block_invoke
+ ___32-[DAExtension _updateWithError:]_block_invoke
+ ___32-[DAExtension _updateWithError:]_block_invoke.cold.1
+ ___33-[DAAppAssetManager _cacheAsset:]_block_invoke
+ ___33-[DAAppAssetManager _pruneCache:]_block_invoke
+ ___33-[DAExtensionCapability activate]_block_invoke
+ ___34+[DAAppAssetManager sharedManager]_block_invoke
+ ___34-[DAAppAssetManager clearAllCache]_block_invoke
+ ___34-[DAAppAssetManager clearAllCache]_block_invoke.cold.1
+ ___34-[DAAppAssetManager clearAllCache]_block_invoke.cold.2
+ ___34-[DAExtension _activateExtension:]_block_invoke
+ ___34-[DAExtension _activateExtension:]_block_invoke_2
+ ___34-[DAExtension _activateExtension:]_block_invoke_3
+ ___34-[DAExtension _activateExtension:]_block_invoke_4
+ ___35-[DAExtensionCapability invalidate]_block_invoke
+ ___37-[DAExtensionCapability reportEvent:]_block_invoke
+ ___40-[DAExtensionCapability _activateDirect]_block_invoke
+ ___40-[DAExtensionCapability _activateDirect]_block_invoke_2
+ ___40-[DAExtensionCapability _activateDirect]_block_invoke_2.cold.1
+ ___40-[DAExtensionCapability _activateDirect]_block_invoke_3
+ ___40-[DAExtensionCapability _activateDirect]_block_invoke_3.cold.1
+ ___40-[DAExtensionCapability _activateDirect]_block_invoke_3.cold.2
+ ___40-[DAExtensionCapability _activateDirect]_block_invoke_3.cold.3
+ ___40-[DAExtensionCapability _activateDirect]_block_invoke_3.cold.4
+ ___40-[DAExtensionCapability _activateDirect]_block_invoke_4
+ ___40-[DAExtensionCapability _activateDirect]_block_invoke_5
+ ___42-[DAExtension _capabilitiesEnsureStarted:]_block_invoke
+ ___42-[DAExtension _capabilitiesEnsureStarted:]_block_invoke_2
+ ___42-[DAExtension _capabilitiesEnsureStarted:]_block_invoke_3
+ ___42-[DAExtension _capabilitiesEnsureStarted:]_block_invoke_3.cold.1
+ ___42-[DAExtension _sandboxExtensionIssueMach:]_block_invoke
+ ___42-[DAExtension _sandboxExtensionIssueMach:]_block_invoke.cold.1
+ ___42-[DAExtension _sandboxExtensionIssueMach:]_block_invoke_2
+ ___42-[DAExtension _sandboxExtensionIssueMach:]_block_invoke_2.cold.1
+ ___42-[DAExtension _sandboxExtensionIssueMach:]_block_invoke_3
+ ___42-[DAExtension _sandboxExtensionIssueMach:]_block_invoke_3.cold.1
+ ___42-[DAExtensionCapability _startCapability:]_block_invoke
+ ___42-[DAExtensionCapability _startCapability:]_block_invoke.cold.1
+ ___42-[DASession diagnosticControl:completion:]_block_invoke
+ ___42-[DASession diagnosticControl:completion:]_block_invoke.cold.1
+ ___42-[DASession diagnosticControl:completion:]_block_invoke_2
+ ___42-[DASession diagnosticControl:completion:]_block_invoke_2.cold.1
+ ___44+[DASession fetchAppAssetForBundleID:error:]_block_invoke
+ ___44-[DAAppAssetManager removeCacheForBundleID:]_block_invoke
+ ___44-[DAExtension _handleCapabilityInterrupted:]_block_invoke
+ ___44-[DAExtension _handleCapabilityInterrupted:]_block_invoke.cold.1
+ ___44-[DAExtension _handleCapabilityInterrupted:]_block_invoke_2
+ ___44-[DAExtension _handleCapabilityInvalidated:]_block_invoke
+ ___44-[DAExtension _handleCapabilityInvalidated:]_block_invoke.cold.1
+ ___46-[DAExtensionCapability invalidateWithReason:]_block_invoke
+ ___46-[DAExtensionSession updateWithConfiguration:]_block_invoke
+ ___47-[DAExtensionSession _updateIfNeededWithBlock:]_block_invoke
+ ___48+[DASession processAllowedWithAuditToken:error:]_block_invoke
+ ___48-[DAExtensionCapability reportEventToExtension:]_block_invoke
+ ___48-[DAExtensionCapability reportEventToExtension:]_block_invoke_2
+ ___48-[DAExtensionCapability reportEventToExtension:]_block_invoke_2.cold.1
+ ___49+[DASession testProxFlow:manufacturerID:modelID:]_block_invoke
+ ___52-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke
+ ___52-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke.cold.1
+ ___52-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke_2
+ ___52-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke_2.cold.1
+ ___52-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke_3
+ ___52-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke_3.cold.1
+ ___55-[DAAppAssetManager getAppAssetForBundleID:completion:]_block_invoke
+ ___55-[DAAppAssetManager getAppAssetForBundleID:completion:]_block_invoke.cold.1
+ ___55-[DAAppAssetManager getAppAssetForBundleID:completion:]_block_invoke.cold.2
+ ___55-[DAAppAssetManager getAppAssetForBundleID:completion:]_block_invoke_2
+ ___55-[DAAppAssetManager getAppAssetForBundleID:completion:]_block_invoke_3
+ ___55-[DAAppAssetManager getAppAssetForBundleID:completion:]_block_invoke_4
+ ___59-[_EXCapabilityEndpoint(CUXPCCodable) encodeWithXPCObject:]_block_invoke
+ ___62+[DAExtensionSession bluetoothRestorationIDForBundleID:error:]_block_invoke
+ ___62+[DAExtensionSession launchExtensionWithBundle:extensionType:]_block_invoke
+ ___62+[DAExtensionSession resumeExtensionWithBundle:extensionType:]_block_invoke
+ ___63+[DAExtensionSession suspendExtensionWithBundle:extensionType:]_block_invoke
+ ___63-[_EXCapabilityEndpoint(CUXPCCodable) initWithXPCObject:error:]_block_invoke
+ ___63-[_EXCapabilityEndpoint(CUXPCCodable) initWithXPCObject:error:]_block_invoke.cold.1
+ ___64+[DASession preflightMigrationWithConfigurations:session:error:]_block_invoke
+ ___68-[DASession preflightMigrationWithConfigurations:completionHandler:]_block_invoke
+ ___68-[DASession preflightMigrationWithConfigurations:completionHandler:]_block_invoke.cold.1
+ ___68-[DASession preflightMigrationWithConfigurations:completionHandler:]_block_invoke_2
+ ___68-[DASession preflightMigrationWithConfigurations:completionHandler:]_block_invoke_2.cold.1
+ ___68-[DASession preflightMigrationWithConfigurations:completionHandler:]_block_invoke_2.cold.2
+ ___71-[DAExtensionSession getEndpointsForCapabilityFlags:completionHandler:]_block_invoke
+ ___71-[DAExtensionSession getEndpointsForCapabilityFlags:completionHandler:]_block_invoke_2
+ ___71-[DAExtensionSession getEndpointsForCapabilityFlags:completionHandler:]_block_invoke_3
+ ___71-[DAExtensionSession getEndpointsForCapabilityFlags:completionHandler:]_block_invoke_4
+ ___88+[DAExtensionSession suspendExtensionWithBundle:extensionType:extensionCapabilityFlags:]_block_invoke
+ ___NSDictionary0__struct
+ ___block_descriptor_32_e35_q24?0"DAAppAsset"8"DAAppAsset"16l
+ ___block_descriptor_40_e8_32s_e26_v16?0"DAEventExtension"8ls32l8
+ ___block_descriptor_40_e8_32s_e37_B24?0r*8"NSObject<OS_xpc_object>"16ls32l8
+ ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e46_v24?0"_EXCapabilityHostSession"8"NSError"16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e5_B8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32bs40r48r_e33_v16?0"NSObject<OS_xpc_object>"8lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32r40r_e48_v32?0"NSNumber"8"DAExtensionCapability"16^B24lr32l8r40l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.146
+ ___block_literal_global.162
+ ___block_literal_global.166
+ ___block_literal_global.169
+ ___block_literal_global.182
+ ___block_literal_global.189
+ ___block_literal_global.198
+ ___block_literal_global.214
+ ___block_literal_global.215
+ ___block_literal_global.216
+ ___block_literal_global.220
+ ___block_literal_global.225
+ ___block_literal_global.241
+ ___block_literal_global.252
+ ___block_literal_global.259
+ __dispatch_queue_attr_concurrent
+ _container_system_group_path_for_identifier
+ _dispatch_after
+ _dispatch_barrier_async
+ _dispatch_barrier_sync
+ _dispatch_time
+ _gLogCategory_DAAppAssetManager
+ _gLogCategory_DAExtensionCapability
+ _kTCCServiceAccessoryAutomaticAudioSwitching
+ _kTCCServiceAccessoryLiveActivities
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_msgSend$URLByAppendingPathComponent:isDirectory:
+ _objc_msgSend$_cacheAsset:
+ _objc_msgSend$_capabilitiesEnsureStarted:
+ _objc_msgSend$_createCacheFileURL
+ _objc_msgSend$_getPartialIPsCompleted:completionHandler:
+ _objc_msgSend$_handleCapabilityInterrupted:
+ _objc_msgSend$_handleCapabilityInvalidated:
+ _objc_msgSend$_invalidateCapabilities
+ _objc_msgSend$_loadCache
+ _objc_msgSend$_loadCachedAssetForBundleID:
+ _objc_msgSend$_pruneCache:
+ _objc_msgSend$_sandboxExtensionIssueMach:
+ _objc_msgSend$_startCapability:
+ _objc_msgSend$_startExtension:
+ _objc_msgSend$_update
+ _objc_msgSend$_updateIfNeededWithBlock:
+ _objc_msgSend$_updateWithError:
+ _objc_msgSend$_writeCache:
+ _objc_msgSend$attributes
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$beginEncoding
+ _objc_msgSend$beginReadingFromXPCObject:
+ _objc_msgSend$bluetoothRestorationIdentifier
+ _objc_msgSend$cachedDate
+ _objc_msgSend$capabilityEndpoint
+ _objc_msgSend$capabilityFlag
+ _objc_msgSend$capabilityFlags
+ _objc_msgSend$capabilityID
+ _objc_msgSend$companionAppBundleID
+ _objc_msgSend$companionAppIsOptional
+ _objc_msgSend$compare:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$containsString:
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$date
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$domain
+ _objc_msgSend$extensionCapability
+ _objc_msgSend$fetchAppAssetForBundleID:error:
+ _objc_msgSend$fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$finishEncoding
+ _objc_msgSend$friendlyName
+ _objc_msgSend$image2xData
+ _objc_msgSend$image3xData
+ _objc_msgSend$initInternal
+ _objc_msgSend$initWithBundleID:adamID:appName:developerName:iconData:
+ _objc_msgSend$initWithCapabilityID:sessionUUID:
+ _objc_msgSend$initWithExtensionIdentity:sessionIdentity:invalidationHandler:
+ _objc_msgSend$initWithIdentity:device:capabilityID:
+ _objc_msgSend$initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoData:companionAppBundleID:companionAppIsOptional:
+ _objc_msgSend$initWithManufacturerID:modelID:info:
+ _objc_msgSend$initWithMessageID:encryptedPayloadData:
+ _objc_msgSend$initWithMessageID:payloadData:
+ _objc_msgSend$invalidateDone
+ _objc_msgSend$isExpired
+ _objc_msgSend$lastObject
+ _objc_msgSend$mainBundle
+ _objc_msgSend$manufacturerID
+ _objc_msgSend$modelID
+ _objc_msgSend$networkEndpoint
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$path
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$sessionWithConfiguration:completion:
+ _objc_msgSend$setBluetoothRestorationIdentifier:
+ _objc_msgSend$setCapabilityFlag:
+ _objc_msgSend$setCompanionAppBundleID:
+ _objc_msgSend$setCompanionAppIsOptional:
+ _objc_msgSend$setEventHandler:
+ _objc_msgSend$setExtensionCapability:
+ _objc_msgSend$setFriendlyName:
+ _objc_msgSend$setImage2xData:
+ _objc_msgSend$setImage3xData:
+ _objc_msgSend$setInvalidateDone:
+ _objc_msgSend$setPid:
+ _objc_msgSend$setSessionID:
+ _objc_msgSend$setVideoData:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$startDiscoveryWithSession:
+ _objc_msgSend$stopDiscoveryWithSession:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$txtRecordData
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSend$updateWithDAExtensionSessionConfiguration:
+ _objc_msgSend$videoData
+ _objc_msgSend$writeToURL:options:error:
+ _processAllowedWithAuditToken:error:.sAllowedExtensionPoints
+ _processAllowedWithAuditToken:error:.sOnce
+ _sharedManager.onceToken
+ _sharedManager.sSharedManager
+ _strlen
+ _xpc_connection_send_message
+ _xpc_dictionary_apply
- -[DAExtension _invalidated].cold.2
- -[DAExtension _invalidated].cold.3
- -[DAExtension dispatchQueue]
- -[DAExtension reportEvent:].cold.1
- -[DAExtension setDispatchQueue:]
- -[DAExtensionEventData capabilityFlags]
- -[DAExtensionEventData initWithDevice:data:capabilityFlag:]
- GCC_except_table14
- GCC_except_table24
- GCC_except_table41
- GCC_except_table5
- GCC_except_table50
- GCC_except_table71
- _NSAppendPrintF_safe
- _OBJC_IVAR_$_DAExtensionEventData._capabilityFlags
- ___30-[DAExtension _activateDirect]_block_invoke_2
- ___30-[DAExtension _activateDirect]_block_invoke_3
- ___30-[DAExtension _activateDirect]_block_invoke_4
- ___30-[DAExtension _activateDirect]_block_invoke_5
- ___30-[DAExtension _activateDirect]_block_invoke_5.cold.1
- ___30-[DAExtension _activateDirect]_block_invoke_6
- ___30-[DAExtension _activateDirect]_block_invoke_6.cold.1
- ___30-[DAExtension _activateDirect]_block_invoke_7
- ___30-[DAExtension _activateDirect]_block_invoke_7.cold.1
- ___38-[DAExtension reportEventToExtension:]_block_invoke.cold.1
- ___38-[DAExtension reportEventToExtension:]_block_invoke.cold.2
- ___block_literal_global.103
- ___block_literal_global.129
- ___block_literal_global.140
- ___block_literal_global.74
- ___block_literal_global.78
- ___block_literal_global.81
- ___block_literal_global.94
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
CStrings:
+ " ]"
+ "### Activate %@ failed: %@, %@"
+ "### Cannot report nil capability '%@' event to extension: %@"
+ "### DAAppAssetManager failed to create cache file URL!"
+ "### Extension XPC failed to consume Logging token: %@, %@"
+ "### Extension XPC failed to consume Wi-Fi Network Sharing token: %@, %@"
+ "### Failed to archive cache: %@"
+ "### Failed to clear cache: %@"
+ "### Failed to create sandbox token: Bluetooth"
+ "### Failed to create sandbox token: Logging"
+ "### Failed to create sandbox token: Wi-Fi Network Sharing"
+ "### Failed to fetch app asset for %@: %@"
+ "### Failed to get capability host session: %@"
+ "### Failed to load cache: %@"
+ "### Failed to unarchive cache: %@"
+ "### Failed to write cache: %@"
+ "### GetEndpointsForCapabilityFlags: %@"
+ "### Received nil XPC event from '%@': %@"
+ "### SandboxExtensionIssueMach failed with nil XPC connection"
+ "### SessionWithConfiguration failed for %@: %@"
+ "### StartExtension failed with nil XPC connection"
+ "### Update: %@"
+ "### _EXCapabilityEndpoint initWithXPCObject: %@"
+ "%@...%@"
+ "'%@'"
+ "(none)"
+ "+[DASession preflightMigrationWithConfigurations:session:error:]"
+ ", "
+ ", Capabilities [ "
+ "-[DAAppAssetManager _createCacheFileURL]"
+ "-[DAAppAssetManager _loadCache]"
+ "-[DAAppAssetManager _writeCache:]"
+ "-[DAAppAssetManager clearAllCache]"
+ "-[DAAppAssetManager clearAllCache]_block_invoke"
+ "-[DAAppAssetManager getAppAssetForBundleID:completion:]"
+ "-[DAAppAssetManager getAppAssetForBundleID:completion:]_block_invoke"
+ "-[DAAppAssetManager initInternal]"
+ "-[DAAppAssetManager removeCacheForBundleID:]"
+ "-[DAExtension _capabilitiesEnsureStarted:]"
+ "-[DAExtension _capabilitiesEnsureStarted:]_block_invoke_3"
+ "-[DAExtension _handleCapabilityInterrupted:]_block_invoke"
+ "-[DAExtension _handleCapabilityInvalidated:]_block_invoke"
+ "-[DAExtension _invalidated:]"
+ "-[DAExtension _sandboxExtensionIssueMach:]"
+ "-[DAExtension _sandboxExtensionIssueMach:]_block_invoke"
+ "-[DAExtension _sandboxExtensionIssueMach:]_block_invoke_2"
+ "-[DAExtension _sandboxExtensionIssueMach:]_block_invoke_3"
+ "-[DAExtension _startExtension:]"
+ "-[DAExtension _startExtension:]_block_invoke"
+ "-[DAExtension _updateWithError:]"
+ "-[DAExtension _updateWithError:]_block_invoke"
+ "-[DAExtension reportEvent:]_block_invoke"
+ "-[DAExtension setEnrolledFlags:]"
+ "-[DAExtensionCapability _activateDirect]"
+ "-[DAExtensionCapability _activateDirect]_block_invoke"
+ "-[DAExtensionCapability _activateDirect]_block_invoke_2"
+ "-[DAExtensionCapability _activateDirect]_block_invoke_3"
+ "-[DAExtensionCapability _activated]"
+ "-[DAExtensionCapability _interrupted]"
+ "-[DAExtensionCapability _invalidate]"
+ "-[DAExtensionCapability _invalidated]"
+ "-[DAExtensionCapability _sandboxExtensionIssueMach:]"
+ "-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke"
+ "-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke_2"
+ "-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke_3"
+ "-[DAExtensionCapability _startCapability:]"
+ "-[DAExtensionCapability _startCapability:]_block_invoke"
+ "-[DAExtensionCapability activate]_block_invoke"
+ "-[DAExtensionCapability reportEvent:]"
+ "-[DAExtensionCapability reportEventToExtension:]"
+ "-[DAExtensionCapability reportEventToExtension:]_block_invoke_2"
+ "-[DAExtensionSession _update]"
+ "-[DAExtensionSession getEndpointsForCapabilityFlags:completionHandler:]_block_invoke_2"
+ "-[DASession preflightMigrationWithConfigurations:completionHandler:]_block_invoke"
+ "-[DASession preflightMigrationWithConfigurations:completionHandler:]_block_invoke_2"
+ "-[_EXCapabilityEndpoint(CUXPCCodable) initWithXPCObject:error:]_block_invoke"
+ "."
+ "<%@: %@, messageID=%@, destinationDeviceID=%@, featureID=%@>"
+ "<%@: %@, messageID=%@, sourceDeviceID=%@, featureID=%@>"
+ "<%@: %p; friendlyName=%@; image2x=%@; image3x=%@; video=%@; companionAppBundleID=%@; companionAppIsOptional=%@>"
+ "<%@: %p; manufacturerID=%@; modelID=%@; friendlyName=%@; image2x=%@; image3x=%@; video=%@; companionAppBundleID=%@; companionAppIsOptional=%@>"
+ "<DAAppAsset bundleID=%@ adamID=%@ appName=%@ developerName=%@  iconSize=%lu cached=%@>"
+ "@\"DADeviceRegistry\""
+ "@\"DAExtensionCapability\""
+ "@\"NSDate\""
+ "@\"_EXCapabilityEndpoint\""
+ "@\"_EXCapabilityHostSession\""
+ "@24@0:8Q16"
+ "@48@0:8@16@24@32^@40"
+ "@56@0:8@16@24@32@40@48"
+ "@76@0:8@16@24@32@40@48@56@64B72"
+ "AEnK %@ (%lu bytes)"
+ "APubK %@ (%lu bytes)"
+ "Asset"
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "B8@?0"
+ "BluetoothID '%@'"
+ "Cache hit for bundle ID: %@"
+ "Cache miss/expired for bundle ID: %@, fetching from remote"
+ "Caches"
+ "CapFl %@"
+ "Capability %@"
+ "Capability host configuration invalidated with identity: %@"
+ "Capability host session configuration: %@"
+ "Capability host session for %@: %@"
+ "Capability session identity: %@"
+ "CapibilityID '%@' : SessionID '%@'"
+ "Clearing all cache from %@"
+ "DAAppAsset"
+ "DAAppAssetCache.plist"
+ "DAAppAssetManager"
+ "DAAppAssetManager initialized with cache at: %@"
+ "DADeviceRegistry"
+ "DADeviceRegistryInfo"
+ "DAExtensionCapability"
+ "DAIncomingMessage"
+ "DAOutgoingMessage"
+ "DASession-FetchAppAsset"
+ "DASession-PreflightMigration"
+ "DASession-TestProxFlow"
+ "DASession-getBTRestoreID"
+ "DASession-launchExtension"
+ "DASession-resumeExtension"
+ "DASession-suspendExtension"
+ "DataProvider"
+ "Decrypted data for SessionID '%s': %s (%ld bytes) -> %s (%ld bytes) with %@"
+ "Destination %@"
+ "DeviceAccess"
+ "DgCt"
+ "EnFl %@"
+ "EnK %@ (%lu bytes)"
+ "Encrypted data for SessionID '%s': %s (%ld bytes) -> %s (%ld bytes) with %@"
+ "Endpoint %@"
+ "Enrolled capabilities changed: %@ -> %@: %@"
+ "EventType %@"
+ "ExBtRID"
+ "ExCp %@"
+ "ExFl %@"
+ "ExGE"
+ "ExLa"
+ "ExRes"
+ "ExSusp"
+ "ExTer"
+ "Found extension capabilities for %@: %@"
+ "Getting app asset for bundle ID: %@"
+ "ID '%@'"
+ "Invalidated %@"
+ "InvalidationHandler for capability %@"
+ "Issuing sandbox extension mach: Bluetooth"
+ "Issuing sandbox extension mach: Logging"
+ "Issuing sandbox extension mach: Wi-Fi Network Sharing"
+ "NO"
+ "No adamID"
+ "No appName"
+ "No developerName"
+ "No iconData"
+ "PreflightMigration completed: canMigrateSilently = %s"
+ "PreflightMigration failed: %@"
+ "PreflightMigration start with %lu configurations"
+ "PreflightMigration sync completed: canMigrateSilently = %s"
+ "PreflightMigration sync start with %lu configurations"
+ "PrfM"
+ "PrivK %@ (%lu bytes)"
+ "ProximitySetup"
+ "PubK %@ (%lu bytes)"
+ "Push %@"
+ "Removed %@ capability (interrupted): %lu, %@"
+ "Removed %@ capability (invalidated): %lu, %@"
+ "Removing cache for bundle ID: %@"
+ "ReportEventToExtension %@"
+ "Service %@"
+ "SessionID '%@'"
+ "Starting extension: %@"
+ "Successfully cleared cache"
+ "T@\"DAAppAssetManager\",R"
+ "T@\"DADeviceRegistry\",&,N,V_deviceRegistry"
+ "T@\"DAExtensionCapability\",&,N,V_extensionCapability"
+ "T@\"NSData\",&,N,V_encryptedPayloadData"
+ "T@\"NSData\",&,N,V_payloadData"
+ "T@\"NSData\",C,N,V_devicePushToken"
+ "T@\"NSData\",C,N,V_image2xData"
+ "T@\"NSData\",C,N,V_image3xData"
+ "T@\"NSData\",C,N,V_videoData"
+ "T@\"NSData\",R,C,N,V_iconData"
+ "T@\"NSData\",R,C,N,V_image2xData"
+ "T@\"NSData\",R,C,N,V_image3xData"
+ "T@\"NSData\",R,C,N,V_videoData"
+ "T@\"NSDate\",R,C,N,V_cachedDate"
+ "T@\"NSString\",C,N,V_bluetoothRestorationIdentifier"
+ "T@\"NSString\",C,N,V_cbRestorationID"
+ "T@\"NSString\",C,N,V_companionAppBundleID"
+ "T@\"NSString\",C,N,V_destinationDeviceID"
+ "T@\"NSString\",C,N,V_devicePushTopic"
+ "T@\"NSString\",C,N,V_featureID"
+ "T@\"NSString\",C,N,V_friendlyName"
+ "T@\"NSString\",C,N,V_messageID"
+ "T@\"NSString\",C,N,V_payloadFilePath"
+ "T@\"NSString\",C,N,V_queueOneIdentifier"
+ "T@\"NSString\",C,N,V_sessionID"
+ "T@\"NSString\",C,N,V_sourceDeviceID"
+ "T@\"NSString\",R,C,N,V_adamID"
+ "T@\"NSString\",R,C,N,V_appName"
+ "T@\"NSString\",R,C,N,V_bundleID"
+ "T@\"NSString\",R,C,N,V_companionAppBundleID"
+ "T@\"NSString\",R,C,N,V_developerName"
+ "T@\"NSString\",R,C,N,V_friendlyName"
+ "T@\"NSString\",R,C,N,V_manufacturerID"
+ "T@\"NSString\",R,C,N,V_modelID"
+ "T@\"NSString\",R,N,V_capabilityID"
+ "T@\"NSString\",R,N,V_identifier"
+ "T@\"_EXCapabilityEndpoint\",&,N,V_endpoint"
+ "TB,N,V_companionAppIsOptional"
+ "TB,R,N,V_companionAppIsOptional"
+ "TB,V_invalidateDone"
+ "TQ,N,V_capabilityFlag"
+ "TQ,N,V_capabilityFlags"
+ "TQ,N,V_enrolledFlags"
+ "TQ,R,N,V_capabilityFlag"
+ "TQ,R,N,V_newState"
+ "TQ,R,N,V_previousState"
+ "Td,N,V_expiresAt"
+ "Td,N,V_lastAttemptedAt"
+ "Td,N,V_originatedAt"
+ "Td,N,V_receivedAt"
+ "Token %@"
+ "Tq,N,V_payloadVersion"
+ "Tq,N,V_retryCount"
+ "Tq,N,V_transportPriority"
+ "Tq,R,N"
+ "TransportLocal"
+ "TstPF"
+ "Type %@"
+ "URLByAppendingPathComponent:isDirectory:"
+ "Update: %@"
+ "Update: unchanged"
+ "Updated PID: %@"
+ "Using container path %s"
+ "Value %@ (%ld bytes)"
+ "_EXExtensionCapabilities"
+ "_adamID"
+ "_appName"
+ "_bluetoothRestorationIdentifier"
+ "_cacheAsset:"
+ "_cacheFileURL"
+ "_cachedDate"
+ "_capabilitesMap"
+ "_capabilitiesEnsureStarted:"
+ "_capabilityFlag"
+ "_capabilityID"
+ "_cbRestorationID"
+ "_changesPending"
+ "_companionAppBundleID"
+ "_companionAppIsOptional"
+ "_createCacheFileURL"
+ "_destinationDeviceID"
+ "_developerName"
+ "_devicePushToken"
+ "_devicePushTopic"
+ "_deviceRegistry"
+ "_encryptedPayloadData"
+ "_enrolledFlags"
+ "_expiresAt"
+ "_extensionCapability"
+ "_extensionCapabilityMap"
+ "_extensionFlags"
+ "_featureID"
+ "_friendlyName"
+ "_handleCapabilityInterrupted:"
+ "_handleCapabilityInvalidated:"
+ "_iconData"
+ "_image2xData"
+ "_image3xData"
+ "_invalidateCapabilities"
+ "_invalidated:"
+ "_lastAttemptedAt"
+ "_loadCache"
+ "_loadCachedAssetForBundleID:"
+ "_manufacturerID"
+ "_messageID"
+ "_modelID"
+ "_newState"
+ "_originatedAt"
+ "_payloadData"
+ "_payloadFilePath"
+ "_payloadVersion"
+ "_previousState"
+ "_pruneCache:"
+ "_queue"
+ "_queueOneIdentifier"
+ "_receivedAt"
+ "_retryCount"
+ "_sandboxExtensionIssueMach:"
+ "_sessionID"
+ "_sessionUUID"
+ "_sourceDeviceID"
+ "_startCapability:"
+ "_startExtension:"
+ "_transportPriority"
+ "_update"
+ "_updateIfNeededWithBlock:"
+ "_updateWithError:"
+ "_videoData"
+ "_writeCache:"
+ "adam"
+ "adamID"
+ "apDv"
+ "apNm"
+ "appName"
+ "attributes"
+ "bI"
+ "base64EncodedStringWithOptions:"
+ "beginEncoding"
+ "beginReadingFromXPCObject:"
+ "bluetoothRestorationIDForBundleID:error:"
+ "bluetoothRestorationIdentifier"
+ "btRId"
+ "btRestoreID '%@'"
+ "cI"
+ "cachedDate"
+ "capabilitiesForFlags:"
+ "capabilityEndpoint"
+ "capabilityFlag"
+ "capabilityID"
+ "capabilityWithSessionID:"
+ "cbRestorationID"
+ "clearAllCache"
+ "com.apple.DeviceAccess.DAAppAssetManager"
+ "com.apple.accessory-data-provider"
+ "com.apple.accessory-transport-security"
+ "com.apple.appintents-extension"
+ "com.apple.developer.accessory-data-provider"
+ "com.apple.developer.accessory-transport-security"
+ "com.apple.ui-services"
+ "com.apple.widgetkit-extension"
+ "companionAppBundleID"
+ "companionAppIsOptional"
+ "compare:"
+ "componentsSeparatedByString:"
+ "containsObject:"
+ "containsString:"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "dI"
+ "dataWithContentsOfURL:options:error:"
+ "date"
+ "decodeObjectOfClass:forKey:"
+ "decryptData:withCryptoInfo:sessionID:error:"
+ "defaultManager"
+ "destinationDeviceID"
+ "developerName"
+ "devicePushToken"
+ "devicePushTopic"
+ "deviceRegistry"
+ "diagnosticControl:completion:"
+ "dictionaryWithCapacity:"
+ "drCAB"
+ "drCAO"
+ "drFN"
+ "drI2x"
+ "drI3x"
+ "drMI"
+ "drMoI"
+ "drVid"
+ "dvRg"
+ "eA"
+ "eD"
+ "encryptData:withCryptoInfo:sessionID:error:"
+ "encryptedPayloadData"
+ "enrolledFlags"
+ "exCp"
+ "exCpE"
+ "exCpEs"
+ "exCpID"
+ "exSID"
+ "exSU"
+ "expiresAt"
+ "extension is missing attributes"
+ "extension is missing capabilities"
+ "extensionCapability"
+ "fI"
+ "failed to decode endpoint"
+ "featureID"
+ "fetchAppAssetForBundleID:error:"
+ "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
+ "fileURLWithPath:"
+ "finishEncoding"
+ "friendlyName"
+ "getAppAssetForBundleID:completion:"
+ "getEndpointsForCapabilityFlags:completionHandler:"
+ "icon"
+ "iconData"
+ "image2xData"
+ "image3xData"
+ "initInternal"
+ "initWithBluetoothRestorationID:"
+ "initWithBundleID:adamID:appName:developerName:iconData:"
+ "initWithCapabilityID:sessionUUID:"
+ "initWithDevice:data:"
+ "initWithDevice:data:sessionID:"
+ "initWithExtensionIdentity:sessionIdentity:invalidationHandler:"
+ "initWithIdentity:device:capabilityID:"
+ "initWithManufacturerID:modelID:"
+ "initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoData:companionAppBundleID:companionAppIsOptional:"
+ "initWithManufacturerID:modelID:info:"
+ "initWithMessageID:encryptedPayloadData:"
+ "initWithMessageID:payloadData:"
+ "initWithMessageID:payloadFilePath:"
+ "invalidateDone"
+ "isExpired"
+ "kTCCServiceAccessoryAutomaticAudioSwitching"
+ "kTCCServiceAccessoryLiveActivities"
+ "kTCCServiceAccessoryNotifications"
+ "kTCCServiceAccessoryWiFiNetworkSharing"
+ "lA"
+ "lastAttemptedAt"
+ "lastObject"
+ "launch"
+ "launchExtensionWithBundle:extensionType:"
+ "load"
+ "load cache from %@"
+ "mI"
+ "manufacturerID"
+ "messageID"
+ "mgSl"
+ "missing completion handler"
+ "modelID"
+ "newState"
+ "oA"
+ "objectAtIndexedSubscript:"
+ "originatedAt"
+ "pD"
+ "pF"
+ "pTc"
+ "pTn"
+ "pV"
+ "path"
+ "payloadData"
+ "payloadFilePath"
+ "payloadSize"
+ "payloadVersion"
+ "pid '%d'"
+ "preflightMigrationWithConfigurations:completionHandler:"
+ "preflightMigrationWithConfigurations:session:error:"
+ "previousState"
+ "q24@?0@\"DAAppAsset\"8@\"DAAppAsset\"16"
+ "qI"
+ "queueOneIdentifier"
+ "rA"
+ "rC"
+ "receivedAt"
+ "removeCacheForBundleID:"
+ "removeItemAtURL:error:"
+ "resumeExtensionWithBundle:extensionType:"
+ "retryCount"
+ "sI"
+ "sessionID"
+ "sessionWithConfiguration:completion:"
+ "setBluetoothRestorationIdentifier:"
+ "setCapabilityFlag:"
+ "setCapabilityFlags:"
+ "setCbRestorationID:"
+ "setCompanionAppBundleID:"
+ "setCompanionAppIsOptional:"
+ "setDestinationDeviceID:"
+ "setDevicePushToken:"
+ "setDevicePushTopic:"
+ "setDeviceRegistry:"
+ "setEncryptedPayloadData:"
+ "setEnrolledFlags:"
+ "setExpiresAt:"
+ "setExtensionCapability:"
+ "setFeatureID:"
+ "setFriendlyName:"
+ "setImage2xData:"
+ "setImage3xData:"
+ "setInvalidateDone:"
+ "setLastAttemptedAt:"
+ "setMessageID:"
+ "setOriginatedAt:"
+ "setPayloadData:"
+ "setPayloadFilePath:"
+ "setPayloadVersion:"
+ "setQueueOneIdentifier:"
+ "setReceivedAt:"
+ "setRetryCount:"
+ "setSessionID:"
+ "setSourceDeviceID:"
+ "setTransportPriority:"
+ "setVideoData:"
+ "setWithObjects:"
+ "sharedManager"
+ "sortedArrayUsingComparator:"
+ "sourceDeviceID"
+ "substringFromIndex:"
+ "substringToIndex:"
+ "suspend"
+ "suspendExtensionWithBundle:extensionType:"
+ "suspendExtensionWithBundle:extensionType:extensionCapabilityFlags:"
+ "systemgroup.com.apple.accessorysetupkit"
+ "tP"
+ "terminate"
+ "testProxFlow:manufacturerID:modelID:"
+ "timeIntervalSinceDate:"
+ "transportPriority"
+ "unsignedLongValue"
+ "updateWithConfiguration:"
+ "updateWithDAExtensionSession:"
+ "updateWithDAExtensionSessionConfiguration:"
+ "v16@?0@\"DAEventExtension\"8"
+ "v24@0:8^@16"
+ "v24@?0@\"_EXCapabilityHostSession\"8@\"NSError\"16"
+ "v32@0:8@16q24"
+ "v32@?0@\"NSNumber\"8@\"DAExtensionCapability\"16^B24"
+ "v40@0:8@16q24Q32"
+ "videoData"
+ "writeToURL:options:error:"
- " %@"
- " '%@'"
- " EventType %@"
- " ID %@,"
- " Type %@,"
- "### Extension XPC failed to consume WiFi token: %@, %@"
- "### ReportEventToExtension failed with nil xpc connection"
- ", AEnK %@ (%lu bytes)"
- ", APubK %@ (%lu bytes)"
- ", BluetoothID '%@'"
- ", CF %@"
- ", Destination %@"
- ", EnK %@ (%lu bytes)"
- ", ID '%@'"
- ", PrivK %@ (%lu bytes)"
- ", PubK %@ (%lu bytes)"
- ", Service %@"
- "-[DAExtension _activateDirect]_block_invoke_5"
- "-[DAExtension _activateDirect]_block_invoke_6"
- "-[DAExtension _activateDirect]_block_invoke_7"
- "-[DAExtension reportEvent:]"
- ": %@ (%ld bytes)"
- "@40@0:8@16@24Q32"
- "@48@0:8@16@24Q32^@40"
- "DecryptedData for %s: %s (%ld bytes) -> %s (%ld bytes) with %@"
- "EncryptedData for %s: %s (%ld bytes) -> %s (%ld bytes) with %@"
- "Local"
- "TQ,R,N,V_capabilityFlags"
- "decryptData:withCryptoInfo:capability:error:"
- "encryptData:withCryptoInfo:capability:error:"
- "initWithDevice:data:capabilityFlag:"

```
