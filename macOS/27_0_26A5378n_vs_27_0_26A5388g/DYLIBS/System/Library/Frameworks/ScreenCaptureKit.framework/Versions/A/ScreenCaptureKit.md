## ScreenCaptureKit

> `/System/Library/Frameworks/ScreenCaptureKit.framework/Versions/A/ScreenCaptureKit`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-740.53.1.0.0
-  __TEXT.__text: 0x3fda8
-  __TEXT.__objc_methlist: 0x37d4
+740.57.1.0.0
+  __TEXT.__text: 0x4016c
+  __TEXT.__objc_methlist: 0x37ec
   __TEXT.__const: 0x21a
   __TEXT.__oslogstring: 0x3e8c
-  __TEXT.__cstring: 0x6981
+  __TEXT.__cstring: 0x6a75
   __TEXT.__gcc_except_tab: 0x7d4
   __TEXT.__constg_swiftt: 0x54
   __TEXT.__swift5_typeref: 0x2e

   __TEXT.__swift5_fieldmd: 0x74
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xe60
+  __TEXT.__unwind_info: 0xe68
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x250
+  __DATA_CONST.__const: 0x278
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2280
+  __DATA_CONST.__objc_selrefs: 0x2288
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x538
-  __AUTH_CONST.__const: 0xf98
-  __AUTH_CONST.__cfstring: 0x2900
-  __AUTH_CONST.__objc_const: 0x8688
+  __AUTH_CONST.__const: 0xff8
+  __AUTH_CONST.__cfstring: 0x2a60
+  __AUTH_CONST.__objc_const: 0x86c8
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x650
+  __AUTH_CONST.__auth_got: 0x658
   __AUTH.__objc_data: 0x7a8
-  __DATA.__objc_ivar: 0x584
+  __DATA.__objc_ivar: 0x58c
   __DATA.__data: 0x730
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x848

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard
   - /System/Library/PrivateFrameworks/CMCapture.framework/Versions/A/CMCapture
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/Versions/A/PhotosFormats
   - /System/Library/PrivateFrameworks/RTCReporting.framework/Versions/A/RTCReporting
   - /System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/SkyLight

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1571
-  Symbols:   3490
-  CStrings:  948
+  Functions: 1576
+  Symbols:   3502
+  CStrings:  960
 
Symbols:
+ +[SCPreviewViewController recordingEditorActionForActivityTypes:]
+ -[SCPreviewViewController editorExtensionDidFinishWithAction:]
+ -[SCRecordingEditor previewViewControllerDidFinish:action:]
+ OBJC_IVAR_$_SCRecordingEditor._analyticsSender
+ OBJC_IVAR_$_SCRecordingEditor._clientBundleID
+ _AnalyticsSendEventLazy
+ _SendRecordingEditorDismissed
+ _SendRecordingEditorPresented
+ _SendRecordingEditorReport
+ __OBJC_$_CLASS_METHODS_SCPreviewViewController
+ ___62-[SCPreviewViewController editorExtensionDidFinishWithAction:]_block_invoke
+ ___SendRecordingEditorReport_block_invoke
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0l
+ ___block_descriptor_48_e8_32s_e5_v8?0l
+ _objc_msgSend$previewViewControllerDidFinish:action:
+ _objc_msgSend$recordingEditorActionForActivityTypes:
- -[SCPreviewViewController viewControlerDidFinish]
- -[SCRecordingEditor previewViewControllerDidFinish:]
- ___49-[SCPreviewViewController viewControlerDidFinish]_block_invoke
- _objc_msgSend$previewViewControllerDidFinish:
CStrings:
+ "-[SCPreviewViewController editorExtensionDidFinishWithAction:]"
+ "@\"NSDictionary\"8@?0"
+ "Action"
+ "ApplicationBundleId"
+ "Cancel"
+ "Dismissed"
+ "Error"
+ "Invalid"
+ "Save"
+ "Share"
+ "a"
+ "com.apple.UIKit.activity.SaveToCameraRoll"
+ "com.apple.screencapture.recordingeditor.dismissed"
+ "com.apple.screencapture.recordingeditor.presented"
- "-[SCPreviewViewController viewControlerDidFinish]"
- "A"
```
