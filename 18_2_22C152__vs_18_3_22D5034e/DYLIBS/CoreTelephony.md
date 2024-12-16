## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-12214.4.0.0.0
-  __TEXT.__text: 0x1781e4
-  __TEXT.__auth_stubs: 0x1860
-  __TEXT.__objc_methlist: 0x16e58
+12225.1.0.0.0
+  __TEXT.__text: 0x17b48c
+  __TEXT.__auth_stubs: 0x1880
+  __TEXT.__objc_methlist: 0x170b0
   __TEXT.__const: 0x1047
-  __TEXT.__gcc_except_tab: 0x1bce0
-  __TEXT.__cstring: 0x1cd96
-  __TEXT.__oslogstring: 0x3e84
-  __TEXT.__unwind_info: 0xc028
-  __TEXT.__objc_classname: 0x51bc
-  __TEXT.__objc_methname: 0x20619
-  __TEXT.__objc_methtype: 0x7275
-  __TEXT.__objc_stubs: 0x15720
-  __DATA_CONST.__got: 0xa70
-  __DATA_CONST.__const: 0x7268
-  __DATA_CONST.__objc_classlist: 0x1380
+  __TEXT.__gcc_except_tab: 0x1c064
+  __TEXT.__cstring: 0x1cf39
+  __TEXT.__oslogstring: 0x42b6
+  __TEXT.__unwind_info: 0xc1a0
+  __TEXT.__objc_classname: 0x5220
+  __TEXT.__objc_methname: 0x2068c
+  __TEXT.__objc_methtype: 0x72e4
+  __TEXT.__objc_stubs: 0x15840
+  __DATA_CONST.__got: 0xa90
+  __DATA_CONST.__const: 0x7318
+  __DATA_CONST.__objc_classlist: 0x13a0
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ba0
+  __DATA_CONST.__objc_selrefs: 0x6bc8
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x1550
+  __DATA_CONST.__objc_superrefs: 0x1570
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xc48
+  __AUTH_CONST.__auth_got: 0xc58
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x1df0
-  __AUTH_CONST.__cfstring: 0x1a580
-  __AUTH_CONST.__objc_const: 0x2f330
+  __AUTH_CONST.__const: 0x1e10
+  __AUTH_CONST.__cfstring: 0x1a640
+  __AUTH_CONST.__objc_const: 0x2f890
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x9a60
-  __DATA.__objc_ivar: 0x133c
+  __AUTH.__objc_data: 0x9ba0
+  __DATA.__objc_ivar: 0x134c
   __DATA.__data: 0x1d38
   __DATA.__bss: 0x218
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x28a0
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x1368
+  __DATA_DIRTY.__bss: 0x1378
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10371
-  Symbols:   13208
-  CStrings:  12440
+  Functions: 10434
+  Symbols:   13289
+  CStrings:  12497
 
Symbols:
+ _OBJC_CLASS_$_CTStewieAnywhereMessage
+ _OBJC_CLASS_$_CTStewieDiagMessage
+ _OBJC_CLASS_$_CTStewieIMessageLiteRawMessage
+ _OBJC_CLASS_$_CTStewieSatSmsRawMessage
+ _OBJC_METACLASS_$_CTStewieAnywhereMessage
+ _OBJC_METACLASS_$_CTStewieDiagMessage
+ _OBJC_METACLASS_$_CTStewieIMessageLiteRawMessage
+ _OBJC_METACLASS_$_CTStewieSatSmsRawMessage
+ _kCTCellMonitorNRFrequencyType
+ _kCTCellMonitorNRRedCapInfo
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
+ "12225.1"
+ "12225.1~14"
+ "Available features: [%s]"
+ "Blocking %s (request: '%s', state: %s, required: %s, %p)"
+ "CTStewieAnywhereMessage"
+ "CTStewieDiagMessage"
+ "CTStewieIMessageLiteRawMessage"
+ "CTStewieRequestReasonAnywhere"
+ "CTStewieRequestReasonAnywhereTest"
+ "CTStewieRequestReasonTest"
+ "CTStewieSatSmsRawMessage"
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
+ "injectMTsms:smsData:completion:"
+ "invalidateKey:"
+ "invalidateKey:with:"
+ "isEqualToAnywhereMessage:"
+ "isEqualToDiagMessage:"
+ "kBaseband"
+ "kCTCellMonitorNRFrequencyType"
+ "kCTCellMonitorNRRedCapInfo"
+ "kDaemonRunning"
+ "kDefaultAllowed"
+ "kNotRunning"
+ "kRunning"
+ "kTestBlocked"
+ "kThumper"
+ "kUnknown"
+ "v12@?0i8"
+ "v24@?0@\"NSError\"8@\"NSDictionary\"16"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSMSDataType\"24@?<v@?^@>32"
- "12214.4"
- "12214.4~1"

```
