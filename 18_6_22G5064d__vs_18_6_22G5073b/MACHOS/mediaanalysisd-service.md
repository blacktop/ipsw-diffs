## mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

-325.3.1.0.0
-  __TEXT.__text: 0x1888e4
+325.4.1.0.0
+  __TEXT.__text: 0x188d44
   __TEXT.__auth_stubs: 0x1100
   __TEXT.__objc_stubs: 0x131e0
   __TEXT.__objc_methlist: 0x9148

   __TEXT.__objc_methname: 0x1a75b
   __TEXT.__objc_methtype: 0x37cc
   __TEXT.__const: 0x4a8
-  __TEXT.__gcc_except_tab: 0x322f4
-  __TEXT.__oslogstring: 0x220f8
+  __TEXT.__gcc_except_tab: 0x32390
+  __TEXT.__oslogstring: 0x2222a
   __TEXT.__dlopen_cstrs: 0x60a
   __TEXT.__unwind_info: 0x5db8
   __DATA_CONST.__auth_got: 0x898

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 9431D2B5-BD98-38B0-855E-A6935ABFF4E9
+  UUID: 8C85AD84-51E3-3CBB-9C27-E65BE6F28D08
   Functions: 3929
   Symbols:   732
-  CStrings:  11041
+  CStrings:  11045
 
Functions:
~ sub_10000c6c8 : 1848 -> 2436
~ sub_100078288 -> sub_1000784d4 : 2080 -> 2252
~ sub_100078aa8 -> sub_100078da0 : 2508 -> 2676
~ sub_1000aa184 -> sub_1000aa524 : 2016 -> 2208
CStrings:
+ "%@ Analysis has future version (v%d); discarding existing analysis"
+ "[MergeAnalysis]%@ Analysis A has future version (v%d), use B: %@"
+ "[MergeAnalysis]%@ Analysis B has future version (v%d), use A: %@"
+ "[MergeAnalysis]%@ Both analyses have future versions (A: v%d, B: v%d, current: %d), no valid analysis to use"

```
