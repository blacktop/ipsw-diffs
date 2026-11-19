## com.apple.AppKit

> `/System/Library/Accessibility/BundlesBase/com.apple.AppKit.axbundle/Versions/A/com.apple.AppKit`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__got`

```diff

-334.1.0.0.0
-  __TEXT.__text: 0x3204
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_stubs: 0xc60
-  __TEXT.__objc_methlist: 0x530
-  __TEXT.__objc_classname: 0x3b7
-  __TEXT.__cstring: 0x898
-  __TEXT.__objc_methname: 0xce0
+336.2.3.0.0
+  __TEXT.__text: 0x3728
+  __TEXT.__auth_stubs: 0x290
+  __TEXT.__objc_stubs: 0xca0
+  __TEXT.__objc_methlist: 0x5a4
+  __TEXT.__objc_classname: 0x403
+  __TEXT.__cstring: 0x8ba
+  __TEXT.__objc_methname: 0xd0a
   __TEXT.__objc_methtype: 0x85
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x7c
+  __TEXT.__gcc_except_tab: 0x8c
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x218
+  __TEXT.__unwind_info: 0x240
   __DATA_CONST.__const: 0x288
-  __DATA_CONST.__cfstring: 0xa80
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__cfstring: 0xaa0
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x50
-  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__auth_got: 0x158
   __DATA_CONST.__got: 0xf8
-  __DATA.__objc_const: 0x1030
-  __DATA.__objc_selrefs: 0x3e0
+  __DATA.__objc_const: 0x1150
+  __DATA.__objc_selrefs: 0x3f0
   __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0x8c0
+  __DATA.__objc_data: 0x960
   __DATA.__bss: 0x41
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 118
-  Symbols:   466
-  CStrings:  245
+  Functions: 128
+  Symbols:   489
+  CStrings:  249
 
Symbols:
+ +[NSWindowWritingToolsAccessibility _accessibilityPerformValidations:]
+ +[NSWindowWritingToolsAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[NSWindowWritingToolsAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[NSWindowWritingToolsAccessibility _canBringUpSiriWritingToolsUI]
+ -[NSWindowWritingToolsAccessibility _writingToolsCandidateView]
+ -[NSWindowWritingToolsAccessibility accessibilityActionDescription:]
+ -[NSWindowWritingToolsAccessibility accessibilityActionNames]
+ -[NSWindowWritingToolsAccessibility accessibilityPerformAction:]
+ _OBJC_CLASS_$_NSWindowWritingToolsAccessibility
+ _OBJC_CLASS_$___NSWindowWritingToolsAccessibility_super
+ _OBJC_METACLASS_$_NSWindowWritingToolsAccessibility
+ _OBJC_METACLASS_$___NSWindowWritingToolsAccessibility_super
+ __OBJC_$_CLASS_METHODS_NSWindowWritingToolsAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_NSWindowWritingToolsAccessibility
+ __OBJC_CLASS_RO_$_NSWindowWritingToolsAccessibility
+ __OBJC_CLASS_RO_$___NSWindowWritingToolsAccessibility_super
+ __OBJC_METACLASS_RO_$_NSWindowWritingToolsAccessibility
+ __OBJC_METACLASS_RO_$___NSWindowWritingToolsAccessibility_super
+ ___64-[NSWindowWritingToolsAccessibility accessibilityPerformAction:]_block_invoke
+ ___66-[NSWindowWritingToolsAccessibility _canBringUpSiriWritingToolsUI]_block_invoke
+ _objc_msgSend$_writingToolsCandidateView
+ _objc_msgSend$firstResponder
+ _objc_retainAutoreleaseReturnValue
CStrings:
+ "NSWindowWritingToolsAccessibility"
+ "__NSWindowWritingToolsAccessibility_super"
+ "_writingToolsCandidateView"
+ "firstResponder"
```
