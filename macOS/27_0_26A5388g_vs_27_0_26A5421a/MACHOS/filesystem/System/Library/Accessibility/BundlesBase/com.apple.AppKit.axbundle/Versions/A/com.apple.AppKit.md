## com.apple.AppKit

> `/System/Library/Accessibility/BundlesBase/com.apple.AppKit.axbundle/Versions/A/com.apple.AppKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__const`

```diff

-331.0.0.0.0
-  __TEXT.__text: 0x2e28
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x478
-  __TEXT.__objc_classname: 0x30f
-  __TEXT.__cstring: 0x75f
-  __TEXT.__objc_methname: 0xbdb
+334.1.0.0.0
+  __TEXT.__text: 0x345c
+  __TEXT.__auth_stubs: 0x280
+  __TEXT.__objc_stubs: 0xc60
+  __TEXT.__objc_methlist: 0x530
+  __TEXT.__objc_classname: 0x3b7
+  __TEXT.__cstring: 0x898
+  __TEXT.__objc_methname: 0xce0
   __TEXT.__objc_methtype: 0x85
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x6c
+  __TEXT.__gcc_except_tab: 0x7c
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x1a8
-  __DATA_CONST.__const: 0x268
-  __DATA_CONST.__cfstring: 0x8c0
-  __DATA_CONST.__objc_classlist: 0xc0
+  __TEXT.__unwind_info: 0x1e0
+  __DATA_CONST.__const: 0x288
+  __DATA_CONST.__cfstring: 0xa80
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x48
-  __DATA_CONST.__auth_got: 0x140
-  __DATA_CONST.__got: 0xf0
-  __DATA.__objc_const: 0xdf0
-  __DATA.__objc_selrefs: 0x388
+  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0xf8
+  __DATA.__objc_const: 0x1030
+  __DATA.__objc_selrefs: 0x3e0
   __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0x780
+  __DATA.__objc_data: 0x8c0
   __DATA.__bss: 0x41
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 103
-  Symbols:   419
-  CStrings:  223
+  Functions: 118
+  Symbols:   466
+  CStrings:  245
 
Symbols:
+ +[NSCampoLightweightUIHostWindowAccessibility _accessibilityPerformValidations:]
+ +[NSCampoLightweightUIHostWindowAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[NSCampoLightweightUIHostWindowAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[NSViewWritingToolsAccessibility _accessibilityPerformValidations:]
+ +[NSViewWritingToolsAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[NSViewWritingToolsAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[NSCampoLightweightUIHostWindowAccessibility accessibilityPerformCancel]
+ -[NSCampoLightweightUIHostWindowAccessibility accessibilitySubrole]
+ -[NSViewWritingToolsAccessibility _canBringUpSiriWritingToolsUI]
+ -[NSViewWritingToolsAccessibility accessibilityActionDescription:]
+ -[NSViewWritingToolsAccessibility accessibilityActionNames]
+ -[NSViewWritingToolsAccessibility accessibilityPerformAction:]
+ GCC_except_table3
+ _AXSafeClassFromString
+ _OBJC_CLASS_$_NSCampoLightweightUIHostWindowAccessibility
+ _OBJC_CLASS_$_NSViewWritingToolsAccessibility
+ _OBJC_CLASS_$___NSCampoLightweightUIHostWindowAccessibility_super
+ _OBJC_CLASS_$___NSViewWritingToolsAccessibility_super
+ _OBJC_METACLASS_$_NSCampoLightweightUIHostWindowAccessibility
+ _OBJC_METACLASS_$_NSViewWritingToolsAccessibility
+ _OBJC_METACLASS_$___NSCampoLightweightUIHostWindowAccessibility_super
+ _OBJC_METACLASS_$___NSViewWritingToolsAccessibility_super
+ __OBJC_$_CLASS_METHODS_NSCampoLightweightUIHostWindowAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_NSViewWritingToolsAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_NSCampoLightweightUIHostWindowAccessibility
+ __OBJC_$_INSTANCE_METHODS_NSViewWritingToolsAccessibility
+ __OBJC_CLASS_RO_$_NSCampoLightweightUIHostWindowAccessibility
+ __OBJC_CLASS_RO_$_NSViewWritingToolsAccessibility
+ __OBJC_CLASS_RO_$___NSCampoLightweightUIHostWindowAccessibility_super
+ __OBJC_CLASS_RO_$___NSViewWritingToolsAccessibility_super
+ __OBJC_METACLASS_RO_$_NSCampoLightweightUIHostWindowAccessibility
+ __OBJC_METACLASS_RO_$_NSViewWritingToolsAccessibility
+ __OBJC_METACLASS_RO_$___NSCampoLightweightUIHostWindowAccessibility_super
+ __OBJC_METACLASS_RO_$___NSViewWritingToolsAccessibility_super
+ ___62-[NSViewWritingToolsAccessibility accessibilityPerformAction:]_block_invoke
+ ___64-[NSViewWritingToolsAccessibility _canBringUpSiriWritingToolsUI]_block_invoke
+ ___73-[NSCampoLightweightUIHostWindowAccessibility accessibilityPerformCancel]_block_invoke
+ ___NSArray0__struct
+ _objc_msgSend$_canBringUpSiriWritingToolsUI
+ _objc_msgSend$_isCampoAvailableForWritingTools
+ _objc_msgSend$allowsWritingToolsAffordance
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$dismissImmediately
+ _objc_msgSend$isEligible
+ _objc_msgSend$performSelector:
+ _objc_msgSend$showExpandedForView:
+ _objc_opt_respondsToSelector
CStrings:
+ "AXShowWritingTools"
+ "AXSiriUIAffordance"
+ "NSCampoLightweightUIController"
+ "NSCampoLightweightUIHostWindow"
+ "NSCampoLightweightUIHostWindowAccessibility"
+ "NSTextView"
+ "NSViewWritingToolsAccessibility"
+ "NSWindow"
+ "__NSCampoLightweightUIHostWindowAccessibility_super"
+ "__NSViewWritingToolsAccessibility_super"
+ "_canBringUpSiriWritingToolsUI"
+ "_isCampoAvailableForWritingTools"
+ "accessibilityActionDescription:"
+ "accessibilityPerformCancel"
+ "accessibilitySubrole"
+ "allowsWritingToolsAffordance"
+ "arrayByAddingObject:"
+ "dismissImmediately"
+ "isEligible"
+ "performSelector:"
+ "show.writingtools"
+ "showExpandedForView:"
```
