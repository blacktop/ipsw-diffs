## EventKitUI

> `/System/Library/Frameworks/EventKitUI.framework/EventKitUI`

```diff

-1519.1.0.0.0
-  __TEXT.__text: 0x1d53ac
-  __TEXT.__auth_stubs: 0x21d0
-  __TEXT.__objc_methlist: 0x1ec2c
+1521.1.0.0.0
+  __TEXT.__text: 0x1d6dcc
+  __TEXT.__auth_stubs: 0x2240
+  __TEXT.__objc_methlist: 0x1ed8c
   __TEXT.__const: 0x2584
-  __TEXT.__cstring: 0xdb71
-  __TEXT.__gcc_except_tab: 0x41d0
+  __TEXT.__cstring: 0xdc01
+  __TEXT.__gcc_except_tab: 0x428c
   __TEXT.__oslogstring: 0x785d
   __TEXT.__ustring: 0x8ca
   __TEXT.__dlopen_cstrs: 0x322

   __TEXT.__swift5_types: 0xf8
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x7570
+  __TEXT.__unwind_info: 0x7608
   __TEXT.__eh_frame: 0x5d0
-  __TEXT.__objc_classname: 0x4229
-  __TEXT.__objc_methname: 0x44b0c
-  __TEXT.__objc_methtype: 0xc152
-  __TEXT.__objc_stubs: 0x31840
-  __DATA_CONST.__got: 0x1920
-  __DATA_CONST.__const: 0x4600
-  __DATA_CONST.__objc_classlist: 0xc50
+  __TEXT.__objc_classname: 0x4265
+  __TEXT.__objc_methname: 0x44f68
+  __TEXT.__objc_methtype: 0xc1bd
+  __TEXT.__objc_stubs: 0x31b60
+  __DATA_CONST.__got: 0x1940
+  __DATA_CONST.__const: 0x4658
+  __DATA_CONST.__objc_classlist: 0xc60
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x620
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf438
+  __DATA_CONST.__objc_selrefs: 0xf528
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x8a0
+  __DATA_CONST.__objc_superrefs: 0x8b8
   __DATA_CONST.__objc_arraydata: 0x1c8
-  __AUTH_CONST.__auth_got: 0x10f8
-  __AUTH_CONST.__const: 0x27f0
-  __AUTH_CONST.__cfstring: 0xb380
-  __AUTH_CONST.__objc_const: 0x30070
-  __AUTH_CONST.__objc_intobj: 0x588
+  __AUTH_CONST.__auth_got: 0x1130
+  __AUTH_CONST.__const: 0x2770
+  __AUTH_CONST.__cfstring: 0xb3c0
+  __AUTH_CONST.__objc_const: 0x302d0
   __AUTH_CONST.__objc_arrayobj: 0x1c8
+  __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x7b48
+  __AUTH.__objc_data: 0x7be8
   __AUTH.__data: 0xbd0
-  __DATA.__objc_ivar: 0x24c4
+  __DATA.__objc_ivar: 0x24dc
   __DATA.__data: 0x4b60
-  __DATA.__bss: 0x1600
+  __DATA.__bss: 0x15f0
   __DATA.__common: 0x218
   __DATA_DIRTY.__objc_data: 0x13b0
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AD4812EE-F6ED-38C5-99DD-9F08AD9D4172
-  Functions: 11688
-  Symbols:   34641
-  CStrings:  16320
+  UUID: 584DC519-8F14-3ED5-BA49-168903AE4A6B
+  Functions: 11715
+  Symbols:   34740
+  CStrings:  16369
 
Symbols:
+ +[EKDayTimeView _noonAttributedStringForString:orientation:]
+ +[EKDayTimeView noonAttributedStringComponentsForOrientation:]
+ +[EKDayTimeView noonAttributedStringForOrientation:]
+ +[EKDayTimeView noonString]
+ +[EKReminderListDetailItem bottomSpaceAdjustment]
+ +[EKReminderTextDetailItem bottomSpaceAdjustment]
+ -[EKCurrentTimeMarkerView layoutSubviews]
+ -[EKDayOccurrenceView backgroundChangedCallback]
+ -[EKDayOccurrenceView backgroundViewForEventIndicator]
+ -[EKDayOccurrenceView setBackgroundChangedCallback:]
+ -[EKDayViewContent _layoutDayIfNeeded:]
+ -[EKDayViewContent _layoutNeededForDay:]
+ -[EKDayViewContent invalidateOccurrenceLayout]
+ -[EKDayViewContent layoutParameters]
+ -[EKDayViewContent setNeedsDisplay]
+ -[EKDayViewContent updateCurrentLayoutParameters]
+ -[EKDayViewContentItem backgroundChangedCallback]
+ -[EKDayViewContentItem setBackgroundChangedCallback:]
+ -[EKDayViewContentItem updateViewBackgroundChangedCallback]
+ -[EKDayViewContentLayoutParameters boundsSize]
+ -[EKDayViewContentLayoutParameters initWithBoundsSize:]
+ -[EKDayViewContentLayoutParameters isEqual:]
+ -[EKDayViewContentStackView .cxx_destruct]
+ -[EKDayViewContentStackView init]
+ -[EKDayViewContentStackView updateWithRows:]
+ -[EKEventDetailTitleCell _dateTimeViewForLine:color:]
+ -[EKEventDetailTitleCell _setDateTimeString:line:color:]
+ -[EKReminderDetailTextCell commonSetupCellWithTitle:showExtraSpaceAtBottom:extraBottomSpaceAdjustment:]
+ -[EKReminderDetailTextCell initWithEvent:reminder:editable:showExtraSpaceAtBottom:extraBottomSpaceAdjustment:allowDataDetector:title:textFromEventAndReminderBlock:]
+ -[EKReminderListDetailItem defaultCellHeightForSubitemAtIndex:forWidth:forceUpdate:]
+ -[EKReminderListDetailItem showExtraSpaceAtBottom]
+ -[EKSubscribedCalendarEditor _updateTableHeaderLayoutForWidth:]
+ -[EKUIAvailabilityNavigationController wantsDismissOnSizeClassChangeWithNewTraitCollection:]
+ -[EKUIListViewAllDayEventCell wantsPillShape]
+ -[EKUIListViewCell .cxx_destruct]
+ -[EKUIListViewCell _commonInit]
+ -[EKUIListViewCell _updateVisualEffectBackground]
+ -[EKUIListViewCell _usesVisualEffectBackground]
+ -[EKUIListViewCell carplayBackgroundViewInsets]
+ -[EKUIListViewCell carplayUsesColorfulBackgrounds]
+ -[EKUIListViewCell cellContentView]
+ -[EKUIListViewCell effectView]
+ -[EKUIListViewCell layoutSubviews]
+ -[EKUIListViewCell setEffectView:]
+ -[EKUIListViewCell wantsPillShape]
+ -[EKUIListViewReminderCell wantsPillShape]
+ -[EKUIListViewTimedEventCell _initializeTravelLine]
+ GCC_except_table105
+ GCC_except_table116
+ GCC_except_table122
+ GCC_except_table124
+ GCC_except_table130
+ GCC_except_table134
+ GCC_except_table138
+ GCC_except_table140
+ GCC_except_table142
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table197
+ GCC_except_table71
+ GCC_except_table72
+ GCC_except_table87
+ _CFDictionaryCreateMutable
+ _CFDictionaryRemoveValue
+ _CFDictionarySetValue
+ _CFSetCreateMutable
+ _CGFloatNearlyEqualToFloat
+ _CGSizeNearlyEqualToSize
+ _CUIKAbbreviatedEnDashDayStringForDate
+ _CUIKDurationStringForDatesWithDash
+ _CUIKEnDashDayStringForDate
+ _CalCanvasPocketEventIndicatorEnabled
+ _OBJC_CLASS_$_EKDayViewContentLayoutParameters
+ _OBJC_CLASS_$_EKDayViewContentStackView
+ _OBJC_IVAR_$_EKDayOccurrenceView._backgroundChangedCallback
+ _OBJC_IVAR_$_EKDayViewContent._lastLayoutParametersForDay
+ _OBJC_IVAR_$_EKDayViewContent._lastLayoutParametersForDayForPreload
+ _OBJC_IVAR_$_EKDayViewContent._layoutParameters
+ _OBJC_IVAR_$_EKDayViewContent._layoutParametersLock
+ _OBJC_IVAR_$_EKDayViewContent._pinningValid
+ _OBJC_IVAR_$_EKDayViewContent._topStackViews
+ _OBJC_IVAR_$_EKDayViewContentItem._backgroundChangedCallback
+ _OBJC_IVAR_$_EKDayViewContentLayoutParameters._boundsSize
+ _OBJC_IVAR_$_EKDayViewContentStackView._currentItems
+ _OBJC_IVAR_$_EKUIListViewCell._effectView
+ _OBJC_METACLASS_$_EKDayViewContentLayoutParameters
+ _OBJC_METACLASS_$_EKDayViewContentStackView
+ __OBJC_$_INSTANCE_METHODS_EKDayViewContentLayoutParameters
+ __OBJC_$_INSTANCE_METHODS_EKDayViewContentStackView
+ __OBJC_$_INSTANCE_VARIABLES_EKDayViewContentLayoutParameters
+ __OBJC_$_INSTANCE_VARIABLES_EKDayViewContentStackView
+ __OBJC_$_PROP_LIST_EKDayViewContentLayoutParameters
+ __OBJC_CLASS_RO_$_EKDayViewContentLayoutParameters
+ __OBJC_CLASS_RO_$_EKDayViewContentStackView
+ __OBJC_METACLASS_RO_$_EKDayViewContentLayoutParameters
+ __OBJC_METACLASS_RO_$_EKDayViewContentStackView
+ ___32-[EKEventDetailTitleCell update]_block_invoke.234
+ ___44-[EKDayViewContentStackView updateWithRows:]_block_invoke
+ ___44-[EKDayViewContentStackView updateWithRows:]_block_invoke_2
+ ___44-[EKDayViewContentStackView updateWithRows:]_block_invoke_3
+ ___44-[EKDayViewContentStackView updateWithRows:]_block_invoke_4
+ ___59-[EKDayViewContentItem updateViewBackgroundChangedCallback]_block_invoke
+ ___62+[EKDayTimeView noonAttributedStringComponentsForOrientation:]_block_invoke
+ ___block_descriptor_40_e8_32w_e29_v16?0"EKDayOccurrenceView"8lw32l8
+ ___block_descriptor_40_e8_32w_e30_v16?0"EKDayViewContentItem"8lw32l8
+ ___block_descriptor_56_e8_32s_e20_v16?0^{CGContext=}8ls32l8
+ ___block_descriptor_56_e8_32s_e25_v32?0"NSString"8Q16^B24ls32l8
+ ___block_literal_global.276
+ ___block_literal_global.290
+ __fontLock
+ _equalCallbackForPointerEquality
+ _hashCallbackForPointerHash
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _kCFTypeSetCallBacks
+ _objc_msgSend$CUIKSmallCapAMPMTimezoneClarificationStringForStartDate:endDate:startTimeZone:endTimeZone:color:
+ _objc_msgSend$_carSystemPrimaryColor
+ _objc_msgSend$_carSystemSecondaryColor
+ _objc_msgSend$_dateTimeViewForLine:color:
+ _objc_msgSend$_initializeTravelLine
+ _objc_msgSend$_layoutDayIfNeeded:
+ _objc_msgSend$_layoutNeededForDay:
+ _objc_msgSend$_noonAttributedStringForString:orientation:
+ _objc_msgSend$_setDateTimeString:line:color:
+ _objc_msgSend$_updateTableHeaderLayoutForWidth:
+ _objc_msgSend$_updateVisualEffectBackground
+ _objc_msgSend$_usesVisualEffectBackground
+ _objc_msgSend$backgroundViewForEventIndicator
+ _objc_msgSend$bottomSpaceAdjustment
+ _objc_msgSend$boundsSize
+ _objc_msgSend$calculateBackgroundImageFrame:travelTimeFrame:forState:withMargins:
+ _objc_msgSend$carplayBackgroundViewInsets
+ _objc_msgSend$cellContentView
+ _objc_msgSend$commonSetupCellWithTitle:showExtraSpaceAtBottom:extraBottomSpaceAdjustment:
+ _objc_msgSend$effectView
+ _objc_msgSend$initWithBoundsSize:
+ _objc_msgSend$initWithEvent:reminder:editable:showExtraSpaceAtBottom:extraBottomSpaceAdjustment:allowDataDetector:title:textFromEventAndReminderBlock:
+ _objc_msgSend$insertArrangedSubview:atIndex:
+ _objc_msgSend$invalidateOccurrenceLayout
+ _objc_msgSend$layoutParameters
+ _objc_msgSend$noonAttributedStringComponentsForOrientation:
+ _objc_msgSend$noonAttributedStringForOrientation:
+ _objc_msgSend$noonString
+ _objc_msgSend$registerForTraitChanges:withAction:
+ _objc_msgSend$reminderBackgroundColor:style:miniPreview:completed:darkenForAllDayArea:
+ _objc_msgSend$setBackground:
+ _objc_msgSend$setBackgroundChangedCallback:
+ _objc_msgSend$setBackgroundEffects:
+ _objc_msgSend$standardBackgroundMargins:
+ _objc_msgSend$updateCurrentLayoutParameters
+ _objc_msgSend$updateViewBackgroundChangedCallback
+ _objc_msgSend$updateWithRows:
+ _objc_msgSend$wantsPillShape
+ _pointerEqualitySetWithObjects
+ _s_locationFont
+ _s_scaledLocationFont
+ _s_scaledTitleFont
+ _s_titleFont
- +[EKEventDetailTitleCell _locationFont].cold.1
- +[EKEventDetailTitleCell _scaledLocationFont].cold.1
- +[EKEventDetailTitleCell _scaledTitleFont].cold.1
- +[EKEventDetailTitleCell _titleFont].cold.1
- -[EKDayOccurrenceView _updateColorBarFrame]
- -[EKDayViewContent _layoutDayIfNeeded:isLoadingAsync:]
- -[EKDayViewContent _layoutNeededForDay:isLoadingAsync:]
- -[EKDayViewContent setNeedsLayout]
- -[EKEventDetailTitleCell _dateTimeViewForLine:]
- -[EKEventDetailTitleCell _setDateTimeString:line:]
- -[EKEventProposeNewTimeViewController _viewControllerForPresentingViewControllers]
- -[EKReminderDetailTextCell commonSetupCellWithTitle:showExtraSpaceAtBottom:]
- -[EKReminderDetailTextCell initWithEvent:reminder:editable:showExtraSpaceAtBottom:allowDataDetector:title:textFromEventAndReminderBlock:]
- -[EKSubscribedCalendarEditor _updateTableHeaderLayout]
- -[EKUIListViewAllDayEventCell carplayBackgroundViewVerticalInset]
- -[EKUIListViewAllDayEventCell initForCarplayWithReuseIdentifier:]
- -[EKUIListViewAllDayEventCell initForDragPreview]
- -[EKUIListViewAllDayEventCell initWithStyle:reuseIdentifier:]
- -[EKUIListViewReminderCell initForCarplayWithReuseIdentifier:]
- -[EKUIListViewReminderCell initForDragPreview]
- -[EKUIListViewReminderCell initWithStyle:reuseIdentifier:]
- -[EKUIListViewTimedEventCell carplayBackgroundViewVerticalInset]
- -[EKUIListViewTimedEventCell initForCarplayWithReuseIdentifier:]
- -[EKUIListViewTimedEventCell initForDragPreview]
- -[EKUIListViewTimedEventCell initWithStyle:reuseIdentifier:]
- GCC_except_table101
- GCC_except_table111
- GCC_except_table115
- GCC_except_table117
- GCC_except_table123
- GCC_except_table127
- GCC_except_table129
- GCC_except_table131
- GCC_except_table133
- GCC_except_table135
- GCC_except_table137
- GCC_except_table139
- GCC_except_table59
- GCC_except_table68
- GCC_except_table81
- GCC_except_table82
- GCC_except_table83
- _CUIKAbbreviatedEmDashDayStringForDate
- _CUIKDurationStringForDates
- _CUIKLongEmDashDayStringForDate
- _OBJC_IVAR_$_EKDayOccurrenceView._eventBackgroundColorBar
- _OBJC_IVAR_$_EKDayViewContent._lastLayoutWidthForDay
- _OBJC_IVAR_$_EKDayViewContent._lastLayoutWidthForDayForPreload
- _OBJC_IVAR_$_EKDayViewContent._layoutBounds
- _OBJC_IVAR_$_EKDayViewContent._layoutBoundsLock
- _UIFontTextStyleTitle3
- ___32-[EKEventDetailTitleCell update]_block_invoke.242
- ___36+[EKEventDetailTitleCell _titleFont]_block_invoke
- ___39+[EKEventDetailTitleCell _locationFont]_block_invoke
- ___42+[EKEventDetailTitleCell _scaledTitleFont]_block_invoke
- ___45+[EKEventDetailTitleCell _scaledLocationFont]_block_invoke
- ___block_descriptor_40_e8_32s_e20_v16?0^{CGContext=}8ls32l8
- ___block_literal_global.226
- ___block_literal_global.228
- ___block_literal_global.230
- ___block_literal_global.254
- ___block_literal_global.266
- ___block_literal_global.279
- __fontUpdateTokenBody
- __fontUpdateTokenFootnote
- __locationFont.font
- __scaledLocationFont.font
- __scaledTitleFont.font
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_EventKitUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_EventKitUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_EventKitUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_EventKitUI
- __titleFont.font
- _objc_msgSend$_dateTimeViewForLine:
- _objc_msgSend$_frameMutatedForProximityToHourLine:
- _objc_msgSend$_layoutDayIfNeeded:isLoadingAsync:
- _objc_msgSend$_layoutNeededForDay:isLoadingAsync:
- _objc_msgSend$_setDateTimeString:line:
- _objc_msgSend$_updateColorBarFrame
- _objc_msgSend$_updateTableHeaderLayout
- _objc_msgSend$_viewControllerForPresentingViewControllers
- _objc_msgSend$carplayBackgroundViewVerticalInset
- _objc_msgSend$commonSetupCellWithTitle:showExtraSpaceAtBottom:
- _objc_msgSend$initWithEvent:reminder:editable:showExtraSpaceAtBottom:allowDataDetector:title:textFromEventAndReminderBlock:
- _objc_msgSend$reminderBackgroundColor:style:miniPreview:completed:
- _objc_msgSend$secondarySystemFillColor
CStrings:
+ "@\"EKDayViewContentLayoutParameters\""
+ "@32@0:8{CGSize=dd}16"
+ "@68@0:8@16@24B32B36d40B48@52@?60"
+ "B24@0:8@\"UITraitCollection\"16"
+ "CUIKSmallCapAMPMTimezoneClarificationStringForStartDate:endDate:startTimeZone:endTimeZone:color:"
+ "EKDayViewContentLayoutParameters"
+ "EKDayViewContentStackView"
+ "Find"
+ "How should this change be applied?"
+ "T@\"UIVisualEffectView\",&,N,V_effectView"
+ "T@?,C,N,V_backgroundChangedCallback"
+ "T{CGSize=dd},R,N,V_boundsSize"
+ "Unknown Presentation Option"
+ "_backgroundChangedCallback"
+ "_boundsSize"
+ "_carSystemPrimaryColor"
+ "_carSystemSecondaryColor"
+ "_dateTimeViewForLine:color:"
+ "_effectView"
+ "_initializeTravelLine"
+ "_lastLayoutParametersForDay"
+ "_lastLayoutParametersForDayForPreload"
+ "_layoutDayIfNeeded:"
+ "_layoutNeededForDay:"
+ "_layoutParameters"
+ "_layoutParametersLock"
+ "_noonAttributedStringForString:orientation:"
+ "_pinningValid"
+ "_setDateTimeString:line:color:"
+ "_topStackViews"
+ "_updateTableHeaderLayoutForWidth:"
+ "_updateVisualEffectBackground"
+ "_usesVisualEffectBackground"
+ "backgroundChangedCallback"
+ "backgroundViewForEventIndicator"
+ "bottomSpaceAdjustment"
+ "boundsSize"
+ "calculateBackgroundImageFrame:travelTimeFrame:forState:withMargins:"
+ "carplayBackgroundViewInsets"
+ "carplayUsesColorfulBackgrounds"
+ "cellContentView"
+ "commonSetupCellWithTitle:showExtraSpaceAtBottom:extraBottomSpaceAdjustment:"
+ "effectView"
+ "initWithBoundsSize:"
+ "initWithEvent:reminder:editable:showExtraSpaceAtBottom:extraBottomSpaceAdjustment:allowDataDetector:title:textFromEventAndReminderBlock:"
+ "insertArrangedSubview:atIndex:"
+ "invalidateOccurrenceLayout"
+ "layoutParameters"
+ "noonAttributedStringComponentsForOrientation:"
+ "noonAttributedStringForOrientation:"
+ "noonString"
+ "plus.square.on.square"
+ "registerForTraitChanges:withAction:"
+ "reminderBackgroundColor:style:miniPreview:completed:darkenForAllDayArea:"
+ "setBackground:"
+ "setBackgroundChangedCallback:"
+ "setBackgroundEffects:"
+ "setEffectView:"
+ "standardBackgroundMargins:"
+ "updateCurrentLayoutParameters"
+ "updateViewBackgroundChangedCallback"
+ "updateWithRows:"
+ "v16@?0@\"EKDayOccurrenceView\"8"
+ "v16@?0@\"EKDayViewContentItem\"8"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "v36@0:8@16B24d28"
+ "wantsDismissOnSizeClassChangeWithNewTraitCollection:"
+ "wantsPillShape"
+ "\xf0\xf0q"
- "@60@0:8@16@24B32B36B40@44@?52"
- "_dateTimeViewForLine:"
- "_eventBackgroundColorBar"
- "_lastLayoutWidthForDay"
- "_lastLayoutWidthForDayForPreload"
- "_layoutBounds"
- "_layoutBoundsLock"
- "_layoutDayIfNeeded:isLoadingAsync:"
- "_layoutNeededForDay:isLoadingAsync:"
- "_setDateTimeString:line:"
- "_updateColorBarFrame"
- "_updateTableHeaderLayout"
- "_viewControllerForPresentingViewControllers"
- "carplayBackgroundViewVerticalInset"
- "commonSetupCellWithTitle:showExtraSpaceAtBottom:"
- "doc.badge.plus"
- "initWithEvent:reminder:editable:showExtraSpaceAtBottom:allowDataDetector:title:textFromEventAndReminderBlock:"
- "reminderBackgroundColor:style:miniPreview:completed:"
- "secondarySystemFillColor"
- "\xf0\xf0!b"
- "\xf0\xf0\x91"

```
