## AppleAVE2FW_H13S.im4p

> `AppleAVE2FW_H13S.im4p`

```diff

 
-  __TEXT.__text: 0xbae9c
-  __TEXT.__cstring: 0x114a1
-  __TEXT.__const: 0x1e558
-  __TEXT.__chain_starts: 0x0
+  __TEXT.__text: 0xcb4d0
   __TEXT._rtk_mtab: 0x308
+  __TEXT.__const: 0x1e560
+  __TEXT.__cstring: 0x113c7
   __TEXT.__constructor: 0x0
+  __TEXT.__chain_starts: 0x0
   __DATA.__const: 0x27f8
+  __DATA._rtk_patchbay: 0x228
   __DATA.__data: 0x1188
-  __DATA._rtk_patchbay: 0x208
+  __DATA._rtk_power: 0x368
+  __DATA.__gxf_data: 0x10
+  __DATA._rtk_tunables: 0x1e8
   __DATA._rtk_init_stack: 0x10000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_boot: 0x8000
   __DATA._rtk_page_tables: 0x40000
-  __DATA._rtk_power: 0x368
-  __DATA._rtk_data_uuid: 0x0
-  __DATA._rtk_tunables: 0x1e8
-  __DATA.__gxf_data: 0x10
   __DATA.__mod_init_func: 0x0
   __DATA.__noinit: 0x0
-  __DATA._rtk_threads: 0x0
+  __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_heap: 0x0
+  __DATA._rtk_threads: 0x0
   __DATA.__zerofill: 0xc68b8
-  UUID: 50B60696-E172-3DF5-924B-2BD45A2B00D5
+  UUID: 4B0B9A31-A15C-3BBB-8BB2-100329BD2938
   Functions: 0
-  Symbols:   1378
-  CStrings:  2112
+  Symbols:   1370
+  CStrings:  2110
 
Symbols:
+ __rtk_patch_RTK_platform_flags
+ __rtk_patch__pac_entropy
- __ZN10CAVEClient12CommandQueue8ConvertPEj
- __ZN12CAvePipeMcpu24LoadFirmwareImageDynamicEiib
- __ZN19CPlatformISRManager23HandleSoftwareInterruptEj
- __ZNK14CAVCController15SetLRMERCPerRefEv
- __rtk_arch_unhandled_exception
- __rtk_thread_terminate_self
- __rtk_tracekit_add_trace_vector_event
- __rtk_tracekit_thread_init
- __rtk_tracekit_transition_context
- _putchar
CStrings:
+ "%d %d %d %d %d %d %d %hhu %d %hhu %d %hhu "
+ "%d | %d %d | %d %d | %hhu %d %hhu %d "
+ "%s::%s:%d  %d F %d Type %d POC %d | %d %d | S0 %d %hhu %d %hhu | S1 %d %hhu"
+ "%s::%s:%d %d F %d Type %d POC %d | %d %d | %d %hhu %d %hhu"
+ "%s::%s:%d i %d PicOrderCntVal %d UsedByCurrPicS0 %hhu DeltaPocS0 %d"
+ "%s::%s:%d i %d PicOrderCntVal %d UsedByCurrPicS1 %hhu DeltaPocS1 %d"
+ "%s::%s:%d ptr->UsedByCurrPicS0[%d] %hhu"
+ "8002.41.0"
+ "RPSparams.strps.rps[%d].used_by_curr_pic_s0_flag[%d]  %hhu\n"
+ "RPSparams.strps.rps[%d].used_by_curr_pic_s1_flag[%d]  %hhu\n"
- "%d %d %d %d %d %d %d %d %d %d %d %d "
- "%d | %d %d | %d %d | %d %d %d %d "
- "%s::%s:%d  %d F %d Type %d POC %d | %d %d | S0 %d %d %d %d | S1 %d %d"
- "%s::%s:%d %d F %d Type %d POC %d | %d %d | %d %d %d %d"
- "%s::%s:%d i %d PicOrderCntVal %d UsedByCurrPicS0 %d DeltaPocS0 %d"
- "%s::%s:%d i %d PicOrderCntVal %d UsedByCurrPicS1 %d DeltaPocS1 %d"
- "%s::%s:%d ptr->UsedByCurrPicS0[%d] %d"
- "8002.36.1"
- "RPSparams.strps.rps[%d].used_by_curr_pic_s0_flag[%d]  %d\n"
- "RPSparams.strps.rps[%d].used_by_curr_pic_s1_flag[%d]  %d\n"
- "wp->delta_chroma_offset_l0[i][j] >= -4*WpOffsetHalfRangeC && wp->delta_chroma_offset_l0[i][j] <= (4*WpOffsetHalfRangeC - 1)"
- "wp->delta_chroma_offset_l1[i][j] >= -4*WpOffsetHalfRangeC && wp->delta_chroma_offset_l1[i][j] <= (4*WpOffsetHalfRangeC - 1)"

```
