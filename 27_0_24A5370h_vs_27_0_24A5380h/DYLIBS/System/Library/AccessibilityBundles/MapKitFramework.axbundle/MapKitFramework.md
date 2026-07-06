## MapKitFramework

> `/System/Library/AccessibilityBundles/MapKitFramework.axbundle/MapKitFramework`

```diff

-  __TEXT.__text: 0xabd4
-  __TEXT.__objc_methlist: 0x1254
+  __TEXT.__text: 0xb17c
+  __TEXT.__objc_methlist: 0x129c
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__cstring: 0x2011
+  __TEXT.__cstring: 0x2067
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x420
+  __TEXT.__unwind_info: 0x430
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x2c0
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x700
+  __DATA_CONST.__objc_selrefs: 0x730
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x2940
+  __AUTH_CONST.__cfstring: 0x29a0
   __AUTH_CONST.__objc_const: 0x3910
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x500

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 349
-  Symbols:   1556
-  CStrings:  693
+  Functions: 355
+  Symbols:   1576
+  CStrings:  699
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[MKMapViewAccessibility _axIsHostedInLocationConsentSecureWindow]
+ -[MKMapViewAccessibility accessibilityLabel]
+ -[MKMapViewAccessibility accessibilityTraits]
+ -[MKMapViewAccessibility isAccessibilityElement]
+ -[UIButtonAccessibility__MapKit__UIKit _axIsDuplicateButtonInLocationConsentSecureWindow]
+ -[UIButtonAccessibility__MapKit__UIKit isAccessibilityElement]
+ GCC_except_table108
+ GCC_except_table135
+ GCC_except_table158
+ GCC_except_table175
+ _CGRectEqualToRect
+ _OBJC_CLASS_$_AXRemoteElement
+ _OBJC_CLASS_$_NSNumber
+ _objc_msgSend$_axIsDuplicateButtonInLocationConsentSecureWindow
+ _objc_msgSend$_axIsHostedInLocationConsentSecureWindow
+ _objc_msgSend$frame
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$remoteChildrenDelegate
+ _objc_msgSend$superview
- GCC_except_table104
- GCC_except_table131
- GCC_except_table154
- GCC_except_table171
- _objc_retainAutoreleaseReturnValue
CStrings:
+ "AXIsDuplicateInLocationConsent"
+ "AXIsInLocationConsentWindow"
+ "_UIViewServiceSecureWindow"

```
