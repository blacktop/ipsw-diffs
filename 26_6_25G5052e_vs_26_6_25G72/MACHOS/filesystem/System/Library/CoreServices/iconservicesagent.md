## iconservicesagent

> `/System/Library/CoreServices/iconservicesagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-743.5.2.400.0
-  __TEXT.__text: 0x644c
+743.5.2.401.0
+  __TEXT.__text: 0x668c
   __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0x1400
   __TEXT.__objc_methlist: 0x42c
-  __TEXT.__const: 0x98
+  __TEXT.__const: 0xa8
   __TEXT.__cstring: 0x568
-  __TEXT.__oslogstring: 0x9b9
+  __TEXT.__oslogstring: 0xae9
   __TEXT.__objc_classname: 0xb6
   __TEXT.__objc_methtype: 0x385
-  __TEXT.__gcc_except_tab: 0x98
+  __TEXT.__gcc_except_tab: 0x144
   __TEXT.__objc_methname: 0x1318
-  __TEXT.__unwind_info: 0x1c0
+  __TEXT.__unwind_info: 0x1c8
   __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 132
+  Functions: 134
   Symbols:   143
-  CStrings:  441
+  CStrings:  444
 
CStrings:
+ "... Done. Cache cleared: removed %lu files, %lu failures"
+ "... Done. Cache reset complete: removed %lu items, %lu failures at path: %@"
+ "... Done. Garbage collection complete: removed %lu source units, %lu tint units. Stale index entries remain for lazy cleanup."
+ "Failed to remove cache item at URL: %@ with error: %@"
- "... Done"
```
