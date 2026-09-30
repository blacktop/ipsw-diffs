## EventKitUI

> `/System/Library/Frameworks/EventKitUI.framework/EventKitUI`

```diff

-1521.1.0.0.0
-  __TEXT.__text: 0x1d6dcc
+1523.0.0.0.0
+  __TEXT.__text: 0x1d8e74
   __TEXT.__auth_stubs: 0x2240
-  __TEXT.__objc_methlist: 0x1ed8c
-  __TEXT.__const: 0x2584
+  __TEXT.__objc_methlist: 0x1ef94
+  __TEXT.__const: 0x2594
   __TEXT.__cstring: 0xdc01
-  __TEXT.__gcc_except_tab: 0x428c
+  __TEXT.__gcc_except_tab: 0x42d8
   __TEXT.__oslogstring: 0x785d
-  __TEXT.__ustring: 0x8ca
+  __TEXT.__ustring: 0x8b2
   __TEXT.__dlopen_cstrs: 0x322
   __TEXT.__swift5_typeref: 0xd4e
   __TEXT.__swift5_capture: 0x4a8

   __TEXT.__swift5_types: 0xf8
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x7608
+  __TEXT.__unwind_info: 0x7730
   __TEXT.__eh_frame: 0x5d0
-  __TEXT.__objc_classname: 0x4265
-  __TEXT.__objc_methname: 0x44f68
-  __TEXT.__objc_methtype: 0xc1bd
-  __TEXT.__objc_stubs: 0x31b60
-  __DATA_CONST.__got: 0x1940
-  __DATA_CONST.__const: 0x4658
-  __DATA_CONST.__objc_classlist: 0xc60
+  __TEXT.__objc_classname: 0x427f
+  __TEXT.__objc_methname: 0x451c0
+  __TEXT.__objc_methtype: 0xc215
+  __TEXT.__objc_stubs: 0x31d20
+  __DATA_CONST.__got: 0x1948
+  __DATA_CONST.__const: 0x4690
+  __DATA_CONST.__objc_classlist: 0xc68
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x620
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf528
+  __DATA_CONST.__objc_selrefs: 0xf5b8
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x8b8
+  __DATA_CONST.__objc_superrefs: 0x8c0
   __DATA_CONST.__objc_arraydata: 0x1c8
   __AUTH_CONST.__auth_got: 0x1130
   __AUTH_CONST.__const: 0x2770
-  __AUTH_CONST.__cfstring: 0xb3c0
-  __AUTH_CONST.__objc_const: 0x302d0
+  __AUTH_CONST.__cfstring: 0xb360
+  __AUTH_CONST.__objc_const: 0x30560
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x7be8
+  __AUTH.__objc_data: 0x7c38
   __AUTH.__data: 0xbd0
-  __DATA.__objc_ivar: 0x24dc
+  __DATA.__objc_ivar: 0x2510
   __DATA.__data: 0x4b60
-  __DATA.__bss: 0x15f0
+  __DATA.__bss: 0x1610
   __DATA.__common: 0x218
   __DATA_DIRTY.__objc_data: 0x13b0
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 584DC519-8F14-3ED5-BA49-168903AE4A6B
-  Functions: 11715
-  Symbols:   34740
-  CStrings:  16369
+  UUID: 580C7491-598A-3AFA-BC64-CF959609E91D
+  Functions: 11758
+  Symbols:   34865
+  CStrings:  16400
 
Symbols:
+ +[EKReminderTitleDetailCell _dateFont]
+ +[EKReminderTitleDetailCell _invalidateCachedFonts]
+ +[EKReminderTitleDetailCell _registerForInvalidation]
+ -[EKCalendarChooserDefaultImpl _addCalendarButtonSection]
+ -[EKCalendarChooserDefaultImpl _configureAddCalendarButtonCell:indexPath:item:]
+ -[EKCalendarChooserDefaultImpl _isAddCalendarButtonSection:]
+ -[EKCalendarChooserDefaultImpl _menuForAddCalendarButton:]
+ -[EKCalendarChooserDefaultImpl _shouldShowAddCalendarButtonSection]
+ -[EKCalendarEditor viewWillAppear:]
+ -[EKDayOccurrenceView setCurrentImageState:]
+ -[EKDayPreviewController dayViewShouldDrawSynchronously:]
+ -[EKDayPreviewController presentationControllerForEditMenu]
+ -[EKDayPreviewController selectedEventsForEditMenu]
+ -[EKDayView additionalGridCurtainHeight]
+ -[EKDayView leadingMargin]
+ -[EKDayView setAdditionalGridCurtainHeight:]
+ -[EKDayView setLeadingMargin:]
+ -[EKDayViewContent occurrenceLayoutLeadingInset]
+ -[EKDayViewContent occurrenceLayoutTrailingInset]
+ -[EKDayViewContent setOccurrenceLayoutLeadingInset:]
+ -[EKDayViewContent setOccurrenceLayoutTrailingInset:]
+ -[EKDayViewContentItem setCurrentState:]
+ -[EKEventEditViewControllerModernImpl _configureStatusButtonsToolbar]
+ -[EKEventTitleDetailItem titleShouldInsetForEditButton:]
+ -[EKEventViewControllerDefaultImpl _configureStatusButtonsToolbar]
+ -[EKEventViewControllerDefaultImpl _customInsets]
+ -[EKEventViewControllerDefaultImpl _presentedInAPopOver]
+ -[EKEventViewControllerDefaultImpl titleShouldInsetForEditButton:]
+ -[EKEventViewControllerDefaultImpl useDynamicPocket]
+ -[EKReminderDetailTextCell _updateTextViewColorAndFont]
+ -[EKReminderDetailTextCell commonSetupCellWithTitle:showExtraSpaceAtBottom:]
+ -[EKReminderDetailTextCell hideBottomCellSeparator]
+ -[EKReminderDetailTextCell initWithEvent:reminder:editable:showExtraSpaceAtBottom:allowDataDetector:title:textFromEventAndReminderBlock:noBackgroundStyle:]
+ -[EKReminderDetailTextCell setHideBottomCellSeparator:]
+ -[EKReminderDetailTextCell setTitleFont:]
+ -[EKReminderDetailTextCell setTitleTextColor:]
+ -[EKReminderListDetailItem _createEventDetailCell]
+ -[EKReminderNotesDetailItem showExtraSpaceAtBottom]
+ -[EKReminderTextDetailItem defaultCellHeightForSubitemAtIndex:forWidth:forceUpdate:]
+ -[EKReminderTitleDetailCell _editButton]
+ -[EKReminderTitleDetailItem titleShouldInsetForEditButton:]
+ -[EKReminderURLDetailItem hasCellBelow]
+ -[EKReminderURLDetailItem showExtraSpaceAtBottom]
+ -[EKShowInRemindersDetailCell didTap]
+ -[EKShowInRemindersDetailItem eventViewController:didSelectReadOnlySubitem:]
+ -[EKShowInRemindersDetailItem section]
+ -[EKUIAvailabilityViewController cancelButton]
+ -[EKUIAvailabilityViewController largeDateNavItem]
+ -[EKUIAvailabilityViewController setCancelButton:]
+ -[EKUIAvailabilityViewController setLargeDateNavItem:]
+ -[EKUIEventStatusButtonsView _configureButton:forAction:]
+ -[EKUIHorizontalGradientView .cxx_destruct]
+ -[EKUIHorizontalGradientView drawRect:]
+ -[EKUIHorizontalGradientView initWithStartColor:endColor:start:end:]
+ -[EKUIHorizontalGradientView layoutSublayersOfLayer:]
+ GCC_except_table119
+ GCC_except_table120
+ GCC_except_table125
+ GCC_except_table127
+ GCC_except_table133
+ GCC_except_table137
+ GCC_except_table139
+ GCC_except_table141
+ GCC_except_table145
+ GCC_except_table147
+ GCC_except_table149
+ GCC_except_table156
+ GCC_except_table161
+ GCC_except_table202
+ GCC_except_table42
+ GCC_except_table73
+ GCC_except_table88
+ GCC_except_table98
+ _CalDetailStringsForReminderEvent
+ _CollectionViewRowIdentifierAddCalendarButton
+ _CollectionViewSectionIdentifierAddCalendarButton
+ _OBJC_CLASS_$_CAGradientLayer
+ _OBJC_CLASS_$_EKUIHorizontalGradientView
+ _OBJC_IVAR_$_EKCalendarChooserDefaultImpl._addCalendarBarButton
+ _OBJC_IVAR_$_EKDayView._additionalGridCurtainHeight
+ _OBJC_IVAR_$_EKDayView._leadingMargin
+ _OBJC_IVAR_$_EKDayViewContent._occurrenceLayoutLeadingInset
+ _OBJC_IVAR_$_EKDayViewContent._occurrenceLayoutTrailingInset
+ _OBJC_IVAR_$_EKEventViewControllerDefaultImpl._previewItem
+ _OBJC_IVAR_$_EKReminderDetailTextCell._hideBottomCellSeparator
+ _OBJC_IVAR_$_EKReminderDetailTextCell._noBackgroundStyle
+ _OBJC_IVAR_$_EKReminderTitleDetailCell._bottomView
+ _OBJC_IVAR_$_EKReminderTitleDetailCell._dateLabelLine1
+ _OBJC_IVAR_$_EKReminderTitleDetailCell._dateLabelLine2
+ _OBJC_IVAR_$_EKReminderTitleDetailCell._dateLabelLine3
+ _OBJC_IVAR_$_EKReminderTitleDetailCell._dateLabelLine4
+ _OBJC_IVAR_$_EKReminderTitleDetailCell._recurrenceLabel
+ _OBJC_IVAR_$_EKShowInRemindersDetailCell._titleLabel
+ _OBJC_IVAR_$_EKUIAvailabilityViewController._cancelButton
+ _OBJC_IVAR_$_EKUIAvailabilityViewController._largeDateNavItem
+ _OBJC_IVAR_$_EKUIHorizontalGradientView._endColor
+ _OBJC_IVAR_$_EKUIHorizontalGradientView._endPoint
+ _OBJC_IVAR_$_EKUIHorizontalGradientView._gradientLayer
+ _OBJC_IVAR_$_EKUIHorizontalGradientView._startColor
+ _OBJC_IVAR_$_EKUIHorizontalGradientView._startPoint
+ _OBJC_METACLASS_$_EKUIHorizontalGradientView
+ __OBJC_$_CLASS_METHODS_EKReminderTitleDetailCell
+ __OBJC_$_INSTANCE_METHODS_EKUIHorizontalGradientView
+ __OBJC_$_INSTANCE_VARIABLES_EKUIHorizontalGradientView
+ __OBJC_$_PROP_LIST_EKReminderDetailTextCell
+ __OBJC_CLASS_RO_$_EKUIHorizontalGradientView
+ __OBJC_METACLASS_RO_$_EKUIHorizontalGradientView
+ ___35-[EKCalendarEditor _deleteCalendar]_block_invoke.60
+ ___37-[EKShowInRemindersDetailCell didTap]_block_invoke
+ ___40-[EKCalendarChooserDefaultImpl loadView]_block_invoke_15
+ ___45-[EKUIAvailabilityViewController doneTapped:]_block_invoke.133
+ ___53+[EKReminderTitleDetailCell _registerForInvalidation]_block_invoke
+ ___57-[EKUIEventStatusButtonsView _configureButton:forAction:]_block_invoke
+ ___58-[EKCalendarChooserDefaultImpl _menuForAddCalendarButton:]_block_invoke
+ ___58-[EKCalendarChooserDefaultImpl _menuForAddCalendarButton:]_block_invoke_2
+ ___58-[EKCalendarChooserDefaultImpl _menuForAddCalendarButton:]_block_invoke_3
+ ___58-[EKCalendarChooserDefaultImpl _menuForAddCalendarButton:]_block_invoke_4
+ ___64-[EKCalendarChooserDefaultImpl openAddRegularCalendarWithTitle:]_block_invoke
+ ___64-[EKCalendarChooserDefaultImpl openAddRegularCalendarWithTitle:]_block_invoke_2
+ ___65-[EKCalendarChooserDefaultImpl showAddSubscribedCalendarWithURL:]_block_invoke_2
+ ___65-[EKCalendarChooserDefaultImpl showAddSubscribedCalendarWithURL:]_block_invoke_3
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104s112w_e77_"UICollectionViewCell"32?0"UICollectionView"8"NSIndexPath"16"NSString"24lw112l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_56_e8_32s40s48s_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_literal_global.190
+ ___block_literal_global.277
+ ___block_literal_global.291
+ ___block_literal_global.433
+ ___block_literal_global.456
+ ___block_literal_global.81
+ _kEmptyViewForPocketHeight
+ _objc_msgSend$_addCalendarButtonSection
+ _objc_msgSend$_configureAddCalendarButtonCell:indexPath:item:
+ _objc_msgSend$_configureButton:forAction:
+ _objc_msgSend$_configureStatusButtonsToolbar
+ _objc_msgSend$_customInsets
+ _objc_msgSend$_dateFont
+ _objc_msgSend$_isAddCalendarButtonSection:
+ _objc_msgSend$_menuForAddCalendarButton:
+ _objc_msgSend$_shouldShowAddCalendarButtonSection
+ _objc_msgSend$_updateTextViewColorAndFont
+ _objc_msgSend$additionalGridCurtainHeight
+ _objc_msgSend$cancelButton
+ _objc_msgSend$commonSetupCellWithTitle:showExtraSpaceAtBottom:
+ _objc_msgSend$defaultFontForTextStyle:
+ _objc_msgSend$didTap
+ _objc_msgSend$eventViewControllerPresentedInAPopover:
+ _objc_msgSend$hasCellBelow
+ _objc_msgSend$initWithEvent:reminder:editable:showExtraSpaceAtBottom:allowDataDetector:title:textFromEventAndReminderBlock:noBackgroundStyle:
+ _objc_msgSend$initWithStartColor:endColor:start:end:
+ _objc_msgSend$initWithState:
+ _objc_msgSend$insertSublayer:atIndex:
+ _objc_msgSend$largeDateNavItem
+ _objc_msgSend$leadingMargin
+ _objc_msgSend$nextButton
+ _objc_msgSend$secondarySystemFillColor
+ _objc_msgSend$setAdditionalGridCurtainHeight:
+ _objc_msgSend$setColors:
+ _objc_msgSend$setCurrentImageState:
+ _objc_msgSend$setCurrentState:
+ _objc_msgSend$setEndPoint:
+ _objc_msgSend$setHidesSharedBackground:
+ _objc_msgSend$setLeadingItemGroups:
+ _objc_msgSend$setLeadingMargin:
+ _objc_msgSend$setOccurrenceLayoutLeadingInset:
+ _objc_msgSend$setOccurrenceLayoutTrailingInset:
+ _objc_msgSend$setSharesBackground:
+ _objc_msgSend$setStartPoint:
+ _objc_msgSend$sheetPresentationController
+ _objc_msgSend$titleShouldInsetForEditButton:
+ _objc_msgSend$useDynamicPocket
+ _s_dateFont
- +[EKReminderListDetailItem bottomSpaceAdjustment]
- +[EKReminderTextDetailItem bottomSpaceAdjustment]
- -[EKEventViewControllerDefaultImpl setBottomInset:]
- -[EKReminderDetailTextCell commonSetupCellWithTitle:showExtraSpaceAtBottom:extraBottomSpaceAdjustment:]
- -[EKReminderDetailTextCell initWithEvent:reminder:editable:showExtraSpaceAtBottom:extraBottomSpaceAdjustment:allowDataDetector:title:textFromEventAndReminderBlock:]
- -[EKUIAvailabilityViewController dateNavContainer]
- -[EKUIAvailabilityViewController largeDateNavContainer]
- -[EKUIAvailabilityViewController largeNavLeadingConstraint]
- -[EKUIAvailabilityViewController participantDivider]
- -[EKUIAvailabilityViewController setDateNavContainer:]
- -[EKUIAvailabilityViewController setLargeDateNavContainer:]
- -[EKUIAvailabilityViewController setLargeNavLeadingConstraint:]
- -[EKUIAvailabilityViewController setParticipantDivider:]
- -[EKUIAvailabilityViewController setTitleConstraints:]
- -[EKUIAvailabilityViewController titleConstraints]
- -[EKUIAvailabilityViewController viewWillTransitionToSize:withTransitionCoordinator:]
- -[EKUIEventStatusButtonsView _newSolariumButtonForAction:]
- GCC_except_table105
- GCC_except_table113
- GCC_except_table116
- GCC_except_table122
- GCC_except_table124
- GCC_except_table130
- GCC_except_table134
- GCC_except_table136
- GCC_except_table138
- GCC_except_table140
- GCC_except_table142
- GCC_except_table144
- GCC_except_table150
- GCC_except_table151
- GCC_except_table197
- GCC_except_table64
- GCC_except_table70
- _OBJC_CLASS_$_UIToolbarAppearance
- _OBJC_IVAR_$_EKCalendarChooserDefaultImpl._addCalendarButton
- _OBJC_IVAR_$_EKReminderTitleDetailCell._background
- _OBJC_IVAR_$_EKReminderTitleDetailCell._subtitle
- _OBJC_IVAR_$_EKShowInRemindersDetailCell._button
- _OBJC_IVAR_$_EKUIAvailabilityViewController._dateNavContainer
- _OBJC_IVAR_$_EKUIAvailabilityViewController._largeDateNavContainer
- _OBJC_IVAR_$_EKUIAvailabilityViewController._largeNavLeadingConstraint
- _OBJC_IVAR_$_EKUIAvailabilityViewController._participantDivider
- _OBJC_IVAR_$_EKUIAvailabilityViewController._titleConstraints
- ___35-[EKCalendarEditor _deleteCalendar]_block_invoke.58
- ___45-[EKUIAvailabilityViewController doneTapped:]_block_invoke.134
- ___50-[EKUIEventStatusButtonsView _newButtonForAction:]_block_invoke
- ___54-[EKShowInRemindersDetailCell initWithEvent:editable:]_block_invoke
- ___54-[EKShowInRemindersDetailCell initWithEvent:editable:]_block_invoke_2
- ___58-[EKUIEventStatusButtonsView _newSolariumButtonForAction:]_block_invoke
- ___71-[EKCalendarChooserDefaultImpl _updateOrCreateAddCalendarBarButtonItem]_block_invoke
- ___71-[EKCalendarChooserDefaultImpl _updateOrCreateAddCalendarBarButtonItem]_block_invoke_2
- ___71-[EKCalendarChooserDefaultImpl _updateOrCreateAddCalendarBarButtonItem]_block_invoke_3
- ___71-[EKCalendarChooserDefaultImpl _updateOrCreateAddCalendarBarButtonItem]_block_invoke_4
- ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104w_e77_"UICollectionViewCell"32?0"UICollectionView"8"NSIndexPath"16"NSString"24lw104l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___block_literal_global.105
- ___block_literal_global.166
- ___block_literal_global.176
- ___block_literal_global.276
- ___block_literal_global.290
- ___block_literal_global.420
- ___block_literal_global.75
- _objc_msgSend$_newSolariumButtonForAction:
- _objc_msgSend$bottomSpaceAdjustment
- _objc_msgSend$commonSetupCellWithTitle:showExtraSpaceAtBottom:extraBottomSpaceAdjustment:
- _objc_msgSend$configureWithDefaultBackground
- _objc_msgSend$configureWithTransparentBackground
- _objc_msgSend$dateNavContainer
- _objc_msgSend$effectiveTimeZone
- _objc_msgSend$initWithEvent:reminder:editable:showExtraSpaceAtBottom:extraBottomSpaceAdjustment:allowDataDetector:title:textFromEventAndReminderBlock:
- _objc_msgSend$largeDateNavContainer
- _objc_msgSend$largeNavLeadingConstraint
- _objc_msgSend$minDateLabelWidth
- _objc_msgSend$palette
- _objc_msgSend$participantDivider
- _objc_msgSend$performChangesWithState:
- _objc_msgSend$setAdjustsImageSizeForAccessibilityContentSizeCategory:
- _objc_msgSend$setBottomInset:
- _objc_msgSend$setCompactAppearance:
- _objc_msgSend$setCompactScrollEdgeAppearance:
- _objc_msgSend$setDateFormat:
- _objc_msgSend$setPalette:
- _objc_msgSend$setParticipantDivider:
- _objc_msgSend$setPreferredHeight:
- _objc_msgSend$setTopInset:
- _objc_msgSend$setTranslucent:
- _objc_msgSend$titleConstraints
- _objc_msgSend$uses24HourTime
CStrings:
+ "@\"CAGradientLayer\""
+ "@\"EKEventPreviewDetailItem\""
+ "@48@0:8@16@24d32d40"
+ "@64@0:8@16@24B32B36B40@44@?52B60"
+ "Are you sure you want to unsubscribe?"
+ "B24@0:8@\"EKReminderTitleDetailCell\"16"
+ "CollectionViewRowIdentifierAddCalendarButton"
+ "CollectionViewSectionIdentifierAddCalendarButton"
+ "Delegate Calendars"
+ "EKUIHorizontalGradientView"
+ "H:[avatar(==35)]"
+ "H:[avatar]-[subtitle]"
+ "H:[avatar]-[title]"
+ "Invitees (%lu)"
+ "List"
+ "List-reminder-detail"
+ "Notes-reminder-detail"
+ "T@\"CUIKOROccurrenceState\",&,V_currentImageState"
+ "T@\"CUIKOROccurrenceState\",&,V_currentState"
+ "T@\"UIBarButtonItem\",&,V_cancelButton"
+ "T@\"UIBarButtonItem\",&,V_largeDateNavItem"
+ "T@\"UIBarButtonItem\",&,V_nextButton"
+ "T@\"UIBarButtonItem\",&,V_previousButton"
+ "Td,N,V_additionalGridCurtainHeight"
+ "Td,N,V_leadingMargin"
+ "Td,N,V_occurrenceLayoutLeadingInset"
+ "Td,N,V_occurrenceLayoutTrailingInset"
+ "This event is read-only"
+ "Unsubscribing will delete all events from this subscription."
+ "V:[avatar(==35)]"
+ "V:[participantListDivider]|"
+ "V:[title]-(>=0)-[subtitle]"
+ "_addCalendarBarButton"
+ "_addCalendarButtonSection"
+ "_additionalGridCurtainHeight"
+ "_bottomView"
+ "_configureAddCalendarButtonCell:indexPath:item:"
+ "_configureButton:forAction:"
+ "_configureStatusButtonsToolbar"
+ "_customInsets"
+ "_dateFont"
+ "_dateLabelLine1"
+ "_dateLabelLine2"
+ "_dateLabelLine3"
+ "_dateLabelLine4"
+ "_endColor"
+ "_endPoint"
+ "_gradientLayer"
+ "_isAddCalendarButtonSection:"
+ "_largeDateNavItem"
+ "_leadingMargin"
+ "_menuForAddCalendarButton:"
+ "_noBackgroundStyle"
+ "_occurrenceLayoutLeadingInset"
+ "_occurrenceLayoutTrailingInset"
+ "_presentedInAPopOver"
+ "_previewItem"
+ "_shouldShowAddCalendarButtonSection"
+ "_startColor"
+ "_startPoint"
+ "_updateTextViewColorAndFont"
+ "additionalGridCurtainHeight"
+ "cancelButton"
+ "commonSetupCellWithTitle:showExtraSpaceAtBottom:"
+ "defaultFontForTextStyle:"
+ "eventViewControllerPresentedInAPopover:"
+ "hasCellBelow"
+ "initWithEvent:reminder:editable:showExtraSpaceAtBottom:allowDataDetector:title:textFromEventAndReminderBlock:noBackgroundStyle:"
+ "initWithStartColor:endColor:start:end:"
+ "initWithState:"
+ "insertSublayer:atIndex:"
+ "largeDateNavItem"
+ "occurrenceLayoutLeadingInset"
+ "occurrenceLayoutTrailingInset"
+ "person.2.fill"
+ "secondarySystemFillColor"
+ "setAdditionalGridCurtainHeight:"
+ "setCancelButton:"
+ "setColors:"
+ "setCurrentImageState:"
+ "setCurrentState:"
+ "setEndPoint:"
+ "setHidesSharedBackground:"
+ "setLargeDateNavItem:"
+ "setLeadingItemGroups:"
+ "setLeadingMargin:"
+ "setOccurrenceLayoutLeadingInset:"
+ "setOccurrenceLayoutTrailingInset:"
+ "setSharesBackground:"
+ "setStartPoint:"
+ "setTitleFont:"
+ "setTitleTextColor:"
+ "titleShouldInsetForEditButton:"
+ "useDynamicPocket"
+ "\xf0\xf0\xf0\""
+ "\xf0\xf1b"
- ", %@ %@"
- "@68@0:8@16@24B32B36d40B48@52@?60"
- "Are you sure you want to unsubscribe? Unsubscribing will delete all events from this subscription."
- "H:[avatar(==30)]"
- "H:[avatar]-[subtitle]-|"
- "H:[avatar]-[title]-|"
- "H:[prev][next][date]|"
- "H:|-(>=0)-[prev]-[date]-[next]-(>=0)-|"
- "HH:mm zzz"
- "INVITEES"
- "LIST"
- "LIST-reminder-detail"
- "NOTES"
- "NOTES-reminder-detail"
- "T@\"CUIKOROccurrenceState\",R,N,V_currentImageState"
- "T@\"CUIKOROccurrenceState\",R,N,V_currentState"
- "T@\"NSLayoutConstraint\",&,V_largeNavLeadingConstraint"
- "T@\"NSMutableArray\",&,V_titleConstraints"
- "T@\"UIButton\",&,V_nextButton"
- "T@\"UIButton\",&,V_previousButton"
- "T@\"UIView\",&,V_dateNavContainer"
- "T@\"UIView\",&,V_largeDateNavContainer"
- "T@\"UIView\",&,V_participantDivider"
- "This event was imported (read-only)"
- "V:[avatar(==30)]"
- "V:|-(3)-[title][subtitle]-(3)-|"
- "V:|-[participantListDivider]|"
- "_dateNavContainer"
- "_largeDateNavContainer"
- "_largeNavLeadingConstraint"
- "_newSolariumButtonForAction:"
- "_participantDivider"
- "_subtitle"
- "_titleConstraints"
- "bottomSpaceAdjustment"
- "commonSetupCellWithTitle:showExtraSpaceAtBottom:extraBottomSpaceAdjustment:"
- "configureWithDefaultBackground"
- "configureWithTransparentBackground"
- "dateNavContainer"
- "effectiveTimeZone"
- "hh:mm a zzz"
- "initWithEvent:reminder:editable:showExtraSpaceAtBottom:extraBottomSpaceAdjustment:allowDataDetector:title:textFromEventAndReminderBlock:"
- "largeDateNavContainer"
- "largeNavLeadingConstraint"
- "participantDivider"
- "performChangesWithState:"
- "prev"
- "setAdjustsImageSizeForAccessibilityContentSizeCategory:"
- "setBottomInset:"
- "setCompactAppearance:"
- "setCompactScrollEdgeAppearance:"
- "setDateFormat:"
- "setDateNavContainer:"
- "setLargeDateNavContainer:"
- "setLargeNavLeadingConstraint:"
- "setParticipantDivider:"
- "setPreferredHeight:"
- "setTitleConstraints:"
- "setTranslucent:"
- "titleConstraints"
- "uses24HourTime"
- "v36@0:8@16B24d28"

```
