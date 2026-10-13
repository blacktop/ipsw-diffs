## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`

```diff

 3605.33.1.0.0
-  __TEXT.__text: 0xda87e4
-  __TEXT.__objc_methlist: 0x10ff94
-  __TEXT.__const: 0x18c04
-  __TEXT.__swift5_typeref: 0x1ff2
-  __TEXT.__cstring: 0x98e16
-  __TEXT.__constg_swiftt: 0x8458
+  __TEXT.__text: 0xdbe6b4
+  __TEXT.__objc_methlist: 0x111c94
+  __TEXT.__const: 0x18fc4
+  __TEXT.__swift5_typeref: 0x2012
+  __TEXT.__cstring: 0x99424
+  __TEXT.__constg_swiftt: 0x84b8
   __TEXT.__swift5_reflstr: 0x22d
   __TEXT.__swift5_fieldmd: 0x488
-  __TEXT.__swift5_builtin: 0x4d30
+  __TEXT.__swift5_builtin: 0x4d6c
   __TEXT.__swift5_assocty: 0x150
-  __TEXT.__swift5_proto: 0x159c
-  __TEXT.__swift5_types: 0xfc8
+  __TEXT.__swift5_proto: 0x15b8
+  __TEXT.__swift5_types: 0xfd4
   __TEXT.__oslogstring: 0x111
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_capture: 0x14
-  __TEXT.__unwind_info: 0x37ea8
+  __TEXT.__unwind_info: 0x384f8
   __TEXT.__eh_frame: 0x4cf0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3ff70
-  __DATA_CONST.__objc_classlist: 0x6a50
+  __DATA_CONST.__const: 0x400f8
+  __DATA_CONST.__objc_classlist: 0x6b28
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x44488
+  __DATA_CONST.__objc_selrefs: 0x44650
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x6a00
-  __DATA_CONST.__got: 0x6ba8
-  __AUTH_CONST.__const: 0x27338
-  __AUTH_CONST.__cfstring: 0x83500
-  __AUTH_CONST.__objc_const: 0x184bf0
-  __AUTH_CONST.__objc_intobj: 0xd20
+  __DATA_CONST.__objc_superrefs: 0x6ad8
+  __DATA_CONST.__got: 0x6c80
+  __AUTH_CONST.__const: 0x271f0
+  __AUTH_CONST.__cfstring: 0x83aa0
+  __AUTH_CONST.__objc_const: 0x1877b0
+  __AUTH_CONST.__objc_intobj: 0xd38
   __AUTH_CONST.__auth_got: 0x9c8
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x13170
-  __DATA.__data: 0x3540
+  __DATA.__objc_ivar: 0x1337c
+  __DATA.__data: 0x3570
   __DATA.__common: 0x38
-  __DATA_DIRTY.__objc_data: 0x42850
+  __DATA_DIRTY.__objc_data: 0x430c0
   __DATA_DIRTY.__data: 0x518
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 96268
-  Symbols:   134787
-  CStrings:  17962
+  Functions: 96883
+  Symbols:   135706
+  CStrings:  18007
 
Symbols:
+ +[RISchemaRIClientEvent(Component) joinability]
+ +[RISchemaRIClientEvent(InnerEventContainer) getInnerTypeStringByTag:]
+ +[RISessionSchemaRISessionClientEvent(Component) joinability]
+ +[RISessionSchemaRISessionClientEvent(InnerEventContainer) getInnerTypeStringByTag:]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived .cxx_destruct]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived addIdentityAggressors:]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived clearIdentityAggressors]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived deleteIdentityAggressors]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived deleteIsRecentlySeen]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived hasIsRecentlySeen]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived identityAggressorsAtIndex:]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived identityAggressorsCount]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived identityAggressors]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived isRecentlySeen]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived setHasIsRecentlySeen:]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived setIdentityAggressors:]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived setIsRecentlySeen:]
+ -[PLANNERSchemaPLANNERUserIdentityChecked deleteIsRecentlySeen]
+ -[PLANNERSchemaPLANNERUserIdentityChecked hasIsRecentlySeen]
+ -[PLANNERSchemaPLANNERUserIdentityChecked isRecentlySeen]
+ -[PLANNERSchemaPLANNERUserIdentityChecked setHasIsRecentlySeen:]
+ -[PLANNERSchemaPLANNERUserIdentityChecked setIsRecentlySeen:]
+ -[RISchemaRIClientEvent .cxx_destruct]
+ -[RISchemaRIClientEvent deleteEventMetadata]
+ -[RISchemaRIClientEvent deleteRemoteContext]
+ -[RISchemaRIClientEvent deleteSourceContext]
+ -[RISchemaRIClientEvent dictionaryRepresentation]
+ -[RISchemaRIClientEvent eventMetadata]
+ -[RISchemaRIClientEvent hasEventMetadata]
+ -[RISchemaRIClientEvent hasRemoteContext]
+ -[RISchemaRIClientEvent hasSourceContext]
+ -[RISchemaRIClientEvent hash]
+ -[RISchemaRIClientEvent initWithDictionary:]
+ -[RISchemaRIClientEvent initWithJSON:]
+ -[RISchemaRIClientEvent isEqual:]
+ -[RISchemaRIClientEvent jsonData]
+ -[RISchemaRIClientEvent qualifiedMessageName]
+ -[RISchemaRIClientEvent readFrom:]
+ -[RISchemaRIClientEvent remoteContext]
+ -[RISchemaRIClientEvent setEventMetadata:]
+ -[RISchemaRIClientEvent setHasEventMetadata:]
+ -[RISchemaRIClientEvent setHasRemoteContext:]
+ -[RISchemaRIClientEvent setHasSourceContext:]
+ -[RISchemaRIClientEvent setRemoteContext:]
+ -[RISchemaRIClientEvent setSourceContext:]
+ -[RISchemaRIClientEvent sourceContext]
+ -[RISchemaRIClientEvent whichEvent_Type]
+ -[RISchemaRIClientEvent writeTo:]
+ -[RISchemaRIClientEvent(Component) componentName]
+ -[RISchemaRIClientEvent(Component) getComponentId]
+ -[RISchemaRIClientEvent(InnerEventContainer) innerEvent]
+ -[RISchemaRIClientEvent(InnerEventContainer) whichInnerEventType]
+ -[RISchemaRIClientEvent(InstrumentationAdditions) getAnyEventType]
+ -[RISchemaRIClientEventMetadata .cxx_destruct]
+ -[RISchemaRIClientEventMetadata deleteRiId]
+ -[RISchemaRIClientEventMetadata dictionaryRepresentation]
+ -[RISchemaRIClientEventMetadata hasRiId]
+ -[RISchemaRIClientEventMetadata hash]
+ -[RISchemaRIClientEventMetadata initWithDictionary:]
+ -[RISchemaRIClientEventMetadata initWithJSON:]
+ -[RISchemaRIClientEventMetadata isEqual:]
+ -[RISchemaRIClientEventMetadata jsonData]
+ -[RISchemaRIClientEventMetadata readFrom:]
+ -[RISchemaRIClientEventMetadata riId]
+ -[RISchemaRIClientEventMetadata setHasRiId:]
+ -[RISchemaRIClientEventMetadata setRiId:]
+ -[RISchemaRIClientEventMetadata writeTo:]
+ -[RISchemaRIError .cxx_destruct]
+ -[RISchemaRIError deleteErrorCode]
+ -[RISchemaRIError deleteErrorDomain]
+ -[RISchemaRIError dictionaryRepresentation]
+ -[RISchemaRIError errorCode]
+ -[RISchemaRIError errorDomain]
+ -[RISchemaRIError hasErrorCode]
+ -[RISchemaRIError hasErrorDomain]
+ -[RISchemaRIError hash]
+ -[RISchemaRIError initWithDictionary:]
+ -[RISchemaRIError initWithJSON:]
+ -[RISchemaRIError isEqual:]
+ -[RISchemaRIError jsonData]
+ -[RISchemaRIError readFrom:]
+ -[RISchemaRIError setErrorCode:]
+ -[RISchemaRIError setErrorDomain:]
+ -[RISchemaRIError setHasErrorCode:]
+ -[RISchemaRIError setHasErrorDomain:]
+ -[RISchemaRIError writeTo:]
+ -[RISchemaRIRemoteContext .cxx_destruct]
+ -[RISchemaRIRemoteContext deleteEnded]
+ -[RISchemaRIRemoteContext deleteFailed]
+ -[RISchemaRIRemoteContext deleteStartedOrChanged]
+ -[RISchemaRIRemoteContext dictionaryRepresentation]
+ -[RISchemaRIRemoteContext ended]
+ -[RISchemaRIRemoteContext failed]
+ -[RISchemaRIRemoteContext hasEnded]
+ -[RISchemaRIRemoteContext hasFailed]
+ -[RISchemaRIRemoteContext hasStartedOrChanged]
+ -[RISchemaRIRemoteContext hash]
+ -[RISchemaRIRemoteContext initWithDictionary:]
+ -[RISchemaRIRemoteContext initWithJSON:]
+ -[RISchemaRIRemoteContext isEqual:]
+ -[RISchemaRIRemoteContext jsonData]
+ -[RISchemaRIRemoteContext readFrom:]
+ -[RISchemaRIRemoteContext setEnded:]
+ -[RISchemaRIRemoteContext setFailed:]
+ -[RISchemaRIRemoteContext setHasEnded:]
+ -[RISchemaRIRemoteContext setHasFailed:]
+ -[RISchemaRIRemoteContext setHasStartedOrChanged:]
+ -[RISchemaRIRemoteContext setStartedOrChanged:]
+ -[RISchemaRIRemoteContext startedOrChanged]
+ -[RISchemaRIRemoteContext whichContextevent]
+ -[RISchemaRIRemoteContext writeTo:]
+ -[RISchemaRIRemoteEnded deleteExists]
+ -[RISchemaRIRemoteEnded dictionaryRepresentation]
+ -[RISchemaRIRemoteEnded exists]
+ -[RISchemaRIRemoteEnded hasExists]
+ -[RISchemaRIRemoteEnded hash]
+ -[RISchemaRIRemoteEnded initWithDictionary:]
+ -[RISchemaRIRemoteEnded initWithJSON:]
+ -[RISchemaRIRemoteEnded isEqual:]
+ -[RISchemaRIRemoteEnded jsonData]
+ -[RISchemaRIRemoteEnded readFrom:]
+ -[RISchemaRIRemoteEnded setExists:]
+ -[RISchemaRIRemoteEnded setHasExists:]
+ -[RISchemaRIRemoteEnded writeTo:]
+ -[RISchemaRIRemoteFailed .cxx_destruct]
+ -[RISchemaRIRemoteFailed deleteError]
+ -[RISchemaRIRemoteFailed deleteExists]
+ -[RISchemaRIRemoteFailed deleteUnderUnderlyingError]
+ -[RISchemaRIRemoteFailed deleteUnderlyingError]
+ -[RISchemaRIRemoteFailed dictionaryRepresentation]
+ -[RISchemaRIRemoteFailed error]
+ -[RISchemaRIRemoteFailed exists]
+ -[RISchemaRIRemoteFailed hasError]
+ -[RISchemaRIRemoteFailed hasExists]
+ -[RISchemaRIRemoteFailed hasUnderUnderlyingError]
+ -[RISchemaRIRemoteFailed hasUnderlyingError]
+ -[RISchemaRIRemoteFailed hash]
+ -[RISchemaRIRemoteFailed initWithDictionary:]
+ -[RISchemaRIRemoteFailed initWithJSON:]
+ -[RISchemaRIRemoteFailed isEqual:]
+ -[RISchemaRIRemoteFailed jsonData]
+ -[RISchemaRIRemoteFailed readFrom:]
+ -[RISchemaRIRemoteFailed setError:]
+ -[RISchemaRIRemoteFailed setExists:]
+ -[RISchemaRIRemoteFailed setHasError:]
+ -[RISchemaRIRemoteFailed setHasExists:]
+ -[RISchemaRIRemoteFailed setHasUnderUnderlyingError:]
+ -[RISchemaRIRemoteFailed setHasUnderlyingError:]
+ -[RISchemaRIRemoteFailed setUnderUnderlyingError:]
+ -[RISchemaRIRemoteFailed setUnderlyingError:]
+ -[RISchemaRIRemoteFailed underUnderlyingError]
+ -[RISchemaRIRemoteFailed underlyingError]
+ -[RISchemaRIRemoteFailed writeTo:]
+ -[RISchemaRIRemoteStarted .cxx_destruct]
+ -[RISchemaRIRemoteStarted deleteIsColdLaunch]
+ -[RISchemaRIRemoteStarted deleteRiSessionId]
+ -[RISchemaRIRemoteStarted dictionaryRepresentation]
+ -[RISchemaRIRemoteStarted hasIsColdLaunch]
+ -[RISchemaRIRemoteStarted hasRiSessionId]
+ -[RISchemaRIRemoteStarted hash]
+ -[RISchemaRIRemoteStarted initWithDictionary:]
+ -[RISchemaRIRemoteStarted initWithJSON:]
+ -[RISchemaRIRemoteStarted isColdLaunch]
+ -[RISchemaRIRemoteStarted isEqual:]
+ -[RISchemaRIRemoteStarted jsonData]
+ -[RISchemaRIRemoteStarted readFrom:]
+ -[RISchemaRIRemoteStarted riSessionId]
+ -[RISchemaRIRemoteStarted setHasIsColdLaunch:]
+ -[RISchemaRIRemoteStarted setHasRiSessionId:]
+ -[RISchemaRIRemoteStarted setIsColdLaunch:]
+ -[RISchemaRIRemoteStarted setRiSessionId:]
+ -[RISchemaRIRemoteStarted writeTo:]
+ -[RISchemaRISourceContext .cxx_destruct]
+ -[RISchemaRISourceContext deleteEnded]
+ -[RISchemaRISourceContext deleteFailed]
+ -[RISchemaRISourceContext deleteStartedOrChanged]
+ -[RISchemaRISourceContext dictionaryRepresentation]
+ -[RISchemaRISourceContext ended]
+ -[RISchemaRISourceContext failed]
+ -[RISchemaRISourceContext hasEnded]
+ -[RISchemaRISourceContext hasFailed]
+ -[RISchemaRISourceContext hasStartedOrChanged]
+ -[RISchemaRISourceContext hash]
+ -[RISchemaRISourceContext initWithDictionary:]
+ -[RISchemaRISourceContext initWithJSON:]
+ -[RISchemaRISourceContext isEqual:]
+ -[RISchemaRISourceContext jsonData]
+ -[RISchemaRISourceContext readFrom:]
+ -[RISchemaRISourceContext setEnded:]
+ -[RISchemaRISourceContext setFailed:]
+ -[RISchemaRISourceContext setHasEnded:]
+ -[RISchemaRISourceContext setHasFailed:]
+ -[RISchemaRISourceContext setHasStartedOrChanged:]
+ -[RISchemaRISourceContext setStartedOrChanged:]
+ -[RISchemaRISourceContext startedOrChanged]
+ -[RISchemaRISourceContext whichContextevent]
+ -[RISchemaRISourceContext writeTo:]
+ -[RISchemaRISourceEnded deleteExists]
+ -[RISchemaRISourceEnded deleteRemoteTimeInMs]
+ -[RISchemaRISourceEnded deleteRoundTripCount]
+ -[RISchemaRISourceEnded deleteSizeInBytes]
+ -[RISchemaRISourceEnded dictionaryRepresentation]
+ -[RISchemaRISourceEnded exists]
+ -[RISchemaRISourceEnded hasExists]
+ -[RISchemaRISourceEnded hasRemoteTimeInMs]
+ -[RISchemaRISourceEnded hasRoundTripCount]
+ -[RISchemaRISourceEnded hasSizeInBytes]
+ -[RISchemaRISourceEnded hash]
+ -[RISchemaRISourceEnded initWithDictionary:]
+ -[RISchemaRISourceEnded initWithJSON:]
+ -[RISchemaRISourceEnded isEqual:]
+ -[RISchemaRISourceEnded jsonData]
+ -[RISchemaRISourceEnded readFrom:]
+ -[RISchemaRISourceEnded remoteTimeInMs]
+ -[RISchemaRISourceEnded roundTripCount]
+ -[RISchemaRISourceEnded setExists:]
+ -[RISchemaRISourceEnded setHasExists:]
+ -[RISchemaRISourceEnded setHasRemoteTimeInMs:]
+ -[RISchemaRISourceEnded setHasRoundTripCount:]
+ -[RISchemaRISourceEnded setHasSizeInBytes:]
+ -[RISchemaRISourceEnded setRemoteTimeInMs:]
+ -[RISchemaRISourceEnded setRoundTripCount:]
+ -[RISchemaRISourceEnded setSizeInBytes:]
+ -[RISchemaRISourceEnded sizeInBytes]
+ -[RISchemaRISourceEnded writeTo:]
+ -[RISchemaRISourceFailed .cxx_destruct]
+ -[RISchemaRISourceFailed deleteError]
+ -[RISchemaRISourceFailed deleteExists]
+ -[RISchemaRISourceFailed deleteUnderUnderlyingError]
+ -[RISchemaRISourceFailed deleteUnderlyingError]
+ -[RISchemaRISourceFailed dictionaryRepresentation]
+ -[RISchemaRISourceFailed error]
+ -[RISchemaRISourceFailed exists]
+ -[RISchemaRISourceFailed hasError]
+ -[RISchemaRISourceFailed hasExists]
+ -[RISchemaRISourceFailed hasUnderUnderlyingError]
+ -[RISchemaRISourceFailed hasUnderlyingError]
+ -[RISchemaRISourceFailed hash]
+ -[RISchemaRISourceFailed initWithDictionary:]
+ -[RISchemaRISourceFailed initWithJSON:]
+ -[RISchemaRISourceFailed isEqual:]
+ -[RISchemaRISourceFailed jsonData]
+ -[RISchemaRISourceFailed readFrom:]
+ -[RISchemaRISourceFailed setError:]
+ -[RISchemaRISourceFailed setExists:]
+ -[RISchemaRISourceFailed setHasError:]
+ -[RISchemaRISourceFailed setHasExists:]
+ -[RISchemaRISourceFailed setHasUnderUnderlyingError:]
+ -[RISchemaRISourceFailed setHasUnderlyingError:]
+ -[RISchemaRISourceFailed setUnderUnderlyingError:]
+ -[RISchemaRISourceFailed setUnderlyingError:]
+ -[RISchemaRISourceFailed underUnderlyingError]
+ -[RISchemaRISourceFailed underlyingError]
+ -[RISchemaRISourceFailed writeTo:]
+ -[RISchemaRISourceStarted .cxx_destruct]
+ -[RISchemaRISourceStarted communicationType]
+ -[RISchemaRISourceStarted deleteCommunicationType]
+ -[RISchemaRISourceStarted deleteRiSessionId]
+ -[RISchemaRISourceStarted dictionaryRepresentation]
+ -[RISchemaRISourceStarted hasCommunicationType]
+ -[RISchemaRISourceStarted hasRiSessionId]
+ -[RISchemaRISourceStarted hash]
+ -[RISchemaRISourceStarted initWithDictionary:]
+ -[RISchemaRISourceStarted initWithJSON:]
+ -[RISchemaRISourceStarted isEqual:]
+ -[RISchemaRISourceStarted jsonData]
+ -[RISchemaRISourceStarted readFrom:]
+ -[RISchemaRISourceStarted riSessionId]
+ -[RISchemaRISourceStarted setCommunicationType:]
+ -[RISchemaRISourceStarted setHasCommunicationType:]
+ -[RISchemaRISourceStarted setHasRiSessionId:]
+ -[RISchemaRISourceStarted setRiSessionId:]
+ -[RISchemaRISourceStarted writeTo:]
+ -[RISessionSchemaRISessionClientEvent .cxx_destruct]
+ -[RISessionSchemaRISessionClientEvent deleteEventMetadata]
+ -[RISessionSchemaRISessionClientEvent deleteRemoteSessionContext]
+ -[RISessionSchemaRISessionClientEvent deleteSourceSessionContext]
+ -[RISessionSchemaRISessionClientEvent dictionaryRepresentation]
+ -[RISessionSchemaRISessionClientEvent eventMetadata]
+ -[RISessionSchemaRISessionClientEvent hasEventMetadata]
+ -[RISessionSchemaRISessionClientEvent hasRemoteSessionContext]
+ -[RISessionSchemaRISessionClientEvent hasSourceSessionContext]
+ -[RISessionSchemaRISessionClientEvent hash]
+ -[RISessionSchemaRISessionClientEvent initWithDictionary:]
+ -[RISessionSchemaRISessionClientEvent initWithJSON:]
+ -[RISessionSchemaRISessionClientEvent isEqual:]
+ -[RISessionSchemaRISessionClientEvent jsonData]
+ -[RISessionSchemaRISessionClientEvent qualifiedMessageName]
+ -[RISessionSchemaRISessionClientEvent readFrom:]
+ -[RISessionSchemaRISessionClientEvent remoteSessionContext]
+ -[RISessionSchemaRISessionClientEvent setEventMetadata:]
+ -[RISessionSchemaRISessionClientEvent setHasEventMetadata:]
+ -[RISessionSchemaRISessionClientEvent setHasRemoteSessionContext:]
+ -[RISessionSchemaRISessionClientEvent setHasSourceSessionContext:]
+ -[RISessionSchemaRISessionClientEvent setRemoteSessionContext:]
+ -[RISessionSchemaRISessionClientEvent setSourceSessionContext:]
+ -[RISessionSchemaRISessionClientEvent sourceSessionContext]
+ -[RISessionSchemaRISessionClientEvent whichEvent_Type]
+ -[RISessionSchemaRISessionClientEvent writeTo:]
+ -[RISessionSchemaRISessionClientEvent(Component) componentName]
+ -[RISessionSchemaRISessionClientEvent(Component) getComponentId]
+ -[RISessionSchemaRISessionClientEvent(InnerEventContainer) innerEvent]
+ -[RISessionSchemaRISessionClientEvent(InnerEventContainer) whichInnerEventType]
+ -[RISessionSchemaRISessionClientEvent(InstrumentationAdditions) getAnyEventType]
+ -[RISessionSchemaRISessionClientEventMetadata .cxx_destruct]
+ -[RISessionSchemaRISessionClientEventMetadata deleteRiSessionId]
+ -[RISessionSchemaRISessionClientEventMetadata dictionaryRepresentation]
+ -[RISessionSchemaRISessionClientEventMetadata hasRiSessionId]
+ -[RISessionSchemaRISessionClientEventMetadata hash]
+ -[RISessionSchemaRISessionClientEventMetadata initWithDictionary:]
+ -[RISessionSchemaRISessionClientEventMetadata initWithJSON:]
+ -[RISessionSchemaRISessionClientEventMetadata isEqual:]
+ -[RISessionSchemaRISessionClientEventMetadata jsonData]
+ -[RISessionSchemaRISessionClientEventMetadata readFrom:]
+ -[RISessionSchemaRISessionClientEventMetadata riSessionId]
+ -[RISessionSchemaRISessionClientEventMetadata setHasRiSessionId:]
+ -[RISessionSchemaRISessionClientEventMetadata setRiSessionId:]
+ -[RISessionSchemaRISessionClientEventMetadata writeTo:]
+ -[RISessionSchemaRISessionError .cxx_destruct]
+ -[RISessionSchemaRISessionError deleteErrorCode]
+ -[RISessionSchemaRISessionError deleteErrorDomain]
+ -[RISessionSchemaRISessionError dictionaryRepresentation]
+ -[RISessionSchemaRISessionError errorCode]
+ -[RISessionSchemaRISessionError errorDomain]
+ -[RISessionSchemaRISessionError hasErrorCode]
+ -[RISessionSchemaRISessionError hasErrorDomain]
+ -[RISessionSchemaRISessionError hash]
+ -[RISessionSchemaRISessionError initWithDictionary:]
+ -[RISessionSchemaRISessionError initWithJSON:]
+ -[RISessionSchemaRISessionError isEqual:]
+ -[RISessionSchemaRISessionError jsonData]
+ -[RISessionSchemaRISessionError readFrom:]
+ -[RISessionSchemaRISessionError setErrorCode:]
+ -[RISessionSchemaRISessionError setErrorDomain:]
+ -[RISessionSchemaRISessionError setHasErrorCode:]
+ -[RISessionSchemaRISessionError setHasErrorDomain:]
+ -[RISessionSchemaRISessionError writeTo:]
+ -[RISessionSchemaRISessionRemoteContext .cxx_destruct]
+ -[RISessionSchemaRISessionRemoteContext deleteEnded]
+ -[RISessionSchemaRISessionRemoteContext deleteFailed]
+ -[RISessionSchemaRISessionRemoteContext deleteStartedOrChanged]
+ -[RISessionSchemaRISessionRemoteContext dictionaryRepresentation]
+ -[RISessionSchemaRISessionRemoteContext ended]
+ -[RISessionSchemaRISessionRemoteContext failed]
+ -[RISessionSchemaRISessionRemoteContext hasEnded]
+ -[RISessionSchemaRISessionRemoteContext hasFailed]
+ -[RISessionSchemaRISessionRemoteContext hasStartedOrChanged]
+ -[RISessionSchemaRISessionRemoteContext hash]
+ -[RISessionSchemaRISessionRemoteContext initWithDictionary:]
+ -[RISessionSchemaRISessionRemoteContext initWithJSON:]
+ -[RISessionSchemaRISessionRemoteContext isEqual:]
+ -[RISessionSchemaRISessionRemoteContext jsonData]
+ -[RISessionSchemaRISessionRemoteContext readFrom:]
+ -[RISessionSchemaRISessionRemoteContext setEnded:]
+ -[RISessionSchemaRISessionRemoteContext setFailed:]
+ -[RISessionSchemaRISessionRemoteContext setHasEnded:]
+ -[RISessionSchemaRISessionRemoteContext setHasFailed:]
+ -[RISessionSchemaRISessionRemoteContext setHasStartedOrChanged:]
+ -[RISessionSchemaRISessionRemoteContext setStartedOrChanged:]
+ -[RISessionSchemaRISessionRemoteContext startedOrChanged]
+ -[RISessionSchemaRISessionRemoteContext whichContextevent]
+ -[RISessionSchemaRISessionRemoteContext writeTo:]
+ -[RISessionSchemaRISessionRemoteEnded deleteExists]
+ -[RISessionSchemaRISessionRemoteEnded dictionaryRepresentation]
+ -[RISessionSchemaRISessionRemoteEnded exists]
+ -[RISessionSchemaRISessionRemoteEnded hasExists]
+ -[RISessionSchemaRISessionRemoteEnded hash]
+ -[RISessionSchemaRISessionRemoteEnded initWithDictionary:]
+ -[RISessionSchemaRISessionRemoteEnded initWithJSON:]
+ -[RISessionSchemaRISessionRemoteEnded isEqual:]
+ -[RISessionSchemaRISessionRemoteEnded jsonData]
+ -[RISessionSchemaRISessionRemoteEnded readFrom:]
+ -[RISessionSchemaRISessionRemoteEnded setExists:]
+ -[RISessionSchemaRISessionRemoteEnded setHasExists:]
+ -[RISessionSchemaRISessionRemoteEnded writeTo:]
+ -[RISessionSchemaRISessionRemoteFailed .cxx_destruct]
+ -[RISessionSchemaRISessionRemoteFailed deleteError]
+ -[RISessionSchemaRISessionRemoteFailed deleteExists]
+ -[RISessionSchemaRISessionRemoteFailed deleteUnderUnderlyingError]
+ -[RISessionSchemaRISessionRemoteFailed deleteUnderlyingError]
+ -[RISessionSchemaRISessionRemoteFailed dictionaryRepresentation]
+ -[RISessionSchemaRISessionRemoteFailed error]
+ -[RISessionSchemaRISessionRemoteFailed exists]
+ -[RISessionSchemaRISessionRemoteFailed hasError]
+ -[RISessionSchemaRISessionRemoteFailed hasExists]
+ -[RISessionSchemaRISessionRemoteFailed hasUnderUnderlyingError]
+ -[RISessionSchemaRISessionRemoteFailed hasUnderlyingError]
+ -[RISessionSchemaRISessionRemoteFailed hash]
+ -[RISessionSchemaRISessionRemoteFailed initWithDictionary:]
+ -[RISessionSchemaRISessionRemoteFailed initWithJSON:]
+ -[RISessionSchemaRISessionRemoteFailed isEqual:]
+ -[RISessionSchemaRISessionRemoteFailed jsonData]
+ -[RISessionSchemaRISessionRemoteFailed readFrom:]
+ -[RISessionSchemaRISessionRemoteFailed setError:]
+ -[RISessionSchemaRISessionRemoteFailed setExists:]
+ -[RISessionSchemaRISessionRemoteFailed setHasError:]
+ -[RISessionSchemaRISessionRemoteFailed setHasExists:]
+ -[RISessionSchemaRISessionRemoteFailed setHasUnderUnderlyingError:]
+ -[RISessionSchemaRISessionRemoteFailed setHasUnderlyingError:]
+ -[RISessionSchemaRISessionRemoteFailed setUnderUnderlyingError:]
+ -[RISessionSchemaRISessionRemoteFailed setUnderlyingError:]
+ -[RISessionSchemaRISessionRemoteFailed underUnderlyingError]
+ -[RISessionSchemaRISessionRemoteFailed underlyingError]
+ -[RISessionSchemaRISessionRemoteFailed writeTo:]
+ -[RISessionSchemaRISessionRemoteStarted deleteExists]
+ -[RISessionSchemaRISessionRemoteStarted dictionaryRepresentation]
+ -[RISessionSchemaRISessionRemoteStarted exists]
+ -[RISessionSchemaRISessionRemoteStarted hasExists]
+ -[RISessionSchemaRISessionRemoteStarted hash]
+ -[RISessionSchemaRISessionRemoteStarted initWithDictionary:]
+ -[RISessionSchemaRISessionRemoteStarted initWithJSON:]
+ -[RISessionSchemaRISessionRemoteStarted isEqual:]
+ -[RISessionSchemaRISessionRemoteStarted jsonData]
+ -[RISessionSchemaRISessionRemoteStarted readFrom:]
+ -[RISessionSchemaRISessionRemoteStarted setExists:]
+ -[RISessionSchemaRISessionRemoteStarted setHasExists:]
+ -[RISessionSchemaRISessionRemoteStarted writeTo:]
+ -[RISessionSchemaRISessionSourceContext .cxx_destruct]
+ -[RISessionSchemaRISessionSourceContext deleteEnded]
+ -[RISessionSchemaRISessionSourceContext deleteFailed]
+ -[RISessionSchemaRISessionSourceContext deleteStartedOrChanged]
+ -[RISessionSchemaRISessionSourceContext dictionaryRepresentation]
+ -[RISessionSchemaRISessionSourceContext ended]
+ -[RISessionSchemaRISessionSourceContext failed]
+ -[RISessionSchemaRISessionSourceContext hasEnded]
+ -[RISessionSchemaRISessionSourceContext hasFailed]
+ -[RISessionSchemaRISessionSourceContext hasStartedOrChanged]
+ -[RISessionSchemaRISessionSourceContext hash]
+ -[RISessionSchemaRISessionSourceContext initWithDictionary:]
+ -[RISessionSchemaRISessionSourceContext initWithJSON:]
+ -[RISessionSchemaRISessionSourceContext isEqual:]
+ -[RISessionSchemaRISessionSourceContext jsonData]
+ -[RISessionSchemaRISessionSourceContext readFrom:]
+ -[RISessionSchemaRISessionSourceContext setEnded:]
+ -[RISessionSchemaRISessionSourceContext setFailed:]
+ -[RISessionSchemaRISessionSourceContext setHasEnded:]
+ -[RISessionSchemaRISessionSourceContext setHasFailed:]
+ -[RISessionSchemaRISessionSourceContext setHasStartedOrChanged:]
+ -[RISessionSchemaRISessionSourceContext setStartedOrChanged:]
+ -[RISessionSchemaRISessionSourceContext startedOrChanged]
+ -[RISessionSchemaRISessionSourceContext whichContextevent]
+ -[RISessionSchemaRISessionSourceContext writeTo:]
+ -[RISessionSchemaRISessionSourceEnded deleteExists]
+ -[RISessionSchemaRISessionSourceEnded dictionaryRepresentation]
+ -[RISessionSchemaRISessionSourceEnded exists]
+ -[RISessionSchemaRISessionSourceEnded hasExists]
+ -[RISessionSchemaRISessionSourceEnded hash]
+ -[RISessionSchemaRISessionSourceEnded initWithDictionary:]
+ -[RISessionSchemaRISessionSourceEnded initWithJSON:]
+ -[RISessionSchemaRISessionSourceEnded isEqual:]
+ -[RISessionSchemaRISessionSourceEnded jsonData]
+ -[RISessionSchemaRISessionSourceEnded readFrom:]
+ -[RISessionSchemaRISessionSourceEnded setExists:]
+ -[RISessionSchemaRISessionSourceEnded setHasExists:]
+ -[RISessionSchemaRISessionSourceEnded writeTo:]
+ -[RISessionSchemaRISessionSourceFailed .cxx_destruct]
+ -[RISessionSchemaRISessionSourceFailed deleteError]
+ -[RISessionSchemaRISessionSourceFailed deleteExists]
+ -[RISessionSchemaRISessionSourceFailed deleteUnderUnderlyingError]
+ -[RISessionSchemaRISessionSourceFailed deleteUnderlyingError]
+ -[RISessionSchemaRISessionSourceFailed dictionaryRepresentation]
+ -[RISessionSchemaRISessionSourceFailed error]
+ -[RISessionSchemaRISessionSourceFailed exists]
+ -[RISessionSchemaRISessionSourceFailed hasError]
+ -[RISessionSchemaRISessionSourceFailed hasExists]
+ -[RISessionSchemaRISessionSourceFailed hasUnderUnderlyingError]
+ -[RISessionSchemaRISessionSourceFailed hasUnderlyingError]
+ -[RISessionSchemaRISessionSourceFailed hash]
+ -[RISessionSchemaRISessionSourceFailed initWithDictionary:]
+ -[RISessionSchemaRISessionSourceFailed initWithJSON:]
+ -[RISessionSchemaRISessionSourceFailed isEqual:]
+ -[RISessionSchemaRISessionSourceFailed jsonData]
+ -[RISessionSchemaRISessionSourceFailed readFrom:]
+ -[RISessionSchemaRISessionSourceFailed setError:]
+ -[RISessionSchemaRISessionSourceFailed setExists:]
+ -[RISessionSchemaRISessionSourceFailed setHasError:]
+ -[RISessionSchemaRISessionSourceFailed setHasExists:]
+ -[RISessionSchemaRISessionSourceFailed setHasUnderUnderlyingError:]
+ -[RISessionSchemaRISessionSourceFailed setHasUnderlyingError:]
+ -[RISessionSchemaRISessionSourceFailed setUnderUnderlyingError:]
+ -[RISessionSchemaRISessionSourceFailed setUnderlyingError:]
+ -[RISessionSchemaRISessionSourceFailed underUnderlyingError]
+ -[RISessionSchemaRISessionSourceFailed underlyingError]
+ -[RISessionSchemaRISessionSourceFailed writeTo:]
+ -[RISessionSchemaRISessionSourceStarted communicationType]
+ -[RISessionSchemaRISessionSourceStarted deleteCommunicationType]
+ -[RISessionSchemaRISessionSourceStarted deleteExists]
+ -[RISessionSchemaRISessionSourceStarted dictionaryRepresentation]
+ -[RISessionSchemaRISessionSourceStarted exists]
+ -[RISessionSchemaRISessionSourceStarted hasCommunicationType]
+ -[RISessionSchemaRISessionSourceStarted hasExists]
+ -[RISessionSchemaRISessionSourceStarted hash]
+ -[RISessionSchemaRISessionSourceStarted initWithDictionary:]
+ -[RISessionSchemaRISessionSourceStarted initWithJSON:]
+ -[RISessionSchemaRISessionSourceStarted isEqual:]
+ -[RISessionSchemaRISessionSourceStarted jsonData]
+ -[RISessionSchemaRISessionSourceStarted readFrom:]
+ -[RISessionSchemaRISessionSourceStarted setCommunicationType:]
+ -[RISessionSchemaRISessionSourceStarted setExists:]
+ -[RISessionSchemaRISessionSourceStarted setHasCommunicationType:]
+ -[RISessionSchemaRISessionSourceStarted setHasExists:]
+ -[RISessionSchemaRISessionSourceStarted writeTo:]
+ -[SISchemaClientEvent deleteUeiResponseAppLaunchContext]
+ -[SISchemaClientEvent hasUeiResponseAppLaunchContext]
+ -[SISchemaClientEvent setHasUeiResponseAppLaunchContext:]
+ -[SISchemaClientEvent setUeiResponseAppLaunchContext:]
+ -[SISchemaClientEvent ueiResponseAppLaunchContext]
+ -[SISchemaUEIResponseAppLaunchCanceled deleteExists]
+ -[SISchemaUEIResponseAppLaunchCanceled dictionaryRepresentation]
+ -[SISchemaUEIResponseAppLaunchCanceled exists]
+ -[SISchemaUEIResponseAppLaunchCanceled hasExists]
+ -[SISchemaUEIResponseAppLaunchCanceled hash]
+ -[SISchemaUEIResponseAppLaunchCanceled initWithDictionary:]
+ -[SISchemaUEIResponseAppLaunchCanceled initWithJSON:]
+ -[SISchemaUEIResponseAppLaunchCanceled isEqual:]
+ -[SISchemaUEIResponseAppLaunchCanceled jsonData]
+ -[SISchemaUEIResponseAppLaunchCanceled readFrom:]
+ -[SISchemaUEIResponseAppLaunchCanceled setExists:]
+ -[SISchemaUEIResponseAppLaunchCanceled setHasExists:]
+ -[SISchemaUEIResponseAppLaunchCanceled writeTo:]
+ -[SISchemaUEIResponseAppLaunchContext .cxx_destruct]
+ -[SISchemaUEIResponseAppLaunchContext canceled]
+ -[SISchemaUEIResponseAppLaunchContext deleteCanceled]
+ -[SISchemaUEIResponseAppLaunchContext deleteEnded]
+ -[SISchemaUEIResponseAppLaunchContext deleteFailed]
+ -[SISchemaUEIResponseAppLaunchContext deleteStartedOrChanged]
+ -[SISchemaUEIResponseAppLaunchContext dictionaryRepresentation]
+ -[SISchemaUEIResponseAppLaunchContext ended]
+ -[SISchemaUEIResponseAppLaunchContext failed]
+ -[SISchemaUEIResponseAppLaunchContext hasCanceled]
+ -[SISchemaUEIResponseAppLaunchContext hasEnded]
+ -[SISchemaUEIResponseAppLaunchContext hasFailed]
+ -[SISchemaUEIResponseAppLaunchContext hasStartedOrChanged]
+ -[SISchemaUEIResponseAppLaunchContext hash]
+ -[SISchemaUEIResponseAppLaunchContext initWithDictionary:]
+ -[SISchemaUEIResponseAppLaunchContext initWithJSON:]
+ -[SISchemaUEIResponseAppLaunchContext isEqual:]
+ -[SISchemaUEIResponseAppLaunchContext jsonData]
+ -[SISchemaUEIResponseAppLaunchContext readFrom:]
+ -[SISchemaUEIResponseAppLaunchContext setCanceled:]
+ -[SISchemaUEIResponseAppLaunchContext setEnded:]
+ -[SISchemaUEIResponseAppLaunchContext setFailed:]
+ -[SISchemaUEIResponseAppLaunchContext setHasCanceled:]
+ -[SISchemaUEIResponseAppLaunchContext setHasEnded:]
+ -[SISchemaUEIResponseAppLaunchContext setHasFailed:]
+ -[SISchemaUEIResponseAppLaunchContext setHasStartedOrChanged:]
+ -[SISchemaUEIResponseAppLaunchContext setStartedOrChanged:]
+ -[SISchemaUEIResponseAppLaunchContext startedOrChanged]
+ -[SISchemaUEIResponseAppLaunchContext whichContextevent]
+ -[SISchemaUEIResponseAppLaunchContext writeTo:]
+ -[SISchemaUEIResponseAppLaunchEnded .cxx_destruct]
+ -[SISchemaUEIResponseAppLaunchEnded deleteExecutorAppIntentMetrics]
+ -[SISchemaUEIResponseAppLaunchEnded dictionaryRepresentation]
+ -[SISchemaUEIResponseAppLaunchEnded executorAppIntentMetrics]
+ -[SISchemaUEIResponseAppLaunchEnded hasExecutorAppIntentMetrics]
+ -[SISchemaUEIResponseAppLaunchEnded hash]
+ -[SISchemaUEIResponseAppLaunchEnded initWithDictionary:]
+ -[SISchemaUEIResponseAppLaunchEnded initWithJSON:]
+ -[SISchemaUEIResponseAppLaunchEnded isEqual:]
+ -[SISchemaUEIResponseAppLaunchEnded jsonData]
+ -[SISchemaUEIResponseAppLaunchEnded readFrom:]
+ -[SISchemaUEIResponseAppLaunchEnded setExecutorAppIntentMetrics:]
+ -[SISchemaUEIResponseAppLaunchEnded setHasExecutorAppIntentMetrics:]
+ -[SISchemaUEIResponseAppLaunchEnded writeTo:]
+ -[SISchemaUEIResponseAppLaunchFailed .cxx_destruct]
+ -[SISchemaUEIResponseAppLaunchFailed addErrors:]
+ -[SISchemaUEIResponseAppLaunchFailed clearErrors]
+ -[SISchemaUEIResponseAppLaunchFailed deleteErrors]
+ -[SISchemaUEIResponseAppLaunchFailed dictionaryRepresentation]
+ -[SISchemaUEIResponseAppLaunchFailed errorsAtIndex:]
+ -[SISchemaUEIResponseAppLaunchFailed errorsCount]
+ -[SISchemaUEIResponseAppLaunchFailed errors]
+ -[SISchemaUEIResponseAppLaunchFailed hash]
+ -[SISchemaUEIResponseAppLaunchFailed initWithDictionary:]
+ -[SISchemaUEIResponseAppLaunchFailed initWithJSON:]
+ -[SISchemaUEIResponseAppLaunchFailed isEqual:]
+ -[SISchemaUEIResponseAppLaunchFailed jsonData]
+ -[SISchemaUEIResponseAppLaunchFailed readFrom:]
+ -[SISchemaUEIResponseAppLaunchFailed setErrors:]
+ -[SISchemaUEIResponseAppLaunchFailed writeTo:]
+ -[SISchemaUEIResponseAppLaunchStarted deleteExists]
+ -[SISchemaUEIResponseAppLaunchStarted dictionaryRepresentation]
+ -[SISchemaUEIResponseAppLaunchStarted exists]
+ -[SISchemaUEIResponseAppLaunchStarted hasExists]
+ -[SISchemaUEIResponseAppLaunchStarted hash]
+ -[SISchemaUEIResponseAppLaunchStarted initWithDictionary:]
+ -[SISchemaUEIResponseAppLaunchStarted initWithJSON:]
+ -[SISchemaUEIResponseAppLaunchStarted isEqual:]
+ -[SISchemaUEIResponseAppLaunchStarted jsonData]
+ -[SISchemaUEIResponseAppLaunchStarted readFrom:]
+ -[SISchemaUEIResponseAppLaunchStarted setExists:]
+ -[SISchemaUEIResponseAppLaunchStarted setHasExists:]
+ -[SISchemaUEIResponseAppLaunchStarted writeTo:]
+ OBJC_IVAR_$_ORCHSchemaORCHSpeakerIdentificationResultReceived._identityAggressors
+ OBJC_IVAR_$_ORCHSchemaORCHSpeakerIdentificationResultReceived._isRecentlySeen
+ OBJC_IVAR_$_PLANNERSchemaPLANNERUserIdentityChecked._isRecentlySeen
+ OBJC_IVAR_$_RISchemaRIClientEvent._eventMetadata
+ OBJC_IVAR_$_RISchemaRIClientEvent._remoteContext
+ OBJC_IVAR_$_RISchemaRIClientEvent._sourceContext
+ OBJC_IVAR_$_RISchemaRIClientEventMetadata._riId
+ OBJC_IVAR_$_RISchemaRIError._errorCode
+ OBJC_IVAR_$_RISchemaRIError._errorDomain
+ OBJC_IVAR_$_RISchemaRIError._has
+ OBJC_IVAR_$_RISchemaRIRemoteContext._ended
+ OBJC_IVAR_$_RISchemaRIRemoteContext._failed
+ OBJC_IVAR_$_RISchemaRIRemoteContext._startedOrChanged
+ OBJC_IVAR_$_RISchemaRIRemoteEnded._exists
+ OBJC_IVAR_$_RISchemaRIRemoteEnded._has
+ OBJC_IVAR_$_RISchemaRIRemoteFailed._error
+ OBJC_IVAR_$_RISchemaRIRemoteFailed._exists
+ OBJC_IVAR_$_RISchemaRIRemoteFailed._has
+ OBJC_IVAR_$_RISchemaRIRemoteFailed._underUnderlyingError
+ OBJC_IVAR_$_RISchemaRIRemoteFailed._underlyingError
+ OBJC_IVAR_$_RISchemaRIRemoteStarted._has
+ OBJC_IVAR_$_RISchemaRIRemoteStarted._isColdLaunch
+ OBJC_IVAR_$_RISchemaRIRemoteStarted._riSessionId
+ OBJC_IVAR_$_RISchemaRISourceContext._ended
+ OBJC_IVAR_$_RISchemaRISourceContext._failed
+ OBJC_IVAR_$_RISchemaRISourceContext._startedOrChanged
+ OBJC_IVAR_$_RISchemaRISourceEnded._exists
+ OBJC_IVAR_$_RISchemaRISourceEnded._has
+ OBJC_IVAR_$_RISchemaRISourceEnded._remoteTimeInMs
+ OBJC_IVAR_$_RISchemaRISourceEnded._roundTripCount
+ OBJC_IVAR_$_RISchemaRISourceEnded._sizeInBytes
+ OBJC_IVAR_$_RISchemaRISourceFailed._error
+ OBJC_IVAR_$_RISchemaRISourceFailed._exists
+ OBJC_IVAR_$_RISchemaRISourceFailed._has
+ OBJC_IVAR_$_RISchemaRISourceFailed._underUnderlyingError
+ OBJC_IVAR_$_RISchemaRISourceFailed._underlyingError
+ OBJC_IVAR_$_RISchemaRISourceStarted._communicationType
+ OBJC_IVAR_$_RISchemaRISourceStarted._has
+ OBJC_IVAR_$_RISchemaRISourceStarted._riSessionId
+ OBJC_IVAR_$_RISessionSchemaRISessionClientEvent._eventMetadata
+ OBJC_IVAR_$_RISessionSchemaRISessionClientEvent._remoteSessionContext
+ OBJC_IVAR_$_RISessionSchemaRISessionClientEvent._sourceSessionContext
+ OBJC_IVAR_$_RISessionSchemaRISessionClientEventMetadata._riSessionId
+ OBJC_IVAR_$_RISessionSchemaRISessionError._errorCode
+ OBJC_IVAR_$_RISessionSchemaRISessionError._errorDomain
+ OBJC_IVAR_$_RISessionSchemaRISessionError._has
+ OBJC_IVAR_$_RISessionSchemaRISessionRemoteContext._ended
+ OBJC_IVAR_$_RISessionSchemaRISessionRemoteContext._failed
+ OBJC_IVAR_$_RISessionSchemaRISessionRemoteContext._startedOrChanged
+ OBJC_IVAR_$_RISessionSchemaRISessionRemoteEnded._exists
+ OBJC_IVAR_$_RISessionSchemaRISessionRemoteEnded._has
+ OBJC_IVAR_$_RISessionSchemaRISessionRemoteFailed._error
+ OBJC_IVAR_$_RISessionSchemaRISessionRemoteFailed._exists
+ OBJC_IVAR_$_RISessionSchemaRISessionRemoteFailed._has
+ OBJC_IVAR_$_RISessionSchemaRISessionRemoteFailed._underUnderlyingError
+ OBJC_IVAR_$_RISessionSchemaRISessionRemoteFailed._underlyingError
+ OBJC_IVAR_$_RISessionSchemaRISessionRemoteStarted._exists
+ OBJC_IVAR_$_RISessionSchemaRISessionRemoteStarted._has
+ OBJC_IVAR_$_RISessionSchemaRISessionSourceContext._ended
+ OBJC_IVAR_$_RISessionSchemaRISessionSourceContext._failed
+ OBJC_IVAR_$_RISessionSchemaRISessionSourceContext._startedOrChanged
+ OBJC_IVAR_$_RISessionSchemaRISessionSourceEnded._exists
+ OBJC_IVAR_$_RISessionSchemaRISessionSourceEnded._has
+ OBJC_IVAR_$_RISessionSchemaRISessionSourceFailed._error
+ OBJC_IVAR_$_RISessionSchemaRISessionSourceFailed._exists
+ OBJC_IVAR_$_RISessionSchemaRISessionSourceFailed._has
+ OBJC_IVAR_$_RISessionSchemaRISessionSourceFailed._underUnderlyingError
+ OBJC_IVAR_$_RISessionSchemaRISessionSourceFailed._underlyingError
+ OBJC_IVAR_$_RISessionSchemaRISessionSourceStarted._communicationType
+ OBJC_IVAR_$_RISessionSchemaRISessionSourceStarted._exists
+ OBJC_IVAR_$_RISessionSchemaRISessionSourceStarted._has
+ OBJC_IVAR_$_SISchemaClientEvent._ueiResponseAppLaunchContext
+ OBJC_IVAR_$_SISchemaUEIResponseAppLaunchCanceled._exists
+ OBJC_IVAR_$_SISchemaUEIResponseAppLaunchCanceled._has
+ OBJC_IVAR_$_SISchemaUEIResponseAppLaunchContext._canceled
+ OBJC_IVAR_$_SISchemaUEIResponseAppLaunchContext._ended
+ OBJC_IVAR_$_SISchemaUEIResponseAppLaunchContext._failed
+ OBJC_IVAR_$_SISchemaUEIResponseAppLaunchContext._startedOrChanged
+ OBJC_IVAR_$_SISchemaUEIResponseAppLaunchEnded._executorAppIntentMetrics
+ OBJC_IVAR_$_SISchemaUEIResponseAppLaunchFailed._errors
+ OBJC_IVAR_$_SISchemaUEIResponseAppLaunchStarted._exists
+ OBJC_IVAR_$_SISchemaUEIResponseAppLaunchStarted._has
+ _OBJC_CLASS_$_RISchemaRIClientEvent
+ _OBJC_CLASS_$_RISchemaRIClientEventMetadata
+ _OBJC_CLASS_$_RISchemaRIError
+ _OBJC_CLASS_$_RISchemaRIRemoteContext
+ _OBJC_CLASS_$_RISchemaRIRemoteEnded
+ _OBJC_CLASS_$_RISchemaRIRemoteFailed
+ _OBJC_CLASS_$_RISchemaRIRemoteStarted
+ _OBJC_CLASS_$_RISchemaRISourceContext
+ _OBJC_CLASS_$_RISchemaRISourceEnded
+ _OBJC_CLASS_$_RISchemaRISourceFailed
+ _OBJC_CLASS_$_RISchemaRISourceStarted
+ _OBJC_CLASS_$_RISessionSchemaRISessionClientEvent
+ _OBJC_CLASS_$_RISessionSchemaRISessionClientEventMetadata
+ _OBJC_CLASS_$_RISessionSchemaRISessionError
+ _OBJC_CLASS_$_RISessionSchemaRISessionRemoteContext
+ _OBJC_CLASS_$_RISessionSchemaRISessionRemoteEnded
+ _OBJC_CLASS_$_RISessionSchemaRISessionRemoteFailed
+ _OBJC_CLASS_$_RISessionSchemaRISessionRemoteStarted
+ _OBJC_CLASS_$_RISessionSchemaRISessionSourceContext
+ _OBJC_CLASS_$_RISessionSchemaRISessionSourceEnded
+ _OBJC_CLASS_$_RISessionSchemaRISessionSourceFailed
+ _OBJC_CLASS_$_RISessionSchemaRISessionSourceStarted
+ _OBJC_CLASS_$_SISchemaUEIResponseAppLaunchCanceled
+ _OBJC_CLASS_$_SISchemaUEIResponseAppLaunchContext
+ _OBJC_CLASS_$_SISchemaUEIResponseAppLaunchEnded
+ _OBJC_CLASS_$_SISchemaUEIResponseAppLaunchFailed
+ _OBJC_CLASS_$_SISchemaUEIResponseAppLaunchStarted
+ _OBJC_IVAR_$_RISchemaRIClientEvent._hasEventMetadata
+ _OBJC_IVAR_$_RISchemaRIClientEvent._hasRemoteContext
+ _OBJC_IVAR_$_RISchemaRIClientEvent._hasSourceContext
+ _OBJC_IVAR_$_RISchemaRIClientEvent._whichEvent_Type
+ _OBJC_IVAR_$_RISchemaRIClientEventMetadata._hasRiId
+ _OBJC_IVAR_$_RISchemaRIError._hasErrorDomain
+ _OBJC_IVAR_$_RISchemaRIRemoteContext._hasEnded
+ _OBJC_IVAR_$_RISchemaRIRemoteContext._hasFailed
+ _OBJC_IVAR_$_RISchemaRIRemoteContext._hasStartedOrChanged
+ _OBJC_IVAR_$_RISchemaRIRemoteContext._whichContextevent
+ _OBJC_IVAR_$_RISchemaRIRemoteFailed._hasError
+ _OBJC_IVAR_$_RISchemaRIRemoteFailed._hasUnderUnderlyingError
+ _OBJC_IVAR_$_RISchemaRIRemoteFailed._hasUnderlyingError
+ _OBJC_IVAR_$_RISchemaRIRemoteStarted._hasRiSessionId
+ _OBJC_IVAR_$_RISchemaRISourceContext._hasEnded
+ _OBJC_IVAR_$_RISchemaRISourceContext._hasFailed
+ _OBJC_IVAR_$_RISchemaRISourceContext._hasStartedOrChanged
+ _OBJC_IVAR_$_RISchemaRISourceContext._whichContextevent
+ _OBJC_IVAR_$_RISchemaRISourceFailed._hasError
+ _OBJC_IVAR_$_RISchemaRISourceFailed._hasUnderUnderlyingError
+ _OBJC_IVAR_$_RISchemaRISourceFailed._hasUnderlyingError
+ _OBJC_IVAR_$_RISchemaRISourceStarted._hasRiSessionId
+ _OBJC_IVAR_$_RISessionSchemaRISessionClientEvent._hasEventMetadata
+ _OBJC_IVAR_$_RISessionSchemaRISessionClientEvent._hasRemoteSessionContext
+ _OBJC_IVAR_$_RISessionSchemaRISessionClientEvent._hasSourceSessionContext
+ _OBJC_IVAR_$_RISessionSchemaRISessionClientEvent._whichEvent_Type
+ _OBJC_IVAR_$_RISessionSchemaRISessionClientEventMetadata._hasRiSessionId
+ _OBJC_IVAR_$_RISessionSchemaRISessionError._hasErrorDomain
+ _OBJC_IVAR_$_RISessionSchemaRISessionRemoteContext._hasEnded
+ _OBJC_IVAR_$_RISessionSchemaRISessionRemoteContext._hasFailed
+ _OBJC_IVAR_$_RISessionSchemaRISessionRemoteContext._hasStartedOrChanged
+ _OBJC_IVAR_$_RISessionSchemaRISessionRemoteContext._whichContextevent
+ _OBJC_IVAR_$_RISessionSchemaRISessionRemoteFailed._hasError
+ _OBJC_IVAR_$_RISessionSchemaRISessionRemoteFailed._hasUnderUnderlyingError
+ _OBJC_IVAR_$_RISessionSchemaRISessionRemoteFailed._hasUnderlyingError
+ _OBJC_IVAR_$_RISessionSchemaRISessionSourceContext._hasEnded
+ _OBJC_IVAR_$_RISessionSchemaRISessionSourceContext._hasFailed
+ _OBJC_IVAR_$_RISessionSchemaRISessionSourceContext._hasStartedOrChanged
+ _OBJC_IVAR_$_RISessionSchemaRISessionSourceContext._whichContextevent
+ _OBJC_IVAR_$_RISessionSchemaRISessionSourceFailed._hasError
+ _OBJC_IVAR_$_RISessionSchemaRISessionSourceFailed._hasUnderUnderlyingError
+ _OBJC_IVAR_$_RISessionSchemaRISessionSourceFailed._hasUnderlyingError
+ _OBJC_IVAR_$_SISchemaClientEvent._hasUeiResponseAppLaunchContext
+ _OBJC_IVAR_$_SISchemaUEIResponseAppLaunchContext._hasCanceled
+ _OBJC_IVAR_$_SISchemaUEIResponseAppLaunchContext._hasEnded
+ _OBJC_IVAR_$_SISchemaUEIResponseAppLaunchContext._hasFailed
+ _OBJC_IVAR_$_SISchemaUEIResponseAppLaunchContext._hasStartedOrChanged
+ _OBJC_IVAR_$_SISchemaUEIResponseAppLaunchContext._whichContextevent
+ _OBJC_IVAR_$_SISchemaUEIResponseAppLaunchEnded._hasExecutorAppIntentMetrics
+ _OBJC_METACLASS_$_RISchemaRIClientEvent
+ _OBJC_METACLASS_$_RISchemaRIClientEventMetadata
+ _OBJC_METACLASS_$_RISchemaRIError
+ _OBJC_METACLASS_$_RISchemaRIRemoteContext
+ _OBJC_METACLASS_$_RISchemaRIRemoteEnded
+ _OBJC_METACLASS_$_RISchemaRIRemoteFailed
+ _OBJC_METACLASS_$_RISchemaRIRemoteStarted
+ _OBJC_METACLASS_$_RISchemaRISourceContext
+ _OBJC_METACLASS_$_RISchemaRISourceEnded
+ _OBJC_METACLASS_$_RISchemaRISourceFailed
+ _OBJC_METACLASS_$_RISchemaRISourceStarted
+ _OBJC_METACLASS_$_RISessionSchemaRISessionClientEvent
+ _OBJC_METACLASS_$_RISessionSchemaRISessionClientEventMetadata
+ _OBJC_METACLASS_$_RISessionSchemaRISessionError
+ _OBJC_METACLASS_$_RISessionSchemaRISessionRemoteContext
+ _OBJC_METACLASS_$_RISessionSchemaRISessionRemoteEnded
+ _OBJC_METACLASS_$_RISessionSchemaRISessionRemoteFailed
+ _OBJC_METACLASS_$_RISessionSchemaRISessionRemoteStarted
+ _OBJC_METACLASS_$_RISessionSchemaRISessionSourceContext
+ _OBJC_METACLASS_$_RISessionSchemaRISessionSourceEnded
+ _OBJC_METACLASS_$_RISessionSchemaRISessionSourceFailed
+ _OBJC_METACLASS_$_RISessionSchemaRISessionSourceStarted
+ _OBJC_METACLASS_$_SISchemaUEIResponseAppLaunchCanceled
+ _OBJC_METACLASS_$_SISchemaUEIResponseAppLaunchContext
+ _OBJC_METACLASS_$_SISchemaUEIResponseAppLaunchEnded
+ _OBJC_METACLASS_$_SISchemaUEIResponseAppLaunchFailed
+ _OBJC_METACLASS_$_SISchemaUEIResponseAppLaunchStarted
+ __OBJC_$_CLASS_METHODS_RISchemaRIClientEvent(InstrumentationAdditions|Component|InnerEventContainer)
+ __OBJC_$_CLASS_METHODS_RISessionSchemaRISessionClientEvent(InstrumentationAdditions|Component|InnerEventContainer)
+ __OBJC_$_INSTANCE_METHODS_RISchemaRIClientEvent(InstrumentationAdditions|Component|InnerEventContainer)
+ __OBJC_$_INSTANCE_METHODS_RISchemaRIClientEventMetadata
+ __OBJC_$_INSTANCE_METHODS_RISchemaRIError
+ __OBJC_$_INSTANCE_METHODS_RISchemaRIRemoteContext
+ __OBJC_$_INSTANCE_METHODS_RISchemaRIRemoteEnded
+ __OBJC_$_INSTANCE_METHODS_RISchemaRIRemoteFailed
+ __OBJC_$_INSTANCE_METHODS_RISchemaRIRemoteStarted
+ __OBJC_$_INSTANCE_METHODS_RISchemaRISourceContext
+ __OBJC_$_INSTANCE_METHODS_RISchemaRISourceEnded
+ __OBJC_$_INSTANCE_METHODS_RISchemaRISourceFailed
+ __OBJC_$_INSTANCE_METHODS_RISchemaRISourceStarted
+ __OBJC_$_INSTANCE_METHODS_RISessionSchemaRISessionClientEvent(InstrumentationAdditions|Component|InnerEventContainer)
+ __OBJC_$_INSTANCE_METHODS_RISessionSchemaRISessionClientEventMetadata
+ __OBJC_$_INSTANCE_METHODS_RISessionSchemaRISessionError
+ __OBJC_$_INSTANCE_METHODS_RISessionSchemaRISessionRemoteContext
+ __OBJC_$_INSTANCE_METHODS_RISessionSchemaRISessionRemoteEnded
+ __OBJC_$_INSTANCE_METHODS_RISessionSchemaRISessionRemoteFailed
+ __OBJC_$_INSTANCE_METHODS_RISessionSchemaRISessionRemoteStarted
+ __OBJC_$_INSTANCE_METHODS_RISessionSchemaRISessionSourceContext
+ __OBJC_$_INSTANCE_METHODS_RISessionSchemaRISessionSourceEnded
+ __OBJC_$_INSTANCE_METHODS_RISessionSchemaRISessionSourceFailed
+ __OBJC_$_INSTANCE_METHODS_RISessionSchemaRISessionSourceStarted
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEIResponseAppLaunchCanceled
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEIResponseAppLaunchContext
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEIResponseAppLaunchEnded
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEIResponseAppLaunchFailed
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEIResponseAppLaunchStarted
+ __OBJC_$_INSTANCE_VARIABLES_RISchemaRIClientEvent
+ __OBJC_$_INSTANCE_VARIABLES_RISchemaRIClientEventMetadata
+ __OBJC_$_INSTANCE_VARIABLES_RISchemaRIError
+ __OBJC_$_INSTANCE_VARIABLES_RISchemaRIRemoteContext
+ __OBJC_$_INSTANCE_VARIABLES_RISchemaRIRemoteEnded
+ __OBJC_$_INSTANCE_VARIABLES_RISchemaRIRemoteFailed
+ __OBJC_$_INSTANCE_VARIABLES_RISchemaRIRemoteStarted
+ __OBJC_$_INSTANCE_VARIABLES_RISchemaRISourceContext
+ __OBJC_$_INSTANCE_VARIABLES_RISchemaRISourceEnded
+ __OBJC_$_INSTANCE_VARIABLES_RISchemaRISourceFailed
+ __OBJC_$_INSTANCE_VARIABLES_RISchemaRISourceStarted
+ __OBJC_$_INSTANCE_VARIABLES_RISessionSchemaRISessionClientEvent
+ __OBJC_$_INSTANCE_VARIABLES_RISessionSchemaRISessionClientEventMetadata
+ __OBJC_$_INSTANCE_VARIABLES_RISessionSchemaRISessionError
+ __OBJC_$_INSTANCE_VARIABLES_RISessionSchemaRISessionRemoteContext
+ __OBJC_$_INSTANCE_VARIABLES_RISessionSchemaRISessionRemoteEnded
+ __OBJC_$_INSTANCE_VARIABLES_RISessionSchemaRISessionRemoteFailed
+ __OBJC_$_INSTANCE_VARIABLES_RISessionSchemaRISessionRemoteStarted
+ __OBJC_$_INSTANCE_VARIABLES_RISessionSchemaRISessionSourceContext
+ __OBJC_$_INSTANCE_VARIABLES_RISessionSchemaRISessionSourceEnded
+ __OBJC_$_INSTANCE_VARIABLES_RISessionSchemaRISessionSourceFailed
+ __OBJC_$_INSTANCE_VARIABLES_RISessionSchemaRISessionSourceStarted
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEIResponseAppLaunchCanceled
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEIResponseAppLaunchContext
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEIResponseAppLaunchEnded
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEIResponseAppLaunchFailed
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEIResponseAppLaunchStarted
+ __OBJC_$_PROP_LIST_RISchemaRIClientEventMetadata
+ __OBJC_$_PROP_LIST_RISchemaRIError
+ __OBJC_$_PROP_LIST_RISchemaRIRemoteContext
+ __OBJC_$_PROP_LIST_RISchemaRIRemoteEnded
+ __OBJC_$_PROP_LIST_RISchemaRIRemoteFailed
+ __OBJC_$_PROP_LIST_RISchemaRIRemoteStarted
+ __OBJC_$_PROP_LIST_RISchemaRISourceContext
+ __OBJC_$_PROP_LIST_RISchemaRISourceEnded
+ __OBJC_$_PROP_LIST_RISchemaRISourceFailed
+ __OBJC_$_PROP_LIST_RISchemaRISourceStarted
+ __OBJC_$_PROP_LIST_RISessionSchemaRISessionClientEventMetadata
+ __OBJC_$_PROP_LIST_RISessionSchemaRISessionError
+ __OBJC_$_PROP_LIST_RISessionSchemaRISessionRemoteContext
+ __OBJC_$_PROP_LIST_RISessionSchemaRISessionRemoteEnded
+ __OBJC_$_PROP_LIST_RISessionSchemaRISessionRemoteFailed
+ __OBJC_$_PROP_LIST_RISessionSchemaRISessionRemoteStarted
+ __OBJC_$_PROP_LIST_RISessionSchemaRISessionSourceContext
+ __OBJC_$_PROP_LIST_RISessionSchemaRISessionSourceEnded
+ __OBJC_$_PROP_LIST_RISessionSchemaRISessionSourceFailed
+ __OBJC_$_PROP_LIST_RISessionSchemaRISessionSourceStarted
+ __OBJC_$_PROP_LIST_SISchemaUEIResponseAppLaunchCanceled
+ __OBJC_$_PROP_LIST_SISchemaUEIResponseAppLaunchContext
+ __OBJC_$_PROP_LIST_SISchemaUEIResponseAppLaunchEnded
+ __OBJC_$_PROP_LIST_SISchemaUEIResponseAppLaunchFailed
+ __OBJC_$_PROP_LIST_SISchemaUEIResponseAppLaunchStarted
+ __OBJC_CLASS_PROTOCOLS_$_RISchemaRIClientEvent(InstrumentationAdditions|Component|InnerEventContainer)
+ __OBJC_CLASS_PROTOCOLS_$_RISessionSchemaRISessionClientEvent(InstrumentationAdditions|Component|InnerEventContainer)
+ __OBJC_CLASS_RO_$_RISchemaRIClientEvent
+ __OBJC_CLASS_RO_$_RISchemaRIClientEventMetadata
+ __OBJC_CLASS_RO_$_RISchemaRIError
+ __OBJC_CLASS_RO_$_RISchemaRIRemoteContext
+ __OBJC_CLASS_RO_$_RISchemaRIRemoteEnded
+ __OBJC_CLASS_RO_$_RISchemaRIRemoteFailed
+ __OBJC_CLASS_RO_$_RISchemaRIRemoteStarted
+ __OBJC_CLASS_RO_$_RISchemaRISourceContext
+ __OBJC_CLASS_RO_$_RISchemaRISourceEnded
+ __OBJC_CLASS_RO_$_RISchemaRISourceFailed
+ __OBJC_CLASS_RO_$_RISchemaRISourceStarted
+ __OBJC_CLASS_RO_$_RISessionSchemaRISessionClientEvent
+ __OBJC_CLASS_RO_$_RISessionSchemaRISessionClientEventMetadata
+ __OBJC_CLASS_RO_$_RISessionSchemaRISessionError
+ __OBJC_CLASS_RO_$_RISessionSchemaRISessionRemoteContext
+ __OBJC_CLASS_RO_$_RISessionSchemaRISessionRemoteEnded
+ __OBJC_CLASS_RO_$_RISessionSchemaRISessionRemoteFailed
+ __OBJC_CLASS_RO_$_RISessionSchemaRISessionRemoteStarted
+ __OBJC_CLASS_RO_$_RISessionSchemaRISessionSourceContext
+ __OBJC_CLASS_RO_$_RISessionSchemaRISessionSourceEnded
+ __OBJC_CLASS_RO_$_RISessionSchemaRISessionSourceFailed
+ __OBJC_CLASS_RO_$_RISessionSchemaRISessionSourceStarted
+ __OBJC_CLASS_RO_$_SISchemaUEIResponseAppLaunchCanceled
+ __OBJC_CLASS_RO_$_SISchemaUEIResponseAppLaunchContext
+ __OBJC_CLASS_RO_$_SISchemaUEIResponseAppLaunchEnded
+ __OBJC_CLASS_RO_$_SISchemaUEIResponseAppLaunchFailed
+ __OBJC_CLASS_RO_$_SISchemaUEIResponseAppLaunchStarted
+ __OBJC_METACLASS_RO_$_RISchemaRIClientEvent
+ __OBJC_METACLASS_RO_$_RISchemaRIClientEventMetadata
+ __OBJC_METACLASS_RO_$_RISchemaRIError
+ __OBJC_METACLASS_RO_$_RISchemaRIRemoteContext
+ __OBJC_METACLASS_RO_$_RISchemaRIRemoteEnded
+ __OBJC_METACLASS_RO_$_RISchemaRIRemoteFailed
+ __OBJC_METACLASS_RO_$_RISchemaRIRemoteStarted
+ __OBJC_METACLASS_RO_$_RISchemaRISourceContext
+ __OBJC_METACLASS_RO_$_RISchemaRISourceEnded
+ __OBJC_METACLASS_RO_$_RISchemaRISourceFailed
+ __OBJC_METACLASS_RO_$_RISchemaRISourceStarted
+ __OBJC_METACLASS_RO_$_RISessionSchemaRISessionClientEvent
+ __OBJC_METACLASS_RO_$_RISessionSchemaRISessionClientEventMetadata
+ __OBJC_METACLASS_RO_$_RISessionSchemaRISessionError
+ __OBJC_METACLASS_RO_$_RISessionSchemaRISessionRemoteContext
+ __OBJC_METACLASS_RO_$_RISessionSchemaRISessionRemoteEnded
+ __OBJC_METACLASS_RO_$_RISessionSchemaRISessionRemoteFailed
+ __OBJC_METACLASS_RO_$_RISessionSchemaRISessionRemoteStarted
+ __OBJC_METACLASS_RO_$_RISessionSchemaRISessionSourceContext
+ __OBJC_METACLASS_RO_$_RISessionSchemaRISessionSourceEnded
+ __OBJC_METACLASS_RO_$_RISessionSchemaRISessionSourceFailed
+ __OBJC_METACLASS_RO_$_RISessionSchemaRISessionSourceStarted
+ __OBJC_METACLASS_RO_$_SISchemaUEIResponseAppLaunchCanceled
+ __OBJC_METACLASS_RO_$_SISchemaUEIResponseAppLaunchContext
+ __OBJC_METACLASS_RO_$_SISchemaUEIResponseAppLaunchEnded
+ __OBJC_METACLASS_RO_$_SISchemaUEIResponseAppLaunchFailed
+ __OBJC_METACLASS_RO_$_SISchemaUEIResponseAppLaunchStarted
+ _symbolic _____ So015RISessionSchemaA17CommunicationTypeV
+ _symbolic _____ So27RISchemaRICommunicationTypeV
+ _symbolic _____ So31ORCHSchemaORCHIdentityAggressorV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So20SISchemaAnyEventTypeV
CStrings:
+ "COMPONENTNAME_RI"
+ "COMPONENTNAME_RISESSION"
+ "DISMISSALREASON_ACTIVE_USER_CHANGED"
+ "IEROUTING_REMOTE_INTELLIGENCE"
+ "INFERENCEPROJECTINTENT_HOMEACCESSORY_AUDIO_APP_SELECTION"
+ "INVOCATIONSOURCE_PULL_DOWN_GESTURE"
+ "ORCHIDENTITYAGGRESSOR_AUTOMATIC_RECOGNITION_DISABLED"
+ "ORCHIDENTITYAGGRESSOR_DISTANCE"
+ "ORCHIDENTITYAGGRESSOR_FACE_COVERING"
+ "ORCHIDENTITYAGGRESSOR_LOW_LIGHT"
+ "ORCHIDENTITYAGGRESSOR_MOTION"
+ "ORCHIDENTITYAGGRESSOR_NO_RECENT_EMBEDDINGS"
+ "ORCHIDENTITYAGGRESSOR_OCCLUSION"
+ "ORCHIDENTITYAGGRESSOR_POSE"
+ "ORCHIDENTITYAGGRESSOR_SPOOF_ATTEMPT"
+ "ORCHIDENTITYAGGRESSOR_UNKNOWN"
+ "PLANNERUSERIDENTITYCHECKOUTCOME_UNRECOGNIZED_SPEAKER_ON_HOME_ACCESSORY"
+ "PLANNERUSERIDENTITYCHECKOUTCOME_VISUAL_IDENTITY_REQUIRED"
+ "RICOMMUNICATIONTYPE_ACK_RECEIVED"
+ "RICOMMUNICATIONTYPE_REQUEST_SENT"
+ "RICOMMUNICATIONTYPE_UNKNOWN"
+ "RISESSIONCOMMUNICATIONTYPE_ACK_RECEIVED"
+ "RISESSIONCOMMUNICATIONTYPE_REQUEST_SENT"
+ "RISESSIONCOMMUNICATIONTYPE_UNKNOWN"
+ "RISESSION_CLIENT_EVENT"
+ "RI_CLIENT_EVENT"
+ "TVREMOTETYPE_SIRI_REMOTE_2026"
+ "com.apple.aiml.siri.ri.RIClientEvent"
+ "com.apple.aiml.siri.ri.RIClientEvent.RIRemoteContext"
+ "com.apple.aiml.siri.ri.RIClientEvent.RISourceContext"
+ "com.apple.aiml.siri.risession.RISessionClientEvent"
+ "com.apple.aiml.siri.risession.RISessionClientEvent.RISessionRemoteContext"
+ "com.apple.aiml.siri.risession.RISessionClientEvent.RISessionSourceContext"
+ "com.apple.aiml.siri.uei.ClientEvent.UEIResponseAppLaunchContext"
+ "identityAggressors"
+ "isRecentlySeen"
+ "remoteContext"
+ "remoteSessionContext"
+ "remoteTimeInMs"
+ "riId"
+ "riSessionId"
+ "roundTripCount"
+ "sourceContext"
+ "sourceSessionContext"
+ "ueiResponseAppLaunchContext"
```
