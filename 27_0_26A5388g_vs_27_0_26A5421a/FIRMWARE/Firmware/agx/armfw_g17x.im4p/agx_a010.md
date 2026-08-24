## agx_a010

> `Firmware/agx/armfw_g17x.im4p/agx_a010`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__TEXT.__chain_starts`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x3c74c
+  __TEXT.__text: 0x3cc7c
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
-  __DATA.__zerofill: 0x57ff8
+  __DATA.__zerofill: 0x58018
   __DATA_SHARED_RO._RTK_EXT_SHD_DTA: 0x8000
   Functions: 414
   Symbols:   171
-  CStrings:  229
+  CStrings:  231
 
Functions:
~ sub_fffffc00000036b8 : 12096 -> 12104
~ sub_fffffc000000bfa8 -> sub_fffffc000000bfb0 : 10120 -> 10500
~ sub_fffffc000000f798 -> sub_fffffc000000f91c : 772 -> 764
~ sub_fffffc000000fa9c -> sub_fffffc000000fc18 : 9804 -> 9824
~ sub_fffffc00000122c0 -> sub_fffffc0000012450 : 5088 -> 5132
~ sub_fffffc0000014fac -> sub_fffffc0000015168 : 2116 -> 2164
~ sub_fffffc000001cfc4 -> sub_fffffc000001d1b0 : 1252 -> 1260
~ sub_fffffc000001d8d0 -> sub_fffffc000001dac4 : 668 -> 680
~ sub_fffffc000001de9c -> sub_fffffc000001e09c : 800 -> 784
~ sub_fffffc000001e8bc -> sub_fffffc000001eaac : 2372 -> 2376
~ sub_fffffc0000023560 -> sub_fffffc0000023754 : 384 -> 368
~ sub_fffffc0000024fb0 -> sub_fffffc0000025194 : 556 -> 560
~ sub_fffffc000002753c -> sub_fffffc0000027724 : 7484 -> 8196
~ sub_fffffc0000029278 -> sub_fffffc0000029728 : 1996 -> 2124
CStrings:
+ "Aug 11 2026 21:43:02"
+ "kAGFIPIORegionTypeAFRD2DNIRegisters"
+ "kAGFIPIORegionTypeMTRPMSRegisters"
- "Jul 14 2026 21:22:07"
```
