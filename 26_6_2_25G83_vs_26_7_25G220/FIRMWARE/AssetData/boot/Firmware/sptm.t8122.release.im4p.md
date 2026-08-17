## sptm.t8122.release.im4p

> `AssetData/boot/Firmware/sptm.t8122.release.im4p`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__LATE_CONST.__late_const`

```diff

-611.161.4.0.0
-  __TEXT.__cstring: 0x10f26
+611.161.4.700.2
+  __TEXT.__cstring: 0x10e3f
   __TEXT.__const: 0xa80
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
   __DATA_CONST.__const: 0x5838
   __LATE_CONST.__late_const: 0x7c1b0
-  __TEXT_EXEC.__text: 0x58f14
+  __TEXT_EXEC.__text: 0x58e08
   __LAST.__pinst: 0x8
   __DATA.__data: 0xf
   __DATA.__auth_ptr: 0x18

   __BOOTDATA.__data: 0x14000
   Functions: 360
   Symbols:   1
-  CStrings:  2136
+  CStrings:  2132
 
Functions:
~ sub_fffffff0270c0bfc : 540 -> 548
~ sub_fffffff0270cbd68 -> sub_fffffff0270cbd70 : 1036 -> 872
~ sub_fffffff0270d2748 -> sub_fffffff0270d26ac : 948 -> 836
~ sub_fffffff0270f8ee8 -> sub_fffffff0270f8ddc : 56 -> 52
CStrings:
+ "SPTM-611.161.4.700.2|2026-08-10:23:53:46.733886|"
- "%s: dart %p (%s:%u): DART instance %u: SID_CONFIG[%u] 0x%08x does not match shadow 0x%08x"
- "%s: dart %p (%s:%u): DART instance %u: TTBR[%u] 0x%08x does not match shadow 0x%08x"
- "SPTM-611.161.4|2026-07-31:18:16:29.470735|"
- "t8110dart_verify_sid_config"
- "t8110dart_verify_sid_shadow_config"
```
