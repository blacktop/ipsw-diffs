## InputContext

> `/System/Library/PrivateFrameworks/InputContext.framework/InputContext`

```diff

-129.0.0.0.0
-  __TEXT.__text: 0x138fc
+133.0.0.0.0
+  __TEXT.__text: 0x138cc
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x108c
+  __TEXT.__objc_methlist: 0x13ec
   __TEXT.__const: 0xe8
   __TEXT.__cstring: 0x87e
   __TEXT.__gcc_except_tab: 0x7ec
   __TEXT.__oslogstring: 0xf39
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0x5a0
+  __TEXT.__unwind_info: 0x5d0
   __TEXT.__objc_classname: 0x272
   __TEXT.__objc_methname: 0x3116
   __TEXT.__objc_methtype: 0x98f

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbb8
+  __DATA_CONST.__objc_selrefs: 0xc40
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__auth_got: 0x2f8
   __AUTH_CONST.__const: 0x650
   __AUTH_CONST.__cfstring: 0xca0
-  __AUTH_CONST.__objc_const: 0x27a8
+  __AUTH_CONST.__objc_const: 0x2180
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x3c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E03F4FA0-EF8F-3728-BD0D-2DED189D9592
-  Functions: 518
-  Symbols:   1380
+  UUID: 2AADBAD3-AC6D-309B-875B-FE6BC333C974
+  Functions: 525
+  Symbols:   1388
   CStrings:  1004
 
Symbols:
+ +[_ICInputContextManager sharedManager].cold.1
+ -[_ICInternalSource localizedStringForKey:withLocale:].cold.1
+ -[_ICNamedEntityStore exemplarSetForSupportedLocales].cold.1
+ -[_ICPortraitLexiconSource _makePPNamedEntityStore].cold.1
+ -[_ICPortraitPredictionSource _makePPQuickTypeBroker].cold.1
+ -[_ICTransientLexicon(TestingSupport) getEntryRefCount:].cold.1
+ _ICMachTimeToNanoseconds.cold.1
+ _ICPersContactOSLogFacility.cold.1
+ _ICPersNamedEntityOSLogFacility.cold.1
+ _ICProactiveQuickTypeOSLogFacility.cold.1
+ __122-[_ICPortraitPredictionSource _quickTypeQueryWithTrigger:searchContext:limit:timeoutInMilliseconds:errorWithExplanations:]_block_invoke.81
+ __48-[_ICPortraitLexiconSource _makeContactDelegate]_block_invoke.16
+ __48-[_ICPortraitLexiconSource _makeContactDelegate]_block_invoke.20
+ __48-[_ICPortraitLexiconSource _makeContactDelegate]_block_invoke.23
+ __52-[_ICPortraitLexiconSource _makeNamedEntityDelegate]_block_invoke.28
+ __52-[_ICPortraitLexiconSource _makeNamedEntityDelegate]_block_invoke_2.29
- -[_ICTransientLexicon addEntity:forEntry:].cold.1
- __122-[_ICPortraitPredictionSource _quickTypeQueryWithTrigger:searchContext:limit:timeoutInMilliseconds:errorWithExplanations:]_block_invoke.75
- __48-[_ICPortraitLexiconSource _makeContactDelegate]_block_invoke.10
- __48-[_ICPortraitLexiconSource _makeContactDelegate]_block_invoke.14
- __48-[_ICPortraitLexiconSource _makeContactDelegate]_block_invoke.17
- __52-[_ICPortraitLexiconSource _makeNamedEntityDelegate]_block_invoke.22
- __52-[_ICPortraitLexiconSource _makeNamedEntityDelegate]_block_invoke_2.23

```
