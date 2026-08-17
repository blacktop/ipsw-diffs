## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/Versions/A/SPOwner`

```diff

 423.26.4.19.2
-  __TEXT.__text: 0x80c08
-  __TEXT.__auth_stubs: 0xb20
-  __TEXT.__objc_methlist: 0xb344
-  __TEXT.__cstring: 0x6557
-  __TEXT.__const: 0x498
+  __TEXT.__text: 0x82b64
+  __TEXT.__auth_stubs: 0xb50
+  __TEXT.__objc_methlist: 0xb7f4
+  __TEXT.__cstring: 0x6727
+  __TEXT.__const: 0x578
   __TEXT.__gcc_except_tab: 0x1ccc
-  __TEXT.__oslogstring: 0x7858
-  __TEXT.__swift5_typeref: 0x124
+  __TEXT.__oslogstring: 0x78a8
+  __TEXT.__constg_swiftt: 0x128
+  __TEXT.__swift5_typeref: 0x12e
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_reflstr: 0x85
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__swift5_proto: 0x3c
+  __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_fieldmd: 0xfc
-  __TEXT.__constg_swiftt: 0xfc
-  __TEXT.__swift5_reflstr: 0x75
-  __TEXT.__swift5_proto: 0x30
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift5_capture: 0x60
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__unwind_info: 0x2798
-  __TEXT.__eh_frame: 0x2c0
-  __TEXT.__objc_classname: 0x138e
-  __TEXT.__objc_methname: 0x130af
-  __TEXT.__objc_methtype: 0x3918
-  __TEXT.__objc_stubs: 0xab20
-  __DATA_CONST.__got: 0x5b8
-  __DATA_CONST.__const: 0x860
-  __DATA_CONST.__objc_classlist: 0x430
-  __DATA_CONST.__objc_protolist: 0x1b8
+  __TEXT.__unwind_info: 0x2848
+  __TEXT.__eh_frame: 0x330
+  __TEXT.__objc_classname: 0x143e
+  __TEXT.__objc_methname: 0x13241
+  __TEXT.__objc_methtype: 0x3998
+  __TEXT.__objc_stubs: 0xac00
+  __DATA_CONST.__got: 0x5c8
+  __DATA_CONST.__const: 0x870
+  __DATA_CONST.__objc_classlist: 0x450
+  __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ba0
-  __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x358
+  __DATA_CONST.__objc_selrefs: 0x3c08
+  __DATA_CONST.__objc_protorefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0x378
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x5a0
-  __AUTH_CONST.__const: 0x2111
-  __AUTH_CONST.__cfstring: 0x5d60
-  __AUTH_CONST.__objc_const: 0x13540
+  __AUTH_CONST.__auth_got: 0x5b8
+  __AUTH_CONST.__const: 0x2191
+  __AUTH_CONST.__cfstring: 0x5de0
+  __AUTH_CONST.__objc_const: 0x13f40
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x10d8
-  __DATA.__objc_ivar: 0xe44
-  __DATA.__data: 0x14d8
-  __DATA.__bss: 0x5a0
+  __AUTH.__objc_data: 0x1218
+  __DATA.__objc_ivar: 0xec4
+  __DATA.__data: 0x1608
+  __DATA.__bss: 0x730
   __DATA_DIRTY.__objc_data: 0x1918
   __DATA_DIRTY.__data: 0x1b8
   __DATA_DIRTY.__bss: 0x368

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4178
-  Symbols:   8519
-  CStrings:  4813
+  Functions: 4286
+  Symbols:   8711
+  CStrings:  4855
 
Symbols:
+ +[SPIntentSessionContext deviceListUseCase]
+ +[SPIntentSessionContext itemListUseCase]
+ +[SPIntentSessionContext supportsSecureCoding]
+ +[SPSimpleBeaconContext unifiedBeaconContext]
+ +[SPUnifiedSupportSession beaconsChanges:]
+ +[SPUnifiedSupportSession unifiedBeacons:]
+ -[SPIntentSession .cxx_destruct]
+ -[SPIntentSession context]
+ -[SPIntentSession init]
+ -[SPIntentSession proxy]
+ -[SPIntentSession remoteInterface]
+ -[SPIntentSession serviceDescription]
+ -[SPIntentSession session]
+ -[SPIntentSession setContext:]
+ -[SPIntentSession setProxy:]
+ -[SPIntentSession setServiceDescription:]
+ -[SPIntentSession setSession:]
+ -[SPIntentSession startSessionWithContext:completion:]
+ -[SPIntentSession stopSessionWithCompletion:]
+ -[SPIntentSessionContext .cxx_destruct]
+ -[SPIntentSessionContext copyWithZone:]
+ -[SPIntentSessionContext encodeWithCoder:]
+ -[SPIntentSessionContext identifier]
+ -[SPIntentSessionContext initWithCoder:]
+ -[SPIntentSessionContext initWithUseCase:]
+ -[SPIntentSessionContext setIdentifier:]
+ -[SPIntentSessionContext setUseCase:]
+ -[SPIntentSessionContext useCase]
+ -[SPOwnerInterface unifiedSupportSession]
+ -[SPUnifiedBeacon .cxx_destruct]
+ -[SPUnifiedBeacon accessoryProductInfo]
+ -[SPUnifiedBeacon batteryLevel]
+ -[SPUnifiedBeacon batteryPercentage]
+ -[SPUnifiedBeacon connected]
+ -[SPUnifiedBeacon deviceClass]
+ -[SPUnifiedBeacon deviceColor]
+ -[SPUnifiedBeacon deviceDisplayName]
+ -[SPUnifiedBeacon deviceModel]
+ -[SPUnifiedBeacon deviceVariant]
+ -[SPUnifiedBeacon groupIdentifier]
+ -[SPUnifiedBeacon identifier]
+ -[SPUnifiedBeacon initWithInternalSimpleBeacon:]
+ -[SPUnifiedBeacon isMine]
+ -[SPUnifiedBeacon lostModeInfo]
+ -[SPUnifiedBeacon lowPowerMode]
+ -[SPUnifiedBeacon multipartStatus]
+ -[SPUnifiedBeacon name]
+ -[SPUnifiedBeacon online]
+ -[SPUnifiedBeacon owner]
+ -[SPUnifiedBeacon partIdentifier]
+ -[SPUnifiedBeacon rawDeviceModel]
+ -[SPUnifiedBeacon role]
+ -[SPUnifiedBeacon setAccessoryProductInfo:]
+ -[SPUnifiedBeacon setBatteryLevel:]
+ -[SPUnifiedBeacon setBatteryPercentage:]
+ -[SPUnifiedBeacon setConnected:]
+ -[SPUnifiedBeacon setDeviceClass:]
+ -[SPUnifiedBeacon setDeviceColor:]
+ -[SPUnifiedBeacon setDeviceDisplayName:]
+ -[SPUnifiedBeacon setDeviceModel:]
+ -[SPUnifiedBeacon setDeviceVariant:]
+ -[SPUnifiedBeacon setGroupIdentifier:]
+ -[SPUnifiedBeacon setIdentifier:]
+ -[SPUnifiedBeacon setIsMine:]
+ -[SPUnifiedBeacon setLostModeInfo:]
+ -[SPUnifiedBeacon setLowPowerMode:]
+ -[SPUnifiedBeacon setMultipartStatus:]
+ -[SPUnifiedBeacon setName:]
+ -[SPUnifiedBeacon setOnline:]
+ -[SPUnifiedBeacon setOwner:]
+ -[SPUnifiedBeacon setPartIdentifier:]
+ -[SPUnifiedBeacon setRawDeviceModel:]
+ -[SPUnifiedBeacon setRole:]
+ -[SPUnifiedBeacon setTaskInformation:]
+ -[SPUnifiedBeacon setThisDevice:]
+ -[SPUnifiedBeacon setType:]
+ -[SPUnifiedBeacon taskInformation]
+ -[SPUnifiedBeacon thisDevice]
+ -[SPUnifiedBeacon type]
+ -[SPUnifiedSupportSession .cxx_destruct]
+ -[SPUnifiedSupportSession init]
+ -[SPUnifiedSupportSession queue]
+ -[SPUnifiedSupportSession registerSimpleBeaconInterfaceWithContext:collectionDifference:completion:]
+ -[SPUnifiedSupportSession setQueue:]
+ -[SPUnifiedSupportSession setSimpleBeaconUpdateInterface:]
+ -[SPUnifiedSupportSession simpleBeaconUpdateInterface]
+ -[SPUnifiedSupportSession startUpdatingBeaconsWithContext:collectionDifference:completion:]
+ -[SPUnifiedSupportSession stopUpdatingBeaconsWithCompletion:]
+ -[SPUnifiedSupportSession unifiedBeacons]
+ LogCategory_UnifiedSupport
+ LogCategory_UnifiedSupport.log
+ LogCategory_UnifiedSupport.onceToken
+ OBJC_IVAR_$_SPIntentSession._context
+ OBJC_IVAR_$_SPIntentSession._proxy
+ OBJC_IVAR_$_SPIntentSession._serviceDescription
+ OBJC_IVAR_$_SPIntentSession._session
+ OBJC_IVAR_$_SPIntentSessionContext._identifier
+ OBJC_IVAR_$_SPIntentSessionContext._useCase
+ OBJC_IVAR_$_SPUnifiedBeacon._accessoryProductInfo
+ OBJC_IVAR_$_SPUnifiedBeacon._batteryLevel
+ OBJC_IVAR_$_SPUnifiedBeacon._batteryPercentage
+ OBJC_IVAR_$_SPUnifiedBeacon._connected
+ OBJC_IVAR_$_SPUnifiedBeacon._deviceClass
+ OBJC_IVAR_$_SPUnifiedBeacon._deviceColor
+ OBJC_IVAR_$_SPUnifiedBeacon._deviceDisplayName
+ OBJC_IVAR_$_SPUnifiedBeacon._deviceModel
+ OBJC_IVAR_$_SPUnifiedBeacon._deviceVariant
+ OBJC_IVAR_$_SPUnifiedBeacon._groupIdentifier
+ OBJC_IVAR_$_SPUnifiedBeacon._identifier
+ OBJC_IVAR_$_SPUnifiedBeacon._isMine
+ OBJC_IVAR_$_SPUnifiedBeacon._lostModeInfo
+ OBJC_IVAR_$_SPUnifiedBeacon._lowPowerMode
+ OBJC_IVAR_$_SPUnifiedBeacon._multipartStatus
+ OBJC_IVAR_$_SPUnifiedBeacon._name
+ OBJC_IVAR_$_SPUnifiedBeacon._online
+ OBJC_IVAR_$_SPUnifiedBeacon._owner
+ OBJC_IVAR_$_SPUnifiedBeacon._partIdentifier
+ OBJC_IVAR_$_SPUnifiedBeacon._rawDeviceModel
+ OBJC_IVAR_$_SPUnifiedBeacon._role
+ OBJC_IVAR_$_SPUnifiedBeacon._taskInformation
+ OBJC_IVAR_$_SPUnifiedBeacon._thisDevice
+ OBJC_IVAR_$_SPUnifiedBeacon._type
+ OBJC_IVAR_$_SPUnifiedSupportSession._queue
+ OBJC_IVAR_$_SPUnifiedSupportSession._simpleBeaconUpdateInterface
+ _LogCategory_UnifiedSupport
+ _OBJC_CLASS_$_SPIntentSession
+ _OBJC_CLASS_$_SPIntentSessionContext
+ _OBJC_CLASS_$_SPUnifiedBeacon
+ _OBJC_CLASS_$_SPUnifiedSupportSession
+ _OBJC_METACLASS_$_SPIntentSession
+ _OBJC_METACLASS_$_SPIntentSessionContext
+ _OBJC_METACLASS_$_SPUnifiedBeacon
+ _OBJC_METACLASS_$_SPUnifiedSupportSession
+ _SPIntentSessionErrorDomain
+ _SPUnifiedSupportErrorDomain
+ __OBJC_$_CLASS_METHODS_SPIntentSessionContext
+ __OBJC_$_CLASS_METHODS_SPUnifiedSupportSession
+ __OBJC_$_CLASS_PROP_LIST_SPIntentSessionContext
+ __OBJC_$_INSTANCE_METHODS_SPIntentSession
+ __OBJC_$_INSTANCE_METHODS_SPIntentSessionContext
+ __OBJC_$_INSTANCE_METHODS_SPUnifiedBeacon
+ __OBJC_$_INSTANCE_METHODS_SPUnifiedSupportSession
+ __OBJC_$_INSTANCE_VARIABLES_SPIntentSession
+ __OBJC_$_INSTANCE_VARIABLES_SPIntentSessionContext
+ __OBJC_$_INSTANCE_VARIABLES_SPUnifiedBeacon
+ __OBJC_$_INSTANCE_VARIABLES_SPUnifiedSupportSession
+ __OBJC_$_PROP_LIST_SPIntentSession
+ __OBJC_$_PROP_LIST_SPIntentSessionContext
+ __OBJC_$_PROP_LIST_SPUnifiedBeacon
+ __OBJC_$_PROP_LIST_SPUnifiedSupportProtocol
+ __OBJC_$_PROP_LIST_SPUnifiedSupportSession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SPIntentSessionProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SPUnifiedSupportProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SPIntentSessionProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SPUnifiedSupportProtocol
+ __OBJC_$_PROTOCOL_REFS_SPIntentSessionClientXPCProtocol
+ __OBJC_$_PROTOCOL_REFS_SPIntentSessionProtocol
+ __OBJC_$_PROTOCOL_REFS_SPUnifiedSupportProtocol
+ __OBJC_CLASS_PROTOCOLS_$_SPIntentSession
+ __OBJC_CLASS_PROTOCOLS_$_SPIntentSessionContext
+ __OBJC_CLASS_PROTOCOLS_$_SPUnifiedSupportSession
+ __OBJC_CLASS_RO_$_SPIntentSession
+ __OBJC_CLASS_RO_$_SPIntentSessionContext
+ __OBJC_CLASS_RO_$_SPUnifiedBeacon
+ __OBJC_CLASS_RO_$_SPUnifiedSupportSession
+ __OBJC_LABEL_PROTOCOL_$_SPIntentSessionClientXPCProtocol
+ __OBJC_LABEL_PROTOCOL_$_SPIntentSessionProtocol
+ __OBJC_LABEL_PROTOCOL_$_SPUnifiedSupportProtocol
+ __OBJC_METACLASS_RO_$_SPIntentSession
+ __OBJC_METACLASS_RO_$_SPIntentSessionContext
+ __OBJC_METACLASS_RO_$_SPUnifiedBeacon
+ __OBJC_METACLASS_RO_$_SPUnifiedSupportSession
+ __OBJC_PROTOCOL_$_SPIntentSessionClientXPCProtocol
+ __OBJC_PROTOCOL_$_SPIntentSessionProtocol
+ __OBJC_PROTOCOL_$_SPUnifiedSupportProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_SPIntentSessionProtocol
+ ___100-[SPUnifiedSupportSession registerSimpleBeaconInterfaceWithContext:collectionDifference:completion:]_block_invoke
+ ___42+[SPUnifiedSupportSession beaconsChanges:]_block_invoke
+ ___42+[SPUnifiedSupportSession unifiedBeacons:]_block_invoke
+ ___61-[SPUnifiedSupportSession stopUpdatingBeaconsWithCompletion:]_block_invoke
+ ___91-[SPUnifiedSupportSession startUpdatingBeaconsWithContext:collectionDifference:completion:]_block_invoke
+ ___LogCategory_UnifiedSupport_block_invoke
+ _objc_msgSend$initWithUseCase:
+ _objc_msgSend$setUseCase:
+ _objc_msgSend$simpleBeacons
+ _objc_msgSend$startSessionWithContext:completion:
+ _objc_msgSend$stopSessionWithContext:completion:
+ _objc_msgSend$unifiedBeacons:
+ _objc_msgSend$useCase
+ _swift_getForeignTypeMetadata
+ _symbolic Si
+ _symbolic _____ So20SPDeviceImageVariantV
CStrings:
+ "-[SPUnifiedSupportSession startUpdatingBeaconsWithContext:collectionDifference:completion:]"
+ "-[SPUnifiedSupportSession stopUpdatingBeaconsWithCompletion:]"
+ "@\"<SPIntentSessionProtocol>\""
+ "@\"NSArray\"16@0:8"
+ "@\"SPIntentSessionContext\""
+ "SPIntentSession"
+ "SPIntentSessionClientXPCProtocol"
+ "SPIntentSessionContext"
+ "SPIntentSessionProtocol"
+ "SPUnifiedBeacon"
+ "SPUnifiedSupportProtocol"
+ "SPUnifiedSupportSession"
+ "T@\"<SPIntentSessionProtocol>\",&,N,V_proxy"
+ "T@\"SPIntentSessionContext\",&,N,V_context"
+ "TQ,N,V_useCase"
+ "Tq,N,V_deviceVariant"
+ "Unexpected number of multipart groups"
+ "Unexpected partIdentifier: %ld"
+ "_deviceVariant"
+ "_useCase"
+ "caseLidOpenLeftInside"
+ "caseLidOpenLeftRightInside"
+ "caseLidOpenRightInside"
+ "com.apple.SPOwner.SPUnifiedSupport.ErrorDomain"
+ "com.apple.SPOwner.SPUnifiedSupportSession"
+ "com.apple.icloud.searchpartyd.SPIntentSession.ErrorDomain"
+ "com.apple.icloud.searchpartyd.intentsession"
+ "deviceListUseCase"
+ "deviceVariant"
+ "initWithUseCase:"
+ "itemListUseCase"
+ "setDeviceVariant:"
+ "setUseCase:"
+ "startSessionWithContext:completion:"
+ "stopSessionWithCompletion:"
+ "stopSessionWithContext:completion:"
+ "unifiedBeaconContext"
+ "unifiedBeacons"
+ "unifiedSupport"
+ "unifiedSupportSession"
+ "useCase"
+ "v32@0:8@\"SPIntentSessionContext\"16@?<v@?@\"NSError\">24"
```
