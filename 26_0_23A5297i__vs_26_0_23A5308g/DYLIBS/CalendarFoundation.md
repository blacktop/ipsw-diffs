## CalendarFoundation

> `/System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation`

```diff

-1602.0.0.0.0
-  __TEXT.__text: 0x5beb0
+1603.0.0.0.0
+  __TEXT.__text: 0x5ba68
   __TEXT.__auth_stubs: 0x13b0
-  __TEXT.__objc_methlist: 0x5c4c
-  __TEXT.__cstring: 0x6692
+  __TEXT.__objc_methlist: 0x5bfc
+  __TEXT.__cstring: 0x64b2
   __TEXT.__const: 0x3d4
   __TEXT.__gcc_except_tab: 0xb58
   __TEXT.__oslogstring: 0x384c

   __TEXT.__swift5_fieldmd: 0x5c
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1a20
+  __TEXT.__unwind_info: 0x1a18
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_classname: 0xba5
-  __TEXT.__objc_methname: 0xe95f
-  __TEXT.__objc_methtype: 0x16ad
-  __TEXT.__objc_stubs: 0xaa20
+  __TEXT.__objc_methname: 0xe85d
+  __TEXT.__objc_methtype: 0x169c
+  __TEXT.__objc_stubs: 0xa9c0
   __DATA_CONST.__got: 0x838
-  __DATA_CONST.__const: 0x17d8
+  __DATA_CONST.__const: 0x1710
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4110
+  __DATA_CONST.__objc_selrefs: 0x40d8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x100
   __AUTH_CONST.__auth_got: 0x9e8
-  __AUTH_CONST.__const: 0xc58
-  __AUTH_CONST.__cfstring: 0x96a0
+  __AUTH_CONST.__const: 0xc38
+  __AUTH_CONST.__cfstring: 0x9340
   __AUTH_CONST.__objc_const: 0x7808
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x18

   __AUTH.__data: 0xe8
   __DATA.__objc_ivar: 0x348
   __DATA.__data: 0xa30
-  __DATA.__bss: 0x650
+  __DATA.__bss: 0x640
   __DATA_DIRTY.__objc_data: 0x1090
   __DATA_DIRTY.__data: 0xc0
   __DATA_DIRTY.__bss: 0x340

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A6F02970-462B-30F6-88B3-1CFB02D05D5A
-  Functions: 2529
-  Symbols:   8607
-  CStrings:  5591
+  UUID: 10A66E64-F3AD-3242-959A-DF824A628C7D
+  Functions: 2520
+  Symbols:   8559
+  CStrings:  5529
 
Symbols:
+ ___block_literal_global.53
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_CalendarFoundation
- +[CalPreferences _debugColorPreferences]
- +[CalPreferences _debugColorPreferences].cold.1
- +[CalPreferences getDebugColorNumberForPreference:dark:]
- +[CalPreferences getDebugColorStringForPreference:dark:]
- +[CalPreferences removeDebugColorPreference:dark:]
- +[CalPreferences setDebugColorNumberForPreference:value:dark:]
- +[CalPreferences setDebugColorStringForPreference:value:dark:]
- -[CalPreferences debugColorStringForString:isDark:]
- _CalDebugColorBackgroundAlpha
- _CalDebugColorBackgroundBlend
- _CalDebugColorBackgroundBrightness
- _CalDebugColorBackgroundCalendarOpacity
- _CalDebugColorBackgroundFinalOpacity
- _CalDebugColorBackgroundSaturation
- _CalDebugColorBackgroundType
- _CalDebugColorReminderBorderColor
- _CalDebugColorReminderColor
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
- _CalDebugColorTextDarkBlendBrightness
- _CalDebugColorTextDarkBlendGreenYellow
- _CalDebugColorTextSaturation
- _CalDebugColorTextType
- _CalDebugColorTextWhiteBlendAlpha
- ___40+[CalPreferences _debugColorPreferences]_block_invoke
- ___block_literal_global.148
- ___block_literal_global.95
- __debugColorPreferences._preferences
- __debugColorPreferences.onceToken
- _objc_msgSend$_debugColorPreferences
- _objc_msgSend$debugColorStringForString:isDark:
- _objc_msgSend$removePreference:notificationName:
CStrings:
+ "caldav"
- "Background Alpha"
- "Blend"
- "Blend With Label"
- "Brightness Adjust"
- "Calendar Opacity"
- "Dark Blend"
- "Dark Blend (Green/Yellow)"
- "DebugColorDark-%@"
- "DebugColorLight-%@"
- "Final Opacity"
- "OverrideBackgroundType"
- "OverrideSelectedTextType"
- "OverrideTextType"
- "Reminder Border"
- "Reminder Color"
- "Saturation Adjust"
- "Secondary Alpha"
- "Secondary Blend"
- "Secondary Brightness"
- "Secondary Sat"
- "SecondaryTextType"
- "Selected Alpha"
- "Selected Brightness"
- "Selected Saturation"
- "Text Alpha"
- "Text Brightness"
- "Text Saturation"
- "White Blend Alpha"
- "_debugColorPreferences"
- "debugColorStringForString:isDark:"
- "getDebugColorNumberForPreference:dark:"
- "getDebugColorStringForPreference:dark:"
- "removeDebugColorPreference:dark:"
- "setDebugColorNumberForPreference:value:dark:"
- "setDebugColorStringForPreference:value:dark:"
- "v36@0:8@16@24B32"

```
