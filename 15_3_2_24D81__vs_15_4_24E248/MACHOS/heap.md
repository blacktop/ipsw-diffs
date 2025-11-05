## heap

> `/usr/bin/heap`

```diff

-64566.82.1.0.0
-  __TEXT.__text: 0xb71c
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_stubs: 0x16e0
-  __TEXT.__objc_methlist: 0x218
-  __TEXT.__const: 0xc8
-  __TEXT.__objc_methname: 0x1184
+64570.34.1.0.0
+  __TEXT.__text: 0xbfa8
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__objc_stubs: 0x1740
+  __TEXT.__objc_methlist: 0x230
+  __TEXT.__const: 0x108
+  __TEXT.__objc_methname: 0x11f7
   __TEXT.__objc_classname: 0x39
-  __TEXT.__objc_methtype: 0x124
-  __TEXT.__gcc_except_tab: 0x3dc
-  __TEXT.__cstring: 0x2ab5
+  __TEXT.__objc_methtype: 0x155
+  __TEXT.__gcc_except_tab: 0x488
+  __TEXT.__cstring: 0x2b62
   __TEXT.__oslogstring: 0x840
-  __TEXT.__unwind_info: 0x268
-  __DATA_CONST.__auth_got: 0x498
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x7a0
-  __DATA_CONST.__cfstring: 0x920
+  __TEXT.__unwind_info: 0x298
+  __DATA_CONST.__auth_got: 0x4a8
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__const: 0x800
+  __DATA_CONST.__cfstring: 0x9c0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x4f8
-  __DATA.__objc_selrefs: 0x5d8
+  __DATA.__objc_selrefs: 0x5f0
   __DATA.__objc_ivar: 0x48
   __DATA.__objc_data: 0xf0
   __DATA.__crash_info: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxcselect.dylib
-  UUID: 1431CB6F-B2C9-3341-9A61-0855C0829726
-  Functions: 186
-  Symbols:   190
-  CStrings:  657
+  UUID: 082A6580-591B-3006-899C-275B291144EC
+  Functions: 191
+  Symbols:   191
+  CStrings:  671
 
Symbols:
+ _VMUCallMallocEnumeratorWithAttributeGraphWorkaround
+ _mergesort_b
- _OBJC_CLASS_$_VMUProcessDescription
CStrings:
+ ""
+ "SKIPPING PROCESS %5d: %s\n"
+ "SKIPPING PROCESS OF WRONG ARCHITECTURE:  %d %s\n"
+ "SKIP_WEBCONTENT"
+ "Target process:  %@ [%u] (%@)\n"
+ "WebKit"
+ "core file"
+ "corpse"
+ "live task"
+ "nodeDetails:"
+ "printPatternMatchedNode:info:zoneName:"
+ "printSortedClassPatternMatcherForZoneIndex:zoneName:allowNonObjects:blockCount:"
+ "prints the addresses of matching objects found on the heap in ascending address order, or in descending order of sizes if --sortBySize is passed"
+ "sort output by total size of class instances, rather than by count, or (for -addresses) by allocation size"
+ "taskIsCorpse"
+ "v36@0:8i16r*20B28I32"
+ "v52@0:8I16{?=Qb60b4@}20r*44"
- "--"
- "-al"
- "Skipping process of wrong architecture:  %d %s\n"
- "Target process:  %@ [%u]\n"
- "initWithTask:getBinariesList:"
- "prints the addresses of matching objects found on the heap in ascending address order"
- "sort output by total size of class instances, rather than by count"

```
