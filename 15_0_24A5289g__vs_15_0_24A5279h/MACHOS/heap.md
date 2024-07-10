## heap

> `/usr/bin/heap`

```diff

-64566.76.1.0.0
-  __TEXT.__text: 0xb814
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_stubs: 0x1700
+64566.67.1.0.0
+  __TEXT.__text: 0xb10c
+  __TEXT.__auth_stubs: 0x8e0
+  __TEXT.__objc_stubs: 0x16c0
   __TEXT.__objc_methlist: 0x218
   __TEXT.__const: 0xc0
-  __TEXT.__objc_methname: 0x1189
+  __TEXT.__objc_methname: 0x117d
   __TEXT.__objc_classname: 0x39
   __TEXT.__objc_methtype: 0x124
-  __TEXT.__gcc_except_tab: 0x3dc
-  __TEXT.__cstring: 0x2ab5
+  __TEXT.__gcc_except_tab: 0x3c4
+  __TEXT.__cstring: 0x2824
   __TEXT.__oslogstring: 0x86a
-  __TEXT.__info_plist: 0x47b
-  __TEXT.__unwind_info: 0x260
-  __DATA_CONST.__auth_got: 0x498
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x7a0
-  __DATA_CONST.__cfstring: 0x920
+  __TEXT.__info_plist: 0x471
+  __TEXT.__unwind_info: 0x250
+  __DATA_CONST.__auth_got: 0x480
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__const: 0x6b0
+  __DATA_CONST.__cfstring: 0x8e0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x4f8
-  __DATA.__objc_selrefs: 0x5e0
+  __DATA.__objc_selrefs: 0x5d0
   __DATA.__objc_ivar: 0x48
   __DATA.__objc_data: 0xf0
   __DATA.__crash_info: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxcselect.dylib
-  Functions: 186
-  Symbols:   190
-  CStrings:  301
+  Functions: 179
+  Symbols:   186
+  CStrings:  286
 
Symbols:
- _OBJC_CLASS_$_VMUNonOverlappingRangeArray
- _VMUMallocRangeTypeString
- _VMUTask_foreach_malloc_zone
- _withPeekFunctionForVMUTask
CStrings:
- "    ISSUE:  PTR_IN_USE IS NOT CONTAINED IN ANY PTR_REGION"
- "    ISSUE:  PTR_IN_USE IS ONLY PARTIALLY CONTAINED IN A PTR_REGION"
- "    ISSUE:  UNEXPECTED MALLOC RANGE TYPE"
- "%!s(MISSING)   %!l(MISSING)lx-%!l(MISSING)lx[%!l(MISSING)lu]  %!s(MISSING)\n"
- "-enumerateZones not supported for memgraphs"
- "-printZones not supported for memgraphs"
- "Enumeration failed for malloc zone %!s(MISSING)\n"
- "Running print_task on %!s(MISSING)\n"
- "Running print_task on %!s(MISSING) is not supported.\n"
- "See output lines containing \"ISSUE:\" near the start to see possible malloc zone enumeration bugs.\n"
- "enumerateZones"
- "for debugging, enumerate all malloc zones"
- "i32@?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16@\"NSString\"24"
- "v16@?0^?8"
- "v24@?0I8^{?=QQ}12I20"

```
