## WritingToolsUI

> `/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI`

```diff

-151.1.9.0.0
-  __TEXT.__text: 0x6ad18
-  __TEXT.__objc_methlist: 0x4dcc
+151.1.11.0.0
+  __TEXT.__text: 0x6b868
+  __TEXT.__objc_methlist: 0x4df4
   __TEXT.__const: 0x30b4
-  __TEXT.__cstring: 0x3777
-  __TEXT.__oslogstring: 0x21ed
-  __TEXT.__gcc_except_tab: 0xdc8
+  __TEXT.__cstring: 0x3797
+  __TEXT.__oslogstring: 0x23cd
+  __TEXT.__gcc_except_tab: 0xde0
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__swift5_typeref: 0xde2c
   __TEXT.__swift5_capture: 0x45c

   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0x20
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2610
+  __TEXT.__unwind_info: 0x2660
   __TEXT.__eh_frame: 0x8c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe48
+  __DATA_CONST.__const: 0xeb8
   __DATA_CONST.__objc_classlist: 0x178
-  __DATA_CONST.__objc_catlist: 0x28
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3180
+  __DATA_CONST.__objc_selrefs: 0x31a8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x70
-  __DATA_CONST.__got: 0xa48
-  __AUTH_CONST.__const: 0x2108
+  __DATA_CONST.__got: 0xa68
+  __AUTH_CONST.__const: 0x2148
   __AUTH_CONST.__cfstring: 0xfe0
-  __AUTH_CONST.__objc_const: 0x6a28
+  __AUTH_CONST.__objc_const: 0x6a68
   __AUTH_CONST.__objc_intobj: 0x588
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0x60

   __AUTH.__objc_data: 0x14d0
   __AUTH.__data: 0x900
   __DATA.__objc_ivar: 0x390
-  __DATA.__data: 0x1ef0
+  __DATA.__data: 0x1f38
   __DATA.__common: 0x120
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3035
-  Symbols:   3227
-  CStrings:  562
+  Functions: 3051
+  Symbols:   3239
+  CStrings:  571
 
Symbols:
+ -[NSUndoManager(WTTurnTracking) wt_registerTurnWithHandler:]
+ -[WTWritingToolsController _registerUndoTrackingTurnOnUndoManager:]
+ GCC_except_table124
+ GCC_except_table130
+ GCC_except_table167
+ GCC_except_table183
+ GCC_except_table186
+ GCC_except_table230
+ GCC_except_table239
+ GCC_except_table241
+ GCC_except_table76
+ GCC_except_table78
+ GCC_except_table85
+ _OBJC_CLASS_$_NSUndoManager
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSUndoManager_$_WTTurnTracking
+ __OBJC_$_CATEGORY_NSUndoManager_$_WTTurnTracking
+ ___48-[WTWritingToolsController beginTextPlaceholder]_block_invoke
+ ___60-[NSUndoManager(WTTurnTracking) wt_registerTurnWithHandler:]_block_invoke
+ ___65-[WTWritingToolsController didBeginWritingToolsSession:contexts:]_block_invoke
+ ___67-[WTWritingToolsController _registerUndoTrackingTurnOnUndoManager:]_block_invoke
+ ___block_descriptor_32_e8_v16?08l
+ ___block_descriptor_40_e8_32bs_e23_v16?0"NSUndoManager"8ls32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0B8lw32l8
- GCC_except_table120
- GCC_except_table126
- GCC_except_table163
- GCC_except_table179
- GCC_except_table182
- GCC_except_table226
- GCC_except_table233
- GCC_except_table235
- GCC_except_table74
- GCC_except_table82
- _swift_retain_x27
CStrings:
+ "_registerUndoTrackingTurnOnUndoManager: %@"
+ "cancel-undo action fired for Proofread review: hasPendingSuggestions=%s"
+ "cancel-undo action fired for the generating placeholder"
+ "registering cancel-undo action for pending Proofread review on undoManager=%@"
+ "registering cancel-undo action for the generating placeholder on undoManager=%@"
+ "undo tracking turn fired: isUndo=%s remainingUndoCount=%lu remainingRedoCount=%lu"
+ "undo tracking turn reconciled: remainingUndoCount=%lu remainingRedoCount=%lu"
+ "v16@?0@\"NSUndoManager\"8"
+ "v16@?0@8"
```
