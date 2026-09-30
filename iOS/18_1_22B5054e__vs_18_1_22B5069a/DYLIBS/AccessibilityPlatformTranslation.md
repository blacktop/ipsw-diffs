## AccessibilityPlatformTranslation

> `/System/Library/PrivateFrameworks/AccessibilityPlatformTranslation.framework/AccessibilityPlatformTranslation`

```diff

-496.8.0.0.0
-  __TEXT.__text: 0x12c68
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0xdd0
+496.10.0.0.0
+  __TEXT.__text: 0x1471c
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_methlist: 0xf90
   __TEXT.__const: 0x578
-  __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__cstring: 0x2198
-  __TEXT.__oslogstring: 0x438
+  __TEXT.__gcc_except_tab: 0x2e0
+  __TEXT.__cstring: 0x242c
+  __TEXT.__oslogstring: 0x56f
   __TEXT.__dlopen_cstrs: 0x6a
-  __TEXT.__unwind_info: 0x478
-  __TEXT.__objc_classname: 0x11b
-  __TEXT.__objc_methname: 0x34d8
-  __TEXT.__objc_methtype: 0x660
-  __TEXT.__objc_stubs: 0x2ea0
+  __TEXT.__unwind_info: 0x4f0
+  __TEXT.__objc_classname: 0x120
+  __TEXT.__objc_methname: 0x3ce8
+  __TEXT.__objc_methtype: 0x69c
+  __TEXT.__objc_stubs: 0x3260
   __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0x9e8
+  __DATA_CONST.__const: 0xa60
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc78
+  __DATA_CONST.__objc_selrefs: 0xd80
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x5c8
-  __AUTH_CONST.__auth_got: 0x3f0
-  __AUTH_CONST.__const: 0x220
+  __DATA_CONST.__objc_arraydata: 0x560
+  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__cfstring: 0x2580
-  __AUTH_CONST.__objc_const: 0x1400
-  __AUTH_CONST.__objc_intobj: 0xbd0
-  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_const: 0x16b0
+  __AUTH_CONST.__objc_intobj: 0xbe8
+  __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0xc4
+  __DATA.__objc_ivar: 0x100
   __DATA.__data: 0x240
-  __DATA.__bss: 0xf0
+  __DATA.__bss: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 395
-  Symbols:   660
-  CStrings:  982
+  Functions: 447
+  Symbols:   713
+  CStrings:  1067
 
Symbols:
+ _AXRequestingClient
+ _dispatch_after
+ _dispatch_queue_attr_make_with_qos_class
- _CGRectIsEmpty
- _dispatch_get_global_queue
CStrings:
+ "\x01c"
+ "\x04\x11&\x13"
+ "\x11"
+ "\"\x12"
+ "#\x12"
+ "%!s(MISSING): additional AX tree dump terminated early!"
+ "%!s(MISSING): axTreeDumpSharedBackgroundQueue is NULL!"
+ "%!s(MISSING): failed to look up translation in backTranslationCache: %!@(MISSING)"
+ "%!s(MISSING): finished generating additional hierarchy"
+ "%!s(MISSING): initial AX tree dump terminated early!"
+ "%!s(MISSING): notification: %!l(MISSING)u"
+ "%!s(MISSING): pendingAXTreeGeneration, generating another AX hierarchy"
+ "%!s(MISSING): shouldStopGeneratingAXTree"
+ "-[AXPRemoteCacheManager _axHierarchyGenerationQueue]"
+ "-[AXPRemoteCacheManager _sendAXHierachyOnBackgroundQueue]"
+ "-[AXPRemoteCacheManager axAdditionalTreeDumpGeneratedOnBackgroundThreadCallback:success:]"
+ "-[AXPRemoteCacheManager axInitialTreeDumpGeneratedOnBackgroundThreadCallback:success:]"
+ "-[AXPRemoteCacheManager axTreeGenerationEnded]"
+ "-[AXPRemoteCacheManager handleNotification:data:associatedObject:]"
+ "-[AXPTranslator_iOS _safelyAddAXTreeDumpResponseToCurrentOutput:]"
+ "-[AXPTranslator_iOS axTreeDumpGenerateNextSetOfElementAttrsOnMainThread]"
+ "-[AXPTranslator_iOS createPlatformElementFromTranslationObject:]_block_invoke"
+ "-[AXPTranslator_iOS stopGeneratingAXTreeDump]"
+ "@\"NSLock\""
+ "T@\"NSLock\",&,N,V_axTreeDumpLock"
+ "T@\"NSLock\",&,N,V_axTreeGenerationLock"
+ "T@\"NSMutableArray\",&,N,V_axTreeDumpCurrentOutput"
+ "T@\"NSMutableArray\",&,N,V_axTreeDumpCurrentlyProcessingChildren"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V__axHierarchyGenerationQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_axTreeDumpSharedBackgroundQueue"
+ "T@\"NSString\",&,N,V_axTreeDumpCurrentType"
+ "T@?,C,N,V_axTreeDumpCompletionHandler"
+ "TB,N,V_lastAXTreeFullyGenerated"
+ "TB,N,V_shouldHonorGroupsForElementTraversal"
+ "TB,N,V_shouldStopGeneratingAXTree"
+ "TQ,N,V_treeDumpStatus"
+ "Tq,N,V_axTreeDumpCurrentChildIndex"
+ "__axHierarchyGenerationQueue"
+ "_allAXTreeCanSetAttrValues"
+ "_axHierarchyGenerationQueue"
+ "_axTreeDumpCleanUpState"
+ "_axTreeDumpCompletionHandler"
+ "_axTreeDumpCurrentChildIndex"
+ "_axTreeDumpCurrentOutput"
+ "_axTreeDumpCurrentType"
+ "_axTreeDumpCurrentlyProcessingChildren"
+ "_axTreeDumpLock"
+ "_axTreeDumpSharedBackgroundQueue"
+ "_axTreeGenerationLock"
+ "_handleFocusedUIElementChangedForInitialDump:"
+ "_lastAXTreeFullyGenerated"
+ "_safelyAddAXTreeDumpResponseToCurrentOutput:"
+ "_sendAXHierachyOnBackgroundQueue"
+ "_sendTextRelatedAttributesForTranslation:"
+ "_shouldHonorGroupsForElementTraversal"
+ "_shouldStopGeneratingAXTree"
+ "_textEditingTranslationObj"
+ "_treeDumpStatus"
+ "axAdditionalTreeDumpGeneratedOnBackgroundThreadCallback:success:"
+ "axInitialTreeDumpGeneratedOnBackgroundThreadCallback:success:"
+ "axTreeDumpCompletionHandler"
+ "axTreeDumpCurrentChildIndex"
+ "axTreeDumpCurrentOutput"
+ "axTreeDumpCurrentType"
+ "axTreeDumpCurrentlyProcessingChildren"
+ "axTreeDumpGenerateNextSetOfElementAttrsOnMainThread"
+ "axTreeDumpLock"
+ "axTreeDumpSharedBackgroundQueue"
+ "axTreeGenerationEnded"
+ "axTreeGenerationLock"
+ "com.apple.accessibility.AXPRemoteCacheManager.axHierarchyGeneration"
+ "fetchNextSetOfElementAttrsOnBackgroundThreadWithEarlyTermination:"
+ "generateAXTreeDumpTypeOnBackgroundThread:completionHandler:"
+ "lastAXTreeFullyGenerated"
+ "q16@0:8"
+ "setAxTreeDumpCompletionHandler:"
+ "setAxTreeDumpCurrentChildIndex:"
+ "setAxTreeDumpCurrentOutput:"
+ "setAxTreeDumpCurrentType:"
+ "setAxTreeDumpCurrentlyProcessingChildren:"
+ "setAxTreeDumpLock:"
+ "setAxTreeDumpSharedBackgroundQueue:"
+ "setAxTreeGenerationLock:"
+ "setLastAXTreeFullyGenerated:"
+ "setShouldHonorGroupsForElementTraversal:"
+ "setShouldStopGeneratingAXTree:"
+ "setTreeDumpStatus:"
+ "set_axHierarchyGenerationQueue:"
+ "shouldHonorGroupsForElementTraversal"
+ "shouldStopGeneratingAXTree"
+ "stopGeneratingAXTreeDump"
+ "treeDumpStatus"
+ "v20@?0B8@\"AXPTranslatorResponse\"12"
+ "v24@0:8q16"
+ "v28@0:8@16B24"
+ "v32@0:8@16@?24"
- "\x04\x11#"
- "\x12\x12"
- "\x13"
- "-[AXPRemoteCacheManager _sendAXHierachy]"
- "-[AXPTranslator_iOS _safelyAddAXTreeDumpResponse:toResponsesDict:]"
- "Unhandled notification received: %!l(MISSING)u. Data: %!@(MISSING)"
- "_safelyAddAXTreeDumpResponse:toResponsesDict:"
- "_sendAXHierachy"
- "b"
- "generateAXTreeDumpForRequest:treeDumpType:"
- "generateAdditionalAXTreeDump"
- "generateInitialAXTreeDump"
- "rectWithAXAttribute:"

```
