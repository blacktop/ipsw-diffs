## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet`

```diff

-  __TEXT.__text: 0x18f77c
+  __TEXT.__text: 0x18f800
   __TEXT.__objc_methlist: 0x1168c
-  __TEXT.__cstring: 0x15c4a
+  __TEXT.__cstring: 0x15cd7
   __TEXT.__const: 0x5b8
   __TEXT.__oslogstring: 0x18e01
   __TEXT.__gcc_except_tab: 0x73ec

   __DATA_CONST.__objc_arraydata: 0x710
   __DATA_CONST.__got: 0x1198
   __AUTH_CONST.__const: 0x1b00
-  __AUTH_CONST.__cfstring: 0x12ce0
+  __AUTH_CONST.__cfstring: 0x12d40
   __AUTH_CONST.__objc_const: 0x22df8
-  __AUTH_CONST.__objc_intobj: 0x2298
+  __AUTH_CONST.__objc_intobj: 0x22b0
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x630
   __AUTH_CONST.__objc_dictobj: 0xc8

   - /usr/lib/libobjc.A.dylib
   Functions: 8782
   Symbols:   27994
-  CStrings:  7056
+  CStrings:  7062
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Functions:
~ -[_CDSpotlightItemRecorder runOperation:] : 940 -> 944
~ _OUTLINED_FUNCTION_27 : 12 -> 20
~ ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.652 : 660 -> 664
~ -[_CDSpotlightItemRecorder _deleteUserActivitiesWithPersistentIdentifiers:bundleID:] : 884 -> 888
~ ___83-[_CDSpotlightItemRecorder deleteSearchableItemsSinceDate:bundleID:withCompletion:]_block_invoke : 344 -> 388
~ ___81-[_CDSpotlightItemRecorder deleteAllItemsWithBundleID:isCSSIDeletion:completion:]_block_invoke : 92 -> 160
CStrings:
+ "deleteAllItemsWithBundleID (excluding sharesheet)"
+ "mechanism != %@ AND mechanism != %@"
+ "mechanism != %@ AND mechanism != %@ AND bundleId == %@"

```
