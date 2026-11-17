## WebContentRestrictions

> `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions`

```diff

-79.0.0.0.0
-  __TEXT.__text: 0x109a0
-  __TEXT.__objc_methlist: 0x1050
+79.2.2.0.0
+  __TEXT.__text: 0x11778
+  __TEXT.__objc_methlist: 0x10e8
   __TEXT.__const: 0x5c0
-  __TEXT.__cstring: 0x18dc
+  __TEXT.__cstring: 0x192c
   __TEXT.__gcc_except_tab: 0x250
   __TEXT.__oslogstring: 0x883
   __TEXT.__ustring: 0x1bc

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x34
-  __TEXT.__unwind_info: 0x618
+  __TEXT.__unwind_info: 0x640
   __TEXT.__eh_frame: 0x2b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x618
+  __DATA_CONST.__const: 0x620
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb28
+  __DATA_CONST.__objc_selrefs: 0xc38
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x78
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__got: 0x1e8
   __AUTH_CONST.__const: 0x389
-  __AUTH_CONST.__cfstring: 0x1ca0
-  __AUTH_CONST.__objc_const: 0x1de0
+  __AUTH_CONST.__cfstring: 0x1dc0
+  __AUTH_CONST.__objc_const: 0x1e10
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x5b8
   __AUTH.__objc_data: 0x4a0
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0xf4
+  __DATA.__objc_ivar: 0xf8
   __DATA.__data: 0x488
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 470
-  Symbols:   1205
-  CStrings:  313
+  Functions: 482
+  Symbols:   1219
+  CStrings:  322
 
Symbols:
+ +[WCRBrowserEngineClient _askToBrowseURLForURL:state:matchedEntry:]
+ +[WCRBrowserEngineClient _blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:matchedEntry:]
+ +[WCRBrowserEngineClient _displayStringForMatchedEntry:]
+ +[WCRBrowserEngineClient _matchedEntry:isOnSiteOfURL:]
+ +[WCRBrowserEngineClient _matchedEntryFromReferrer:forURL:]
+ +[WCRBrowserEngineClient _queryValueForMatchedEntry:]
+ +[WCRBrowserEngineClient _schemelessMatchedEntry:]
+ +[WCRBrowserEngineClient shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:matchedEntry:language:]
+ +[WCRURLList _entry:matchesBrowserURLString:browserURLHost:]
+ +[WCRURLList _indexOfEntryInList:matchingURLString:longest:]
+ +[WCRURLList entry:matchesURLString:]
+ -[WCRURLList longestMatchingEntryForURLString:]
+ -[WCRURLList originalURLStringList]
+ -[WCRURLList setOriginalURLStringList:]
+ GCC_except_table61
+ GCC_except_table93
+ GCC_except_table95
+ GCC_except_table97
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_IVAR_$_WCRURLList._originalURLStringList
+ ___131+[WCRBrowserEngineClient shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:matchedEntry:language:]_block_invoke
+ ___132+[WCRBrowserEngineClient _blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:matchedEntry:]_block_invoke
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80bs_e21_v24?0Q8"NSString"16ls32l8s40l8s48l8s56l8s64l8s80l8s72l8
+ ___block_descriptor_57_e8_32s_e28_"NSString"16?0"NSString"8ls32l8
- +[WCRBrowserEngineClient _blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:]
- +[WCRBrowserEngineClient shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:language:]
- GCC_except_table55
- GCC_except_table87
- GCC_except_table89
- GCC_except_table91
- ___118+[WCRBrowserEngineClient shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:language:]_block_invoke
- ___119+[WCRBrowserEngineClient _blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:]_block_invoke
- ___block_descriptor_105_e8_32s40s48s56s64s72s80bs_e8_v16?0Q8ls32l8s40l8s48l8s56l8s64l8s80l8s72l8
- ___block_descriptor_41_e28_"NSString"16?0"NSString"8l
CStrings:
+ "&=+#'\"<>"
+ "&matchedEntry=%@"
+ ":"
+ "://"
+ "<>\"'&"
+ "?#"
+ "https"
+ "https://"
+ "matchedEntry"
+ "v24@?0Q8@\"NSString\"16"
- "v16@?0Q8"
```
