## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

```diff

-324.25.1.2.0
-  __TEXT.__text: 0x4a9dc
-  __TEXT.__auth_stubs: 0x14f0
-  __TEXT.__objc_methlist: 0x3c34
-  __TEXT.__const: 0x608
-  __TEXT.__cstring: 0x85c3
-  __TEXT.__gcc_except_tab: 0xd30
-  __TEXT.__constg_swiftt: 0x3d0
+325.7.1.1.0
+  __TEXT.__text: 0x52100
+  __TEXT.__auth_stubs: 0x1600
+  __TEXT.__objc_methlist: 0x4454
+  __TEXT.__const: 0x688
+  __TEXT.__cstring: 0x9933
+  __TEXT.__gcc_except_tab: 0x1064
+  __TEXT.__constg_swiftt: 0x3d8
   __TEXT.__swift5_typeref: 0x258
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__swift5_reflstr: 0x128
   __TEXT.__swift5_fieldmd: 0x164
-  __TEXT.__oslogstring: 0x32d
+  __TEXT.__oslogstring: 0x34d
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0x1238
-  __TEXT.__eh_frame: 0x570
-  __TEXT.__objc_classname: 0x5c4
-  __TEXT.__objc_methname: 0x7a3e
-  __TEXT.__objc_methtype: 0xaf6
-  __TEXT.__objc_stubs: 0x3f60
-  __DATA_CONST.__got: 0x4f0
-  __DATA_CONST.__const: 0xcb8
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __TEXT.__unwind_info: 0x1428
+  __TEXT.__eh_frame: 0x5d8
+  __TEXT.__objc_classname: 0x6a4
+  __TEXT.__objc_methname: 0x86fb
+  __TEXT.__objc_methtype: 0xb86
+  __TEXT.__objc_stubs: 0x4820
+  __DATA_CONST.__got: 0x540
+  __DATA_CONST.__const: 0xd80
+  __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bc0
+  __DATA_CONST.__objc_selrefs: 0x1e70
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x150
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0xa88
-  __AUTH_CONST.__const: 0x690
-  __AUTH_CONST.__cfstring: 0x30e0
-  __AUTH_CONST.__objc_const: 0x6c70
+  __AUTH_CONST.__auth_got: 0xb10
+  __AUTH_CONST.__const: 0x630
+  __AUTH_CONST.__cfstring: 0x3420
+  __AUTH_CONST.__objc_const: 0x7bb8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x8e0
-  __AUTH.__data: 0x288
-  __DATA.__objc_ivar: 0x5fc
+  __AUTH.__objc_data: 0xb60
+  __AUTH.__data: 0x290
+  __DATA.__objc_ivar: 0x6c4
   __DATA.__data: 0xc30
   __DATA.__bss: 0x2e0
   __DATA.__common: 0x8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E60720A9-09B4-3855-ACAA-96817012942B
-  Functions: 2010
-  Symbols:   5661
-  CStrings:  3305
+  UUID: FB52EE9F-506E-3E7A-8F43-E372B6A1C9D0
+  Functions: 2227
+  Symbols:   6312
+  CStrings:  3632
 
Symbols:
+ +[DAAccessoryMessage supportsSecureCoding]
+ +[DACryptoInternetInfo keychainType]
+ +[DACryptoInternetInfo supportsSecureCoding]
+ +[DACryptoInternetKeyRing keychainType]
+ +[DAExtensionCommand allocInitWithXPCObject:error:]
+ +[DAExtensionCommand supportsSecureCoding]
+ +[DAExtensionSession _executeCommandRuntimeAssertionSync:error:]
+ +[DAExtensionSession executeCommand:error:]
+ +[DAExtensionSession peripheralUUIDFromRestorationID:bundleID:peripheralUUID:error:]
+ +[DAExtensionXPCStartConfiguration supportsSecureCoding]
+ -[DAAccessoryMessage .cxx_destruct]
+ -[DAAccessoryMessage capabilityFlags]
+ -[DAAccessoryMessage copyWithZone:]
+ -[DAAccessoryMessage descriptionWithLevel:]
+ -[DAAccessoryMessage description]
+ -[DAAccessoryMessage encodeWithCoder:]
+ -[DAAccessoryMessage encodeWithXPCObject:]
+ -[DAAccessoryMessage expiresAt]
+ -[DAAccessoryMessage featureID]
+ -[DAAccessoryMessage initWithCoder:]
+ -[DAAccessoryMessage initWithCoder:].cold.1
+ -[DAAccessoryMessage initWithMessageID:]
+ -[DAAccessoryMessage initWithXPCObject:error:]
+ -[DAAccessoryMessage messageID]
+ -[DAAccessoryMessage payloadVersion]
+ -[DAAccessoryMessage setCapabilityFlags:]
+ -[DAAccessoryMessage setExpiresAt:]
+ -[DAAccessoryMessage setFeatureID:]
+ -[DAAccessoryMessage setPayloadVersion:]
+ -[DAAccessoryMessage setTransportType:]
+ -[DAAccessoryMessage transportType]
+ -[DACryptoInternetInfo .cxx_destruct]
+ -[DACryptoInternetInfo copyWithZone:]
+ -[DACryptoInternetInfo createdAt]
+ -[DACryptoInternetInfo descriptionWithLevel:]
+ -[DACryptoInternetInfo description]
+ -[DACryptoInternetInfo dictionaryRepresentation]
+ -[DACryptoInternetInfo encodeWithCoder:]
+ -[DACryptoInternetInfo encodeWithXPCObject:]
+ -[DACryptoInternetInfo identifier]
+ -[DACryptoInternetInfo initWithCoder:]
+ -[DACryptoInternetInfo initWithCoder:].cold.1
+ -[DACryptoInternetInfo initWithDictionary:error:]
+ -[DACryptoInternetInfo initWithIdentifier:internetKey:]
+ -[DACryptoInternetInfo initWithXPCObject:error:]
+ -[DACryptoInternetInfo internetKey]
+ -[DACryptoInternetInfo isExpired]
+ -[DACryptoInternetInfo isRotationEligible]
+ -[DACryptoInternetInfo keyID]
+ -[DACryptoInternetInfo setCreatedAt:]
+ -[DACryptoInternetInfo setIdentifier:]
+ -[DACryptoInternetInfo setInternetKey:]
+ -[DACryptoInternetInfo setKeyID:]
+ -[DACryptoInternetKeyRing .cxx_destruct]
+ -[DACryptoInternetKeyRing addKey:]
+ -[DACryptoInternetKeyRing allKeys]
+ -[DACryptoInternetKeyRing copyWithZone:]
+ -[DACryptoInternetKeyRing currentKey]
+ -[DACryptoInternetKeyRing descriptionWithLevel:]
+ -[DACryptoInternetKeyRing description]
+ -[DACryptoInternetKeyRing dictionaryRepresentation]
+ -[DACryptoInternetKeyRing identifier]
+ -[DACryptoInternetKeyRing initWithDictionary:error:]
+ -[DACryptoInternetKeyRing initWithIdentifier:]
+ -[DACryptoInternetKeyRing keyForKeyID:]
+ -[DACryptoInternetKeyRing purgeExpiredKeys]
+ -[DACryptoInternetKeyRing setIdentifier:]
+ -[DADevice internetCryptoInfo]
+ -[DADevice setInternetCryptoInfo:]
+ -[DADeviceAppAccessInfo appPrivateToken]
+ -[DADeviceAppAccessInfo setAppPrivateToken:]
+ -[DADeviceRegistry initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoURL:companionAppBundleID:companionAppIsOptional:supportedModes:]
+ -[DADeviceRegistry supportedMode]
+ -[DADeviceRegistry videoURL]
+ -[DADeviceRegistryInfo setSupportedMode:]
+ -[DADeviceRegistryInfo setVideoURL:]
+ -[DADeviceRegistryInfo supportedMode]
+ -[DADeviceRegistryInfo videoURL]
+ -[DAExtension _assertWithDuration:]
+ -[DAExtension _assertionTimerFired]
+ -[DAExtension _configureExtensionProcessWithError:]
+ -[DAExtension _configureXPCConnectionWithError:]
+ -[DAExtension _handleCapabilityActivated:process:]
+ -[DAExtension _invalidateAssertionTimer]
+ -[DAExtension _sandboxExtensionIssueMach].cold.10
+ -[DAExtension _sandboxExtensionIssueMach].cold.11
+ -[DAExtension _startExtension]
+ -[DAExtension _startExtension].cold.1
+ -[DAExtension _startExtension].cold.2
+ -[DAExtension _terminateProcessIfNeeded]
+ -[DAExtension alwaysRunningOverride]
+ -[DAExtension assertCapabilitiesWithFlags:duration:]
+ -[DAExtension assertWithDuration:]
+ -[DAExtension bundleID]
+ -[DAExtension initWithConfiguration:]
+ -[DAExtension initWithConfiguration:].cold.1
+ -[DAExtension initWithConfiguration:].cold.2
+ -[DAExtension initWithConfiguration:].cold.3
+ -[DAExtension initWithConfiguration:].cold.4
+ -[DAExtension initWithConfiguration:].cold.5
+ -[DAExtension setAlwaysRunningOverride:]
+ -[DAExtension stateRestorationID]
+ -[DAExtensionCapability _configureHostSessionWithError:]
+ -[DAExtensionCapability _configureXPCConnectionWithError:]
+ -[DAExtensionCapability _resumeWithError:]
+ -[DAExtensionCapability _resumed]
+ -[DAExtensionCapability _resumed].cold.1
+ -[DAExtensionCapability _sandboxExtensionIssueMach]
+ -[DAExtensionCapability _sandboxExtensionIssueMach].cold.1
+ -[DAExtensionCapability _sandboxExtensionIssueMach].cold.2
+ -[DAExtensionCapability _sandboxExtensionIssueMach].cold.3
+ -[DAExtensionCapability _sandboxExtensionIssueMach].cold.4
+ -[DAExtensionCapability _sandboxExtensionIssueMach].cold.5
+ -[DAExtensionCapability _sandboxExtensionIssueMach].cold.6
+ -[DAExtensionCapability _sandboxExtensionIssueMach].cold.7
+ -[DAExtensionCapability _startCapability]
+ -[DAExtensionCapability _startCapability].cold.1
+ -[DAExtensionCapability _startCapability].cold.2
+ -[DAExtensionCapability _suspend]
+ -[DAExtensionCapability _suspend].cold.1
+ -[DAExtensionCapability _suspend].cold.2
+ -[DAExtensionCapability activationHandler]
+ -[DAExtensionCapability bundleID]
+ -[DAExtensionCapability extensionType]
+ -[DAExtensionCapability initWithConfiguration:]
+ -[DAExtensionCapability initWithConfiguration:].cold.1
+ -[DAExtensionCapability initWithConfiguration:].cold.2
+ -[DAExtensionCapability initWithConfiguration:].cold.3
+ -[DAExtensionCapability initWithConfiguration:].cold.4
+ -[DAExtensionCapability initWithConfiguration:].cold.5
+ -[DAExtensionCapability initWithConfiguration:].cold.6
+ -[DAExtensionCapability initWithConfiguration:].cold.7
+ -[DAExtensionCapability resume]
+ -[DAExtensionCapability setActivationHandler:]
+ -[DAExtensionCapability setExtensionType:]
+ -[DAExtensionCapability suspend]
+ -[DAExtensionCapabilityConfiguration .cxx_destruct]
+ -[DAExtensionCapabilityConfiguration capabilityID]
+ -[DAExtensionCapabilityConfiguration descriptionWithLevel:]
+ -[DAExtensionCapabilityConfiguration description]
+ -[DAExtensionCapabilityConfiguration device]
+ -[DAExtensionCapabilityConfiguration extensionIdentity]
+ -[DAExtensionCapabilityConfiguration setCapabilityID:]
+ -[DAExtensionCapabilityConfiguration setDevice:]
+ -[DAExtensionCapabilityConfiguration setExtensionIdentity:]
+ -[DAExtensionCapabilityConfiguration setStateRestorationID:]
+ -[DAExtensionCapabilityConfiguration stateRestorationID]
+ -[DAExtensionCapabilityConfiguration valid]
+ -[DAExtensionCommand .cxx_destruct]
+ -[DAExtensionCommand activationHandler]
+ -[DAExtensionCommand descriptionWithLevel:]
+ -[DAExtensionCommand encodeWithXPCObject:]
+ -[DAExtensionCommand initWithType:]
+ -[DAExtensionCommand initWithXPCObject:error:]
+ -[DAExtensionCommand setActivationHandler:]
+ -[DAExtensionCommand type]
+ -[DAExtensionConfiguration .cxx_destruct]
+ -[DAExtensionConfiguration descriptionWithLevel:]
+ -[DAExtensionConfiguration description]
+ -[DAExtensionConfiguration device]
+ -[DAExtensionConfiguration extensionIdentity]
+ -[DAExtensionConfiguration setDevice:]
+ -[DAExtensionConfiguration setExtensionIdentity:]
+ -[DAExtensionConfiguration setType:]
+ -[DAExtensionConfiguration type]
+ -[DAExtensionConfiguration valid]
+ -[DAExtensionEventData accessoryMessages]
+ -[DAExtensionEventData deliveryStatus]
+ -[DAExtensionEventData initWithDevice:accessoryMessages:]
+ -[DAExtensionEventData messageID]
+ -[DAExtensionEventData setAccessoryMessages:]
+ -[DAExtensionEventData setDeliveryStatus:]
+ -[DAExtensionEventData setMessageID:]
+ -[DAExtensionEventLifecycle setStateRestorationID:]
+ -[DAExtensionEventLifecycle stateRestorationID]
+ -[DAExtensionRuntimeAssertion .cxx_destruct]
+ -[DAExtensionRuntimeAssertion bundleID]
+ -[DAExtensionRuntimeAssertion capabilityFlags]
+ -[DAExtensionRuntimeAssertion descriptionWithLevel:]
+ -[DAExtensionRuntimeAssertion description]
+ -[DAExtensionRuntimeAssertion device]
+ -[DAExtensionRuntimeAssertion dispatchQueue]
+ -[DAExtensionRuntimeAssertion duration]
+ -[DAExtensionRuntimeAssertion encodeWithXPCObject:]
+ -[DAExtensionRuntimeAssertion initWithBundleID:peripheralUUID:]
+ -[DAExtensionRuntimeAssertion initWithDevice:capabilityFlags:]
+ -[DAExtensionRuntimeAssertion initWithXPCObject:error:]
+ -[DAExtensionRuntimeAssertion invalidationHandler]
+ -[DAExtensionRuntimeAssertion peripheralUUID]
+ -[DAExtensionRuntimeAssertion setBundleID:]
+ -[DAExtensionRuntimeAssertion setCapabilityFlags:]
+ -[DAExtensionRuntimeAssertion setDevice:]
+ -[DAExtensionRuntimeAssertion setDispatchQueue:]
+ -[DAExtensionRuntimeAssertion setDuration:]
+ -[DAExtensionRuntimeAssertion setInvalidationHandler:]
+ -[DAExtensionRuntimeAssertion setPeripheralUUID:]
+ -[DAExtensionRuntimeAssertion setXpcCnx:]
+ -[DAExtensionRuntimeAssertion setXpcListenerEndpoint:]
+ -[DAExtensionRuntimeAssertion xpcCnx]
+ -[DAExtensionRuntimeAssertion xpcListenerEndpoint]
+ -[DAExtensionSession activateReason]
+ -[DAExtensionSession activatingCommand]
+ -[DAExtensionSession setActivateReason:]
+ -[DAExtensionSession setActivatingCommand:]
+ -[DAExtensionSessionConfiguration initWithStateRestorationID:]
+ -[DAExtensionSessionConfiguration initWithStateRestorationID:].cold.1
+ -[DAExtensionSessionConfiguration setStateRestorationID:]
+ -[DAExtensionSessionConfiguration stateRestorationID]
+ -[DAExtensionXPCStartConfiguration .cxx_destruct]
+ -[DAExtensionXPCStartConfiguration appBundleID]
+ -[DAExtensionXPCStartConfiguration device]
+ -[DAExtensionXPCStartConfiguration encodeWithCoder:]
+ -[DAExtensionXPCStartConfiguration encodeWithXPCObject:]
+ -[DAExtensionXPCStartConfiguration initWithCoder:]
+ -[DAExtensionXPCStartConfiguration initWithCoder:].cold.1
+ -[DAExtensionXPCStartConfiguration initWithXPCObject:error:]
+ -[DAExtensionXPCStartConfiguration restorationID]
+ -[DAExtensionXPCStartConfiguration setAppBundleID:]
+ -[DAExtensionXPCStartConfiguration setDevice:]
+ -[DAExtensionXPCStartConfiguration setRestorationID:]
+ -[DAExtensionXPCStartConfiguration setType:]
+ -[DAExtensionXPCStartConfiguration type]
+ -[DAIncomingMessage descriptionWithLevel:]
+ -[DAIncomingMessage encodeWithXPCObject:]
+ -[DAIncomingMessage initWithXPCObject:error:]
+ -[DAOutgoingMessage deliveryStatus]
+ -[DAOutgoingMessage descriptionWithLevel:]
+ -[DAOutgoingMessage encodeWithXPCObject:]
+ -[DAOutgoingMessage initWithXPCObject:error:]
+ -[DAOutgoingMessage setDeliveryStatus:]
+ -[DASession _queue_XPCConnectionAccept:]
+ -[DASession _queue_XPCDispatchMessage:]
+ -[DASession _queue_XPCDispatchMessage:].cold.1
+ -[DASession _queue_XPCListenerEvent:]
+ -[DASession _queue_XPCListenerEvent:].cold.1
+ -[DASession _queue_XPCListenerEvent:].cold.2
+ -[DASession _queue_XPCReceivedDAEvent:]
+ -[DASession _queue_XPCReceivedDAEvent:].cold.1
+ -[DASession _queue_XPCReceivedDAEvent:].cold.2
+ -[DASession _queue_XPCReceivedDAEvent:].cold.3
+ -[DASession _queue_XPCReceivedMessage:]
+ -[DASession _queue_XPCReceivedMessage:].cold.1
+ -[DASession _queue_XPCReceivedMessage:].cold.2
+ -[DASession _queue_XPCReceivedMessage:].cold.3
+ -[DASession _queue_activateDirect]
+ -[DASession _queue_activateDirect].cold.1
+ -[DASession _queue_activateXPCCompleted:]
+ -[DASession _queue_ensureXPCStarted]
+ -[DASession _queue_getAuthorizedDevicesCompleted:completionHandler:]
+ -[DASession _queue_getBluetoothAccessInfoCompleted:completionHandler:]
+ -[DASession _queue_getDevicesCompleted:completionHandler:]
+ -[DASession _queue_getPartialIPsCompleted:completionHandler:]
+ -[DASession _queue_interrupted]
+ -[DASession _queue_interrupted].cold.1
+ -[DASession _queue_invalidate]
+ -[DASession _queue_invalidate].cold.1
+ -[DASession _queue_noteXPCConnectionInvalidated]
+ -[DASession _queue_noteXPCConnectionInvalidated].cold.1
+ -[DASession _queue_reconnectIfNecessaryFromDaemonSpawn]
+ -[DASession _queue_reconnectIfNecessaryFromDaemonSpawn].cold.1
+ -[DASession _queue_reportEvent:]
+ -[DASession _queue_reportEvent:].cold.1
+ -[DASession _queue_reportEventType:]
+ -[DASession _queue_sendActivationXPCMessage]
+ -[DASession _queue_sendActivationXPCMessage].cold.1
+ -[DASession _queue_setupXPCConnectionIfNecessary]
+ -[DASession _queue_synthesizeDeviceEventsFromPrior:toNewDevices:]
+ -[DASession _queue_synthesizeDeviceEventsFromPrior:toNewDevices:].cold.1
+ -[DASession _startSpawnNotificationListener]
+ -[DASession _startSpawnNotificationListener].cold.1
+ -[DASession deferReconnect]
+ -[DASession setDeferReconnect:]
+ GCC_except_table137
+ GCC_except_table19
+ GCC_except_table32
+ GCC_except_table35
+ GCC_except_table44
+ GCC_except_table48
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table57
+ GCC_except_table62
+ GCC_except_table63
+ GCC_except_table66
+ GCC_except_table67
+ GCC_except_table71
+ GCC_except_table72
+ GCC_except_table96
+ _DACryptoInternetInfoDeriveKeyID
+ _DAExtensionCommandTypeToString
+ _DATransportTypeToString
+ _OBJC_CLASS_$_DAAccessoryMessage
+ _OBJC_CLASS_$_DACryptoInternetInfo
+ _OBJC_CLASS_$_DACryptoInternetKeyRing
+ _OBJC_CLASS_$_DAExtensionCapabilityConfiguration
+ _OBJC_CLASS_$_DAExtensionCommand
+ _OBJC_CLASS_$_DAExtensionConfiguration
+ _OBJC_CLASS_$_DAExtensionRuntimeAssertion
+ _OBJC_CLASS_$_DAExtensionXPCStartConfiguration
+ _OBJC_CLASS_$_NSMutableIndexSet
+ _OBJC_IVAR_$_DAAccessoryMessage._capabilityFlags
+ _OBJC_IVAR_$_DAAccessoryMessage._expiresAt
+ _OBJC_IVAR_$_DAAccessoryMessage._featureID
+ _OBJC_IVAR_$_DAAccessoryMessage._messageID
+ _OBJC_IVAR_$_DAAccessoryMessage._payloadVersion
+ _OBJC_IVAR_$_DAAccessoryMessage._transportType
+ _OBJC_IVAR_$_DACryptoInternetInfo._createdAt
+ _OBJC_IVAR_$_DACryptoInternetInfo._identifier
+ _OBJC_IVAR_$_DACryptoInternetInfo._internetKey
+ _OBJC_IVAR_$_DACryptoInternetInfo._keyID
+ _OBJC_IVAR_$_DACryptoInternetKeyRing._identifier
+ _OBJC_IVAR_$_DACryptoInternetKeyRing._keys
+ _OBJC_IVAR_$_DACryptoInternetKeyRing._lock
+ _OBJC_IVAR_$_DADevice._internetCryptoInfo
+ _OBJC_IVAR_$_DADeviceAppAccessInfo._appPrivateToken
+ _OBJC_IVAR_$_DADeviceRegistry._supportedMode
+ _OBJC_IVAR_$_DADeviceRegistry._videoURL
+ _OBJC_IVAR_$_DADeviceRegistryInfo._supportedMode
+ _OBJC_IVAR_$_DADeviceRegistryInfo._videoURL
+ _OBJC_IVAR_$_DAExtension._alwaysRunningOverride
+ _OBJC_IVAR_$_DAExtension._appBundleID
+ _OBJC_IVAR_$_DAExtension._assertionExpiration
+ _OBJC_IVAR_$_DAExtension._assertionTimer
+ _OBJC_IVAR_$_DAExtension._instanceIdentifier
+ _OBJC_IVAR_$_DAExtension._stateRestorationID
+ _OBJC_IVAR_$_DAExtensionCapability._activationHandler
+ _OBJC_IVAR_$_DAExtensionCapability._extensionProcess
+ _OBJC_IVAR_$_DAExtensionCapability._extensionType
+ _OBJC_IVAR_$_DAExtensionCapability._stateRestorationID
+ _OBJC_IVAR_$_DAExtensionCapabilityConfiguration._capabilityID
+ _OBJC_IVAR_$_DAExtensionCapabilityConfiguration._device
+ _OBJC_IVAR_$_DAExtensionCapabilityConfiguration._extensionIdentity
+ _OBJC_IVAR_$_DAExtensionCapabilityConfiguration._stateRestorationID
+ _OBJC_IVAR_$_DAExtensionCommand._activationHandler
+ _OBJC_IVAR_$_DAExtensionCommand._type
+ _OBJC_IVAR_$_DAExtensionConfiguration._device
+ _OBJC_IVAR_$_DAExtensionConfiguration._extensionIdentity
+ _OBJC_IVAR_$_DAExtensionConfiguration._type
+ _OBJC_IVAR_$_DAExtensionEventData._accessoryMessages
+ _OBJC_IVAR_$_DAExtensionEventData._deliveryStatus
+ _OBJC_IVAR_$_DAExtensionEventData._messageID
+ _OBJC_IVAR_$_DAExtensionEventLifecycle._stateRestorationID
+ _OBJC_IVAR_$_DAExtensionRuntimeAssertion._bundleID
+ _OBJC_IVAR_$_DAExtensionRuntimeAssertion._capabilityFlags
+ _OBJC_IVAR_$_DAExtensionRuntimeAssertion._device
+ _OBJC_IVAR_$_DAExtensionRuntimeAssertion._dispatchQueue
+ _OBJC_IVAR_$_DAExtensionRuntimeAssertion._duration
+ _OBJC_IVAR_$_DAExtensionRuntimeAssertion._invalidationHandler
+ _OBJC_IVAR_$_DAExtensionRuntimeAssertion._peripheralUUID
+ _OBJC_IVAR_$_DAExtensionRuntimeAssertion._xpcCnx
+ _OBJC_IVAR_$_DAExtensionRuntimeAssertion._xpcListenerEndpoint
+ _OBJC_IVAR_$_DAExtensionSession._activateReason
+ _OBJC_IVAR_$_DAExtensionSession._activatingCommand
+ _OBJC_IVAR_$_DAExtensionSessionConfiguration._stateRestorationID
+ _OBJC_IVAR_$_DAExtensionXPCStartConfiguration._appBundleID
+ _OBJC_IVAR_$_DAExtensionXPCStartConfiguration._device
+ _OBJC_IVAR_$_DAExtensionXPCStartConfiguration._restorationID
+ _OBJC_IVAR_$_DAExtensionXPCStartConfiguration._type
+ _OBJC_IVAR_$_DAOutgoingMessage._deliveryStatus
+ _OBJC_IVAR_$_DASession._queue
+ _OBJC_IVAR_$_DASession._queue_activateCalled
+ _OBJC_IVAR_$_DASession._queue_hasEverSetDeviceMap
+ _OBJC_IVAR_$_DASession._queue_invalidateCalled
+ _OBJC_IVAR_$_DASession._queue_invalidateDone
+ _OBJC_IVAR_$_DASession._queue_requiresActivation
+ _OBJC_IVAR_$_DASession._queue_spawnNotifyToken
+ _OBJC_IVAR_$_DASession._queue_xpcCnx
+ _OBJC_IVAR_$_DASession._queue_xpcListenerEndpoint
+ _OBJC_IVAR_$_DASession._syncSelf_deferReconnect
+ _OBJC_IVAR_$_DASession._syncSelf_deviceMap
+ _OBJC_METACLASS_$_DAAccessoryMessage
+ _OBJC_METACLASS_$_DACryptoInternetInfo
+ _OBJC_METACLASS_$_DACryptoInternetKeyRing
+ _OBJC_METACLASS_$_DAExtensionCapabilityConfiguration
+ _OBJC_METACLASS_$_DAExtensionCommand
+ _OBJC_METACLASS_$_DAExtensionConfiguration
+ _OBJC_METACLASS_$_DAExtensionRuntimeAssertion
+ _OBJC_METACLASS_$_DAExtensionXPCStartConfiguration
+ __OBJC_$_CLASS_METHODS_DAAccessoryMessage
+ __OBJC_$_CLASS_METHODS_DACryptoInternetInfo
+ __OBJC_$_CLASS_METHODS_DACryptoInternetKeyRing
+ __OBJC_$_CLASS_METHODS_DAExtensionCommand
+ __OBJC_$_CLASS_METHODS_DAExtensionXPCStartConfiguration
+ __OBJC_$_CLASS_PROP_LIST_DAAccessoryMessage
+ __OBJC_$_CLASS_PROP_LIST_DACryptoInternetInfo
+ __OBJC_$_CLASS_PROP_LIST_DAExtensionXPCStartConfiguration
+ __OBJC_$_INSTANCE_METHODS_DAAccessoryMessage
+ __OBJC_$_INSTANCE_METHODS_DACryptoInternetInfo
+ __OBJC_$_INSTANCE_METHODS_DACryptoInternetKeyRing
+ __OBJC_$_INSTANCE_METHODS_DAExtensionCapabilityConfiguration
+ __OBJC_$_INSTANCE_METHODS_DAExtensionCommand
+ __OBJC_$_INSTANCE_METHODS_DAExtensionConfiguration
+ __OBJC_$_INSTANCE_METHODS_DAExtensionRuntimeAssertion
+ __OBJC_$_INSTANCE_METHODS_DAExtensionXPCStartConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_DAAccessoryMessage
+ __OBJC_$_INSTANCE_VARIABLES_DACryptoInternetInfo
+ __OBJC_$_INSTANCE_VARIABLES_DACryptoInternetKeyRing
+ __OBJC_$_INSTANCE_VARIABLES_DAExtensionCapabilityConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_DAExtensionCommand
+ __OBJC_$_INSTANCE_VARIABLES_DAExtensionConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_DAExtensionRuntimeAssertion
+ __OBJC_$_INSTANCE_VARIABLES_DAExtensionXPCStartConfiguration
+ __OBJC_$_PROP_LIST_DAAccessoryMessage
+ __OBJC_$_PROP_LIST_DACryptoInternetInfo
+ __OBJC_$_PROP_LIST_DACryptoInternetKeyRing
+ __OBJC_$_PROP_LIST_DAExtensionCapabilityConfiguration
+ __OBJC_$_PROP_LIST_DAExtensionCommand
+ __OBJC_$_PROP_LIST_DAExtensionConfiguration
+ __OBJC_$_PROP_LIST_DAExtensionRuntimeAssertion
+ __OBJC_$_PROP_LIST_DAExtensionXPCStartConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_DAAccessoryMessage
+ __OBJC_CLASS_PROTOCOLS_$_DACryptoInternetInfo
+ __OBJC_CLASS_PROTOCOLS_$_DACryptoInternetKeyRing
+ __OBJC_CLASS_PROTOCOLS_$_DAExtensionCommand
+ __OBJC_CLASS_PROTOCOLS_$_DAExtensionRuntimeAssertion
+ __OBJC_CLASS_PROTOCOLS_$_DAExtensionXPCStartConfiguration
+ __OBJC_CLASS_RO_$_DAAccessoryMessage
+ __OBJC_CLASS_RO_$_DACryptoInternetInfo
+ __OBJC_CLASS_RO_$_DACryptoInternetKeyRing
+ __OBJC_CLASS_RO_$_DAExtensionCapabilityConfiguration
+ __OBJC_CLASS_RO_$_DAExtensionCommand
+ __OBJC_CLASS_RO_$_DAExtensionConfiguration
+ __OBJC_CLASS_RO_$_DAExtensionRuntimeAssertion
+ __OBJC_CLASS_RO_$_DAExtensionXPCStartConfiguration
+ __OBJC_METACLASS_RO_$_DAAccessoryMessage
+ __OBJC_METACLASS_RO_$_DACryptoInternetInfo
+ __OBJC_METACLASS_RO_$_DACryptoInternetKeyRing
+ __OBJC_METACLASS_RO_$_DAExtensionCapabilityConfiguration
+ __OBJC_METACLASS_RO_$_DAExtensionCommand
+ __OBJC_METACLASS_RO_$_DAExtensionConfiguration
+ __OBJC_METACLASS_RO_$_DAExtensionRuntimeAssertion
+ __OBJC_METACLASS_RO_$_DAExtensionXPCStartConfiguration
+ ___19-[DASession xpcCnx]_block_invoke
+ ___23-[DAExtension _suspend]_block_invoke
+ ___23-[DAExtension _suspend]_block_invoke.cold.1
+ ___23-[DASession setXpcCnx:]_block_invoke
+ ___30-[DAExtension _startExtension]_block_invoke
+ ___30-[DAExtension _startExtension]_block_invoke.cold.1
+ ___31-[DAExtensionCapability resume]_block_invoke
+ ___32-[DAExtensionCapability suspend]_block_invoke
+ ___32-[DASession xpcListenerEndpoint]_block_invoke
+ ___34-[DAExtension assertWithDuration:]_block_invoke
+ ___35-[DAExtension _assertWithDuration:]_block_invoke
+ ___35-[DAExtension _assertWithDuration:]_block_invoke_2
+ ___36-[DAExtension invalidateWithReason:]_block_invoke.cold.1
+ ___36-[DASession setXpcListenerEndpoint:]_block_invoke
+ ___41-[DAExtension _sandboxExtensionIssueMach]_block_invoke_5
+ ___41-[DAExtension _sandboxExtensionIssueMach]_block_invoke_5.cold.1
+ ___41-[DAExtensionCapability _startCapability]_block_invoke
+ ___41-[DAExtensionCapability _startCapability]_block_invoke.cold.1
+ ___41-[DASession _queue_activateXPCCompleted:]_block_invoke
+ ___41-[DASession _queue_activateXPCCompleted:]_block_invoke.cold.1
+ ___41-[DASession _queue_activateXPCCompleted:]_block_invoke_2
+ ___42-[DAExtensionCapability _resumeWithError:]_block_invoke
+ ___42-[DAExtensionCapability _resumeWithError:]_block_invoke.cold.1
+ ___43+[DAExtensionSession executeCommand:error:]_block_invoke
+ ___43+[DAExtensionSession executeCommand:error:]_block_invoke.cold.1
+ ___43-[DACryptoInternetKeyRing purgeExpiredKeys]_block_invoke
+ ___44-[DASession _queue_sendActivationXPCMessage]_block_invoke
+ ___44-[DASession _startSpawnNotificationListener]_block_invoke
+ ___44-[DASession _startSpawnNotificationListener]_block_invoke_2
+ ___48-[DAExtension _configureXPCConnectionWithError:]_block_invoke
+ ___48-[DAExtension _configureXPCConnectionWithError:]_block_invoke_2
+ ___48-[DAExtension _configureXPCConnectionWithError:]_block_invoke_2.cold.1
+ ___48-[DAExtension _configureXPCConnectionWithError:]_block_invoke_3
+ ___48-[DAExtension _configureXPCConnectionWithError:]_block_invoke_3.cold.1
+ ___48-[DAExtension _extensionEnsureStartedWithError:]_block_invoke.cold.1
+ ___49-[DASession _queue_setupXPCConnectionIfNecessary]_block_invoke
+ ___50-[DAExtension _handleCapabilityActivated:process:]_block_invoke
+ ___50-[DAExtension _handleCapabilityActivated:process:]_block_invoke.cold.1
+ ___51-[DAExtension _configureExtensionProcessWithError:]_block_invoke
+ ___51-[DAExtension _configureExtensionProcessWithError:]_block_invoke_2
+ ___51-[DAExtension _configureExtensionProcessWithError:]_block_invoke_2.cold.1
+ ___51-[DAExtensionCapability _sandboxExtensionIssueMach]_block_invoke
+ ___51-[DAExtensionCapability _sandboxExtensionIssueMach]_block_invoke.cold.1
+ ___51-[DAExtensionCapability _sandboxExtensionIssueMach]_block_invoke_2
+ ___51-[DAExtensionCapability _sandboxExtensionIssueMach]_block_invoke_2.cold.1
+ ___51-[DAExtensionCapability _sandboxExtensionIssueMach]_block_invoke_3
+ ___51-[DAExtensionCapability _sandboxExtensionIssueMach]_block_invoke_3.cold.1
+ ___52-[DAExtension assertCapabilitiesWithFlags:duration:]_block_invoke
+ ___52-[DAExtension assertCapabilitiesWithFlags:duration:]_block_invoke_2
+ ___52-[DAExtension assertCapabilitiesWithFlags:duration:]_block_invoke_2.cold.1
+ ___56-[DAExtensionCapability _configureHostSessionWithError:]_block_invoke
+ ___56-[DAExtensionCapability _configureHostSessionWithError:]_block_invoke.cold.1
+ ___56-[DAExtensionCapability _configureHostSessionWithError:]_block_invoke_2
+ ___56-[DAExtensionCapability _configureHostSessionWithError:]_block_invoke_2.cold.1
+ ___56-[DAExtensionCapability _configureHostSessionWithError:]_block_invoke_3
+ ___56-[DAExtensionCapability _configureHostSessionWithError:]_block_invoke_3.cold.1
+ ___57-[DAExtension _capabilitiesEnsureStartedWithFlags:error:]_block_invoke_4
+ ___57-[DAExtension _capabilitiesEnsureStartedWithFlags:error:]_block_invoke_4.cold.1
+ ___58-[DAExtensionCapability _configureXPCConnectionWithError:]_block_invoke
+ ___58-[DAExtensionCapability _configureXPCConnectionWithError:]_block_invoke.cold.1
+ ___58-[DAExtensionCapability _configureXPCConnectionWithError:]_block_invoke_2
+ ___58-[DAExtensionCapability _configureXPCConnectionWithError:]_block_invoke_2.cold.1
+ ___58-[DAExtensionCapability _configureXPCConnectionWithError:]_block_invoke_3
+ ___58-[DAExtensionCapability _configureXPCConnectionWithError:]_block_invoke_3.cold.1
+ ___58-[DASession _queue_getDevicesCompleted:completionHandler:]_block_invoke
+ ___61-[DASession _queue_getPartialIPsCompleted:completionHandler:]_block_invoke
+ ___64+[DAExtensionSession _executeCommandRuntimeAssertionSync:error:]_block_invoke
+ ___64+[DAExtensionSession _executeCommandRuntimeAssertionSync:error:]_block_invoke.cold.1
+ ___64+[DAExtensionSession _executeCommandRuntimeAssertionSync:error:]_block_invoke_2
+ ___65-[DASession _queue_synthesizeDeviceEventsFromPrior:toNewDevices:]_block_invoke
+ ___65-[DASession _queue_synthesizeDeviceEventsFromPrior:toNewDevices:]_block_invoke.cold.1
+ ___65-[DASession _queue_synthesizeDeviceEventsFromPrior:toNewDevices:]_block_invoke_2
+ ___65-[DASession _queue_synthesizeDeviceEventsFromPrior:toNewDevices:]_block_invoke_2.cold.1
+ ___68-[DASession _queue_getAuthorizedDevicesCompleted:completionHandler:]_block_invoke
+ ___70-[DASession _queue_getBluetoothAccessInfoCompleted:completionHandler:]_block_invoke
+ ___72-[DASession launchInteractionWithDevice:flags:reason:completionHandler:]_block_invoke.cold.1
+ ___72-[DASession launchInteractionWithDevice:flags:reason:completionHandler:]_block_invoke_2
+ ___84+[DAExtensionSession peripheralUUIDFromRestorationID:bundleID:peripheralUUID:error:]_block_invoke
+ ___84+[DAExtensionSession peripheralUUIDFromRestorationID:bundleID:peripheralUUID:error:]_block_invoke.cold.1
+ ___84+[DAExtensionSession peripheralUUIDFromRestorationID:bundleID:peripheralUUID:error:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e37_v32?0"DACryptoInternetInfo"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e55_v24?0"DAExtensionCapability"8"_EXExtensionProcess"16ls32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_48_e8_32s40s_e35_v32?0"NSString"8"DADevice"16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e46_v24?0"_EXCapabilityHostSession"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_literal_global.145
+ ___block_literal_global.184
+ ___block_literal_global.197
+ ___block_literal_global.204
+ ___block_literal_global.213
+ ___block_literal_global.216
+ ___block_literal_global.230
+ ___block_literal_global.256
+ ___block_literal_global.267
+ ___block_literal_global.274
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ __dispatch_source_type_timer
+ _dispatch_get_global_queue
+ _dispatch_resume
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_sync
+ _kTCCServiceAudioAccessoryHeadTrackData
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_msgSend$_assertWithDuration:
+ _objc_msgSend$_assertionTimerFired
+ _objc_msgSend$_configureExtensionProcessWithError:
+ _objc_msgSend$_configureHostSessionWithError:
+ _objc_msgSend$_configureXPCConnectionWithError:
+ _objc_msgSend$_executeCommandRuntimeAssertionSync:error:
+ _objc_msgSend$_handleCapabilityActivated:process:
+ _objc_msgSend$_invalidateAssertionTimer
+ _objc_msgSend$_queue_XPCConnectionAccept:
+ _objc_msgSend$_queue_XPCDispatchMessage:
+ _objc_msgSend$_queue_XPCListenerEvent:
+ _objc_msgSend$_queue_XPCReceivedDAEvent:
+ _objc_msgSend$_queue_XPCReceivedMessage:
+ _objc_msgSend$_queue_activateDirect
+ _objc_msgSend$_queue_activateXPCCompleted:
+ _objc_msgSend$_queue_ensureXPCStarted
+ _objc_msgSend$_queue_getAuthorizedDevicesCompleted:completionHandler:
+ _objc_msgSend$_queue_getBluetoothAccessInfoCompleted:completionHandler:
+ _objc_msgSend$_queue_getDevicesCompleted:completionHandler:
+ _objc_msgSend$_queue_getPartialIPsCompleted:completionHandler:
+ _objc_msgSend$_queue_interrupted
+ _objc_msgSend$_queue_invalidate
+ _objc_msgSend$_queue_noteXPCConnectionInvalidated
+ _objc_msgSend$_queue_reconnectIfNecessaryFromDaemonSpawn
+ _objc_msgSend$_queue_reportEvent:
+ _objc_msgSend$_queue_reportEventType:
+ _objc_msgSend$_queue_sendActivationXPCMessage
+ _objc_msgSend$_queue_setupXPCConnectionIfNecessary
+ _objc_msgSend$_queue_synthesizeDeviceEventsFromPrior:toNewDevices:
+ _objc_msgSend$_resumeWithError:
+ _objc_msgSend$_resumed
+ _objc_msgSend$_startCapability
+ _objc_msgSend$_startExtension
+ _objc_msgSend$_startSpawnNotificationListener
+ _objc_msgSend$_terminateProcessIfNeeded
+ _objc_msgSend$addIndex:
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$decodeInt32ForKey:
+ _objc_msgSend$deferReconnect
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$direct
+ _objc_msgSend$encodeInt32:forKey:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$eventHandler
+ _objc_msgSend$expiresAt
+ _objc_msgSend$extensionIdentity
+ _objc_msgSend$featureID
+ _objc_msgSend$firstObject
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithDictionary:error:
+ _objc_msgSend$initWithIdentifier:internetKey:
+ _objc_msgSend$initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoURL:companionAppBundleID:companionAppIsOptional:supportedModes:
+ _objc_msgSend$initWithMessageID:
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$isRotationEligible
+ _objc_msgSend$keyID
+ _objc_msgSend$messageID
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$payloadVersion
+ _objc_msgSend$peripheralUUID
+ _objc_msgSend$process
+ _objc_msgSend$removeObjectsAtIndexes:
+ _objc_msgSend$resumeWithError:
+ _objc_msgSend$setActivationHandler:
+ _objc_msgSend$setAppBundleID:
+ _objc_msgSend$setCapabilityFlags:
+ _objc_msgSend$setCapabilityID:
+ _objc_msgSend$setDevice:
+ _objc_msgSend$setExpiresAt:
+ _objc_msgSend$setFeatureID:
+ _objc_msgSend$setPayloadVersion:
+ _objc_msgSend$setRestorationID:
+ _objc_msgSend$setStateRestorationID:
+ _objc_msgSend$setSupportedMode:
+ _objc_msgSend$setType:
+ _objc_msgSend$setVideoURL:
+ _objc_msgSend$startWithConfiguration:
+ _objc_msgSend$stateRestorationID
+ _objc_msgSend$supportedMode
+ _objc_msgSend$suspend
+ _objc_msgSend$suspendWithError:
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_msgSend$valid
+ _objc_msgSend$videoURL
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _sandbox_extension_issue_generic
+ _xpc_dictionary_get_double
+ _xpc_dictionary_get_uint64
- +[DAExtensionSession bluetoothRestorationIDForBundleID:error:]
- +[DAExtensionSession launchExtensionWithBundle:extensionType:]
- +[DAExtensionSession resumeExtensionWithBundle:extensionType:]
- +[DAExtensionSession suspendExtensionWithBundle:extensionType:]
- +[DAExtensionSession suspendExtensionWithBundle:extensionType:extensionCapabilityFlags:]
- -[DADeviceRegistry initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoData:companionAppBundleID:companionAppIsOptional:]
- -[DADeviceRegistry videoData]
- -[DADeviceRegistryInfo setVideoData:]
- -[DADeviceRegistryInfo videoData]
- -[DAExtension _invalidated:]
- -[DAExtension _invalidated:].cold.1
- -[DAExtension _invalidated:].cold.2
- -[DAExtension _invalidated].cold.2
- -[DAExtension _invalidated].cold.3
- -[DAExtension _startExtension:]
- -[DAExtension _startExtension:].cold.1
- -[DAExtension _startExtension:].cold.2
- -[DAExtension _suspend].cold.1
- -[DAExtension bluetoothRestorationID]
- -[DAExtension initWithDevice:identity:type:]
- -[DAExtension initWithDevice:identity:type:].cold.1
- -[DAExtension launchCapabilitiesWithFlags:]
- -[DAExtension launch]
- -[DAExtension resumeCapabilitiesWithFlags:]
- -[DAExtension resume]
- -[DAExtension setBluetoothRestorationID:]
- -[DAExtension suspendCapabilitiesWithFlags:]
- -[DAExtensionCapability _sandboxExtensionIssueMach:]
- -[DAExtensionCapability _sandboxExtensionIssueMach:].cold.1
- -[DAExtensionCapability _sandboxExtensionIssueMach:].cold.2
- -[DAExtensionCapability _sandboxExtensionIssueMach:].cold.3
- -[DAExtensionCapability _sandboxExtensionIssueMach:].cold.4
- -[DAExtensionCapability _sandboxExtensionIssueMach:].cold.5
- -[DAExtensionCapability _sandboxExtensionIssueMach:].cold.6
- -[DAExtensionCapability _sandboxExtensionIssueMach:].cold.7
- -[DAExtensionCapability _startCapability:]
- -[DAExtensionCapability _startCapability:].cold.1
- -[DAExtensionCapability _startCapability:].cold.2
- -[DAExtensionCapability initWithIdentity:device:capabilityID:]
- -[DAExtensionCapability initWithIdentity:device:capabilityID:].cold.1
- -[DAExtensionCapability initWithIdentity:device:capabilityID:].cold.2
- -[DAExtensionCapability initWithIdentity:device:capabilityID:].cold.3
- -[DAExtensionCapability initWithIdentity:device:capabilityID:].cold.4
- -[DAExtensionCapability initWithIdentity:device:capabilityID:].cold.5
- -[DAExtensionSession launch]
- -[DAExtensionSession resume]
- -[DAExtensionSession suspend]
- -[DAExtensionSession terminate]
- -[DAExtensionSessionConfiguration bluetoothRestorationID]
- -[DAExtensionSessionConfiguration initWithBluetoothRestorationID:]
- -[DAExtensionSessionConfiguration initWithBluetoothRestorationID:].cold.1
- -[DAExtensionSessionConfiguration setBluetoothRestorationID:]
- -[DAIncomingMessage expiresAt]
- -[DAIncomingMessage featureID]
- -[DAIncomingMessage messageID]
- -[DAIncomingMessage payloadVersion]
- -[DAIncomingMessage setExpiresAt:]
- -[DAIncomingMessage setFeatureID:]
- -[DAIncomingMessage setMessageID:]
- -[DAIncomingMessage setPayloadVersion:]
- -[DAOutgoingMessage expiresAt]
- -[DAOutgoingMessage featureID]
- -[DAOutgoingMessage messageID]
- -[DAOutgoingMessage payloadVersion]
- -[DAOutgoingMessage setExpiresAt:]
- -[DAOutgoingMessage setFeatureID:]
- -[DAOutgoingMessage setMessageID:]
- -[DAOutgoingMessage setPayloadVersion:]
- -[DASession _activateDirect]
- -[DASession _activateDirect].cold.1
- -[DASession _activateXPCCompleted:]
- -[DASession _activateXPCStart:]
- -[DASession _activateXPCStart:].cold.1
- -[DASession _ensureXPCStarted]
- -[DASession _getAuthorizedDevicesCompleted:completionHandler:]
- -[DASession _getBluetoothAccessInfoCompleted:completionHandler:]
- -[DASession _getDevicesCompleted:completionHandler:]
- -[DASession _getPartialIPsCompleted:completionHandler:]
- -[DASession _interrupted]
- -[DASession _interrupted].cold.1
- -[DASession _invalidated]
- -[DASession _invalidated].cold.1
- -[DASession _reportEvent:]
- -[DASession _reportEvent:].cold.1
- -[DASession _reportEventType:]
- -[DASession _xpcConnectionAccept:]
- -[DASession _xpcListenerEvent:]
- -[DASession _xpcListenerEvent:].cold.1
- -[DASession _xpcListenerEvent:].cold.2
- -[DASession _xpcReceivedDAEvent:]
- -[DASession _xpcReceivedDAEvent:].cold.1
- -[DASession _xpcReceivedDAEvent:].cold.2
- -[DASession _xpcReceivedMessage:]
- -[DASession _xpcReceivedMessage:].cold.1
- -[DASession launchInteractionWithDevice:flags:reason:completionHandler:].cold.1
- -[DASession xpcReceivedMessage:]
- -[DASession xpcReceivedMessage:].cold.1
- -[DASession xpcReceivedMessage:].cold.2
- -[DASession xpcReceivedMessage:].cold.3
- GCC_except_table10
- GCC_except_table16
- GCC_except_table27
- GCC_except_table28
- GCC_except_table31
- GCC_except_table34
- GCC_except_table46
- GCC_except_table47
- GCC_except_table51
- GCC_except_table55
- GCC_except_table56
- GCC_except_table61
- GCC_except_table8
- GCC_except_table82
- _OBJC_IVAR_$_DADeviceRegistry._videoData
- _OBJC_IVAR_$_DADeviceRegistryInfo._videoData
- _OBJC_IVAR_$_DAExtension._bluetoothRestorationID
- _OBJC_IVAR_$_DAExtensionSession._appContext
- _OBJC_IVAR_$_DAExtensionSessionConfiguration._bluetoothRestorationID
- _OBJC_IVAR_$_DAIncomingMessage._expiresAt
- _OBJC_IVAR_$_DAIncomingMessage._featureID
- _OBJC_IVAR_$_DAIncomingMessage._messageID
- _OBJC_IVAR_$_DAIncomingMessage._payloadVersion
- _OBJC_IVAR_$_DAOutgoingMessage._expiresAt
- _OBJC_IVAR_$_DAOutgoingMessage._featureID
- _OBJC_IVAR_$_DAOutgoingMessage._messageID
- _OBJC_IVAR_$_DAOutgoingMessage._payloadVersion
- _OBJC_IVAR_$_DASession._activateCalled
- _OBJC_IVAR_$_DASession._deviceMap
- _OBJC_IVAR_$_DASession._dispatchQueue
- _OBJC_IVAR_$_DASession._invalidateCalled
- _OBJC_IVAR_$_DASession._invalidateDone
- _OBJC_IVAR_$_DASession._xpcCnx
- _OBJC_IVAR_$_DASession._xpcListenerEndpoint
- __OBJC_$_CLASS_PROP_LIST_DAIncomingMessage
- __OBJC_$_CLASS_PROP_LIST_DAOutgoingMessage
- __OBJC_CLASS_PROTOCOLS_$_DAIncomingMessage
- __OBJC_CLASS_PROTOCOLS_$_DAOutgoingMessage
- ___21-[DAExtension launch]_block_invoke
- ___21-[DAExtension launch]_block_invoke_2
- ___21-[DAExtension resume]_block_invoke
- ___21-[DAExtension resume]_block_invoke_2
- ___23-[DASession invalidate]_block_invoke.cold.1
- ___28-[DAExtensionSession launch]_block_invoke
- ___28-[DAExtensionSession resume]_block_invoke
- ___29-[DAExtensionSession suspend]_block_invoke
- ___30-[DASession _ensureXPCStarted]_block_invoke
- ___31-[DAExtension _startExtension:]_block_invoke
- ___31-[DAExtension _startExtension:]_block_invoke.cold.1
- ___31-[DAExtensionSession terminate]_block_invoke
- ___31-[DASession _activateXPCStart:]_block_invoke
- ___35-[DASession _activateXPCCompleted:]_block_invoke
- ___35-[DASession _activateXPCCompleted:]_block_invoke_2
- ___40-[DAExtensionCapability _activateDirect]_block_invoke_2
- ___40-[DAExtensionCapability _activateDirect]_block_invoke_2.cold.1
- ___40-[DAExtensionCapability _activateDirect]_block_invoke_3
- ___40-[DAExtensionCapability _activateDirect]_block_invoke_3.cold.1
- ___40-[DAExtensionCapability _activateDirect]_block_invoke_3.cold.2
- ___40-[DAExtensionCapability _activateDirect]_block_invoke_3.cold.3
- ___40-[DAExtensionCapability _activateDirect]_block_invoke_3.cold.4
- ___40-[DAExtensionCapability _activateDirect]_block_invoke_4
- ___40-[DAExtensionCapability _activateDirect]_block_invoke_5
- ___42-[DAExtensionCapability _startCapability:]_block_invoke
- ___42-[DAExtensionCapability _startCapability:]_block_invoke.cold.1
- ___43-[DAExtension launchCapabilitiesWithFlags:]_block_invoke
- ___43-[DAExtension launchCapabilitiesWithFlags:]_block_invoke_2
- ___43-[DAExtension launchCapabilitiesWithFlags:]_block_invoke_2.cold.1
- ___43-[DAExtension resumeCapabilitiesWithFlags:]_block_invoke
- ___43-[DAExtension resumeCapabilitiesWithFlags:]_block_invoke_2
- ___43-[DAExtension resumeCapabilitiesWithFlags:]_block_invoke_2.cold.1
- ___44-[DAExtension initWithDevice:identity:type:]_block_invoke
- ___44-[DAExtension suspendCapabilitiesWithFlags:]_block_invoke
- ___48-[DAExtension _extensionEnsureStartedWithError:]_block_invoke_2
- ___48-[DAExtension _extensionEnsureStartedWithError:]_block_invoke_3
- ___48-[DAExtension _extensionEnsureStartedWithError:]_block_invoke_4
- ___52-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke
- ___52-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke.cold.1
- ___52-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke_2
- ___52-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke_2.cold.1
- ___52-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke_3
- ___52-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke_3.cold.1
- ___52-[DASession _getDevicesCompleted:completionHandler:]_block_invoke
- ___55-[DASession _getPartialIPsCompleted:completionHandler:]_block_invoke
- ___57-[DAExtension _capabilitiesEnsureStartedWithFlags:error:]_block_invoke_3.cold.1
- ___62+[DAExtensionSession bluetoothRestorationIDForBundleID:error:]_block_invoke
- ___62+[DAExtensionSession launchExtensionWithBundle:extensionType:]_block_invoke
- ___62+[DAExtensionSession resumeExtensionWithBundle:extensionType:]_block_invoke
- ___62-[DASession _getAuthorizedDevicesCompleted:completionHandler:]_block_invoke
- ___63+[DAExtensionSession suspendExtensionWithBundle:extensionType:]_block_invoke
- ___64-[DASession _getBluetoothAccessInfoCompleted:completionHandler:]_block_invoke
- ___88+[DAExtensionSession suspendExtensionWithBundle:extensionType:extensionCapabilityFlags:]_block_invoke
- ___block_descriptor_40_e8_32r_e48_v32?0"NSString"8"DADeviceAppAccessInfo"16^B24lr32l8
- ___block_descriptor_48_e8_32s40r_e46_v24?0"_EXCapabilityHostSession"8"NSError"16ls32l8r40l8
- ___block_literal_global.146
- ___block_literal_global.162
- ___block_literal_global.166
- ___block_literal_global.169
- ___block_literal_global.182
- ___block_literal_global.198
- ___block_literal_global.215
- ___block_literal_global.223
- ___block_literal_global.225
- ___block_literal_global.229
- ___block_literal_global.234
- ___block_literal_global.241
- ___block_literal_global.252
- ___block_literal_global.259
- ___swift_destroy_boxed_opaque_existential_0Tm
- _objc_msgSend$_capabilitiesEnsureStoppedWithFlags:error:
- _objc_msgSend$_getBluetoothAccessInfoCompleted:completionHandler:
- _objc_msgSend$_getDevicesCompleted:completionHandler:
- _objc_msgSend$_getPartialIPsCompleted:completionHandler:
- _objc_msgSend$_sandboxExtensionIssueMach:
- _objc_msgSend$_startCapability:
- _objc_msgSend$_startExtension:
- _objc_msgSend$_xpcListenerEvent:
- _objc_msgSend$appAccessInfoMap
- _objc_msgSend$bluetoothRestorationID
- _objc_msgSend$initWithIdentity:device:capabilityID:
- _objc_msgSend$initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoData:companionAppBundleID:companionAppIsOptional:
- _objc_msgSend$setBluetoothRestorationID:
- _objc_msgSend$setVideoData:
- _objc_msgSend$startExtension:bundleID:type:
- _objc_msgSend$videoData
CStrings:
+ "\n  %@"
+ "\""
+ "### AssertWithDuration: %@"
+ "### ConfigureExtensionProcess: %@"
+ "### ConfigureHostSession: %@"
+ "### ConfigureXPCConnection: %@"
+ "### DeriveInternetKey %@"
+ "### ExecuteCommand: %@, %@"
+ "### Extension XPC failed for receiveEvent: %@, %@"
+ "### Extension XPC failed to consume Internet Network Sharing token: %@, %@"
+ "### ExtensionEnsureStarted: failed with %@"
+ "### Failed to create sandbox token: Internet Network Sharing"
+ "### Failed to suspend extension process or capabilities: ExPrc %@"
+ "### Init failed with nil bundle identifier"
+ "### Init failed with nil config"
+ "### Init with invalid configuration: %@"
+ "### Init with nil configuration"
+ "### PeripheralUUIDFromRestorationID: %@"
+ "### ResumeWithError: %@"
+ "### RuntimeAssertion: %@, %@"
+ "### StartExtension: failed with nil XPC connection"
+ "%@ : %@"
+ "%lu key(s)"
+ "+[DAExtensionSession _executeCommandRuntimeAssertionSync:error:]_block_invoke"
+ "+[DAExtensionSession executeCommand:error:]_block_invoke"
+ "+[DAExtensionSession peripheralUUIDFromRestorationID:bundleID:peripheralUUID:error:]_block_invoke"
+ "-[DAExtension _assertWithDuration:]"
+ "-[DAExtension _assertWithDuration:]_block_invoke"
+ "-[DAExtension _assertionTimerFired]"
+ "-[DAExtension _capabilitiesEnsureStartedWithFlags:error:]_block_invoke_4"
+ "-[DAExtension _configureExtensionProcessWithError:]_block_invoke"
+ "-[DAExtension _configureExtensionProcessWithError:]_block_invoke_2"
+ "-[DAExtension _configureXPCConnectionWithError:]"
+ "-[DAExtension _configureXPCConnectionWithError:]_block_invoke"
+ "-[DAExtension _configureXPCConnectionWithError:]_block_invoke_2"
+ "-[DAExtension _configureXPCConnectionWithError:]_block_invoke_3"
+ "-[DAExtension _extensionEnsureStartedWithError:]_block_invoke"
+ "-[DAExtension _handleCapabilityActivated:process:]_block_invoke"
+ "-[DAExtension _sandboxExtensionIssueMach]_block_invoke_5"
+ "-[DAExtension _startExtension]"
+ "-[DAExtension _startExtension]_block_invoke"
+ "-[DAExtension _suspend]_block_invoke"
+ "-[DAExtension _terminateProcessIfNeeded]"
+ "-[DAExtension assertCapabilitiesWithFlags:duration:]_block_invoke"
+ "-[DAExtension assertCapabilitiesWithFlags:duration:]_block_invoke_2"
+ "-[DAExtension initWithConfiguration:]"
+ "-[DAExtension invalidateWithReason:]_block_invoke"
+ "-[DAExtensionCapability _configureHostSessionWithError:]"
+ "-[DAExtensionCapability _configureHostSessionWithError:]_block_invoke"
+ "-[DAExtensionCapability _configureHostSessionWithError:]_block_invoke_2"
+ "-[DAExtensionCapability _configureHostSessionWithError:]_block_invoke_3"
+ "-[DAExtensionCapability _configureXPCConnectionWithError:]_block_invoke"
+ "-[DAExtensionCapability _configureXPCConnectionWithError:]_block_invoke_2"
+ "-[DAExtensionCapability _configureXPCConnectionWithError:]_block_invoke_3"
+ "-[DAExtensionCapability _resumeWithError:]"
+ "-[DAExtensionCapability _resumeWithError:]_block_invoke"
+ "-[DAExtensionCapability _resumed]"
+ "-[DAExtensionCapability _sandboxExtensionIssueMach]"
+ "-[DAExtensionCapability _sandboxExtensionIssueMach]_block_invoke"
+ "-[DAExtensionCapability _sandboxExtensionIssueMach]_block_invoke_2"
+ "-[DAExtensionCapability _sandboxExtensionIssueMach]_block_invoke_3"
+ "-[DAExtensionCapability _startCapability]"
+ "-[DAExtensionCapability _startCapability]_block_invoke"
+ "-[DAExtensionCapability _suspend]"
+ "-[DAExtensionCapability initWithConfiguration:]"
+ "-[DASession _queue_XPCDispatchMessage:]"
+ "-[DASession _queue_XPCListenerEvent:]"
+ "-[DASession _queue_XPCReceivedDAEvent:]"
+ "-[DASession _queue_XPCReceivedMessage:]"
+ "-[DASession _queue_activateDirect]"
+ "-[DASession _queue_activateXPCCompleted:]"
+ "-[DASession _queue_activateXPCCompleted:]_block_invoke"
+ "-[DASession _queue_getAuthorizedDevicesCompleted:completionHandler:]"
+ "-[DASession _queue_getAuthorizedDevicesCompleted:completionHandler:]_block_invoke"
+ "-[DASession _queue_getBluetoothAccessInfoCompleted:completionHandler:]"
+ "-[DASession _queue_getBluetoothAccessInfoCompleted:completionHandler:]_block_invoke"
+ "-[DASession _queue_getDevicesCompleted:completionHandler:]"
+ "-[DASession _queue_getDevicesCompleted:completionHandler:]_block_invoke"
+ "-[DASession _queue_getPartialIPsCompleted:completionHandler:]"
+ "-[DASession _queue_getPartialIPsCompleted:completionHandler:]_block_invoke"
+ "-[DASession _queue_interrupted]"
+ "-[DASession _queue_invalidate]"
+ "-[DASession _queue_noteXPCConnectionInvalidated]"
+ "-[DASession _queue_reconnectIfNecessaryFromDaemonSpawn]"
+ "-[DASession _queue_reportEvent:]"
+ "-[DASession _queue_sendActivationXPCMessage]"
+ "-[DASession _queue_synthesizeDeviceEventsFromPrior:toNewDevices:]"
+ "-[DASession _queue_synthesizeDeviceEventsFromPrior:toNewDevices:]_block_invoke"
+ "-[DASession _queue_synthesizeDeviceEventsFromPrior:toNewDevices:]_block_invoke_2"
+ "-[DASession _startSpawnNotificationListener]"
+ "<%@: %p; friendlyName=%@; image2x=%@; image3x=%@; videoURL=%@; companionAppBundleID=%@; companionAppIsOptional=%@; supportedMode=%@>"
+ "<%@: %p; manufacturerID=%@; modelID=%@; friendlyName=%@; image2x=%@; image3x=%@; videoURL=%@; companionAppBundleID=%@; companionAppIsOptional=%@ upportedMode=%@>"
+ "@\"DACryptoInternetInfo\""
+ "@\"DAExtensionCommand\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "@20@0:8I16"
+ "@84@0:8@16@24@32@40@48@56@64B72@76"
+ "ActivateDirect extensionSession: %@"
+ "ActivateDirect xpcConnection: %@"
+ "AppBundleID '%@'"
+ "AppPrivateToken %@ (%lu bytes)"
+ "AssertWithDuration: %@"
+ "Assertion timer expired for %@"
+ "B48@0:8@16@24^@32^@40"
+ "Capability activated: %@"
+ "Capability already exists, adding to resume flags: %@"
+ "CapabilityID '%@'"
+ "ConfigureHostSession: Capability host session configuration: %@"
+ "ConfigureHostSession: calling sessionWithConfiguration"
+ "ConfigureHostSession: returning"
+ "ConfigureHostSession: session for %@: %@"
+ "ConfigureHostSession: sessionWithConfiguration completion called, inSession %@, inError %@"
+ "ConfigureHostSession: signaling semaphore"
+ "ConfigureHostSession: waiting on semaphore"
+ "ConfigureXPCConnection: %@"
+ "Created %@"
+ "CreatedAt"
+ "DAAccessoryMessage"
+ "DACryptoInternetInfo"
+ "DACryptoInternetInfo failed to init with nil dictionary"
+ "DACryptoInternetKeyRing"
+ "DACryptoInternetKeyRing failed to init with nil dictionary"
+ "DAExtensionCapabilityConfiguration"
+ "DAExtensionCommand"
+ "DAExtensionConfiguration"
+ "DAExtensionRuntimeAssertion"
+ "DAExtensionSession-AssertRuntime"
+ "DAExtensionSession-PeripheralUUIDFromRestorationID"
+ "DAExtensionXPCStartConfiguration"
+ "DAInternetKey-v1-"
+ "Daemon spawned — eager reconnect: %@"
+ "Data %@ (%ld bytes)"
+ "Device '%@'"
+ "Duration %f sec"
+ "EXPIRED"
+ "Ensuring capabilities are started: %@"
+ "ExCmd"
+ "ExPID"
+ "ExSes <%p> %@"
+ "ExtensionConfiguration interruptionHandler: %@"
+ "FeatureID '%@'"
+ "Internet"
+ "InternetKey"
+ "Invalidate with reason %@: %@"
+ "Issuing sandbox extension mach: Internet Network Sharing"
+ "Key %@ (%lu bytes)"
+ "KeyID"
+ "KeyID 0x%08X"
+ "Keys"
+ "MessageDeliveryStatus"
+ "MessageID %@"
+ "Messages %@"
+ "No"
+ "No XPC connection to suspend"
+ "PID '%d'"
+ "PeripheralID '%@'"
+ "ProcesStateUpdate: %@"
+ "Process was stopped with no active assertion: %@"
+ "ProcessStateUpdate: extension process stopped and invalidated"
+ "ProcessStateUpdate: resuming capability %@"
+ "ProcessStateUpdate: suspending XPC connection %@"
+ "ROTATION_ELIGIBLE"
+ "Received process state update for %@, BundleID '%@', PID %d: %@ (%ld) -> %@ (%ld)"
+ "Reporting event to capability: %@, PID %d"
+ "RestorationID '%@'"
+ "RestoreID '%@'"
+ "Resume: missing XPC connection for %@"
+ "Resume: missing extension session for %@"
+ "Resumed %@"
+ "Resumed XPC connection: %@"
+ "Resumed extension: %@"
+ "Resuming %@"
+ "RuntimeAssertion"
+ "Skip update – no assertion timer: %@"
+ "Start deviceaccessd spawn notification listener: %@"
+ "StartProcessMonitor: updated PID: %d"
+ "Started monitoring process for: %@"
+ "StateRestorationID '%@'"
+ "Status %ld"
+ "Suspend: capabilitiesMap %@"
+ "Suspend: no XPC connection to suspend for %@"
+ "Suspend: no process to suspend for %@"
+ "Suspend: suspending capabilities %@"
+ "Suspended XPC connection: %@"
+ "Suspended extension: %@"
+ "Synthesizing device %@ event for device: %@"
+ "Synthesizing device changed event for device: %@"
+ "Synthesizing device events: old %lu, new %lu"
+ "Synthesizing device lost event for device: %@"
+ "T@\"DACryptoInternetInfo\",C,N,V_internetCryptoInfo"
+ "T@\"DACryptoInternetInfo\",R,N"
+ "T@\"DADevice\",&,N,V_device"
+ "T@\"DADevice\",C,N,V_device"
+ "T@\"DAExtensionCommand\",&,N,V_activatingCommand"
+ "T@\"NSArray\",C,N,V_accessoryMessages"
+ "T@\"NSArray\",R,C,N"
+ "T@\"NSData\",C,N,V_appPrivateToken"
+ "T@\"NSData\",C,N,V_internetKey"
+ "T@\"NSDate\",&,N,V_createdAt"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSObject<OS_xpc_object>\",&,N"
+ "T@\"NSString\",&,N,V_stateRestorationID"
+ "T@\"NSString\",C,N,V_capabilityID"
+ "T@\"NSString\",C,N,V_restorationID"
+ "T@\"NSString\",C,N,V_stateRestorationID"
+ "T@\"NSString\",C,N,V_supportedMode"
+ "T@\"NSString\",C,N,V_videoURL"
+ "T@\"NSString\",R,C,N,V_messageID"
+ "T@\"NSString\",R,C,N,V_stateRestorationID"
+ "T@\"NSString\",R,C,N,V_supportedMode"
+ "T@\"NSString\",R,C,N,V_videoURL"
+ "T@\"NSString\",R,N,V_bundleID"
+ "T@\"NSUUID\",C,N,V_messageID"
+ "T@\"NSUUID\",C,N,V_peripheralUUID"
+ "T@\"_EXExtensionIdentity\",&,N,V_extensionIdentity"
+ "T@?,C,N,V_activationHandler"
+ "TB,N"
+ "TB,N,V_alwaysRunningOverride"
+ "TI,N,V_keyID"
+ "TQ,N,V_activateReason"
+ "TQ,N,V_transportType"
+ "TQ,R,N,V_type"
+ "Td,N,V_duration"
+ "Terminating process for %@"
+ "Tq,N,V_deliveryStatus"
+ "Transport %@"
+ "Valid %@"
+ "Version1"
+ "XPCConnection interruptionHandler: %@"
+ "XPCConnection invalidationHandler: %@"
+ "Yes"
+ "_EXCapabilityHostSessionInvalidationHandler: %@"
+ "_accessoryMessages"
+ "_activateReason"
+ "_activatingCommand"
+ "_activationHandler"
+ "_alwaysRunningOverride"
+ "_appPrivateToken"
+ "_assertWithDuration:"
+ "_assertionExpiration"
+ "_assertionTimer"
+ "_assertionTimerFired"
+ "_configureExtensionProcessWithError:"
+ "_configureHostSessionWithError:"
+ "_configureXPCConnectionWithError:"
+ "_createdAt"
+ "_deliveryStatus"
+ "_duration"
+ "_executeCommandRuntimeAssertionSync:error:"
+ "_handleCapabilityActivated:process:"
+ "_instanceIdentifier"
+ "_internetCryptoInfo"
+ "_internetKey"
+ "_invalidateAssertionTimer"
+ "_keyID"
+ "_keys"
+ "_peripheralUUID"
+ "_queue_XPCConnectionAccept:"
+ "_queue_XPCDispatchMessage:"
+ "_queue_XPCListenerEvent:"
+ "_queue_XPCReceivedDAEvent:"
+ "_queue_XPCReceivedMessage:"
+ "_queue_activateCalled"
+ "_queue_activateDirect"
+ "_queue_activateXPCCompleted:"
+ "_queue_ensureXPCStarted"
+ "_queue_getAuthorizedDevicesCompleted:completionHandler:"
+ "_queue_getBluetoothAccessInfoCompleted:completionHandler:"
+ "_queue_getDevicesCompleted:completionHandler:"
+ "_queue_getPartialIPsCompleted:completionHandler:"
+ "_queue_hasEverSetDeviceMap"
+ "_queue_interrupted"
+ "_queue_invalidate"
+ "_queue_invalidateCalled"
+ "_queue_invalidateDone"
+ "_queue_noteXPCConnectionInvalidated"
+ "_queue_reconnectIfNecessaryFromDaemonSpawn"
+ "_queue_reportEvent:"
+ "_queue_reportEventType:"
+ "_queue_requiresActivation"
+ "_queue_sendActivationXPCMessage"
+ "_queue_setupXPCConnectionIfNecessary"
+ "_queue_spawnNotifyToken"
+ "_queue_synthesizeDeviceEventsFromPrior:toNewDevices:"
+ "_queue_xpcCnx"
+ "_queue_xpcListenerEndpoint"
+ "_restorationID"
+ "_resumeWithError:"
+ "_resumed"
+ "_startCapability"
+ "_startExtension"
+ "_startSpawnNotificationListener"
+ "_stateRestorationID"
+ "_supportedMode"
+ "_syncSelf_deferReconnect"
+ "_syncSelf_deviceMap"
+ "_terminateProcessIfNeeded"
+ "_transportType"
+ "_videoURL"
+ "acMs"
+ "accessoryMessages"
+ "activateReason"
+ "activatingCommand"
+ "activationHandler"
+ "addIndex:"
+ "addKey:"
+ "alwaysRunningOverride"
+ "apTn"
+ "appPrivateToken"
+ "assertCapabilitiesWithFlags:duration:"
+ "assertWithDuration:"
+ "cF"
+ "changed"
+ "com.apple.deviceaccess.spawn"
+ "com.apple.media-device-discovery.network-client"
+ "createdAt"
+ "currentKey"
+ "dS"
+ "dateByAddingTimeInterval:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "decodeInt32ForKey:"
+ "deferReconnect"
+ "deliveryStatus"
+ "deriveInternetKeyWithCryptoInfo:error:"
+ "drASM"
+ "duration"
+ "either device or peripheralUUID must be set: %@"
+ "encodeInt32:forKey:"
+ "enumerateObjectsUsingBlock:"
+ "exAI"
+ "exCmd"
+ "exCmdTy"
+ "exMDS"
+ "exMID"
+ "executeCommand:error:"
+ "extension is missing capability IDs"
+ "extension process make XPC connection failed with %@"
+ "extension process make XPC connection rturned nil"
+ "failed to create XPC connection"
+ "failed to create host session"
+ "failed to derive internet key for "
+ "firstObject"
+ "found"
+ "icCA"
+ "icID"
+ "icKID"
+ "icKey"
+ "initWithBundleID:peripheralUUID:"
+ "initWithCapacity:"
+ "initWithDevice:accessoryMessages:"
+ "initWithDevice:capabilityFlags:"
+ "initWithIdentifier:internetKey:"
+ "initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoURL:companionAppBundleID:companionAppIsOptional:supportedModes:"
+ "initWithMessageID:"
+ "initWithStateRestorationID:"
+ "initWithType:"
+ "insertObject:atIndex:"
+ "internetCryptoInfo"
+ "internetKey"
+ "invalid bundle identifier"
+ "invalid command type"
+ "invalid state restoration identifier"
+ "isRotationEligible"
+ "kTCCServiceAudioAccessoryHeadTrackData"
+ "keyForKeyID:"
+ "keyID"
+ "make xpc connection failed with %@"
+ "nil extension host session"
+ "nil extension process"
+ "no reply"
+ "numberWithUnsignedInt:"
+ "peripheralUUID"
+ "peripheralUUIDFromRestorationID:bundleID:peripheralUUID:error:"
+ "process"
+ "purgeExpiredKeys"
+ "removeObjectsAtIndexes:"
+ "requires non-nil peripheral UUID"
+ "restorationID"
+ "resumeWithError:"
+ "session with configuration failed: %@"
+ "session with configuration returned nil session"
+ "setAccessoryMessages:"
+ "setActivateReason:"
+ "setActivatingCommand:"
+ "setActivationHandler:"
+ "setAlwaysRunningOverride:"
+ "setAppPrivateToken:"
+ "setCapabilityID:"
+ "setCreatedAt:"
+ "setDeferReconnect:"
+ "setDeliveryStatus:"
+ "setDevice:"
+ "setDuration:"
+ "setInternetCryptoInfo:"
+ "setInternetKey:"
+ "setKeyID:"
+ "setPeripheralUUID:"
+ "setRestorationID:"
+ "setStateRestorationID:"
+ "setSupportedMode:"
+ "setTransportType:"
+ "setVideoURL:"
+ "startWithConfiguration:"
+ "stateRestorationID"
+ "supportedMode"
+ "suspendWithError:"
+ "tT"
+ "timeIntervalSinceNow"
+ "timeIntervalSinceReferenceDate"
+ "trRId"
+ "transportType"
+ "v12@?0i8"
+ "v24@0:8@\"DAExtensionXPCStartConfiguration\"16"
+ "v24@?0@\"DAExtensionCapability\"8@\"_EXExtensionProcess\"16"
+ "v32@0:8Q16d24"
+ "v32@?0@\"DACryptoInternetInfo\"8Q16^B24"
+ "valid"
+ "videoURL"
- "### Failed to get capability host session: %@"
- "### Init with nil bundle identifier"
- "### Launch: %@"
- "### Resume: %@"
- "### ResumeCapabilityWithFlag %@: %@"
- "### SessionWithConfiguration failed for %@: %@"
- "### StartExtension failed with nil XPC connection"
- "%@ releasing extension process assertion..."
- "-[DAExtension _capabilitiesEnsureStartedWithFlags:error:]_block_invoke_3"
- "-[DAExtension _extensionEnsureStartedWithError:]"
- "-[DAExtension _invalidated:]"
- "-[DAExtension _startExtension:]"
- "-[DAExtension _startExtension:]_block_invoke"
- "-[DAExtension initWithDevice:identity:type:]"
- "-[DAExtension launchCapabilitiesWithFlags:]_block_invoke"
- "-[DAExtension launchCapabilitiesWithFlags:]_block_invoke_2"
- "-[DAExtension launch]_block_invoke"
- "-[DAExtension launch]_block_invoke_2"
- "-[DAExtension resumeCapabilitiesWithFlags:]_block_invoke"
- "-[DAExtension resumeCapabilitiesWithFlags:]_block_invoke_2"
- "-[DAExtension resume]_block_invoke"
- "-[DAExtension resume]_block_invoke_2"
- "-[DAExtension suspendCapabilitiesWithFlags:]_block_invoke"
- "-[DAExtensionCapability _activateDirect]_block_invoke_2"
- "-[DAExtensionCapability _activateDirect]_block_invoke_3"
- "-[DAExtensionCapability _sandboxExtensionIssueMach:]"
- "-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke"
- "-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke_2"
- "-[DAExtensionCapability _sandboxExtensionIssueMach:]_block_invoke_3"
- "-[DAExtensionCapability _startCapability:]"
- "-[DAExtensionCapability _startCapability:]_block_invoke"
- "-[DAExtensionCapability initWithIdentity:device:capabilityID:]"
- "-[DASession _activateDirect]"
- "-[DASession _activateXPCCompleted:]"
- "-[DASession _activateXPCCompleted:]_block_invoke"
- "-[DASession _activateXPCStart:]"
- "-[DASession _getAuthorizedDevicesCompleted:completionHandler:]"
- "-[DASession _getAuthorizedDevicesCompleted:completionHandler:]_block_invoke"
- "-[DASession _getBluetoothAccessInfoCompleted:completionHandler:]"
- "-[DASession _getBluetoothAccessInfoCompleted:completionHandler:]_block_invoke"
- "-[DASession _getDevicesCompleted:completionHandler:]"
- "-[DASession _getDevicesCompleted:completionHandler:]_block_invoke"
- "-[DASession _getPartialIPsCompleted:completionHandler:]"
- "-[DASession _getPartialIPsCompleted:completionHandler:]_block_invoke"
- "-[DASession _interrupted]"
- "-[DASession _invalidated]"
- "-[DASession _reportEvent:]"
- "-[DASession _xpcListenerEvent:]"
- "-[DASession _xpcReceivedDAEvent:]"
- "-[DASession _xpcReceivedMessage:]"
- "-[DASession invalidate]_block_invoke"
- "-[DASession xpcReceivedMessage:]"
- "<%@: %@, messageID=%@, destinationDeviceID=%@, featureID=%@>"
- "<%@: %@, messageID=%@, sourceDeviceID=%@, featureID=%@>"
- "<%@: %p; friendlyName=%@; image2x=%@; image3x=%@; video=%@; companionAppBundleID=%@; companionAppIsOptional=%@>"
- "<%@: %p; manufacturerID=%@; modelID=%@; friendlyName=%@; image2x=%@; image3x=%@; video=%@; companionAppBundleID=%@; companionAppIsOptional=%@>"
- "@76@0:8@16@24@32@40@48@56@64B72"
- "ActivateExtension %@"
- "Capability host configuration invalidated with identity: %@"
- "Capability host session configuration: %@"
- "Capability host session for %@: %@"
- "CapibilityID '%@' : SessionID '%@'"
- "Created: %@"
- "Creating DAExtensionCapability..."
- "DASession-getBTRestoreID"
- "DASession-launchExtension"
- "DASession-resumeExtension"
- "DASession-suspendExtension"
- "ExBtRID"
- "ExLa"
- "ExRes"
- "ExSusp"
- "ExTer"
- "Extension XPC start failed with %@"
- "Invalidated %@, XPC connection ended: PID %d"
- "Killing process for %@"
- "Launching: %@"
- "Received process state update for %@, bundleID '%@', PID %d: %@ (%ld) -> %@ (%ld)"
- "Resume: %@"
- "Resuming capability with flag: %@"
- "Started monitoring %@ process with PID: %d"
- "Suspending capability %@ on %@"
- "T@\"NSData\",C,N,V_videoData"
- "T@\"NSData\",R,C,N,V_videoData"
- "T@\"NSString\",C,N,V_bluetoothRestorationID"
- "T@\"NSString\",C,N,V_messageID"
- "_bluetoothRestorationID"
- "_getBluetoothAccessInfoCompleted:completionHandler:"
- "_getDevicesCompleted:completionHandler:"
- "_getPartialIPsCompleted:completionHandler:"
- "_invalidated:"
- "_sandboxExtensionIssueMach:"
- "_startCapability:"
- "_startExtension:"
- "_videoData"
- "bluetoothRestorationID"
- "bluetoothRestorationIDForBundleID:error:"
- "btRId"
- "btRestoreID '%@'"
- "extension is missing capabilities"
- "initWithBluetoothRestorationID:"
- "initWithDevice:identity:type:"
- "initWithIdentity:device:capabilityID:"
- "initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoData:companionAppBundleID:companionAppIsOptional:"
- "launch"
- "launchCapabilitiesWithFlags:"
- "launchExtensionWithBundle:extensionType:"
- "pid '%d'"
- "resumeCapabilitiesWithFlags:"
- "resumeExtensionWithBundle:extensionType:"
- "setBluetoothRestorationID:"
- "setVideoData:"
- "suspendCapabilitiesWithFlags:"
- "suspendExtensionWithBundle:extensionType:"
- "suspendExtensionWithBundle:extensionType:extensionCapabilityFlags:"
- "terminate"
- "v1"
- "v32@0:8@16q24"
- "v40@0:8@16q24Q32"
- "videoData"

```
