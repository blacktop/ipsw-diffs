## DMCEnrollmentProvider

> `/System/Library/AccessibilityBundles/DMCEnrollmentProvider.axbundle/DMCEnrollmentProvider`

```diff

-3050.3.8.0.0
-  __TEXT.__text: 0x4d0
+3050.3.12.0.0
+  __TEXT.__text: 0x47c
   __TEXT.__objc_methlist: 0x100
-  __TEXT.__cstring: 0x1b8
+  __TEXT.__cstring: 0x1c0
   __TEXT.__unwind_info: 0x90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libobjc.A.dylib
   Functions: 19
   Symbols:   91
-  CStrings:  20
+  CStrings:  19
 
Symbols:
+ -[DMCEnrollmentTableViewTitleCellAccessibility accessibilityTraits]
- -[DMCEnrollmentTableViewTitleCellAccessibility _accessibilityLoadAccessibilityInformation]
Functions:
~ +[DMCEnrollmentTableViewTitleCellAccessibility _accessibilityPerformValidations:] : 64 -> 24
~ -[DMCEnrollmentTableViewTitleCellAccessibility _accessibilityLoadAccessibilityInformation] -> -[DMCEnrollmentTableViewTitleCellAccessibility accessibilityTraits] : 116 -> 72
CStrings:
+ "UITableViewCell"
- "@"
- "label"
```
