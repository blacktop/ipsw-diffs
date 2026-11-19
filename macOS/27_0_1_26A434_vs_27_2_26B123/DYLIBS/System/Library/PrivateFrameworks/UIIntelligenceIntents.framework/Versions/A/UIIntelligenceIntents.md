## UIIntelligenceIntents

> `/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/Versions/A/UIIntelligenceIntents`

```diff

-9127.0.84.0.0
-  __TEXT.__text: 0x3054c
+9127.1.13.0.0
+  __TEXT.__text: 0x307b0
   __TEXT.__objc_methlist: 0x1ac
-  __TEXT.__const: 0x42c0
+  __TEXT.__const: 0x42e0
   __TEXT.__constg_swiftt: 0x998
-  __TEXT.__swift5_typeref: 0x138e
+  __TEXT.__swift5_typeref: 0x1398
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_reflstr: 0x92e
   __TEXT.__swift5_fieldmd: 0x820
   __TEXT.__swift5_assocty: 0x510
   __TEXT.__swift5_proto: 0x2f4
   __TEXT.__swift5_types: 0xa0
-  __TEXT.__cstring: 0x1465
-  __TEXT.__swift_as_entry: 0x100
-  __TEXT.__swift_as_ret: 0xcc
+  __TEXT.__cstring: 0x13ca
+  __TEXT.__swift_as_entry: 0x104
+  __TEXT.__swift_as_ret: 0xd0
   __TEXT.__swift_as_cont: 0x194
   __TEXT.__oslogstring: 0xa9a
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_capture: 0xcc
-  __TEXT.__unwind_info: 0xff0
-  __TEXT.__eh_frame: 0x1c8c
+  __TEXT.__unwind_info: 0x1008
+  __TEXT.__eh_frame: 0x1d0c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf8
+  __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e0
+  __DATA_CONST.__objc_selrefs: 0x2e8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__got: 0x2d0
-  __AUTH_CONST.__const: 0x1551
+  __DATA_CONST.__got: 0x2f0
+  __AUTH_CONST.__const: 0x1581
   __AUTH_CONST.__objc_const: 0x2a0
-  __AUTH_CONST.__auth_got: 0x978
+  __AUTH_CONST.__auth_got: 0x980
   __AUTH_CONST.__auth_ptr: 0x710
   __AUTH.__data: 0x1b8
-  __DATA.__data: 0xd20
-  __DATA.__bss: 0x5d90
-  __DATA.__common: 0x380
+  __DATA.__data: 0xc98
+  __DATA.__bss: 0x5c10
+  __DATA.__common: 0x330
+  __DATA_DIRTY.__data: 0x58
+  __DATA_DIRTY.__bss: 0x180
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1194
-  Symbols:   749
-  CStrings:  147
+  Functions: 1186
+  Symbols:   761
+  CStrings:  142
 
Symbols:
+ _IAPayloadKeyWritingToolsBundleID
+ _IASignalWritingToolsIntentInsertText
+ _IASignalWritingToolsIntentKeyPoints
+ _IASignalWritingToolsIntentPresentResult
+ _IASignalWritingToolsIntentProofread
+ _IASignalWritingToolsIntentRequestEditingContext
+ _IASignalWritingToolsIntentRewrite
+ _IASignalWritingToolsIntentSummarize
+ _IASignalWritingToolsIntentTransformList
+ _IASignalWritingToolsIntentTransformTable
+ _objc_msgSend$setCompositionSessionType:
+ _symbolic _____ySSG s11_SetStorageC
CStrings:
+ "Present Writing Tools result "
+ "The text to be inserted into the app’s active text field."
+ "Window number (stringified) of the window that hosts the target text field. When provided on macOS, the bridge activates that window (`makeKeyAndOrderFront:`) before starting Writing Tools so AppKit’s default `keyWindow.firstResponder` coordinator walk lands on the intended field — necessary when a transient popover has stolen key focus."
- "IntentInsertText"
- "IntentPresentResult"
- "IntentRequestEditingContext"
- "IntentTransformList"
- "IntentTransformTable"
- "Present writing tools result "
- "The text to be inserted into the app's active text field."
- "Window number (stringified) of the window that hosts the target text field. When provided on macOS, the bridge activates that window (`makeKeyAndOrderFront:`) before starting Writing Tools so AppKit's default `keyWindow.firstResponder` coordinator walk lands on the intended field — necessary when a transient popover has stolen key focus."
```
