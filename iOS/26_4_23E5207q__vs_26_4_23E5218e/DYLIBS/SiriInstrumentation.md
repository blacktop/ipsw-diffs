## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`

```diff

-3520.65.1.1.1
-  __TEXT.__text: 0xaeb47c
+3520.67.1.0.0
+  __TEXT.__text: 0xaecc5c
   __TEXT.__auth_stubs: 0x10e0
-  __TEXT.__objc_methlist: 0xd8c04
-  __TEXT.__const: 0x130b4
+  __TEXT.__objc_methlist: 0xd8df4
+  __TEXT.__const: 0x130d4
   __TEXT.__swift5_typeref: 0x1a26
-  __TEXT.__cstring: 0x7dbc7
+  __TEXT.__cstring: 0x7dd50
   __TEXT.__constg_swiftt: 0x6920
   __TEXT.__swift5_reflstr: 0x212
   __TEXT.__swift5_fieldmd: 0x42c
   __TEXT.__swift5_builtin: 0x3cf0
   __TEXT.__swift5_assocty: 0x120
-  __TEXT.__swift5_proto: 0xfc4
+  __TEXT.__swift5_proto: 0xfc8
   __TEXT.__swift5_types: 0xc80
   __TEXT.__oslogstring: 0xc1
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__unwind_info: 0x2da98
+  __TEXT.__unwind_info: 0x2daf8
   __TEXT.__eh_frame: 0x3980
-  __TEXT.__objc_classname: 0x161f8
-  __TEXT.__objc_methname: 0x12d1c6
-  __TEXT.__objc_methtype: 0x29e1d
-  __TEXT.__objc_stubs: 0x6cf80
-  __DATA_CONST.__got: 0x4e18
-  __DATA_CONST.__const: 0x36fe8
-  __DATA_CONST.__objc_classlist: 0x4d20
+  __TEXT.__objc_classname: 0x1624d
+  __TEXT.__objc_methname: 0x12d476
+  __TEXT.__objc_methtype: 0x29e85
+  __TEXT.__objc_stubs: 0x6d080
+  __DATA_CONST.__got: 0x4e28
+  __DATA_CONST.__const: 0x371b0
+  __DATA_CONST.__objc_classlist: 0x4d30
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x386b0
+  __DATA_CONST.__objc_selrefs: 0x38728
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x7860
+  __DATA_CONST.__objc_superrefs: 0x7878
   __AUTH_CONST.__auth_got: 0x878
-  __AUTH_CONST.__const: 0x1cf70
-  __AUTH_CONST.__cfstring: 0x6d100
-  __AUTH_CONST.__objc_const: 0x124d30
+  __AUTH_CONST.__const: 0x1cf80
+  __AUTH_CONST.__cfstring: 0x6d220
+  __AUTH_CONST.__objc_const: 0x125010
   __AUTH_CONST.__objc_intobj: 0xb70
-  __AUTH.__objc_data: 0x11170
-  __DATA.__objc_ivar: 0xea30
+  __AUTH.__objc_data: 0x11210
+  __DATA.__objc_ivar: 0xea50
   __DATA.__data: 0x2950
   __DATA.__bss: 0x19e80
   __DATA.__common: 0x20

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A66442B6-747F-34D9-9189-DEDDA3300BF1
-  Functions: 79197
-  Symbols:   195170
-  CStrings:  80389
+  UUID: 8F9DCADC-3947-37D5-9022-DD7CA07BF574
+  Functions: 79242
+  Symbols:   195288
+  CStrings:  80439
 
Symbols:
+ -[SIRISETUPSchemaSIRISETUPClientEvent coreFollowUpPosted]
+ -[SIRISETUPSchemaSIRISETUPClientEvent deleteCoreFollowUpPosted]
+ -[SIRISETUPSchemaSIRISETUPClientEvent deleteOnboardingStarted]
+ -[SIRISETUPSchemaSIRISETUPClientEvent hasCoreFollowUpPosted]
+ -[SIRISETUPSchemaSIRISETUPClientEvent hasOnboardingStarted]
+ -[SIRISETUPSchemaSIRISETUPClientEvent onboardingStarted]
+ -[SIRISETUPSchemaSIRISETUPClientEvent setCoreFollowUpPosted:]
+ -[SIRISETUPSchemaSIRISETUPClientEvent setHasCoreFollowUpPosted:]
+ -[SIRISETUPSchemaSIRISETUPClientEvent setHasOnboardingStarted:]
+ -[SIRISETUPSchemaSIRISETUPClientEvent setOnboardingStarted:]
+ -[SIRISETUPSchemaSIRISETUPCoreFollowUpPosted .cxx_destruct]
+ -[SIRISETUPSchemaSIRISETUPCoreFollowUpPosted actionURL]
+ -[SIRISETUPSchemaSIRISETUPCoreFollowUpPosted deleteActionURL]
+ -[SIRISETUPSchemaSIRISETUPCoreFollowUpPosted dictionaryRepresentation]
+ -[SIRISETUPSchemaSIRISETUPCoreFollowUpPosted hasActionURL]
+ -[SIRISETUPSchemaSIRISETUPCoreFollowUpPosted hash]
+ -[SIRISETUPSchemaSIRISETUPCoreFollowUpPosted initWithDictionary:]
+ -[SIRISETUPSchemaSIRISETUPCoreFollowUpPosted initWithJSON:]
+ -[SIRISETUPSchemaSIRISETUPCoreFollowUpPosted isEqual:]
+ -[SIRISETUPSchemaSIRISETUPCoreFollowUpPosted jsonData]
+ -[SIRISETUPSchemaSIRISETUPCoreFollowUpPosted readFrom:]
+ -[SIRISETUPSchemaSIRISETUPCoreFollowUpPosted setActionURL:]
+ -[SIRISETUPSchemaSIRISETUPCoreFollowUpPosted setHasActionURL:]
+ -[SIRISETUPSchemaSIRISETUPCoreFollowUpPosted writeTo:]
+ -[SIRISETUPSchemaSIRISETUPCoreFollowUpPosted(SensitiveConditions) suppressMessageUnderConditions]
+ -[SIRISETUPSchemaSIRISETUPOnboardingStarted deleteMode]
+ -[SIRISETUPSchemaSIRISETUPOnboardingStarted dictionaryRepresentation]
+ -[SIRISETUPSchemaSIRISETUPOnboardingStarted hasMode]
+ -[SIRISETUPSchemaSIRISETUPOnboardingStarted hash]
+ -[SIRISETUPSchemaSIRISETUPOnboardingStarted initWithDictionary:]
+ -[SIRISETUPSchemaSIRISETUPOnboardingStarted initWithJSON:]
+ -[SIRISETUPSchemaSIRISETUPOnboardingStarted isEqual:]
+ -[SIRISETUPSchemaSIRISETUPOnboardingStarted jsonData]
+ -[SIRISETUPSchemaSIRISETUPOnboardingStarted mode]
+ -[SIRISETUPSchemaSIRISETUPOnboardingStarted readFrom:]
+ -[SIRISETUPSchemaSIRISETUPOnboardingStarted setHasMode:]
+ -[SIRISETUPSchemaSIRISETUPOnboardingStarted setMode:]
+ -[SIRISETUPSchemaSIRISETUPOnboardingStarted writeTo:]
+ -[SIRISETUPSchemaSIRISETUPOnboardingStarted(SensitiveConditions) suppressMessageUnderConditions]
+ -[STSchemaTopicalityAttributes(SensitiveConditions) applySensitiveConditionsPolicy:]
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPClientEvent._coreFollowUpPosted
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPClientEvent._onboardingStarted
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPCoreFollowUpPosted._actionURL
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPOnboardingStarted._has
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPOnboardingStarted._mode
+ _OBJC_CLASS_$_SIRISETUPSchemaSIRISETUPCoreFollowUpPosted
+ _OBJC_CLASS_$_SIRISETUPSchemaSIRISETUPOnboardingStarted
+ _OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPClientEvent._hasCoreFollowUpPosted
+ _OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPClientEvent._hasOnboardingStarted
+ _OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPCoreFollowUpPosted._hasActionURL
+ _OBJC_METACLASS_$_SIRISETUPSchemaSIRISETUPCoreFollowUpPosted
+ _OBJC_METACLASS_$_SIRISETUPSchemaSIRISETUPOnboardingStarted
+ _SIRISETUPSchemaSIRISETUPCoreFollowUpPostedReadFrom
+ _SIRISETUPSchemaSIRISETUPOnboardingStartedReadFrom
+ __OBJC_$_INSTANCE_METHODS_SIRISETUPSchemaSIRISETUPCoreFollowUpPosted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SIRISETUPSchemaSIRISETUPOnboardingStarted(SensitiveConditions)
+ __OBJC_$_INSTANCE_VARIABLES_SIRISETUPSchemaSIRISETUPCoreFollowUpPosted
+ __OBJC_$_INSTANCE_VARIABLES_SIRISETUPSchemaSIRISETUPOnboardingStarted
+ __OBJC_$_PROP_LIST_SIRISETUPSchemaSIRISETUPCoreFollowUpPosted
+ __OBJC_$_PROP_LIST_SIRISETUPSchemaSIRISETUPOnboardingStarted
+ __OBJC_CLASS_RO_$_SIRISETUPSchemaSIRISETUPCoreFollowUpPosted
+ __OBJC_CLASS_RO_$_SIRISETUPSchemaSIRISETUPOnboardingStarted
+ __OBJC_METACLASS_RO_$_SIRISETUPSchemaSIRISETUPCoreFollowUpPosted
+ __OBJC_METACLASS_RO_$_SIRISETUPSchemaSIRISETUPOnboardingStarted
+ _objc_msgSend$actionURL
+ _objc_msgSend$coreFollowUpPosted
+ _objc_msgSend$deleteCoreFollowUpPosted
+ _objc_msgSend$deleteOnboardingStarted
+ _objc_msgSend$onboardingStarted
+ _objc_msgSend$setActionURL:
+ _objc_msgSend$setCoreFollowUpPosted:
+ _objc_msgSend$setOnboardingStarted:
+ _qname_SIRISETUPSchemaSIRISETUPClientEvent_WhichEvent_Type_coreFollowUpPosted
+ _qname_SIRISETUPSchemaSIRISETUPClientEvent_WhichEvent_Type_onboardingStarted
CStrings:
+ "@\"SIRISETUPSchemaSIRISETUPCoreFollowUpPosted\""
+ "@\"SIRISETUPSchemaSIRISETUPOnboardingStarted\""
+ "SIRISETUPENROLLMENTUIMODE_VOICE_PROFILE_REPAIR"
+ "SIRISETUPSchemaSIRISETUPCoreFollowUpPosted"
+ "SIRISETUPSchemaSIRISETUPOnboardingStarted"
+ "SIRISETUPTRAININGMANAGERSTAGESTATUS_HIGH_WER"
+ "SIRISETUPTRAININGMANAGERSTAGESTATUS_LOW_SPEAKER_SIMILARITY"
+ "SIRISETUPTRAININGMANAGERSTAGESTATUS_TOO_NOISY"
+ "T@\"NSString\",C,N,V_actionURL"
+ "T@\"SIRISETUPSchemaSIRISETUPCoreFollowUpPosted\",&,N,V_coreFollowUpPosted"
+ "T@\"SIRISETUPSchemaSIRISETUPOnboardingStarted\",&,N,V_onboardingStarted"
+ "TB,N,V_hasActionURL"
+ "TB,N,V_hasCoreFollowUpPosted"
+ "TB,N,V_hasOnboardingStarted"
+ "_actionURL"
+ "_coreFollowUpPosted"
+ "_hasActionURL"
+ "_hasCoreFollowUpPosted"
+ "_hasOnboardingStarted"
+ "_onboardingStarted"
+ "actionURL"
+ "com.apple.aiml.siri.setup.SIRISETUPClientEvent.SIRISETUPCoreFollowUpPosted"
+ "com.apple.aiml.siri.setup.SIRISETUPClientEvent.SIRISETUPOnboardingStarted"
+ "coreFollowUpPosted"
+ "deleteActionURL"
+ "deleteCoreFollowUpPosted"
+ "deleteOnboardingStarted"
+ "hasActionURL"
+ "hasCoreFollowUpPosted"
+ "hasOnboardingStarted"
+ "onboardingStarted"
+ "setActionURL:"
+ "setCoreFollowUpPosted:"
+ "setHasActionURL:"
+ "setHasCoreFollowUpPosted:"
+ "setHasOnboardingStarted:"
+ "setOnboardingStarted:"
+ "{?=\"mode\"b1}"

```
