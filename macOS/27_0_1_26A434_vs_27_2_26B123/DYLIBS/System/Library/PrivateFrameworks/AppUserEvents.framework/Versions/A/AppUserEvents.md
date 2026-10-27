## AppUserEvents

> `/System/Library/PrivateFrameworks/AppUserEvents.framework/Versions/A/AppUserEvents`

```diff

-10.0.0.0.0
-  __TEXT.__text: 0x34fc8
+12.0.0.0.0
+  __TEXT.__text: 0x3a1cc
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x3208
-  __TEXT.__constg_swiftt: 0x1674
-  __TEXT.__swift5_typeref: 0xf1f
-  __TEXT.__swift5_reflstr: 0x924
-  __TEXT.__swift5_fieldmd: 0xe7c
+  __TEXT.__const: 0x3418
+  __TEXT.__constg_swiftt: 0x1768
+  __TEXT.__swift5_typeref: 0x1019
+  __TEXT.__swift5_reflstr: 0x954
+  __TEXT.__swift5_fieldmd: 0xef8
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x2c
   __TEXT.__swift5_capture: 0x234
-  __TEXT.__cstring: 0xb2a
-  __TEXT.__oslogstring: 0x581
-  __TEXT.__swift5_proto: 0x27c
-  __TEXT.__swift5_types: 0x118
+  __TEXT.__cstring: 0xc4a
+  __TEXT.__oslogstring: 0x591
+  __TEXT.__swift5_proto: 0x2a4
+  __TEXT.__swift5_types: 0x120
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x28
-  __TEXT.__swift_as_cont: 0x30
-  __TEXT.__swift5_protos: 0x3c
+  __TEXT.__swift_as_cont: 0x28
+  __TEXT.__swift5_protos: 0x48
   __TEXT.__swift5_assocty: 0x248
-  __TEXT.__unwind_info: 0xf68
-  __TEXT.__eh_frame: 0x2148
+  __TEXT.__unwind_info: 0x1090
+  __TEXT.__eh_frame: 0x2648
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __DATA_CONST.__got: 0x428
-  __AUTH_CONST.__const: 0x25a0
+  __DATA_CONST.__got: 0x468
+  __AUTH_CONST.__const: 0x26c8
   __AUTH_CONST.__objc_const: 0x4e0
-  __AUTH_CONST.__auth_got: 0xb70
-  __AUTH_CONST.__auth_ptr: 0x7b0
-  __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x6b8
-  __DATA.__data: 0x16e0
-  __DATA.__bss: 0x3710
-  __DATA.__common: 0x48
+  __AUTH_CONST.__auth_got: 0xbb8
+  __AUTH_CONST.__auth_ptr: 0x800
+  __AUTH.__data: 0x610
+  __DATA.__data: 0x1168
+  __DATA.__bss: 0x3810
+  __DATA.__common: 0x30
+  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__data: 0x710
+  __DATA_DIRTY.__bss: 0x200
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/AppPrivateData.framework/Versions/A/AppPrivateData

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1252
-  Symbols:   555
-  CStrings:  81
+  Functions: 1310
+  Symbols:   567
+  CStrings:  87
 
Symbols:
+ ___swift_allocate_boxed_opaque_existential_1Tm
+ ___swift_deallocate_boxed_opaque_existential_0
+ ___swift_memcpy33_8
+ ___unnamed_17
+ ___unnamed_18
+ _symbolic $s13AppUserEvents0B15EventSupplementP
+ _symbolic $s13AppUserEvents16_SQLLiteralRange33_E4D167AB3ED1F72A211C3A17817C6B32LLP
+ _symbolic $s13AppUserEvents19_SQLRangeExpression33_E4D167AB3ED1F72A211C3A17817C6B32LLP
+ _symbolic 5Event_____Qz 13AppUserEvents0B15EventSupplementP
+ _symbolic 6Output_____Qy0_ 10Foundation19PredicateExpressionP
+ _symbolic 6Output_____Qy_ 10Foundation19PredicateExpressionP
+ _symbolic S2S______SayxGtYbKc 10Foundation12DateIntervalV
+ _symbolic SbSg
+ _symbolic _____ 13AppUserEvents12_SQLFragment33_E4D167AB3ED1F72A211C3A17817C6B32LLV
+ _symbolic q_
+ _symbolic ySS______SayxGtYbc 10Foundation4DateV
+ _type_layout_string 13AppUserEvents12_SQLFragment33_E4D167AB3ED1F72A211C3A17817C6B32LLV
- ___unnamed_8
- ___unnamed_9
- _symbolic 7ElementSTQz
- _symbolic ySS_SayxGtYbc
- _symbolic ySS______SayxGtYbKc 10Foundation12DateIntervalV
CStrings:
+ "CREATE TABLE IF NOT EXISTS sessions (\n    id INTEGER PRIMARY KEY,\n    session_id TEXT UNIQUE NOT NULL,\n    end_date INTEGER NOT NULL\n);\nCREATE TABLE IF NOT EXISTS events (\n    session_row_id INTEGER NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,\n    event_index INTEGER NOT NULL,\n    PRIMARY KEY (session_row_id, event_index)\n);\nCREATE TABLE IF NOT EXISTS session_index_coverage (\n    session_id TEXT NOT NULL REFERENCES sessions(session_id) ON DELETE CASCADE,\n    field_name TEXT NOT NULL,\n    PRIMARY KEY (session_id, field_name)\n);\nCREATE INDEX IF NOT EXISTS idx_coverage_field ON session_index_coverage(field_name, session_id);"
+ "Closing event write stream, id=%{public}s"
+ "DROP TABLE IF EXISTS session_index_coverage;\nDROP TABLE IF EXISTS events;\nDROP TABLE IF EXISTS sessions;"
+ "Did save session, id=%{public}s"
+ "Did save session, id=%{public}s, persisted=%{public}s"
+ "Failed to save session, id=%{public}s, error=%{public}@"
+ "INSERT OR IGNORE INTO sessions (id, session_id, end_date) VALUES (?, ?, ?) RETURNING id;"
+ "Opening event write stream, id=%{public}s"
+ "PRAGMA user_version = "
+ "PRAGMA user_version;"
+ "SELECT MAX(id) FROM sessions WHERE id >= ? AND id <= ?;"
+ "Skipping persistence of empty session, id=%{public}s"
+ "Submitting event to write stream, event=%{public}s, id=%{public}s"
+ "Will save session, eventCount=%ld, id=%{public}s"
+ "op value "
- "CREATE TABLE IF NOT EXISTS sessions (\n    id INTEGER PRIMARY KEY AUTOINCREMENT,\n    session_id TEXT UNIQUE NOT NULL\n);\nCREATE TABLE IF NOT EXISTS events (\n    session_row_id INTEGER NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,\n    event_index INTEGER NOT NULL,\n    PRIMARY KEY (session_row_id, event_index)\n);\nCREATE TABLE IF NOT EXISTS session_index_coverage (\n    session_id TEXT NOT NULL REFERENCES sessions(session_id) ON DELETE CASCADE,\n    field_name TEXT NOT NULL,\n    PRIMARY KEY (session_id, field_name)\n);\nCREATE INDEX IF NOT EXISTS idx_coverage_field ON session_index_coverage(field_name, session_id);"
- "Closing event write stream, identifier=%{public}s"
- "Did save session, identifier=%{public}s"
- "Failed to save session, identifier=%{public}s, error=%{public}@"
- "INSERT OR IGNORE INTO sessions (session_id) VALUES (?) RETURNING id;"
- "Opening event write stream, identifier=%{public}s"
- "Skipping persistence of empty session, identifier=%{public}s"
- "Submitting event to write stream, event=%{public}s, identifier=%{public}s"
- "Will save session, eventCount=%ld, identifier=%{public}s"
```
