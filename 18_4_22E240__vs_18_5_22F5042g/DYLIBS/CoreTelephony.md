## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-12322.6.0.0.0
-  __TEXT.__text: 0x179140
-  __TEXT.__auth_stubs: 0x1860
-  __TEXT.__objc_methlist: 0x18964
+12403.2.2.0.0
+  __TEXT.__text: 0x17c998
+  __TEXT.__auth_stubs: 0x1890
+  __TEXT.__objc_methlist: 0x18c3c
   __TEXT.__const: 0x1057
-  __TEXT.__gcc_except_tab: 0x1be0c
-  __TEXT.__cstring: 0x1cfa7
-  __TEXT.__oslogstring: 0x3d71
-  __TEXT.__unwind_info: 0xc168
-  __TEXT.__objc_classname: 0x5315
-  __TEXT.__objc_methname: 0x2082a
-  __TEXT.__objc_methtype: 0x72c3
-  __TEXT.__objc_stubs: 0x15820
-  __DATA_CONST.__got: 0xa78
-  __DATA_CONST.__const: 0x7300
-  __DATA_CONST.__objc_classlist: 0x13c0
+  __TEXT.__gcc_except_tab: 0x1c220
+  __TEXT.__cstring: 0x1d126
+  __TEXT.__oslogstring: 0x41a3
+  __TEXT.__unwind_info: 0xc330
+  __TEXT.__objc_classname: 0x539c
+  __TEXT.__objc_methname: 0x208f1
+  __TEXT.__objc_methtype: 0x7332
+  __TEXT.__objc_stubs: 0x159a0
+  __DATA_CONST.__got: 0xa98
+  __DATA_CONST.__const: 0x73a0
+  __DATA_CONST.__objc_classlist: 0x13e8
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7168
+  __DATA_CONST.__objc_selrefs: 0x71a8
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x15c0
+  __DATA_CONST.__objc_superrefs: 0x15f0
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xc48
+  __AUTH_CONST.__auth_got: 0xc60
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x1dd0
-  __AUTH_CONST.__cfstring: 0x1a6c0
-  __AUTH_CONST.__objc_const: 0x2cb28
+  __AUTH_CONST.__const: 0x1df0
+  __AUTH_CONST.__cfstring: 0x1a760
+  __AUTH_CONST.__objc_const: 0x2d0e8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x9b50
-  __DATA.__objc_ivar: 0x1344
+  __AUTH.__objc_data: 0x9ce0
+  __DATA.__objc_ivar: 0x1354
   __DATA.__data: 0x1df8
   __DATA.__bss: 0x1a0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2a30
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x13c8
+  __DATA_DIRTY.__bss: 0x13d8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10426
-  Symbols:   13295
-  CStrings:  12479
+  Functions: 10499
+  Symbols:   13401
+  CStrings:  12541
 
Symbols:
+ _OBJC_CLASS_$_CTStewieAnywhereMessage
+ _OBJC_CLASS_$_CTStewieDiagMessage
+ _OBJC_CLASS_$_CTStewieIMessageLiteRawMessage
+ _OBJC_CLASS_$_CTStewieSatSmsRawMessage
+ _OBJC_METACLASS_$_CTStewieAnywhereMessage
+ _OBJC_METACLASS_$_CTStewieDiagMessage
+ _OBJC_METACLASS_$_CTStewieIMessageLiteRawMessage
+ _OBJC_METACLASS_$_CTStewieSatSmsRawMessage
+ _TelephonyUtilIsOversteerEnabled
+ _kCTStewieDiagDataKey
+ _notify_get_state
+ _notify_register_dispatch
CStrings:
+ "#D "
+ "#D %s"
+ "#D Body:"
+ "#D DataLen = %u"
+ "#D HeadersLen = %u"
+ "#D Part %u"
+ "#D nEntries = %u"
+ ", epki=%@, shared=%@"
+ "12403.2.2"
+ "12403.2.2~1"
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
+ "XPC message"
+ "XPC message with reply"
+ "_CTServerConnectionGetCommCenterInitializationState request is not allowed at this time"
+ "_CTServerConnectionRegisterForEvent request is not allowed at this time. Registration is delayed"
+ "_CTServerConnectionUnregisterForAllNotifications request is not allowed at this time"
+ "_CTServerConnectionUnregisterForEvent request is not allowed at this time"
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
+ "kTestBlocked"
+ "kThumper"
+ "kUnknown"
+ "pdp_ip"
+ "v12@?0i8"
+ "v24@?0@\"NSError\"8@\"NSDictionary\"16"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSMSDataType\"24@?<v@?^@>32"
- "12322.6"
- "12322.6~1"

```
