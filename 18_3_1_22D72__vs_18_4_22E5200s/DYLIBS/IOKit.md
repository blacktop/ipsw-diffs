## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-100140.80.4.0.0
-  __TEXT.__text: 0x9c80c
-  __TEXT.__auth_stubs: 0x2040
+100150.100.19.0.0
+  __TEXT.__text: 0x9d904
+  __TEXT.__auth_stubs: 0x2050
   __TEXT.__objc_methlist: 0x150
-  __TEXT.__const: 0xeb6c
-  __TEXT.__oslogstring: 0x4ac5
-  __TEXT.__cstring: 0xb6d6
-  __TEXT.__unwind_info: 0x1eb8
+  __TEXT.__const: 0x104a4
+  __TEXT.__oslogstring: 0x4b64
+  __TEXT.__cstring: 0xb6ae
+  __TEXT.__unwind_info: 0x1f68
   __TEXT.__objc_classname: 0x58
   __TEXT.__objc_methname: 0xa3
-  __TEXT.__objc_methtype: 0x1972
+  __TEXT.__objc_methtype: 0x19b4
   __TEXT.__objc_stubs: 0x60
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x2768
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x2790
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x1028
-  __AUTH_CONST.__auth_ptr: 0x28
+  __AUTH_CONST.__auth_got: 0x1030
+  __AUTH_CONST.__auth_ptr: 0x50
   __AUTH_CONST.__const: 0x1c28
-  __AUTH_CONST.__cfstring: 0x7220
+  __AUTH_CONST.__cfstring: 0x7240
   __AUTH_CONST.__objc_const: 0x508
   __AUTH.__objc_data: 0x190
-  __AUTH.__data: 0xa0
+  __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x5a0
-  __DATA.__bss: 0x508
-  __DATA.__common: 0xc0
+  __DATA.__data: 0x588
+  __DATA.__bss: 0x490
+  __DATA.__common: 0x100
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0xa8
-  __DATA_DIRTY.__bss: 0x1c8
+  __DATA_DIRTY.__data: 0xd0
+  __DATA_DIRTY.__bss: 0x248
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3416
-  Symbols:   4135
-  CStrings:  2477
+  Functions: 3320
+  Symbols:   4254
+  CStrings:  2475
 
