## ActivityAchievementsUI

> `/System/Library/AccessibilityBundles/ActivityAchievementsUI.axbundle/ActivityAchievementsUI`

```diff

-923.3.3.0.0
-  __TEXT.__text: 0x37c
-  __TEXT.__auth_stubs: 0xe0
-  __TEXT.__objc_stubs: 0x1a0
-  __TEXT.__objc_methlist: 0x64
-  __TEXT.__cstring: 0x120
-  __TEXT.__objc_classname: 0x78
-  __TEXT.__objc_methname: 0x243
-  __TEXT.__objc_methtype: 0x3b
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x78
+923.3.12.0.0
+  __TEXT.__text: 0x620
+  __TEXT.__auth_stubs: 0x100
+  __TEXT.__objc_stubs: 0x2a0
+  __TEXT.__objc_methlist: 0xc4
+  __TEXT.__cstring: 0x1db
+  __TEXT.__objc_classname: 0xb6
+  __TEXT.__objc_methname: 0x35a
+  __TEXT.__objc_methtype: 0x4b
+  __TEXT.__unwind_info: 0x90
+  __DATA_CONST.__auth_got: 0x88
+  __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__cfstring: 0x140
-  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__cfstring: 0x240
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x1b0
-  __DATA.__objc_selrefs: 0x98
-  __DATA.__objc_classrefs: 0x28
-  __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_data: 0xf0
+  __DATA.__objc_const: 0x2d0
+  __DATA.__objc_selrefs: 0xf0
+  __DATA.__objc_classrefs: 0x30
+  __DATA.__objc_superrefs: 0x10
+  __DATA.__objc_data: 0x190
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
+  - /System/Library/PrivateFrameworks/ActivityAchievementsUI.framework/ActivityAchievementsUI
   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11
-  Symbols:   72
-  CStrings:  42
+  Functions: 17
+  Symbols:   100
+  CStrings:  67
 
Symbols:
+ +[AAUIBadgeViewAccessibility _accessibilityPerformValidations:]
+ +[AAUIBadgeViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[AAUIBadgeViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[AAUIBadgeViewAccessibility accessibilityLabel]
+ -[AAUIBadgeViewAccessibility accessibilityTraits]
+ -[AAUIBadgeViewAccessibility isAccessibilityElement]
+ _OBJC_CLASS_$_AAUIAchievementFormatter
+ _OBJC_CLASS_$_AAUIBadgeViewAccessibility
+ _OBJC_CLASS_$___AAUIBadgeViewAccessibility_super
+ _OBJC_METACLASS_$_AAUIBadgeViewAccessibility
+ _OBJC_METACLASS_$___AAUIBadgeViewAccessibility_super
+ _UIAccessibilityTraitImage
+ __OBJC_$_CLASS_METHODS_AAUIBadgeViewAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_AAUIBadgeViewAccessibility(SafeCategory)
+ __OBJC_CLASS_RO_$_AAUIBadgeViewAccessibility
+ __OBJC_CLASS_RO_$___AAUIBadgeViewAccessibility_super
+ __OBJC_METACLASS_RO_$_AAUIBadgeViewAccessibility
+ __OBJC_METACLASS_RO_$___AAUIBadgeViewAccessibility_super
+ ___UIAccessibilityCastAsClass
+ _objc_msgSend$boolValue
+ _objc_msgSend$isAccessibilityUserDefinedElement
+ _objc_msgSend$localizedAttributedTitleString
+ _objc_msgSend$safeValueForKey:
+ _objc_msgSend$string
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$validateClass:hasInstanceVariable:withType:
+ _objc_release_x23
CStrings:
+ "\n"
+ " "
+ "<AAUIBadgeViewDelegate>"
+ "AAUIAchievementFormatter"
+ "AAUIBadgeView"
+ "AAUIBadgeViewAccessibility"
+ "B16@0:8"
+ "NLAchievementBulletinClientViewController"
+ "Q16@0:8"
+ "__AAUIBadgeViewAccessibility_super"
+ "_badgeDelegate"
+ "_formatter"
+ "accessibilityLabel"
+ "accessibilityTraits"
+ "achievement.badge.format"
+ "boolValue"
+ "isAccessibilityElement"
+ "isAccessibilityUserDefinedElement"
+ "localizedAttributedTitleString"
+ "safeValueForKey:"
+ "string"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "stringWithFormat:"
+ "validateClass:hasInstanceVariable:withType:"

```
