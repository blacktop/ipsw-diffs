## sysstatuscheck

> `/usr/libexec/sysstatuscheck`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`

```diff

 233.0.5.0.0
-  __TEXT.__text: 0xd22c
+  __TEXT.__text: 0xd23c
   __TEXT.__auth_stubs: 0x520
   __TEXT.__init_offsets: 0x4
   __TEXT.__gcc_except_tab: 0x61c
Functions:
~ sub_100002a00 : 340 -> 336
~ sub_100002f4c -> sub_100002f48 : 1308 -> 1312
~ sub_100003bd4 : 284 -> 288
~ sub_10000480c -> sub_100004810 : 256 -> 260
~ sub_100004a1c -> sub_100004a24 : 256 -> 260
~ sub_100004ce8 -> sub_100004cf4 : 580 -> 584
```
