## nsurlsessiond

> `/usr/libexec/nsurlsessiond`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3896.100.1.1.1
-  __TEXT.__text: 0x628d4
-  __TEXT.__auth_stubs: 0xf00
+3896.200.31.0.0
+  __TEXT.__text: 0x62f48
+  __TEXT.__auth_stubs: 0xf50
   __TEXT.__lazy_helpers: 0xfc
   __TEXT.__objc_stubs: 0x8b00
-  __TEXT.__objc_methlist: 0x31bc
+  __TEXT.__objc_methlist: 0x31b4
   __TEXT.__const: 0x260
-  __TEXT.__gcc_except_tab: 0xc604
-  __TEXT.__objc_methname: 0xb505
+  __TEXT.__gcc_except_tab: 0xc66c
+  __TEXT.__objc_methname: 0xb508
   __TEXT.__objc_classname: 0x4e5
-  __TEXT.__cstring: 0x3271
+  __TEXT.__cstring: 0x340c
   __TEXT.__objc_methtype: 0x2030
-  __TEXT.__oslogstring: 0xdfab
-  __TEXT.__unwind_info: 0x2228
-  __DATA_CONST.__const: 0x1338
-  __DATA_CONST.__cfstring: 0x1460
+  __TEXT.__oslogstring: 0xe07b
+  __TEXT.__unwind_info: 0x2230
+  __DATA_CONST.__const: 0x1368
+  __DATA_CONST.__cfstring: 0x14a0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xe8

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x798
+  __DATA_CONST.__auth_got: 0x7c0
   __DATA_CONST.__got: 0x618
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x43e8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1139
-  Symbols:   438
-  CStrings:  2971
+  Functions: 1143
+  Symbols:   443
+  CStrings:  2977
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFEqual
+ _CFPreferencesCopyAppValue
+ _CFStringGetTypeID
CStrings:
+ "AVAssetDownloadFailOnRetryableError"
+ "CREATE INDEX IF NOT EXISTS idx_session_tasks_session_bundle ON session_tasks(session_id, bundle_id);"
+ "Failed to bind session limit params to the insert statement"
+ "Failed to create session_tasks index"
+ "Failed to migrate to version 4"
+ "REPLACE INTO sessions (bundle_id, session_id, configuration, options) \tSELECT ?, ?, ?, (SELECT options FROM sessions WHERE bundle_id = ? AND session_id = ?) \tWHERE EXISTS (SELECT 1 FROM sessions WHERE bundle_id = ? AND session_id = ?) \t\tOR (SELECT COUNT(*) FROM sessions WHERE bundle_id = ?) < ?"
+ "REPLACE INTO sessions (bundle_id, session_id, options, configuration) \tSELECT ?, ?, ?, (SELECT configuration FROM sessions WHERE bundle_id = ? AND session_id = ?) \tWHERE EXISTS (SELECT 1 FROM sessions WHERE bundle_id = ? AND session_id = ?) \t\tOR (SELECT COUNT(*) FROM sessions WHERE bundle_id = ?) < ?"
+ "Refused to persist session %@ for bundle %{public}@: session limit (%d) reached"
+ "updateWorkState"
- "REPLACE INTO sessions (bundle_id, session_id, configuration, options)  values (?, ?, ?, (SELECT options FROM sessions WHERE bundle_id = ? AND session_id = ?))"
- "REPLACE INTO sessions (bundle_id, session_id, options, configuration) \tvalues (?, ?, ?, (SELECT configuration FROM sessions WHERE bundle_id = ? AND session_id = ?))"
- "setWorkState"
```
