## apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

```diff

-1100.200.102.0.0
-  __TEXT.__text: 0xd0e04
-  __TEXT.__auth_stubs: 0x25f0
-  __TEXT.__objc_stubs: 0x101a0
+1100.300.121.0.0
+  __TEXT.__text: 0xc8aec
+  __TEXT.__auth_stubs: 0x2600
+  __TEXT.__objc_stubs: 0xf760
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0xa248
-  __TEXT.__objc_methname: 0x19a03
-  __TEXT.__objc_classname: 0xfcb
-  __TEXT.__objc_methtype: 0x43f0
-  __TEXT.__cstring: 0x9334
-  __TEXT.__const: 0x1c41
-  __TEXT.__oslogstring: 0x11833
-  __TEXT.__gcc_except_tab: 0x24e0
+  __TEXT.__objc_methlist: 0x9908
+  __TEXT.__objc_methname: 0x18b7d
+  __TEXT.__objc_classname: 0xdc2
+  __TEXT.__objc_methtype: 0x432d
+  __TEXT.__cstring: 0x9264
+  __TEXT.__const: 0x1c91
+  __TEXT.__oslogstring: 0x11333
+  __TEXT.__gcc_except_tab: 0x24d8
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__constg_swiftt: 0x3bc
-  __TEXT.__swift5_typeref: 0x2f7
-  __TEXT.__swift5_reflstr: 0x239
-  __TEXT.__swift5_fieldmd: 0x250
-  __TEXT.__swift5_types: 0x30
-  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__constg_swiftt: 0x48c
+  __TEXT.__swift5_typeref: 0x30f
+  __TEXT.__swift5_reflstr: 0x269
+  __TEXT.__swift5_fieldmd: 0x284
+  __TEXT.__swift5_types: 0x3c
+  __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0x3390
+  __TEXT.__unwind_info: 0x31b0
   __TEXT.__eh_frame: 0xb0
-  __DATA_CONST.__auth_got: 0x1310
-  __DATA_CONST.__got: 0x7c8
+  __DATA_CONST.__auth_got: 0x1318
+  __DATA_CONST.__got: 0x758
   __DATA_CONST.__auth_ptr: 0x98
-  __DATA_CONST.__const: 0x5150
-  __DATA_CONST.__cfstring: 0x7fe0
-  __DATA_CONST.__objc_classlist: 0x428
-  __DATA_CONST.__objc_protolist: 0x218
+  __DATA_CONST.__const: 0x50c8
+  __DATA_CONST.__cfstring: 0x7ec0
+  __DATA_CONST.__objc_classlist: 0x3b0
+  __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x398
-  __DATA_CONST.__objc_intobj: 0x2e8
+  __DATA_CONST.__objc_superrefs: 0x318
+  __DATA_CONST.__objc_intobj: 0x300
   __DATA_CONST.__objc_arraydata: 0x68
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x1ec10
-  __DATA.__objc_selrefs: 0x5308
-  __DATA.__objc_ivar: 0xd3c
-  __DATA.__objc_data: 0x3120
-  __DATA.__data: 0x18e8
-  __DATA.__bss: 0x600
+  __DATA.__objc_const: 0x18648
+  __DATA.__objc_selrefs: 0x5090
+  __DATA.__objc_ivar: 0xbc4
+  __DATA.__objc_data: 0x2d38
+  __DATA.__data: 0x1758
+  __DATA.__bss: 0x5c0
   __DATA.__common: 0x148
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal
   - /System/Library/PrivateFrameworks/CommonUtilities.framework/CommonUtilities
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSDB.framework/CoreSDB
   - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics
-  - /usr/lib/libAWDSupportFramework.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4829
-  Symbols:   909
-  CStrings:  7278
+  Functions: 4579
+  Symbols:   897
+  CStrings:  7050
 
Symbols:
+ _$sBi64_WV
+ _AnalyticsSendEvent
+ _swift_getForeignTypeMetadata
- _CFDictionarySetValue
- _OBJC_CLASS_$_AWDPushConnectionConnected
- _OBJC_CLASS_$_AWDPushConnectionDisconnected
- _OBJC_CLASS_$_AWDPushFilterChanged
- _OBJC_CLASS_$_AWDPushFilterSent
- _OBJC_CLASS_$_AWDPushKeepAliveFailed
- _OBJC_CLASS_$_AWDPushKeepAliveSent
- _OBJC_CLASS_$_AWDPushProxyManagerReceive
- _OBJC_CLASS_$_AWDPushProxyManagerSend
- _OBJC_CLASS_$_AWDPushReceived
- _OBJC_CLASS_$_AWDPushReceivedDropped
- _OBJC_CLASS_$_AWDPushReceivedSlow
- _OBJC_CLASS_$_AWDPushSent
- _OBJC_CLASS_$_AWDPushTopicPolicyChange
- _OBJC_CLASS_$_CUTReporting
CStrings:
+ "\n!\x12"
+ "\x12\x11\x142\x11\x91\x152"
+ "%!@(MISSING): Client %!@(MISSING) has out of date filter, send now on %!{(MISSING)public}@"
+ "%!@(MISSING): Out of date filter, send now on %!{(MISSING)public}@"
+ "%!@(MISSING): Sending filter message for version: %!l(MISSING)lu reason %!@(MISSING) triggeringTopic %!@(MISSING) with token %!@(MISSING) on interface %!{(MISSING)public}@ with enabled topics = %!@(MISSING), opportunistic topics = %!@(MISSING), non-waking topics = %!@(MISSING), paused topics = %!@(MISSING), ignored topics = %!@(MISSING)"
+ "-[APSUserCourier _sendFilterMessageOnProtocolConnection:withChange:]"
+ "@\"APSFilterChange\""
+ "APSFilterChange"
+ "APSMetricLogger"
+ "I28@0:8@16B24"
+ "PushConnectionSSLError"
+ "PushType"
+ "Sending disconnect event to CA: %!@(MISSING)"
+ "Sending filter event to CA: %!@(MISSING)"
+ "T@\"NSObject<OS_xpc_object>\",&,N"
+ "T@\"NSString\",N,C"
+ "TQ,N,Vreason"
+ "Tq,N,VtopicGroupChange"
+ "T{os_unfair_lock_s=I},N,V_connectionLock"
+ "_connectionLock"
+ "_requestToSendFilterOnTopicManager:change:"
+ "_sendFilterMessageOnProtocolConnection:withChange:"
+ "anyObject"
+ "changeType"
+ "connectionConnectedWithDuration:interface:linkQuality:dualChannelState:dnsResolutionTimeMilliseconds:tlsHandshakeTimeMilliseconds:"
+ "connectionDisconnected:linkQuality:reason:"
+ "connectionEncounteredSSLError:interface:"
+ "connectionLock"
+ "dualChannelStateFrom:isPiggyBacking:"
+ "filterSent:connectionType:"
+ "handleAcknowledgmentForOutgoingMessageWithResult:ackTimestamp:linkQuality:connectionType:onInterface:"
+ "initWithChange:triggeringTopic:"
+ "setConnectionLock:"
+ "setReason:"
+ "setTopicGroupChange:"
+ "setTriggeringTopic:"
+ "sslErrorFromErrorCode:"
+ "topicGroupChange"
+ "topicManagerRequestToSendFilter:change:"
+ "triggeringTopic"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "v32@0:8@\"APSTopicManager\"16@\"APSFilterChange\"24"
+ "v32@0:8@16B24B28"
+ "v36@0:8q16@24I32"
+ "v52@0:8@16Q24i32q36@44"
+ "v60@0:8@16q24@32I40@44@52"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{os_unfair_lock_s=I}16@0:8"
- "\x01\x11\x11"
- "\x01\x11\x13\x11"
- "\x01\x11\x15"
- "\x02\x11\x12"
- "\t1\x12"
- "\x12\x11\x142\x11\x91\x15\""
- "\x17"
- "                        "
- "                                  "
- "                       GUID : %!@(MISSING)"
- "                      Reason: %!d(MISSING)"
- "                      Topic : %!@(MISSING)"
- "                    isNearby: %!d(MISSING)"
- "                  GUID : %!@(MISSING)"
- "                  Timestamp : %!l(MISSING)lu"
- "               Link Quality : %!d(MISSING)"
- "               Metric Object: %!p(MISSING)"
- "               Topics Count : %!u(MISSING)"
- "             GUID : %!@(MISSING)"
- "             Message command: %!d(MISSING)"
- "            Connection Type : %!u(MISSING)"
- "            Error : %!u(MISSING)"
- "            Topic : %!@(MISSING)"
- "           Dual Channel Sate: %!d(MISSING)"
- "          Flushes : %!u(MISSING)"
- "          Link Quality : %!d(MISSING)"
- "          Metric Object: %!p(MISSING)"
- "         Keep Alive Version : %!u(MISSING)"
- "        SSL Error : %!u(MISSING)"
- "        didCauseFilterChange: %!d(MISSING)"
- "       Connection Type : %!u(MISSING)"
- "       Current growth stage : %!u(MISSING)"
- "       Time since connected : %!u(MISSING)"
- "      Connect Duration : %!u(MISSING)"
- "      Dual Channel Sate: %!d(MISSING)"
- "      Wake Status : %!d(MISSING)"
- "     From Storage : %!u(MISSING)"
- "     Link Quality : %!d(MISSING)"
- "     Metric Object: %!p(MISSING)"
- "     Payload Size : %!u(MISSING)"
- "    Generic Error : %!d(MISSING)"
- "    Keep alive ACK duration : %!u(MISSING)"
- "    Send Duration : %!u(MISSING)"
- "   Last keep alive interval : %!u(MISSING)"
- "   Receive Offset : %!u(MISSING)"
- "  Connection Type : %!u(MISSING)"
- " Dual Channel Sate: %!d(MISSING)"
- " TLS Handshake Duration: %!u(MISSING)"
- " Time since last keep alive : %!u(MISSING)"
- "%!@(MISSING): Out of data filter, send now on %!{(MISSING)public}@"
- "%!@(MISSING): Sending filter message for version: %!l(MISSING)lu reason %!@(MISSING) with token %!@(MISSING) on interface %!{(MISSING)public}@ with enabled topics = %!@(MISSING), opportunistic topics = %!@(MISSING), non-waking topics = %!@(MISSING), paused topics = %!@(MISSING), ignored topics = %!@(MISSING)"
- "-[APSUserCourier _sendFilterMessageOnProtocolConnection:withReason:]"
- "@\"AWDServerConnection\""
- "@\"PBCodable<NSCopying>\"16@0:8"
- "@40@0:8@16I24@28I36"
- "@44@0:8@16@24q32B40"
- "@44@0:8@16q24@32B40"
- "@48@0:8@16B24B28@32@40"
- "@52@0:8@16I24@28I36I40@44"
- "@64@0:8@16@24I32@36I44@48@56"
- "@72@0:8@16I24@28I36@40@48@56@64"
- "@76@0:8@16I24@28I36@40@48@56I64@68"
- "@76@0:8@16I24I28@32I40@44@52@60@68"
- "@80@0:8@16I24@28I36@40@48@56@64@72"
- "@84@0:8@16I24I28@32I40@44@52@60@68@76"
- "APSAWDLogger"
- "APSAWDMetricTypePushConnectionConnected"
- "APSAWDMetricTypePushConnectionDisconnected"
- "APSAWDMetricTypePushFilterChanged"
- "APSAWDMetricTypePushFilterSent"
- "APSAWDMetricTypePushKeepAliveFailed"
- "APSAWDMetricTypePushKeepAliveSent"
- "APSAWDMetricTypePushReceived"
- "APSAWDMetricTypePushReceivedSlow"
- "APSAWDMetricTypePushSent"
- "APSAWDMetricTypePushTopicPolicyChanged"
- "APSCoreAnalyticsLogger"
- "APSPushConnectionConnectedMetric"
- "APSPushConnectionDisconnectedMetric"
- "APSPushFilterChangedMetric"
- "APSPushFilterSentMetric"
- "APSPushKeepAliveFailedMetric"
- "APSPushKeepAliveSentMetric"
- "APSPushProxyManagerReceiveMetric"
- "APSPushProxyManagerSendMetric"
- "APSPushReceivedDroppedMetric"
- "APSPushReceivedMetric"
- "APSPushReceivedSlowMetric"
- "APSPushSentMetric"
- "APSPushTopicPolicyChangedMetric"
- "APSPushWakeTimeToLiveMetric"
- "APSRTCLogger"
- "AWDServerConnection"
- "AnalyticsSendEvent"
- "CUTAWDMetric"
- "CUTCoreAnalyticsMetric"
- "CUTMetric"
- "CUTMetricLogger"
- "CUTRTCMetric"
- "CoreAnalytics"
- "Created metric container: 0x%!x(MISSING) succeeded? %!@(MISSING)"
- "Creating AWD server connection"
- "DNS Resolution Duration: %!u(MISSING)"
- "EnableRTC"
- "Event: %!@(MISSING)"
- "Failed to create RTCReporting session. Error: %!@(MISSING)"
- "No metric or metricContainer to submit"
- "RTCSessionPromiseWithBatchingInterval:"
- "T@\"AWDServerConnection\",R,V_awdServerConnection"
- "T@\"NSDictionary\",R"
- "T@\"NSNumber\",&,N,V_timeToFullyConnect"
- "T@\"NSNumber\",&,N,V_timeToLastFromStorage"
- "T@\"NSNumber\",R,N,V_connectDuration"
- "T@\"NSNumber\",R,N,V_currentGrowthStage"
- "T@\"NSNumber\",R,N,V_dnsResolutionTimeMilliseconds"
- "T@\"NSNumber\",R,N,V_flushes"
- "T@\"NSNumber\",R,N,V_genericError"
- "T@\"NSNumber\",R,N,V_isFromStorage"
- "T@\"NSNumber\",R,N,V_keepAliveACKDuration"
- "T@\"NSNumber\",R,N,V_lastKeepAliveInterval"
- "T@\"NSNumber\",R,N,V_linkQuality"
- "T@\"NSNumber\",R,N,V_payloadSize"
- "T@\"NSNumber\",R,N,V_receiveOffset"
- "T@\"NSNumber\",R,N,V_sendDuration"
- "T@\"NSNumber\",R,N,V_timeSinceConnected"
- "T@\"NSNumber\",R,N,V_timeSinceLastSuccessfulKeepAlive"
- "T@\"NSNumber\",R,N,V_tlsHandshakeTimeMilliseconds"
- "T@\"NSNumber\",R,N,V_topicsCount"
- "T@\"NSString\",R"
- "T@\"NSString\",R,N,V_domain"
- "T@\"NSString\",R,N,V_guid"
- "T@\"NSString\",R,N,V_topic"
- "T@\"NSString\",R,N,V_wakeStatus"
- "T@\"PBCodable<NSCopying>\",R"
- "T@\"PBCodable<NSCopying>\",R,N"
- "TB,N,V_connectedOnWake"
- "TB,N,V_everConnected"
- "TB,R,N,V_didCauseFilterChange"
- "TB,R,N,V_isNearby"
- "TI,R"
- "TI,R,N,V_connectionType"
- "TI,R,N,V_dualChannelState"
- "TI,R,N,V_error"
- "TI,R,N,V_reason"
- "TI,R,N,V_sslError"
- "TI,R,N,V_version"
- "TS,R"
- "Tq,R,N,V_changedReason"
- "Tq,R,N,V_messageCommand"
- "WirelessDiagnostics"
- "_AWDServerConnection"
- "_awdServerConnection"
- "_changedReason"
- "_connectDuration"
- "_connectedOnWake"
- "_connectionTypeForInterface:"
- "_currentGrowthStage"
- "_didCauseFilterChange"
- "_dualChannelState"
- "_error"
- "_everConnected"
- "_flushes"
- "_genericError"
- "_isFromStorage"
- "_isNearby"
- "_keepAliveACKDuration"
- "_lastKeepAliveInterval"
- "_linkQuality"
- "_messageCommand"
- "_payloadSize"
- "_reason"
- "_receiveOffset"
- "_requestToSendFilterOnTopicManager:"
- "_sendDuration"
- "_shouldSubmit"
- "_sslError"
- "_submitAWDMetric:withContainer:"
- "_submitMetric:withIdentifier:"
- "_timeSinceConnected"
- "_timeSinceLastSuccessfulKeepAlive"
- "_timeToFullyConnect"
- "_timeToLastFromStorage"
- "_topicsCount"
- "_wakeStatus"
- "awdIdentifier"
- "awdRepresentation"
- "awdServerConnection"
- "change"
- "changedReason"
- "changedTopicsCount"
- "com.apple.aps.awd-queue"
- "connectedOnWake"
- "dnsDuration"
- "everConnected"
- "handleAcknowledgmentForOutgoingMessageWithResult:ackTimestamp:linkQuality:connectionType:dualChannelState:onInterface:"
- "initWithComponentId:andBlockOnConfiguration:"
- "initWithDomain:"
- "initWithDouble:"
- "initWithGuid:changedReason:topicsCount:topic:"
- "initWithGuid:connectDuration:connectionType:linkQuality:dualChannelState:dnsTimeMilliSeconds:tlsTimeMilliSeconds:"
- "initWithGuid:connectedOnWake:everConnected:timeToFullyConnect:timeToLastFromStorage:"
- "initWithGuid:connectionType:linkQuality:dualChannelState:flushes:sendDuration:payloadSize:error:topic:"
- "initWithGuid:connectionType:linkQuality:dualChannelState:receiveOffset:payloadSize:isFromStorage:topic:"
- "initWithGuid:connectionType:linkQuality:dualChannelState:receiveOffset:payloadSize:isFromStorage:topic:wakeStatus:"
- "initWithGuid:connectionType:linkQuality:error:sslError:genericError:"
- "initWithGuid:connectionType:linkQuality:reason:"
- "initWithGuid:messageCommand:topic:isNearby:"
- "initWithGuid:topic:changedReason:didCauseFilterChange:"
- "initWithGuid:version:connectionType:linkQuality:dualChannelState:timeSinceLastSuccessfulKeepAlive:timeSinceConnected:lastKeepAliveInterval:currentGrowthStage:"
- "initWithGuid:version:connectionType:linkQuality:dualChannelState:timeSinceLastSuccessfulKeepAlive:timeSinceConnected:lastKeepAliveInterval:keepAliveACKDuration:currentGrowthStage:"
- "initWithInt:"
- "keepAliveACKDuration"
- "keepAliveVersion"
- "logMetric:"
- "logger"
- "messageCommand"
- "metric %!@(MISSING) {content:%!{(MISSING)private}@"
- "newMetricContainerWithIdentifier:"
- "numberWithLong:"
- "registerResultBlock:"
- "rtcType"
- "sendMessageWithCategory:type:payload:error:"
- "sentReason"
- "setChange:"
- "setChangedReason:"
- "setChangedTopicsCount:"
- "setConnectDuration:"
- "setConnectedOnWake:"
- "setCurrentGrowthStage:"
- "setDidCauseFilterChange:"
- "setDnsDuration:"
- "setDualChannelState:"
- "setError:"
- "setEverConnected:"
- "setFlushes:"
- "setGenericError:"
- "setIsFromStorage:"
- "setIsNearby:"
- "setKeepAliveACKDuration:"
- "setKeepAliveVersion:"
- "setLastKeepAliveInterval:"
- "setLinkQuality:"
- "setMessageCommand:"
- "setMetric:"
- "setPayloadSize:"
- "setReceiveOffset:"
- "setSendDuration:"
- "setSentReason:"
- "setSslError:"
- "setTimeSinceConnected:"
- "setTimeSinceLastSuccessfulKeepAlive:"
- "setTimeToFullyConnect:"
- "setTimeToLastFromStorage:"
- "setTlsDuration:"
- "setWakeStatus:"
- "submitMetric:"
- "timeToFullyConnect"
- "timeToFullyConnected"
- "timeToLastFromStorage"
- "tlsDuration"
- "topicManagerRequestToSendFilter:"
- "v16@?0@\"CUTResult\"8"
- "v24@0:8@\"<CUTMetric>\"16"
- "v24@0:8@\"APSTopicManager\"16"
- "v32@0:8q16B24B28"
- "v56@0:8@16Q24i32q36I44@48"

```
