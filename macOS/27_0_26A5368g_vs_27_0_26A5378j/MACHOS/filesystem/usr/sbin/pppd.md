## pppd

> `/usr/sbin/pppd`

```diff

-  __TEXT.__text: 0x2ef00
+  __TEXT.__text: 0x2ee78
   __TEXT.__auth_stubs: 0x1190
   __TEXT.__const: 0x708
   __TEXT.__cstring: 0x9be1
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
~ __DATA.__common : content changed
~ __DATA.__bss : content changed
Functions:
~ _auth_ip_addr : 268 -> 264
~ _ChapMS2 : 1136 -> 1144
~ sub_100007778 -> sub_10000777c : 780 -> 772
~ sub_100007a84 -> sub_100007a80 : 332 -> 324
~ sub_100007bd0 -> sub_100007bc4 : 160 -> 156
~ sub_10000c70c -> sub_10000c6fc : 1368 -> 1360
~ _main : 4572 -> 4580
~ _script_setenv : 368 -> 372
~ sub_100012e78 -> sub_100012e6c : 288 -> 296
~ sub_10001302c -> sub_100013028 : 580 -> 572
~ sub_100013560 -> sub_100013554 : 456 -> 392
~ sub_100013850 -> sub_100013804 : 1548 -> 1580
~ _options_for_tty : 284 -> 280
~ _override_value : 104 -> 108
~ sub_10001cfa4 -> sub_10001cf78 : 3048 -> 2968
~ _tdb_error : 96 -> 108
~ _vslprintf : 2764 -> 2772
~ _DesEncrypt : 276 -> 260
~ _DesDecrypt : 276 -> 260

```
