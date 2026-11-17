## AppleVideoEncoder

> `/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-913.64.1.0.0
-  __TEXT.__text: 0x1f35d4
+913.72.1.0.0
+  __TEXT.__text: 0x1f3734
   __TEXT.__auth_stubs: 0x10a0
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0xc
   __TEXT.__const: 0x25528
-  __TEXT.__cstring: 0x5c359
+  __TEXT.__cstring: 0x5c4b1
   __TEXT.__gcc_except_tab: 0x734
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0x2088
+  __TEXT.__unwind_info: 0x2080
   __DATA_CONST.__const: 0xddd0
   __DATA_CONST.__cfstring: 0x3660
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 1994
   Symbols:   501
-  CStrings:  7608
+  CStrings:  7613
 
Functions:
~ sub_13d618 : 3640 -> 3652
~ sub_1636fc -> sub_163708 : 2584 -> 2592
~ sub_166534 -> sub_166548 : 10232 -> 10276
~ sub_17740c -> sub_17744c : 2972 -> 2976
~ sub_1ba82c -> sub_1ba870 : 756 -> 800
~ sub_1c1cb0 -> sub_1c1d20 : 1364 -> 1388
~ sub_1ef544 -> sub_1ef5cc : 508 -> 724
CStrings:
+ "%lld %d AVE %s: %s:%d %s | AVE_MCTF_AdjustStrength failed %p %p %lld %d %d"
+ "%lld %d AVE %s: %s:%d %s | AVE_MCTF_AdjustStrength failed %p %p %lld %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | too many DRL entries %d (max %d)"
+ "%lld %d AVE %s: %s:%d %s | too many DRL entries %d (max %d)\n"
+ "913.72.1"
+ "num <= 2"
+ "pInfo->num_negative_pics <= 16 && pInfo->num_positive_pics <= 16 && (pInfo->num_negative_pics + pInfo->num_positive_pics) <= 16"
- "913.64.1"
- "pInfo->num_negative_pics <= 16 && pInfo->num_positive_pics <= 16"
```
