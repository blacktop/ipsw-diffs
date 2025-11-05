## taskpolicy

> `/usr/sbin/taskpolicy`

```diff

-1012.80.2.0.0
-  __TEXT.__text: 0xa08
-  __TEXT.__auth_stubs: 0x140
+1026.100.5.0.0
+  __TEXT.__text: 0xa98
+  __TEXT.__auth_stubs: 0x1b0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x3c1
-  __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0x28
+  __TEXT.__cstring: 0x4ed
+  __TEXT.__unwind_info: 0x68
+  __DATA_CONST.__auth_got: 0xd8
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__const: 0xa0
   - /usr/lib/libSystem.B.dylib
-  UUID: 6620FFEC-941E-3747-A985-C998E3EA18ED
-  Functions: 23
-  Symbols:   27
-  CStrings:  32
+  UUID: 565B517F-1B12-3DA6-8095-6C2581C79329
+  Functions: 22
+  Symbols:   35
+  CStrings:  43
 
Symbols:
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___strlcpy_chk
+ _errx
+ _posix_spawnattr_set_use_sec_transition_shims_np
+ _strchr
+ _strcmp
+ _strtoull
CStrings:
+ "%s: unknown security transition shim"
+ "Usage: %s [-x|-X] [-d <policy>] [-g <policy>] [-c <clamp>] [-b] [-t <tier>]\n                  [-l <tier>] [-a] [-s] [-S <shims>] <program> [<pargs> [...]]\n"
+ "explicit-check-bypass"
+ "explicit-check-enforce"
+ "explicit-disable"
+ "explicit-disable-inherit"
+ "explicit-enable"
+ "explicit-enable-inherit"
+ "explicit-never-check-disable"
+ "explicit-never-check-enable"
+ "explicit-vm-policy-bypass"
+ "setting security transition shims"
+ "xXbBd:g:c:t:l:p:asS:"
- "Usage: %s [-x|-X] [-d <policy>] [-g policy] [-c clamp] [-b] [-t <tier>]\n                  [-l <tier>] [-a] [-s] <program> [<pargs> [...]]\n"
- "xXbBd:g:c:t:l:p:as"

```
