## libsystem_coreservices.dylib

> `/usr/lib/system/libsystem_coreservices.dylib`

```diff

-191.1.2.0.0
-  __TEXT.__text: 0x1c54
-  __TEXT.__auth_stubs: 0x2b0
+191.2.3.0.0
+  __TEXT.__text: 0x193c
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x329
-  __TEXT.__oslogstring: 0x23d
-  __TEXT.__unwind_info: 0xe8
+  __TEXT.__cstring: 0x31b
+  __TEXT.__oslogstring: 0x1ff
+  __TEXT.__unwind_info: 0xd8
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x948
-  __AUTH_CONST.__auth_got: 0x158
-  __AUTH_CONST.__const: 0xa0
+  __DATA_CONST.__const: 0x928
+  __AUTH_CONST.__auth_got: 0x150
+  __AUTH_CONST.__const: 0x80
   __DATA.__bss: 0x820
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__bss: 0x20
   __DATA_DIRTY.__common: 0x88
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 9C23D5D4-65A0-3FBE-83F8-DE257DE32955
-  Functions: 47
-  Symbols:   201
-  CStrings:  63
+  UUID: 6A36257A-B28C-3EA5-B5AE-BEA3AA55B5C7
+  Functions: 42
+  Symbols:   184
+  CStrings:  59
 
Symbols:
+ _close
+ _fchmod
+ _fstat
+ _makeDirectory.cold.1
+ _makeDirectory.cold.2
+ _open
- _getegid
- _lchmod
- _lchown
- _lstat
- _makeDirectoryWithUIDAndGID
- _makeDirectoryWithUIDAndGID.cold.1
- _makeDirectoryWithUIDAndGID.cold.2
- _makeDirectoryWithUIDAndGID.cold.3
- _makeDirectoryWithUIDAndGID.cold.4
- _makeDirectoryWithUIDAndGID.cold.5
- _makeDirectoryWithUIDAndGID.cold.6
- _strerror
CStrings:
+ "mkdir: created %s"
+ "mkdir: path=%{public}s mode= %{darwin.mode}d: %{darwin.errno}d"
- "%s: chmod error: %s (%d)"
- "%s: chown error for uid=%d, gid=%d: %s (%d)"
- "%s: created %s"
- "%s: mkdir: path=%s mode=%o: %s (%d)"
- "%s: set uid=%d, gid=%d"
- "makeDirectory"

```
