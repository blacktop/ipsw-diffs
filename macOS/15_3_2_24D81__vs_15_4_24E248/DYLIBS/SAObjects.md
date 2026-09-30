## SAObjects

> `/System/Library/PrivateFrameworks/SAObjects.framework/Versions/A/SAObjects`

```diff

-3402.32.1.0.0
-  __TEXT.__text: 0x3ef34
+3404.35.1.0.0
+  __TEXT.__text: 0x3f050
   __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_methlist: 0x31730
-  __TEXT.__cstring: 0x15f8f
+  __TEXT.__objc_methlist: 0x31de0
   __TEXT.__const: 0x9d0
-  __TEXT.__unwind_info: 0x39b8
-  __TEXT.__objc_classname: 0x8aed
-  __TEXT.__objc_methname: 0x29c8c
+  __TEXT.__cstring: 0x160c7
+  __TEXT.__unwind_info: 0x39b0
+  __TEXT.__objc_classname: 0x8b39
+  __TEXT.__objc_methname: 0x29de6
   __TEXT.__objc_methtype: 0x49d
   __TEXT.__objc_stubs: 0xf00
-  __DATA_CONST.__got: 0x8a8
-  __DATA_CONST.__const: 0xf670
-  __DATA_CONST.__objc_classlist: 0x2da0
+  __DATA_CONST.__got: 0x8a0
+  __DATA_CONST.__const: 0xf740
+  __DATA_CONST.__objc_classlist: 0x2db8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xeff0
+  __DATA_CONST.__objc_selrefs: 0xf0f0
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x130
   __AUTH_CONST.__const: 0x310
-  __AUTH_CONST.__cfstring: 0x2dbe0
-  __AUTH_CONST.__objc_const: 0x58e58
+  __AUTH_CONST.__cfstring: 0x2de00
+  __AUTH_CONST.__objc_const: 0x58940
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x1590
+  __AUTH.__objc_data: 0x1680
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0xfc0
   __DATA.__bss: 0x50

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9AC3AE2B-1B15-3122-A6BA-45E4AA49F5F9
-  Functions: 14844
-  Symbols:   34455
-  CStrings:  21242
+  UUID: 0008C444-D859-3A36-AE0F-3B1CBA83CE9F
+  Functions: 14883
+  Symbols:   34539
+  CStrings:  21296
 
Symbols:
+ -[SAAppsLaunchApp personaAccessLevel]
+ -[SAAppsLaunchApp personaId]
+ -[SAAppsLaunchApp setPersonaAccessLevel:]
+ -[SAAppsLaunchApp setPersonaId:]
+ -[SACommandFailed customErrorCode]
+ -[SACommandFailed customErrorDomain]
+ -[SACommandFailed localizedDescription]
+ -[SACommandFailed setCustomErrorCode:]
+ -[SACommandFailed setCustomErrorDomain:]
+ -[SACommandFailed setLocalizedDescription:]
+ -[SACommandFailed setUserInfo:]
+ -[SACommandFailed userInfo]
+ -[SAExecuteOnRemoteRequest personaAccessLevel]
+ -[SAExecuteOnRemoteRequest setPersonaAccessLevel:]
+ -[SARDModelInferenceRequest encodedClassName]
+ -[SARDModelInferenceRequest groupIdentifier]
+ -[SARDModelInferenceRequest inferenceType]
+ -[SARDModelInferenceRequest protobufMessageRequest]
+ -[SARDModelInferenceRequest requiresResponse]
+ -[SARDModelInferenceRequest setInferenceType:]
+ -[SARDModelInferenceRequest setProtobufMessageRequest:]
+ -[SARDModelInferenceResponse encodedClassName]
+ -[SARDModelInferenceResponse groupIdentifier]
+ -[SARDModelInferenceResponse modelInferenceRequestId]
+ -[SARDModelInferenceResponse protobufMessageResponse]
+ -[SARDModelInferenceResponse requiresResponse]
+ -[SARDModelInferenceResponse setModelInferenceRequestId:]
+ -[SARDModelInferenceResponse setProtobufMessageResponse:]
+ -[SAUIAddViews personaAccessLevel]
+ -[SAUIAddViews setPersonaAccessLevel:]
+ -[SAUIPhotoPickerRequest directInvocationBundleIdentifier]
+ -[SAUIPhotoPickerRequest encodedClassName]
+ -[SAUIPhotoPickerRequest groupIdentifier]
+ -[SAUIPhotoPickerRequest requiresResponse]
+ -[SAUIPhotoPickerRequest searchQuery]
+ -[SAUIPhotoPickerRequest selectionLimit]
+ -[SAUIPhotoPickerRequest setDirectInvocationBundleIdentifier:]
+ -[SAUIPhotoPickerRequest setSearchQuery:]
+ -[SAUIPhotoPickerRequest setSelectionLimit:]
+ -[SAUISayIt personaAccessLevel]
+ -[SAUISayIt personaId]
+ -[SAUISayIt setPersonaAccessLevel:]
+ -[SAUISayIt setPersonaId:]
+ _OBJC_CLASS_$_SARDModelInferenceRequest
+ _OBJC_CLASS_$_SARDModelInferenceResponse
+ _OBJC_CLASS_$_SAUIPhotoPickerRequest
+ _OBJC_METACLASS_$_SARDModelInferenceRequest
+ _OBJC_METACLASS_$_SARDModelInferenceResponse
+ _OBJC_METACLASS_$_SAUIPhotoPickerRequest
+ _SAAppsLaunchAppPersonaAccessLevelPListKey
+ _SAAppsLaunchAppPersonaIdPListKey
+ _SACommandFailedCustomErrorCodePListKey
+ _SACommandFailedCustomErrorDomainPListKey
+ _SACommandFailedLocalizedDescriptionPListKey
+ _SACommandFailedUserInfoPListKey
+ _SAExecuteOnRemoteRequestPersonaAccessLevelPListKey
+ _SARDModelInferenceRequestClassIdentifier
+ _SARDModelInferenceRequestInferenceTypePListKey
+ _SARDModelInferenceRequestProtobufMessageRequestPListKey
+ _SARDModelInferenceRequestTypeNLV4_PLYMODELValue
+ _SARDModelInferenceResponseClassIdentifier
+ _SARDModelInferenceResponseModelInferenceRequestIdPListKey
+ _SARDModelInferenceResponseProtobufMessageResponsePListKey
+ _SAUIAddViewsPersonaAccessLevelPListKey
+ _SAUIAppPunchOutLaunchOptionsRemoveResponseUIValue
+ _SAUIAppPunchOutLaunchOptionsRetainSiriValue
+ _SAUIPersonaAccessLevelHighValue
+ _SAUIPersonaAccessLevelLowValue
+ _SAUIPhotoPickerRequestClassIdentifier
+ _SAUIPhotoPickerRequestDirectInvocationBundleIdentifierPListKey
+ _SAUIPhotoPickerRequestSearchQueryPListKey
+ _SAUIPhotoPickerRequestSelectionLimitPListKey
+ _SAUISayItPersonaAccessLevelPListKey
+ _SAUISayItPersonaIdPListKey
+ _SAUIShowRequestHandlingStatusExecutionInputSystemPLANNERValue
+ __OBJC_$_CLASS_PROP_LIST_SARDModelInferenceRequest
+ __OBJC_$_INSTANCE_METHODS_SARDModelInferenceRequest
+ __OBJC_$_INSTANCE_METHODS_SARDModelInferenceResponse
+ __OBJC_$_INSTANCE_METHODS_SAUIPhotoPickerRequest
+ __OBJC_$_PROP_LIST_SARDModelInferenceRequest
+ __OBJC_$_PROP_LIST_SARDModelInferenceResponse
+ __OBJC_$_PROP_LIST_SAUIPhotoPickerRequest
+ __OBJC_CLASS_PROTOCOLS_$_SARDModelInferenceRequest
+ __OBJC_CLASS_RO_$_SARDModelInferenceRequest
+ __OBJC_CLASS_RO_$_SARDModelInferenceResponse
+ __OBJC_CLASS_RO_$_SAUIPhotoPickerRequest
+ __OBJC_METACLASS_RO_$_SARDModelInferenceRequest
+ __OBJC_METACLASS_RO_$_SARDModelInferenceResponse
+ __OBJC_METACLASS_RO_$_SAUIPhotoPickerRequest
- +[SACommandFailed commandFailedWithDictionary:context:]
- +[SACommandFailed commandFailedWithErrorCode:]
- +[SACommandFailed commandFailedWithReason:]
- +[SACommandFailed commandFailed]
- __OBJC_$_CLASS_METHODS_SACommandFailed
CStrings:
+ "ModelInferenceRequest"
+ "ModelInferenceResponse"
+ "NLV4_PLYMODEL"
+ "PLANNER"
+ "PhotoPickerRequest"
+ "RemoveResponseUI"
+ "RetainSiri"
+ "SARDModelInferenceRequest"
+ "SARDModelInferenceResponse"
+ "SAUIPhotoPickerRequest"
+ "customErrorCode"
+ "customErrorDomain"
+ "directInvocationBundleIdentifier"
+ "inferenceType"
+ "modelInferenceRequestId"
+ "personaAccessLevel"
+ "protobufMessageRequest"
+ "protobufMessageResponse"
+ "searchQuery"
+ "selectionLimit"
+ "setCustomErrorCode:"
+ "setCustomErrorDomain:"
+ "setDirectInvocationBundleIdentifier:"
+ "setInferenceType:"
+ "setModelInferenceRequestId:"
+ "setPersonaAccessLevel:"
+ "setProtobufMessageRequest:"
+ "setProtobufMessageResponse:"
+ "setSearchQuery:"
+ "setSelectionLimit:"
- "commandFailedWithDictionary:context:"
- "commandFailedWithErrorCode:"
- "commandFailedWithReason:"

```
