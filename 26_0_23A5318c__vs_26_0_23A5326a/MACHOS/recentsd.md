## recentsd

> `/System/Library/PrivateFrameworks/CoreRecents.framework/recentsd`

```diff

-1228.100.1.0.0
-  __TEXT.__text: 0x17e18
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_stubs: 0x3f60
-  __TEXT.__objc_methlist: 0x1414
+1228.100.1.2.1
+  __TEXT.__text: 0x17f40
+  __TEXT.__auth_stubs: 0xd50
+  __TEXT.__objc_stubs: 0x3fa0
+  __TEXT.__objc_methlist: 0x142c
   __TEXT.__const: 0x10c
-  __TEXT.__objc_methname: 0x39af
-  __TEXT.__cstring: 0x4891
+  __TEXT.__objc_methname: 0x39dc
+  __TEXT.__cstring: 0x4897
   __TEXT.__objc_classname: 0x301
   __TEXT.__objc_methtype: 0xaa7
   __TEXT.__gcc_except_tab: 0x30c
-  __TEXT.__oslogstring: 0x1310
-  __TEXT.__unwind_info: 0x7b0
-  __DATA_CONST.__auth_got: 0x6a0
+  __TEXT.__oslogstring: 0x133d
+  __TEXT.__unwind_info: 0x7b8
+  __DATA_CONST.__auth_got: 0x6b8
   __DATA_CONST.__got: 0x378
   __DATA_CONST.__const: 0xbe0
   __DATA_CONST.__cfstring: 0x1da0

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x23c0
-  __DATA.__objc_selrefs: 0x11d8
+  __DATA.__objc_selrefs: 0x11e8
   __DATA.__objc_ivar: 0x184
   __DATA.__objc_data: 0x870
   __DATA.__data: 0x370

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 7D37CEF9-5C67-3F16-9787-0F32CB157189
-  Functions: 568
-  Symbols:   336
-  CStrings:  1573
+  UUID: 6EC739FE-CF80-3E24-BBFC-81986711ABA7
+  Functions: 571
+  Symbols:   339
+  CStrings:  1577
 
Symbols:
+ _CFDictionaryGetCount
+ _CFDictionaryRemoveAllValues
+ __os_log_fault_impl
CStrings:
+ "            DELETE FROM recents \n            WHERE recents.ROWID IN (:row_ids) \n            AND recents.bundle_identifier = :bundle_identifier"
+ ":row_ids"
+ "Statement cache grew too large to %li values"
+ "clearStatementCache"
+ "isStatementCacheTooLarge"
- "            DELETE FROM recents \n            WHERE recents.ROWID IN (%@) \n            AND recents.bundle_identifier = :bundle_identifier         "

```
