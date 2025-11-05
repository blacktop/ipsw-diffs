## MailKit

> `/System/Library/Frameworks/MailKit.framework/Versions/A/MailKit`

```diff

-3826.400.131.1.6
-  __TEXT.__text: 0x1ef70
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0x1c40
-  __TEXT.__gcc_except_tab: 0x3b88
-  __TEXT.__cstring: 0x15b9
+3826.500.181.1.5
+  __TEXT.__text: 0x1d1ac
+  __TEXT.__auth_stubs: 0x3b0
+  __TEXT.__objc_methlist: 0x1ef4
+  __TEXT.__gcc_except_tab: 0x37ec
+  __TEXT.__cstring: 0x1373
   __TEXT.__const: 0x70
   __TEXT.__oslogstring: 0xd3b
   __TEXT.__ustring: 0x3c6
-  __TEXT.__unwind_info: 0x1268
-  __TEXT.__objc_classname: 0x608
-  __TEXT.__objc_methname: 0x543a
-  __TEXT.__objc_methtype: 0xcc5
-  __TEXT.__objc_stubs: 0x3540
-  __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0x200
-  __DATA_CONST.__objc_classlist: 0x128
+  __TEXT.__unwind_info: 0x11f8
+  __TEXT.__objc_classname: 0x5be
+  __TEXT.__objc_methname: 0x4f87
+  __TEXT.__objc_methtype: 0xc5e
+  __TEXT.__objc_stubs: 0x3280
+  __DATA_CONST.__got: 0x3b0
+  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11b8
+  __DATA_CONST.__objc_selrefs: 0x1178
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x1e0
-  __AUTH_CONST.__const: 0xae0
-  __AUTH_CONST.__cfstring: 0x1620
-  __AUTH_CONST.__objc_const: 0x4830
+  __AUTH_CONST.__auth_got: 0x1e8
+  __AUTH_CONST.__const: 0xb10
+  __AUTH_CONST.__cfstring: 0x12a0
+  __AUTH_CONST.__objc_const: 0x3ce0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xb90
+  __AUTH.__objc_data: 0xaf0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x270
+  __DATA.__objc_ivar: 0x234
   __DATA.__data: 0x960
   __DATA.__bss: 0x168
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 451B1172-2411-3929-9B1C-E5336C253A2D
-  Functions: 705
-  Symbols:   2391
-  CStrings:  1507
+  UUID: D669F73E-3B6B-3136-92A0-E940D23B48EA
+  Functions: 695
+  Symbols:   2305
+  CStrings:  1392
 
Symbols:
+ +[MEAppExtensionsController _emailExtensionAttributeDictionary].cold.1
+ +[MEAppExtensionsController sharedInstance].cold.1
+ +[MEExtensionHostContext extensionHostRequestScheduler].cold.1
+ +[MEExtensionUserPreferences sharedInstance].cold.1
+ +[MEMessage _protectedHeaders].cold.1
+ +[MERemoteExtension allCapabilitiesRequiringMessageContentAccess].cold.1
+ +[MERemoteExtension allCapabilities].cold.1
+ +[NSXPCInterface(Extension) MEExtensionRemoteHostInterface].cold.1
+ +[NSXPCInterface(Extension) MERemoteExtensiontInterface].cold.1
+ -[MEExtensionRemoteViewController serviceViewControllerInterface].cold.1
+ -[MEExtensionServiceViewController exportedInterface].cold.1
+ -[MEExtensionUserPreferences _plistURL].cold.1
+ -[MERemoteExtension addSecurityExtensionErrorHandler:]
+ -[MERemoteExtension securityErrorHandler]
+ -[MERemoteExtension setSecurityErrorHandler:]
+ -[MESecureMessageCompositionHandler _securityImplementationForSender:completionHandler:isStatus:]
+ -[MESecureMessageCompositionHandler _wrappedErrorForError:extensionIdentifier:isErrorHandler:]
+ -[_EDEncodingDatum extensionErrorHandler]
+ -[_EDEncodingDatum setExtensionErrorHandler:]
+ GCC_except_table64
+ GCC_except_table69
+ GCC_except_table72
+ GCC_except_table78
+ GCC_except_table81
+ GCC_except_table91
+ MEMailExtensionsLog.cold.1
+ OBJC_IVAR_$_MERemoteExtension._securityErrorHandler
+ OBJC_IVAR_$__EDEncodingDatum._extensionErrorHandler
+ _ExtensionErrorDomain
+ _MEMailExtensionIsErrorHandlerKey
+ _NSLocalizedDescriptionKey
+ __86-[MESecureMessageCompositionHandler initWithSMIMEImplementation:extensionsController:]_block_invoke.39
+ __97-[MESecureMessageCompositionHandler _securityImplementationForSender:completionHandler:isStatus:]_block_invoke.47
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EFPubliclyDescribable
+ ___97-[MESecureMessageCompositionHandler _securityImplementationForSender:completionHandler:isStatus:]_block_invoke
+ ___block_descriptor_56_ea8_32s40r48r_e34_v32?0"MERemoteExtension"8Q16^B24l
+ ___block_descriptor_57_ea8_32s40bs48r_e5_v8?0l
+ ___copy_helper_block_ea8_32s40b48r
+ ___copy_helper_block_ea8_32s40r48r
+ ___destroy_helper_block_ea8_32s40r48r
+ ___destroy_helper_block_ea8_32s40s48r
+ _objc_msgSend$_securityImplementationForSender:completionHandler:isStatus:
+ _objc_msgSend$_wrappedErrorForError:extensionIdentifier:isErrorHandler:
+ _objc_msgSend$addSecurityExtensionErrorHandler:
+ _objc_msgSend$securityErrorHandler
+ _objc_msgSend$setSecurityErrorHandler:
+ _objc_setProperty_atomic_copy
+ initWKContentRuleListStore.cold.1
- +[MEMessageCategorizationResult supportsSecureCoding]
- +[MEMessageCategorizationResultMetadata supportsSecureCoding]
- -[MEMessageCategorizationResult .cxx_destruct]
- -[MEMessageCategorizationResult categoryType]
- -[MEMessageCategorizationResult encodeWithCoder:]
- -[MEMessageCategorizationResult initWithCategoryType:subCategoryType:metadata:]
- -[MEMessageCategorizationResult initWithCoder:]
- -[MEMessageCategorizationResult init]
- -[MEMessageCategorizationResult metadata]
- -[MEMessageCategorizationResult setCategoryType:]
- -[MEMessageCategorizationResult setMetadata:]
- -[MEMessageCategorizationResult setSubcategory:]
- -[MEMessageCategorizationResult subcategory]
- -[MEMessageCategorizationResultMetadata .cxx_destruct]
- -[MEMessageCategorizationResultMetadata _dictionaryRepresentation]
- -[MEMessageCategorizationResultMetadata encodeWithCoder:]
- -[MEMessageCategorizationResultMetadata experimentDeploymentID]
- -[MEMessageCategorizationResultMetadata experimentID]
- -[MEMessageCategorizationResultMetadata experimentTreatmentID]
- -[MEMessageCategorizationResultMetadata finalRuleVersion]
- -[MEMessageCategorizationResultMetadata hash]
- -[MEMessageCategorizationResultMetadata initWithCoder:]
- -[MEMessageCategorizationResultMetadata initWithScore:senderScore:tsScore:reasonCodes:modelVersion:senderModelVersion:tsModelVersion:finalRuleVersion:experimentID:experimentDeploymentID:experimentTreatmentID:rolloutID:rolloutDeploymentID:rolloutFactorPackID:]
- -[MEMessageCategorizationResultMetadata isEqual:]
- -[MEMessageCategorizationResultMetadata modelVersion]
- -[MEMessageCategorizationResultMetadata reasonCodes]
- -[MEMessageCategorizationResultMetadata rolloutDeploymentID]
- -[MEMessageCategorizationResultMetadata rolloutFactorPackID]
- -[MEMessageCategorizationResultMetadata rolloutID]
- -[MEMessageCategorizationResultMetadata score]
- -[MEMessageCategorizationResultMetadata senderModelVersion]
- -[MEMessageCategorizationResultMetadata senderScore]
- -[MEMessageCategorizationResultMetadata stringRepresentationWithError:]
- -[MEMessageCategorizationResultMetadata tsModelVersion]
- -[MEMessageCategorizationResultMetadata tsScore]
- -[MESecureMessageCompositionHandler _securityImplementationForSender:]
- -[MESecureMessageCompositionHandler _wrappedErrorForError:extensionIdentifier:]
- GCC_except_table62
- GCC_except_table67
- GCC_except_table70
- GCC_except_table73
- GCC_except_table80
- GCC_except_table82
- OBJC_IVAR_$_MEMessageCategorizationResult._categoryType
- OBJC_IVAR_$_MEMessageCategorizationResult._metadata
- OBJC_IVAR_$_MEMessageCategorizationResult._subcategory
- OBJC_IVAR_$_MEMessageCategorizationResultMetadata._experimentDeploymentID
- OBJC_IVAR_$_MEMessageCategorizationResultMetadata._experimentID
- OBJC_IVAR_$_MEMessageCategorizationResultMetadata._experimentTreatmentID
- OBJC_IVAR_$_MEMessageCategorizationResultMetadata._finalRuleVersion
- OBJC_IVAR_$_MEMessageCategorizationResultMetadata._modelVersion
- OBJC_IVAR_$_MEMessageCategorizationResultMetadata._reasonCodes
- OBJC_IVAR_$_MEMessageCategorizationResultMetadata._rolloutDeploymentID
- OBJC_IVAR_$_MEMessageCategorizationResultMetadata._rolloutFactorPackID
- OBJC_IVAR_$_MEMessageCategorizationResultMetadata._rolloutID
- OBJC_IVAR_$_MEMessageCategorizationResultMetadata._score
- OBJC_IVAR_$_MEMessageCategorizationResultMetadata._senderModelVersion
- OBJC_IVAR_$_MEMessageCategorizationResultMetadata._senderScore
- OBJC_IVAR_$_MEMessageCategorizationResultMetadata._tsModelVersion
- OBJC_IVAR_$_MEMessageCategorizationResultMetadata._tsScore
- _OBJC_CLASS_$_MEMessageCategorizationResult
- _OBJC_CLASS_$_MEMessageCategorizationResultMetadata
- _OBJC_CLASS_$_NSJSONSerialization
- _OBJC_METACLASS_$_MEMessageCategorizationResult
- _OBJC_METACLASS_$_MEMessageCategorizationResultMetadata
- _OUTLINED_FUNCTION_3
- __86-[MESecureMessageCompositionHandler initWithSMIMEImplementation:extensionsController:]_block_invoke.25
- __OBJC_$_CLASS_METHODS_MEMessageCategorizationResult
- __OBJC_$_CLASS_METHODS_MEMessageCategorizationResultMetadata
- __OBJC_$_CLASS_PROP_LIST_MEMessageCategorizationResult
- __OBJC_$_CLASS_PROP_LIST_MEMessageCategorizationResultMetadata
- __OBJC_$_INSTANCE_METHODS_MEMessageCategorizationResult
- __OBJC_$_INSTANCE_METHODS_MEMessageCategorizationResultMetadata
- __OBJC_$_INSTANCE_VARIABLES_MEMessageCategorizationResult
- __OBJC_$_INSTANCE_VARIABLES_MEMessageCategorizationResultMetadata
- __OBJC_$_PROP_LIST_MEMessageCategorizationResult
- __OBJC_$_PROP_LIST_MEMessageCategorizationResultMetadata
- __OBJC_CLASS_PROTOCOLS_$_MEMessageCategorizationResult
- __OBJC_CLASS_PROTOCOLS_$_MEMessageCategorizationResultMetadata
- __OBJC_CLASS_RO_$_MEMessageCategorizationResult
- __OBJC_CLASS_RO_$_MEMessageCategorizationResultMetadata
- __OBJC_METACLASS_RO_$_MEMessageCategorizationResult
- __OBJC_METACLASS_RO_$_MEMessageCategorizationResultMetadata
- ___70-[MESecureMessageCompositionHandler _securityImplementationForSender:]_block_invoke
- ___block_descriptor_48_ea8_32s40r_e34_v32?0"MERemoteExtension"8Q16^B24l
- _experimentDeploymentIDKeyName
- _experimentIDKeyName
- _experimentTreatmentIDKeyName
- _finalRuleVersionKeyName
- _modelScoreKeyName
- _modelVersionKeyName
- _objc_msgSend$_dictionaryRepresentation
- _objc_msgSend$_securityImplementationForSender:
- _objc_msgSend$_wrappedErrorForError:extensionIdentifier:
- _objc_msgSend$categoryType
- _objc_msgSend$dataWithJSONObject:options:error:
- _objc_msgSend$decodeDoubleForKey:
- _objc_msgSend$encodeDouble:forKey:
- _objc_msgSend$experimentDeploymentID
- _objc_msgSend$experimentID
- _objc_msgSend$experimentTreatmentID
- _objc_msgSend$finalRuleVersion
- _objc_msgSend$initWithCategoryType:subCategoryType:metadata:
- _objc_msgSend$initWithScore:senderScore:tsScore:reasonCodes:modelVersion:senderModelVersion:tsModelVersion:finalRuleVersion:experimentID:experimentDeploymentID:experimentTreatmentID:rolloutID:rolloutDeploymentID:rolloutFactorPackID:
- _objc_msgSend$isEqualToArray:
- _objc_msgSend$metadata
- _objc_msgSend$modelVersion
- _objc_msgSend$numberWithDouble:
- _objc_msgSend$reasonCodes
- _objc_msgSend$rolloutDeploymentID
- _objc_msgSend$rolloutFactorPackID
- _objc_msgSend$rolloutID
- _objc_msgSend$score
- _objc_msgSend$senderModelVersion
- _objc_msgSend$senderScore
- _objc_msgSend$subcategory
- _objc_msgSend$tsModelVersion
- _objc_msgSend$tsScore
- _reasonCodesKeyName
- _rolloutDeploymentIDKeyName
- _rolloutFactorPackIDKeyName
- _rolloutIDKeyName
- _senderModelScoreKeyName
- _senderModelVersionKeyName
- _tsModelScoreKeyName
- _tsModelVersionKeyName
CStrings:
+ "@36@0:8@16@?24B32"
+ "@?"
+ "@?16@0:8"
+ "An error occurred while trying to encrypt your message."
+ "ExtensionErrorDomain"
+ "MEMailExtensionIsErrorHandlerKey"
+ "T@\"NSString\",?,R,C,N"
+ "T@?,C,V_extensionErrorHandler"
+ "T@?,C,V_securityErrorHandler"
+ "_extensionErrorHandler"
+ "_securityErrorHandler"
+ "_securityImplementationForSender:completionHandler:isStatus:"
+ "_wrappedErrorForError:extensionIdentifier:isErrorHandler:"
+ "addSecurityExtensionErrorHandler:"
+ "ef_shortPublicDescription"
+ "extensionErrorHandler"
+ "securityErrorHandler"
+ "setExtensionErrorHandler:"
+ "setSecurityErrorHandler:"
- "!"
- ";"
- "@\"MEMessageCategorizationResultMetadata\""
- "@128@0:8d16d24d32@40@48@56@64@72@80@88@96@104@112@120"
- "@40@0:8Q16Q24@32"
- "EFPropertyKey_categoryType"
- "EFPropertyKey_experimentDeploymentID"
- "EFPropertyKey_experimentID"
- "EFPropertyKey_experimentTreatmentID"
- "EFPropertyKey_finalRuleVersion"
- "EFPropertyKey_metadata"
- "EFPropertyKey_modelVersion"
- "EFPropertyKey_reasonCodes"
- "EFPropertyKey_rolloutDeploymentID"
- "EFPropertyKey_rolloutFactorPackID"
- "EFPropertyKey_rolloutID"
- "EFPropertyKey_score"
- "EFPropertyKey_senderModelVersion"
- "EFPropertyKey_senderScore"
- "EFPropertyKey_subcategory"
- "EFPropertyKey_tsModelVersion"
- "EFPropertyKey_tsScore"
- "MEMessageCategorizationResult"
- "MEMessageCategorizationResultMetadata"
- "T@\"MEMessageCategorizationResultMetadata\",&,N,V_metadata"
- "T@\"NSArray\",R,N,V_reasonCodes"
- "T@\"NSString\",R,N,V_experimentDeploymentID"
- "T@\"NSString\",R,N,V_experimentID"
- "T@\"NSString\",R,N,V_experimentTreatmentID"
- "T@\"NSString\",R,N,V_finalRuleVersion"
- "T@\"NSString\",R,N,V_modelVersion"
- "T@\"NSString\",R,N,V_rolloutDeploymentID"
- "T@\"NSString\",R,N,V_rolloutFactorPackID"
- "T@\"NSString\",R,N,V_rolloutID"
- "T@\"NSString\",R,N,V_senderModelVersion"
- "T@\"NSString\",R,N,V_tsModelVersion"
- "TQ,N,V_categoryType"
- "TQ,N,V_subcategory"
- "Td,R,N,V_score"
- "Td,R,N,V_senderScore"
- "Td,R,N,V_tsScore"
- "_categoryType"
- "_dictionaryRepresentation"
- "_experimentDeploymentID"
- "_experimentID"
- "_experimentTreatmentID"
- "_finalRuleVersion"
- "_metadata"
- "_modelVersion"
- "_reasonCodes"
- "_rolloutDeploymentID"
- "_rolloutFactorPackID"
- "_rolloutID"
- "_score"
- "_securityImplementationForSender:"
- "_senderModelVersion"
- "_senderScore"
- "_subcategory"
- "_tsModelVersion"
- "_tsScore"
- "_wrappedErrorForError:extensionIdentifier:"
- "categoryType"
- "d"
- "d16@0:8"
- "dataWithJSONObject:options:error:"
- "decodeDoubleForKey:"
- "encodeDouble:forKey:"
- "experimentDeploymentID"
- "experimentID"
- "experimentTreatmentID"
- "finalRuleVersion"
- "initWithCategoryType:subCategoryType:metadata:"
- "initWithScore:senderScore:tsScore:reasonCodes:modelVersion:senderModelVersion:tsModelVersion:finalRuleVersion:experimentID:experimentDeploymentID:experimentTreatmentID:rolloutID:rolloutDeploymentID:rolloutFactorPackID:"
- "isEqualToArray:"
- "metadata"
- "modelVersion"
- "numberWithDouble:"
- "reasonCodes"
- "rolloutDeploymentID"
- "rolloutFactorPackID"
- "rolloutID"
- "score"
- "senderModelVersion"
- "senderScore"
- "setCategoryType:"
- "setMetadata:"
- "setSubcategory:"
- "stringRepresentationWithError:"
- "subcategory"
- "tsModelVersion"
- "tsScore"
- "v24@0:8Q16"

```
