## nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

-  __TEXT.__text: 0x82e54
-  __TEXT.__auth_stubs: 0x11b0
+  __TEXT.__text: 0x82e20
+  __TEXT.__auth_stubs: 0x11d0
   __TEXT.__lazy_helpers: 0xfc
   __TEXT.__objc_stubs: 0xa940
   __TEXT.__objc_methlist: 0x61bc
   __TEXT.__const: 0x270
-  __TEXT.__gcc_except_tab: 0xe5d4
+  __TEXT.__gcc_except_tab: 0xe5b0
   __TEXT.__cstring: 0x3a7e
-  __TEXT.__objc_methname: 0xf185
+  __TEXT.__objc_methname: 0xf154
   __TEXT.__objc_classname: 0xb94
   __TEXT.__objc_methtype: 0x2f57
-  __TEXT.__oslogstring: 0xf81a
+  __TEXT.__oslogstring: 0xf76e
   __TEXT.__unwind_info: 0x2de0
   __DATA_CONST.__const: 0x15c8
   __DATA_CONST.__cfstring: 0x1da0

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x8f0
-  __DATA_CONST.__got: 0x720
+  __DATA_CONST.__auth_got: 0x900
+  __DATA_CONST.__got: 0x7a0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x8e78
+  __DATA.__objc_const: 0x8e38
   __DATA.__objc_selrefs: 0x3718
-  __DATA.__objc_ivar: 0x700
+  __DATA.__objc_ivar: 0x6f8
   __DATA.__objc_data: 0x1630
   __DATA.__lazy_load_got: 0x18
   __DATA.__data: 0xe4c

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 2071
-  Symbols:   514
-  CStrings:  4155
+  Symbols:   516
+  CStrings:  4151
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
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
