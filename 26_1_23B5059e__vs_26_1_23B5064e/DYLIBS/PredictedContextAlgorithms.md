## PredictedContextAlgorithms

> `/System/Library/PrivateFrameworks/PredictedContextAlgorithms.framework/PredictedContextAlgorithms`

```diff

-36.0.0.0.0
-  __TEXT.__text: 0x8e628
+37.0.0.0.0
+  __TEXT.__text: 0x8d6a4
   __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_methlist: 0x6b44
-  __TEXT.__const: 0xbf4
-  __TEXT.__cstring: 0x3399
-  __TEXT.__oslogstring: 0x6a22
+  __TEXT.__objc_methlist: 0x6b0c
+  __TEXT.__const: 0xbe4
+  __TEXT.__cstring: 0x337d
+  __TEXT.__oslogstring: 0x643d
   __TEXT.__swift5_typeref: 0x2e0
   __TEXT.__swift5_reflstr: 0x14d
   __TEXT.__swift5_assocty: 0x30

   __TEXT.__swift_as_ret: 0x20
   __TEXT.__gcc_except_tab: 0xed8
   __TEXT.__ustring: 0xbe
-  __TEXT.__unwind_info: 0x1940
+  __TEXT.__unwind_info: 0x1930
   __TEXT.__eh_frame: 0x628
-  __TEXT.__objc_classname: 0x93f
-  __TEXT.__objc_methname: 0xd64c
-  __TEXT.__objc_methtype: 0x17a4
-  __TEXT.__objc_stubs: 0x8b60
-  __DATA_CONST.__got: 0x690
+  __TEXT.__objc_classname: 0x925
+  __TEXT.__objc_methname: 0xd4fc
+  __TEXT.__objc_methtype: 0x1756
+  __TEXT.__objc_stubs: 0x8ae0
+  __DATA_CONST.__got: 0x688
   __DATA_CONST.__const: 0xb68
-  __DATA_CONST.__objc_classlist: 0x378
+  __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f28
+  __DATA_CONST.__objc_selrefs: 0x2f08
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x868
   __AUTH_CONST.__const: 0x830
-  __AUTH_CONST.__cfstring: 0x4300
-  __AUTH_CONST.__objc_const: 0xad48
+  __AUTH_CONST.__cfstring: 0x42e0
+  __AUTH_CONST.__objc_const: 0xacb8
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x8b0
+  __AUTH.__objc_data: 0x860
   __AUTH.__data: 0x1b0
   __DATA.__objc_ivar: 0x738
-  __DATA.__data: 0x288
+  __DATA.__data: 0x260
   __DATA.__bss: 0x4a0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1e00

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D7D55C9E-79A0-3ED1-8B4F-D154D7BC4C86
-  Functions: 2841
-  Symbols:   9192
-  CStrings:  4125
+  UUID: 79BD9192-6AA4-37D9-912C-A4E1BAF46A54
+  Functions: 2837
+  Symbols:   9174
+  CStrings:  4096
 
Symbols:
- +[PCGenericRoutinePredictor buildValidLoiIdentifiersFromHistory:forDayOfWeek:forHour:forMinute:atTime:inTimeZone:timeWindowHours:requireExactDayOfWeek:]
- +[PCGenericRoutinePredictor filterCandidateVisitsByRoutine:withHistory:atTime:inTimeZone:]
- +[PCGenericRoutinePredictor filterCandidateVisitsByRoutine:withHistory:atTime:inTimeZone:timeWindowHours:requireExactDayOfWeek:]
- +[PCGenericRoutinePredictor shouldKeepCandidateVisit:withValidLoiIdentifiers:]
- _OBJC_CLASS_$_PCGenericRoutinePredictor
- _OBJC_METACLASS_$_PCGenericRoutinePredictor
- _PCLogCategoryGenericRoutinePredictor
- __OBJC_$_CLASS_METHODS_PCGenericRoutinePredictor
- __OBJC_CLASS_RO_$_PCGenericRoutinePredictor
- __OBJC_METACLASS_RO_$_PCGenericRoutinePredictor
- _objc_msgSend$buildValidLoiIdentifiersFromHistory:forDayOfWeek:forHour:forMinute:atTime:inTimeZone:timeWindowHours:requireExactDayOfWeek:
- _objc_msgSend$filterCandidateVisitsByRoutine:withHistory:atTime:inTimeZone:
- _objc_msgSend$filterCandidateVisitsByRoutine:withHistory:atTime:inTimeZone:timeWindowHours:requireExactDayOfWeek:
- _objc_msgSend$shouldKeepCandidateVisit:withValidLoiIdentifiers:
CStrings:
- "@76@0:8@16q24q32q40d48@56d64B72"
- "GMT"
- "GenericRoutinePredictor"
- "PCGenericRoutinePredictor"
- "PCGenericRoutinePredictor: Candidate visit missing LOI information, keeping visit for other predictors"
- "PCGenericRoutinePredictor: Current time - Day of week: %ld, Hour: %ld, Minute: %ld"
- "PCGenericRoutinePredictor: Failed to extract date components - aborting filtering"
- "PCGenericRoutinePredictor: Filtering out visit with LOI ID %@ and probability %.3f - no routine pattern found for this day/time"
- "PCGenericRoutinePredictor: Found %lu valid LOI identifiers for routine filtering"
- "PCGenericRoutinePredictor: Invalid currentTimeCFAbsolute %f - aborting filtering"
- "PCGenericRoutinePredictor: Invalid date components (dow=%ld, h=%ld, m=%ld) - aborting"
- "PCGenericRoutinePredictor: Invalid timeWindowHours %f - using default"
- "PCGenericRoutinePredictor: Large timeWindowHours %f - clamping to 12.0"
- "PCGenericRoutinePredictor: No candidate visits to filter"
- "PCGenericRoutinePredictor: No input time zone - defaulting to PST for routine filtering"
- "PCGenericRoutinePredictor: No timezone available - using system timezone"
- "PCGenericRoutinePredictor: No visit history available for routine filtering"
- "PCGenericRoutinePredictor: PST timezone unavailable - falling back to GMT"
- "PCGenericRoutinePredictor: Removed %lu visits that don't match routine patterns, %lu visits remaining"
- "PCGenericRoutinePredictor: Routine filtering time zone: %@"
- "PCGenericRoutinePredictor: Starting routine filtering with %lu candidate visits and %lu historical visits"
- "PCGenericRoutinePredictor: currentTimeCFAbsolute %f outside reasonable bounds - aborting"
- "buildValidLoiIdentifiersFromHistory:forDayOfWeek:forHour:forMinute:atTime:inTimeZone:timeWindowHours:requireExactDayOfWeek:"
- "filterCandidateVisitsByRoutine:withHistory:atTime:inTimeZone:"
- "filterCandidateVisitsByRoutine:withHistory:atTime:inTimeZone:timeWindowHours:requireExactDayOfWeek:"
- "shouldKeepCandidateVisit:withValidLoiIdentifiers:"
- "v48@0:8@16@24d32@40"
- "v60@0:8@16@24d32@40d48B56"

```
