## AppleAVE2FW_H13D.im4p

> `Firmware/ave/AppleAVE2FW_H13D.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`
- `__DATA.__const`
- `__DATA._rtk_power`

```diff

-  __TEXT.__text: 0xff410
-  __TEXT.__const: 0x22924
-  __TEXT.__cstring: 0x16615
+  __TEXT.__text: 0xff7ac
+  __TEXT.__const: 0x22934
+  __TEXT.__cstring: 0x166cb
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
   __DATA._rtk_patchbay: 0x211
-  __DATA.__data: 0x10b0
+  __DATA.__data: 0x10c8
   __DATA._rtk_mtab: 0x2b8
   __DATA.__const: 0x3be0
   __DATA._rtk_power: 0x3b8

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xd2ee0
-  Functions: 1156
-  Symbols:   1617
-  CStrings:  2546
+  Functions: 1157
+  Symbols:   1619
+  CStrings:  2552
 
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
- "9013.45.1"
```
