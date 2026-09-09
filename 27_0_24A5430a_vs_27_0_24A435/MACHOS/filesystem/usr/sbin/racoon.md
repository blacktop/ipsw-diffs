## racoon

> `/usr/sbin/racoon`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

 1130.0.0.0.0
-  __TEXT.__text: 0x62f28
+  __TEXT.__text: 0x62f40
   __TEXT.__auth_stubs: 0x1060
   __TEXT.__const: 0x70ea
   __TEXT.__oslogstring: 0xc479
Functions:
~ sub_100018e2c : 856 -> 860
~ sub_100023ad8 -> sub_100023adc : 1216 -> 1220
~ sub_10003a6c8 -> sub_10003a6d0 : 316 -> 320
~ sub_10004d4d8 -> sub_10004d4e4 : 8984 -> 8996
~ sub_100052e30 -> sub_100052e48 : 44 -> 28
~ sub_100052e5c -> sub_100052e64 : 28 -> 44
```
