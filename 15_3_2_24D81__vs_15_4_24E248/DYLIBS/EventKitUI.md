## EventKitUI

> `/System/iOSSupport/System/Library/Frameworks/EventKitUI.framework/Versions/A/EventKitUI`

```diff

-1490.4.1.0.0
-  __TEXT.__text: 0x1c5c04
-  __TEXT.__auth_stubs: 0x2250
-  __TEXT.__objc_methlist: 0x19c34
-  __TEXT.__const: 0x1fc4
-  __TEXT.__cstring: 0xceb1
-  __TEXT.__gcc_except_tab: 0x3e68
+1490.5.8.0.0
+  __TEXT.__text: 0x1c3e60
+  __TEXT.__auth_stubs: 0x2230
+  __TEXT.__objc_methlist: 0x1dadc
+  __TEXT.__const: 0x1fb4
+  __TEXT.__cstring: 0xd0e1
+  __TEXT.__gcc_except_tab: 0x3ee4
   __TEXT.__oslogstring: 0x74dd
   __TEXT.__ustring: 0x8aa
   __TEXT.__dlopen_cstrs: 0x226
   __TEXT.__constg_swiftt: 0x183c
-  __TEXT.__swift5_typeref: 0xd42
+  __TEXT.__swift5_typeref: 0xd3a
   __TEXT.__swift5_fieldmd: 0xc30
   __TEXT.__swift5_types: 0xf4
   __TEXT.__swift5_capture: 0x4a8

   __TEXT.__swift5_assocty: 0x248
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_proto: 0xe4
-  __TEXT.__unwind_info: 0x7110
+  __TEXT.__swift_as_entry: 0x10
+  __TEXT.__swift_as_ret: 0x10
+  __TEXT.__unwind_info: 0x7220
   __TEXT.__eh_frame: 0x618
   __TEXT.__objc_classname: 0x4078
-  __TEXT.__objc_methname: 0x42831
-  __TEXT.__objc_methtype: 0xb75a
-  __TEXT.__objc_stubs: 0x30000
+  __TEXT.__objc_methname: 0x428f9
+  __TEXT.__objc_methtype: 0xb7b5
+  __TEXT.__objc_stubs: 0x300a0
   __DATA_CONST.__got: 0x1818
-  __DATA_CONST.__const: 0x4268
+  __DATA_CONST.__const: 0x42e0
   __DATA_CONST.__objc_classlist: 0xc20
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x5e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe230
+  __DATA_CONST.__objc_selrefs: 0xecb0
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x890
   __DATA_CONST.__objc_arraydata: 0x258
-  __AUTH_CONST.__auth_got: 0x1138
+  __AUTH_CONST.__auth_got: 0x1128
   __AUTH_CONST.__const: 0x26e0
-  __AUTH_CONST.__cfstring: 0xa3a0
-  __AUTH_CONST.__objc_const: 0x360e0
-  __AUTH_CONST.__objc_intobj: 0x4f8
+  __AUTH_CONST.__cfstring: 0xa9e0
+  __AUTH_CONST.__objc_const: 0x2ed60
+  __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x8cf8
-  __AUTH.__data: 0xbc8
+  __AUTH.__data: 0xbb8
   __DATA.__objc_ivar: 0x23c0
-  __DATA.__data: 0x48f8
+  __DATA.__data: 0x4900
   __DATA.__bss: 0x15d0
   __DATA.__common: 0x218
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 1091958B-FADB-35D2-A30B-501CA244CEA6
-  Functions: 11311
-  Symbols:   23935
-  CStrings:  15676
+  UUID: 1CA29612-FD8D-3C9A-BF48-BAEAA72D5468
+  Functions: 11346
+  Symbols:   24029
+  CStrings:  15773
 
Symbols:
+ +[CalendarPreferences sharedPreferences].cold.1
+ +[ContactsUtils defaultContactKeysToFetch].cold.1
+ +[EKAlarmsViewModel accessibilityIdentifierForIndex:]
+ +[EKEventDetailTitleCell _locationFont].cold.1
+ +[EKEventDetailTitleCell _scaledLocationFont].cold.1
+ +[EKEventDetailTitleCell _scaledTitleFont].cold.1
+ +[EKEventDetailTitleCell _titleFont].cold.1
+ +[EKUIAppReviewUtils _queue].cold.1
+ +[EKUIAppReviewUtils _sharedStoreReview].cold.1
+ +[EKUIApplicationExtensionOverrides shared].cold.1
+ +[EKUIDebugPreferences shared].cold.1
+ +[EKUIDeclineCommentController _newDeclineCommentControllerWithCompletionBlock:].cold.1
+ +[EKUIDividedGridViewController dividerColor].cold.1
+ +[EKUILabeledAvatarView contactKeysToFetch].cold.1
+ +[EKUILocationSearchModel _dataDetector].cold.1
+ +[EKUILocationSearchModel initialize].cold.1
+ +[EKUISemiConstantCache sharedInstance].cold.1
+ +[SizeContext sharedInstance].cold.1
+ -[EKCalendarChooserDefaultImpl _selectAllCalendarsAndStores:].cold.1
+ -[EKCalendarChooserDefaultImpl _selectCalendar:selected:].cold.1
+ -[EKCalendarChooserDefaultImpl _selectGroup:selected:].cold.1
+ -[EKCalendarChooserDefaultImpl initWithSelectionStyle:displayStyle:entityType:forEvent:eventStore:limitedToSource:showIdentityChooser:showDelegateSetupCell:showAccountStatus:].cold.1
+ -[EKCalendarChooserDefaultImpl setAllowsPullToRefresh:].cold.1
+ -[EKCalendarChooserDefaultImpl setChooserMode:].cold.1
+ -[EKCalendarEditor _deleteClicked:].cold.1
+ -[EKCalendarItemEditor _performDelete:].cold.1
+ -[EKCalendarItemEditor _presentDetachSheetForEvent:saveAttachments:withContinueBlock:].cold.1
+ -[EKCalendarItemLocationInlineEditItem cellForSubitemAtIndex:inEditor:].cold.1
+ -[EKCalendarItemLocationInlineEditItem cellForSubitemAtIndex:inEditor:].cold.2
+ -[EKCalendarItemLocationInlineEditItem cellForSubitemAtIndex:inEditor:].cold.3
+ -[EKDayAllDayView selectEvent:].cold.1
+ -[EKDayOccurrenceView _updateColors].cold.1
+ -[EKEventDetailLocationDisambiguationContentViewController _updateMapRegion].cold.1
+ -[EKEventDetailLocationDisambiguationContentViewController tableView:cellForRowAtIndexPath:].cold.1
+ -[EKEventEditItem setCalendarItem:store:].cold.1
+ -[EKEventGestureController _setUpAfterForcedStartFromPoint:].cold.1
+ -[EKEventGestureController _update].cold.1
+ -[EKEventRecurrenceEditItem setCalendarItem:store:].cold.1
+ -[EKEventStore(MobileCal) colorNamesInRainbowOrder].cold.1
+ -[EKEventStore(MobileCal) localizedStringForSymbolicColorName:].cold.1
+ -[EKLocationEditItemViewController _accessoryTypeForSection:].cold.1
+ -[EKRecurrenceMonthChooserController cellLabels].cold.1
+ -[EKRecurrenceMonthDayChooserController cellLabels].cold.1
+ -[EKRecurrenceOrdinalPickerViewController _leftColumn].cold.1
+ -[EKRecurrenceOrdinalPickerViewController _rightColumn].cold.1
+ -[EKSubscribedCalendarEditor _unsubscribeTapped:].cold.1
+ -[EKUICustomRecurrenceViewController _accessibilityIdentifierStringForFrequency:]
+ -[EKUIEventNotificationRepresentation initWithDictionary:].cold.1
+ -[EKUILocationSearchModel updateVirtualConferenceRoomOptions:].cold.1
+ -[EKUIVirtualConferenceSearchResultCell updateWithRoomType:].cold.1
+ -[EKUIYearMonthView _imageForDayNumber:size:underlineThickness:forPreview:].cold.1
+ -[EKUIYearMonthView _imageForMonthDays:size:underlineThickness:].cold.1
+ -[EKUIYearMonthView _imageForMonthName:].cold.1
+ -[SizeContext hasViewHierarchyForCurrentContext].cold.1
+ -[SizeContext popContextFromViewHierarchy:].cold.1
+ -[SizeContext popContextFromViewHierarchy:].cold.2
+ -[SizeContext viewHierarchyForCurrentContext].cold.1
+ -[UIResponder(EventKitUI) EKUI_editor].cold.1
+ BadgeImageForAlternateWorkday.cold.1
+ BadgeImageForHoliday.cold.1
+ CalInterfaceIsLeftToRight.cold.1
+ CalTimeDirectionIsLeftToRight.cold.1
+ CalendarAppCircleNonTodayBGColor.cold.1
+ CalendarAppCircleTextColor.cold.1
+ ClearButtonImageColor.cold.1
+ EKUIHeightForWindowSizeParadigm.cold.1
+ EKUIIOSMacLogHandle.cold.1
+ EKUILogInitIfNeeded.cold.1
+ EKUILogSignpostHandle.cold.1
+ EKUIMultiwindowAssert.cold.1
+ EKUIPixelSizeInPoints.cold.1
+ EKUIWidthForWindowSizeParadigm.cold.1
+ EventKitUIBundle.cold.1
+ _CUIKAccessibilityIdentifierStringForRepeatType
+ _CUIKAccessibilityIdentifierStringForRepeatTypeDetail
+ _CUIKAdaptiveAbbreviatedEmDashDayStringForDate
+ _CUIKAdaptiveLongEmDashDayStringForDate
+ _CachedSizeForButton.cold.1
+ _OBJC_CLASS_$_NSTextContentStorage
+ _OBJC_CLASS_$_NSTextLayoutManager
+ __132-[EKEventGestureController forceStartWithOccurrence:occurrenceDate:shouldUpdateViewSource:shouldUpdateOrigin:shouldPresentEditMenu:]_block_invoke.cold.1
+ __32-[EKEventDetailTitleCell update]_block_invoke.231
+ __36-[EKEventMapDetailItem setupMapView]_block_invoke.56
+ __37-[EKEventMapDetailItem _loadMapItem:]_block_invoke.62
+ __72-[EKEventDetailURLCell textView:primaryActionForTextItem:defaultAction:]_block_invoke.40
+ __72-[EKEventDetailURLCell textView:primaryActionForTextItem:defaultAction:]_block_invoke_2.42
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.212
+ __block_literal_global.219
+ __block_literal_global.24
+ __block_literal_global.242
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage_$_EventKitUI
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
+ __swift_FORCE_LOAD_$_swiftVideoToolbox_$_EventKitUI
+ _objc_msgSend$_accessibilityIdentifierStringForFrequency:
+ _objc_msgSend$_lp_userVisibleString
+ _objc_msgSend$accessibilityIdentifierForIndex:
+ _objc_msgSend$addTextLayoutManager:
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$setAttributedString:
+ _objc_msgSend$setTextContainer:
+ _objc_msgSend$trimWhiteSpace
+ _rootHierarchyForViewHierarchy.cold.1
+ _swift_setDeallocating
+ logHandle.cold.1
- +[EKDayAllDayView allDayLabelBoldFont]
- +[EKDayTimeView allDayLabelBoldFont]
- _CUIKAbbreviatedEmDashDayStringForDate
- _CUIKLongEmDashDayStringForDate
- _OBJC_CLASS_$_NSLayoutManager
- _OBJC_CLASS_$_NSTextStorage
- __32-[EKEventDetailTitleCell update]_block_invoke.229
- __36-[EKEventMapDetailItem setupMapView]_block_invoke.53
- __37-[EKEventMapDetailItem _loadMapItem:]_block_invoke.59
- __72-[EKEventDetailURLCell textView:primaryActionForTextItem:defaultAction:]_block_invoke.34
- __72-[EKEventDetailURLCell textView:primaryActionForTextItem:defaultAction:]_block_invoke_2.36
- __block_literal_global.210
- __block_literal_global.237
- __block_literal_global.39
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_EventKitUI
- _objc_msgSend$addLayoutManager:
- _objc_msgSend$addTextContainer:
- _objc_msgSend$allDayLabelBoldFont
- _symbolic _____Sg 10Foundation4DateV
CStrings:
+ "_accessibilityIdentifierStringForFrequency:"
+ "_lp_userVisibleString"
+ "accessibilityIdentifierForIndex:"
+ "add-attachment-cell"
+ "addTextLayoutManager:"
+ "alert-cell"
+ "all-day-switch"
+ "all-day-switch-cell"
+ "calendar-menu:%@:%@"
+ "calendar-preview-more-events-text"
+ "calendar-selection-cell"
+ "delete-alert-button"
+ "delete-all-events-alert-button"
+ "delete-all-future-events-alert-button"
+ "delete-event-cell"
+ "end-date-cell"
+ "end-date-picker-cell"
+ "end-repeat-cell"
+ "event-details-%@-cell"
+ "event-details-calendar-cell"
+ "event-details-comment-cell"
+ "event-details-conference-detail-cell"
+ "event-details-edit-button"
+ "event-details-location-map-cell"
+ "event-details-preview-cell"
+ "event-details-recurrence-button"
+ "event-details-recurrence-menu"
+ "event-details-suggested-location-cell"
+ "event-details-title-cell"
+ "event-details-title-text"
+ "event-details-travelt-time-cell"
+ "event-details-url-cell"
+ "event-details-url-link"
+ "event-shown:%@"
+ "frequency-cell"
+ "frequency-item:%@"
+ "interval-summary-cell"
+ "location-field"
+ "location-video-call-field"
+ "location-video-call-search-field"
+ "lowercaseString"
+ "notes-cell"
+ "notes-text-view"
+ "recurrence-show-next-button"
+ "recurrence-show-previous-button"
+ "repeat-cell"
+ "repeat-item:%@"
+ "second-alert-cell"
+ "setAttributedString:"
+ "setTextContainer:"
+ "start-date-picker-cell"
+ "tavel-time-menu-option:%@"
+ "textField:insertInputSuggestion:"
+ "textView:insertInputSuggestion:"
+ "title-field"
+ "travel-time-cell"
+ "travel-time-pop-up-menu"
+ "trimWhiteSpace"
+ "url-cell"
+ "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"
+ "v32@0:8@\"UITextView\"16@\"UIInputSuggestion\"24"
+ "video-call-field"
+ "year-ordinal-switch"
- "EventDetails-%@"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "addLayoutManager:"
- "addTextContainer:"
- "allDayLabelBoldFont"
- "invalid Collection: less than 'count' elements in collection"

```
