## rapportd

> `/usr/libexec/rapportd`

```diff

-630.21.1.0.0
-  __TEXT.__text: 0xb83f8
-  __TEXT.__auth_stubs: 0x1880
-  __TEXT.__objc_stubs: 0xef40
-  __TEXT.__objc_methlist: 0x6594
-  __TEXT.__cstring: 0x28b82
-  __TEXT.__objc_classname: 0x94e
-  __TEXT.__objc_methtype: 0x3831
-  __TEXT.__objc_methname: 0x1521a
+630.41.1.0.0
+  __TEXT.__text: 0xba55c
+  __TEXT.__auth_stubs: 0x1910
+  __TEXT.__objc_stubs: 0xf1e0
+  __TEXT.__objc_methlist: 0x67c4
+  __TEXT.__cstring: 0x28ea2
+  __TEXT.__objc_classname: 0x9c5
+  __TEXT.__objc_methtype: 0x395b
+  __TEXT.__objc_methname: 0x15603
   __TEXT.__const: 0x207a
-  __TEXT.__gcc_except_tab: 0x1cd4
+  __TEXT.__gcc_except_tab: 0x1d80
   __TEXT.__oslogstring: 0x496
   __TEXT.__constg_swiftt: 0xf0
   __TEXT.__swift5_typeref: 0x41

   __TEXT.__swift5_reflstr: 0x24
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x1f20
-  __DATA_CONST.__auth_got: 0xc50
+  __TEXT.__unwind_info: 0x2038
+  __DATA_CONST.__auth_got: 0xc98
   __DATA_CONST.__got: 0x438
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x3f50
-  __DATA_CONST.__cfstring: 0x5660
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __DATA_CONST.__const: 0x4020
+  __DATA_CONST.__cfstring: 0x58c0
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_intobj: 0x330
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xda80
-  __DATA.__objc_selrefs: 0x4580
-  __DATA.__objc_ivar: 0xd30
-  __DATA.__objc_data: 0x1370
-  __DATA.__data: 0x1ff0
+  __DATA.__objc_const: 0xe020
+  __DATA.__objc_selrefs: 0x4680
+  __DATA.__objc_ivar: 0xd68
+  __DATA.__objc_data: 0x1500
+  __DATA.__data: 0x2060
   __DATA.__bss: 0x540
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3037
-  Symbols:   560
-  CStrings:  8236
+  Functions: 3103
+  Symbols:   569
+  CStrings:  8336
 
Symbols:
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
- _nw_parameters_get_required_interface_subtype
CStrings:
+ "\""
+ "+[RPNWActivityMetrics metricsUsingToken:]"
+ "-[RPNWActivityMetrics submitMetrics]"
+ "-[RPNWNetworkAgent convertConnectionParametersToControlFlags:]"
+ "-[RPNWPeer connectToPeer:inboundConnection:controlFlags:applicationService:listenerID:automapListener:connectionID:connectHandler:lostHandler:]"
+ "-[RPNWPeer connectToPeer:inboundConnection:controlFlags:applicationService:listenerID:automapListener:connectionID:connectHandler:lostHandler:]_block_invoke"
+ "-[RPNWPeer connectToPeer:inboundConnection:controlFlags:applicationService:listenerID:automapListener:connectionID:connectHandler:lostHandler:]_block_invoke_2"
+ "510.71.1"
+ "@\"NSObject<OS_nw_activity>\""
+ "@28@0:8i16@20"
+ "Called convertConnectionParametersToControlFlags with parameters=%!@(MISSING)"
+ "Event"
+ "Failed to create NWActivity from token %!p(MISSING)"
+ "Failed to produce XPC metrics from %!p(MISSING)"
+ "Found registered listener %!@(MISSING) for appSvc=%!@(MISSING)\n"
+ "Initializing RPNWListener[%!@(MISSING)]\n"
+ "K\x16"
+ "Pref (profile): '%!@(MISSING)' = '%!@(MISSING)'\n"
+ "Pref (profile): '%!@(MISSING)' = '%!~(MISSING)@'\n"
+ "RPNWActivity"
+ "RPNWActivityEventMetrics"
+ "RPNWActivityMessageMetrics"
+ "RPNWActivityMetrics"
+ "RPNWActivityRequestMetrics"
+ "RPNWActivityUtils"
+ "RPNWListener[%!@(MISSING)][%!@(MISSING)]=%!@(MISSING) : "
+ "Request"
+ "Response"
+ "Returning control flags: CF %!l(MISSING)l{flags}\n"
+ "T@\"NSObject<OS_nw_activity>\",R,N,V_nwActivity"
+ "T@\"NSString\",&,N,V_destination"
+ "T@\"NSString\",&,N,V_peerDeviceModel"
+ "T@\"NSString\",R,N,V_peerOSVersion"
+ "TQ,N,V_controlFlags"
+ "TQ,N,V_eventSize"
+ "TQ,N,V_messageSize"
+ "TQ,N,V_replyTime"
+ "TQ,N,V_requestSize"
+ "TQ,N,V_responseSize"
+ "Ti,N,V_messageType"
+ "WiFi"
+ "_controlFlags"
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
+ "_replyTime"
+ "_requestSize"
+ "_responseSize"
+ "activityFromToken:"
+ "bytesIn"
+ "bytesOut"
+ "canDecode128bit"
+ "cloudDiscovery"
+ "companionLinkSendEventID:event:destinationID:options:nwActivityToken:completion:"
+ "companionLinkSendRequestID:request:destinationID:options:nwActivityToken:responseHandler:"
+ "connectToPeer:inboundConnection:controlFlags:applicationService:listenerID:automapListener:connectionID:connectHandler:lostHandler:"
+ "destination"
+ "domain"
+ "eventSize"
+ "failActivity:error:"
+ "ftCompress"
+ "ftLargeFileBufferBytes"
+ "ftLargeFileMaxOutstanding"
+ "ftLargeFileMaxTasks"
+ "ftSmallFilesMaxBytes"
+ "ftSmallFilesMaxTasks"
+ "initWithSet:"
+ "liveAudioEnabled"
+ "messageSize"
+ "messageType"
+ "metricsUsingToken:"
+ "numberWithUnsignedLong:"
+ "nwActivity"
+ "nwActivityMetrics"
+ "peerDeviceModel"
+ "peerModel"
+ "peerOSVersion"
+ "rapportd"
+ "rdHomeKit"
+ "replyTime"
+ "requestSize"
+ "responseSize"
+ "sendActivityLevelOverInfra"
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
+ "textInputEnabled"
+ "tokenForActivity:"
+ "updateOptions:withNWActivityMetrics:"
+ "v64@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSDictionary\"40@\"NSUUID\"48@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSDictionary\"40@\"NSUUID\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@16@24@32@40@48@?56"
+ "v80@0:8@16B24Q28@36@44B52@56@?64@?72"
- "-[RPNWPeer connectToPeer:inboundConnection:applicationService:listenerID:automapListener:connectionID:connectHandler:lostHandler:]"
- "-[RPNWPeer connectToPeer:inboundConnection:applicationService:listenerID:automapListener:connectionID:connectHandler:lostHandler:]_block_invoke"
- "-[RPNWPeer connectToPeer:inboundConnection:applicationService:listenerID:automapListener:connectionID:connectHandler:lostHandler:]_block_invoke_2"
- "630.21.1"
- "Found registered listener for appSvc=%!@(MISSING)\n"
- "Initializing RPNWListener\n"
- "O\x02"
- "RPNWListener[%!@(MISSING)]=%!@(MISSING) : "
- "companionLinkSendEventID:event:destinationID:options:completion:"
- "companionLinkSendRequestID:request:destinationID:options:responseHandler:"
- "connectToPeer:inboundConnection:applicationService:listenerID:automapListener:connectionID:connectHandler:lostHandler:"
- "v72@0:8@16B24@28@36B44@48@?56@?64"

```
