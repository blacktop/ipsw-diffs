## agx_a000

> `Firmware/agx/armfw_g17x.im4p/agx_a000`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__TEXT.__chain_starts`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3cac8
+  __TEXT.__text: 0x3cff8
   __TEXT.__gxf_code: 0x4f40
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x560
-  __TEXT.__const: 0x11a0
+  __TEXT.__const: 0x11c0
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
-  __TEXT.__cstring: 0x21b9
+  __TEXT.__cstring: 0x21ff
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__gxf_data: 0x80b8
-  __DATA.__data: 0x17580
+  __DATA.__data: 0x17da0
   __DATA._rtk_init_stack: 0x4000
-  __DATA.__const: 0x7b8
+  __DATA.__const: 0x7d8
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x580f8
+  __DATA.__zerofill: 0x58118
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 415
   Symbols:   171
-  CStrings:  229
+  CStrings:  231
 
Functions:
~ sub_fffffc0000003794 : 12140 -> 12148
~ sub_fffffc000000c1fc -> sub_fffffc000000c204 : 10120 -> 10500
~ sub_fffffc000000f9ec -> sub_fffffc000000fb70 : 772 -> 764
~ sub_fffffc000000fcf0 -> sub_fffffc000000fe6c : 9804 -> 9824
~ sub_fffffc0000012514 -> sub_fffffc00000126a4 : 5088 -> 5132
~ sub_fffffc0000015200 -> sub_fffffc00000153bc : 2116 -> 2164
~ sub_fffffc000001d218 -> sub_fffffc000001d404 : 1252 -> 1260
~ sub_fffffc000001db24 -> sub_fffffc000001dd18 : 668 -> 680
~ sub_fffffc000001e0f0 -> sub_fffffc000001e2f0 : 800 -> 784
~ sub_fffffc000001eb10 -> sub_fffffc000001ed00 : 2372 -> 2376
~ sub_fffffc00000238dc -> sub_fffffc0000023ad0 : 384 -> 368
~ sub_fffffc000002532c -> sub_fffffc0000025510 : 556 -> 560
~ sub_fffffc00000278b8 -> sub_fffffc0000027aa0 : 7484 -> 8196
~ sub_fffffc00000295f4 -> sub_fffffc0000029aa4 : 1996 -> 2124
CStrings:
+ "Aug 11 2026 21:50:49"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
+ "kAGFIPIORegionTypeMTRPMSRegisters"
- "Jul 14 2026 21:29:10"
```
