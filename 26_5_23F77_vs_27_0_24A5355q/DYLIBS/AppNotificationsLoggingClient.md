## AppNotificationsLoggingClient

> `/System/Library/PrivateFrameworks/AppNotificationsLoggingClient.framework/AppNotificationsLoggingClient`

```diff

-627.13.0.1.0
-  __TEXT.__text: 0x4b10
-  __TEXT.__auth_stubs: 0x2d0
+658.0.9.0.0
+  __TEXT.__text: 0x4440
   __TEXT.__objc_methlist: 0x300
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x783
+  __TEXT.__cstring: 0x787
   __TEXT.__oslogstring: 0x522
   __TEXT.__gcc_except_tab: 0x70
-  __TEXT.__unwind_info: 0x2d8
-  __TEXT.__objc_classname: 0x74
-  __TEXT.__objc_methname: 0x85a
-  __TEXT.__objc_methtype: 0x29d
-  __TEXT.__objc_stubs: 0x520
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__unwind_info: 0x160
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x268
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_selrefs: 0x278
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0xa0
   __AUTH_CONST.__const: 0x720
   __AUTH_CONST.__cfstring: 0x840
   __AUTH_CONST.__objc_const: 0x410
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x30
   __DATA.__data: 0x128
   __DATA.__bss: 0x2d0

   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CE249355-14C6-3746-B871-58CDFDE160D6
-  Functions: 235
-  Symbols:   795
-  CStrings:  346
+  UUID: 7446C479-2771-3517-A51C-9C6A10F77F50
+  Functions: 233
+  Symbols:   793
+  CStrings:  207
 
Symbols:
+ ___37-[ATXNotificationsLoggingClient init]_block_invoke.63
+ ___66-[ATXNotificationsLoggingClient _processActiveSuggestionsRequests]_block_invoke.66
+ ___66-[ATXNotificationsLoggingClient _processActiveSuggestionsRequests]_block_invoke.70
+ ___66-[ATXNotificationsLoggingClient _processActiveSuggestionsRequests]_block_invoke.70.cold.1
+ ___block_literal_global.73
+ ___block_literal_global.75
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x25
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- ___37-[ATXNotificationsLoggingClient init]_block_invoke.69
- ___66-[ATXNotificationsLoggingClient _processActiveSuggestionsRequests]_block_invoke.72
- ___66-[ATXNotificationsLoggingClient _processActiveSuggestionsRequests]_block_invoke.76
- ___66-[ATXNotificationsLoggingClient _processActiveSuggestionsRequests]_block_invoke.76.cold.1
- ___block_literal_global.85
- ___block_literal_global.87
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
CStrings:
- ".cxx_destruct"
- "@\"NSDate\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSXPCConnection\""
- "@\"_PASSimpleCoalescingTimer\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@72@0:8@16@24@32@40@48@56Q64"
- "ATXNotificationsInterface"
- "ATXNotificationsLoggingClient"
- "ATXNotificationsLoggingProtocol"
- "B16@0:8"
- "NSCoding"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "T@\"NSDate\",&,N,V_publicationDate"
- "T@\"NSString\",&,N,V_message"
- "T@\"NSString\",&,N,V_sectionID"
- "T@\"NSString\",&,N,V_subtitle"
- "T@\"NSString\",&,N,V_title"
- "T@\"NSString\",&,N,V_topic"
- "TB,R"
- "TQ,N,V_feed"
- "TQ,N,V_numSuppActions"
- "_activeSuggestionsRequests"
- "_coalescingTimer"
- "_feed"
- "_message"
- "_numSuppActions"
- "_processActiveSuggestionsRequests"
- "_publicationDate"
- "_queue"
- "_sectionID"
- "_subtitle"
- "_title"
- "_topic"
- "_xpcConnection"
- "activeSuggestionsWithReply:"
- "addObject:"
- "count"
- "createArchivedMetadata:categoryId:title:subtitle:message:numSuppActions:feed:"
- "dealloc"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "extractMetadata"
- "getBundleIdFromMetadata:"
- "getFeedFromMetadata:"
- "getMessageFromMetadata:"
- "getNumSuppActionsFromMetadata:"
- "getSubtitleFromMetadata:"
- "getTimezoneFromMetadata:"
- "getTitleFromMetadata:"
- "getTopicFromMetadata:"
- "init"
- "initWithCoder:"
- "initWithMachServiceName:options:"
- "initWithQueue:operation:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqualToString:"
- "localTimeZone"
- "logNotificationDeliveryUI:notificationUUIDs:"
- "logNotificationEvent:notification:"
- "logNotificationEvent:notification:reason:"
- "logNotificationEvent:notification:reason:interactionUI:"
- "logNotificationGroupEvent:eventIdentifier:"
- "logNotificationGroupEvent:eventIdentifier:timestamp:"
- "logRealTimeTuningCountFrom:"
- "logRealTimeTuningOutcome:withBundleId:"
- "logSuggestionEvent:suggestionType:suggestionIdentifier:timestamp:"
- "now"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "publicationDate"
- "raise:format:"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeObjectForKey:"
- "resume"
- "runAfterDelaySeconds:coalescingBehavior:"
- "secondsFromGMT"
- "sectionID"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setFeed:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setMessage:"
- "setNumSuppActions:"
- "setObject:forKeyedSubscript:"
- "setPublicationDate:"
- "setRemoteObjectInterface:"
- "setSectionID:"
- "setSubtitle:"
- "setTitle:"
- "setTopic:"
- "setWithObjects:"
- "sharedInstance"
- "stringWithFormat:"
- "stripContentInMetadata:"
- "supportsSecureCoding"
- "topic"
- "unsignedIntegerValue"
- "uuid"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8Q16"
- "v32@0:8Q16@\"NSArray\"24"
- "v32@0:8Q16@\"NSString\"24"
- "v32@0:8Q16@24"
- "v32@0:8q16@\"ATXUserNotification\"24"
- "v32@0:8q16@\"NSUUID\"24"
- "v32@0:8q16@24"
- "v40@0:8q16@\"ATXUserNotification\"24Q32"
- "v40@0:8q16@\"NSUUID\"24@\"NSDate\"32"
- "v40@0:8q16@24@32"
- "v40@0:8q16@24Q32"
- "v48@0:8q16@\"ATXUserNotification\"24Q32Q40"
- "v48@0:8q16@24Q32Q40"
- "v48@0:8q16q24@\"NSUUID\"32@\"NSDate\"40"
- "v48@0:8q16q24@32@40"

```
