## tzinit

> `/usr/libexec/tzinit`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`

```diff

 90.0.0.0.0
-  __TEXT.__text: 0x102dc
+  __TEXT.__text: 0x102ec
   __TEXT.__auth_stubs: 0x520
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x726
Functions:
~ sub_100007078 : 340 -> 336
~ sub_1000074b8 -> sub_1000074b4 : 284 -> 288
~ sub_10000dc30 : 1308 -> 1312
~ sub_10000ead0 -> sub_10000ead4 : 256 -> 260
~ sub_10000ece0 -> sub_10000ece8 : 256 -> 260
~ sub_10000efac -> sub_10000efb8 : 580 -> 584
```
