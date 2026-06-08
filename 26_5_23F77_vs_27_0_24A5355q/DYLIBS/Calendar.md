## Calendar

> `/System/Library/Assistant/Plugins/Calendar.assistantBundle/Calendar`

```diff

-912.4.1.0.0
-  __TEXT.__text: 0x689c
-  __TEXT.__auth_stubs: 0x2b0
+919.0.0.0.0
+  __TEXT.__text: 0x60a8
   __TEXT.__objc_methlist: 0x2e4
   __TEXT.__const: 0x88
   __TEXT.__oslogstring: 0xe69
-  __TEXT.__cstring: 0x512
-  __TEXT.__unwind_info: 0x148
-  __TEXT.__objc_classname: 0xd1
-  __TEXT.__objc_methname: 0xacc
-  __TEXT.__objc_methtype: 0x211
-  __TEXT.__objc_stubs: 0x1000
-  __DATA_CONST.__got: 0xe8
+  __TEXT.__cstring: 0x514
+  __TEXT.__unwind_info: 0x130
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4c8
-  __AUTH_CONST.__auth_got: 0x160
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x678
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x128

   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C6C79E09-5EAE-3367-BE92-7FD4447C0B97
-  Functions: 127
-  Symbols:   99
-  CStrings:  337
+  UUID: 58338F4A-3491-39B3-8D0B-90FF464734ED
+  Functions: 125
+  Symbols:   102
+  CStrings:  139
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_retain_x23
- _objc_retain_x25
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"EKEventStore\""
- "@\"EKEventStore\"16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSDictionary\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "AFServiceCommand"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CalAssistant"
- "CalAssistantBundle"
- "CalAssistantCommand"
- "CalAssistantEventCommit"
- "CalAssistantEventDelete"
- "CalAssistantEventRetrieve"
- "CalAssistantEventSearch"
- "CalAssistantGetDefaultCalendar"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"EKEventStore\",&,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "URLWithString:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_ca_eventStoreWithError:"
- "_ca_performBlock:"
- "_commitEvent:serviceHelper:"
- "_deleteEvent:"
- "_eventStore"
- "_eventWithURI:checkValid:"
- "_validate"
- "_validateEvent:"
- "_visibleCalendars"
- "acquireDefaultCalendarForNewEvents"
- "addAlarm:"
- "addAttendee:"
- "addObject:"
- "addObjectsFromArray:"
- "alerts"
- "allDay"
- "array"
- "arrayWithObject:"
- "assistantLocalizedStringForKey:table:bundle:"
- "attendeeWithName:emailAddress:phoneNumber:url:"
- "attendees"
- "autorelease"
- "boolValue"
- "bundle"
- "bundleForClass:"
- "calendar"
- "class"
- "compare:"
- "compare:options:"
- "conformsToProtocol:"
- "constraints"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "data"
- "dateWithTimeIntervalSinceReferenceDate:"
- "debugDescription"
- "description"
- "dictionary"
- "displayText"
- "doubleValue"
- "emailAddress"
- "emails"
- "endCount"
- "endDate"
- "eventStore"
- "eventWithEventStore:"
- "eventsMatchingPredicate:"
- "externalID"
- "externalIdentifierFromAssistantID:"
- "externalURI"
- "frequency"
- "hash"
- "identifier"
- "identifiers"
- "includeRecurrences"
- "initRecurrenceWithFrequency:interval:end:"
- "initWithAceCalendarSource:"
- "initWithCapacity:"
- "initWithDictionary:"
- "initWithEKOptions:"
- "initWithEndDate:"
- "initWithEventStore:visibilityChangedCallback:queue:"
- "initWithOccurrenceCount:"
- "initWithReason:"
- "initWithRelativeOffset:"
- "initWithResults:"
- "intValue"
- "interval"
- "isAllDay"
- "isDefaultSchedulingCalendar"
- "isEditable"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "limit"
- "localizedDescription"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "location"
- "name"
- "notes"
- "numberWithBool:"
- "object"
- "objectAtIndex:"
- "occurrenceCount"
- "participants"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWithCompletion:"
- "performWithCompletion:serviceHelper:"
- "performWithCompletion:serviceHelper:executionInfo:"
- "predicateForAssistantEventSearchWithTimeZone:startDate:endDate:title:location:notes:participants:calendars:limit:"
- "recurrenceEnd"
- "recurrenceRules"
- "recurrences"
- "release"
- "removeEvent:span:commit:error:"
- "requestFullAccessToEventsWithCompletion:"
- "requiresOutgoingInvitationsInDefaultCalendar"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "saveEvent:span:commit:error:"
- "scheme"
- "self"
- "selfParticipantStatus"
- "setAccountIdentifier:"
- "setAccountName:"
- "setAllDay:"
- "setAttendees:"
- "setCalendar:"
- "setCalendarId:"
- "setCalendarPunchoutURI:"
- "setData:"
- "setDisplayText:"
- "setEndCount:"
- "setEndDate:"
- "setEventStore:"
- "setFrequency:"
- "setIdentifier:"
- "setInterval:"
- "setLocation:"
- "setNotes:"
- "setObjects:"
- "setParticipantRole:"
- "setParticipantStatus:"
- "setParticipantType:"
- "setReadOnly:"
- "setRecurrenceRules:"
- "setRecurrences:"
- "setRemote:"
- "setSelfParticipantStatus:"
- "setStartDate:"
- "setStatus:"
- "setStrict:"
- "setTimeZone:"
- "setTimeZoneId:"
- "setTitle:"
- "source"
- "sourceType"
- "startDate"
- "status"
- "stringWithFormat:"
- "superclass"
- "supportsOutgoingInvitations"
- "timeIntervalSinceReferenceDate"
- "timeZoneId"
- "title"
- "v16@0:8"
- "v24@0:8@\"EKEventStore\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v32@0:8@?16@24"
- "v32@0:8@?<v@?@\"NSDictionary\">16@\"<AFServiceHelper>\"24"
- "v40@0:8@?16@24@32"
- "v40@0:8@?<v@?@\"NSDictionary\">16@\"<AFServiceHelper>\"24@\"AFCommandExecutionInfo\"32"
- "visibleCalendars"
- "zone"

```
