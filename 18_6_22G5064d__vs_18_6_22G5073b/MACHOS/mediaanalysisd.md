## mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

-325.3.1.0.0
-  __TEXT.__text: 0x188990
+325.4.1.0.0
+  __TEXT.__text: 0x188df0
   __TEXT.__auth_stubs: 0x1100
   __TEXT.__objc_stubs: 0x131e0
   __TEXT.__objc_methlist: 0x9148
-  __TEXT.__gcc_except_tab: 0x32324
+  __TEXT.__gcc_except_tab: 0x323c0
   __TEXT.__cstring: 0x13f6a
   __TEXT.__objc_classname: 0x1bf1
   __TEXT.__objc_methname: 0x1a75b
   __TEXT.__objc_methtype: 0x37cc
   __TEXT.__const: 0x4a8
-  __TEXT.__oslogstring: 0x220f8
+  __TEXT.__oslogstring: 0x2222a
   __TEXT.__dlopen_cstrs: 0x60a
   __TEXT.__unwind_info: 0x5dc8
   __DATA_CONST.__auth_got: 0x898

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: E796968D-B1F3-3D87-9083-84EF4CB50241
+  UUID: 38D4ED07-1D28-3311-86F2-6C5034AE14C1
   Functions: 3930
   Symbols:   732
-  CStrings:  11041
+  CStrings:  11045
 
Functions (added):
+ sub_10000c7d4
+ sub_1000785e0

Functions (removed):
- sub_10017d784
- sub_10018416c
CStrings:
+ "%@ Analysis has future version (v%d); discarding existing analysis"
+ "[MergeAnalysis]%@ Analysis A has future version (v%d), use B: %@"
+ "[MergeAnalysis]%@ Analysis B has future version (v%d), use A: %@"
+ "[MergeAnalysis]%@ Both analyses have future versions (A: v%d, B: v%d, current: %d), no valid analysis to use"

```
