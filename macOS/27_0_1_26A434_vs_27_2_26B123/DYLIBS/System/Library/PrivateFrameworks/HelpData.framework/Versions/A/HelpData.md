## HelpData

> `/System/Library/PrivateFrameworks/HelpData.framework/Versions/A/HelpData`

```diff

-243.0.0.0.0
-  __TEXT.__text: 0x1da3c
-  __TEXT.__objc_methlist: 0x202c
-  __TEXT.__cstring: 0x35fa
+243.2.3.0.0
+  __TEXT.__text: 0x1ebf0
+  __TEXT.__objc_methlist: 0x2084
+  __TEXT.__cstring: 0x3844
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x414
+  __TEXT.__gcc_except_tab: 0x418
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__oslogstring: 0x250
   __TEXT.__unwind_info: 0x778

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5d0
+  __DATA_CONST.__const: 0x5d8
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17a8
+  __DATA_CONST.__objc_selrefs: 0x17f8
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x2d8
   __AUTH_CONST.__const: 0x6f0
-  __AUTH_CONST.__cfstring: 0x35a0
-  __AUTH_CONST.__objc_const: 0x46b0
+  __AUTH_CONST.__cfstring: 0x36c0
+  __AUTH_CONST.__objc_const: 0x46e0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x6b8
-  __DATA.__objc_ivar: 0x29c
+  __DATA.__objc_ivar: 0x2a0
   __DATA.__data: 0x480
   __DATA.__ddm_mapping: 0x5fa
-  __DATA.__ddm_config: 0x164c
+  __DATA.__ddm_config: 0x170a
   __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0x2f8
   __DATA_DIRTY.__data: 0x4

   - /System/Library/PrivateFrameworks/TipsCore.framework/Versions/A/TipsCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 762
-  Symbols:   2259
-  CStrings:  519
+  Functions: 769
+  Symbols:   2278
+  CStrings:  528
 
Symbols:
+ +[HPDHelpBook _generatedIndexRootForTesting]
+ +[HPDHelpBook _pathIsContainedInRoot:inRoot:]
+ -[DDMConfig _webContentProductNames]
+ -[DDMConfig isWebContentBookID:productName:]
+ -[DDMConfig setWebContentProductNames:]
+ -[DDMConfig webContentProductNames]
+ -[HPDHelpBook _cachedResourceContainmentRoot]
+ GCC_except_table50
+ OBJC_IVAR_$_DDMConfig._webContentProductNames
+ _DDMBookConfigKeyIsWebContent
+ _NSSearchPathForDirectoriesInDomains
+ _objc_msgSend$_cachedResourceContainmentRoot
+ _objc_msgSend$_webContentProductNames
+ _objc_msgSend$isWebContentBookID:productName:
+ _objc_msgSend$setWebContentProductNames:
+ _objc_msgSend$stringByResolvingSymlinksInPath
+ _objc_msgSend$tps_userPreferredLocalizationsFromArray:forLanguages:
+ _objc_msgSend$userGuideSystemLanguages
+ _objc_msgSend$webContentProductNames
CStrings:
+ "%@/%@/%@"
+ "Rejecting ExactMatch.plist %@ for book at %@ - resolves outside the help book"
+ "Rejecting Suggestions.plist %@ for book at %@ - resolves outside the help book"
+ "Rejecting access page %@ for book at %@ - resolves outside the help book"
+ "Rejecting cached ExactMatch.plist %@ for book %@ - resolves outside its resource root"
+ "Rejecting cached Suggestions.plist %@ for book %@ - resolves outside its resource root"
+ "Rejecting cached access page %@ for book at %@ - resolves outside the help book"
+ "Rejecting potential access page %@ - resolves outside its help book directory %@"
+ "isWebContent"
```
