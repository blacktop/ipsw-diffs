## ControlCenterUI

> `/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-701.101.0.0.0
-  __TEXT.__text: 0xbaf24
-  __TEXT.__objc_methlist: 0xb4e0
+702.0.0.0.0
+  __TEXT.__text: 0xbb00c
+  __TEXT.__objc_methlist: 0xb4f0
   __TEXT.__const: 0x2c3a
-  __TEXT.__cstring: 0x47f4
+  __TEXT.__cstring: 0x4824
   __TEXT.__gcc_except_tab: 0x82c
-  __TEXT.__oslogstring: 0x43fb
+  __TEXT.__oslogstring: 0x445b
   __TEXT.__dlopen_cstrs: 0x14e
   __TEXT.__constg_swiftt: 0x2a5c
   __TEXT.__swift5_typeref: 0x2c40

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x5b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68e0
+  __DATA_CONST.__objc_selrefs: 0x68e8
   __DATA_CONST.__objc_protorefs: 0x228
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x68
   __DATA_CONST.__got: 0xd28
   __AUTH_CONST.__const: 0x4471
-  __AUTH_CONST.__cfstring: 0x2f60
+  __AUTH_CONST.__cfstring: 0x2f80
   __AUTH_CONST.__objc_const: 0x11108
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0xa8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5044
-  Symbols:   7790
-  CStrings:  850
+  Functions: 5045
+  Symbols:   7792
+  CStrings:  852
 
Symbols:
+ -[CCUIModuleAlertViewController _propagateUserVisibilityStatus:]
+ _objc_msgSend$_propagateUserVisibilityStatus:
Functions:
+ -[CCUIModuleAlertViewController _propagateUserVisibilityStatus:]
~ -[CCUIModuleAlertViewController viewDidAppear:] : 100 -> 112
~ -[CCUIModuleAlertViewController viewWillDisappear:] : 92 -> 104
CStrings:
+ "[Appearance Propagation] ModuleAlert propagating userVisibilityStatus=%lu to container"
+ "com.apple.replaykit.controlcenter.screencapture"
```
