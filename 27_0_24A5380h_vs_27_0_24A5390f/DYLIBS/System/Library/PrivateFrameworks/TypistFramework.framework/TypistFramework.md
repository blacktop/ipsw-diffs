## TypistFramework

> `/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-489.0.0.0.0
-  __TEXT.__text: 0x41fb4
-  __TEXT.__objc_methlist: 0x3814
+491.0.0.0.0
+  __TEXT.__text: 0x422a4
+  __TEXT.__objc_methlist: 0x382c
   __TEXT.__const: 0x3c2
-  __TEXT.__gcc_except_tab: 0xc40
-  __TEXT.__cstring: 0x5902
-  __TEXT.__ustring: 0x1366
+  __TEXT.__gcc_except_tab: 0xd1c
+  __TEXT.__cstring: 0x5922
+  __TEXT.__ustring: 0x1362
   __TEXT.__dlopen_cstrs: 0x6d
   __TEXT.__oslogstring: 0xc
   __TEXT.__swift5_typeref: 0xaa

   __TEXT.__swift5_fieldmd: 0x94
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0xe30
+  __TEXT.__unwind_info: 0xe40
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8d8
+  __DATA_CONST.__const: 0x8f8
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2468
+  __DATA_CONST.__objc_selrefs: 0x2480
   __DATA_CONST.__objc_superrefs: 0x120
-  __DATA_CONST.__objc_arraydata: 0x3c28
-  __DATA_CONST.__got: 0x530
+  __DATA_CONST.__objc_arraydata: 0x3c18
+  __DATA_CONST.__got: 0x538
   __AUTH_CONST.__const: 0x608
-  __AUTH_CONST.__cfstring: 0x115a0
-  __AUTH_CONST.__objc_const: 0x4a38
+  __AUTH_CONST.__cfstring: 0x11580
+  __AUTH_CONST.__objc_const: 0x4a68
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0xbb8
   __AUTH_CONST.__objc_arrayobj: 0x390

   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH.__objc_data: 0xdb8
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x2b0
+  __DATA.__objc_ivar: 0x2b4
   __DATA.__data: 0x1e8
   __DATA.__bss: 0x2f0
   __DATA.__common: 0x8

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 1308
-  Symbols:   3278
-  CStrings:  2275
+  Functions: 1312
+  Symbols:   3289
+  CStrings:  2274
 
Symbols:
+ +[TypistPathUtilities _getAdvanceWidthAndHeight:forCharacters:]
+ -[TYPathData advanceWidth]
+ -[TYPathData initWithArray:width:height:isCursive:advanceWidth:]
+ -[TYPathData setAdvanceWidth:]
+ GCC_except_table58
+ GCC_except_table63
+ GCC_except_table70
+ GCC_except_table74
+ GCC_except_table78
+ GCC_except_table85
+ GCC_except_table97
+ _OBJC_IVAR_$_TYPathData._advanceWidth
+ _TIUIKeyboardPersistentSplitProgressPreference
+ ___59+[TypistKeyboardDataInProcess generateKeyplaneSwitchTable:]_block_invoke_2
+ ___67+[TypistKeyboardDataInProcess generateKeyplaneSwitchTableFor10Key:]_block_invoke
+ ___block_descriptor_33_e5_v8?0l
+ _objc_msgSend$_getAdvanceWidthAndHeight:forCharacters:
+ _objc_msgSend$advanceWidth
+ _objc_msgSend$initWithArray:width:height:isCursive:advanceWidth:
+ _objc_msgSend$setAdvanceWidth:
+ _objc_msgSend$updateKeyboardIsSplit:locked:
- +[TypistPathUtilities _getWidthAndHeight:forCharacters:]
- -[TYPathData initWithArray:width:height:isCursive:]
- GCC_except_table61
- GCC_except_table64
- GCC_except_table72
- GCC_except_table76
- GCC_except_table83
- GCC_except_table89
- _objc_msgSend$_getWidthAndHeight:forCharacters:
- _objc_msgSend$initWithArray:width:height:isCursive:
CStrings:
+ "Changing Split Settings: Current=%@ Persistent=%@ ChangeTo=%@"
+ "SELECT pathData.pathData, pathData.width, pathData.height, characters.character, pathData.variant_id, pathData.isCursive, pathData.advances FROM pathData INNER JOIN characters ON characters.characterid = pathData.character_id"
- "Changing Split Settings: Current=%@ ChangeTo=%@"
- "SELECT pathData.pathData, pathData.width, pathData.height, characters.character, pathData.variant_id, pathData.isCursive FROM pathData INNER JOIN characters ON characters.characterid = pathData.character_id"
- "ฯ"
```
