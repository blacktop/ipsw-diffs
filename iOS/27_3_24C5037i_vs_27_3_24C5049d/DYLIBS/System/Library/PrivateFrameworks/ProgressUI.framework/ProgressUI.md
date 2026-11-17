## ProgressUI

> `/System/Library/PrivateFrameworks/ProgressUI.framework/ProgressUI`

```diff

-2858.1.5.100.0
-  __TEXT.__text: 0x33d4
-  __TEXT.__objc_methlist: 0x43c
-  __TEXT.__const: 0x248
+2858.1.6.0.0
+  __TEXT.__text: 0x3b40
+  __TEXT.__objc_methlist: 0x49c
+  __TEXT.__const: 0x208
   __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__cstring: 0xa53
-  __TEXT.__unwind_info: 0x158
+  __TEXT.__cstring: 0xb83
+  __TEXT.__unwind_info: 0x178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x460
+  __DATA_CONST.__objc_selrefs: 0x4f0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x108
+  __DATA_CONST.__got: 0x110
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x6a0
-  __AUTH_CONST.__objc_const: 0xb30
+  __AUTH_CONST.__cfstring: 0x7c0
+  __AUTH_CONST.__objc_const: 0xb50
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x88
+  __DATA.__objc_ivar: 0x8c
   __DATA.__data: 0x160
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 61
-  Symbols:   285
-  CStrings:  92
+  Functions: 68
+  Symbols:   297
+  CStrings:  101
 
Symbols:
+ +[PUIProgressWindow _degreesFromDisplayOrientationString:]
+ +[PUIProgressWindow _errorDescriptionForTargetDisplayNotFound]
+ +[PUIProgressWindow _rotationDegreesForDisplay:]
+ -[PUIEnvironment displayWithUniqueId:]
+ -[PUIProgressWindow _initWithOptions:contextLevel:appearance:targetDisplayUniqueId:environment:]
+ -[PUIProgressWindow _mainDisplayNodeIndex]
+ -[PUIProgressWindow initWithOptions:contextLevel:appearance:targetDisplayUniqueId:]
+ GCC_except_table27
+ _OBJC_CLASS_$_NSString
+ _OBJC_IVAR_$_PUIProgressWindow._targetDisplay
+ _fmodf
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x4
- GCC_except_table21
- _objc_retain_x24
CStrings:
+ "%s:/product/display%lu"
+ "(none)"
+ "(null)"
+ "IODeviceTree"
+ "PUIProgressWindow found no display matching unique id %@; attached display unique ids: %@; falling back to main display"
+ "PUIProgressWindow ignoring unrecognized IORegistry boot rotation %@ from %@"
+ "PUIProgressWindow initWithOptions: %@ contextLevel: %@ appearance: %@ targetDisplayUniqueId: %@"
+ "PUIProgressWindow read boot rotation %@ from %@ (main display %@ id %u, %lu displays)"
+ "rot180"
+ "rot270"
+ "rot90"
+ "target display not found"
- "IODeviceTree:/product/display1"
- "PUIProgressWindow ignoring unrecognized IORegistry boot rotation %@"
- "PUIProgressWindow initWithOptions: %@ contextLevel: %@ appearance: %@"
```
