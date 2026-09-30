## jetsam_priority

> `/usr/libexec/jetsam_priority`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

-10848.0.9.0.0
-  __TEXT.__text: 0xafbc
-  __TEXT.__auth_stubs: 0x5d0
+10848.0.13.0.0
+  __TEXT.__text: 0xb404
+  __TEXT.__auth_stubs: 0x610
   __TEXT.__objc_stubs: 0x1e0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x89
-  __TEXT.__gcc_except_tab: 0xcc4
-  __TEXT.__cstring: 0x1320
+  __TEXT.__gcc_except_tab: 0xd20
+  __TEXT.__cstring: 0x135f
   __TEXT.__objc_methname: 0x14a
   __TEXT.__unwind_info: 0x2e0
   __DATA_CONST.__const: 0x178
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x2f8
-  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__auth_got: 0x318
+  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_selrefs: 0x78
   __DATA.__data: 0x50

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 104
-  Symbols:   128
-  CStrings:  190
+  Symbols:   135
+  CStrings:  196
 
Symbols:
+ _XPC_COALITION_INFO_KEY_BUNDLE_IDENTIFIER
+ _XPC_COALITION_INFO_KEY_NAME
+ __xpc_type_dictionary
+ _strdup
+ _strncmp
+ _xpc_coalition_copy_info
+ _xpc_dictionary_get_string
+ _xpc_get_type
- _objc_release_x24
Functions:
~ sub_100000b7c : 27196 -> 28244
~ sub_100007e30 -> sub_100008248 : 532 -> 580
CStrings:
+ "   \n   Internal Only\n"
+ "   -g: Print process coalitions.\n"
+ ":kd:n:hcelifgs:w:rxp:z::"
+ "Unknown"
+ "coalition_id"
+ "coalition_name"
+ "com.apple."
+ "self"
+ "to launchd"
- ":kd:n:hcelifs:w:rxp:z::"
- "Warning: Could not get coalitions for pid %d.\n"
- "coalition"
```
