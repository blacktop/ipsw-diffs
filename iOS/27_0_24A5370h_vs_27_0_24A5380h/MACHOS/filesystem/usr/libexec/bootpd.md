## bootpd

> `/usr/libexec/bootpd`

```diff

-  __TEXT.__text: 0x10fa4
+  __TEXT.__text: 0x10f8c
   __TEXT.__auth_stubs: 0x970
   __TEXT.__const: 0xe8
   __TEXT.__cstring: 0x1ed1
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_1000037b0 : 724 -> 732
~ sub_100004c28 -> sub_100004c30 : 1524 -> 1508
~ sub_10000521c -> sub_100005214 : 308 -> 272
~ sub_100005e28 -> sub_100005dfc : 7544 -> 7548
~ sub_100007e68 -> sub_100007e40 : 128 -> 132
~ sub_10000ad3c -> sub_10000ad18 : 700 -> 708
~ sub_10000cc78 -> sub_10000cc5c : 424 -> 428
~ sub_10000d164 -> sub_10000d14c : 332 -> 360
~ sub_10000d59c -> sub_10000d5a0 : 52 -> 40
~ _SubnetGetOptionPtrAndLength : 96 -> 88
~ _SubnetListCreateWithArray : 1788 -> 1772
~ sub_10000fd28 -> sub_10000fd08 : 164 -> 168
~ sub_100010660 -> sub_100010644 : 652 -> 656

```
