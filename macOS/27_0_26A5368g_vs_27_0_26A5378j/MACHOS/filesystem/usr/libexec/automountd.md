## automountd

> `/usr/libexec/automountd`

```diff

-  __TEXT.__text: 0x14530
+  __TEXT.__text: 0x145c8
   __TEXT.__auth_stubs: 0xd00
   __TEXT.__const: 0x208
   __TEXT.__oslogstring: 0x347
-  __TEXT.__cstring: 0x3bf4
+  __TEXT.__cstring: 0x3c23
   __TEXT.__unwind_info: 0x288
   __DATA_CONST.__const: 0x6c8
   __DATA_CONST.__cfstring: 0x20

   - /usr/lib/libutil.dylib
   Functions: 221
   Symbols:   235
-  CStrings:  581
+  CStrings:  585
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100000e90 : 848 -> 836
~ sub_100001684 -> sub_100001678 : 1384 -> 1396
~ sub_10000344c : 1296 -> 1272
~ sub_10000395c -> sub_100003944 : 560 -> 536
~ sub_100007c34 -> sub_100007c04 : 2340 -> 2316
~ sub_100008700 -> sub_1000086b8 : 3212 -> 3396
~ sub_10000e488 -> sub_10000e4f8 : 2140 -> 2156
~ sub_1000105f4 -> sub_100010674 : 196 -> 188
~ sub_1000106b8 -> sub_100010730 : 376 -> 356
~ sub_100010bd4 -> sub_100010c38 : 496 -> 548
CStrings:
+ ".."
+ "AUTOMOUNTD_NODEV="
+ "Invalid fstype [%s]"
+ "nodev"

```
