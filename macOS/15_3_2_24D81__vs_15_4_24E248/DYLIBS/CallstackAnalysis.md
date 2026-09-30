## CallstackAnalysis

> `/System/Library/PrivateFrameworks/CallstackAnalysis.framework/Versions/A/CallstackAnalysis`

```diff

-83.0.0.0.0
-  __TEXT.__text: 0xb7a4
+84.0.0.0.0
+  __TEXT.__text: 0xb6c0
   __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_methlist: 0xba4
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0xb4
-  __TEXT.__cstring: 0x1872
+  __TEXT.__cstring: 0x1869
   __TEXT.__unwind_info: 0x1b8
   __TEXT.__objc_classname: 0xb0
   __TEXT.__objc_methname: 0x3738

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B9ACC06B-0FA3-35DD-95F0-B340C3AE034C
-  Functions: 285
-  Symbols:   760
+  UUID: 349E6437-354E-3ACF-8D4B-AFBE5F1E3D8F
+  Functions: 288
+  Symbols:   765
   CStrings:  848
 
Symbols:
+ +[TPCSignatureObject isBlockInvokeFrame:].cold.1
+ +[TPCSignatureObject isSwiftClosureFrame:].cold.1
+ +[TPCSignatureObject retrieveModifiedFrame:frameType:].cold.1
+ +[TPCSignatureStore supportedFormatTypes].cold.1
+ -[TPCCallstackMatching matchWithSignatures:store:type:diagnostics:error:].cold.1
CStrings:
+ "[SignatureStoreDict objectForKey:frame] != ((void*)0)"
+ "child != ((void*)0)"
+ "i_obj != ((void*)0)"
+ "i_obj.last3PFrame != ((void*)0)"
+ "object != ((void*)0)"
+ "object.path != ((void*)0)"
+ "previous != ((void*)0)"
+ "queue != ((void*)0)"
+ "root != ((void*)0)"
- "[SignatureStoreDict objectForKey:frame] != ((void *)0)"
- "child != ((void *)0)"
- "i_obj != ((void *)0)"
- "i_obj.last3PFrame != ((void *)0)"
- "object != ((void *)0)"
- "object.path != ((void *)0)"
- "previous != ((void *)0)"
- "queue != ((void *)0)"
- "root != ((void *)0)"

```
