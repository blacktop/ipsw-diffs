## AppleAVE2FW_H16C.im4p

> `Firmware/ave/AppleAVE2FW_H16C.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`
- `__DATA.__const`
- `__DATA._rtk_power`

```diff

-  __TEXT.__text: 0x113e14
-  __TEXT.__const: 0x27774
-  __TEXT.__cstring: 0x17f3c
+  __TEXT.__text: 0x1141d0
+  __TEXT.__const: 0x27784
+  __TEXT.__cstring: 0x18010
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
   __DATA.__zerofill: 0xccf60
-  Functions: 1223
-  Symbols:   1713
-  CStrings:  2715
+  Functions: 1224
+  Symbols:   1715
+  CStrings:  2722
 
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
