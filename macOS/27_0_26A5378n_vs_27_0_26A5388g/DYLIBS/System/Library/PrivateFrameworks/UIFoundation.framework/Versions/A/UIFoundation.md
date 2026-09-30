## UIFoundation

> `/System/Library/PrivateFrameworks/UIFoundation.framework/Versions/A/UIFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__dof_UIFoundat`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1053.0.0.0.0
-  __TEXT.__text: 0x145904
+1054.0.0.0.0
+  __TEXT.__text: 0x145a50
   __TEXT.__objc_methlist: 0xd10c
-  __TEXT.__const: 0x12e4
-  __TEXT.__cstring: 0x17397
+  __TEXT.__const: 0x12f4
+  __TEXT.__cstring: 0x173fa
   __TEXT.__ustring: 0x31a
-  __TEXT.__gcc_except_tab: 0x3784
+  __TEXT.__gcc_except_tab: 0x3788
   __TEXT.__oslogstring: 0xb
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__dof_UIFoundat: 0x2bd
-  __TEXT.__unwind_info: 0x46f0
+  __TEXT.__unwind_info: 0x46f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0xa8
   __DATA_CONST.__got: 0xad8
-  __AUTH_CONST.__const: 0x4718
-  __AUTH_CONST.__cfstring: 0x10700
-  __AUTH_CONST.__objc_const: 0x14e68
+  __AUTH_CONST.__const: 0x47a8
+  __AUTH_CONST.__cfstring: 0x10740
+  __AUTH_CONST.__objc_const: 0x14e88
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0xa0

   __AUTH_CONST.__auth_got: 0x13e0
   __AUTH.__objc_data: 0x1630
   __AUTH.__data: 0x1d0
-  __DATA.__objc_ivar: 0x1608
+  __DATA.__objc_ivar: 0x160c
   __DATA.__data: 0x1370
-  __DATA.__bss: 0xb58
+  __DATA.__bss: 0xb30
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1a90
   __DATA_DIRTY.__data: 0x459
-  __DATA_DIRTY.__bss: 0xa78
+  __DATA_DIRTY.__bss: 0xa98
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 6119
-  Symbols:   13693
-  CStrings:  3976
+  Functions: 6122
+  Symbols:   13701
+  CStrings:  3978
 
Symbols:
+ +[NSRTFReader maximumNestedGroups]
+ OBJC_IVAR_$_NSRTFReader._maximumNestedGroups
+ ___34+[NSRTFReader maximumNestedGroups]_block_invoke
+ ___41-[NSWritingToolsEditTracker adjustRange:]_block_invoke
+ ___43-[NSRTFReader attributedStringToEndOfGroup]_block_invoke
+ ___45-[NSWritingToolsEditTracker _adjustLocation:]_block_invoke
+ ___block_descriptor_40_e8_32o_e18_"NSString"16?08l
+ maximumNestedGroups._maximumNestedGroups
+ maximumNestedGroups.onceToken
- GCC_except_table17
CStrings:
+ "Encountered an RTF document with groups nested beyond the limit %ul"
+ "__NSDefaultMaximumNestedGroups"
```
