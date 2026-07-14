## sptm.t8150.release.im4p

> `Firmware/sptm.t8150.release.im4p`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__LATE_CONST.__late_const`

```diff

-  __TEXT.__cstring: 0x12639
+  __TEXT.__cstring: 0x12725
   __TEXT.__const: 0xa80
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x24
   __DATA_CONST.__const: 0x5ca8
   __LATE_CONST.__late_const: 0x7c1f0
-  __TEXT_EXEC.__text: 0x5f754
+  __TEXT_EXEC.__text: 0x5f86c
   __LAST.__pinst: 0x8
   __DATA.__data: 0xf
   __DATA.__auth_ptr: 0x18

   __BOOTDATA.__data: 0x14000
   Functions: 393
   Symbols:   1
-  CStrings:  2317
+  CStrings:  2321
 
Functions:
~ sub_fffffff0270cf270 : 956 -> 1120
~ sub_fffffff0270d6368 -> sub_fffffff0270d640c : 932 -> 1048
~ sub_fffffff0270ff728 -> sub_fffffff0270ff840 : 56 -> 48
CStrings:
+ "%s: dart %p (%s:%u): DART instance %u: SID_CONFIG[%u] 0x%08x does not match shadow 0x%08x"
+ "%s: dart %p (%s:%u): DART instance %u: TTBR[%u] 0x%08x does not match shadow 0x%08x"
+ "SPTM-611.162.3|2026-07-09:23:17:37.791119|"
+ "t8110dart_verify_sid_config"
+ "t8110dart_verify_sid_shadow_config"
- "SPTM-611.160.18|2026-06-26:15:30:10.716031|"
```
