## EventKitUI

> `/System/Library/Frameworks/EventKitUI.framework/EventKitUI`

```diff

-1525.0.0.0.0
-  __TEXT.__text: 0x1d9aa0
-  __TEXT.__auth_stubs: 0x2240
-  __TEXT.__objc_methlist: 0x1f02c
+1528.0.0.0.0
+  __TEXT.__text: 0x1da704
+  __TEXT.__auth_stubs: 0x2250
+  __TEXT.__objc_methlist: 0x1f07c
   __TEXT.__const: 0x25a4
-  __TEXT.__cstring: 0xdbc1
-  __TEXT.__gcc_except_tab: 0x42f0
-  __TEXT.__oslogstring: 0x785d
-  __TEXT.__ustring: 0x87c
+  __TEXT.__cstring: 0xdcb1
+  __TEXT.__gcc_except_tab: 0x433c
+  __TEXT.__oslogstring: 0x78bd
+  __TEXT.__ustring: 0x862
   __TEXT.__dlopen_cstrs: 0x322
   __TEXT.__swift5_typeref: 0xd4e
   __TEXT.__swift5_capture: 0x4a8

   __TEXT.__swift5_types: 0xf8
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x7760
+  __TEXT.__unwind_info: 0x7778
   __TEXT.__eh_frame: 0x5d0
-  __TEXT.__objc_classname: 0x427f
-  __TEXT.__objc_methname: 0x4538d
-  __TEXT.__objc_methtype: 0xc266
-  __TEXT.__objc_stubs: 0x31e20
-  __DATA_CONST.__got: 0x1948
-  __DATA_CONST.__const: 0x4690
-  __DATA_CONST.__objc_classlist: 0xc68
+  __TEXT.__objc_classname: 0x426b
+  __TEXT.__objc_methname: 0x455bb
+  __TEXT.__objc_methtype: 0xc2ce
+  __TEXT.__objc_stubs: 0x31f00
+  __DATA_CONST.__got: 0x1968
+  __DATA_CONST.__const: 0x46e8
+  __DATA_CONST.__objc_classlist: 0xc60
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x620
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf618
+  __DATA_CONST.__objc_selrefs: 0xf620
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x8c0
-  __DATA_CONST.__objc_arraydata: 0x1f0
-  __AUTH_CONST.__auth_got: 0x1130
-  __AUTH_CONST.__const: 0x27b0
-  __AUTH_CONST.__cfstring: 0xb2a0
-  __AUTH_CONST.__objc_const: 0x305d8
+  __DATA_CONST.__objc_superrefs: 0x8b8
+  __DATA_CONST.__objc_arraydata: 0x1c0
+  __AUTH_CONST.__auth_got: 0x1138
+  __AUTH_CONST.__const: 0x2808
+  __AUTH_CONST.__cfstring: 0xb280
+  __AUTH_CONST.__objc_const: 0x30670
   __AUTH_CONST.__objc_arrayobj: 0x1f8
-  __AUTH_CONST.__objc_intobj: 0x570
+  __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__objc_dictobj: 0xf0
+  __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x7c38
-  __AUTH.__data: 0xbd0
-  __DATA.__objc_ivar: 0x251c
+  __AUTH.__objc_data: 0x7be8
+  __AUTH.__data: 0xbc0
+  __DATA.__objc_ivar: 0x2534
   __DATA.__data: 0x4b60
   __DATA.__bss: 0x1630
   __DATA.__common: 0x218

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 35581658-D57A-36E6-A5DD-3A8651F20D67
-  Functions: 11775
-  Symbols:   34915
-  CStrings:  16409
+  UUID: D5744F81-7E5B-3E72-8647-099798D4DC0C
+  Functions: 11785
+  Symbols:   34946
+  CStrings:  16436
 
Symbols:
+ +[EKDayAllDayView allDayWidth]
+ +[EKDayTimeView _calculateWidthForSizeClass:orientation:excludeCurrentTime:inViewHierarchy:]
+ +[EKDayTimeView _timeTextWidthForSizeClass:orientation:inViewHierarchy:]
+ +[EKEventURLDetailItem titleForCell]
+ +[EKEventURLDetailItem titleForExtendedViewController]
+ +[EKUICalendarListViewHeader _overlayCalendarHasLongString]
+ -[EKCalendarChooser hidesSuggestedEventCalendar]
+ -[EKCalendarChooser navigationDelegate]
+ -[EKCalendarChooser presentAddCalendarView]
+ -[EKCalendarChooser setHidesSuggestedEventCalendar:]
+ -[EKCalendarChooser setNavigationDelegate:]
+ -[EKCalendarChooserDefaultImpl hidesSuggestedEventCalendar]
+ -[EKCalendarChooserDefaultImpl presentAddCalendarView]
+ -[EKCalendarChooserDefaultImpl presentationNavigationDelegate]
+ -[EKCalendarChooserDefaultImpl setHidesSuggestedEventCalendar:]
+ -[EKCalendarChooserOOPWrapperImpl presentAddCalendarView]
+ -[EKDayTimeView setBackgroundColor:]
+ -[EKDayView _updateVerticalGridExtensionsForScrollView:]
+ -[EKDayViewController trackingAreaMinimumYPosition]
+ -[EKEventDetailTextCell _shouldTruncateGivenWidth:]
+ -[EKEventDetailTextCell initWithEvent:title:attributedTextFromEventBlock:textViewDelegate:axTextView:]
+ -[EKEventDetailTextCell initWithEvent:title:textFromEventBlock:]
+ -[EKEventDetailTextCell initWithEvent:title:textFromEventBlock:attributedTextFromEventBlock:textViewDelegate:axTextView:]
+ -[EKEventDetailTextCellHeader _contentCategorySizeChanged:]
+ -[EKEventDetailsHighlightControl initWithFrame:leadingMargin:]
+ -[EKEventGestureController _capOccurrenceViewYOrigin:ignoreTopInsets:]
+ -[EKEventReportJunkView reportButtonTapped]
+ -[EKEventReportJunkView updateConstraints]
+ -[EKEventURLDetailItem _createEventDetailCell]
+ -[EKEventURLDetailItem attributedTextFromEventBlock]
+ -[EKEventURLDetailItem linkWithLaunchInfo]
+ -[EKEventURLDetailItem linkWithURL]
+ -[EKEventURLDetailItem textForCopyAction]
+ -[EKEventURLDetailItem textForExtendedViewController]
+ -[EKEventURLDetailItem textView:primaryActionForTextItem:defaultAction:]
+ -[EKEventViewController dismissJunkView]
+ -[EKEventViewControllerDefaultImpl _contentSizeCategoryChanged:]
+ -[EKEventViewControllerDefaultImpl _createAndAddHeaderView]
+ -[EKEventViewControllerDefaultImpl dismissJunkView]
+ -[EKEventViewControllerOOPWrapperImpl _configureStatusButtonsToolbar]
+ -[EKEventViewControllerOOPWrapperImpl _updateResponseVisibility]
+ -[EKEventViewControllerOOPWrapperImpl dismissJunkView]
+ -[EKEventViewControllerOOPWrapperImpl statusButtonActions]
+ -[EKEventViewControllerOOPWrapperImpl updateStatusButtonsView]
+ -[EKEventViewControllerOOPWrapperImpl viewTitle]
+ -[EKEventViewControllerOOPWrapperImpl viewWillLayoutSubviews]
+ -[EKUICalendarListContentConfiguration setUseAccessibilityLayoutForAltCalendarText:]
+ -[EKUICalendarListContentConfiguration useAccessibilityLayoutForAltCalendarText]
+ -[EKUIListViewCellBackground updateBackgroundColorForEvent:highlighted:dimmed:carplayMode:dragPreview:traitCollection:]
+ GCC_except_table101
+ GCC_except_table129
+ GCC_except_table159
+ GCC_except_table170
+ GCC_except_table178
+ GCC_except_table225
+ GCC_except_table233
+ GCC_except_table39
+ GCC_except_table68
+ _EKUITableViewCellCornerRadius
+ _NSCalendarIdentifierChinese
+ _NSCalendarIdentifierHebrew
+ _NSCalendarIdentifierVietnamese
+ _OBJC_CLASS_$_UIGlassEffect
+ _OBJC_IVAR_$_EKCalendarChooserDefaultImpl._hidesSuggestedEventCalendar
+ _OBJC_IVAR_$_EKEventDetailTextCell._attributedTextFromEventBlock
+ _OBJC_IVAR_$_EKEventReportJunkView._bannerView
+ _OBJC_IVAR_$_EKEventReportJunkView._centerXConstraint
+ _OBJC_IVAR_$_EKEventReportJunkView._containerLeadingConstraint
+ _OBJC_IVAR_$_EKEventReportJunkView._containerTrailingConstraint
+ _OBJC_IVAR_$_EKEventReportJunkView._containerView
+ _OBJC_IVAR_$_EKEventReportJunkView._containerWidthConstraint
+ _OBJC_IVAR_$_EKEventReportJunkView._effectView
+ _OBJC_IVAR_$_EKEventReportJunkView._reportButton
+ _OBJC_IVAR_$_EKEventReportJunkView._reportLabel
+ _OBJC_IVAR_$_EKEventViewControllerDefaultImpl._junkView
+ _OBJC_IVAR_$_EKUICalendarListContentConfiguration._useAccessibilityLayoutForAltCalendarText
+ _OBJC_IVAR_$_EKUICalendarListViewHeaderContentView._activatedConstraints
+ _OBJC_IVAR_$_EKUICalendarListViewHeaderContentView._activatedConstraintsIsForAccessibilityLayout
+ __OBJC_$_PROP_LIST_EKEventURLDetailItem
+ __OBJC_CLASS_PROTOCOLS_$_EKEventURLDetailItem
+ ___151-[EKDayView initWithFrame:sizeClass:orientation:displayDate:backgroundColor:opaque:scrollbarShowsInside:isMiniPreviewInEventDetail:rightClickDelegate:]_block_invoke
+ ___32-[EKEventDetailTitleCell update]_block_invoke.235
+ ___44-[EKEventDetailLocationItem _locationTapped]_block_invoke.35
+ ___48-[EKEventReportJunkView initWithViewController:]_block_invoke
+ ___48-[EKEventReportJunkView initWithViewController:]_block_invoke_2
+ ___52-[EKEventURLDetailItem attributedTextFromEventBlock]_block_invoke
+ ___72-[EKEventURLDetailItem textView:primaryActionForTextItem:defaultAction:]_block_invoke
+ ___72-[EKEventURLDetailItem textView:primaryActionForTextItem:defaultAction:]_block_invoke.43
+ ___72-[EKEventURLDetailItem textView:primaryActionForTextItem:defaultAction:]_block_invoke_2
+ ___72-[EKEventURLDetailItem textView:primaryActionForTextItem:defaultAction:]_block_invoke_2.45
+ ___block_descriptor_40_e8_32w_e37_"NSAttributedString"16?0"EKEvent"8lw32l8
+ ___block_descriptor_48_e8_32s40w_e52_v24?0"<UITraitEnvironment>"8"UITraitCollection"16lw40l8s32l8
+ ___block_literal_global.38
+ ___block_literal_global.48
+ ___swift_memcpy0_1
+ ___swift_noop_void_return
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_EventKitUI
+ _objc_msgSend$_calculateWidthForSizeClass:orientation:excludeCurrentTime:inViewHierarchy:
+ _objc_msgSend$_capOccurrenceViewYOrigin:ignoreTopInsets:
+ _objc_msgSend$_clearVerticalGridExtensionImageCache
+ _objc_msgSend$_createAndAddHeaderView
+ _objc_msgSend$_overlayCalendarHasLongString
+ _objc_msgSend$_preferredFontDescriptorWithTextStyle:weight:
+ _objc_msgSend$_shouldTruncateGivenWidth:
+ _objc_msgSend$_timeTextWidthForSizeClass:orientation:inViewHierarchy:
+ _objc_msgSend$_updateVerticalGridExtensionsForScrollView:
+ _objc_msgSend$allDayWidth
+ _objc_msgSend$attributedTextFromEventBlock
+ _objc_msgSend$constraintLessThanOrEqualToConstant:
+ _objc_msgSend$currentAllDayView
+ _objc_msgSend$dismissJunkView
+ _objc_msgSend$hidesSuggestedEventCalendar
+ _objc_msgSend$identifierString
+ _objc_msgSend$initWithEvent:title:attributedTextFromEventBlock:textViewDelegate:axTextView:
+ _objc_msgSend$initWithEvent:title:textFromEventBlock:
+ _objc_msgSend$initWithEvent:title:textFromEventBlock:attributedTextFromEventBlock:textViewDelegate:axTextView:
+ _objc_msgSend$initWithFrame:leadingMargin:
+ _objc_msgSend$linkWithLaunchInfo
+ _objc_msgSend$linkWithURL
+ _objc_msgSend$presentAddCalendarView
+ _objc_msgSend$presentationStyle
+ _objc_msgSend$recurrenceIdentifier
+ _objc_msgSend$reportButtonTapped
+ _objc_msgSend$setHidesSuggestedEventCalendar:
+ _objc_msgSend$setLineSpacing:
+ _objc_msgSend$setNeedsUpdateProperties
+ _objc_msgSend$setUseAccessibilityLayoutForAltCalendarText:
+ _objc_msgSend$systemOrangeColor
+ _objc_msgSend$tertiarySystemFillColor
+ _objc_msgSend$topContentInset
+ _objc_msgSend$trackingAreaMinimumYPosition
+ _objc_msgSend$updateBackgroundColorForEvent:highlighted:dimmed:carplayMode:dragPreview:traitCollection:
+ _objc_msgSend$useAccessibilityLayoutForAltCalendarText
+ _s_allDayWidth
- +[EKDayAllDayView shouldTimeBarWidthMatchAllDayTextWithResultWidth:]
- +[EKDayTimeView _calculateWidthForSizeClass:orientation:excludeCurrentTime:]
- +[EKDayTimeView _timeTextWidthForSizeClass:orientation:]
- +[EKDayTimeView hourWidthForSizeClass:orientation:]
- +[EKEventDetailURLCell _SGSuggestionsServiceClass]
- -[EKCalendarChooserOOPWrapperImpl addCalendarButtonPressed:]
- -[EKCalendarChooserOOPWrapperImpl safeAreaCaulk]
- -[EKCalendarChooserOOPWrapperImpl setSafeAreaCaulk:]
- -[EKDayView setSizeTimeViewUsingOnlyHourText:]
- -[EKDayView sizeTimeViewUsingOnlyHourText]
- -[EKEventAttachmentsEditItem defaultCellHeightForSubitemAtIndex:forWidth:]
- -[EKEventCommentDetailItem defaultCellHeightForSubitemAtIndex:forWidth:forceUpdate:]
- -[EKEventConferenceDetailItem defaultCellHeightForSubitemAtIndex:forWidth:forceUpdate:]
- -[EKEventDetailExtendedTextViewController loadView]
- -[EKEventDetailProposeNewTimeCell hasCustomLayout]
- -[EKEventDetailProposedTimeCell hasCustomLayout]
- -[EKEventDetailTextCell _headerView]
- -[EKEventDetailTextCell _sizeForTextViewGivenWidth:outTruncatingText:]
- -[EKEventDetailTextCell _textView]
- -[EKEventDetailTextCell initWithEvent:editable:title:textFromEventBlock:]
- -[EKEventDetailTextCell layoutForWidth:position:]
- -[EKEventDetailURLCell .cxx_destruct]
- -[EKEventDetailURLCell _URLTitleView]
- -[EKEventDetailURLCell _URLView]
- -[EKEventDetailURLCell _layoutForWidth:position:]
- -[EKEventDetailURLCell initWithEvent:launchInfo:editable:style:]
- -[EKEventDetailURLCell initWithEvent:url:editable:style:]
- -[EKEventDetailURLCell layoutForWidth:position:]
- -[EKEventDetailURLCell layoutSubviews]
- -[EKEventDetailURLCell textView:primaryActionForTextItem:defaultAction:]
- -[EKEventDetailURLCell updateLinkWithLaunchInfo]
- -[EKEventDetailURLCell updateLinkWithURL]
- -[EKEventDetailURLCell updateLink]
- -[EKEventDetailURLCell updateWithURL:launchInfo:]
- -[EKEventDetailURLCell update]
- -[EKEventReportJunkView didMoveToSuperview]
- -[EKEventReportJunkView tapped:]
- -[EKEventReportJunkView tintColorDidChange]
- -[EKEventReportJunkView updateActionText]
- -[EKEventSuggestedLocationDetailItem defaultCellHeightForSubitemAtIndex:forWidth:forceUpdate:]
- -[EKEventURLDetailItem _updateWithChanges]
- -[EKEventURLDetailItem cellForSubitemAtIndex:]
- -[EKEventURLDetailItem defaultCellHeightForSubitemAtIndex:forWidth:forceUpdate:]
- -[EKEventURLDetailItem hasDetailViewControllerAtIndex:]
- -[EKEventViewControllerDefaultImpl _updateTableContentForSizeCategoryChange:]
- -[EKEventViewControllerOOPWrapperImpl _setupStatusToolbarButtons]
- -[EKEventViewControllerOOPWrapperImpl statusButtons]
- -[EKUIListViewCellBackground updateBackgroundColorForEvent:highlighted:dimmed:carplayMode:dragPreview:]
- GCC_except_table157
- GCC_except_table168
- GCC_except_table177
- GCC_except_table224
- GCC_except_table232
- GCC_except_table38
- _OBJC_CLASS_$_EKEventDetailURLCell
- _OBJC_IVAR_$_EKCalendarChooserOOPWrapperImpl._safeAreaCaulk
- _OBJC_IVAR_$_EKDayView._sizeTimeViewUsingOnlyHourText
- _OBJC_IVAR_$_EKEventDetailURLCell._URLTitleView
- _OBJC_IVAR_$_EKEventDetailURLCell._URLView
- _OBJC_IVAR_$_EKEventDetailURLCell._lastLayoutPosition
- _OBJC_IVAR_$_EKEventDetailURLCell._launchInfo
- _OBJC_IVAR_$_EKEventDetailURLCell._url
- _OBJC_IVAR_$_EKEventReportJunkView._control
- _OBJC_IVAR_$_EKEventViewControllerDefaultImpl._tableViewTopConstraints
- _OBJC_METACLASS_$_EKEventDetailURLCell
- __OBJC_$_CLASS_METHODS_EKEventDetailURLCell
- __OBJC_$_INSTANCE_METHODS_EKEventDetailURLCell
- __OBJC_$_INSTANCE_VARIABLES_EKEventDetailURLCell
- __OBJC_$_PROP_LIST_EKEventDetailURLCell
- __OBJC_CLASS_PROTOCOLS_$_EKEventDetailURLCell
- __OBJC_CLASS_RO_$_EKEventDetailURLCell
- __OBJC_METACLASS_RO_$_EKEventDetailURLCell
- ___32-[EKEventDetailTitleCell update]_block_invoke.234
- ___44-[EKEventDetailLocationItem _locationTapped]_block_invoke.34
- ___72-[EKEventDetailURLCell textView:primaryActionForTextItem:defaultAction:]_block_invoke
- ___72-[EKEventDetailURLCell textView:primaryActionForTextItem:defaultAction:]_block_invoke.40
- ___72-[EKEventDetailURLCell textView:primaryActionForTextItem:defaultAction:]_block_invoke_2
- ___72-[EKEventDetailURLCell textView:primaryActionForTextItem:defaultAction:]_block_invoke_2.42
- ___block_literal_global.246
- _objc_msgSend$_URLTitleView
- _objc_msgSend$_URLView
- _objc_msgSend$_calculateWidthForSizeClass:orientation:excludeCurrentTime:
- _objc_msgSend$_headerView
- _objc_msgSend$_layoutForWidth:position:
- _objc_msgSend$_setupStatusToolbarButtons
- _objc_msgSend$_sizeForTextViewGivenWidth:outTruncatingText:
- _objc_msgSend$_textView
- _objc_msgSend$_timeTextWidthForSizeClass:orientation:
- _objc_msgSend$_updateWithChanges
- _objc_msgSend$additionalLeftPadding
- _objc_msgSend$darkerColorWithFactor:
- _objc_msgSend$hourWidthForSizeClass:orientation:
- _objc_msgSend$initWithEvent:editable:title:textFromEventBlock:
- _objc_msgSend$initWithEvent:launchInfo:editable:style:
- _objc_msgSend$initWithEvent:url:editable:style:
- _objc_msgSend$leftAnchor
- _objc_msgSend$rightAnchor
- _objc_msgSend$safeAreaCaulk
- _objc_msgSend$setActionText:color:
- _objc_msgSend$setSafeAreaCaulk:
- _objc_msgSend$shouldTimeBarWidthMatchAllDayTextWithResultWidth:
- _objc_msgSend$sizeTimeViewUsingOnlyHourText
- _objc_msgSend$updateActionText
- _objc_msgSend$updateBackgroundColorForEvent:highlighted:dimmed:carplayMode:dragPreview:
- _objc_msgSend$updateLink
- _objc_msgSend$updateLinkWithLaunchInfo
- _objc_msgSend$updateLinkWithURL
- _objc_msgSend$updateWithURL:launchInfo:
CStrings:
+ "    View->occurrence = %@\n"
+ "    View->occurrenceArray = %@\n"
+ "    recurrence ID: %{public}@"
+ "@\"<EKEventEditViewDelegateAllOutOfProcess>\""
+ "@\"EKEventReportJunkView\""
+ "@\"NSAttributedString\"16@?0@\"EKEvent\"8"
+ "@56@0:8@16@24@?32@40@48"
+ "@56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16d48"
+ "@64@0:8@16@24@?32@?40@48@56"
+ "Delete This Event Only"
+ "Stack height is 0, implying that occurrence view is visible without associated occurrence. View = %@\n"
+ "TB,N,V_hidesSuggestedEventCalendar"
+ "TB,N,V_useAccessibilityLayoutForAltCalendarText"
+ "V:|-(10)-[_control(>=48)]-(10)-|"
+ "V:|-8-[junkView][dividerView(==separatorLineThickness)]|"
+ "V:|[_tableView]|"
+ "_activatedConstraints"
+ "_activatedConstraintsIsForAccessibilityLayout"
+ "_attributedTextFromEventBlock"
+ "_bannerView"
+ "_calculateWidthForSizeClass:orientation:excludeCurrentTime:inViewHierarchy:"
+ "_capOccurrenceViewYOrigin:ignoreTopInsets:"
+ "_centerXConstraint"
+ "_containerLeadingConstraint"
+ "_containerTrailingConstraint"
+ "_containerWidthConstraint"
+ "_createAndAddHeaderView"
+ "_hidesSuggestedEventCalendar"
+ "_junkView"
+ "_overlayCalendarHasLongString"
+ "_preferredFontDescriptorWithTextStyle:weight:"
+ "_reportButton"
+ "_reportLabel"
+ "_shouldTruncateGivenWidth:"
+ "_timeTextWidthForSizeClass:orientation:inViewHierarchy:"
+ "_updateVerticalGridExtensionsForScrollView:"
+ "_useAccessibilityLayoutForAltCalendarText"
+ "allDayWidth"
+ "attributedTextFromEventBlock"
+ "constraintLessThanOrEqualToConstant:"
+ "d40@0:8q16q24@32"
+ "dangi"
+ "dismissJunkView"
+ "hidesSuggestedEventCalendar"
+ "identifierString"
+ "initWithEvent:title:attributedTextFromEventBlock:textViewDelegate:axTextView:"
+ "initWithEvent:title:textFromEventBlock:"
+ "initWithEvent:title:textFromEventBlock:attributedTextFromEventBlock:textViewDelegate:axTextView:"
+ "initWithFrame:leadingMargin:"
+ "islamic-civil"
+ "linkWithLaunchInfo"
+ "linkWithURL"
+ "presentAddCalendarView"
+ "recurrenceIdentifier"
+ "reportButtonTapped"
+ "setHidesSuggestedEventCalendar:"
+ "setLineSpacing:"
+ "setNeedsUpdateProperties"
+ "setUseAccessibilityLayoutForAltCalendarText:"
+ "systemOrangeColor"
+ "tertiarySystemFillColor"
+ "trackingAreaMinimumYPosition"
+ "updateBackgroundColorForEvent:highlighted:dimmed:carplayMode:dragPreview:traitCollection:"
+ "useAccessibilityLayoutForAltCalendarText"
+ "v44@0:8q16q24B32@36"
+ "v48@0:8@16B24B28B32B36@40"
- "@44@0:8@16B24@28@?36"
- "B24@0:8^d16"
- "Delete Only This Event"
- "EKEventDetailURLCell"
- "H:|[_control]-(16)-|"
- "R"
- "T@\"UIView\",&,N,V_safeAreaCaulk"
- "TB,N,V_sizeTimeViewUsingOnlyHourText"
- "V:[_tableView]|"
- "V:|[_control]|"
- "V:|[_tableView]"
- "V:|[junkView][dividerView(==separatorLineThickness)]|"
- "We are displaying a cell with no launchInfo and no url. This should not be possible."
- "_URLTitleView"
- "_URLView"
- "_calculateWidthForSizeClass:orientation:excludeCurrentTime:"
- "_lastLayoutPosition"
- "_layoutForWidth:position:"
- "_safeAreaCaulk"
- "_setupStatusToolbarButtons"
- "_sizeForTextViewGivenWidth:outTruncatingText:"
- "_sizeTimeViewUsingOnlyHourText"
- "_tableViewTopConstraints"
- "_timeTextWidthForSizeClass:orientation:"
- "_updateTableContentForSizeCategoryChange:"
- "_updateWithChanges"
- "a"
- "darkerColorWithFactor:"
- "hasCustomLayout"
- "hourWidthForSizeClass:orientation:"
- "initWithEvent:editable:title:textFromEventBlock:"
- "initWithEvent:launchInfo:editable:style:"
- "initWithEvent:url:editable:style:"
- "leftAnchor"
- "rightAnchor"
- "safeAreaCaulk"
- "setSafeAreaCaulk:"
- "setSizeTimeViewUsingOnlyHourText:"
- "shouldTimeBarWidthMatchAllDayTextWithResultWidth:"
- "sizeTimeViewUsingOnlyHourText"
- "tapped:"
- "updateActionText"
- "updateBackgroundColorForEvent:highlighted:dimmed:carplayMode:dragPreview:"
- "updateLink"
- "updateLinkWithLaunchInfo"
- "updateLinkWithURL"
- "updateWithURL:launchInfo:"
- "v40@0:8@16B24B28B32B36"
- "{CGSize=dd}32@0:8d16^B24"

```
