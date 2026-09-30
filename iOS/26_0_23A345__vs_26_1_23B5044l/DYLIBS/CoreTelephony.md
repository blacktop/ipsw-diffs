## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-13091.1.14.0.0
-  __TEXT.__text: 0x18e9c0
-  __TEXT.__auth_stubs: 0x1960
-  __TEXT.__objc_methlist: 0x1b494
+13105.1.1.0.0
+  __TEXT.__text: 0x1975c4
+  __TEXT.__auth_stubs: 0x1990
+  __TEXT.__objc_methlist: 0x1b794
   __TEXT.__const: 0x1002
-  __TEXT.__gcc_except_tab: 0x1e110
-  __TEXT.__cstring: 0x1f8c5
-  __TEXT.__oslogstring: 0x3fbd
+  __TEXT.__gcc_except_tab: 0x1f8b8
+  __TEXT.__cstring: 0x1fa76
+  __TEXT.__oslogstring: 0x43ef
   __TEXT.__swift5_typeref: 0x17
-  __TEXT.__unwind_info: 0xd268
-  __TEXT.__objc_classname: 0x5999
-  __TEXT.__objc_methname: 0x22f27
-  __TEXT.__objc_methtype: 0x72b3
-  __TEXT.__objc_stubs: 0x16de0
-  __DATA_CONST.__got: 0xae8
-  __DATA_CONST.__const: 0x7328
-  __DATA_CONST.__objc_classlist: 0x1540
+  __TEXT.__unwind_info: 0xd460
+  __TEXT.__objc_classname: 0x5a20
+  __TEXT.__objc_methname: 0x2306f
+  __TEXT.__objc_methtype: 0x7322
+  __TEXT.__objc_stubs: 0x16fa0
+  __DATA_CONST.__got: 0xb08
+  __DATA_CONST.__const: 0x73e8
+  __DATA_CONST.__objc_classlist: 0x1568
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7878
+  __DATA_CONST.__objc_selrefs: 0x78c8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x17e0
+  __DATA_CONST.__objc_superrefs: 0x1810
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xcc8
-  __AUTH_CONST.__const: 0x20a0
-  __AUTH_CONST.__cfstring: 0x1dd20
-  __AUTH_CONST.__objc_const: 0x2f800
+  __AUTH_CONST.__auth_got: 0xce0
+  __AUTH_CONST.__const: 0x2078
+  __AUTH_CONST.__cfstring: 0x1dde0
+  __AUTH_CONST.__objc_const: 0x2fdf0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xaaf0
-  __DATA.__objc_ivar: 0x1430
+  __AUTH.__objc_data: 0xac80
+  __DATA.__objc_ivar: 0x1444
   __DATA.__data: 0x1f88
-  __DATA.__bss: 0x198
+  __DATA.__bss: 0x1a8
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2990
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x1319
+  __DATA_DIRTY.__bss: 0x1329
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 84160231-73B2-38ED-AF16-E49A52D3767A
-  Functions: 11286
-  Symbols:   38241
-  CStrings:  17136
+  UUID: D2FD2EBB-9395-330B-948A-B3EFA997713B
+  Functions: 11363
+  Symbols:   38549
+  CStrings:  17209
 
