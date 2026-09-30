## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

-64566.98.1.0.0
-  __TEXT.__text: 0xa7374
-  __TEXT.__auth_stubs: 0x1fb0
-  __TEXT.__objc_methlist: 0x5d2c
+64566.105.1.0.0
+  __TEXT.__text: 0xa7964
+  __TEXT.__auth_stubs: 0x1fc0
+  __TEXT.__objc_methlist: 0x5d3c
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0xef66
-  __TEXT.__gcc_except_tab: 0x4bd0
-  __TEXT.__oslogstring: 0x152f
+  __TEXT.__cstring: 0xf11d
+  __TEXT.__gcc_except_tab: 0x4c5c
+  __TEXT.__oslogstring: 0x160a
   __TEXT.__ustring: 0x24
-  __TEXT.__unwind_info: 0x26d0
+  __TEXT.__unwind_info: 0x26d8
   __TEXT.__objc_classname: 0x7df
-  __TEXT.__objc_methname: 0xe857
-  __TEXT.__objc_methtype: 0x82c2
-  __TEXT.__objc_stubs: 0x94a0
-  __DATA_CONST.__got: 0x408
-  __DATA_CONST.__const: 0x3308
+  __TEXT.__objc_methname: 0xe8e4
+  __TEXT.__objc_methtype: 0x82f9
+  __TEXT.__objc_stubs: 0x9500
+  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__const: 0x3388
   __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32d0
+  __DATA_CONST.__objc_selrefs: 0x32e8
   __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0x718
-  __AUTH_CONST.__auth_got: 0xff0
+  __AUTH_CONST.__auth_got: 0xff8
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0xaa8
-  __AUTH_CONST.__cfstring: 0xc640
+  __AUTH_CONST.__cfstring: 0xc6a0
   __AUTH_CONST.__objc_const: 0xbf38
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x320
+  __AUTH.__objc_data: 0x230
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0xc24
   __DATA.__data: 0xce8
-  __DATA.__bss: 0x520
+  __DATA.__bss: 0x530
   __DATA.__common: 0x9
-  __DATA_DIRTY.__objc_data: 0x1770
+  __DATA_DIRTY.__objc_data: 0x1860
   __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__bss: 0xe0
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2866
-  Symbols:   3739
-  CStrings:  5733
+  Functions: 2868
+  Symbols:   3744
+  CStrings:  5745
 
Symbols:
+ _CSSymbolIsFunction
+ _malloc_num_zones
+ _malloc_zones
CStrings:
+ "%!s(MISSING) in analysis process, for %!s(MISSING) in target process"
+ "B36@0:8@16I24@28"
+ "Malloc enumeration of zone \"%!@(MISSING)\" failed to get full information about malloc metadata and/or allocations with the error \"%!s(MISSING) (%!d(MISSING))\". It is likely that the target was suspended while malloc metadata was being modified."
+ "TIGHTBEAM"
+ "_identifyNonObjectsPointedToByTypedIvars"
+ "_identifyNonObjectsPointingToSwiftMetadata"
+ "_replaceFieldRecursively:atOffset:withField:"
+ "addVariantRecursively:forField:atOffset:withEvaluator:"
+ "error: malloc enumeration of zone \"%!@(MISSING)\" failed to get full information about malloc metadata and/or allocations with the error \"%!s(MISSING) (%!d(MISSING))\". It is likely that the target was suspended while malloc metadata was being modified."
+ "flushRemoteMirrorMemoryCache"
+ "flushRemoteMirrorMemoryCacheEntryForAddress:"
+ "i24@0:8@?<i@?^vQ>16"
+ "ignoring request to break region at excess length %!l(MISSING)lu (%!s(MISSING)) for %!s(MISSING)\n"
+ "introspect structure %!s(MISSING) for the malloc zone has invalid enumerator function address %!l(MISSING)lx in %!s(MISSING)"
+ "replaceFieldRecursively:atOffset:withField:"
+ "swift_reflection_dumpInfoForMetadata"
+ "v36@0:8@16I24@28"
+ "v44@0:8@16@24I32@?36"
+ "zone %!s(MISSING) - using analysis tool's' %!s(MISSING) to look for zone introspect struct for target process's %!s(MISSING)\n"
- "_identifyNonObjectsPointingToSwiftMetadata:"
- "_replaceFieldRecursively:withField:"
- "addVariantRecursively:forField:withEvaluator:"
- "error: malloc enumeration of zone \"%!@(MISSING)\" failed with the error \"%!s(MISSING) (%!d(MISSING))\""
- "malloc enumeration of zone \"%!@(MISSING)\" failed with the error \"%!s(MISSING) (%!d(MISSING))\""
- "replaceFieldRecursively:withField:"
- "v24@0:8@?<i@?^vQ>16"

```
