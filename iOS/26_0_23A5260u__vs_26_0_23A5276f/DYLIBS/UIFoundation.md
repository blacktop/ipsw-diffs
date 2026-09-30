## UIFoundation

> `/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation`

```diff

-1005.0.0.0.0
-  __TEXT.__text: 0x104e70
+1008.0.0.0.0
+  __TEXT.__text: 0x105410
   __TEXT.__auth_stubs: 0x25c0
-  __TEXT.__objc_methlist: 0xba4c
+  __TEXT.__objc_methlist: 0xbaa4
   __TEXT.__const: 0x73c
-  __TEXT.__cstring: 0xff49
-  __TEXT.__gcc_except_tab: 0x3408
+  __TEXT.__cstring: 0xff0d
+  __TEXT.__gcc_except_tab: 0x3428
   __TEXT.__ustring: 0x2b4
   __TEXT.__oslogstring: 0xb
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__dof_UIFoundat: 0x2bd
-  __TEXT.__unwind_info: 0x3c20
-  __TEXT.__objc_classname: 0x1291
-  __TEXT.__objc_methname: 0x1fc06
-  __TEXT.__objc_methtype: 0x86fa
-  __TEXT.__objc_stubs: 0x14a80
+  __TEXT.__unwind_info: 0x3c38
+  __TEXT.__objc_classname: 0x1294
+  __TEXT.__objc_methname: 0x1fed4
+  __TEXT.__objc_methtype: 0x8724
+  __TEXT.__objc_stubs: 0x14b40
   __DATA_CONST.__got: 0x8b0
-  __DATA_CONST.__const: 0x9038
+  __DATA_CONST.__const: 0x9010
   __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6848
+  __DATA_CONST.__objc_selrefs: 0x6890
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x12f0
   __AUTH_CONST.__const: 0x1268
-  __AUTH_CONST.__cfstring: 0xc900
-  __AUTH_CONST.__objc_const: 0x12758
+  __AUTH_CONST.__cfstring: 0xc8e0
+  __AUTH_CONST.__objc_const: 0x12818
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x1298
   __AUTH.__data: 0xb0
-  __DATA.__objc_ivar: 0x12e4
+  __DATA.__objc_ivar: 0x12f8
   __DATA.__data: 0xed8
   __DATA.__bss: 0x818
   __DATA_DIRTY.__objc_data: 0x1a18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FD090560-0C1A-32EE-9F20-713C74A4D7E1
-  Functions: 5249
-  Symbols:   17887
-  CStrings:  10590
+  UUID: 2EFB0CB8-FEBB-317E-821F-0D0498DA3337
+  Functions: 5254
+  Symbols:   17908
+  CStrings:  10604
 
Symbols:
+ -[NSTextLayoutManager _delegateCanSendViewProviderInvalidationNotification]
+ -[NSTextLayoutManager _platformDelegateCanSendViewProviderInvalidationNotification]
+ -[NSTextLayoutManager platformDelegate]
+ -[NSTextLayoutManager setPlatformDelegate:]
+ -[NSTextSelectionNavigation _isVisuallyContiguousNavigation]
+ -[NSTextSelectionNavigation _mergeVisuallyContiguousRanges:withRanges:]
+ -[NSTextSelectionNavigation initWithDataSource:].cold.1
+ -[NSTextSelectionNavigation prefersVisuallyContiguousNavigation]
+ -[NSTextSelectionNavigation setPrefersVisuallyContiguousNavigation:]
+ -[__NSTextSelectionLineFragmentInfo rangesBetweenStartingOffset:endOffset:logicallyContinuous:]
+ GCC_except_table103
+ GCC_except_table106
+ GCC_except_table126
+ GCC_except_table127
+ GCC_except_table136
+ GCC_except_table139
+ GCC_except_table146
+ GCC_except_table149
+ GCC_except_table170
+ GCC_except_table179
+ GCC_except_table193
+ GCC_except_table196
+ GCC_except_table205
+ GCC_except_table212
+ GCC_except_table215
+ GCC_except_table216
+ GCC_except_table219
+ GCC_except_table228
+ GCC_except_table243
+ GCC_except_table244
+ GCC_except_table245
+ GCC_except_table252
+ GCC_except_table258
+ GCC_except_table259
+ GCC_except_table260
+ GCC_except_table65
+ GCC_except_table76
+ GCC_except_table77
+ _OBJC_IVAR_$_NSTextLayoutManager._platformDelegate
+ _OBJC_IVAR_$_NSTextLayoutManager._platformDelegateWithCachedViewProviderForTextAttachment
+ _OBJC_IVAR_$_NSTextLayoutManager._platformDelegateWithViewProviderInvalidationNotification
+ _OBJC_IVAR_$_NSTextSelectionNavigation._prefersVisuallyContiguousNavigation
+ _OBJC_IVAR_$___NSTextSelectionLineFragmentInfo._lastCaretPrefersSecondaryLocation
+ ___95-[__NSTextSelectionLineFragmentInfo rangesBetweenStartingOffset:endOffset:logicallyContinuous:]_block_invoke
+ ___block_literal_global.121
+ ___block_literal_global.143
+ ___block_literal_global.154
+ ___block_literal_global.156
+ ___block_literal_global.173
+ ___block_literal_global.180
+ ___block_literal_global.195
+ ___block_literal_global.198
+ ___block_literal_global.222
+ ___block_literal_global.235
+ ___block_literal_global.241
+ ___block_literal_global.621
+ ___block_literal_global.623
+ _objc_msgSend$_delegateCanSendViewProviderInvalidationNotification
+ _objc_msgSend$_isVisuallyContiguousNavigation
+ _objc_msgSend$_mergeVisuallyContiguousRanges:withRanges:
+ _objc_msgSend$_platformDelegateCanSendViewProviderInvalidationNotification
+ _objc_msgSend$platformDelegate
+ _objc_msgSend$platformDelegateForTextLayoutManager:cachedTextAttachmentViewProviderForTextAttachment:
+ _objc_msgSend$platformDelegateForTextLayoutManager:willInvalidateTextAttachmentViewProvider:forTextAttachment:
+ _objc_msgSend$rangesBetweenStartingOffset:endOffset:logicallyContinuous:
- +[NSTextRange combineTextRanges:withTextRanges:usingOperator:].cold.5
- -[NSTextSelectionNavigation _usesVisualBidiSelection]
- -[NSTextSelectionNavigation _usesVisualBidiSelection].cold.1
- -[__NSTextSelectionLineFragmentInfo rangesBetweenStartingOffset:endOffset:continuous:]
- GCC_except_table113
- GCC_except_table118
- GCC_except_table125
- GCC_except_table134
- GCC_except_table137
- GCC_except_table144
- GCC_except_table147
- GCC_except_table148
- GCC_except_table168
- GCC_except_table171
- GCC_except_table190
- GCC_except_table191
- GCC_except_table199
- GCC_except_table210
- GCC_except_table213
- GCC_except_table214
- GCC_except_table217
- GCC_except_table226
- GCC_except_table239
- GCC_except_table240
- GCC_except_table241
- GCC_except_table248
- GCC_except_table254
- GCC_except_table255
- GCC_except_table256
- GCC_except_table48
- GCC_except_table95
- GCC_except_table96
- ___125-[NSTextSelectionNavigation _rangesForSelectionStartingOffset:inLineFragmentInfo:endingOffset:inLineFragmentInfo:contiguous:]_block_invoke_2
- ___86-[__NSTextSelectionLineFragmentInfo rangesBetweenStartingOffset:endOffset:continuous:]_block_invoke
- ___block_descriptor_56_e8_32o40o48o_e18_"NSString"16?08ls32l8s40l8s48l8
- ___block_literal_global.139
- ___block_literal_global.150
- ___block_literal_global.152
- ___block_literal_global.169
- ___block_literal_global.176
- ___block_literal_global.191
- ___block_literal_global.194
- ___block_literal_global.213
- ___block_literal_global.218
- ___block_literal_global.231
- ___block_literal_global.237
- ___block_literal_global.240
- ___block_literal_global.609
- ___block_literal_global.611
- _objc_msgSend$_usesVisualBidiSelection
- _objc_msgSend$rangesBetweenStartingOffset:endOffset:continuous:
CStrings:
+ "@\"<_NSTextLayoutManagerPlatformDelegate>\""
+ "TB,V_prefersVisuallyContiguousNavigation"
+ "_delegateCanSendViewProviderInvalidationNotification"
+ "_isVisuallyContiguousNavigation"
+ "_lastCaretPrefersSecondaryLocation"
+ "_mergeVisuallyContiguousRanges:withRanges:"
+ "_platformDelegate"
+ "_platformDelegateCanSendViewProviderInvalidationNotification"
+ "_platformDelegateWithCachedViewProviderForTextAttachment"
+ "_platformDelegateWithViewProviderInvalidationNotification"
+ "_prefersVisuallyContiguousNavigation"
+ "platformDelegate"
+ "platformDelegateForTextLayoutManager:cachedTextAttachmentViewProviderForTextAttachment:"
+ "platformDelegateForTextLayoutManager:willInvalidateTextAttachmentViewProvider:forTextAttachment:"
+ "prefersVisuallyContiguousNavigation"
+ "rangesBetweenStartingOffset:endOffset:logicallyContinuous:"
+ "setPlatformDelegate:"
+ "setPrefersVisuallyContiguousNavigation:"
- "Reverse ordering in locations found. %@:%@ documentRange:%@"
- "_usesVisualBidiSelection"
- "rangesBetweenStartingOffset:endOffset:continuous:"

```
