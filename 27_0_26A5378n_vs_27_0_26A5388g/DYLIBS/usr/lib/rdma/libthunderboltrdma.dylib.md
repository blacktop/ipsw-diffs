## libthunderboltrdma.dylib

> `/usr/lib/rdma/libthunderboltrdma.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`

```diff

-53.0.0.0.0
-  __TEXT.__text: 0x3ad0
+58.0.0.0.0
+  __TEXT.__text: 0x3b00
   __TEXT.__init_offsets: 0x4
-  __TEXT.__const: 0x30
-  __TEXT.__oslogstring: 0xc30
+  __TEXT.__const: 0x28
+  __TEXT.__oslogstring: 0xbce
   __TEXT.__cstring: 0x7c
-  __TEXT.__unwind_info: 0xc8
+  __TEXT.__unwind_info: 0xc0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__got: 0x0

   - /usr/lib/rdma/libibverbs.dylib
   Functions: 94
   Symbols:   102
-  CStrings:  82
+  CStrings:  80
 
Functions:
~ _tbt_post_recv : 888 -> 768
~ _tbt_post_send : 940 -> 860
~ _tbt_poll_qp_send : 300 -> 404
~ _tbt_poll_qp_recv : 504 -> 632
~ tbt_poll_qp_recv.cold.1 : 52 -> 60
~ tbt_poll_qp_recv.cold.2 : 52 -> 60
CStrings:
- "post_recv: sge->addr=0x%llx sgeDVA=0x%llx len=%u"
- "post_send: sge->addr=0x%llx sgeDVA=0x%llx len=%u"
```
