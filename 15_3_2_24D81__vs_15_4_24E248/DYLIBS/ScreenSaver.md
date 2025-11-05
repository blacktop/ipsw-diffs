## ScreenSaver

> `/System/Library/Frameworks/ScreenSaver.framework/Versions/A/ScreenSaver`

```diff

-347.0.0.0.0
-  __TEXT.__text: 0x12b8c
+347.3.4.0.0
+  __TEXT.__text: 0x12dec
   __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x1164
+  __TEXT.__objc_methlist: 0x18ec
   __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x21c
   __TEXT.__cstring: 0x243b
   __TEXT.__oslogstring: 0x1aa0
-  __TEXT.__unwind_info: 0x648
+  __TEXT.__unwind_info: 0x668
   __TEXT.__objc_classname: 0x2df
   __TEXT.__objc_methname: 0x4852
   __TEXT.__objc_methtype: 0xfbc

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11e8
+  __DATA_CONST.__objc_selrefs: 0x15f0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x380
   __AUTH_CONST.__const: 0x690
   __AUTH_CONST.__cfstring: 0x18a0
-  __AUTH_CONST.__objc_const: 0x3018
+  __AUTH_CONST.__objc_const: 0x21b0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /System/Library/PrivateFrameworks/login.framework/Versions/A/login
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 60522903-1EFB-3C43-A337-C2E853A215ED
-  Functions: 549
-  Symbols:   1632
+  UUID: 3DA5ACDE-84BB-3113-9213-DE9E81DD8780
+  Functions: 564
+  Symbols:   1648
   CStrings:  1641
 
Symbols:
+ +[ScreenSaverDefaultsManager defaultsManager].cold.1
+ +[ScreenSaverExtensionModule _exportedInterface].cold.1
+ +[ScreenSaverMessageTracerLogger sharedLogger].cold.1
+ +[ScreenSaverModules homeFolder].cold.1
+ +[ScreenSaverModules sharedInstance].cold.1
+ +[ScreenSaverPhotoChooser _builtInCollectionsOrder].cold.1
+ -[ScreenSaverExtensionModule loadViewForFrame:isPreview:completionBlock:].cold.2
+ -[ScreenSaverMessageTracerLogger logMessageWithName:dictionary:].cold.1
+ -[ScreenSaverMessageTracerLogger logMessageWithName:dictionary:].cold.2
+ -[ScreenSaverMessageTracerLogger logMessageWithName:signature:].cold.1
+ -[ScreenSaverMessageTracerLogger logMessageWithName:signature:].cold.2
+ OSLogForCategory.cold.1
+ __65-[ScreenSaverExtensionModule requestConfigurationViewController:]_block_invoke.cold.1
+ __70-[ScreenSaverExtensionModule requestConfigurationSheetViewController:]_block_invoke.cold.1
+ __73-[ScreenSaverExtensionModule loadViewForFrame:isPreview:completionBlock:]_block_invoke.85.cold.1
+ __73-[ScreenSaverExtensionModule loadViewForFrame:isPreview:completionBlock:]_block_invoke_2.cold.1
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8

```
