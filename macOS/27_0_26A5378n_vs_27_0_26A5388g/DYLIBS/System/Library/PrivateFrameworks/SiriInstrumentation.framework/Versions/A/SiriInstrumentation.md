## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/Versions/A/SiriInstrumentation`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3600.79.1.0.0
-  __TEXT.__text: 0xdecb6c
-  __TEXT.__objc_methlist: 0x10789c
-  __TEXT.__const: 0x17654
-  __TEXT.__swift5_typeref: 0x1e9a
-  __TEXT.__cstring: 0x93c3b
-  __TEXT.__constg_swiftt: 0x7e14
+3600.80.1.0.0
+  __TEXT.__text: 0xdef7f4
+  __TEXT.__objc_methlist: 0x107c6c
+  __TEXT.__const: 0x17714
+  __TEXT.__swift5_typeref: 0x1ea6
+  __TEXT.__cstring: 0x94176
+  __TEXT.__constg_swiftt: 0x7e54
   __TEXT.__swift5_reflstr: 0x21d
   __TEXT.__swift5_fieldmd: 0x45c
-  __TEXT.__swift5_builtin: 0x4984
+  __TEXT.__swift5_builtin: 0x49ac
   __TEXT.__swift5_assocty: 0x150
-  __TEXT.__swift5_proto: 0x136c
-  __TEXT.__swift5_types: 0xf08
+  __TEXT.__swift5_proto: 0x1374
+  __TEXT.__swift5_types: 0xf10
   __TEXT.__oslogstring: 0xc1
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__unwind_info: 0x338c0
+  __TEXT.__unwind_info: 0x33978
   __TEXT.__eh_frame: 0x4838
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3d1a0
-  __DATA_CONST.__objc_classlist: 0x6718
+  __DATA_CONST.__const: 0x3d3d8
+  __DATA_CONST.__objc_classlist: 0x6730
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x41fa8
+  __DATA_CONST.__objc_selrefs: 0x420d0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x66c8
-  __DATA_CONST.__got: 0x6850
-  __AUTH_CONST.__const: 0x245d9
-  __AUTH_CONST.__cfstring: 0x7ee00
-  __AUTH_CONST.__objc_const: 0x179730
+  __DATA_CONST.__objc_superrefs: 0x66e0
+  __DATA_CONST.__got: 0x6868
+  __AUTH_CONST.__const: 0x24619
+  __AUTH_CONST.__cfstring: 0x7f220
+  __AUTH_CONST.__objc_const: 0x179c20
   __AUTH_CONST.__objc_intobj: 0xc48
   __AUTH_CONST.__auth_got: 0x7f8
-  __AUTH.__objc_data: 0x28f50
+  __AUTH.__objc_data: 0x29040
   __AUTH.__data: 0x160
-  __DATA.__objc_ivar: 0x128ec
-  __DATA.__data: 0x3430
-  __DATA.__bss: 0x1f380
+  __DATA.__objc_ivar: 0x12920
+  __DATA.__data: 0x3448
+  __DATA.__bss: 0x1f480
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x17a10
   __DATA_DIRTY.__data: 0x248

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 92897
-  Symbols:   144540
-  CStrings:  17350
+  Functions: 92982
+  Symbols:   144671
+  CStrings:  17383
 
