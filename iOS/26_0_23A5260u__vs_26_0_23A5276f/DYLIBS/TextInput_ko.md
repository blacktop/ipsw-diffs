## TextInput_ko

> `/System/Library/TextInput/TextInput_ko.bundle/TextInput_ko`

```diff

-3504.100.0.0.0
-  __TEXT.__text: 0x5bec
-  __TEXT.__auth_stubs: 0x4e0
+3508.0.0.0.0
+  __TEXT.__text: 0x52b8
+  __TEXT.__auth_stubs: 0x460
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0x3dc
-  __TEXT.__cstring: 0xe0
+  __TEXT.__objc_methlist: 0x38c
+  __TEXT.__cstring: 0xd2
   __TEXT.__ustring: 0x8e
-  __TEXT.__const: 0x4e0
+  __TEXT.__const: 0x4d0
   __TEXT.__unwind_info: 0x78
   __TEXT.__objc_classname: 0x51
-  __TEXT.__objc_methname: 0xe04
-  __TEXT.__objc_methtype: 0x1b7
-  __TEXT.__objc_stubs: 0xd60
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x98
+  __TEXT.__objc_methname: 0xa98
+  __TEXT.__objc_methtype: 0x199
+  __TEXT.__objc_stubs: 0x960
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x488
+  __DATA_CONST.__objc_selrefs: 0x3a8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x550
-  __AUTH_CONST.__auth_got: 0x278
+  __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__const: 0xb0
-  __AUTH_CONST.__cfstring: 0xbc0
-  __AUTH_CONST.__objc_const: 0x360
+  __AUTH_CONST.__cfstring: 0xba0
+  __AUTH_CONST.__objc_const: 0x300
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x24
+  __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x78
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2434CCBD-3974-37FC-B435-789ABCB21F4A
-  Functions: 168
-  Symbols:   573
-  CStrings:  343
+  UUID: 7D4F5704-983A-3E0C-BDA7-DA2060614CB6
+  Functions: 159
+  Symbols:   507
+  CStrings:  307
 
Symbols:
+ +[TIKeyboardInputManager_ko generateKeyLayoutMapReverse]
+ +[TIKeyboardInputManager_ko generateKeyLayoutMap]
- -[TIKeyboardInputManager_ko externalStringToInternal:]
- -[TIKeyboardInputManager_ko externalStringToInternal:ignoreCompositionDisabled:]
- -[TIKeyboardInputManager_ko initializeKeyLayoutMaps]
- -[TIKeyboardInputManager_ko internalStringToExternal:]
- -[TIKeyboardInputManager_ko internalStringToSecondaryExternal:]
- -[TIKeyboardInputManager_ko keyLayoutMapReverse]
- -[TIKeyboardInputManager_ko keyLayoutMap]
- -[TIKeyboardInputManager_ko setInput:withIndex:]
- -[TIKeyboardInputManager_ko validUSetForAutocorrectionSecondary]
- _OBJC_CLASS_$_TIAutocorrectionList
- _OBJC_CLASS_$_TICorrectionCandidates
- _OBJC_IVAR_$_TIKeyboardInputManager_ko._keyLayoutMap
- _OBJC_IVAR_$_TIKeyboardInputManager_ko._keyLayoutMapReverse
- __ZN14TIInputManager25or_input_flags_from_inputERKN2KB6StringE
- __ZN2KB11utf8_stringEP8NSString
- __ZNK14TIInputManager12is_uppercaseEj
- __ZZ64-[TIKeyboardInputManager_ko validUSetForAutocorrectionSecondary]E10onceToken2
- __ZZ64-[TIKeyboardInputManager_ko validUSetForAutocorrectionSecondary]E13secondary_set
- ___48-[TIKeyboardInputManager_ko setInput:withIndex:]_block_invoke
- ___64-[TIKeyboardInputManager_ko validUSetForAutocorrectionSecondary]_block_invoke
- ___block_descriptor_40_a8_32s_e5_v8?0ls32l8
- ___block_descriptor_48_a8_32r_e12_v20?0I8^B12lr32l8
- _objc_alloc
- _objc_msgSend$_enumerateLongCharactersInRange:usingBlock:
- _objc_msgSend$alternateCorrections
- _objc_msgSend$autocorrection
- _objc_msgSend$candidateArray:withCandidateUniquelyInsertedToFront:
- _objc_msgSend$candidateByReplacingWithCandidate:
- _objc_msgSend$corrections
- _objc_msgSend$emojiList
- _objc_msgSend$externalStringToInternal:ignoreCompositionDisabled:
- _objc_msgSend$externalStringToInternal:ignoreCompositionDisabled:useReverseMap:
- _objc_msgSend$generateTypingAutocorrectionsWithCandidateRange:
- _objc_msgSend$hasPrefix:
- _objc_msgSend$initWithAutocorrection:alternateCorrections:
- _objc_msgSend$initializeKeyLayoutMaps
- _objc_msgSend$input
- _objc_msgSend$internalStringToExternal:ignoreCompositionDisabled:
- _objc_msgSend$internalStringToSecondaryExternal:
- _objc_msgSend$isEqual:
- _objc_msgSend$keyLayoutMap
- _objc_msgSend$keyLayoutMapReverse
- _objc_msgSend$lexiconLocale
- _objc_msgSend$listWithCorrections:predictions:emojiList:proactiveTriggers:
- _objc_msgSend$predictions
- _objc_msgSend$proactiveTriggers
- _objc_msgSend$reasonForFreezing
- _objc_msgSend$setChoseSecondary:
- _objc_msgSend$setPregeneratedTypingAutocorrections:
- _objc_msgSend$shouldDynamicallySwitchBetweenPrimaryAndSecondary
- _objc_msgSend$stringByAppendingString:
- _objc_msgSend$substringWithRange:
- _objc_msgSend$updateAutocorrectionListGivenOutdatedInput:andUpdatedInput:
- _objc_msgSend$uppercaseString
- _objc_msgSend$validUSetForAutocorrectionSecondary
- _objc_release_x28
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x19
- _objc_retain_x26
CStrings:
+ "!"
+ "generateKeyLayoutMap"
+ "generateKeyLayoutMapReverse"
- ""
- "#"
- "@\"NSDictionary\""
- "T@\"NSDictionary\",R,N,V_keyLayoutMap"
- "T@\"NSDictionary\",R,N,V_keyLayoutMapReverse"
- "_enumerateLongCharactersInRange:usingBlock:"
- "_keyLayoutMap"
- "_keyLayoutMapReverse"
- "alternateCorrections"
- "autocorrection"
- "candidateArray:withCandidateUniquelyInsertedToFront:"
- "candidateByReplacingWithCandidate:"
- "corrections"
- "emojiList"
- "externalStringToInternal:ignoreCompositionDisabled:"
- "generateTypingAutocorrectionsWithCandidateRange:"
- "hasPrefix:"
- "initWithAutocorrection:alternateCorrections:"
- "initializeKeyLayoutMaps"
- "input"
- "internalStringToSecondaryExternal:"
- "isEqual:"
- "keyLayoutMap"
- "keyLayoutMapReverse"
- "lexiconLocale"
- "listWithCorrections:predictions:emojiList:proactiveTriggers:"
- "predictions"
- "proactiveTriggers"
- "reasonForFreezing"
- "setChoseSecondary:"
- "setInput:withIndex:"
- "setPregeneratedTypingAutocorrections:"
- "stringByAppendingString:"
- "substringWithRange:"
- "updateAutocorrectionListGivenOutdatedInput:andUpdatedInput:"
- "uppercaseString"
- "v20@?0I8^B12"
- "v28@0:8@16I24"
- "validUSetForAutocorrectionSecondary"

```
