## AppleAVE2FW_H16G.im4p

> `Firmware/ave/AppleAVE2FW_H16G.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`
- `__DATA.__const`
- `__DATA._rtk_power`

```diff

-  __TEXT.__text: 0x113d34
-  __TEXT.__const: 0x258f4
-  __TEXT.__cstring: 0x17f0c
+  __TEXT.__text: 0x1140e0
+  __TEXT.__const: 0x25904
+  __TEXT.__cstring: 0x17fe0
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
   __DATA._rtk_patchbay: 0x211
-  __DATA.__data: 0x11b0
+  __DATA.__data: 0x11c8
   __DATA._rtk_mtab: 0x2d0
   __DATA.__const: 0x3cf0
   __DATA._rtk_power: 0x3b8

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc9ba0
-  Functions: 1222
-  Symbols:   1711
-  CStrings:  2713
+  Functions: 1223
+  Symbols:   1713
+  CStrings:  2720
 
Symbols:
+ __ZN11RateControl13updateFixedQPEi
+ __ZN12CRateControl13UpdateFixedQPEi
CStrings:
+ "%s:%d %s | too many parameter sets %d %d %d %p %d"
+ "%s:%s Enter %d"
+ "%s:%s Exit %d"
+ "0 <= iNum && iNum < (1 + ((2) < ((63 + 1)) ? (2) : ((63 + 1))) * (1 + 9 ))"
+ "9013.55.1"
+ "Applying gating for frame: %d"
+ "UpdateFixedQP"
+ "updateFixedQP"
- "9013.45.1"
```
