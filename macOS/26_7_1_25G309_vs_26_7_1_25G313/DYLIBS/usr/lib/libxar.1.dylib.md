## libxar.1.dylib

> `/usr/lib/libxar.1.dylib`

```diff

-503.160.5.700.1
-  __TEXT.__text: 0xc768
+503.160.5.701.1
+  __TEXT.__text: 0xc6b8
   __TEXT.__auth_stubs: 0x8b0
   __TEXT.__const: 0x168
   __TEXT.__cstring: 0xbf9

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 221
-  Symbols:   370
+  Functions: 222
+  Symbols:   371
   CStrings:  192
 
Symbols:
+ _xar_file_detach
Functions:
~ _xar_add_node : 720 -> 604
~ _xar_add_frombuffer : 444 -> 360
~ _xar_add_folder : 388 -> 312
~ _xar_add_from_archive : 348 -> 360
+ _xar_file_detach
```
