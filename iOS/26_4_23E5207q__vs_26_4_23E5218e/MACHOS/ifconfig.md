## ifconfig

> `/sbin/ifconfig`

```diff

-741.0.0.0.0
-  __TEXT.__text: 0xbb6c
+741.100.2.0.0
+  __TEXT.__text: 0xbbd4
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__init_offsets: 0x2c
   __TEXT.__const: 0x1f0
-  __TEXT.__cstring: 0x39db
+  __TEXT.__cstring: 0x3a08
   __TEXT.__unwind_info: 0x218
   __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0x38

   __DATA.__common: 0x7c
   __DATA.__bss: 0x1260
   - /usr/lib/libSystem.B.dylib
-  UUID: F350CEA3-B893-39D9-ACF7-0C329B9F428F
+  UUID: 45396985-2DE3-3C85-BC7E-6934B7F927C5
   Functions: 254
   Symbols:   443
-  CStrings:  840
+  CStrings:  841
 
Functions:
~ _main : 8288 -> 8296
~ _setnetem : 840 -> 876
~ _netem_parse_args : 1232 -> 1284
~ _print_netem_params : 408 -> 416
CStrings:
+ "\tdelay latency                  %dms\n\t      jitter                   %dms\n\tcorruption                     %.3f%%\n\treordering                     %.3f%% %dms\n\n\trecovery                       %dms\n"
+ "reordering delay %dms too big (> 1 sec)"
- "\tdelay latency                  %dms\n\t      jitter                   %dms\n\tcorruption                     %.3f%%\n\treordering                     %.3f%%\n\n\trecovery                       %dms\n"

```
