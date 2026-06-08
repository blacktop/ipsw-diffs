## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-100231.120.3.0.0
-  __TEXT.__text: 0xa27f4
-  __TEXT.__auth_stubs: 0x2130
+100284.0.0.0.0
+  __TEXT.__text: 0xa2680
   __TEXT.__objc_methlist: 0x150
-  __TEXT.__const: 0x104a4
-  __TEXT.__oslogstring: 0x5302
-  __TEXT.__cstring: 0xbca3
-  __TEXT.__unwind_info: 0x21b0
-  __TEXT.__objc_classname: 0x58
-  __TEXT.__objc_methname: 0xa3
-  __TEXT.__objc_methtype: 0x1ad5
-  __TEXT.__objc_stubs: 0x60
-  __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x2b38
+  __TEXT.__const: 0x104bc
+  __TEXT.__oslogstring: 0x5630
+  __TEXT.__cstring: 0xbd59
+  __TEXT.__unwind_info: 0x22b8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2c88
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x10a0
-  __AUTH_CONST.__const: 0x1df0
-  __AUTH_CONST.__cfstring: 0x74a0
+  __DATA_CONST.__got: 0x1e0
+  __AUTH_CONST.__const: 0x1e30
+  __AUTH_CONST.__cfstring: 0x75a0
   __AUTH_CONST.__objc_const: 0x508
+  __AUTH_CONST.__auth_got: 0x10b0
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x78
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x5a8
-  __DATA.__bss: 0x4b0
+  __DATA.__bss: 0x4b8
   __DATA.__common: 0x100
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0xc8
-  __DATA_DIRTY.__bss: 0x248
+  __DATA_DIRTY.__bss: 0x240
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 344F785E-9EDC-3B54-93FA-B14072F0FC64
-  Functions: 3533
-  Symbols:   6841
-  CStrings:  3515
+  UUID: C259E25E-0C4F-31BE-92EF-8B76E6DAAEF9
+  Functions: 3568
+  Symbols:   6862
+  CStrings:  3519
 
