## ifconfig

> `/sbin/ifconfig`

```diff

-  __TEXT.__text: 0xbc94
+  __TEXT.__text: 0xbc20
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__init_offsets: 0x2c
   __TEXT.__const: 0x1f0
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _bond_status : 772 -> 740
~ _main : 8308 -> 8300
~ _printb : 228 -> 232
~ _setifsubfamily : 236 -> 256
~ _netem_parse_args : 1356 -> 1296
~ _setmedia : 376 -> 368
~ _domediaopt : 492 -> 484
~ _get_subtype_desc : 112 -> 96
~ _bridge_status : 3296 -> 3288

```
