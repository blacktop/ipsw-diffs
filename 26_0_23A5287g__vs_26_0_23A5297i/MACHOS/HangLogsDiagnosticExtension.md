## HangLogsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension`

```diff

-380.0.0.0.0
-  __TEXT.__text: 0x11350
-  __TEXT.__auth_stubs: 0x990
+382.0.0.0.0
+  __TEXT.__text: 0x13578
+  __TEXT.__auth_stubs: 0x9c0
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_stubs: 0x1a80
-  __TEXT.__objc_methlist: 0xb24
+  __TEXT.__objc_stubs: 0x1c40
+  __TEXT.__objc_methlist: 0xb34
   __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x2476
-  __TEXT.__oslogstring: 0x1820
+  __TEXT.__cstring: 0x260d
+  __TEXT.__oslogstring: 0x1bd2
   __TEXT.__gcc_except_tab: 0x1cc
-  __TEXT.__objc_methname: 0x4032
+  __TEXT.__objc_methname: 0x41ab
   __TEXT.__objc_classname: 0xb2
-  __TEXT.__objc_methtype: 0x78e
+  __TEXT.__objc_methtype: 0x79a
   __TEXT.__ustring: 0xe0
-  __TEXT.__unwind_info: 0x3a8
-  __DATA_CONST.__auth_got: 0x4d8
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0xc10
-  __DATA_CONST.__cfstring: 0x2380
+  __TEXT.__unwind_info: 0x3f0
+  __DATA_CONST.__auth_got: 0x4f0
+  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__const: 0xd38
+  __DATA_CONST.__cfstring: 0x2600
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x1e58
-  __DATA.__objc_selrefs: 0xb20
-  __DATA.__objc_ivar: 0x210
+  __DATA.__objc_const: 0x1e88
+  __DATA.__objc_selrefs: 0xb98
+  __DATA.__objc_ivar: 0x214
   __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0xb4
-  __DATA.__bss: 0xe0
+  __DATA.__data: 0xfc
+  __DATA.__bss: 0xf0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 961C4306-83A9-33F9-B75B-E70F2A5FA362
-  Functions: 414
-  Symbols:   434
-  CStrings:  1412
+  UUID: 95F9A641-9928-315D-99B0-90A553A01213
+  Functions: 439
+  Symbols:   466
+  CStrings:  1483
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _HTGetMachAbsoluteTimeFromNSDate
+ _NSStringFromRBSRole
+ _OBJC_CLASS_$_NSNull
+ _SEC_TO_MATU
+ ___exp10
+ __isValidStateInfoSortedArray
+ _addNewCPURoleToHangEvent
+ _calcluateDurationInCPURoleFromSortedArray
+ _calculateDurationInCPURoleFromStateInfoDict
+ _createStateInfoJSONBlobForHang
+ _createStateInfoSortedArrayWithPtr
+ _kHTCPURoleBreakdownKey
+ _kHTCPURoleEnumKey
+ _kHTCPURoleNameKey
+ _kHTCoreAnalyticsAssertionOtherCPURole
+ _kHTCoreAnalyticsAssertionUIFocal
+ _kHTCoreAnalyticsAssertionUINonFocal
+ _kHTCoreAnalyticsHTForegroundOtherCPURole
+ _kHTCoreAnalyticsHTForegroundUIFocal
+ _kHTCoreAnalyticsHTForegroundUINonFocal
+ _kHTCoreAnalyticsHangOtherCPURole
+ _kHTCoreAnalyticsHangUIFocal
+ _kHTCoreAnalyticsHangUINonFocal
+ _kHTEndCPURoleKey
+ _kHTIntervalsInCPURoleKey
+ _kHTPercentInCPURoleKey
+ _kHTPrefsShouldCollectCPURoleInfo
+ _kHTSecondsSinceCPURoleTransitionBeforeHangKey
+ _kHTStartCPURoleKey
+ _kHTTimeInCPURoleKey
+ _objc_retain_x26
+ _roundDoubleToDecimalPlace
+ _stateInfoSortedArrayComparator
- _addNewTaskStateToHangEvent
- _objc_retain_x9
CStrings:
+ "@32@0:8^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQAQAQ}16Q24"
+ "C"
+ "Compsed final stateInfo sorted Array: %{public}@"
+ "Failed to parse State info dictionary object from sorted array '%@', object is type of class '%@'"
+ "Failed to parse State info dictionary object of key '%@' from sorted array '%@', object is type of class '%@'"
+ "Invalid object(s) of class '%@' and '%@' passed into StateInfo timestamp comparator."
+ "Invalid timestamp(s) of class '%@' and '%@' found in dictionary '%@' during sorting."
+ "Invalid timestamp(s) of class '%@' and '%@' found in dictionary during sorting."
+ "No states were present in the state info array before a hang occurred."
+ "No valid data in recentStateInfo for hang, not sending CPURole data."
+ "Object in state info array is not a dictionary. Is kind of class %@"
+ "Passed in nil stateInfoPtr, returning nil."
+ "RB Notification contained a nil bundle identifier, defaulting to event bundle id."
+ "Received RB Notification for CPU Role change of process(%d) '%{public}@'. Changed from %{public}@ to %{public}@ at %@"
+ "ShouldCollectCPURoleInfo"
+ "TB,R,V_shouldCollectCPURoleInfo"
+ "T^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQAQAQ},R,V_shmem_region"
+ "The provided stateInfoArray '%@' only has state objects AFTER then end of the hang (%llu matu)."
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQAQAQ}"
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQAQAQ}16@0:8"
+ "_shouldCollectCPURoleInfo"
+ "assertion_other_ms"
+ "assertion_ui_focal_ms"
+ "assertion_ui_nonfocal_ms"
+ "cpuRole"
+ "cpuRoleBreakdown"
+ "cpuRoleEnum"
+ "cpuRoleName"
+ "dictionary"
+ "dictionaryWithDictionary:"
+ "duration_other_ms"
+ "duration_ui_focal_ms"
+ "duration_ui_nonfocal_ms"
+ "endCPURole"
+ "foreground_other_ms"
+ "foreground_ui_focal_ms"
+ "foreground_ui_nonfocal_ms"
+ "identifier"
+ "indexOfObject:inSortedRange:options:usingComparator:"
+ "insertObject:atIndex:"
+ "intervalsInCPURole"
+ "isEqualToNumber:"
+ "lastObject"
+ "lastStateChangeTimestamp"
+ "numberWithUnsignedChar:"
+ "numberWithUnsignedLong:"
+ "percentInCPURole"
+ "q24@?0@8@16"
+ "removeObjectAtIndex:"
+ "secondsSinceCPURoleTransitionBeforeHangStart"
+ "setValue:forKey:"
+ "shouldCollectCPURoleInfo"
+ "startCPURole"
+ "stringValue"
+ "timeInCPURole"
+ "timestamp"
+ "unsignedCharValue"
- "@32@0:8^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16Q24"
- "Received RB Notification for state change of pid %d with bundleID '%{public}@'. State changed from %d to %d"
- "T^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ},R,V_shmem_region"
- "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}"
- "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}16@0:8"
- "taskState"

```
