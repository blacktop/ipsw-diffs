## BaseBoard

> `/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard`

```diff

-651.5.0.0.0
-  __TEXT.__text: 0x8b5d0
+652.108.0.0.0
+  __TEXT.__text: 0x92134
   __TEXT.__auth_stubs: 0x2050
-  __TEXT.__objc_methlist: 0x59fc
-  __TEXT.__const: 0x238
-  __TEXT.__gcc_except_tab: 0xddf8
-  __TEXT.__cstring: 0x7a06
+  __TEXT.__objc_methlist: 0x5cbc
+  __TEXT.__const: 0x240
+  __TEXT.__gcc_except_tab: 0xe4d0
+  __TEXT.__cstring: 0x7c72
   __TEXT.__oslogstring: 0x2fc4
   __TEXT.__dlopen_cstrs: 0xe8
-  __TEXT.__ustring: 0x1c
-  __TEXT.__unwind_info: 0x4c90
-  __TEXT.__objc_classname: 0xea1
-  __TEXT.__objc_methname: 0xa6fa
-  __TEXT.__objc_methtype: 0x1ff0
-  __TEXT.__objc_stubs: 0x6ae0
+  __TEXT.__ustring: 0x20
+  __TEXT.__unwind_info: 0x4e48
+  __TEXT.__objc_classname: 0xec8
+  __TEXT.__objc_methname: 0xacf6
+  __TEXT.__objc_methtype: 0x206a
+  __TEXT.__objc_stubs: 0x6be0
   __DATA_CONST.__got: 0x320
-  __DATA_CONST.__const: 0x19e8
-  __DATA_CONST.__objc_classlist: 0x3f0
+  __DATA_CONST.__const: 0x1b48
+  __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9a38
-  __DATA_CONST.__objc_selrefs: 0x2ce0
+  __DATA_CONST.__objc_const: 0x9f88
+  __DATA_CONST.__objc_selrefs: 0x2e48
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x4f0
+  __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__objc_const: 0x38a0
-  __AUTH_CONST.__cfstring: 0x78a0
+  __AUTH_CONST.__objc_const: 0x3978
+  __AUTH_CONST.__cfstring: 0x7d00
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__const: 0x9a0
+  __AUTH_CONST.__const: 0xa80
   __AUTH_CONST.__auth_got: 0x1038
-  __AUTH.__objc_data: 0x1270
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x4e0
-  __DATA.__objc_superrefs: 0x2c0
-  __DATA.__objc_ivar: 0x778
-  __DATA.__data: 0xe58
+  __AUTH.__objc_data: 0x12c0
+  __DATA.__objc_ivar: 0x7b8
+  __DATA.__data: 0xe60
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x20
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_ivar: 0x38
-  __DATA_DIRTY.__objc_data: 0x14f0
+  __DATA_DIRTY.__objc_data: 0x1540
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x408
+  __DATA_DIRTY.__bss: 0x478
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 250D0C3E-C00F-36A9-9C07-BFE22E78B504
-  Functions: 2780
-  Symbols:   9996
-  CStrings:  5018
+  UUID: 92218324-64F6-3920-997F-053F08482085
+  Functions: 2872
+  Symbols:   10241
+  CStrings:  5165
 
Symbols:
+ +[BSAuditToken invalidToken]
+ +[BSDescriptionStream descriptionForRootObject:withStyle:]
+ +[BSDescriptionStyle build:]
+ +[BSDescriptionStyle collectionLineBreakEachItemStyle]
+ +[BSDescriptionStyle collectionLineBreakNoneStyle]
+ +[BSDescriptionStyle debugStyle]
+ +[BSDescriptionStyle defaultCollectionLineBreakStyle]
+ +[BSDescriptionStyle keyValuePairSortedByKeyStyle]
+ +[BSDescriptionStyle new]
+ +[BSDescriptionStyle styleForEndTruncatingCollectionsOverItemCount:]
+ +[BSDescriptionStyle succinctStyle]
+ -[BSDescriptionBuilder appendCustomFormatWithNameFromObjectDescription:block:]
+ -[BSDescriptionBuilder hasDebugStyle]
+ -[BSDescriptionBuilder hasSuccinctStyle]
+ -[BSDescriptionBuilder style]
+ -[BSDescriptionStream _appendDictionary:withName:itemBlock:]
+ -[BSDescriptionStream _appendSectionWithTotalItemCount:truncatedItemCount:openDelimiter:closeDelimiter:block:]
+ -[BSDescriptionStream _overlayStyle:block:]
+ -[BSDescriptionStream _overrideCollectionLineBreaking:force:block:]
+ -[BSDescriptionStream appendCustomFormatForValue:withCustomFormatForName:]
+ -[BSDescriptionStream appendCustomFormatWithNameFromObjectDescription:block:]
+ -[BSDescriptionStream hasDebugStyle]
+ -[BSDescriptionStream hasSuccinctStyle]
+ -[BSDescriptionStream initWithDescriptionStyle:]
+ -[BSDescriptionStream overlayStyle:block:]
+ -[BSDescriptionStream style]
+ -[BSDescriptionStyle .cxx_destruct]
+ -[BSDescriptionStyle _initWithCopyOf:]
+ -[BSDescriptionStyle _init]
+ -[BSDescriptionStyle _styleByOverlayingStyle:]
+ -[BSDescriptionStyle appendDescriptionToFormatter:]
+ -[BSDescriptionStyle bodyItemSeparator]
+ -[BSDescriptionStyle clientInformation]
+ -[BSDescriptionStyle collectionLineBreak]
+ -[BSDescriptionStyle collectionTruncationStyle]
+ -[BSDescriptionStyle copyWithZone:]
+ -[BSDescriptionStyle debugging]
+ -[BSDescriptionStyle description]
+ -[BSDescriptionStyle hash]
+ -[BSDescriptionStyle init]
+ -[BSDescriptionStyle isEqual:]
+ -[BSDescriptionStyle keyValuePairSorting]
+ -[BSDescriptionStyle maximumItemCountForTruncation]
+ -[BSDescriptionStyle maximumNameLengthBeforeTruncation]
+ -[BSDescriptionStyle maximumValueLengthBeforeTruncation]
+ -[BSDescriptionStyle mutableCopyWithZone:]
+ -[BSDescriptionStyle nameTruncation]
+ -[BSDescriptionStyle proemItemSeparator]
+ -[BSDescriptionStyle styleByOverlayingStyle:]
+ -[BSDescriptionStyle valueTruncation]
+ -[BSDescriptionStyle verbosity]
+ -[BSMutableDescriptionStyle copyWithZone:]
+ -[BSMutableDescriptionStyle setBodyItemSeparator:]
+ -[BSMutableDescriptionStyle setClientInformation:]
+ -[BSMutableDescriptionStyle setCollectionLineBreak:]
+ -[BSMutableDescriptionStyle setCollectionTruncationStyle:]
+ -[BSMutableDescriptionStyle setDebugging:]
+ -[BSMutableDescriptionStyle setKeyValuePairSorting:]
+ -[BSMutableDescriptionStyle setMaximumItemCountForTruncation:]
+ -[BSMutableDescriptionStyle setMaximumNameLengthBeforeTruncation:]
+ -[BSMutableDescriptionStyle setMaximumValueLengthBeforeTruncation:]
+ -[BSMutableDescriptionStyle setNameTruncation:]
+ -[BSMutableDescriptionStyle setProemItemSeparator:]
+ -[BSMutableDescriptionStyle setValueTruncation:]
+ -[BSMutableDescriptionStyle setVerbosity:]
+ -[_BSActionResponder _consumeLock_trySendResponse:alreadyLocked:alreadyOnResponseQueue:fireLegacyInvalidationHandler:]
+ -[_BSActionResponder _lock_invalidateForEncode:]
+ GCC_except_table84
+ GCC_except_table85
+ GCC_except_table86
+ GCC_except_table87
+ GCC_except_table88
+ _.str.102
+ _BSDescribeTruncationCommit
+ _NSStringFromBSDescriptionCollectionLineBreak
+ _NSStringFromBSDescriptionCollectionTruncationStyle
+ _NSStringFromBSDescriptionDebugging
+ _NSStringFromBSDescriptionItemSeparator
+ _NSStringFromBSDescriptionKeyValuePairSorting
+ _NSStringFromBSDescriptionLineTruncation
+ _NSStringFromBSDescriptionVerbosity
+ _OBJC_CLASS_$_BSDescriptionStyle
+ _OBJC_CLASS_$_BSMutableDescriptionStyle
+ _OBJC_IVAR_$_BSDescriptionStream._forceSuccinct
+ _OBJC_IVAR_$_BSDescriptionStream._lineTruncation
+ _OBJC_IVAR_$_BSDescriptionStream._maximumLengthBeforeTruncation
+ _OBJC_IVAR_$_BSDescriptionStream._proemNestCount
+ _OBJC_IVAR_$_BSDescriptionStream._style
+ _OBJC_IVAR_$_BSDescriptionStream._truncationStartIndex
+ _OBJC_IVAR_$_BSDescriptionStyle._bodyItemSeparator
+ _OBJC_IVAR_$_BSDescriptionStyle._clientInformation
+ _OBJC_IVAR_$_BSDescriptionStyle._collectionLineBreak
+ _OBJC_IVAR_$_BSDescriptionStyle._collectionTruncationStyle
+ _OBJC_IVAR_$_BSDescriptionStyle._debugging
+ _OBJC_IVAR_$_BSDescriptionStyle._keyValuePairSorting
+ _OBJC_IVAR_$_BSDescriptionStyle._maximumItemCountForTruncation
+ _OBJC_IVAR_$_BSDescriptionStyle._maximumNameLengthBeforeTruncation
+ _OBJC_IVAR_$_BSDescriptionStyle._maximumValueLengthBeforeTruncation
+ _OBJC_IVAR_$_BSDescriptionStyle._nameTruncation
+ _OBJC_IVAR_$_BSDescriptionStyle._proemItemSeparator
+ _OBJC_IVAR_$_BSDescriptionStyle._valueTruncation
+ _OBJC_IVAR_$_BSDescriptionStyle._verbosity
+ _OBJC_IVAR_$__BSActionResponder._originator_responseQueue
+ _OBJC_METACLASS_$_BSDescriptionStyle
+ _OBJC_METACLASS_$_BSMutableDescriptionStyle
+ __BSCollectionLineBreakEachItemStyle
+ __BSCollectionLineBreakNoneStyle
+ __BSDefaultCollectionLineBreakStyle
+ __BSDefaultDescriptionStyle
+ __OBJC_$_CLASS_METHODS_BSAuditToken
+ __OBJC_$_CLASS_METHODS_BSDescriptionStyle
+ __OBJC_$_INSTANCE_METHODS_BSAuditToken
+ __OBJC_$_INSTANCE_METHODS_BSDescriptionStyle
+ __OBJC_$_INSTANCE_METHODS_BSMutableDescriptionStyle
+ __OBJC_$_INSTANCE_VARIABLES_BSDescriptionStyle
+ __OBJC_$_PROP_LIST_BSBlockSentinelSignalContext.62
+ __OBJC_$_PROP_LIST_BSDescriptionFormatting
+ __OBJC_$_PROP_LIST_BSDescriptionStyle
+ __OBJC_$_PROP_LIST_BSMutableDescriptionStyle
+ __OBJC_$_PROP_LIST_BSTimer.111
+ __OBJC_CLASS_PROTOCOLS_$_BSDescriptionStyle
+ __OBJC_CLASS_RO_$_BSDescriptionStyle
+ __OBJC_CLASS_RO_$_BSMutableDescriptionStyle
+ __OBJC_METACLASS_RO_$_BSDescriptionStyle
+ __OBJC_METACLASS_RO_$_BSMutableDescriptionStyle
+ ___110-[BSDescriptionStream _appendSectionWithTotalItemCount:truncatedItemCount:openDelimiter:closeDelimiter:block:]_block_invoke
+ ___118-[_BSActionResponder _consumeLock_trySendResponse:alreadyLocked:alreadyOnResponseQueue:fireLegacyInvalidationHandler:]_block_invoke
+ ___32+[BSDescriptionStyle debugStyle]_block_invoke
+ ___35+[BSDescriptionStyle succinctStyle]_block_invoke
+ ___35-[BSDescriptionStream setSortKeys:]_block_invoke
+ ___50+[BSDescriptionStyle keyValuePairSortedByKeyStyle]_block_invoke
+ ___51-[BSDescriptionStyle appendDescriptionToFormatter:]_block_invoke
+ ___59-[BSDescriptionStream appendCollection:withName:itemBlock:]_block_invoke_3
+ ___60-[BSDescriptionStream _appendDictionary:withName:itemBlock:]_block_invoke
+ ___60-[BSDescriptionStream _appendDictionary:withName:itemBlock:]_block_invoke_2
+ ___60-[BSDescriptionStream _appendDictionary:withName:itemBlock:]_block_invoke_3
+ ___60-[BSDescriptionStream _appendDictionary:withName:itemBlock:]_block_invoke_4
+ ___60-[BSDescriptionStream _appendDictionary:withName:itemBlock:]_block_invoke_5
+ ___78-[BSDescriptionBuilder appendCustomFormatWithNameFromObjectDescription:block:]_block_invoke
+ ____BSCollectionLineBreakEachItemStyle_block_invoke
+ ____BSCollectionLineBreakNoneStyle_block_invoke
+ ____BSDefaultCollectionLineBreakStyle_block_invoke
+ ____BSDefaultDescriptionStyle_block_invoke
+ ____BSXPCDecodeObject_block_invoke.250
+ ___block_descriptor_33_e35_v16?0"BSMutableDescriptionStyle"8l
+ ___block_descriptor_40_ea8_32bs_e11_v24?0816ls32l8
+ ___block_descriptor_65_ea8_32s40bs48r_e15_v32?0816^B24lr48l8s32l8s40l8
+ ___block_descriptor_65_ea8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_66_ea8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_73_ea8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_literal_global.127
+ ___block_literal_global.209
+ ___block_literal_global.243
+ ___block_literal_global.506
+ ___block_literal_global.52
+ ___block_literal_global.56
+ ___block_literal_global.58
+ ___block_literal_global.597
+ ___block_literal_global.62
+ _objc_msgSend$appendDescriptionToStream:
+ _objc_msgSend$build:
+ _objc_msgSend$collectionLineBreakEachItemStyle
+ _objc_msgSend$collectionLineBreakNoneStyle
+ _objc_msgSend$debugStyle
+ _objc_msgSend$initWithDescriptionStyle:
+ _objc_msgSend$overlayStyle:block:
+ _objc_msgSend$replaceCharactersInRange:withString:
+ _objc_msgSend$setByAddingObjectsFromSet:
+ _objc_msgSend$setKeyValuePairSorting:
- +[BSAuditToken(Invalid) invalidToken]
- -[BSDescriptionStream appendSectionWithItemCount:openDelimiter:closeDelimiter:block:]
- -[_BSActionResponder _consumeLock_trySendResponse:alreadyOnResponseQueue:fireLegacyInvalidationHandler:]
- -[_BSActionResponder _lock_invalidate]
- -[_BSActionResponder _responseQueue_originator_receivedResponse:]
- _.str.101
- _OBJC_IVAR_$_BSDescriptionStream._groupVerbosityOptions
- _OBJC_IVAR_$_BSDescriptionStream._pendingFieldTerminator
- _OBJC_IVAR_$_BSDescriptionStream._sortKeys
- _OBJC_IVAR_$__BSActionResponder._lock_originator_responseQueue
- __OBJC_$_CLASS_METHODS_BSAuditToken(Invalid)
- __OBJC_$_INSTANCE_METHODS_BSAuditToken(Invalid)
- __OBJC_$_PROP_LIST_BSBlockSentinelSignalContext.61
- __OBJC_$_PROP_LIST_BSTimer.110
- ___104-[_BSActionResponder _consumeLock_trySendResponse:alreadyOnResponseQueue:fireLegacyInvalidationHandler:]_block_invoke
- ___59-[BSDescriptionStream appendDictionary:withName:itemBlock:]_block_invoke_2
- ___59-[BSDescriptionStream appendDictionary:withName:itemBlock:]_block_invoke_3
- ___59-[BSDescriptionStream appendDictionary:withName:itemBlock:]_block_invoke_4
- ____BSXPCDecodeObject_block_invoke.249
- ___block_descriptor_48_ea8_32s40bs_e15_v32?0816^B24ls32l8s40l8
- ___block_descriptor_57_ea8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.126
- ___block_literal_global.208
- ___block_literal_global.242
- ___block_literal_global.505
- ___block_literal_global.596
- _objc_msgSend$appendDictionary:withName:itemBlock:
- _objc_msgSend$sameLine:
CStrings:
+ "\x01\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xb1"
+ "& "
+ "+[BSDescriptionStyle new]"
+ "-[BSDescriptionStyle init]"
+ "<invalid:%X>"
+ "@\"BSDescriptionStyle\""
+ "@\"BSDescriptionStyle\"16@0:8"
+ "BSDescriptionStream.m"
+ "BSDescriptionStyle"
+ "BSDescriptionStyle cannot be subclassed"
+ "BSDescriptionStyle.m"
+ "BSMutableDescriptionStyle"
+ "T@\"NSSet\",C,D,N"
+ "T@\"NSSet\",R,C,N"
+ "T@\"NSString\",?,R,C"
+ "TB,N"
+ "Tq,D,N"
+ "Tq,R,N,V_nameTruncation"
+ "Tq,R,N,V_valueTruncation"
+ "_bodyItemSeparator"
+ "_clientInformation"
+ "_collectionLineBreak"
+ "_collectionTruncationStyle"
+ "_consumeLock_trySendResponse:alreadyLocked:alreadyOnResponseQueue:fireLegacyInvalidationHandler:"
+ "_debugging"
+ "_forceSuccinct"
+ "_keyValuePairSorting"
+ "_lineTruncation"
+ "_maximumItemCountForTruncation"
+ "_maximumLengthBeforeTruncation"
+ "_maximumNameLengthBeforeTruncation"
+ "_maximumValueLengthBeforeTruncation"
+ "_nameTruncation"
+ "_originator_responseQueue"
+ "_proemItemSeparator"
+ "_proemNestCount"
+ "_style"
+ "_truncationStartIndex"
+ "_valueTruncation"
+ "_verbosity"
+ "appendCustomFormatForValue:withCustomFormatForName:"
+ "appendCustomFormatWithNameFromObjectDescription:block:"
+ "appendDescriptionToStream:"
+ "atEnd"
+ "bodyItemSeparator"
+ "build:"
+ "byKey"
+ "cannot directly allocate BSDescriptionStyle"
+ "clientInformation"
+ "collectionLineBreak"
+ "collectionLineBreakEachItemStyle"
+ "collectionLineBreakNoneStyle"
+ "collectionTruncationStyle"
+ "colon"
+ "debugStyle"
+ "debugging"
+ "default"
+ "defaultCollectionLineBreakStyle"
+ "descriptionForRootObject:withStyle:"
+ "eachItem"
+ "equals"
+ "hasDebugStyle"
+ "hasSuccinctStyle"
+ "inherit"
+ "initWithDescriptionStyle:"
+ "keyValuePairSortedByKeyStyle"
+ "keyValuePairSorting"
+ "leading"
+ "maximumItemCountForTruncation"
+ "maximumNameLengthBeforeTruncation"
+ "maximumObjectStringLength"
+ "maximumValueLengthBeforeTruncation"
+ "middle"
+ "nameTruncation"
+ "nameTruncationStyle"
+ "never"
+ "objectTruncationStyle"
+ "off"
+ "on"
+ "overlayStyle:block:"
+ "proemItemSeparator"
+ "replaceCharactersInRange:withString:"
+ "rightArrow"
+ "setBodyItemSeparator:"
+ "setByAddingObjectsFromSet:"
+ "setClientInformation:"
+ "setCollectionLineBreak:"
+ "setCollectionTruncationStyle:"
+ "setDebugging:"
+ "setKeyValuePairSorting:"
+ "setMaximumItemCountForTruncation:"
+ "setMaximumNameLengthBeforeTruncation:"
+ "setMaximumValueLengthBeforeTruncation:"
+ "setNameTruncation:"
+ "setProemItemSeparator:"
+ "setValueTruncation:"
+ "setVerbosity:"
+ "style"
+ "styleByOverlayingStyle:"
+ "styleForEndTruncatingCollectionsOverItemCount:"
+ "succinct"
+ "succinctStyle"
+ "trailing"
+ "v16@?0@\"BSMutableDescriptionStyle\"8"
+ "v32@0:8@16@?<v@?@\"<BSDescriptionStringAppendTarget>\">24"
+ "v32@0:8@?16@?24"
+ "valueTruncation"
+ "verbosity"
+ "|"
+ "| "
+ "\xc1"
- "Invalid"
- "TB,N,V_sortKeys"
- "_consumeLock_trySendResponse:alreadyOnResponseQueue:fireLegacyInvalidationHandler:"
- "_groupVerbosityOptions"
- "_lock_originator_responseQueue"
- "_pendingFieldTerminator"
- "_responseQueue_originator_receivedResponse:"
- "_sortKeys"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa1\x11"

```
