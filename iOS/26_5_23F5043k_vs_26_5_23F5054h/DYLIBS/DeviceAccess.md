## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

```diff

-325.7.1.1.0
-  __TEXT.__text: 0x52100
-  __TEXT.__auth_stubs: 0x1600
-  __TEXT.__objc_methlist: 0x4454
-  __TEXT.__const: 0x688
-  __TEXT.__cstring: 0x9933
-  __TEXT.__gcc_except_tab: 0x1064
-  __TEXT.__constg_swiftt: 0x3d8
-  __TEXT.__swift5_typeref: 0x258
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_types: 0x1c
+325.12.1.0.0
+  __TEXT.__text: 0x556f4
+  __TEXT.__auth_stubs: 0x1640
+  __TEXT.__objc_methlist: 0x45bc
+  __TEXT.__const: 0x8e0
+  __TEXT.__cstring: 0x9d83
+  __TEXT.__gcc_except_tab: 0x12f8
+  __TEXT.__constg_swiftt: 0x3b8
+  __TEXT.__swift5_typeref: 0x264
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_reflstr: 0x138
+  __TEXT.__swift5_fieldmd: 0x174
+  __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__swift5_reflstr: 0x128
-  __TEXT.__swift5_fieldmd: 0x164
   __TEXT.__oslogstring: 0x34d
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0x1428
-  __TEXT.__eh_frame: 0x5d8
-  __TEXT.__objc_classname: 0x6a4
-  __TEXT.__objc_methname: 0x86fb
-  __TEXT.__objc_methtype: 0xb86
-  __TEXT.__objc_stubs: 0x4820
-  __DATA_CONST.__got: 0x540
-  __DATA_CONST.__const: 0xd80
+  __TEXT.__unwind_info: 0x14d8
+  __TEXT.__eh_frame: 0x5c0
+  __TEXT.__objc_classname: 0x6b4
+  __TEXT.__objc_methname: 0x89c0
+  __TEXT.__objc_methtype: 0xc26
+  __TEXT.__objc_stubs: 0x4a20
+  __DATA_CONST.__got: 0x518
+  __DATA_CONST.__const: 0xe80
   __DATA_CONST.__objc_classlist: 0x1e8
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e70
+  __DATA_CONST.__objc_selrefs: 0x1f08
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0xb10
-  __AUTH_CONST.__const: 0x630
-  __AUTH_CONST.__cfstring: 0x3420
-  __AUTH_CONST.__objc_const: 0x7bb8
+  __AUTH_CONST.__auth_got: 0xb30
+  __AUTH_CONST.__const: 0x6b0
+  __AUTH_CONST.__cfstring: 0x34a0
+  __AUTH_CONST.__objc_const: 0x7e08
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xb60
-  __AUTH.__data: 0x290
-  __DATA.__objc_ivar: 0x6c4
-  __DATA.__data: 0xc30
+  __AUTH.__data: 0x250
+  __DATA.__objc_ivar: 0x6f8
+  __DATA.__data: 0xc48
   __DATA.__bss: 0x2e0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x780

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FB52EE9F-506E-3E7A-8F43-E372B6A1C9D0
-  Functions: 2227
-  Symbols:   6312
-  CStrings:  3632
+  UUID: FAD0DBA1-9ED2-351E-B030-FA7FD38A1377
+  Functions: 2283
+  Symbols:   6441
+  CStrings:  3714
 
Symbols:
+ -[DABluetoothPairingInfo initWithBluetoothIdentifier:pairedCTKD:appConfirmsAuth:pairingRequired:btSCPairing:pairingType:]
+ -[DACryptoInfo setSupportedTransports:]
+ -[DACryptoInfo supportedTransports]
+ -[DACryptoInternetInfo initWithIdentifier:internetKey:keyID:]
+ -[DACryptoInternetInfo setSupportedTransports:]
+ -[DACryptoInternetInfo supportedTransports]
+ -[DADevice capabilityInfoMapForBundleID:capabilityFlags:]
+ -[DADevice capabilityInfoMapForBundleID:capabilityFlags:].cold.1
+ -[DADevice capabilityInfoMapForBundleID:capabilityFlags:].cold.2
+ -[DADevice capabilityInfoMapForBundleID:capabilityFlags:].cold.3
+ -[DADeviceAccessoryServiceInfo capabilityFlag]
+ -[DADeviceAccessoryServiceInfo capabilityID]
+ -[DADeviceAccessoryServiceInfo setCapabilityFlag:]
+ -[DADeviceAccessoryServiceInfo setCapabilityID:]
+ -[DAEvent setEventType:]
+ -[DAExtension _capabilityStarted:process:]
+ -[DAExtension _capabilityStarted:process:].cold.1
+ -[DAExtension _capabilityStopped:invalidated:]
+ -[DAExtension _capabilityStopped:invalidated:].cold.1
+ -[DAExtension _modifyInternetSessionPolicy:]
+ -[DAExtension _modifyInternetSessionPolicy:].cold.1
+ -[DAExtension _modifyInternetSessionPolicy:].cold.2
+ -[DAExtension _modifyInternetSessionPolicy:].cold.3
+ -[DAExtension _modifyInternetSessionPolicy:].cold.4
+ -[DAExtension _modifyInternetSessionPolicy:].cold.5
+ -[DAExtension _modifyLocalNetworkSessionPolicy:]
+ -[DAExtension _modifyNetworkSessionPolicyIfNeeded:]
+ -[DAExtension _networkUUIDForExtension]
+ -[DAExtension _removeLocalNetworkSessionPolicy]
+ -[DAExtension _removeLocalNetworkSessionPolicy].cold.1
+ -[DAExtension _removeLocalNetworkSessionPolicy].cold.2
+ -[DAExtension _removeLocalNetworkSessionPolicy].cold.3
+ -[DAExtension _removeLocalNetworkSessionPolicy].cold.4
+ -[DAExtension capabilityStarted:process:]
+ -[DAExtension capabilityStopped:invalidated:]
+ -[DAExtension interrupted]
+ -[DAExtension xpcInterrupted]
+ -[DAExtension xpcInvalidated]
+ -[DAExtensionCapability initWithConfiguration:].cold.8
+ -[DAExtensionCapability xpcInterrupted]
+ -[DAExtensionCapability xpcInvalidated]
+ -[DAExtensionCapabilityConfiguration sessionUUID]
+ -[DAExtensionCapabilityConfiguration setSessionUUID:]
+ -[DAExtensionCommand clientPID]
+ -[DAExtensionCommand setClientPID:]
+ -[DAExtensionEventKeyExchange deliveryStatus]
+ -[DAExtensionEventKeyExchange setDeliveryStatus:]
+ -[DAExtensionSession clientPID]
+ -[DAExtensionSession setClientPID:]
+ -[_EXExtensionIdentity(DAInternal) capabilitiesNullable]
+ GCC_except_table0
+ GCC_except_table104
+ GCC_except_table110
+ GCC_except_table114
+ GCC_except_table26
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table42
+ GCC_except_table45
+ GCC_except_table55
+ GCC_except_table56
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table75
+ GCC_except_table79
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table9
+ _CUPrintPID
+ _DAEnumerateFlagsWithDescriptors
+ _DAExtensionActivateReasonToString
+ _DAMessageNotificationsOutgoingExpirationInterval
+ _DASupportedTransportFlagsToString
+ _OBJC_CLASS_$__EXExtensionIdentity
+ _OBJC_IVAR_$_DACryptoInfo._supportedTransports
+ _OBJC_IVAR_$_DACryptoInternetInfo._supportedTransports
+ _OBJC_IVAR_$_DADeviceAccessoryServiceInfo._capabilityFlag
+ _OBJC_IVAR_$_DADeviceAccessoryServiceInfo._capabilityID
+ _OBJC_IVAR_$_DAExtension._capabilitesInvalidated
+ _OBJC_IVAR_$_DAExtension._networkExtensionID
+ _OBJC_IVAR_$_DAExtension._networkPolicySession
+ _OBJC_IVAR_$_DAExtension._pendingProcessState
+ _OBJC_IVAR_$_DAExtension._restartPending
+ _OBJC_IVAR_$_DAExtension._xpcSuspended
+ _OBJC_IVAR_$_DAExtensionCapability._xpcSuspended
+ _OBJC_IVAR_$_DAExtensionCapabilityConfiguration._sessionUUID
+ _OBJC_IVAR_$_DAExtensionCommand._clientPID
+ _OBJC_IVAR_$_DAExtensionEventKeyExchange._deliveryStatus
+ _OBJC_IVAR_$_DAExtensionSession._clientPID
+ __OBJC_$_CATEGORY_INSTANCE_METHODS__EXExtensionIdentity_$_DAInternal
+ __OBJC_$_CATEGORY__EXExtensionIdentity_$_DAInternal
+ ___26-[DAExtension interrupted]_block_invoke
+ ___27-[DAExtension _interrupted]_block_invoke
+ ___29-[DAExtension xpcInterrupted]_block_invoke
+ ___29-[DAExtension xpcInterrupted]_block_invoke.cold.1
+ ___29-[DAExtension xpcInvalidated]_block_invoke
+ ___39-[DAExtension _networkUUIDForExtension]_block_invoke
+ ___39-[DAExtensionCapability xpcInterrupted]_block_invoke
+ ___39-[DAExtensionCapability xpcInvalidated]_block_invoke
+ ___41-[DAExtension capabilityStarted:process:]_block_invoke
+ ___45-[DAExtension capabilityStopped:invalidated:]_block_invoke
+ ___46-[DAExtension _capabilityStopped:invalidated:]_block_invoke
+ ___48-[DAExtension _modifyLocalNetworkSessionPolicy:]_block_invoke
+ ___48-[DAExtension _modifyLocalNetworkSessionPolicy:]_block_invoke.cold.1
+ ___DAExtensionCapabilityFlagsFromString_block_invoke
+ ___DAExtensionCapabilityFlagsToTCCStrings_block_invoke
+ ___block_descriptor_48_e8_32r_e21_v20?0C8"NSString"12lr32l8
+ ___block_descriptor_48_e8_32s40r_e21_v20?0C8"NSString"12ls32l8r40l8
+ ___block_descriptor_49_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_literal_global.218
+ ___swift_memcpy4_4
+ ___swift_noop_void_return
+ _objc_msgSend$_capabilityStarted:process:
+ _objc_msgSend$_capabilityStopped:invalidated:
+ _objc_msgSend$_modifyInternetSessionPolicy:
+ _objc_msgSend$_modifyLocalNetworkSessionPolicy:
+ _objc_msgSend$_modifyNetworkSessionPolicyIfNeeded:
+ _objc_msgSend$_networkUUIDForExtension
+ _objc_msgSend$_removeLocalNetworkSessionPolicy
+ _objc_msgSend$accessoryServicesInternalMap
+ _objc_msgSend$capabilities
+ _objc_msgSend$capabilitiesNullable
+ _objc_msgSend$capabilityInfoMapForBundleID:capabilityFlags:
+ _objc_msgSend$capabilityStarted:process:
+ _objc_msgSend$capabilityStopped:invalidated:
+ _objc_msgSend$effectivePID:
+ _objc_msgSend$getDevicesWithFlags:appID:error:
+ _objc_msgSend$initWithBluetoothIdentifier:pairedCTKD:appConfirmsAuth:pairingRequired:btSCPairing:
+ _objc_msgSend$initWithIdentifier:internetKey:keyID:
+ _objc_msgSend$interrupted
+ _objc_msgSend$sessionUUID
+ _objc_msgSend$setSessionUUID:
+ _objc_msgSend$setSupportedTransports:
+ _objc_msgSend$supportedTransports
+ _objc_msgSend$xpcInterrupted
+ _objc_msgSend$xpcInvalidated
+ _symbolic _____ So16os_unfair_lock_sV
+ _symbolic _____ s6UInt32V
+ _symbolic _____Sg 9CryptoKit4HPKEO6SenderV
+ _symbolic _____ySDySS_____GG 2os21OSAllocatedUnfairLockV 12DeviceAccess15DACryptoSession33_5AB05284E0EF12DCB3E81D39A96118B8LLC
+ _symbolic _____ySDySS_____G_____G s13ManagedBufferCsRi__rlE 12DeviceAccess15DACryptoSession33_5AB05284E0EF12DCB3E81D39A96118B8LLC So16os_unfair_lock_sV
+ _type_layout_string So16os_unfair_lock_sV
- -[DACryptoInfo accessoryEncapsulatedKey]
- -[DACryptoInfo setAccessoryEncapsulatedKey:]
- -[DACryptoInternetInfo initWithIdentifier:internetKey:]
- -[DAExtension _handleCapabilityActivated:process:]
- -[DAExtension _handleCapabilityInterrupted:]
- -[DAExtension _handleCapabilityInvalidated:]
- -[DAExtensionCapability _suspend].cold.2
- GCC_except_table19
- GCC_except_table23
- GCC_except_table32
- GCC_except_table37
- GCC_except_table40
- GCC_except_table44
- GCC_except_table49
- GCC_except_table62
- GCC_except_table7
- GCC_except_table71
- GCC_except_table76
- _DACryptoInternetInfoDeriveKeyID
- _DAExtensionCapabilityFlagFromTCCString
- _OBJC_IVAR_$_DACryptoInfo._accessoryEncapsulatedKey
- _OBJC_IVAR_$_DAExtension._clientInvalidated
- ___44-[DAExtension _handleCapabilityInterrupted:]_block_invoke
- ___44-[DAExtension _handleCapabilityInterrupted:]_block_invoke_2
- ___44-[DAExtension _handleCapabilityInvalidated:]_block_invoke
- ___48-[DAExtension _configureXPCConnectionWithError:]_block_invoke_2.cold.1
- ___48-[DAExtension _configureXPCConnectionWithError:]_block_invoke_3.cold.1
- ___50-[DAExtension _handleCapabilityActivated:process:]_block_invoke
- ___50-[DAExtension _handleCapabilityActivated:process:]_block_invoke.cold.1
- ___51-[DAExtension _configureExtensionProcessWithError:]_block_invoke_2.cold.1
- ___56-[DAExtensionCapability _configureHostSessionWithError:]_block_invoke_2.cold.1
- ___56-[DAExtensionCapability _configureHostSessionWithError:]_block_invoke_3.cold.1
- ___57-[DAExtension _capabilitiesEnsureStartedWithFlags:error:]_block_invoke_4.cold.1
- ___58-[DAExtensionCapability _configureXPCConnectionWithError:]_block_invoke_2.cold.1
- ___58-[DAExtensionCapability _configureXPCConnectionWithError:]_block_invoke_3.cold.1
- ___block_literal_global.216
- _kTCCServiceAccessoryAutomaticAudioSwitching
- _kTCCServiceAccessoryLiveActivities
- _kTCCServiceAccessoryNotifications
- _kTCCServiceAccessoryWiFiNetworkSharing
- _kTCCServiceAudioAccessoryHeadTrackData
- _objc_msgSend$_handleCapabilityActivated:process:
- _objc_msgSend$_handleCapabilityInterrupted:
- _objc_msgSend$_handleCapabilityInvalidated:
- _objc_msgSend$accessoryEncapsulatedKey
- _objc_msgSend$containsString:
- _objc_msgSend$getDevicesWithFlags:appID:
- _objc_msgSend$initWithIdentifier:internetKey:
- _objc_msgSend$setAccessoryEncapsulatedKey:
- _swift_beginAccess
- _swift_endAccess
- _symbolic SDySS_____G 12DeviceAccess15DACryptoSession33_5AB05284E0EF12DCB3E81D39A96118B8LLC
- _symbolic _____ 9CryptoKit4HPKEO6SenderV
- _symbolic _____Sg 9CryptoKit19XWingMLKEM768X25519O9PublicKeyV
- _symbolic _____So12DACryptoInfoCKc 9CryptoKit4HPKEO9RecipientV
CStrings:
+ "!"
+ "### CreateInternetRatchet %@"
+ "### Extension XPC failed to consume Networking Client token: %@, %@"
+ "### Failed to add extensionMatchPolicy for Internet extensionID: %@"
+ "### Failed to add localNetworkPolicy for Internet extensionID: %@"
+ "### Failed to create UUID from capability identifier for %@: %@"
+ "### Failed to create sandbox token: Networking Client"
+ "### Init failed with nil session UUID for capability %@"
+ "### ModifyLocalNetworkSessionPolicy: %@"
+ "### NetworkUUIDForExtension bundleID is nil"
+ "### OpenInternetMessage %@"
+ "### SealInternetMessage %@"
+ "### Skipping capability service info with missing ID for %@: %@"
+ "### XPC interrupted: %@"
+ "### XPC invalidated: %@"
+ "%@: %@, %@"
+ "-[DADevice capabilityInfoMapForBundleID:capabilityFlags:]"
+ "-[DAExtension _capabilityStarted:process:]"
+ "-[DAExtension _capabilityStopped:invalidated:]"
+ "-[DAExtension _configureExtensionProcessWithError:]"
+ "-[DAExtension _extensionEnsureStartedWithError:]"
+ "-[DAExtension _modifyInternetSessionPolicy:]"
+ "-[DAExtension _modifyLocalNetworkSessionPolicy:]"
+ "-[DAExtension _modifyLocalNetworkSessionPolicy:]_block_invoke"
+ "-[DAExtension _networkUUIDForExtension]"
+ "-[DAExtension _removeLocalNetworkSessionPolicy]"
+ "-[DAExtension xpcInterrupted]_block_invoke"
+ "-[DAExtension xpcInvalidated]_block_invoke"
+ "-[DAExtensionCapability xpcInterrupted]_block_invoke"
+ "-[DAExtensionCapability xpcInvalidated]_block_invoke"
+ "@\"NEPolicySession\""
+ "@36@0:8@16@24I32"
+ "@40@0:8@16^@24^@32"
+ "@48@0:8@16B24B28B32B36q40"
+ "@56@0:8@16@24@32^@40^@48"
+ "Adding NEPolicySession for Internet extensionID: %@"
+ "Adding NEPolicySession for LocalNetwork extensionID: %@"
+ "AssertWithExpiration for %@, '%@': %@"
+ "B24@0:8^@16"
+ "CapID %@"
+ "Capability started: %@"
+ "CapabilityInfoMap: bundleID mismatch: %@ vs %@"
+ "CapabilityInfoMap: capability flag mismatch: %@ vs %@"
+ "CapabilityInfoMap: no accessory services found for %@"
+ "CapabilityInfoMap: no capabilityID found for info: %@"
+ "Client %@"
+ "Connected"
+ "DAInternal"
+ "DAInternetKey-v1-A2D-"
+ "DAInternetKey-v1-D2A-"
+ "Enrolled"
+ "Ensure started: %@"
+ "Failed to apply session for Internet extensionID: %@"
+ "Failed to apply session for extensionID: %@"
+ "Failed to create Internet NEPolicy session for Internet extensionID: %@"
+ "Failed to create Internet NEPolicy session for invalid PID: %d"
+ "Failed to create LocalNetwork NEPolicy session for extensionID: %@"
+ "Found extension capabilities for %@: CapabilityIDs %@, %@"
+ "From %@"
+ "Initialized extension process: %@"
+ "Interrupted"
+ "Issuing sandbox extension mach: Networking Client"
+ "LocalNetwork"
+ "NEPolicySession Internet, app: %@, added: %@"
+ "NEPolicySession removed"
+ "NEPolicySession, app: %@, added: %@"
+ "Nil Internet extensionID"
+ "Nil LocalNetwork extensionID"
+ "NotConnected"
+ "Pending %@"
+ "ProcessStateUpdate: Running but pending Suspended, re-suspending: %@"
+ "ProcessStateUpdate: Suspended but pending Running, re-resuming: %@"
+ "PushService"
+ "Reason %@"
+ "Skipping capability with missing service info for %@: %@"
+ "Skipping unauthorized capability: %@"
+ "SupportedTransports"
+ "Suspending capabilities: %@"
+ "T@\"NSUUID\",C,N,V_sessionUUID"
+ "TQ,N,V_supportedTransports"
+ "Ti,N,V_clientPID"
+ "Tq,N,V_eventType"
+ "TransportBluetooth"
+ "TransportInternet"
+ "TransportLocalNetwork"
+ "TransportWiFiAware"
+ "Transports %@"
+ "XPC interrupted: %@"
+ "XPC invalidated: %@"
+ "_capabilitesInvalidated"
+ "_capabilityStarted:process:"
+ "_capabilityStopped:invalidated:"
+ "_clientPID"
+ "_modifyInternetSessionPolicy:"
+ "_modifyLocalNetworkSessionPolicy:"
+ "_modifyNetworkSessionPolicyIfNeeded:"
+ "_networkExtensionID"
+ "_networkPolicySession"
+ "_networkUUIDForExtension"
+ "_pendingProcessState"
+ "_removeLocalNetworkSessionPolicy"
+ "_restartPending"
+ "_supportedTransports"
+ "_xpcSuspended"
+ "appConfirmsAuth %s"
+ "btACA"
+ "btPR"
+ "btPSC"
+ "capabilities"
+ "capabilitiesNullable"
+ "capabilityInfoMapForBundleID:capabilityFlags:"
+ "capabilityStarted:process:"
+ "capabilityStopped:invalidated:"
+ "ciphertext too short for DAEncryptedMessage"
+ "clientPID"
+ "createInternetRatchetWithCryptoInfo:keyID:error:"
+ "effectivePID:"
+ "extension is missing capabilities"
+ "failed to configure XPC connection"
+ "failed to configure extension process"
+ "failed to configure extension session"
+ "failed to create internet ratchet for "
+ "failed with missing sender: "
+ "getDevicesWithFlags:appID:error:"
+ "initWithBluetoothIdentifier:pairedCTKD:appConfirmsAuth:pairingRequired:btSCPairing:pairingType:"
+ "initWithIdentifier:internetKey:keyID:"
+ "interrupted"
+ "no accessory key for "
+ "openInternetMessage:ratchetData:keyID:updatedRatchetData:error:"
+ "pairingRequired %s"
+ "sealInternetMessage:ratchetData:keyID:updatedRatchetData:error:"
+ "secureConnectionPairing %s"
+ "sessionUUID"
+ "setClientPID:"
+ "setEventType:"
+ "setSessionUUID:"
+ "setSupportedTransports:"
+ "startSession requires accessoryKey: "
+ "suTr"
+ "supportedTransports"
+ "v20@?0C8@\"NSString\"12"
+ "v28@0:8Q16B24"
+ "xpcInterrupted"
+ "xpcInvalidated"
- "### DeriveInternetKey %@"
- "### Extension XPC failed to consume Internet Network Sharing token: %@, %@"
- "### Failed to create sandbox token: Internet Network Sharing"
- "### StopSession %@"
- "-[DAExtension _capabilitiesEnsureStartedWithFlags:error:]_block_invoke_4"
- "-[DAExtension _configureExtensionProcessWithError:]_block_invoke_2"
- "-[DAExtension _configureXPCConnectionWithError:]_block_invoke_2"
- "-[DAExtension _configureXPCConnectionWithError:]_block_invoke_3"
- "-[DAExtension _handleCapabilityActivated:process:]_block_invoke"
- "-[DAExtensionCapability _configureHostSessionWithError:]_block_invoke_2"
- "-[DAExtensionCapability _configureHostSessionWithError:]_block_invoke_3"
- "-[DAExtensionCapability _configureXPCConnectionWithError:]_block_invoke_2"
- "-[DAExtensionCapability _configureXPCConnectionWithError:]_block_invoke_3"
- "AEnK %@ (%lu bytes)"
- "AccessoryEncapsulatedKey"
- "AssertWithDuration: %@"
- "Capability activated: %@"
- "ConfigureHostSession: Capability host session configuration: %@"
- "ConfigureHostSession: calling sessionWithConfiguration"
- "ConfigureHostSession: returning"
- "ConfigureHostSession: sessionWithConfiguration completion called, inSession %@, inError %@"
- "ConfigureHostSession: signaling semaphore"
- "ConfigureHostSession: waiting on semaphore"
- "DAInternetKey-v1-"
- "ExtensionConfiguration interruptionHandler: %@"
- "Found extension capabilities for %@: %@"
- "InvalidationHandler for capability %@"
- "Issuing sandbox extension mach: Internet Network Sharing"
- "KeyMaterial"
- "KeyReply"
- "Network"
- "No XPC connection to suspend"
- "ProcesStateUpdate: %@"
- "ProcessStateUpdate: extension process stopped and invalidated"
- "Resuming %@"
- "Suspend: capabilitiesMap %@"
- "Suspend: no XPC connection to suspend for %@"
- "Suspend: suspending capabilities %@"
- "T@\"NSData\",C,N,V_accessoryEncapsulatedKey"
- "Tq,R,N,V_eventType"
- "TransportLocal"
- "Updated crypto session for %@"
- "XPCConnection interruptionHandler: %@"
- "XPCConnection invalidationHandler: %@"
- "_EXCapabilityHostSessionInvalidationHandler: %@"
- "_accessoryEncapsulatedKey"
- "_handleCapabilityActivated:process:"
- "_handleCapabilityInterrupted:"
- "_handleCapabilityInvalidated:"
- "accessoryEncapsulatedKey"
- "ciAEK"
- "containsString:"
- "deriveInternetKeyWithCryptoInfo:error:"
- "extension is missing attributes"
- "extension is missing capability IDs"
- "failed to create recipient"
- "failed to derive internet key for "
- "failed with nil accessory encapsulated key for "
- "failed with nil private key for "
- "getDevicesWithFlags:appID:"
- "initWithIdentifier:internetKey:"
- "kTCCServiceAccessoryAutomaticAudioSwitching"
- "kTCCServiceAccessoryLiveActivities"
- "kTCCServiceAccessoryNotifications"
- "kTCCServiceAccessoryWiFiNetworkSharing"
- "kTCCServiceAudioAccessoryHeadTrackData"
- "setAccessoryEncapsulatedKey:"
- "updateSessionWithInfo:error:"

```
