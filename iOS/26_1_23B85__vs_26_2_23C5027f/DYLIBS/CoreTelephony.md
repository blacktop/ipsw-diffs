## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-13114.1.0.0.0
-  __TEXT.__text: 0x19474c
-  __TEXT.__auth_stubs: 0x1990
-  __TEXT.__objc_methlist: 0x1b4f4
+13123.3.0.0.0
+  __TEXT.__text: 0x1982bc
+  __TEXT.__auth_stubs: 0x19c0
+  __TEXT.__objc_methlist: 0x1b804
   __TEXT.__const: 0x1012
-  __TEXT.__gcc_except_tab: 0x1f4d0
-  __TEXT.__cstring: 0x1f9a4
-  __TEXT.__oslogstring: 0x409e
+  __TEXT.__gcc_except_tab: 0x1f948
+  __TEXT.__cstring: 0x1fb6e
+  __TEXT.__oslogstring: 0x44d0
   __TEXT.__swift5_typeref: 0x17
-  __TEXT.__unwind_info: 0xd2b0
-  __TEXT.__objc_classname: 0x5999
-  __TEXT.__objc_methname: 0x2309d
-  __TEXT.__objc_methtype: 0x72b3
-  __TEXT.__objc_stubs: 0x16ec0
-  __DATA_CONST.__got: 0xae8
-  __DATA_CONST.__const: 0x7380
-  __DATA_CONST.__objc_classlist: 0x1540
+  __TEXT.__unwind_info: 0xd478
+  __TEXT.__objc_classname: 0x5a20
+  __TEXT.__objc_methname: 0x2323e
+  __TEXT.__objc_methtype: 0x734f
+  __TEXT.__objc_stubs: 0x170c0
+  __DATA_CONST.__got: 0xb08
+  __DATA_CONST.__const: 0x7420
+  __DATA_CONST.__objc_classlist: 0x1568
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x78b8
+  __DATA_CONST.__objc_selrefs: 0x7920
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x17e0
+  __DATA_CONST.__objc_superrefs: 0x1810
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xce0
-  __AUTH_CONST.__const: 0x2058
-  __AUTH_CONST.__cfstring: 0x1dda0
-  __AUTH_CONST.__objc_const: 0x2f860
+  __AUTH_CONST.__auth_got: 0xcf8
+  __AUTH_CONST.__const: 0x2078
+  __AUTH_CONST.__cfstring: 0x1dec0
+  __AUTH_CONST.__objc_const: 0x2fe80
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xaa50
-  __DATA.__objc_ivar: 0x1438
+  __AUTH.__objc_data: 0xabe0
+  __DATA.__objc_ivar: 0x1450
   __DATA.__data: 0x1f88
   __DATA.__bss: 0x1a8
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2a30
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x1319
+  __DATA_DIRTY.__bss: 0x1329
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 2FE6CDE8-E28D-3EC5-B767-6520FE95808F
-  Functions: 11299
-  Symbols:   38285
-  CStrings:  17162
+  UUID: DB701B6E-15BD-3B95-A353-F5F6044A17E7
+  Functions: 11376
+  Symbols:   38594
+  CStrings:  17246
 
