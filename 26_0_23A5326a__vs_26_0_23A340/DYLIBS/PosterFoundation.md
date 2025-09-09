## PosterFoundation

> `/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation`

```diff

-290.108.0.0.0
-  __TEXT.__text: 0x43230
+290.112.0.0.0
+  __TEXT.__text: 0x433d8
   __TEXT.__auth_stubs: 0x1040
   __TEXT.__objc_methlist: 0x3158
   __TEXT.__const: 0x196
   __TEXT.__cstring: 0x3cf9
-  __TEXT.__oslogstring: 0x30d1
+  __TEXT.__oslogstring: 0x316f
   __TEXT.__gcc_except_tab: 0x10f8
   __TEXT.__unwind_info: 0x1258
   __TEXT.__objc_classname: 0x720

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 17C1A593-261E-3405-BDA4-36752B643F4B
-  Functions: 1587
-  Symbols:   5567
-  CStrings:  2831
+  UUID: 508ADF14-6C44-332B-8624-B1F89FBA398A
+  Functions: 1589
+  Symbols:   5569
+  CStrings:  2833
 
Symbols:
+ -[PFPosterArchiver _unarchiveWithHandler:manifest:error:].cold.12
+ ___65-[PFPosterArchiver unarchivePathAppleArchiveData:manifest:error:]_block_invoke_2.cold.1
CStrings:
+ "Error writing archive data to pipe: %{public}@"
+ "Failed to create tempDirectory %@ : %{public}@"
+ "Manifest data failed to load from URL %@, error: %{public}@"
+ "Unable to copy contents for poster configuration: %{public}@"
+ "Unable to create directory for poster configuration: %{public}@"
+ "Unable to create finalURL: %{public}@"
+ "Unable to create incoming poster path: %{public}@"
+ "Unable to create placement URL: %{public}@"
+ "Unable to move item at provider URL to finalURL: %{public}@"
+ "unarchivingContainerURL %@ is not reachable URL : %{public}@"
- "Manifest data failed to load from URL %@, error: %@"
- "Unable to copy contents for poster configuration: %@"
- "Unable to create directory for poster configuration: %@"
- "Unable to create finalURL: %@"
- "Unable to create incoming poster path: %@"
- "Unable to create placement URL: %@"
- "Unable to move item at provider URL to finalURL: %@"
- "unarchivingContainerURL %@ is not reachable URL : %@"

```
