## CalendarUI

> `/System/Library/PrivateFrameworks/CalendarUI.framework/Versions/A/CalendarUI`

```diff

-1197.3.4.0.0
-  __TEXT.__text: 0xefcd4
+1197.5.5.0.0
+  __TEXT.__text: 0xefb7c
   __TEXT.__auth_stubs: 0x9d0
-  __TEXT.__objc_methlist: 0x11230
-  __TEXT.__const: 0x710
+  __TEXT.__objc_methlist: 0x132e8
+  __TEXT.__const: 0x6f8
   __TEXT.__gcc_except_tab: 0x1140
-  __TEXT.__cstring: 0x69ba
+  __TEXT.__cstring: 0x6a8d
   __TEXT.__oslogstring: 0x1c60
   __TEXT.__ustring: 0x482
-  __TEXT.__unwind_info: 0x3868
+  __TEXT.__unwind_info: 0x38e8
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x20ce
-  __TEXT.__objc_methname: 0x2c836
+  __TEXT.__objc_methname: 0x2c830
   __TEXT.__objc_methtype: 0x556f
   __TEXT.__objc_stubs: 0x238a0
-  __DATA_CONST.__got: 0x1318
-  __DATA_CONST.__const: 0x4f0
+  __DATA_CONST.__got: 0x1310
+  __DATA_CONST.__const: 0x510
   __DATA_CONST.__objc_classlist: 0x820
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa7d0
+  __DATA_CONST.__objc_selrefs: 0xae80
   __DATA_CONST.__objc_superrefs: 0x648
   __DATA_CONST.__objc_arraydata: 0x448
   __AUTH_CONST.__auth_got: 0x4f8
   __AUTH_CONST.__const: 0x20e0
-  __AUTH_CONST.__cfstring: 0x8dc0
-  __AUTH_CONST.__objc_const: 0x1fb88
+  __AUTH_CONST.__cfstring: 0x8ea0
+  __AUTH_CONST.__objc_const: 0x1beb0
   __AUTH_CONST.__objc_intobj: 0x5b8
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x258

   - /System/Library/PrivateFrameworks/iCalendar.framework/Versions/A/iCalendar
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1A46A4E-80BC-39D8-9AE6-AAFE1D7D7116
-  Functions: 6015
-  Symbols:   15249
-  CStrings:  11215
+  UUID: 5AEFDEB3-4B0E-3F05-937A-4598FB9382D2
+  Functions: 6099
+  Symbols:   15339
+  CStrings:  11230
 
Symbols:
+ +[CalUIBoxOccurrenceContentView _cachedImageWithName:].cold.1
+ +[CalUICalendarInfoViewController logHandle].cold.1
+ +[CalUIEventViewTouchBar interestedChangeKeys].cold.1
+ +[CalUILayerBackedView disableAnimatedActionsForLayer:excludingPosition:excludingBounds:].cold.1
+ +[CalUILocationSuggestionManager manager].cold.1
+ +[CalUILogSubsystem autocomplete].cold.1
+ +[CalUILogSubsystem certificatePanel].cold.1
+ +[CalUILogSubsystem customRecurrence].cold.1
+ +[CalUILogSubsystem defaultCategory].cold.1
+ +[CalUILogSubsystem inspectorNewTimeProposal].cold.1
+ +[CalUILogSubsystem inspectorUpdate].cold.1
+ +[CalUILogSubsystem inspector].cold.1
+ +[CalUILogSubsystem locations].cold.1
+ +[CalUILogSubsystem notificationCenter].cold.1
+ +[CalUILogSubsystem travel].cold.1
+ +[CalUIOccurrenceUtilities dotIconTextDifferencesForFontSize].cold.1
+ +[CalUIOccurrenceUtilities lineHeightPaddingForFontSize].cold.1
+ +[CalUIOccurrenceUtilities shouldClarifyTimeZone:].cold.1
+ +[CalUIOccurrenceUtilities timeTitleDifferenceForFontSize].cold.1
+ +[CalUITouchBarUtilities imageNamed:].cold.1
+ +[EKUIAbstractTimeZoneGadget interestedChangeKeys].cold.1
+ +[EKUIAlarmCompositeGadget interestedChangeKeys].cold.1
+ +[EKUIAlarmSummaryGadget interestedChangeKeys].cold.1
+ +[EKUIAttachmentGadget interestedChangeKeys].cold.1
+ +[EKUIAttendeeCommentCompositeGadget interestedChangeKeys].cold.1
+ +[EKUIAttendeesGadget interestedChangeKeys].cold.1
+ +[EKUIAvailabilityGadget interestedChangeKeys].cold.1
+ +[EKUICalendarGadget interestedChangeKeys].cold.1
+ +[EKUICommentGadget interestedChangeKeys].cold.1
+ +[EKUIConferenceURLGadget interestedChangeKeys].cold.1
+ +[EKUIDateTimeGadget interestedChangeKeys].cold.1
+ +[EKUIDateTimeSummaryGadget interestedChangeKeys].cold.1
+ +[EKUIDoneButtonGadget interestedChangeKeys].cold.1
+ +[EKUIDueGadget interestedChangeKeys].cold.1
+ +[EKUIGadgetContainerAnimator animatorForEventViewController:].cold.1
+ +[EKUIJunkGadget interestedChangeKeys].cold.1
+ +[EKUILocationGadget interestedChangeKeys].cold.1
+ +[EKUIMapGadget interestedChangeKeys].cold.1
+ +[EKUINewTimeOptionsGadget interestedChangeKeys].cold.1
+ +[EKUINoteGadget interestedChangeKeys].cold.1
+ +[EKUINoteURLAttachmentSummaryGadget interestedChangeKeys].cold.1
+ +[EKUIParticipantDisplayState templateStatusImageForName:].cold.1
+ +[EKUIPriorityGadget interestedChangeKeys].cold.1
+ +[EKUIPrivateGadget interestedChangeKeys].cold.1
+ +[EKUIProposeNewTimeSummaryGadget interestedChangeKeys].cold.1
+ +[EKUIProposedTimeCompositeGadget interestedChangeKeys].cold.1
+ +[EKUIProposedTimeDateTimeGadget interestedChangeKeys].cold.1
+ +[EKUIShareesGadget interestedChangeKeys].cold.1
+ +[EKUIStatusGadget interestedChangeKeys].cold.1
+ +[EKUITitleGadget interestedChangeKeys].cold.1
+ +[EKUITravelTimeGadget interestedChangeKeys].cold.1
+ +[EKUITravelTimeSummaryGadget interestedChangeKeys].cold.1
+ +[EKUIURLGadget _suggestionsServiceForEvents].cold.1
+ +[EKUIURLGadget interestedChangeKeys].cold.1
+ +[EKUIUnsubscribeGadget interestedChangeKeys].cold.1
+ -[CalUICustomRecurrenceWindowController _openWithAnimation:].cold.1
+ -[CalUICustomRecurrenceWindowController _openWithAnimation:].cold.2
+ -[CalUICustomRecurrenceWindowController _openWithAnimation:].cold.3
+ -[CalUICustomRecurrenceWindowController _openWithAnimation:].cold.4
+ -[CalUICustomRecurrenceWindowController _openWithAnimation:].cold.5
+ -[CalUIEventTimeViewController _segmentsForLevel:].cold.1
+ -[CalUIEventTimeViewController _timeIntervalForLevel:].cold.1
+ -[CalUIEventTimeViewController maxViewSizeForLevel:].cold.1
+ -[CalUIEventTimeViewController minViewSizeForLevel:].cold.1
+ -[CalUIOccurrenceTableCellView suggestionString].cold.1
+ -[CalUIResizingTextField enableAutomaticLinkDetection].cold.1
+ -[CalUIResizingTextField enableEntireFieldTreatedAsLink].cold.1
+ -[CalUIResizingTextField setCalDelegate:].cold.1
+ -[CalUITimeZonePicker _commonInit].cold.1
+ -[EKUIAlarmSummaryGadget accessibilityIdentifier]
+ -[EKUIAttachmentGadget claimedPboardTypes].cold.1
+ -[EKUIAttendeesGadget claimedPboardTypes].cold.1
+ -[EKUIGadgetContainer addSubitemsByClasses:].cold.1
+ -[EKUILocationGadget claimedPboardTypes].cold.1
+ -[EKUILocationGadget roomTypes].cold.1
+ -[EKUINewEventSummaryGadget accessibilityIdentifier]
+ -[EKUINoteGadget claimedPboardTypes].cold.1
+ -[EKUIProposedTimeCompositeGadget setObject:].cold.1
+ -[EKUIShareesGadget claimedPboardTypes].cold.1
+ -[EKUITitleGadget claimedPboardTypes].cold.1
+ -[EKUITravelTimeSummaryGadget accessibilityIdentifier]
+ -[EKUIURLGadget claimedPboardTypes].cold.1
+ -[IGPopupWindowController openWithAnimation:].cold.1
+ -[NSAttributedString(CalUIClassAdditions) stringWithRange:formattedWithURL:withColor:andUnderline:insertIsolates:ltrOverride:addedCharacters:].cold.1
+ CalOffsetToCenterNumberWithFont.cold.1
+ CalUILocationHandle.cold.1
+ CalUIPasswordPanelHandle.cold.1
+ CalUITravelTimeLogHandle.cold.1
+ GCC_except_table155
+ GCC_except_table156
+ GCC_except_table184
+ GCC_except_table194
+ __36-[CalUIRowView alignBaselinesToView]_block_invoke.cold.1
+ __57-[EKUIAlarmSummaryGadget recurrenceDifferenceDescription]_block_invoke.44
+ __block_literal_global.27
+ __block_literal_global.278
+ __block_literal_global.50
+ __block_literal_global.82
+ __block_literal_global.84
+ _objc_msgSend$boundingRectForFont
- GCC_except_table153
- GCC_except_table154
- GCC_except_table182
- GCC_except_table191
- GCC_except_table193
- _OBJC_CLASS_$_NSLayoutManager
- __57-[EKUIAlarmSummaryGadget recurrenceDifferenceDescription]_block_invoke.41
- __block_literal_global.275
- __block_literal_global.28
- __block_literal_global.39
- __block_literal_global.83
- __block_literal_global.85
- _objc_msgSend$defaultLineHeightForFont:
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CalendarUI/CalendarUI/EventKitUI/EKViewController.m"
+ "/System/AppleInternal/Library/Frameworks/CalendarLink.framework/CalendarLink"
+ "alarm-item:%@"
+ "alert-repeat-traveltime-button"
+ "boundingRectForFont"
+ "calendar-item:%@:%@"
+ "repeat-item:%@"
+ "source-item:%@"
+ "travel-time-button"
+ "travel-time-item:%@"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CalendarUI/CalendarUI/EventKitUI/EKViewController.m"
- "defaultLineHeightForFont:"

```