Symbols:
+ _IOHIDEventSystemRematchServices
+ _IOHIDServiceRegister
+ _IOHIDSessionGetEventSystem
+ _kIOHIDServiceUnregisteredKey
+ _xpc_dictionary_get_int64
CStrings:
+ "Async assertion: setting offload delay to %llu"
+ "OSKEXT_BUILD_DATE 03:11:56 Feb 16 2025"
+ "Service: %@ trigger matching failed: service is already registered"
+ "Service:0x%llx  is unregistered, not matching"
+ "Unregistered"
+ "assertion failure: \"!device->cancelHandler && handler\" -> %llu"
+ "assertion failure: \"!manager->cancelHandler && handler\" -> %llu"
+ "assertion failure: \"!manager->runLoop && !manager->dispatchQueue\" -> %llu"
+ "assertion failure: \"!queue->cancelHandler && handler\" -> %llu"
+ "assertion failure: \"__IOHIDQueueSetupAsyncSupport(queue)\" -> %llu"
+ "assertion failure: \"__IOHIDUserDeviceSetupAsyncSupport(device)\" -> %llu"
+ "assertion failure: \"completionElement\" -> %llu"
+ "assertion failure: \"pthread_cond_init(&session->stateCondition, ((void*)0))\" -> %llu"
+ "assertion failure: \"pthread_mutex_init(&service->queueContext->lock, &mutexattr)\" -> %llu"
+ "assertion failure: \"pthread_mutex_init(&session->queueContext->lock, &mutexattr)\" -> %llu"
+ "assertion failure: \"pthread_mutex_lock(&(queueContext)->lock)\" -> %llu"
+ "assertion failure: \"pthread_mutex_lock(&(service->queueContext)->lock)\" -> %llu"
+ "assertion failure: \"pthread_mutex_lock(&(session->queueContext)->lock)\" -> %llu"
+ "assertion failure: \"pthread_mutex_unlock(&(queueContext)->lock)\" -> %llu"
+ "assertion failure: \"pthread_mutex_unlock(&(service->queueContext)->lock)\" -> %llu"
+ "assertion failure: \"pthread_mutex_unlock(&(session->queueContext)->lock)\" -> %llu"
+ "assertion failure: \"pthread_mutexattr_destroy(&mutexattr)\" -> %llu"
+ "assertion failure: \"pthread_mutexattr_init(&mutexattr)\" -> %llu"
+ "assertion failure: \"retainCount < (2147483647 *2U +1U)\" -> %llu"
+ "assertion failure: \"retainCount\" -> %llu"
+ "assertion failure: \"semaphore\" -> %llu"
+ "assertionAsyncOffloadDelay"
+ "{?=\"session\"^{__IOHIDSession}\"service\"I\"serviceInterface\"^^{IOHIDServiceInterface}\"serviceInterface2\"^^{IOHIDServiceInterface2}\"plugInInterface\"^^{IOCFPlugInInterfaceStruct}\"registryID\"^{__CFNumber}\"locationID\"^v\"entitlements\"^{__CFArray}\"queueContext\"^{__IOHIDServiceQueueContext}\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"notificationPort\"^{IONotificationPort}\"notification\"I\"removalNotificationSet\"^{__CFSet}\"propertyNotificationSet\"^{__CFSet}\"requestTerminationNotificationSet\"^{__CFSet}\"eventTarget\"^v\"eventRefcon\"^v\"eventCallback\"^?\"lastLEDMask\"I\"lastButtonMask\"I\"currentReportInterval\"I\"currentBatchInterval\"I\"defaultReportInterval\"I\"defaultBatchInterval\"I\"primaryUsagePage\"I\"primaryUsage\"I\"transport\"[32c]\"queueSize\"I\"containsReportInterval\"i\"state\"I\"eventCount\"I\"eventMask\"Q\"clientCacheDict\"^{__CFDictionary}\"simpleFilters\"^{__CFArray}\"filters\"^{__CFArray}\"keyboardEventInProgress\"^{__CFSet}\"nullEventMask\"Q\"displayIntegratedDigitizer\"i\"builtIn\"i\"inMomentumPhase\"i\"inDigitizerPhase\"i\"supportReportLatency\"i\"hidden\"i\"registered\"i\"protectedAccess\"i\"propertyCache\"^{__CFDictionary}\"propertyCacheHit\"I\"propertyCacheMiss\"I\"activityLastTimestamp\"Q\"virtualService\"{?=\"connection\"^v\"target\"^v\"refcon\"^v\"callbacks\"^{IOHIDServiceVirtualCallbacksV2}}\"connections\"^^v\"propertySetTime\"Q\"propertyGetTime\"Q\"elementSetTime\"Q\"regID\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^Q\"pluginCancelHandler\"@?\"filterCancelHandler\"@?\"pendingPluginCancel\"B\"pendingFilterCancels\"I\"cancelTimer\"@\"NSObject<OS_dispatch_source>\"\"dataLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"hidAnalyticsEvent\"^v\"hidAnalyticsDispatchEvent\"^v\"objc\"{?=\"interface\"^v\"name\"^{__CFString}\"getProperty\":\"setProperty\":\"eventMatching\":\"setEventDispatcher\":\"setCancelHandler\":\"activate\":\"cancel\":\"setDispatchQueue\":\"clientNotification\":\"copyEvent\":\"setOutputEvent\":}}"
+ "{?=\"system\"^{__IOHIDEventSystem}\"notifications\"^{__CFDictionary}\"queue\"^{__IOHIDEventQueue}\"port\"^{__IOMIGMachPort}\"reply_port\"I\"demuxCallback\"^?\"demuxRefcon\"^v\"terminationCallback\"^?\"terminationRefcon\"^v\"services\"^{__CFSet}\"pid\"i\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"sendPossiblePort\"I\"sendPossibleSource\"@\"NSObject<OS_dispatch_source>\"\"replySendPossibleSource\"@\"NSObject<OS_dispatch_source>\"\"sendPossible\"i\"propertySet\"^{__CFSet}\"caller\"^{__CFString}\"procName\"^{__CFString}\"uuid\"^{__CFString}\"uuidStr\"*\"type\"i\"attributes\"^{__CFDictionary}\"task_name_port\"I\"audit_token\"{?=\"val\"[8I]}\"lock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"entitlements\"^(IOHIDEventSystemConnectionEntitlements)\"connectionEntitlements\"@\"NSObject<OS_xpc_object>\"\"disableProtectedServices\"i\"filterPriority\"i\"state\"I\"notificationsLock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"virtualServices\"^{__CFDictionary}\"eventFilterMask\"Q\"eventFilteredCount\"I\"eventFilterTimeoutCount\"I\"droppedEventCount\"I\"currentDroppedEventCount\"I\"droppedEventTypeMask\"Q\"eventCount\"I\"eventMask\"Q\"lastDroppedEventTime\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"firstDroppedEventTime\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"maxEventLatency\"Q\"droppedEventStatus\"i\"propertyChangeNotificationHandlingTime\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^I\"activityState\"I\"activityStateChangeCount\"I\"idleNotificationTime\"Q\"activityDispatchSource\"@\"NSObject<OS_dispatch_source>\"\"activityNotification\"^{__IOHIDNotification}\"activityLog\"^{__CFData}\"filter\"^{__IOHIDConnectionFilter}\"serverDied\"i}"
- ".."
- "ColorComponent0:"
- "ColorComponent1:"
- "ColorComponent2:"
- "ColorSpace:"
- "OSKEXT_BUILD_DATE 02:58:52 Jan 16 2025"
- "Undefined"
- "XYZ"
- "assertion failure: \"!device->cancelHandler && handler\" -> %lld"
- "assertion failure: \"!manager->cancelHandler && handler\" -> %lld"
- "assertion failure: \"!manager->runLoop && !manager->dispatchQueue\" -> %lld"
- "assertion failure: \"!queue->cancelHandler && handler\" -> %lld"
- "assertion failure: \"__IOHIDQueueSetupAsyncSupport(queue)\" -> %lld"
- "assertion failure: \"__IOHIDUserDeviceSetupAsyncSupport(device)\" -> %lld"
- "assertion failure: \"completionElement\" -> %lld"
- "assertion failure: \"pthread_cond_init(&session->stateCondition, ((void *)0))\" -> %lld"
- "assertion failure: \"pthread_mutex_init(&service->queueContext->lock, &mutexattr)\" -> %lld"
- "assertion failure: \"pthread_mutex_init(&session->queueContext->lock, &mutexattr)\" -> %lld"
- "assertion failure: \"pthread_mutex_lock(&(queueContext)->lock)\" -> %lld"
- "assertion failure: \"pthread_mutex_lock(&(service->queueContext)->lock)\" -> %lld"
- "assertion failure: \"pthread_mutex_lock(&(session->queueContext)->lock)\" -> %lld"
- "assertion failure: \"pthread_mutex_unlock(&(queueContext)->lock)\" -> %lld"
- "assertion failure: \"pthread_mutex_unlock(&(service->queueContext)->lock)\" -> %lld"
- "assertion failure: \"pthread_mutex_unlock(&(session->queueContext)->lock)\" -> %lld"
- "assertion failure: \"pthread_mutexattr_destroy(&mutexattr)\" -> %lld"
- "assertion failure: \"pthread_mutexattr_init(&mutexattr)\" -> %lld"
- "assertion failure: \"retainCount < (2147483647 *2U +1U)\" -> %lld"
- "assertion failure: \"retainCount\" -> %lld"
- "assertion failure: \"semaphore\" -> %lld"
- "{?=\"session\"^{__IOHIDSession}\"service\"I\"serviceInterface\"^^{IOHIDServiceInterface}\"serviceInterface2\"^^{IOHIDServiceInterface2}\"plugInInterface\"^^{IOCFPlugInInterfaceStruct}\"registryID\"^{__CFNumber}\"locationID\"^v\"entitlements\"^{__CFArray}\"queueContext\"^{__IOHIDServiceQueueContext}\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"notificationPort\"^{IONotificationPort}\"notification\"I\"removalNotificationSet\"^{__CFSet}\"propertyNotificationSet\"^{__CFSet}\"requestTerminationNotificationSet\"^{__CFSet}\"eventTarget\"^v\"eventRefcon\"^v\"eventCallback\"^?\"lastLEDMask\"I\"lastButtonMask\"I\"currentReportInterval\"I\"currentBatchInterval\"I\"defaultReportInterval\"I\"defaultBatchInterval\"I\"primaryUsagePage\"I\"primaryUsage\"I\"transport\"[32c]\"queueSize\"I\"containsReportInterval\"i\"state\"I\"eventCount\"I\"eventMask\"Q\"clientCacheDict\"^{__CFDictionary}\"simpleFilters\"^{__CFArray}\"filters\"^{__CFArray}\"keyboardEventInProgress\"^{__CFSet}\"nullEventMask\"Q\"displayIntegratedDigitizer\"i\"builtIn\"i\"inMomentumPhase\"i\"inDigitizerPhase\"i\"supportReportLatency\"i\"hidden\"i\"protectedAccess\"i\"propertyCache\"^{__CFDictionary}\"propertyCacheHit\"I\"propertyCacheMiss\"I\"activityLastTimestamp\"Q\"virtualService\"{?=\"connection\"^v\"target\"^v\"refcon\"^v\"callbacks\"^{IOHIDServiceVirtualCallbacksV2}}\"connections\"^^v\"propertySetTime\"Q\"propertyGetTime\"Q\"elementSetTime\"Q\"regID\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^Q\"pluginCancelHandler\"@?\"filterCancelHandler\"@?\"pendingPluginCancel\"B\"pendingFilterCancels\"I\"cancelTimer\"@\"NSObject<OS_dispatch_source>\"\"dataLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"hidAnalyticsEvent\"^v\"hidAnalyticsDispatchEvent\"^v\"objc\"{?=\"interface\"^v\"name\"^{__CFString}\"getProperty\":\"setProperty\":\"eventMatching\":\"setEventDispatcher\":\"setCancelHandler\":\"activate\":\"cancel\":\"setDispatchQueue\":\"clientNotification\":\"copyEvent\":\"setOutputEvent\":}}"
- "{?=\"system\"^{__IOHIDEventSystem}\"notifications\"^{__CFDictionary}\"queue\"^{__IOHIDEventQueue}\"port\"^{__IOMIGMachPort}\"reply_port\"I\"demuxCallback\"^?\"demuxRefcon\"^v\"terminationCallback\"^?\"terminationRefcon\"^v\"services\"^{__CFSet}\"pid\"i\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"sendPossiblePort\"I\"sendPossibleSource\"@\"NSObject<OS_dispatch_source>\"\"replySendPossibleSource\"@\"NSObject<OS_dispatch_source>\"\"sendPossible\"i\"propertySet\"^{__CFSet}\"caller\"^{__CFString}\"procName\"^{__CFString}\"uuid\"^{__CFString}\"uuidStr\"*\"type\"i\"attributes\"^{__CFDictionary}\"task_name_port\"I\"audit_token\"{?=\"val\"[8I]}\"lock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"entitlements\"^(IOHIDEventSystemConnectionEntitlements)\"connectionEntitlements\"@\"NSObject<OS_xpc_object>\"\"disableProtectedServices\"i\"filterPriority\"i\"state\"I\"notificationsLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"virtualServices\"^{__CFDictionary}\"eventFilterMask\"Q\"eventFilteredCount\"I\"eventFilterTimeoutCount\"I\"droppedEventCount\"I\"currentDroppedEventCount\"I\"droppedEventTypeMask\"Q\"eventCount\"I\"eventMask\"Q\"lastDroppedEventTime\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"firstDroppedEventTime\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"maxEventLatency\"Q\"droppedEventStatus\"i\"propertyChangeNotificationHandlingTime\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^I\"activityState\"I\"activityStateChangeCount\"I\"idleNotificationTime\"Q\"activityDispatchSource\"@\"NSObject<OS_dispatch_source>\"\"activityNotification\"^{__IOHIDNotification}\"activityLog\"^{__CFData}\"filter\"^{__IOHIDConnectionFilter}\"serverDied\"i}"

```
