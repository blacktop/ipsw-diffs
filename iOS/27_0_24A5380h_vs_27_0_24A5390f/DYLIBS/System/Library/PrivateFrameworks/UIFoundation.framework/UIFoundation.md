## UIFoundation

> `/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__dof_UIFoundat`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1053.0.0.0.0
-  __TEXT.__text: 0x109048
+1054.0.0.0.0
+  __TEXT.__text: 0x109194
   __TEXT.__objc_methlist: 0xbb9c
   __TEXT.__const: 0x76c
-  __TEXT.__gcc_except_tab: 0x350c
-  __TEXT.__cstring: 0x1021d
+  __TEXT.__gcc_except_tab: 0x3510
+  __TEXT.__cstring: 0x10280
   __TEXT.__ustring: 0x2b4
   __TEXT.__oslogstring: 0xb
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__dof_UIFoundat: 0x2bd
-  __TEXT.__unwind_info: 0x3fc8
+  __TEXT.__unwind_info: 0x3fd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x91f8
+  __DATA_CONST.__const: 0x9220
   __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_arraydata: 0xa8
   __DATA_CONST.__got: 0x8c0
-  __AUTH_CONST.__const: 0x1278
-  __AUTH_CONST.__cfstring: 0xca80
-  __AUTH_CONST.__objc_const: 0x12b00
+  __AUTH_CONST.__const: 0x12d8
+  __AUTH_CONST.__cfstring: 0xcac0
+  __AUTH_CONST.__objc_const: 0x12b20
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x18

   __AUTH_CONST.__auth_got: 0x12e0
   __AUTH.__objc_data: 0x12c0
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x1318
-  __DATA.__data: 0xe19
-  __DATA.__bss: 0x818
+  __DATA.__objc_ivar: 0x131c
+  __DATA.__data: 0xe21
+  __DATA.__bss: 0x820
   __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__data: 0x81
   __DATA_DIRTY.__bss: 0x9c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5349
-  Symbols:   11976
-  CStrings:  3217
+  Functions: 5352
+  Symbols:   11986
+  CStrings:  3219
 
Symbols:
+ +[NSRTFReader maximumNestedGroups]
+ GCC_except_table87
+ _OBJC_IVAR_$_NSRTFReader._maximumNestedGroups
+ ___34+[NSRTFReader maximumNestedGroups]_block_invoke
+ ___41-[NSWritingToolsEditTracker adjustRange:]_block_invoke
+ ___43-[NSRTFReader attributedStringToEndOfGroup]_block_invoke
+ ___45-[NSWritingToolsEditTracker _adjustLocation:]_block_invoke
+ ___block_descriptor_40_e8_32o_e18_"NSString"16?08ls32l8
+ _maximumNestedGroups._maximumNestedGroups
+ _maximumNestedGroups.onceToken
CStrings:
+ "Encountered an RTF document with groups nested beyond the limit %ul"
+ "__NSDefaultMaximumNestedGroups"
```
