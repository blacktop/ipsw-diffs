## pam_tid.so.2

> `/usr/lib/pam/pam_tid.so.2`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`

```diff

-231.0.0.0.0
-  __TEXT.__text: 0x18e4
-  __TEXT.__auth_stubs: 0x2f0
+231.0.1.0.0
+  __TEXT.__text: 0x18b8
+  __TEXT.__auth_stubs: 0x2e0
   __TEXT.__objc_stubs: 0x1e0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x36f
+  __TEXT.__cstring: 0x34d
   __TEXT.__oslogstring: 0xab
   __TEXT.__dlopen_cstrs: 0x5d
   __TEXT.__gcc_except_tab: 0x44

   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x188
+  __DATA_CONST.__auth_got: 0x180
   __DATA_CONST.__got: 0x50
   __DATA.__objc_selrefs: 0x78
   __DATA.__bss: 0x20

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpam.2.dylib
   Functions: 33
-  Symbols:   124
-  CStrings:  54
+  Symbols:   123
+  CStrings:  52
 
Symbols:
+ _getaudit_addr
- _strcmp
- _vproc_swap_string
Functions:
~ _pam_sm_authenticate : 1080 -> 1036
CStrings:
- "Aqua"
- "unable to determine session."
```
