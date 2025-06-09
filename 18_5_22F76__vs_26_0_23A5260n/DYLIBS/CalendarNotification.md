## CalendarNotification

> `/System/Library/PrivateFrameworks/CalendarNotification.framework/CalendarNotification`

```diff

-1513.5.3.0.0
-  __TEXT.__text: 0x56f74
+1527.0.0.0.0
+  __TEXT.__text: 0x57354
   __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_methlist: 0x6904
+  __TEXT.__objc_methlist: 0x693c
   __TEXT.__const: 0x1d8
-  __TEXT.__oslogstring: 0xda9f
+  __TEXT.__oslogstring: 0xdb1c
   __TEXT.__cstring: 0x3f48
   __TEXT.__gcc_except_tab: 0x55c
-  __TEXT.__unwind_info: 0x1588
-  __TEXT.__objc_classname: 0x1c32
-  __TEXT.__objc_methname: 0x126c3
-  __TEXT.__objc_methtype: 0x3078
-  __TEXT.__objc_stubs: 0xbba0
+  __TEXT.__unwind_info: 0x1580
+  __TEXT.__objc_classname: 0x1c33
+  __TEXT.__objc_methname: 0x12942
+  __TEXT.__objc_methtype: 0x3088
+  __TEXT.__objc_stubs: 0xbcc0
   __DATA_CONST.__got: 0x948
   __DATA_CONST.__const: 0xd00
   __DATA_CONST.__objc_classlist: 0x498
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3388
+  __DATA_CONST.__objc_selrefs: 0x33c8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x408
   __AUTH_CONST.__const: 0x4e0
   __AUTH_CONST.__cfstring: 0x2e40
-  __AUTH_CONST.__objc_const: 0xe350
+  __AUTH_CONST.__objc_const: 0xe440
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0x788
+  __AUTH.__objc_data: 0x7d0
+  __DATA.__objc_ivar: 0x79c
   __DATA.__data: 0x1aa0
   __DATA.__bss: 0x18
-  __DATA_DIRTY.__objc_data: 0x25d0
+  __DATA_DIRTY.__objc_data: 0x2620
   __DATA_DIRTY.__bss: 0x3b8
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/iCalendar.framework/iCalendar
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 46D2C9EE-AEC5-3322-B3CF-6F555CF417C2
-  Functions: 2232
-  Symbols:   8629
-  CStrings:  4273
+  UUID: 842DE747-7420-3441-A88F-552E45C71855
+  Functions: 2237
+  Symbols:   8619
+  CStrings:  4286
 
Symbols:
+ -[CALNDefaultTriggeredEventNotificationTriggerHelper eventStoreProvider]
+ -[CALNDefaultTriggeredEventNotificationTriggerHelper initWithTravelAdvisoryAuthority:dateProvider:eventStoreProvider:]
+ -[CALNTriggeredEventNotificationInfo initWithTitle:location:locationWithoutPrediction:startDate:endDate:isAllDay:isTimeSensitive:eventID:eventOccurrenceID:eventObjectID:organizerPhoneNumber:organizerEmailAddress:calendarIdentifier:eventRepresentationDictionary:legacyIdentifier:preferredLocation:conferenceURL:conferenceURLIsBroadcast:mailtoURL:hasSuggestedLocation:eventHasAlarms:allowsLocationAlerts:forceDisplayOfNewTravelAdvisoryHypotheses:travelAdvisoryDisabled:]
+ -[CALNTriggeredEventNotificationInfo organizerEmailAddress]
+ -[CALNTriggeredEventNotificationInfo organizerPhoneNumber]
+ -[CALNTriggeredEventNotificationSourceNotificationInfo initWithTitle:location:locationWithoutPrediction:preferredLocation:startDate:endDate:isAllDay:isTimeSensitive:launchURL:isLocationEvent:eventID:eventObjectID:organizerPhoneNumber:organizerEmailAddress:calendarIdentifier:eventRepresentationDictionary:legacyIdentifier:mapItemURL:conferenceURL:conferenceURLIsBroadcast:mailtoURL:hasSuggestedLocation:eventHasAlarms:alarmID:isOffsetFromTravelTimeStart:lastFireTimeOfAlertOffsetFromTravelTime:allowsLocationAlerts:hypothesis:travelAdvisoryTimelinessPeriod:forceDisplayOfNewTravelAdvisoryHypotheses:travelAdvisoryDisabled:]
+ -[CALNTriggeredEventNotificationSourceNotificationInfo organizerEmailAddress]
+ -[CALNTriggeredEventNotificationSourceNotificationInfo organizerPhoneNumber]
+ _OBJC_IVAR_$_CALNDefaultTriggeredEventNotificationTriggerHelper._eventStoreProvider
+ _OBJC_IVAR_$_CALNTriggeredEventNotificationInfo._organizerEmailAddress
+ _OBJC_IVAR_$_CALNTriggeredEventNotificationInfo._organizerPhoneNumber
+ _OBJC_IVAR_$_CALNTriggeredEventNotificationSourceNotificationInfo._organizerEmailAddress
+ _OBJC_IVAR_$_CALNTriggeredEventNotificationSourceNotificationInfo._organizerPhoneNumber
+ _objc_msgSend$batchLoadNotifications:
+ _objc_msgSend$blockList
+ _objc_msgSend$initWithTitle:location:locationWithoutPrediction:preferredLocation:startDate:endDate:isAllDay:isTimeSensitive:launchURL:isLocationEvent:eventID:eventObjectID:organizerPhoneNumber:organizerEmailAddress:calendarIdentifier:eventRepresentationDictionary:legacyIdentifier:mapItemURL:conferenceURL:conferenceURLIsBroadcast:mailtoURL:hasSuggestedLocation:eventHasAlarms:alarmID:isOffsetFromTravelTimeStart:lastFireTimeOfAlertOffsetFromTravelTime:allowsLocationAlerts:hypothesis:travelAdvisoryTimelinessPeriod:forceDisplayOfNewTravelAdvisoryHypotheses:travelAdvisoryDisabled:
+ _objc_msgSend$initWithTitle:location:locationWithoutPrediction:startDate:endDate:isAllDay:isTimeSensitive:eventID:eventOccurrenceID:eventObjectID:organizerPhoneNumber:organizerEmailAddress:calendarIdentifier:eventRepresentationDictionary:legacyIdentifier:preferredLocation:conferenceURL:conferenceURLIsBroadcast:mailtoURL:hasSuggestedLocation:eventHasAlarms:allowsLocationAlerts:forceDisplayOfNewTravelAdvisoryHypotheses:travelAdvisoryDisabled:
+ _objc_msgSend$initWithTransportType:conservativeDepartureDate:conservativeTravelTime:suggestedDepartureDate:estimatedTravelTime:aggressiveDepartureDate:aggressiveTravelTime:routeName:supportsLiveTraffic:currentTrafficDensity:trafficDensityDescription:travelState:travelSections:
+ _objc_msgSend$initWithTravelAdvisoryAuthority:dateProvider:eventStoreProvider:
+ _objc_msgSend$isBlockedWithEmail:
+ _objc_msgSend$isBlockedWithPhoneNumber:
+ _objc_msgSend$organizerEmailAddress
+ _objc_msgSend$organizerPhoneNumber
+ _objc_msgSend$travelSections
- -[CALNDefaultTriggeredEventNotificationTriggerHelper initWithTravelAdvisoryAuthority:dateProvider:]
- -[CALNTriggeredEventNotificationInfo initWithTitle:location:locationWithoutPrediction:startDate:endDate:isAllDay:isTimeSensitive:eventID:eventOccurrenceID:eventObjectID:calendarIdentifier:eventRepresentationDictionary:legacyIdentifier:preferredLocation:conferenceURL:conferenceURLIsBroadcast:mailtoURL:hasSuggestedLocation:eventHasAlarms:allowsLocationAlerts:forceDisplayOfNewTravelAdvisoryHypotheses:travelAdvisoryDisabled:]
- -[CALNTriggeredEventNotificationSourceNotificationInfo initWithTitle:location:locationWithoutPrediction:preferredLocation:startDate:endDate:isAllDay:isTimeSensitive:launchURL:isLocationEvent:eventID:eventObjectID:calendarIdentifier:eventRepresentationDictionary:legacyIdentifier:mapItemURL:conferenceURL:conferenceURLIsBroadcast:mailtoURL:hasSuggestedLocation:eventHasAlarms:alarmID:isOffsetFromTravelTimeStart:lastFireTimeOfAlertOffsetFromTravelTime:allowsLocationAlerts:hypothesis:travelAdvisoryTimelinessPeriod:forceDisplayOfNewTravelAdvisoryHypotheses:travelAdvisoryDisabled:]
- _objc_msgSend$initWithTitle:location:locationWithoutPrediction:preferredLocation:startDate:endDate:isAllDay:isTimeSensitive:launchURL:isLocationEvent:eventID:eventObjectID:calendarIdentifier:eventRepresentationDictionary:legacyIdentifier:mapItemURL:conferenceURL:conferenceURLIsBroadcast:mailtoURL:hasSuggestedLocation:eventHasAlarms:alarmID:isOffsetFromTravelTimeStart:lastFireTimeOfAlertOffsetFromTravelTime:allowsLocationAlerts:hypothesis:travelAdvisoryTimelinessPeriod:forceDisplayOfNewTravelAdvisoryHypotheses:travelAdvisoryDisabled:
- _objc_msgSend$initWithTitle:location:locationWithoutPrediction:startDate:endDate:isAllDay:isTimeSensitive:eventID:eventOccurrenceID:eventObjectID:calendarIdentifier:eventRepresentationDictionary:legacyIdentifier:preferredLocation:conferenceURL:conferenceURLIsBroadcast:mailtoURL:hasSuggestedLocation:eventHasAlarms:allowsLocationAlerts:forceDisplayOfNewTravelAdvisoryHypotheses:travelAdvisoryDisabled:
CStrings:
+ "@176@0:8@16@24@32@40@48B56B60@64@72@80@88@96@104@112@120@128@136B144@148B156B160B164B168B172"
+ "@224@0:8@16@24@32@40@48@56B64B68@72B80@84@92@100@108@116@124@132@140@148B156@160B168B172@176B184@188B196@200Q208B216B220"
+ "Should not trigger for notification. email = %@ is blocked"
+ "Should not trigger for notification. phone number = %@ is blocked"
+ "T@\"NSString\",R,C,N,V_organizerEmailAddress"
+ "T@\"NSString\",R,C,N,V_organizerPhoneNumber"
+ "_organizerPhoneNumber"
+ "batchLoadNotifications:"
+ "blockList"
+ "initWithTitle:location:locationWithoutPrediction:preferredLocation:startDate:endDate:isAllDay:isTimeSensitive:launchURL:isLocationEvent:eventID:eventObjectID:organizerPhoneNumber:organizerEmailAddress:calendarIdentifier:eventRepresentationDictionary:legacyIdentifier:mapItemURL:conferenceURL:conferenceURLIsBroadcast:mailtoURL:hasSuggestedLocation:eventHasAlarms:alarmID:isOffsetFromTravelTimeStart:lastFireTimeOfAlertOffsetFromTravelTime:allowsLocationAlerts:hypothesis:travelAdvisoryTimelinessPeriod:forceDisplayOfNewTravelAdvisoryHypotheses:travelAdvisoryDisabled:"
+ "initWithTitle:location:locationWithoutPrediction:startDate:endDate:isAllDay:isTimeSensitive:eventID:eventOccurrenceID:eventObjectID:organizerPhoneNumber:organizerEmailAddress:calendarIdentifier:eventRepresentationDictionary:legacyIdentifier:preferredLocation:conferenceURL:conferenceURLIsBroadcast:mailtoURL:hasSuggestedLocation:eventHasAlarms:allowsLocationAlerts:forceDisplayOfNewTravelAdvisoryHypotheses:travelAdvisoryDisabled:"
+ "initWithTransportType:conservativeDepartureDate:conservativeTravelTime:suggestedDepartureDate:estimatedTravelTime:aggressiveDepartureDate:aggressiveTravelTime:routeName:supportsLiveTraffic:currentTrafficDensity:trafficDensityDescription:travelState:travelSections:"
+ "initWithTravelAdvisoryAuthority:dateProvider:eventStoreProvider:"
+ "isBlockedWithEmail:"
+ "isBlockedWithPhoneNumber:"
+ "organizerPhoneNumber"
+ "travelSections"
- "@160@0:8@16@24@32@40@48B56B60@64@72@80@88@96@104@112@120B128@132B140B144B148B152B156"
- "@208@0:8@16@24@32@40@48@56B64B68@72B80@84@92@100@108@116@124@132B140@144B152B156@160B168@172B180@184Q192B200B204"
- "initWithTitle:location:locationWithoutPrediction:preferredLocation:startDate:endDate:isAllDay:isTimeSensitive:launchURL:isLocationEvent:eventID:eventObjectID:calendarIdentifier:eventRepresentationDictionary:legacyIdentifier:mapItemURL:conferenceURL:conferenceURLIsBroadcast:mailtoURL:hasSuggestedLocation:eventHasAlarms:alarmID:isOffsetFromTravelTimeStart:lastFireTimeOfAlertOffsetFromTravelTime:allowsLocationAlerts:hypothesis:travelAdvisoryTimelinessPeriod:forceDisplayOfNewTravelAdvisoryHypotheses:travelAdvisoryDisabled:"
- "initWithTitle:location:locationWithoutPrediction:startDate:endDate:isAllDay:isTimeSensitive:eventID:eventOccurrenceID:eventObjectID:calendarIdentifier:eventRepresentationDictionary:legacyIdentifier:preferredLocation:conferenceURL:conferenceURLIsBroadcast:mailtoURL:hasSuggestedLocation:eventHasAlarms:allowsLocationAlerts:forceDisplayOfNewTravelAdvisoryHypotheses:travelAdvisoryDisabled:"

```
