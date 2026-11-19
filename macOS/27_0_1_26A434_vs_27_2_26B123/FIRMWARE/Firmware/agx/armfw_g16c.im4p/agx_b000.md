## agx_b000

> `Firmware/agx/armfw_g16c.im4p/agx_b000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x51a54
-  __TEXT.__gxf_code: 0x4f40
+  __TEXT.__text: 0x51c8c
+  __TEXT.__gxf_code: 0x50c0
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x12e8
+  __TEXT.__const: 0x132c
   __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
-  __TEXT.__cstring: 0x2f06
+  __TEXT.__cstring: 0x2f23
   __TEXT.__init_offsets: 0x0
-  __TEXT.__chain_starts: 0x1c
-  __DATA.__gxf_data: 0x80b8
+  __TEXT.__chain_starts: 0x20
+  __DATA.__gxf_data: 0x8130
   __DATA.__data: 0x179b8
   __DATA._rtk_init_stack: 0x4000
   __DATA.__const: 0xbb0

   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x5eb78
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
-  Functions: 498
-  Symbols:   169
-  CStrings:  304
+  Functions: 497
+  Symbols:   173
+  CStrings:  305
 
Symbols:
+ _agfUPPLRegisterPageCount
+ _agfUPPLRegisterPages
+ _gClientFunctions
+ _premap_ranges
CStrings:
+ "Oct 14 2026 23:11:47"
+ "uPPL extension %u failed: %d"
- "Aug 30 2026 19:02:49"
```
