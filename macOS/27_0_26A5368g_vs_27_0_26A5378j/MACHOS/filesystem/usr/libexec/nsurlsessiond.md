## nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

-  __TEXT.__text: 0x637bc
-  __TEXT.__auth_stubs: 0xee0
+  __TEXT.__text: 0x63730
+  __TEXT.__auth_stubs: 0xf00
   __TEXT.__lazy_helpers: 0xfc
   __TEXT.__objc_stubs: 0x8b00
   __TEXT.__objc_methlist: 0x31bc
   __TEXT.__const: 0x260
-  __TEXT.__gcc_except_tab: 0xc608
-  __TEXT.__objc_methname: 0xb64e
+  __TEXT.__gcc_except_tab: 0xc5e4
+  __TEXT.__objc_methname: 0xb61d
   __TEXT.__objc_classname: 0x4e5
   __TEXT.__cstring: 0x3266
   __TEXT.__objc_methtype: 0x2030
-  __TEXT.__oslogstring: 0xe057
-  __TEXT.__unwind_info: 0x2148
+  __TEXT.__oslogstring: 0xdfab
+  __TEXT.__unwind_info: 0x2140
   __DATA_CONST.__const: 0x1340
   __DATA_CONST.__cfstring: 0x1440
   __DATA_CONST.__objc_classlist: 0xd8

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x788
-  __DATA_CONST.__got: 0x5c8
+  __DATA_CONST.__auth_got: 0x798
+  __DATA_CONST.__got: 0x618
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x4568
+  __DATA.__objc_const: 0x4528
   __DATA.__objc_selrefs: 0x2a08
-  __DATA.__objc_ivar: 0x428
+  __DATA.__objc_ivar: 0x420
   __DATA.__objc_data: 0x870
   __DATA.__lazy_load_got: 0x18
   __DATA.__data: 0xae4

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 1136
-  Symbols:   436
-  CStrings:  3162
+  Symbols:   438
+  CStrings:  3158
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _sqlite3_clear_bindings
+ _sqlite3_free
CStrings:
+ "Failed to delete expired entries from session_tasks table of DB: %s"
+ "Failed to delete expired entries from sessions table of DB: %s"
- "Failed to delete expired entries from session_tasks table of DB. Error= %s"
- "Failed to delete expired entries from sessions table of DB. Error= %s"
- "Failed to init the _deleteEntriesStmt statement for session_tasks. Error = %s"
- "Failed to init the _deleteSessionEntriesStmt statement for sessions. Error = %s"
- "_deleteSessionEntriesStmt"
- "_deleteTaskEntriesStmt"

```
