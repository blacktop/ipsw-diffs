## AssistantUI

> `/System/Library/AccessibilityBundles/AssistantUI.axbundle/AssistantUI`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__DATA_DIRTY.__objc_data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x1b68
-  __TEXT.__objc_methlist: 0x204
+3048.0.0.0.0
+  __TEXT.__text: 0x1c0c
+  __TEXT.__objc_methlist: 0x20c
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x5e7
   __TEXT.__oslogstring: 0x35
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__unwind_info: 0xf8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x238
+  __DATA_CONST.__objc_selrefs: 0x240
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__got: 0xd8
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x780
   __AUTH_CONST.__objc_const: 0x510

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 44
-  Symbols:   226
+  Functions: 45
+  Symbols:   233
   CStrings:  79
 
Symbols:
+ -[AFUISiriSessionAccessibility _axClarityBundleIdentifierForStandardBundleIdentifier:]
+ _AX_CameraBundleName
+ _AX_ClarityCameraBundleName
+ _AX_ClarityPhotosBundleName
+ _AX_PhotosBundleName
+ _objc_msgSend$_axClarityBundleIdentifierForStandardBundleIdentifier:
+ _objc_retainAutoreleaseReturnValue
Functions:
~ -[AFUISiriSessionAccessibility _axIsAppInClarity:] : 132 -> 168
+ -[AFUISiriSessionAccessibility _axClarityBundleIdentifierForStandardBundleIdentifier:]
```
