## com.apple.kec.pthread

> `com.apple.kec.pthread`

```diff

-539.80.3.0.0
-  __TEXT.__const: 0x48
+539.100.3.0.0
+  __TEXT.__const: 0x40
   __TEXT.__cstring: 0x72d
-  __TEXT_EXEC.__text: 0x5e90
+  __TEXT_EXEC.__text: 0x5c00
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12c
   __DATA.__bss: 0x21

   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x3f8
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: F6E724C0-273C-326B-996D-95B7181DC4BC
+  UUID: E002D896-F1E7-355A-9264-3D9682040ED8
   Functions: 60
   Symbols:   0
   CStrings:  42
Functions:
~ sub_fffffe000b0d6078 -> sub_fffffe000a6ddc98 : 1364 -> 1216
~ _workq_set_register_state : 540 -> 396
~ __psynch_mutexwait : 1120 -> 1060
~ _ksyn_wqfind : 1268 -> 1264
~ _ksyn_queue_insert : 908 -> 876
~ _ksyn_queue_remove_item : 572 -> 564
~ _CLEAR_REINIT_BITS : 168 -> 160
~ __psynch_mutexdrop : 816 -> 800
~ _ksyn_signal : 296 -> 256
~ ___psynch_cvsignal : 1924 -> 1892
~ sub_fffffe000b0d9d14 -> sub_fffffe000a6e1748 : 1084 -> 1064
~ sub_fffffe000b0da150 -> sub_fffffe000a6e1b70 : 144 -> 136
~ sub_fffffe000b0da1e0 -> sub_fffffe000a6e1bf8 : 560 -> 532
~ __psynch_cvwait : 1080 -> 1076
~ sub_fffffe000b0da874 -> sub_fffffe000a6e226c : 616 -> 600
~ sub_fffffe000b0daadc -> sub_fffffe000a6e24c4 : 468 -> 444
~ sub_fffffe000b0dacbc -> sub_fffffe000a6e268c : 808 -> 772
~ _kwq_handle_unlock : 1044 -> 1060
~ sub_fffffe000b0db50c -> sub_fffffe000a6e2ec8 : 248 -> 228
~ sub_fffffe000b0db640 -> sub_fffffe000a6e2fe8 : 692 -> 672
~ sub_fffffe000b0db9a8 -> sub_fffffe000a6e333c : 600 -> 596

```
