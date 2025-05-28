## dirs_cleaner

> `/usr/libexec/dirs_cleaner`

```diff

-712.60.2.0.0
-  __TEXT.__text: 0xe40
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__cstring: 0x531
+718.0.0.0.0
+  __TEXT.__text: 0xef4
+  __TEXT.__auth_stubs: 0x240
+  __TEXT.__cstring: 0x5c2
   __TEXT.__unwind_info: 0x5c
-  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__auth_got: 0x120
   __DATA_CONST.__got: 0x10
+  __DATA_CONST.__auth_ptr: 0x8
   - /usr/lib/libSystem.B.dylib
   Functions: 6
-  Symbols:   39
-  CStrings:  42
+  Symbols:   41
+  CStrings:  44
 
Symbols:
+ ___chkstk_darwin
+ _strlen
CStrings:
+ "%s: (bad path: %s, NULL, ...) failed with errno=%d: %s\n"
+ "%s: realpath: (%s, NULL, ...) failed with errno=%d: %s\n"
+ "%s: statfs: (%s, NULL, ...) failed with errno=%d: %s\n"
+ "get_tmp_path"
- "/private/var/mobile/"
- "/var/mobile/"

```
