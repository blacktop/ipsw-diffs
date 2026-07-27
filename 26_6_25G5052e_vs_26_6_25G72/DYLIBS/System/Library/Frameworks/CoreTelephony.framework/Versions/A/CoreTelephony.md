## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/Versions/A/CoreTelephony`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-13192.0.0.0.0
-  __TEXT.__text: 0x15d3f8
-  __TEXT.__auth_stubs: 0x1860
-  __TEXT.__objc_methlist: 0x13c04
-  __TEXT.__cstring: 0x192b8
+13193.0.0.0.0
+  __TEXT.__text: 0x15b550
+  __TEXT.__auth_stubs: 0x1840
+  __TEXT.__objc_methlist: 0x13bdc
+  __TEXT.__cstring: 0x19158
   __TEXT.__const: 0x1270
-  __TEXT.__gcc_except_tab: 0x1638c
-  __TEXT.__oslogstring: 0x4106
+  __TEXT.__gcc_except_tab: 0x162cc
+  __TEXT.__oslogstring: 0x3c66
   __TEXT.__swift5_typeref: 0x18d
   __TEXT.__swift5_reflstr: 0xc1
   __TEXT.__swift5_assocty: 0x48

   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0xa4a8
+  __TEXT.__unwind_info: 0xa488
   __TEXT.__eh_frame: 0x2b8
   __TEXT.__objc_classname: 0x3ff6
-  __TEXT.__objc_methname: 0x1b1f5
-  __TEXT.__objc_methtype: 0x6792
-  __TEXT.__objc_stubs: 0x112c0
+  __TEXT.__objc_methname: 0x1b1c1
+  __TEXT.__objc_methtype: 0x6722
+  __TEXT.__objc_stubs: 0x11200
   __DATA_CONST.__got: 0x898
-  __DATA_CONST.__const: 0x4958
+  __DATA_CONST.__const: 0x48e8
   __DATA_CONST.__objc_classlist: 0xeb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5df8
+  __DATA_CONST.__objc_selrefs: 0x5de8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xef8
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xc48
-  __AUTH_CONST.__const: 0x3590
-  __AUTH_CONST.__cfstring: 0x17bc0
-  __AUTH_CONST.__objc_const: 0x21ff8
+  __AUTH_CONST.__auth_got: 0xc38
+  __AUTH_CONST.__const: 0x3540
+  __AUTH_CONST.__cfstring: 0x17b60
+  __AUTH_CONST.__objc_const: 0x21fe8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x7080

   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2260
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x12c8
+  __DATA_DIRTY.__bss: 0x12a8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Network.framework/Versions/A/Network

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8623
-  Symbols:   18606
-  CStrings:  10211
+  Functions: 8602
+  Symbols:   18567
+  CStrings:  10165
 
Symbols:
- -[CoreTelephonyClient(SMS) injectMTsms:smsData:completion:]
- _CTServerConnectionGetCommCenterInitializationState
- _CTServerConnectionRegisterForEvent
- _CTServerConnectionUnregisterForAllNotifications
- _CTServerConnectionUnregisterForEvent
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _Z25SendXpcMessageWithCachingP20__CTServerConnectionRKN3xpc4dictERS2_20CTFeatureRequirement
- _ZL17logBlockedRequestPKcRKN3xpc4dictEP20__CTServerConnection20CTFeatureRequirement
- _ZN12_GLOBAL__N_128ReregisterClientForAllEventsEP20__CTServerConnection
- _ZN13MMSPduDecoder19decodeEncodedHeaderEPK20MMSHeaderEncodingMap
- _ZN9CCMonitor10initializeEv
- _ZN9CCMonitor17handleDaemonReadyEv
- _ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_
- _ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_
- _ZZN8dispatch5asyncIZZN9CCMonitor10initializeEvEUb_E3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_
- __ZL17logBlockedRequestPKcRKN3xpc4dictEP20__CTServerConnection20CTFeatureRequirement
- __ZZN8dispatch5asyncIZN9CCMonitor10initializeEvE3$_1EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_
- __ZZN8dispatch5asyncIZZN9CCMonitor10initializeEvEUb_E3$_0EEvP16dispatch_queue_sNSt3__110unique_ptrIT_NS5_14default_deleteIS7_EEEEENUlPvE_8__invokeESB_
- __ZZN9CCMonitor9getLoggerEvE10sOnceToken
- __ZZN9CCMonitor9getLoggerEvE7sLogger
- ___55-[CoreTelephonyClient(Stewie) testStewieCommand:error:]_block_invoke
- ___55-[CoreTelephonyClient(Stewie) testStewieCommand:error:]_block_invoke_2
- ___59-[CoreTelephonyClient(SMS) injectMTsms:smsData:completion:]_block_invoke
- ___60-[CoreTelephonyClient(Stewie) testStewieCommand:completion:]_block_invoke
- ___ZL25_HandlePrepWorkBeforeSendP20__CTServerConnectionRN3xpc4dictEb_block_invoke
- ___ZL30_CTServerConnectionReEstablishP20__CTServerConnection_block_invoke
- ___ZN9CCMonitor9getLoggerEv_block_invoke
- ____ZN9CCMonitor10initializeEv_block_invoke
- ____ZN9CCMonitor9getLoggerEv_block_invoke
- ___block_descriptor_48_e8_32r40r_e34_v24?0"NSError"8"NSDictionary"16l
- _notify_get_state
- _notify_register_dispatch
- _objc_msgSend$epki
- _objc_msgSend$injectMTsms:smsData:completion:
- _objc_msgSend$setEpki:
- _objc_msgSend$setShared:
- _objc_msgSend$shared
- _objc_msgSend$testStewieCommand:completion:
CStrings:
+ "13193"
+ "13193~52"
- "#D "
- "#D %s"
- "#D Body:"
- "#D DataLen = %u"
- "#D HeadersLen = %u"
- "#D Part %u"
- "#D nEntries = %u"
- ", epki=%@, shared=%@"
- "13192"
- "13192~61"
- "Attempt to connect to CT from %s blocked, use _CTServerConnectionAddIdentifierException to add exception"
- "Available features: [%s]"
- "Blocking %s (request: '%s', state: %s, required: %s, %p)"
- "CTStewieRequestReasonAnywhere"
- "CTStewieRequestReasonAnywhereTest"
- "CTStewieRequestReasonTest"
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
- "injectMTsms:smsData:completion:"
- "invalidateKey:with:"
- "kBaseband"
- "kDaemonRunning"
- "kDefaultAllowed"
- "kNotRunning"
- "kRunning"
- "kTestBlocked"
- "kThumper"
- "kUnknown"
- "v12@?0i8"
- "v24@?0@\"NSError\"8@\"NSDictionary\"16"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
- "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSMSDataType\"24@?<v@?^@>32"
```
