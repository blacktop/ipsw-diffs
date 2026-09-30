## sysstatuscheck

> `/usr/libexec/sysstatuscheck`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__const`

```diff

-233.0.0.502.1
-  __TEXT.__text: 0xd0cc
-  __TEXT.__auth_stubs: 0x510
+233.0.5.0.0
+  __TEXT.__text: 0xd22c
+  __TEXT.__auth_stubs: 0x520
   __TEXT.__init_offsets: 0x4
-  __TEXT.__gcc_except_tab: 0x5a0
-  __TEXT.__const: 0x548
-  __TEXT.__cstring: 0xc5a
-  __TEXT.__unwind_info: 0x520
+  __TEXT.__gcc_except_tab: 0x61c
+  __TEXT.__const: 0x4c8
+  __TEXT.__cstring: 0xc74
+  __TEXT.__unwind_info: 0x548
   __DATA_CONST.__const: 0x728
-  __DATA_CONST.__auth_got: 0x290
-  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__auth_got: 0x298
+  __DATA_CONST.__got: 0x70
   __DATA.__data: 0x60
-  __DATA.__bss: 0x4c
+  __DATA.__bss: 0x4
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 247
-  Symbols:   128
-  CStrings:  83
+  Functions: 249
+  Symbols:   127
+  CStrings:  86
 
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
