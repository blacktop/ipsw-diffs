## libsystem_sandbox.dylib

> `/usr/lib/system/libsystem_sandbox.dylib`

```diff

-2401.40.25.0.0
-  __TEXT.__text: 0x3378
-  __TEXT.__auth_stubs: 0x2f0
+2401.60.100.0.1
+  __TEXT.__text: 0x37e0
+  __TEXT.__auth_stubs: 0x330
   __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x64a
-  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__cstring: 0x7b4
+  __TEXT.__unwind_info: 0x1c8
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x178
+  __AUTH_CONST.__auth_got: 0x198
   __DATA.__data: 0x13
   __DATA.__bss: 0x8
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  Functions: 132
-  Symbols:   208
-  CStrings:  58
+  Functions: 134
+  Symbols:   213
+  CStrings:  71
 
Symbols:
+ _basename_r
+ _dirname_r
+ _fstat
+ _mkdirat
+ _openat
+ _sandbox_check_finder_automation_for_path
+ _unlinkat
- _mkdir
- _rmdir
CStrings:
+ "%!s(MISSING): %!s(MISSING) for %!s(MISSING)"
+ "%!s(MISSING): failed for %!s(MISSING): %!s(MISSING) (%!d(MISSING))"
+ "%!s(MISSING): failed: %!s(MISSING) moved before protection"
+ "%!s(MISSING): failed: %!s(MISSING) not on same filesystem as parent"
+ "%!s(MISSING): failed: %!s(MISSING) not protected"
+ "%!s(MISSING): unsupported flags: %!u(MISSING)"
+ "denied by sandbox policy"
+ "failed POSIX permissions check"
+ "failed canonical check"
+ "file-write-unlink"
+ "rootless_mkdir_protected"
+ "sandbox_check_finder_automation_for_path"
+ "unknown failure"

```
