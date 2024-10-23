## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-12109.5.0.0.0
-  __TEXT.__text: 0x177aa0
-  __TEXT.__auth_stubs: 0x1860
-  __TEXT.__objc_methlist: 0x16d88
+12209.3.0.0.0
+  __TEXT.__text: 0x17b058
+  __TEXT.__auth_stubs: 0x1880
+  __TEXT.__objc_methlist: 0x17008
   __TEXT.__const: 0x1047
-  __TEXT.__gcc_except_tab: 0x1bbe4
-  __TEXT.__cstring: 0x1cca9
-  __TEXT.__oslogstring: 0x3e84
-  __TEXT.__unwind_info: 0xbfd8
-  __TEXT.__objc_classname: 0x51a8
-  __TEXT.__objc_methname: 0x20497
-  __TEXT.__objc_methtype: 0x725e
-  __TEXT.__objc_stubs: 0x15600
-  __DATA_CONST.__got: 0xa68
-  __DATA_CONST.__const: 0x7258
-  __DATA_CONST.__objc_classlist: 0x1378
+  __TEXT.__gcc_except_tab: 0x1bfcc
+  __TEXT.__cstring: 0x1ce7d
+  __TEXT.__oslogstring: 0x42b6
+  __TEXT.__unwind_info: 0xc160
+  __TEXT.__objc_classname: 0x520c
+  __TEXT.__objc_methname: 0x20579
+  __TEXT.__objc_methtype: 0x72cd
+  __TEXT.__objc_stubs: 0x15780
+  __DATA_CONST.__got: 0xa88
+  __DATA_CONST.__const: 0x7308
+  __DATA_CONST.__objc_classlist: 0x1398
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b58
+  __DATA_CONST.__objc_selrefs: 0x6b98
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x1548
+  __DATA_CONST.__objc_superrefs: 0x1568
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xc48
+  __AUTH_CONST.__auth_got: 0xc58
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x1df0
-  __AUTH_CONST.__cfstring: 0x1a460
-  __AUTH_CONST.__objc_const: 0x2f178
+  __AUTH_CONST.__const: 0x1e10
+  __AUTH_CONST.__cfstring: 0x1a540
+  __AUTH_CONST.__objc_const: 0x2f728
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x9830
-  __DATA.__objc_ivar: 0x132c
+  __AUTH.__objc_data: 0x9970
+  __DATA.__objc_ivar: 0x1340
   __DATA.__data: 0x1d38
   __DATA.__bss: 0x218
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2a80
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x1360
+  __DATA_DIRTY.__bss: 0x1378
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10355
-  Symbols:   13189
-  CStrings:  12410
+  Functions: 10422
+  Symbols:   13273
+  CStrings:  12475
 
Symbols:
+ _OBJC_CLASS_$_CTStewieAnywhereMessage
+ _OBJC_CLASS_$_CTStewieDiagMessage
+ _OBJC_CLASS_$_CTStewieIMessageLiteRawMessage
+ _OBJC_CLASS_$_CTStewieSatSmsRawMessage
+ _OBJC_METACLASS_$_CTStewieAnywhereMessage
+ _OBJC_METACLASS_$_CTStewieDiagMessage
+ _OBJC_METACLASS_$_CTStewieIMessageLiteRawMessage
+ _OBJC_METACLASS_$_CTStewieSatSmsRawMessage
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERj
+ _kCTRegistrationDataIndicator5G_CA
+ _kCTStewieDiagDataKey
+ _notify_get_state
+ _notify_register_dispatch
- __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEErsERt
CStrings:
+ "!\x1d"
+ "#D "
+ "#D %!s(MISSING)"
+ "#D Body:"
+ "#D DataLen = %!u(MISSING)"
+ "#D HeadersLen = %!u(MISSING)"
+ "#D Part %!u(MISSING)"
+ "#D nEntries = %!u(MISSING)"
+ ", epki=%!@(MISSING), shared=%!@(MISSING)"
+ ", servicePartners=%!@(MISSING)"
+ "12209.3"
+ "12209.3~2"
+ "5GA"
+ "Available features: [%!s(MISSING)]"
+ "Blocking %!s(MISSING) (request: '%!s(MISSING)', state: %!s(MISSING), required: %!s(MISSING), %!p(MISSING))"
+ "CTNRDisableReasonNotProvisioned"
+ "CTStewieAnywhereMessage"
+ "CTStewieDiagMessage"
+ "CTStewieIMessageLiteRawMessage"
+ "CTStewieRequestReasonAnywhere"
+ "CTStewieRequestReasonAnywhereTest"
+ "CTStewieRequestReasonTest"
+ "CTStewieSatSmsRawMessage"
+ "CommCenter is always-on. CCMonitor is NOT used"
+ "Communication blocked but cached value found. Request: '%!s(MISSING)'. Reply: '%!s(MISSING)'"
+ "CoreTelephony logging is %!s(MISSING) by default"
+ "Daemon becomes ready..."
+ "Failed to create notify token for '%!s(MISSING)'. Logging is %!s(MISSING) by default"
+ "Failed to re-register notifications in _HandleConnectionReEstablished(). Error: {domain=%!d(MISSING), error=%!d(MISSING)}"
+ "Failed to re-register notifications in _HandlePrepWorkBeforeSend(). Error: {domain=%!d(MISSING), error=%!d(MISSING)}"
+ "Logging is %!s(MISSING)"
+ "OS log created"
+ "ReregisterClientForAllEvents request is not allowed at this time. Registration is delayed"
+ "T@\"NSDictionary\",&,N,V_servicePartners"
+ "XPC message"
+ "XPC message with reply"
+ "_CTServerConnectionGetCommCenterInitializationState request is not allowed at this time"
+ "_CTServerConnectionRegisterForEvent request is not allowed at this time. Registration is delayed"
+ "_CTServerConnectionUnregisterForAllNotifications request is not allowed at this time"
+ "_CTServerConnectionUnregisterForEvent request is not allowed at this time"
+ "_servicePartners"
+ "activateTurboMode:"
+ "async XPC message"
+ "com.apple.CoreTelephony.LoggingEnabled"
+ "diagData"
+ "injectMTsms:smsData:completion:"
+ "invalidateKey:"
+ "invalidateKey:with:"
+ "isEqualToAnywhereMessage:"
+ "isEqualToDiagMessage:"
+ "kBaseband"
+ "kCTRegistrationDataIndicator5G_CA"
+ "kDaemonRunning"
+ "kDefaultAllowed"
+ "kNotRunning"
+ "kRunning"
+ "kTestBlocked"
+ "kThumper"
+ "kUnknown"
+ "servicePartners"
+ "setServicePartners:"
+ "v12@?0i8"
+ "v24@?0@\"NSError\"8@\"NSDictionary\"16"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSMSDataType\"24@?<v@?^@>32"
- "!\x1c"
- "12109.5"
- "12109.5~1"

```
