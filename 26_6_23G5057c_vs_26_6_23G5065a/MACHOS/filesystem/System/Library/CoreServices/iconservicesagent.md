## iconservicesagent

> `/System/Library/CoreServices/iconservicesagent`

```diff

-  __TEXT.__text: 0x5a88
+  __TEXT.__text: 0x5c68
   __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_stubs: 0x1460
   __TEXT.__objc_methlist: 0x434
-  __TEXT.__const: 0x58
+  __TEXT.__const: 0x68
   __TEXT.__cstring: 0x411
-  __TEXT.__oslogstring: 0x8f2
-  __TEXT.__gcc_except_tab: 0xb0
+  __TEXT.__oslogstring: 0xa22
+  __TEXT.__gcc_except_tab: 0x15c
   __TEXT.__objc_classname: 0xb6
   __TEXT.__objc_methtype: 0x3ae
   __TEXT.__objc_methname: 0x1343
-  __TEXT.__unwind_info: 0x1c0
+  __TEXT.__unwind_info: 0x1c8
   __DATA_CONST.__auth_got: 0x2e8
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__const: 0x268

   - /usr/lib/libobjc.A.dylib
   Functions: 112
   Symbols:   153
-  CStrings:  480
+  CStrings:  483
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100001e48 : 2204 -> 2280
~ sub_10000442c -> sub_100004478 : 728 -> 944
~ sub_100004704 -> sub_100004828 : 964 -> 1172
~ sub_100004ac8 -> sub_100004cbc : 316 -> 336
~ sub_100004c04 -> sub_100004e0c : 532 -> 552
~ sub_100005b44 -> sub_100005d60 : 16 -> 12
~ sub_10000632c -> sub_100006544 : 200 -> 196
~ sub_1000063f4 -> sub_100006608 : 164 -> 160
~ sub_100006594 -> sub_1000067a4 : 144 -> 148
~ sub_1000066c8 -> sub_1000068dc : 144 -> 88
~ sub_100006a08 -> sub_100006be4 : 116 -> 120
CStrings:
+ "... Done. Cache cleared: removed %lu files, %lu failures"
+ "... Done. Cache reset complete: removed %lu items, %lu failures at path: %@"
+ "... Done. Garbage collection complete: removed %lu source units, %lu tint units. Stale index entries remain for lazy cleanup."
+ "Failed to remove cache item at URL: %@ with error: %@"
- "... Done"

```
