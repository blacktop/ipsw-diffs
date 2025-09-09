## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-6106.1.2.9.0
-  __TEXT.__text: 0x78cf48
+6106.1.2.11.0
+  __TEXT.__text: 0x790578
   __TEXT.__auth_stubs: 0x4820
-  __TEXT.__objc_methlist: 0x43614
+  __TEXT.__objc_methlist: 0x43a54
   __TEXT.__const: 0x1dd74
   __TEXT.__dlopen_cstrs: 0x15b
-  __TEXT.__cstring: 0x7c209
+  __TEXT.__cstring: 0x7c2fd
   __TEXT.__constg_swiftt: 0x14a4
   __TEXT.__swift5_typeref: 0xd25
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__swift_as_ret: 0x60
   __TEXT.__gcc_except_tab: 0x38470
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x1cc00
+  __TEXT.__unwind_info: 0x1ccb0
   __TEXT.__eh_frame: 0x2310
-  __TEXT.__objc_classname: 0xc522
-  __TEXT.__objc_methname: 0x8e5d0
-  __TEXT.__objc_methtype: 0x16a85
-  __TEXT.__objc_stubs: 0x50340
-  __DATA_CONST.__got: 0x5630
-  __DATA_CONST.__const: 0x1d2d0
-  __DATA_CONST.__objc_classlist: 0x29b0
+  __TEXT.__objc_classname: 0xc597
+  __TEXT.__objc_methname: 0x8ea14
+  __TEXT.__objc_methtype: 0x16af4
+  __TEXT.__objc_stubs: 0x504a0
+  __DATA_CONST.__got: 0x5650
+  __DATA_CONST.__const: 0x1d250
+  __DATA_CONST.__objc_classlist: 0x29c8
   __DATA_CONST.__objc_catlist: 0x4c0
   __DATA_CONST.__objc_protolist: 0x9b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19d50
+  __DATA_CONST.__objc_selrefs: 0x19e98
   __DATA_CONST.__objc_protorefs: 0x1d8
-  __DATA_CONST.__objc_superrefs: 0x1d70
+  __DATA_CONST.__objc_superrefs: 0x1d88
   __DATA_CONST.__objc_arraydata: 0x8478
   __AUTH_CONST.__auth_got: 0x2428
-  __AUTH_CONST.__const: 0xfde8
-  __AUTH_CONST.__cfstring: 0x3d220
-  __AUTH_CONST.__objc_const: 0x7d2c8
+  __AUTH_CONST.__const: 0xfe40
+  __AUTH_CONST.__cfstring: 0x3d400
+  __AUTH_CONST.__objc_const: 0x7d7d0
   __AUTH_CONST.__objc_arrayobj: 0x1e90
   __AUTH_CONST.__objc_intobj: 0x3e58
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0xd2a8
+  __AUTH.__objc_data: 0xd398
   __AUTH.__data: 0x7e0
-  __DATA.__objc_ivar: 0x4378
+  __DATA.__objc_ivar: 0x43ac
   __DATA.__data: 0x8188
   __DATA.__common: 0x64
   __DATA.__bss: 0x14c8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CF8FCCC4-B923-3C21-93F1-46C439E4350B
-  Functions: 34615
-  Symbols:   103593
-  CStrings:  44123
+  UUID: 32FD3324-4565-30F3-AC69-553F06AA92B7
+  Functions: 34708
+  Symbols:   103822
+  CStrings:  44213
 
