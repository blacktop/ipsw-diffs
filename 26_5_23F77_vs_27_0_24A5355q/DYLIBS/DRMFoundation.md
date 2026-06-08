## DRMFoundation

> `/System/Library/PrivateFrameworks/DRMFoundation.framework/DRMFoundation`

```diff

-234.120.3.0.0
-  __TEXT.__text: 0x2e2c
-  __TEXT.__auth_stubs: 0x3c0
+269.0.0.0.0
+  __TEXT.__text: 0x2b40
   __TEXT.__objc_methlist: 0x3d4
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x140
-  __TEXT.__cstring: 0x1a6
-  __TEXT.__unwind_info: 0x1c8
-  __TEXT.__objc_classname: 0x7a
-  __TEXT.__objc_methname: 0xa6e
-  __TEXT.__objc_methtype: 0x148
-  __TEXT.__objc_stubs: 0x640
-  __DATA_CONST.__got: 0x98
+  __TEXT.__cstring: 0x1af
+  __TEXT.__unwind_info: 0x198
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1f8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2f0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__got: 0x98
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x750
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3D8FB6C7-076D-3D36-BE86-AFDC30464CCD
+  UUID: 75D007E8-15F2-32C7-8277-984A82442570
   Functions: 96
-  Symbols:   427
-  CStrings:  188
+  Symbols:   429
+  CStrings:  19
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x5
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
CStrings:
- ".cxx_destruct"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSUUID\""
- "@\"_OSDataProtectionManager\""
- "@16@0:8"
- "@24@0:8@?16"
- "@56@0:8@16d24Q32@40@?48"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "Q"
- "Q16@0:8"
- "T@\"NSMutableArray\",&,N,V_workItems"
- "T@\"NSMutableDictionary\",&,N,V_objects"
- "T@\"NSMutableDictionary\",R,N,V_availableState"
- "T@\"NSMutableDictionary\",R,N,V_handlers"
- "T@\"NSNumber\",&,N,V_highestPriority"
- "T@\"NSNumber\",&,N,V_lowestPriority"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_executionQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_syncQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_notifyQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_stateQueue"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_timer"
- "T@\"NSUUID\",R,N,V_handlerUUID"
- "T@\"_OSDataProtectionManager\",R,N,V_manager"
- "T@?,C,N,V_changeHandler"
- "T@?,C,N,V_workHandler"
- "TB,R,N,V_deviceFormatedForContentProtection"
- "TB,R,N,V_notifyEnabled"
- "TQ,N,V_count"
- "TQ,N,V_maxQueueDepth"
- "Td,N,V_maxDelay"
- "Ti,R,N,V_notifyToken"
- "UTF8String"
- "UUID"
- "_DKDeduping"
- "_OSBatchingQueue"
- "_OSDataProtectionManager"
- "_OSDataProtectionStateMonitor"
- "_OSDeduping"
- "_OSPriorityQueue"
- "_availableState"
- "_changeHandler"
- "_count"
- "_deviceFormatedForContentProtection"
- "_executionQueue"
- "_handlerUUID"
- "_handlers"
- "_highestPriority"
- "_lowestPriority"
- "_manager"
- "_maxDelay"
- "_maxQueueDepth"
- "_notifyEnabled"
- "_notifyQueue"
- "_notifyToken"
- "_objects"
- "_os_dedup"
- "_stateQueue"
- "_syncQueue"
- "_timer"
- "_workHandler"
- "_workItems"
- "addObject:"
- "addObject:withPriority:"
- "addWorkItem:"
- "allObjects"
- "allValues"
- "array"
- "arrayWithArray:"
- "availableState"
- "boolValue"
- "changeHandler"
- "compare:"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countForObject:"
- "d"
- "d16@0:8"
- "dataProtectionClassA"
- "dataProtectionClassC"
- "dataProtectionClassD"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "deregisterStateChangeHandler:"
- "description"
- "deviceFormatedForContentProtection"
- "deviceHasBeenUnlockedSinceBoot"
- "deviceIsLocked"
- "deviceIsPasswordConfigured"
- "dictionary"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "executionQueue"
- "firstObject"
- "handleKeyBagLockNotification"
- "handlerUUID"
- "handlers"
- "highestPriority"
- "i"
- "i16@0:8"
- "init"
- "initWithName:maxBatchingDelay:maxQueueDepth:queue:workItemsHandler:"
- "isDataAvailableFor:"
- "isDataAvailableForClassA"
- "isDataAvailableForClassC"
- "lastObject"
- "lowestPriority"
- "manager"
- "maxDelay"
- "maxQueueDepth"
- "member:"
- "minusSet:"
- "notifyEnabled"
- "notifyQueue"
- "notifyToken"
- "numberWithBool:"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "objects"
- "popFirst"
- "popLast"
- "priorityQueue"
- "queueWithName:maxBatchingDelay:maxQueueDepth:queue:workItemsHandler:"
- "registerStateChangeHandler:"
- "removeAllObjects"
- "removeLastObject"
- "removeObject:"
- "removeObject:atPriority:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "set"
- "setChangeHandler:"
- "setCount:"
- "setExecutionQueue:"
- "setHighestPriority:"
- "setLowestPriority:"
- "setMaxDelay:"
- "setMaxQueueDepth:"
- "setObject:forKeyedSubscript:"
- "setObjects:"
- "setSyncQueue:"
- "setTimer:"
- "setWorkHandler:"
- "setWorkItems:"
- "sharedInstance"
- "stateQueue"
- "stringWithFormat:"
- "syncQueue"
- "timeIntervalSinceReferenceDate"
- "timer"
- "unnotifiedIsDataAvailableForClassC"
- "unprotectedExecuteWorkItems"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v32@0:8@16Q24"
- "workHandler"
- "workItems"

```
