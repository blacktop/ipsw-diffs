## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput`

```diff

-423.0.0.0.0
-  __TEXT.__text: 0x6ff90
+424.2.0.0.0
+  __TEXT.__text: 0x70724
   __TEXT.__auth_stubs: 0x1930
-  __TEXT.__objc_methlist: 0x6d4c
+  __TEXT.__objc_methlist: 0x6dec
   __TEXT.__gcc_except_tab: 0x1898
   __TEXT.__const: 0x908
-  __TEXT.__cstring: 0x5958
+  __TEXT.__cstring: 0x59a8
   __TEXT.__oslogstring: 0x1f5b
   __TEXT.__ustring: 0x96
   __TEXT.__swift5_typeref: 0x39a

   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1e90
+  __TEXT.__unwind_info: 0x1e98
   __TEXT.__eh_frame: 0x678
-  __TEXT.__objc_classname: 0xa9c
-  __TEXT.__objc_methname: 0xf7a7
-  __TEXT.__objc_methtype: 0x2257
-  __TEXT.__objc_stubs: 0xd460
+  __TEXT.__objc_classname: 0xab8
+  __TEXT.__objc_methname: 0xf968
+  __TEXT.__objc_methtype: 0x2293
+  __TEXT.__objc_stubs: 0xd600
   __DATA_CONST.__got: 0x578
-  __DATA_CONST.__const: 0xc58
-  __DATA_CONST.__objc_classlist: 0x2a0
+  __DATA_CONST.__const: 0xc78
+  __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e00
+  __DATA_CONST.__objc_selrefs: 0x3e70
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x380
   __AUTH_CONST.__auth_got: 0xca8
-  __AUTH_CONST.__const: 0x18b0
-  __AUTH_CONST.__cfstring: 0x5120
-  __AUTH_CONST.__objc_const: 0xed98
+  __AUTH_CONST.__const: 0x18f0
+  __AUTH_CONST.__cfstring: 0x5140
+  __AUTH_CONST.__objc_const: 0xf010
   __AUTH_CONST.__objc_intobj: 0x9c0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xbd0
+  __AUTH.__objc_data: 0xc20
   __AUTH.__data: 0x5b8
-  __DATA.__objc_ivar: 0x838
-  __DATA.__data: 0x1028
+  __DATA.__objc_ivar: 0x844
+  __DATA.__data: 0x1030
   __DATA.__common: 0x28
   __DATA.__bss: 0x7c8
   __DATA_DIRTY.__objc_data: 0xe10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F7FAF406-936E-30B6-AF03-088A32534C42
-  Functions: 2830
-  Symbols:   9094
-  CStrings:  4724
+  UUID: 08C5794C-FFFC-39D4-BFF2-F050B417BFE2
+  Functions: 2841
+  Symbols:   9143
+  CStrings:  4748
 
Symbols:
+ +[SCROSharedInputProperties sharedInstance]
+ +[SCROSharedInputProperties sharedInstance].cold.1
+ -[SCRO2DBrailleImageContent multiLineBraille]
+ -[SCRO2DBrailleListContent initWithBrailleData:width:height:wordWrap:]
+ -[SCRO2DBrailleListContent multiLineBraille]
+ -[SCRO2DBraillePlane _isPlanarCapable]
+ -[SCRO2DBraillePlane createContentWithBrailleData:width:height:canvas:]
+ -[SCRO2DBraillePlane refresh]
+ -[SCRO2DBrailleReadingContent initWithBrailleData:width:height:wordWrap:]
+ -[SCRO2DBrailleReadingContent multiLineBraille]
+ -[SCRO2DBrailleReadingContent multiLineBraille].cold.1
+ -[SCROBrailleDisplay isMultiLine]
+ -[SCROBrailleUIListItem initWithIdentifier:label:prepopulatedBraille:shouldBulkSelect:]
+ -[SCROBrailleUIListItem shouldBulkSelectPrepopulatedBraille]
+ -[SCROSharedInputProperties lastBrailleChordPosted]
+ -[SCROSharedInputProperties setLastBrailleChordPosted:]
+ GCC_except_table114
+ GCC_except_table116
+ GCC_except_table136
+ GCC_except_table146
+ GCC_except_table150
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table170
+ GCC_except_table172
+ GCC_except_table183
+ GCC_except_table204
+ GCC_except_table255
+ _OBJC_CLASS_$_SCROSharedInputProperties
+ _OBJC_IVAR_$_SCRO2DBraillePlane._shouldUseMultiRow
+ _OBJC_IVAR_$_SCROBrailleLine._shouldUseMultiRow
+ _OBJC_IVAR_$_SCROBrailleUIListItem._shouldBulkSelectPrepopulatedBraille
+ _OBJC_IVAR_$_SCROSharedInputProperties._lastBrailleChordPosted
+ _OBJC_METACLASS_$_SCROSharedInputProperties
+ __OBJC_$_CLASS_METHODS_SCROSharedInputProperties
+ __OBJC_$_INSTANCE_METHODS_SCROSharedInputProperties
+ __OBJC_$_INSTANCE_VARIABLES_SCROSharedInputProperties
+ __OBJC_$_PROP_LIST_SCROSharedInputProperties
+ __OBJC_CLASS_RO_$_SCROSharedInputProperties
+ __OBJC_METACLASS_RO_$_SCROSharedInputProperties
+ ___43+[SCROSharedInputProperties sharedInstance]_block_invoke
+ ___68-[SCROBrailleUIFinderApp _fileItemsInURL:directoriesOnly:excluding:]_block_invoke
+ ___block_descriptor_32_e57_q24?0"SCROBrailleUIListItem"8"SCROBrailleUIListItem"16l
+ ___block_literal_global.105
+ ___block_literal_global.109
+ _kSCROBrailleDisplayIsMultiLine
+ _objc_msgSend$_isPlanarCapable
+ _objc_msgSend$createContentWithBrailleData:width:height:canvas:
+ _objc_msgSend$handleMoveCursorLeft
+ _objc_msgSend$handleMoveCursorRight
+ _objc_msgSend$initWithBrailleData:width:height:wordWrap:
+ _objc_msgSend$initWithIdentifier:label:prepopulatedBraille:shouldBulkSelect:
+ _objc_msgSend$localizedCaseInsensitiveCompare:
+ _objc_msgSend$multiLineBraille
+ _objc_msgSend$refresh
+ _objc_msgSend$rowCount
+ _objc_msgSend$rowSize
+ _objc_msgSend$setMainCellsArray:
+ _objc_msgSend$shouldBulkSelectPrepopulatedBraille
+ _objc_msgSend$shouldUseMultiRow
+ _objc_msgSend$sortUsingComparator:
- +[SCROBrailleDisplayInput sharedInstance]
- -[SCRO2DBrailleListContent initWithBrailleData:canvas:wordWrap:]
- -[SCRO2DBrailleReadingContent drawOnCanvas:].cold.1
- -[SCRO2DBrailleReadingContent initWithBrailleData:canvas:wordWrap:]
- -[SCROBrailleDisplayInput lastBrailleChordPosted]
- -[SCROBrailleDisplayInput setLastBrailleChordPosted:]
- GCC_except_table112
- GCC_except_table115
- GCC_except_table135
- GCC_except_table145
- GCC_except_table148
- GCC_except_table152
- GCC_except_table154
- GCC_except_table169
- GCC_except_table171
- GCC_except_table181
- GCC_except_table202
- GCC_except_table254
- _OBJC_IVAR_$_SCROBrailleDisplayInput._lastBrailleChordPosted
- __OBJC_$_CLASS_METHODS_SCROBrailleDisplayInput
- ___41+[SCROBrailleDisplayInput sharedInstance]_block_invoke
- ___block_literal_global.106
- _objc_msgSend$initWithBrailleData:canvas:wordWrap:
- _objc_msgSend$numberOfCellsInRowAvailable
CStrings:
+ "@44@0:8@16@24@32B40"
+ "@44@0:8@16q24q32B40"
+ "@48@0:8@16q24q32@40"
+ "BrailleDisplayIsMultiLine"
+ "SCROSharedInputProperties"
+ "TB,R,N,V_shouldBulkSelectPrepopulatedBraille"
+ "_isPlanarCapable"
+ "_shouldBulkSelectPrepopulatedBraille"
+ "_shouldUseMultiRow"
+ "createContentWithBrailleData:width:height:canvas:"
+ "handleMoveCursorLeft"
+ "handleMoveCursorRight"
+ "initWithBrailleData:width:height:wordWrap:"
+ "initWithIdentifier:label:prepopulatedBraille:shouldBulkSelect:"
+ "localizedCaseInsensitiveCompare:"
+ "multiLineBraille"
+ "q24@?0@\"SCROBrailleUIListItem\"8@\"SCROBrailleUIListItem\"16"
+ "refresh"
+ "rowCount"
+ "rowSize"
+ "setMainCellsArray:"
+ "shouldBulkSelectPrepopulatedBraille"
+ "shouldUseMultiRow"
+ "sortUsingComparator:"
+ "\xf0\xf0\xf1"
- "initWithBrailleData:canvas:wordWrap:"
- "\xf0\xf0\xe1"

```
