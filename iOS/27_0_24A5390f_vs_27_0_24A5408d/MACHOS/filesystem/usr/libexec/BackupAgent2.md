## BackupAgent2

> `/usr/libexec/BackupAgent2`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3039.0.1.0.0
-  __TEXT.__text: 0x90c98
+3039.2.2.0.0
+  __TEXT.__text: 0x90d80
   __TEXT.__auth_stubs: 0x1850
   __TEXT.__objc_stubs: 0xc9c0
   __TEXT.__objc_methlist: 0x5ffc
   __TEXT.__const: 0x4c8
-  __TEXT.__cstring: 0x18fb5
-  __TEXT.__oslogstring: 0xdf81
+  __TEXT.__cstring: 0x1900c
+  __TEXT.__oslogstring: 0xdfd8
   __TEXT.__objc_methname: 0xe80d
   __TEXT.__objc_classname: 0xa09
   __TEXT.__objc_methtype: 0x1e9d

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2455
+  Functions: 2457
   Symbols:   558
-  CStrings:  5763
+  CStrings:  5765
 
CStrings:
+ "Ignoring DLRequestFile message from the host"
+ "Ignoring DLSendFile message from the host"
```
