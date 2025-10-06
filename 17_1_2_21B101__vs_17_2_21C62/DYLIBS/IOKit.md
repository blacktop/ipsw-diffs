## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-100065.40.4.0.0
-  __TEXT.__text: 0x9d760
-  __TEXT.__auth_stubs: 0x1f80
+100065.60.6.0.0
+  __TEXT.__text: 0x9dcd0
+  __TEXT.__auth_stubs: 0x1f90
   __TEXT.__objc_methlist: 0x14c
-  __TEXT.__oslogstring: 0x47a7
-  __TEXT.__cstring: 0xb258
+  __TEXT.__oslogstring: 0x4818
+  __TEXT.__cstring: 0xb303
   __TEXT.__const: 0xea80
-  __TEXT.__unwind_info: 0x1e48
+  __TEXT.__unwind_info: 0x1e60
   __TEXT.__objc_classname: 0x58
   __TEXT.__objc_methname: 0xa3
-  __TEXT.__objc_methtype: 0x18ec
+  __TEXT.__objc_methtype: 0x1945
   __TEXT.__objc_stubs: 0x60
   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0x2688

   __DATA_CONST.__objc_selrefs: 0x40
   __AUTH_CONST.__const: 0x1bb8
   __AUTH_CONST.__objc_const: 0x1f8
-  __AUTH_CONST.__cfstring: 0x6e80
-  __AUTH_CONST.__auth_got: 0xfc8
+  __AUTH_CONST.__cfstring: 0x6f00
+  __AUTH_CONST.__auth_got: 0xfd0
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0xa0
   __DATA.__objc_classrefs: 0x38

   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5024BA32-7E79-3587-8C48-7149C0C4BBA6
-  Functions: 3607
-  Symbols:   6036
-  CStrings:  3290
+  UUID: F5369613-C587-3FC1-B85B-023931EC8DB6
+  Functions: 3612
+  Symbols:   6044
+  CStrings:  3301
 
