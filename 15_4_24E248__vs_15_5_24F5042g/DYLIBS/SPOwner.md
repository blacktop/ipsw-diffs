## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/Versions/A/SPOwner`

```diff

-396.24.7.11.41
-  __TEXT.__text: 0x7ab54
+396.25.2.11.11
+  __TEXT.__text: 0x7cb28
   __TEXT.__auth_stubs: 0xb20
-  __TEXT.__objc_methlist: 0xaddc
-  __TEXT.__cstring: 0x6457
+  __TEXT.__objc_methlist: 0xb33c
+  __TEXT.__cstring: 0x6637
   __TEXT.__const: 0x440
-  __TEXT.__oslogstring: 0x74e8
-  __TEXT.__gcc_except_tab: 0x1b24
+  __TEXT.__gcc_except_tab: 0x1b3c
+  __TEXT.__oslogstring: 0x75c8
   __TEXT.__swift5_typeref: 0x124
   __TEXT.__swift5_fieldmd: 0xfc
   __TEXT.__constg_swiftt: 0xfc

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift5_capture: 0x50
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__unwind_info: 0x22f0
+  __TEXT.__unwind_info: 0x2380
   __TEXT.__eh_frame: 0x278
-  __TEXT.__objc_classname: 0x1278
-  __TEXT.__objc_methname: 0x125c4
-  __TEXT.__objc_methtype: 0x3891
-  __TEXT.__objc_stubs: 0xa7c0
-  __DATA_CONST.__got: 0x5a0
-  __DATA_CONST.__const: 0x860
-  __DATA_CONST.__objc_classlist: 0x408
-  __DATA_CONST.__objc_protolist: 0x1b8
+  __TEXT.__objc_classname: 0x1350
+  __TEXT.__objc_methname: 0x12737
+  __TEXT.__objc_methtype: 0x3938
+  __TEXT.__objc_stubs: 0xa8c0
+  __DATA_CONST.__got: 0x5b8
+  __DATA_CONST.__const: 0x870
+  __DATA_CONST.__objc_classlist: 0x430
+  __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3978
-  __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x338
+  __DATA_CONST.__objc_selrefs: 0x39d8
+  __DATA_CONST.__objc_protorefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x5a0
   __AUTH_CONST.__auth_ptr: 0x120
-  __AUTH_CONST.__const: 0x2080
-  __AUTH_CONST.__cfstring: 0x5a60
-  __AUTH_CONST.__objc_const: 0x12ad8
+  __AUTH_CONST.__const: 0x2120
+  __AUTH_CONST.__cfstring: 0x5b00
+  __AUTH_CONST.__objc_const: 0x135c8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1960
+  __AUTH.__objc_data: 0x1af0
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0xdb4
-  __DATA.__data: 0x1568
-  __DATA.__bss: 0x8e0
+  __DATA.__objc_ivar: 0xe38
+  __DATA.__data: 0x16e8
+  __DATA.__bss: 0x910
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0xf00
   __DATA_DIRTY.__bss: 0x40

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4034
-  Symbols:   8581
-  CStrings:  5091
+  Functions: 4150
+  Symbols:   8815
+  CStrings:  5138
 
Symbols:
+ +[SPIntentSessionContext deviceListUseCase]
+ +[SPIntentSessionContext itemListUseCase]
+ +[SPIntentSessionContext supportsSecureCoding]
+ +[SPSimpleBeaconContext unifiedBeaconContext]
+ +[SPUnifiedSupportSession beaconsChanges:]
+ +[SPUnifiedSupportSession unifiedBeacons:]
+ +[ServerDrivenStrings exportedInterface]
+ +[ServerDrivenStrings remoteInterface]
+ +[ServerDrivenStrings remoteInterface].cold.1
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
+ -[SPUnifiedBeacon role]
+ -[SPUnifiedBeacon setAccessoryProductInfo:]
+ -[SPUnifiedBeacon setBatteryLevel:]
+ -[SPUnifiedBeacon setBatteryPercentage:]
+ -[SPUnifiedBeacon setConnected:]
+ -[SPUnifiedBeacon setDeviceClass:]
+ -[SPUnifiedBeacon setDeviceColor:]
+ -[SPUnifiedBeacon setDeviceDisplayName:]
+ -[SPUnifiedBeacon setDeviceModel:]
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
+ -[ServerDrivenStrings .cxx_destruct]
+ -[ServerDrivenStrings fetchTheftAndLossStrings:completion:]
+ -[ServerDrivenStrings init]
+ -[ServerDrivenStrings interruptionHandler:]
+ -[ServerDrivenStrings invalidationHandler:]
+ -[ServerDrivenStrings proxy]
+ -[ServerDrivenStrings queue]
+ -[ServerDrivenStrings serviceDescription]
+ -[ServerDrivenStrings session]
+ -[ServerDrivenStrings setQueue:]
+ -[ServerDrivenStrings setServiceDescription:]
+ -[ServerDrivenStrings setSession:]
+ LogCategory_ServerStrings.cold.1
+ LogCategory_ServerStrings.log
+ LogCategory_ServerStrings.onceToken
+ LogCategory_UnifiedSupport.cold.1
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
+ OBJC_IVAR_$_SPUnifiedBeacon._role
+ OBJC_IVAR_$_SPUnifiedBeacon._taskInformation
+ OBJC_IVAR_$_SPUnifiedBeacon._thisDevice
+ OBJC_IVAR_$_SPUnifiedBeacon._type
+ OBJC_IVAR_$_SPUnifiedSupportSession._queue
+ OBJC_IVAR_$_SPUnifiedSupportSession._simpleBeaconUpdateInterface
+ OBJC_IVAR_$_ServerDrivenStrings._queue
+ OBJC_IVAR_$_ServerDrivenStrings._serviceDescription
+ OBJC_IVAR_$_ServerDrivenStrings._session
+ _LogCategory_ServerStrings
+ _LogCategory_UnifiedSupport
+ _OBJC_CLASS_$_SPIntentSession
+ _OBJC_CLASS_$_SPIntentSessionContext
+ _OBJC_CLASS_$_SPUnifiedBeacon
+ _OBJC_CLASS_$_SPUnifiedSupportSession
+ _OBJC_CLASS_$_ServerDrivenStrings
+ _OBJC_METACLASS_$_SPIntentSession
+ _OBJC_METACLASS_$_SPIntentSessionContext
+ _OBJC_METACLASS_$_SPUnifiedBeacon
+ _OBJC_METACLASS_$_SPUnifiedSupportSession
+ _OBJC_METACLASS_$_ServerDrivenStrings
+ _SPIntentSessionErrorDomain
+ _SPUnifiedSupportErrorDomain
+ __27-[ServerDrivenStrings init]_block_invoke.1
+ __59-[ServerDrivenStrings fetchTheftAndLossStrings:completion:]_block_invoke.52
+ __OBJC_$_CLASS_METHODS_SPIntentSessionContext
+ __OBJC_$_CLASS_METHODS_SPUnifiedSupportSession
+ __OBJC_$_CLASS_METHODS_ServerDrivenStrings
+ __OBJC_$_CLASS_PROP_LIST_SPIntentSessionContext
+ __OBJC_$_INSTANCE_METHODS_SPIntentSession
+ __OBJC_$_INSTANCE_METHODS_SPIntentSessionContext
+ __OBJC_$_INSTANCE_METHODS_SPUnifiedBeacon
+ __OBJC_$_INSTANCE_METHODS_SPUnifiedSupportSession
+ __OBJC_$_INSTANCE_METHODS_ServerDrivenStrings
+ __OBJC_$_INSTANCE_VARIABLES_SPIntentSession
+ __OBJC_$_INSTANCE_VARIABLES_SPIntentSessionContext
+ __OBJC_$_INSTANCE_VARIABLES_SPUnifiedBeacon
+ __OBJC_$_INSTANCE_VARIABLES_SPUnifiedSupportSession
+ __OBJC_$_INSTANCE_VARIABLES_ServerDrivenStrings
+ __OBJC_$_PROP_LIST_SPIntentSession
+ __OBJC_$_PROP_LIST_SPIntentSessionContext
+ __OBJC_$_PROP_LIST_SPUnifiedBeacon
+ __OBJC_$_PROP_LIST_SPUnifiedSupportProtocol
+ __OBJC_$_PROP_LIST_SPUnifiedSupportSession
+ __OBJC_$_PROP_LIST_ServerDrivenStrings
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SPIntentSessionProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SPUnifiedSupportProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ServerDrivenStringsXPCProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SPIntentSessionProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SPUnifiedSupportProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ServerDrivenStringsXPCProtocol
+ __OBJC_$_PROTOCOL_REFS_SPIntentSessionClientXPCProtocol
+ __OBJC_$_PROTOCOL_REFS_SPIntentSessionProtocol
+ __OBJC_$_PROTOCOL_REFS_SPUnifiedSupportProtocol
+ __OBJC_$_PROTOCOL_REFS_ServerDrivenStringsXPCProtocol
+ __OBJC_CLASS_PROTOCOLS_$_SPIntentSession
+ __OBJC_CLASS_PROTOCOLS_$_SPIntentSessionContext
+ __OBJC_CLASS_PROTOCOLS_$_SPUnifiedSupportSession
+ __OBJC_CLASS_RO_$_SPIntentSession
+ __OBJC_CLASS_RO_$_SPIntentSessionContext
+ __OBJC_CLASS_RO_$_SPUnifiedBeacon
+ __OBJC_CLASS_RO_$_SPUnifiedSupportSession
+ __OBJC_CLASS_RO_$_ServerDrivenStrings
+ __OBJC_LABEL_PROTOCOL_$_SPIntentSessionClientXPCProtocol
+ __OBJC_LABEL_PROTOCOL_$_SPIntentSessionProtocol
+ __OBJC_LABEL_PROTOCOL_$_SPUnifiedSupportProtocol
+ __OBJC_LABEL_PROTOCOL_$_ServerDrivenStringsXPCProtocol
+ __OBJC_METACLASS_RO_$_SPIntentSession
+ __OBJC_METACLASS_RO_$_SPIntentSessionContext
+ __OBJC_METACLASS_RO_$_SPUnifiedBeacon
+ __OBJC_METACLASS_RO_$_SPUnifiedSupportSession
+ __OBJC_METACLASS_RO_$_ServerDrivenStrings
+ __OBJC_PROTOCOL_$_SPIntentSessionClientXPCProtocol
+ __OBJC_PROTOCOL_$_SPIntentSessionProtocol
+ __OBJC_PROTOCOL_$_SPUnifiedSupportProtocol
+ __OBJC_PROTOCOL_$_ServerDrivenStringsXPCProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_SPIntentSessionProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ServerDrivenStringsXPCProtocol
+ ___100-[SPUnifiedSupportSession registerSimpleBeaconInterfaceWithContext:collectionDifference:completion:]_block_invoke
+ ___27-[ServerDrivenStrings init]_block_invoke
+ ___38+[ServerDrivenStrings remoteInterface]_block_invoke
+ ___42+[SPUnifiedSupportSession beaconsChanges:]_block_invoke
+ ___42+[SPUnifiedSupportSession unifiedBeacons:]_block_invoke
+ ___59-[ServerDrivenStrings fetchTheftAndLossStrings:completion:]_block_invoke
+ ___61-[SPUnifiedSupportSession stopUpdatingBeaconsWithCompletion:]_block_invoke
+ ___91-[SPUnifiedSupportSession startUpdatingBeaconsWithContext:collectionDifference:completion:]_block_invoke
+ ___LogCategory_ServerStrings_block_invoke
+ ___LogCategory_UnifiedSupport_block_invoke
+ __block_literal_global.64
+ __block_literal_global.67
+ __block_literal_global.9
+ _objc_msgSend$fetchTheftAndLossStrings:completion:
+ _objc_msgSend$initWithUseCase:
+ _objc_msgSend$setUseCase:
+ _objc_msgSend$simpleBeacons
+ _objc_msgSend$startSessionWithContext:completion:
+ _objc_msgSend$stopSessionWithContext:completion:
+ _objc_msgSend$unifiedBeacons:
+ _objc_msgSend$useCase
CStrings:
+ "\x1b\x11\x16"
+ "-[SPUnifiedSupportSession startUpdatingBeaconsWithContext:collectionDifference:completion:]"
+ "-[SPUnifiedSupportSession stopUpdatingBeaconsWithCompletion:]"
+ "@\"<SPIntentSessionProtocol>\""
+ "@\"NSArray\"16@0:8"
+ "@\"SPIntentSessionContext\""
+ "Fetching server strings"
+ "SPIntentSession"
+ "SPIntentSessionClientXPCProtocol"
+ "SPIntentSessionContext"
+ "SPIntentSessionProtocol"
+ "SPUnifiedBeacon"
+ "SPUnifiedSupportProtocol"
+ "SPUnifiedSupportSession"
+ "ServerDrivenMetaData: interruptionHandler called"
+ "ServerDrivenMetaData: invalidationHandler called"
+ "ServerDrivenStrings"
+ "ServerDrivenStrings.fetchTheftAndLossStrings"
+ "ServerDrivenStringsXPCProtocol"
+ "ServerSettings: Establishing XPC connection to %@"
+ "T@\"<SPIntentSessionProtocol>\",&,N,V_proxy"
+ "T@\"SPIntentSessionContext\",&,N,V_context"
+ "TQ,N,V_useCase"
+ "_useCase"
+ "com.apple.SPOwner.SPUnifiedSupport.ErrorDomain"
+ "com.apple.SPOwner.SPUnifiedSupportSession"
+ "com.apple.findmy.serverDrivenStrings"
+ "com.apple.icloud.searchpartyd.SPIntentSession.ErrorDomain"
+ "com.apple.icloud.searchpartyd.intentsession"
+ "com.apple.icloud.searchpartyd.serverDrivenStrings"
+ "deviceListUseCase"
+ "fetchTheftAndLossStrings:completion:"
+ "initWithUseCase:"
+ "itemListUseCase"
+ "serverDrivenStrings"
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
+ "v32@0:8q16@?<v@?@\"NSString\"@\"NSError\">24"

```