Symbols:
+ +[CTStewieAnywhereMessage supportsSecureCoding]
+ +[CTStewieDiagMessage supportsSecureCoding]
+ +[CTStewieIMessageLiteRawMessage supportsSecureCoding]
+ +[CTStewieSatSmsRawMessage supportsSecureCoding]
+ +[CTXPCFakeCrossPlatformEventRequest allowedClassesForArguments]
+ -[CTLazuliFileCryptoMaterial isEqualToCTLazuliFileCryptoMaterial:]
+ -[CTLazuliFileCryptoMaterial originalFileSizeInBytes]
+ -[CTLazuliFileCryptoMaterial setOriginalFileSizeInBytes:]
+ -[CTLazuliSecurity initWithReflection:]
+ -[CTLazuliSecurity isEqualToCTLazuliSecurity:]
+ -[CTStewieAnywhereMessage .cxx_destruct]
+ -[CTStewieAnywhereMessage copyWithZone:]
+ -[CTStewieAnywhereMessage data]
+ -[CTStewieAnywhereMessage description]
+ -[CTStewieAnywhereMessage encodeWithCoder:]
+ -[CTStewieAnywhereMessage initWithCoder:]
+ -[CTStewieAnywhereMessage isEqual:]
+ -[CTStewieAnywhereMessage isEqualToAnywhereMessage:]
+ -[CTStewieAnywhereMessage setData:]
+ -[CTStewieDiagMessage .cxx_destruct]
+ -[CTStewieDiagMessage copyWithZone:]
+ -[CTStewieDiagMessage data]
+ -[CTStewieDiagMessage description]
+ -[CTStewieDiagMessage encodeWithCoder:]
+ -[CTStewieDiagMessage initWithCoder:]
+ -[CTStewieDiagMessage isEqual:]
+ -[CTStewieDiagMessage isEqualToDiagMessage:]
+ -[CTStewieDiagMessage setData:]
+ -[CTStewieIMessageLiteRawMessage .cxx_destruct]
+ -[CTStewieIMessageLiteRawMessage copyWithZone:]
+ -[CTStewieIMessageLiteRawMessage data]
+ -[CTStewieIMessageLiteRawMessage description]
+ -[CTStewieIMessageLiteRawMessage encodeWithCoder:]
+ -[CTStewieIMessageLiteRawMessage initWithCoder:]
+ -[CTStewieIMessageLiteRawMessage isEqual:]
+ -[CTStewieIMessageLiteRawMessage isEqualToOther:]
+ -[CTStewieIMessageLiteRawMessage setData:]
+ -[CTStewieSatSmsRawMessage .cxx_destruct]
+ -[CTStewieSatSmsRawMessage copyWithZone:]
+ -[CTStewieSatSmsRawMessage data]
+ -[CTStewieSatSmsRawMessage description]
+ -[CTStewieSatSmsRawMessage encodeWithCoder:]
+ -[CTStewieSatSmsRawMessage initWithCoder:]
+ -[CTStewieSatSmsRawMessage isEqual:]
+ -[CTStewieSatSmsRawMessage isEqualToOther:]
+ -[CTStewieSatSmsRawMessage setData:]
+ -[CTXPCFakeCrossPlatformEventRequest eventName]
+ -[CTXPCFakeCrossPlatformEventRequest initWithEvent:payload:]
+ -[CTXPCFakeCrossPlatformEventRequest payload]
+ -[CTXPCFakeCrossPlatformEventRequest performRequestWithHandler:completionHandler:]
+ -[CTXPCFakeCrossPlatformEventRequest requiredEntitlement]
+ -[CoreTelephonyClient(CrossPlatformTransfer) fakeCrossPlatformTransferEvent:payload:completion:]
+ -[CoreTelephonyClient(CrossPlatformTransfer) fakeCrossPlatformTransferEvent:payload:completion:].cold.1
+ -[CoreTelephonyClient(Provisioning) invalidateKey:]
+ -[CoreTelephonyClient(SMS) injectMTsms:smsData:completion:]
+ GCC_except_table330
+ GCC_except_table385
+ GCC_except_table457
+ GCC_except_table473
+ GCC_except_table486
+ GCC_except_table500
+ GCC_except_table510
+ GCC_except_table518
+ GCC_except_table519
+ GCC_except_table558
+ GCC_except_table584
+ GCC_except_table598
+ GCC_except_table617
+ GCC_except_table660
+ GCC_except_table674
+ GCC_except_table675
+ GCC_except_table686
+ GCC_except_table759
+ GCC_except_table761
+ GCC_except_table769
+ GCC_except_table770
+ GCC_except_table775
+ GCC_except_table784
+ GCC_except_table786
+ GCC_except_table802
+ GCC_except_table803
+ GCC_except_table804
+ GCC_except_table806
+ GCC_except_table814
+ GCC_except_table818
+ GCC_except_table820
+ GCC_except_table828
+ GCC_except_table832
+ _CTLogCellMonitor
+ _CTLogCellMonitor.cold.1
+ _CTLogCellMonitor.logger
+ _CTLogCellMonitor.once
+ _OBJC_CLASS_$_CTStewieAnywhereMessage
+ _OBJC_CLASS_$_CTStewieDiagMessage
+ _OBJC_CLASS_$_CTStewieIMessageLiteRawMessage
+ _OBJC_CLASS_$_CTStewieSatSmsRawMessage
+ _OBJC_CLASS_$_CTXPCFakeCrossPlatformEventRequest
+ _OBJC_IVAR_$_CTLazuliFileCryptoMaterial._originalFileSizeInBytes
+ _OBJC_IVAR_$_CTStewieAnywhereMessage._data
+ _OBJC_IVAR_$_CTStewieDiagMessage._data
+ _OBJC_IVAR_$_CTStewieIMessageLiteRawMessage._data
+ _OBJC_IVAR_$_CTStewieSatSmsRawMessage._data
+ _OBJC_METACLASS_$_CTStewieAnywhereMessage
+ _OBJC_METACLASS_$_CTStewieDiagMessage
+ _OBJC_METACLASS_$_CTStewieIMessageLiteRawMessage
+ _OBJC_METACLASS_$_CTStewieSatSmsRawMessage
+ _OBJC_METACLASS_$_CTXPCFakeCrossPlatformEventRequest
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _TelephonyUtilIsOversteerEnabled
+ __CTServerConnectionGetCommCenterInitializationState.cold.1
+ __CTServerConnectionRegisterForEvent.cold.1
+ __CTServerConnectionUnregisterForAllNotifications.cold.1
+ __CTServerConnectionUnregisterForEvent.cold.1
+ __OBJC_$_CLASS_METHODS_CTStewieAnywhereMessage
+ __OBJC_$_CLASS_METHODS_CTStewieDiagMessage
+ __OBJC_$_CLASS_METHODS_CTStewieIMessageLiteRawMessage
+ __OBJC_$_CLASS_METHODS_CTStewieSatSmsRawMessage
+ __OBJC_$_CLASS_METHODS_CTXPCFakeCrossPlatformEventRequest
+ __OBJC_$_CLASS_PROP_LIST_CTStewieAnywhereMessage
+ __OBJC_$_CLASS_PROP_LIST_CTStewieDiagMessage
+ __OBJC_$_CLASS_PROP_LIST_CTStewieIMessageLiteRawMessage
+ __OBJC_$_CLASS_PROP_LIST_CTStewieSatSmsRawMessage
+ __OBJC_$_INSTANCE_METHODS_CTStewieAnywhereMessage
+ __OBJC_$_INSTANCE_METHODS_CTStewieDiagMessage
+ __OBJC_$_INSTANCE_METHODS_CTStewieIMessageLiteRawMessage
+ __OBJC_$_INSTANCE_METHODS_CTStewieSatSmsRawMessage
+ __OBJC_$_INSTANCE_METHODS_CTXPCFakeCrossPlatformEventRequest
+ __OBJC_$_INSTANCE_VARIABLES_CTStewieAnywhereMessage
+ __OBJC_$_INSTANCE_VARIABLES_CTStewieDiagMessage
+ __OBJC_$_INSTANCE_VARIABLES_CTStewieIMessageLiteRawMessage
+ __OBJC_$_INSTANCE_VARIABLES_CTStewieSatSmsRawMessage
+ __OBJC_$_PROP_LIST_CTStewieAnywhereMessage
+ __OBJC_$_PROP_LIST_CTStewieDiagMessage
+ __OBJC_$_PROP_LIST_CTStewieIMessageLiteRawMessage
+ __OBJC_$_PROP_LIST_CTStewieSatSmsRawMessage
+ __OBJC_CLASS_PROTOCOLS_$_CTStewieAnywhereMessage
+ __OBJC_CLASS_PROTOCOLS_$_CTStewieDiagMessage
+ __OBJC_CLASS_PROTOCOLS_$_CTStewieIMessageLiteRawMessage
+ __OBJC_CLASS_PROTOCOLS_$_CTStewieSatSmsRawMessage
+ __OBJC_CLASS_RO_$_CTStewieAnywhereMessage
+ __OBJC_CLASS_RO_$_CTStewieDiagMessage
+ __OBJC_CLASS_RO_$_CTStewieIMessageLiteRawMessage
+ __OBJC_CLASS_RO_$_CTStewieSatSmsRawMessage
+ __OBJC_CLASS_RO_$_CTXPCFakeCrossPlatformEventRequest
+ __OBJC_METACLASS_RO_$_CTStewieAnywhereMessage
+ __OBJC_METACLASS_RO_$_CTStewieDiagMessage
+ __OBJC_METACLASS_RO_$_CTStewieIMessageLiteRawMessage
+ __OBJC_METACLASS_RO_$_CTStewieSatSmsRawMessage
+ __OBJC_METACLASS_RO_$_CTXPCFakeCrossPlatformEventRequest
+ __Z25SendXpcMessageWithCachingP20__CTServerConnectionRKN3xpc4dictERS2_20CTFeatureRequirement.cold.1
+ __Z34encode_CTLazuliFileCryptoAlgorithmRKN6Lazuli23CryptoMaterialAlgorithmE
+ __ZL17logBlockedRequestPKcRKN3xpc4dictEP20__CTServerConnection20CTFeatureRequirement
+ __ZL17logBlockedRequestPKcRKN3xpc4dictEP20__CTServerConnection20CTFeatureRequirement.cold.1
+ __ZN12_GLOBAL__N_128ReregisterClientForAllEventsEP20__CTServerConnection.cold.1
+ __ZN13MMSPduDecoder14decodeMimePartEj.cold.10
+ __ZN13MMSPduDecoder14decodeMimePartEj.cold.11
+ __ZN13MMSPduDecoder14decodeMimePartEj.cold.12
+ __ZN13MMSPduDecoder14decodeMimePartEj.cold.13
+ __ZN13MMSPduDecoder14decodeMimePartEj.cold.9
+ __ZN13MMSPduDecoder18decodeSimpleHeaderEPK20MMSHeaderEncodingMap.cold.4
+ __ZN13MMSPduDecoder19decodeEncodedHeaderEPK20MMSHeaderEncodingMap.cold.1
+ __ZN13MMSPduDecoder19decodeMultipartBodyERNSt3__16vectorIP11MMSMimePartNS0_9allocatorIS3_EEEE.cold.2
+ __ZN13MMSPduDecoder19decodeMultipartBodyERNSt3__16vectorIP11MMSMimePartNS0_9allocatorIS3_EEEE.cold.3
+ __ZN9CCMonitor10initializeEv.cold.1
+ __ZN9CCMonitor17handleDaemonReadyEv.cold.1
+ __ZN9CCMonitorC2Ev.cold.2
+ __ZN9CCMonitorD2Ev.cold.2
+ __ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_.cold.1
+ __ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_
+ __ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_.cold.1
+ __ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_.cold.2
+ __ZZN8dispatch5asyncIZZN9CCMonitor10initializeEvEUb_E3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_
+ __ZZN8dispatch5asyncIZZN9CCMonitor10initializeEvEUb_E3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_.cold.1
+ __ZZN9CCMonitor9getLoggerEvE10sOnceToken
+ __ZZN9CCMonitor9getLoggerEvE7sLogger
+ ___51-[CoreTelephonyClient(Provisioning) invalidateKey:]_block_invoke
+ ___51-[CoreTelephonyClient(Provisioning) invalidateKey:]_block_invoke_2
+ ___52-[CTStewieDataClient createConnectionPairIfRequired]_block_invoke.92
+ ___55-[CoreTelephonyClient(Stewie) testStewieCommand:error:]_block_invoke
+ ___55-[CoreTelephonyClient(Stewie) testStewieCommand:error:]_block_invoke_2
+ ___59-[CoreTelephonyClient(SMS) injectMTsms:smsData:completion:]_block_invoke
+ ___60-[CoreTelephonyClient(Stewie) testStewieCommand:completion:]_block_invoke
+ ___69-[CTStewieDataClient sendMessageInternal:usingConnection:completion:]_block_invoke.65
+ ___69-[CTStewieDataClient sendMessageInternal:usingConnection:completion:]_block_invoke.66
+ ___82-[CTXPCFakeCrossPlatformEventRequest performRequestWithHandler:completionHandler:]_block_invoke
+ ___96-[CoreTelephonyClient(CrossPlatformTransfer) fakeCrossPlatformTransferEvent:payload:completion:]_block_invoke
+ ___96-[CoreTelephonyClient(CrossPlatformTransfer) fakeCrossPlatformTransferEvent:payload:completion:]_block_invoke_2
+ ___CTLogCellMonitor_block_invoke
+ ____ZL19sHandleNotificationP13CTServerStateN3xpc4dictE_block_invoke.99
+ ____ZL25_HandlePrepWorkBeforeSendP20__CTServerConnectionRN3xpc4dictEb_block_invoke.cold.1
+ ____ZL30_CTServerConnectionReEstablishP20__CTServerConnection_block_invoke.cold.1
+ ____ZN9CCMonitor10initializeEv_block_invoke
+ ____ZN9CCMonitor9getLoggerEv_block_invoke
+ ____ZN9CCMonitor9getLoggerEv_block_invoke.cold.1
+ ____ZNK13CTServerState21sendNotification_syncE7CTEventPK10__CFStringPK14__CFDictionary_block_invoke.12
+ ___block_descriptor_48_e8_32r40r_e34_v24?0"NSError"8"NSDictionary"16lr32l8r40l8
+ ___block_descriptor_tmp.100
+ ___block_descriptor_tmp.107
+ ___block_descriptor_tmp.120
+ ___block_descriptor_tmp.123
+ ___block_descriptor_tmp.131
+ ___block_descriptor_tmp.135
+ ___block_descriptor_tmp.35
+ ___block_descriptor_tmp.39
+ ___block_descriptor_tmp.40
+ ___block_descriptor_tmp.41
+ ___block_descriptor_tmp.44
+ ___block_descriptor_tmp.45
+ ___block_descriptor_tmp.72
+ ___block_descriptor_tmp.73
+ ___block_descriptor_tmp.74
+ ___block_descriptor_tmp.80
+ ___block_descriptor_tmp.83
+ ___block_literal_global.1020
+ ___block_literal_global.1029
+ ___block_literal_global.5
+ ___block_literal_global.64
+ _kCTStewieDiagDataKey
+ _notify_get_state
+ _notify_register_dispatch
+ _objc_msgSend$epki
+ _objc_msgSend$eventName
+ _objc_msgSend$fakeCrossPlatformTransferEvent:payload:completion:
+ _objc_msgSend$initWithEvent:payload:
+ _objc_msgSend$injectMTsms:smsData:completion:
+ _objc_msgSend$invalidateKey:with:
+ _objc_msgSend$isEqualToAnywhereMessage:
+ _objc_msgSend$isEqualToCTLazuliFileCryptoMaterial:
+ _objc_msgSend$isEqualToCTLazuliSecurity:
+ _objc_msgSend$isEqualToDiagMessage:
+ _objc_msgSend$originalFileSizeInBytes
+ _objc_msgSend$setEpki:
+ _objc_msgSend$setOriginalFileSizeInBytes:
+ _objc_msgSend$setShared:
+ _objc_msgSend$shared
+ _objc_msgSend$testStewieCommand:completion:
- -[CTLazuliFileCryptoMaterial isEqualToFileCryptoMaterial:]
- -[CTLazuliSecurity isEqualToSecurityContext:]
- GCC_except_table406
- GCC_except_table493
- GCC_except_table503
- GCC_except_table511
- GCC_except_table550
- GCC_except_table565
- GCC_except_table580
- GCC_except_table591
- GCC_except_table610
- GCC_except_table641
- GCC_except_table668
- GCC_except_table681
- GCC_except_table756
- GCC_except_table758
- GCC_except_table762
- GCC_except_table766
- GCC_except_table771
- GCC_except_table778
- GCC_except_table780
- GCC_except_table794
- GCC_except_table795
- GCC_except_table797
- GCC_except_table798
- GCC_except_table801
- GCC_except_table807
- GCC_except_table808
- GCC_except_table809
- GCC_except_table823
- __Z34encode_CTLazuliFileCryptoAlgorithmN6Lazuli23CryptoMaterialAlgorithmE
- __ZN6Lazuli11MessageTextD1Ev
- __ZN6Lazuli22MessageGeoLocationPushD1Ev
- ___52-[CTStewieDataClient createConnectionPairIfRequired]_block_invoke.88
- ___69-[CTStewieDataClient sendMessageInternal:usingConnection:completion:]_block_invoke.62
- ___69-[CTStewieDataClient sendMessageInternal:usingConnection:completion:]_block_invoke.63
- ____ZL19sHandleNotificationP13CTServerStateN3xpc4dictE_block_invoke.84
- ____ZNK13CTServerState21sendNotification_syncE7CTEventPK10__CFStringPK14__CFDictionary_block_invoke.4
- ___block_descriptor_tmp.105
- ___block_descriptor_tmp.108
- ___block_descriptor_tmp.112
- ___block_descriptor_tmp.118
- ___block_descriptor_tmp.23
- ___block_descriptor_tmp.25
- ___block_descriptor_tmp.27
- ___block_descriptor_tmp.29
- ___block_descriptor_tmp.32
- ___block_descriptor_tmp.5
- ___block_descriptor_tmp.57
- ___block_descriptor_tmp.59
- ___block_descriptor_tmp.65
- ___block_descriptor_tmp.68
- ___block_descriptor_tmp.85
- ___block_descriptor_tmp.92
- ___block_descriptor_tmp.98
- ___block_literal_global.1016
- ___block_literal_global.1021
- ___block_literal_global.91
- _objc_msgSend$isEqualToFileCryptoMaterial:
- _objc_msgSend$isEqualToSecurityContext:
CStrings:
+ "#D "
+ "#D %s"
+ "#D Body:"
+ "#D DataLen = %u"
+ "#D HeadersLen = %u"
+ "#D Part %u"
+ "#D nEntries = %u"
+ ", epki=%@, shared=%@"
+ ", originalFileSizeInBytes = %@"
+ "13105.1.1"
+ "13105.1.1~1"
+ "Available features: [%s]"
+ "Blocking %s (request: '%s', state: %s, required: %s, %p)"
+ "CTPlanTransferCapabilityNotSupportedReachedRegulatoryeSIMLimit"
+ "CTStewieAnywhereMessage"
+ "CTStewieDiagMessage"
+ "CTStewieIMessageLiteRawMessage"
+ "CTStewieRequestReasonAnywhere"
+ "CTStewieRequestReasonAnywhereTest"
+ "CTStewieRequestReasonTest"
+ "CTStewieSatSmsRawMessage"
+ "CTXPCFakeCrossPlatformEventRequest"
+ "CommCenter is always-on. CCMonitor is NOT used"
+ "Communication blocked but cached value found. Request: '%s'. Reply: '%s'"
+ "CoreTelephony logging is %s by default"
+ "Daemon becomes ready..."
+ "Failed to create notify token for '%s'. Logging is %s by default"
+ "Failed to re-register notifications in _HandleConnectionReEstablished(). Error: {domain=%d, error=%d}"
+ "Failed to re-register notifications in _HandlePrepWorkBeforeSend(). Error: {domain=%d, error=%d}"
+ "Logging is %s"
+ "OS log created"
+ "ReregisterClientForAllEvents request is not allowed at this time. Registration is delayed"
+ "T@\"NSNumber\",&,N,V_originalFileSizeInBytes"
+ "XPC message"
+ "XPC message with reply"
+ "_CTServerConnectionGetCommCenterInitializationState request is not allowed at this time"
+ "_CTServerConnectionRegisterForEvent request is not allowed at this time. Registration is delayed"
+ "_CTServerConnectionUnregisterForAllNotifications request is not allowed at this time"
+ "_CTServerConnectionUnregisterForEvent request is not allowed at this time"
+ "_originalFileSizeInBytes"
+ "async XPC message"
+ "com.apple.CoreTelephony.LoggingEnabled"
+ "diagData"
+ "eventName"
+ "fakeCrossPlatformTransferEvent:payload:completion:"
+ "feth"
+ "initWithEvent:payload:"
+ "injectMTsms:smsData:completion:"
+ "invalidateKey:"
+ "invalidateKey:with:"
+ "isEqualToAnywhereMessage:"
+ "isEqualToCTLazuliFileCryptoMaterial:"
+ "isEqualToCTLazuliSecurity:"
+ "isEqualToDiagMessage:"
+ "kBaseband"
+ "kDaemonRunning"
+ "kDefaultAllowed"
+ "kNotRunning"
+ "kOriginalFileSize"
+ "kRunning"
+ "kTestBlocked"
+ "kThumper"
+ "kUnknown"
+ "originalFileSizeInBytes"
+ "pdp_ip"
+ "setOriginalFileSizeInBytes:"
+ "v12@?0i8"
+ "v24@?0@\"NSError\"8@\"NSDictionary\"16"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSMSDataType\"24@?<v@?^@>32"
- "13091.1.14"
- "13091.1.14~1"
- "CCCallSourceMode::kCCCallSourceModeScreeningNoHO"
- "RemoteOnly"
- "isEqualToFileCryptoMaterial:"
- "isEqualToSecurityContext:"
- "kSecure"

```
