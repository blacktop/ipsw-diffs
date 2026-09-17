## AVKit

> `/System/iOSSupport/System/Library/AccessibilityBundles/AVKit.axbundle/Contents/MacOS/AVKit`

```diff

-3048.0.0.0.0
-  __TEXT.__text: 0xbc84
-  __TEXT.__objc_methlist: 0x1350
+3050.3.0.0.0
+  __TEXT.__text: 0xbe3c
+  __TEXT.__objc_methlist: 0x1368
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x414
-  __TEXT.__cstring: 0x2757
+  __TEXT.__cstring: 0x27ca
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x610
+  __TEXT.__unwind_info: 0x618
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x360
+  __DATA_CONST.__const: 0x380
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x798
+  __DATA_CONST.__objc_selrefs: 0x7b0
   __DATA_CONST.__objc_superrefs: 0x150
-  __DATA_CONST.__got: 0x178
-  __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x30c0
+  __DATA_CONST.__got: 0x180
+  __AUTH_CONST.__const: 0x240
+  __AUTH_CONST.__cfstring: 0x3160
   __AUTH_CONST.__objc_const: 0x39f0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xbe0
+  __AUTH.__objc_data: 0x2030
   __DATA.__data: 0x18
-  __DATA_DIRTY.__objc_data: 0x1450
-  __DATA_DIRTY.__common: 0x8
+  __DATA.__common: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 389
-  Symbols:   1265
-  CStrings:  419
+  Functions: 392
+  Symbols:   1272
+  CStrings:  425
 
Symbols:
+ -[AVMobileGlassPlaybackControlButtonAccessibility setPlaybackControlButtonIconState:]
+ -[_AVFocusContainerViewAccessibility _axUnifiedPlayerControlsViewController]
+ GCC_except_table164
+ GCC_except_table166
+ GCC_except_table175
+ GCC_except_table183
+ GCC_except_table227
+ GCC_except_table265
+ GCC_except_table302
+ GCC_except_table315
+ GCC_except_table329
+ GCC_except_table335
+ GCC_except_table349
+ GCC_except_table355
+ GCC_except_table374
+ ___104-[AVUnifiedPlayerPlaybackControlsViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2
+ ___NSArray0__struct
+ ___block_descriptor_32_e15_B32?08Q16^B24l
+ _objc_msgSend$_axUnifiedPlayerControlsViewController
+ _objc_msgSend$ax_filteredArrayUsingBlock:
- GCC_except_table163
- GCC_except_table165
- GCC_except_table174
- GCC_except_table182
- GCC_except_table226
- GCC_except_table264
- GCC_except_table300
- GCC_except_table313
- GCC_except_table327
- GCC_except_table333
- GCC_except_table347
- GCC_except_table353
- GCC_except_table371
Functions:
~ +[AVUnifiedPlayerPlaybackControlsViewControllerAccessibility _accessibilityPerformValidations:] : 284 -> 316
~ ___104-[AVUnifiedPlayerPlaybackControlsViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 264 -> 324
+ ___104-[AVUnifiedPlayerPlaybackControlsViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2
~ +[AVMobileGlassPlaybackControlButtonAccessibility _accessibilityPerformValidations:] : 72 -> 160
~ -[AVMobileGlassPlaybackControlButtonAccessibility setImageName:] : 208 -> 216
+ -[AVMobileGlassPlaybackControlButtonAccessibility setPlaybackControlButtonIconState:]
+ -[_AVFocusContainerViewAccessibility _axUnifiedPlayerControlsViewController]
~ -[_AVFocusContainerViewAccessibility _accessibilityShouldIncludeMediaDescriptionsRotor] : 128 -> 96
CStrings:
+ "B32@?0@8Q16^B24"
+ "pause"
+ "play"
+ "playbackControlButtonIconState"
+ "playbackControlsState"
+ "setPlaybackControlButtonIconState:"
```
