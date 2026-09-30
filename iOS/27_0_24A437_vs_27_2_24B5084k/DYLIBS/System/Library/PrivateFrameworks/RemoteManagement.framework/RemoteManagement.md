## RemoteManagement

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement`

```diff

-624.2.3.0.0
-  __TEXT.__text: 0x4a7c4
-  __TEXT.__objc_methlist: 0x1bf0
+624.40.12.0.0
+  __TEXT.__text: 0x4b204
+  __TEXT.__objc_methlist: 0x1e98
   __TEXT.__const: 0x180c
-  __TEXT.__cstring: 0x2397
-  __TEXT.__oslogstring: 0x492b
-  __TEXT.__gcc_except_tab: 0x41c
+  __TEXT.__cstring: 0x23a7
+  __TEXT.__oslogstring: 0x49fb
+  __TEXT.__gcc_except_tab: 0x4b0
   __TEXT.__swift5_typeref: 0x63b
   __TEXT.__constg_swiftt: 0x9a8
   __TEXT.__swift5_reflstr: 0x303

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1538
+  __TEXT.__unwind_info: 0x1580
   __TEXT.__eh_frame: 0x15d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x660
-  __DATA_CONST.__objc_classlist: 0x160
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1418
+  __DATA_CONST.__objc_selrefs: 0x1588
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__got: 0x598
-  __AUTH_CONST.__const: 0xbf0
+  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__got: 0x5b0
+  __AUTH_CONST.__const: 0xc10
   __AUTH_CONST.__cfstring: 0x1b00
-  __AUTH_CONST.__objc_const: 0x2eb8
+  __AUTH_CONST.__objc_const: 0x3358
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0xb68
-  __AUTH.__objc_data: 0x568
+  __AUTH_CONST.__auth_got: 0xb70
+  __AUTH.__objc_data: 0x608
   __AUTH.__data: 0x830
-  __DATA.__objc_ivar: 0xc8
-  __DATA.__data: 0x6c8
+  __DATA.__objc_ivar: 0xf4
+  __DATA.__data: 0x788
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x670
   __DATA_DIRTY.__data: 0x290

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1389
-  Symbols:   2028
-  CStrings:  691
+  Functions: 1421
+  Symbols:   2124
+  CStrings:  695
 
