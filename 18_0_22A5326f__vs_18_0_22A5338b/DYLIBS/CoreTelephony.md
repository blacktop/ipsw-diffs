## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-12084.3.0.0.0
-  __TEXT.__text: 0x176c98
-  __TEXT.__auth_stubs: 0x1880
-  __TEXT.__objc_methlist: 0x16b58
+12088.0.0.0.0
+  __TEXT.__text: 0x1739f0
+  __TEXT.__auth_stubs: 0x1860
+  __TEXT.__objc_methlist: 0x16900
   __TEXT.__const: 0x1047
-  __TEXT.__gcc_except_tab: 0x1b758
-  __TEXT.__cstring: 0x1cca9
-  __TEXT.__oslogstring: 0x42b6
-  __TEXT.__unwind_info: 0xbeb0
-  __TEXT.__objc_classname: 0x5113
-  __TEXT.__objc_methname: 0x1fdf4
-  __TEXT.__objc_methtype: 0x7275
-  __TEXT.__objc_stubs: 0x153a0
-  __DATA_CONST.__got: 0xa78
-  __DATA_CONST.__const: 0x72e0
-  __DATA_CONST.__objc_classlist: 0x1360
+  __TEXT.__gcc_except_tab: 0x1b3d4
+  __TEXT.__cstring: 0x1cb3d
+  __TEXT.__oslogstring: 0x3e84
+  __TEXT.__unwind_info: 0xbd40
+  __TEXT.__objc_classname: 0x50af
+  __TEXT.__objc_methname: 0x1fd81
+  __TEXT.__objc_methtype: 0x7206
+  __TEXT.__objc_stubs: 0x15280
+  __DATA_CONST.__got: 0xa58
+  __DATA_CONST.__const: 0x7240
+  __DATA_CONST.__objc_classlist: 0x1340
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a70
+  __DATA_CONST.__objc_selrefs: 0x6a48
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x1508
+  __DATA_CONST.__objc_superrefs: 0x14e8
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xc58
+  __AUTH_CONST.__auth_got: 0xc48
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x1e10
-  __AUTH_CONST.__cfstring: 0x1a300
-  __AUTH_CONST.__objc_const: 0x2eec8
+  __AUTH_CONST.__const: 0x1df0
+  __AUTH_CONST.__cfstring: 0x1a280
+  __AUTH_CONST.__objc_const: 0x2e968
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x97e0
-  __DATA.__objc_ivar: 0x1308
+  __AUTH.__objc_data: 0x96a0
+  __DATA.__objc_ivar: 0x12f8
   __DATA.__data: 0x1d38
   __DATA.__bss: 0x218
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x29e0
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x1370
+  __DATA_DIRTY.__bss: 0x1360
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10312
-  Symbols:   13153
-  CStrings:  12386
+  Functions: 10249
+  Symbols:   13074
+  CStrings:  12331
 
Symbols:
- _OBJC_CLASS_$_CTStewieAnywhereMessage
- _OBJC_CLASS_$_CTStewieDiagMessage
- _OBJC_CLASS_$_CTStewieIMessageLiteRawMessage
- _OBJC_CLASS_$_CTStewieSatSmsRawMessage
- _OBJC_METACLASS_$_CTStewieAnywhereMessage
- _OBJC_METACLASS_$_CTStewieDiagMessage
- _OBJC_METACLASS_$_CTStewieIMessageLiteRawMessage
- _OBJC_METACLASS_$_CTStewieSatSmsRawMessage
- _kCTStewieDiagDataKey
- _notify_get_state
- _notify_register_dispatch
CStrings:
+ "12088"
+ "12088~15"
- "#D "
- "#D %!s(MISSING)"
- "#D Body:"
- "#D DataLen = %!u(MISSING)"
- "#D HeadersLen = %!u(MISSING)"
- "#D Part %!u(MISSING)"
- "#D nEntries = %!u(MISSING)"
- ", epki=%!@(MISSING), shared=%!@(MISSING)"
- "12084.3"
- "12084.3~1"
- "Available features: [%!s(MISSING)]"
- "Blocking %!s(MISSING) (request: '%!s(MISSING)', state: %!s(MISSING), required: %!s(MISSING), %!p(MISSING))"
- "CTStewieAnywhereMessage"
- "CTStewieDiagMessage"
- "CTStewieIMessageLiteRawMessage"
- "CTStewieRequestReasonAnywhere"
- "CTStewieRequestReasonAnywhereTest"
- "CTStewieRequestReasonTest"
- "CTStewieSatSmsRawMessage"
- "CommCenter is always-on. CCMonitor is NOT used"
- "Communication blocked but cached value found. Request: '%!s(MISSING)'. Reply: '%!s(MISSING)'"
- "CoreTelephony logging is %!s(MISSING) by default"
- "Daemon becomes ready..."
- "Failed to create notify token for '%!s(MISSING)'. Logging is %!s(MISSING) by default"
- "Failed to re-register notifications in _HandleConnectionReEstablished(). Error: {domain=%!d(MISSING), error=%!d(MISSING)}"
- "Failed to re-register notifications in _HandlePrepWorkBeforeSend(). Error: {domain=%!d(MISSING), error=%!d(MISSING)}"
- "Logging is %!s(MISSING)"
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
- "v12@?0i8"
- "v24@?0@\"NSError\"8@\"NSDictionary\"16"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
- "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSMSDataType\"24@?<v@?^@>32"

```
