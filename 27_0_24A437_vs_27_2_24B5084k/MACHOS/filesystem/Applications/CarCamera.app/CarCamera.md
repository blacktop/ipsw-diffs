## CarCamera

> `/Applications/CarCamera.app/CarCamera`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`

```diff

-342.1.0.0.0
-  __TEXT.__text: 0x27840
-  __TEXT.__auth_stubs: 0x1620
-  __TEXT.__objc_stubs: 0x600
+351.2.0.0.0
+  __TEXT.__text: 0x2706c
+  __TEXT.__auth_stubs: 0x15f0
+  __TEXT.__objc_stubs: 0x680
   __TEXT.__objc_methlist: 0x880
-  __TEXT.__const: 0x20b4
-  __TEXT.__constg_swiftt: 0xfb4
-  __TEXT.__swift5_typeref: 0x24c8
-  __TEXT.__swift5_reflstr: 0x767
+  __TEXT.__const: 0x20a4
+  __TEXT.__constg_swiftt: 0xfc4
+  __TEXT.__swift5_typeref: 0x24c0
+  __TEXT.__swift5_reflstr: 0x787
   __TEXT.__swift5_fieldmd: 0x8cc
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_mpenum: 0x10

   __TEXT.__swift5_proto: 0xa0
   __TEXT.__swift5_types: 0x98
   __TEXT.__objc_classname: 0x308
-  __TEXT.__objc_methname: 0x1cdd
-  __TEXT.__oslogstring: 0xd7d
-  __TEXT.__cstring: 0x32b
-  __TEXT.__swift5_capture: 0x1c0
+  __TEXT.__objc_methname: 0x1d2d
+  __TEXT.__oslogstring: 0xf6d
+  __TEXT.__cstring: 0x31b
+  __TEXT.__swift5_capture: 0x1d0
   __TEXT.__objc_methtype: 0x102b
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0xad0
-  __TEXT.__eh_frame: 0x488
-  __DATA_CONST.__const: 0xd68
+  __TEXT.__unwind_info: 0xaf8
+  __TEXT.__eh_frame: 0x4b8
+  __DATA_CONST.__const: 0xd90
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__auth_got: 0xb18
+  __DATA_CONST.__auth_got: 0xb00
   __DATA_CONST.__got: 0x380
   __DATA_CONST.__auth_ptr: 0x678
   __DATA.__objc_const: 0x1308
-  __DATA.__objc_selrefs: 0x598
-  __DATA.__objc_data: 0x9e0
-  __DATA.__data: 0x1bf0
+  __DATA.__objc_selrefs: 0x5b8
+  __DATA.__objc_data: 0x9f0
+  __DATA.__data: 0x1bd0
   __DATA.__common: 0xb8
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 778
-  Symbols:   656
-  CStrings:  470
+  Functions: 783
+  Symbols:   653
+  CStrings:  479
 
Symbols:
+ _swift_bridgeObjectRelease_n
- _$s10CAFCombine25CAFCameraButtonObservableC12buttonActionSo09CAFButtonF0VSgvgTj
- _$s10CAFCombine25CAFCameraButtonObservableC12buttonActionSo09CAFButtonF0VSgvsTj
- _$s10CAFCombine25CAFCameraButtonObservableC16contentURLActionSSSgvgTj
- _$s10CAFCombine25CAFCameraButtonObservableC8disabledSbSgvgTj
CStrings:
+ "[CAMERAMODEL] CAFCameraButtonObserver %s didUpdateButtonAction %hhu"
+ "[CAMERAMODEL] CAFCameraButtonObserver %s didUpdateDisabled %{bool}d"
+ "[CAMERAMODEL] RequestContent URL button pressed (URL: %s)"
+ "[CAMERAMODEL] RequestContent failed, missing window scene."
+ "[CAMERAMODEL] RequestContent opening url %s was not successful"
+ "[CAMERAMODEL] nothing to do for %s"
+ "[CAMERAMODEL] performAction %s"
+ "[CAMERAMODEL] performAction failed, no service for %s"
+ "[CAMERAMODEL] sendAction to vehicle with .performAction"
+ "[CAMERAMODEL] submenu %s has no actionable entry, returning to top level"
+ "[CameraActionButton] submenu %s has no exit path, staying at top level"
+ "[CameraButtonGroup] no selected action resolved for %s"
+ "[CameraButtonGroup] no service for selected entry %s in %s, falling back to parent"
+ "[CameraButtonGroup] selectedEntryIndex %ld out of range for %ld entries in %s, falling back to parent"
+ "_submenuParentIdentifier"
+ "buttonAction"
+ "contentURLAction"
+ "disabled"
+ "entering submenu (using identifier)"
+ "setButtonAction:"
+ "sink submenuParentIdentifier"
+ "submenuParentIdentifier"
- "[CameraActionButton] %s sending action"
- "[CameraActionButton] RequestContent URL button pressed (URL: %s)"
- "[CameraActionButton] RequestContent failed, missing window scene."
- "[CameraActionButton] equestContent opening url %s was not successful"
- "[CameraActionButton] nothing to do"
- "[CameraActionButton] sendAction to vehicle with .performAction"
- "[are these buttons correct] %s"
- "_submenuParent"
- "entering submenu (using parent)"
- "sink submenuParent"
- "subItems"
- "submenuButtons update: static sort (active not at front)"
- "submenuParent"
```
