## CoordinationCore

> `/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore`

```diff

-196.30.2.0.0
+196.40.16.0.0
   __TEXT.__text: 0xc485c
   __TEXT.__auth_stubs: 0x920
   __TEXT.__objc_methlist: 0x84c8
   __TEXT.__const: 0x278
   __TEXT.__gcc_except_tab: 0x2fbc
-  __TEXT.__cstring: 0x2841
+  __TEXT.__cstring: 0x2842
   __TEXT.__oslogstring: 0x94b8
   __TEXT.__unwind_info: 0x3104
   __TEXT.__objc_classname: 0x175f
-  __TEXT.__objc_methname: 0x1286e
+  __TEXT.__objc_methname: 0x12876
   __TEXT.__objc_methtype: 0x39f7
   __TEXT.__objc_stubs: 0xdc20
   __DATA_CONST.__got: 0x320

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xfaa0
   __DATA_CONST.__objc_selrefs: 0x3ca8
+  __DATA_CONST.__objc_protorefs: 0x88
+  __DATA_CONST.__objc_classrefs: 0x768
+  __DATA_CONST.__objc_superrefs: 0x418
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__objc_const: 0x40f0
   __AUTH_CONST.__cfstring: 0x2560

   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x4a0
   __AUTH.__objc_data: 0x2030
-  __DATA.__objc_protorefs: 0x88
-  __DATA.__objc_classrefs: 0x768
-  __DATA.__objc_superrefs: 0x418
   __DATA.__objc_ivar: 0xa08
   __DATA.__data: 0x1980
   __DATA.__bss: 0x70

   - /usr/lib/libobjc.A.dylib
   Functions: 4167
   Symbols:   13485
-  CStrings:  5083
+  CStrings:  5084
 
Symbols:
+ ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke.102
+ ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke.102.cold.1
+ ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke.104
+ ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke.111
+ ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke.111.cold.1
+ ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke.113
+ ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke_2.114
+ ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke_3.115
+ ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke_3.115.cold.1
+ ___101-[CORapportTransport handleResponseToRequest:rapportRepresentation:options:error:responseHandler:at:]_block_invoke.128
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.149
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.151.cold.1
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.152
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.154
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.156
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.150
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.153
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.153.cold.1
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.155
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.155.cold.1
+ ___52-[COMeshController node:didReceiveError:forCommand:]_block_invoke.184
+ ___53-[COMessagingService addOn:receivedRequest:callback:]_block_invoke.119.cold.1
+ ___53-[COMessagingService addOn:receivedRequest:callback:]_block_invoke.120
+ ___54-[CONodeController sendCommand:withCompletionHandler:]_block_invoke.133
+ ___54-[CORapportTransport sendRequest:withResponseHandler:]_block_invoke.109
+ ___54-[CORapportTransport sendRequest:withResponseHandler:]_block_invoke_2.110
+ ___58-[CORapportTransport _setUpRegistrationCompletionHandlers]_block_invoke.99
+ ___58-[CORapportTransport _setUpRegistrationCompletionHandlers]_block_invoke_2.100
+ ___60-[COAlarmService _postNotificationName:connection:userInfo:]_block_invoke.82
+ ___60-[COAlarmService _postNotificationName:connection:userInfo:]_block_invoke.82.cold.1
+ ___60-[COMTActionDirector registerHandler:forType:actions:queue:]_block_invoke.124
+ ___60-[COTimerService _postNotificationName:connection:userInfo:]_block_invoke.82
+ ___60-[COTimerService _postNotificationName:connection:userInfo:]_block_invoke.82.cold.1
+ ___63-[COMTActionDirector handlePerformActionRequest:from:callback:]_block_invoke.111
+ ___63-[COMTActionDirector handlePerformActionRequest:from:callback:]_block_invoke.113
+ ___73-[COMeshController _finalizeCompletionOfNode:memberOfMesh:eventProvider:]_block_invoke.178
+ ___77-[CORapportTransport _updateRequestTimesFromRapportRepresentation:start:end:]_block_invoke.135
+ ___95-[CORapportTransport handleRequestIdentifier:rapportRepresentation:options:responseHandler:at:]_block_invoke.123
+ ___95-[CORapportTransport handleRequestIdentifier:rapportRepresentation:options:responseHandler:at:]_block_invoke_2.127
- ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke.101
- ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke.101.cold.1
- ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke.103
- ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke.110
- ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke.110.cold.1
- ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke.112
- ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke_2.113
- ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke_3.114
- ___101-[COMessagingService sendRequestWithPayload:payloadType:requestType:requestID:members:activityToken:]_block_invoke_3.114.cold.1
- ___101-[CORapportTransport handleResponseToRequest:rapportRepresentation:options:error:responseHandler:at:]_block_invoke.127
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.148
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.150
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.150.cold.1
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.153
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.155
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.149
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.152
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.152.cold.1
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.154
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.154.cold.1
- ___52-[COMeshController node:didReceiveError:forCommand:]_block_invoke.182
- ___53-[COMessagingService addOn:receivedRequest:callback:]_block_invoke.118
- ___53-[COMessagingService addOn:receivedRequest:callback:]_block_invoke.118.cold.1
- ___54-[CONodeController sendCommand:withCompletionHandler:]_block_invoke.132
- ___54-[CORapportTransport sendRequest:withResponseHandler:]_block_invoke.108
- ___54-[CORapportTransport sendRequest:withResponseHandler:]_block_invoke_2.109
- ___58-[CORapportTransport _setUpRegistrationCompletionHandlers]_block_invoke.98
- ___58-[CORapportTransport _setUpRegistrationCompletionHandlers]_block_invoke_2.99
- ___60-[COAlarmService _postNotificationName:connection:userInfo:]_block_invoke.81
- ___60-[COAlarmService _postNotificationName:connection:userInfo:]_block_invoke.81.cold.1
- ___60-[COMTActionDirector registerHandler:forType:actions:queue:]_block_invoke.123
- ___60-[COTimerService _postNotificationName:connection:userInfo:]_block_invoke.81
- ___60-[COTimerService _postNotificationName:connection:userInfo:]_block_invoke.81.cold.1
- ___63-[COMTActionDirector handlePerformActionRequest:from:callback:]_block_invoke.110
- ___63-[COMTActionDirector handlePerformActionRequest:from:callback:]_block_invoke.112
- ___73-[COMeshController _finalizeCompletionOfNode:memberOfMesh:eventProvider:]_block_invoke.177
- ___77-[CORapportTransport _updateRequestTimesFromRapportRepresentation:start:end:]_block_invoke.134
- ___95-[CORapportTransport handleRequestIdentifier:rapportRepresentation:options:responseHandler:at:]_block_invoke.122
- ___95-[CORapportTransport handleRequestIdentifier:rapportRepresentation:options:responseHandler:at:]_block_invoke_2.126
CStrings:
+ "196.40.16"
+ "T@\"NSString\",?,R,C"
+ "home:didUpdateSupportsResidentActionSetStateEvaluation:"
- "196.30.2"
- "accessory:didUpdateBulletinBoardNotificationServiceGroupForService:"

```
