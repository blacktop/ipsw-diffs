## WritingToolsUI

> `/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI`

```diff

-151.2.5.0.0
-  __TEXT.__text: 0x6d0d0
-  __TEXT.__objc_methlist: 0x4f2c
+151.2.7.0.0
+  __TEXT.__text: 0x6d734
+  __TEXT.__objc_methlist: 0x4f8c
   __TEXT.__const: 0x30e4
-  __TEXT.__cstring: 0x37a7
-  __TEXT.__oslogstring: 0x25ed
-  __TEXT.__gcc_except_tab: 0xe64
+  __TEXT.__cstring: 0x3837
+  __TEXT.__oslogstring: 0x26dd
+  __TEXT.__gcc_except_tab: 0xe78
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__swift5_typeref: 0xe426
   __TEXT.__swift5_reflstr: 0xe9c

   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0x20
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x26f8
+  __TEXT.__unwind_info: 0x2710
   __TEXT.__eh_frame: 0x8c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf18
+  __DATA_CONST.__const: 0xf68
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32d0
+  __DATA_CONST.__objc_selrefs: 0x3308
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0xa80
-  __AUTH_CONST.__const: 0x2158
+  __AUTH_CONST.__const: 0x2138
   __AUTH_CONST.__cfstring: 0xfe0
-  __AUTH_CONST.__objc_const: 0x6b60
+  __AUTH_CONST.__objc_const: 0x6bc0
   __AUTH_CONST.__objc_intobj: 0x5a0
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0xfa0
   __AUTH.__objc_data: 0x14f0
   __AUTH.__data: 0x900
-  __DATA.__objc_ivar: 0x3a0
+  __DATA.__objc_ivar: 0x3a8
   __DATA.__data: 0x1f78
   __DATA.__common: 0x128
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3093
-  Symbols:   3278
-  CStrings:  580
+  Functions: 3103
+  Symbols:   3289
+  CStrings:  586
 
Symbols:
+ -[WTMainPopoverViewController abandoned]
+ -[WTMainPopoverViewController setAbandoned:]
+ -[WTSceneHostedInputDashboardViewController dismissShareSheet]
+ -[WTSceneHostedInputDashboardViewController triggerShareSheetWithText:]
+ -[WTWritingToolsController _suspendEndOnSourceResignForPopoverPresentation]
+ -[WTWritingToolsController endOnSourceResignSuspension]
+ -[WTWritingToolsController restoreEndOnSourceResignAfterPopoverPresentation]
+ -[WTWritingToolsController setEndOnSourceResignSuspension:]
+ GCC_except_table193
+ GCC_except_table196
+ GCC_except_table240
+ GCC_except_table251
+ _OBJC_IVAR_$_WTMainPopoverViewController._abandoned
+ _OBJC_IVAR_$_WTWritingToolsController._endOnSourceResignSuspension
+ ___block_descriptor_40_e8_32w_e8_B12?0B8lw32l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- GCC_except_table191
- GCC_except_table194
- GCC_except_table238
- GCC_except_table245
- ___58-[WTUIActionClientToHost performActionForSceneController:]_block_invoke_5
CStrings:
+ "%@ does not implement dismissShareSheet"
+ "%@ does not implement triggerShareSheetWithText:"
+ "-[WTSceneHostedInputDashboardViewController dismissShareSheet]"
+ "-[WTSceneHostedInputDashboardViewController triggerShareSheetWithText:]"
+ "Cancelling delayed popover presentation for endWritingTools"
+ "Dismissing main popover that is no longer current (current=%@, presented=%@)"
+ "_presentMainPopoverViewControllerWithCompletion: existing presentedVC=%@ is being dismissed or orphaned, waiting before presenting Writing Tools popover"
- "_presentMainPopoverViewControllerWithCompletion: existing presentedVC=%@ is being dismissed, waiting before presenting Writing Tools popover"
```
