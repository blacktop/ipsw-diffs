## EditScript

> `/System/Library/PrivateFrameworks/EditScript.framework/EditScript`

```diff

 4.0.0.0.0
-  __TEXT.__text: 0x3764
-  __TEXT.__auth_stubs: 0x2a0
+  __TEXT.__text: 0x398c
+  __TEXT.__auth_stubs: 0x290
   __TEXT.__objc_methlist: 0x5fc
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x4d6
   __TEXT.__ustring: 0x126
-  __TEXT.__unwind_info: 0x150
+  __TEXT.__unwind_info: 0x168
   __TEXT.__objc_classname: 0x97
   __TEXT.__objc_methname: 0xda9
   __TEXT.__objc_methtype: 0x3bb

   __DATA_CONST.__objc_selrefs: 0x3b8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x158
+  __AUTH_CONST.__auth_got: 0x150
   __AUTH_CONST.__cfstring: 0xae0
   __AUTH_CONST.__objc_const: 0x9a0
   __AUTH_CONST.__objc_intobj: 0x48

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3E6A0887-2FCC-3D68-BE89-7A4F707996E4
+  UUID: ACB23D65-1E51-3611-98BD-1661C5067FF7
   Functions: 97
-  Symbols:   426
+  Symbols:   425
   CStrings:  390
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x8
Functions:
~ -[ESEditScriptDataArray initWithString:chunkSize:] : 660 -> 684
~ _IsCharacterAtIndexMemberOfCharacterSet : 196 -> 192
~ -[ESEditScriptDataArray stringValue] : 100 -> 112
~ -[ESEditScriptDataArray lengthOfItem:] : 60 -> 64
~ -[ESEditScriptDataArray indexOfFirstDifferenceWithOtherData:shouldReverseIterate:fallsOnWordBoundary:] : 400 -> 412
~ -[ESEditScriptDataArray setData:] : 12 -> 64
~ -[ESEditScriptDataArray setCachedStringValue:] : 12 -> 64
~ -[ESEditScript initWithOperationPrecedence:orderAtomsAscending:] : 176 -> 184
~ -[ESEditScript description] : 404 -> 420
~ -[ESEditScript computeDistanceMatrix] : 472 -> 476
~ -[ESEditScript computeEditsFromMatrix] : 716 -> 740
~ -[ESEditScript setScript:] : 12 -> 64
~ -[ESEditScriptIndexed initWithOperationPrecedence:dataClass:fromArray:toArray:orderAtomsAscending:] : 224 -> 228
~ +[ESEditScriptIndexed editScriptFromArray:toArray:orderAtomsAscending:operationPrecedence:] : 180 -> 176
~ -[ESEditScriptIndexed applyToArray:] : 456 -> 472
~ -[ESEditScriptIndexed finalizeCurrentScriptAtom] : 424 -> 436
~ _TestEditScriptRanged : 372 -> 376
~ _TestEditScriptSmallestSingleEditRanged : 300 -> 308
~ _TestEditScriptIndexed : 692 -> 708
~ _TestEditScript : 388 -> 392
~ _TestSmallestEditThinkLikeAHuman : 444 -> 456
~ _TestEditScriptDataArray : 172 -> 184
~ _main : 1120 -> 1140
~ -[ESAtomRanged isEqualToEditScriptAtomRanged:] : 260 -> 276
~ -[ESAtomRanged setReplacementText:] : 12 -> 64
~ -[ESIntArray2D description] : 296 -> 304
~ -[ESEditScriptRanged initWithOperationPrecedence:dataClass:chunkSize:stringA:stringB:orderAtomsAscending:options:] : 260 -> 264
~ +[ESEditScriptRanged editScriptFromString:toString:chunkSize:orderAtomsAscending:operationPrecedence:options:] : 348 -> 352
~ -[ESEditScriptRanged applyToString:] : 368 -> 380
~ -[ESEditScriptRanged addToCurrentScriptAtomEditOperation:editIndex:newText:indexInArrayB:] : 388 -> 400
~ -[ESEditScriptRanged finalizeCurrentScriptAtom] : 436 -> 452
~ -[ESEditScriptRanged computeSmallestSingleEdit] : 356 -> 372
~ +[ESEditScriptRanged editScriptForSmallestSingleEditFromString:toString:chunkSize:] : 180 -> 176
~ -[ESAtomIndexed description] : 296 -> 300
~ -[ESAtomIndexed setReplacementText:] : 12 -> 64

```
