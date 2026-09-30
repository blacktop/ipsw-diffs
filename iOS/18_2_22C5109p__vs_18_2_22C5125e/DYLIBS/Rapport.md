## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`

```diff

-630.21.1.0.0
-  __TEXT.__text: 0x792c0
-  __TEXT.__auth_stubs: 0x1160
-  __TEXT.__objc_methlist: 0x7a68
+630.41.1.0.0
+  __TEXT.__text: 0x7bd04
+  __TEXT.__auth_stubs: 0x1220
+  __TEXT.__objc_methlist: 0x7ca0
   __TEXT.__const: 0x203c
-  __TEXT.__cstring: 0x13443
-  __TEXT.__gcc_except_tab: 0x12e0
+  __TEXT.__cstring: 0x135c8
+  __TEXT.__gcc_except_tab: 0x16c4
   __TEXT.__oslogstring: 0x588
-  __TEXT.__unwind_info: 0x19e0
-  __TEXT.__objc_classname: 0x9ae
-  __TEXT.__objc_methname: 0xfda1
-  __TEXT.__objc_methtype: 0x286a
-  __TEXT.__objc_stubs: 0x8600
+  __TEXT.__unwind_info: 0x1b78
+  __TEXT.__objc_classname: 0xa25
+  __TEXT.__objc_methname: 0x101b1
+  __TEXT.__objc_methtype: 0x29a9
+  __TEXT.__objc_stubs: 0x8960
   __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0x2318
-  __DATA_CONST.__objc_classlist: 0x230
+  __DATA_CONST.__const: 0x2490
+  __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3588
+  __DATA_CONST.__objc_selrefs: 0x3688
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x1b8
+  __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x8c0
+  __AUTH_CONST.__auth_got: 0x920
   __AUTH_CONST.__const: 0x500
-  __AUTH_CONST.__cfstring: 0x49a0
-  __AUTH_CONST.__objc_const: 0x10e88
+  __AUTH_CONST.__cfstring: 0x4ae0
+  __AUTH_CONST.__objc_const: 0x11428
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x10bc
-  __DATA.__data: 0x1990
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x10f4
+  __DATA.__data: 0x1a00
   __DATA.__bss: 0x120
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x14a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3202
-  Symbols:   3711
-  CStrings:  5995
+  Functions: 3276
+  Symbols:   3798
+  CStrings:  6082
 
Symbols:
+ _RPOptionNWActivity
+ __CFXPCCreateXPCObjectFromCFObject
+ _nw_activity_activate
+ _nw_activity_complete_with_reason
+ _nw_activity_complete_with_reason_and_underlying_error_string
+ _nw_activity_create
+ _nw_activity_create_from_token
+ _nw_activity_get_token
+ _nw_activity_is_activated
+ _nw_activity_set_parent_activity
+ _nw_activity_submit_metrics
+ _objc_release_x10
+ _uuid_is_null
CStrings:
+ "\""
+ "+[RPNWActivityMetrics metricsUsingToken:]"
+ "-[RPCompanionLinkClient sendEventID:event:destinationID:options:completion:]_block_invoke_4"
+ "-[RPCompanionLinkClient sendRequestID:request:destinationID:options:responseHandler:]_block_invoke_4"
+ "-[RPConnection _sendEncryptedResponse:options:error:xid:requestID:highPriority:isChatty:replyStartTime:]"
+ "-[RPNWActivityMetrics submitMetrics]"
+ "510.71.1"
+ "@\"NSObject<OS_nw_activity>\""
+ "@28@0:8i16@20"
+ "Event"
+ "Failed to create NWActivity from token %!p(MISSING)"
+ "Failed to produce XPC metrics from %!p(MISSING)"
+ "RPNWActivity"
+ "RPNWActivityEventMetrics"
+ "RPNWActivityMessageMetrics"
+ "RPNWActivityMetrics"
+ "RPNWActivityRequestMetrics"
+ "RPNWActivityUtils"
+ "Request"
+ "Response"
+ "T@\"NSObject<OS_nw_activity>\",R,N,V_nwActivity"
+ "T@\"NSString\",&,N,V_destination"
+ "T@\"NSString\",&,N,V_peerDeviceModel"
+ "T@\"NSString\",R,N,V_peerOSVersion"
+ "TB,N,V_canDecode128bit"
+ "TQ,N,V_eventSize"
+ "TQ,N,V_messageSize"
+ "TQ,N,V_replyTime"
+ "TQ,N,V_requestSize"
+ "TQ,N,V_responseSize"
+ "Ti,N,V_messageType"
+ "_canDecode128bit"
+ "_destination"
+ "_eventSize"
+ "_initWithNWActivity:"
+ "_lock"
+ "_messageSize"
+ "_messageType"
+ "_metricsDictionary"
+ "_nwActivity"
+ "_peerDeviceModel"
+ "_peerOSVersion"
+ "_rT"
+ "_replyTime"
+ "_requestSize"
+ "_responseSize"
+ "_sendEncryptedResponse:options:error:xid:requestID:highPriority:isChatty:replyStartTime:"
+ "_startNWActivity:options:result:"
+ "activityFromToken:"
+ "bytesIn"
+ "bytesOut"
+ "canDecode128bit"
+ "companionLinkSendEventID:event:destinationID:options:nwActivityToken:completion:"
+ "companionLinkSendRequestID:request:destinationID:options:nwActivityToken:responseHandler:"
+ "destination"
+ "eventSize"
+ "failActivity:error:"
+ "getUUIDBytes:"
+ "messageSize"
+ "messageType"
+ "metricsUsingToken:"
+ "nwActivity"
+ "nwActivityMetrics"
+ "peerDeviceModel"
+ "peerModel"
+ "peerOSVersion"
+ "rapportd"
+ "replyTime"
+ "requestSize"
+ "responseSize"
+ "setCanDecode128bit:"
+ "setDestination:"
+ "setEventSize:"
+ "setMessageSize:"
+ "setMessageType:"
+ "setPeerDeviceModel:"
+ "setPeerOSVersion:"
+ "setReplyTime:"
+ "setRequestSize:"
+ "setResponseSize:"
+ "startMessageMetrics:withParent:"
+ "submitMetrics"
+ "tokenForActivity:"
+ "updateOptions:withNWActivityMetrics:"
+ "v24@?0@\"NSObject<OS_nw_activity>\"8@\"NSDictionary\"16"
+ "v36@0:8I16@20@?28"
+ "v64@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSDictionary\"40@\"NSUUID\"48@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSDictionary\"40@\"NSUUID\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@16@24@32@40@48@?56"
+ "v72@0:8@16@24@32@40@48B56B60@64"
- "-[RPCompanionLinkClient sendEventID:event:destinationID:options:completion:]_block_invoke_2"
- "-[RPCompanionLinkClient sendRequestID:request:destinationID:options:responseHandler:]_block_invoke"
- "-[RPConnection _sendEncryptedResponse:error:xid:requestID:highPriority:isChatty:]"
- "630.21.1"
- "_sendEncryptedResponse:error:xid:requestID:highPriority:isChatty:"
- "companionLinkSendEventID:event:destinationID:options:completion:"
- "companionLinkSendRequestID:request:destinationID:options:responseHandler:"
- "v56@0:8@16@24@32@40B48B52"

```
