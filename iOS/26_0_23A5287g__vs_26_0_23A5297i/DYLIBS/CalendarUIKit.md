## CalendarUIKit

> `/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit`

```diff

-1274.0.0.0.0
-  __TEXT.__text: 0x2243d0
+1276.0.0.0.0
+  __TEXT.__text: 0x22474c
   __TEXT.__auth_stubs: 0x47f0
-  __TEXT.__objc_methlist: 0x7a50
-  __TEXT.__const: 0x10724
+  __TEXT.__objc_methlist: 0x7a60
+  __TEXT.__const: 0x10714
   __TEXT.__cstring: 0xcb92
   __TEXT.__oslogstring: 0x3b08
   __TEXT.__gcc_except_tab: 0xe80

   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0x50
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x6f60
+  __TEXT.__unwind_info: 0x6f68
   __TEXT.__eh_frame: 0x4c7c
   __TEXT.__objc_classname: 0x1098
-  __TEXT.__objc_methname: 0x1953f
+  __TEXT.__objc_methname: 0x19597
   __TEXT.__objc_methtype: 0x256a
-  __TEXT.__objc_stubs: 0x12480
+  __TEXT.__objc_stubs: 0x124a0
   __DATA_CONST.__got: 0x1a60
   __DATA_CONST.__const: 0x1d10
   __DATA_CONST.__objc_classlist: 0x4f8
   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6480
+  __DATA_CONST.__objc_selrefs: 0x6490
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x1d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 688A76DE-EDE9-3262-AD81-E35097661973
-  Functions: 11099
-  Symbols:   13943
-  CStrings:  7416
+  UUID: 389157EF-E1DA-390C-AB52-0A402D3F9D79
+  Functions: 11102
+  Symbols:   13949
+  CStrings:  7418
 
Symbols:
+ +[CUIKDateStrings overlayShortStringForDate:inCalendar:alwaysShowingDayNumber:]
+ +[CUIKTimeTextProvider need24HourFormatForLocale:]
+ _CUIKColorMatchesColor
+ ___block_descriptor_58_e8_32s40r_e17_v16?0"UIColor"8ls32l8r40l8
+ ___block_literal_global.56
+ _objc_msgSend$overlayShortStringForDate:inCalendar:alwaysShowingDayNumber:
- GCC_except_table26
- GCC_except_table31
- GCC_except_table45
- ___block_descriptor_58_e8_32s40r_e17_v16?0"UIColor"8lr40l8s32l8
- ___block_literal_global.41
Functions:
~ ___CUIKBackgroundColorForCalendarColorWithOpaqueForStyle_block_invoke : 392 -> 596
+ _CUIKColorMatchesColor
~ _CUIKLightStripeColorForColor : 136 -> 604
~ +[CUIKORStringGenerator _attributedStringWithSystemImageName:symbolAttributes:widthForSymbol:baseString:] : 612 -> 620
+ +[CUIKTimeTextProvider need24HourFormatForLocale:]
~ -[CUIKDefaultIconGenerator _drawDateNameWithContext:] : 1116 -> 1124
~ +[CUIKDateStrings overlayShortStringForDate:inCalendar:] : 160 -> 8
+ +[CUIKDateStrings overlayShortStringForDate:inCalendar:alwaysShowingDayNumber:]
~ ___70+[CUIKDateStrings stylizedTimelineHourStringForHourDate:baseFontSize:]_block_invoke_2 : 120 -> 128
CStrings:
+ "need24HourFormatForLocale:"
+ "overlayShortStringForDate:inCalendar:alwaysShowingDayNumber:"

```
