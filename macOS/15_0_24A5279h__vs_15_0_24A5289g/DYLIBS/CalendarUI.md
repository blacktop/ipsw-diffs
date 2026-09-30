## CalendarUI

> `/System/Library/PrivateFrameworks/CalendarUI.framework/Versions/A/CalendarUI`

```diff

-1188.0.0.0.0
-  __TEXT.__text: 0xedbf0
-  __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_methlist: 0x11064
-  __TEXT.__const: 0x720
+1190.0.0.0.0
+  __TEXT.__text: 0xee848
+  __TEXT.__auth_stubs: 0x9b0
+  __TEXT.__objc_methlist: 0x1110c
+  __TEXT.__const: 0x710
   __TEXT.__gcc_except_tab: 0x1140
-  __TEXT.__cstring: 0x68c2
+  __TEXT.__cstring: 0x6896
   __TEXT.__oslogstring: 0x1ba6
-  __TEXT.__ustring: 0x462
-  __TEXT.__unwind_info: 0x3830
+  __TEXT.__ustring: 0x482
+  __TEXT.__unwind_info: 0x3840
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x2091
-  __TEXT.__objc_methname: 0x2c3bc
-  __TEXT.__objc_methtype: 0x54b1
-  __TEXT.__objc_stubs: 0x233c0
-  __DATA_CONST.__got: 0x12d8
+  __TEXT.__objc_classname: 0x20a2
+  __TEXT.__objc_methname: 0x2c4c8
+  __TEXT.__objc_methtype: 0x54fd
+  __TEXT.__objc_stubs: 0x23560
+  __DATA_CONST.__got: 0x12e8
   __DATA_CONST.__const: 0x4f0
-  __DATA_CONST.__objc_classlist: 0x808
+  __DATA_CONST.__objc_classlist: 0x810
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa6a8
-  __DATA_CONST.__objc_superrefs: 0x630
-  __DATA_CONST.__objc_arraydata: 0x458
-  __AUTH_CONST.__auth_got: 0x4c0
-  __AUTH_CONST.__const: 0x20f0
+  __DATA_CONST.__objc_selrefs: 0xa708
+  __DATA_CONST.__objc_superrefs: 0x638
+  __DATA_CONST.__objc_arraydata: 0x448
+  __AUTH_CONST.__auth_got: 0x4e8
+  __AUTH_CONST.__const: 0x20e0
   __AUTH_CONST.__cfstring: 0x8c60
-  __AUTH_CONST.__objc_const: 0x1f790
+  __AUTH_CONST.__objc_const: 0x1f8b8
   __AUTH_CONST.__objc_intobj: 0x5b8
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x258
-  __AUTH_CONST.__objc_doubleobj: 0x130
+  __AUTH_CONST.__objc_doubleobj: 0x110
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x1320
+  __AUTH.__objc_data: 0x8c0
+  __DATA.__objc_ivar: 0x1330
   __DATA.__data: 0x1c68
-  __DATA.__bss: 0x5c0
+  __DATA.__bss: 0x5d0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x47e0
   __DATA_DIRTY.__bss: 0x60

   - /System/Library/PrivateFrameworks/iCalendar.framework/Versions/A/iCalendar
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5976
-  Symbols:   15129
-  CStrings:  1205
+  Functions: 5989
+  Symbols:   15173
+  CStrings:  1204
 
Symbols:
+ +[CalUIBoxOccurrenceContentView _cachedImageWithName:]
+ -[DottedLineView .cxx_destruct]
+ -[DottedLineView _updateShapeLayer]
+ -[DottedLineView init]
+ -[DottedLineView layout]
+ -[DottedLineView setBackgroundColor:]
+ -[EKUINewTimeOptionView index]
+ -[EKUINewTimeOptionView initWithController:delegate:alternativeTime:index:]
+ -[EKUINewTimeOptionView setIndex:]
+ -[EKUINewTimeOptionsGadget _createNewTimeOptionViewWithAlternativeTime:index:]
+ -[EKUIShowMoreOptionView axTitle]
+ -[EKUIShowMoreOptionView initWithViewController:delegate:axTitle:]
+ -[EKUIShowMoreOptionView setAxTitle:]
+ -[ReminderStackContentView _event1:ordersBeforeEvent2:]
+ -[TimedContentView _createAttachmentViewsIfNeeded]
+ -[TimedContentView _createAttendeeViewsIfNeeded]
+ -[TimedContentView _createLocationViewsIfNeeded]
+ -[TimedContentView _createRepeatViewsIfNeeded]
+ OBJC_IVAR_$_CalUIBoxOccurrenceContentView._cachedTileOptions
+ OBJC_IVAR_$_DottedLineView._color
+ OBJC_IVAR_$_DottedLineView._shapeLayer
+ OBJC_IVAR_$_EKUINewTimeOptionView._index
+ OBJC_IVAR_$_EKUIShowMoreOptionView._axTitle
+ _CGPathAddLines
+ _CGPathCreateMutable
+ _CGRectGetMaxY
+ _CGRectGetMidX
+ _CGRectGetMinY
+ _OBJC_CLASS_$_DottedLineView
+ _OBJC_METACLASS_$_DottedLineView
+ __37-[CalUIResizingTextField updateLinks]_block_invoke.140
+ __37-[CalUIResizingTextField updateLinks]_block_invoke.142
+ __37-[CalUIResizingTextField updateLinks]_block_invoke_2.143
+ __OBJC_$_INSTANCE_METHODS_DottedLineView
+ __OBJC_$_INSTANCE_VARIABLES_DottedLineView
+ __OBJC_CLASS_RO_$_DottedLineView
+ __OBJC_METACLASS_RO_$_DottedLineView
+ ___54+[CalUIBoxOccurrenceContentView _cachedImageWithName:]_block_invoke
+ __block_literal_global.220
+ _cachedImageWithName:._cache
+ _cachedImageWithName:.onceToken
+ _kCALineCapRound
+ _objc_msgSend$_cachedImageWithName:
+ _objc_msgSend$_createAttachmentViewsIfNeeded
+ _objc_msgSend$_createAttendeeViewsIfNeeded
+ _objc_msgSend$_createLocationViewsIfNeeded
+ _objc_msgSend$_createNewTimeOptionViewWithAlternativeTime:index:
+ _objc_msgSend$_createRepeatViewsIfNeeded
+ _objc_msgSend$_updateShapeLayer
+ _objc_msgSend$axTitle
+ _objc_msgSend$cal_isWalletURL
+ _objc_msgSend$index
+ _objc_msgSend$initWithController:delegate:alternativeTime:index:
+ _objc_msgSend$initWithViewController:delegate:axTitle:
+ _objc_msgSend$insertView:atIndex:inGravity:
+ _objc_msgSend$setLineCap:
+ _objc_msgSend$setLineDashPhase:
+ _objc_msgSend$setTravelTimeView:
- -[CalUIBoxOccurrenceTravelTimeView fontSmoothingColor]
- -[CalUIBoxOccurrenceTravelTimeView setFontSmoothingColor:]
- -[EKUINewTimeOptionView initWithController:delegate:alternativeTime:]
- -[EKUINewTimeOptionsGadget _createNewTimeOptionViewWithAlternativeTime:]
- -[EKUIShowMoreOptionView initWithViewController:delegate:]
- OBJC_IVAR_$_CalUIBoxOccurrenceTravelTimeView._fontSmoothingColor
- __37-[CalUIResizingTextField updateLinks]_block_invoke.137
- __37-[CalUIResizingTextField updateLinks]_block_invoke.139
- __37-[CalUIResizingTextField updateLinks]_block_invoke_2.140
- ___80-[CalUIBoxOccurrenceTravelTimeView setDividerColor:backgroundColor:stripeColor:]_block_invoke
- ___block_descriptor_64_e8_32s40s_e39_B40?0{CGRect={CGPoint=dd}{CGSize=dd}}8l
- _objc_msgSend$_createNewTimeOptionViewWithAlternativeTime:
- _objc_msgSend$initWithController:delegate:alternativeTime:
- _objc_msgSend$initWithViewController:delegate:
CStrings:
+ "%!@(MISSING). %!@(MISSING) %!@(MISSING) %!@(MISSING). %!@(MISSING)."
+ "%!@(MISSING). %!@(MISSING) %!@(MISSING) %!@(MISSING). %!@(MISSING). %!@(MISSING) %!@(MISSING)"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CalendarUI/CalendarUI/EventKitUI/EKViewController.m"
+ "AXHeading"
+ "Go to Next Occurrence"
+ "Go to Previous Occurrence"
+ "H:|[divider]|"
+ "Option %!i(MISSING)"
+ "V:|-(vInset)-[colorBar]-(vInset@vInsetPriority)-[divider(divHeight)]|"
- "%!@(MISSING). %!@(MISSING) %!@(MISSING) %!@(MISSING)"
- "%!@(MISSING). %!@(MISSING) %!@(MISSING) %!@(MISSING). %!@(MISSING) %!@(MISSING)"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CalendarUI/CalendarUI/EventKitUI/EKViewController.m"
- "Go to Next Repeating"
- "Go to Previous Repeating"
- "H:|-(divInset)-[divider]-(divInset@999)-|"
- "H:|[_alarmPicker(>=minWidth)]-(>=0)-|"
- "H:|[_alarmPicker]-(3)-[_addButton]"
- "V:|[colorBar][divider(divHeight)]|"
- "divInset"

```
