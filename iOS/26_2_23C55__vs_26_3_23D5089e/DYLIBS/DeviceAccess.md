## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

```diff

-322.8.0.0.0
-  __TEXT.__text: 0x36488
-  __TEXT.__auth_stubs: 0x1280
-  __TEXT.__objc_methlist: 0x2f64
-  __TEXT.__cstring: 0x6902
-  __TEXT.__gcc_except_tab: 0x904
-  __TEXT.__const: 0x3e8
-  __TEXT.__swift5_typeref: 0x246
-  __TEXT.__constg_swiftt: 0x31c
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_types: 0x18
-  __TEXT.__oslogstring: 0x1dd
-  __TEXT.__swift5_reflstr: 0xd8
-  __TEXT.__swift5_fieldmd: 0xf4
-  __TEXT.__swift5_proto: 0x10
+323.4.1.0.0
+  __TEXT.__text: 0x3b688
+  __TEXT.__auth_stubs: 0x1530
+  __TEXT.__objc_methlist: 0x30e4
+  __TEXT.__cstring: 0x64c2
+  __TEXT.__gcc_except_tab: 0x8c8
+  __TEXT.__const: 0x5c8
+  __TEXT.__swift5_typeref: 0x258
+  __TEXT.__constg_swiftt: 0x3d0
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__swift5_mpenum: 0x14
+  __TEXT.__swift5_reflstr: 0x128
+  __TEXT.__swift5_fieldmd: 0x164
+  __TEXT.__oslogstring: 0x30d
+  __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0xce8
-  __TEXT.__eh_frame: 0x3a0
-  __TEXT.__objc_classname: 0x466
-  __TEXT.__objc_methname: 0x60a9
-  __TEXT.__objc_methtype: 0x9ba
-  __TEXT.__objc_stubs: 0x3320
-  __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0x9e8
-  __DATA_CONST.__objc_classlist: 0x160
+  __TEXT.__unwind_info: 0xd98
+  __TEXT.__eh_frame: 0x5b8
+  __TEXT.__objc_classname: 0x49d
+  __TEXT.__objc_methname: 0x6072
+  __TEXT.__objc_methtype: 0x977
+  __TEXT.__objc_stubs: 0x3100
+  __DATA_CONST.__got: 0x458
+  __DATA_CONST.__const: 0x9b8
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1640
+  __DATA_CONST.__objc_selrefs: 0x1608
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x108
-  __AUTH_CONST.__auth_got: 0x950
-  __AUTH_CONST.__const: 0x4f8
-  __AUTH_CONST.__cfstring: 0x2620
-  __AUTH_CONST.__objc_const: 0x5470
+  __DATA_CONST.__objc_superrefs: 0x118
+  __AUTH_CONST.__auth_got: 0xaa8
+  __AUTH_CONST.__const: 0x530
+  __AUTH_CONST.__cfstring: 0x2780
+  __AUTH_CONST.__objc_const: 0x5840
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH.__objc_data: 0x630
-  __AUTH.__data: 0x178
-  __DATA.__objc_ivar: 0x494
-  __DATA.__data: 0xab8
-  __DATA.__bss: 0x240
+  __AUTH.__objc_data: 0x6b0
+  __AUTH.__data: 0x288
+  __DATA.__objc_ivar: 0x4b4
+  __DATA.__data: 0xb50
+  __DATA.__bss: 0x2c0
+  __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__common: 0x8

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D9989777-222A-3519-8A77-539700D359CD
-  Functions: 1476
-  Symbols:   4324
-  CStrings:  2634
+  UUID: 4A878AD0-9DB1-32E3-98CC-2B68073FA9C3
+  Functions: 1555
+  Symbols:   4403
+  CStrings:  2644
 
Symbols:
+ +[DAEventExtension allocInitWithXPCObject:error:]
+ +[DAExtensionEventLifecycle supportsSecureCoding]
+ +[DAExtensionSessionConfiguration supportsSecureCoding]
+ -[DACryptoInfo accessoryEncapsulatedKey]
+ -[DACryptoInfo bluetoothIdentifier]
+ -[DACryptoInfo encapsulatedKey]
+ -[DACryptoInfo setAccessoryEncapsulatedKey:]
+ -[DACryptoInfo setBluetoothIdentifier:]
+ -[DACryptoInfo setEncapsulatedKey:]
+ -[DACryptoInfo setVersion:]
+ -[DACryptoInfo updateWithDACryptoInfo:]
+ -[DACryptoInfo version]
+ -[DAEventExtension extensionType]
+ -[DAEventExtension setExtensionType:]
+ -[DAExtension _invalidated].cold.3
+ -[DAExtension dispatchQueue]
+ -[DAExtension extensionIdentity]
+ -[DAExtension initWithDevice:identity:type:]
+ -[DAExtension initWithDevice:identity:type:].cold.1
+ -[DAExtension invalidationHandler]
+ -[DAExtension setDispatchQueue:]
+ -[DAExtension setInvalidationHandler:]
+ -[DAExtension setType:]
+ -[DAExtensionEventData accessoryService]
+ -[DAExtensionEventData capabilityFlags]
+ -[DAExtensionEventData destination]
+ -[DAExtensionEventData initWithDevice:data:capabilityFlag:]
+ -[DAExtensionEventData initWithDevice:data:service:]
+ -[DAExtensionEventData setDestination:]
+ -[DAExtensionEventKeyExchange cryptoInfo]
+ -[DAExtensionEventKeyExchange initWithEventType:device:cryptoInfo:]
+ -[DAExtensionEventKeyExchange setCryptoInfo:]
+ -[DAExtensionEventLifecycle descriptionWithLevel:]
+ -[DAExtensionEventLifecycle description]
+ -[DAExtensionEventLifecycle encodeWithCoder:]
+ -[DAExtensionEventLifecycle encodeWithXPCObject:]
+ -[DAExtensionEventLifecycle initWithCoder:]
+ -[DAExtensionEventLifecycle initWithCoder:].cold.1
+ -[DAExtensionEventLifecycle initWithDevice:eventType:extensionType:]
+ -[DAExtensionEventLifecycle initWithXPCObject:error:]
+ -[DAExtensionSession .cxx_destruct]
+ -[DAExtensionSession _activateDirect]
+ -[DAExtensionSession _activateDirect].cold.1
+ -[DAExtensionSession _activateXPCCompleted:]
+ -[DAExtensionSession _activateXPCStart:]
+ -[DAExtensionSession _activateXPCStart:].cold.1
+ -[DAExtensionSession _ensureXPCStarted]
+ -[DAExtensionSession _interrupted]
+ -[DAExtensionSession _interrupted].cold.1
+ -[DAExtensionSession _invalidated]
+ -[DAExtensionSession _invalidated].cold.1
+ -[DAExtensionSession _reportEvent:]
+ -[DAExtensionSession _reportEvent:].cold.1
+ -[DAExtensionSession _reportEventType:]
+ -[DAExtensionSession _xpcConnectionAccept:]
+ -[DAExtensionSession _xpcListenerEvent:]
+ -[DAExtensionSession _xpcListenerEvent:].cold.1
+ -[DAExtensionSession _xpcListenerEvent:].cold.2
+ -[DAExtensionSession _xpcReceivedDAExtensionEvent:]
+ -[DAExtensionSession _xpcReceivedDAExtensionEvent:].cold.1
+ -[DAExtensionSession _xpcReceivedDAExtensionEvent:].cold.2
+ -[DAExtensionSession _xpcReceivedMessage:]
+ -[DAExtensionSession _xpcReceivedMessage:].cold.1
+ -[DAExtensionSession activate]
+ -[DAExtensionSession clientID]
+ -[DAExtensionSession configuration]
+ -[DAExtensionSession descriptionWithLevel:]
+ -[DAExtensionSession description]
+ -[DAExtensionSession direct]
+ -[DAExtensionSession dispatchQueue]
+ -[DAExtensionSession encodeWithXPCObject:]
+ -[DAExtensionSession eventHandler]
+ -[DAExtensionSession initWithConfiguration:]
+ -[DAExtensionSession initWithConfiguration:].cold.1
+ -[DAExtensionSession initWithXPCObject:error:]
+ -[DAExtensionSession invalidate]
+ -[DAExtensionSession sendExtensionDataEvent:completionHandler:]
+ -[DAExtensionSession setClientID:]
+ -[DAExtensionSession setDirect:]
+ -[DAExtensionSession setDispatchQueue:]
+ -[DAExtensionSession setEventHandler:]
+ -[DAExtensionSession setXpcCnx:]
+ -[DAExtensionSession setXpcListenerEndpoint:]
+ -[DAExtensionSession xpcCnx]
+ -[DAExtensionSession xpcListenerEndpoint]
+ -[DAExtensionSession xpcReceivedMessage:]
+ -[DAExtensionSession xpcReceivedMessage:].cold.1
+ -[DAExtensionSession xpcReceivedMessage:].cold.2
+ -[DAExtensionSession xpcReceivedMessage:].cold.3
+ -[DAExtensionSessionConfiguration .cxx_destruct]
+ -[DAExtensionSessionConfiguration bundleID]
+ -[DAExtensionSessionConfiguration descriptionWithLevel:]
+ -[DAExtensionSessionConfiguration description]
+ -[DAExtensionSessionConfiguration device]
+ -[DAExtensionSessionConfiguration dispatchQueue]
+ -[DAExtensionSessionConfiguration encodeWithCoder:]
+ -[DAExtensionSessionConfiguration encodeWithXPCObject:]
+ -[DAExtensionSessionConfiguration initWithCoder:]
+ -[DAExtensionSessionConfiguration initWithCoder:].cold.1
+ -[DAExtensionSessionConfiguration initWithDevice:]
+ -[DAExtensionSessionConfiguration initWithDevice:].cold.1
+ -[DAExtensionSessionConfiguration initWithXPCObject:error:]
+ -[DAExtensionSessionConfiguration setBundleID:]
+ -[DAExtensionSessionConfiguration setDispatchQueue:]
+ GCC_except_table14
+ GCC_except_table24
+ GCC_except_table5
+ GCC_except_table6
+ _DACryptoSuiteVersionToString
+ _DAExtensionCapabilityFlagFromTCCString
+ _NSClassFromString
+ _OBJC_CLASS_$_DAExtensionEventLifecycle
+ _OBJC_CLASS_$_DAExtensionSession
+ _OBJC_CLASS_$_DAExtensionSessionConfiguration
+ _OBJC_IVAR_$_DACryptoInfo._accessoryEncapsulatedKey
+ _OBJC_IVAR_$_DACryptoInfo._bluetoothIdentifier
+ _OBJC_IVAR_$_DACryptoInfo._encapsulatedKey
+ _OBJC_IVAR_$_DACryptoInfo._version
+ _OBJC_IVAR_$_DAEventExtension._extensionType
+ _OBJC_IVAR_$_DAExtension._extensionConfiguration
+ _OBJC_IVAR_$_DAExtension._extensionIdentity
+ _OBJC_IVAR_$_DAExtension._extensionProcess
+ _OBJC_IVAR_$_DAExtension._invalidationHandler
+ _OBJC_IVAR_$_DAExtensionEventData._accessoryService
+ _OBJC_IVAR_$_DAExtensionEventData._capabilityFlags
+ _OBJC_IVAR_$_DAExtensionEventData._destination
+ _OBJC_IVAR_$_DAExtensionEventKeyExchange._cryptoInfo
+ _OBJC_IVAR_$_DAExtensionSession._activateCalled
+ _OBJC_IVAR_$_DAExtensionSession._appContext
+ _OBJC_IVAR_$_DAExtensionSession._clientID
+ _OBJC_IVAR_$_DAExtensionSession._configuration
+ _OBJC_IVAR_$_DAExtensionSession._direct
+ _OBJC_IVAR_$_DAExtensionSession._dispatchQueue
+ _OBJC_IVAR_$_DAExtensionSession._eventHandler
+ _OBJC_IVAR_$_DAExtensionSession._invalidateCalled
+ _OBJC_IVAR_$_DAExtensionSession._invalidateDone
+ _OBJC_IVAR_$_DAExtensionSession._xpcCnx
+ _OBJC_IVAR_$_DAExtensionSession._xpcEndpoint
+ _OBJC_IVAR_$_DAExtensionSession._xpcListener
+ _OBJC_IVAR_$_DAExtensionSession._xpcListenerEndpoint
+ _OBJC_IVAR_$_DAExtensionSessionConfiguration._bundleID
+ _OBJC_IVAR_$_DAExtensionSessionConfiguration._device
+ _OBJC_IVAR_$_DAExtensionSessionConfiguration._dispatchQueue
+ _OBJC_METACLASS_$_DAExtensionEventLifecycle
+ _OBJC_METACLASS_$_DAExtensionSession
+ _OBJC_METACLASS_$_DAExtensionSessionConfiguration
+ __DATA__TtC12DeviceAccessP33_5AB05284E0EF12DCB3E81D39A96118B815DACryptoSession
+ __IVARS__TtC12DeviceAccess18DACryptoKitManager
+ __IVARS__TtC12DeviceAccessP33_5AB05284E0EF12DCB3E81D39A96118B815DACryptoSession
+ __METACLASS_DATA__TtC12DeviceAccessP33_5AB05284E0EF12DCB3E81D39A96118B815DACryptoSession
+ __OBJC_$_CLASS_METHODS_DAExtensionEventLifecycle
+ __OBJC_$_CLASS_METHODS_DAExtensionSessionConfiguration
+ __OBJC_$_CLASS_PROP_LIST_DAExtensionSessionConfiguration
+ __OBJC_$_INSTANCE_METHODS_DAExtensionEventLifecycle
+ __OBJC_$_INSTANCE_METHODS_DAExtensionSession
+ __OBJC_$_INSTANCE_METHODS_DAExtensionSessionConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_DAExtensionSession
+ __OBJC_$_INSTANCE_VARIABLES_DAExtensionSessionConfiguration
+ __OBJC_$_PROP_LIST_DAExtensionSession
+ __OBJC_$_PROP_LIST_DAExtensionSessionConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_DAExtensionSession
+ __OBJC_CLASS_PROTOCOLS_$_DAExtensionSessionConfiguration
+ __OBJC_CLASS_RO_$_DAExtensionEventLifecycle
+ __OBJC_CLASS_RO_$_DAExtensionSession
+ __OBJC_CLASS_RO_$_DAExtensionSessionConfiguration
+ __OBJC_METACLASS_RO_$_DAExtensionEventLifecycle
+ __OBJC_METACLASS_RO_$_DAExtensionSession
+ __OBJC_METACLASS_RO_$_DAExtensionSessionConfiguration
+ ___27-[DAExtension reportEvent:]_block_invoke
+ ___30-[DAExtensionSession activate]_block_invoke
+ ___30-[DAExtensionSession activate]_block_invoke.cold.1
+ ___32-[DAExtensionSession invalidate]_block_invoke
+ ___32-[DAExtensionSession invalidate]_block_invoke.cold.1
+ ___39-[DAExtensionSession _ensureXPCStarted]_block_invoke
+ ___40-[DAExtensionSession _activateXPCStart:]_block_invoke
+ ___44-[DAExtension initWithDevice:identity:type:]_block_invoke
+ ___44-[DAExtensionSession _activateXPCCompleted:]_block_invoke
+ ___63-[DAExtensionSession sendExtensionDataEvent:completionHandler:]_block_invoke
+ ___63-[DAExtensionSession sendExtensionDataEvent:completionHandler:]_block_invoke.cold.1
+ ___63-[DAExtensionSession sendExtensionDataEvent:completionHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32r_e48_v32?0"NSString"8"DADeviceAppAccessInfo"16^B24lr32l8
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_memcpy24_8
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_stdlib_malloc_size
+ _bzero
+ _gLogCategory_DAExtensionSession
+ _get_enum_tag_for_layout_string So8DACryptoC12DeviceAccessE5ErrorO
+ _kTCCServiceAccessoryNotifications
+ _kTCCServiceAccessoryWiFiNetworkSharing
+ _malloc_size
+ _memmove
+ _objc_msgSend$_xpcReceivedDAExtensionEvent:
+ _objc_msgSend$accessoryEncapsulatedKey
+ _objc_msgSend$appAccessInfoMap
+ _objc_msgSend$ciphersuite
+ _objc_msgSend$encapsulatedKey
+ _objc_msgSend$initWithConfiguration:
+ _objc_msgSend$privateKey
+ _objc_msgSend$setAccessoryEncapsulatedKey:
+ _objc_msgSend$setCiphersuite:
+ _objc_msgSend$setEncapsulatedKey:
+ _objc_msgSend$setExtensionType:
+ _objc_msgSend$setVersion:
+ _objc_msgSend$version
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_cvw_enumFn_getEnumTag
+ _swift_endAccess
+ _swift_getObjectType
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _symbolic SDySS_____G 12DeviceAccess15DACryptoSession33_5AB05284E0EF12DCB3E81D39A96118B8LLC
+ _symbolic SS_______pt s5ErrorP
+ _symbolic So8DACryptoC
+ _symbolic _____ 12DeviceAccess15DACryptoSession33_5AB05284E0EF12DCB3E81D39A96118B8LLC
+ _symbolic _____ 9CryptoKit4HPKEO6SenderV
+ _symbolic _____ So20DACryptoSuiteVersionV
+ _symbolic _____ So8DACryptoC12DeviceAccessE5ErrorO
+ _symbolic _____Sg 9CryptoKit12SymmetricKeyV
+ _symbolic _____Sg 9CryptoKit3AESO3GCMO5NonceV
+ _symbolic _____Sg 9CryptoKit4HPKEO9RecipientV
+ _symbolic _____So12DACryptoInfoCKc 9CryptoKit4HPKEO9RecipientV
+ _symbolic _____ySS_____G s18_DictionaryStorageC 12DeviceAccess15DACryptoSession33_5AB05284E0EF12DCB3E81D39A96118B8LLC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _type_layout_string So8DACryptoC12DeviceAccessE5ErrorO
- -[DACryptoInfo info]
- -[DACryptoInfo setInfo:]
- -[DAExtension ekExtension]
- -[DAExtension initWithCoordinator:ekExtension:type:transportType:]
- -[DAExtension setEkExtension:]
- -[DAExtension transportType]
- -[DAExtensionCoordinator .cxx_destruct]
- -[DAExtensionCoordinator _activateDirect]
- -[DAExtensionCoordinator _activateExtension:]
- -[DAExtensionCoordinator _activateExtension:].cold.1
- -[DAExtensionCoordinator _activateExtension:].cold.2
- -[DAExtensionCoordinator _extensionActivatedWithType:transportType:]
- -[DAExtensionCoordinator _extensionEnsureStartedWithType:transportType:]
- -[DAExtensionCoordinator _extensionEnsureStartedWithType:transportType:].cold.1
- -[DAExtensionCoordinator _extensionEnsureStoppedWithType:transportType:]
- -[DAExtensionCoordinator _extensionInvalidatedWithType:transportType:]
- -[DAExtensionCoordinator _extensionInvalidatedWithType:transportType:].cold.1
- -[DAExtensionCoordinator _extensionInvalidatedWithType:transportType:].cold.2
- -[DAExtensionCoordinator _extensionShouldRunWithType:transportType:]
- -[DAExtensionCoordinator _extensionShouldRunWithType:transportType:].cold.1
- -[DAExtensionCoordinator _extensionShouldRunWithType:transportType:].cold.2
- -[DAExtensionCoordinator _extensionWithType:transportType:]
- -[DAExtensionCoordinator _findExtensionWithType:transportType:completion:]
- -[DAExtensionCoordinator _findExtensionWithType:transportType:completion:].cold.1
- -[DAExtensionCoordinator _findExtensionWithType:transportType:completion:].cold.2
- -[DAExtensionCoordinator _findExtensionWithType:transportType:completion:].cold.3
- -[DAExtensionCoordinator _findExtensionWithType:transportType:completion:].cold.4
- -[DAExtensionCoordinator _handleAccessoryTransportEvent:transportType:]
- -[DAExtensionCoordinator _handleAccessoryTransportInternetEvent:]
- -[DAExtensionCoordinator _handleAccessoryTransportInternetEvent:].cold.1
- -[DAExtensionCoordinator _handleAccessoryTransportInternetEvent:].cold.2
- -[DAExtensionCoordinator _handleAccessoryTransportLocalEvent:]
- -[DAExtensionCoordinator _handleAccessoryTransportLocalEvent:].cold.1
- -[DAExtensionCoordinator _handleAccessoryTransportLocalEvent:].cold.2
- -[DAExtensionCoordinator _handleEvent:type:transportType:]
- -[DAExtensionCoordinator _interrupted]
- -[DAExtensionCoordinator _interrupted].cold.1
- -[DAExtensionCoordinator _invalidateExtensions]
- -[DAExtensionCoordinator _invalidate]
- -[DAExtensionCoordinator _invalidate].cold.1
- -[DAExtensionCoordinator _invalidated]
- -[DAExtensionCoordinator _invalidated].cold.1
- -[DAExtensionCoordinator _performKeyExchange]
- -[DAExtensionCoordinator _reportEvent:]
- -[DAExtensionCoordinator _reportEvent:].cold.1
- -[DAExtensionCoordinator _reportEventToSessions:]
- -[DAExtensionCoordinator _reportEventType:]
- -[DAExtensionCoordinator _update]
- -[DAExtensionCoordinator _update].cold.1
- -[DAExtensionCoordinator _update].cold.2
- -[DAExtensionCoordinator activate]
- -[DAExtensionCoordinator addSession:]
- -[DAExtensionCoordinator addSession:].cold.1
- -[DAExtensionCoordinator bundleID]
- -[DAExtensionCoordinator descriptionWithLevel:]
- -[DAExtensionCoordinator description]
- -[DAExtensionCoordinator device]
- -[DAExtensionCoordinator dispatchQueue]
- -[DAExtensionCoordinator eventHandler]
- -[DAExtensionCoordinator getExtensionPidByType:transport:]
- -[DAExtensionCoordinator initWithDevice:bundleID:]
- -[DAExtensionCoordinator initWithDevice:bundleID:].cold.1
- -[DAExtensionCoordinator initWithDevice:bundleID:].cold.2
- -[DAExtensionCoordinator invalidateWithReason:]
- -[DAExtensionCoordinator invalidate]
- -[DAExtensionCoordinator removeSession:]
- -[DAExtensionCoordinator sessionSet]
- -[DAExtensionCoordinator setDispatchQueue:]
- -[DAExtensionCoordinator setEventHandler:]
- -[DAExtensionCoordinator update]
- -[DAExtensionEventData initWithDevice:data:key:]
- -[DAExtensionEventData key]
- -[DAExtensionEventData setKey:]
- -[DAExtensionEventKeyExchange bundleID]
- -[DAExtensionEventKeyExchange context]
- -[DAExtensionEventKeyExchange initWithDevice:publicKey:]
- -[DAExtensionEventKeyExchange initWithDevice:publicKey:context:]
- -[DAExtensionEventKeyExchange publicKey]
- -[DAExtensionEventKeyExchange setBundleID:]
- -[DAExtensionEventKeyExchange setContext:]
- -[DAExtensionEventKeyExchange setPublicKey:]
- GCC_except_table11
- GCC_except_table13
- GCC_except_table16
- GCC_except_table20
- _DAAccessoryTransportTypeToString
- _NSDataWithHex
- _OBJC_CLASS_$_DACryptoPrivate
- _OBJC_CLASS_$_DAExtensionCoordinator
- _OBJC_IVAR_$_DACryptoInfo._info
- _OBJC_IVAR_$_DAExtension._ekExtension
- _OBJC_IVAR_$_DAExtension._ekExtensionProcess
- _OBJC_IVAR_$_DAExtension._ekHostConfiguration
- _OBJC_IVAR_$_DAExtension._transportType
- _OBJC_IVAR_$_DAExtensionCoordinator._activateCalled
- _OBJC_IVAR_$_DAExtensionCoordinator._bundleID
- _OBJC_IVAR_$_DAExtensionCoordinator._device
- _OBJC_IVAR_$_DAExtensionCoordinator._dispatchQueue
- _OBJC_IVAR_$_DAExtensionCoordinator._eventHandler
- _OBJC_IVAR_$_DAExtensionCoordinator._extensionMap
- _OBJC_IVAR_$_DAExtensionCoordinator._invalidateCalled
- _OBJC_IVAR_$_DAExtensionCoordinator._invalidateDone
- _OBJC_IVAR_$_DAExtensionCoordinator._invalidateReason
- _OBJC_IVAR_$_DAExtensionCoordinator._relaunchExtensions
- _OBJC_IVAR_$_DAExtensionCoordinator._sessionAdded
- _OBJC_IVAR_$_DAExtensionCoordinator._sessionSet
- _OBJC_IVAR_$_DAExtensionEventData._key
- _OBJC_IVAR_$_DAExtensionEventKeyExchange._bundleID
- _OBJC_IVAR_$_DAExtensionEventKeyExchange._context
- _OBJC_IVAR_$_DAExtensionEventKeyExchange._publicKey
- _OBJC_METACLASS_$_DACryptoPrivate
- _OBJC_METACLASS_$_DAExtensionCoordinator
- __CLASS_METHODS_DACryptoPrivate
- __DATA_DACryptoPrivate
- __INSTANCE_METHODS_DACryptoPrivate
- __METACLASS_DATA_DACryptoPrivate
- __OBJC_$_INSTANCE_METHODS_DAExtensionCoordinator
- __OBJC_$_INSTANCE_VARIABLES_DAExtensionCoordinator
- __OBJC_$_PROP_LIST_DAExtensionCoordinator
- __OBJC_CLASS_RO_$_DAExtensionCoordinator
- __OBJC_METACLASS_RO_$_DAExtensionCoordinator
- ___32-[DAExtensionCoordinator update]_block_invoke
- ___34-[DAExtensionCoordinator activate]_block_invoke
- ___36-[DAExtensionCoordinator invalidate]_block_invoke
- ___45-[DAExtensionCoordinator _activateExtension:]_block_invoke
- ___45-[DAExtensionCoordinator _performKeyExchange]_block_invoke
- ___45-[DAExtensionCoordinator _performKeyExchange]_block_invoke.cold.1
- ___45-[DAExtensionCoordinator _performKeyExchange]_block_invoke.cold.2
- ___47-[DAExtensionCoordinator invalidateWithReason:]_block_invoke
- ___49-[DAExtensionCoordinator _reportEventToSessions:]_block_invoke
- ___58-[DAExtensionCoordinator _handleEvent:type:transportType:]_block_invoke
- ___58-[DAExtensionCoordinator _handleEvent:type:transportType:]_block_invoke.cold.1
- ___72-[DAExtensionCoordinator _extensionEnsureStartedWithType:transportType:]_block_invoke
- ___block_descriptor_40_e8_32r_e30_v16?0"_EXExtensionIdentity"8lr32l8
- ___block_descriptor_56_e8_32s40s_e17_v16?0"DAEvent"8ls32l8s40l8
- ___block_descriptor_64_e8_32s40s_e5_v8?0ls32l8s40l8
- ___swift_destroy_boxed_opaque_existential_1
- ___swift_memcpy16_8
- _gLogCategory_DAExtensionCoordinator
- _objc_msgSend$_extensionActivatedWithType:transportType:
- _objc_msgSend$_extensionEnsureStartedWithType:transportType:
- _objc_msgSend$_extensionEnsureStoppedWithType:transportType:
- _objc_msgSend$_extensionInvalidatedWithType:transportType:
- _objc_msgSend$_extensionShouldRunWithType:transportType:
- _objc_msgSend$_extensionWithType:transportType:
- _objc_msgSend$_findExtensionWithType:transportType:completion:
- _objc_msgSend$_handleAccessoryTransportEvent:transportType:
- _objc_msgSend$_handleAccessoryTransportInternetEvent:
- _objc_msgSend$_handleAccessoryTransportLocalEvent:
- _objc_msgSend$_handleEvent:type:transportType:
- _objc_msgSend$_invalidateExtensions
- _objc_msgSend$_performKeyExchange
- _objc_msgSend$_reportEventToSessions:
- _objc_msgSend$_update
- _objc_msgSend$componentsJoinedByString:
- _objc_msgSend$connectionStatus
- _objc_msgSend$containsObject:
- _objc_msgSend$cryptoInfo
- _objc_msgSend$eventHandler
- _objc_msgSend$executeQuery:
- _objc_msgSend$initWithCoordinator:ekExtension:type:transportType:
- _objc_msgSend$initWithDevice:publicKey:
- _objc_msgSend$setConnectionStatus:
- _objc_msgSend$setContext:
- _objc_msgSend$setData:
- _objc_msgSend$setEventHandler:
- _objc_msgSend$setKey:
- _objc_msgSend$transportType
- _objc_msgSend$update
- _swift_getErrorValue
- _symbolic 10PrivateKey_____Qz 12DeviceAccess23DACryptoHandlerProtocol33_5AB05284E0EF12DCB3E81D39A96118B8LLP
- _symbolic 10PrivateKey______06PublicB0_____QZ 12DeviceAccess23DACryptoHandlerProtocol33_5AB05284E0EF12DCB3E81D39A96118B8LLP 9CryptoKit13KEMPrivateKeyP
- _symbolic 9PublicKey_____Qz 12DeviceAccess23DACryptoHandlerProtocol33_5AB05284E0EF12DCB3E81D39A96118B8LLP
- _symbolic SSSg
- _symbolic _____ 12DeviceAccess13DACryptoErrorV
- _symbolic _____ So13DACryptoSuiteV
- _symbolic _____So12DACryptoInfoC______tKc 9CryptoKit4HPKEO9RecipientV 10Foundation4DataV
- _type_layout_string 12DeviceAccess13DACryptoErrorV
CStrings:
+ " EventType %@"
+ " ID %@,"
+ " Type %@,"
+ "### Decrypt %@"
+ "### Encrypt %@"
+ "### Encrypt: %@"
+ "### Extension XPC failed to consume Bluetooth token: %@, %@"
+ "### Extension XPC failed to consume WiFi token: %@, %@"
+ "### Failed to get symmetric key for %s: %s"
+ "### GenerateKeyPair %@"
+ "### StartSession %@"
+ "### StopSession %@"
+ "### XPC DAEventExtension decode failed: %@, %@"
+ "%@ %@"
+ "%@ '%@'"
+ ", AEnK %@ (%lu bytes)"
+ ", APubK %@ (%lu bytes)"
+ ", BluetoothID '%@'"
+ ", CF %@"
+ ", Destination %@"
+ ", EnK %@ (%lu bytes)"
+ ", PrivK %@ (%lu bytes)"
+ ", PubK %@ (%lu bytes)"
+ ", Service %@"
+ "-[DAExtensionSession _activateDirect]"
+ "-[DAExtensionSession _activateXPCCompleted:]"
+ "-[DAExtensionSession _activateXPCCompleted:]_block_invoke"
+ "-[DAExtensionSession _activateXPCStart:]"
+ "-[DAExtensionSession _interrupted]"
+ "-[DAExtensionSession _invalidated]"
+ "-[DAExtensionSession _reportEvent:]"
+ "-[DAExtensionSession _xpcListenerEvent:]"
+ "-[DAExtensionSession _xpcReceivedDAExtensionEvent:]"
+ "-[DAExtensionSession _xpcReceivedMessage:]"
+ "-[DAExtensionSession activate]_block_invoke"
+ "-[DAExtensionSession invalidate]_block_invoke"
+ "-[DAExtensionSession xpcReceivedMessage:]"
+ ": %@ (%ld bytes)"
+ ": CryptoKitError '"
+ "@\"DAExtensionSessionConfiguration\""
+ "@40@0:8@16@24Q32"
+ "@40@0:8@16q24q32"
+ "@48@0:8@16@24Q32^@40"
+ "AccessoryEncapsulatedKey"
+ "AuthenticationFailure"
+ "B48@0:8Q16^@24^@32^@40"
+ "BluetoothIdentifier"
+ "CryptoKit.CryptoKitError"
+ "DAExtensionEvent init bad type: %d"
+ "DAExtensionEventLifecycle"
+ "DAExtensionSession"
+ "DAExtensionSessionConfiguration"
+ "DecryptedData for %s: %s (%ld bytes) -> %s (%ld bytes) with %@"
+ "DeviceID '%@'"
+ "EncapsulatedKey"
+ "EncryptedData for %s: %s (%ld bytes) -> %s (%ld bytes) with %@"
+ "ExCfg <%p> %@"
+ "ExId <%p> %@"
+ "ExPrc <%p> %d"
+ "ExSA"
+ "ExSD"
+ "IncorrectKeySize"
+ "IncorrectParameterSize"
+ "Invalid ciphersuite with value "
+ "InvalidParameter"
+ "KeyExchangeDone"
+ "KeyMaterial"
+ "KeyReply"
+ "KeyRequest"
+ "Killing process for %@"
+ "NIST P-256"
+ "Network"
+ "Reporting event: %@, PID %d"
+ "Started crypto session for: %@"
+ "Stopping %s"
+ "T@\"DAExtensionSessionConfiguration\",R,N,V_configuration"
+ "T@\"NSData\",C,N,V_accessoryEncapsulatedKey"
+ "T@\"NSData\",C,N,V_encapsulatedKey"
+ "T@\"NSString\",C,N,V_bluetoothIdentifier"
+ "T@\"NSString\",R,C,N,V_accessoryService"
+ "T@\"_EXExtensionIdentity\",R,N,V_extensionIdentity"
+ "TQ,N,V_version"
+ "TQ,R,N,V_capabilityFlags"
+ "Tq,N,V_destination"
+ "Tq,N,V_extensionType"
+ "UnderlyingCoreCryptoError"
+ "Updated crypto session for %@"
+ "Version"
+ "_TtC12DeviceAccessP33_5AB05284E0EF12DCB3E81D39A96118B815DACryptoSession"
+ "_accessoryEncapsulatedKey"
+ "_accessoryService"
+ "_capabilityFlags"
+ "_destination"
+ "_encapsulatedKey"
+ "_extensionIdentity"
+ "_extensionProcess"
+ "_extensionType"
+ "_version"
+ "_xpcReceivedDAExtensionEvent:"
+ "accessoryEncapsulatedKey"
+ "accessoryService"
+ "capabilityFlags"
+ "ciAEK"
+ "ciBID"
+ "ciEK"
+ "ciVer"
+ "decryptData:withCryptoInfo:capability:error:"
+ "destination"
+ "domain"
+ "encapsulatedKey"
+ "encryptData:withCryptoInfo:capability:error:"
+ "event cannot be nil"
+ "exCF"
+ "exDE"
+ "exDaD"
+ "exSC"
+ "exSe"
+ "exSv"
+ "exTy"
+ "extensionIdentity"
+ "extensionType"
+ "failed to create recipient"
+ "failed to create sender"
+ "failed to generate key pair"
+ "failed to get combined data for "
+ "failed to get handler"
+ "failed to get symmetric key for "
+ "failed to seal data for "
+ "failed with nil accessory encapsulated key for "
+ "failed with nil accessory key for "
+ "failed with nil ciphertext data"
+ "failed with nil crypto info"
+ "failed with nil plaintext data"
+ "failed with nil private key for "
+ "generateKeyPairForSuite:publicKey:privateKey:error:"
+ "initWithConfiguration:"
+ "initWithDevice:"
+ "initWithDevice:data:capabilityFlag:"
+ "initWithDevice:data:service:"
+ "initWithDevice:eventType:extensionType:"
+ "initWithDevice:identity:type:"
+ "initWithEventType:device:cryptoInfo:"
+ "mainBundle"
+ "recipient"
+ "sendExtensionDataEvent:completionHandler:"
+ "sender"
+ "sessionMap"
+ "setAccessoryEncapsulatedKey:"
+ "setDestination:"
+ "setEncapsulatedKey:"
+ "setExtensionType:"
+ "setVersion:"
+ "startSessionWithInfo:error:"
+ "stopSessionWithInfo:error:"
+ "updateSessionWithInfo:error:"
+ "updateWithDACryptoInfo:"
+ "v1"
+ "version"
- "    %@"
- " '%@', "
- " Type %@"
- "### Extension cannot be started with missing name: %@"
- "### Failed to activate nil extension"
- "### Failed to find %@ EKExtension for %@"
- "### Failed to get event from DAExtensionEventData: %@"
- "### Failed to get key exchange event from %@"
- "### Init failed with nil bundle identifier"
- "### Init failed with nil device"
- "### Invalidated extension missing name: %@"
- "### PerformKeyExchange cryptoInfo is nil: %@"
- "### PerformKeyExchange cryptoInfo public key is nil: %@"
- "### Received transport event with nil local transport extension"
- "### Unknown invalidated extension: %@"
- "%@ extension event %@"
- "%@-%@ connected: %s, keyExchangeDone: %s"
- "%@-%@ should run: %s"
- "'%@'"
- ", "
- ", AccK %@"
- ", Ctx %@"
- ", Info %@"
- ", Key %@"
- ", PK %@"
- ", Priv %@"
- ", Pub %@"
- "-[DAExtensionCoordinator _activateDirect]"
- "-[DAExtensionCoordinator _activateExtension:]"
- "-[DAExtensionCoordinator _extensionEnsureStartedWithType:transportType:]"
- "-[DAExtensionCoordinator _extensionInvalidatedWithType:transportType:]"
- "-[DAExtensionCoordinator _extensionShouldRunWithType:transportType:]"
- "-[DAExtensionCoordinator _findExtensionWithType:transportType:completion:]"
- "-[DAExtensionCoordinator _handleAccessoryTransportInternetEvent:]"
- "-[DAExtensionCoordinator _handleAccessoryTransportLocalEvent:]"
- "-[DAExtensionCoordinator _handleEvent:type:transportType:]_block_invoke"
- "-[DAExtensionCoordinator _interrupted]"
- "-[DAExtensionCoordinator _invalidate]"
- "-[DAExtensionCoordinator _invalidated]"
- "-[DAExtensionCoordinator _performKeyExchange]_block_invoke"
- "-[DAExtensionCoordinator _reportEvent:]"
- "-[DAExtensionCoordinator _update]"
- "-[DAExtensionCoordinator activate]_block_invoke"
- "-[DAExtensionCoordinator addSession:]"
- "-[DAExtensionCoordinator initWithDevice:bundleID:]"
- "-[DAExtensionCoordinator removeSession:]"
- "@32@0:8q16q24"
- "@40@0:8@16Q24^@32"
- "@48@0:8@16@24@32^@40"
- "@48@0:8@16@24^@32^@40"
- "@48@0:8@16@24q32q40"
- "AccessoryTransport"
- "Activating %@ extension with bundleID '%@': %@"
- "Added %@"
- "B32@0:8q16q24"
- "CreateCryptoInfo failed to generate key pair for "
- "CreateCryptoInfo failed to get handler for "
- "CreateCryptoInfo failed: %@"
- "CreateRecipient failed with nil info property: "
- "CreateSender failed with missing parameters: "
- "DACryptoPrivate"
- "DAExtensionCoordinator"
- "Decrypt failed for "
- "Decrypt failed to create recipient for "
- "Decrypt failed to get handler for "
- "Decrypt failed: %@"
- "Encrypt failed to get handler for "
- "Encrypt failed to seal data for "
- "Encrypt failed: %@"
- "Existing sessions for %@"
- "ExtC <%p> %@"
- "ExtI <%p> %@"
- "ExtP <%p> %d"
- "Extension already running: %@"
- "Extensions [ %@ ]"
- "Found %lu extensions for '%@'"
- "Found extension with bundleID '%@', extensionParentID '%@'"
- "Ignoring extension with parent bundleID mismatch: expected '%@' vs '%@'"
- "Ignoring extension without entitlement: '%@'"
- "InfoBlob"
- "Internet"
- "Invalid ciphersuite: "
- "PrivateKeyFromCryptoInfo info failed with nil key: "
- "Q24@0:8@16"
- "Received accessory event with nil transport extension"
- "RecipientKeyFromCryptoInfo failed with nil key: "
- "Removed session '%@' from %@"
- "Searching for %@ extension with bundleID '%@'"
- "Sessions %lu"
- "Skip running extension with type %@"
- "T@\"NSData\",C,N,V_context"
- "T@\"NSData\",C,N,V_info"
- "T@\"NSData\",C,N,V_key"
- "T@\"NSMutableSet\",R,C,N,V_sessionSet"
- "T@\"NSString\",R,C,N,V_bundleID"
- "Tq,R,N,V_transportType"
- "Tq,R,N,V_type"
- "TransportType %@"
- "Type %@"
- "Update %@: %@"
- "XPC report event to %@ extension: %@, queue: %@"
- "[BadParameter] ciphertext cannot be nil"
- "[BadParameter] crypto info cannot be nil"
- "[BadParameter] plaintext cannot be nil"
- "_context"
- "_ekExtensionProcess"
- "_ekHostConfiguration"
- "_extensionActivatedWithType:transportType:"
- "_extensionEnsureStartedWithType:transportType:"
- "_extensionEnsureStoppedWithType:transportType:"
- "_extensionInvalidatedWithType:transportType:"
- "_extensionMap"
- "_extensionShouldRunWithType:transportType:"
- "_extensionWithType:transportType:"
- "_findExtensionWithType:transportType:completion:"
- "_handleAccessoryTransportEvent:transportType:"
- "_handleAccessoryTransportInternetEvent:"
- "_handleAccessoryTransportLocalEvent:"
- "_handleEvent:type:transportType:"
- "_info"
- "_invalidateExtensions"
- "_key"
- "_performKeyExchange"
- "_relaunchExtensions"
- "_reportEventToSessions:"
- "_sessionAdded"
- "_sessionSet"
- "_transportType"
- "_update"
- "addSession:"
- "ciIB"
- "com.apple.dautil"
- "componentsJoinedByString:"
- "containsObject:"
- "context"
- "createCryptoInfoForDevice:suite:error:"
- "decryptData:withCryptoInfo:encapsulatedKey:error:"
- "encryptData:withCryptoInfo:encapsulatedKey:error:"
- "exDI"
- "exDK"
- "executeQuery:"
- "getExtensionPidByType:transport:"
- "i32@0:8q16q24"
- "info"
- "initWithCoordinator:ekExtension:type:transportType:"
- "initWithDevice:bundleID:"
- "initWithDevice:data:key:"
- "initWithDevice:publicKey:"
- "initWithDevice:publicKey:context:"
- "key"
- "nil device identifier: "
- "removeSession:"
- "sessionSet"
- "setContext:"
- "setInfo:"
- "setKey:"
- "transportType"
- "update"
- "v16@?0@\"_EXExtensionIdentity\"8"
- "v32@0:8@16q24"
- "v32@0:8q16q24"
- "v40@0:8@16q24q32"
- "v40@0:8q16q24@?32"

```
