## AppleAVE2FW_H18G.im4p

> `Firmware/ave/AppleAVE2FW_H18G.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`
- `__DATA.__const`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x118ac8
-  __TEXT.__const: 0x17ab8
-  __TEXT.__cstring: 0x1a2ff
+  __TEXT.__text: 0x118e64
+  __TEXT.__const: 0x17ac8
+  __TEXT.__cstring: 0x1a3d6
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_patchbay: 0x21a
-  __DATA.__data: 0x1248
+  __DATA.__data: 0x1260
   __DATA._rtk_mtab: 0x298
   __DATA.__const: 0x7bd0
   __DATA._rtk_power: 0x3b8

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc68e0
-  Functions: 1319
-  Symbols:   1800
-  CStrings:  2939
+  Functions: 1320
+  Symbols:   1802
+  CStrings:  2946
 
Symbols:
+ __ZN11RateControl13updateFixedQPEi
+ __ZN12CRateControl13UpdateFixedQPEi
CStrings:
+ "%s:%d %s | too many parameter sets %d %d %d %p %d"
+ "%s:%d stopping CtxSched time out %d %d 0x%x"
+ "%s:%s Enter %d"
+ "%s:%s Exit %d"
+ "0 <= iNum && iNum < (1 + ((2) < ((63 + 1)) ? (2) : ((63 + 1))) * (1 + 9 ))"
+ "9013.55.1"
+ "Applying gating for frame: %d"
+ "UpdateFixedQP"
+ "updateFixedQP"
- "%s:%d stopping CtxSched time out %d 0x%x"
- "9013.45.1"
```
