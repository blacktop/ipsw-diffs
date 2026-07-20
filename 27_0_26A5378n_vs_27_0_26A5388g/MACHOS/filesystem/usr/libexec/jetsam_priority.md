## jetsam_priority

> `/usr/libexec/jetsam_priority`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

-10848.0.9.0.0
-  __TEXT.__text: 0xa2b4
-  __TEXT.__auth_stubs: 0x520
+10848.0.13.0.0
+  __TEXT.__text: 0xa598
+  __TEXT.__auth_stubs: 0x570
   __TEXT.__objc_stubs: 0x100
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x89
-  __TEXT.__gcc_except_tab: 0xb1c
-  __TEXT.__cstring: 0x125a
+  __TEXT.__gcc_except_tab: 0xb74
+  __TEXT.__cstring: 0x1299
   __TEXT.__objc_methname: 0xc5
   __TEXT.__unwind_info: 0x2e0
   __DATA_CONST.__const: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__auth_got: 0x2c8
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_selrefs: 0x40
   __DATA.__data: 0x4c

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 104
-  Symbols:   115
-  CStrings:  173
+  Symbols:   123
+  CStrings:  179
 
Symbols:
+ _XPC_COALITION_INFO_KEY_BUNDLE_IDENTIFIER
+ _XPC_COALITION_INFO_KEY_NAME
+ __xpc_type_dictionary
+ _strdup
+ _strncmp
+ _xpc_coalition_copy_info
+ _xpc_dictionary_get_string
+ _xpc_get_type
Functions:
~ sub_100000ad4 : 23828 -> 24520
~ sub_100007064 -> sub_100007318 : 532 -> 580
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
