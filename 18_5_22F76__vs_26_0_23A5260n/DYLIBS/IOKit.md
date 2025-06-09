## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-100150.120.2.0.0
-  __TEXT.__text: 0x9d9d4
-  __TEXT.__auth_stubs: 0x2050
+100222.0.0.0.0
+  __TEXT.__text: 0xa4f08
+  __TEXT.__auth_stubs: 0x2120
   __TEXT.__objc_methlist: 0x150
-  __TEXT.__const: 0x104a4
-  __TEXT.__oslogstring: 0x4b64
-  __TEXT.__cstring: 0xb6fb
-  __TEXT.__unwind_info: 0x1f90
+  __TEXT.__const: 0x104cc
+  __TEXT.__oslogstring: 0x52bd
+  __TEXT.__cstring: 0xbb21
+  __TEXT.__unwind_info: 0x2088
   __TEXT.__objc_classname: 0x58
   __TEXT.__objc_methname: 0xa3
-  __TEXT.__objc_methtype: 0x19b4
+  __TEXT.__objc_methtype: 0x19bc
   __TEXT.__objc_stubs: 0x60
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x2790
+  __DATA_CONST.__const: 0x2a68
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x1030
-  __AUTH_CONST.__const: 0x1c28
-  __AUTH_CONST.__cfstring: 0x7240
+  __AUTH_CONST.__auth_got: 0x1098
+  __AUTH_CONST.__const: 0x1df0
+  __AUTH_CONST.__cfstring: 0x73e0
   __AUTH_CONST.__objc_const: 0x508
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x588
-  __DATA.__bss: 0x490
+  __DATA.__data: 0x590
+  __DATA.__bss: 0x4a8
   __DATA.__common: 0x100
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0xd0
-  __DATA_DIRTY.__bss: 0x248
+  __DATA_DIRTY.__data: 0xe8
+  __DATA_DIRTY.__bss: 0x260
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9FE4D49C-A09B-3D14-BC98-D8E9CA6166E1
-  Functions: 3320
-  Symbols:   6339
-  CStrings:  3395
+  UUID: CD1AB08A-0482-31AD-BF21-F00E49F9E5CD
+  Functions: 3460
+  Symbols:   6653
+  CStrings:  3489
 
