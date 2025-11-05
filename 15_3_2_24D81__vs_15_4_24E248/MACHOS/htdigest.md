## htdigest

> `/usr/sbin/htdigest`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xc68
+880.0.0.0.0
+  __TEXT.__text: 0xb7c
   __TEXT.__auth_stubs: 0x1b0
   __TEXT.__cstring: 0x283
   __TEXT.__unwind_info: 0x70

   - /usr/lib/libiconv.2.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 11B54BF8-E568-341E-A3DA-53E260FB8616
+  UUID: 96E257C2-A86F-37CC-A81A-48B754113AE0
   Functions: 9
   Symbols:   41
   CStrings:  24
Functions:
~ _main : 1604 -> 1476
~ _add_password : 548 -> 520
~ _cleanup_tempfile_and_exit : 68 -> 60
~ _get_line : 328 -> 296
~ _putline : 120 -> 112
~ _getword : 368 -> 336

```
