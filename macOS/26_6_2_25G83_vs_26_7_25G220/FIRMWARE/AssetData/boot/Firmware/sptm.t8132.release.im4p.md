## sptm.t8132.release.im4p

> `AssetData/boot/Firmware/sptm.t8132.release.im4p`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__LATE_CONST.__late_const`

```diff

-611.161.4.0.0
-  __TEXT.__cstring: 0x123c9
+611.161.4.700.2
+  __TEXT.__cstring: 0x122e2
   __TEXT.__const: 0xa80
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
   __DATA_CONST.__const: 0x5ca8
   __LATE_CONST.__late_const: 0x7c260
-  __TEXT_EXEC.__text: 0x5dbb4
+  __TEXT_EXEC.__text: 0x5da88
   __LAST.__pinst: 0x8
   __DATA.__data: 0xf
   __DATA.__auth_ptr: 0x18

   __BOOTDATA.__data: 0x14000
   Functions: 385
   Symbols:   1
-  CStrings:  2291
+  CStrings:  2287
 
Functions:
~ sub_fffffff0270c5fd8 : 348 -> 356
~ sub_fffffff0270ce3cc -> sub_fffffff0270ce3d4 : 1124 -> 960
~ sub_fffffff0270d5544 -> sub_fffffff0270d54a8 : 1052 -> 936
~ sub_fffffff0270e623c -> sub_fffffff0270e612c : 1396 -> 1368
~ sub_fffffff0270fdb88 -> sub_fffffff0270fda5c : 56 -> 52
CStrings:
+ "SPTM-611.161.4.700.2|2026-08-10:23:53:46.733886|"
- "%s: dart %p (%s:%u): DART instance %u: SID_CONFIG[%u] 0x%08x does not match shadow 0x%08x"
- "%s: dart %p (%s:%u): DART instance %u: TTBR[%u] 0x%08x does not match shadow 0x%08x"
- "SPTM-611.161.4|2026-07-31:18:16:29.470735|"
- "t8110dart_verify_sid_config"
- "t8110dart_verify_sid_shadow_config"
```
