## libncurses.5.4.dylib

> `/usr/lib/libncurses.5.4.dylib`

```diff

-81.0.0.0.0
-  __TEXT.__text: 0x2ff4c
+85.0.0.0.0
+  __TEXT.__text: 0x2ffd0
   __TEXT.__const: 0x72e4
-  __TEXT.__cstring: 0x3c60
+  __TEXT.__cstring: 0x3c8e
   __TEXT.__unwind_info: 0xe08
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x2f10
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x2e8
+  __AUTH_CONST.__auth_got: 0x2f0
   __AUTH.__data: 0x18
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_data: 0x4

   __DATA_DIRTY.__bss: 0x8
   __DATA_DIRTY.__common: 0x30a
   - /usr/lib/libSystem.B.dylib
-  Functions: 1014
-  Symbols:   1042
-  CStrings:  1681
+  Functions: 1015
+  Symbols:   1044
+  CStrings:  1682
 
Symbols:
+ __nc_env_access
+ _fopen$DARWIN_EXTSN
+ _issetugid
+ _select$DARWIN_EXTSN
- _fopen
- _select
Functions:
~ __nc_home_terminfo : 124 -> 140
+ __nc_env_access
~ __nc_tic_dir : 124 -> 144
~ __nc_first_db : 968 -> 1000
~ __nc_read_termcap_entry : 844 -> 864
~ __nc_set_writedir : 240 -> 252
CStrings:
+ "/usr/share/terminfo:/usr/local/share/terminfo"
```
