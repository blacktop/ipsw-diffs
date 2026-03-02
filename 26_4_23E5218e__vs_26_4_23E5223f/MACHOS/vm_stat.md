## vm_stat

> `/usr/bin/vm_stat`

```diff

-1042.100.6.0.0
-  __TEXT.__text: 0xc04
-  __TEXT.__auth_stubs: 0x110
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x55a
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x88
+1042.100.6.0.1
+  __TEXT.__text: 0x938
+  __TEXT.__auth_stubs: 0xf0
+  __TEXT.__const: 0x50
+  __TEXT.__cstring: 0x37d
+  __TEXT.__unwind_info: 0x70
+  __DATA_CONST.__auth_got: 0x78
   __DATA_CONST.__got: 0x30
-  __DATA.__common: 0x208
+  __DATA.__common: 0x200
   __DATA.__bss: 0x4
   - /usr/lib/libSystem.B.dylib
-  UUID: 71AAB81F-F60A-317D-B02F-8201FD18A749
+  UUID: 9B169164-16F7-31A0-99F1-8560318F5041
   Functions: 8
-  Symbols:   25
-  CStrings:  81
+  Symbols:   23
+  CStrings:  57
 
Symbols:
- _mach_error_string
- _sysctlbyname
Functions:
~ sub_1000005d8 : 380 -> 316
~ sub_100000754 -> sub_100000714 : 920 -> 624
~ sub_100000aec -> sub_100000984 : 728 -> 532
~ sub_100000e08 -> sub_100000bdc : 508 -> 360
~ sub_100001190 -> sub_100000ed0 : 76 -> 64
CStrings:
+ "%-30s %16llu.\n"
+ "%8s %8s %8s %8s %8s %8s %8s %8s %8s %8s %8s %8s %11s %9s %8s %8s %8s %8s %8s %8s %8s %8s\n"
+ "%s: failed to get statistics. error %d\n"
- " %8s %9s %12s %11s %8s %8s %13s %14s %11s %10s %11s"
- "%-35s %16llu.\n"
- "%8s %8s %8s %8s %8s %8s %8s %8s %8s %8s %8s %8s %11s %9s %8s %8s %8s %8s %8s %8s %8s %8s"
- "%s: failed to get statistics. error %s\n"
- "Bytes of compressed tags:"
- "Pages tag-storage free:"
- "Pages tag-storage holding tags:"
- "Pages tag-storage non-tag pageable:"
- "Pages tag-storage non-tag wired:"
- "Pages tag-storage:"
- "Pages tagged compressed:"
- "Pages tagged resident:"
- "Pages tagged:"
- "Tagged compressions:"
- "Tagged decompressions:"
- "cmprsd-tags"
- "hw.optional.arm.FEAT_MTE2"
- "tag-storage"
- "tagged"
- "tgd-cmprssed"
- "tgd-comprs"
- "tgd-dcomprs"
- "tgd-rsdnt"
- "tgs-free"
- "tgs-ntag-pgbl"
- "tgs-ntag-wired"
- "tgs-tags"

```
