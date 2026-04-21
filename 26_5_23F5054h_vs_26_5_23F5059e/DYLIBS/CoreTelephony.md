## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-13185.1.0.0.0
-  __TEXT.__text: 0x1b6570
-  __TEXT.__auth_stubs: 0x1c70
-  __TEXT.__objc_methlist: 0x1bd4c
+13186.1.0.0.0
+  __TEXT.__text: 0x1b2b90
+  __TEXT.__auth_stubs: 0x1c40
+  __TEXT.__objc_methlist: 0x1ba6c
   __TEXT.__const: 0x1300
-  __TEXT.__gcc_except_tab: 0x204b4
-  __TEXT.__cstring: 0x1fa48
-  __TEXT.__oslogstring: 0x4ca6
+  __TEXT.__gcc_except_tab: 0x2008c
+  __TEXT.__cstring: 0x1f8d8
+  __TEXT.__oslogstring: 0x4876
   __TEXT.__swift5_typeref: 0x18d
   __TEXT.__swift5_reflstr: 0xc1
   __TEXT.__swift5_assocty: 0x48

   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0xe980
+  __TEXT.__unwind_info: 0xe7a0
   __TEXT.__eh_frame: 0x2b8
-  __TEXT.__objc_classname: 0x5bc6
-  __TEXT.__objc_methname: 0x2399a
-  __TEXT.__objc_methtype: 0x7492
-  __TEXT.__objc_stubs: 0x175a0
-  __DATA_CONST.__got: 0xb80
-  __DATA_CONST.__const: 0x73c8
-  __DATA_CONST.__objc_classlist: 0x15b8
+  __TEXT.__objc_classname: 0x5b46
+  __TEXT.__objc_methname: 0x238d3
+  __TEXT.__objc_methtype: 0x7422
+  __TEXT.__objc_stubs: 0x17420
+  __DATA_CONST.__got: 0xb60
+  __DATA_CONST.__const: 0x7328
+  __DATA_CONST.__objc_classlist: 0x1590
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a80
+  __DATA_CONST.__objc_selrefs: 0x7a40
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x1880
+  __DATA_CONST.__objc_superrefs: 0x1850
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xe50
-  __AUTH_CONST.__const: 0x2360
-  __AUTH_CONST.__cfstring: 0x1e0e0
-  __AUTH_CONST.__objc_const: 0x30828
+  __AUTH_CONST.__auth_got: 0xe38
+  __AUTH_CONST.__const: 0x2340
+  __AUTH_CONST.__cfstring: 0x1e040
+  __AUTH_CONST.__objc_const: 0x30268
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xadc0
+  __AUTH.__objc_data: 0xac30
   __AUTH.__data: 0xb0
-  __DATA.__objc_ivar: 0x1484
+  __DATA.__objc_ivar: 0x1474
   __DATA.__data: 0x20a0
   __DATA.__bss: 0x600
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2b20
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x1308
+  __DATA_DIRTY.__bss: 0x12e8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 8A5D04BA-985A-303C-B827-4F20A7184D5C
-  Functions: 11607
-  Symbols:   39139
-  CStrings:  17405
+  UUID: 963E6140-E037-354F-A778-9808D246D3A0
+  Functions: 11533
+  Symbols:   38836
+  CStrings:  17338
 
