## NotesUI

> `/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI`

```diff

-3001.60.6.0.0
-  __TEXT.__text: 0x2af930
+3001.60.10.0.0
+  __TEXT.__text: 0x2b0974
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0x6ec
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x17320
+  __TEXT.__objc_methlist: 0x17350
   __TEXT.__const: 0xa3d4
   __TEXT.__cstring: 0x14099
-  __TEXT.__gcc_except_tab: 0x4b1c
-  __TEXT.__oslogstring: 0xa502
+  __TEXT.__gcc_except_tab: 0x4b2c
+  __TEXT.__oslogstring: 0xa572
   __TEXT.__ustring: 0x13668
   __TEXT.__swift5_typeref: 0xcb64
   __TEXT.__constg_swiftt: 0x3c68

   __TEXT.__swift_as_ret: 0x120
   __TEXT.__swift_as_cont: 0x208
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xc600
-  __TEXT.__eh_frame: 0x4b38
+  __TEXT.__unwind_info: 0xc628
+  __TEXT.__eh_frame: 0x4b40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x3c8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10160
+  __DATA_CONST.__objc_selrefs: 0x10180
   __DATA_CONST.__objc_protorefs: 0x178
-  __DATA_CONST.__objc_superrefs: 0x698
+  __DATA_CONST.__objc_superrefs: 0x6a0
   __DATA_CONST.__objc_arraydata: 0x338
-  __DATA_CONST.__got: 0x2f40
+  __DATA_CONST.__got: 0x2f48
   __AUTH_CONST.__const: 0xa700
   __AUTH_CONST.__cfstring: 0xc360
-  __AUTH_CONST.__objc_const: 0x246e0
+  __AUTH_CONST.__objc_const: 0x24718
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_intobj: 0x660

   __AUTH_CONST.__auth_got: 0x3348
   __AUTH.__objc_data: 0x40e8
   __AUTH.__data: 0x1c58
-  __DATA.__objc_ivar: 0x11f0
+  __DATA.__objc_ivar: 0x11f4
   __DATA.__data: 0x587c
   __DATA.__objc_stublist: 0x28
   __DATA.__common: 0x70

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15138
-  Symbols:   16015
-  CStrings:  3283
+  Functions: 15148
+  Symbols:   16026
+  CStrings:  3285
 
Symbols:
+ -[ICNote(UI) convertUnconvertedAttachmentsInTextStorage:]
+ -[ICTK2TextController attachmentNeedsConversion:]
+ -[ICTK2TextController init]
+ -[ICTTTextStorage unconvertedAttachmentRange]
+ GCC_except_table104
+ GCC_except_table126
+ GCC_except_table128
+ GCC_except_table130
+ GCC_except_table137
+ GCC_except_table139
+ GCC_except_table143
+ GCC_except_table148
+ GCC_except_table159
+ GCC_except_table71
+ GCC_except_table78
+ GCC_except_table86
+ _ICTTAttachmentNeedsConversionNotification
+ _OBJC_IVAR_$_ICTK2TextController._didFailAttachmentConversion
+ __OBJC_$_INSTANCE_VARIABLES_ICTK2TextController
+ ___45-[ICTTTextStorage unconvertedAttachmentRange]_block_invoke
+ ___56-[ICTTTextStorage redactAuthorAttributionsToCurrentUser]_block_invoke
- GCC_except_table103
- GCC_except_table125
- GCC_except_table127
- GCC_except_table136
- GCC_except_table138
- GCC_except_table142
- GCC_except_table158
- GCC_except_table79
- GCC_except_table82
- GCC_except_table96
CStrings:
+ "Attachments in %@ at %@ are still unconverted after filtering"
+ "Converting unconverted attachments in %@ at %@"
```
