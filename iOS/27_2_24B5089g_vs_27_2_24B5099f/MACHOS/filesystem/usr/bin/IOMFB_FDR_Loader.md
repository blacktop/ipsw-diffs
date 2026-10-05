## IOMFB_FDR_Loader

> `/usr/bin/IOMFB_FDR_Loader`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-700.50.104.1.0
-  __TEXT.__text: 0x343b8
+700.50.108.0.0
+  __TEXT.__text: 0x34408
   __TEXT.__auth_stubs: 0x720
   __TEXT.__gcc_except_tab: 0x3e0
   __TEXT.__const: 0x1c00
-  __TEXT.__cstring: 0x8fa2
+  __TEXT.__cstring: 0x8fea
   __TEXT.__unwind_info: 0x810
   __DATA_CONST.__const: 0x2b40
   __DATA_CONST.__cfstring: 0x4a0
Functions:
~ sub_1000083f0 : 100 -> 144
~ sub_1000229dc -> sub_100022a08 : 240 -> 276
CStrings:
+ "Parser SetBlock failed with ret=0x%x, pbt=%d, data=%p, block_size=%u, indexes=%p, nindex=%u"
+ "Parser e: failed to set PTUC TLS RR LUT dbv_nits=%d, attempt %u/%u\n"
- "Parser SetBlock failed with 0x%x"
- "Parser e: failed to set PTUC TLS RR LUT brightness %d\n"
```
