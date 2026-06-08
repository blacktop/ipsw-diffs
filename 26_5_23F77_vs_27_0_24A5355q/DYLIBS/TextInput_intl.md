## TextInput_intl

> `/System/Library/TextInput/TextInput_intl.bundle/TextInput_intl`

```diff

-3532.5.3.100.0
-  __TEXT.__text: 0xef4
-  __TEXT.__auth_stubs: 0x180
+3557.12.1.0.0
+  __TEXT.__text: 0xdd0
   __TEXT.__objc_methlist: 0x164
-  __TEXT.__cstring: 0x13
+  __TEXT.__cstring: 0x15
   __TEXT.__ustring: 0x8
   __TEXT.__unwind_info: 0xb8
-  __TEXT.__objc_classname: 0x22
-  __TEXT.__objc_methname: 0x5a4
-  __TEXT.__objc_methtype: 0x96
-  __TEXT.__objc_stubs: 0x680
-  __DATA_CONST.__got: 0x68
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x210
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x110
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D1E63484-ADF2-3F19-B39F-212A59C9B825
+  UUID: 655BA484-2D92-3A54-AE91-260486B444BC
   Functions: 31
-  Symbols:   171
-  CStrings:  94
+  Symbols:   172
+  CStrings:  9
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
Functions:
~ -[TIKeyboardInputManager_intl_HWR recognizer] : 84 -> 68
~ ___45-[TIKeyboardInputManager_intl_HWR recognizer]_block_invoke : 136 -> 132
~ -[TIKeyboardInputManager_intl_HWR recognitionResultsForStrokes:context:] : 392 -> 384
~ -[TIKeyboardInputManager_intl_HWR updateCandidates] : 608 -> 572
~ -[TIKeyboardInputManager_intl_HWR candidateResultSet] : 248 -> 220
~ -[TIKeyboardInputManager_intl_HWR initialSelectedIndex] : 124 -> 120
~ -[TIKeyboardInputManager_intl_HWR isDummyCandidate:] : 100 -> 96
~ -[TIKeyboardInputManager_intl_HWR handleKeyboardInput:] : 196 -> 188
~ -[TIKeyboardInputManager_intl_HWR addInput:withContext:] : 304 -> 284
~ -[TIKeyboardInputManager_intl_HWR addInputObject:withContext:] : 684 -> 640
~ -[TIKeyboardInputManager_intl_HWR deleteFromInputWithContext:] : 92 -> 88
~ -[TIKeyboardInputManager_intl_HWR inputCount] : 60 -> 56
~ -[TIKeyboardInputManager_intl_HWR userDrawing] : 16 -> 20
~ -[TIKeyboardInputManager_intl_HWR setUserDrawing:] : 80 -> 20
~ -[TIKeyboardInputManager_intl_HWR candidates] : 16 -> 20
~ -[TIKeyboardInputManager_intl_HWR setCandidates:] : 80 -> 20
CStrings:
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"TIHandwritingStrokes\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "B16@0:8"
- "B24@0:8@16"
- "I16@0:8"
- "Q16@0:8"
- "T@\"CHRecognizer\",R,N"
- "T@\"NSArray\",&,N,V_candidates"
- "T@\"TIHandwritingStrokes\",&,N,V_userDrawing"
- "TIKeyboardInputManager_intl_HWR"
- "_candidates"
- "_firstChar"
- "_userDrawing"
- "acceptCurrentCandidateWithContext:"
- "addInput:withContext:"
- "addInputObject:withContext:"
- "addObject:"
- "addPoint:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "canHandleKeyHitTest"
- "candidate"
- "candidateResultSet"
- "candidateResultSetFromCandidates:"
- "candidateWithUnchangedInput:"
- "candidates"
- "characterIsMember:"
- "characterSetWithCharactersInString:"
- "clearInput"
- "closeCandidateGenerationContextWithResults:"
- "contextBeforeWithDesiredLength:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "defaultCandidate"
- "deleteBackward:"
- "deleteFromInputWithContext:"
- "dictionaryWithObjects:forKeys:count:"
- "dummySet"
- "endStroke"
- "firstObject"
- "handleKeyboardInput:"
- "initWithKeyboardState:"
- "initWithMode:locale:"
- "initialSelectedIndex"
- "inputCount"
- "inputLocationChanged"
- "insertText:"
- "isBackspace"
- "isDummyCandidate:"
- "isEqual:"
- "keyboardBehaviors"
- "keyboardState"
- "loadDictionaries"
- "localeWithLocaleIdentifier:"
- "null"
- "numberOfPointsInStrokeAtIndex:"
- "numberOfStrokes"
- "object"
- "output"
- "pointAtIndex:inStrokeAtIndex:"
- "recognitionResultsForDrawing:options:"
- "recognitionResultsForStrokes:context:"
- "recognizer"
- "setCandidates:"
- "setMaxRecognitionResultCount:"
- "setString:"
- "setUserDrawing:"
- "shouldExtendPriorWord"
- "string"
- "suppliesCompletions"
- "supportsLearning"
- "supportsReversionUI"
- "syncMarkedTextForKeyboardState:afterContextChange:"
- "updateCandidates"
- "userDrawing"
- "usesAutoDeleteWord"
- "usesCandidateSelection"
- "v16@0:8"
- "v24@0:8@16"
- "v28@0:8@16B24"
- "v32@0:8@16@24"

```
