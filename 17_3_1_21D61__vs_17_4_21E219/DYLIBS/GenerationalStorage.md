## GenerationalStorage

> `/System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage`

```diff

-362.0.0.0.0
-  __TEXT.__text: 0x17f0c
-  __TEXT.__auth_stubs: 0x910
+365.100.2.0.0
+  __TEXT.__text: 0x180cc
+  __TEXT.__auth_stubs: 0x920
   __TEXT.__objc_methlist: 0xa64
   __TEXT.__const: 0xc8
   __TEXT.__cstring: 0x112a
-  __TEXT.__oslogstring: 0x56d
+  __TEXT.__oslogstring: 0x60d
   __TEXT.__gcc_except_tab: 0x3a8
   __TEXT.__unwind_info: 0x5e4
   __TEXT.__objc_classname: 0x192

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x16a8
   __DATA_CONST.__objc_selrefs: 0x8c8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x120
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__cfstring: 0x10c0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0x498
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x120
-  __DATA.__objc_superrefs: 0x50
+  __AUTH_CONST.__auth_got: 0x4a0
   __DATA.__objc_ivar: 0xe0
   __DATA.__data: 0x300
-  __DATA.__bss: 0x18
+  __DATA.__bss: 0x19
   __DATA.__common: 0x8
   __DATA_DIRTY.__const: 0xe0
   __DATA_DIRTY.__objc_const: 0x540

   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3B464CAA-6645-3346-955C-7D5DC3045E0C
-  Functions: 523
-  Symbols:   1768
-  CStrings:  863
+  UUID: 28755145-241A-3F23-ABC1-03DB113EE5A9
+  Functions: 525
+  Symbols:   1774
+  CStrings:  865
 
Symbols:
+ _GSLibraryGetMNTInfo.cold.1
+ _GSLibraryGetMNTInfo.warned
+ _GSLibraryResolveDocumentIdCachedAPFS.cold.2
+ ___102-[GSStorageManager removeAdditionsInNamespace:underPath:withMatchingPredicate:errorPerAddition:error:]_block_invoke.37
+ __os_log_fault_impl
- ___102-[GSStorageManager removeAdditionsInNamespace:underPath:withMatchingPredicate:errorPerAddition:error:]_block_invoke.34
CStrings:
+ "[CRIT] getfsstat() returned as many mount points\u00a0as we can process (%d = %zu) - possible docID resolution failures"
+ "[DEBUG] Cache negative entry for %@"
+ "[DEBUG] gDevCache needs to be rebuilt"
- "[DEBUG] gDevCache needs flush"

```
