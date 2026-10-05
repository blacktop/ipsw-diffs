## AppUserEvents

> `/System/Library/PrivateFrameworks/AppUserEvents.framework/AppUserEvents`

```diff

-11.0.0.0.0
-  __TEXT.__text: 0x36f24
+12.0.0.0.0
+  __TEXT.__text: 0x38324
   __TEXT.__objc_methlist: 0x20
   __TEXT.__const: 0x3418
-  __TEXT.__constg_swiftt: 0x175c
-  __TEXT.__swift5_typeref: 0x1013
-  __TEXT.__swift5_reflstr: 0x944
-  __TEXT.__swift5_fieldmd: 0xeec
+  __TEXT.__constg_swiftt: 0x1768
+  __TEXT.__swift5_typeref: 0x1019
+  __TEXT.__swift5_reflstr: 0x954
+  __TEXT.__swift5_fieldmd: 0xef8
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x2c
   __TEXT.__swift5_capture: 0x234
-  __TEXT.__cstring: 0xb3a
+  __TEXT.__cstring: 0xc4a
   __TEXT.__oslogstring: 0x591
   __TEXT.__swift5_proto: 0x2a4
-  __TEXT.__swift5_types: 0x11c
+  __TEXT.__swift5_types: 0x120
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x28
-  __TEXT.__swift_as_cont: 0x30
+  __TEXT.__swift_as_cont: 0x28
   __TEXT.__swift5_protos: 0x48
   __TEXT.__swift5_assocty: 0x248
-  __TEXT.__unwind_info: 0x1410
-  __TEXT.__eh_frame: 0x2558
+  __TEXT.__unwind_info: 0x1418
+  __TEXT.__eh_frame: 0x2650
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__got: 0x468
   __AUTH_CONST.__const: 0x26c8
   __AUTH_CONST.__objc_const: 0x4e0
-  __AUTH_CONST.__auth_got: 0xcc0
-  __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x6c8
-  __DATA.__data: 0x1720
-  __DATA.__common: 0x48
+  __AUTH_CONST.__auth_got: 0xcc8
+  __AUTH.__data: 0x610
+  __DATA.__data: 0x1168
+  __DATA.__common: 0x30
+  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__data: 0x710
+  __DATA_DIRTY.__bss: 0x200
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppPrivateData.framework/AppPrivateData

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1299
-  Symbols:   593
-  CStrings:  83
+  Functions: 1310
+  Symbols:   594
+  CStrings:  87
 
Symbols:
+ _objc_release_x26
+ _symbolic ySS______SayxGtYbc 10Foundation4DateV
- _symbolic ySS_SayxGtYbc
CStrings:
+ "CREATE TABLE IF NOT EXISTS sessions (\n    id INTEGER PRIMARY KEY,\n    session_id TEXT UNIQUE NOT NULL,\n    end_date INTEGER NOT NULL\n);\nCREATE TABLE IF NOT EXISTS events (\n    session_row_id INTEGER NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,\n    event_index INTEGER NOT NULL,\n    PRIMARY KEY (session_row_id, event_index)\n);\nCREATE TABLE IF NOT EXISTS session_index_coverage (\n    session_id TEXT NOT NULL REFERENCES sessions(session_id) ON DELETE CASCADE,\n    field_name TEXT NOT NULL,\n    PRIMARY KEY (session_id, field_name)\n);\nCREATE INDEX IF NOT EXISTS idx_coverage_field ON session_index_coverage(field_name, session_id);"
+ "DROP TABLE IF EXISTS session_index_coverage;\nDROP TABLE IF EXISTS events;\nDROP TABLE IF EXISTS sessions;"
+ "INSERT OR IGNORE INTO sessions (id, session_id, end_date) VALUES (?, ?, ?) RETURNING id;"
+ "PRAGMA user_version = "
+ "PRAGMA user_version;"
+ "SELECT MAX(id) FROM sessions WHERE id >= ? AND id <= ?;"
- "CREATE TABLE IF NOT EXISTS sessions (\n    id INTEGER PRIMARY KEY AUTOINCREMENT,\n    session_id TEXT UNIQUE NOT NULL\n);\nCREATE TABLE IF NOT EXISTS events (\n    session_row_id INTEGER NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,\n    event_index INTEGER NOT NULL,\n    PRIMARY KEY (session_row_id, event_index)\n);\nCREATE TABLE IF NOT EXISTS session_index_coverage (\n    session_id TEXT NOT NULL REFERENCES sessions(session_id) ON DELETE CASCADE,\n    field_name TEXT NOT NULL,\n    PRIMARY KEY (session_id, field_name)\n);\nCREATE INDEX IF NOT EXISTS idx_coverage_field ON session_index_coverage(field_name, session_id);"
- "INSERT OR IGNORE INTO sessions (session_id) VALUES (?) RETURNING id;"
```
