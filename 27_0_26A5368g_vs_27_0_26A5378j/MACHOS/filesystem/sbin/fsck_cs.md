## fsck_cs

> `/sbin/fsck_cs`

```diff

-  __TEXT.__text: 0x158f0
+  __TEXT.__text: 0x15920
   __TEXT.__auth_stubs: 0x880
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x500
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100002dbc : 1856 -> 1864
~ sub_10000468c -> sub_100004694 : 616 -> 628
~ sub_10000d748 -> sub_10000d75c : 304 -> 292
~ sub_10000d988 -> sub_10000d990 : 972 -> 984
~ sub_10000dda0 -> sub_10000ddb4 : 500 -> 504
~ sub_100010e18 -> sub_100010e30 : 500 -> 508
~ sub_100015c68 -> sub_100015c88 : 816 -> 832

```
