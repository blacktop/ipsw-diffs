## analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-577.40.5.0.0
-  __TEXT.__text: 0x141734
+577.40.7.0.0
+  __TEXT.__text: 0x1423a0
   __TEXT.__auth_stubs: 0x1e60
   __TEXT.__objc_stubs: 0x2cc0
   __TEXT.__init_offsets: 0x24
   __TEXT.__objc_methlist: 0xb9c
-  __TEXT.__gcc_except_tab: 0x17794
-  __TEXT.__const: 0xa464
-  __TEXT.__cstring: 0x16215
-  __TEXT.__oslogstring: 0x1af99
+  __TEXT.__gcc_except_tab: 0x178b8
+  __TEXT.__const: 0xa474
+  __TEXT.__cstring: 0x162b5
+  __TEXT.__oslogstring: 0x1b039
   __TEXT.__objc_methname: 0x2f83
   __TEXT.__objc_classname: 0x20a
   __TEXT.__objc_methtype: 0x1879

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x9cf8
-  __TEXT.__eh_frame: 0x3a8
-  __DATA_CONST.__const: 0xadc8
+  __TEXT.__unwind_info: 0x9d40
+  __TEXT.__eh_frame: 0x3e0
+  __DATA_CONST.__const: 0xade8
   __DATA_CONST.__cfstring: 0xd40
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x58

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6410
+  Functions: 6418
   Symbols:   734
-  CStrings:  4139
+  CStrings:  4141
 
Symbols:
+ _swift_release_x19
- _swift_release_x20
CStrings:
+ "SELECT session_id FROM sessions WHERE cadence = ?1 AND start <= ?2 UNION SELECT DISTINCT tm.session_id FROM transform_metadata tm LEFT JOIN sessions s ON tm.session_id = s.session_id WHERE s.session_id IS NULL AND tm.session_id IS NOT NULL"
+ "SessionNotAcceptingEvents"
+ "[FW Event] ERROR: Event '%s' dropped: session '%{public}s' does not exist or has ended."
+ "[SessionManager] Failed to re-create session row for leftover state: %s"
+ "[Sink] No session row for %{public}s; stamping log with the cadence log start instead"
- "SELECT session_id FROM sessions WHERE state = ?1 AND cadence = ?2 AND start <= ?3"
- "[Transform Manager] Session %s not enabled for transform, using main session"
- "sessionsEnabled"
```
