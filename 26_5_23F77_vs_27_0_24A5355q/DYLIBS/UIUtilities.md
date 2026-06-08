## UIUtilities

> `/System/Library/SubFrameworks/UIUtilities.framework/UIUtilities`

```diff

-9126.5.5.2.103
-  __TEXT.__text: 0x15c0
-  __TEXT.__auth_stubs: 0x210
+9127.0.66.1.105
+  __TEXT.__text: 0x14c0
   __TEXT.__objc_methlist: 0x228
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x2cb
+  __TEXT.__cstring: 0x2d1
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0xf0
-  __TEXT.__objc_classname: 0x68
-  __TEXT.__objc_methname: 0x56b
-  __TEXT.__objc_methtype: 0xd0
-  __TEXT.__objc_stubs: 0x580
-  __DATA_CONST.__got: 0x40
+  __TEXT.__unwind_info: 0xe0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1a8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x40
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x3a0
   __AUTH_CONST.__objc_const: 0x478
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x20
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x190

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CC65FE72-5C26-32E4-899B-0D6838FE5899
+  UUID: B6B81393-59BA-3A0D-ACB1-25EC7225968E
   Functions: 44
-  Symbols:   227
-  CStrings:  145
+  Symbols:   232
+  CStrings:  58
 
Symbols:
+ ___block_literal_global.105
+ ___block_literal_global.99
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x27
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x8
- ___block_literal_global.100
- ___block_literal_global.106
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
Functions:
~ +[_UIDebugLogMessage messageWithString:] : 224 -> 216
~ -[_UIDebugLogMessage initWithString:] : 200 -> 204
~ +[_UIDebugLogMessage messageWithStyle:string:] : 304 -> 288
~ +[_UIDebugLogNodeTreeStyle defaultStyle] : 100 -> 84
~ ___40+[_UIDebugLogNodeTreeStyle defaultStyle]_block_invoke : 100 -> 96
~ -[_UIDebugLogNodeTreeStyle initWithNode:lastNode:intermediate:trailing:] : 224 -> 236
~ +[_UIDebugLogNodeTreeStyle styleWithNode:lastNode:intermediate:trailing:] : 148 -> 160
~ +[_UIDebugLogMessage messageWithFormat:] : 228 -> 220
~ +[_UIDebugLogMessage messageWithPrefix:string:] : 456 -> 436
~ -[_UIDebugLogMessage _stringRepresentation] : 56 -> 8
~ -[_UIDebugLogNode __genericAppendChildDescription:withPrefix:inheritedTreeStyle:recursionSelector:appendHandler:] : 600 -> 588
~ __prefixForItem : 288 -> 264
~ -[_UIDebugLogNode description] : 112 -> 108
~ -[_UIDebugLogNode setTreeStyle:] : 64 -> 12
~ -[__UIDebugLogRootNode description] : 376 -> 372
~ -[_UIDebugLogStack init] : 140 -> 132
~ -[_UIDebugLogStack addMessage:] : 228 -> 212
~ -[_UIDebugLogStack pushNode:] : 240 -> 224
~ -[_UIDebugLogStack popNode] : 172 -> 164
~ -[_UIDebugLogStack performWithPushedNode:block:] : 620 -> 600
CStrings:
- ".cxx_destruct"
- "@\"NSMutableArray\""
- "@\"NSString\""
- "@\"_UIDebugLogNodeTreeStyle\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@32@0:8Q16@24"
- "@48@0:8@16@24@32@40"
- "B16@0:8"
- "T@\"NSString\",R,N,V_intermediate"
- "T@\"NSString\",R,N,V_lastNode"
- "T@\"NSString\",R,N,V_node"
- "T@\"NSString\",R,N,V_trailing"
- "T@\"_UIDebugLogNode\",R,N"
- "T@\"_UIDebugLogNodeTreeStyle\",&,N,V_treeStyle"
- "TB,R,N"
- "_UIDebugLogMessage"
- "_UIDebugLogNode"
- "_UIDebugLogNodeTreeStyle"
- "_UIDebugLogStack"
- "__UIDebugLogRootNode"
- "__genericAppendChildDescription:withPrefix:inheritedTreeStyle:recursionSelector:appendHandler:"
- "_appendChildDescription:withPrefix:inheritedTreeStyle:"
- "_childMessages"
- "_intermediate"
- "_isNode"
- "_isTransparent"
- "_lastNode"
- "_node"
- "_stack"
- "_string"
- "_stringRepresentation"
- "_topNode"
- "_trailing"
- "_treeStyle"
- "addMessage:"
- "addObject:"
- "appendFormat:"
- "appendString:"
- "arrayWithObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "defaultStyle"
- "description"
- "firstObject"
- "handleFailureInFunction:file:lineNumber:description:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hasMessages"
- "indexOfObjectWithOptions:passingTest:"
- "init"
- "initWithFormat:arguments:"
- "initWithNode:lastNode:intermediate:trailing:"
- "initWithString:"
- "intermediate"
- "lastNode"
- "lastObject"
- "length"
- "messageWithFormat:"
- "messageWithNewline"
- "messageWithPrefix:string:"
- "messageWithString:"
- "messageWithStyle:string:"
- "mutableCopy"
- "node"
- "objectAtIndexedSubscript:"
- "performWithPushedNode:block:"
- "popNode"
- "pushNode:"
- "removeLastObject"
- "rootNode"
- "setTreeStyle:"
- "stringByAppendingString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "styleWithNode:lastNode:intermediate:trailing:"
- "trailing"
- "treeStyle"
- "uppercaseString"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@32"
- "v56@0:8@16@24@32:40@?48"

```