Symbols:
+ +[HDCodableBloodPressureJournal timeIntervalType]
+ +[HDCodableBloodPressureJournalState bloodPressureJournalType]
+ -[HDCodableBloodPressureJournal .cxx_destruct]
+ -[HDCodableBloodPressureJournal StringAsJournalState:]
+ -[HDCodableBloodPressureJournal StringAsJournalType:]
+ -[HDCodableBloodPressureJournal StringAsScheduleType:]
+ -[HDCodableBloodPressureJournal addTimeInterval:]
+ -[HDCodableBloodPressureJournal clearTimeIntervals]
+ -[HDCodableBloodPressureJournal copyTo:]
+ -[HDCodableBloodPressureJournal copyWithZone:]
+ -[HDCodableBloodPressureJournal description]
+ -[HDCodableBloodPressureJournal dictionaryRepresentation]
+ -[HDCodableBloodPressureJournal endDate]
+ -[HDCodableBloodPressureJournal hasEndDate]
+ -[HDCodableBloodPressureJournal hasJournalState]
+ -[HDCodableBloodPressureJournal hasJournalType]
+ -[HDCodableBloodPressureJournal hasScheduleType]
+ -[HDCodableBloodPressureJournal hasStartDate]
+ -[HDCodableBloodPressureJournal hasTimestamp]
+ -[HDCodableBloodPressureJournal hasUuid]
+ -[HDCodableBloodPressureJournal hash]
+ -[HDCodableBloodPressureJournal isEqual:]
+ -[HDCodableBloodPressureJournal journalStateAsString:]
+ -[HDCodableBloodPressureJournal journalState]
+ -[HDCodableBloodPressureJournal journalTypeAsString:]
+ -[HDCodableBloodPressureJournal journalType]
+ -[HDCodableBloodPressureJournal mergeFrom:]
+ -[HDCodableBloodPressureJournal readFrom:]
+ -[HDCodableBloodPressureJournal scheduleTypeAsString:]
+ -[HDCodableBloodPressureJournal scheduleType]
+ -[HDCodableBloodPressureJournal setEndDate:]
+ -[HDCodableBloodPressureJournal setHasEndDate:]
+ -[HDCodableBloodPressureJournal setHasJournalState:]
+ -[HDCodableBloodPressureJournal setHasJournalType:]
+ -[HDCodableBloodPressureJournal setHasScheduleType:]
+ -[HDCodableBloodPressureJournal setHasStartDate:]
+ -[HDCodableBloodPressureJournal setHasTimestamp:]
+ -[HDCodableBloodPressureJournal setJournalState:]
+ -[HDCodableBloodPressureJournal setJournalType:]
+ -[HDCodableBloodPressureJournal setScheduleType:]
+ -[HDCodableBloodPressureJournal setStartDate:]
+ -[HDCodableBloodPressureJournal setTimeIntervals:]
+ -[HDCodableBloodPressureJournal setTimestamp:]
+ -[HDCodableBloodPressureJournal setUuid:]
+ -[HDCodableBloodPressureJournal startDate]
+ -[HDCodableBloodPressureJournal timeIntervalAtIndex:]
+ -[HDCodableBloodPressureJournal timeIntervalsCount]
+ -[HDCodableBloodPressureJournal timeIntervals]
+ -[HDCodableBloodPressureJournal timestamp]
+ -[HDCodableBloodPressureJournal uuid]
+ -[HDCodableBloodPressureJournal writeTo:]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval .cxx_destruct]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval StringAsDayWindowType:]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval copyTo:]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval copyWithZone:]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval dayWindowTypeAsString:]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval dayWindowType]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval description]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval dictionaryRepresentation]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval hasDayWindowType]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval hasScheduledTime]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval hash]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval isEqual:]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval mergeFrom:]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval readFrom:]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval scheduledTime]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval setDayWindowType:]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval setHasDayWindowType:]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval setScheduledTime:]
+ -[HDCodableBloodPressureJournalScheduleTimeInterval writeTo:]
+ -[HDCodableBloodPressureJournalState .cxx_destruct]
+ -[HDCodableBloodPressureJournalState addBloodPressureJournal:]
+ -[HDCodableBloodPressureJournalState bloodPressureJournalAtIndex:]
+ -[HDCodableBloodPressureJournalState bloodPressureJournalsCount]
+ -[HDCodableBloodPressureJournalState bloodPressureJournals]
+ -[HDCodableBloodPressureJournalState clearBloodPressureJournals]
+ -[HDCodableBloodPressureJournalState copyTo:]
+ -[HDCodableBloodPressureJournalState copyWithZone:]
+ -[HDCodableBloodPressureJournalState description]
+ -[HDCodableBloodPressureJournalState dictionaryRepresentation]
+ -[HDCodableBloodPressureJournalState hash]
+ -[HDCodableBloodPressureJournalState isEqual:]
+ -[HDCodableBloodPressureJournalState mergeFrom:]
+ -[HDCodableBloodPressureJournalState readFrom:]
+ -[HDCodableBloodPressureJournalState setBloodPressureJournals:]
+ -[HDCodableBloodPressureJournalState writeTo:]
+ OBJC_IVAR_$_HDCodableBloodPressureJournal._endDate
+ OBJC_IVAR_$_HDCodableBloodPressureJournal._has
+ OBJC_IVAR_$_HDCodableBloodPressureJournal._journalState
+ OBJC_IVAR_$_HDCodableBloodPressureJournal._journalType
+ OBJC_IVAR_$_HDCodableBloodPressureJournal._scheduleType
+ OBJC_IVAR_$_HDCodableBloodPressureJournal._startDate
+ OBJC_IVAR_$_HDCodableBloodPressureJournal._timeIntervals
+ OBJC_IVAR_$_HDCodableBloodPressureJournal._timestamp
+ OBJC_IVAR_$_HDCodableBloodPressureJournal._uuid
+ OBJC_IVAR_$_HDCodableBloodPressureJournalScheduleTimeInterval._dayWindowType
+ OBJC_IVAR_$_HDCodableBloodPressureJournalScheduleTimeInterval._has
+ OBJC_IVAR_$_HDCodableBloodPressureJournalScheduleTimeInterval._scheduledTime
+ OBJC_IVAR_$_HDCodableBloodPressureJournalState._bloodPressureJournals
+ _HDCodableBloodPressureJournalReadFrom
+ _HDCodableBloodPressureJournalScheduleTimeIntervalReadFrom
+ _HDCodableBloodPressureJournalStateReadFrom
+ _OBJC_CLASS_$_HDCodableBloodPressureJournal
+ _OBJC_CLASS_$_HDCodableBloodPressureJournalScheduleTimeInterval
+ _OBJC_CLASS_$_HDCodableBloodPressureJournalState
+ _OBJC_METACLASS_$_HDCodableBloodPressureJournal
+ _OBJC_METACLASS_$_HDCodableBloodPressureJournalScheduleTimeInterval
+ _OBJC_METACLASS_$_HDCodableBloodPressureJournalState
+ __OBJC_$_CLASS_METHODS_HDCodableBloodPressureJournal
+ __OBJC_$_CLASS_METHODS_HDCodableBloodPressureJournalState
+ __OBJC_$_INSTANCE_METHODS_HDCodableBloodPressureJournal
+ __OBJC_$_INSTANCE_METHODS_HDCodableBloodPressureJournalScheduleTimeInterval
+ __OBJC_$_INSTANCE_METHODS_HDCodableBloodPressureJournalState
+ __OBJC_$_INSTANCE_VARIABLES_HDCodableBloodPressureJournal
+ __OBJC_$_INSTANCE_VARIABLES_HDCodableBloodPressureJournalScheduleTimeInterval
+ __OBJC_$_INSTANCE_VARIABLES_HDCodableBloodPressureJournalState
+ __OBJC_$_PROP_LIST_HDCodableBloodPressureJournal
+ __OBJC_$_PROP_LIST_HDCodableBloodPressureJournalScheduleTimeInterval
+ __OBJC_$_PROP_LIST_HDCodableBloodPressureJournalState
+ __OBJC_CLASS_PROTOCOLS_$_HDCodableBloodPressureJournal
+ __OBJC_CLASS_PROTOCOLS_$_HDCodableBloodPressureJournalScheduleTimeInterval
+ __OBJC_CLASS_PROTOCOLS_$_HDCodableBloodPressureJournalState
+ __OBJC_CLASS_RO_$_HDCodableBloodPressureJournal
+ __OBJC_CLASS_RO_$_HDCodableBloodPressureJournalScheduleTimeInterval
+ __OBJC_CLASS_RO_$_HDCodableBloodPressureJournalState
+ __OBJC_METACLASS_RO_$_HDCodableBloodPressureJournal
+ __OBJC_METACLASS_RO_$_HDCodableBloodPressureJournalScheduleTimeInterval
+ __OBJC_METACLASS_RO_$_HDCodableBloodPressureJournalState
+ ___swift_memcpy4_4
+ _kHKAgeGatingKeyEnableBloodPressureClassification
+ _kHKBloodPressureClassificationAgeGatingAge
+ _objc_msgSend$addBloodPressureJournal:
+ _objc_msgSend$addTimeInterval:
+ _objc_msgSend$bloodPressureJournalAtIndex:
+ _objc_msgSend$bloodPressureJournalsCount
+ _objc_msgSend$chutney
+ _objc_msgSend$clearBloodPressureJournals
+ _objc_msgSend$clearTimeIntervals
+ _objc_msgSend$hermit
+ _objc_msgSend$setScheduledTime:
+ _objc_msgSend$timeIntervalAtIndex:
+ _objc_msgSend$timeIntervalsCount
CStrings:
+ "BedTime"
+ "HDCodableBloodPressureJournal"
+ "HDCodableBloodPressureJournalScheduleTimeInterval"
+ "HDCodableBloodPressureJournalState"
+ "LearnHypertensionRisk"
+ "MonitorHypertension"
+ "R"
+ "StringAsDayWindowType:"
+ "StringAsJournalState:"
+ "StringAsJournalType:"
+ "StringAsScheduleType:"
+ "T@\"HDCodableDateComponents\",&,N,V_scheduledTime"
+ "T@\"NSMutableArray\",&,N,V_bloodPressureJournals"
+ "T@\"NSMutableArray\",&,N,V_timeIntervals"
+ "Ti,N,V_dayWindowType"
+ "Ti,N,V_journalState"
+ "Ti,N,V_journalType"
+ "Ti,N,V_scheduleType"
+ "TypicalDay"
+ "UserDefined"
+ "WakeUp"
+ "_bloodPressureJournals"
+ "_dayWindowType"
+ "_journalState"
+ "_scheduleType"
+ "_scheduledTime"
+ "_timeIntervals"
+ "addBloodPressureJournal:"
+ "addTimeInterval:"
+ "bloodPressureJournal"
+ "bloodPressureJournalAtIndex:"
+ "bloodPressureJournalType"
+ "bloodPressureJournals"
+ "bloodPressureJournalsCount"
+ "blood_pressure_journal_notifications"
+ "chutney"
+ "clearBloodPressureJournals"
+ "clearTimeIntervals"
+ "dayWindowType"
+ "dayWindowTypeAsString:"
+ "hasDayWindowType"
+ "hasJournalState"
+ "hasJournalType"
+ "hasScheduleType"
+ "hasScheduledTime"
+ "hermit"
+ "hypertension_notifications"
+ "journalState"
+ "journalStateAsString:"
+ "journalTypeAsString:"
+ "scheduleType"
+ "scheduleTypeAsString:"
+ "scheduledTime"
+ "setBloodPressureJournals:"
+ "setDayWindowType:"
+ "setHasDayWindowType:"
+ "setHasJournalState:"
+ "setHasJournalType:"
+ "setHasScheduleType:"
+ "setJournalState:"
+ "setScheduleType:"
+ "setScheduledTime:"
+ "setTimeIntervals:"
+ "timeIntervalAtIndex:"
+ "timeIntervalType"
+ "timeIntervals"
+ "timeIntervalsCount"
+ "{?=\"dayWindowType\"b1}"
+ "{?=\"endDate\"b1\"startDate\"b1\"timestamp\"b1\"journalState\"b1\"journalType\"b1\"scheduleType\"b1}"

```
