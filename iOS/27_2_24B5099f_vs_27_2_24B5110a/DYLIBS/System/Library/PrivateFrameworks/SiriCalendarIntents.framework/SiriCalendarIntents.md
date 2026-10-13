## SiriCalendarIntents

> `/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents`

```diff

-3605.9.1.0.0
-  __TEXT.__text: 0x10e62c
+3605.10.1.0.0
+  __TEXT.__text: 0x119d80
   __TEXT.__objc_methlist: 0x484
-  __TEXT.__const: 0xf616
-  __TEXT.__cstring: 0x1ce4
-  __TEXT.__constg_swiftt: 0x45c0
-  __TEXT.__swift5_typeref: 0x4768
+  __TEXT.__const: 0xf9c6
+  __TEXT.__cstring: 0x1d44
+  __TEXT.__constg_swiftt: 0x4684
+  __TEXT.__swift5_typeref: 0x4830
   __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x2d21
-  __TEXT.__swift5_fieldmd: 0x3e90
-  __TEXT.__swift5_assocty: 0xab8
-  __TEXT.__swift5_proto: 0xc28
-  __TEXT.__swift5_types: 0x44c
-  __TEXT.__swift_as_entry: 0x6a4
-  __TEXT.__swift_as_ret: 0x720
-  __TEXT.__swift_as_cont: 0x698
-  __TEXT.__oslogstring: 0x99b1
-  __TEXT.__swift5_capture: 0xd98
+  __TEXT.__swift5_reflstr: 0x2d91
+  __TEXT.__swift5_fieldmd: 0x3f54
+  __TEXT.__swift5_assocty: 0xb18
+  __TEXT.__swift5_proto: 0xc44
+  __TEXT.__swift5_types: 0x464
+  __TEXT.__oslogstring: 0xa071
+  __TEXT.__swift_as_entry: 0x6bc
+  __TEXT.__swift_as_ret: 0x76c
+  __TEXT.__swift_as_cont: 0x720
+  __TEXT.__swift5_capture: 0xddc
   __TEXT.__swift5_protos: 0x9c
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__unwind_info: 0x5e90
-  __TEXT.__eh_frame: 0xb030
+  __TEXT.__unwind_info: 0x6140
+  __TEXT.__eh_frame: 0xb9f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7c8
+  __DATA_CONST.__objc_selrefs: 0x7d0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x9cf0
+  __AUTH_CONST.__const: 0x9fe8
   __AUTH_CONST.__objc_const: 0x2ab8
-  __AUTH_CONST.__auth_got: 0x2598
+  __AUTH_CONST.__auth_got: 0x2638
   __AUTH.__objc_data: 0x988
   __AUTH.__data: 0x2958
-  __DATA.__data: 0x32c8
+  __DATA.__data: 0x33a0
   __DATA.__common: 0x340
   __DATA_DIRTY.__objc_data: 0x90
   __DATA_DIRTY.__data: 0x1100

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7336
-  Symbols:   2189
-  CStrings:  839
+  Functions: 7512
+  Symbols:   2212
+  CStrings:  861
 
Symbols:
+ _associated conformance 19SiriCalendarIntents16EventEntityErrorOSHAASQ
+ _symbolic Sny_____G 10Foundation4DateV
+ _symbolic _____ 19SiriCalendarIntents04OpenB13ViewAppIntentV
+ _symbolic _____ 19SiriCalendarIntents04OpenB4ViewO
+ _symbolic _____ 19SiriCalendarIntents04OpenB4ViewO14OutputProviderV
+ _symbolic _____ 19SiriCalendarIntents13NoOpAppIntentV
+ _symbolic _____ 19SiriCalendarIntents16EventEntityErrorO
+ _symbolic _____ 19SiriCalendarIntents17OpenDateAppIntentV
+ _symbolic _____ 19SiriCalendarIntents19ListEventsAppIntentV
+ _symbolic _____5lower_AA5uppert 10Foundation4DateV
+ _symbolic _____Sg 10Foundation12DateIntervalV
+ _symbolic _____Sg 10Foundation4DateV11FormatStyleV04TimeD0V
+ _symbolic _____Sg 10Foundation4DateV11FormatStyleV0bD0V
+ _symbolic ______pSg 18AppIntentsServices0A20IntentRepresentationP
+ _symbolic _____ySSG 18AppIntentsServices15IntentParameterC
+ _symbolic _____ySSSgG s23_ContiguousArrayStorageC
+ _symbolic _____ySay_____GG 18AppIntentsServices15IntentParameterC 012SiriCalendarB025EventEntityRepresentationC
+ _symbolic _____y_____G 18AppIntentsServices15IntentParameterC 012SiriCalendarB00gA18ViewRepresentationO
+ _symbolic _____y_____G 18AppIntentsServices15IntentParameterC 10Foundation4DateV
+ _symbolic _____y_____SgG 18AppIntentsServices15IntentParameterC 012SiriCalendarB00gA18ViewRepresentationO
+ _type_layout_string 19SiriCalendarIntents04OpenB13ViewAppIntentV
+ _type_layout_string 19SiriCalendarIntents04OpenB4ViewO14OutputProviderV
+ _type_layout_string 19SiriCalendarIntents17OpenDateAppIntentV
+ _type_layout_string 19SiriCalendarIntents19ListEventsAppIntentV
- ___swift_project_boxed_opaque_existential_2Tm
CStrings:
+ "ListEventsIntent"
+ "OpenCalendarViewIntent"
+ "[CalendarTvOSFlowProvider] Open calendar view intent is not supported on this platform returning noFlow"
+ "[CalendarTvOSFlowProvider] Using open calendar view flow for on device execution"
+ "[ConfirmConflictStrategy] Creating snippet for create and compose with conflicting event"
+ "[ConfirmParticipantStrategy] Making compose and create snippet"
+ "[CreateEvent HandleIntentStrategy] Using OpenDate App Intent"
+ "[EventEntityRepresentation] Attempted to create an EventEntityRepresentation without identifier"
+ "[EventReadingStrategy] Intent has more than date query or the date query is not entire days, using ListEventsIntent"
+ "[EventReadingStrategy] Intent is date search only or all results are on the same day, showing OpenDate for %s"
+ "[EventReadingStrategy] Not using an app intent for date introduction"
+ "[EventReadingStrategy] Running %s Intent again to make sure emphasis ids are sent."
+ "[EventReadingStrategy] shouldUseOpenDateIntent: %{bool}d, dateOnlySearch: %{bool}d, rangeIsAllDay: %{bool}d, allOnSameDay: %{bool}d"
+ "[FindEvents.ResponseStrategy] Adjusting targetDate for multiday event, target: %s, eventStart: %s, searchStart: %s"
+ "[FindEvents.ResponseStrategy] Making multi event output with ListEventsIntent"
+ "[FindEvents.ResponseStrategy] Making multi event output with OpenDateIntent"
+ "[FindEvents.ResponseStrategy] Making open OpenDateAppIntent for single event result"
+ "[OpenCalendarView.OutputProvider] Making output for %s"
+ "[OpenCalendarView.OutputProvider] Using OpenCalendarViewAppIntent"
+ "[OpenCalendarView.OutputProvider] Using OpenDateIntent"
+ "[UpdateEvent HandleIntentStrategy] Using OpenEventDetailsIntent App Intent"
+ "com.apple.CalendarPebble"
+ "isAllDay: %{bool}d, dateInterval: %s"
- "[CalendarTvOSFlowProvider] openCalendarView not supported on this platform"
```
