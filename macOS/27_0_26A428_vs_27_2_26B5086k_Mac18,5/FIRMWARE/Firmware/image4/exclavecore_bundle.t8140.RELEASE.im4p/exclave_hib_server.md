## exclave_hib_server

> `Firmware/image4/exclavecore_bundle.t8140.RELEASE.im4p/exclave_hib_server`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA.__auth_ptr`
- `__DATA.__mod_init_func`

```diff

-1490.0.21.0.0
-  __TEXT.__text: 0x3eda8
+1490.40.21.0.0
+  __TEXT.__text: 0x3ec3c
   __TEXT.__const: 0x1c910
-  __TEXT.__cstring: 0xde78
+  __TEXT.__cstring: 0xdeda
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0

   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  Functions: 871
+  Functions: 870
   Symbols:   4
-  CStrings:  1240
+  CStrings:  1244
 
CStrings:
+ "!DO_CHUNKS_OVERLAP(currp, victimp) && !DO_CHUNKS_OVERLAP(currp->next, victimp)"
+ "!os_add_overflow(round_bytes, HEADER_UNIT_SIZE * UNIT_SIZE, &alloc_bytes)"
+ "!os_mul_overflow(units, UNIT_SIZE, &nb)"
+ "!overflow"
+ "_insecure_random_buf"
+ "lcm"
+ "round_bytes >= alloc_bytes"
+ "s[0] || s[1]"
- "!(alignment % sizeof(Header)) && !(alignment % UNIT_SIZE)"
- "!os_mul_overflow(nu + PAD_ALLOC(align), UNIT_SIZE, &nb)"
- "alloc_bytes >= sz"
- "p->size * UNIT_SIZE >= sizeof(Header)"
```
