## TextInput_ja

> `/System/Library/TextInput/TextInput_ja.bundle/TextInput_ja`

```diff

-  __TEXT.__text: 0x1e4c0
+  __TEXT.__text: 0x1e6e0
   __TEXT.__init_offsets: 0x18
-  __TEXT.__objc_methlist: 0x2148
+  __TEXT.__objc_methlist: 0x2150
   __TEXT.__cstring: 0xd3c
   __TEXT.__ustring: 0x250
   __TEXT.__const: 0x238

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1840
+  __DATA_CONST.__objc_selrefs: 0x1858
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x290
   __DATA_CONST.__got: 0x380
   __AUTH_CONST.__const: 0x1b0
   __AUTH_CONST.__cfstring: 0x1440
-  __AUTH_CONST.__objc_const: 0x26c0
+  __AUTH_CONST.__objc_const: 0x26f0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x1f0
+  __DATA.__objc_ivar: 0x1f4
   __DATA.__data: 0x320
   __DATA.__bss: 0xe8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 745
-  Symbols:   2778
+  Functions: 746
+  Symbols:   2784
   CStrings:  425
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[TIWordSearchJapaneseOperationGetCandidates initWithWordSearch:inputString:keyboardInput:contextString:onScreenContext:segmentBreakIndex:predictionEnabled:reanalysisMode:autocapitalizationType:target:action:geometryModelData:flickUsed:phraseBoundarySet:hardwareKeyboardMode:logger:]
+ -[TIWordSearchJapaneseOperationGetCandidates onScreenContext]
+ -[TIWordSearchKana makeCandidates:input:contextString:onScreenContext:predictionEnabled:reanalysisMode:withInputManager:geometryModelData:flickUsed:hardwareKeyboardMode:referenceMode:singlePhrase:]
+ _OBJC_IVAR_$_TIWordSearchJapaneseOperationGetCandidates._onScreenContext
+ _objc_msgSend$initWithWordSearch:inputString:keyboardInput:contextString:onScreenContext:segmentBreakIndex:predictionEnabled:reanalysisMode:autocapitalizationType:target:action:geometryModelData:flickUsed:phraseBoundarySet:hardwareKeyboardMode:logger:
+ _objc_msgSend$makeCandidates:input:contextString:onScreenContext:predictionEnabled:reanalysisMode:withInputManager:geometryModelData:flickUsed:hardwareKeyboardMode:referenceMode:singlePhrase:
+ _objc_msgSend$onScreenContext
+ _objc_msgSend$onScreenContextForCandidates
+ _objc_msgSend$setOnScreenContext:
- -[TIWordSearchJapaneseOperationGetCandidates initWithWordSearch:inputString:keyboardInput:contextString:segmentBreakIndex:predictionEnabled:reanalysisMode:autocapitalizationType:target:action:geometryModelData:flickUsed:phraseBoundarySet:hardwareKeyboardMode:logger:]
- -[TIWordSearchKana makeCandidates:input:contextString:predictionEnabled:reanalysisMode:withInputManager:geometryModelData:flickUsed:hardwareKeyboardMode:referenceMode:singlePhrase:]
- _objc_msgSend$initWithWordSearch:inputString:keyboardInput:contextString:segmentBreakIndex:predictionEnabled:reanalysisMode:autocapitalizationType:target:action:geometryModelData:flickUsed:phraseBoundarySet:hardwareKeyboardMode:logger:
- _objc_msgSend$makeCandidates:input:contextString:predictionEnabled:reanalysisMode:withInputManager:geometryModelData:flickUsed:hardwareKeyboardMode:referenceMode:singlePhrase:

```
