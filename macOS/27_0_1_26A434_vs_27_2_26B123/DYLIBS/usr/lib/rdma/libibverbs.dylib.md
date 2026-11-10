## libibverbs.dylib

> `/usr/lib/rdma/libibverbs.dylib`

```diff

-112.1.1.0.0
-  __TEXT.__text: 0xd728
-  __TEXT.__cstring: 0x12a9
+112.40.17.0.0
+  __TEXT.__text: 0xd79c
+  __TEXT.__cstring: 0x1285
   __TEXT.__const: 0x1f8
   __TEXT.__unwind_info: 0x330
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/rdma/libccan.dylib
   Functions: 385
   Symbols:   477
-  CStrings:  214
+  CStrings:  212
 
Symbols:
+ _ibv_darwin_set_resolver_ifname
- _darwin_bind_interface
Functions:
~ _darwin_bind_interface -> _ibv_darwin_set_resolver_ifname : 180 -> 296
CStrings:
- "%s: failed %u\n"
- "darwin_bind_interface"
```
