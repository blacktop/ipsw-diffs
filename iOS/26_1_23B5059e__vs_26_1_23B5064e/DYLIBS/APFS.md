## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/APFS`

```diff

-2632.40.13.0.1
-  __TEXT.__text: 0x50554
+2632.40.15.0.1
+  __TEXT.__text: 0x50694
   __TEXT.__auth_stubs: 0xb60
-  __TEXT.__const: 0x8410
-  __TEXT.__cstring: 0xdda4
+  __TEXT.__const: 0x8420
+  __TEXT.__cstring: 0xdde9
   __TEXT.__oslogstring: 0xb0e
-  __TEXT.__gcc_except_tab: 0x18
+  __TEXT.__gcc_except_tab: 0x1c
   __TEXT.__unwind_info: 0x918
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x4e8
   __AUTH_CONST.__auth_got: 0x5b8
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x1160
+  __AUTH_CONST.__cfstring: 0x1180
   __DATA.__data: 0x98
   __DATA.__bss: 0x40
   __DATA.__common: 0x418

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: E3666BAD-280E-3D1B-B04F-4D4F099E9F05
+  UUID: AD70A29E-FFC5-3206-B371-21CBF6D16DE6
   Functions: 809
-  Symbols:   1764
-  CStrings:  1442
+  Symbols:   1765
+  CStrings:  1445
 
Symbols:
+ __ZL16s_strUnpackTable
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
Functions:
~ _set_metric_default_values : 172 -> 160
~ _cleanup_metrics : 80 -> 96
~ _print_additional_migrator_metrics : 3500 -> 3556
~ _APFSVolumeConvertToUserCrypto : 636 -> 644
~ __ZN16MetricsCompactor6ImportEPKcR7metricsP12Perfcounters : 2644 -> 2688
~ __ZN16MetricsCompactor4ReadERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 156 -> 380
~ _MetricsCompactor_Import : 144 -> 128
CStrings:
+ "%@msg='%s' "
+ "2632.40.15.0.1"
+ "? 01234567890abcdefghijklmnopqrstuvwxyz+-*/_'#$&%()=[]\"\\"
- "2632.40.13.0.1"

```