Symbols:
+ _EntitlementCheckApplier
+ _IOHIDEventSystemConnectionHasEntitlement
+ _IOHIDServiceCheckEntitlements
+ ___IOHIDEventSystemConnectionCheckServerStatus
+ ___IOHIDEventSystemConnectionCheckServerStatus.cold.1
+ ___IOHIDServiceInit.cold.4
+ ___block_descriptor_tmp.125
+ ___block_descriptor_tmp.126
+ ___block_descriptor_tmp.134
+ ___block_descriptor_tmp.135
+ ___block_descriptor_tmp.136
+ ___block_descriptor_tmp.146
+ ___block_descriptor_tmp.178
+ ___block_descriptor_tmp.179
+ ___block_descriptor_tmp.189
+ ___block_descriptor_tmp.190
+ ___block_descriptor_tmp.192
+ ___block_descriptor_tmp.223
+ ___block_descriptor_tmp.264
+ ___block_descriptor_tmp.265
+ ___block_descriptor_tmp.267
+ _xpc_copy_description
- ___block_descriptor_tmp.122
- ___block_descriptor_tmp.123
- ___block_descriptor_tmp.129
- ___block_descriptor_tmp.130
- ___block_descriptor_tmp.131
- ___block_descriptor_tmp.143
- ___block_descriptor_tmp.155
- ___block_descriptor_tmp.175
- ___block_descriptor_tmp.217
- ___block_descriptor_tmp.258
- ___block_descriptor_tmp.259
- ___block_descriptor_tmp.261
CStrings:
+ "%s: Server died, preventing any future MIG calls"
+ "ConnectionEntitlements"
+ "EventSystemEntitlements"
+ "HIDServiceAccessEntitlement"
+ "OSKEXT_BUILD_DATE 06:54:10 Nov 12 2023"
+ "ServiceEntitlements"
+ "[%#llx] Invalid entitlements property, expected Array or String"
+ "com.apple.private.hid.client.debug-tool"
+ "com.apple.private.hid.client.debug-tool.internal"
+ "{?=\"session\"^{__IOHIDSession}\"service\"I\"serviceInterface\"^^{IOHIDServiceInterface}\"serviceInterface2\"^^{IOHIDServiceInterface2}\"plugInInterface\"^^{IOCFPlugInInterfaceStruct}\"registryID\"^{__CFNumber}\"locationID\"^v\"entitlements\"^{__CFArray}\"queueContext\"^{__IOHIDServiceQueueContext}\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"notificationPort\"^{IONotificationPort}\"notification\"I\"removalNotificationSet\"^{__CFSet}\"propertyNotificationSet\"^{__CFSet}\"eventTarget\"^v\"eventRefcon\"^v\"eventCallback\"^?\"lastLEDMask\"I\"lastButtonMask\"I\"currentReportInterval\"I\"currentBatchInterval\"I\"defaultReportInterval\"I\"defaultBatchInterval\"I\"primaryUsagePage\"I\"primaryUsage\"I\"transport\"[32c]\"queueSize\"I\"containsReportInterval\"i\"state\"I\"eventCount\"I\"eventMask\"Q\"clientCacheDict\"^{__CFDictionary}\"simpleFilters\"^{__CFArray}\"filters\"^{__CFArray}\"keyboardEventInProgress\"^{__CFSet}\"nullEventMask\"Q\"displayIntegratedDigitizer\"i\"builtIn\"i\"inMomentumPhase\"i\"inDigitizerPhase\"i\"supportReportLatency\"i\"hidden\"i\"protectedAccess\"i\"propertyCache\"^{__CFDictionary}\"propertyCacheHit\"I\"propertyCacheMiss\"I\"activityLastTimestamp\"Q\"virtualService\"{?=\"connection\"^v\"target\"^v\"refcon\"^v\"callbacks\"^{IOHIDServiceVirtualCallbacksV2}}\"connections\"^^v\"propertySetTime\"Q\"propertyGetTime\"Q\"elementSetTime\"Q\"regID\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^Q\"pluginCancelHandler\"@?\"filterCancelHandler\"@?\"pendingPluginCancel\"B\"pendingFilterCancels\"I\"cancelTimer\"@\"NSObject<OS_dispatch_source>\"\"dataLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"hidAnalyticsEvent\"^v\"hidAnalyticsDispatchEvent\"^v\"objc\"{?=\"interface\"^v\"name\"^{__CFString}\"getProperty\":\"setProperty\":\"eventMatching\":\"setEventDispatcher\":\"setCancelHandler\":\"activate\":\"cancel\":\"setDispatchQueue\":\"clientNotification\":\"copyEvent\":\"setOutputEvent\":}}"
+ "{?=\"system\"^{__IOHIDEventSystem}\"notifications\"^{__CFDictionary}\"queue\"^{__IOHIDEventQueue}\"port\"^{__IOMIGMachPort}\"reply_port\"I\"demuxCallback\"^?\"demuxRefcon\"^v\"terminationCallback\"^?\"terminationRefcon\"^v\"services\"^{__CFSet}\"pid\"i\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"sendPossiblePort\"I\"sendPossibleSource\"@\"NSObject<OS_dispatch_source>\"\"replySendPossibleSource\"@\"NSObject<OS_dispatch_source>\"\"sendPossible\"i\"propertySet\"^{__CFSet}\"caller\"^{__CFString}\"procName\"^{__CFString}\"uuid\"^{__CFString}\"uuidStr\"*\"type\"i\"attributes\"^{__CFDictionary}\"task_name_port\"I\"audit_token\"{?=\"val\"[8I]}\"lock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"entitlements\"^(IOHIDEventSystemConnectionEntitlements)\"connectionEntitlements\"@\"NSObject<OS_xpc_object>\"\"disableProtectedServices\"i\"filterPriority\"i\"state\"I\"notificationsLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"virtualServices\"^{__CFDictionary}\"eventFilterMask\"Q\"eventFilteredCount\"I\"eventFilterTimeoutCount\"I\"droppedEventCount\"I\"currentDroppedEventCount\"I\"droppedEventTypeMask\"Q\"eventCount\"I\"eventMask\"Q\"lastDroppedEventTime\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"firstDroppedEventTime\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"maxEventLatency\"Q\"droppedEventStatus\"i\"propertyChangeNotificationHandlingTime\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^I\"activityState\"I\"activityStateChangeCount\"I\"idleNotificationTime\"Q\"activityDispatchSource\"@\"NSObject<OS_dispatch_source>\"\"activityNotification\"^{__IOHIDNotification}\"activityLog\"^{__CFData}\"filter\"^{__IOHIDConnectionFilter}\"serverDied\"i}"
- "Entitlements"
- "OSKEXT_BUILD_DATE 12:59:24 Sep 30 2023"
- "{?=\"session\"^{__IOHIDSession}\"service\"I\"serviceInterface\"^^{IOHIDServiceInterface}\"serviceInterface2\"^^{IOHIDServiceInterface2}\"plugInInterface\"^^{IOCFPlugInInterfaceStruct}\"registryID\"^{__CFNumber}\"locationID\"^v\"queueContext\"^{__IOHIDServiceQueueContext}\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"notificationPort\"^{IONotificationPort}\"notification\"I\"removalNotificationSet\"^{__CFSet}\"propertyNotificationSet\"^{__CFSet}\"eventTarget\"^v\"eventRefcon\"^v\"eventCallback\"^?\"lastLEDMask\"I\"lastButtonMask\"I\"currentReportInterval\"I\"currentBatchInterval\"I\"defaultReportInterval\"I\"defaultBatchInterval\"I\"primaryUsagePage\"I\"primaryUsage\"I\"transport\"[32c]\"queueSize\"I\"containsReportInterval\"i\"state\"I\"eventCount\"I\"eventMask\"Q\"clientCacheDict\"^{__CFDictionary}\"simpleFilters\"^{__CFArray}\"filters\"^{__CFArray}\"keyboardEventInProgress\"^{__CFSet}\"nullEventMask\"Q\"displayIntegratedDigitizer\"i\"builtIn\"i\"inMomentumPhase\"i\"inDigitizerPhase\"i\"supportReportLatency\"i\"hidden\"i\"protectedAccess\"i\"propertyCache\"^{__CFDictionary}\"propertyCacheHit\"I\"propertyCacheMiss\"I\"activityLastTimestamp\"Q\"virtualService\"{?=\"connection\"^v\"target\"^v\"refcon\"^v\"callbacks\"^{IOHIDServiceVirtualCallbacksV2}}\"connections\"^^v\"propertySetTime\"Q\"propertyGetTime\"Q\"elementSetTime\"Q\"regID\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^Q\"pluginCancelHandler\"@?\"filterCancelHandler\"@?\"pendingPluginCancel\"B\"pendingFilterCancels\"I\"cancelTimer\"@\"NSObject<OS_dispatch_source>\"\"dataLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"hidAnalyticsEvent\"^v\"hidAnalyticsDispatchEvent\"^v\"objc\"{?=\"interface\"^v\"name\"^{__CFString}\"getProperty\":\"setProperty\":\"eventMatching\":\"setEventDispatcher\":\"setCancelHandler\":\"activate\":\"cancel\":\"setDispatchQueue\":\"clientNotification\":\"copyEvent\":\"setOutputEvent\":}}"
- "{?=\"system\"^{__IOHIDEventSystem}\"notifications\"^{__CFDictionary}\"queue\"^{__IOHIDEventQueue}\"port\"^{__IOMIGMachPort}\"reply_port\"I\"demuxCallback\"^?\"demuxRefcon\"^v\"terminationCallback\"^?\"terminationRefcon\"^v\"services\"^{__CFSet}\"pid\"i\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"sendPossiblePort\"I\"sendPossibleSource\"@\"NSObject<OS_dispatch_source>\"\"replySendPossibleSource\"@\"NSObject<OS_dispatch_source>\"\"sendPossible\"i\"propertySet\"^{__CFSet}\"caller\"^{__CFString}\"procName\"^{__CFString}\"uuid\"^{__CFString}\"uuidStr\"*\"type\"i\"attributes\"^{__CFDictionary}\"task_name_port\"I\"audit_token\"{?=\"val\"[8I]}\"lock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"entitlements\"^(IOHIDEventSystemConnectionEntitlements)\"disableProtectedServices\"i\"filterPriority\"i\"state\"I\"notificationsLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"virtualServices\"^{__CFDictionary}\"eventFilterMask\"Q\"eventFilteredCount\"I\"eventFilterTimeoutCount\"I\"droppedEventCount\"I\"currentDroppedEventCount\"I\"droppedEventTypeMask\"Q\"eventCount\"I\"eventMask\"Q\"lastDroppedEventTime\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"firstDroppedEventTime\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"maxEventLatency\"Q\"droppedEventStatus\"i\"propertyChangeNotificationHandlingTime\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^I\"activityState\"I\"activityStateChangeCount\"I\"idleNotificationTime\"Q\"activityDispatchSource\"@\"NSObject<OS_dispatch_source>\"\"activityNotification\"^{__IOHIDNotification}\"activityLog\"^{__CFData}\"filter\"^{__IOHIDConnectionFilter}}"

```