Symbols:
+ ___52-[CTStewieDataClient createConnectionPairIfRequired]_block_invoke.88
+ ___69-[CTStewieDataClient sendMessageInternal:usingConnection:completion:]_block_invoke.62
+ ___69-[CTStewieDataClient sendMessageInternal:usingConnection:completion:]_block_invoke.63
+ ____ZL19sHandleNotificationP13CTServerStateN3xpc4dictE_block_invoke.84
+ ____ZNK13CTServerState21sendNotification_syncE7CTEventPK10__CFStringPK14__CFDictionary_block_invoke.4
+ ___block_descriptor_tmp.105
+ ___block_descriptor_tmp.108
+ ___block_descriptor_tmp.112
+ ___block_descriptor_tmp.118
+ ___block_descriptor_tmp.23
+ ___block_descriptor_tmp.25
+ ___block_descriptor_tmp.27
+ ___block_descriptor_tmp.29
+ ___block_descriptor_tmp.32
+ ___block_descriptor_tmp.5
+ ___block_descriptor_tmp.57
+ ___block_descriptor_tmp.59
+ ___block_descriptor_tmp.65
+ ___block_descriptor_tmp.68
+ ___block_descriptor_tmp.85
+ ___block_descriptor_tmp.92
+ ___block_descriptor_tmp.98
+ ___block_literal_global.1023
+ ___block_literal_global.1028
+ ___block_literal_global.91
- +[CTStewieAnywhereMessage supportsSecureCoding]
- +[CTStewieDiagMessage supportsSecureCoding]
- +[CTStewieIMessageLiteRawMessage supportsSecureCoding]
- +[CTStewieSatSmsRawMessage supportsSecureCoding]
- +[CTXPCFakeCrossPlatformEventRequest allowedClassesForArguments]
- -[CTStewieAnywhereMessage .cxx_destruct]
- -[CTStewieAnywhereMessage copyWithZone:]
- -[CTStewieAnywhereMessage data]
- -[CTStewieAnywhereMessage description]
- -[CTStewieAnywhereMessage encodeWithCoder:]
- -[CTStewieAnywhereMessage initWithCoder:]
- -[CTStewieAnywhereMessage isEqual:]
- -[CTStewieAnywhereMessage isEqualToAnywhereMessage:]
- -[CTStewieAnywhereMessage setData:]
- -[CTStewieDiagMessage .cxx_destruct]
- -[CTStewieDiagMessage copyWithZone:]
- -[CTStewieDiagMessage data]
- -[CTStewieDiagMessage description]
- -[CTStewieDiagMessage encodeWithCoder:]
- -[CTStewieDiagMessage initWithCoder:]
- -[CTStewieDiagMessage isEqual:]
- -[CTStewieDiagMessage isEqualToDiagMessage:]
- -[CTStewieDiagMessage setData:]
- -[CTStewieIMessageLiteRawMessage .cxx_destruct]
- -[CTStewieIMessageLiteRawMessage copyWithZone:]
- -[CTStewieIMessageLiteRawMessage data]
- -[CTStewieIMessageLiteRawMessage description]
- -[CTStewieIMessageLiteRawMessage encodeWithCoder:]
- -[CTStewieIMessageLiteRawMessage initWithCoder:]
- -[CTStewieIMessageLiteRawMessage isEqual:]
- -[CTStewieIMessageLiteRawMessage isEqualToOther:]
- -[CTStewieIMessageLiteRawMessage setData:]
- -[CTStewieSatSmsRawMessage .cxx_destruct]
- -[CTStewieSatSmsRawMessage copyWithZone:]
- -[CTStewieSatSmsRawMessage data]
- -[CTStewieSatSmsRawMessage description]
- -[CTStewieSatSmsRawMessage encodeWithCoder:]
- -[CTStewieSatSmsRawMessage initWithCoder:]
- -[CTStewieSatSmsRawMessage isEqual:]
- -[CTStewieSatSmsRawMessage isEqualToOther:]
- -[CTStewieSatSmsRawMessage setData:]
- -[CTXPCFakeCrossPlatformEventRequest eventName]
- -[CTXPCFakeCrossPlatformEventRequest initWithEvent:payload:]
- -[CTXPCFakeCrossPlatformEventRequest payload]
- -[CTXPCFakeCrossPlatformEventRequest performRequestWithHandler:completionHandler:]
- -[CTXPCFakeCrossPlatformEventRequest requiredEntitlement]
- -[CoreTelephonyClient(CrossPlatformTransfer) fakeCrossPlatformTransferEvent:payload:completion:]
- -[CoreTelephonyClient(CrossPlatformTransfer) fakeCrossPlatformTransferEvent:payload:completion:].cold.1
- -[CoreTelephonyClient(Provisioning) invalidateKey:]
- -[CoreTelephonyClient(SMS) injectMTsms:smsData:completion:]
- _OBJC_CLASS_$_CTStewieAnywhereMessage
- _OBJC_CLASS_$_CTStewieDiagMessage
- _OBJC_CLASS_$_CTStewieIMessageLiteRawMessage
- _OBJC_CLASS_$_CTStewieSatSmsRawMessage
- _OBJC_CLASS_$_CTXPCFakeCrossPlatformEventRequest
- _OBJC_IVAR_$_CTStewieAnywhereMessage._data
- _OBJC_IVAR_$_CTStewieDiagMessage._data
- _OBJC_IVAR_$_CTStewieIMessageLiteRawMessage._data
- _OBJC_IVAR_$_CTStewieSatSmsRawMessage._data
- _OBJC_METACLASS_$_CTStewieAnywhereMessage
- _OBJC_METACLASS_$_CTStewieDiagMessage
- _OBJC_METACLASS_$_CTStewieIMessageLiteRawMessage
- _OBJC_METACLASS_$_CTStewieSatSmsRawMessage
- _OBJC_METACLASS_$_CTXPCFakeCrossPlatformEventRequest
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _TelephonyUtilIsOversteerEnabled
- __CTServerConnectionGetCommCenterInitializationState.cold.1
- __CTServerConnectionRegisterForEvent.cold.1
- __CTServerConnectionUnregisterForAllNotifications.cold.1
- __CTServerConnectionUnregisterForEvent.cold.1
- __OBJC_$_CLASS_METHODS_CTStewieAnywhereMessage
- __OBJC_$_CLASS_METHODS_CTStewieDiagMessage
- __OBJC_$_CLASS_METHODS_CTStewieIMessageLiteRawMessage
- __OBJC_$_CLASS_METHODS_CTStewieSatSmsRawMessage
- __OBJC_$_CLASS_METHODS_CTXPCFakeCrossPlatformEventRequest
- __OBJC_$_CLASS_PROP_LIST_CTStewieAnywhereMessage
- __OBJC_$_CLASS_PROP_LIST_CTStewieDiagMessage
- __OBJC_$_CLASS_PROP_LIST_CTStewieIMessageLiteRawMessage
- __OBJC_$_CLASS_PROP_LIST_CTStewieSatSmsRawMessage
- __OBJC_$_INSTANCE_METHODS_CTStewieAnywhereMessage
- __OBJC_$_INSTANCE_METHODS_CTStewieDiagMessage
- __OBJC_$_INSTANCE_METHODS_CTStewieIMessageLiteRawMessage
- __OBJC_$_INSTANCE_METHODS_CTStewieSatSmsRawMessage
- __OBJC_$_INSTANCE_METHODS_CTXPCFakeCrossPlatformEventRequest
- __OBJC_$_INSTANCE_VARIABLES_CTStewieAnywhereMessage
- __OBJC_$_INSTANCE_VARIABLES_CTStewieDiagMessage
- __OBJC_$_INSTANCE_VARIABLES_CTStewieIMessageLiteRawMessage
- __OBJC_$_INSTANCE_VARIABLES_CTStewieSatSmsRawMessage
- __OBJC_$_PROP_LIST_CTStewieAnywhereMessage
- __OBJC_$_PROP_LIST_CTStewieDiagMessage
- __OBJC_$_PROP_LIST_CTStewieIMessageLiteRawMessage
- __OBJC_$_PROP_LIST_CTStewieSatSmsRawMessage
- __OBJC_CLASS_PROTOCOLS_$_CTStewieAnywhereMessage
- __OBJC_CLASS_PROTOCOLS_$_CTStewieDiagMessage
- __OBJC_CLASS_PROTOCOLS_$_CTStewieIMessageLiteRawMessage
- __OBJC_CLASS_PROTOCOLS_$_CTStewieSatSmsRawMessage
- __OBJC_CLASS_RO_$_CTStewieAnywhereMessage
- __OBJC_CLASS_RO_$_CTStewieDiagMessage
- __OBJC_CLASS_RO_$_CTStewieIMessageLiteRawMessage
- __OBJC_CLASS_RO_$_CTStewieSatSmsRawMessage
- __OBJC_CLASS_RO_$_CTXPCFakeCrossPlatformEventRequest
- __OBJC_METACLASS_RO_$_CTStewieAnywhereMessage
- __OBJC_METACLASS_RO_$_CTStewieDiagMessage
- __OBJC_METACLASS_RO_$_CTStewieIMessageLiteRawMessage
- __OBJC_METACLASS_RO_$_CTStewieSatSmsRawMessage
- __OBJC_METACLASS_RO_$_CTXPCFakeCrossPlatformEventRequest
- __Z25SendXpcMessageWithCachingP20__CTServerConnectionRKN3xpc4dictERS2_20CTFeatureRequirement.cold.1
- __ZL17logBlockedRequestPKcRKN3xpc4dictEP20__CTServerConnection20CTFeatureRequirement
- __ZL17logBlockedRequestPKcRKN3xpc4dictEP20__CTServerConnection20CTFeatureRequirement.cold.1
- __ZN12_GLOBAL__N_128ReregisterClientForAllEventsEP20__CTServerConnection.cold.1
- __ZN13MMSPduDecoder14decodeMimePartEj.cold.10
- __ZN13MMSPduDecoder14decodeMimePartEj.cold.11
- __ZN13MMSPduDecoder14decodeMimePartEj.cold.12
- __ZN13MMSPduDecoder14decodeMimePartEj.cold.13
- __ZN13MMSPduDecoder14decodeMimePartEj.cold.9
- __ZN13MMSPduDecoder18decodeSimpleHeaderEPK20MMSHeaderEncodingMap.cold.4
- __ZN13MMSPduDecoder19decodeEncodedHeaderEPK20MMSHeaderEncodingMap.cold.1
- __ZN13MMSPduDecoder19decodeMultipartBodyERNSt3__16vectorIP11MMSMimePartNS0_9allocatorIS3_EEEE.cold.2
- __ZN13MMSPduDecoder19decodeMultipartBodyERNSt3__16vectorIP11MMSMimePartNS0_9allocatorIS3_EEEE.cold.3
- __ZN9CCMonitor10initializeEv.cold.1
- __ZN9CCMonitor17handleDaemonReadyEv.cold.1
- __ZN9CCMonitorC2Ev.cold.2
- __ZN9CCMonitorD2Ev.cold.2
- __ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_.cold.1
- __ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_
- __ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_.cold.1
- __ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_.cold.2
- __ZZN8dispatch5asyncIZZN9CCMonitor10initializeEvEUb_E3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_
- __ZZN8dispatch5asyncIZZN9CCMonitor10initializeEvEUb_E3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_.cold.1
- __ZZN9CCMonitor9getLoggerEvE10sOnceToken
- __ZZN9CCMonitor9getLoggerEvE7sLogger
- ___51-[CoreTelephonyClient(Provisioning) invalidateKey:]_block_invoke
- ___51-[CoreTelephonyClient(Provisioning) invalidateKey:]_block_invoke_2
- ___52-[CTStewieDataClient createConnectionPairIfRequired]_block_invoke.92
- ___55-[CoreTelephonyClient(Stewie) testStewieCommand:error:]_block_invoke
- ___55-[CoreTelephonyClient(Stewie) testStewieCommand:error:]_block_invoke_2
- ___59-[CoreTelephonyClient(SMS) injectMTsms:smsData:completion:]_block_invoke
- ___60-[CoreTelephonyClient(Stewie) testStewieCommand:completion:]_block_invoke
- ___69-[CTStewieDataClient sendMessageInternal:usingConnection:completion:]_block_invoke.65
- ___69-[CTStewieDataClient sendMessageInternal:usingConnection:completion:]_block_invoke.66
- ___82-[CTXPCFakeCrossPlatformEventRequest performRequestWithHandler:completionHandler:]_block_invoke
- ___96-[CoreTelephonyClient(CrossPlatformTransfer) fakeCrossPlatformTransferEvent:payload:completion:]_block_invoke
- ___96-[CoreTelephonyClient(CrossPlatformTransfer) fakeCrossPlatformTransferEvent:payload:completion:]_block_invoke_2
- ____ZL19sHandleNotificationP13CTServerStateN3xpc4dictE_block_invoke.99
- ____ZL25_HandlePrepWorkBeforeSendP20__CTServerConnectionRN3xpc4dictEb_block_invoke.cold.1
- ____ZL30_CTServerConnectionReEstablishP20__CTServerConnection_block_invoke.cold.1
- ____ZN9CCMonitor10initializeEv_block_invoke
- ____ZN9CCMonitor9getLoggerEv_block_invoke
- ____ZN9CCMonitor9getLoggerEv_block_invoke.cold.1
- ____ZNK13CTServerState21sendNotification_syncE7CTEventPK10__CFStringPK14__CFDictionary_block_invoke.12
- ___block_descriptor_48_e8_32r40r_e34_v24?0"NSError"8"NSDictionary"16lr32l8r40l8
- ___block_descriptor_tmp.100
- ___block_descriptor_tmp.107
- ___block_descriptor_tmp.120
- ___block_descriptor_tmp.123
- ___block_descriptor_tmp.131
- ___block_descriptor_tmp.135
- ___block_descriptor_tmp.35
- ___block_descriptor_tmp.39
- ___block_descriptor_tmp.40
- ___block_descriptor_tmp.41
- ___block_descriptor_tmp.44
- ___block_descriptor_tmp.45
- ___block_descriptor_tmp.72
- ___block_descriptor_tmp.73
- ___block_descriptor_tmp.74
- ___block_descriptor_tmp.80
- ___block_descriptor_tmp.83
- ___block_literal_global.1027
- ___block_literal_global.1036
- ___block_literal_global.5
- _kCTStewieDiagDataKey
- _notify_get_state
- _notify_register_dispatch
- _objc_msgSend$epki
- _objc_msgSend$eventName
- _objc_msgSend$fakeCrossPlatformTransferEvent:payload:completion:
- _objc_msgSend$initWithEvent:payload:
- _objc_msgSend$injectMTsms:smsData:completion:
- _objc_msgSend$invalidateKey:with:
- _objc_msgSend$isEqualToAnywhereMessage:
- _objc_msgSend$isEqualToDiagMessage:
- _objc_msgSend$setEpki:
- _objc_msgSend$setShared:
- _objc_msgSend$shared
- _objc_msgSend$testStewieCommand:completion:
CStrings:
+ "13186.1"
+ "13186.1~71"
- "#D "
- "#D %s"
- "#D Body:"
- "#D DataLen = %u"
- "#D HeadersLen = %u"
- "#D Part %u"
- "#D nEntries = %u"
- ", epki=%@, shared=%@"
- "13185.1"
- "13185.1~19"
- "Available features: [%s]"
- "Blocking %s (request: '%s', state: %s, required: %s, %p)"
- "CTStewieAnywhereMessage"
- "CTStewieDiagMessage"
- "CTStewieIMessageLiteRawMessage"
- "CTStewieRequestReasonAnywhere"
- "CTStewieRequestReasonAnywhereTest"
- "CTStewieRequestReasonTest"
- "CTStewieSatSmsRawMessage"
- "CTXPCFakeCrossPlatformEventRequest"
- "CommCenter is always-on. CCMonitor is NOT used"
- "Communication blocked but cached value found. Request: '%s'. Reply: '%s'"
- "CoreTelephony logging is %s by default"
- "Daemon becomes ready..."
- "Failed to create notify token for '%s'. Logging is %s by default"
- "Failed to re-register notifications in _HandleConnectionReEstablished(). Error: {domain=%d, error=%d}"
- "Failed to re-register notifications in _HandlePrepWorkBeforeSend(). Error: {domain=%d, error=%d}"
- "Logging is %s"
- "OS log created"
- "ReregisterClientForAllEvents request is not allowed at this time. Registration is delayed"
- "XPC message"
- "XPC message with reply"
- "_CTServerConnectionGetCommCenterInitializationState request is not allowed at this time"
- "_CTServerConnectionRegisterForEvent request is not allowed at this time. Registration is delayed"
- "_CTServerConnectionUnregisterForAllNotifications request is not allowed at this time"
- "_CTServerConnectionUnregisterForEvent request is not allowed at this time"
- "async XPC message"
- "com.apple.CoreTelephony.LoggingEnabled"
- "diagData"
- "eventName"
- "fakeCrossPlatformTransferEvent:payload:completion:"
- "feth"
- "initWithEvent:payload:"
- "injectMTsms:smsData:completion:"
- "invalidateKey:"
- "invalidateKey:with:"
- "isEqualToAnywhereMessage:"
- "isEqualToDiagMessage:"
- "kBaseband"
- "kDaemonRunning"
- "kDefaultAllowed"
- "kNotRunning"
- "kRunning"
- "kTestBlocked"
- "kThumper"
- "kUnknown"
- "pdp_ip"
- "v12@?0i8"
- "v24@?0@\"NSError\"8@\"NSDictionary\"16"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
- "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSMSDataType\"24@?<v@?^@>32"

```
