## HID

> `/System/Library/PrivateFrameworks/HID.framework/HID`

```diff

-2115.100.21.0.0
-  __TEXT.__text: 0x7388
-  __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0x1a64
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x1a3d
+2222.0.0.0.1
+  __TEXT.__text: 0x8fd8
+  __TEXT.__auth_stubs: 0xe20
+  __TEXT.__objc_methlist: 0x1c8c
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x1b90
   __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__oslogstring: 0x5f
-  __TEXT.__unwind_info: 0x5a0
-  __TEXT.__objc_classname: 0x4ef
-  __TEXT.__objc_methname: 0x302b
-  __TEXT.__objc_methtype: 0x5d2
-  __TEXT.__objc_stubs: 0x7c0
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x418
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__oslogstring: 0x34f
+  __TEXT.__unwind_info: 0x608
+  __TEXT.__objc_classname: 0x511
+  __TEXT.__objc_methname: 0x3368
+  __TEXT.__objc_methtype: 0x6ae
+  __TEXT.__objc_stubs: 0xaa0
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__const: 0x448
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1018
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_selrefs: 0x1118
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x640
-  __AUTH_CONST.__cfstring: 0x7a0
-  __AUTH_CONST.__objc_const: 0xaf8
-  __AUTH_CONST.__objc_intobj: 0x528
+  __AUTH_CONST.__auth_got: 0x720
+  __AUTH_CONST.__cfstring: 0x880
+  __AUTH_CONST.__objc_const: 0xe30
+  __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __DATA.__objc_ivar: 0x6c
-  __DATA.__data: 0x1870
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0xa0
+  __DATA.__data: 0x1900
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/TimeSync.framework/TimeSync
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ECC020C2-1FB3-314A-AE0B-760AFC7DC821
-  Functions: 597
-  Symbols:   1661
-  CStrings:  1071
+  UUID: DD5A5E1B-E379-36AA-A0C0-6E2D9B74DDAA
+  Functions: 666
+  Symbols:   1890
+  CStrings:  1177
 
Symbols:
+ +[HIDTimeSync findDeviceForServiceID:]
+ +[HIDTimeSync findDeviceForServiceID:].cold.1
+ +[HIDTimeSync findDeviceForServiceID:].cold.2
+ +[HIDTimeSync findDeviceForServiceID:].cold.3
+ +[HIDTimeSync findDeviceForServiceID:].cold.4
+ +[HIDTimeSync timeSyncFromHIDDevice:]
+ +[HIDTimeSync timeSyncFromHIDEventService:]
+ +[HIDTimeSync timeSyncFromHIDServiceClient:]
+ +[HIDTimeSync timeSyncFromProtocol:]
+ -[HIDBasicTimeSync .cxx_destruct]
+ -[HIDBasicTimeSync dataFromSyncedTime:error:]
+ -[HIDBasicTimeSync dataFromSyncedTime:error:].cold.1
+ -[HIDBasicTimeSync handleActivate]
+ -[HIDBasicTimeSync handleActivate].cold.1
+ -[HIDBasicTimeSync handleCancel]
+ -[HIDBasicTimeSync handleCancel].cold.1
+ -[HIDBasicTimeSync handlePropertyUpdate:]
+ -[HIDBasicTimeSync handlePropertyUpdate:].cold.1
+ -[HIDBasicTimeSync init]
+ -[HIDBasicTimeSync syncedTimeFromData:error:]
+ -[HIDBasicTimeSync syncedTimeFromData:error:].cold.1
+ -[HIDBasicTimeSync syncedTimeFromData:error:].cold.2
+ -[HIDConnection(HIDFramework) type]
+ -[HIDEvent(HIDFramework) needsUngroupForLegacy]
+ -[HIDEventService(HIDFramework) workIntervalCancel]
+ -[HIDEventService(HIDFramework) workIntervalFinish]
+ -[HIDEventService(HIDFramework) workIntervalStart:deadline:complexity:]
+ -[HIDEventService(HIDFramework) workIntervalUpdate:complexity:]
+ -[HIDEventService(HIDFrameworkPrivate) eventStatistics]
+ -[HIDEventService(HIDFrameworkPrivate) setProperty:forKey:and:]
+ -[HIDTimeSync .cxx_destruct]
+ -[HIDTimeSync activate]
+ -[HIDTimeSync activate].cold.1
+ -[HIDTimeSync activate].cold.2
+ -[HIDTimeSync activate].cold.3
+ -[HIDTimeSync cancelHandler]
+ -[HIDTimeSync cancel]
+ -[HIDTimeSync cancel].cold.1
+ -[HIDTimeSync cancel].cold.2
+ -[HIDTimeSync dataFromSyncedTime:error:]
+ -[HIDTimeSync dealloc]
+ -[HIDTimeSync dealloc].cold.1
+ -[HIDTimeSync eventHandler]
+ -[HIDTimeSync findDevice]
+ -[HIDTimeSync handleActivate]
+ -[HIDTimeSync handleCancel]
+ -[HIDTimeSync handlePropertyUpdate:]
+ -[HIDTimeSync initInternal]
+ -[HIDTimeSync init]
+ -[HIDTimeSync properties]
+ -[HIDTimeSync queue]
+ -[HIDTimeSync registerPropertyNotification:]
+ -[HIDTimeSync registerPropertyNotification:].cold.1
+ -[HIDTimeSync setCancelHandler:]
+ -[HIDTimeSync setCancelHandler:].cold.1
+ -[HIDTimeSync setDispatchQueue:]
+ -[HIDTimeSync setDispatchQueue:].cold.1
+ -[HIDTimeSync setEventHandler:]
+ -[HIDTimeSync setEventHandler:].cold.1
+ -[HIDTimeSync setProviderProperty:forKey:]
+ -[HIDTimeSync setState:]
+ -[HIDTimeSync state]
+ -[HIDTimeSync syncedTimeFromData:error:]
+ _CFDictionaryGetTypeID
+ _CFGetTypeID
+ _CollectionEventFields
+ _HIDTimeSyncPropertyHandler
+ _HeartRateEventFields
+ _IOHIDEventNeedsUngroupForLegacy
+ _IOHIDEventSystemConnectionGetType
+ _IOHIDServiceWorkIntervalCancel
+ _IOHIDServiceWorkIntervalFinish
+ _IOHIDServiceWorkIntervalStart
+ _IOHIDServiceWorkIntervalUpdate
+ _IOIteratorNext
+ _IONotificationPortCreate
+ _IONotificationPortDestroy
+ _IONotificationPortSetDispatchQueue
+ _IOObjectConformsTo
+ _IOObjectRetain
+ _IORegistryEntryCreateIterator
+ _IORegistryEntryIDMatching
+ _IORegistryEntrySearchCFProperty
+ _IOServiceAddInterestNotification
+ _IOServiceGetMatchingService
+ _OBJC_CLASS_$_HIDBasicTimeSync
+ _OBJC_CLASS_$_HIDTimeSync
+ _OBJC_CLASS_$_TSClockManager
+ _OBJC_IVAR_$_HIDBasicTimeSync._active
+ _OBJC_IVAR_$_HIDBasicTimeSync._clockID
+ _OBJC_IVAR_$_HIDBasicTimeSync._tsClock
+ _OBJC_IVAR_$_HIDBasicTimeSync._tsMgr
+ _OBJC_IVAR_$_HIDTimeSync._cancelHandler
+ _OBJC_IVAR_$_HIDTimeSync._client
+ _OBJC_IVAR_$_HIDTimeSync._device
+ _OBJC_IVAR_$_HIDTimeSync._eventHandler
+ _OBJC_IVAR_$_HIDTimeSync._propertyNotify
+ _OBJC_IVAR_$_HIDTimeSync._propertyPort
+ _OBJC_IVAR_$_HIDTimeSync._queue
+ _OBJC_IVAR_$_HIDTimeSync._service
+ _OBJC_IVAR_$_HIDTimeSync._state
+ _OBJC_METACLASS_$_HIDBasicTimeSync
+ _OBJC_METACLASS_$_HIDTimeSync
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __IOHIDLog
+ __IOHIDServiceCopyEventCounts
+ __IOHIDServiceSetPropertyForClient
+ __OBJC_$_CLASS_METHODS_HIDTimeSync
+ __OBJC_$_INSTANCE_METHODS_HIDBasicTimeSync
+ __OBJC_$_INSTANCE_METHODS_HIDTimeSync
+ __OBJC_$_INSTANCE_VARIABLES_HIDBasicTimeSync
+ __OBJC_$_INSTANCE_VARIABLES_HIDTimeSync
+ __OBJC_$_PROP_LIST_HIDTimeSync
+ __OBJC_CLASS_RO_$_HIDBasicTimeSync
+ __OBJC_CLASS_RO_$_HIDTimeSync
+ __OBJC_METACLASS_RO_$_HIDBasicTimeSync
+ __OBJC_METACLASS_RO_$_HIDTimeSync
+ ___21-[HIDTimeSync cancel]_block_invoke
+ ___23-[HIDTimeSync activate]_block_invoke
+ ___kCFBooleanFalse
+ __os_log_debug_impl
+ __os_log_error_impl
+ _kIOMainPortDefault
+ _mach_absolute_time
+ _mach_timebase_info
+ _objc_msgSend$clockIdentifier
+ _objc_msgSend$clockWithClockIdentifier:
+ _objc_msgSend$close
+ _objc_msgSend$convertFromDomainToMachAbsoluteTime:
+ _objc_msgSend$eventHandler
+ _objc_msgSend$findDevice
+ _objc_msgSend$findDeviceForServiceID:
+ _objc_msgSend$handleActivate
+ _objc_msgSend$handleCancel
+ _objc_msgSend$handlePropertyUpdate:
+ _objc_msgSend$initWithService:
+ _objc_msgSend$lockState
+ _objc_msgSend$newTestTimeSync
+ _objc_msgSend$open
+ _objc_msgSend$properties
+ _objc_msgSend$registerPropertyNotification:
+ _objc_msgSend$service
+ _objc_msgSend$setMatching:
+ _objc_msgSend$setProperty:forKey:
+ _objc_msgSend$setProviderProperty:forKey:
+ _objc_msgSend$sharedClockManager
+ _objc_msgSend$state
+ _objc_msgSend$timeSyncFromProtocol:
+ _objc_release_x9
+ _objc_retain_x22
CStrings:
+ "+"
+ "-"
+ "@\"HIDDevice\""
+ "@\"HIDEventService\""
+ "@\"TSClockManager\""
+ "@\"TSUserFilteredClock\""
+ "@24@0:8Q16"
+ "@32@0:8Q16o^@24"
+ "@?16@0:8"
+ "AI"
+ "Active"
+ "B40@0:8@16@24@32"
+ "Couldn't create TSUserFilteredClock!"
+ "Failed find device for ID 0x%llx"
+ "Failed to create iterator for ID 0x%llx"
+ "Failed to get matching for ID 0x%llx"
+ "Failed to get service for ID 0x%llx"
+ "HIDBasicTimeSync"
+ "HIDTimeSync"
+ "HIDTimeSyncProperties"
+ "HIDTimeSyncProtocol"
+ "I24@0:8Q16"
+ "IOGeneralInterest"
+ "IOHIDDevice"
+ "IOService"
+ "PrimaryUsage"
+ "PrimaryUsagePage"
+ "Q"
+ "Q32@0:8@16o^@24"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@?,R,N,V_cancelHandler"
+ "T@?,R,N,V_eventHandler"
+ "TB,R"
+ "TI,N"
+ "TSClockID"
+ "Ti,R"
+ "TimeSync: not locked, clockID: 0x%llx state: %d"
+ "TimeSyncEnabled"
+ "W2 btclk(ns):%llu local abs:%llu Synced ts:%llu remote->local latency(ns):%s%llu"
+ "^{IONotificationPort=}"
+ "_active"
+ "_clockID"
+ "_propertyNotify"
+ "_propertyPort"
+ "_tsClock"
+ "_tsMgr"
+ "assertion failure: \"_eventHandler\" -> %llu"
+ "assertion failure: \"_queue\" -> %llu"
+ "assertion failure: \"_state & HIDTimeSyncStateActivate\" -> %llu"
+ "assertion failure: \"_state == HIDTimeSyncStateInit\" -> %llu"
+ "assertion failure: \"self.state == HIDTimeSyncStateActivate\" -> %llu"
+ "assertion failure: IOServiceAddInterestNotification:%x"
+ "assertion failure: Invalid dispatch state: 0x%x"
+ "assertion failure: Unimplemented in base class"
+ "cancelHandler"
+ "clockIdentifier"
+ "clockWithClockIdentifier:"
+ "collectionUngroupForLegacy"
+ "collectionUsage"
+ "collectionUsagePage"
+ "convertFromDomainToMachAbsoluteTime:"
+ "dataFromSyncedTime:error:"
+ "eventHandler"
+ "eventStatistics"
+ "findDevice"
+ "findDeviceForServiceID:"
+ "handleActivate"
+ "handleActivate enabling TS failed"
+ "handleCancel"
+ "handleCancel disabling TS failed"
+ "handlePropertyUpdate:"
+ "heartRateConfidence "
+ "heartRateGenerationCount"
+ "heartRateLocation"
+ "heartRateRate"
+ "i16@0:8"
+ "i32@0:8Q16Q24"
+ "i40@0:8Q16Q24Q32"
+ "initInternal"
+ "lockState"
+ "needsUngroupForLegacy"
+ "newTestTimeSync"
+ "properties"
+ "registerPropertyNotification:"
+ "setProperty:forKey:and:"
+ "setProviderProperty:forKey:"
+ "setState:"
+ "sharedClockManager"
+ "state"
+ "syncedTimeFromData:error:"
+ "timeSyncFromHIDDevice:"
+ "timeSyncFromHIDEventService:"
+ "timeSyncFromHIDServiceClient:"
+ "timeSyncFromProtocol:"
+ "workIntervalCancel"
+ "workIntervalFinish"
+ "workIntervalStart:deadline:complexity:"
+ "workIntervalUpdate:complexity:"

```
