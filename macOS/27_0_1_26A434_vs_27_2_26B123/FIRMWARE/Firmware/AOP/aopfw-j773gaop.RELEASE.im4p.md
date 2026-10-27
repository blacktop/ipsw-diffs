## aopfw-j773gaop.RELEASE.im4p

> `Firmware/AOP/aopfw-j773gaop.RELEASE.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA.__const`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`
- `__DATA.__version`
- `__DATA._spu_service`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x8be00
-  __TEXT.__const: 0x84f0
-  __TEXT.__cstring: 0x4c7f
+  __TEXT.__text: 0x8bec8
+  __TEXT.__const: 0x84f4
+  __TEXT.__cstring: 0x4c80
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x28
   __DATA._rtk_boot: 0x3000

   __DATA._rtk_ext_stack: 0x1800
   __DATA._rtk_heap: 0xca20
   __DATA.__const: 0xaac8
-  __DATA.__data: 0x6b30
+  __DATA.__data: 0x6b28
   __DATA._rtk_patchbay: 0x306
   __DATA._rtk_mtab: 0x5f8
   __DATA.__version: 0x8

   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x99960
-  __ETEXT.__text: 0x66f8
+  __ETEXT.__text: 0x66fc
   __ETEXT.__StaticInit: 0xf0c
   __ETEXT.__const: 0x135
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x29b54
+  __OS_LOG.__string: 0x29b53
   __MISC.__apf_list: 0x30
   Functions: 2147
   Symbols:   0
Functions:
~ sub_100b534 : 640 -> 644
~ sub_100f370 -> sub_100f374 : 80 -> 156
~ sub_100f41c -> sub_100f46c : 704 -> 680
~ sub_100ffdc -> sub_1010014 : 392 -> 400
~ sub_10118e0 -> sub_1011920 : 672 -> 676
~ sub_107bdec -> sub_107be30 : 384 -> 388
~ sub_1081020 -> sub_1081068 : 424 -> 460
~ sub_10811c8 -> sub_1081234 : 428 -> 540
~ sub_108759c -> sub_1087678 : 2300 -> 2288
~ sub_108a9dc -> sub_108aaac : 4416 -> 4408
~ sub_108bcc0 -> sub_108bd88 : 320 -> 328
CStrings:
+ "13:48:46"
+ "13:53:11"
+ "AppleSPUFirmware-2444.41.1~32"
+ "Oct  3 2026"
+ "[AUD] RTKitAudioFramework v610.1 ('%s' built %s %s) ready!! {%zu nodes}"
- "13:01:27"
- "13:06:01"
- "AppleSPUFirmware-2444.1.1~64"
- "Aug  8 2026"
- "[AUD] RTKitAudioFramework v601.41 ('%s' built %s %s) ready!! {%zu nodes}"
```
