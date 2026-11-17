## ShareSheet

> `/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet`

```diff

-2131.30.43.2.1
-  __TEXT.__text: 0xc5db8
-  __TEXT.__objc_methlist: 0x1154c
+2131.30.65.0.0
+  __TEXT.__text: 0xc6158
+  __TEXT.__objc_methlist: 0x115bc
   __TEXT.__const: 0x630
-  __TEXT.__gcc_except_tab: 0x2120
+  __TEXT.__gcc_except_tab: 0x2158
   __TEXT.__oslogstring: 0x74ae
-  __TEXT.__cstring: 0x73fc
+  __TEXT.__cstring: 0x73e1
   __TEXT.__dlopen_cstrs: 0xb96
-  __TEXT.__ustring: 0x20a
-  __TEXT.__unwind_info: 0x41b8
+  __TEXT.__ustring: 0x1e4
+  __TEXT.__unwind_info: 0x41e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2960
+  __DATA_CONST.__const: 0x2988
   __DATA_CONST.__objc_classlist: 0x638
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x3a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8d80
+  __DATA_CONST.__objc_selrefs: 0x8de0
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x678
   __DATA_CONST.__got: 0xfe8
   __AUTH_CONST.__const: 0x1120
-  __AUTH_CONST.__cfstring: 0x5b20
-  __AUTH_CONST.__objc_const: 0x2a658
+  __AUTH_CONST.__cfstring: 0x5aa0
+  __AUTH_CONST.__objc_const: 0x2a688
   __AUTH_CONST.__objc_arrayobj: 0x510
   __AUTH_CONST.__objc_dictobj: 0x730
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2dc8
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0x14c0
+  __DATA.__objc_ivar: 0x14c4
   __DATA.__data: 0x2be9
   __DATA_DIRTY.__objc_data: 0x1068
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5962
-  Symbols:   10337
-  CStrings:  1640
+  Functions: 5973
+  Symbols:   10348
+  CStrings:  1636
 
Symbols:
+ -[SHSheetPresenter _presentCollaborationOptionsForCollaborationItem:share:]
+ -[SHSheetRouter _cancelOptionsViewController]
+ -[SHSheetRouter _closeOptionsViewController]
+ -[SHSheetRouter _commitOptionsViewController]
+ -[SHSheetRouter _installCommitButtonsOnOptionsViewController:]
+ -[SHSheetRouter _optionsDoneButtonWithAction:]
+ -[SHSheetRouter optionsViewControllerCommitHandler]
+ -[SHSheetRouter presentOptionsViewController:commitHandler:dismissalHandler:]
+ -[SHSheetRouter setOptionsViewControllerCommitHandler:]
+ GCC_except_table144
+ _OBJC_IVAR_$_SHSheetRouter._optionsViewControllerCommitHandler
+ ___75-[SHSheetPresenter _presentCollaborationOptionsForCollaborationItem:share:]_block_invoke
+ ___75-[SHSheetPresenter _presentCollaborationOptionsForCollaborationItem:share:]_block_invoke_2
+ ___block_descriptor_48_e8_32r40w_e38_v16?0"_SWCollaborationShareOptions"8lr32l8w40l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
- GCC_except_table141
- ___46-[SHSheetPresenter handleCollaborationOptions]_block_invoke_3
- ___46-[SHSheetPresenter handleCollaborationOptions]_block_invoke_4
- ___block_descriptor_40_e8_32s_e38_v16?0"_SWCollaborationShareOptions"8ls32l8
CStrings:
- "CREATING_TEXT"
- "Creating…"
- "WAITING_TEXT"
- "Waiting…"
```
