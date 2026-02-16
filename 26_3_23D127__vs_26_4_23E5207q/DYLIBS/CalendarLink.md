## CalendarLink

> `/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink`

```diff

-1279.2.5.0.0
-  __TEXT.__text: 0xf0680
-  __TEXT.__auth_stubs: 0x2d00
-  __TEXT.__objc_methlist: 0x49c
-  __TEXT.__const: 0xfc68
+1279.4.15.0.0
+  __TEXT.__text: 0xff964
+  __TEXT.__auth_stubs: 0x2e60
+  __TEXT.__objc_methlist: 0x5ac
+  __TEXT.__const: 0x10228
   __TEXT.__gcc_except_tab: 0x44
-  __TEXT.__cstring: 0xbe50
+  __TEXT.__cstring: 0xb890
   __TEXT.__dlopen_cstrs: 0x141
-  __TEXT.__swift5_typeref: 0x4852
-  __TEXT.__swift5_reflstr: 0x271f
-  __TEXT.__swift5_assocty: 0x1570
-  __TEXT.__constg_swiftt: 0x2058
-  __TEXT.__swift5_fieldmd: 0x2174
-  __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_proto: 0xce4
-  __TEXT.__swift5_types: 0x1f4
-  __TEXT.__swift_as_entry: 0x2a0
-  __TEXT.__swift_as_ret: 0x204
+  __TEXT.__swift5_typeref: 0x49c2
+  __TEXT.__swift5_reflstr: 0x285f
+  __TEXT.__swift5_assocty: 0x15e8
+  __TEXT.__constg_swiftt: 0x21d8
+  __TEXT.__swift5_fieldmd: 0x22ac
+  __TEXT.__swift5_builtin: 0xc8
+  __TEXT.__swift5_proto: 0xd10
+  __TEXT.__swift5_types: 0x214
+  __TEXT.__swift_as_entry: 0x2f0
+  __TEXT.__swift_as_ret: 0x24c
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__oslogstring: 0x2e8
+  __TEXT.__oslogstring: 0x708
+  __TEXT.__swift5_capture: 0x248
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_capture: 0x58
-  __TEXT.__unwind_info: 0x4860
-  __TEXT.__eh_frame: 0x38fc
-  __TEXT.__objc_classname: 0x161
-  __TEXT.__objc_methname: 0x188f
-  __TEXT.__objc_methtype: 0x332
-  __TEXT.__objc_stubs: 0x440
-  __DATA_CONST.__got: 0x780
-  __DATA_CONST.__const: 0x1790
-  __DATA_CONST.__objc_classlist: 0x50
+  __TEXT.__unwind_info: 0x42f8
+  __TEXT.__eh_frame: 0x46ac
+  __TEXT.__objc_classname: 0x5d8
+  __TEXT.__objc_methname: 0x1ec9
+  __TEXT.__objc_methtype: 0x4b6
+  __TEXT.__objc_stubs: 0x1f40
+  __DATA_CONST.__got: 0x848
+  __DATA_CONST.__const: 0x17a0
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8b0
+  __DATA_CONST.__objc_selrefs: 0x978
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1690
-  __AUTH_CONST.__const: 0x46d0
+  __AUTH_CONST.__auth_got: 0x1740
+  __AUTH_CONST.__const: 0x4d40
   __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__objc_const: 0x1358
-  __AUTH.__objc_data: 0x5c0
-  __AUTH.__data: 0x860
+  __AUTH_CONST.__objc_const: 0x1480
+  __AUTH.__objc_data: 0x6f8
+  __AUTH.__data: 0x780
   __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0x3960
-  __DATA.__bss: 0xf580
-  __DATA.__common: 0x100
-  __DATA_DIRTY.__objc_data: 0x1f0
-  __DATA_DIRTY.__data: 0xc98
-  __DATA_DIRTY.__bss: 0x9710
+  __DATA.__data: 0x3560
+  __DATA.__bss: 0xea00
+  __DATA.__common: 0xe8
+  __DATA_DIRTY.__objc_data: 0x2f0
+  __DATA_DIRTY.__data: 0x1418
+  __DATA_DIRTY.__bss: 0xa790
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 66769F40-20E7-3C5A-80B5-58F32212C9FC
-  Functions: 6392
-  Symbols:   2583
-  CStrings:  1351
+  UUID: D27E4B76-E918-338F-AB1B-B7095923865A
+  Functions: 6402
+  Symbols:   2924
+  CStrings:  1401
 
Symbols:
+ +[CUIKEventActionHandler handleCalendarDeletion:reportJunk:]
+ +[CUIKEventActionHandler handleEventCreation:]
+ +[CUIKEventActionHandler handleEventDeletion:span:]
+ +[CUIKEventActionHandler handleEventUpdate:span:]
+ +[CUIKEventActionHandler handleOpenCalendarEditor:]
+ +[CUIKEventActionHandler handleOpenEventDetails:]
+ +[CUIKEventActionHandler handleOpenEventEditor:]
+ -[CUIKSpotlightEntityAnnotator associateCalendarEntityWithIdentifier:withSearchableItem:]
+ _EKChangedAlarmsAdded
+ _EKChangedAlarmsModified
+ _EKChangedAlarmsRemoved
+ _EKChangedAllDay
+ _EKChangedAttendeesAdded
+ _EKChangedAttendeesModified
+ _EKChangedAttendeesRemoved
+ _EKChangedAvailability
+ _EKChangedCalendar
+ _EKChangedEndDate
+ _EKChangedNotes
+ _EKChangedPrivacy
+ _EKChangedRecurrenceRule
+ _EKChangedStartDate
+ _EKChangedTravelTime
+ _EKChangedURL
+ _OBJC_CLASS_$_CUIKEventActionHandler
+ _OBJC_CLASS_$_CUIKIntentDonation
+ _OBJC_CLASS_$_EKObjectChangeSummarizer
+ _OBJC_CLASS_$__TtC12CalendarLink18IntentDonationMock
+ _OBJC_METACLASS_$_CUIKEventActionHandler
+ _OBJC_METACLASS_$_CUIKIntentDonation
+ _OBJC_METACLASS_$__TtC12CalendarLink18IntentDonationMock
+ __Block_copy
+ __CLASS_METHODS_CUIKIntentDonation
+ __DATA_CUIKIntentDonation
+ __DATA__TtC12CalendarLink18IntentDonationMock
+ __INSTANCE_METHODS_CUIKIntentDonation
+ __INSTANCE_METHODS__TtC12CalendarLink18IntentDonationMock
+ __METACLASS_DATA_CUIKIntentDonation
+ __METACLASS_DATA__TtC12CalendarLink18IntentDonationMock
+ __OBJC_$_CLASS_METHODS_CUIKEventActionHandler
+ __OBJC_CLASS_RO_$_CUIKEventActionHandler
+ __OBJC_METACLASS_RO_$_CUIKEventActionHandler
+ ___46+[CUIKEventActionHandler handleEventCreation:]_block_invoke
+ ___48+[CUIKEventActionHandler handleOpenEventEditor:]_block_invoke
+ ___49+[CUIKEventActionHandler handleEventUpdate:span:]_block_invoke
+ ___49+[CUIKEventActionHandler handleOpenEventDetails:]_block_invoke
+ ___51+[CUIKEventActionHandler handleEventDeletion:span:]_block_invoke
+ ___51+[CUIKEventActionHandler handleOpenCalendarEditor:]_block_invoke
+ ___60+[CUIKEventActionHandler handleCalendarDeletion:reportJunk:]_block_invoke
+ ___block_literal_global.11
+ ___block_literal_global.13
+ ___block_literal_global.15
+ ___block_literal_global.17
+ ___block_literal_global.19
+ ___block_literal_global.9
+ ___swift_memcpy168_8
+ ___swift_memcpy88_8
+ _get_witness_table 10AppIntents21IntentResultContainerVy12CalendarLink11EventEntityVs5NeverOA2HGAA05OpensC0HPyHC.34
+ _get_witness_table 10AppIntents21IntentResultContainerVy12CalendarLink11EventEntityVs5NeverOA2HGAA05OpensC0HPyHC.52
+ _get_witness_table 10AppIntents21IntentResultContainerVy12CalendarLink11EventEntityVs5NeverOA2HGAA12ReturnsValueHPyHC.35
+ _get_witness_table 10AppIntents21IntentResultContainerVy12CalendarLink11EventEntityVs5NeverOA2HGAA12ReturnsValueHPyHC.53
+ _get_witness_table 10AppIntents21IntentResultContainerVys5NeverOA3EGAA0cD0HPyHC.25
+ _get_witness_table 10AppIntents21IntentResultContainerVys5NeverOA3EGAA0cD0HPyHC.4
+ _get_witness_table 10AppIntents22IntentParameterSummaryVy12CalendarLink011CreateEventC0VGAA0dE0HPyHC.33
+ _get_witness_table 10AppIntents22IntentParameterSummaryVy12CalendarLink011DeleteEventC0VGAA0dE0HPyHC.13
+ _get_witness_table 10AppIntents22IntentParameterSummaryVy12CalendarLink014EmailOrganizerC0VGAA0dE0HPyHC.3
+ _get_witness_table 10AppIntents22IntentParameterSummaryVy12CalendarLink015DeleteCalendarsC0VGAA0dE0HPyHC.24
+ _get_witness_table 10AppIntents22IntentParameterSummaryVy12CalendarLink09EditEventC0VGAA0dE0HPyHC.51
+ _keypath_set.32Tm
+ _objc_autorelease
+ _objc_msgSend$URL
+ _objc_msgSend$UUID
+ _objc_msgSend$__swift_objectForKeyedSubscript:
+ _objc_msgSend$absoluteDate
+ _objc_msgSend$acceptSuggestedEvent:
+ _objc_msgSend$acknowledgeWithEventStore:error:
+ _objc_msgSend$addAlarm:
+ _objc_msgSend$addAttendee:
+ _objc_msgSend$alarms
+ _objc_msgSend$allKeys
+ _objc_msgSend$allowsAttendeesModifications
+ _objc_msgSend$allowsAvailabilityModifications
+ _objc_msgSend$allowsContentModifications
+ _objc_msgSend$allowsParticipationStatusModifications
+ _objc_msgSend$allowsPrivacyLevelModifications
+ _objc_msgSend$associateCalendarEntityWithIdentifier:with:
+ _objc_msgSend$attendees
+ _objc_msgSend$attributeSet
+ _objc_msgSend$availability
+ _objc_msgSend$cal_isMultidayEventForUIWithStartDate:endDate:
+ _objc_msgSend$calendar
+ _objc_msgSend$calendarForEntityType:eventStore:
+ _objc_msgSend$calendarFromEventStore:
+ _objc_msgSend$calendarIdentifier
+ _objc_msgSend$calendarWithIdentifier:
+ _objc_msgSend$calendarsForEntityType:
+ _objc_msgSend$calendarsWithIdentifiers:
+ _objc_msgSend$commitWithRollback:
+ _objc_msgSend$committedCopy
+ _objc_msgSend$conferenceURLForDisplay
+ _objc_msgSend$configurationWithScale:
+ _objc_msgSend$coordinate
+ _objc_msgSend$couldBeJunk
+ _objc_msgSend$currentDevice
+ _objc_msgSend$currentUserMayActAsOrganizer
+ _objc_msgSend$dateInTimeZone:fromTimeZone:
+ _objc_msgSend$dayOfWeek:weekNumber:
+ _objc_msgSend$defaultCalendarForNewEvents
+ _objc_msgSend$defaultEventDuration
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$deleteEvent:span:error:
+ _objc_msgSend$deleteSuggestedEvent:
+ _objc_msgSend$dialog
+ _objc_msgSend$diffSummaryBetweenObject:andObject:
+ _objc_msgSend$displayColor
+ _objc_msgSend$donateCreateEventIntentWithEvent:completionHandler:
+ _objc_msgSend$donateDeleteCalendarIntentWithCalendar:reportJunk:completionHandler:
+ _objc_msgSend$donateDeletionEventIntentWithEvent:span:completionHandler:
+ _objc_msgSend$donateEditEventIntentWithOriginalEvent:newEvent:span:completionHandler:
+ _objc_msgSend$donateOpenCalendarEditorWithCalendar:completionHandler:
+ _objc_msgSend$donateOpenEventDetailWithEvent:completionHandler:
+ _objc_msgSend$donateOpenEventEditorIntentWithEvent:completionHandler:
+ _objc_msgSend$duration
+ _objc_msgSend$ekCalendarComparator
+ _objc_msgSend$ekOtherCalendarComparator
+ _objc_msgSend$emailAddress
+ _objc_msgSend$endDate
+ _objc_msgSend$event
+ _objc_msgSend$eventNotifications
+ _objc_msgSend$eventStore
+ _objc_msgSend$eventWithAppEntityIdentifier:
+ _objc_msgSend$eventWithEventStore:
+ _objc_msgSend$eventWithExternalURI:
+ _objc_msgSend$eventWithIdentifier:
+ _objc_msgSend$eventWithRecurrenceIdentifier:
+ _objc_msgSend$eventsMatchingPredicate:
+ _objc_msgSend$eventsWithIdentifiers:
+ _objc_msgSend$executeFetchRequest:error:
+ _objc_msgSend$exportToICSWithOptions:
+ _objc_msgSend$externalID
+ _objc_msgSend$fetchReminderDataForReminderURLs:error:
+ _objc_msgSend$hasAttendees
+ _objc_msgSend$hasChanges
+ _objc_msgSend$hasRecurrenceRules
+ _objc_msgSend$identifier
+ _objc_msgSend$identifierString
+ _objc_msgSend$init
+ _objc_msgSend$initRecurrenceWithFrequency:interval:daysOfTheWeek:daysOfTheMonth:monthsOfTheYear:weeksOfTheYear:daysOfTheYear:setPositions:end:
+ _objc_msgSend$initWithAbsoluteDate:
+ _objc_msgSend$initWithCalendars:
+ _objc_msgSend$initWithEditingManager:
+ _objc_msgSend$initWithEndDate:
+ _objc_msgSend$initWithEventStore:
+ _objc_msgSend$initWithEventStore:visibilityChangedCallback:queue:
+ _objc_msgSend$initWithKeysToFetch:
+ _objc_msgSend$initWithLatitude:longitude:
+ _objc_msgSend$initWithName:emailAddress:phoneNumber:url:
+ _objc_msgSend$initWithOccurrenceCount:
+ _objc_msgSend$initWithRelativeOffset:
+ _objc_msgSend$initWithStartDate:endDate:
+ _objc_msgSend$isAllDay
+ _objc_msgSend$isCurrentUser
+ _objc_msgSend$isDelegate
+ _objc_msgSend$isDeletable
+ _objc_msgSend$isDetached
+ _objc_msgSend$isEditable
+ _objc_msgSend$isEnabled
+ _objc_msgSend$isEnabledForEvents
+ _objc_msgSend$isEqualToParticipant:
+ _objc_msgSend$isExternallyOrganizedInvitation
+ _objc_msgSend$isFirstOccurrence
+ _objc_msgSend$isFloating
+ _objc_msgSend$isIntegrationEvent
+ _objc_msgSend$isNaturalLanguageSuggestedEventCalendar
+ _objc_msgSend$isOrWasPartOfRecurringSeries
+ _objc_msgSend$isReminderIntegrationEvent
+ _objc_msgSend$isSubscribed
+ _objc_msgSend$isSuggestedEventCalendar
+ _objc_msgSend$isTopographicallyEqualToAlarm:
+ _objc_msgSend$isValid
+ _objc_msgSend$loadCalendarLinkAppleInternal
+ _objc_msgSend$location
+ _objc_msgSend$locationWithTitle:
+ _objc_msgSend$markResourceChangeAlertedAndSave:error:
+ _objc_msgSend$masterEvent
+ _objc_msgSend$model
+ _objc_msgSend$needsResponse
+ _objc_msgSend$nextConfirmation
+ _objc_msgSend$notification
+ _objc_msgSend$objectID
+ _objc_msgSend$openURL:configuration:completionHandler:
+ _objc_msgSend$organizer
+ _objc_msgSend$participantRole
+ _objc_msgSend$participantStatus
+ _objc_msgSend$perform
+ _objc_msgSend$phoneNumber
+ _objc_msgSend$predicateForContactsMatchingHandleStrings:
+ _objc_msgSend$predicateForEventsWithStartDate:endDate:calendars:
+ _objc_msgSend$predicateForEventsWithStartDate:endDate:calendars:exclusionOptions:filterdOutTitles:randomize:limit:
+ _objc_msgSend$privacyLevel
+ _objc_msgSend$proposeFuture
+ _objc_msgSend$recurrenceIdentifierWithLocalUID:recurrenceDate:
+ _objc_msgSend$recurrenceIdentifierWithString:
+ _objc_msgSend$recurrenceRules
+ _objc_msgSend$rejectionReason
+ _objc_msgSend$relativeOffset
+ _objc_msgSend$reminderEntityAnnotationForIntegrationEvent:
+ _objc_msgSend$reminderEntityIdentifierForIntegrationEvent:
+ _objc_msgSend$removeAttendee:
+ _objc_msgSend$removeEvent:span:commit:error:
+ _objc_msgSend$removeEvent:span:error:
+ _objc_msgSend$requirementsToMoveToCalendar:
+ _objc_msgSend$resourceChangeFromEventStore:
+ _objc_msgSend$respondToSharedCalendarInvitation:withStatus:
+ _objc_msgSend$responseMustApplyToAll
+ _objc_msgSend$saveCalendar:commit:error:
+ _objc_msgSend$saveEvent:span:commit:error:
+ _objc_msgSend$saveEvent:span:error:
+ _objc_msgSend$saveNewEvents:commit:error:
+ _objc_msgSend$seconds
+ _objc_msgSend$selectConfirmationOptionAtIndex:
+ _objc_msgSend$selfAttendee
+ _objc_msgSend$setAddress:
+ _objc_msgSend$setAlarms:
+ _objc_msgSend$setAllDay:
+ _objc_msgSend$setAvailability:
+ _objc_msgSend$setCalendar:
+ _objc_msgSend$setContactLabel:
+ _objc_msgSend$setDateStyle:
+ _objc_msgSend$setDefaultAlarm:
+ _objc_msgSend$setEndDate:
+ _objc_msgSend$setFirstDayOfTheWeek:
+ _objc_msgSend$setGeoLocation:
+ _objc_msgSend$setImprecise:
+ _objc_msgSend$setInvitationStatus:
+ _objc_msgSend$setIsJunk:
+ _objc_msgSend$setIsJunk:shouldSave:
+ _objc_msgSend$setLocation:
+ _objc_msgSend$setMapKitHandle:
+ _objc_msgSend$setNumberStyle:
+ _objc_msgSend$setParticipantRole:
+ _objc_msgSend$setParticipationStatus:
+ _objc_msgSend$setPredicate:
+ _objc_msgSend$setPrivacyLevel:
+ _objc_msgSend$setRadius:
+ _objc_msgSend$setRecurrenceEnd:
+ _objc_msgSend$setRecurrenceRules:
+ _objc_msgSend$setSource:
+ _objc_msgSend$setStartDate:
+ _objc_msgSend$setStatus:
+ _objc_msgSend$setStructuredLocation:
+ _objc_msgSend$setTimeStyle:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$setTravelTime:
+ _objc_msgSend$setURL:
+ _objc_msgSend$setUndoDelegate:
+ _objc_msgSend$setUnifyResults:
+ _objc_msgSend$setUnselectedCalendarIdentifiersForFocusMode:
+ _objc_msgSend$shared
+ _objc_msgSend$shouldRequestSpan
+ _objc_msgSend$sortedSourcesEnabledForEntityType:
+ _objc_msgSend$source
+ _objc_msgSend$sourceType
+ _objc_msgSend$sourceWithIdentifier:
+ _objc_msgSend$sources
+ _objc_msgSend$sourcesEnabledForEntityType:
+ _objc_msgSend$spanDecisionInfoForEvents:
+ _objc_msgSend$startDate
+ _objc_msgSend$status
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$stringFromInteger:
+ _objc_msgSend$stringRepresentation
+ _objc_msgSend$structuredLocation
+ _objc_msgSend$supportedEventAvailabilities
+ _objc_msgSend$supportsCalendarCreation
+ _objc_msgSend$textRepresentationForEvent:withTextFormat:showURI:
+ _objc_msgSend$timeZone
+ _objc_msgSend$title
+ _objc_msgSend$titleStringWithOptions:
+ _objc_msgSend$type
+ _objc_msgSend$uniqueID
+ _objc_msgSend$unlocalizedTitle
+ _objc_msgSend$urlWithAllowedScheme
+ _objc_msgSend$value
+ _objc_msgSend$virtualConference
+ _objc_msgSend$visibleCalendars
+ _objc_release_x11
+ _objc_retain_x3
+ _objectdestroy.22Tm
+ _objectdestroy.43Tm
+ _objectdestroyTm
+ _swift_getErrorValue
+ _swift_release_n
+ _swift_willThrowTypedImpl
+ _symbolic IeAgH_
+ _symbolic IeghH_
+ _symbolic IeyB_
+ _symbolic Say_____G 10AppIntents12IntentPersonV
+ _symbolic Say_____G 13CalendarUIKit19EKAlarmModelWrapperV
+ _symbolic Say_____G 13CalendarUIKit22EKAttendeeModelWrapperV
+ _symbolic Say_____G 13CalendarUIKit28EKRecurrenceRuleModelWrapperV
+ _symbolic Say_____GSg 13CalendarUIKit19EKAlarmModelWrapperV
+ _symbolic Say_____GSg 13CalendarUIKit22EKAttendeeModelWrapperV
+ _symbolic Say_____GSg 13CalendarUIKit28EKRecurrenceRuleModelWrapperV
+ _symbolic SbSg
+ _symbolic SdSg
+ _symbolic So10EKCalendarC
+ _symbolic So7EKEventC
+ _symbolic _____ 10ObjectiveC8ObjCBoolV
+ _symbolic _____ 12CalendarLink14IntentDonationC
+ _symbolic _____ 12CalendarLink18EventChangedFieldsV
+ _symbolic _____ 12CalendarLink18IntentDonationMockC
+ _symbolic _____ 13CalendarUIKit19EKEventModelWrapperV
+ _symbolic _____ So13EKEventStatusV
+ _symbolic _____ So14EKPrivacyLevelV
+ _symbolic _____ So19EKEventAvailabilityV
+ _symbolic _____ So19EKParticipantStatusV
+ _symbolic _____ So6EKSpanV
+ _symbolic _____3key_yp5valuet s11AnyHashableV
+ _symbolic _____Sg 12CalendarLink18EventChangedFieldsV
+ _symbolic _____Sg 13CalendarUIKit22EKCalendarModelWrapperV
+ _symbolic _____Sg So13EKEventStatusV
+ _symbolic _____Sg So14EKPrivacyLevelV
+ _symbolic _____Sg So19EKEventAvailabilityV
+ _symbolic _____Sg So19EKParticipantStatusV
+ _symbolic _____Sg_ABt 10AppIntents12IntentPersonV6HandleV
+ _symbolic _____Sg_ABt 10Foundation3URLV
+ _symbolic _____Sg_ABt 10Foundation8CalendarV14RecurrenceRuleV
+ _symbolic _____Sg_ABt 12CalendarLink15EditEventIntentV12updateAlarms33_B858B8DB122A689813BB984D38FDD106LL5event03newG0ySo7EKEventC_SaySo7EKAlarmCGtF9AlarmInfoL_O
+ _symbolic _____XMo 12CalendarLink14IntentDonationC
+ _symbolic ______p 10AppIntents0A6IntentP
+ _symbolic _____y_____G s11_SetStorageC 10Foundation8CalendarV9ComponentO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation8CalendarV9ComponentO
+ _symbolic _____y______pG s23_ContiguousArrayStorageC 10AppIntents0D6IntentP
- _get_witness_table 10AppIntents21IntentResultContainerVy12CalendarLink11EventEntityVs5NeverOA2HGAA05OpensC0HPyHC.32
- _get_witness_table 10AppIntents21IntentResultContainerVy12CalendarLink11EventEntityVs5NeverOA2HGAA05OpensC0HPyHC.48
- _get_witness_table 10AppIntents21IntentResultContainerVy12CalendarLink11EventEntityVs5NeverOA2HGAA12ReturnsValueHPyHC.33
- _get_witness_table 10AppIntents21IntentResultContainerVy12CalendarLink11EventEntityVs5NeverOA2HGAA12ReturnsValueHPyHC.49
- _get_witness_table 10AppIntents21IntentResultContainerVys5NeverOA3EGAA0cD0HPyHC.24
- _get_witness_table 10AppIntents21IntentResultContainerVys5NeverOA3EGAA0cD0HPyHC.84
- _get_witness_table 10AppIntents22IntentParameterSummaryVy12CalendarLink011CreateEventC0VGAA0dE0HPyHC.31
- _get_witness_table 10AppIntents22IntentParameterSummaryVy12CalendarLink011DeleteEventC0VGAA0dE0HPyHC.12
- _get_witness_table 10AppIntents22IntentParameterSummaryVy12CalendarLink014EmailOrganizerC0VGAA0dE0HPyHC.83
- _get_witness_table 10AppIntents22IntentParameterSummaryVy12CalendarLink015DeleteCalendarsC0VGAA0dE0HPyHC.23
- _get_witness_table 10AppIntents22IntentParameterSummaryVy12CalendarLink09EditEventC0VGAA0dE0HPyHC.47
- _keypath_get.31Tm
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutorelease
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x4
- _symbolic _____Sg 10AppIntents19IntentSystemContextV6SourceO
CStrings:
+ "CUIKEventActionHandler"
+ "CUIKIntentDonation"
+ "CalendarLinkSpotlightEntityAnnotator"
+ "Error shown to the user when we fail to calculate start or end date This is not an expected error."
+ "Failed to donate CreateEventIntent for event %s: %s"
+ "Failed to donate DeleteCalendarIntent for calendar %s: %s"
+ "Failed to donate DeleteEventIntent for event %s: %s"
+ "Failed to donate EditEventIntent for event %s with span %ld: %s"
+ "Failed to donate OpenCalendarEditor for calendar %s: %s"
+ "Failed to donate OpenEventDetail for event %s: %s"
+ "Failed to donate OpenEventEditorIntent for event %s: %s"
+ "Failed to get event store when providing default result. Returning nil"
+ "Failed to set event dates."
+ "No default calendar in event store when providing default result. Returning nil"
+ "Successfully donated CreateEventIntent for event %s"
+ "Successfully donated DeleteCalendarIntent for calendar %s"
+ "Successfully donated DeleteEventIntent for event %s"
+ "Successfully donated EditEventIntent for event %s with span %ld"
+ "Successfully donated OpenCalendarEditor for calendar %s"
+ "Successfully donated OpenEventDetail for event %s"
+ "Successfully donated OpenEventEditorIntent for event %s"
+ "UUID"
+ "_TtC12CalendarLink18IntentDonationMock"
+ "associateCalendarEntityWithIdentifier:with:"
+ "associateCalendarEntityWithIdentifier:withSearchableItem:"
+ "calendar.calendar"
+ "committedCopy"
+ "diffSummaryBetweenObject:andObject:"
+ "donateCreateEventIntentWithEvent:completionHandler:"
+ "donateDeleteCalendarIntentWithCalendar:reportJunk:completionHandler:"
+ "donateDeletionEventIntentWithEvent:span:completionHandler:"
+ "donateEditEventIntentWithOriginalEvent:newEvent:span:completionHandler:"
+ "donateOpenCalendarEditorWithCalendar:completionHandler:"
+ "donateOpenEventDetailWithEvent:completionHandler:"
+ "donateOpenEventEditorIntentWithEvent:completionHandler:"
+ "duration"
+ "handleCalendarDeletion:reportJunk:"
+ "handleEventCreation:"
+ "handleEventDeletion:span:"
+ "handleEventUpdate:span:"
+ "handleOpenCalendarEditor:"
+ "handleOpenEventDetails:"
+ "handleOpenEventEditor:"
+ "isSubscribed"
+ "location"
+ "participantStatus"
+ "selfAttendee"
+ "structuredLocation"
+ "v28@0:8@16B24"
+ "v32@0:8@\"EKCalendar\"16@?<v@?>24"
+ "v32@0:8@\"EKEvent\"16@?<v@?>24"
+ "v32@0:8@\"NSString\"16@\"CSSearchableItem\"24"
+ "v32@0:8@16q24"
+ "v36@0:8@\"EKCalendar\"16B24@?<v@?>28"
+ "v40@0:8@\"EKEvent\"16q24@?<v@?>32"
+ "v48@0:8@\"EKEvent\"16@\"EKEvent\"24q32@?<v@?>40"

```
