## UIFoundation

> `/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation`

```diff

-906.1.4.0.0
-  __TEXT.__text: 0xed564
+907.10.0.0.0
+  __TEXT.__text: 0xee05c
   __TEXT.__auth_stubs: 0x24b0
-  __TEXT.__objc_methlist: 0x9d40
+  __TEXT.__objc_methlist: 0x9d68
   __TEXT.__const: 0x69c
-  __TEXT.__cstring: 0xec52
-  __TEXT.__gcc_except_tab: 0x2a3c
-  __TEXT.__ustring: 0x2b6
+  __TEXT.__cstring: 0xec41
+  __TEXT.__gcc_except_tab: 0x2aac
+  __TEXT.__ustring: 0x2b0
   __TEXT.__oslogstring: 0xb
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__dof_UIFoundat: 0x2bd
-  __TEXT.__unwind_info: 0x33e4
+  __TEXT.__unwind_info: 0x3418
   __TEXT.__objc_classname: 0xec2
-  __TEXT.__objc_methname: 0x1b348
+  __TEXT.__objc_methname: 0x1b3ba
   __TEXT.__objc_methtype: 0x795b
-  __TEXT.__objc_stubs: 0x127e0
+  __TEXT.__objc_stubs: 0x12840
   __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0x8640
+  __DATA_CONST.__const: 0x86d8
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xd410
-  __DATA_CONST.__objc_selrefs: 0x5b98
+  __DATA_CONST.__objc_const: 0xd440
+  __DATA_CONST.__objc_selrefs: 0x5bb0
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__cfstring: 0xbc80
+  __AUTH_CONST.__cfstring: 0xbc40
   __AUTH_CONST.__objc_const: 0x3510
-  __AUTH_CONST.__const: 0xf68
+  __AUTH_CONST.__const: 0xf88
   __AUTH_CONST.__auth_ptr: 0x40
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0xa8

   __DATA.__objc_protorefs: 0x30
   __DATA.__objc_classrefs: 0x548
   __DATA.__objc_superrefs: 0x388
-  __DATA.__objc_ivar: 0x1040
+  __DATA.__objc_ivar: 0x1044
   __DATA.__data: 0xfca
   __DATA.__bss: 0x4d8
   __DATA_DIRTY.__objc_data: 0x19f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4378
-  Symbols:   15086
-  CStrings:  8094
+  Functions: 4389
+  Symbols:   15119
+  CStrings:  8100
 
Symbols:
+ -[NSTextLayoutFragment _resetLayoutFragmentFrame]
+ -[NSTextLineFragment enumerateTextSegmentBoundsInTextRange:dataSourceLocationsOnly:usingBlock:]
+ -[NSTextParagraph setElementRange:]
+ -[_NSTextRunStorage contentRange]
+ -[__NSTextSelectionLineFragmentInfo _resolveTrailingEdges].cold.1
+ GCC_except_table113
+ GCC_except_table39
+ GCC_except_table47
+ GCC_except_table77
+ GCC_except_table86
+ GCC_except_table87
+ GCC_except_table89
+ GCC_except_table97
+ _OBJC_IVAR_$__NSTextRunStorage._contentRange
+ ___33-[_NSTextRunStorage contentRange]_block_invoke
+ ___33-[_NSTextRunStorage contentRange]_block_invoke_2
+ ___33-[_NSTextRunStorage contentRange]_block_invoke_3
+ ___58-[__NSTextSelectionLineFragmentInfo _resolveTrailingEdges]_block_invoke
+ ___58-[__NSTextSelectionLineFragmentInfo _resolveTrailingEdges]_block_invoke.cold.1
+ ___58-[__NSTextSelectionLineFragmentInfo _resolveTrailingEdges]_block_invoke.cold.2
+ ___58-[__NSTextSelectionLineFragmentInfo _resolveTrailingEdges]_block_invoke_2
+ ___95-[NSTextLineFragment enumerateTextSegmentBoundsInTextRange:dataSourceLocationsOnly:usingBlock:]_block_invoke
+ _____NSTextContentStorageCacheElementIndexRange_block_invoke_2
+ _____NSTextContentStorageCacheElementIndexRange_block_invoke_3
+ _____NSTextContentStorageGetTextElementAtIndex_block_invoke_2
+ ___block_descriptor_40_e8_32o_e44_"<NSTextLocation>"16?0"<NSTextLocation>"8ls32l8
+ ___block_descriptor_40_e8_32r_e21_v32?0^{?=}8q16^B24lr32l8
+ ___block_descriptor_48_e18_"NSString"16?08l
+ ___block_descriptor_48_e8_32o40o_e50_v32?0"NSTextLayoutFragment"8"NSTextRange"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32o40r_e27_v16?0"_NSTextRunStorage"8ls32l8r40l8
+ ___block_descriptor_55_e8_32o40b_e107_B80?0"NSTextLineFragment"8"NSTextRange"16"NSTextRange"24{CGPoint=dd}32q48B56B60"NSTextContainer"64^d72ls40l8s32l8
+ ___block_descriptor_56_e8_32o40o48o_e50_v32?0"NSTextLayoutFragment"8"NSTextRange"16^B24ls32l8s40l8s48l8
+ ___block_literal_global.231
+ ___block_literal_global.234
+ ___block_literal_global.296
+ ___block_literal_global.308
+ ___block_literal_global.319
+ __unnamed_array_storage.130
+ _objc_msgSend$_resetLayoutFragmentFrame
+ _objc_msgSend$contentRange
+ _objc_msgSend$enumerateTextSegmentBoundsInTextRange:dataSourceLocationsOnly:usingBlock:
+ _objc_msgSend$sortUsingSelector:
- -[NSTextLineFragment enumerateTextSegmentBoundsInTextRange:usingBlock:]
- -[__NSTextSelectionLineFragmentInfo caretIndexForLocation:inTextRanges:secondaryCaretIndex:].cold.2
- -[__NSTextSelectionLineFragmentInfo caretIndexForLocation:inTextRanges:secondaryCaretIndex:].cold.3
- GCC_except_table111
- GCC_except_table15
- GCC_except_table56
- GCC_except_table81
- GCC_except_table88
- GCC_except_table91
- ___71-[NSTextLineFragment enumerateTextSegmentBoundsInTextRange:usingBlock:]_block_invoke
- ___77-[NSTextContentStorage enumerateTextElementsFromLocation:options:usingBlock:]_block_invoke
- ___block_descriptor_48_e8_32o40o_e34_v24?0"NSTextLayoutFragment"8^B16ls32l8s40l8
- ___block_descriptor_54_e8_32o40b_e107_B80?0"NSTextLineFragment"8"NSTextRange"16"NSTextRange"24{CGPoint=dd}32q48B56B60"NSTextContainer"64^d72ls40l8s32l8
- ___block_descriptor_56_e8_32o40o48o_e34_v24?0"NSTextLayoutFragment"8^B16ls32l8s40l8s48l8
- ___block_literal_global.115
- ___block_literal_global.205
- ___block_literal_global.223
- ___block_literal_global.227
- ___block_literal_global.230
- ___block_literal_global.303
- ___block_literal_global.322
- __unnamed_array_storage.126
- _objc_msgSend$enumerateTextSegmentBoundsInTextRange:usingBlock:
CStrings:
+ "%@: Requested to instantiate a new text element while textStorage being edited."
+ "-[__NSTextSelectionLineFragmentInfo _resolveTrailingEdges]"
+ "-[__NSTextSelectionLineFragmentInfo _resolveTrailingEdges]_block_invoke"
+ "@\"<NSTextLocation>\"16@?0@\"<NSTextLocation>\"8"
+ "NULL != _carets"
+ "T@\"NSTextRange\",R,&"
+ "_resetLayoutFragmentFrame"
+ "contentRange"
+ "enumerateTextSegmentBoundsInTextRange:dataSourceLocationsOnly:usingBlock:"
+ "index != NSNotFound"
+ "index < leadingEdges.count"
+ "sortUsingSelector:"
- "%@: Requested to enumerate while textStorage being edited."
- "NSTextContentManager.m"
- "[primaryCaret->primaryLocation compare:location] == NSOrderedSame"
- "[secondaryCaret->secondaryLocation compare:location] == NSOrderedSame"
- "enumerateTextSegmentBoundsInTextRange:usingBlock:"
- "void __NSTextContentStorageCacheElementIndexRange(NSTextContentStorage *, NSRange, const NSTextElement **, NSInteger)"

```
