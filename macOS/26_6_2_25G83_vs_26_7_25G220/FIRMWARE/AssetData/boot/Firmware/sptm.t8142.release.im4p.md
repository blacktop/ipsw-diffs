## sptm.t8142.release.im4p

> `AssetData/boot/Firmware/sptm.t8142.release.im4p`

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
   __LATE_CONST.__late_const: 0x7c270
-  __TEXT_EXEC.__text: 0x5ee08
+  __TEXT_EXEC.__text: 0x5ed1c
   __LAST.__pinst: 0x8
   __DATA.__data: 0xf
   __DATA.__auth_ptr: 0x18

   __BOOTDATA.__data: 0x14000
   Functions: 394
   Symbols:   1
-  CStrings:  2323
+  CStrings:  2319
 
Functions:
~ sub_fffffff0270c0f54 : 884 -> 948
~ sub_fffffff0270c61c0 -> sub_fffffff0270c6200 : 340 -> 348
~ sub_fffffff0270ce6e8 -> sub_fffffff0270ce730 : 1120 -> 956
~ sub_fffffff0270d5884 -> sub_fffffff0270d5828 : 1048 -> 932
~ sub_fffffff0270e610c -> sub_fffffff0270e603c : 1396 -> 1368
~ sub_fffffff0270feddc -> sub_fffffff0270fecf0 : 52 -> 48
CStrings:
+ "SPTM-611.161.4.700.2|2026-08-10:23:53:46.733886|"
- "%s: dart %p (%s:%u): DART instance %u: SID_CONFIG[%u] 0x%08x does not match shadow 0x%08x"
- "%s: dart %p (%s:%u): DART instance %u: TTBR[%u] 0x%08x does not match shadow 0x%08x"
- "SPTM-611.161.4|2026-07-31:18:16:29.470735|"
- "t8110dart_verify_sid_config"
- "t8110dart_verify_sid_shadow_config"
```
