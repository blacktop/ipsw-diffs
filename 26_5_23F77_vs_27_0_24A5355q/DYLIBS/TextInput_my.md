## TextInput_my

> `/System/Library/TextInput/TextInput_my.bundle/TextInput_my`

```diff

-3532.5.3.100.0
-  __TEXT.__text: 0xce0
-  __TEXT.__auth_stubs: 0x210
+3557.12.1.0.0
+  __TEXT.__text: 0xcb8
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x8
   __TEXT.__ustring: 0x50
   __TEXT.__cstring: 0x24e
-  __TEXT.__objc_classname: 0x1a
-  __TEXT.__objc_methname: 0x2bb
-  __TEXT.__objc_methtype: 0x1f
-  __TEXT.__objc_stubs: 0x2c0
-  __DATA_CONST.__got: 0x38
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x1e0
   __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__weak_auth_got: 0x8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__data: 0x28
   __DATA.__bss: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 76967D14-B4DB-34C2-942D-C133BEFE2DE4
+  UUID: 71AFC541-B2C4-34DA-A8E1-5E402335FCC5
   Functions: 16
-  Symbols:   120
-  CStrings:  50
+  Symbols:   123
+  CStrings:  20
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
+ _objc_storeStrong
- _objc_release_x9
- _objc_retain
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[TIKeyboardInputManager_my internalStringToExternal:] : 524 -> 520
~ ___54-[TIKeyboardInputManager_my internalStringToExternal:]_block_invoke : 976 -> 960
~ ___54-[TIKeyboardInputManager_my internalStringToExternal:]_block_invoke_3 : 76 -> 72
~ -[TIKeyboardInputManager_my externalStringToInternal:] : 288 -> 312
~ ___54-[TIKeyboardInputManager_my externalStringToInternal:]_block_invoke : 336 -> 324
~ -[TIKeyboardInputManager_my deleteFromInput:] : 600 -> 580
~ ____ZL23InternalToExternalRegexv_block_invoke : 120 -> 116
~ ____ZL23ExternalToInternalRegexv_block_invoke : 120 -> 116
CStrings:
- "@24@0:8@16"
- "@24@0:8^Q16"
- "B16@0:8"
- "TIKeyboardInputManager_my"
- "characterAtIndex:"
- "characterIsMember:"
- "characterSetWithCharactersInString:"
- "deleteCharactersInRange:"
- "deleteFromInput:"
- "deletesComposedTextByComposedCharacterSequence"
- "doesComposeText"
- "enumerateMatchesInString:options:range:usingBlock:"
- "externalStringToInternal:"
- "getCharacters:range:"
- "hasSuffix:"
- "inputIndex"
- "insertString:atIndex:"
- "internalStringToExternal:"
- "length"
- "mutableCopy"
- "range"
- "rangeAtIndex:"
- "rangeOfComposedCharacterSequenceAtIndex:"
- "regularExpressionWithPattern:options:error:"
- "replaceCharactersInRange:withString:"
- "replaceOccurrencesOfString:withString:options:range:"
- "setString:"
- "stringWithCharacters:length:"
- "substringWithRange:"
- "suffixOfDesiredString:toAppendToInputString:withInputIndex:afterDeletionCount:"

```
