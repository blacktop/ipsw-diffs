## CryptoTokenKit

> `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit`

```diff

-738.100.34.0.0
-  __TEXT.__text: 0x40f1c
-  __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_methlist: 0x3dfc
-  __TEXT.__gcc_except_tab: 0x1594
-  __TEXT.__const: 0x258
-  __TEXT.__cstring: 0x29a9
-  __TEXT.__oslogstring: 0x2f49
+805.0.5.0.1
+  __TEXT.__text: 0x45af0
+  __TEXT.__auth_stubs: 0xc20
+  __TEXT.__objc_methlist: 0x442c
+  __TEXT.__gcc_except_tab: 0x1670
+  __TEXT.__const: 0x268
+  __TEXT.__cstring: 0x2b0f
+  __TEXT.__oslogstring: 0x33fd
   __TEXT.__dlopen_cstrs: 0x104
-  __TEXT.__unwind_info: 0x14a8
-  __TEXT.__objc_classname: 0xaba
-  __TEXT.__objc_methname: 0x7e7f
-  __TEXT.__objc_methtype: 0x1d30
-  __TEXT.__objc_stubs: 0x5f60
-  __DATA_CONST.__got: 0x588
-  __DATA_CONST.__const: 0x14a0
-  __DATA_CONST.__objc_classlist: 0x2a0
-  __DATA_CONST.__objc_protolist: 0x100
+  __TEXT.__unwind_info: 0x1688
+  __TEXT.__objc_classname: 0xc00
+  __TEXT.__objc_methname: 0x8913
+  __TEXT.__objc_methtype: 0x2166
+  __TEXT.__objc_stubs: 0x6680
+  __DATA_CONST.__got: 0x5d8
+  __DATA_CONST.__const: 0x16a0
+  __DATA_CONST.__objc_classlist: 0x2d8
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e70
-  __DATA_CONST.__objc_protorefs: 0x90
-  __DATA_CONST.__objc_superrefs: 0x248
+  __DATA_CONST.__objc_selrefs: 0x2088
+  __DATA_CONST.__objc_protorefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x5d0
-  __AUTH_CONST.__const: 0x980
-  __AUTH_CONST.__cfstring: 0x2360
-  __AUTH_CONST.__objc_const: 0x7ab8
-  __AUTH_CONST.__objc_intobj: 0x210
+  __AUTH_CONST.__auth_got: 0x620
+  __AUTH_CONST.__const: 0xaa0
+  __AUTH_CONST.__cfstring: 0x2520
+  __AUTH_CONST.__objc_const: 0x84b8
+  __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x520
-  __DATA.__data: 0xc08
-  __DATA.__bss: 0x150
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x558
+  __DATA.__data: 0xe48
+  __DATA.__bss: 0x1b8
   __DATA_DIRTY.__objc_data: 0x19a0
   __DATA_DIRTY.__bss: 0x2b8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F750517A-F240-3182-8195-8C4A38C3C96B
-  Functions: 1771
-  Symbols:   6305
-  CStrings:  2861
+  UUID: 7FE32FA4-3E8C-3C4F-ACD9-9421FC8EABB4
+  Functions: 1915
+  Symbols:   6808
+  CStrings:  3037
 
Symbols:
+ +[NSError(TKError) _errorWithCode:userInfo:]
+ +[NSError(TKError) errorWithCode:debugDescription:]
+ +[TKMLDSAPrehasher prehashDataWithMessageData:publicKey:context:]
+ +[TKSmartCardTokenRegistrationManager defaultManager]
+ +[TKSmartCardTokenRegistrationManager defaultManager].cold.1
+ +[TKXPCInterface interfaceForSlotClientNotification]
+ +[TKXPCInterface interfaceForSlotClient]
+ +[TKXPCInterface interfaceForSmartCardTokenRegistration]
+ +[TKXPCInterface interfaceForXPCProtocol:]
+ +[TKXPCInterface interfaceForXPCProtocol:].cold.1
+ -[TKClientToken canRequireCardInsertion]
+ -[TKClientToken notifyOperation:forToken:withStatus:]
+ -[TKClientToken notifyOperation:forToken:withStatus:].cold.1
+ -[TKClientToken setCanRequireCardInsertion:]
+ -[TKExtensionClientToken ensureConnectionCanRequireCardInsertion:error:]
+ -[TKExtensionClientToken notifyOperation:forToken:withStatus:]
+ -[TKLocalSEPRefKey signDigest:attributes:error:]
+ -[TKLocalSEPSystemKey signDigest:attributes:error:]
+ -[TKRemoteSEPKey signDigest:attributes:error:]
+ -[TKSEPKey signDigest:attributes:error:]
+ -[TKSmartCardSlotManager _createAIDsValidationError]
+ -[TKSmartCardSlotManager createNFCSlotWithMessage:completion:]
+ -[TKSmartCardSlotManager endNFCSlotWithError:]
+ -[TKSmartCardSlotManager getValidAIDsFromCallingBundle]
+ -[TKSmartCardSlotManager isNFCSupported]
+ -[TKSmartCardSlotManager setNFCAllowedAIDs:]
+ -[TKSmartCardSlotManager synchronous:remoteSlotClientWithErrorHandler:]
+ -[TKSmartCardSlotManager updateNFCSlotMessageWithMessage:error:]
+ -[TKSmartCardSlotNFCSession .cxx_destruct]
+ -[TKSmartCardSlotNFCSession endSession]
+ -[TKSmartCardSlotNFCSession initWithSlotName:nfcSlotManager:]
+ -[TKSmartCardSlotNFCSession slotName]
+ -[TKSmartCardSlotNFCSession updateWithMessage:error:]
+ -[TKSmartCardToken proprietaryCardUsage]
+ -[TKSmartCardToken setProprietaryCardUsage:]
+ -[TKSmartCardTokenDriver createTokenWithSlot:AID:proprietaryCardUsage:error:]
+ -[TKSmartCardTokenDriver createTokenWithSlot:AID:proprietaryCardUsage:error:].cold.1
+ -[TKSmartCardTokenRegistrationManager .cxx_destruct]
+ -[TKSmartCardTokenRegistrationManager init]
+ -[TKSmartCardTokenRegistrationManager registerSmartCardWithTokenID:promptMessage:error:]
+ -[TKSmartCardTokenRegistrationManager registeredSmartCardTokens]
+ -[TKSmartCardTokenRegistrationManager unregisterSmartCardWithTokenID:error:]
+ -[TKSmartCardTokenRegistrationXPCClient .cxx_destruct]
+ -[TKSmartCardTokenRegistrationXPCClient _connectionWithErrorHandler:]
+ -[TKSmartCardTokenRegistrationXPCClient _handleConnectionClose]
+ -[TKSmartCardTokenRegistrationXPCClient _remoteObjectProxy]
+ -[TKSmartCardTokenRegistrationXPCClient _synchronousRemoteObjectProxyWithErrorHandler:]
+ -[TKSmartCardTokenRegistrationXPCClient _synchronousRemoteObjectProxy]
+ -[TKSmartCardTokenRegistrationXPCClient connectionDidActivate:]
+ -[TKSmartCardTokenRegistrationXPCClient connectionDidActivate:].cold.1
+ -[TKSmartCardTokenRegistrationXPCClient connectionDidInterrupt:]
+ -[TKSmartCardTokenRegistrationXPCClient connectionDidInvalidate:]
+ -[TKSmartCardTokenRegistrationXPCClient dealloc]
+ -[TKSmartCardTokenRegistrationXPCClient init]
+ -[TKSmartCardTokenRegistrationXPCClient registerSmartCardWithTokenID:promptMessage:callerBundleID:completion:]
+ -[TKSmartCardTokenRegistrationXPCClient registerSmartCardWithTokenID:promptMessage:callerBundleID:error:]
+ -[TKSmartCardTokenRegistrationXPCClient registeredSmartCardTokens]
+ -[TKSmartCardTokenRegistrationXPCClient registeredSmartCardsWithCompletion:]
+ -[TKSmartCardTokenRegistrationXPCClient unregisterSmartCardWithTokenID:callerBundleID:completion:]
+ -[TKSmartCardTokenRegistrationXPCClient unregisterSmartCardWithTokenID:callerBundleID:error:]
+ -[TKSmartCardTokenSession getSmartCardWithError:]
+ -[TKSmartCardTokenSession getSmartCardWithError:].cold.1
+ -[TKSmartCardTokenSession getSmartCardWithError:].cold.2
+ -[TKSmartCardTokenSession getSmartCardWithError:].cold.3
+ -[TKTokenAccessDBBackedByUserDefaults _installationKeyForBundleID:]
+ -[TKTokenAccessDBBackedByUserDefaults allStoredBundleIDs]
+ -[TKTokenAccessDBBackedByUserDefaults fetchStoredInstallationIDForBundleID:]
+ -[TKTokenAccessDBBackedByUserDefaults removeAccessForBundleID:matchPartial:]
+ -[TKTokenAccessDBBackedByUserDefaults removeAccessForBundleID:matchPartial:].cold.1
+ -[TKTokenAccessDBBackedByUserDefaults removeAccessForBundleID:matchPartial:].cold.2
+ -[TKTokenAccessDBBackedByUserDefaults storeInstallationID:forBundleID:]
+ -[TKTokenAccessRegistry _storeInstallationID:forBundleID:]
+ -[TKTokenAccessRegistry allStoredBundleIDs]
+ -[TKTokenAccessRegistry fetchStoredInstallationIDForBundleID:]
+ -[TKTokenAccessRegistry getInstallationIDFromBundleID:]
+ -[TKTokenAccessRegistry removeAccessForBundleID:matchPartial:]
+ -[TKTokenDriver acquireTokenWithSlot:AID:proprietaryCardUsage:reply:]
+ -[TKTokenDriver acquireTokenWithSlot:AID:proprietaryCardUsage:reply:].cold.1
+ -[TKTokenDriver createTokenWithSlot:AID:proprietaryCardUsage:error:]
+ -[TKTokenDriverContext _setupDriver]
+ -[TKTokenDriverContext _setupWithDriver:error:]
+ -[TKTokenDriverContext _setupWithDriver:error:].cold.1
+ -[TKTokenDriverContext acquireTokenWithSlot:AID:proprietaryCardUsage:reply:]
+ -[TKTokenKeyAlgorithm description]
+ -[TKTokenKeychainContents initWithTokenID:error:]
+ -[TKTokenKeychainContents initWithTokenID:error:].cold.1
+ -[TKTokenWatcherTokenInfo initWithTokenID:slotName:driverName:]
+ -[TKXPCConnectionConfigurationDefault .cxx_destruct]
+ -[TKXPCConnectionConfigurationDefault exportedInterface]
+ -[TKXPCConnectionConfigurationDefault exportedObject]
+ -[TKXPCConnectionConfigurationDefault initWithRemoteObjectInterface:exportedInterface:exportedObject:replyQueue:]
+ -[TKXPCConnectionConfigurationDefault remoteObjectInterface]
+ -[TKXPCConnectionConfigurationDefault replyQueue]
+ -[TKXPCConnectionDefault .cxx_destruct]
+ -[TKXPCConnectionDefault activate]
+ -[TKXPCConnectionDefault configureWithConfiguration:]
+ -[TKXPCConnectionDefault configureWithConfiguration:].cold.1
+ -[TKXPCConnectionDefault configureWithConfiguration:].cold.2
+ -[TKXPCConnectionDefault connection]
+ -[TKXPCConnectionDefault delegate]
+ -[TKXPCConnectionDefault hasEntitlement:]
+ -[TKXPCConnectionDefault initWithConnection:]
+ -[TKXPCConnectionDefault initWithListenerEndpoint:]
+ -[TKXPCConnectionDefault initWithMachServiceName:options:]
+ -[TKXPCConnectionDefault invalidate]
+ -[TKXPCConnectionDefault remoteObjectProxyWithErrorHandler:]
+ -[TKXPCConnectionDefault remoteObjectProxy]
+ -[TKXPCConnectionDefault setDelegate:]
+ -[TKXPCConnectionDefault synchronousRemoteObjectProxyWithErrorHandler:]
+ GCC_except_table121
+ GCC_except_table140
+ GCC_except_table161
+ GCC_except_table164
+ GCC_except_table167
+ GCC_except_table27
+ GCC_except_table37
+ GCC_except_table51
+ GCC_except_table57
+ GCC_except_table59
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table74
+ GCC_except_table93
+ _BaseBoardLibraryCore
+ _NSLocalizedFailureReasonErrorKey
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_TKMLDSAPrehasher
+ _OBJC_CLASS_$_TKSmartCardSlotNFCSession
+ _OBJC_CLASS_$_TKSmartCardTokenRegistrationManager
+ _OBJC_CLASS_$_TKSmartCardTokenRegistrationXPCClient
+ _OBJC_CLASS_$_TKXPCConnectionConfigurationDefault
+ _OBJC_CLASS_$_TKXPCConnectionDefault
+ _OBJC_CLASS_$_TKXPCInterface
+ _OBJC_IVAR_$_TKClientToken._canRequireCardInsertion
+ _OBJC_IVAR_$_TKSmartCardSlotManager._nfcAppIdentifiers
+ _OBJC_IVAR_$_TKSmartCardSlotNFCSession._nfcSlotManager
+ _OBJC_IVAR_$_TKSmartCardSlotNFCSession._queue
+ _OBJC_IVAR_$_TKSmartCardSlotNFCSession._slotName
+ _OBJC_IVAR_$_TKSmartCardToken._proprietaryCardUsage
+ _OBJC_IVAR_$_TKSmartCardTokenRegistrationManager._remoteObjectProxy
+ _OBJC_IVAR_$_TKSmartCardTokenRegistrationXPCClient._connection
+ _OBJC_IVAR_$_TKSmartCardTokenRegistrationXPCClient._connectionLock
+ _OBJC_IVAR_$_TKXPCConnectionConfigurationDefault._exportedInterface
+ _OBJC_IVAR_$_TKXPCConnectionConfigurationDefault._exportedObject
+ _OBJC_IVAR_$_TKXPCConnectionConfigurationDefault._remoteObjectInterface
+ _OBJC_IVAR_$_TKXPCConnectionConfigurationDefault._replyQueue
+ _OBJC_IVAR_$_TKXPCConnectionDefault._connection
+ _OBJC_IVAR_$_TKXPCConnectionDefault.delegate
+ _OBJC_METACLASS_$_TKMLDSAPrehasher
+ _OBJC_METACLASS_$_TKSmartCardSlotNFCSession
+ _OBJC_METACLASS_$_TKSmartCardTokenRegistrationManager
+ _OBJC_METACLASS_$_TKSmartCardTokenRegistrationXPCClient
+ _OBJC_METACLASS_$_TKXPCConnectionConfigurationDefault
+ _OBJC_METACLASS_$_TKXPCConnectionDefault
+ _OBJC_METACLASS_$_TKXPCInterface
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _SpringBoardServicesLibraryCore
+ _TKNFCSlotName
+ _TKSmartCardRegistrationClientName
+ _TKTokenClassDriverConsoleUserOnly
+ _TKTokenClassDriverProprietaryCardUsage
+ _TK_LOG_xpc.log
+ _TK_LOG_xpc.once
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSError_$_TKError
+ __OBJC_$_CATEGORY_NSError_$_TKError
+ __OBJC_$_CLASS_METHODS_TKMLDSAPrehasher
+ __OBJC_$_CLASS_METHODS_TKSmartCardTokenRegistrationManager
+ __OBJC_$_CLASS_METHODS_TKXPCInterface
+ __OBJC_$_CLASS_PROP_LIST_TKSmartCardTokenRegistrationManager
+ __OBJC_$_INSTANCE_METHODS_TKSmartCardSlotNFCSession
+ __OBJC_$_INSTANCE_METHODS_TKSmartCardTokenRegistrationManager
+ __OBJC_$_INSTANCE_METHODS_TKSmartCardTokenRegistrationXPCClient
+ __OBJC_$_INSTANCE_METHODS_TKXPCConnectionConfigurationDefault
+ __OBJC_$_INSTANCE_METHODS_TKXPCConnectionDefault
+ __OBJC_$_INSTANCE_VARIABLES_TKSmartCardSlotNFCSession
+ __OBJC_$_INSTANCE_VARIABLES_TKSmartCardTokenRegistrationManager
+ __OBJC_$_INSTANCE_VARIABLES_TKSmartCardTokenRegistrationXPCClient
+ __OBJC_$_INSTANCE_VARIABLES_TKXPCConnectionConfigurationDefault
+ __OBJC_$_INSTANCE_VARIABLES_TKXPCConnectionDefault
+ __OBJC_$_PROP_LIST_TKSmartCardSlotNFCSession
+ __OBJC_$_PROP_LIST_TKSmartCardTokenRegistrationManager
+ __OBJC_$_PROP_LIST_TKSmartCardTokenRegistrationXPCClient
+ __OBJC_$_PROP_LIST_TKXPCConnection
+ __OBJC_$_PROP_LIST_TKXPCConnectionConfigurationDefault
+ __OBJC_$_PROP_LIST_TKXPCConnectionDefault
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_TKXPCConnectionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TKSmartCardSlotNFCManaging
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TKSmartCardTokenRegistrationXPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TKSmartCardTokenRegistrationXPCClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TKXPCConnection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TKSmartCardSlotNFCManaging
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TKSmartCardTokenRegistrationXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TKSmartCardTokenRegistrationXPCClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TKXPCConnection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TKXPCConnectionDelegate
+ __OBJC_$_PROTOCOL_REFS_TKSmartCardSlotNFCManaging
+ __OBJC_$_PROTOCOL_REFS_TKSmartCardTokenRegistrationXPC
+ __OBJC_$_PROTOCOL_REFS_TKSmartCardTokenRegistrationXPCClient
+ __OBJC_$_PROTOCOL_REFS_TKXPCConnection
+ __OBJC_$_PROTOCOL_REFS_TKXPCConnectionConfiguration
+ __OBJC_$_PROTOCOL_REFS_TKXPCConnectionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_TKSmartCardTokenRegistrationXPCClient
+ __OBJC_CLASS_PROTOCOLS_$_TKXPCConnectionConfigurationDefault
+ __OBJC_CLASS_PROTOCOLS_$_TKXPCConnectionDefault
+ __OBJC_CLASS_RO_$_TKMLDSAPrehasher
+ __OBJC_CLASS_RO_$_TKSmartCardSlotNFCSession
+ __OBJC_CLASS_RO_$_TKSmartCardTokenRegistrationManager
+ __OBJC_CLASS_RO_$_TKSmartCardTokenRegistrationXPCClient
+ __OBJC_CLASS_RO_$_TKXPCConnectionConfigurationDefault
+ __OBJC_CLASS_RO_$_TKXPCConnectionDefault
+ __OBJC_CLASS_RO_$_TKXPCInterface
+ __OBJC_LABEL_PROTOCOL_$_TKSmartCardSlotNFCManaging
+ __OBJC_LABEL_PROTOCOL_$_TKSmartCardTokenRegistrationXPC
+ __OBJC_LABEL_PROTOCOL_$_TKSmartCardTokenRegistrationXPCClient
+ __OBJC_LABEL_PROTOCOL_$_TKXPCConnection
+ __OBJC_LABEL_PROTOCOL_$_TKXPCConnectionConfiguration
+ __OBJC_LABEL_PROTOCOL_$_TKXPCConnectionDelegate
+ __OBJC_METACLASS_RO_$_TKMLDSAPrehasher
+ __OBJC_METACLASS_RO_$_TKSmartCardSlotNFCSession
+ __OBJC_METACLASS_RO_$_TKSmartCardTokenRegistrationManager
+ __OBJC_METACLASS_RO_$_TKSmartCardTokenRegistrationXPCClient
+ __OBJC_METACLASS_RO_$_TKXPCConnectionConfigurationDefault
+ __OBJC_METACLASS_RO_$_TKXPCConnectionDefault
+ __OBJC_METACLASS_RO_$_TKXPCInterface
+ __OBJC_PROTOCOL_$_TKSmartCardSlotNFCManaging
+ __OBJC_PROTOCOL_$_TKSmartCardTokenRegistrationXPC
+ __OBJC_PROTOCOL_$_TKSmartCardTokenRegistrationXPCClient
+ __OBJC_PROTOCOL_$_TKXPCConnection
+ __OBJC_PROTOCOL_$_TKXPCConnectionConfiguration
+ __OBJC_PROTOCOL_$_TKXPCConnectionDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_TKSmartCardTokenRegistrationXPC
+ ___105-[TKSmartCardTokenRegistrationXPCClient registerSmartCardWithTokenID:promptMessage:callerBundleID:error:]_block_invoke
+ ___105-[TKSmartCardTokenRegistrationXPCClient registerSmartCardWithTokenID:promptMessage:callerBundleID:error:]_block_invoke.cold.1
+ ___105-[TKSmartCardTokenRegistrationXPCClient registerSmartCardWithTokenID:promptMessage:callerBundleID:error:]_block_invoke.cold.2
+ ___32-[TKSmartCardSlot makeSmartCard]_block_invoke.218
+ ___36-[TKTokenDriverContext _setupDriver]_block_invoke
+ ___36-[TKTokenDriverContext _setupDriver]_block_invoke.cold.1
+ ___36-[TKTokenDriverContext _setupDriver]_block_invoke.cold.2
+ ___36-[TKTokenDriverContext _setupDriver]_block_invoke.cold.3
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.312
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.314
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.316
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.321
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.313
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.313.cold.1
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.315
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.315.cold.1
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.320
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.320.cold.1
+ ___37-[TKSmartCard transmitRequest:reply:]_block_invoke.336
+ ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke.306
+ ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_2.307
+ ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_3.308
+ ___39-[TKSmartCardSlotNFCSession endSession]_block_invoke
+ ___39-[TKSmartCardSlotNFCSession endSession]_block_invoke.cold.1
+ ___39-[TKSmartCardSlotNFCSession endSession]_block_invoke.cold.2
+ ___40-[TKSmartCardSlotManager isNFCSupported]_block_invoke
+ ___40-[TKSmartCardSlotManager isNFCSupported]_block_invoke.53
+ ___40-[TKSmartCardSlotManager isNFCSupported]_block_invoke.53.cold.1
+ ___40-[TKSmartCardSlotManager isNFCSupported]_block_invoke.cold.1
+ ___41-[TKSmartCardSlotManager setupConnection]_block_invoke.33
+ ___42+[TKXPCInterface interfaceForXPCProtocol:]_block_invoke
+ ___43-[TKSmartCard sendIns:p1:p2:data:le:reply:]_block_invoke.371
+ ___46-[TKSmartCardSlotManager endNFCSlotWithError:]_block_invoke
+ ___46-[TKSmartCardSlotManager endNFCSlotWithError:]_block_invoke.50
+ ___46-[TKSmartCardSlotManager endNFCSlotWithError:]_block_invoke.50.cold.1
+ ___46-[TKSmartCardSlotManager endNFCSlotWithError:]_block_invoke.cold.1
+ ___47-[TKTokenDriverContext _setupWithDriver:error:]_block_invoke
+ ___52-[TKSmartCardSlot simulateCardReinsertionWithError:]_block_invoke.229
+ ___53+[TKSmartCardTokenRegistrationManager defaultManager]_block_invoke
+ ___53-[TKSmartCardSlotNFCSession updateWithMessage:error:]_block_invoke
+ ___53-[TKXPCConnectionDefault configureWithConfiguration:]_block_invoke
+ ___53-[TKXPCConnectionDefault configureWithConfiguration:]_block_invoke_2
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.211
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.211.cold.1
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.212
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.212.cold.1
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.213
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.213.cold.1
+ ___59-[TKSmartCardTokenRegistrationXPCClient _remoteObjectProxy]_block_invoke
+ ___59-[TKSmartCardTokenRegistrationXPCClient _remoteObjectProxy]_block_invoke.cold.1
+ ___62-[TKExtensionClientToken notifyOperation:forToken:withStatus:]_block_invoke
+ ___62-[TKSmartCardSlotManager createNFCSlotWithMessage:completion:]_block_invoke
+ ___62-[TKSmartCardSlotManager createNFCSlotWithMessage:completion:]_block_invoke.43
+ ___62-[TKSmartCardSlotManager createNFCSlotWithMessage:completion:]_block_invoke.43.cold.1
+ ___62-[TKSmartCardSlotManager createNFCSlotWithMessage:completion:]_block_invoke.43.cold.2
+ ___62-[TKSmartCardSlotManager createNFCSlotWithMessage:completion:]_block_invoke.43.cold.3
+ ___62-[TKSmartCardSlotManager createNFCSlotWithMessage:completion:]_block_invoke.cold.1
+ ___64-[TKSmartCardSlotManager updateNFCSlotMessageWithMessage:error:]_block_invoke
+ ___64-[TKSmartCardSlotManager updateNFCSlotMessageWithMessage:error:]_block_invoke.52
+ ___64-[TKSmartCardSlotManager updateNFCSlotMessageWithMessage:error:]_block_invoke.52.cold.1
+ ___64-[TKSmartCardSlotManager updateNFCSlotMessageWithMessage:error:]_block_invoke.cold.1
+ ___66-[TKSmartCardTokenRegistrationXPCClient registeredSmartCardTokens]_block_invoke
+ ___69-[TKSmartCardTokenRegistrationXPCClient _connectionWithErrorHandler:]_block_invoke
+ ___70-[TKSmartCardTokenRegistrationXPCClient _synchronousRemoteObjectProxy]_block_invoke
+ ___70-[TKSmartCardTokenRegistrationXPCClient _synchronousRemoteObjectProxy]_block_invoke.66
+ ___70-[TKSmartCardTokenRegistrationXPCClient _synchronousRemoteObjectProxy]_block_invoke.66.cold.1
+ ___70-[TKSmartCardTokenRegistrationXPCClient _synchronousRemoteObjectProxy]_block_invoke.cold.1
+ ___72-[TKExtensionClientToken ensureConnectionCanRequireCardInsertion:error:]_block_invoke
+ ___72-[TKExtensionClientToken ensureConnectionCanRequireCardInsertion:error:]_block_invoke.1
+ ___76-[TKTokenDriverContext acquireTokenWithSlot:AID:proprietaryCardUsage:reply:]_block_invoke
+ ___76-[TKTokenDriverContext acquireTokenWithSlot:AID:proprietaryCardUsage:reply:]_block_invoke.cold.1
+ ___77-[TKSmartCardTokenDriver createTokenWithSlot:AID:proprietaryCardUsage:error:]_block_invoke
+ ___93-[TKSmartCardTokenRegistrationXPCClient unregisterSmartCardWithTokenID:callerBundleID:error:]_block_invoke
+ ___93-[TKSmartCardTokenRegistrationXPCClient unregisterSmartCardWithTokenID:callerBundleID:error:]_block_invoke.cold.1
+ ___93-[TKSmartCardTokenRegistrationXPCClient unregisterSmartCardWithTokenID:callerBundleID:error:]_block_invoke.cold.2
+ ___TK_LOG_xpc_block_invoke
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8lr32l8
+ ___block_descriptor_40_e8_32r_e20_v20?0B8"NSError"12lr32l8
+ ___block_descriptor_40_e8_32s_e29_"TKXPCConnectionDefault"8?0ls32l8
+ ___block_descriptor_41_e8_32s_e43_24?0"<TKClientTokenServerProtocol>"8^16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e23_v24?0B8B12"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e20_v20?0B8"NSError"12ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e20_v20?0B8"NSError"12ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s_e43_24?0"<TKClientTokenServerProtocol>"8^16ls32l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_literal_global.100
+ ___block_literal_global.109
+ ___block_literal_global.114
+ ___block_literal_global.160
+ ___block_literal_global.217
+ ___block_literal_global.250
+ ___block_literal_global.276
+ ___block_literal_global.310
+ ___block_literal_global.314
+ ___block_literal_global.319
+ ___block_literal_global.331
+ ___block_literal_global.344
+ ___block_literal_global.347
+ ___block_literal_global.349
+ ___block_literal_global.433
+ ___block_literal_global.65
+ ___block_literal_global.67
+ ___block_literal_global.68
+ ___block_literal_global.899
+ ___block_literal_global.91
+ ___block_literal_global.94
+ ___getSBSRemoteAlertPresentationTargetPredicateClass_block_invoke
+ __setupWithDriver:error:.onceToken
+ __setupWithDriver:error:.selfTask
+ _acm_mem_alloc_typed
+ _ccmldsa65
+ _ccmldsa87
+ _ccmldsa_hash_nbytes_ctx
+ _ccmldsa_import_pubkey
+ _ccmldsa_prehash
+ _ccmldsa_prehash_with_context
+ _ccmldsa_pubkey_nbytes_params
+ _ccmldsa_sizeof_pub_ctx
+ _defaultManager.onceToken
+ _defaultManager.sharedInstance
+ _getSBSRemoteAlertPresentationTargetPredicateClass.softClass
+ _hasSystemKey:ACMHandle:.supported.348
+ _interfaceForXPCProtocol:.onceToken
+ _interfaceForXPCProtocol:.protocolCache
+ _kSecAttrKeyTypeMLDSA
+ _kSecAttrKeyTypeMLKEM
+ _kSecKeyAlgorithmKEMMLKEM
+ _kSecKeyAlgorithmMLDSASignatureMessage
+ _kSecKeySignatureParameterContext
+ _objc_msgSend$_connectionWithErrorHandler:
+ _objc_msgSend$_createAIDsValidationError
+ _objc_msgSend$_errorWithCode:userInfo:
+ _objc_msgSend$_handleConnectionClose
+ _objc_msgSend$_installationKeyForBundleID:
+ _objc_msgSend$_remoteObjectProxy
+ _objc_msgSend$_setupDriver
+ _objc_msgSend$_storeInstallationID:forBundleID:
+ _objc_msgSend$_synchronousRemoteObjectProxy
+ _objc_msgSend$acquireTokenWithSlot:AID:proprietaryCardUsage:reply:
+ _objc_msgSend$activate
+ _objc_msgSend$allStoredBundleIDs
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$bundleRecordWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$canRequireCardInsertion
+ _objc_msgSend$configureWithConfiguration:
+ _objc_msgSend$connectionDidActivate:
+ _objc_msgSend$connectionDidInterrupt:
+ _objc_msgSend$connectionDidInvalidate:
+ _objc_msgSend$containingBundleRecord
+ _objc_msgSend$createTokenWithSlot:AID:proprietaryCardUsage:error:
+ _objc_msgSend$endNFCSlotWithError:
+ _objc_msgSend$endNFCSlotWithName:reply:
+ _objc_msgSend$ensureConnectionCanRequireCardInsertion:error:
+ _objc_msgSend$errorWithCode:debugDescription:
+ _objc_msgSend$exportedInterface
+ _objc_msgSend$exportedObject
+ _objc_msgSend$fetchStoredInstallationIDForBundleID:
+ _objc_msgSend$getInstallationIDFromBundleID:
+ _objc_msgSend$getSmartCardWithError:
+ _objc_msgSend$getTokenEndpointForTokenID:canRequireCardInsertion:reply:
+ _objc_msgSend$getValidAIDsFromCallingBundle
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$initWithRemoteObjectInterface:exportedInterface:exportedObject:replyQueue:
+ _objc_msgSend$initWithSlotName:nfcSlotManager:
+ _objc_msgSend$initWithTargetPredicate:
+ _objc_msgSend$initWithTokenID:error:
+ _objc_msgSend$installSessionIdentifier
+ _objc_msgSend$interfaceForSlotClient
+ _objc_msgSend$interfaceForSlotClientNotification
+ _objc_msgSend$interfaceForSmartCardTokenRegistration
+ _objc_msgSend$isNFCSupportedWithReply:
+ _objc_msgSend$localizedInfoDictionary
+ _objc_msgSend$notifyOperation:forToken:withStatus:
+ _objc_msgSend$predicateForProcess:
+ _objc_msgSend$prehashDataWithMessageData:publicKey:context:
+ _objc_msgSend$proprietaryCardUsage
+ _objc_msgSend$publicKey
+ _objc_msgSend$registerSmartCardWithTokenID:promptMessage:callerBundleID:completion:
+ _objc_msgSend$registerSmartCardWithTokenID:promptMessage:callerBundleID:error:
+ _objc_msgSend$registeredSmartCardTokens
+ _objc_msgSend$registeredSmartCardsWithCompletion:
+ _objc_msgSend$remoteObjectInterface
+ _objc_msgSend$removeAccessForBundleID:matchPartial:
+ _objc_msgSend$replyQueue
+ _objc_msgSend$set
+ _objc_msgSend$setProprietaryCardUsage:
+ _objc_msgSend$startNFCSlotWithName:uiSheetMessage:supportedAppIdentifiers:reply:
+ _objc_msgSend$storeInstallationID:forBundleID:
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$synchronous:remoteSlotClientWithErrorHandler:
+ _objc_msgSend$unregisterSmartCardWithTokenID:callerBundleID:completion:
+ _objc_msgSend$unregisterSmartCardWithTokenID:callerBundleID:error:
+ _objc_msgSend$updateNFCSlotMessageWithMessage:error:
+ _objc_msgSend$updateNFCSlotUIMessageWithMessage:slotName:reply:
+ _objc_retainAutoreleasedReturnValue
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- -[TKExtensionClientToken ensureConnectionWithError:]
- -[TKSmartCardTokenDriver createTokenWithSlot:AID:error:]
- -[TKSmartCardTokenDriver createTokenWithSlot:AID:error:].cold.1
- -[TKTokenDriver acquireTokenWithSlot:AID:reply:]
- -[TKTokenDriver acquireTokenWithSlot:AID:reply:].cold.1
- -[TKTokenDriver createTokenWithSlot:AID:error:]
- -[TKTokenDriverContext acquireTokenWithSlot:AID:reply:]
- -[TKTokenKeychainContents initWithTokenID:].cold.1
- GCC_except_table105
- GCC_except_table124
- GCC_except_table145
- GCC_except_table148
- GCC_except_table151
- GCC_except_table17
- GCC_except_table20
- GCC_except_table56
- GCC_except_table58
- GCC_except_table60
- GCC_except_table77
- _BaseBoardLibrary
- _BaseBoardLibrary.cold.1
- _OBJC_CLASS_$_LSApplicationWorkspace
- _OBJC_IVAR_$_TKSmartCardTokenSession._errorCard
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_33
- _OUTLINED_FUNCTION_34
- _SpringBoardServicesLibrary
- _SpringBoardServicesLibrary.cold.1
- ___29-[TKTokenDriverContext setup]_block_invoke
- ___29-[TKTokenDriverContext setup]_block_invoke.cold.1
- ___29-[TKTokenDriverContext setup]_block_invoke.cold.2
- ___29-[TKTokenDriverContext setup]_block_invoke.cold.3
- ___32-[TKSmartCardSlot makeSmartCard]_block_invoke.127
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.228
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.230
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.232
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.237
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.229
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.229.cold.1
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.231
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.231.cold.1
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.236
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.236.cold.1
- ___37-[TKSmartCard transmitRequest:reply:]_block_invoke.252
- ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke.222
- ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_2.223
- ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_3.224
- ___41-[TKSmartCardSlotManager setupConnection]_block_invoke.14
- ___43-[TKSmartCard sendIns:p1:p2:data:le:reply:]_block_invoke.287
- ___43-[TKTokenAccessDBBackedByUserDefaults init]_block_invoke
- ___43-[TKTokenAccessDBBackedByUserDefaults init]_block_invoke.cold.1
- ___52-[TKExtensionClientToken ensureConnectionWithError:]_block_invoke
- ___52-[TKExtensionClientToken ensureConnectionWithError:]_block_invoke.1
- ___52-[TKSmartCardSlot simulateCardReinsertionWithError:]_block_invoke.140
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.120
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.120.cold.1
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.121
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.121.cold.1
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.122
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.122.cold.1
- ___55-[TKTokenDriverContext acquireTokenWithSlot:AID:reply:]_block_invoke
- ___55-[TKTokenDriverContext acquireTokenWithSlot:AID:reply:]_block_invoke.cold.1
- ___56-[TKSmartCardTokenDriver createTokenWithSlot:AID:error:]_block_invoke
- ___block_literal_global.108
- ___block_literal_global.111
- ___block_literal_global.138
- ___block_literal_global.157
- ___block_literal_global.226
- ___block_literal_global.235
- ___block_literal_global.240
- ___block_literal_global.247
- ___block_literal_global.255
- ___block_literal_global.260
- ___block_literal_global.263
- ___block_literal_global.296
- ___block_literal_global.342
- ___block_literal_global.428
- ___block_literal_global.66
- ___block_literal_global.817
- ___block_literal_global.88
- ___block_literal_global.93
- ___getBSAuditTokenClass_block_invoke.cold.1
- ___getBSAuditTokenClass_block_invoke.cold.2
- ___getBSProcessHandleClass_block_invoke.cold.1
- ___getSBSRemoteAlertActivationContextClass_block_invoke.cold.1
- ___getSBSRemoteAlertConfigurationContextClass_block_invoke.cold.1
- ___getSBSRemoteAlertDefinitionClass_block_invoke.cold.1
- ___getSBSRemoteAlertHandleClass_block_invoke.cold.1
- ___getSBSRemoteAlertPresentationTargetClass_block_invoke.cold.1
- _acm_mem_alloc
- _dispatch_get_global_queue
- _hasSystemKey:ACMHandle:.supported.343
- _objc_msgSend$acquireTokenWithSlot:AID:reply:
- _objc_msgSend$applicationIsInstalled:
- _objc_msgSend$createTokenWithSlot:AID:error:
- _objc_msgSend$defaultWorkspace
- _objc_msgSend$ensureConnectionWithError:
- _objc_msgSend$getTokenEndpointForTokenID:reply:
- _objc_msgSend$handleFailureInFunction:file:lineNumber:description:
- _objc_msgSend$initWithTargetProcess:
CStrings:
+ "%@ configured with unsupported configuration object %@"
+ "%s: %s: CS[%u] deleted (contextDestroyed=%s).\n"
+ "-[LAContext evaluateAccessControl:] failed but did not provide an error, synthesizing: %{public}@"
+ "<%@: %p> algorithms: %@"
+ "@\"<TKSmartCardSlotNFCManaging>\""
+ "@\"<TKSmartCardTokenRegistrationXPCClient>\""
+ "@\"<TKXPCConnection>\""
+ "@\"<TKXPCConnectionDelegate>\""
+ "@\"<TKXPCConnectionDelegate>\"16@0:8"
+ "@\"NSArray\"16@0:8"
+ "@\"NSSet\"16@0:8"
+ "@\"NSString\"24@0:8@\"NSString\"16"
+ "@\"TKXPCConnectionDefault\"8@?0"
+ "@24@0:8@?<v@?@\"NSError\">16"
+ "@32@0:8@16Q24"
+ "@32@0:8q16@24"
+ "ACMRequirement - ACMRequirementDataPushButton"
+ "AIDs must be provided in Info.plist"
+ "B24@0:8@\"NSString\"16"
+ "B28@0:8B16^@20"
+ "B32@0:8@\"NSString\"16^@24"
+ "B40@0:8@\"TKTokenID\"16@\"NSString\"24^@32"
+ "B48@0:8@\"TKTokenID\"16@\"NSString\"24@\"NSString\"32^@40"
+ "B48@0:8@16@24@32^@40"
+ "Built-in NFC Slot"
+ "CFBundleDisplayName"
+ "CFBundleName"
+ "CFBundleVisibleComponentName"
+ "Called empty implementation of notifyOperation"
+ "Couldn't read \"com.apple.developer.nfc.readersession.iso7816 .select-identifiers\" record in Info.plist"
+ "Failed notify operation %ld status %ld error %{public}@"
+ "Failed to end NFC session, error: %@"
+ "Failed to register smartcard, tokenID: %{public}@, error: %@"
+ "Failed to unregister smartcard, tokenID: %{public}@, error: %@"
+ "Invalid tokenID format: %@"
+ "REGISTERED_SMARTCARD_NFC_PROMPT_MESSAGE"
+ "Registered smartcard, tokenID: %{public}@, bundleID: %@"
+ "Remote object proxy failed: %{public}@"
+ "Removing stored token access for: %@"
+ "SBSRemoteAlertPresentationTargetPredicate"
+ "Scan your registered smartcard for %@"
+ "Slot %{public}@': failed to check NFC support, error:%{public}@"
+ "Slot %{public}@': failed to end NFC slot session, error:%{public}@"
+ "Slot %{public}@': failed to register, error:%{public}@"
+ "Slot %{public}@': failed to update NFC slot UI message, error:%{public}@"
+ "Slot %{public}@': successfully created"
+ "Slot already exists and you are not authorized to receive the TKSmartCardSlotNFCSession"
+ "Synchronous call failed: %{public}@"
+ "Synchronous remote object proxy failed: %{public}@"
+ "T@\"<TKXPCConnectionDelegate>\",W,N"
+ "T@\"<TKXPCConnectionDelegate>\",W,N,Vdelegate"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_replyQueue"
+ "T@\"NSString\",R,C,N,V_slotName"
+ "T@\"NSXPCConnection\",R,N,V_connection"
+ "T@\"NSXPCInterface\",R,N,V_exportedInterface"
+ "T@\"NSXPCInterface\",R,N,V_remoteObjectInterface"
+ "T@\"TKSmartCardTokenRegistrationManager\",R"
+ "T@,R,N,V_exportedObject"
+ "TB,N,V_canRequireCardInsertion"
+ "TB,N,V_proprietaryCardUsage"
+ "TKError"
+ "TKMLDSAPrehasher"
+ "TKSmartCardSlotNFCManaging"
+ "TKSmartCardSlotNFCSession"
+ "TKSmartCardTokenRegistrationManager"
+ "TKSmartCardTokenRegistrationXPC"
+ "TKSmartCardTokenRegistrationXPCClient"
+ "TKXPCConnection"
+ "TKXPCConnectionConfiguration"
+ "TKXPCConnectionConfigurationDefault"
+ "TKXPCConnectionDefault"
+ "TKXPCConnectionDelegate"
+ "TKXPCInterface"
+ "Tried to end NFC session but it was already deallocated"
+ "Unregistered smartcard, tokenID: %{public}@"
+ "XPC connection %@ was activated"
+ "XPC connection to TKSmartCardTokenRegistrationXPC could not be created"
+ "_canRequireCardInsertion"
+ "_connectionLock"
+ "_connectionWithErrorHandler:"
+ "_createAIDsValidationError"
+ "_errorWithCode:userInfo:"
+ "_handleConnectionClose"
+ "_installationKeyForBundleID:"
+ "_nfcAppIdentifiers"
+ "_nfcSlotManager"
+ "_proprietaryCardUsage"
+ "_remoteObjectInterface"
+ "_remoteObjectProxy"
+ "_replyQueue"
+ "_setupDriver"
+ "_setupWithDriver:error:"
+ "_storeInstallationID:forBundleID:"
+ "_synchronousRemoteObjectProxy"
+ "_synchronousRemoteObjectProxyWithErrorHandler:"
+ "acquireTokenWithSlot:AID:proprietaryCardUsage:reply:"
+ "activate"
+ "allStoredBundleIDs"
+ "attempt to begin session failed: %{public}@"
+ "attempt to select AID failed: %{public}@"
+ "base64EncodedStringWithOptions:"
+ "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
+ "canRequireCardInsertion"
+ "com.apple.ctk.consoleUserOnly"
+ "com.apple.ctk.proprietaryCardUsage"
+ "com.apple.ctkd.smartcardregistration-client"
+ "com.apple.developer.nfc.readersession.iso7816.select-identifiers"
+ "com.apple.private.ctk.virtual-token"
+ "configureWithConfiguration:"
+ "connectionDidActivate:"
+ "connectionDidInterrupt:"
+ "connectionDidInvalidate:"
+ "containingBundleRecord"
+ "createNFCSlotWithMessage:completion:"
+ "createTokenWithSlot:AID:proprietaryCardUsage:error:"
+ "ctk: connecting to slot registration server (%{public}@) failed, error:%{public}@"
+ "endNFCSlotWithError:"
+ "endNFCSlotWithName:reply:"
+ "ensureConnectionCanRequireCardInsertion:error:"
+ "errorWithCode:debugDescription:"
+ "fetchStoredInstallationIDForBundleID:"
+ "getInstallationIDFromBundleID:"
+ "getSmartCardWithError:"
+ "getTokenEndpointForTokenID:canRequireCardInsertion:reply:"
+ "getValidAIDsFromCallingBundle"
+ "hasEntitlement:"
+ "infoDictionary"
+ "initWithRemoteObjectInterface:exportedInterface:exportedObject:replyQueue:"
+ "initWithSlotName:nfcSlotManager:"
+ "initWithTargetPredicate:"
+ "initWithTokenID:error:"
+ "initWithTokenID:slotName:driverName:"
+ "installSessionIdentifier"
+ "installation:"
+ "installation:%@"
+ "interfaceForSlotClient"
+ "interfaceForSlotClientNotification"
+ "interfaceForSmartCardTokenRegistration"
+ "interfaceForXPCProtocol:"
+ "isNFCSupported"
+ "isNFCSupportedWithReply:"
+ "localizedInfoDictionary"
+ "missing virtual token entitlement"
+ "mlkem1024"
+ "mlkem768"
+ "notifyOperation:forToken:withStatus:"
+ "predicateForProcess:"
+ "prehashDataWithMessageData:publicKey:context:"
+ "proprietaryCardUsage"
+ "registerSmartCardWithTokenID:promptMessage:callerBundleID:completion:"
+ "registerSmartCardWithTokenID:promptMessage:callerBundleID:error:"
+ "registerSmartCardWithTokenID:promptMessage:error:"
+ "registeredSmartCardTokens"
+ "registeredSmartCardsWithCompletion:"
+ "remoteObjectInterface"
+ "removeAccessForBundleID:matchPartial:"
+ "replyQueue"
+ "set"
+ "setCanRequireCardInsertion:"
+ "setNFCAllowedAIDs:"
+ "setProprietaryCardUsage:"
+ "signDigest:attributes:error:"
+ "smartCardSlotNFCSession.%@"
+ "startNFCSlotWithName:uiSheetMessage:supportedAppIdentifiers:reply:"
+ "storeInstallationID:forBundleID:"
+ "stringForKey:"
+ "synchronous:remoteSlotClientWithErrorHandler:"
+ "token session persists: %{public}d"
+ "unregisterSmartCardWithTokenID:callerBundleID:completion:"
+ "unregisterSmartCardWithTokenID:callerBundleID:error:"
+ "unregisterSmartCardWithTokenID:error:"
+ "updateNFCSlotMessageWithMessage:error:"
+ "updateNFCSlotUIMessageWithMessage:slotName:reply:"
+ "updateWithMessage:error:"
+ "v24@0:8@\"<TKXPCConnection>\"16"
+ "v24@0:8@\"<TKXPCConnectionConfiguration>\"16"
+ "v24@0:8@\"<TKXPCConnectionDelegate>\"16"
+ "v24@?0B8B12@\"NSError\"16"
+ "v28@0:8@\"NSString\"16B24"
+ "v28@0:8@16B24"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">28"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"TKTokenID\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8q16@\"NSString\"24q32"
+ "v40@0:8q16@24q32"
+ "v44@0:8@\"NSXPCListenerEndpoint\"16@\"NSData\"24B32@?<v@?@\"NSXPCListenerEndpoint\"@\"NSString\"@\"NSError\">36"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32@?<v@?BB@\"NSError\">40"
+ "v48@0:8@\"TKTokenID\"16@\"NSString\"24@\"NSString\"32@?<v@?B@\"NSError\">40"
+ "xpc"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "%s"
- "%s: %s: CS[%u] %s.\n"
- "'%@' removed from token registry DB"
- "-[LAContext evaluateAccessControl:] failed but did not provide an error, syntesizing: %{public}@"
- "1024"
- "768"
- "Class getBSAuditTokenClass(void)_block_invoke"
- "Class getBSProcessHandleClass(void)_block_invoke"
- "Class getSBSRemoteAlertActivationContextClass(void)_block_invoke"
- "Class getSBSRemoteAlertConfigurationContextClass(void)_block_invoke"
- "Class getSBSRemoteAlertDefinitionClass(void)_block_invoke"
- "Class getSBSRemoteAlertHandleClass(void)_block_invoke"
- "Class getSBSRemoteAlertPresentationTargetClass(void)_block_invoke"
- "TKTokenAccessRequest.m"
- "TKTokenKeychainItem.m"
- "Unable to find class %s"
- "_errorCard"
- "acquireTokenWithSlot:AID:reply:"
- "applicationIsInstalled:"
- "createTokenWithSlot:AID:error:"
- "defaultWorkspace"
- "deleted"
- "destroyed"
- "ensureConnectionWithError:"
- "getTokenEndpointForTokenID:reply:"
- "handleFailureInFunction:file:lineNumber:description:"
- "initWithTargetProcess:"
- "v40@0:8@\"NSXPCListenerEndpoint\"16@\"NSData\"24@?<v@?@\"NSXPCListenerEndpoint\"@\"NSString\"@\"NSError\">32"
- "void *BaseBoardLibrary(void)"
- "void *SpringBoardServicesLibrary(void)"

```
