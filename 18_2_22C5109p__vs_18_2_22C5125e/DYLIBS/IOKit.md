## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-100140.60.10.0.0
-  __TEXT.__text: 0x9c6b4
-  __TEXT.__auth_stubs: 0x2030
+100140.60.14.0.0
+  __TEXT.__text: 0x9c7b0
+  __TEXT.__auth_stubs: 0x2040
   __TEXT.__objc_methlist: 0x150
   __TEXT.__const: 0xeb6c
-  __TEXT.__oslogstring: 0x4a6a
+  __TEXT.__oslogstring: 0x4b03
   __TEXT.__cstring: 0xb689
-  __TEXT.__unwind_info: 0x1ea0
+  __TEXT.__unwind_info: 0x1eb8
   __TEXT.__objc_classname: 0x58
   __TEXT.__objc_methname: 0xa3
   __TEXT.__objc_methtype: 0x1972

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x1020
+  __AUTH_CONST.__auth_got: 0x1028
   __AUTH_CONST.__auth_ptr: 0x28
   __AUTH_CONST.__const: 0x1c28
   __AUTH_CONST.__cfstring: 0x7220

   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3416
-  Symbols:   4134
-  CStrings:  2470
+  Functions: 3417
+  Symbols:   4137
+  CStrings:  2472
 
Symbols:
+ _CFPropertyListCreateDeepCopy
CStrings:
+ "CopyServiceRecords deep copy failed. Service record for %!@(MISSING) is not serializable."
+ "Creating deep copy of record belonging to service: %!@(MISSING)"
+ "OSKEXT_BUILD_DATE 00:47:33 Oct 26 2024"
+ "assertion failure: retainCount:%!d(MISSING) on attempt to retain object"
- "OSKEXT_BUILD_DATE 11:51:31 Oct 16 2024"
- "Service record for %!@(MISSING) is not serializable."

```
