## CalendarDaemon

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon`

```diff

-1219.0.0.0.0
-  __TEXT.__text: 0x714cc
-  __TEXT.__auth_stubs: 0x3810
-  __TEXT.__objc_methlist: 0x617c
+1221.0.0.0.0
+  __TEXT.__text: 0x71558
+  __TEXT.__auth_stubs: 0x3820
+  __TEXT.__objc_methlist: 0x6184
   __TEXT.__cstring: 0x6f58
   __TEXT.__const: 0x150
   __TEXT.__oslogstring: 0x81fe

   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x1ad8
   __TEXT.__objc_classname: 0x1499
-  __TEXT.__objc_methname: 0xea51
-  __TEXT.__objc_methtype: 0x6620
-  __TEXT.__objc_stubs: 0x9b40
+  __TEXT.__objc_methname: 0xeaaa
+  __TEXT.__objc_methtype: 0x6639
+  __TEXT.__objc_stubs: 0x9bc0
   __DATA_CONST.__got: 0x9e8
   __DATA_CONST.__const: 0x1fe0
   __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3120
+  __DATA_CONST.__objc_selrefs: 0x3140
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x350
-  __AUTH_CONST.__auth_got: 0x1c18
+  __AUTH_CONST.__auth_got: 0x1c20
   __AUTH_CONST.__const: 0x880
   __AUTH_CONST.__cfstring: 0x79a0
-  __AUTH_CONST.__objc_const: 0xc0d0
-  __AUTH_CONST.__objc_intobj: 0x438
+  __AUTH_CONST.__objc_const: 0xc0f0
+  __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1400
   __AUTH.__data: 0xa50
-  __DATA.__objc_ivar: 0x784
+  __DATA.__objc_ivar: 0x788
   __DATA.__data: 0x1728
   __DATA.__bss: 0x198
   __DATA.__common: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 92E20832-4684-3BBA-B311-10C6B0D9FDFD
-  Functions: 2148
-  Symbols:   8937
-  CStrings:  5545
+  UUID: 8AB983A5-B679-3753-AAA9-E4B2A4C4702A
+  Functions: 2149
+  Symbols:   8945
+  CStrings:  5551
 
Symbols:
+ -[CADFetchCalendarItemsWithPredicateOperation _callCompletionOnceWithResults:]
+ _CalCalendarCopySharedOwnerName
+ _OBJC_IVAR_$_CADFetchCalendarItemsWithPredicateOperation._hasRunCompletion
+ ___99-[CADSpotlightIndexer reindexItemsWithIdentifiers:bundleID:protectionClass:acknowledgementHandler:]_block_invoke.201
+ _objc_msgSend$_callCompletionOnceWithResults:
+ _objc_msgSend$setOwnerName:
+ _objc_msgSend$setShared:
+ _objc_msgSend$setUserOwned:
- ___99-[CADSpotlightIndexer reindexItemsWithIdentifiers:bundleID:protectionClass:acknowledgementHandler:]_block_invoke.196
Functions:
~ -[CADFetchCalendarItemsWithPredicateOperation main] : 236 -> 220
~ -[CADSpotlightIndexer _spotlightItemAttributes:] : 2948 -> 3064
~ -[CADFetchCalendarItemsWithPredicateOperation cancel] : 96 -> 80
+ -[CADFetchCalendarItemsWithPredicateOperation _callCompletionOnceWithResults:]
CStrings:
+ "_callCompletionOnceWithResults:"
+ "_hasRunCompletion"
+ "setOwnerName:"
+ "setShared:"
+ "setUserOwned:"
+ "{atomic_flag=\"_Value\"AB}"

```
