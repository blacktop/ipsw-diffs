## AppleIDSettings

> `/System/Library/ExtensionKit/Extensions/AppleIDSettings.appex/Contents/MacOS/AppleIDSettings`

```diff

-  __TEXT.__text: 0x7bf18
-  __TEXT.__auth_stubs: 0x2470
-  __TEXT.__objc_stubs: 0x2340
+  __TEXT.__text: 0x7ece8
+  __TEXT.__auth_stubs: 0x24b0
+  __TEXT.__objc_stubs: 0x2480
   __TEXT.__objc_methlist: 0x838
-  __TEXT.__const: 0x5e04
-  __TEXT.__constg_swiftt: 0x1d98
-  __TEXT.__swift5_typeref: 0x979c
+  __TEXT.__const: 0x5f14
+  __TEXT.__constg_swiftt: 0x1e00
+  __TEXT.__swift5_typeref: 0x9b54
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0x10dd
-  __TEXT.__swift5_fieldmd: 0x1058
+  __TEXT.__swift5_reflstr: 0x114d
+  __TEXT.__swift5_fieldmd: 0x1088
   __TEXT.__swift5_assocty: 0x6e8
   __TEXT.__swift5_proto: 0x288
   __TEXT.__swift5_types: 0x144
   __TEXT.__objc_classname: 0x6ff
-  __TEXT.__objc_methname: 0x2bf5
+  __TEXT.__objc_methname: 0x2ce5
   __TEXT.__objc_methtype: 0xae7
-  __TEXT.__oslogstring: 0x3d73
+  __TEXT.__oslogstring: 0x3fe3
   __TEXT.__cstring: 0x1b2d
-  __TEXT.__swift5_capture: 0x9b4
-  __TEXT.__swift_as_entry: 0x80
-  __TEXT.__swift_as_ret: 0xa0
-  __TEXT.__swift_as_cont: 0x110
+  __TEXT.__swift5_capture: 0xa38
+  __TEXT.__swift_as_entry: 0x90
+  __TEXT.__swift_as_ret: 0xac
+  __TEXT.__swift_as_cont: 0x124
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1828
-  __TEXT.__eh_frame: 0x1730
-  __DATA_CONST.__const: 0x3a88
+  __TEXT.__unwind_info: 0x18c0
+  __TEXT.__eh_frame: 0x1948
+  __DATA_CONST.__const: 0x3ba0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__auth_got: 0x1240
-  __DATA_CONST.__got: 0xab8
-  __DATA_CONST.__auth_ptr: 0xc40
-  __DATA.__objc_const: 0x32e8
-  __DATA.__objc_selrefs: 0xb88
-  __DATA.__objc_data: 0x15a8
-  __DATA.__data: 0x3160
-  __DATA.__bss: 0x5228
-  __DATA.__common: 0xd8
+  __DATA_CONST.__auth_got: 0x1260
+  __DATA_CONST.__got: 0xad8
+  __DATA_CONST.__auth_ptr: 0xc58
+  __DATA.__objc_const: 0x3368
+  __DATA.__objc_selrefs: 0xbd8
+  __DATA.__objc_data: 0x1630
+  __DATA.__data: 0x31d0
+  __DATA.__bss: 0x5248
+  __DATA.__common: 0xe8
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2378
-  Symbols:   335
-  CStrings:  1002
+  Functions: 2424
+  Symbols:   339
+  CStrings:  1026
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_entry : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
Symbols:
+ _OBJC_CLASS_$_ACDataclassAction
+ _OBJC_CLASS_$_NSPanel
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_task_immediate
+ _swift_task_isCurrentExecutorWithFlags
- _swift_dynamicCastObjCProtocolUnconditional
CStrings:
+ "Auth flow sheet cleanup"
+ "Auth flow sheet parent window changed; recreating sheet"
+ "Closing detached auth flow sheet"
+ "Dismissing auth flow sheet"
+ "Ending auth flow sheet via parent"
+ "_isComputingSignOutConfirmation"
+ "authFlowPanel"
+ "beginSheet:completionHandler:"
+ "close"
+ "dataclassActionsForDeletion"
+ "endSheet:"
+ "initWithContentRect:styleMask:backing:defer:"
+ "isSignOutConfirmationEnabled - false (active deviceLocator)"
+ "isSignOutConfirmationEnabled - false (merge action present)"
+ "isSignOutConfirmationEnabled - true (default)"
+ "isSignOutConfirmationEnabled - true (no account)"
+ "isSignOutConfirmationEnabled - true (services nil)"
+ "mmServicesProvider"
+ "setContentSize:"
+ "setContentView:"
+ "setMovable:"
+ "setTitleVisibility:"
+ "setTitlebarAppearsTransparent:"
+ "sheetParent"
+ "showCDPView invoked with no active auth flow sheet; falling back to inline contentView"
- "endAuthFlowUI"

```
