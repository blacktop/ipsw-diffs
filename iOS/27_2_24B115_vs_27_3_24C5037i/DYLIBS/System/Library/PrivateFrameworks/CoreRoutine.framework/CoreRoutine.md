## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-1123.0.3.0.0
-  __TEXT.__text: 0x6eff8
-  __TEXT.__objc_methlist: 0x8c68
-  __TEXT.__const: 0x2c0
-  __TEXT.__oslogstring: 0x35c8
-  __TEXT.__cstring: 0x7735
+1123.0.6.0.0
+  __TEXT.__text: 0x70b40
+  __TEXT.__objc_methlist: 0x8f00
+  __TEXT.__const: 0x2d0
+  __TEXT.__oslogstring: 0x3606
+  __TEXT.__cstring: 0x7a4d
   __TEXT.__gcc_except_tab: 0x38c
-  __TEXT.__unwind_info: 0x25b8
+  __TEXT.__ustring: 0x70
+  __TEXT.__unwind_info: 0x2650
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1558
-  __DATA_CONST.__objc_classlist: 0x4d8
+  __DATA_CONST.__const: 0x1588
+  __DATA_CONST.__objc_classlist: 0x4f0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c08
+  __DATA_CONST.__objc_selrefs: 0x2c98
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x4a0
+  __DATA_CONST.__objc_superrefs: 0x4b8
   __DATA_CONST.__objc_arraydata: 0x98
-  __DATA_CONST.__got: 0x550
+  __DATA_CONST.__got: 0x570
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x6580
-  __AUTH_CONST.__objc_const: 0xffa8
-  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__cfstring: 0x6860
+  __AUTH_CONST.__objc_const: 0x103f8
+  __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x12c0
-  __DATA.__objc_ivar: 0x934
+  __AUTH.__objc_data: 0x13b0
+  __DATA.__objc_ivar: 0x954
   __DATA.__data: 0x2e8
-  __DATA_DIRTY.__objc_ivar: 0x160
+  __DATA_DIRTY.__objc_ivar: 0x168
   __DATA_DIRTY.__objc_data: 0x1db0
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3113
-  Symbols:   5501
-  CStrings:  1218
+  Functions: 3167
+  Symbols:   5594
+  CStrings:  1243
 
