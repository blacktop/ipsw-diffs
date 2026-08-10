## AccessibilityLiveListenControlCenterModule

> `/System/Library/ControlCenter/Bundles/AccessibilityLiveListenControlCenterModule.bundle/AccessibilityLiveListenControlCenterModule`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-3237.1.0.0.0
-  __TEXT.__text: 0x10f8
+3240.3.0.0.0
+  __TEXT.__text: 0x1474
   __TEXT.__objc_methlist: 0x3ac
-  __TEXT.__const: 0x10
+  __TEXT.__const: 0x30
   __TEXT.__gcc_except_tab: 0x8c
   __TEXT.__cstring: 0x6f
-  __TEXT.__oslogstring: 0x75
+  __TEXT.__oslogstring: 0x2cc
   __TEXT.__unwind_info: 0xf8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x360
+  __DATA_CONST.__objc_selrefs: 0x368
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x88

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 38
-  Symbols:   58
-  CStrings:  11
+  Symbols:   60
+  CStrings:  15
 
Symbols:
+ _AXAIWhiteGloveLoggingEnabled
+ _objc_release_x24
Functions:
~ sub_242d78aa0 -> sub_2426feaa0 : 164 -> 352
~ sub_242d78e90 -> sub_2426fef4c : 340 -> 748
~ sub_242d790e4 -> sub_2426ff338 : 200 -> 496
CStrings:
+ "rdar://148155597 AXLiveListenModuleViewController _updateAlphas expanded=%d platterAlpha=%f shortcutFrame={%f,%f,%f,%f} buttonFrame={%f,%f,%f,%f}"
+ "rdar://148155597 AXLiveListenModuleViewController buttonTapped expanded=%d isLiveListenEnabled=%d isLiveListenRouteSelected=%d buttonFrame={%f,%f,%f,%f} platterAlpha=%f"
+ "rdar://148155597 AXLiveListenModuleViewController buttonTapped ignored (long-press) touchDownAge=%f expanded=%d isLiveListenEnabled=%d"
+ "rdar://148155597 AXLiveListenModuleViewController shortcutDidChangeSize expanded=%d viewBounds={%f,%f} newContentSize={%f,%f} isLiveListenEnabled=%d"
```
