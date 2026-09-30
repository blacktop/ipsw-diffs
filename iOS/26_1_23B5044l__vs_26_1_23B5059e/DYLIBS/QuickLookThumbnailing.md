## QuickLookThumbnailing

> `/System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing`

```diff

-208.1.1.0.0
-  __TEXT.__text: 0x32ab0
+208.1.3.0.0
+  __TEXT.__text: 0x32ae0
   __TEXT.__auth_stubs: 0x1330
   __TEXT.__objc_methlist: 0x3088
   __TEXT.__const: 0x92a
   __TEXT.__cstring: 0x23dd
-  __TEXT.__gcc_except_tab: 0xc80
-  __TEXT.__oslogstring: 0x2cf5
+  __TEXT.__gcc_except_tab: 0xc70
+  __TEXT.__oslogstring: 0x2cc5
   __TEXT.__dlopen_cstrs: 0x50
   __TEXT.__swift5_typeref: 0x3b3
   __TEXT.__swift5_capture: 0xe4

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 63AB8E8E-92AE-3E0F-BB37-3736DC0C68C0
-  Functions: 1555
-  Symbols:   4896
+  UUID: 69DE4437-A6E9-3E16-82AD-CAACB36406B4
+  Functions: 1557
+  Symbols:   4902
   CStrings:  2314
 
Symbols:
+ -[QLThumbnailAdditionCache thumbnailAdditionForItemAtURL:error:].cold.1
+ -[QLThumbnailAdditionCache thumbnailAdditionForItemAtURL:error:].cold.2
+ -[QLThumbnailAdditionCache thumbnailAdditionForItemAtURL:error:].cold.3
+ GCC_except_table159
- GCC_except_table156
CStrings:
+ "Found addition in cache for docID %@, but it is stale"
+ "No addition found in cache for docID %@"
+ "Using cached addition for docID %@"
- "Found addition in cache %@ for %@ (docID %@), but it is stale"
- "No addition found in cache %@ for %@ (docID %@)"
- "Using cached addition (%@) for %@ (%@) in cache %@, user info %@"

```
