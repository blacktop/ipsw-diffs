## ScreenCaptureKit

> `/System/Library/Frameworks/ScreenCaptureKit.framework/ScreenCaptureKit`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
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
-  __TEXT.__text: 0x368e8
-  __TEXT.__objc_methlist: 0x384c
+740.57.1.0.0
+  __TEXT.__text: 0x36c84
+  __TEXT.__objc_methlist: 0x3864
   __TEXT.__const: 0x1fe
   __TEXT.__oslogstring: 0x3c42
-  __TEXT.__cstring: 0x5bf8
+  __TEXT.__cstring: 0x5cd8
   __TEXT.__gcc_except_tab: 0x55c
   __TEXT.__swift5_typeref: 0x5f
   __TEXT.__constg_swiftt: 0x54

   __TEXT.__swift5_fieldmd: 0x74
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xcf8
+  __TEXT.__unwind_info: 0xd00
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xaf0
+  __DATA_CONST.__const: 0xb68
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22f0
+  __DATA_CONST.__objc_selrefs: 0x22f8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x5c8
   __AUTH_CONST.__const: 0x278
-  __AUTH_CONST.__cfstring: 0x24a0
-  __AUTH_CONST.__objc_const: 0x8af0
+  __AUTH_CONST.__cfstring: 0x2600
+  __AUTH_CONST.__objc_const: 0x8b30
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x6c0
+  __AUTH_CONST.__auth_got: 0x6c8
   __AUTH.__objc_data: 0xf00
-  __DATA.__objc_ivar: 0x598
+  __DATA.__objc_ivar: 0x5a0
   __DATA.__data: 0x818
   __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1446
-  Symbols:   3347
-  CStrings:  859
+  Functions: 1451
+  Symbols:   3359
+  CStrings:  871
 
Symbols:
+ +[SCPreviewViewController recordingEditorActionForActivityTypes:]
+ -[SCRecordingEditor previewViewControllerDidFinish:action:]
+ _AnalyticsSendEventLazy
+ _OBJC_IVAR_$_SCRecordingEditor._analyticsSender
+ _OBJC_IVAR_$_SCRecordingEditor._clientBundleID
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
