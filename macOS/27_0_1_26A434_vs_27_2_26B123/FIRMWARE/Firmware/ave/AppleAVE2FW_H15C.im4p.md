## AppleAVE2FW_H15C.im4p

> `Firmware/ave/AppleAVE2FW_H15C.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`
- `__DATA.__const`
- `__DATA._rtk_power`

```diff

-  __TEXT.__text: 0x1120fc
-  __TEXT.__const: 0x25e34
-  __TEXT.__cstring: 0x17dc5
+  __TEXT.__text: 0x1124a8
+  __TEXT.__const: 0x25e44
+  __TEXT.__cstring: 0x17e99
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
   __DATA._rtk_patchbay: 0x211
-  __DATA.__data: 0x11b0
+  __DATA.__data: 0x11c8
   __DATA._rtk_mtab: 0x2d0
   __DATA.__const: 0x3ce0
   __DATA._rtk_power: 0x3b8

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xd3720
-  Functions: 1222
-  Symbols:   1710
-  CStrings:  2708
+  Functions: 1223
+  Symbols:   1712
+  CStrings:  2715
 
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
