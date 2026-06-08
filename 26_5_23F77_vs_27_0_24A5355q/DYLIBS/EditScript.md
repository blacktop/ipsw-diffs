## EditScript

> `/System/Library/PrivateFrameworks/EditScript.framework/EditScript`

```diff

 4.0.0.0.0
-  __TEXT.__text: 0x398c
-  __TEXT.__auth_stubs: 0x290
+  __TEXT.__text: 0x37dc
   __TEXT.__objc_methlist: 0x5fc
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x4d6
+  __TEXT.__cstring: 0x4e1
   __TEXT.__ustring: 0x126
-  __TEXT.__unwind_info: 0x168
-  __TEXT.__objc_classname: 0x97
-  __TEXT.__objc_methname: 0xda9
-  __TEXT.__objc_methtype: 0x3bb
-  __TEXT.__objc_stubs: 0xb00
-  __DATA_CONST.__got: 0x78
+  __TEXT.__unwind_info: 0x150
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_selrefs: 0x3b8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0x78
   __AUTH_CONST.__cfstring: 0xae0
   __AUTH_CONST.__objc_const: 0x9a0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x58
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F7963B86-D4F9-3858-8085-FE115C9336F5
+  UUID: 8AA0194E-B19B-30D2-B4AD-857E55FA38EC
   Functions: 97
-  Symbols:   425
-  CStrings:  390
+  Symbols:   426
+  CStrings:  165
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x22
- _objc_retain_x24
- _objc_retain_x28
Functions:
~ -[ESEditScriptDataArray initWithString:chunkSize:] : 684 -> 660
~ _IsCharacterAtIndexMemberOfCharacterSet : 192 -> 196
~ -[ESEditScriptDataArray stringValue] : 112 -> 100
~ -[ESEditScriptDataArray lengthOfItem:] : 64 -> 60
~ -[ESEditScriptDataArray indexOfFirstDifferenceWithOtherData:shouldReverseIterate:fallsOnWordBoundary:] : 412 -> 400
~ -[ESEditScriptDataArray setData:] : 64 -> 12
~ -[ESEditScriptDataArray setCachedStringValue:] : 64 -> 12
~ -[ESEditScript initWithOperationPrecedence:orderAtomsAscending:] : 184 -> 176
~ -[ESEditScript description] : 420 -> 408
~ -[ESEditScript computeDistanceMatrix] : 476 -> 464
~ -[ESEditScript computeEditsFromMatrix] : 740 -> 720
~ -[ESEditScript setScript:] : 64 -> 12
~ -[ESEditScriptIndexed initWithOperationPrecedence:dataClass:fromArray:toArray:orderAtomsAscending:] : 228 -> 232
~ +[ESEditScriptIndexed editScriptFromArray:toArray:orderAtomsAscending:operationPrecedence:] : 176 -> 180
~ -[ESEditScriptIndexed applyToArray:] : 472 -> 460
~ -[ESEditScriptIndexed initializeCurrentScriptAtom] : 20 -> 24
~ -[ESEditScriptIndexed addToCurrentScriptAtomEditOperation:editIndex:newText:indexInArrayB:] : 164 -> 168
~ _TestEditScriptRanged : 376 -> 372
~ _TestEditScriptSmallestSingleEditRanged : 308 -> 300
~ _TestEditScriptIndexed : 708 -> 696
~ _TestEditScript : 392 -> 388
~ _TestSmallestEditThinkLikeAHuman : 456 -> 444
~ _TestEditScriptDataArray : 184 -> 172
~ _main : 1140 -> 1120
~ -[ESAtomRanged isEqualToEditScriptAtomRanged:] : 276 -> 260
~ -[ESAtomRanged setReplacementText:] : 64 -> 12
~ -[ESIntArray2D description] : 304 -> 296
~ -[ESIntArray2D ::] : 68 -> 72
~ -[ESIntArray2D ::newValue:] : 72 -> 76
~ -[ESEditScriptRanged initWithOperationPrecedence:dataClass:chunkSize:stringA:stringB:orderAtomsAscending:options:] : 264 -> 272
~ -[ESEditScriptRanged stringA] : 20 -> 24
~ -[ESEditScriptRanged stringB] : 20 -> 24
~ +[ESEditScriptRanged editScriptFromString:toString:chunkSize:orderAtomsAscending:operationPrecedence:options:] : 352 -> 348
~ -[ESEditScriptRanged applyToString:] : 380 -> 372
~ -[ESEditScriptRanged initializeCurrentScriptAtom] : 20 -> 24
~ -[ESEditScriptRanged addToCurrentScriptAtomEditOperation:editIndex:newText:indexInArrayB:] : 400 -> 408
~ -[ESEditScriptRanged finalizeCurrentScriptAtom] : 452 -> 448
~ -[ESEditScriptRanged removeAnyOverlapBetweenIndexOfFirstDifference:andReverseIndexOfLastDifference:shouldShortenFirstDifference:] : 160 -> 168
~ -[ESEditScriptRanged computeSmallestSingleEdit] : 372 -> 364
~ +[ESEditScriptRanged editScriptForSmallestSingleEditFromString:toString:chunkSize:] : 176 -> 180
~ -[ESAtomIndexed description] : 300 -> 296
~ -[ESAtomIndexed setReplacementText:] : 64 -> 12
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "::"
- "::newValue:"
- "::outOfBoundsReturnValue:"
- "@\"<ESEditScriptData>\""
- "@\"<ESEditScriptData>\"24@0:8@\"NSArray\"16"
- "@\"<ESEditScriptData>\"32@0:8@\"NSString\"16q24"
- "@\"ESAtomIndexed\""
- "@\"ESAtomRanged\""
- "@\"ESIntArray2D\""
- "@\"NSArray\""
- "@\"NSMutableArray\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8q16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8q16"
- "@28@0:8q16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@32@0:8Q16Q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24q32"
- "@40@0:8{_NSRange=QQ}16@32"
- "@44@0:8@16@24B32q36"
- "@48@0:8q16Q24@32Q40"
- "@52@0:8q16#24@32@40B48"
- "@60@0:8@16@24q32B40q44q52"
- "@68@0:8q16#24q32@40@48B56q60"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8Q16Q24"
- "ESAtomIndexed"
- "ESAtomRanged"
- "ESEditScript"
- "ESEditScriptData"
- "ESEditScriptDataArray"
- "ESEditScriptIndexed"
- "ESEditScriptRanged"
- "ESIntArray2D"
- "EditScriptDataWithArray:"
- "EditScriptDataWithString:chunkSize:"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"NSArray\",&,N,V_data"
- "T@\"NSArray\",C,N,V_operationPrecedenceArray"
- "T@\"NSMutableArray\",&,N,V_script"
- "T@\"NSString\",&,N,V_cachedStringValue"
- "T@\"NSString\",&,N,V_replacementText"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,W,N"
- "TB,N,V_shouldBoundsCheck"
- "TQ,N,V_indexInArrayB"
- "TQ,N,V_indexToEdit"
- "TQ,R"
- "TQ,R,N,V_iSize"
- "TQ,R,N,V_jSize"
- "Tq,N,V_editOperation"
- "T{_NSRange=QQ},N,V_editRange"
- "UTF8String"
- "Vv16@0:8"
- "^q"
- "^{_NSZone=}16@0:8"
- "_arrayData"
- "_cachedStringValue"
- "_currentOperation"
- "_currentScriptAtom"
- "_data"
- "_distanceMatrix"
- "_editOperation"
- "_editRange"
- "_iSize"
- "_indexInArrayB"
- "_indexToEdit"
- "_itemAData"
- "_itemBData"
- "_jSize"
- "_operationPrecedenceArray"
- "_options"
- "_orderAtomsAscending"
- "_replacementText"
- "_script"
- "_shouldBoundsCheck"
- "addObject:"
- "addToCurrentScriptAtomEditOperation:editIndex:newText:indexInArrayB:"
- "appendFormat:"
- "appendString:"
- "applyToArray:"
- "applyToString:"
- "arrayWithCapacity:"
- "arrayWithISize:jSize:"
- "assertBoundsForIIndex:jIndex:"
- "atomWithEditOperation:indexToEdit:newText:indexInArrayB:"
- "atomWithEditRange:replacementText:"
- "autorelease"
- "cachedStringValue"
- "characterAtIndex:"
- "characterIndexForItem:"
- "characterIsMember:"
- "class"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "computeDistanceMatrix"
- "computeEditsFromMatrix"
- "computeSmallestSingleEdit"
- "conformsToProtocol:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "data"
- "dealloc"
- "debugDescription"
- "description"
- "editOperation"
- "editRange"
- "editScriptForSmallestSingleEditFromString:toString:"
- "editScriptForSmallestSingleEditFromString:toString:chunkSize:"
- "editScriptFromArray:toArray:"
- "editScriptFromArray:toArray:orderAtomsAscending:operationPrecedence:"
- "editScriptFromString:toString:"
- "editScriptFromString:toString:chunkSize:orderAtomsAscending:operationPrecedence:options:"
- "enumerateSubstringsInRange:options:usingBlock:"
- "finalizeCurrentScriptAtom"
- "firstObject"
- "formUnionWithCharacterSet:"
- "hash"
- "iSize"
- "inBoundsForIIndex:jIndex:"
- "indexInArrayB"
- "indexOfFirstDifferenceWithOtherData:shouldReverseIterate:fallsOnWordBoundary:"
- "indexToEdit"
- "init"
- "initWithArray:"
- "initWithEditOperation:indexToEdit:newText:indexInArrayB:"
- "initWithEditRange:replacementText:"
- "initWithFormat:arguments:"
- "initWithISize:jSize:"
- "initWithOperationPrecedence:dataClass:chunkSize:stringA:stringB:orderAtomsAscending:options:"
- "initWithOperationPrecedence:dataClass:fromArray:toArray:orderAtomsAscending:"
- "initWithOperationPrecedence:orderAtomsAscending:"
- "initWithString:chunkSize:"
- "initializeCurrentScriptAtom"
- "insertObject:atIndex:"
- "integerValue"
- "isEqual:"
- "isEqualToEditScriptAtomRanged:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "jSize"
- "length"
- "lengthOfItem:"
- "longCharacterIsMember:"
- "mutableCopy"
- "objectAtIndex:"
- "operationPrecedenceArray"
- "operationPrecedenceArrayFromOperationPrecedence:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "punctuationCharacterSet"
- "q16@0:8"
- "q24@0:8q16"
- "q32@0:8Q16Q24"
- "q36@0:8@\"<ESEditScriptData>\"16B24^B28"
- "q36@0:8@16B24^B28"
- "q40@0:8Q16Q24q32"
- "release"
- "removeAnyOverlapBetweenIndexOfFirstDifference:andReverseIndexOfLastDifference:shouldShortenFirstDifference:"
- "removeObjectAtIndex:"
- "replaceCharactersInRange:withString:"
- "replacementText"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "script"
- "self"
- "setCachedStringValue:"
- "setData:"
- "setEditOperation:"
- "setEditRange:"
- "setIndexInArrayB:"
- "setIndexToEdit:"
- "setObject:atIndexedSubscript:"
- "setOperationPrecedenceArray:"
- "setReplacementText:"
- "setScript:"
- "setShouldBoundsCheck:"
- "shouldBoundsCheck"
- "stringA"
- "stringAtIndex:"
- "stringB"
- "stringValue"
- "stringWithCapacity:"
- "stringWithFormat:"
- "substringWithRange:"
- "superclass"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v32@0:8Q16Q24"
- "v32@0:8{_NSRange=QQ}16"
- "v36@0:8^q16^q24B32"
- "v40@0:8Q16Q24q32"
- "v48@0:8q16Q24@32Q40"
- "whitespaceAndNewlineCharacterSet"
- "whitespaceCharacterSet"
- "zone"
- "{_NSRange=\"location\"Q\"length\"Q}"
- "{_NSRange=QQ}16@0:8"

```
