## NewsUI

> `/System/Library/PrivateFrameworks/NewsUI.framework/NewsUI`

```diff

-5883.0.0.0.0
-  __TEXT.__text: 0x388bc
+5884.0.0.0.0
+  __TEXT.__text: 0x389d8
   __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0x662c
-  __TEXT.__const: 0x258
+  __TEXT.__objc_methlist: 0x6624
+  __TEXT.__const: 0x260
   __TEXT.__cstring: 0x21be
   __TEXT.__gcc_except_tab: 0x858
-  __TEXT.__oslogstring: 0xf46
+  __TEXT.__oslogstring: 0xf83
   __TEXT.__ustring: 0x146
-  __TEXT.__unwind_info: 0x1368
-  __TEXT.__objc_classname: 0x1415
-  __TEXT.__objc_methname: 0xfbc2
+  __TEXT.__unwind_info: 0x1370
+  __TEXT.__objc_classname: 0x1413
+  __TEXT.__objc_methname: 0xfc07
   __TEXT.__objc_methtype: 0x3798
-  __TEXT.__objc_stubs: 0x9940
+  __TEXT.__objc_stubs: 0x99c0
   __DATA_CONST.__got: 0x830
   __DATA_CONST.__const: 0x1918
   __DATA_CONST.__objc_classlist: 0x3b8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37d8
+  __DATA_CONST.__objc_selrefs: 0x37f8
   __DATA_CONST.__objc_protorefs: 0x1d0
   __DATA_CONST.__objc_superrefs: 0x2f8
   __DATA_CONST.__objc_arraydata: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E34C8E32-D567-3AAD-8408-06AD467C2F5D
+  UUID: C9C72432-7984-3222-AEF7-49480099A5FB
   Functions: 1693
-  Symbols:   7189
-  CStrings:  3705
+  Symbols:   7193
+  CStrings:  3708
 
Symbols:
+ -[NULiveCoverageManager hasInitializedPostIdentifiers]
+ -[NULiveCoverageManager knownPostIdentifiers]
+ -[NULiveCoverageManager liveBlogPostIdentifiersInContext:]
+ -[NULiveCoverageManager setHasInitializedPostIdentifiers:]
+ _OBJC_IVAR_$_NULiveCoverageManager._hasInitializedPostIdentifiers
+ _OBJC_IVAR_$_NULiveCoverageManager._knownPostIdentifiers
+ ___58-[NULiveCoverageManager liveBlogPostIdentifiersInContext:]_block_invoke
+ _objc_msgSend$componentIdentifiers
+ _objc_msgSend$hasInitializedPostIdentifiers
+ _objc_msgSend$knownPostIdentifiers
+ _objc_msgSend$liveBlogPostIdentifiersInContext:
+ _objc_msgSend$minusSet:
+ _objc_msgSend$set
+ _objc_msgSend$setHasInitializedPostIdentifiers:
+ _objc_msgSend$setSet:
+ _objc_msgSend$unionSet:
- -[NULiveCoverageManager countLiveBlogPostsInContext:]
- -[NULiveCoverageManager hasInitializedPostCount]
- -[NULiveCoverageManager lastLiveBlogPostCount]
- -[NULiveCoverageManager setHasInitializedPostCount:]
- -[NULiveCoverageManager setLastLiveBlogPostCount:]
- GCC_except_table16
- _OBJC_IVAR_$_NULiveCoverageManager._hasInitializedPostCount
- _OBJC_IVAR_$_NULiveCoverageManager._lastLiveBlogPostCount
- ___43-[NULiveCoverageManager processNewContext:]_block_invoke
- ___53-[NULiveCoverageManager countLiveBlogPostsInContext:]_block_invoke
- _objc_msgSend$countLiveBlogPostsInContext:
- _objc_msgSend$hasInitializedPostCount
- _objc_msgSend$lastLiveBlogPostCount
- _objc_msgSend$setHasInitializedPostCount:
- _objc_msgSend$setLastLiveBlogPostCount:
CStrings:
+ "Initial LiveBlog post identifiers count set to %lu"
+ "LiveCoverage detected %ld new posts (current identifiers: %lu, known identifiers: %lu)"
+ "Processing new context: current identifiers count=%lu, known identifiers count=%lu"
+ "T@\"NSMutableSet\",R,N,V_knownPostIdentifiers"
+ "TB,N,V_hasInitializedPostIdentifiers"
+ "_hasInitializedPostIdentifiers"
+ "_knownPostIdentifiers"
+ "componentIdentifiers"
+ "hasInitializedPostIdentifiers"
+ "knownPostIdentifiers"
+ "liveBlogPostIdentifiersInContext:"
+ "minusSet:"
+ "set"
+ "setHasInitializedPostIdentifiers:"
+ "setSet:"
+ "unionSet:"
- "#"
- "Initial LiveBlog post count set to %ld"
- "LiveCoverage detected %ld new posts (total: %ld)"
- "Processing new context: current post count=%ld, previous post count=%ld"
- "TB,N,V_hasInitializedPostCount"
- "Tq,N,V_lastLiveBlogPostCount"
- "_hasInitializedPostCount"
- "_lastLiveBlogPostCount"
- "countLiveBlogPostsInContext:"
- "hasInitializedPostCount"
- "lastLiveBlogPostCount"
- "setHasInitializedPostCount:"
- "setLastLiveBlogPostCount:"

```
