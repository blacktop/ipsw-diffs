## netstat

> `/usr/sbin/netstat`

```diff

-  __TEXT.__text: 0x1b058
+  __TEXT.__text: 0x1afe4
   __TEXT.__auth_stubs: 0x4e0
   __TEXT.__cstring: 0xeebc
   __TEXT.__const: 0x3d8
-  __TEXT.__unwind_info: 0x1f8
+  __TEXT.__unwind_info: 0x200
   __DATA_CONST.__const: 0x14b8
   __DATA_CONST.__auth_got: 0x270
   __DATA_CONST.__got: 0x38
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
~ __DATA.__bss : content changed
Functions:
~ _intpr_ri : 1860 -> 1852
~ _ipsec_hist : 256 -> 232
~ _knownname : 120 -> 104
~ _mbpr : 3280 -> 3212
~ _printb : 232 -> 236
~ _p_sockaddr : 872 -> 868

```
