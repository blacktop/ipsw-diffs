## aopfw-mac13gaop.RELEASE.im4p

> `Firmware/AOP/aopfw-mac13gaop.RELEASE.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA.__const`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`
- `__DATA.__version`
- `__DATA._spu_service`
- `__DATA._spu_endpoint`
- `__DATA._rtk_power`

```diff

-  __TEXT.__text: 0x74018
-  __TEXT.__const: 0x4638
+  __TEXT.__text: 0x740e4
+  __TEXT.__const: 0x4648
   __TEXT.__cstring: 0x144e4
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x2c

   __DATA._rtk_ext_stack: 0x1800
   __DATA._rtk_heap: 0xe368
   __DATA.__const: 0x7850
-  __DATA.__data: 0x8650
+  __DATA.__data: 0x8648
   __DATA._rtk_patchbay: 0x333
   __DATA._rtk_mtab: 0x610
   __DATA.__version: 0x8
Functions:
~ sub_10124a4 : 264 -> 268
~ sub_10172f4 -> sub_10172f8 : 80 -> 156
~ sub_1017398 -> sub_10173e8 : 684 -> 660
~ sub_101ca38 -> sub_101ca70 : 564 -> 568
~ sub_10538e0 -> sub_105391c : 644 -> 648
~ sub_1065b30 -> sub_1065b70 : 424 -> 460
~ sub_1065cd8 -> sub_1065d3c : 428 -> 540
~ sub_10724d4 -> sub_10725a8 : 5872 -> 5864
~ sub_1073ebc -> sub_1073f88 : 356 -> 348
CStrings:
+ "13:47:50"
+ "AppleSPUFirmware-2444.41.1~32"
+ "Oct  3 2026"
+ "RTKitAudioFramework v610.1 ('%s' built %s %s) ready!! {%zu nodes}"
- "13:00:42"
- "AppleSPUFirmware-2444.1.1~64"
- "Aug  8 2026"
- "RTKitAudioFramework v601.41 ('%s' built %s %s) ready!! {%zu nodes}"
```
