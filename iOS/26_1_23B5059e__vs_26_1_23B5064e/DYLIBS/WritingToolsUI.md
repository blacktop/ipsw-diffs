## WritingToolsUI

> `/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI`

```diff

-96.0.1.0.0
-  __TEXT.__text: 0x354e8
+96.1.1.0.0
+  __TEXT.__text: 0x35c3c
   __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x3dfc
+  __TEXT.__objc_methlist: 0x3e14
   __TEXT.__const: 0xa44
   __TEXT.__cstring: 0x254e
-  __TEXT.__oslogstring: 0x16ad
+  __TEXT.__oslogstring: 0x17d0
   __TEXT.__gcc_except_tab: 0xb68
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__constg_swiftt: 0x610

   __TEXT.__swift5_types: 0x3c
   __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xf60
+  __TEXT.__unwind_info: 0xf80
   __TEXT.__eh_frame: 0xf8
   __TEXT.__objc_classname: 0x665
-  __TEXT.__objc_methname: 0xa2b9
-  __TEXT.__objc_methtype: 0x2135
-  __TEXT.__objc_stubs: 0x6d80
+  __TEXT.__objc_methname: 0xa304
+  __TEXT.__objc_methtype: 0x2140
+  __TEXT.__objc_stubs: 0x6dc0
   __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__const: 0xa58
+  __DATA_CONST.__const: 0xaf0
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27e8
+  __DATA_CONST.__objc_selrefs: 0x27f8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb0
   __AUTH_CONST.__auth_got: 0x5e0
   __AUTH_CONST.__const: 0x820
   __AUTH_CONST.__cfstring: 0xae0
-  __AUTH_CONST.__objc_const: 0x54f0
+  __AUTH_CONST.__objc_const: 0x5520
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH.__objc_data: 0x10d0
   __AUTH.__data: 0x1f0
-  __DATA.__objc_ivar: 0x2c4
+  __DATA.__objc_ivar: 0x2c8
   __DATA.__data: 0xc48
   __DATA.__bss: 0x8c0
   __DATA.__common: 0xa0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DE6F0ADE-06B1-37EF-900C-788F01F3EBCE
-  Functions: 1595
-  Symbols:   4297
-  CStrings:  2482
+  UUID: 97952A02-7FCD-380E-B9B2-F649FE337469
+  Functions: 1607
+  Symbols:   4328
+  CStrings:  2494
 
Symbols:
+ -[WTWritingToolsController pendingError]
+ -[WTWritingToolsController presentError:].cold.1
+ -[WTWritingToolsController setPendingError:]
+ GCC_except_table120
+ GCC_except_table138
+ GCC_except_table170
+ GCC_except_table81
+ GCC_except_table87
+ _OBJC_IVAR_$_WTWritingToolsController._pendingError
+ ___41-[WTWritingToolsController presentError:]_block_invoke.542
+ ___41-[WTWritingToolsController presentError:]_block_invoke.542.cold.1
+ ___41-[WTWritingToolsController presentError:]_block_invoke_3
+ ___53-[WTWritingToolsController endWritingToolsWithError:]_block_invoke.475.cold.1
+ ___53-[WTWritingToolsController endWritingToolsWithError:]_block_invoke.477
+ ___59-[WTWritingToolsController presentFullScreenViewController]_block_invoke.667
+ ___60+[WTUIActionClientToHost actionForEndWritingToolsWithError:]_block_invoke
+ ___60+[WTUIActionClientToHost actionForEndWritingToolsWithError:]_block_invoke.cold.1
+ ___62-[WTWritingToolsController enrollmentDismissedWithCompletion:]_block_invoke.669
+ ___63-[WTWritingToolsController didEndWritingToolsSession:accepted:]_block_invoke
+ ___block_descriptor_32_e26_v16?0"BSActionResponse"8l
+ ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ _objc_msgSend$pendingError
+ _objc_msgSend$setPendingError:
- GCC_except_table117
- GCC_except_table132
- GCC_except_table166
- GCC_except_table37
- GCC_except_table43
- GCC_except_table78
- GCC_except_table84
- ___53-[WTWritingToolsController endWritingToolsWithError:]_block_invoke.476
- ___62-[WTWritingToolsController enrollmentDismissedWithCompletion:]_block_invoke.668
- ___block_literal_global.527
CStrings:
+ "@\"NSError\""
+ "Begin presenting fullScreenViewController for %ld..."
+ "End presenting fullScreenViewController for %ld..."
+ "Handling pendingError after fullScreenViewController presentation"
+ "T@\"NSError\",&,N,V_pendingError"
+ "Unable to present error at this time, pend for later presentation"
+ "Unexpected error when ending writing tools: %@"
+ "_pendingError"
+ "did present error: %@"
+ "pendingError"
+ "setPendingError:"
+ "updateKBSuppression shouldSuppress: %@, shouldSuppressForUCBUI: %@, sheet/popover: %@, appSizedContainerView %@, error: %d"
+ "updateSourceView shouldHostInAppSizedContainerView return NO (D)"
+ "updateSourceView shouldHostInAppSizedContainerView return NO (G)"
+ "updateSourceView shouldHostInAppSizedContainerView return YES (C)"
+ "updateSourceView shouldHostInAppSizedContainerView return YES (E))"
+ "updateSourceView shouldHostInAppSizedContainerView return YES (F)"
+ "v12@?0B8"
+ "will present error: %@"
- "Presenting fullScreenViewController for %ld..."
- "updateKBSuppression shouldSuppress: %@, shouldSuppressForUCBUI: %@, sheet/popover: %@,  appSizedContainerView %@"
- "updateSourceView shouldHostInAppSizedContainerView return NO (C)"
- "updateSourceView shouldHostInAppSizedContainerView return NO (E)"
- "updateSourceView shouldHostInAppSizedContainerView return YES (D)"
- "updateSourceView shouldHostInAppSizedContainerView return YES (F))"
- "updateSourceView shouldHostInAppSizedContainerView return YES (G)"

```
