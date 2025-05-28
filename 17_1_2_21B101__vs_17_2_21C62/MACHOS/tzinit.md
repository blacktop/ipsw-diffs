## tzinit

> `/usr/libexec/tzinit`

```diff

-87.0.0.0.0
-  __TEXT.__text: 0x110a0
-  __TEXT.__auth_stubs: 0x4f0
+87.2.0.0.0
+  __TEXT.__text: 0x110c8
+  __TEXT.__auth_stubs: 0x500
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x726
-  __TEXT.__gcc_except_tab: 0xc08
-  __TEXT.__cstring: 0x591
+  __TEXT.__gcc_except_tab: 0xc0c
+  __TEXT.__cstring: 0x5da
   __TEXT.__unwind_info: 0x848
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x280
+  __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__const: 0x8a8
   __DATA.__bss: 0x18
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   Functions: 366
-  Symbols:   105
-  CStrings:  51
+  Symbols:   106
+  CStrings:  52
 
Symbols:
+ _setiopolicy_np
CStrings:
+ "setiopolicy IOPOL_TYPE_VFS_ALLOW_LOW_SPACE_WRITES returned error code %d"

```
