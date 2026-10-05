## rans.t8160.release.im4p

> `Firmware/rans.t8160.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__chain_starts`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`
- `__DATA.__const`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x20a6ec
+  __TEXT.__text: 0x20a794
   __TEXT.shared: 0xe264
   __TEXT.read: 0x6ad0
   __TEXT.__const: 0x6590
-  __TEXT.__cstring: 0x27c36
+  __TEXT.__cstring: 0x27c38
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x8000

   __DATA._rtk_patchbay: 0x4ad
   __DATA._rtk_tunables: 0xa10
   __DATA._rtk_mtab: 0x330
-  __DATA.__data: 0x83a8
+  __DATA.__data: 0x83b0
   __DATA.__const: 0x1b70
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x17a
Functions:
~ sub_1dc6c : 460 -> 496
~ sub_1de38 -> sub_1de5c : 448 -> 640
~ sub_b82fc -> sub_b83e0 : 83400 -> 83328
~ sub_20c600 -> sub_20c69c : 23920 -> 23932
~ sub_212588 -> sub_212630 : 360 -> 368
CStrings:
+ "3975.40.15"
+ "3975.40.15~155"
+ "AppleStorageFirmware-3975.40.15~155"
- "3975.40.14"
- "3975.40.14~74"
- "AppleStorageFirmware-3975.40.14~74"
```
