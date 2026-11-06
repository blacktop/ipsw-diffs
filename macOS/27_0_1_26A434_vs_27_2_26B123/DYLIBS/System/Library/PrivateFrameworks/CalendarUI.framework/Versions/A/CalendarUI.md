## CalendarUI

> `/System/Library/PrivateFrameworks/CalendarUI.framework/Versions/A/CalendarUI`

```diff

-1281.0.0.0.0
-  __TEXT.__text: 0x122b20
-  __TEXT.__objc_methlist: 0x144cc
-  __TEXT.__const: 0x1914
-  __TEXT.__cstring: 0x811f
-  __TEXT.__gcc_except_tab: 0x11d0
-  __TEXT.__oslogstring: 0x1dfd
+1281.2.5.100.0
+  __TEXT.__text: 0x125dbc
+  __TEXT.__objc_methlist: 0x145f4
+  __TEXT.__const: 0x1ae4
+  __TEXT.__cstring: 0x80ef
+  __TEXT.__gcc_except_tab: 0x11e8
+  __TEXT.__oslogstring: 0x1dcd
   __TEXT.__ustring: 0x492
-  __TEXT.__swift5_typeref: 0x13a6
-  __TEXT.__swift5_capture: 0x67c
-  __TEXT.__swift5_fieldmd: 0x6c4
-  __TEXT.__constg_swiftt: 0xb2c
-  __TEXT.__swift5_reflstr: 0x85f
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_assocty: 0x100
-  __TEXT.__swift5_proto: 0x50
-  __TEXT.__swift5_types: 0x5c
+  __TEXT.__swift5_typeref: 0x142a
+  __TEXT.__swift5_capture: 0x674
+  __TEXT.__swift5_fieldmd: 0x704
+  __TEXT.__constg_swiftt: 0xb58
+  __TEXT.__swift5_reflstr: 0x8bf
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_assocty: 0x130
+  __TEXT.__swift5_proto: 0x68
+  __TEXT.__swift5_types: 0x60
   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x20
   __TEXT.__swift_as_cont: 0x48
-  __TEXT.__unwind_info: 0x44d0
-  __TEXT.__eh_frame: 0x8cc
+  __TEXT.__unwind_info: 0x4540
+  __TEXT.__eh_frame: 0x864
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb800
+  __DATA_CONST.__objc_selrefs: 0xb8e8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x658
   __DATA_CONST.__objc_arraydata: 0x388
-  __DATA_CONST.__got: 0x18b8
-  __AUTH_CONST.__const: 0x35b0
-  __AUTH_CONST.__cfstring: 0x9d60
-  __AUTH_CONST.__objc_const: 0x1d998
+  __DATA_CONST.__got: 0x1978
+  __AUTH_CONST.__const: 0x34f0
+  __AUTH_CONST.__cfstring: 0x9c80
+  __AUTH_CONST.__objc_const: 0x1daf0
   __AUTH_CONST.__objc_intobj: 0x6a8
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_doubleobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0x1230
-  __AUTH_CONST.__auth_ptr: 0x510
-  __AUTH.__objc_data: 0x34a0
-  __AUTH.__data: 0x570
-  __DATA.__objc_ivar: 0x1418
-  __DATA.__data: 0x2438
-  __DATA.__bss: 0xdd8
+  __AUTH_CONST.__auth_got: 0x12a0
+  __AUTH_CONST.__auth_ptr: 0x518
+  __AUTH.__objc_data: 0x34b8
+  __AUTH.__data: 0x568
+  __DATA.__objc_ivar: 0x142c
+  __DATA.__data: 0x24e0
+  __DATA.__bss: 0x10d8
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x2bc0
   __DATA_DIRTY.__bss: 0x3f0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7197
-  Symbols:   16208
-  CStrings:  1591
+  Functions: 7231
+  Symbols:   16301
+  CStrings:  1581
 
Symbols:
+ -[EKUIAttendeesGadget updateCanShowAvailabilityButton]
+ -[EKUICalendarPopUpButton hitTest:]
+ -[EKUICustomAlarmView popover]
+ -[EKUICustomAlarmView setPopover:]
+ -[EKUICustomAlarmViewController popoverWillShow:]
+ -[EKUIGadgetContainer setHorizontalInset:]
+ -[EKUIMagicComposeGadget bottomPadding]
+ -[EKUISendRevertGadget _affirmativeButtonTitle]
+ -[EKUISendRevertGadget _deleteButtonTitle]
+ -[EKUISendRevertGadget _revertButtonTitle]
+ -[EKUISendRevertGadget _showButtonTitle]
+ -[EKUISendRevertGadget secondButtonIsLeading]
+ -[EKUISingleViewGadget bottomPadding]
+ -[EKUISummaryButton intrinsicContentSize]
+ -[EKUISummaryButton setAttributedTitle:]
+ -[EKUISummaryButton setFrameSize:]
+ -[EKUIThreeButtonGadget secondButtonIsLeading]
+ -[EKUITitleGadget _cancelInFlightTitleMorph]
+ -[EKUITitleGadget _completeTitleMorphWithSnapshotLayer:]
+ -[EKUITitleGadget _fadeTitleLeadingLabelForMinimize:duration:]
+ -[EKUITitleGadget _updateTitleFieldMinHeight]
+ -[EKUITitleGadget minimizeTitleField:animated:]
+ -[EKUITitleGadget setTitleFieldCenterYConstraint:]
+ -[EKUITitleGadget setTitleFieldMinHeightConstraint:]
+ -[EKUITitleGadget setTitleMorphSnapshotLayer:]
+ -[EKUITitleGadget textFieldWasMinimizedBeforeBecomingFirstResponder]
+ -[EKUITitleGadget titleFieldCenterYConstraint]
+ -[EKUITitleGadget titleFieldMinHeightConstraint]
+ -[EKUITitleGadget titleMorphSnapshotLayer]
+ GCC_except_table131
+ GCC_except_table140
+ GCC_except_table26
+ GCC_except_table31
+ GCC_except_table33
+ GCC_except_table39
+ GCC_except_table51
+ GCC_except_table55
+ GCC_except_table68
+ GCC_except_table82
+ GCC_except_table85
+ GCC_except_table87
+ GCC_except_table90
+ GCC_except_table96
+ OBJC_IVAR_$_EKUIColorBarGadgetContainer._mitosisSplitGeneration
+ OBJC_IVAR_$_EKUICustomAlarmView._popover
+ OBJC_IVAR_$_EKUIGadgetContainer._horizontalInset
+ OBJC_IVAR_$_EKUITitleGadget._titleFieldCenterYConstraint
+ OBJC_IVAR_$_EKUITitleGadget._titleFieldMinHeightConstraint
+ OBJC_IVAR_$_EKUITitleGadget._titleMorphSnapshotLayer
+ _CACurrentMediaTime
+ _CFRunLoopGetMain
+ _CFRunLoopPerformBlock
+ _CFRunLoopWakeUp
+ _CGColorSpaceCreateDeviceRGB
+ _CGContextScaleCTM
+ _CUIKAXEventEditorTitleField
+ _CUIKAXMacEventEditorAlarmPopUp
+ _CUIKAXMacEventEditorAttachmentButton
+ _CUIKAXMacEventEditorCalendarPopUp
+ _CUIKAXMacEventEditorDateTimeButton
+ _CUIKAXMacEventEditorLocationField
+ _CUIKAXMacEventEditorRecurrencePopUp
+ _CUIKAXMacEventEditorTravelTimePopUp
+ _CUIKAXMacEventEditorVirtualConferenceButton
+ _CUIKAXSidebarMiniCalMonthTitle
+ _CUIKAXSidebarMiniCalNextMonthButton
+ _CUIKAXSidebarMiniCalPrevMonthButton
+ _CalAnimatePivotScaleAndSlide
+ _CalPerformAfterEventTracking
+ _CalSnapshotViewAndHide
+ _OBJC_CLASS_$_NSLayoutManager
+ __47-[EKUITitleGadget minimizeTitleField:animated:]_block_invoke
+ __47-[EKUITitleGadget minimizeTitleField:animated:]_block_invoke_2
+ __52-[EKUIColorBarGadgetContainer _animateMitosisSplit:]_block_invoke_2
+ ___40-[EKUICalendarPopUpButton menuDidClose:]_block_invoke
+ ___47-[EKUITitleGadget minimizeTitleField:animated:]_block_invoke
+ ___47-[EKUITitleGadget minimizeTitleField:animated:]_block_invoke_2
+ ___59-[EKUIColorBarGadgetContainer _revealSummaryButtonForError]_block_invoke_3
+ ___69-[EKUIColorBarGadgetContainer _animateRevealFieldHidingSummaryButton]_block_invoke_2
+ ___CGBitmapContextCreate
+ ___CalAnimatePivotScaleAndSlide_block_invoke
+ ___block_descriptor_40_e8_32bs_e5_v8?0l
+ ___block_descriptor_65_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_81_e8_32s40s_e5_v8?0l
+ _associated conformance So21NSAttributedStringKeyaSHSCSQ
+ _associated conformance So21NSAttributedStringKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So21NSAttributedStringKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _kCAFillModeBoth
+ _kCFRunLoopDefaultMode
+ _objc_msgSend$_affirmativeButtonTitle
+ _objc_msgSend$_cancelInFlightTitleMorph
+ _objc_msgSend$_completeTitleMorphWithSnapshotLayer:
+ _objc_msgSend$_deleteButtonTitle
+ _objc_msgSend$_fadeTitleLeadingLabelForMinimize:duration:
+ _objc_msgSend$_revertButtonTitle
+ _objc_msgSend$_showButtonTitle
+ _objc_msgSend$_updateTitleFieldMinHeight
+ _objc_msgSend$autoArchived
+ _objc_msgSend$behavior
+ _objc_msgSend$bottomPadding
+ _objc_msgSend$constraintGreaterThanOrEqualToAnchor:constant:
+ _objc_msgSend$defaultLineHeightForFont:
+ _objc_msgSend$descender
+ _objc_msgSend$drawingRectForBounds:
+ _objc_msgSend$localURLExpandingArchiveIfNeeded
+ _objc_msgSend$minimizeTitleField:animated:
+ _objc_msgSend$participationStatus
+ _objc_msgSend$renderInContext:
+ _objc_msgSend$secondButtonIsLeading
+ _objc_msgSend$setBeginTime:
+ _objc_msgSend$setContentsScale:
+ _objc_msgSend$setHorizontalInset:
+ _objc_msgSend$setTitleFieldCenterYConstraint:
+ _objc_msgSend$setTitleFieldMinHeightConstraint:
+ _objc_msgSend$setTitleMorphSnapshotLayer:
+ _objc_msgSend$setTypingAttributes:
+ _objc_msgSend$sizeWithAttributes:
+ _objc_msgSend$titleFieldCenterYConstraint
+ _objc_msgSend$titleFieldMinHeightConstraint
+ _objc_msgSend$titleMorphSnapshotLayer
+ _objc_msgSend$updateCanShowAvailabilityButton
+ _swift_initStackObject
+ _symbolic So7CALayerC
+ _symbolic So7CALayerCSg
+ _symbolic _____ So21NSAttributedStringKeya
+ _symbolic _____XDXMT 10CalendarUI29CalUIMagicComposePromptEditorC
+ _symbolic ______ypt So21NSAttributedStringKeya
+ _symbolic _____y___________Qo_ 7SwiftUI4ViewPAAE11buttonStyleyQrqd__AA015PrimitiveButtonE0Rd__lFQO 13CalendarUIKit014ReportAConcernG0V AA05PlaingE0V
+ _symbolic _____y______yptG s23_ContiguousArrayStorageC So21NSAttributedStringKeya
+ _symbolic _____y_____y___________Qo_G 7SwiftUI13NSHostingViewC AA0D0PAAE11buttonStyleyQrqd__AA015PrimitiveButtonF0Rd__lFQO 13CalendarUIKit014ReportAConcernH0V AA05PlainhF0V
+ _symbolic _____y_____ypG s18_DictionaryStorageC So21NSAttributedStringKeya
+ _type_layout_string So21NSAttributedStringKeya
- -[EKUIAttachmentGadget _prepareAttachmentsForQuickLook:]
- -[EKUIAttachmentGadget dealloc]
- -[EKUIAttachmentGadget prepareAllAttachmentsForQuickLook]
- -[EKUIAttachmentGadget viewControllerViewDidDisappear]
- -[EKUIAttachmentGadget viewControllerViewWillAppear]
- -[EKUICalendarPopUpButton mouseDown:]
- -[EKUITitleGadget minimizeTitleField:]
- -[EKUITitleGadget verticalPadding]
- GCC_except_table132
- GCC_except_table141
- GCC_except_table23
- GCC_except_table28
- GCC_except_table30
- GCC_except_table47
- GCC_except_table52
- GCC_except_table54
- GCC_except_table69
- GCC_except_table83
- GCC_except_table86
- GCC_except_table92
- GCC_except_table97
- OBJC_IVAR_$_EKUIAttachmentGadget._attachmentPreviewURLs
- _CalAnimateDissolveScale
- __38-[EKUITitleGadget minimizeTitleField:]_block_invoke
- __38-[EKUITitleGadget minimizeTitleField:]_block_invoke_2
- __38-[EKUITitleGadget minimizeTitleField:]_block_invoke_3
- ___38-[EKUITitleGadget minimizeTitleField:]_block_invoke
- ___38-[EKUITitleGadget minimizeTitleField:]_block_invoke_2
- ___38-[EKUITitleGadget minimizeTitleField:]_block_invoke_3
- ___block_descriptor_48_e8_32s_e28_v16?0"NSAnimationContext"8l
- ___block_descriptor_57_e8_32s40s48s_e5_v8?0l
- _objc_msgSend$_prepareAttachmentsForQuickLook:
- _objc_msgSend$minimizeTitleField:
- _objc_msgSend$minusSet:
- _objc_msgSend$prepareAllAttachmentsForQuickLook
- _swift_task_getMainExecutor
- _swift_task_isCurrentExecutor
- _symbolic _____y_____G 7SwiftUI13NSHostingViewC 13CalendarUIKit20ReportAConcernButtonV
- _symbolic yt______pIgrzo_ s5ErrorP
CStrings:
+ "Ag"
+ "CR"
+ "H:|[firstButton(>=defaultButtonWidth)]-(spacing)-[secondButton(>=defaultButtonWidth)]"
+ "H:|[firstButton(>=defaultButtonWidth)]-(spacing)-[secondButton(>=defaultButtonWidth)]-(>=spacing)-[thirdButton(>=defaultButtonWidth)]|"
+ "V:|-(verticalPadding)-[controlView]-(bottomPadding)-|"
+ "V:|[controlView]-(bottomPadding)-|"
+ "bottomPadding"
+ "morphScale"
+ "titleLabelFade"
+ "\xa1!"
- "CB"
- "Failed to access attachment URL %@"
- "Incorrect actor executor assumption; Expected same executor as "
- "MiniCalMonthTitle"
- "MiniCalNextMonthButton"
- "MiniCalPrevMonthButton"
- "V:|-(verticalPadding)-[controlView]-(verticalPadding)-|"
- "V:|[controlView]-(verticalPadding)-|"
- "attachment-button"
- "calendar-button"
- "date-time-button"
- "dissolveScale"
- "location-field"
- "recurrence-button"
- "title-field"
- "transform.scale"
- "traveltime-button"
- "virtualconference-button"
- "\xa1"
- "\xc1"
```
