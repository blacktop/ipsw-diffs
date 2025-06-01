## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

```diff

-208.60.13.0.2
+208.80.5.0.0
   __TEXT.__os_log: 0x1190
   __TEXT.__cstring: 0x1d00
   __TEXT.__const: 0x270
-  __TEXT_EXEC.__text: 0x19b2c
+  __TEXT_EXEC.__text: 0x19b58
   __TEXT_EXEC.__auth_stubs: 0xf10
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1688
   __DATA_CONST.__kalloc_type: 0xb40
-  UUID: 26620D80-27B5-309E-86FA-905D94596194
+  UUID: C229A0F6-8610-3976-ACDD-97B3D9C8C72D
   Functions: 302
   Symbols:   2784
   CStrings:  352
Symbols:
+ lifs_create_endio_context.kalloc_type_view_857
+ lifs_destroy_endio_context.kalloc_type_view_876
+ lifs_koio_done.kalloc_type_view_1839
+ lifs_reclaim_done.kalloc_type_view_4107
+ lifs_submit_io.kalloc_type_view_1810
+ lifs_submit_koio.kalloc_type_view_1864
+ lifs_vnop_readdir.kalloc_type_view_2533
+ lifs_vnop_readdir.kalloc_type_view_2535
+ lifs_vnop_readdir.kalloc_type_view_2617
+ lifs_vnop_readdir.kalloc_type_view_2619
+ lifs_vnop_reclaim.kalloc_type_view_4151
+ lifs_vnop_reclaim.kalloc_type_view_4203
+ lifs_vnop_strategy.kalloc_type_view_1921
+ lifs_vnop_strategy_done.kalloc_type_view_1674
- lifs_create_endio_context.kalloc_type_view_853
- lifs_destroy_endio_context.kalloc_type_view_872
- lifs_koio_done.kalloc_type_view_1835
- lifs_reclaim_done.kalloc_type_view_4103
- lifs_submit_io.kalloc_type_view_1806
- lifs_submit_koio.kalloc_type_view_1860
- lifs_vnop_readdir.kalloc_type_view_2529
- lifs_vnop_readdir.kalloc_type_view_2531
- lifs_vnop_readdir.kalloc_type_view_2613
- lifs_vnop_readdir.kalloc_type_view_2615
- lifs_vnop_reclaim.kalloc_type_view_4147
- lifs_vnop_reclaim.kalloc_type_view_4199
- lifs_vnop_strategy.kalloc_type_view_1917
- lifs_vnop_strategy_done.kalloc_type_view_1670

```
