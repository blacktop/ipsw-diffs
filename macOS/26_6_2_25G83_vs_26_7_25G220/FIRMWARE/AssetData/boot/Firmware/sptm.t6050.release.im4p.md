## sptm.t6050.release.im4p

> `AssetData/boot/Firmware/sptm.t6050.release.im4p`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__LATE_CONST.__late_const`

```diff

-611.161.4.0.0
-  __TEXT.__cstring: 0x127e8
+611.161.4.700.2
+  __TEXT.__cstring: 0x12701
   __TEXT.__const: 0xa80
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
   __DATA_CONST.__const: 0x5ca8
   __LATE_CONST.__late_const: 0x7c5b0
-  __TEXT_EXEC.__text: 0x5eeec
+  __TEXT_EXEC.__text: 0x5ee00
   __LAST.__pinst: 0x8
   __DATA.__data: 0xf
   __DATA.__auth_ptr: 0x18

   __BOOTDATA.__data: 0x14000
   Functions: 394
   Symbols:   1
-  CStrings:  2323
+  CStrings:  2319
 
Functions:
~ sub_fffffff0270c0ec8 : 888 -> 952
~ sub_fffffff0270c643c -> sub_fffffff0270c647c : 340 -> 348
~ sub_fffffff0270ce964 -> sub_fffffff0270ce9ac : 1120 -> 956
~ sub_fffffff0270d5b00 -> sub_fffffff0270d5aa4 : 1048 -> 932
~ sub_fffffff0270e61f0 -> sub_fffffff0270e6120 : 1396 -> 1368
~ sub_fffffff0270feec0 -> sub_fffffff0270fedd4 : 48 -> 44
CStrings:
+ "SPTM-611.161.4.700.2|2026-08-10:23:53:46.733886|"
- "%s: dart %p (%s:%u): DART instance %u: SID_CONFIG[%u] 0x%08x does not match shadow 0x%08x"
- "%s: dart %p (%s:%u): DART instance %u: TTBR[%u] 0x%08x does not match shadow 0x%08x"
- "SPTM-611.161.4|2026-07-31:18:16:29.470735|"
- "t8110dart_verify_sid_config"
- "t8110dart_verify_sid_shadow_config"
```
