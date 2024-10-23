## SiriCalendarIntents

> `/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents`

```diff

-3401.2.1.0.0
-  __TEXT.__text: 0x12ef20
-  __TEXT.__auth_stubs: 0x4820
+3402.29.1.1.1
+  __TEXT.__text: 0x12b830
+  __TEXT.__auth_stubs: 0x48d0
   __TEXT.__objc_methlist: 0x1a4
-  __TEXT.__const: 0xbfda
-  __TEXT.__cstring: 0x34c6
-  __TEXT.__constg_swiftt: 0x4794
-  __TEXT.__swift5_typeref: 0x434e
+  __TEXT.__const: 0xc49a
+  __TEXT.__cstring: 0x3366
+  __TEXT.__constg_swiftt: 0x44c0
+  __TEXT.__swift5_typeref: 0x4514
   __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_reflstr: 0x2c29
-  __TEXT.__swift5_fieldmd: 0x3bc8
-  __TEXT.__swift5_assocty: 0xac0
-  __TEXT.__swift5_proto: 0xb68
-  __TEXT.__swift5_types: 0x41c
-  __TEXT.__swift5_capture: 0x814
+  __TEXT.__swift5_reflstr: 0x2bd9
+  __TEXT.__swift5_fieldmd: 0x3cdc
+  __TEXT.__swift5_assocty: 0xa58
+  __TEXT.__swift5_proto: 0xbd8
+  __TEXT.__swift5_types: 0x430
+  __TEXT.__swift5_capture: 0x7e8
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__oslogstring: 0x9911
-  __TEXT.__swift5_protos: 0x94
-  __TEXT.__unwind_info: 0x5be8
-  __TEXT.__eh_frame: 0xd3e4
-  __TEXT.__objc_classname: 0x109
-  __TEXT.__objc_methname: 0x1874
-  __TEXT.__objc_methtype: 0x713
-  __DATA_CONST.__got: 0xa88
-  __DATA_CONST.__const: 0x1a8
-  __DATA_CONST.__objc_classlist: 0x128
-  __DATA_CONST.__objc_protolist: 0xf0
+  __TEXT.__oslogstring: 0x92b1
+  __TEXT.__swift5_protos: 0x98
+  __TEXT.__unwind_info: 0x59a8
+  __TEXT.__eh_frame: 0xc1d4
+  __TEXT.__objc_classname: 0x90
+  __TEXT.__objc_methname: 0x15b6
+  __TEXT.__objc_methtype: 0x656
+  __DATA_CONST.__got: 0xa50
+  __DATA_CONST.__const: 0x1c8
+  __DATA_CONST.__objc_classlist: 0x108
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7c0
-  __DATA_CONST.__objc_protorefs: 0x78
-  __AUTH_CONST.__auth_got: 0x2410
-  __AUTH_CONST.__auth_ptr: 0x1668
-  __AUTH_CONST.__const: 0x88f8
-  __AUTH_CONST.__objc_const: 0x35e8
-  __AUTH.__objc_data: 0xb60
-  __AUTH.__data: 0x3880
-  __DATA.__data: 0x4718
-  __DATA.__bss: 0x14a30
-  __DATA.__common: 0x3d8
+  __DATA_CONST.__objc_selrefs: 0x6d8
+  __DATA_CONST.__objc_protorefs: 0x38
+  __AUTH_CONST.__auth_got: 0x2468
+  __AUTH_CONST.__auth_ptr: 0x1880
+  __AUTH_CONST.__const: 0x8b40
+  __AUTH_CONST.__objc_const: 0x2f88
+  __AUTH.__objc_data: 0xa18
+  __AUTH.__data: 0x3588
+  __DATA.__data: 0x43d8
+  __DATA.__bss: 0x157b0
+  __DATA.__common: 0x3c0
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/EventKit.framework/EventKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/MapKit.framework/MapKit
+  - /System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation
+  - /System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit
   - /System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7304
-  Symbols:   2547
-  CStrings:  1314
+  Functions: 7326
+  Symbols:   2439
+  CStrings:  1229
 
Symbols:
- _OBJC_CLASS_$_SACalendarShowNextEvent
- _OBJC_CLASS_$_SASTButtonItem
- _OBJC_CLASS_$_SASTCardItem
- _OBJC_CLASS_$_SASTColumnDataListItem
- _OBJC_CLASS_$_SASTCommandTemplateAction
- _OBJC_CLASS_$_SASTItemGroup
- _OBJC_CLASS_$_SAUIColor
- _OBJC_CLASS_$_SAUIDecoratedText
CStrings:
+ "CalendarFlowPluginCompanionExecutionOnly"
+ "CarPlaySnippets"
+ "ComposeEventIntent"
+ "ExecuteOnRemote failed with an error=%!s(MISSING): Possible server redirect. Will redirect this input to server as a fallback."
+ "ExecuteOnRemote flow completed with: %!s(MISSING)"
+ "ExecuteOnRemote guard flows failed, assuming a server redirect or handoff should have happened, doing nothing."
+ "SiriCalendar"
+ "[CalendarDateTimeResolver] DateTimeQuery Occurring In: %!s(MISSING)"
+ "[CalendarFlowProvider] Open Calendar View not yet supported on this platform"
+ "[CalendarTvOSFlowProvider] Using execute on remote for non open calendar view task"
+ "[CalendarTvOSFlowProvider] openCalendarView not supported on this platform"
+ "[CalendarTvOSFlowProvider] returning no flow for unknown parse %!s(MISSING)"
+ "[CreateEvent HandleIntentStrategy] Unexpectedly found nil for createdEvent in intent response"
+ "[OutputHelper] overriding default response mode of %!s(MISSING) to %!s(MISSING)"
+ "_TtC19SiriCalendarIntents21SimpleHandoffStrategy"
+ "_TtC19SiriCalendarIntents23RedirectToCompanionFlow"
+ "_TtC19SiriCalendarIntents25EventEntityRepresentation"
+ "conflictConfirmation"
+ "endDay"
+ "eventNameWithParticipants"
+ "identifierString"
+ "participantInvitation"
+ "recurrenceFrequency"
+ "recurrenceIdentifier"
+ "startDay"
- "@\"NSArray\"16@0:8"
- "@\"NSMutableDictionary\"16@0:8"
- "@24@0:8@\"NSDictionary\"16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8@\"NSDictionary\"16@\"<AceContext>\"24"
- "@32@0:8@16@24"
- "AceObject"
- "Common#EventTimeOnWatch"
- "Common#IntentUnsupportedOnDevice"
- "CreateEvent#ConfirmCreateRecurringEvent"
- "NSCopying"
- "NSMutableCopying"
- "ResponseFramework"
- "SAAceCommand"
- "SAAceReferable"
- "SAAceSerializable"
- "SAClientBoundCommand"
- "SASTTemplateItem"
- "SMART"
- "T@\"NSArray\",C,N"
- "T@\"NSString\",C,N"
- "[CalendarDateTimeResolving] DateTimeQuery Occurring In: %!s(MISSING)"
- "[CalendarDateTimeResolving] DateTimeQuery: %!s(MISSING)"
- "[CalendarFlowProvider] Using punch out to next event on watchOS"
- "[CalendarFlowProvider] delete event is unsupported on watch returning unsupported flow"
- "[CalendarFlowProvider] update event is unsupported on watch returning unsupported flow"
- "[ConfirmationParsing] Returning .cancel() for rejected confirmation"
- "[ConfirmationParsing] Returning .handle() for confirmed confirmation"
- "[CreateEvent HandleIntentStrategy] Using legacy snippet for watch"
- "[CreateEvent+WatchConflictConfirmationStrategy] Did not get confirmed ConfirmationTask from parse: %!s(MISSING)"
- "[CreateEvent+WatchConflictConfirmationStrategy] Intent date time range updated with confirmed value"
- "[CreateEvent+WatchConflictConfirmationStrategy] Making prompt for confirmation"
- "[CreateEvent.FlowProducers] Adding custom confirm intent and conflict step for watchOS"
- "[CreateEvent.IntentHander] Failed to run title template, prompting for title. %!s(MISSING)"
- "[CreateEvent.IntentHander] No title on intent, using noun %!s(MISSING) as title"
- "[CreateEvent.OutputProvider] Unexpectedly found nil for createdEvent in intent response"
- "[CreateEvent.WatchConfirmIntentStrategy] Did not get ConfirmationTask from parse: %!s(MISSING)"
- "[CreateEvent.WatchConfirmIntentStrategy] Making prompt for confirmation"
- "[CreateEvent.WatchConfirmIntentStrategy] Making prompt for confirmation of a recurring event"
- "[FindEvents.FlowProducers] Device is watch, using watch specific handle intent strategy"
- "[FindEvents.WatchHandleIntentStrategy] Creating empty result set output"
- "[FindEvents.WatchHandleIntentStrategy] Creating watch specific intent handled response"
- "[FindEvents.WatchHandleIntentStrategy] Found no events returning not found dialog"
- "[FindEvents.WatchHandleIntentStrategy] Got an invalid calendar without a start date"
- "[FindEvents.WatchHandleIntentStrategy] Only found one event, punching out to it"
- "[FindEvents.WatchHandleIntentStrategy] Should punchout for watch event"
- "[ParticipantDisambiguationFlowStrategy] Creating participant disambiguation output with smart snippet."
- "[ParticipantDisambiguationFlowStrategy] Creating participant handle disambiguation output with smart snippet."
- "[PunchoutToNextEventFlow] Sending SACalendarShowNextEvent ace command"
- "_TtC19SiriCalendarIntents23CalendarSelectableEvent"
- "_TtC19SiriCalendarIntents26CalendarSelectableLocation"
- "_TtC19SiriCalendarIntents31CalendarSelectableDateTimeRange"
- "_TtCC19SiriCalendarIntents23CalendarSelectableEvent7Builder"
- "_TtCC19SiriCalendarIntents26CalendarSelectableLocation7Builder"
- "_TtCC19SiriCalendarIntents31CalendarSelectableDateTimeRange7Builder"
- "aceId"
- "appId"
- "calendar.SelectableDateTimeRange"
- "calendar.SelectableEvent"
- "calendar.SelectableLocation"
- "callbacks"
- "contactResolutionPatternGenerator"
- "copyWithZone:"
- "dictionary"
- "displayAppName"
- "encodedClassName"
- "eventOccurrenceID"
- "eventView"
- "fullSpeak"
- "groupIdentifier"
- "id"
- "initWithDictionary:"
- "initWithDictionary:context:"
- "isApprovedForGrading"
- "meta"
- "mutableCopyWithZone:"
- "properties"
- "refId"
- "requiresResponse"
- "selectAction"
- "setAceId:"
- "setAction:"
- "setAlpha:"
- "setAppId:"
- "setBackgroundColor:"
- "setBlueValue:"
- "setCallbacks:"
- "setCentered:"
- "setCommands:"
- "setDecoratedLabel:"
- "setDecoratedRows:"
- "setFootnote:"
- "setGreenValue:"
- "setLabel:"
- "setLabelTextColor:"
- "setRedValue:"
- "setRefId:"
- "setTemplateItems:"
- "setText:"
- "setTitleBackgroundColor:"
- "setTitleTextColor:"
- "spokenOnly"
- "startDateTimeOnly"
- "supportingPrint"
- "supportingSpeak"
- "templateItems"
- "unfilteredFullPrint"
- "unfilteredFullSpeak"
- "unfilteredSupportingPrint"
- "unfilteredSupportingSpeak"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSString\"16"

```