Symbols:
+ _CFPropertyListWrite
+ _IOHIDEventCreateMotionActivityEvent
+ _IOHIDEventGetDoubleMultiple
+ _IOHIDEventGetDoubleMultipleWithOptions
+ _IOPSSetBatteryDateOfFirstUseCommon
+ _IOPSSetBatteryDateOfFirstUseCommon.cold.1
+ _IOPSSetBatteryDateOfFirstUseCommon.cold.2
+ _IOPSSetBatteryDateOfFirstUseWithPackDetails
+ _IOPSShippingChargeLimitEnable
+ _IOPSShippingChargeLimitEnable.cold.1
+ _IOPSShippingChargeLimitEnable.cold.2
+ _IOPSShippingChargeLimitEnable.cold.3
+ _IOPSShippingChargeLimitEnable.cold.4
+ _IOPSShippingChargeLimitEnable.cold.5
+ _IOPSShippingChargeLimitGetState
+ _IOPSShippingChargeLimitGetState.cold.1
+ _IOPSShippingChargeLimitGetState.cold.2
+ _IOPSShippingChargeLimitGetState.cold.3
+ _IOPSShippingChargeLimitGetState.cold.4
+ _IOPSShippingChargeLimitGetState.cold.5
+ _IOPSShippingChargeLimitGetState.cold.6
+ _IOPSShippingChargeLimitGetState.cold.7
+ _IOServiceGetWaitInfo
+ ___IOHIDEventSystemClientCacheMatchingServices.cold.1
+ ___IOHIDEventSystemClientSetupAsyncSupport.cold.1
+ ___IOHIDEventSystemClientSetupAsyncSupport.cold.2
+ ___IOHIDEventSystemClientSetupAsyncSupport.cold.3
+ ___IOHIDEventSystemClientSetupAsyncSupport.cold.4
+ ___IOHIDEventSystemClientSetupAsyncSupport.cold.5
+ ___IOHIDServiceFilterCreateWithClass_block_invoke.cold.1
+ ___IOHIDServiceInit.cold.8
+ ___IOHIDSessionCopyEvent_block_invoke
+ ___IOHIDSessionCopyEvent_block_invoke.42
+ ___IOHIDSessionCopyEvent_block_invoke.42.cold.1
+ ___IOHIDSessionCopyEvent_block_invoke.42.cold.2
+ ___IOHIDSessionCopyEvent_block_invoke.43
+ ___IOPSSetBatteryDateOfFirstUseCommon_block_invoke
+ ___IOPSSetBatteryDateOfFirstUseCommon_block_invoke.cold.1
+ ___IOPSSetBatteryDateOfFirstUseWithPackDetails_block_invoke
+ ___IOPSSetBatteryDateOfFirstUseWithPackDetails_block_invoke.cold.1
+ ___IOPSShippingChargeLimitEnable_block_invoke
+ ___IOPSShippingChargeLimitEnable_block_invoke.61
+ ___IOPSShippingChargeLimitEnable_block_invoke.61.cold.1
+ ___IOPSShippingChargeLimitEnable_block_invoke.61.cold.2
+ ___IOPSShippingChargeLimitEnable_block_invoke.61.cold.3
+ ___IOPSShippingChargeLimitEnable_block_invoke.61.cold.4
+ ___IOPSShippingChargeLimitEnable_block_invoke.cold.1
+ ___IOPSShippingChargeLimitGetState_block_invoke
+ ___IOPSShippingChargeLimitGetState_block_invoke.cold.1
+ ____IOHIDServiceMatchPropertyTable_block_invoke
+ _____IOHIDServiceInit_block_invoke.211
+ ___block_descriptor_tmp.128
+ ___block_descriptor_tmp.138
+ ___block_descriptor_tmp.194
+ ___block_descriptor_tmp.195
+ ___block_descriptor_tmp.202
+ ___block_descriptor_tmp.203
+ ___block_descriptor_tmp.207
+ ___block_descriptor_tmp.208
+ ___block_descriptor_tmp.212
+ ___block_descriptor_tmp.242
+ ___block_descriptor_tmp.252
+ ___block_descriptor_tmp.294
+ ___block_descriptor_tmp.297
+ ___block_descriptor_tmp.298
+ ___block_descriptor_tmp.300
+ ___block_descriptor_tmp.305
+ ___block_descriptor_tmp.46
+ ___block_descriptor_tmp.69
+ ___block_descriptor_tmp.70
+ ___block_descriptor_tmp.78
+ ___block_descriptor_tmp.84
+ ___block_literal_global.104
+ ___block_literal_global.107
+ ___block_literal_global.130
+ ___block_literal_global.135
+ ___block_literal_global.140
+ ___block_literal_global.296
+ ___block_literal_global.72
+ ___block_literal_global.80
+ ___block_literal_global.86
+ _dispatch_queue_attr_make_with_qos_class
+ _io_service_get_wait_info
- _IOHIDEventCreateMotionActivtyEvent
- _IOPSSetBatteryDateOfFirstUse.cold.1
- _IOPSSetBatteryDateOfFirstUse.cold.2
- _OUTLINED_FUNCTION_25
- _OUTLINED_FUNCTION_26
- _OUTLINED_FUNCTION_27
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- __IOHIDCreateBinaryData.cold.1
- ___CopyEventForObjectFunction
- ___CopyEventForObjectFunction.cold.1
- ___CopyEventForObjectFunction.cold.2
- ___FilterFunctionCopyEvent
- ___FilterFunctionFilterCopyEvent
- ___IOPSSetBatteryDateOfFirstUse_block_invoke.94
- ___IOPSSetBatteryDateOfFirstUse_block_invoke.cold.1
- ___block_descriptor_tmp.192
- ___block_descriptor_tmp.199
- ___block_descriptor_tmp.200
- ___block_descriptor_tmp.204
- ___block_descriptor_tmp.205
- ___block_descriptor_tmp.235
- ___block_descriptor_tmp.245
- ___block_descriptor_tmp.287
- ___block_descriptor_tmp.290
- ___block_descriptor_tmp.291
- ___block_descriptor_tmp.293
- ___block_descriptor_tmp.51
- ___block_descriptor_tmp.79
- ___block_descriptor_tmp.82
- ___block_descriptor_tmp.90
- ___block_literal_global.101
- ___block_literal_global.106
- ___block_literal_global.289
- ___block_literal_global.63
- ___block_literal_global.81
- ___block_literal_global.84
- ___block_literal_global.92
CStrings:
+ "0x%llx: __IOHIDServiceInit creating queue with high-priority QOS"
+ "AppleSmartBattery"
+ "BatteryPacks"
+ "Began"
+ "Enabled flag not found\n"
+ "Failed to convert XPC to CF object\n"
+ "Failed to create ASBM services\n"
+ "Failed to create CF properties: 0x%x\n"
+ "Failed to create XPC connection\n"
+ "Failed to create XPC connection to PowerD\n"
+ "Failed to create XPC message\n"
+ "Failed to get PM queue\n"
+ "HIDPropertiesRequiredForMatching"
+ "IOHIDServiceFilter cancel handler invoked more than once for filter:%@"
+ "Invalid reply from PowerD\n"
+ "Invalid reply type\n"
+ "Missing key '%s'\n"
+ "Missing state in reply\n"
+ "OSKEXT_BUILD_DATE 09:48:24 May 24 2026"
+ "PackID"
+ "PowerD error: 0x%x\n"
+ "Session Filter:%@ filtered copy event (service:0x%llx, type:%d)"
+ "Session Filter:%@ filtered copy event (service:0x%llx, type:%d, new type:%d)"
+ "ShipChargeLimitData"
+ "ShipChargeLimitEnabled"
+ "Shipping charge limit data not found\n"
+ "XPC event handler: %@\n"
+ "XPC event: %@\n"
+ "_IOHIDCreateBinaryData: %@"
+ "assertion failure: \"client->notifyPort\" -> %llu"
+ "assertion failure: \"client->queuePort\" -> %llu"
+ "assertion failure: \"queuePort\" -> %llu"
+ "batteryShippingChargeLimit"
+ "batteryShippingChargeLimitAction"
+ "batteryShippingChargeLimitEnable"
+ "batteryShippingChargeLimitState"
+ "invalid matching dictionary: %@"
+ "qos"
- "@16@0:8"
- "@40@0:8Q16I24Q28I36"
- "B24@0:8@16"
- "ColorComponent0:"
- "ColorComponent1:"
- "ColorComponent2:"
- "ColorSpace:"
- "Filter Copy Event filtered type:%d service:0x%llx session filter:%@"
- "HIDConnection"
- "HIDDevice"
- "HIDElement"
- "HIDEvent"
- "HIDEventService"
- "HIDServiceClient"
- "HIDSession"
- "OSKEXT_BUILD_DATE 16:11:41 Apr 18 2026"
- "Q16@0:8"
- "Unable to serialize CFObject: %@"
- "XYZ"
- "_cfTypeID"
- "_client"
- "_connection"
- "_device"
- "_element"
- "_event"
- "_service"
- "_session"
- "allocWithZone:"
- "dealloc"
- "hash"
- "init"
- "initWithSize:type:timestamp:options:"
- "isEqual:"
- "v16@0:8"
- "{?=\"client\"^{__IOHIDEventSystem}\"callback\"^?\"refCon\"^v\"queueContext\"^{__IOHIDSessionQueueContext}\"stateCondition\"{_opaque_pthread_cond_t=\"__sig\"q\"__opaque\"[40c]}\"state\"i\"stateBusy\"i\"eventDispatchQueueSession\"@\"NSObject<OS_dispatch_queue>\"\"eventDispatchSource\"@\"NSObject<OS_dispatch_source>\"\"eventDipsatchPending\"^{__CFArray}\"properties\"^{__CFDictionary}\"logLevel\"I\"serviceSet\"^{__CFSet}\"simpleSessionFilters\"^{__CFArray}\"sessionFilters\"^{__CFArray}\"pendingSessionFilters\"^{__CFArray}\"activityLastTimestamp\"Q\"activityLastTime\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"activityNotificationSet\"^{__CFSet}}"
- "{?=\"deviceInterface\"^^{IOHIDDeviceDeviceInterface}\"device\"^{__IOHIDDevice}\"value\"^{__IOHIDValue}\"elementStructPtr\"^{IOHIDElementStruct}\"index\"I\"data\"^{__CFData}\"attachedElements\"^{__CFArray}\"childElements\"^{__CFArray}\"parentElement\"^{__IOHIDElement}\"originalElement\"^{__IOHIDElement}\"calibrationPtr\"^{_IOHIDCalibrationStruct}\"properties\"^{__CFDictionary}\"rootKey\"^{__CFString}\"isDirty\"C}"
- "{?=\"service\"I\"regID\"Q\"deviceInterface\"^^{IOHIDDeviceDeviceInterface}\"deviceTimeStampedInterface\"^^{IOHIDDeviceTimeStampedDeviceInterface}\"plugInInterface\"^^{IOCFPlugInInterfaceStruct}\"deviceLock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"properties\"^{__CFDictionary}\"elements\"^{__CFSet}\"rootKey\"^{__CFString}\"UUIDKey\"^{__CFString}\"notificationPort\"^{IONotificationPort}\"notification\"I\"asyncEventSource\"^{__CFRunLoopSource}\"sourceContext\"{?=\"version\"q\"info\"^v\"retain\"^?\"release\"^?\"copyDescription\"^?\"equal\"^?\"hash\"^?\"getPort\"^?\"perform\"^?}\"queuePort\"^{__CFMachPort}\"runLoop\"^{__CFRunLoop}\"runLoopMode\"^{__CFString}\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"dispatchMach\"@\"NSObject<OS_dispatch_mach>\"\"dispatchStateMask\"AI\"cancelHandler\"@?\"queue\"^{__IOHIDQueue}\"inputMatchingMultiple\"^{__CFArray}\"loadProperties\"C\"isDirty\"C\"transaction\"^v\"callbackLock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"reportBuffer\"^{__CFData}\"batchElements\"^{__CFArray}\"removalCallbackSet\"^{__CFSet}\"inputReportCallbackSet\"^{__CFSet}\"inputValueCallbackSet\"^{__CFSet}\"asyncCommitCallbacks\"^{__CFDictionary}\"asyncElementCallbacks\"^{__CFDictionary}\"asyncReportCallbacks\"^{__CFDictionary}\"elementHandler\"A^v\"removalHandler\"A^v\"inputReportHandler\"A^v\"propertyNotificationHandler\"A^v\"propertyNotificationKeys\"^{__CFArray}\"previousPropertyValues\"^{__CFDictionary}\"propertyPort\"^{IONotificationPort}\"propertyNotify\"I}"
- "{?=\"session\"^{__IOHIDSession}\"service\"I\"serviceInterface\"^^{IOHIDServiceInterface}\"serviceInterface2\"^^{IOHIDServiceInterface2}\"plugInInterface\"^^{IOCFPlugInInterfaceStruct}\"registryID\"^{__CFNumber}\"locationID\"^v\"entitlements\"^{__CFArray}\"queueContext\"^{__IOHIDServiceQueueContext}\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"notificationPort\"^{IONotificationPort}\"notification\"I\"removalNotificationSet\"^{__CFSet}\"propertyNotificationSet\"^{__CFSet}\"requestTerminationNotificationSet\"^{__CFSet}\"eventTarget\"^v\"eventRefcon\"^v\"eventCallback\"^?\"lastLEDMask\"I\"lastButtonMask\"I\"currentReportInterval\"I\"currentBatchInterval\"I\"defaultReportInterval\"I\"defaultBatchInterval\"I\"primaryUsagePage\"I\"primaryUsage\"I\"transport\"[32c]\"queueSize\"I\"containsReportInterval\"i\"state\"I\"eventCount\"I\"eventMask\"Q\"clientCacheDict\"^{__CFDictionary}\"simpleFilters\"^{__CFArray}\"filters\"^{__CFArray}\"keyboardEventInProgress\"^{__CFSet}\"nullEventMask\"Q\"displayIntegratedDigitizer\"i\"builtIn\"i\"inMomentumPhase\"i\"inDigitizerPhase\"i\"sensorControlOptions\"C\"hidden\"i\"registered\"i\"protectedAccess\"i\"propertyCache\"^{__CFDictionary}\"propertyCacheHit\"I\"propertyCacheMiss\"I\"activityLastTimestamp\"Q\"virtualService\"{?=\"connection\"^v\"target\"^v\"refcon\"^v\"callbacks\"^{IOHIDServiceVirtualCallbacksV2}}\"connections\"^^v\"propertySetTime\"Q\"propertyGetTime\"Q\"elementSetTime\"Q\"regID\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^Q\"pluginCancelHandler\"@?\"filterCancelHandler\"@?\"pendingPluginCancel\"B\"pendingFilterCancels\"I\"cancelTimer\"@\"NSObject<OS_dispatch_source>\"\"dataLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"hidAnalyticsEvent\"^v\"hidAnalyticsDispatchEvent\"^v\"objc\"{?=\"interface\"^v\"name\"^{__CFString}\"getProperty\":\"setProperty\":\"eventMatching\":\"setEventDispatcher\":\"setCancelHandler\":\"activate\":\"cancel\":\"setDispatchQueue\":\"clientNotification\":\"copyEvent\":\"setOutputEvent\":\"setHIDEventService\":}}"
- "{?=\"system\"^{__IOHIDEventSystemClient}\"serviceID\"^v\"callbackLock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"removal\"{?=\"callback\"^?\"block\"@?\"target\"^v\"refcon\"^v}\"virtualService\"{?=\"callbacks\"^{__IOHIDVirtualServiceClientCallbacksV2}\"target\"^v\"refcon\"^v}\"serviceLock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"cachedProperties\"^{__CFDictionary}\"fastPathInterface\"^^{IOHIDServiceFastPathInterface}\"plugInInterface\"^^{IOCFPlugInInterfaceStruct}\"removalHandler\"^v\"primaryUsagePage\"I\"primaryUsage\"I\"usagePairs\"^{_IOHIDServiceClientUsagePair}\"usagePairsCount\"I}"
- "{?=\"system\"^{__IOHIDEventSystem}\"notifications\"^{__CFDictionary}\"queue\"^{__IOHIDEventQueue}\"port\"^{__IOMIGMachPort}\"reply_port\"I\"demuxCallback\"^?\"demuxRefcon\"^v\"terminationCallback\"^?\"terminationRefcon\"^v\"services\"^{__CFSet}\"pid\"i\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"sendPossiblePort\"I\"sendPossibleSource\"@\"NSObject<OS_dispatch_source>\"\"replySendPossibleSource\"@\"NSObject<OS_dispatch_source>\"\"sendPossible\"i\"propertySet\"^{__CFSet}\"caller\"^{__CFString}\"procName\"^{__CFString}\"uuid\"^{__CFString}\"uuidStr\"*\"type\"i\"attributes\"^{__CFDictionary}\"task_name_port\"I\"audit_token\"{?=\"val\"[8I]}\"lock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"entitlements\"^(IOHIDEventSystemConnectionEntitlements)\"connectionEntitlements\"@\"NSObject<OS_xpc_object>\"\"disableProtectedServices\"i\"filterPriority\"i\"state\"I\"notificationsLock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}\"virtualServices\"^{__CFDictionary}\"eventFilterMask\"Q\"eventFilteredCount\"I\"eventFilterTimeoutCount\"I\"droppedEventCount\"I\"currentDroppedEventCount\"I\"droppedEventTypeMask\"Q\"eventCount\"I\"eventMask\"Q\"lastDroppedEventTime\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"firstDroppedEventTime\"{timeval=\"tv_sec\"q\"tv_usec\"i}\"maxEventLatency\"Q\"droppedEventStatus\"i\"propertyChangeNotificationHandlingTime\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^I\"activityState\"I\"activityStateChangeCount\"I\"idleNotificationTime\"Q\"activityDispatchSource\"@\"NSObject<OS_dispatch_source>\"\"activityNotification\"^{__IOHIDNotification}\"activityLog\"^{__CFData}\"filter\"^{__IOHIDConnectionFilter}\"serverDied\"i}"
- "{?=\"timeStamp\"Q\"senderID\"Q\"typeMask\"Q\"options\"I\"attributeData\"*\"context\"^v\"attachments\"^{__CFDictionary}\"sender\"^v\"children\"^{__CFArray}\"parent\"^{__IOHIDEvent}\"attributeDataLength\"q\"eventData\"^{IOHIDEventData}}"

```
