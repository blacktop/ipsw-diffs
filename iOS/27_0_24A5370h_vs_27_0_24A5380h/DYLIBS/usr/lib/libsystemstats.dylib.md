## libsystemstats.dylib

> `/usr/lib/libsystemstats.dylib`

```diff

-  __TEXT.__text: 0x77ec
+  __TEXT.__text: 0x77f4
   __TEXT.__const: 0x100
   __TEXT.__cstring: 0x6cb
   __TEXT.__gcc_except_tab: 0x1dc
   __TEXT.__oslogstring: 0xd35
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__unwind_info: 0x238
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ sub_2bff7ed1c -> _systemstats_get_microstackshot_cycle_interval_override : 412 -> 352
~ _systemstats_get_microstackshot_cycle_interval_xlog_tasking -> sub_2c1006e7c : 352 -> 412
~ sub_2bff7f14c -> sub_2c100714c : 276 -> 220
~ sub_2bff7f260 -> sub_2c1007228 : 572 -> 276
~ sub_2bff7f49c -> sub_2c100733c : 372 -> 572
~ sub_2bff7f610 -> sub_2c1007578 : 404 -> 372
~ __systemstats_get_file_stats -> sub_2c10076ec : 4 -> 404
~ sub_2bff7f7a8 -> __systemstats_get_file_stats : 220 -> 4
~ sub_2bff7f92c -> sub_2c100792c : 48 -> 56

```