Symbols:
+ +[ODSIGNALSiriSchemaODSIGNALClientEvent(InnerEventContainer) getInnerTypeStringByTag:]
+ -[ASRSchemaASRStarted deleteSpeechProfileSizeBucket]
+ -[ASRSchemaASRStarted hasSpeechProfileSizeBucket]
+ -[ASRSchemaASRStarted setHasSpeechProfileSizeBucket:]
+ -[ASRSchemaASRStarted setSpeechProfileSizeBucket:]
+ -[ASRSchemaASRStarted speechProfileSizeBucket]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource cascadeFieldType]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource deleteCascadeFieldType]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource deleteNumEnrolledEntities]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource dictionaryRepresentation]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource hasCascadeFieldType]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource hasNumEnrolledEntities]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource hash]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource initWithDictionary:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource initWithJSON:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource isEqual:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource jsonData]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource numEnrolledEntities]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource readFrom:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource setCascadeFieldType:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource setHasCascadeFieldType:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource setHasNumEnrolledEntities:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource setNumEnrolledEntities:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource writeTo:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileDonatedAppEntityMetric deleteNumCandidateInteractions]
+ -[ASRSpeechProfileSchemaASRSpeechProfileDonatedAppEntityMetric hasNumCandidateInteractions]
+ -[ASRSpeechProfileSchemaASRSpeechProfileDonatedAppEntityMetric numCandidateInteractions]
+ -[ASRSpeechProfileSchemaASRSpeechProfileDonatedAppEntityMetric setHasNumCandidateInteractions:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileDonatedAppEntityMetric setNumCandidateInteractions:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded addCascadeEntitySources:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded cascadeEntitySourcesAtIndex:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded cascadeEntitySourcesCount]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded cascadeEntitySources]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded clearCascadeEntitySources]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded deleteCascadeEntitySources]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded deleteSpeechProfileSize]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded hasSpeechProfileSize]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded setCascadeEntitySources:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded setHasSpeechProfileSize:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded setSpeechProfileSize:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded speechProfileSize]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted deleteSpeechProfileUpdateReason]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted hasSpeechProfileUpdateReason]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted setHasSpeechProfileUpdateReason:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted setSpeechProfileUpdateReason:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted speechProfileUpdateReason]
+ -[ODSIGNALSiriSchemaODSIGNALAppForegrounded deleteExists]
+ -[ODSIGNALSiriSchemaODSIGNALAppForegrounded dictionaryRepresentation]
+ -[ODSIGNALSiriSchemaODSIGNALAppForegrounded exists]
+ -[ODSIGNALSiriSchemaODSIGNALAppForegrounded hasExists]
+ -[ODSIGNALSiriSchemaODSIGNALAppForegrounded hash]
+ -[ODSIGNALSiriSchemaODSIGNALAppForegrounded initWithDictionary:]
+ -[ODSIGNALSiriSchemaODSIGNALAppForegrounded initWithJSON:]
+ -[ODSIGNALSiriSchemaODSIGNALAppForegrounded isEqual:]
+ -[ODSIGNALSiriSchemaODSIGNALAppForegrounded jsonData]
+ -[ODSIGNALSiriSchemaODSIGNALAppForegrounded readFrom:]
+ -[ODSIGNALSiriSchemaODSIGNALAppForegrounded setExists:]
+ -[ODSIGNALSiriSchemaODSIGNALAppForegrounded setHasExists:]
+ -[ODSIGNALSiriSchemaODSIGNALAppForegrounded writeTo:]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent .cxx_destruct]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent appForegrounded]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent deleteAppForegrounded]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent dictionaryRepresentation]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent hasAppForegrounded]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent hash]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent initWithDictionary:]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent initWithJSON:]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent isEqual:]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent jsonData]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent qualifiedMessageName]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent readFrom:]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent setAppForegrounded:]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent setHasAppForegrounded:]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent whichEvent_Type]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent writeTo:]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent(InnerEventContainer) innerEvent]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent(InnerEventContainer) whichInnerEventType]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent(InstrumentationAdditions) getAnyEventType]
+ -[ODSIGNALSiriSchemaODSIGNALClientEvent(IsolationLevel) clockIsolationLevel]
+ OBJC_IVAR_$_ASRSchemaASRStarted._speechProfileSizeBucket
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource._cascadeFieldType
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource._has
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource._numEnrolledEntities
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileDonatedAppEntityMetric._numCandidateInteractions
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded._cascadeEntitySources
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded._speechProfileSize
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted._speechProfileUpdateReason
+ OBJC_IVAR_$_ODSIGNALSiriSchemaODSIGNALAppForegrounded._exists
+ OBJC_IVAR_$_ODSIGNALSiriSchemaODSIGNALAppForegrounded._has
+ OBJC_IVAR_$_ODSIGNALSiriSchemaODSIGNALClientEvent._appForegrounded
+ OBJC_IVAR_$_ODSIGNALSiriSchemaODSIGNALClientEvent._hasAppForegrounded
+ OBJC_IVAR_$_ODSIGNALSiriSchemaODSIGNALClientEvent._whichEvent_Type
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource
+ _OBJC_CLASS_$_ODSIGNALSiriSchemaODSIGNALAppForegrounded
+ _OBJC_CLASS_$_ODSIGNALSiriSchemaODSIGNALClientEvent
+ _OBJC_METACLASS_$_ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource
+ _OBJC_METACLASS_$_ODSIGNALSiriSchemaODSIGNALAppForegrounded
+ _OBJC_METACLASS_$_ODSIGNALSiriSchemaODSIGNALClientEvent
+ __OBJC_$_CLASS_METHODS_ODSIGNALSiriSchemaODSIGNALClientEvent(InstrumentationAdditions|InnerEventContainer|IsolationLevel)
+ __OBJC_$_INSTANCE_METHODS_ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource
+ __OBJC_$_INSTANCE_METHODS_ODSIGNALSiriSchemaODSIGNALAppForegrounded
+ __OBJC_$_INSTANCE_METHODS_ODSIGNALSiriSchemaODSIGNALClientEvent(InstrumentationAdditions|InnerEventContainer|IsolationLevel)
+ __OBJC_$_INSTANCE_VARIABLES_ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource
+ __OBJC_$_INSTANCE_VARIABLES_ODSIGNALSiriSchemaODSIGNALAppForegrounded
+ __OBJC_$_INSTANCE_VARIABLES_ODSIGNALSiriSchemaODSIGNALClientEvent
+ __OBJC_$_PROP_LIST_ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource
+ __OBJC_$_PROP_LIST_ODSIGNALSiriSchemaODSIGNALAppForegrounded
+ __OBJC_CLASS_PROTOCOLS_$_ODSIGNALSiriSchemaODSIGNALClientEvent(InstrumentationAdditions|InnerEventContainer|IsolationLevel)
+ __OBJC_CLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource
+ __OBJC_CLASS_RO_$_ODSIGNALSiriSchemaODSIGNALAppForegrounded
+ __OBJC_CLASS_RO_$_ODSIGNALSiriSchemaODSIGNALClientEvent
+ __OBJC_METACLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource
+ __OBJC_METACLASS_RO_$_ODSIGNALSiriSchemaODSIGNALAppForegrounded
+ __OBJC_METACLASS_RO_$_ODSIGNALSiriSchemaODSIGNALClientEvent
+ _objc_msgSend$addCascadeEntitySources:
+ _objc_msgSend$appForegrounded
+ _objc_msgSend$cascadeEntitySources
+ _objc_msgSend$clearCascadeEntitySources
+ _objc_msgSend$numCandidateInteractions
+ _objc_msgSend$numEnrolledEntities
+ _objc_msgSend$setAppForegrounded:
+ _objc_msgSend$setNumCandidateInteractions:
+ _objc_msgSend$setNumEnrolledEntities:
+ _objc_msgSend$setSpeechProfileSize:
+ _objc_msgSend$setSpeechProfileSizeBucket:
+ _objc_msgSend$setSpeechProfileUpdateReason:
+ _objc_msgSend$speechProfileSize
+ _objc_msgSend$speechProfileSizeBucket
+ _objc_msgSend$speechProfileUpdateReason
+ _symbolic _____ So022ASRSpeechProfileSchemaaB12UpdateReasonV
+ _symbolic _____ So35ASRSchemaASRSpeechProfileSizeBucketV
CStrings:
+ "ASRSPEECHPROFILESIZEBUCKET_128_KB_TO_256_KB"
+ "ASRSPEECHPROFILESIZEBUCKET_1_MB_TO_2_MB"
+ "ASRSPEECHPROFILESIZEBUCKET_256_KB_TO_512_KB"
+ "ASRSPEECHPROFILESIZEBUCKET_2_MB_TO_4_MB"
+ "ASRSPEECHPROFILESIZEBUCKET_32_KB_TO_64_KB"
+ "ASRSPEECHPROFILESIZEBUCKET_4_MB_TO_8_MB"
+ "ASRSPEECHPROFILESIZEBUCKET_512_KB_TO_1_MB"
+ "ASRSPEECHPROFILESIZEBUCKET_64_KB_TO_128_KB"
+ "ASRSPEECHPROFILESIZEBUCKET_8_MB_TO_16_MB"
+ "ASRSPEECHPROFILESIZEBUCKET_ABOVE_16_MB"
+ "ASRSPEECHPROFILESIZEBUCKET_UNDER_32_KB"
+ "ASRSPEECHPROFILESIZEBUCKET_UNKNOWN"
+ "ASRSPEECHPROFILEUPDATEREASON_ASSISTANT_ASSET_UPDATE"
+ "ASRSPEECHPROFILEUPDATEREASON_CASCADE_DATASET_CHANGE"
+ "ASRSPEECHPROFILEUPDATEREASON_DAILY_MAINTENANCE"
+ "ASRSPEECHPROFILEUPDATEREASON_FIRST_UNLOCK"
+ "ASRSPEECHPROFILEUPDATEREASON_MOBILE_ASSET_STARTUP_ACTIVATION"
+ "ASRSPEECHPROFILEUPDATEREASON_POST_INSTALL_MIGRATION"
+ "ASRSPEECHPROFILEUPDATEREASON_SIRI_LANGUAGE_CHANGE"
+ "ASRSPEECHPROFILEUPDATEREASON_SIRI_PREFERENCES_CHANGE"
+ "ASRSPEECHPROFILEUPDATEREASON_SYSTEM_SUBSCRIPTIONS_CHANGE"
+ "ASRSPEECHPROFILEUPDATEREASON_TRIAL_EXPERIMENT_UPDATE"
+ "ASRSPEECHPROFILEUPDATEREASON_UNKNOWN"
+ "ODSIGNAL_CLIENT_EVENT"
+ "appForegrounded"
+ "cascadeEntitySources"
+ "com.apple.aiml.siri.odsignal.ODSIGNALClientEvent"
+ "com.apple.aiml.siri.odsignal.ODSIGNALClientEvent.ODSIGNALAppForegrounded"
+ "numCandidateInteractions"
+ "numEnrolledEntities"
+ "speechProfileSize"
+ "speechProfileSizeBucket"
+ "speechProfileUpdateReason"
```
