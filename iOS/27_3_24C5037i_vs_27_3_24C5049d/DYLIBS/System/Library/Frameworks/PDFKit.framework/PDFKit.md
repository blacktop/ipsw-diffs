## PDFKit

> `/System/Library/Frameworks/PDFKit.framework/PDFKit`

```diff

-1537.2.2.0.0
-  __TEXT.__text: 0xbb930
-  __TEXT.__objc_methlist: 0xb0bc
+1537.2.4.0.0
+  __TEXT.__text: 0xbbe90
+  __TEXT.__objc_methlist: 0xb13c
   __TEXT.__const: 0x944
-  __TEXT.__cstring: 0x7384
-  __TEXT.__gcc_except_tab: 0x8010
+  __TEXT.__cstring: 0x7374
+  __TEXT.__gcc_except_tab: 0x8024
   __TEXT.__dlopen_cstrs: 0x201
   __TEXT.__ustring: 0xb4
   __TEXT.__oslogstring: 0x1a

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x4490
+  __TEXT.__unwind_info: 0x44b8
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2430
+  __DATA_CONST.__const: 0x2438
   __DATA_CONST.__objc_classlist: 0x408
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7168
+  __DATA_CONST.__objc_selrefs: 0x71a8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__got: 0xb08
-  __AUTH_CONST.__const: 0x9d8
+  __AUTH_CONST.__const: 0x9b8
   __AUTH_CONST.__cfstring: 0x7680
-  __AUTH_CONST.__objc_const: 0xf180
+  __AUTH_CONST.__objc_const: 0xf220
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x2e8

   __AUTH_CONST.__auth_got: 0x1798
   __AUTH.__objc_data: 0x2558
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0xc88
+  __DATA.__objc_ivar: 0xc9c
   __DATA.__data: 0x13d0
   __DATA_DIRTY.__objc_data: 0x2a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3774
-  Symbols:   7477
+  Functions: 3784
+  Symbols:   7495
   CStrings:  1273
 
Symbols:
+ +[PDFPage _shouldRenderDarkModeInContext:withOptions:]
+ -[PDFAnnotation _acroFormDictionaryForPage:]
+ -[PDFAnnotation _colorWithComponents:inColorSpaceNamed:]
+ -[PDFAnnotation _getInheritedDefaultAppearanceString:fromDictionary:forPage:]
+ -[PDFAnnotation addDefaultPopup]
+ -[PDFAnnotation prefersAppearanceStream]
+ -[PDFDocument appearanceStyle]
+ -[PDFDocument setAppearanceStyle:]
+ -[PDFPage _createDisplayListAsynchronouslyForDarkMode:generation:]
+ -[PDFPage _createDisplayListTrackingGlyphs:darkMode:]
+ -[PDFPage _drawOptionsForThumbnail:]
+ -[PDFPage _installDisplayList:forDarkMode:]
+ -[PDFPage _startCreatingDisplayListForDarkMode:]
+ -[PDFPage copyDisplayListForDarkMode:]
+ -[PDFPage requestDisplayListForDarkMode:]
+ GCC_except_table102
+ GCC_except_table105
+ GCC_except_table115
+ GCC_except_table133
+ GCC_except_table135
+ GCC_except_table136
+ GCC_except_table139
+ GCC_except_table140
+ GCC_except_table166
+ GCC_except_table175
+ GCC_except_table191
+ GCC_except_table192
+ GCC_except_table193
+ GCC_except_table201
+ GCC_except_table209
+ GCC_except_table219
+ GCC_except_table220
+ GCC_except_table224
+ GCC_except_table225
+ GCC_except_table229
+ GCC_except_table230
+ GCC_except_table231
+ GCC_except_table333
+ GCC_except_table339
+ GCC_except_table71
+ GCC_except_table75
+ GCC_except_table76
+ GCC_except_table85
+ GCC_except_table86
+ _OBJC_IVAR_$_PDFAnnotation._appearanceStreamStringValue
+ _OBJC_IVAR_$_PDFAnnotation._formNeedsAppearances
+ _OBJC_IVAR_$_PDFPage._creatingDisplayListIsDarkMode
+ _OBJC_IVAR_$_PDFPage._displayListGeneration
+ _OBJC_IVAR_$_PDFPage._displayListIsDarkMode
+ _OBJC_IVAR_$_PDFPage._displayListRequestedForOtherMode
+ ___48-[PDFPage _startCreatingDisplayListForDarkMode:]_block_invoke
+ ___block_descriptor_49_ea8_32w_e5_v8?0lw32l8
+ _kCGColorSpaceSRGB
+ _os_unfair_recursive_lock_lock
- -[PDFPage _createDisplayListTrackingGlyphs:]
- -[PDFPage _createRetainedDisplayList]
- -[PDFPage copyDisplayList]
- -[PDFPage getDisplayListWithCompletion:onQueue:]
- GCC_except_table104
- GCC_except_table107
- GCC_except_table117
- GCC_except_table130
- GCC_except_table134
- GCC_except_table138
- GCC_except_table142
- GCC_except_table148
- GCC_except_table149
- GCC_except_table151
- GCC_except_table172
- GCC_except_table178
- GCC_except_table187
- GCC_except_table195
- GCC_except_table196
- GCC_except_table197
- GCC_except_table204
- GCC_except_table212
- GCC_except_table213
- GCC_except_table222
- GCC_except_table226
- GCC_except_table227
- GCC_except_table228
- GCC_except_table328
- GCC_except_table334
- GCC_except_table90
- _OBJC_IVAR_$_PDFPage._createDisplayListCompletionBlocks
- ___37-[PDFPage _createRetainedDisplayList]_block_invoke
- ___48-[PDFPage getDisplayListWithCompletion:onQueue:]_block_invoke
- ___block_descriptor_32_e34_v32?0"PDFBlockQueuePair"8Q16^B24l
- _kCGColorSpaceGenericRGB
- _os_unfair_recursive_lock_lock_with_options
CStrings:
+ "NeedAppearances"
- "v32@?0@\"PDFBlockQueuePair\"8Q16^B24"
```
