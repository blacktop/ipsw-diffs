## CalendarUIKit

> `/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit`

```diff

-1276.0.0.0.0
-  __TEXT.__text: 0x22474c
-  __TEXT.__auth_stubs: 0x47f0
-  __TEXT.__objc_methlist: 0x7a60
+1279.0.0.0.0
+  __TEXT.__text: 0x224410
+  __TEXT.__auth_stubs: 0x47e0
+  __TEXT.__objc_methlist: 0x7a78
   __TEXT.__const: 0x10714
-  __TEXT.__cstring: 0xcb92
+  __TEXT.__cstring: 0xcbb2
   __TEXT.__oslogstring: 0x3b08
-  __TEXT.__gcc_except_tab: 0xe80
+  __TEXT.__gcc_except_tab: 0xe8c
   __TEXT.__ustring: 0x2042
   __TEXT.__dlopen_cstrs: 0xb1
   __TEXT.__constg_swiftt: 0x59f8

   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0x50
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x6f68
+  __TEXT.__unwind_info: 0x6f78
   __TEXT.__eh_frame: 0x4c7c
   __TEXT.__objc_classname: 0x1098
-  __TEXT.__objc_methname: 0x19597
+  __TEXT.__objc_methname: 0x195c3
   __TEXT.__objc_methtype: 0x256a
-  __TEXT.__objc_stubs: 0x124a0
-  __DATA_CONST.__got: 0x1a60
-  __DATA_CONST.__const: 0x1d10
+  __TEXT.__objc_stubs: 0x12500
+  __DATA_CONST.__got: 0x19e8
+  __DATA_CONST.__const: 0x1d40
   __DATA_CONST.__objc_classlist: 0x4f8
   __DATA_CONST.__objc_catlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6490
+  __DATA_CONST.__objc_selrefs: 0x64a0
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x1d0
-  __AUTH_CONST.__auth_got: 0x2408
-  __AUTH_CONST.__const: 0x8ea8
-  __AUTH_CONST.__cfstring: 0x8700
+  __AUTH_CONST.__auth_got: 0x2400
+  __AUTH_CONST.__const: 0x9428
+  __AUTH_CONST.__cfstring: 0x8720
   __AUTH_CONST.__objc_const: 0xda88
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0xa8

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
-  UUID: 389157EF-E1DA-390C-AB52-0A402D3F9D79
-  Functions: 11102
-  Symbols:   13949
-  CStrings:  7418
+  UUID: 0DB32C24-A11A-3F79-8DF8-CC9B242CA6D3
+  Functions: 11110
+  Symbols:   13943
+  CStrings:  7423
 
Symbols:
+ +[CUIKDefaultIconGenerator _adjustedAttributesWithLanguageIdentifierIfNeeded:calendar:]
+ +[CUIKDefaultIconGenerator _languageIdentifierForNumberingSystem:]
+ -[CUIKIcon _imageForDescriptor:]
+ -[CUIKIcon _imageForDescriptor:].cold.1
+ GCC_except_table26
+ _CUIKIsDarkColor
+ _NSLanguageIdentifierAttributeName
+ ___70+[CUIKDateStrings stylizedTimelineHourStringForHourDate:baseFontSize:]_block_invoke.191
+ ___block_descriptor_40_e8_32s_e27_v40?08{_NSRange=QQ}16^B32ls32l8
+ ___block_literal_global.55
+ ___block_literal_global.67
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_CalendarUIKit
+ _objc_msgSend$_adjustedAttributesWithLanguageIdentifierIfNeeded:calendar:
+ _objc_msgSend$_imageForDescriptor:
+ _objc_msgSend$_languageIdentifierForNumberingSystem:
+ _objc_msgSend$_numberingSystem
+ _objc_msgSend$enumerateAttribute:inRange:options:usingBlock:
+ _objc_msgSend$isRepeatedDay
+ _objc_msgSend$setShadow:forAppearance:
- -[CUIKIcon imageForDescriptor:].cold.1
- -[UIColor(CUIKPlatforms) darkerColorWithFactor:]
- _CUIKColorAdjustSaturationBrightnessAlpha
- _CUIKColorFromString
- _CalDebugColorBackgroundCalendarOpacity
- _CalDebugColorBackgroundFinalOpacity
- _CalDebugColorReminderBorderColor
- _CalDebugColorSecondaryTextAlpha
- _CalDebugColorSecondaryTextBlendWithLabel
- _CalDebugColorSecondaryTextBrightness
- _CalDebugColorSecondaryTextSaturation
- _CalDebugColorSecondaryTextType
- _CalDebugColorSelectedTextAlpha
- _CalDebugColorSelectedTextBrightness
- _CalDebugColorSelectedTextSaturation
- _CalDebugColorSelectedTextType
- _CalDebugColorTextAlpha
- _CalDebugColorTextBlendWithLabel
- _CalDebugColorTextBrightness
- _CalDebugColorTextSaturation
- _CalDebugColorTextType
- _CalGetRGBAFromString
- ___block_literal_global.56
- ___block_literal_global.68
- _objc_msgSend$colorWithHue:saturation:brightness:alpha:
- _objc_msgSend$getDebugColorNumberForPreference:dark:
- _objc_msgSend$getDebugColorStringForPreference:dark:
- _objc_msgSend$getHue:saturation:brightness:alpha:
CStrings:
+ "_adjustedAttributesWithLanguageIdentifierIfNeeded:calendar:"
+ "_imageForDescriptor:"
+ "_languageIdentifierForNumberingSystem:"
+ "_numberingSystem"
+ "arabext"
+ "enumerateAttribute:inRange:options:usingBlock:"
+ "isRepeatedDay"
+ "setShadow:forAppearance:"
+ "v40@?0@8{_NSRange=QQ}16^B32"
- "colorWithHue:saturation:brightness:alpha:"
- "darkerColorWithFactor:"
- "getDebugColorNumberForPreference:dark:"
- "getDebugColorStringForPreference:dark:"
- "getHue:saturation:brightness:alpha:"

```
