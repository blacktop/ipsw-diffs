## HeartHealth

> `/System/Library/PrivateFrameworks/HeartHealth.framework/HeartHealth`

```diff

-6200.2.7.2.1
-  __TEXT.__text: 0x28e28
+6200.2.11.2.0
+  __TEXT.__text: 0x2937c
   __TEXT.__auth_stubs: 0xa10
-  __TEXT.__objc_methlist: 0x2f34
+  __TEXT.__objc_methlist: 0x2f7c
   __TEXT.__const: 0x272
-  __TEXT.__cstring: 0x36b1
-  __TEXT.__oslogstring: 0x17b4
-  __TEXT.__gcc_except_tab: 0x26c
+  __TEXT.__cstring: 0x36c1
+  __TEXT.__oslogstring: 0x1824
+  __TEXT.__gcc_except_tab: 0x27c
   __TEXT.__swift5_typeref: 0x23
   __TEXT.__swift5_reflstr: 0x57
   __TEXT.__swift5_assocty: 0x18

   __TEXT.__swift5_fieldmd: 0x74
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xc08
+  __TEXT.__unwind_info: 0xc10
   __TEXT.__eh_frame: 0x70
-  __TEXT.__objc_classname: 0xc33
-  __TEXT.__objc_methname: 0x89de
-  __TEXT.__objc_methtype: 0x1088
-  __TEXT.__objc_stubs: 0x4d00
+  __TEXT.__objc_classname: 0xc38
+  __TEXT.__objc_methname: 0x8b03
+  __TEXT.__objc_methtype: 0x1098
+  __TEXT.__objc_stubs: 0x4da0
   __DATA_CONST.__got: 0x618
-  __DATA_CONST.__const: 0xd90
+  __DATA_CONST.__const: 0xdb0
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c30
+  __DATA_CONST.__objc_selrefs: 0x1c60
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x518
-  __AUTH_CONST.__const: 0x350
-  __AUTH_CONST.__cfstring: 0x2d20
-  __AUTH_CONST.__objc_const: 0x5c80
+  __AUTH_CONST.__const: 0x370
+  __AUTH_CONST.__cfstring: 0x2d00
+  __AUTH_CONST.__objc_const: 0x5d18
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xf00
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0x2f8
+  __DATA.__objc_ivar: 0x300
   __DATA.__data: 0x8c8
   __DATA.__bss: 0x1c0
   __DATA.__common: 0x20

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 4E5C5465-760F-3C06-BF6A-EEE4AEFCFC11
-  Functions: 1213
-  Symbols:   4191
-  CStrings:  2319
+  UUID: 40AF5B74-4D9E-3301-B312-6601338CEA48
+  Functions: 1219
+  Symbols:   4212
+  CStrings:  2331
 
Symbols:
+ -[HKHRBloodPressureJournalSummaryBuilder buildAverageClassificationForSummary:]
+ -[HKHRBloodPressureJournalSummaryBuilder buildAverageClassificationForSummary:].cold.1
+ -[HKHRBloodPressureJournalSummaryBuilder fetchStatisticsForQuantityType:completeDate:resultsHandler:]
+ -[HKHRLearnHypertensionJournalSummary completeDate]
+ -[HKHRLearnHypertensionJournalSummary completedDate]
+ -[HKHRLearnHypertensionJournalSummary initWithWakeupSampleMap:bedtimeSampleMap:completeDate:]
+ -[HKHRMonitorHypertensionJournalSummary completeDateAsOfDate:]
+ -[HKHRMonitorHypertensionJournalSummary completeDate]
+ -[HKHRMonitorHypertensionJournalSummary samples]
+ _OBJC_IVAR_$_HKHRLearnHypertensionJournalSummary._completedDate
+ _OBJC_IVAR_$_HKHRMonitorHypertensionJournalSummary._samples
+ ___73+[HKHRLearnHypertensionJournalSummaryBuilder summaryFromSamples:journal:]_block_invoke
+ ___79-[HKHRBloodPressureJournalSummaryBuilder buildAverageClassificationForSummary:]_block_invoke
+ ___79-[HKHRBloodPressureJournalSummaryBuilder buildAverageClassificationForSummary:]_block_invoke_2
+ ___79-[HKHRBloodPressureJournalSummaryBuilder buildAverageClassificationForSummary:]_block_invoke_3
+ ___block_descriptor_32_e31_q24?0"HKSample"8"HKSample"16l
+ _objc_msgSend$buildAverageClassificationForSummary:
+ _objc_msgSend$compare:
+ _objc_msgSend$completeDate
+ _objc_msgSend$completeDateAsOfDate:
+ _objc_msgSend$completedDate
+ _objc_msgSend$fetchStatisticsForQuantityType:completeDate:resultsHandler:
+ _objc_msgSend$hk_isBeforeDate:
+ _objc_msgSend$initWithWakeupSampleMap:bedtimeSampleMap:completeDate:
+ _objc_msgSend$isDate:inSameDayAsDate:
+ _objc_msgSend$predicateForSamplesWithStartDate:endDate:inclusiveEndDates:options:
+ _objc_msgSend$sortedArrayUsingComparator:
- -[HKHRBloodPressureJournalSummaryBuilder buildAverageClassification]
- -[HKHRBloodPressureJournalSummaryBuilder buildAverageClassification].cold.1
- -[HKHRBloodPressureJournalSummaryBuilder fetchStatisticsForQuantityType:resultsHandler:]
- -[HKHRLearnHypertensionJournalSummary initWithWakeupSampleMap:bedtimeSampleMap:]
- ___68-[HKHRBloodPressureJournalSummaryBuilder buildAverageClassification]_block_invoke
- ___68-[HKHRBloodPressureJournalSummaryBuilder buildAverageClassification]_block_invoke_2
- ___68-[HKHRBloodPressureJournalSummaryBuilder buildAverageClassification]_block_invoke_3
- _objc_msgSend$allObjects
- _objc_msgSend$buildAverageClassification
- _objc_msgSend$datesWithSamples
- _objc_msgSend$fetchStatisticsForQuantityType:resultsHandler:
- _objc_msgSend$initWithWakeupSampleMap:bedtimeSampleMap:
- _objc_msgSend$valueForKeyPath:
CStrings:
+ "@\"NSDate\"16@0:8"
+ "T@\"NSArray\",R,C,N,V_samples"
+ "T@\"NSDate\",R,N"
+ "T@\"NSDate\",R,N,V_completedDate"
+ "[%@] Fetching statistics with startDate: %@ and completeDate: %@"
+ "[%{public}s] date of sample that completed journal: %@)"
+ "_completedDate"
+ "buildAverageClassificationForSummary:"
+ "compare:"
+ "completeDate"
+ "completeDateAsOfDate:"
+ "completedDate"
+ "fetchStatisticsForQuantityType:completeDate:resultsHandler:"
+ "hk_isBeforeDate:"
+ "initWithWakeupSampleMap:bedtimeSampleMap:completeDate:"
+ "isDate:inSameDayAsDate:"
+ "predicateForSamplesWithStartDate:endDate:inclusiveEndDates:options:"
+ "q24@?0@\"HKSample\"8@\"HKSample\"16"
+ "sortedArrayUsingComparator:"
- "@max.self"
- "allObjects"
- "buildAverageClassification"
- "fetchStatisticsForQuantityType:resultsHandler:"
- "initWithWakeupSampleMap:bedtimeSampleMap:"
- "valueForKeyPath:"

```