Symbols:
+ _CFAllocatorAllocateTyped
+ _CFAllocatorReallocateTyped
+ _CFLocaleCopyCurrent
+ _CFNumberFormatterCreate
+ _CFNumberFormatterCreateStringWithNumber
+ _IOAVDisplayMemoryRead64
+ _IOAVDisplayMemoryWrite64
+ _IOCircularDataQueueCopyCurrent
+ _IOCircularDataQueueCopyLatest
+ _IOCircularDataQueueCopyNext
+ _IOCircularDataQueueCopyPrevious
+ _IOCircularDataQueueCreateWithConnection
+ _IOCircularDataQueueCreateWithConnection.cold.1
+ _IOCircularDataQueueCreateWithConnection.cold.2
+ _IOCircularDataQueueDestroy
+ _IOCircularDataQueueEnqueue
+ _IOCircularDataQueueGetCurrent
+ _IOCircularDataQueueGetLatest
+ _IOCircularDataQueueGetNext
+ _IOCircularDataQueueGetPrevious
+ _IOCircularDataQueueIsCurrentDataValid
+ _IOCircularDataQueueSetCursorLatest
+ _IOCreatePlugInInterfaceForService.cold.1
+ _IOCreatePlugInInterfaceForService.cold.10
+ _IOCreatePlugInInterfaceForService.cold.11
+ _IOCreatePlugInInterfaceForService.cold.12
+ _IOCreatePlugInInterfaceForService.cold.13
+ _IOCreatePlugInInterfaceForService.cold.14
+ _IOCreatePlugInInterfaceForService.cold.15
+ _IOCreatePlugInInterfaceForService.cold.16
+ _IOCreatePlugInInterfaceForService.cold.17
+ _IOCreatePlugInInterfaceForService.cold.18
+ _IOCreatePlugInInterfaceForService.cold.19
+ _IOCreatePlugInInterfaceForService.cold.2
+ _IOCreatePlugInInterfaceForService.cold.20
+ _IOCreatePlugInInterfaceForService.cold.21
+ _IOCreatePlugInInterfaceForService.cold.22
+ _IOCreatePlugInInterfaceForService.cold.23
+ _IOCreatePlugInInterfaceForService.cold.24
+ _IOCreatePlugInInterfaceForService.cold.25
+ _IOCreatePlugInInterfaceForService.cold.26
+ _IOCreatePlugInInterfaceForService.cold.3
+ _IOCreatePlugInInterfaceForService.cold.4
+ _IOCreatePlugInInterfaceForService.cold.5
+ _IOCreatePlugInInterfaceForService.cold.6
+ _IOCreatePlugInInterfaceForService.cold.7
+ _IOCreatePlugInInterfaceForService.cold.8
+ _IOCreatePlugInInterfaceForService.cold.9
+ _IODPHDMIControllerGetPCONStatus
+ _IODPHDMIControllerPortCreate
+ _IODPHDMIControllerPortCreateWithService
+ _IODPHDMIControllerPortDisablePCON
+ _IODPHDMIControllerPortEnablePCON
+ _IODPHDMIControllerPortGetAddress
+ _IODPHDMIControllerPortGetTypeID
+ _IODPHDMIControllerPortSetHDMIHPD
+ _IODPHDMIControllerPortSetPortEnable
+ _IODPPortCreate
+ _IODPPortCreateWithService
+ _IODPPortGetAVRoot
+ _IODPPortGetAddress
+ _IODPPortGetTypeID
+ _IODPPortGetVirtual
+ _IODPPortSetPortEvent
+ _IODPPortSetVirtual
+ _IODPPortSetVirtualDPCD
+ _IODPPortSetVirtualEDID
+ _IOHIDEventCreateArrayOfEventsWithType
+ _IOHIDEventCreateCollectionEventWithUsage
+ _IOHIDEventCreateHeartRateEvent
+ _IOHIDEventGetDataLengthInternal
+ _IOHIDEventNeedsUngroupForLegacy
+ _IOHIDServiceFilterFilterEventForClient
+ _IOHIDServiceFilterFilterSetPropertyForClient
+ _IOHIDServiceWorkIntervalCancel
+ _IOHIDServiceWorkIntervalFinish
+ _IOHIDServiceWorkIntervalStart
+ _IOHIDServiceWorkIntervalUpdate
+ _IOPMSetGamingEnergyModePreference
+ _IOPMSetGamingEnergyModePreference.cold.1
+ _IOPSCopyChargeStatus
+ _IOPSCopyChargeStatus.cold.1
+ _IOPSCopyChargeStatus.cold.2
+ __IOHIDEventSystemClientUngroupAndDispatchEventFilter
+ __IOHIDServiceSetPropertyForClient.cold.5
+ __IOHIDServiceSetPropertyForClient.cold.6
+ __IOHIDServiceSetPropertyForClient.cold.7
+ __IOHIDServiceSetPropertyForClient.cold.8
+ ___IOCFPlugInLog
+ ___IOCFPlugInLog.cold.1
+ ___IOCFPlugInLog.log
+ ___IOCFPlugInLog.onceToken
+ ___IODPCopyFirstMatchingPort
+ ___IODPHDMIControllerPortClass
+ ___IODPHDMIControllerPortFree
+ ___IODPHDMIControllerPortRegister
+ ___IODPPortClass
+ ___IODPPortFree
+ ___IODPPortMatching
+ ___IODPPortRegister
+ ___IOHIDEventCreateArrayOfEventsWithType_block_invoke
+ ___IOHIDEventGetLength
+ ___IOHIDEventPopulateDigitizerCurrentData
+ ___IOHIDEventPopulateDigitizerLegacyData
+ ___IOHIDEventPopulatePointerCurrentData
+ ___IOHIDEventPopulatePointerLegacyData
+ ___IOHIDEventPopulateTranslationCurrentData
+ ___IOHIDEventPopulateTranslationLegacyData
+ ___IOHIDEventSetSenderID_block_invoke
+ ___IOHIDEventTypeDescriptorCollection
+ ___IOHIDEventTypeDescriptorHeartRateEvent
+ ___IOHIDServiceFilterEventForClient
+ ___IOHIDServiceFilterEventForClient.cold.1
+ ___IOHIDServiceFilterEventForClient.cold.2
+ ___IOHIDServiceInit.cold.7
+ ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.229
+ ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.229.cold.1
+ ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.229.cold.2
+ ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.229.cold.3
+ ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.229.cold.4
+ ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.229.cold.5
+ ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.229.cold.6
+ ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.232
+ ___IOPMSetGamingEnergyModePreference_block_invoke
+ ___IOPSCopyChargeStatus_block_invoke
+ ___IOPSCopyChargeStatus_block_invoke.cold.1
+ ___IOPSSetBatteryDateOfFirstUse_block_invoke.94
+ ____IOHIDEventSystemClientUngroupAndDispatchEventFilter_block_invoke
+ ____IOHIDEventSystemClientUngroupAndDispatchEventFilter_block_invoke_2
+ ____IOHIDServiceSetPropertyForClient_block_invoke
+ ____IOHIDServiceUnscheduleAsync_block_invoke.91
+ ____IOHIDServiceUnscheduleAsync_block_invoke.91.cold.1
+ ____IOHIDServiceUnscheduleAsync_block_invoke.93
+ ____IOHIDServiceUnscheduleAsync_block_invoke.93.cold.1
+ _____IOCFPlugInLog_block_invoke
+ _____IOHIDEventSystemClientQueueCallback_block_invoke
+ _____IOHIDEventSystemFilterEvent_block_invoke
+ _____IOHIDEventSystemFilterEvent_block_invoke_2
+ _____IOHIDEventSystemInvalidateServiceRemovalNotifications_block_invoke
+ _____IOHIDEventSystemInvalidateServiceRemovalNotifications_block_invoke_2
+ _____IOHIDServiceEventCallback_block_invoke
+ _____IOHIDServiceFilterEventForClient_block_invoke
+ _____IOHIDServiceLoadServiceFilterBundles_block_invoke
+ ___block_descriptor_tmp.104
+ ___block_descriptor_tmp.108
+ ___block_descriptor_tmp.112
+ ___block_descriptor_tmp.120
+ ___block_descriptor_tmp.127
+ ___block_descriptor_tmp.130
+ ___block_descriptor_tmp.137
+ ___block_descriptor_tmp.165
+ ___block_descriptor_tmp.188
+ ___block_descriptor_tmp.193
+ ___block_descriptor_tmp.194
+ ___block_descriptor_tmp.198
+ ___block_descriptor_tmp.199
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.201
+ ___block_descriptor_tmp.224
+ ___block_descriptor_tmp.229
+ ___block_descriptor_tmp.233
+ ___block_descriptor_tmp.234
+ ___block_descriptor_tmp.236
+ ___block_descriptor_tmp.239
+ ___block_descriptor_tmp.247
+ ___block_descriptor_tmp.281
+ ___block_descriptor_tmp.284
+ ___block_descriptor_tmp.285
+ ___block_descriptor_tmp.287
+ ___block_descriptor_tmp.41
+ ___block_descriptor_tmp.49
+ ___block_descriptor_tmp.58
+ ___block_descriptor_tmp.59
+ ___block_descriptor_tmp.60
+ ___block_descriptor_tmp.63
+ ___block_descriptor_tmp.65
+ ___block_descriptor_tmp.66
+ ___block_descriptor_tmp.82
+ ___block_descriptor_tmp.90
+ ___block_descriptor_tmp.92
+ ___block_descriptor_tmp.94
+ ___block_descriptor_tmp.97
+ ___block_descriptor_tmp.99
+ ___block_literal_global.101
+ ___block_literal_global.106
+ ___block_literal_global.114
+ ___block_literal_global.129
+ ___block_literal_global.136
+ ___block_literal_global.139
+ ___block_literal_global.190
+ ___block_literal_global.203
+ ___block_literal_global.212
+ ___block_literal_global.226
+ ___block_literal_global.249
+ ___block_literal_global.283
+ ___block_literal_global.43
+ ___block_literal_global.46
+ ___block_literal_global.51
+ ___block_literal_global.55
+ ___block_literal_global.84
+ ___block_literal_global.92
+ ___block_literal_global.94
+ ___fetchAssertionCategoryPolicies_block_invoke
+ ___fetchAssertionCategoryPolicies_block_invoke.48
+ ___fetchAssertionCategoryPolicies_block_invoke.48.cold.1
+ ___fetchAssertionCategoryPolicies_block_invoke.48.cold.2
+ ___fetchAssertionCategoryPolicies_block_invoke.cold.1
+ ___fetchAssertionCategoryPolicies_block_invoke.cold.2
+ ___initialSetup_block_invoke_3
+ ___kIODPHDMIControllerPortTypeID
+ ___kIODPPortTypeID
+ ___portTypeInit
+ ___registerForAssertionPolicy_block_invoke
+ __getCurrentInQueueMemInternal
+ __getLatestInQueueMemInternal
+ __getNextInQueueMemInternal
+ __getPrevInQueueMemInternal
+ __get_cpu_capabilities
+ _activateAsyncAssertion.cold.3
+ _activateAsyncAssertion.cold.4
+ _activateAsyncAssertion.cold.5
+ _activateAsyncAssertion.cold.6
+ _activateAsyncAssertion.cold.7
+ _activateAsyncAssertion.cold.8
+ _convertCFNumberToCFStringRef
+ _dispatch_workloop_set_os_workgroup
+ _evaluateAssertionCategoryPolicies
+ _evaluateAssertionCategoryPolicies.cold.1
+ _fetchAssertionCategoryPolicies
+ _fetchAssertionCategoryPolicies.cold.1
+ _fetchAssertionCategoryPolicies.cold.2
+ _fetchAssertionCategoryPolicies.cold.3
+ _fetchAssertionCategoryPolicies.onceToken
+ _gAssertionCategoryPolicies
+ _gAssertionPolicyActive
+ _getPolicyTimeout
+ _getPortProperty
+ _getTimeoutForAssertionCategory
+ _getTimeoutForAssertionCategory.cold.1
+ _getTimeoutForAssertionCategory.cold.2
+ _getTimeoutForAssertionCategory.cold.3
+ _getTimeoutForAssertionCategory.cold.4
+ _io_connect_map_shared_memory
+ _kIOHIDServiceWorkgroupInterval
+ _os_log_is_debug_enabled
+ _os_workgroup_attr_set_interval_type
+ _os_workgroup_interval_create_with_workload_id
+ _os_workgroup_interval_data_set_complexity
+ _os_workgroup_interval_finish
+ _os_workgroup_interval_start
+ _os_workgroup_interval_update
+ _printf
+ _registerForAssertionPolicy
+ _undoCategoryPolicyTimers
+ _undoCategoryPolicyTimers.cold.1
- _CFAllocatorAllocate
- _CFAllocatorReallocate
- __IOHIDServiceSupportReportLatency
- ___IOHIDEventGetLengthAndCount
- ___IOHIDEventSystemFilterEventFunction
- ___IOHIDEventSystemIsTimeToDispatchEvent
- ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.205
- ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.205.cold.1
- ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.205.cold.2
- ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.205.cold.3
- ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.205.cold.4
- ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.205.cold.5
- ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.205.cold.6
- ___IOPMCopyAssertionActivityUpdateWithCallback_block_invoke.208
- ___IOPSSetBatteryDateOfFirstUse_block_invoke.83
- ____IOHIDServiceUnscheduleAsync_block_invoke.90
- ____IOHIDServiceUnscheduleAsync_block_invoke.90.cold.1
- ____IOHIDServiceUnscheduleAsync_block_invoke.92
- ____IOHIDServiceUnscheduleAsync_block_invoke.92.cold.1
- ___block_descriptor_tmp.110
- ___block_descriptor_tmp.113
- ___block_descriptor_tmp.124
- ___block_descriptor_tmp.128
- ___block_descriptor_tmp.164
- ___block_descriptor_tmp.184
- ___block_descriptor_tmp.192
- ___block_descriptor_tmp.197
- ___block_descriptor_tmp.200
- ___block_descriptor_tmp.209
- ___block_descriptor_tmp.212
- ___block_descriptor_tmp.223
- ___block_descriptor_tmp.230
- ___block_descriptor_tmp.271
- ___block_descriptor_tmp.272
- ___block_descriptor_tmp.274
- ___block_descriptor_tmp.54
- ___block_descriptor_tmp.69
- ___block_descriptor_tmp.73
- ___block_descriptor_tmp.76
- ___block_descriptor_tmp.80
- ___block_descriptor_tmp.83
- ___block_descriptor_tmp.91
- ___block_literal_global.105
- ___block_literal_global.112
- ___block_literal_global.115
- ___block_literal_global.166
- ___block_literal_global.202
- ___block_literal_global.225
- ___block_literal_global.78
- ___block_literal_global.90
CStrings:
+ "%s: Filtered event type:%@ sender:%#llx eventInfo:(%@) -> outEventInfo: (%@)"
+ "%x, %lx, 0x%llx, 0x%llx\n"
+ "0x%llx: os_workgroup_interval_finish error: %d, service %@"
+ "0x%llx: os_workgroup_interval_finish(cancel) error: %d, service %@"
+ "0x%llx: os_workgroup_interval_start error: %d, service %@"
+ "Assertion has a category %@"
+ "Assertion has a policy category timestamp %@"
+ "CFPlugInCreate failed for url %@ for %@"
+ "CFPlugInFindFactoriesForPlugInTypeInPlugIn failed for plugin url %@ for %@"
+ "Category %@ has a policy %@"
+ "Category %@ not found"
+ "Checking for timeout for category %@ %d"
+ "Checking getTimeout for string %@"
+ "EventForClient filtered type:%d sender:0x%llx eventInfo:(%@) service filter:%@ for client:%@"
+ "EventToConnection filtered type:%d service:0x%llx connection:%@ session filter:%@"
+ "Failed to create event at index=%d eventCount=%d eventDataOffset=%d lenght=%ld"
+ "Failed to get %s for portType=%d, portNumber=%d, portVariant=%d\n"
+ "Filter Copy Event filtered type:%d service:0x%llx session filter:%@"
+ "FilterEvent filtered type:%d service:0x%llx eventInfo:(%@) session filter:%@"
+ "Found timeout %@ for category string %@"
+ "Generation:"
+ "HIDDefaultSensorControlOptions"
+ "HandFlick"
+ "HeartRate"
+ "IOCircularDataQueueCreateWithConnection"
+ "IOCircularDataQueueImplementation.h"
+ "IOCircularQueueDescription"
+ "IODPHDMIControllerPort"
+ "IODPPort"
+ "IOHIDService name:%s id:0x%llx primaryUsagePage:0x%x primaryUsage:0x%x transport:%s locationID:%@ reportInterval:%d batchInterval:%d events:%d mask:0x%llx sensorcontrols:%d"
+ "IOHIDServiceFilterFilterSetPropertyForClient %@  %@ -> %@ filter:%@"
+ "IOServiceMatchPropertyTable failed for url %@ for %@"
+ "Initial connection to powerd not setup"
+ "Left Headphone"
+ "Location:"
+ "Malformed PropertyMerge value in bundle: %@"
+ "No category"
+ "No plist for plugin url %@ for %@"
+ "No policies defined for this process"
+ "No timeout for category %@ for policy %@"
+ "No timeout ts. Remove from timed list"
+ "OSKEXT_BUILD_DATE 01:04:25 May 23 2025"
+ "PolicyTimeoutTimeStamp"
+ "PortNumber"
+ "PortType"
+ "PortVariant"
+ "PropertyMerge"
+ "Rate:"
+ "Received assertion category policies from powerd %@"
+ "Registering for assertion policy changes"
+ "Right Headphone"
+ "Setting assertion timeout to fire in %d msecs for timeout_ts %llu"
+ "Setting category timeout timestamp to %@, monotonic time %llu"
+ "SupportsCollectionEvents"
+ "SystemTimeOutExpired"
+ "Timeout from category %d"
+ "Timeout is less than 0 %d"
+ "Timeout: assertion id 0x%x with time %llu, policy timeout %llu"
+ "Ungroup for legacy clients"
+ "Update assertion policy %llu"
+ "Watch"
+ "assertionUpdateCategoryPolicy"
+ "batteryChargingIconoGraphy"
+ "batteryChargingIconoGraphyAction"
+ "batteryChargingIconoGraphyState"
+ "bundle invalid for pluginType %@"
+ "buttonState: %ld"
+ "chargeSocLimitIsEOC"
+ "com.apple.backboardd.hid"
+ "com.apple.iokit.cfplugin"
+ "com.apple.powerd.assertionpolicy"
+ "failed to create instance for plugin for %@"
+ "failed to get interface for plugin for %@"
+ "failed to open io_service_t err=0x%x"
+ "fetchAssertionCategoryPolicies: Reply is not a dict"
+ "filterEvent:forClient:"
+ "filterSetProperty:forKey:forClient:"
+ "gamingEnergyMode"
+ "hid-workgroup-interval"
+ "invalid io_service_t for %@"
+ "io_service_t has no IOCFPlugInTypes for %@"
+ "io_service_t has no plugin for %@"
+ "keyboardPress: %ld"
+ "no factories for plugin for %@, kr = 0x%x, factories = %p, factoryCount = %ld"
+ "onePlugin invalid for pluginType %@"
+ "plist invalid for pluginType %@"
+ "pluginPath == NULL, unable to allocate a CFString"
+ "probe failed for plugin for %@"
+ "queueHeaderShadow->allocMemSize == map_size"
+ "sentinel %qx\n"
+ "setHIDEventService:"
+ "sizeof(IOCircularDataQueueDescription) == inband_outputCnt"
+ "start failed (%s) for plugin for %@"
+ "there is a timeout for category %@ and policy %@"
+ "timeout"
+ "usagePage: %ld usage: %ld children: %ld ungroupForLegacy: %ld"
+ "vendorUsagePage: %ld vendorUsage:%ld dataLength:%ld"
+ "workgroup_interval_force_disable"
+ "workgroup_interval_force_enable"
+ "{?=\"session\"^{__IOHIDSession}\"service\"I\"serviceInterface\"^^{IOHIDServiceInterface}\"serviceInterface2\"^^{IOHIDServiceInterface2}\"plugInInterface\"^^{IOCFPlugInInterfaceStruct}\"registryID\"^{__CFNumber}\"locationID\"^v\"entitlements\"^{__CFArray}\"queueContext\"^{__IOHIDServiceQueueContext}\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"notificationPort\"^{IONotificationPort}\"notification\"I\"removalNotificationSet\"^{__CFSet}\"propertyNotificationSet\"^{__CFSet}\"requestTerminationNotificationSet\"^{__CFSet}\"eventTarget\"^v\"eventRefcon\"^v\"eventCallback\"^?\"lastLEDMask\"I\"lastButtonMask\"I\"currentReportInterval\"I\"currentBatchInterval\"I\"defaultReportInterval\"I\"defaultBatchInterval\"I\"primaryUsagePage\"I\"primaryUsage\"I\"transport\"[32c]\"queueSize\"I\"containsReportInterval\"i\"state\"I\"eventCount\"I\"eventMask\"Q\"clientCacheDict\"^{__CFDictionary}\"simpleFilters\"^{__CFArray}\"filters\"^{__CFArray}\"keyboardEventInProgress\"^{__CFSet}\"nullEventMask\"Q\"displayIntegratedDigitizer\"i\"builtIn\"i\"inMomentumPhase\"i\"inDigitizerPhase\"i\"sensorControlOptions\"C\"hidden\"i\"registered\"i\"protectedAccess\"i\"propertyCache\"^{__CFDictionary}\"propertyCacheHit\"I\"propertyCacheMiss\"I\"activityLastTimestamp\"Q\"virtualService\"{?=\"connection\"^v\"target\"^v\"refcon\"^v\"callbacks\"^{IOHIDServiceVirtualCallbacksV2}}\"connections\"^^v\"propertySetTime\"Q\"propertyGetTime\"Q\"elementSetTime\"Q\"regID\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^Q\"pluginCancelHandler\"@?\"filterCancelHandler\"@?\"pendingPluginCancel\"B\"pendingFilterCancels\"I\"cancelTimer\"@\"NSObject<OS_dispatch_source>\"\"dataLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"hidAnalyticsEvent\"^v\"hidAnalyticsDispatchEvent\"^v\"objc\"{?=\"interface\"^v\"name\"^{__CFString}\"getProperty\":\"setProperty\":\"eventMatching\":\"setEventDispatcher\":\"setCancelHandler\":\"activate\":\"cancel\":\"setDispatchQueue\":\"clientNotification\":\"copyEvent\":\"setOutputEvent\":\"setHIDEventService\":}}"
+ "{?=\"timeStamp\"Q\"senderID\"Q\"typeMask\"Q\"options\"I\"attributeData\"*\"context\"^v\"attachments\"^{__CFDictionary}\"sender\"^v\"children\"^{__CFArray}\"parent\"^{__IOHIDEvent}\"attributeDataLength\"q\"eventData\"^{IOHIDEventData}}"
- "%s: Filtered event type:%d sender:%#llx eventInfo:(%@)"
- "ColorComponent0:"
- "ColorComponent1:"
- "ColorComponent2:"
- "ColorSpace:"
- "Event filtered type:%d service:0x%llx connection:%@ session filter:%@"
- "Event filtered type:%d service:0x%llx eventInfo:(%@) session filter:%@"
- "Event filtered type:%d service:0x%llx session filter:%@"
- "Failed to create event at index=%d eventCount=%d eventDataOffset=%d totalEventDataSize=%d"
- "IOHIDService name:%s id:0x%llx primaryUsagePage:0x%x primaryUsage:0x%x transport:%s locationID:%@ reportInterval:%d batchInterval:%d events:%d mask:0x%llx"
- "OSKEXT_BUILD_DATE 23:52:52 Apr 18 2025"
- "Setting assertion timeout to fire in %d secs for timeout_ts %llu"
- "Timeout: assertion id 0x%x with time %llu"
- "Undefined"
- "XYZ"
- "buttonState: %d"
- "keyboardPress: %d"
- "vendorUsagePage: %d vendorUsage:%d dataLength:%d"
- "{?=\"session\"^{__IOHIDSession}\"service\"I\"serviceInterface\"^^{IOHIDServiceInterface}\"serviceInterface2\"^^{IOHIDServiceInterface2}\"plugInInterface\"^^{IOCFPlugInInterfaceStruct}\"registryID\"^{__CFNumber}\"locationID\"^v\"entitlements\"^{__CFArray}\"queueContext\"^{__IOHIDServiceQueueContext}\"dispatchQueue\"@\"NSObject<OS_dispatch_queue>\"\"notificationPort\"^{IONotificationPort}\"notification\"I\"removalNotificationSet\"^{__CFSet}\"propertyNotificationSet\"^{__CFSet}\"requestTerminationNotificationSet\"^{__CFSet}\"eventTarget\"^v\"eventRefcon\"^v\"eventCallback\"^?\"lastLEDMask\"I\"lastButtonMask\"I\"currentReportInterval\"I\"currentBatchInterval\"I\"defaultReportInterval\"I\"defaultBatchInterval\"I\"primaryUsagePage\"I\"primaryUsage\"I\"transport\"[32c]\"queueSize\"I\"containsReportInterval\"i\"state\"I\"eventCount\"I\"eventMask\"Q\"clientCacheDict\"^{__CFDictionary}\"simpleFilters\"^{__CFArray}\"filters\"^{__CFArray}\"keyboardEventInProgress\"^{__CFSet}\"nullEventMask\"Q\"displayIntegratedDigitizer\"i\"builtIn\"i\"inMomentumPhase\"i\"inDigitizerPhase\"i\"supportReportLatency\"i\"hidden\"i\"registered\"i\"protectedAccess\"i\"propertyCache\"^{__CFDictionary}\"propertyCacheHit\"I\"propertyCacheMiss\"I\"activityLastTimestamp\"Q\"virtualService\"{?=\"connection\"^v\"target\"^v\"refcon\"^v\"callbacks\"^{IOHIDServiceVirtualCallbacksV2}}\"connections\"^^v\"propertySetTime\"Q\"propertyGetTime\"Q\"elementSetTime\"Q\"regID\"Q\"eventLog\"^{__CFData}\"eventTypeCnt\"^Q\"pluginCancelHandler\"@?\"filterCancelHandler\"@?\"pendingPluginCancel\"B\"pendingFilterCancels\"I\"cancelTimer\"@\"NSObject<OS_dispatch_source>\"\"dataLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"hidAnalyticsEvent\"^v\"hidAnalyticsDispatchEvent\"^v\"objc\"{?=\"interface\"^v\"name\"^{__CFString}\"getProperty\":\"setProperty\":\"eventMatching\":\"setEventDispatcher\":\"setCancelHandler\":\"activate\":\"cancel\":\"setDispatchQueue\":\"clientNotification\":\"copyEvent\":\"setOutputEvent\":}}"
- "{?=\"timeStamp\"Q\"senderID\"Q\"typeMask\"Q\"options\"I\"attributeData\"*\"context\"^v\"attachments\"^{__CFDictionary}\"sender\"^v\"children\"^{__CFArray}\"parent\"^{__IOHIDEvent}\"attributeDataLength\"q\"eventCount\"q\"eventData\"^{IOHIDEventData}}"

```
