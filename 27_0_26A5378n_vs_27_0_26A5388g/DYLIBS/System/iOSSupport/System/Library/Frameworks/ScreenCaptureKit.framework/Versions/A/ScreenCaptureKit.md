## ScreenCaptureKit

> `/System/iOSSupport/System/Library/Frameworks/ScreenCaptureKit.framework/Versions/A/ScreenCaptureKit`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-740.53.1.0.0
-  __TEXT.__text: 0x3f040
-  __TEXT.__objc_methlist: 0x388c
+740.57.1.0.0
+  __TEXT.__text: 0x3f3dc
+  __TEXT.__objc_methlist: 0x38a4
   __TEXT.__const: 0x21e
   __TEXT.__oslogstring: 0x3e87
-  __TEXT.__cstring: 0x6768
+  __TEXT.__cstring: 0x6848
   __TEXT.__gcc_except_tab: 0x76c
   __TEXT.__swift5_typeref: 0x5f
   __TEXT.__constg_swiftt: 0x54

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe18
+  __DATA_CONST.__const: 0xe90
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21f8
+  __DATA_CONST.__objc_selrefs: 0x2200
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x530
   __AUTH_CONST.__const: 0x278
-  __AUTH_CONST.__cfstring: 0x2780
-  __AUTH_CONST.__objc_const: 0x8a28
+  __AUTH_CONST.__cfstring: 0x28e0
+  __AUTH_CONST.__objc_const: 0x8a68
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x778
+  __AUTH_CONST.__auth_got: 0x780
   __AUTH.__objc_data: 0x7a8
-  __DATA.__objc_ivar: 0x584
+  __DATA.__objc_ivar: 0x58c
   __DATA.__data: 0x810
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x848

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard
   - /System/Library/PrivateFrameworks/CMCapture.framework/Versions/A/CMCapture
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/Versions/A/PhotosFormats
   - /System/Library/PrivateFrameworks/RTCReporting.framework/Versions/A/RTCReporting
   - /System/Library/PrivateFrameworks/ReplayKitMacHelper.framework/Versions/A/ReplayKitMacHelper

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1540
-  Symbols:   3466
-  CStrings:  936
+  Functions: 1545
+  Symbols:   3478
+  CStrings:  948
 
Symbols:
+ +[SCPreviewViewController recordingEditorActionForActivityTypes:]
+ -[SCRecordingEditor previewViewControllerDidFinish:action:]
+ OBJC_IVAR_$_SCRecordingEditor._analyticsSender
+ OBJC_IVAR_$_SCRecordingEditor._clientBundleID
+ _AnalyticsSendEventLazy
+ _SendRecordingEditorDismissed
+ _SendRecordingEditorPresented
+ _SendRecordingEditorReport
+ __OBJC_$_CLASS_METHODS_SCPreviewViewController
+ ___SendRecordingEditorReport_block_invoke
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ _objc_msgSend$previewViewControllerDidFinish:action:
+ _objc_msgSend$recordingEditorActionForActivityTypes:
- -[SCRecordingEditor previewViewControllerDidFinish:]
- _objc_msgSend$previewViewControllerDidFinish:
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "Action"
+ "ApplicationBundleId"
+ "Cancel"
+ "Dismissed"
+ "Error"
+ "Invalid"
+ "Save"
+ "Share"
+ "com.apple.UIKit.activity.SaveToCameraRoll"
+ "com.apple.screencapture.recordingeditor.dismissed"
+ "com.apple.screencapture.recordingeditor.presented"
```
