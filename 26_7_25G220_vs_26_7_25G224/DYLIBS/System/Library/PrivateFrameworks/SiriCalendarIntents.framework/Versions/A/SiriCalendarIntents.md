## SiriCalendarIntents

> `/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/Versions/A/SiriCalendarIntents`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

 3520.30.1.0.0
-  __TEXT.__text: 0x12ed04
-  __TEXT.__auth_stubs: 0x4980
+  __TEXT.__text: 0x125ee8
+  __TEXT.__auth_stubs: 0x4840
   __TEXT.__objc_methlist: 0x484
-  __TEXT.__const: 0xf7f6
+  __TEXT.__const: 0xf536
   __TEXT.__cstring: 0x1cd4
-  __TEXT.__constg_swiftt: 0x4620
-  __TEXT.__swift5_typeref: 0x4724
+  __TEXT.__constg_swiftt: 0x4594
+  __TEXT.__swift5_typeref: 0x4668
   __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x2d31
-  __TEXT.__swift5_fieldmd: 0x3ec4
-  __TEXT.__swift5_assocty: 0xae8
-  __TEXT.__swift5_proto: 0xc28
-  __TEXT.__swift5_types: 0x458
-  __TEXT.__oslogstring: 0xa131
-  __TEXT.__swift_as_entry: 0x6bc
-  __TEXT.__swift_as_ret: 0x740
+  __TEXT.__swift5_reflstr: 0x2cf1
+  __TEXT.__swift5_fieldmd: 0x3e44
+  __TEXT.__swift5_assocty: 0xab8
+  __TEXT.__swift5_proto: 0xc14
+  __TEXT.__swift5_types: 0x448
+  __TEXT.__swift_as_entry: 0x6a4
+  __TEXT.__swift_as_ret: 0x720
+  __TEXT.__oslogstring: 0x9a31
   __TEXT.__swift5_protos: 0x9c
-  __TEXT.__swift5_capture: 0x88c
+  __TEXT.__swift5_capture: 0x848
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__unwind_info: 0x5458
-  __TEXT.__eh_frame: 0xc380
+  __TEXT.__unwind_info: 0x52a8
+  __TEXT.__eh_frame: 0xbd98
   __TEXT.__objc_classname: 0xa79
-  __TEXT.__objc_methname: 0x1f49
+  __TEXT.__objc_methname: 0x1f39
   __TEXT.__objc_methtype: 0x76b
-  __TEXT.__objc_stubs: 0x1800
-  __DATA_CONST.__got: 0xb28
+  __TEXT.__objc_stubs: 0x17e0
+  __DATA_CONST.__got: 0xb08
   __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x790
+  __DATA_CONST.__objc_selrefs: 0x788
   __DATA_CONST.__objc_protorefs: 0x38
-  __AUTH_CONST.__auth_got: 0x24c8
-  __AUTH_CONST.__const: 0x9168
+  __AUTH_CONST.__auth_got: 0x2428
+  __AUTH_CONST.__const: 0x8f18
   __AUTH_CONST.__objc_const: 0x2ab8
   __AUTH.__objc_data: 0x988
   __AUTH.__data: 0x2958
-  __DATA.__data: 0x33a8
+  __DATA.__data: 0x3310
   __DATA.__common: 0x340
   __DATA_DIRTY.__objc_data: 0x90
   __DATA_DIRTY.__data: 0x10f8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7423
-  Symbols:   2330
-  CStrings:  1216
+  Functions: 7306
+  Symbols:   2309
+  CStrings:  1195
 
Symbols:
- _associated conformance 19SiriCalendarIntents16EventEntityErrorOSHAASQ
- _objc_msgSend$dateInterval
- _symbolic Sny_____G 10Foundation4DateV
- _symbolic _____ 19SiriCalendarIntents04OpenB4ViewO
- _symbolic _____ 19SiriCalendarIntents04OpenB4ViewO14OutputProviderV
- _symbolic _____ 19SiriCalendarIntents13NoOpAppIntentV
- _symbolic _____ 19SiriCalendarIntents16EventEntityErrorO
- _symbolic _____ 19SiriCalendarIntents17OpenDateAppIntentV
- _symbolic _____5lower_AA5uppert 10Foundation4DateV
- _symbolic _____Sg 10Foundation12DateIntervalV
- _symbolic _____Sg 10Foundation4DateV11FormatStyleV04TimeD0V
- _symbolic _____Sg 10Foundation4DateV11FormatStyleV0bD0V
- _symbolic ______pSg 18AppIntentsServices0A20IntentRepresentationP
- _symbolic _____ySSG 18AppIntentsServices15IntentParameterC
- _symbolic _____ySSSgG s23_ContiguousArrayStorageC
- _symbolic _____ySay_____GG 18AppIntentsServices15IntentParameterC 012SiriCalendarB025EventEntityRepresentationC
- _symbolic _____y_____G 18AppIntentsServices15IntentParameterC 012SiriCalendarB00gA18ViewRepresentationO
- _symbolic _____y_____G 18AppIntentsServices15IntentParameterC 10Foundation4DateV
- _symbolic _____y_____SgG 18AppIntentsServices15IntentParameterC 012SiriCalendarB00gA18ViewRepresentationO
- _type_layout_string 19SiriCalendarIntents04OpenB4ViewO14OutputProviderV
- _type_layout_string 19SiriCalendarIntents17OpenDateAppIntentV
CStrings:
+ "[CalendarTvOSFlowProvider] openCalendarView not supported on this platform"
+ "com.apple.mobilecal"
- "[CalendarTvOSFlowProvider] Open calendar view intent is not supported on this platform returning noFlow"
- "[CalendarTvOSFlowProvider] Using open calendar view flow for on device execution"
- "[ConfirmConflictStrategy] Creating snippet for create and compose with conflicting event"
- "[ConfirmParticipantStrategy] Making compose and create snippet"
- "[CreateEvent HandleIntentStrategy] Using OpenDate App Intent"
- "[EventEntityRepresentation] Attempted to create an EventEntityRepresentation without identifier"
- "[EventReadingStrategy] Intent has more than date query or the date query is not entire days, using ListEventsIntent"
- "[EventReadingStrategy] Intent is date search only or all results are on the same day, showing OpenDate for %s"
- "[EventReadingStrategy] Not using an app intent for date introduction"
- "[EventReadingStrategy] Running %s Intent again to make sure emphasis ids are sent."
- "[EventReadingStrategy] shouldUseOpenDateIntent: %{bool}d, dateOnlySearch: %{bool}d, rangeIsAllDay: %{bool}d, allOnSameDay: %{bool}d"
- "[FindEvents.ResponseStrategy] Adjusting targetDate for multiday event, target: %s, eventStart: %s, searchStart: %s"
- "[FindEvents.ResponseStrategy] Making multi event output with ListEventsIntent"
- "[FindEvents.ResponseStrategy] Making multi event output with OpenDateIntent"
- "[FindEvents.ResponseStrategy] Making open OpenDateAppIntent for single event result"
- "[OpenCalendarView.OutputProvider] Making output for %s"
- "[OpenCalendarView.OutputProvider] Using OpenCalendarViewAppIntent"
- "[OpenCalendarView.OutputProvider] Using OpenDateIntent"
- "[OutputHelper] Unable to send App Intent on this platform"
- "[UpdateEvent HandleIntentStrategy] Using OpenEventDetailsIntent App Intent"
- "com.apple.CalendarPebble"
- "dateInterval"
- "isAllDay: %{bool}d, dateInterval: %s"
```
