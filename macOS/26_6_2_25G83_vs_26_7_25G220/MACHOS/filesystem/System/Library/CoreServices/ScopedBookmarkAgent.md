## ScopedBookmarkAgent

> `System/Library/CoreServices/ScopedBookmarkAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-579.5.4.0.0
-  __TEXT.__text: 0xca24
-  __TEXT.__auth_stubs: 0xa90
+579.5.5.0.0
+  __TEXT.__text: 0xcdf8
+  __TEXT.__auth_stubs: 0xaa0
   __TEXT.__objc_stubs: 0xc40
   __TEXT.__objc_methlist: 0x1f0
-  __TEXT.__gcc_except_tab: 0x127c
+  __TEXT.__gcc_except_tab: 0x12bc
   __TEXT.__const: 0x8c
   __TEXT.__objc_methname: 0xa79
-  __TEXT.__cstring: 0x113a
-  __TEXT.__oslogstring: 0x16f8
+  __TEXT.__cstring: 0x1221
+  __TEXT.__oslogstring: 0x1737
   __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methtype: 0x130
   __TEXT.__unwind_info: 0x330
-  __DATA_CONST.__auth_got: 0x558
+  __DATA_CONST.__auth_got: 0x560
   __DATA_CONST.__got: 0x220
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x140
-  __DATA_CONST.__cfstring: 0x920
+  __DATA_CONST.__cfstring: 0x980
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 192
-  Symbols:   549
-  CStrings:  426
+  Functions: 196
+  Symbols:   551
+  CStrings:  432
 
Symbols:
+ _OUTLINED_FUNCTION_16
+ _sandbox_query_user_intent_for_process_with_audit_token
CStrings:
+ "Error checking intent for PID %d: %{errno}d"
+ "PID %d: %{public}@"
+ "Process does not have access to '/'."
+ "Process is not allowed to create bookmark to '/' without explicit user intent. Use an open panel to convey intent from the user."
+ "Process is not allowed to create bookmark to '/'."
+ "file-read-data"
```
