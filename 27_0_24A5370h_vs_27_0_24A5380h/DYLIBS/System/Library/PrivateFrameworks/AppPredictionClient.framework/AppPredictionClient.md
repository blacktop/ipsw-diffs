## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-  __TEXT.__text: 0x18c1b0
-  __TEXT.__objc_methlist: 0x18f1c
+  __TEXT.__text: 0x18c128
+  __TEXT.__objc_methlist: 0x18f2c
   __TEXT.__const: 0x708
-  __TEXT.__cstring: 0x1c2fe
-  __TEXT.__oslogstring: 0x17966
+  __TEXT.__cstring: 0x1c35a
+  __TEXT.__oslogstring: 0x179bc
   __TEXT.__gcc_except_tab: 0x2038
   __TEXT.__dlopen_cstrs: 0x491
   __TEXT.__ustring: 0x18a

   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa0d0
+  __DATA_CONST.__objc_selrefs: 0xa0d8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0xc48
   __DATA_CONST.__objc_arraydata: 0xb28
   __DATA_CONST.__got: 0x1718
   __AUTH_CONST.__const: 0x2b00
-  __AUTH_CONST.__cfstring: 0x15500
+  __AUTH_CONST.__cfstring: 0x15520
   __AUTH_CONST.__objc_const: 0x46148
   __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_arrayobj: 0x708
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__auth_got: 0x790
-  __AUTH.__objc_data: 0x3ca0
+  __AUTH.__objc_data: 0x4740
   __DATA.__objc_ivar: 0x1c94
   __DATA.__data: 0x1cf0
   __DATA.__bss: 0x438
-  __DATA_DIRTY.__objc_data: 0x51e0
+  __DATA_DIRTY.__objc_data: 0x4740
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x258
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10917
-  Symbols:   35736
-  CStrings:  7551
+  Functions: 10919
+  Symbols:   35740
+  CStrings:  7555
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
Symbols:
+ +[ATXAppDirectoryCategory categorizationVersion]
Functions:
~ _ATXSlotSetsDeserialize : 1556 -> 1544
+ +[ATXAppDirectoryCategory categorizationVersion]
~ _PPZipUnarchive : 1720 -> 1728
~ -[ATXDefaultHomeScreenItemProducer _initializeCachedWidgetPersonalityToAppScoreCache] : 860 -> 596
+ -[ATXDefaultHomeScreenItemProducer _initializeCachedWidgetPersonalityToAppScoreCache].cold.1
CStrings:
+ "%s: _appLaunchCounts is %@; widget ranking will fall back to no launch-history signal"
+ "-[ATXDefaultHomeScreenItemProducer _initializeCachedWidgetPersonalityToAppScoreCache]"
+ "empty"

```
