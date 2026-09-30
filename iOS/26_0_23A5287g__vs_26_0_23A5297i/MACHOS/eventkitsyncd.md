## eventkitsyncd

> `/usr/libexec/eventkitsyncd`

```diff

-413.0.0.0.0
-  __TEXT.__text: 0x6f550
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_stubs: 0xc200
+414.0.0.0.0
+  __TEXT.__text: 0x6f870
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__objc_stubs: 0xc220
   __TEXT.__objc_methlist: 0x7008
-  __TEXT.__cstring: 0x5769
-  __TEXT.__objc_methname: 0xef04
+  __TEXT.__cstring: 0x576e
+  __TEXT.__objc_methname: 0xef13
   __TEXT.__objc_classname: 0x8e3
   __TEXT.__objc_methtype: 0x2339
   __TEXT.__const: 0x298
-  __TEXT.__oslogstring: 0xa844
+  __TEXT.__oslogstring: 0xa949
   __TEXT.__gcc_except_tab: 0x988
-  __TEXT.__unwind_info: 0x1550
-  __DATA_CONST.__auth_got: 0x698
+  __TEXT.__unwind_info: 0x1560
+  __DATA_CONST.__auth_got: 0x6a0
   __DATA_CONST.__got: 0x408
   __DATA_CONST.__const: 0x1738
   __DATA_CONST.__cfstring: 0x4960

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x50
   __DATA.__objc_const: 0xf688
-  __DATA.__objc_selrefs: 0x3ca8
+  __DATA.__objc_selrefs: 0x3cb0
   __DATA.__objc_ivar: 0x914
   __DATA.__objc_data: 0x1d10
   __DATA.__data: 0x800

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 8F50C5E6-6C30-33B7-B8ED-63EC614E6100
-  Functions: 2672
-  Symbols:   355
-  CStrings:  5198
+  UUID: 6059FE03-541F-3685-BD64-3980BBEBFDD4
+  Functions: 2675
+  Symbols:   356
+  CStrings:  5202
 
Symbols:
+ _sqlite3_get_autocommit
CStrings:
+ "%@: [%d] %s"
+ "== Started EventKitSync-414"
+ "ROLLBACK attempted without an active transaction (autocommit mode is on) for [%@]"
+ "ROLLBACK failed during an active transaction (autocommit mode is off) with errCode [%d] for [%@]"
+ "ROLLBACK succeeded during an active transaction (autocommit mode is off) for [%@]"
+ "pathComponents"
- "%@: %s"
- "== Started EventKitSync-413"

```
