## RemoteTextInput

> `/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput`

```diff

-159.206.0.0.0
-  __TEXT.__text: 0x1ec5c
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x2594
-  __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x2c0c
-  __TEXT.__oslogstring: 0xc0c
-  __TEXT.__gcc_except_tab: 0x1cc
+159.308.0.0.0
+  __TEXT.__text: 0x21040
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_methlist: 0x2b64
+  __TEXT.__const: 0x108
+  __TEXT.__cstring: 0x2f29
+  __TEXT.__oslogstring: 0xc6c
+  __TEXT.__gcc_except_tab: 0x270
   __TEXT.__dlopen_cstrs: 0xf6
-  __TEXT.__unwind_info: 0x858
-  __TEXT.__objc_classname: 0x408
-  __TEXT.__objc_methname: 0x6ddf
-  __TEXT.__objc_methtype: 0x15f5
-  __TEXT.__objc_stubs: 0x4040
-  __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0xae8
-  __DATA_CONST.__objc_classlist: 0x100
+  __TEXT.__unwind_info: 0x920
+  __TEXT.__objc_classname: 0x419
+  __TEXT.__objc_methname: 0x746f
+  __TEXT.__objc_methtype: 0x1745
+  __TEXT.__objc_stubs: 0x4700
+  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__const: 0xc88
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1738
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xd0
-  __AUTH_CONST.__auth_got: 0x380
-  __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x28e0
-  __AUTH_CONST.__objc_const: 0x6cc0
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x304
+  __DATA_CONST.__objc_selrefs: 0x1928
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0xd8
+  __AUTH_CONST.__auth_got: 0x3b0
+  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__cfstring: 0x2d60
+  __AUTH_CONST.__objc_const: 0x68f8
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x328
   __DATA.__data: 0x480
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x9b0
-  __DATA_DIRTY.__bss: 0x68
+  __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TextInput.framework/TextInput
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 949
-  Symbols:   1209
-  CStrings:  1855
+  Functions: 1007
+  Symbols:   1279
+  CStrings:  1964
 
Symbols:
+ _MGCopyAnswer
+ _NSUnionRange
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_RTIServiceOptions
+ _OBJC_CLASS_$_TIAttributedDocumentState
+ _OBJC_METACLASS_$_RTIServiceOptions
+ _RTIAttributeNSAdaptiveImageGlyphKey
+ _RTIAttributeNSTextAttachmentKey
+ _RTIServiceOnenessName
+ ___NSArray0__struct
+ _dispatch_get_current_queue
+ _dispatch_queue_get_specific
+ _dispatch_queue_set_specific
+ _objc_opt_new
+ _objc_retain_x26
- _RTIAttributeNSTextAttributeKey
- _objc_retain_x28
CStrings:
+ "\x14\x18\x16"
+ "%s  RTIDocumentState with TIAttributedDocumentState: non-serializable attribute encountered: %@"
+ "(?=\"integerValue\"I\"fields\"{?=\"setHasText\"b1\"setScrolling\"b1\"setOriginatedFromSource\"b1\"setCanSuggestSupplementalItemsForCurrentSelection\"b1})"
+ ")"
+ "-[RTIDocumentState encodeWithCoder:]_block_invoke_2"
+ "-[RTIInputSystemUIClient _initializeConnectionWithMachName:serviceName:]"
+ "; attributedDocumentState = %@"
+ "; deviceClass = %@"
+ "; displayOptions = %lu"
+ "; enumeratedInsertionAnimationStyle = %ld"
+ "@\"NSDictionary\"16@?0@\"NSDictionary\"8"
+ "@\"TIAttributedDocumentState\""
+ "@32@0:8@16^Q24"
+ "AppleTV"
+ "CTAdaptiveImageProvider"
+ "DeviceClassNumber"
+ "Mac"
+ "NSAccessibilitySpellingState"
+ "NSDominantLanguageAttributeName"
+ "NSDominantScriptAttributeName"
+ "NSGrammarAutocorrected"
+ "NSGrammarConfidenceScore"
+ "NSGrammarIssueType"
+ "NSGrammarLanguage"
+ "NSGrammarLeftOffsetAttributeName"
+ "NSGrammarRightOffsetAttributeName"
+ "NSGrammarTargetPair"
+ "NSIgnoringSubstitution"
+ "NSOrthography"
+ "NSReplacedString"
+ "NSSpellingState"
+ "NSTemporaryTextCorrection"
+ "NSTextAlternativesDisplayStyle"
+ "NSTextChecked"
+ "NSTextCorrection"
+ "NSTextEdited"
+ "NSTextReverted"
+ "RTIServiceOptions"
+ "T@\"NSMutableArray\",&,N,V_endpointConnections"
+ "T@\"NSMutableArray\",&,N,V_endpointServiceOptions"
+ "T@\"NSMutableArray\",&,N,V_machNames"
+ "T@\"NSMutableDictionary\",&,N,V_connectionServiceOptions"
+ "T@\"RTIServiceOptions\",R,N"
+ "T@\"TIAttributedDocumentState\",&,N,V_attributedDocumentState"
+ "TQ,N,V_displayOptions"
+ "Ti,N,V_serviceDeviceClass"
+ "Tq,N,V_enumeratedInsertionAnimationStyle"
+ "Unknown"
+ "VisionPro"
+ "Vv32@0:8@\"NSUUID\"16@\"RTIServiceOptions\"24"
+ "Watch"
+ "["
+ "_attributedDocumentState"
+ "_attributesToAllowForCoding"
+ "_connectionServiceOptions"
+ "_connectionsLock"
+ "_displayOptions"
+ "_endpointServiceOptions"
+ "_endpointsLock"
+ "_enumerateDocumentRects:options:block:"
+ "_enumeratedInsertionAnimationStyle"
+ "_initializeConnectionWithMachName:serviceName:"
+ "_queueFromCurrentConnection:remoteTextInputSessionWithID:didUpdateServiceOptions:"
+ "_serviceDeviceClass"
+ "_textAnnotationAttributes"
+ "_ti_attributedStringByKeepingAttributes:"
+ "_updateMask"
+ "addAttributes:range:"
+ "addMachNames:"
+ "addObjectsFromArray:"
+ "allValues"
+ "anyObject"
+ "attrDocSt"
+ "attributedDocumentState"
+ "com.apple.rti-screencontinuity"
+ "combinedServiceOptions:"
+ "connectionServiceOptions"
+ "currentClientCodingServiceOptions"
+ "currentConnection"
+ "defaultServiceOptions"
+ "defaultServiceOptionsForService:"
+ "deviceClass"
+ "displayOptions"
+ "documentStateByMergingInDocumentState:mergeResultOut:"
+ "documentStateWithAttributeIterator:"
+ "endpointServiceOptions"
+ "enumeratedInsertionAnimationStyle"
+ "iPad"
+ "iPhone"
+ "iPod"
+ "initWithUIHostMachName:serviceName:"
+ "inputSession:documentStateDidChange:withMergeResult:"
+ "insertionAnimationStyle"
+ "intValue"
+ "kRTIUtilitiesClientCodingQueueContextKey"
+ "keyEnumerator"
+ "mergeInDocumentState:"
+ "nextObject"
+ "null"
+ "objectAtIndex:"
+ "objectEnumerator"
+ "objectsForKeys:notFoundMarker:"
+ "performClientCoding:withServiceOptions:"
+ "remoteTextInputSessionWithID:didUpdateServiceOptions:"
+ "removeMachNames:"
+ "removeObjectAtIndex:"
+ "removeObjectsForKeys:"
+ "removeObjectsInArray:"
+ "replaceObjectAtIndex:withObject:"
+ "serviceDeviceClass"
+ "serviceName"
+ "serviceOptions"
+ "serviceOptionsDidChange:"
+ "setActivateOnResume"
+ "setAttributedDocumentState:"
+ "setConnectionServiceOptions:"
+ "setDisplayOptions:"
+ "setEndpointServiceOptions:"
+ "setEnumeratedInsertionAnimationStyle:"
+ "setServiceDeviceClass:"
+ "updateMask"
+ "v24@?0@\"RTIServiceOptions\"8^B16"
+ "v32@0:8@?16@24"
+ "v32@?0@\"NSXPCConnection\"8Q16^B24"
+ "v40@0:8@\"RTIInputSystemSession\"16@\"RTIDocumentState\"24Q32"
+ "v40@0:8@16@24Q32"
+ "v40@0:8@16Q24@?32"
- "\x18"
- "\x1c\x16"
- "-[RTIInputSystemUIClient _initializeConnectionWithMachName:]"
- "1"
- "IMMentionAutomaticConfirmedMention"
- "T@\"NSArray\",&,N,V_machNames"
- "T@\"NSMutableSet\",&,N,V_endpointConnections"
- "T{_NSRange=QQ},N"
- "_UIAnimatedTextSpacer"
- "_attributedStringWithoutDefaultAttributes:"
- "enumerateAttribute:inRange:options:usingBlock:"
- "font_base_key"
- "paragraph_style_base_key"
- "removeAttribute:range:"
- "set"
- "setAttributes:range:"
- "v24@?0@\"NSXPCConnection\"8^B16"
- "v40@?0@\"NSTextAttachment\"8{_NSRange=QQ}16^B32"

```
