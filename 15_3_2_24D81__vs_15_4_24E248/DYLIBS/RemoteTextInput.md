## RemoteTextInput

> `/System/Library/PrivateFrameworks/RemoteTextInput.framework/Versions/A/RemoteTextInput`

```diff

-159.205.0.0.0
-  __TEXT.__text: 0x210b0
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x2454
-  __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x2bdf
-  __TEXT.__oslogstring: 0xbf5
-  __TEXT.__gcc_except_tab: 0x1b4
+159.309.2.0.0
+  __TEXT.__text: 0x23be8
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_methlist: 0x2a0c
+  __TEXT.__const: 0x108
+  __TEXT.__cstring: 0x2f16
+  __TEXT.__oslogstring: 0xcb5
+  __TEXT.__gcc_except_tab: 0x290
   __TEXT.__dlopen_cstrs: 0x9b
-  __TEXT.__unwind_info: 0x848
-  __TEXT.__objc_classname: 0x3c3
-  __TEXT.__objc_methname: 0x6bb6
-  __TEXT.__objc_methtype: 0x1556
-  __TEXT.__objc_stubs: 0x3e40
-  __DATA_CONST.__got: 0x208
-  __DATA_CONST.__const: 0x1a0
-  __DATA_CONST.__objc_classlist: 0xf8
+  __TEXT.__unwind_info: 0x8f8
+  __TEXT.__objc_classname: 0x3d4
+  __TEXT.__objc_methname: 0x71fa
+  __TEXT.__objc_methtype: 0x16a6
+  __TEXT.__objc_stubs: 0x44e0
+  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__const: 0x230
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16b0
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x2a8
-  __AUTH_CONST.__const: 0xba0
-  __AUTH_CONST.__cfstring: 0x2860
-  __AUTH_CONST.__objc_const: 0x6818
-  __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x2f4
+  __DATA_CONST.__objc_selrefs: 0x1898
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0xc0
+  __AUTH_CONST.__auth_got: 0x2e8
+  __AUTH_CONST.__const: 0xd70
+  __AUTH_CONST.__cfstring: 0x2ce0
+  __AUTH_CONST.__objc_const: 0x6470
+  __AUTH.__objc_data: 0x730
+  __DATA.__objc_ivar: 0x318
   __DATA.__data: 0x420
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/AppSupport.framework/Versions/A/AppSupport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/TextInput.framework/Versions/A/TextInput
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 060FE893-08E4-3D5A-B1F6-13EA49F7D77F
-  Functions: 952
-  Symbols:   2381
-  CStrings:  2130
+  UUID: BD64B3AC-77A5-34C4-AC78-B966D2FE8D48
+  Functions: 1013
+  Symbols:   2560
+  CStrings:  2277
 
Symbols:
+ +[RTIDocumentState _enumerateDocumentRects:options:block:]
+ +[RTIInputSystemService sharedServiceWithMachName:].cold.1
+ +[RTIServiceOptions combinedServiceOptions:]
+ +[RTIServiceOptions defaultServiceOptionsForService:]
+ +[RTIServiceOptions defaultServiceOptions]
+ +[RTIServiceOptions supportsSecureCoding]
+ +[RTIStyledIntermediateText _attributedStringAllowedClasses].cold.1
+ +[RTITextOperations customInfoDictionary].cold.1
+ +[RTIUtilities _attributesToAllowForCoding]
+ +[RTIUtilities _attributesToAllowForCoding].cold.1
+ +[RTIUtilities _textAnnotationAttributes]
+ +[RTIUtilities _textAnnotationAttributes].cold.1
+ +[RTIUtilities currentClientCodingServiceOptions]
+ +[RTIUtilities customInfoDictionary].cold.1
+ +[RTIUtilities performClientCoding:withServiceOptions:]
+ -[RTIDocumentState attributedDocumentState]
+ -[RTIDocumentState documentStateByMergingInDocumentState:mergeResultOut:]
+ -[RTIDocumentState mergeInDocumentState:]
+ -[RTIDocumentState setAttributedDocumentState:]
+ -[RTIInputSystemClient _queueFromCurrentConnection:remoteTextInputSessionWithID:didUpdateServiceOptions:]
+ -[RTIInputSystemClient addMachNames:]
+ -[RTIInputSystemClient connectionServiceOptions]
+ -[RTIInputSystemClient endpointServiceOptions]
+ -[RTIInputSystemClient remoteTextInputSessionWithID:didUpdateServiceOptions:]
+ -[RTIInputSystemClient removeMachNames:]
+ -[RTIInputSystemClient serviceOptions]
+ -[RTIInputSystemClient setConnectionServiceOptions:]
+ -[RTIInputSystemClient setEndpointServiceOptions:]
+ -[RTIInputSystemSession documentStateAfterModifyAndFlushTextOperations:]
+ -[RTIInputSystemSession documentStateAfterModifyAndFlushTextOperations:resultHandler:]
+ -[RTIInputSystemSession modifyAndFlushTextOperations:]
+ -[RTIInputSystemSession modifyAndFlushTextOperations:resultHandler:]
+ -[RTIServiceOptions copyWithZone:]
+ -[RTIServiceOptions description]
+ -[RTIServiceOptions displayOptions]
+ -[RTIServiceOptions encodeWithCoder:]
+ -[RTIServiceOptions initWithCoder:]
+ -[RTIServiceOptions isEqual:]
+ -[RTIServiceOptions serviceDeviceClass]
+ -[RTIServiceOptions setDisplayOptions:]
+ -[RTIServiceOptions setServiceDeviceClass:]
+ -[RTITextOperations encodeWithCoder:].cold.1
+ -[RTITextOperations enumeratedInsertionAnimationStyle]
+ -[RTITextOperations setEnumeratedInsertionAnimationStyle:]
+ GCC_except_table108
+ GCC_except_table11
+ GCC_except_table118
+ GCC_except_table168
+ GCC_except_table17
+ GCC_except_table25
+ GCC_except_table29
+ GCC_except_table3
+ GCC_except_table43
+ GCC_except_table47
+ GCC_except_table55
+ OBJC_IVAR_$_RTIDocumentState._attributedDocumentState
+ OBJC_IVAR_$_RTIDocumentState._updateMask
+ OBJC_IVAR_$_RTIInputSystemClient._connectionServiceOptions
+ OBJC_IVAR_$_RTIInputSystemClient._connectionsLock
+ OBJC_IVAR_$_RTIInputSystemClient._endpointServiceOptions
+ OBJC_IVAR_$_RTIInputSystemClient._endpointsLock
+ OBJC_IVAR_$_RTIServiceOptions._displayOptions
+ OBJC_IVAR_$_RTIServiceOptions._serviceDeviceClass
+ OBJC_IVAR_$_RTITextOperations._enumeratedInsertionAnimationStyle
+ RTIInputSessionChangeLogFacility.cold.1
+ RTILogFacility.cold.1
+ _MGCopyAnswer
+ _NSGrammarCorrections
+ _NSGrammarRange
+ _NSGrammarUserDescription
+ _NSUnionRange
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_RTIServiceOptions
+ _OBJC_CLASS_$_TIAttributedDocumentState
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_METACLASS_$_RTIServiceOptions
+ _RTIAttributeNSAdaptiveImageGlyphKey
+ _RTIAttributeNSParagraphStyleKey
+ _RTIAttributeNSTextAttachmentKey
+ _RTIServiceOnenessName
+ __104-[RTIInputSystemServiceSession remoteTextInputSessionWithID:didRemoveSupplementalLexiconWithIdentifier:]_block_invoke.160
+ __107-[RTIInputSystemServiceSession remoteTextInputSessionWithID:didRemoveRTISupplementalLexiconWithIdentifier:]_block_invoke.170
+ __110-[RTIInputSystemServiceSession beginRemoteTextInputSessionWithID:options:documentTraits:initialDocumentState:]_block_invoke.116
+ __110-[RTIInputSystemServiceSession beginRemoteTextInputSessionWithID:options:documentTraits:initialDocumentState:]_block_invoke.120
+ __36-[RTIDocumentState encodeWithCoder:]_block_invoke_2.cold.1
+ __41-[RTIDocumentState mergeInDocumentState:]_block_invoke.153
+ __51-[RTIInputSystemServiceSession initWithConnection:]_block_invoke.93
+ __58-[RTIInputSystemClient _configureConnection:withMachName:]_block_invoke.132
+ __58-[RTIInputSystemClient _configureConnection:withMachName:]_block_invoke.134
+ __58-[RTIInputSystemClient _configureConnection:withMachName:]_block_invoke.137
+ __61-[RTIInputSystemClient enumerateConnections:force:withBlock:]_block_invoke.151
+ __61-[RTIInputSystemClient enumerateConnections:force:withBlock:]_block_invoke_2.152
+ __62-[RTIInputSystemClient endAllowingRemoteTextInput:completion:]_block_invoke.144
+ __66-[RTIInputSystemServiceSession performDocumentRequest:completion:]_block_invoke.104
+ __66-[RTIInputSystemServiceSession performDocumentRequest:completion:]_block_invoke.104.cold.1
+ __73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke.162
+ __73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke.165
+ __73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke.165.cold.1
+ __75-[RTIInputSystemClient endRemoteTextInputSessionWithID:options:completion:]_block_invoke.182
+ __OBJC_$_CLASS_METHODS_RTIServiceOptions
+ __OBJC_$_CLASS_PROP_LIST_RTIServiceOptions
+ __OBJC_$_INSTANCE_METHODS_RTIServiceOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTIServiceOptions
+ __OBJC_$_PROP_LIST_RTIServiceOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTIServiceOptions
+ __OBJC_CLASS_RO_$_RTIServiceOptions
+ __OBJC_METACLASS_RO_$_RTIServiceOptions
+ __OBJC_PROTOCOL_REFERENCE_$_NSSecureCoding
+ ___105-[RTIInputSystemClient _queueFromCurrentConnection:remoteTextInputSessionWithID:didUpdateServiceOptions:]_block_invoke
+ ___34-[RTIDocumentState initWithCoder:]_block_invoke
+ ___36-[RTIDocumentState encodeWithCoder:]_block_invoke
+ ___36-[RTIDocumentState encodeWithCoder:]_block_invoke_2
+ ___40-[RTIInputSystemClient removeMachNames:]_block_invoke
+ ___41+[RTIUtilities _textAnnotationAttributes]_block_invoke
+ ___41-[RTIDocumentState mergeInDocumentState:]_block_invoke
+ ___43+[RTIUtilities _attributesToAllowForCoding]_block_invoke
+ ___44+[RTIServiceOptions combinedServiceOptions:]_block_invoke
+ ___77-[RTIInputSystemClient remoteTextInputSessionWithID:didUpdateServiceOptions:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_32_e32_v32?0"NSXPCConnection"8Q16^B24l
+ ___block_descriptor_32_e36_"NSDictionary"16?0"NSDictionary"8l
+ ___block_descriptor_40_e8_32bs_e25_v16?0"NSXPCConnection"8l
+ ___block_descriptor_40_e8_32r_e25_v32?0"NSString"816^B24l
+ ___block_descriptor_40_e8_32r_e31_v24?0"RTIServiceOptions"8^B16l
+ ___block_descriptor_40_e8_32r_e31_v48?0{?={?=II}{?=ffff}iB}8^B40l
+ ___block_descriptor_48_e8_32s40bs_e32_v32?0"NSXPCConnection"8Q16^B24l
+ ___block_descriptor_48_e8_32s40r_e31_v48?0{?={?=II}{?=ffff}iB}8^B40l
+ ___block_descriptor_48_e8_32s_e41_v16?0"<RTIInputSystemSessionDelegate>"8l
+ ___block_descriptor_56_e8_32s40r48r_e32_v32?0"NSXPCConnection"8Q16^B24l
+ ___block_descriptor_56_e8_32s40s48bs_e42_v32?0"NSString"8"NSXPCConnection"16^B24l
+ ___block_descriptor_64_e8_32s40s48s56r_e32_v32?0"NSXPCConnection"8Q16^B24l
+ ___block_descriptor_64_e8_32s40s48w56w_e5_v8?0l
+ ___copy_helper_block_e8_32s40r48r
+ ___copy_helper_block_e8_32s40s48s56r
+ ___copy_helper_block_e8_32s40s48w56w
+ ___destroy_helper_block_e8_32s40r48r
+ ___destroy_helper_block_e8_32s40s48w56w
+ __block_literal_global.112
+ __block_literal_global.29
+ __block_literal_global.31
+ __block_literal_global.79
+ _attributesToAllowForCoding.attributesToAllow
+ _attributesToAllowForCoding.onceToken
+ _dispatch_get_current_queue
+ _dispatch_queue_get_specific
+ _dispatch_queue_set_specific
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$_attributesToAllowForCoding
+ _objc_msgSend$_enumerateDocumentRects:options:block:
+ _objc_msgSend$_queueFromCurrentConnection:remoteTextInputSessionWithID:didUpdateServiceOptions:
+ _objc_msgSend$_textAnnotationAttributes
+ _objc_msgSend$_ti_attributedStringByKeepingAttributes:
+ _objc_msgSend$addAttributes:range:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$allValues
+ _objc_msgSend$anyObject
+ _objc_msgSend$attributedDocumentState
+ _objc_msgSend$combinedServiceOptions:
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$currentClientCodingServiceOptions
+ _objc_msgSend$currentConnection
+ _objc_msgSend$defaultServiceOptions
+ _objc_msgSend$defaultServiceOptionsForService:
+ _objc_msgSend$displayOptions
+ _objc_msgSend$documentStateByMergingInDocumentState:mergeResultOut:
+ _objc_msgSend$documentStateWithAttributeIterator:
+ _objc_msgSend$enumeratedInsertionAnimationStyle
+ _objc_msgSend$firstSelectionRectInEntitySpace
+ _objc_msgSend$flushOperations
+ _objc_msgSend$inputSession:documentStateDidChange:withMergeResult:
+ _objc_msgSend$intValue
+ _objc_msgSend$keyEnumerator
+ _objc_msgSend$mergeInDocumentState:
+ _objc_msgSend$nextObject
+ _objc_msgSend$null
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$objectEnumerator
+ _objc_msgSend$objectsForKeys:notFoundMarker:
+ _objc_msgSend$performClientCoding:withServiceOptions:
+ _objc_msgSend$remoteTextInputSessionWithID:didUpdateServiceOptions:
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$removeObjectsInArray:
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$serviceDeviceClass
+ _objc_msgSend$serviceName
+ _objc_msgSend$serviceOptions
+ _objc_msgSend$serviceOptionsDidChange:
+ _objc_msgSend$setAttributedDocumentState:
+ _objc_msgSend$setAutocorrectBubbleStyling:
+ _objc_msgSend$setAutocorrectTextBackgroundColor:
+ _objc_msgSend$setAutocorrectTextColor:
+ _objc_msgSend$setCanSuggestSupplementalItemsForCurrentSelection:
+ _objc_msgSend$setCaretRectInWindow:
+ _objc_msgSend$setClientFrameInEntitySpace:
+ _objc_msgSend$setClientFrameInWindow:
+ _objc_msgSend$setFirstSelectionRectInEntitySpace:
+ _objc_msgSend$setFirstSelectionRectInWindow:
+ _objc_msgSend$setHasText:
+ _objc_msgSend$setInsertionPointColor:
+ _objc_msgSend$setOriginatedFromSource:
+ _objc_msgSend$setScrolling:
+ _objc_msgSend$setTabStops:
+ _objc_msgSend$setTextCheckingAnnotatedString:
+ _objc_msgSend$setTextLists:
+ _objc_opt_new
+ _textAnnotationAttributes._attributes
+ _textAnnotationAttributes.onceToken
- +[RTIUtilities _attributedStringWithoutDefaultAttributes:]
- -[RTIInputSystemClient _canResumeConnection]
- GCC_except_table105
- GCC_except_table14
- GCC_except_table15
- GCC_except_table151
- GCC_except_table26
- GCC_except_table27
- GCC_except_table40
- _OUTLINED_FUNCTION_4
- _RTIAttributeNSTextAttributeKey
- __104-[RTIInputSystemServiceSession remoteTextInputSessionWithID:didRemoveSupplementalLexiconWithIdentifier:]_block_invoke.153
- __107-[RTIInputSystemServiceSession remoteTextInputSessionWithID:didRemoveRTISupplementalLexiconWithIdentifier:]_block_invoke.163
- __110-[RTIInputSystemServiceSession beginRemoteTextInputSessionWithID:options:documentTraits:initialDocumentState:]_block_invoke.114
- __110-[RTIInputSystemServiceSession beginRemoteTextInputSessionWithID:options:documentTraits:initialDocumentState:]_block_invoke.118
- __51-[RTIInputSystemServiceSession initWithConnection:]_block_invoke.91
- __58-[RTIInputSystemClient _configureConnection:withMachName:]_block_invoke.125
- __58-[RTIInputSystemClient _configureConnection:withMachName:]_block_invoke.127
- __58-[RTIInputSystemClient _configureConnection:withMachName:]_block_invoke.130
- __58-[RTIInputSystemClient enumerateServices:force:withBlock:]_block_invoke.139
- __62-[RTIInputSystemClient endAllowingRemoteTextInput:completion:]_block_invoke.137
- __66-[RTIInputSystemServiceSession performDocumentRequest:completion:]_block_invoke.102
- __66-[RTIInputSystemServiceSession performDocumentRequest:completion:]_block_invoke.102.cold.1
- __73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke.149
- __73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke.153
- __73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke.153.cold.1
- __75-[RTIInputSystemClient endRemoteTextInputSessionWithID:options:completion:]_block_invoke.169
- ___58+[RTIUtilities _attributedStringWithoutDefaultAttributes:]_block_invoke
- ___58+[RTIUtilities _attributedStringWithoutDefaultAttributes:]_block_invoke_2
- ___block_descriptor_32_e29_v24?0"NSXPCConnection"8^B16l
- ___block_descriptor_40_e8_32bs_e29_v24?0"NSXPCConnection"8^B16l
- ___block_descriptor_40_e8_32s_e45_v40?0"NSTextAttachment"8{_NSRange=QQ}16^B32l
- ___block_descriptor_48_e8_32s40bs_e42_v32?0"NSString"8"NSXPCConnection"16^B24l
- ___block_descriptor_48_e8_32s40r_e29_v24?0"NSXPCConnection"8^B16l
- __block_literal_global.27
- _attributedStringWithoutDefaultAttributes:.attributesToRemove
- _attributedStringWithoutDefaultAttributes:.onceToken
- _objc_msgSend$_attributedStringWithoutDefaultAttributes:
- _objc_msgSend$enumerateAttribute:inRange:options:usingBlock:
- _objc_msgSend$removeAttribute:range:
- _objc_msgSend$set
- _objc_msgSend$setAttributes:range:
CStrings:
+ "%s  RTIDocumentState with TIAttributedDocumentState: non-serializable attribute encountered: %@"
+ "%s  RTITextOperations with textCheckingAnnotatedString: non-serializable string encountered: %@"
+ "(?=\"integerValue\"I\"fields\"{?=\"setHasText\"b1\"setScrolling\"b1\"setOriginatedFromSource\"b1\"setCanSuggestSupplementalItemsForCurrentSelection\"b1})"
+ ")"
+ "-[RTIDocumentState encodeWithCoder:]_block_invoke_2"
+ "-[RTITextOperations encodeWithCoder:]"
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
+ "setAttributedDocumentState:"
+ "setConnectionServiceOptions:"
+ "setDisplayOptions:"
+ "setEndpointServiceOptions:"
+ "setEnumeratedInsertionAnimationStyle:"
+ "setServiceDeviceClass:"
+ "setTabStops:"
+ "setTextLists:"
+ "updateMask"
+ "v24@?0@\"RTIServiceOptions\"8^B16"
+ "v32@0:8@?16@24"
+ "v32@?0@\"NSXPCConnection\"8Q16^B24"
+ "v40@0:8@\"RTIInputSystemSession\"16@\"RTIDocumentState\"24Q32"
+ "v40@0:8@16@24Q32"
+ "v40@0:8@16Q24@?32"
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
