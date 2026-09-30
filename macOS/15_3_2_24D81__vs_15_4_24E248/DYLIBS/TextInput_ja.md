## TextInput_ja

> `/System/Library/TextInput/TextInput_ja.bundle/Versions/A/TextInput_ja`

```diff

-3479.227.0.0.0
-  __TEXT.__text: 0x21cd0
+3479.319.0.0.0
+  __TEXT.__text: 0x21ed0
   __TEXT.__auth_stubs: 0x540
   __TEXT.__init_offsets: 0x18
-  __TEXT.__objc_methlist: 0x20ac
+  __TEXT.__objc_methlist: 0x2130
   __TEXT.__cstring: 0xd1b
   __TEXT.__ustring: 0x250
   __TEXT.__const: 0x240
   __TEXT.__oslogstring: 0xf7
-  __TEXT.__unwind_info: 0x360
+  __TEXT.__unwind_info: 0x368
   __TEXT.__objc_classname: 0x344
-  __TEXT.__objc_methname: 0x5e70
+  __TEXT.__objc_methname: 0x5e7b
   __TEXT.__objc_methtype: 0x607
-  __TEXT.__objc_stubs: 0x54a0
+  __TEXT.__objc_stubs: 0x54c0
   __DATA_CONST.__got: 0x380
   __DATA_CONST.__const: 0x540
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1818
+  __DATA_CONST.__objc_selrefs: 0x1820
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x290
   __AUTH_CONST.__auth_got: 0x2a8
   __AUTH_CONST.__const: 0x5a0
   __AUTH_CONST.__cfstring: 0x1440
-  __AUTH_CONST.__objc_const: 0x2788
+  __AUTH_CONST.__objc_const: 0x2690
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x780

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2964D930-7593-3F4C-987C-3287C967189B
-  Functions: 743
-  Symbols:   1993
-  CStrings:  1498
+  UUID: 2203ECA4-64C3-3669-9191-90FC006F6E47
+  Functions: 757
+  Symbols:   2009
+  CStrings:  1499
 
Symbols:
+ +[NSCharacterSet(RomajiAdditions) alphabetCharacterSet].cold.1
+ -[TIKeyboardInputManagerLiveConversion_ja validCharacterSetForAutocorrection].cold.1
+ -[TIKeyboardInputManager_ja groupedCandidatesFromCandidates:usingSortingMethod:].cold.1
+ -[TIKeyboardInputManager_ja groupedCandidatesFromCandidates:usingSortingMethod:completion:].cold.1
+ -[TIKeyboardInputManager_ja groupedCandidatesFromCandidates:usingSortingMethod:completion:].cold.2
+ -[TIKeyboardInputManager_ja groupedCandidatesFromCandidates:usingSortingMethod:inputString:].cold.1
+ -[TIKeyboardInputManager_ja hasGroupedCandidatesFromCandidates:usingSortingMethod:inputString:].cold.1
+ -[TIKeyboardInputManager_ja_Candidates groupedCandidatesFromCandidates:usingSortingMethod:].cold.1
+ -[TIKeyboardInputManager_ja_Candidates sortingMethods].cold.1
+ -[TIKeyboardInputManager_ja_Kana validCharacterSetForAutocorrection].cold.1
+ -[TIKeyboardInputManager_ja_Romaji handleKeyboardInput:].cold.1
+ -[TIKeyboardInputManager_ja_Romaji validCharacterSetForAutocorrection].cold.1
+ -[TIWordSearchKana shouldMoveCursor:].cold.1
+ TransliterateStringWithOption.cold.1
+ _ZL24GetMultitapSequenceTablev.cold.1
+ __54-[TIKeyboardInputManager_ja mecabraLearningValidator:]_block_invoke.cold.2
+ __MergedGlobals
+ __ZNSt3__119__shared_weak_count16__release_sharedB8nn190102Ev
+ _objc_msgSend$isSiriMode
- __ZGVZ56-[TIKeyboardInputManager_ja_Romaji handleKeyboardInput:]E10whitespace
- __ZNSt3__119__shared_weak_count16__release_sharedB8nn180100Ev
- __ZZ56-[TIKeyboardInputManager_ja_Romaji handleKeyboardInput:]E10whitespace
CStrings:
+ "isSiriMode"

```
