## EventKitSyncServices

> `/System/Library/PrivateFrameworks/EventKitSyncServices.framework/EventKitSyncServices`

```diff

-420.1.0.0.0
-  __TEXT.__text: 0xea0
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_methlist: 0x254
-  __TEXT.__const: 0x58
+428.0.0.0.0
+  __TEXT.__text: 0x13fc
+  __TEXT.__objc_methlist: 0x2bc
+  __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__cstring: 0x141
-  __TEXT.__oslogstring: 0x66
-  __TEXT.__unwind_info: 0xd0
-  __TEXT.__objc_classname: 0x6d
-  __TEXT.__objc_methname: 0x45c
-  __TEXT.__objc_methtype: 0x15a
-  __TEXT.__objc_stubs: 0x360
-  __DATA_CONST.__got: 0x70
+  __TEXT.__cstring: 0x143
+  __TEXT.__oslogstring: 0x1d9
+  __TEXT.__unwind_info: 0xc8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x78
-  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b8
+  __DATA_CONST.__objc_selrefs: 0x238
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xe0
+  __DATA_CONST.__got: 0x88
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x100
-  __AUTH_CONST.__objc_const: 0x320
+  __AUTH_CONST.__objc_const: 0x3f0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x40
+  __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3BFC1B4F-41A1-3071-BEAB-5CED6567505D
-  Functions: 34
-  Symbols:   201
-  CStrings:  120
+  UUID: 9E3BDD75-F3A4-3209-8621-DCCC3B6950B6
+  Functions: 49
+  Symbols:   263
+  CStrings:  32
 
Symbols:
+ +[EKSSyncRange ensureNonNilInterval:]
+ +[EKSSyncRange ensureNonNilInterval:].cold.1
+ +[EKSSyncRange normalizeAnchorDate:withCalendar:]
+ +[EKSSyncRange normalizeAnchorDate:withCalendar:].cold.1
+ +[EKSSyncRange rangeStartingAtDate:calendar:unit:pastDistance:futureDistance:]
+ +[EKSSyncRange rangeStartingAtDate:calendar:unit:pastDistance:futureDistance:].cold.1
+ +[EKSSyncRange rangeStartingAtDate:calendar:unit:pastDistance:futureDistance:].cold.2
+ +[EKSSyncRange rangeStartingAtDate:calendar:unit:pastDistance:futureDistance:].cold.3
+ +[EKSSyncRange resetSyncRangeWithCalendar:anchorDate:]
+ +[EKSSyncRange resetSyncRangeWithCalendar:anchorDate:].cold.1
+ +[EKSSyncRange resetSyncRange]
+ -[NSCalendar(EKSAdditions) eks_daysInMonth:]
+ -[NSCalendar(EKSAdditions) eks_firstDayOfMonth:]
+ _OBJC_CLASS_$_EKSSyncRange
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSDateInterval
+ _OBJC_METACLASS_$_EKSSyncRange
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSCalendar_$_EKSAdditions
+ __OBJC_$_CATEGORY_NSCalendar_$_EKSAdditions
+ __OBJC_$_CLASS_METHODS_EKSSyncRange
+ __OBJC_CLASS_RO_$_EKSSyncRange
+ __OBJC_METACLASS_RO_$_EKSSyncRange
+ __os_log_default
+ __os_log_fault_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$autoupdatingCurrentCalendar
+ _objc_msgSend$compare:
+ _objc_msgSend$components:fromDate:
+ _objc_msgSend$date
+ _objc_msgSend$dateByAddingUnit:value:toDate:options:
+ _objc_msgSend$dateFromComponents:
+ _objc_msgSend$eks_firstDayOfMonth:
+ _objc_msgSend$ensureNonNilInterval:
+ _objc_msgSend$initWithStartDate:endDate:
+ _objc_msgSend$normalizeAnchorDate:withCalendar:
+ _objc_msgSend$rangeOfUnit:inUnit:forDate:
+ _objc_msgSend$rangeStartingAtDate:calendar:unit:pastDistance:futureDistance:
+ _objc_msgSend$resetSyncRangeWithCalendar:anchorDate:
+ _objc_msgSend$startOfDayForDate:
+ _objc_release_x23
+ _objc_release_x24
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
CStrings:
+ "Failed to create interval, returning zero-length interval from now"
+ "Failed to normalize to first of month,, using today as fallback"
+ "Failed to produce boundary future date, futureDistance: %ld, startDate: %@"
+ "Failed to produce boundary past date, pastDistance: %ld, startDate: %@"
+ "nil Calendar passed to resetSyncRangeWithCalendar"
+ "nil startDate passed to rangeStartingAtDate"
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "EKSSClientInterface"
- "EKSSServerInterface"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",&,N,V_logText"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,R"
- "TQ,R"
- "URLByAppendingPathComponent:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_connection"
- "_createConnection"
- "_logText"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "dealloc"
- "debugDescription"
- "decodeObjectOfClasses:forKey:"
- "defaultManager"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "dumpDiagnosticsWithCompletion:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "fileURLWithPath:"
- "hash"
- "init"
- "initWithCoder:"
- "initWithMachServiceName:options:"
- "initWithString:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "log"
- "mergeLogger:"
- "now"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLogText:"
- "setRemoteObjectInterface:"
- "setWithObjects:"
- "stringByAppendingString:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "timestampLogForString:"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSURL\"@\"NSURL\"@\"EKSSLogger\">16"
- "writeLogFileWithDirectory:andFileName:"
- "writeToURL:atomically:encoding:error:"
- "zone"

```
