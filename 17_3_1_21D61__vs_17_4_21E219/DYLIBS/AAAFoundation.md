## AAAFoundation

> `/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation`

```diff

-54.1.3.0.0
-  __TEXT.__text: 0xde94
+54.6.0.0.0
+  __TEXT.__text: 0xe040
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x11e0
-  __TEXT.__const: 0x80
-  __TEXT.__oslogstring: 0xa47
-  __TEXT.__cstring: 0xc95
-  __TEXT.__gcc_except_tab: 0x168
+  __TEXT.__objc_methlist: 0x1260
+  __TEXT.__const: 0x90
+  __TEXT.__oslogstring: 0x9bd
+  __TEXT.__cstring: 0xca7
+  __TEXT.__gcc_except_tab: 0x15c
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x4b4
-  __TEXT.__objc_classname: 0x276
-  __TEXT.__objc_methname: 0x2fa8
-  __TEXT.__objc_methtype: 0x796
-  __TEXT.__objc_stubs: 0x23c0
+  __TEXT.__unwind_info: 0x4bc
+  __TEXT.__objc_classname: 0x292
+  __TEXT.__objc_methname: 0x3184
+  __TEXT.__objc_methtype: 0x7b8
+  __TEXT.__objc_stubs: 0x2420
   __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x858
+  __DATA_CONST.__const: 0x898
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x24a0
-  __DATA_CONST.__objc_selrefs: 0xd78
+  __DATA_CONST.__objc_const: 0x2678
+  __DATA_CONST.__objc_selrefs: 0xdd8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x148
+  __DATA_CONST.__objc_superrefs: 0x68
   __AUTH_CONST.__objc_const: 0xd0
   __AUTH_CONST.__cfstring: 0xb00
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x470
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x8
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x148
-  __DATA.__objc_superrefs: 0x68
-  __DATA.__objc_ivar: 0x134
-  __DATA.__data: 0x2a8
-  __DATA.__bss: 0xc8
+  __DATA.__objc_ivar: 0x144
+  __DATA.__data: 0x350
+  __DATA.__bss: 0x60
   __DATA_DIRTY.__const: 0x140
   __DATA_DIRTY.__objc_const: 0xa68
   __DATA_DIRTY.__objc_data: 0x730
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1D196E0A-52D5-36FC-8C31-79872926799E
-  Functions: 496
-  Symbols:   1969
-  CStrings:  1015
+  UUID: 85D2485B-2672-3CB0-88CE-078135C64E0E
+  Functions: 510
+  Symbols:   2013
+  CStrings:  1043
 
Symbols:
+ -[AAFAnalyticsTransportInProcessRTC _sendMessageWithCategory:payload:error:]
+ -[AAFAnalyticsTransportInProcessRTC configureReportingSessionWithCompletion:]
+ -[AAFAnalyticsTransportInProcessRTC dealloc]
+ -[AAFAnalyticsTransportInProcessRTC dealloc].cold.1
+ -[AAFAnalyticsTransportInProcessRTC eventQueue]
+ -[AAFAnalyticsTransportInProcessRTC rtcReportingSession]
+ -[AAFAnalyticsTransportInProcessRTC sendEvent:].cold.3
+ -[AAFAnalyticsTransportInProcessRTC sessionGracePeriod]
+ -[AAFAnalyticsTransportInProcessRTC sessionState]
+ -[AAFAnalyticsTransportInProcessRTC setEventQueue:]
+ -[AAFAnalyticsTransportInProcessRTC setRtcReportingSession:]
+ -[AAFAnalyticsTransportInProcessRTC setSessionGracePeriod:]
+ -[AAFAnalyticsTransportInProcessRTC setSessionInfo:]
+ -[AAFAnalyticsTransportInProcessRTC setSessionState:]
+ _OBJC_IVAR_$_AAFAnalyticsTransportInProcessRTC._eventQueue
+ _OBJC_IVAR_$_AAFAnalyticsTransportInProcessRTC._rtcReportingSession
+ _OBJC_IVAR_$_AAFAnalyticsTransportInProcessRTC._sessionGracePeriod
+ _OBJC_IVAR_$_AAFAnalyticsTransportInProcessRTC._sessionState
+ __OBJC_$_PROP_LIST_AAFAnalyticstRTCTransport
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AAFAnalyticstRTCTransport
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AAFAnalyticstRTCTransport
+ __OBJC_$_PROTOCOL_REFS_AAFAnalyticstRTCTransport
+ __OBJC_LABEL_PROTOCOL_$_AAFAnalyticstRTCTransport
+ __OBJC_PROTOCOL_$_AAFAnalyticstRTCTransport
+ ___77-[AAFAnalyticsTransportInProcessRTC configureReportingSessionWithCompletion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8ls32l8
+ _kAAFDeviceSessionIdString
+ _kAAFFlowIdString
+ _kAAFTestSignatureString
+ _objc_msgSend$_sendMessageWithCategory:payload:error:
+ _objc_msgSend$initWithSessionInfo:userInfo:frameworksToCheck:
+ _objc_msgSend$rtcReportingSession
+ _objc_msgSend$sendMessageWithCategory:type:payload:error:
+ _objc_msgSend$startConfigurationWithCompletionHandler:
- -[AAFAnalyticsEvent setObject:forKeyedSubscript:].cold.2
- -[AAFAnalyticsTransportInProcessRTC _sendOneMessageWithSessionInfo:userInfo:category:payload:error:]
- _objc_msgSend$_sendOneMessageWithSessionInfo:userInfo:category:payload:error:
- _objc_msgSend$sendOneMessageWithSessionInfo:userInfo:category:type:payload:error:
CStrings:
+ "%@ deallocated"
+ "'"
+ "<%@: %p> RTCReporting send failed with error: %{public}@"
+ "<%@: %p> RTCReporting send success!"
+ "@\"NSMutableArray\"16@0:8"
+ "@\"RTCReporting\""
+ "AAFAnalyticstRTCTransport"
+ "T@\"NSDictionary\",C,N,V_sessionInfo"
+ "T@\"NSMutableArray\",&,N,V_eventQueue"
+ "T@\"NSMutableArray\",R,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"RTCReporting\",&,N,V_rtcReportingSession"
+ "TQ,N"
+ "TQ,N,V_sessionGracePeriod"
+ "TQ,N,V_sessionState"
+ "_eventQueue"
+ "_rtcReportingSession"
+ "_sendMessageWithCategory:payload:error:"
+ "_sessionGracePeriod"
+ "_sessionState"
+ "configureReportingSessionWithCompletion:"
+ "eventQueue"
+ "initWithSessionInfo:userInfo:frameworksToCheck:"
+ "rtcReportingSession"
+ "sendMessageWithCategory:type:payload:error:"
+ "sessionGracePeriod"
+ "sessionState"
+ "setEventQueue:"
+ "setRtcReportingSession:"
+ "setSessionGracePeriod:"
+ "setSessionInfo:"
+ "setSessionState:"
+ "startConfigurationWithCompletionHandler:"
+ "v16@?0@\"NSArray\"8"
+ "v24@0:8@?<v@?B>16"
- "\"AAFAnalyticsEvent gets a nil object. Please check if the payload is constructed properly.\""
- "<%@: %p> RTCReporting sendOneMessageWithSessionInfo failed with error: %@"
- "<%@: %p> RTCReporting sendOneMessageWithSessionInfo with error: %@, success: %d"
- "B56@0:8@16@24@32@40^@48"
- "T@\"NSDictionary\",R,C,N,V_sessionInfo"
- "_sendOneMessageWithSessionInfo:userInfo:category:payload:error:"
- "sendOneMessageWithSessionInfo:userInfo:category:type:payload:error:"

```
