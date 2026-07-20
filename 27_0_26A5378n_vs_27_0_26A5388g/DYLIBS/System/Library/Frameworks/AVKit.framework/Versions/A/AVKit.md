## AVKit

> `/System/Library/Frameworks/AVKit.framework/Versions/A/AVKit`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__gcc_except_tab`
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
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1360.65.1.15.2
-  __TEXT.__text: 0xe9078
-  __TEXT.__objc_methlist: 0xe758
-  __TEXT.__const: 0x1e38
+1360.69.1.0.0
+  __TEXT.__text: 0xe922c
+  __TEXT.__objc_methlist: 0xe760
+  __TEXT.__const: 0x1e48
   __TEXT.__constg_swiftt: 0x9c4
   __TEXT.__swift5_typeref: 0x310e
   __TEXT.__swift5_fieldmd: 0x5b4

   __TEXT.__swift_as_entry: 0x58
   __TEXT.__swift_as_cont: 0x68
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__oslogstring: 0x2384
+  __TEXT.__oslogstring: 0x23d3
   __TEXT.__gcc_except_tab: 0xe40
   __TEXT.__ustring: 0x15e
   __TEXT.__unwind_info: 0x3a78

   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7ea8
+  __DATA_CONST.__objc_selrefs: 0x7eb0
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x458
   __DATA_CONST.__objc_arraydata: 0x1e0
   __DATA_CONST.__got: 0xef0
   __AUTH_CONST.__const: 0x2f10
   __AUTH_CONST.__cfstring: 0x7e80
-  __AUTH_CONST.__objc_const: 0x18f28
+  __AUTH_CONST.__objc_const: 0x18f30
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x1e0

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 5387
   Symbols:   12174
-  CStrings:  1506
+  CStrings:  1507
 
Functions:
~ -[AVRoutePickerView layout] : 448 -> 532
~ -[AVRoutePickerView intrinsicContentSize] : 188 -> 264
~ ___89-[AVControlsContainerViewController _updateControlsVisibilityStateIfNeededWithAnimation:]_block_invoke_2 : 520 -> 784
~ -[AVFloatingPlaybackControlsViewController _updateAuxiliaryControlsViewStateIfNeeded] : 564 -> 576
CStrings:
+ "%s re-homing first responder to player content view after hiding HUD (was: %@)"
```
