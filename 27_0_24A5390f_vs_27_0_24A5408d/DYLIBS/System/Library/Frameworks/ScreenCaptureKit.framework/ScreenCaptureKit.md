## ScreenCaptureKit

> `/System/Library/Frameworks/ScreenCaptureKit.framework/ScreenCaptureKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-740.57.1.0.0
-  __TEXT.__text: 0x36c84
+740.63.1.1.0
+  __TEXT.__text: 0x36c90
   __TEXT.__objc_methlist: 0x3864
   __TEXT.__const: 0x1fe
   __TEXT.__oslogstring: 0x3c42
Symbols:
+ -[SCControlCenterManager pickerDidDismiss:forStreamInfo:isCancelled:]
+ _objc_msgSend$pickerDidDismiss:forStream:isCancelled:
- -[SCControlCenterManager pickerDidCancel:forStreamInfo:]
- _objc_msgSend$pickerDidCancel:forStream:
Functions:
~ -[SCControlCenterManager pickerDidCancel:forStreamInfo:] -> -[SCControlCenterManager pickerDidDismiss:forStreamInfo:isCancelled:] : 196 -> 208
```
