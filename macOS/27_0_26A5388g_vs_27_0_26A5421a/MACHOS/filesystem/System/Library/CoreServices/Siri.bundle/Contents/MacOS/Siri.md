## Siri

> `/System/Library/CoreServices/Siri.bundle/Contents/MacOS/Siri`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`

```diff

-3600.46.14.0.0
-  __TEXT.__text: 0x13c0
-  __TEXT.__auth_stubs: 0x130
-  __TEXT.__objc_stubs: 0x900
-  __TEXT.__objc_methlist: 0x118
+3600.46.19.14.4
+  __TEXT.__text: 0x1648
+  __TEXT.__auth_stubs: 0x140
+  __TEXT.__objc_stubs: 0x9e0
+  __TEXT.__objc_methlist: 0x14c
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x230
-  __TEXT.__objc_methname: 0x64f
-  __TEXT.__oslogstring: 0x110
+  __TEXT.__cstring: 0x274
+  __TEXT.__objc_methname: 0x6f1
+  __TEXT.__oslogstring: 0x136
   __TEXT.__objc_classname: 0xf
-  __TEXT.__objc_methtype: 0x94
-  __TEXT.__unwind_info: 0xb0
+  __TEXT.__objc_methtype: 0xa1
+  __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0x260
+  __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0xb0
-  __DATA.__objc_const: 0xb8
-  __DATA.__objc_selrefs: 0x290
-  __DATA.__objc_ivar: 0x4
+  __DATA_CONST.__auth_got: 0xa8
+  __DATA_CONST.__got: 0xc0
+  __DATA.__objc_const: 0xf0
+  __DATA.__objc_selrefs: 0x2d0
+  __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/SpeechObjects.framework/Versions/A/Frameworks/DictationServices.framework/Versions/A/DictationServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 27
-  Symbols:   49
-  CStrings:  128
+  Functions: 31
+  Symbols:   52
+  CStrings:  144
 
Symbols:
+ _NSSelectorFromString
+ _OBJC_CLASS_$_NSStatusItem
+ ___kCFBooleanTrue
CStrings:
+ "%s Got hardware menu press invocation"
+ "-[SiriStatusMenu _onMouse:]"
+ "B"
+ "TB,V_ignoreMouseUp"
+ "_ignoreMouseUp"
+ "_onMouse:"
+ "_supportsDirectEvents"
+ "ignoreMouseUp"
+ "instancesRespondToSelector:"
+ "needsDirectEvents"
+ "sendActionOn:"
+ "setIgnoreMouseUp:"
+ "setNeedsDirectEvents:"
+ "setValue:forKey:"
+ "type"
+ "v20@0:8B16"
```