Symbols:
+ +[CTStewieAnywhereMessage supportsSecureCoding]
+ +[CTStewieDiagMessage supportsSecureCoding]
+ +[CTStewieIMessageLiteRawMessage supportsSecureCoding]
+ +[CTStewieSatSmsRawMessage supportsSecureCoding]
+ +[CTXPCFakeCrossPlatformEventRequest allowedClassesForArguments]
+ -[CTLazuliOriginalMessageID sentAt]
+ -[CTLazuliOriginalMessageID setSentAt:]
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
+ -[CTStewieState searchingForTerrestrialNetworks]
+ -[CTStewieState setTerrestrialNwAssessmentPending:]
+ -[CTStewieState terrestrialNwAssessmentPending]
+ -[CTXPCFakeCrossPlatformEventRequest eventName]
+ -[CTXPCFakeCrossPlatformEventRequest initWithEvent:payload:]
+ -[CTXPCFakeCrossPlatformEventRequest payload]
+ -[CTXPCFakeCrossPlatformEventRequest performRequestWithHandler:completionHandler:]
+ -[CTXPCFakeCrossPlatformEventRequest requiredEntitlement]
+ -[CoreTelephonyClient(CrossPlatformTransfer) fakeCrossPlatformTransferEvent:payload:completion:]
+ -[CoreTelephonyClient(CrossPlatformTransfer) fakeCrossPlatformTransferEvent:payload:completion:].cold.1
+ -[CoreTelephonyClient(Provisioning) invalidateKey:]
+ -[CoreTelephonyClient(SMS) injectMTsms:smsData:completion:]
+ GCC_except_table363
+ GCC_except_table445
+ GCC_except_table477
+ GCC_except_table511
+ GCC_except_table562
+ GCC_except_table678
+ GCC_except_table765
+ GCC_except_table769
+ GCC_except_table773
+ GCC_except_table774
+ GCC_except_table779
+ GCC_except_table790
+ GCC_except_table803
+ GCC_except_table809
+ GCC_except_table810
+ GCC_except_table818
+ GCC_except_table821
+ GCC_except_table826
+ GCC_except_table831
+ GCC_except_table832
+ GCC_except_table836
+ _OBJC_CLASS_$_CTStewieAnywhereMessage
+ _OBJC_CLASS_$_CTStewieDiagMessage
+ _OBJC_CLASS_$_CTStewieIMessageLiteRawMessage
+ _OBJC_CLASS_$_CTStewieSatSmsRawMessage
+ _OBJC_CLASS_$_CTXPCFakeCrossPlatformEventRequest
+ _OBJC_IVAR_$_CTLazuliOriginalMessageID._sentAt
+ _OBJC_IVAR_$_CTStewieAnywhereMessage._data
+ _OBJC_IVAR_$_CTStewieDiagMessage._data
+ _OBJC_IVAR_$_CTStewieIMessageLiteRawMessage._data
+ _OBJC_IVAR_$_CTStewieSatSmsRawMessage._data
+ _OBJC_IVAR_$_CTStewieState._terrestrialNwAssessmentPending
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
+ __ZNSt3__110unique_ptrIZ33-[CoreTelephonyClientMux dealloc]E3$_2NS_14default_deleteIS1_EEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrIZ41-[CoreTelephonyClientMux removeDelegate:]E3$_4NS_14default_deleteIS1_EEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrIZ44-[CoreTelephonyClientMux addDelegate:queue:]E3$_3NS_14default_deleteIS1_EEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrIZ50-[CoreTelephonyClientMux sink:handleNotification:]E3$_7NS_14default_deleteIS1_EEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrIZ70-[CoreTelephonyClientMux _sendConnectionInterruptedNotification_sync:]E4$_10NS_14default_deleteIS1_EEED1B8nn200100Ev
+ __ZZ45-[CoreTelephonyClientMux _getAssertionTypeId]EN4$_128__invokeEPv
+ __ZZN8dispatch5asyncIZ33-[CoreTelephonyClientMux dealloc]E3$_2EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
+ __ZZN8dispatch5asyncIZ41-[CoreTelephonyClientMux removeDelegate:]E3$_4EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
+ __ZZN8dispatch5asyncIZ41-[CoreTelephonyClientMux removeDelegate:]E3$_4EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_.cold.1
+ __ZZN8dispatch5asyncIZ44-[CoreTelephonyClientMux addDelegate:queue:]E3$_3EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
+ __ZZN8dispatch5asyncIZ50-[CoreTelephonyClientMux sink:handleNotification:]E3$_7EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
+ __ZZN8dispatch5asyncIZ70-[CoreTelephonyClientMux _sendConnectionInterruptedNotification_sync:]E4$_10EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
+ __ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_.cold.1
+ __ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_
+ __ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_.cold.1
+ __ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_.cold.2
+ __ZZN8dispatch5asyncIZZN9CCMonitor10initializeEvEUb_E3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_
+ __ZZN8dispatch5asyncIZZN9CCMonitor10initializeEvEUb_E3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_.cold.1
+ __ZZN9CCMonitor9getLoggerEvE10sOnceToken
+ __ZZN9CCMonitor9getLoggerEvE7sLogger
+ __ZZZ45-[CoreTelephonyClientMux _getAssertionTypeId]ENK4$_12clEPvE27kCTAssertionConnectionClass
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
+ ____ZL19sHandleNotificationP13CTServerStateN3xpc4dictE_block_invoke.99
+ ____ZL25_HandlePrepWorkBeforeSendP20__CTServerConnectionRN3xpc4dictEb_block_invoke.cold.1
+ ____ZL30_CTServerConnectionReEstablishP20__CTServerConnection_block_invoke.cold.1
+ ____ZN8dispatch9sync_implIZ54-[CoreTelephonyClientMux proxyWithQueue:errorHandler:]E3$_8EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
+ ____ZN8dispatch9sync_implIZ59-[CoreTelephonyClientMux synchronousProxyWithErrorHandler:]E3$_9EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
+ ____ZN8dispatch9sync_implIZ69-[CoreTelephonyClientMux removeAssertionForInvalidationNotification:]E4$_11EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
+ ____ZN8dispatch9sync_implIZ90-[CoreTelephonyClientMux registerBlockForInvalidationNotification:callbackQueue:callback:]E4$_13EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
+ ____ZN9CCMonitor10initializeEv_block_invoke
+ ____ZN9CCMonitor9getLoggerEv_block_invoke
+ ____ZN9CCMonitor9getLoggerEv_block_invoke.cold.1
+ ____ZNK13CTServerState21sendNotification_syncE7CTEventPK10__CFStringPK14__CFDictionary_block_invoke.12
+ ____ZZ41-[CoreTelephonyClientMux removeDelegate:]ENK3$_4clEv_block_invoke
+ ____ZZ41-[CoreTelephonyClientMux removeDelegate:]ENK3$_4clEv_block_invoke.cold.1
+ ____ZZ44-[CoreTelephonyClientMux addDelegate:queue:]ENK3$_3clEv_block_invoke
+ ____ZZ44-[CoreTelephonyClientMux addDelegate:queue:]ENK3$_3clEv_block_invoke.cold.1
+ ____ZZ59-[CoreTelephonyClientMux synchronousProxyWithErrorHandler:]ENK3$_9clEv_block_invoke
+ ____ZZ59-[CoreTelephonyClientMux synchronousProxyWithErrorHandler:]ENK3$_9clEv_block_invoke.cold.1
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
+ _objc_msgSend$isEqualToDiagMessage:
+ _objc_msgSend$sentAt
+ _objc_msgSend$setEpki:
+ _objc_msgSend$setSentAt:
+ _objc_msgSend$setShared:
+ _objc_msgSend$setTerrestrialNwAssessmentPending:
+ _objc_msgSend$shared
+ _objc_msgSend$terrestrialNwAssessmentPending
+ _objc_msgSend$testStewieCommand:completion:
- GCC_except_table394
- GCC_except_table409
- GCC_except_table437
- GCC_except_table453
- GCC_except_table469
- GCC_except_table504
- GCC_except_table515
- GCC_except_table568
- GCC_except_table569
- GCC_except_table591
- GCC_except_table597
- GCC_except_table613
- GCC_except_table614
- GCC_except_table671
- GCC_except_table711
- GCC_except_table715
- GCC_except_table761
- GCC_except_table767
- GCC_except_table771
- GCC_except_table772
- GCC_except_table777
- GCC_except_table784
- GCC_except_table801
- GCC_except_table802
- GCC_except_table805
- GCC_except_table812
- GCC_except_table815
- GCC_except_table820
- GCC_except_table829
- GCC_except_table830
- GCC_except_table834
- __ZNSt3__110unique_ptrIZ33-[CoreTelephonyClientMux dealloc]E3$_0NS_14default_deleteIS1_EEED1B8nn200100Ev
- __ZNSt3__110unique_ptrIZ41-[CoreTelephonyClientMux removeDelegate:]E3$_2NS_14default_deleteIS1_EEED1B8nn200100Ev
- __ZNSt3__110unique_ptrIZ44-[CoreTelephonyClientMux addDelegate:queue:]E3$_1NS_14default_deleteIS1_EEED1B8nn200100Ev
- __ZNSt3__110unique_ptrIZ50-[CoreTelephonyClientMux sink:handleNotification:]E3$_3NS_14default_deleteIS1_EEED1B8nn200100Ev
- __ZNSt3__110unique_ptrIZ70-[CoreTelephonyClientMux _sendConnectionInterruptedNotification_sync:]E3$_6NS_14default_deleteIS1_EEED1B8nn200100Ev
- __ZZ45-[CoreTelephonyClientMux _getAssertionTypeId]EN3$_88__invokeEPv
- __ZZN8dispatch5asyncIZ33-[CoreTelephonyClientMux dealloc]E3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
- __ZZN8dispatch5asyncIZ41-[CoreTelephonyClientMux removeDelegate:]E3$_2EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
- __ZZN8dispatch5asyncIZ41-[CoreTelephonyClientMux removeDelegate:]E3$_2EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_.cold.1
- __ZZN8dispatch5asyncIZ44-[CoreTelephonyClientMux addDelegate:queue:]E3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
- __ZZN8dispatch5asyncIZ50-[CoreTelephonyClientMux sink:handleNotification:]E3$_3EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
- __ZZN8dispatch5asyncIZ70-[CoreTelephonyClientMux _sendConnectionInterruptedNotification_sync:]E3$_6EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS4_14default_deleteIS6_EEEEENUlPvE_8__invokeESA_
- __ZZZ45-[CoreTelephonyClientMux _getAssertionTypeId]ENK3$_8clEPvE27kCTAssertionConnectionClass
- ___52-[CTStewieDataClient createConnectionPairIfRequired]_block_invoke.88
- ___69-[CTStewieDataClient sendMessageInternal:usingConnection:completion:]_block_invoke.62
- ___69-[CTStewieDataClient sendMessageInternal:usingConnection:completion:]_block_invoke.63
- ____ZL19sHandleNotificationP13CTServerStateN3xpc4dictE_block_invoke.84
- ____ZN8dispatch9sync_implIZ54-[CoreTelephonyClientMux proxyWithQueue:errorHandler:]E3$_4EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
- ____ZN8dispatch9sync_implIZ59-[CoreTelephonyClientMux synchronousProxyWithErrorHandler:]E3$_5EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
- ____ZN8dispatch9sync_implIZ69-[CoreTelephonyClientMux removeAssertionForInvalidationNotification:]E3$_7EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
- ____ZN8dispatch9sync_implIZ90-[CoreTelephonyClientMux registerBlockForInvalidationNotification:callbackQueue:callback:]E3$_9EEvP16dispatch_queue_sOT_NSt3__117integral_constantIbLb1EEE_block_invoke
- ____ZNK13CTServerState21sendNotification_syncE7CTEventPK10__CFStringPK14__CFDictionary_block_invoke.4
- ____ZZ41-[CoreTelephonyClientMux removeDelegate:]ENK3$_2clEv_block_invoke
- ____ZZ41-[CoreTelephonyClientMux removeDelegate:]ENK3$_2clEv_block_invoke.cold.1
- ____ZZ44-[CoreTelephonyClientMux addDelegate:queue:]ENK3$_1clEv_block_invoke
- ____ZZ44-[CoreTelephonyClientMux addDelegate:queue:]ENK3$_1clEv_block_invoke.cold.1
- ____ZZ59-[CoreTelephonyClientMux synchronousProxyWithErrorHandler:]ENK3$_5clEv_block_invoke
- ____ZZ59-[CoreTelephonyClientMux synchronousProxyWithErrorHandler:]ENK3$_5clEv_block_invoke.cold.1
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
CStrings:
+ "#D "
+ "#D %s"
+ "#D Body:"
+ "#D DataLen = %u"
+ "#D HeadersLen = %u"
+ "#D Part %u"
+ "#D nEntries = %u"
+ ", Replace Message=%u"
+ ", Reply Enabled=%d"
+ ", epki=%@, shared=%@"
+ ", sentAt = %@"
+ ", terrestrialNwAssessmentPending=%s"
+ "13123.3"
+ "13123.3~1"
+ "@24@0:8r^{StewieState=SSSSSSSSSCCCBB}16"
+ "@80@0:8{MCC=S{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}16{MNC=S{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}48"
+ "Available features: [%s]"
+ "Blocking %s (request: '%s', state: %s, required: %s, %p)"
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
+ "T@\"NSDate\",C,N,V_sentAt"
+ "TB,N,V_terrestrialNwAssessmentPending"
+ "XPC message"
+ "XPC message with reply"
+ "_CTServerConnectionGetCommCenterInitializationState request is not allowed at this time"
+ "_CTServerConnectionRegisterForEvent request is not allowed at this time. Registration is delayed"
+ "_CTServerConnectionUnregisterForAllNotifications request is not allowed at this time"
+ "_CTServerConnectionUnregisterForEvent request is not allowed at this time"
+ "_sentAt"
+ "_terrestrialNwAssessmentPending"
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
+ "isEqualToDiagMessage:"
+ "kBaseband"
+ "kDaemonRunning"
+ "kDefaultAllowed"
+ "kNotRunning"
+ "kRunning"
+ "kSentAtKey"
+ "kTestBlocked"
+ "kThumper"
+ "kUnknown"
+ "pdp_ip"
+ "searchingForTerrestrialNetworks"
+ "sentAt"
+ "setSentAt:"
+ "setTerrestrialNwAssessmentPending:"
+ "terrestrialNwAssessmentPending"
+ "v12@?0i8"
+ "v24@?0@\"NSError\"8@\"NSDictionary\"16"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSMSDataType\"24@?<v@?^@>32"
+ "{map<__CTAssertionType *, std::pair<dispatch::queue, void (^)(NSError *)>, std::less<__CTAssertionType *>, std::allocator<std::pair<__CTAssertionType *const, std::pair<dispatch::queue, void (^)(NSError *)>>>>=\"__tree_\"{__tree<std::__value_type<__CTAssertionType *, std::pair<dispatch::queue, void (^)(NSError *)>>, std::__map_value_compare<__CTAssertionType *, std::__value_type<__CTAssertionType *, std::pair<dispatch::queue, void (^)(NSError *)>>, std::less<__CTAssertionType *>>, std::allocator<std::__value_type<__CTAssertionType *, std::pair<dispatch::queue, void (^)(NSError *)>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{map<__unsafe_unretained id, (anonymous namespace)::DelegateContext, std::less<__unsafe_unretained id>, std::allocator<std::pair<const __unsafe_unretained id, (anonymous namespace)::DelegateContext>>>=\"__tree_\"{__tree<std::__value_type<__unsafe_unretained id, (anonymous namespace)::DelegateContext>, std::__map_value_compare<__unsafe_unretained id, std::__value_type<__unsafe_unretained id, (anonymous namespace)::DelegateContext>, std::less<__unsafe_unretained id>>, std::allocator<std::__value_type<__unsafe_unretained id, (anonymous namespace)::DelegateContext>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{map<std::string, dispatch::block<void (^)(CTStewieMessageAck *, NSDictionary *)>, std::less<std::string>, std::allocator<std::pair<const std::string, dispatch::block<void (^)(CTStewieMessageAck *, NSDictionary *)>>>>=\"__tree_\"{__tree<std::__value_type<std::string, dispatch::block<void (^)(CTStewieMessageAck *, NSDictionary *)>>, std::__map_value_compare<std::string, std::__value_type<std::string, dispatch::block<void (^)(CTStewieMessageAck *, NSDictionary *)>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, dispatch::block<void (^)(CTStewieMessageAck *, NSDictionary *)>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- ", Replace Message=%{bool}u"
- ", Reply Enabled=%{bool}d"
- "13114.1"
- "13114.1~59"
- "@24@0:8r^{StewieState=SSSSSSSSSCCCB}16"
- "@80@0:8{MCC=S{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16{MNC=S{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}48"
- "{map<__CTAssertionType *, std::pair<dispatch::queue, void (^)(NSError *)>, std::less<__CTAssertionType *>, std::allocator<std::pair<__CTAssertionType *const, std::pair<dispatch::queue, void (^)(NSError *)>>>>=\"__tree_\"{__tree<std::__value_type<__CTAssertionType *, std::pair<dispatch::queue, void (^)(NSError *)>>, std::__map_value_compare<__CTAssertionType *, std::__value_type<__CTAssertionType *, std::pair<dispatch::queue, void (^)(NSError *)>>, std::less<__CTAssertionType *>>, std::allocator<std::__value_type<__CTAssertionType *, std::pair<dispatch::queue, void (^)(NSError *)>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{map<__unsafe_unretained id, (anonymous namespace)::DelegateContext, std::less<__unsafe_unretained id>, std::allocator<std::pair<const __unsafe_unretained id, (anonymous namespace)::DelegateContext>>>=\"__tree_\"{__tree<std::__value_type<__unsafe_unretained id, (anonymous namespace)::DelegateContext>, std::__map_value_compare<__unsafe_unretained id, std::__value_type<__unsafe_unretained id, (anonymous namespace)::DelegateContext>, std::less<__unsafe_unretained id>>, std::allocator<std::__value_type<__unsafe_unretained id, (anonymous namespace)::DelegateContext>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{map<std::string, dispatch::block<void (^)(CTStewieMessageAck *, NSDictionary *)>, std::less<std::string>, std::allocator<std::pair<const std::string, dispatch::block<void (^)(CTStewieMessageAck *, NSDictionary *)>>>>=\"__tree_\"{__tree<std::__value_type<std::string, dispatch::block<void (^)(CTStewieMessageAck *, NSDictionary *)>>, std::__map_value_compare<std::string, std::__value_type<std::string, dispatch::block<void (^)(CTStewieMessageAck *, NSDictionary *)>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, dispatch::block<void (^)(CTStewieMessageAck *, NSDictionary *)>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"

```
