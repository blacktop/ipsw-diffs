## geoanalyticsd

> `/System/Library/PrivateFrameworks/GeoAnalytics.framework/geoanalyticsd`

```diff

-1986.32.8.22.11
-  __TEXT.__text: 0x183c0
+1986.32.8.22.14
+  __TEXT.__text: 0x183b8
   __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_stubs: 0x31c0
+  __TEXT.__objc_stubs: 0x3200
   __TEXT.__objc_methlist: 0x884
   __TEXT.__const: 0x108
   __TEXT.__gcc_except_tab: 0x448
-  __TEXT.__cstring: 0x38b4
+  __TEXT.__cstring: 0x38c9
   __TEXT.__oslogstring: 0x11f1
   __TEXT.__objc_classname: 0x22d
-  __TEXT.__objc_methname: 0x2ca5
+  __TEXT.__objc_methname: 0x2cee
   __TEXT.__objc_methtype: 0xabc
   __TEXT.__unwind_info: 0x648
   __DATA_CONST.__auth_got: 0x408

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x2798
-  __DATA.__objc_selrefs: 0xce8
+  __DATA.__objc_selrefs: 0xcf8
   __DATA.__objc_ivar: 0xc4
   __DATA.__objc_data: 0x500
   __DATA.__data: 0x300

   - /usr/lib/libsqlite3.dylib
   Functions: 390
   Symbols:   234
-  CStrings:  1285
+  CStrings:  1287
 
CStrings:
+ "INSERT INTO shadow (analytic,COL_TYPE,createtime) VALUES ( @analytic,@type, DATETIME( @createtime, 'UNIXEPOCH', 'SUBSEC'))"
+ "SELECT analytic,COL_TYPE, strftime('%!s(MISSING)',createtime, 'SUBSEC' ) FROM shadow;"
+ "bindRealParameter:toValue:inStatement:error:"
+ "doubleForColumn:inStatment:"
- "INSERT INTO shadow (analytic,COL_TYPE,createtime) VALUES ( @analytic,@type, DATETIME( @createtime, 'UNIXEPOCH'))"
- "SELECT analytic,COL_TYPE, strftime('%!s(MISSING)',createtime) FROM shadow;"

```
