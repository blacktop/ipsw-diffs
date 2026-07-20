## sysstatuscheck

> `/usr/libexec/sysstatuscheck`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`

```diff

-233.0.0.0.0
-  __TEXT.__text: 0xebc
-  __TEXT.__auth_stubs: 0x150
+233.0.5.0.0
+  __TEXT.__text: 0x1010
+  __TEXT.__auth_stubs: 0x180
   __TEXT.__init_offsets: 0x4
-  __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x33a
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0xb0
-  __DATA_CONST.__got: 0x28
-  __DATA.__bss: 0x48
+  __TEXT.__gcc_except_tab: 0xd8
+  __TEXT.__const: 0x20
+  __TEXT.__cstring: 0x354
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x20
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 15
-  Symbols:   112
-  CStrings:  20
+  Functions: 16
+  Symbols:   111
+  CStrings:  23
 
Symbols:
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
CStrings:
+ "/var/db/mmaintenanced/"
+ "Failed to query data for '%s': (%d) %s\n"
+ "Failed to setup environment for memory error reporting (non-fatal)).\n"
+ "Failed to update ownership/permissions for '%s'\n"
+ "Failed to update permisions to %04o and/or user/group ownership to %d/%d for '%s'.\n"
+ "dramecc.db"
+ "memory_errors.db"
+ "vm.ecc.enabled"
- "Failed to migrate ECC database (non-fatal).\n"
- "Failed to query UID for '%s'.\n"
- "Failed to update permissions to %04o and/or user/group ownership to %d/%d for '%s'.\n"
- "Failed to update permissions to %04o for '%s': %d (%s)\n"
- "Failed to update user/group ownership to %d/%d for '%s': %d (%s)\n"
```
