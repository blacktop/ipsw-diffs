## fontd

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/Current/Frameworks/ATS.framework/Versions/A/Support/fontd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-424.0.0.0.0
-  __TEXT.__text: 0x36d30
-  __TEXT.__auth_stubs: 0x14a0
+425.0.0.0.0
+  __TEXT.__text: 0x37a40
+  __TEXT.__auth_stubs: 0x14b0
   __TEXT.__objc_stubs: 0xe60
   __TEXT.__objc_methlist: 0x608
-  __TEXT.__gcc_except_tab: 0x5870
-  __TEXT.__const: 0x7b8
-  __TEXT.__cstring: 0x7a60
+  __TEXT.__gcc_except_tab: 0x59cc
+  __TEXT.__const: 0x7d0
+  __TEXT.__cstring: 0x7f78
   __TEXT.__objc_classname: 0xac
   __TEXT.__objc_methname: 0x10b9
   __TEXT.__objc_methtype: 0x8af
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x1c60
-  __DATA_CONST.__const: 0x4430
-  __DATA_CONST.__cfstring: 0x2680
+  __TEXT.__unwind_info: 0x1ca8
+  __DATA_CONST.__const: 0x4460
+  __DATA_CONST.__cfstring: 0x26e0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__auth_got: 0xa68
+  __DATA_CONST.__auth_got: 0xa70
   __DATA_CONST.__got: 0x250
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x5f8
   __DATA.__objc_selrefs: 0x568
   __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x710
+  __DATA.__data: 0x738
   __DATA.__bss: 0x268
   __DATA.__common: 0x71
   __RESTRICT.__restrict: 0x0

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 997
-  Symbols:   418
-  CStrings:  813
+  Functions: 1007
+  Symbols:   419
+  CStrings:  821
 
Symbols:
+ _sqlite3_changes
CStrings:
+ "DELETE FROM bookmarks_table WHERE bookmark_ref_column >= ?1 AND (bookmark_flags_column & 1) == 0 AND NOT EXISTS ( SELECT 1 FROM font_table WHERE font_table.bookmark_ref_column == bookmarks_table.bookmark_ref_column ) AND NOT EXISTS ( SELECT 1 FROM lwfn_table WHERE lwfn_table.bookmark_ref_column == bookmarks_table.bookmark_ref_column );"
+ "DELETE FROM charset_table WHERE charsetref_column >= ?1 AND NOT EXISTS ( SELECT 1 FROM font_table WHERE font_table.charsetref_column == charset_table.charsetref_column );"
+ "DELETE FROM languagecodes_table WHERE languagecodesref_column >= ?1 AND languagecodesref_column NOT IN ( SELECT supportedlanguagecodes_column FROM font_table WHERE supportedlanguagecodes_column >= ?1 UNION SELECT designlanguagecodes_column FROM font_table WHERE designlanguagecodes_column >= ?1 );"
+ "UPDATE bookmarks_table SET dir_column = ?1 WHERE dir_column = 0 AND bookmark_ref_column IN ( SELECT bookmark_ref_column FROM font_table WHERE dir_column = 0 AND instr(path_column, ?2) == 1 );"
+ "UPDATE font_table SET dir_column = ?1 WHERE dir_column = 0 AND instr(path_column, ?2) == 1;"
+ "XType: adopted %zu orphaned font rows into directory %u"
+ "XType: could not register the directory for domain %u before registering fonts in it"
+ "XType: registered font directory %@ ahead of a client font registration"
```
