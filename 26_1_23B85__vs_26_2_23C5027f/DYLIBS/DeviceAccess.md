## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

```diff

-321.9.0.0.0
-  __TEXT.__text: 0x2a1f4
-  __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_methlist: 0x26ac
-  __TEXT.__cstring: 0x54d7
-  __TEXT.__gcc_except_tab: 0x75c
-  __TEXT.__const: 0x268
-  __TEXT.__swift5_typeref: 0x119
-  __TEXT.__oslogstring: 0x17d
+322.6.2.0.0
+  __TEXT.__text: 0x36474
+  __TEXT.__auth_stubs: 0x1280
+  __TEXT.__objc_methlist: 0x2f64
+  __TEXT.__cstring: 0x6902
+  __TEXT.__gcc_except_tab: 0x904
+  __TEXT.__const: 0x3e8
+  __TEXT.__swift5_typeref: 0x246
+  __TEXT.__constg_swiftt: 0x31c
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_types: 0x18
+  __TEXT.__oslogstring: 0x1dd
+  __TEXT.__swift5_reflstr: 0xd8
+  __TEXT.__swift5_fieldmd: 0xf4
+  __TEXT.__swift5_proto: 0x10
+  __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__swift5_fieldmd: 0x6c
-  __TEXT.__constg_swiftt: 0x1b0
-  __TEXT.__swift5_reflstr: 0x88
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0x8
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x9b8
-  __TEXT.__objc_classname: 0x382
-  __TEXT.__objc_methname: 0x5693
-  __TEXT.__objc_methtype: 0x7b9
-  __TEXT.__objc_stubs: 0x2c60
-  __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0x928
-  __DATA_CONST.__objc_classlist: 0x110
-  __DATA_CONST.__objc_protolist: 0x50
+  __TEXT.__unwind_info: 0xce0
+  __TEXT.__eh_frame: 0x3a0
+  __TEXT.__objc_classname: 0x466
+  __TEXT.__objc_methname: 0x60a9
+  __TEXT.__objc_methtype: 0x9ba
+  __TEXT.__objc_stubs: 0x3320
+  __DATA_CONST.__got: 0x3b8
+  __DATA_CONST.__const: 0x9e8
+  __DATA_CONST.__objc_classlist: 0x160
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1388
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0xd8
-  __AUTH_CONST.__auth_got: 0x728
-  __AUTH_CONST.__const: 0x458
-  __AUTH_CONST.__cfstring: 0x21c0
-  __AUTH_CONST.__objc_const: 0x45e0
+  __DATA_CONST.__objc_selrefs: 0x1640
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x108
+  __AUTH_CONST.__auth_got: 0x950
+  __AUTH_CONST.__const: 0x4f8
+  __AUTH_CONST.__cfstring: 0x2620
+  __AUTH_CONST.__objc_const: 0x5470
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x3e4
-  __DATA.__data: 0x7a8
-  __DATA.__bss: 0x140
+  __AUTH.__objc_data: 0x630
+  __AUTH.__data: 0x178
+  __DATA.__objc_ivar: 0x494
+  __DATA.__data: 0xab8
+  __DATA.__bss: 0x240
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__common: 0x8

   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F98C1BCB-3553-3364-9867-91A51E514351
-  Functions: 1187
-  Symbols:   3636
-  CStrings:  2254
+  UUID: 48D2BA8F-C36E-3451-879F-A55310E6AEFD
+  Functions: 1476
+  Symbols:   4326
+  CStrings:  2634
 
Symbols:
+ +[DACryptoInfo keychainType]
+ +[DACryptoInfo supportsSecureCoding]
+ +[DAEventExtension supportsSecureCoding]
+ +[DAExtensionEventData supportsSecureCoding]
+ +[DAExtensionEventKeyExchange supportsSecureCoding]
+ -[DABluetoothPairingInfo initWithBluetoothIdentifier:pairedCTKD:appConfirmsAuth:pairingRequired:btSCPairing:]
+ -[DABluetoothPairingInfo secureConnectionPairing]
+ -[DACryptoInfo .cxx_destruct]
+ -[DACryptoInfo accessoryKey]
+ -[DACryptoInfo ciphersuite]
+ -[DACryptoInfo copyWithZone:]
+ -[DACryptoInfo descriptionWithLevel:]
+ -[DACryptoInfo description]
+ -[DACryptoInfo dictionaryRepresentation]
+ -[DACryptoInfo encodeWithCoder:]
+ -[DACryptoInfo encodeWithXPCObject:]
+ -[DACryptoInfo identifier]
+ -[DACryptoInfo info]
+ -[DACryptoInfo initWithCoder:]
+ -[DACryptoInfo initWithCoder:].cold.1
+ -[DACryptoInfo initWithDictionary:error:]
+ -[DACryptoInfo initWithXPCObject:error:]
+ -[DACryptoInfo initWithXPCObject:error:].cold.1
+ -[DACryptoInfo privateKey]
+ -[DACryptoInfo publicKey]
+ -[DACryptoInfo setAccessoryKey:]
+ -[DACryptoInfo setCiphersuite:]
+ -[DACryptoInfo setIdentifier:]
+ -[DACryptoInfo setInfo:]
+ -[DACryptoInfo setPrivateKey:]
+ -[DACryptoInfo setPublicKey:]
+ -[DADevice cryptoInfo]
+ -[DADevice setCryptoInfo:]
+ -[DAEventExtension .cxx_destruct]
+ -[DAEventExtension descriptionWithLevel:]
+ -[DAEventExtension device]
+ -[DAEventExtension encodeWithCoder:]
+ -[DAEventExtension encodeWithXPCObject:]
+ -[DAEventExtension initWithCoder:]
+ -[DAEventExtension initWithCoder:].cold.1
+ -[DAEventExtension initWithEventType:device:]
+ -[DAEventExtension initWithEventType:device:error:]
+ -[DAEventExtension initWithXPCObject:error:]
+ -[DAExtension .cxx_destruct]
+ -[DAExtension _activateDirect]
+ -[DAExtension _activated]
+ -[DAExtension _activated].cold.1
+ -[DAExtension _interrupted]
+ -[DAExtension _interrupted].cold.1
+ -[DAExtension _invalidate]
+ -[DAExtension _invalidate].cold.1
+ -[DAExtension _invalidated]
+ -[DAExtension _invalidated].cold.1
+ -[DAExtension _invalidated].cold.2
+ -[DAExtension _reportEventType:]
+ -[DAExtension activate]
+ -[DAExtension activate].cold.1
+ -[DAExtension descriptionWithLevel:]
+ -[DAExtension description]
+ -[DAExtension ekExtension]
+ -[DAExtension eventHandler]
+ -[DAExtension initWithCoordinator:ekExtension:type:transportType:]
+ -[DAExtension invalidateWithReason:]
+ -[DAExtension invalidate]
+ -[DAExtension name]
+ -[DAExtension pid]
+ -[DAExtension reportEvent:]
+ -[DAExtension reportEvent:].cold.1
+ -[DAExtension reportEventToExtension:]
+ -[DAExtension setEkExtension:]
+ -[DAExtension setEventHandler:]
+ -[DAExtension setName:]
+ -[DAExtension setPid:]
+ -[DAExtension transportType]
+ -[DAExtension type]
+ -[DAExtensionCoordinator .cxx_destruct]
+ -[DAExtensionCoordinator _activateDirect]
+ -[DAExtensionCoordinator _activateExtension:]
+ -[DAExtensionCoordinator _activateExtension:].cold.1
+ -[DAExtensionCoordinator _activateExtension:].cold.2
+ -[DAExtensionCoordinator _extensionActivatedWithType:transportType:]
+ -[DAExtensionCoordinator _extensionEnsureStartedWithType:transportType:]
+ -[DAExtensionCoordinator _extensionEnsureStartedWithType:transportType:].cold.1
+ -[DAExtensionCoordinator _extensionEnsureStoppedWithType:transportType:]
+ -[DAExtensionCoordinator _extensionInvalidatedWithType:transportType:]
+ -[DAExtensionCoordinator _extensionInvalidatedWithType:transportType:].cold.1
+ -[DAExtensionCoordinator _extensionInvalidatedWithType:transportType:].cold.2
+ -[DAExtensionCoordinator _extensionShouldRunWithType:transportType:]
+ -[DAExtensionCoordinator _extensionShouldRunWithType:transportType:].cold.1
+ -[DAExtensionCoordinator _extensionShouldRunWithType:transportType:].cold.2
+ -[DAExtensionCoordinator _extensionWithType:transportType:]
+ -[DAExtensionCoordinator _findExtensionWithType:transportType:completion:]
+ -[DAExtensionCoordinator _findExtensionWithType:transportType:completion:].cold.1
+ -[DAExtensionCoordinator _findExtensionWithType:transportType:completion:].cold.2
+ -[DAExtensionCoordinator _findExtensionWithType:transportType:completion:].cold.3
+ -[DAExtensionCoordinator _findExtensionWithType:transportType:completion:].cold.4
+ -[DAExtensionCoordinator _handleAccessoryTransportEvent:transportType:]
+ -[DAExtensionCoordinator _handleAccessoryTransportInternetEvent:]
+ -[DAExtensionCoordinator _handleAccessoryTransportInternetEvent:].cold.1
+ -[DAExtensionCoordinator _handleAccessoryTransportInternetEvent:].cold.2
+ -[DAExtensionCoordinator _handleAccessoryTransportLocalEvent:]
+ -[DAExtensionCoordinator _handleAccessoryTransportLocalEvent:].cold.1
+ -[DAExtensionCoordinator _handleAccessoryTransportLocalEvent:].cold.2
+ -[DAExtensionCoordinator _handleEvent:type:transportType:]
+ -[DAExtensionCoordinator _interrupted]
+ -[DAExtensionCoordinator _interrupted].cold.1
+ -[DAExtensionCoordinator _invalidateExtensions]
+ -[DAExtensionCoordinator _invalidate]
+ -[DAExtensionCoordinator _invalidate].cold.1
+ -[DAExtensionCoordinator _invalidated]
+ -[DAExtensionCoordinator _invalidated].cold.1
+ -[DAExtensionCoordinator _performKeyExchange]
+ -[DAExtensionCoordinator _reportEvent:]
+ -[DAExtensionCoordinator _reportEvent:].cold.1
+ -[DAExtensionCoordinator _reportEventToSessions:]
+ -[DAExtensionCoordinator _reportEventType:]
+ -[DAExtensionCoordinator _update]
+ -[DAExtensionCoordinator _update].cold.1
+ -[DAExtensionCoordinator _update].cold.2
+ -[DAExtensionCoordinator activate]
+ -[DAExtensionCoordinator addSession:]
+ -[DAExtensionCoordinator addSession:].cold.1
+ -[DAExtensionCoordinator bundleID]
+ -[DAExtensionCoordinator descriptionWithLevel:]
+ -[DAExtensionCoordinator description]
+ -[DAExtensionCoordinator device]
+ -[DAExtensionCoordinator dispatchQueue]
+ -[DAExtensionCoordinator eventHandler]
+ -[DAExtensionCoordinator getExtensionPidByType:transport:]
+ -[DAExtensionCoordinator initWithDevice:bundleID:]
+ -[DAExtensionCoordinator initWithDevice:bundleID:].cold.1
+ -[DAExtensionCoordinator initWithDevice:bundleID:].cold.2
+ -[DAExtensionCoordinator invalidateWithReason:]
+ -[DAExtensionCoordinator invalidate]
+ -[DAExtensionCoordinator removeSession:]
+ -[DAExtensionCoordinator sessionSet]
+ -[DAExtensionCoordinator setDispatchQueue:]
+ -[DAExtensionCoordinator setEventHandler:]
+ -[DAExtensionCoordinator update]
+ -[DAExtensionEventData .cxx_destruct]
+ -[DAExtensionEventData data]
+ -[DAExtensionEventData descriptionWithLevel:]
+ -[DAExtensionEventData description]
+ -[DAExtensionEventData encodeWithCoder:]
+ -[DAExtensionEventData encodeWithXPCObject:]
+ -[DAExtensionEventData initWithCoder:]
+ -[DAExtensionEventData initWithCoder:].cold.1
+ -[DAExtensionEventData initWithDevice:data:key:]
+ -[DAExtensionEventData initWithXPCObject:error:]
+ -[DAExtensionEventData key]
+ -[DAExtensionEventData setData:]
+ -[DAExtensionEventData setKey:]
+ -[DAExtensionEventKeyExchange .cxx_destruct]
+ -[DAExtensionEventKeyExchange bundleID]
+ -[DAExtensionEventKeyExchange context]
+ -[DAExtensionEventKeyExchange descriptionWithLevel:]
+ -[DAExtensionEventKeyExchange description]
+ -[DAExtensionEventKeyExchange encodeWithCoder:]
+ -[DAExtensionEventKeyExchange encodeWithXPCObject:]
+ -[DAExtensionEventKeyExchange initWithCoder:]
+ -[DAExtensionEventKeyExchange initWithCoder:].cold.1
+ -[DAExtensionEventKeyExchange initWithDevice:publicKey:]
+ -[DAExtensionEventKeyExchange initWithDevice:publicKey:context:]
+ -[DAExtensionEventKeyExchange initWithXPCObject:error:]
+ -[DAExtensionEventKeyExchange publicKey]
+ -[DAExtensionEventKeyExchange setBundleID:]
+ -[DAExtensionEventKeyExchange setContext:]
+ -[DAExtensionEventKeyExchange setPublicKey:]
+ -[DASession launchInteractionWithDevice:flags:reason:completionHandler:].cold.1
+ -[DASession pid]
+ -[DASession setPid:]
+ GCC_except_table11
+ GCC_except_table13
+ GCC_except_table16
+ GCC_except_table20
+ GCC_except_table71
+ _CUPrintNSObjectMasked
+ _DAAccessoryTransportTypeToString
+ _DACryptoSuiteToString
+ _DAExtensionInvalidateReasonToEventType
+ _DAExtensionInvalidateReasonToString
+ _DAExtensionPointEntitlementAccessoryTransport
+ _DAExtensionPointIdentifierAccessoryTransport
+ _DAExtensionTypeToEntitlement
+ _DAExtensionTypeToPointIdentifier
+ _DAExtensionTypeToString
+ _NSAppendPrintF_safe
+ _NSDataWithHex
+ _OBJC_CLASS_$_DACrypto
+ _OBJC_CLASS_$_DACryptoInfo
+ _OBJC_CLASS_$_DACryptoPrivate
+ _OBJC_CLASS_$_DAEventExtension
+ _OBJC_CLASS_$_DAExtension
+ _OBJC_CLASS_$_DAExtensionCoordinator
+ _OBJC_CLASS_$_DAExtensionEvent
+ _OBJC_CLASS_$_DAExtensionEventData
+ _OBJC_CLASS_$_DAExtensionEventKeyExchange
+ _OBJC_CLASS_$_RBSProcessPredicate
+ _OBJC_CLASS_$_RBSTerminateContext
+ _OBJC_CLASS_$_RBSTerminateRequest
+ _OBJC_CLASS_$__EXExtensionInstanceIdentifier
+ _OBJC_CLASS_$__EXExtensionProcess
+ _OBJC_CLASS_$__EXHostConfiguration
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_DABluetoothPairingInfo._secureConnectionPairing
+ _OBJC_IVAR_$_DACryptoInfo._accessoryKey
+ _OBJC_IVAR_$_DACryptoInfo._ciphersuite
+ _OBJC_IVAR_$_DACryptoInfo._identifier
+ _OBJC_IVAR_$_DACryptoInfo._info
+ _OBJC_IVAR_$_DACryptoInfo._privateKey
+ _OBJC_IVAR_$_DACryptoInfo._publicKey
+ _OBJC_IVAR_$_DADevice._cryptoInfo
+ _OBJC_IVAR_$_DAEventExtension._device
+ _OBJC_IVAR_$_DAExtension._activateCalled
+ _OBJC_IVAR_$_DAExtension._bundleID
+ _OBJC_IVAR_$_DAExtension._clientInvalidated
+ _OBJC_IVAR_$_DAExtension._device
+ _OBJC_IVAR_$_DAExtension._dispatchQueue
+ _OBJC_IVAR_$_DAExtension._ekExtension
+ _OBJC_IVAR_$_DAExtension._ekExtensionProcess
+ _OBJC_IVAR_$_DAExtension._ekHostConfiguration
+ _OBJC_IVAR_$_DAExtension._eventHandler
+ _OBJC_IVAR_$_DAExtension._invalidateCalled
+ _OBJC_IVAR_$_DAExtension._invalidateDone
+ _OBJC_IVAR_$_DAExtension._invalidateReason
+ _OBJC_IVAR_$_DAExtension._name
+ _OBJC_IVAR_$_DAExtension._pid
+ _OBJC_IVAR_$_DAExtension._transportType
+ _OBJC_IVAR_$_DAExtension._type
+ _OBJC_IVAR_$_DAExtension._xpcConnection
+ _OBJC_IVAR_$_DAExtensionCoordinator._activateCalled
+ _OBJC_IVAR_$_DAExtensionCoordinator._bundleID
+ _OBJC_IVAR_$_DAExtensionCoordinator._device
+ _OBJC_IVAR_$_DAExtensionCoordinator._dispatchQueue
+ _OBJC_IVAR_$_DAExtensionCoordinator._eventHandler
+ _OBJC_IVAR_$_DAExtensionCoordinator._extensionMap
+ _OBJC_IVAR_$_DAExtensionCoordinator._invalidateCalled
+ _OBJC_IVAR_$_DAExtensionCoordinator._invalidateDone
+ _OBJC_IVAR_$_DAExtensionCoordinator._invalidateReason
+ _OBJC_IVAR_$_DAExtensionCoordinator._relaunchExtensions
+ _OBJC_IVAR_$_DAExtensionCoordinator._sessionAdded
+ _OBJC_IVAR_$_DAExtensionCoordinator._sessionSet
+ _OBJC_IVAR_$_DAExtensionEventData._data
+ _OBJC_IVAR_$_DAExtensionEventData._key
+ _OBJC_IVAR_$_DAExtensionEventKeyExchange._bundleID
+ _OBJC_IVAR_$_DAExtensionEventKeyExchange._context
+ _OBJC_IVAR_$_DAExtensionEventKeyExchange._publicKey
+ _OBJC_IVAR_$_DASession._pid
+ _OBJC_METACLASS_$_DACrypto
+ _OBJC_METACLASS_$_DACryptoInfo
+ _OBJC_METACLASS_$_DACryptoPrivate
+ _OBJC_METACLASS_$_DAEventExtension
+ _OBJC_METACLASS_$_DAExtension
+ _OBJC_METACLASS_$_DAExtensionCoordinator
+ _OBJC_METACLASS_$_DAExtensionEvent
+ _OBJC_METACLASS_$_DAExtensionEventData
+ _OBJC_METACLASS_$_DAExtensionEventKeyExchange
+ __CLASS_METHODS_DACrypto
+ __CLASS_METHODS_DACryptoPrivate
+ __DATA_DACrypto
+ __DATA_DACryptoPrivate
+ __DATA__TtC12DeviceAccess18DACryptoKitManager
+ __INSTANCE_METHODS_DACrypto
+ __INSTANCE_METHODS_DACryptoPrivate
+ __METACLASS_DATA_DACrypto
+ __METACLASS_DATA_DACryptoPrivate
+ __METACLASS_DATA__TtC12DeviceAccess18DACryptoKitManager
+ __OBJC_$_CLASS_METHODS_DACryptoInfo
+ __OBJC_$_CLASS_METHODS_DAEventExtension
+ __OBJC_$_CLASS_METHODS_DAExtensionEventData
+ __OBJC_$_CLASS_METHODS_DAExtensionEventKeyExchange
+ __OBJC_$_CLASS_PROP_LIST_DACryptoInfo
+ __OBJC_$_INSTANCE_METHODS_DACryptoInfo
+ __OBJC_$_INSTANCE_METHODS_DAEventExtension
+ __OBJC_$_INSTANCE_METHODS_DAExtension
+ __OBJC_$_INSTANCE_METHODS_DAExtensionCoordinator
+ __OBJC_$_INSTANCE_METHODS_DAExtensionEventData
+ __OBJC_$_INSTANCE_METHODS_DAExtensionEventKeyExchange
+ __OBJC_$_INSTANCE_VARIABLES_DACryptoInfo
+ __OBJC_$_INSTANCE_VARIABLES_DAEventExtension
+ __OBJC_$_INSTANCE_VARIABLES_DAExtension
+ __OBJC_$_INSTANCE_VARIABLES_DAExtensionCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_DAExtensionEventData
+ __OBJC_$_INSTANCE_VARIABLES_DAExtensionEventKeyExchange
+ __OBJC_$_PROP_LIST_DACryptoInfo
+ __OBJC_$_PROP_LIST_DAEventExtension
+ __OBJC_$_PROP_LIST_DAExtension
+ __OBJC_$_PROP_LIST_DAExtensionCoordinator
+ __OBJC_$_PROP_LIST_DAExtensionEventData
+ __OBJC_$_PROP_LIST_DAExtensionEventKeyExchange
+ __OBJC_$_PROP_LIST_DAKeychainCodable
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_CLASS_METHODS_DAKeychainCodable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DAExtensionXPCProtocolExtension
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DAExtensionXPCProtocolHost
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DAKeychainCodable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DAExtensionXPCProtocolExtension
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DAExtensionXPCProtocolHost
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DAKeychainCodable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_DAKeychainCodable
+ __OBJC_CLASS_PROTOCOLS_$_DACryptoInfo
+ __OBJC_CLASS_PROTOCOLS_$_DAExtension
+ __OBJC_CLASS_RO_$_DACryptoInfo
+ __OBJC_CLASS_RO_$_DAEventExtension
+ __OBJC_CLASS_RO_$_DAExtension
+ __OBJC_CLASS_RO_$_DAExtensionCoordinator
+ __OBJC_CLASS_RO_$_DAExtensionEvent
+ __OBJC_CLASS_RO_$_DAExtensionEventData
+ __OBJC_CLASS_RO_$_DAExtensionEventKeyExchange
+ __OBJC_LABEL_PROTOCOL_$_DAExtensionXPCProtocolExtension
+ __OBJC_LABEL_PROTOCOL_$_DAExtensionXPCProtocolHost
+ __OBJC_LABEL_PROTOCOL_$_DAKeychainCodable
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_DACryptoInfo
+ __OBJC_METACLASS_RO_$_DAEventExtension
+ __OBJC_METACLASS_RO_$_DAExtension
+ __OBJC_METACLASS_RO_$_DAExtensionCoordinator
+ __OBJC_METACLASS_RO_$_DAExtensionEvent
+ __OBJC_METACLASS_RO_$_DAExtensionEventData
+ __OBJC_METACLASS_RO_$_DAExtensionEventKeyExchange
+ __OBJC_PROTOCOL_$_DAExtensionXPCProtocolExtension
+ __OBJC_PROTOCOL_$_DAExtensionXPCProtocolHost
+ __OBJC_PROTOCOL_$_DAKeychainCodable
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_REFERENCE_$_DAExtensionXPCProtocolExtension
+ __OBJC_PROTOCOL_REFERENCE_$_DAExtensionXPCProtocolHost
+ ___23-[DAExtension activate]_block_invoke
+ ___25-[DAExtension invalidate]_block_invoke
+ ___30-[DAExtension _activateDirect]_block_invoke
+ ___30-[DAExtension _activateDirect]_block_invoke_2
+ ___30-[DAExtension _activateDirect]_block_invoke_3
+ ___30-[DAExtension _activateDirect]_block_invoke_4
+ ___30-[DAExtension _activateDirect]_block_invoke_5
+ ___30-[DAExtension _activateDirect]_block_invoke_5.cold.1
+ ___30-[DAExtension _activateDirect]_block_invoke_6
+ ___30-[DAExtension _activateDirect]_block_invoke_6.cold.1
+ ___30-[DAExtension _activateDirect]_block_invoke_7
+ ___30-[DAExtension _activateDirect]_block_invoke_7.cold.1
+ ___32-[DAExtensionCoordinator update]_block_invoke
+ ___34-[DAExtensionCoordinator activate]_block_invoke
+ ___36-[DAExtension invalidateWithReason:]_block_invoke
+ ___36-[DAExtensionCoordinator invalidate]_block_invoke
+ ___38-[DAExtension reportEventToExtension:]_block_invoke
+ ___38-[DAExtension reportEventToExtension:]_block_invoke.cold.1
+ ___38-[DAExtension reportEventToExtension:]_block_invoke.cold.2
+ ___38-[DAExtension reportEventToExtension:]_block_invoke_2
+ ___38-[DAExtension reportEventToExtension:]_block_invoke_2.cold.1
+ ___45-[DAExtensionCoordinator _activateExtension:]_block_invoke
+ ___45-[DAExtensionCoordinator _performKeyExchange]_block_invoke
+ ___45-[DAExtensionCoordinator _performKeyExchange]_block_invoke.cold.1
+ ___45-[DAExtensionCoordinator _performKeyExchange]_block_invoke.cold.2
+ ___47-[DAExtensionCoordinator invalidateWithReason:]_block_invoke
+ ___49-[DAExtensionCoordinator _reportEventToSessions:]_block_invoke
+ ___58-[DAExtensionCoordinator _handleEvent:type:transportType:]_block_invoke
+ ___58-[DAExtensionCoordinator _handleEvent:type:transportType:]_block_invoke.cold.1
+ ___72-[DAExtensionCoordinator _extensionEnsureStartedWithType:transportType:]_block_invoke
+ ___72-[DASession launchInteractionWithDevice:flags:reason:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32r_e30_v16?0"_EXExtensionIdentity"8lr32l8
+ ___block_descriptor_56_e8_32s40s_e17_v16?0"DAEvent"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.103
+ ___block_literal_global.129
+ ___block_literal_global.140
+ ___block_literal_global.78
+ ___block_literal_global.81
+ ___block_literal_global.94
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_memcpy16_8
+ ___swift_project_boxed_opaque_existential_1
+ __swift_stdlib_bridgeErrorToNSError
+ _gLogCategory_DAExtension
+ _gLogCategory_DAExtensionCoordinator
+ _memcpy
+ _objc_msgSend$_activated
+ _objc_msgSend$_extensionActivatedWithType:transportType:
+ _objc_msgSend$_extensionEnsureStartedWithType:transportType:
+ _objc_msgSend$_extensionEnsureStoppedWithType:transportType:
+ _objc_msgSend$_extensionInvalidatedWithType:transportType:
+ _objc_msgSend$_extensionShouldRunWithType:transportType:
+ _objc_msgSend$_extensionWithType:transportType:
+ _objc_msgSend$_findExtensionWithType:transportType:completion:
+ _objc_msgSend$_handleAccessoryTransportEvent:transportType:
+ _objc_msgSend$_handleAccessoryTransportInternetEvent:
+ _objc_msgSend$_handleAccessoryTransportLocalEvent:
+ _objc_msgSend$_handleEvent:type:transportType:
+ _objc_msgSend$_invalidateExtensions
+ _objc_msgSend$_performKeyExchange
+ _objc_msgSend$_reportEventToSessions:
+ _objc_msgSend$_update
+ _objc_msgSend$accessoryKey
+ _objc_msgSend$code
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$connectionStatus
+ _objc_msgSend$containsObject:
+ _objc_msgSend$cryptoInfo
+ _objc_msgSend$didReceiveEvent:
+ _objc_msgSend$dispatchQueue
+ _objc_msgSend$eventHandler
+ _objc_msgSend$execute:
+ _objc_msgSend$executeQuery:
+ _objc_msgSend$extensionProcessWithConfiguration:error:
+ _objc_msgSend$initWithCoordinator:ekExtension:type:transportType:
+ _objc_msgSend$initWithDevice:publicKey:
+ _objc_msgSend$initWithExplanation:
+ _objc_msgSend$initWithExtensionIdentity:instanceIdentifier:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithPredicate:context:
+ _objc_msgSend$instanceIdentifier
+ _objc_msgSend$invalidateWithReason:
+ _objc_msgSend$pid
+ _objc_msgSend$predicateMatchingIdentifier:
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$publicKey
+ _objc_msgSend$reportEvent:
+ _objc_msgSend$runProximitySetupWithDiscovery:
+ _objc_msgSend$setAccessoryKey:
+ _objc_msgSend$setConnectionStatus:
+ _objc_msgSend$setContext:
+ _objc_msgSend$setData:
+ _objc_msgSend$setEventHandler:
+ _objc_msgSend$setExtensionIdentity:
+ _objc_msgSend$setKey:
+ _objc_msgSend$setPublicKey:
+ _objc_msgSend$startExtension:bundleID:
+ _objc_msgSend$transportType
+ _objc_msgSend$uniqueIdentifier
+ _objc_msgSend$update
+ _swift_allocError
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deletedMethodError
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getErrorValue
+ _swift_getForeignTypeMetadata
+ _swift_getFunctionTypeMetadata0
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getSingletonMetadata
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release_n
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_willThrow
+ _symbolic $s12DeviceAccess23DACryptoHandlerProtocol33_5AB05284E0EF12DCB3E81D39A96118B8LLP
+ _symbolic 10PrivateKey_____Qz 12DeviceAccess23DACryptoHandlerProtocol33_5AB05284E0EF12DCB3E81D39A96118B8LLP
+ _symbolic 10PrivateKey______06PublicB0_____QZ 12DeviceAccess23DACryptoHandlerProtocol33_5AB05284E0EF12DCB3E81D39A96118B8LLP 9CryptoKit13KEMPrivateKeyP
+ _symbolic 9PublicKey_____Qz 12DeviceAccess23DACryptoHandlerProtocol33_5AB05284E0EF12DCB3E81D39A96118B8LLP
+ _symbolic SS
+ _symbolic SSSg
+ _symbolic _____ 12DeviceAccess13DACryptoErrorV
+ _symbolic _____ 12DeviceAccess15DACryptoHandler33_5AB05284E0EF12DCB3E81D39A96118B8LLV
+ _symbolic _____ 12DeviceAccess18DACryptoKitManagerC
+ _symbolic _____ 9CryptoKit4HPKEO11CiphersuiteV
+ _symbolic _____ So13DACryptoSuiteV
+ _symbolic _____Sg 9CryptoKit19XWingMLKEM768X25519O9PublicKeyV
+ _symbolic _____So12DACryptoInfoCKc 9CryptoKit4HPKEO6SenderV
+ _symbolic _____So12DACryptoInfoC______tKc 9CryptoKit4HPKEO9RecipientV 10Foundation4DataV
+ _symbolic ______AAtyKc 10Foundation4DataV
+ _symbolic ______p 10Foundation15ContiguousBytesP
+ _symbolic ______p s5ErrorP
+ _symbolic ______pSg 10Foundation15ContiguousBytesP
+ _type_layout_string 12DeviceAccess13DACryptoErrorV
- -[DABluetoothPairingInfo initWithBluetoothIdentifier:pairedCTKD:appConfirmsAuth:pairingRequired:]
- GCC_except_table3
- GCC_except_table70
- ___block_literal_global.119
- ___block_literal_global.130
- ___block_literal_global.67
- ___block_literal_global.71
- ___block_literal_global.87
- ___block_literal_global.96
CStrings:
+ "    %@"
+ " %@"
+ " '%@'"
+ " '%@', "
+ " Type %@"
+ "### DAExtension activate failed with missing type: %@"
+ "### Extension XPC failed for start extension: %@, %@"
+ "### Extension XPC failed for startExtension: %@, %@"
+ "### Extension cannot be started with missing name: %@"
+ "### Failed to activate nil extension"
+ "### Failed to find %@ EKExtension for %@"
+ "### Failed to get event from DAExtensionEventData: %@"
+ "### Failed to get key exchange event from %@"
+ "### Failed to terminate context: %@"
+ "### Init failed with nil bundle identifier"
+ "### Init failed with nil device"
+ "### Interrupted %@"
+ "### Invalidated extension missing name: %@"
+ "### PerformKeyExchange cryptoInfo is nil: %@"
+ "### PerformKeyExchange cryptoInfo public key is nil: %@"
+ "### Received nil XPC event from %@ extension"
+ "### Received transport event with nil local transport extension"
+ "### ReportEventToExtension failed with nil xpc connection"
+ "### Unknown invalidated extension: %@"
+ "#16@0:8"
+ "%@ extension event %@"
+ "%@-%@"
+ "%@-%@ connected: %s, keyExchangeDone: %s"
+ "%@-%@ should run: %s"
+ "'%@'"
+ ", "
+ ", AccK %@"
+ ", Ctx %@"
+ ", ID '%@'"
+ ", Info %@"
+ ", Key %@"
+ ", PK %@"
+ ", Priv %@"
+ ", Pub %@"
+ "-[DAExtension _activateDirect]_block_invoke"
+ "-[DAExtension _activateDirect]_block_invoke_5"
+ "-[DAExtension _activateDirect]_block_invoke_6"
+ "-[DAExtension _activateDirect]_block_invoke_7"
+ "-[DAExtension _activated]"
+ "-[DAExtension _interrupted]"
+ "-[DAExtension _invalidate]"
+ "-[DAExtension _invalidated]"
+ "-[DAExtension activate]"
+ "-[DAExtension activate]_block_invoke"
+ "-[DAExtension reportEvent:]"
+ "-[DAExtension reportEventToExtension:]_block_invoke"
+ "-[DAExtension reportEventToExtension:]_block_invoke_2"
+ "-[DAExtensionCoordinator _activateDirect]"
+ "-[DAExtensionCoordinator _activateExtension:]"
+ "-[DAExtensionCoordinator _extensionEnsureStartedWithType:transportType:]"
+ "-[DAExtensionCoordinator _extensionInvalidatedWithType:transportType:]"
+ "-[DAExtensionCoordinator _extensionShouldRunWithType:transportType:]"
+ "-[DAExtensionCoordinator _findExtensionWithType:transportType:completion:]"
+ "-[DAExtensionCoordinator _handleAccessoryTransportInternetEvent:]"
+ "-[DAExtensionCoordinator _handleAccessoryTransportLocalEvent:]"
+ "-[DAExtensionCoordinator _handleEvent:type:transportType:]_block_invoke"
+ "-[DAExtensionCoordinator _interrupted]"
+ "-[DAExtensionCoordinator _invalidate]"
+ "-[DAExtensionCoordinator _invalidated]"
+ "-[DAExtensionCoordinator _performKeyExchange]_block_invoke"
+ "-[DAExtensionCoordinator _reportEvent:]"
+ "-[DAExtensionCoordinator _update]"
+ "-[DAExtensionCoordinator activate]_block_invoke"
+ "-[DAExtensionCoordinator addSession:]"
+ "-[DAExtensionCoordinator initWithDevice:bundleID:]"
+ "-[DAExtensionCoordinator removeSession:]"
+ "@\"DACryptoInfo\""
+ "@\"NSDictionary\"16@0:8"
+ "@\"NSString\"16@0:8"
+ "@\"_EXExtensionProcess\""
+ "@\"_EXHostConfiguration\""
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@32@0:8@\"NSDictionary\"16^@24"
+ "@32@0:8q16q24"
+ "@40@0:8:16@24@32"
+ "@40@0:8@16@24@32"
+ "@40@0:8@16B24B28B32B36"
+ "@40@0:8@16Q24^@32"
+ "@48@0:8@16@24@32^@40"
+ "@48@0:8@16@24^@32^@40"
+ "@48@0:8@16@24q32q40"
+ "AccessoryKey"
+ "AccessoryTransport"
+ "Activate %@"
+ "ActivateFailed"
+ "Activated %@"
+ "Activating %@ extension with bundleID '%@': %@"
+ "Added %@"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B32@0:8q16q24"
+ "BTLESC"
+ "BundleID '%@'"
+ "Ciphersuite"
+ "Conn < %@ >"
+ "CreateCryptoInfo failed to generate key pair for "
+ "CreateCryptoInfo failed to get handler for "
+ "CreateCryptoInfo failed: %@"
+ "CreateRecipient failed with nil info property: "
+ "CreateSender failed with missing parameters: "
+ "DACrypto"
+ "DACryptoInfo"
+ "DACryptoInfo failed to init with nil dictionary"
+ "DACryptoPrivate"
+ "DAEventExtension"
+ "DAExtension"
+ "DAExtensionCoordinator"
+ "DAExtensionEvent"
+ "DAExtensionEventData"
+ "DAExtensionEventKeyExchange"
+ "DAExtensionXPCProtocolExtension"
+ "DAExtensionXPCProtocolHost"
+ "DAKeychainCodable"
+ "Data"
+ "Decrypt failed for "
+ "Decrypt failed to create recipient for "
+ "Decrypt failed to get handler for "
+ "Decrypt failed: %@"
+ "DeviceRemoved"
+ "DeviceServicesChanged"
+ "Direct"
+ "Disconnected"
+ "Encrypt failed to get handler for "
+ "Encrypt failed to seal data for "
+ "Encrypt failed: %@"
+ "Existing sessions for %@"
+ "ExtC <%p> %@"
+ "ExtI <%p> %@"
+ "ExtP <%p> %d"
+ "Extension XPC start failed with %@"
+ "Extension already running: %@"
+ "ExtensionProcessWithConfiguration failed with %@"
+ "Extensions [ %@ ]"
+ "Found %lu extensions for '%@'"
+ "Found extension with bundleID '%@', extensionParentID '%@'"
+ "Ignoring extension with parent bundleID mismatch: expected '%@' vs '%@'"
+ "Ignoring extension without entitlement: '%@'"
+ "InfoBlob"
+ "Internet"
+ "Invalid ciphersuite: "
+ "Invalidate %@"
+ "InvalidateReason %@"
+ "Invalidated %@, XPC connection ended: PID %d"
+ "KeyExchange"
+ "Local"
+ "ML-KEM768 with X25519"
+ "NSObject"
+ "NotAuthorized"
+ "PID %d"
+ "PrivateKey"
+ "PrivateKeyFromCryptoInfo info failed with nil key: "
+ "PublicKey"
+ "Q24@0:8@16"
+ "Received accessory event with nil transport extension"
+ "RecipientKeyFromCryptoInfo failed with nil key: "
+ "Removed session '%@' from %@"
+ "Searching for %@ extension with bundleID '%@'"
+ "SesLI"
+ "SessionRefCount"
+ "Sessions %lu"
+ "Skip running extension with type %@"
+ "T#,R"
+ "T@\"DACryptoInfo\",C,N,V_cryptoInfo"
+ "T@\"NSData\",C,N,V_accessoryKey"
+ "T@\"NSData\",C,N,V_context"
+ "T@\"NSData\",C,N,V_data"
+ "T@\"NSData\",C,N,V_info"
+ "T@\"NSData\",C,N,V_key"
+ "T@\"NSData\",C,N,V_privateKey"
+ "T@\"NSData\",C,N,V_publicKey"
+ "T@\"NSMutableSet\",R,C,N,V_sessionSet"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N"
+ "T@\"NSString\",R,C"
+ "T@\"NSString\",R,C,N,V_bundleID"
+ "TB,R,N,V_secureConnectionPairing"
+ "TQ,N,V_ciphersuite"
+ "TQ,R"
+ "Ti,N,V_pid"
+ "Tq,R,N,V_transportType"
+ "Tq,R,N,V_type"
+ "TransportType %@"
+ "Type %@"
+ "Update %@: %@"
+ "Vv16@0:8"
+ "XPC report event to %@ extension: %@, queue: %@"
+ "XWingMLKEM768X25519"
+ "[BadParameter] ciphertext cannot be nil"
+ "[BadParameter] crypto info cannot be nil"
+ "[BadParameter] plaintext cannot be nil"
+ "^{_NSZone=}16@0:8"
+ "_TtC12DeviceAccess18DACryptoKitManager"
+ "_accessoryKey"
+ "_activated"
+ "_ciphersuite"
+ "_clientInvalidated"
+ "_context"
+ "_cryptoInfo"
+ "_data"
+ "_ekExtensionProcess"
+ "_ekHostConfiguration"
+ "_extensionActivatedWithType:transportType:"
+ "_extensionEnsureStartedWithType:transportType:"
+ "_extensionEnsureStoppedWithType:transportType:"
+ "_extensionInvalidatedWithType:transportType:"
+ "_extensionMap"
+ "_extensionShouldRunWithType:transportType:"
+ "_extensionWithType:transportType:"
+ "_findExtensionWithType:transportType:completion:"
+ "_handleAccessoryTransportEvent:transportType:"
+ "_handleAccessoryTransportInternetEvent:"
+ "_handleAccessoryTransportLocalEvent:"
+ "_handleEvent:type:transportType:"
+ "_info"
+ "_invalidateExtensions"
+ "_invalidateReason"
+ "_key"
+ "_performKeyExchange"
+ "_pid"
+ "_privateKey"
+ "_publicKey"
+ "_relaunchExtensions"
+ "_reportEventToSessions:"
+ "_secureConnectionPairing"
+ "_sessionAdded"
+ "_sessionSet"
+ "_transportType"
+ "_update"
+ "accessoryKey"
+ "addSession:"
+ "autorelease"
+ "ciAK"
+ "ciCS"
+ "ciIB"
+ "ciID"
+ "ciPr"
+ "ciPu"
+ "ciphersuite"
+ "class"
+ "cnSt"
+ "code"
+ "com.apple.accessory-transport-extension"
+ "com.apple.dautil"
+ "com.apple.developer.accessory-transport-extension"
+ "com.apple.developer.wifi-infrastructure.WiFiNetworkSharingExtension"
+ "com.apple.media-device-discovery.network-sharing"
+ "com.apple.server.bluetooth.le.att.xpc"
+ "componentsJoinedByString:"
+ "conformsToProtocol:"
+ "containsObject:"
+ "context"
+ "crIn"
+ "createCryptoInfoForDevice:suite:error:"
+ "cryptoInfo"
+ "debugDescription"
+ "decryptData:withCryptoInfo:encapsulatedKey:error:"
+ "device cannot be nil"
+ "dictionaryRepresentation"
+ "didReceiveEvent:"
+ "dvIT"
+ "encryptData:withCryptoInfo:encapsulatedKey:error:"
+ "exDI"
+ "exDK"
+ "exDa"
+ "execute:"
+ "executeQuery:"
+ "extensionProcessWithConfiguration:error:"
+ "getExtensionPidByType:transport:"
+ "i16@0:8"
+ "i32@0:8q16q24"
+ "info"
+ "initWithBluetoothIdentifier:pairedCTKD:appConfirmsAuth:pairingRequired:btSCPairing:"
+ "initWithCoordinator:ekExtension:type:transportType:"
+ "initWithDevice:bundleID:"
+ "initWithDevice:data:key:"
+ "initWithDevice:publicKey:"
+ "initWithDevice:publicKey:context:"
+ "initWithDictionary:error:"
+ "initWithExplanation:"
+ "initWithExtensionIdentity:instanceIdentifier:"
+ "initWithIdentifier:"
+ "initWithPredicate:context:"
+ "instanceIdentifier"
+ "isKindOfClass:"
+ "isProxy"
+ "key"
+ "keychainType"
+ "missing bundle identifier"
+ "missing device identifier"
+ "nil device identifier: "
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "pid"
+ "predicateMatchingIdentifier:"
+ "privateKey"
+ "publicKey"
+ "release"
+ "removeSession:"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "runProximitySetupWithDiscovery:"
+ "secureConnectionPairing"
+ "self"
+ "sessionSet"
+ "setAccessoryKey:"
+ "setCiphersuite:"
+ "setContext:"
+ "setCryptoInfo:"
+ "setData:"
+ "setExtensionIdentity:"
+ "setInfo:"
+ "setKey:"
+ "setPid:"
+ "setPrivateKey:"
+ "setPublicKey:"
+ "slcR"
+ "startExtension:bundleID:"
+ "stopExtension"
+ "superclass"
+ "transportType"
+ "uniqueIdentifier"
+ "update"
+ "v16@?0@\"_EXExtensionIdentity\"8"
+ "v20@0:8i16"
+ "v24@0:8@\"DAEventExtension\"16"
+ "v24@0:8@\"NSString\"16"
+ "v32@0:8@\"DADevice\"16@\"NSString\"24"
+ "v32@0:8@16q24"
+ "v32@0:8q16q24"
+ "v40@0:8@16q24q32"
+ "v40@0:8q16q24@?32"
+ "zone"
- "@36@0:8@16B24B28B32"
- "initWithBluetoothIdentifier:pairedCTKD:appConfirmsAuth:pairingRequired:"

```
