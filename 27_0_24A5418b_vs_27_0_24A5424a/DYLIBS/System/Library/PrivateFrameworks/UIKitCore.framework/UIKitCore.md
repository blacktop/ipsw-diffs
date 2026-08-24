## UIKitCore

> `/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`

```diff

-9127.0.84.1.902
-  __TEXT.__text: 0x1bcb194
+9127.0.84.1.115
+  __TEXT.__text: 0x1bcb43c
   __TEXT.__delay_helper: 0x1bc
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x19fa40
+  __TEXT.__objc_methlist: 0x19fa48
   __TEXT.__const: 0x4c6a8
   __TEXT.__dlopen_cstrs: 0x5164
   __TEXT.__swift5_typeref: 0x18cca

   __TEXT.__swift5_proto: 0x24fc
   __TEXT.__swift5_types: 0x1bbc
   __TEXT.__cstring: 0x101b1d
-  __TEXT.__oslogstring: 0x54b26
+  __TEXT.__oslogstring: 0x54c32
   __TEXT.__swift_as_entry: 0x2ac
   __TEXT.__swift_as_ret: 0x22c
   __TEXT.__swift_as_cont: 0x4f4

   __DATA_CONST.__objc_catlist: 0x368
   __DATA_CONST.__objc_protolist: 0x3550
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x95c28
+  __DATA_CONST.__objc_selrefs: 0x95c30
   __DATA_CONST.__objc_protorefs: 0xdc8
   __DATA_CONST.__objc_superrefs: 0x7500
   __DATA_CONST.__objc_arraydata: 0x41f8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 181271
-  Symbols:   291936
-  CStrings:  33767
+  Functions: 181272
+  Symbols:   291938
+  CStrings:  33771
 
Symbols:
+ -[_UIKeyboardFocusAssistant _shouldCancelDeferralPolicyTask:forRunnableTaskWithResponder:needsFocus:isReentrant:]
+ _objc_msgSend$_shouldCancelDeferralPolicyTask:forRunnableTaskWithResponder:needsFocus:isReentrant:
Functions:
~ -[UIKeyboardSceneDelegate _setKeyWindowSceneInputViews:animationStyle:] : 3336 -> 3564
~ -[_UIKeyboardFocusAssistant performWhenReadyForResponder:needsFocus:precedence:reason:readyTask:meanwhileTask:] : 2716 -> 2796
+ -[_UIKeyboardFocusAssistant _shouldCancelDeferralPolicyTask:forRunnableTaskWithResponder:needsFocus:isReentrant:]
CStrings:
+ "Do not cancel deferralPolicyTask: running task for snapshotting (responder:%{public}@)"
+ "Set key window scene input views for snapshotting"
+ "_setKeyWindowSceneInputViews: preparing input views for TEW"
+ "_setKeyWindowSceneInputViews: preparing input views for keyboardWindow"
```