Symbols:
+ +[RTDataIntegrityValidationResult displayNameForOrphanType:]
+ +[RTDataIntegrityValidationResult explanationForOrphanType:]
+ +[RTTripParkingMetrics getHourIDFromTimeID:]
+ +[RTTripParkingMetrics getTimeIDFromDate:]
+ +[RTTripParkingMetrics getWeekdayIDFromTimeID:]
+ +[RTTripParkingMetrics supportsSecureCoding]
+ +[RTTripParkingMetricsEnumerationContext supportsSecureCoding]
+ +[RTTripParkingMetricsEnumerationOptions supportsSecureCoding]
+ -[RTDataIntegrityValidationResult detailedDescriptionWithTriggerReason:]
+ -[RTDataIntegrityValidationResult initWithOrphanCountsByType:sampleOrphanedVisitIdentifiers:sampleOrphanedLOIIdentifiers:sampleUnexpectedFileExtensions:totalUnexpectedFilesDetected:executionDuration:]
+ -[RTDataIntegrityValidationResult totalUnexpectedFilesDetected]
+ -[RTRoutineManager fetchTripParkingMetricsWithOptions:handler:]
+ -[RTTripParkingMetrics .cxx_destruct]
+ -[RTTripParkingMetrics circlingTime]
+ -[RTTripParkingMetrics commuteID]
+ -[RTTripParkingMetrics copyWithZone:]
+ -[RTTripParkingMetrics description]
+ -[RTTripParkingMetrics encodeWithCoder:]
+ -[RTTripParkingMetrics expirationDate]
+ -[RTTripParkingMetrics hash]
+ -[RTTripParkingMetrics initWithCoder:]
+ -[RTTripParkingMetrics initWithCommuteID:timeID:circlingTime:walkingTime:expirationDate:]
+ -[RTTripParkingMetrics isEqual:]
+ -[RTTripParkingMetrics isEqualToTripParkingMetrics:]
+ -[RTTripParkingMetrics timeID]
+ -[RTTripParkingMetrics walkingTime]
+ -[RTTripParkingMetricsEnumerationContext .cxx_destruct]
+ -[RTTripParkingMetricsEnumerationContext copyWithZone:]
+ -[RTTripParkingMetricsEnumerationContext description]
+ -[RTTripParkingMetricsEnumerationContext encodeWithCoder:]
+ -[RTTripParkingMetricsEnumerationContext hash]
+ -[RTTripParkingMetricsEnumerationContext initWithCoder:]
+ -[RTTripParkingMetricsEnumerationContext initWithEnumerationOptions:]
+ -[RTTripParkingMetricsEnumerationContext initWithEnumerationOptions:offset:]
+ -[RTTripParkingMetricsEnumerationContext init]
+ -[RTTripParkingMetricsEnumerationContext isEqual:]
+ -[RTTripParkingMetricsEnumerationContext offset]
+ -[RTTripParkingMetricsEnumerationContext options]
+ -[RTTripParkingMetricsEnumerationOptions .cxx_destruct]
+ -[RTTripParkingMetricsEnumerationOptions batchSize]
+ -[RTTripParkingMetricsEnumerationOptions commuteID]
+ -[RTTripParkingMetricsEnumerationOptions copyWithZone:]
+ -[RTTripParkingMetricsEnumerationOptions description]
+ -[RTTripParkingMetricsEnumerationOptions encodeWithCoder:]
+ -[RTTripParkingMetricsEnumerationOptions hash]
+ -[RTTripParkingMetricsEnumerationOptions initWithCoder:]
+ -[RTTripParkingMetricsEnumerationOptions initWithCommuteID:]
+ -[RTTripParkingMetricsEnumerationOptions init]
+ -[RTTripParkingMetricsEnumerationOptions isEqual:]
+ -[RTTripParkingMetricsEnumerationOptions setBatchSize:]
+ -[RTTripParkingMetricsEnumerationOptions setCommuteID:]
+ GCC_except_table183
+ GCC_except_table189
+ GCC_except_table459
+ GCC_except_table462
+ GCC_except_table588
+ GCC_except_table592
+ _OBJC_CLASS_$_RTTripParkingMetrics
+ _OBJC_CLASS_$_RTTripParkingMetricsEnumerationContext
+ _OBJC_CLASS_$_RTTripParkingMetricsEnumerationOptions
+ _OBJC_IVAR_$_RTDataIntegrityValidationResult._totalUnexpectedFilesDetected
+ _OBJC_IVAR_$_RTTripParkingMetrics._circlingTime
+ _OBJC_IVAR_$_RTTripParkingMetrics._commuteID
+ _OBJC_IVAR_$_RTTripParkingMetrics._expirationDate
+ _OBJC_IVAR_$_RTTripParkingMetrics._timeID
+ _OBJC_IVAR_$_RTTripParkingMetrics._walkingTime
+ _OBJC_IVAR_$_RTTripParkingMetricsEnumerationContext._offset
+ _OBJC_IVAR_$_RTTripParkingMetricsEnumerationContext._options
+ _OBJC_METACLASS_$_RTTripParkingMetrics
+ _OBJC_METACLASS_$_RTTripParkingMetricsEnumerationContext
+ _OBJC_METACLASS_$_RTTripParkingMetricsEnumerationOptions
+ __OBJC_$_CLASS_METHODS_RTTripParkingMetrics
+ __OBJC_$_CLASS_METHODS_RTTripParkingMetricsEnumerationContext
+ __OBJC_$_CLASS_METHODS_RTTripParkingMetricsEnumerationOptions
+ __OBJC_$_CLASS_PROP_LIST_RTTripParkingMetrics
+ __OBJC_$_CLASS_PROP_LIST_RTTripParkingMetricsEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTTripParkingMetrics
+ __OBJC_$_INSTANCE_METHODS_RTTripParkingMetricsEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTTripParkingMetricsEnumerationOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTTripParkingMetrics
+ __OBJC_$_INSTANCE_VARIABLES_RTTripParkingMetricsEnumerationContext
+ __OBJC_$_INSTANCE_VARIABLES_RTTripParkingMetricsEnumerationOptions
+ __OBJC_$_PROP_LIST_RTTripParkingMetrics
+ __OBJC_$_PROP_LIST_RTTripParkingMetricsEnumerationContext
+ __OBJC_$_PROP_LIST_RTTripParkingMetricsEnumerationOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTTripParkingMetrics
+ __OBJC_CLASS_PROTOCOLS_$_RTTripParkingMetricsEnumerationContext
+ __OBJC_CLASS_PROTOCOLS_$_RTTripParkingMetricsEnumerationOptions
+ __OBJC_CLASS_RO_$_RTTripParkingMetrics
+ __OBJC_CLASS_RO_$_RTTripParkingMetricsEnumerationContext
+ __OBJC_CLASS_RO_$_RTTripParkingMetricsEnumerationOptions
+ __OBJC_METACLASS_RO_$_RTTripParkingMetrics
+ __OBJC_METACLASS_RO_$_RTTripParkingMetricsEnumerationContext
+ __OBJC_METACLASS_RO_$_RTTripParkingMetricsEnumerationOptions
+ ___63-[RTRoutineManager fetchTripParkingMetricsWithOptions:handler:]_block_invoke
+ ___63-[RTRoutineManager fetchTripParkingMetricsWithOptions:handler:]_block_invoke_2
+ ___63-[RTRoutineManager fetchTripParkingMetricsWithOptions:handler:]_block_invoke_3
+ ___63-[RTRoutineManager fetchTripParkingMetricsWithOptions:handler:]_block_invoke_4
+ _kRTTripParkingMetricsTimeIDBucketsPerDay
+ _kRTTripParkingMetricsUnknownDuration
- -[RTDataIntegrityValidationResult initWithOrphanCountsByType:sampleOrphanedVisitIdentifiers:sampleOrphanedLOIIdentifiers:sampleUnexpectedFileExtensions:executionDuration:]
- GCC_except_table178
- GCC_except_table179
- GCC_except_table454
- GCC_except_table457
- GCC_except_table583
- GCC_except_table587
CStrings:
+ "\nSample Orphaned LOI Identifiers (%lu shown):\n"
+ "\nSample Orphaned Visit Identifiers (%lu shown):\n"
+ "\nSample Unexpected Files (%lu shown):\n"
+ "\nUnexpected Files Detected: %lu (cache files with unexpected or missing extensions)\n"
+ "  %@\n"
+ "  • %@: %lu (%@)\n"
+ "-[RTRoutineManager fetchTripParkingMetricsWithOptions:handler:]"
+ "Execution Duration: %.2fs\n\n"
+ "LOI→MapItem"
+ "Locations of Interest with unresolvable mapItem references (MUID)"
+ "Orphan Breakdown:\n"
+ "RTDataIntegrityValidationResult, total, %lu, visitToPlace, %@, visitToMapItem, %@, loiToMapItem, %@, unexpectedFilesDetected, %lu, duration, %.2fs"
+ "RTRoutineManager: invoked fetchTripParkingMetricsWithOptions."
+ "RTTripParkingMetricsEnumerationContext: options=%@, offset=%lu"
+ "RTTripParkingMetricsEnumerationOptions: commuteID=%@, batchSize=%lu"
+ "Unknown orphan type"
+ "Validation Trigger: %@\n"
+ "Visits with incomplete place references"
+ "Visits with unresolvable finerGranularityMapItemIdentifier"
+ "Visit→MapItem"
+ "Visit→Place"
+ "circlingTime"
+ "commuteID,%@,timeID,%d,circlingTime,%f,walkingTime,%f"
+ "timeID"
+ "totalUnexpectedFilesDetected"
+ "walkingTime"
- "RTDataIntegrityValidationResult, total, %lu, visitToPlace, %@, visitToMapItem, %@, loiToMapItem, %@, unexpectedFileExtensions, %@, duration, %.2fs"
```
