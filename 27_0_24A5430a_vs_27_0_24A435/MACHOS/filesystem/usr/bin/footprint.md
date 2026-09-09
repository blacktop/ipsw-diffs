## footprint

> `/usr/bin/footprint`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`

```diff

 365.0.0.0.0
-  __TEXT.__text: 0x215c0
+  __TEXT.__text: 0x215c8
   __TEXT.__auth_stubs: 0xcf0
   __TEXT.__objc_stubs: 0x2560
   __TEXT.__objc_methlist: 0x131c
Functions:
~ -[FPUserProcess _enumerateDispositionChunksWithStartAddr:pagesToQuery:block:] : 392 -> 400
~ ___33-[FPUserProcess _gatherImageData]_block_invoke_2 : 1576 -> 1584
~ -[FPBootCarveout _gatherData:extendedInfoProvider:] : 4256 -> 4240
~ -[FPKernelProcess _gatherData:extendedInfoProvider:] : 2604 -> 2608
~ _enumerateObjects : 324 -> 328
```
