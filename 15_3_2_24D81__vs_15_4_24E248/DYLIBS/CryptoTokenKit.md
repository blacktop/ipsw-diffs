## CryptoTokenKit

> `/System/Library/Frameworks/CryptoTokenKit.framework/Versions/A/CryptoTokenKit`

```diff

-738.80.3.0.0
-  __TEXT.__text: 0x454ac
+738.100.34.0.0
+  __TEXT.__text: 0x45824
   __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_methlist: 0x3674
+  __TEXT.__objc_methlist: 0x3d6c
   __TEXT.__const: 0x258
-  __TEXT.__oslogstring: 0x308f
-  __TEXT.__cstring: 0x2674
-  __TEXT.__gcc_except_tab: 0x156c
-  __TEXT.__unwind_info: 0x1320
-  __TEXT.__objc_classname: 0xa65
-  __TEXT.__objc_methname: 0x7bb0
-  __TEXT.__objc_methtype: 0x1c94
-  __TEXT.__objc_stubs: 0x5cc0
-  __DATA_CONST.__got: 0x598
-  __DATA_CONST.__const: 0x418
-  __DATA_CONST.__objc_classlist: 0x298
+  __TEXT.__oslogstring: 0x2f9c
+  __TEXT.__cstring: 0x2712
+  __TEXT.__gcc_except_tab: 0x14e0
+  __TEXT.__unwind_info: 0x1410
+  __TEXT.__objc_classname: 0xa70
+  __TEXT.__objc_methname: 0x7cc4
+  __TEXT.__objc_methtype: 0x1cc4
+  __TEXT.__objc_stubs: 0x5ca0
+  __DATA_CONST.__got: 0x5a0
+  __DATA_CONST.__const: 0x3f8
+  __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cf0
-  __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__objc_selrefs: 0x1dd0
+  __DATA_CONST.__objc_protorefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x510
-  __AUTH_CONST.__const: 0x1c10
-  __AUTH_CONST.__cfstring: 0x2320
-  __AUTH_CONST.__objc_const: 0x83e8
+  __AUTH_CONST.__const: 0x1bf0
+  __AUTH_CONST.__cfstring: 0x2380
+  __AUTH_CONST.__objc_const: 0x7978
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x19f0
-  __DATA.__objc_ivar: 0x508
+  __AUTH.__objc_data: 0x1a40
+  __DATA.__objc_ivar: 0x510
   __DATA.__data: 0xb48
-  __DATA.__bss: 0x398
+  __DATA.__bss: 0x3a0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CF10D9F9-DB16-31A8-8DA6-9032AA7BAA8C
-  Functions: 1676
-  Symbols:   4324
-  CStrings:  2809
+  UUID: 391DCA01-97F7-3759-9596-45A33B31EBFE
+  Functions: 1766
+  Symbols:   4416
+  CStrings:  2821
 
Symbols:
+ +[TKAKSParameters _dumpPlist:into:].cold.1
+ +[TKBERTLVRecord(TKPropertyList) zuluDateFormatter].cold.1
+ +[TKLocalSEPKey _eosDeviceType].cold.1
+ +[TKLocalSEPKey keyClassForProtection:].cold.1
+ +[TKLocalSEPKey protectionForKeyClass:].cold.1
+ +[TKLocalSEPSystemKey initSystemKeyIDs].cold.1
+ +[TKPowerMonitor defaultMonitor].cold.1
+ +[TKSEPClientToken builtinTokenIDs].cold.1
+ +[TKSEPKey canUseSEPLocally].cold.1
+ +[TKSEPKey ctkdConnection]
+ +[TKSEPKey runsInSystemSession].cold.1
+ +[TKSEPKey setCtkdConnection:]
+ +[TKTokenBaseContext _extensionAuxiliaryHostProtocol].cold.1
+ +[TKTokenBaseContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[TKTokenConfiguration interfaceForChangeProtocol].cold.1
+ +[TKTokenConfiguration interfaceForProtocol].cold.1
+ +[TKTokenDriverConfiguration _connectionWithCTKDConnection:]
+ +[TKTokenDriverConfiguration driverConfigurationsWithCTKDConnection:]
+ +[TKTokenDriverConfiguration driverConfigurations].cold.1
+ -[TKCTKDConnection .cxx_destruct]
+ -[TKCTKDConnection _testing_noAutomaticReconnect]
+ -[TKCTKDConnection configurationEndpoint]
+ -[TKCTKDConnection dealloc]
+ -[TKCTKDConnection endpoint]
+ -[TKCTKDConnection exportedInterface]
+ -[TKCTKDConnection exportedObject]
+ -[TKCTKDConnection initWithCTKDEndpoint:targetUID:]
+ -[TKCTKDConnection invalidate]
+ -[TKCTKDConnection serverConnection]
+ -[TKCTKDConnection serverConnection].cold.1
+ -[TKCTKDConnection setExportedInterface:]
+ -[TKCTKDConnection setExportedObject:]
+ -[TKCTKDConnection set_testing_noAutomaticReconnect:]
+ -[TKCTKDConnection withError:invoke:]
+ -[TKCTKDConnection withError:invoke:].cold.1
+ -[TKCTKDConnection withError:invoke:].cold.2
+ -[TKCTKDConnection withError:invoke:].cold.3
+ -[TKClientToken ctkdConnection]
+ -[TKClientToken initWithTokenID:ctkdConnection:]
+ -[TKClientTokenObject operationResult:error:].cold.1
+ -[TKExtensionClientToken ctkdConnection]
+ -[TKExtensionClientToken initWithTokenID:]
+ -[TKExtensionClientToken initWithTokenID:ctkdConnection:]
+ -[TKExtensionClientToken invalidate]
+ -[TKLocalSEPKey authContextWithError:].cold.3
+ -[TKLocalSEPKey valueForEntitlement:].cold.1
+ -[TKLocalSEPSystemKey attestKey:nonce:error:].cold.5
+ -[TKRemoteSEPKey attestKey:nonce:error:].cold.1
+ -[TKSEPClientToken initWithTokenID:]
+ -[TKSmartCardSlot simulateCardReinsertionWithError:]
+ -[TKSmartCardSlot simulateCardReinsertionWithError:].cold.1
+ -[TKSmartCardSlot simulateCardReinsertionWithError:].cold.2
+ -[TKSmartCardSlotEngine canSimulateCardReinsertion]
+ -[TKSmartCardSlotEngine setCardReinsertionSimulationCallInterval:]
+ -[TKSmartCardSlotEngine simulateCardReinsertionWithReply:]
+ -[TKSmartCardSlotEngine simulateCardReinsertionWithReply:].cold.1
+ -[TKTokenAuthOperation importOperation:].cold.1
+ -[TKTokenConfigurationTransaction commit].cold.1
+ -[TKTokenConfigurationTransaction dealloc].cold.1
+ -[TKTokenDriverRequest beginRequestWithExtensionContext:].cold.2
+ -[TKTokenKeychainContents initWithTokenID:].cold.1
+ -[TKTokenSessionConnection withSessionID:invoke:].cold.2
+ -[TKTokenWatcher initWithCTKDConnection:]
+ -[TKTokenWatcher initWithCTKDConnection:].cold.1
+ GCC_except_table10
+ GCC_except_table128
+ GCC_except_table147
+ GCC_except_table151
+ GCC_except_table168
+ GCC_except_table176
+ GCC_except_table23
+ GCC_except_table27
+ GCC_except_table3
+ GCC_except_table46
+ GCC_except_table50
+ GCC_except_table78
+ GCC_except_table79
+ GCC_except_table91
+ GCC_except_table99
+ LA_LOG_EndpointProvider.cold.1
+ OBJC_IVAR_$_TKCTKDConnection.__testing_noAutomaticReconnect
+ OBJC_IVAR_$_TKCTKDConnection._exportedInterface
+ OBJC_IVAR_$_TKCTKDConnection._exportedObject
+ OBJC_IVAR_$_TKCTKDConnection._namedConnection
+ OBJC_IVAR_$_TKCTKDConnection._serverConnection
+ OBJC_IVAR_$_TKCTKDConnection._serverEndpoint
+ OBJC_IVAR_$_TKCTKDConnection._targetUID
+ OBJC_IVAR_$_TKClientToken._ctkdConnection
+ OBJC_IVAR_$_TKRemoteSEPKey._ctkdConnection
+ OBJC_IVAR_$_TKSmartCardSlotEngine._cardReinsertionSimulationCallInterval
+ OBJC_IVAR_$_TKSmartCardSlotEngine._lastCardReinsertionSimulationCallTime
+ OBJC_IVAR_$_TKTokenWatcher._ctkdConnection
+ TK_LOG_AHP.cold.1
+ TK_LOG_client.cold.1
+ TK_LOG_rsepkey.cold.1
+ TK_LOG_sepkey.cold.1
+ TK_LOG_sharedrsc.cold.1
+ TK_LOG_smartcard.cold.1
+ TK_LOG_token.cold.1
+ TK_LOG_token_access_registry.cold.1
+ TK_LOG_tokencfg.cold.1
+ TK_LOG_watcher.cold.1
+ _OBJC_CLASS_$_TKCTKDConnection
+ _OBJC_METACLASS_$_TKCTKDConnection
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ __30-[TKSmartCardSlotEngine reset]_block_invoke.218
+ __32-[TKSmartCardSlot makeSmartCard]_block_invoke.135
+ __34-[TKSmartCardSlotEngine terminate]_block_invoke.252
+ __35-[TKRemoteSEPKey withError:invoke:]_block_invoke.23
+ __35-[TKRemoteSEPKey withError:invoke:]_block_invoke.23.cold.1
+ __35-[TKRemoteSEPKey withError:invoke:]_block_invoke.28
+ __35-[TKSmartCard endSessionWithReply:]_block_invoke.cold.1
+ __37-[TKSmartCard querySessionWithReply:]_block_invoke.242
+ __37-[TKSmartCard querySessionWithReply:]_block_invoke.244
+ __37-[TKSmartCard querySessionWithReply:]_block_invoke.246
+ __37-[TKSmartCard querySessionWithReply:]_block_invoke.251
+ __37-[TKSmartCard querySessionWithReply:]_block_invoke.251.cold.1
+ __37-[TKSmartCard querySessionWithReply:]_block_invoke.252
+ __37-[TKSmartCard querySessionWithReply:]_block_invoke_2.243
+ __37-[TKSmartCard querySessionWithReply:]_block_invoke_2.243.cold.1
+ __37-[TKSmartCard querySessionWithReply:]_block_invoke_2.245
+ __37-[TKSmartCard querySessionWithReply:]_block_invoke_2.245.cold.1
+ __37-[TKSmartCard transmitRequest:reply:]_block_invoke.275
+ __37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.229
+ __37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.232
+ __37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.233
+ __37-[TKSmartCardSlotEngine setProtocol:]_block_invoke.222
+ __38-[TKSmartCardSlotEngine leaveSession:]_block_invoke.240
+ __39-[TKSmartCard releaseSessionWithReply:]_block_invoke.232
+ __39-[TKSmartCard releaseSessionWithReply:]_block_invoke.237
+ __39-[TKSmartCard releaseSessionWithReply:]_block_invoke_2.238
+ __43-[TKSmartCard sendIns:p1:p2:data:le:reply:]_block_invoke.321
+ __43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.419
+ __43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.422
+ __46-[TKSmartCardSlotEngine scheduleIdlePowerDown]_block_invoke.226
+ __49-[TKSmartCardSlotEngine _setupWithName:delegate:]_block_invoke.132
+ __49-[TKSmartCardSlotEngine _setupWithName:delegate:]_block_invoke.132.cold.1
+ __49-[TKSmartCardSlotEngine _setupWithName:delegate:]_block_invoke.142
+ __52-[TKExtensionClientToken ensureConnectionWithError:]_block_invoke.1
+ __52-[TKSmartCardSlot simulateCardReinsertionWithError:]_block_invoke.148
+ __52-[TKSmartCardSlot simulateCardReinsertionWithError:]_block_invoke.cold.1
+ __55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.125
+ __55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.125.cold.1
+ __55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.128
+ __55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.128.cold.1
+ __58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.238
+ __58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.238.cold.1
+ __58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.238.cold.2
+ __58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.239
+ __58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.239.cold.1
+ __61-[TKTokenSession evaluateAuthOperation:tokenOperation:reply:]_block_invoke.cold.1
+ __68-[TKSEPKey initWithAttributes:authContext:forceSystemSession:error:]_block_invoke.cold.1
+ __72-[TKSmartCardSlotEngine reserveProtocols:reservationId:exclusive:reply:]_block_invoke.245
+ __73-[TKRemoteSEPKey _initWithObjectID:authContext:forceSystemSession:error:]_block_invoke.32
+ __85-[TKSmartCard transmitChunkedIns:p1:p2:data:fromOffset:realLe:chained:isCase4:reply:]_block_invoke.309
+ __OBJC_$_INSTANCE_METHODS_TKCTKDConnection
+ __OBJC_$_INSTANCE_VARIABLES_TKCTKDConnection
+ __OBJC_$_PROP_LIST_TKCTKDConnection
+ __OBJC_CLASS_RO_$_TKCTKDConnection
+ __OBJC_METACLASS_RO_$_TKCTKDConnection
+ ___28-[TKCTKDConnection endpoint]_block_invoke
+ ___28-[TKCTKDConnection endpoint]_block_invoke_2
+ ___31-[TKTokenWatcher startWatching]_block_invoke_2
+ ___37-[TKCTKDConnection withError:invoke:]_block_invoke
+ ___41-[TKCTKDConnection configurationEndpoint]_block_invoke
+ ___41-[TKCTKDConnection configurationEndpoint]_block_invoke_2
+ ___41-[TKTokenWatcher initWithCTKDConnection:]_block_invoke
+ ___52-[TKSmartCardSlot simulateCardReinsertionWithError:]_block_invoke
+ ___block_descriptor_32_e26_v16?0"TKCTKDConnection"8l
+ ___block_descriptor_32_e43_24?0"<TKClientTokenServerProtocol>"8^16l
+ ___block_descriptor_40_e8_32bs_e43_24?0"<TKClientTokenServerProtocol>"8^16l
+ ___block_descriptor_40_e8_32s_e27_"TKCTKDConnection"16?0^8l
+ ___block_descriptor_40_e8_32s_e43_24?0"<TKClientTokenServerProtocol>"8^16l
+ __block_literal_global.107
+ __block_literal_global.117
+ __block_literal_global.138
+ __block_literal_global.140
+ __block_literal_global.169
+ __block_literal_global.196
+ __block_literal_global.198
+ __block_literal_global.217
+ __block_literal_global.220
+ __block_literal_global.224
+ __block_literal_global.225
+ __block_literal_global.231
+ __block_literal_global.235
+ __block_literal_global.249
+ __block_literal_global.254
+ __block_literal_global.270
+ __block_literal_global.285
+ __block_literal_global.290
+ __block_literal_global.292
+ __block_literal_global.418
+ __block_literal_global.421
+ __block_literal_global.424
+ __block_literal_global.426
+ __block_literal_global.454
+ __block_literal_global.855
+ __block_literal_global.90
+ __ctkdConnection
+ _objc_msgSend$_connectionWithCTKDConnection:
+ _objc_msgSend$canSimulateCardReinsertion
+ _objc_msgSend$ctkdConnection
+ _objc_msgSend$date
+ _objc_msgSend$distantPast
+ _objc_msgSend$engineSimulateCardReinsertion:
+ _objc_msgSend$initWithCTKDConnection:
+ _objc_msgSend$initWithCTKDEndpoint:targetUID:
+ _objc_msgSend$initWithTokenID:ctkdConnection:
+ _objc_msgSend$simulateCardReinsertionWithReply:
+ _objc_msgSend$timeIntervalSinceDate:
+ provideEndpoint.cold.4
+ provideEndpoint.cold.5
+ updateLogLevelFromKext.cold.1
+ withError:invoke:.clientResourceSlot
- +[TKSEPKey clientToken]
- +[TKSEPKey setClientToken:]
- +[TKTokenDriverConfiguration _connectionWithClient:]
- -[TKClientToken SEPKeyEndpoint]
- -[TKClientToken _testing_noAutomaticReconnect]
- -[TKClientToken configurationEndpoint]
- -[TKClientToken endpoint]
- -[TKClientToken set_testing_noAutomaticReconnect:]
- -[TKClientToken watcherEndpoint]
- -[TKExtensionClientToken SEPKeyEndpoint]
- -[TKExtensionClientToken configurationEndpoint]
- -[TKExtensionClientToken endpoint]
- -[TKExtensionClientToken ensureConnectionWithError:].cold.1
- -[TKExtensionClientToken ensureConnectionWithError:].cold.2
- -[TKExtensionClientToken initWithTokenID:serverEndpoint:targetUID:]
- -[TKExtensionClientToken serverConnection]
- -[TKExtensionClientToken serverConnection].cold.1
- -[TKExtensionClientToken serverConnection].cold.2
- -[TKExtensionClientToken watcherEndpoint]
- -[TKExtensionClientToken withError:getServerEndpoint:]
- -[TKExtensionClientToken withError:getServerEndpoint:].cold.1
- -[TKRemoteSEPKey withError:invoke:].cold.1
- -[TKSEPClientToken initWithTokenID:serverEndpoint:targetUID:]
- -[TKTokenWatcher client]
- -[TKTokenWatcher endpoint]
- -[TKTokenWatcher initWithClient:]
- -[TKTokenWatcher initWithClient:].cold.1
- -[TKTokenWatcher startWatching].cold.1
- GCC_except_table123
- GCC_except_table144
- GCC_except_table146
- GCC_except_table15
- GCC_except_table165
- GCC_except_table17
- GCC_except_table170
- GCC_except_table31
- GCC_except_table35
- GCC_except_table41
- GCC_except_table44
- GCC_except_table59
- GCC_except_table61
- GCC_except_table68
- GCC_except_table76
- GCC_except_table83
- GCC_except_table88
- GCC_except_table94
- OBJC_IVAR_$_TKClientToken._SEPKeyEndpoint
- OBJC_IVAR_$_TKClientToken.__testing_noAutomaticReconnect
- OBJC_IVAR_$_TKClientToken._configurationEndpoint
- OBJC_IVAR_$_TKClientToken._endpoint
- OBJC_IVAR_$_TKClientToken._watcherEndpoint
- OBJC_IVAR_$_TKExtensionClientToken._namedConnection
- OBJC_IVAR_$_TKExtensionClientToken._serverEndpoint
- OBJC_IVAR_$_TKExtensionClientToken._targetUID
- OBJC_IVAR_$_TKTokenWatcher._client
- OBJC_IVAR_$_TKTokenWatcher._connection
- __30-[TKSmartCardSlotEngine reset]_block_invoke.205
- __31-[TKTokenWatcher startWatching]_block_invoke.43
- __31-[TKTokenWatcher startWatching]_block_invoke.43.cold.1
- __31-[TKTokenWatcher startWatching]_block_invoke.45
- __31-[TKTokenWatcher startWatching]_block_invoke.cold.1
- __32-[TKSmartCardSlot makeSmartCard]_block_invoke.133
- __34-[TKSmartCardSlotEngine terminate]_block_invoke.241
- __35-[TKRemoteSEPKey withError:invoke:]_block_invoke.93
- __35-[TKRemoteSEPKey withError:invoke:]_block_invoke.93.cold.1
- __35-[TKRemoteSEPKey withError:invoke:]_block_invoke.97
- __35-[TKRemoteSEPKey withError:invoke:]_block_invoke_2.cold.1
- __35-[TKRemoteSEPKey withError:invoke:]_block_invoke_2.cold.2
- __37-[TKSmartCard querySessionWithReply:]_block_invoke.230
- __37-[TKSmartCard querySessionWithReply:]_block_invoke.233
- __37-[TKSmartCard querySessionWithReply:]_block_invoke.235
- __37-[TKSmartCard querySessionWithReply:]_block_invoke.240
- __37-[TKSmartCard querySessionWithReply:]_block_invoke.240.cold.1
- __37-[TKSmartCard querySessionWithReply:]_block_invoke.241
- __37-[TKSmartCard querySessionWithReply:]_block_invoke_2.232
- __37-[TKSmartCard querySessionWithReply:]_block_invoke_2.232.cold.1
- __37-[TKSmartCard querySessionWithReply:]_block_invoke_2.234
- __37-[TKSmartCard querySessionWithReply:]_block_invoke_2.234.cold.1
- __37-[TKSmartCard transmitRequest:reply:]_block_invoke.263
- __37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.216
- __37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.219
- __37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.220
- __37-[TKSmartCardSlotEngine setProtocol:]_block_invoke.209
- __38-[TKSmartCardSlotEngine leaveSession:]_block_invoke.228
- __39-[TKSmartCard releaseSessionWithReply:]_block_invoke.219
- __39-[TKSmartCard releaseSessionWithReply:]_block_invoke.224
- __39-[TKSmartCard releaseSessionWithReply:]_block_invoke_2.225
- __43-[TKSmartCard sendIns:p1:p2:data:le:reply:]_block_invoke.309
- __43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.403
- __43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.406
- __46-[TKSmartCardSlotEngine scheduleIdlePowerDown]_block_invoke.213
- __49-[TKSmartCardSlotEngine _setupWithName:delegate:]_block_invoke.131
- __49-[TKSmartCardSlotEngine _setupWithName:delegate:]_block_invoke.131.cold.1
- __49-[TKSmartCardSlotEngine _setupWithName:delegate:]_block_invoke.141
- __52-[TKExtensionClientToken ensureConnectionWithError:]_block_invoke.73
- __52-[TKExtensionClientToken ensureConnectionWithError:]_block_invoke.cold.1
- __55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.123
- __55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.123.cold.1
- __55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.124
- __55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.124.cold.1
- __58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.226
- __58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.226.cold.1
- __58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.226.cold.2
- __58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.227
- __58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.227.cold.1
- __72-[TKSmartCardSlotEngine reserveProtocols:reservationId:exclusive:reply:]_block_invoke.234
- __85-[TKSmartCard transmitChunkedIns:p1:p2:data:fromOffset:realLe:chained:isCase4:reply:]_block_invoke.297
- __OBJC_PROTOCOL_REFERENCE_$_TKProtocolTokenWatcherServer
- __OBJC_PROTOCOL_REFERENCE_$_TKRemoteSEPKeyProtocol
- ___33-[TKTokenWatcher initWithClient:]_block_invoke
- ___34-[TKExtensionClientToken endpoint]_block_invoke
- ___34-[TKExtensionClientToken endpoint]_block_invoke_2
- ___40-[TKExtensionClientToken SEPKeyEndpoint]_block_invoke
- ___40-[TKExtensionClientToken SEPKeyEndpoint]_block_invoke_2
- ___41-[TKExtensionClientToken watcherEndpoint]_block_invoke
- ___41-[TKExtensionClientToken watcherEndpoint]_block_invoke_2
- ___47-[TKExtensionClientToken configurationEndpoint]_block_invoke
- ___47-[TKExtensionClientToken configurationEndpoint]_block_invoke_2
- ___54-[TKExtensionClientToken withError:getServerEndpoint:]_block_invoke
- ___73-[TKRemoteSEPKey _initWithObjectID:authContext:forceSystemSession:error:]_block_invoke_2
- ___block_descriptor_32_e25_v16?0"NSXPCConnection"8l
- ___block_descriptor_32_e26_"NSXPCConnection"16?0^8l
- ___block_descriptor_32_e66_"NSXPCListenerEndpoint"24?0"<TKClientTokenServerProtocol>"8^16l
- ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8l
- __block_literal_global.132
- __block_literal_global.136
- __block_literal_global.150
- __block_literal_global.152
- __block_literal_global.174
- __block_literal_global.199
- __block_literal_global.201
- __block_literal_global.203
- __block_literal_global.204
- __block_literal_global.207
- __block_literal_global.211
- __block_literal_global.218
- __block_literal_global.222
- __block_literal_global.227
- __block_literal_global.238
- __block_literal_global.243
- __block_literal_global.258
- __block_literal_global.273
- __block_literal_global.278
- __block_literal_global.280
- __block_literal_global.402
- __block_literal_global.405
- __block_literal_global.408
- __block_literal_global.410
- __block_literal_global.438
- __block_literal_global.68
- __block_literal_global.70
- __block_literal_global.72
- __block_literal_global.844
- __block_literal_global.86
- __block_literal_global.96
- __block_literal_global.97
- __clientToken
- _objc_msgSend$SEPKeyEndpoint
- _objc_msgSend$_connectionWithClient:
- _objc_msgSend$client
- _objc_msgSend$clientToken
- _objc_msgSend$getSEPKeyEndpoint:
- _objc_msgSend$getWatcherEndpoint:
- _objc_msgSend$initWithClient:
- _objc_msgSend$initWithTokenID:serverEndpoint:targetUID:
- _objc_msgSend$invalidationHandler
- _objc_msgSend$removeAllTokens
- _objc_msgSend$watcherEndpoint
- _objc_msgSend$withError:getServerEndpoint:
- withError:invoke:.SEPKeyInterface
- withError:invoke:.connectionSlot
CStrings:
+ "%{public}@: Error when simulating card reinsertion: %@"
+ "%{public}@: Reinsertion simulation cancelled due to call rate limitation"
+ "%{public}@: Skipping simulated card reinsertion due to missing card"
+ "%{public}@: Started simulated card reinsertion"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "@\"NSDate\""
+ "@\"NSXPCInterface\""
+ "@\"TKCTKDConnection\""
+ "@\"TKCTKDConnection\"16@?0^@8"
+ "@24@?0@\"<TKClientTokenServerProtocol>\"8^@16"
+ "Card is missing"
+ "Missing TKSmartCardSlotEngineDelegate delegate"
+ "Reinsertion simulation is currently running or was run recently. Please wait at least %f seconds between the calls."
+ "T@\"NSXPCInterface\",&,N,V_exportedInterface"
+ "T@\"NSXPCListenerEndpoint\",R,N"
+ "T@\"TKCTKDConnection\",&,N"
+ "T@\"TKCTKDConnection\",R,N,V_ctkdConnection"
+ "T@,&,N,V_exportedObject"
+ "TKCTKDConnection"
+ "_cardReinsertionSimulationCallInterval"
+ "_connectionWithCTKDConnection:"
+ "_ctkdConnection"
+ "_exportedInterface"
+ "_exportedObject"
+ "_lastCardReinsertionSimulationCallTime"
+ "canSimulateCardReinsertion"
+ "ctkdConnection"
+ "date"
+ "distantPast"
+ "driverConfigurationsWithCTKDConnection:"
+ "engineSimulateCardReinsertion:"
+ "exportedInterface"
+ "exportedObject"
+ "initWithCTKDConnection:"
+ "initWithCTKDEndpoint:targetUID:"
+ "initWithTokenID:ctkdConnection:"
+ "invoke on token-client connection failed with connection error %{public}@"
+ "setCardReinsertionSimulationCallInterval:"
+ "setCtkdConnection:"
+ "simulateCardReinsertionWithError:"
+ "simulateCardReinsertionWithReply:"
+ "timeIntervalSinceDate:"
+ "v16@?0@\"TKCTKDConnection\"8"
+ "\xf0a1"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "@\"NSXPCConnection\"16@?0^@8"
- "@\"NSXPCListenerEndpoint\"24@?0@\"<TKClientTokenServerProtocol>\"8^@16"
- "Failed to get TKTokenWatcher endpoint, watcher will be mute."
- "Failed to get connection for tokenID=%{public}@ (error %{public}@)"
- "SEPKeyEndpoint"
- "T@\"NSXPCListenerEndpoint\",R"
- "T@\"NSXPCListenerEndpoint\",R,N,V_SEPKeyEndpoint"
- "T@\"NSXPCListenerEndpoint\",R,N,V_endpoint"
- "T@\"NSXPCListenerEndpoint\",R,N,V_watcherEndpoint"
- "T@\"TKClientToken\",&,N"
- "T@\"TKClientToken\",R,N,V_client"
- "_SEPKeyEndpoint"
- "_client"
- "_connectionWithClient:"
- "_watcherEndpoint"
- "clientToken"
- "connection to the watcher endpoint invalidated/interrupted!"
- "creating rsepkey xpc connection"
- "detected interruption on token-client connection, retrying %d"
- "failed to call remotesepkey repeatedly, giving up, error: %{public}@"
- "failed to call remotesepkey, try %d, error %{public}@"
- "failed to register TKTokenWatcher, error %{public}@"
- "get*Endpoint on token-client connection failed with connection error %{public}@"
- "getSEPKeyEndpoint:"
- "getWatcherEndpoint:"
- "initWithClient:"
- "invalidationHandler"
- "setClientToken:"
- "unable to get endpoint"
- "v16@?0@\"NSXPCConnection\"8"
- "watcherEndpoint"
- "withError:getServerEndpoint:"
- "\xf0A1"

```
