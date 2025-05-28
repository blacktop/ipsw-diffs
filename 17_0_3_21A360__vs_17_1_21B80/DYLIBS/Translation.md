## Translation

> `/System/Library/PrivateFrameworks/Translation.framework/Translation`

```diff

-249.2.0.0.0
-  __TEXT.__text: 0x25394
+252.2.1.0.0
+  __TEXT.__text: 0x25764
   __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_methlist: 0x35f8
+  __TEXT.__objc_methlist: 0x3638
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x190e
-  __TEXT.__oslogstring: 0x22aa
+  __TEXT.__cstring: 0x19e2
+  __TEXT.__oslogstring: 0x23db
   __TEXT.__gcc_except_tab: 0x2a0
-  __TEXT.__unwind_info: 0xb34
+  __TEXT.__unwind_info: 0xb40
   __TEXT.__objc_classname: 0x7d2
-  __TEXT.__objc_methname: 0x7463
-  __TEXT.__objc_methtype: 0x11c3
-  __TEXT.__objc_stubs: 0x3d60
+  __TEXT.__objc_methname: 0x74d7
+  __TEXT.__objc_methtype: 0x11ca
+  __TEXT.__objc_stubs: 0x3d80
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0xde8
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5d18
-  __DATA_CONST.__objc_selrefs: 0x18c8
+  __DATA_CONST.__objc_const: 0x5d58
+  __DATA_CONST.__objc_selrefs: 0x18e8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__cfstring: 0x2260
+  __AUTH_CONST.__cfstring: 0x22c0
   __AUTH_CONST.__objc_const: 0x1e80
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__objc_arrayobj: 0x30

   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x298
   __DATA.__objc_superrefs: 0x1a8
-  __DATA.__objc_ivar: 0x528
+  __DATA.__objc_ivar: 0x52c
   __DATA.__data: 0x480
   __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x780

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1366
-  Symbols:   4471
-  CStrings:  2064
+  Functions: 1375
+  Symbols:   4491
+  CStrings:  2076
 
Symbols:
+ -[_LTSpeakRequest audioStartHandler]
+ -[_LTSpeakRequest setAudioStartHandler:]
+ -[_LTSpeakRequest ttsAudioStarted:duration:]
+ -[_LTTextTranslationRequest _callCompletionHandlersWithResult:error:].cold.4
+ -[_LTTextTranslationRequest _cleanUpTemporaryStorage]
+ -[_LTTextTranslationRequest _handleParagraphResponse:error:].cold.1
+ -[_LTWordTimingInfo debugDescription]
+ -[_LTWordTimingInfo description]
+ -[_LTWordTimingInfo setStartTime:]
+ -[_LTWordTimingInfo setTextRange:]
+ -[_LTWordTimingInfo startTime]
+ -[_LTWordTimingInfo textRange]
+ -[_LTWordTimingInfo unredactedDescription]
+ GCC_except_table114
+ _OBJC_IVAR_$__LTSpeakRequest._audioStartHandler
+ _OBJC_IVAR_$__LTWordTimingInfo._startTime
+ _OBJC_IVAR_$__LTWordTimingInfo._textRange
+ _objc_msgSend$_cleanUpTemporaryStorage
+ _objc_msgSend$audioStartHandler
- -[_LTSpeakRequest setTtsProgressHandler:]
- -[_LTSpeakRequest ttsProgressHandler]
- -[_LTSpeakRequest ttsProgressed:]
- -[_LTWordTimingInfo setTimestamp:]
- -[_LTWordTimingInfo timestamp]
- GCC_except_table113
- _OBJC_IVAR_$__LTSpeakRequest._ttsProgressHandler
- _OBJC_IVAR_$__LTWordTimingInfo._timestamp
- _objc_msgSend$ttsProgressHandler
CStrings:
+ "<%@: %p; _sampleIndex: [%u]; _word length: %zu; _textRange: %@; _length: %u; _offset %u; _startTime %f>"
+ "<%@: %p; _sampleIndex: [%u]; _word: \"%@\"; _textRange: %@; _length: %u; _offset %u; _startTime %f>"
+ "Attempted to call _LTTextTranslationRequest completion handler with nil `_receivedParagraphs`; this completion handler was likely already called, or translation never started"
+ "Received a paragraph response with ID %{public}@, but we didn't expect any paragraphs to be outstanding; this should never happen"
+ "T@?,C,N,V_audioStartHandler"
+ "Td,N,V_startTime"
+ "T{_NSRange=QQ},N,V_textRange"
+ "_audioStartHandler"
+ "_cleanUpTemporaryStorage"
+ "_startTime"
+ "_textRange"
+ "audioStartHandler"
+ "setAudioStartHandler:"
+ "setStartTime:"
+ "setTextRange:"
+ "startTime"
+ "textRange"
+ "ttsAudioStarted:duration:"
+ "unredactedDescription"
+ "v32@0:8@\"NSArray\"16d24"
+ "v32@0:8@16d24"
- "T@?,C,N,V_ttsProgressHandler"
- "Td,N,V_timestamp"
- "_timestamp"
- "_ttsProgressHandler"
- "setTimestamp:"
- "setTtsProgressHandler:"
- "timestamp"
- "ttsProgressHandler"
- "ttsProgressed:"
- "v24@0:8@\"_LTWordTimingInfo\"16"

```
