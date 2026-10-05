## AppleAVE2FW_H19.im4p

> `Firmware/ave/AppleAVE2FW_H19.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`
- `__DATA.__const`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x118cdc
+  __TEXT.__text: 0x1190b0
   __TEXT.__const: 0x1dc34
-  __TEXT.__cstring: 0x1a2cd
+  __TEXT.__cstring: 0x1a383
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_patchbay: 0x21a
-  __DATA.__data: 0x1250
+  __DATA.__data: 0x1268
   __DATA._rtk_mtab: 0x298
   __DATA.__const: 0x7598
   __DATA._rtk_power: 0x3b8

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc68e0
-  Functions: 1319
-  Symbols:   1800
-  CStrings:  2942
+  Functions: 1321
+  Symbols:   1802
+  CStrings:  2948
 
Symbols:
+ __ZN11RateControl13updateFixedQPEi
+ __ZN12CRateControl13UpdateFixedQPEi
CStrings:
+ "%s:%d %s | too many parameter sets %d %d %d %p %d"
+ "%s:%s Enter %d"
+ "%s:%s Exit %d"
+ "0 <= iNum && iNum < (1 + ((2) < ((63 + 1)) ? (2) : ((63 + 1))) * (1 + 9 ))"
+ "9013.55.1"
+ "UpdateFixedQP"
+ "updateFixedQP"
- "9013.48.1"
```
