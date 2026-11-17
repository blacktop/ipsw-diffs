## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-13504.1.0.0.0
-  __TEXT.__text: 0x1cc1fc
-  __TEXT.__objc_methlist: 0x1fb8c
+13508.0.0.0.0
+  __TEXT.__text: 0x1c9434
+  __TEXT.__objc_methlist: 0x1f91c
   __TEXT.__const: 0x1746
-  __TEXT.__gcc_except_tab: 0x25ab8
-  __TEXT.__cstring: 0x223e8
-  __TEXT.__oslogstring: 0x5526
+  __TEXT.__gcc_except_tab: 0x25764
+  __TEXT.__cstring: 0x222a8
+  __TEXT.__oslogstring: 0x5106
   __TEXT.__swift5_typeref: 0x2b4
   __TEXT.__constg_swiftt: 0x140
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__unwind_info: 0x11b50
+  __TEXT.__unwind_info: 0x119b8
   __TEXT.__eh_frame: 0x370
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7908
-  __DATA_CONST.__objc_classlist: 0x1988
+  __DATA_CONST.__const: 0x7870
+  __DATA_CONST.__objc_classlist: 0x1968
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x88e8
+  __DATA_CONST.__objc_selrefs: 0x88c8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x1d78
+  __DATA_CONST.__objc_superrefs: 0x1d58
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0xc58
-  __AUTH_CONST.__const: 0x2738
-  __AUTH_CONST.__cfstring: 0x20c40
-  __AUTH_CONST.__objc_const: 0x376f0
+  __DATA_CONST.__got: 0xc38
+  __AUTH_CONST.__const: 0x2718
+  __AUTH_CONST.__cfstring: 0x20be0
+  __AUTH_CONST.__objc_const: 0x371d8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0xf88
-  __AUTH.__objc_data: 0xd138
+  __AUTH_CONST.__auth_got: 0xf70
+  __AUTH.__objc_data: 0xcff8
   __AUTH.__data: 0xb0
-  __DATA.__objc_ivar: 0x16bc
+  __DATA.__objc_ivar: 0x16ac
   __DATA.__data: 0x2360
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2dc8
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x12e8
+  __DATA_DIRTY.__bss: 0x12c8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 13115
-  Symbols:   24209
-  CStrings:  6562
+  Functions: 13053
+  Symbols:   24106
+  CStrings:  6520
 
Symbols:
+ +[CTXPCLazuliDiagnosticCommandRequest allowedClassesForArguments]
+ -[CTXPCLazuliDiagnosticCommandRequest command]
+ -[CTXPCLazuliDiagnosticCommandRequest ct_shortName]
+ -[CTXPCLazuliDiagnosticCommandRequest initWithCommand:]
+ -[CTXPCLazuliDiagnosticCommandRequest performRequestWithHandler:completionHandler:]
+ -[CTXPCLazuliDiagnosticCommandRequest requiredEntitlement]
+ -[CoreTelephonyClient(Lazuli) runLazuliDiagnosticCommand:withError:]
+ GCC_except_table384
+ _OBJC_CLASS_$_CTXPCLazuliDiagnosticCommandRequest
+ _OBJC_METACLASS_$_CTXPCLazuliDiagnosticCommandRequest
+ __OBJC_$_CLASS_METHODS_CTXPCLazuliDiagnosticCommandRequest
+ __OBJC_$_INSTANCE_METHODS_CTXPCLazuliDiagnosticCommandRequest
+ __OBJC_$_PROP_LIST_CTXPCLazuliDiagnosticCommandRequest
+ __OBJC_CLASS_RO_$_CTXPCLazuliDiagnosticCommandRequest
+ __OBJC_METACLASS_RO_$_CTXPCLazuliDiagnosticCommandRequest
+ ___68-[CoreTelephonyClient(Lazuli) runLazuliDiagnosticCommand:withError:]_block_invoke
+ ___68-[CoreTelephonyClient(Lazuli) runLazuliDiagnosticCommand:withError:]_block_invoke_2
+ ___83-[CTXPCLazuliDiagnosticCommandRequest performRequestWithHandler:completionHandler:]_block_invoke
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
- _OUTLINED_FUNCTION_10
- _TelephonyUtilIsOversteerEnabled
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
- __ZL17logBlockedRequestPKcRKN3xpc4dictEP20__CTServerConnection20CTFeatureRequirement
- __ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_
- __ZZN8dispatch5asyncIZZN9CCMonitor10initializeEvEUb_E3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_
- __ZZN9CCMonitor9getLoggerEvE10sOnceToken
- __ZZN9CCMonitor9getLoggerEvE7sLogger
- ___51-[CoreTelephonyClient(Provisioning) invalidateKey:]_block_invoke
- ___51-[CoreTelephonyClient(Provisioning) invalidateKey:]_block_invoke_2
- ___55-[CoreTelephonyClient(Stewie) testStewieCommand:error:]_block_invoke
- ___55-[CoreTelephonyClient(Stewie) testStewieCommand:error:]_block_invoke_2
- ___59-[CoreTelephonyClient(SMS) injectMTsms:smsData:completion:]_block_invoke
- ___60-[CoreTelephonyClient(Stewie) testStewieCommand:completion:]_block_invoke
- ___82-[CTXPCFakeCrossPlatformEventRequest performRequestWithHandler:completionHandler:]_block_invoke
- ___96-[CoreTelephonyClient(CrossPlatformTransfer) fakeCrossPlatformTransferEvent:payload:completion:]_block_invoke
- ___96-[CoreTelephonyClient(CrossPlatformTransfer) fakeCrossPlatformTransferEvent:payload:completion:]_block_invoke_2
- ____ZN9CCMonitor10initializeEv_block_invoke
- ____ZN9CCMonitor9getLoggerEv_block_invoke
- ___block_descriptor_48_e8_32r40r_e34_v24?0"NSError"8"NSDictionary"16lr32l8r40l8
- _kCTStewieDiagDataKey
- _notify_get_state
- _notify_register_dispatch
CStrings:
+ "13508"
+ "13508~21"
+ "LazuliDiagnosticCommandRequest"
+ "command"
+ "messagesAppNotInstalled"
- ", epki=%@, shared=%@"
- "13504.1"
- "13504.1~57"
- "Available features: [%s]"
- "Blocking %s (request: '%s', state: %s, required: %s, %p)"
- "Body:"
- "CTStewieRequestReasonAnywhere"
- "CTStewieRequestReasonAnywhereTest"
- "CTStewieRequestReasonTest"
- "CommCenter is always-on. CCMonitor is NOT used"
- "Communication blocked but cached value found. Request: '%s'. Reply: '%s'"
- "CoreTelephony logging is %s by default"
- "Daemon becomes ready..."
- "DataLen = %u"
- "Failed to create notify token for '%s'. Logging is %s by default"
- "Failed to re-register notifications in _HandleConnectionReEstablished(). Error: {domain=%d, error=%d}"
- "Failed to re-register notifications in _HandlePrepWorkBeforeSend(). Error: {domain=%d, error=%d}"
- "HeadersLen = %u"
- "Logging is %s"
- "OS log created"
- "Part %u"
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
- "epki"
- "event"
- "feth"
- "kBaseband"
- "kDaemonRunning"
- "kDefaultAllowed"
- "kNotRunning"
- "kRunning"
- "kTestBlocked"
- "kThumper"
- "kUnknown"
- "nEntries = %u"
- "pdp_ip"
- "shared"
- "v12@?0i8"
- "v24@?0@\"NSError\"8@\"NSDictionary\"16"
```