Symbols:
+ +[RMLog(throttlingDebounceTimer) throttlingDebounceTimer]
+ +[RMThrottlingDebounceTimer throttlingDebounceTimerWithThreshold:window:minimumInterval:maximumInterval:identifier:action:]
+ +[RMXPCUtilities doesConnection:haveEntitlement:]
+ +[RMXPCUtilities isPlatformBinaryForConnection:]
+ -[RMThrottlingDebounceTimer .cxx_destruct]
+ -[RMThrottlingDebounceTimer _pruneSignalsBefore:]
+ -[RMThrottlingDebounceTimer _releaseThrottleLocked]
+ -[RMThrottlingDebounceTimer action]
+ -[RMThrottlingDebounceTimer coalescedSignalCount]
+ -[RMThrottlingDebounceTimer debouncer]
+ -[RMThrottlingDebounceTimer identifier]
+ -[RMThrottlingDebounceTimer initWithThreshold:window:minimumInterval:maximumInterval:identifier:action:]
+ -[RMThrottlingDebounceTimer isThrottling]
+ -[RMThrottlingDebounceTimer maximumInterval]
+ -[RMThrottlingDebounceTimer minimumInterval]
+ -[RMThrottlingDebounceTimer setAction:]
+ -[RMThrottlingDebounceTimer setCoalescedSignalCount:]
+ -[RMThrottlingDebounceTimer setDebouncer:]
+ -[RMThrottlingDebounceTimer setIdentifier:]
+ -[RMThrottlingDebounceTimer setMaximumInterval:]
+ -[RMThrottlingDebounceTimer setMinimumInterval:]
+ -[RMThrottlingDebounceTimer setSignalTimestamps:]
+ -[RMThrottlingDebounceTimer setThreshold:]
+ -[RMThrottlingDebounceTimer setThrottling:]
+ -[RMThrottlingDebounceTimer setWindow:]
+ -[RMThrottlingDebounceTimer signalTimestamps]
+ -[RMThrottlingDebounceTimer threshold]
+ -[RMThrottlingDebounceTimer triggerAggregatingTimerAction]
+ -[RMThrottlingDebounceTimer trigger]
+ -[RMThrottlingDebounceTimer window]
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_RMThrottlingDebounceTimer
+ _OBJC_CLASS_$_RMXPCUtilities
+ _OBJC_IVAR_$_RMThrottlingDebounceTimer._action
+ _OBJC_IVAR_$_RMThrottlingDebounceTimer._coalescedSignalCount
+ _OBJC_IVAR_$_RMThrottlingDebounceTimer._debouncer
+ _OBJC_IVAR_$_RMThrottlingDebounceTimer._identifier
+ _OBJC_IVAR_$_RMThrottlingDebounceTimer._lock
+ _OBJC_IVAR_$_RMThrottlingDebounceTimer._maximumInterval
+ _OBJC_IVAR_$_RMThrottlingDebounceTimer._minimumInterval
+ _OBJC_IVAR_$_RMThrottlingDebounceTimer._signalTimestamps
+ _OBJC_IVAR_$_RMThrottlingDebounceTimer._threshold
+ _OBJC_IVAR_$_RMThrottlingDebounceTimer._throttling
+ _OBJC_IVAR_$_RMThrottlingDebounceTimer._window
+ _OBJC_METACLASS_$_RMThrottlingDebounceTimer
+ _OBJC_METACLASS_$_RMXPCUtilities
+ __OBJC_$_CLASS_METHODS_RMLog(nsdata_rm|nsdictionary_rm|accountHelper|debounceTimer|device|enrollmentController|jsonUtilities|locations|managedDevice|managedKeychainController|managedTrustStoreController|mcAdapter|mdmHelper|sandbox|sharedLock|throttlingDebounceTimer|timeddispatch|xpcEvent|xpcNotifications)
+ __OBJC_$_CLASS_METHODS_RMThrottlingDebounceTimer
+ __OBJC_$_CLASS_METHODS_RMXPCUtilities
+ __OBJC_$_INSTANCE_METHODS_RMThrottlingDebounceTimer
+ __OBJC_$_INSTANCE_VARIABLES_RMThrottlingDebounceTimer
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_RMThrottlingDebounceTimer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RMDebounceTimerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RMDebounceTimerDelegate
+ __OBJC_$_PROTOCOL_REFS_RMDebounceTimerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_RMThrottlingDebounceTimer
+ __OBJC_CLASS_RO_$_RMThrottlingDebounceTimer
+ __OBJC_CLASS_RO_$_RMXPCUtilities
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_RMDebounceTimerDelegate
+ __OBJC_METACLASS_RO_$_RMThrottlingDebounceTimer
+ __OBJC_METACLASS_RO_$_RMXPCUtilities
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_RMDebounceTimerDelegate
+ ___57+[RMLog(throttlingDebounceTimer) throttlingDebounceTimer]_block_invoke
+ _csops_audittoken
+ _objc_msgSend$_pruneSignalsBefore:
+ _objc_msgSend$_releaseThrottleLocked
+ _objc_msgSend$action
+ _objc_msgSend$auditToken
+ _objc_msgSend$coalescedSignalCount
+ _objc_msgSend$debounceTimerWithMinimumInterval:maximumInterval:delegate:identifier:
+ _objc_msgSend$debouncer
+ _objc_msgSend$doubleValue
+ _objc_msgSend$initWithThreshold:window:minimumInterval:maximumInterval:identifier:action:
+ _objc_msgSend$isThrottling
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$processInfo
+ _objc_msgSend$removeObjectsInRange:
+ _objc_msgSend$setCoalescedSignalCount:
+ _objc_msgSend$setDebouncer:
+ _objc_msgSend$setThrottling:
+ _objc_msgSend$signalTimestamps
+ _objc_msgSend$systemUptime
+ _objc_msgSend$threshold
+ _objc_msgSend$throttlingDebounceTimer
+ _objc_msgSend$trigger
+ _objc_msgSend$valueForEntitlement:
+ _objc_msgSend$window
+ _throttlingDebounceTimer.onceToken
+ _throttlingDebounceTimer.result
- __OBJC_$_CLASS_METHODS_RMLog(nsdata_rm|nsdictionary_rm|accountHelper|debounceTimer|device|enrollmentController|jsonUtilities|locations|managedDevice|managedKeychainController|managedTrustStoreController|mcAdapter|mdmHelper|sandbox|sharedLock|timeddispatch|xpcEvent|xpcNotifications)
CStrings:
+ "Throttling engaged for %{public}@ (%lu signals within %g s)"
+ "Throttling released for %{public}@ (coalesced %lu signals into one action)"
+ "Throttling released for %{public}@ (rate subsided, coalesced %lu signals)"
+ "throttlingDebounceTimer"
```
