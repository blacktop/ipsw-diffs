## ScreenCaptureKit

> `/System/Library/Frameworks/ScreenCaptureKit.framework/ScreenCaptureKit`

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
