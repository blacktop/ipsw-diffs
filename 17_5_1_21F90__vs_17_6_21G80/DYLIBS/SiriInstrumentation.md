## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`

```diff

-3305.16.1.0.0
-  __TEXT.__text: 0x67dc84
+3306.9.1.0.0
+  __TEXT.__text: 0x682b50
   __TEXT.__auth_stubs: 0xfc0
-  __TEXT.__objc_methlist: 0x8fd58
-  __TEXT.__const: 0xb064
-  __TEXT.__constg_swiftt: 0x4870
-  __TEXT.__swift5_typeref: 0x11c2
-  __TEXT.__swift5_builtin: 0x2990
+  __TEXT.__objc_methlist: 0x90390
+  __TEXT.__const: 0xb224
+  __TEXT.__constg_swiftt: 0x4910
+  __TEXT.__swift5_typeref: 0x11e0
+  __TEXT.__swift5_builtin: 0x29f4
   __TEXT.__swift5_reflstr: 0x192
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_proto: 0x8d0
-  __TEXT.__swift5_types: 0x890
-  __TEXT.__cstring: 0x45dbc
+  __TEXT.__swift5_proto: 0x8e4
+  __TEXT.__swift5_types: 0x8a4
+  __TEXT.__cstring: 0x46429
   __TEXT.__swift5_fieldmd: 0x2e8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x1d8f0
+  __TEXT.__unwind_info: 0x1da5c
   __TEXT.__eh_frame: 0x6f0
-  __TEXT.__objc_classname: 0xeaf7
-  __TEXT.__objc_methname: 0xcf09e
-  __TEXT.__objc_methtype: 0x1d0a6
-  __TEXT.__objc_stubs: 0x4bda0
+  __TEXT.__objc_classname: 0xebed
+  __TEXT.__objc_methname: 0xcfa3d
+  __TEXT.__objc_methtype: 0x1d25e
+  __TEXT.__objc_stubs: 0x4c020
   __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x267e8
-  __DATA_CONST.__objc_classlist: 0x3390
+  __DATA_CONST.__const: 0x26cb0
+  __DATA_CONST.__objc_classlist: 0x33b8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa3f10
-  __DATA_CONST.__objc_selrefs: 0x27d88
+  __DATA_CONST.__objc_const: 0xa46a8
+  __DATA_CONST.__objc_selrefs: 0x27ef0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x3338
-  __DATA_CONST.__objc_superrefs: 0x4e80
-  __AUTH_CONST.__const: 0xb70
-  __AUTH_CONST.__cfstring: 0x4dd00
+  __DATA_CONST.__objc_classrefs: 0x3360
+  __DATA_CONST.__objc_superrefs: 0x4eb0
+  __AUTH_CONST.__const: 0xc10
+  __AUTH_CONST.__cfstring: 0x4e1c0
   __AUTH_CONST.__auth_ptr: 0x58
-  __AUTH_CONST.__objc_const: 0x2c20
+  __AUTH_CONST.__objc_const: 0x2d88
   __AUTH_CONST.__objc_intobj: 0xa38
   __AUTH_CONST.__auth_got: 0x7e8
-  __AUTH.__objc_data: 0x2a30
-  __DATA.__objc_ivar: 0x9978
-  __DATA.__data: 0x17d0
-  __DATA.__bss: 0x11600
+  __AUTH.__objc_data: 0x2bc0
+  __DATA.__objc_ivar: 0x99e8
+  __DATA.__data: 0x17f8
+  __DATA.__bss: 0x11880
   __DATA.__common: 0x20
   __DATA_DIRTY.__const: 0x40d8
   __DATA_DIRTY.__objc_const: 0x1ba58

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 52092
-  Symbols:   129774
-  CStrings:  46158
+  Functions: 52244
+  Symbols:   130129
+  CStrings:  46282
 
Symbols:
+ -[FLOWSchemaFLOWClientEvent deleteLocationAccessPermissionPromptContext]
+ -[FLOWSchemaFLOWClientEvent hasLocationAccessPermissionPromptContext]
+ -[FLOWSchemaFLOWClientEvent locationAccessPermissionPromptContext]
+ -[FLOWSchemaFLOWClientEvent setHasLocationAccessPermissionPromptContext:]
+ -[FLOWSchemaFLOWClientEvent setLocationAccessPermissionPromptContext:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext .cxx_destruct]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext deleteEnded]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext deleteFailed]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext deleteStartedOrChanged]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext dictionaryRepresentation]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext ended]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext failed]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext hasEnded]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext hasFailed]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext hasStartedOrChanged]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext hash]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext initWithDictionary:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext initWithJSON:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext isEqual:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext jsonData]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext readFrom:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext setEnded:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext setFailed:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext setHasEnded:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext setHasFailed:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext setHasStartedOrChanged:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext setStartedOrChanged:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext startedOrChanged]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext whichContextevent]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext writeTo:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded deleteIsPreciseLocationResult]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded deletePermissionStatusResult]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded dictionaryRepresentation]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded hasIsPreciseLocationResult]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded hasPermissionStatusResult]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded hash]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded initWithDictionary:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded initWithJSON:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded isEqual:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded isPreciseLocationResult]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded jsonData]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded permissionStatusResult]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded readFrom:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded setHasIsPreciseLocationResult:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded setHasPermissionStatusResult:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded setIsPreciseLocationResult:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded setPermissionStatusResult:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded writeTo:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded(SensitiveConditions) suppressMessageUnderConditions]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed deleteFailureReason]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed dictionaryRepresentation]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed failureReason]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed hasFailureReason]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed hash]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed initWithDictionary:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed initWithJSON:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed isEqual:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed jsonData]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed readFrom:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed setFailureReason:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed setHasFailureReason:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed writeTo:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed(SensitiveConditions) suppressMessageUnderConditions]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted deleteExists]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted dictionaryRepresentation]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted exists]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted hasExists]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted hash]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted initWithDictionary:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted initWithJSON:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted isEqual:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted jsonData]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted readFrom:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted setExists:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted setHasExists:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted writeTo:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted(SensitiveConditions) suppressMessageUnderConditions]
+ -[MHSchemaMHClientEvent deleteVoiceProfileICloudSyncFinished]
+ -[MHSchemaMHClientEvent hasVoiceProfileICloudSyncFinished]
+ -[MHSchemaMHClientEvent setHasVoiceProfileICloudSyncFinished:]
+ -[MHSchemaMHClientEvent setVoiceProfileICloudSyncFinished:]
+ -[MHSchemaMHClientEvent voiceProfileICloudSyncFinished]
+ -[MHSchemaMHClientEvent(IsolationLevel) clockIsolationLevel]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished .cxx_destruct]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished deleteEnrollmentId]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished deleteIsVoiceProfileSyncSuccess]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished deleteLocale]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished deleteVoiceProfileSyncFailureReason]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished dictionaryRepresentation]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished enrollmentId]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished hasEnrollmentId]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished hasIsVoiceProfileSyncSuccess]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished hasLocale]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished hasVoiceProfileSyncFailureReason]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished hash]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished initWithDictionary:]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished initWithJSON:]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished isEqual:]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished isVoiceProfileSyncSuccess]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished jsonData]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished locale]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished readFrom:]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished setEnrollmentId:]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished setHasEnrollmentId:]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished setHasIsVoiceProfileSyncSuccess:]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished setHasLocale:]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished setHasVoiceProfileSyncFailureReason:]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished setIsVoiceProfileSyncSuccess:]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished setLocale:]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished setVoiceProfileSyncFailureReason:]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished voiceProfileSyncFailureReason]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished writeTo:]
+ -[MHSchemaMHVoiceProfileICloudSyncFinished(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantProperties deleteLocationAccessPermission]
+ -[ODDSiriSchemaODDAssistantProperties hasLocationAccessPermission]
+ -[ODDSiriSchemaODDAssistantProperties locationAccessPermission]
+ -[ODDSiriSchemaODDAssistantProperties setHasLocationAccessPermission:]
+ -[ODDSiriSchemaODDAssistantProperties setLocationAccessPermission:]
+ -[POMMESSchemaPOMMESRequestResult deletePegasusPromptType]
+ -[POMMESSchemaPOMMESRequestResult hasPegasusPromptType]
+ -[POMMESSchemaPOMMESRequestResult pegasusPromptType]
+ -[POMMESSchemaPOMMESRequestResult setHasPegasusPromptType:]
+ -[POMMESSchemaPOMMESRequestResult setPegasusPromptType:]
+ -[SISchemaEnabledStatus deleteLocationAccessPermission]
+ -[SISchemaEnabledStatus hasLocationAccessPermission]
+ -[SISchemaEnabledStatus locationAccessPermission]
+ -[SISchemaEnabledStatus setHasLocationAccessPermission:]
+ -[SISchemaEnabledStatus setLocationAccessPermission:]
+ OBJC_IVAR_$_FLOWSchemaFLOWClientEvent._locationAccessPermissionPromptContext
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext._ended
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext._failed
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext._startedOrChanged
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptEnded._has
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptEnded._isPreciseLocationResult
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptEnded._permissionStatusResult
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptFailed._failureReason
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptFailed._has
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptStarted._exists
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptStarted._has
+ OBJC_IVAR_$_MHSchemaMHClientEvent._voiceProfileICloudSyncFinished
+ OBJC_IVAR_$_MHSchemaMHVoiceProfileICloudSyncFinished._enrollmentId
+ OBJC_IVAR_$_MHSchemaMHVoiceProfileICloudSyncFinished._has
+ OBJC_IVAR_$_MHSchemaMHVoiceProfileICloudSyncFinished._isVoiceProfileSyncSuccess
+ OBJC_IVAR_$_MHSchemaMHVoiceProfileICloudSyncFinished._locale
+ OBJC_IVAR_$_MHSchemaMHVoiceProfileICloudSyncFinished._voiceProfileSyncFailureReason
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantProperties._locationAccessPermission
+ OBJC_IVAR_$_POMMESSchemaPOMMESRequestResult._pegasusPromptType
+ OBJC_IVAR_$_SISchemaEnabledStatus._locationAccessPermission
+ _FLOWSchemaFLOWLocationAccessPermissionPromptContextReadFrom
+ _FLOWSchemaFLOWLocationAccessPermissionPromptEndedReadFrom
+ _FLOWSchemaFLOWLocationAccessPermissionPromptFailedReadFrom
+ _FLOWSchemaFLOWLocationAccessPermissionPromptStartedReadFrom
+ _MHSchemaMHVoiceProfileICloudSyncFinishedReadFrom
+ _OBJC_CLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext
+ _OBJC_CLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptEnded
+ _OBJC_CLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptFailed
+ _OBJC_CLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptStarted
+ _OBJC_CLASS_$_MHSchemaMHVoiceProfileICloudSyncFinished
+ _OBJC_IVAR_$_FLOWSchemaFLOWClientEvent._hasLocationAccessPermissionPromptContext
+ _OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext._hasEnded
+ _OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext._hasFailed
+ _OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext._hasStartedOrChanged
+ _OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext._whichContextevent
+ _OBJC_IVAR_$_MHSchemaMHClientEvent._hasVoiceProfileICloudSyncFinished
+ _OBJC_IVAR_$_MHSchemaMHVoiceProfileICloudSyncFinished._hasEnrollmentId
+ _OBJC_IVAR_$_MHSchemaMHVoiceProfileICloudSyncFinished._hasVoiceProfileSyncFailureReason
+ _OBJC_METACLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext
+ _OBJC_METACLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptEnded
+ _OBJC_METACLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptFailed
+ _OBJC_METACLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptStarted
+ _OBJC_METACLASS_$_MHSchemaMHVoiceProfileICloudSyncFinished
+ __OBJC_$_CLASS_METHODS_MHSchemaMHClientEvent(Component|SensitiveConditions|InnerEventContainer|IsolationLevel|InstrumentationAdditions)
+ __OBJC_$_INSTANCE_METHODS_FLOWSchemaFLOWLocationAccessPermissionPromptContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_FLOWSchemaFLOWLocationAccessPermissionPromptEnded(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_FLOWSchemaFLOWLocationAccessPermissionPromptFailed(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_FLOWSchemaFLOWLocationAccessPermissionPromptStarted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_MHSchemaMHClientEvent(Component|SensitiveConditions|InnerEventContainer|IsolationLevel|InstrumentationAdditions)
+ __OBJC_$_INSTANCE_METHODS_MHSchemaMHVoiceProfileICloudSyncFinished(SensitiveConditions)
+ __OBJC_$_INSTANCE_VARIABLES_FLOWSchemaFLOWLocationAccessPermissionPromptContext
+ __OBJC_$_INSTANCE_VARIABLES_FLOWSchemaFLOWLocationAccessPermissionPromptEnded
+ __OBJC_$_INSTANCE_VARIABLES_FLOWSchemaFLOWLocationAccessPermissionPromptFailed
+ __OBJC_$_INSTANCE_VARIABLES_FLOWSchemaFLOWLocationAccessPermissionPromptStarted
+ __OBJC_$_INSTANCE_VARIABLES_MHSchemaMHVoiceProfileICloudSyncFinished
+ __OBJC_$_PROP_LIST_FLOWSchemaFLOWLocationAccessPermissionPromptContext
+ __OBJC_$_PROP_LIST_FLOWSchemaFLOWLocationAccessPermissionPromptEnded
+ __OBJC_$_PROP_LIST_FLOWSchemaFLOWLocationAccessPermissionPromptFailed
+ __OBJC_$_PROP_LIST_FLOWSchemaFLOWLocationAccessPermissionPromptStarted
+ __OBJC_$_PROP_LIST_MHSchemaMHVoiceProfileICloudSyncFinished
+ __OBJC_CLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext
+ __OBJC_CLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptEnded
+ __OBJC_CLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptFailed
+ __OBJC_CLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptStarted
+ __OBJC_CLASS_RO_$_MHSchemaMHVoiceProfileICloudSyncFinished
+ __OBJC_METACLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext
+ __OBJC_METACLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptEnded
+ __OBJC_METACLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptFailed
+ __OBJC_METACLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptStarted
+ __OBJC_METACLASS_RO_$_MHSchemaMHVoiceProfileICloudSyncFinished
+ _objc_msgSend$deleteLocationAccessPermissionPromptContext
+ _objc_msgSend$deleteVoiceProfileICloudSyncFinished
+ _objc_msgSend$enrollmentId
+ _objc_msgSend$isPreciseLocationResult
+ _objc_msgSend$isVoiceProfileSyncSuccess
+ _objc_msgSend$locationAccessPermission
+ _objc_msgSend$locationAccessPermissionPromptContext
+ _objc_msgSend$pegasusPromptType
+ _objc_msgSend$permissionStatusResult
+ _objc_msgSend$setEnrollmentId:
+ _objc_msgSend$setIsPreciseLocationResult:
+ _objc_msgSend$setIsVoiceProfileSyncSuccess:
+ _objc_msgSend$setLocationAccessPermission:
+ _objc_msgSend$setLocationAccessPermissionPromptContext:
+ _objc_msgSend$setPegasusPromptType:
+ _objc_msgSend$setPermissionStatusResult:
+ _objc_msgSend$setVoiceProfileICloudSyncFinished:
+ _objc_msgSend$setVoiceProfileSyncFailureReason:
+ _objc_msgSend$voiceProfileICloudSyncFinished
+ _objc_msgSend$voiceProfileSyncFailureReason
+ _qname_FLOWSchemaFLOWClientEvent_WhichEvent_Type_locationAccessPermissionPromptContext
+ _qname_MHSchemaMHClientEvent_WhichEvent_Type_voiceProfileICloudSyncFinished
+ _symbolic _____ So32SISchemaLocationAccessPermissionV
+ _symbolic _____ So35POMMESSchemaPOMMESPegasusPromptTypeV
+ _symbolic _____ So40ODDSiriSchemaODDLocationAccessPermissionV
+ _symbolic _____ So50FLOWSchemaFLOWLocationAccessPermissionStatusResultV
+ _symbolic _____ So51FLOWSchemaFLOWLocationAccessPermissionFailureReasonV
- __OBJC_$_CLASS_METHODS_MHSchemaMHClientEvent(Component|SensitiveConditions|InnerEventContainer|InstrumentationAdditions)
- __OBJC_$_INSTANCE_METHODS_MHSchemaMHClientEvent(Component|SensitiveConditions|InnerEventContainer|InstrumentationAdditions)
CStrings:
+ "\x0f\x0f\x0f\x0e"
+ "@\"FLOWSchemaFLOWLocationAccessPermissionPromptContext\""
+ "@\"FLOWSchemaFLOWLocationAccessPermissionPromptEnded\""
+ "@\"FLOWSchemaFLOWLocationAccessPermissionPromptFailed\""
+ "@\"FLOWSchemaFLOWLocationAccessPermissionPromptStarted\""
+ "@\"MHSchemaMHVoiceProfileICloudSyncFinished\""
+ "FLOWLOCATIONACCESSPERMISSIONFAILUREREASON_DISABLED_LOCATION_SERVICE"
+ "FLOWLOCATIONACCESSPERMISSIONFAILUREREASON_INSUFFICIENT_PRECISION"
+ "FLOWLOCATIONACCESSPERMISSIONFAILUREREASON_LOCKED_DEVICE"
+ "FLOWLOCATIONACCESSPERMISSIONFAILUREREASON_TIMEOUT"
+ "FLOWLOCATIONACCESSPERMISSIONFAILUREREASON_UNKNOWN"
+ "FLOWLOCATIONACCESSPERMISSIONFAILUREREASON_UNSUPPORTED_RESPONSE"
+ "FLOWLOCATIONACCESSPERMISSIONSTATUSRESULT_ALLOW_ONCE"
+ "FLOWLOCATIONACCESSPERMISSIONSTATUSRESULT_ALLOW_WHILE_USING_SIRI"
+ "FLOWLOCATIONACCESSPERMISSIONSTATUSRESULT_NEVER"
+ "FLOWLOCATIONACCESSPERMISSIONSTATUSRESULT_UNKNOWN"
+ "FLOWSchemaFLOWLocationAccessPermissionPromptContext"
+ "FLOWSchemaFLOWLocationAccessPermissionPromptEnded"
+ "FLOWSchemaFLOWLocationAccessPermissionPromptFailed"
+ "FLOWSchemaFLOWLocationAccessPermissionPromptStarted"
+ "LOCATIONACCESSPERMISSION_ALLOW_ALWAYS"
+ "LOCATIONACCESSPERMISSION_ALLOW_WHILE_USING_SIRI"
+ "LOCATIONACCESSPERMISSION_ASK_NEXT_TIME"
+ "LOCATIONACCESSPERMISSION_DENIED"
+ "LOCATIONACCESSPERMISSION_LOCATION_SERVICES_OFF"
+ "LOCATIONACCESSPERMISSION_RESTRICTED"
+ "LOCATIONACCESSPERMISSION_UNKNOWN"
+ "MHSchemaMHVoiceProfileICloudSyncFinished"
+ "ODDLOCATIONACCESSPERMISSION_ALLOW_ALWAYS"
+ "ODDLOCATIONACCESSPERMISSION_ALLOW_WHILE_USING_SIRI"
+ "ODDLOCATIONACCESSPERMISSION_ASK_NEXT_TIME"
+ "ODDLOCATIONACCESSPERMISSION_DENIED"
+ "ODDLOCATIONACCESSPERMISSION_LOCATION_SERVICES_OFF"
+ "ODDLOCATIONACCESSPERMISSION_RESTRICTED"
+ "ODDLOCATIONACCESSPERMISSION_UNKNOWN"
+ "POMMESPEGASUSPROMPTTYPE_SHARE_DEVICE_LOCATION"
+ "POMMESPEGASUSPROMPTTYPE_SHARE_PRECISE_DEVICE_LOCATION"
+ "POMMESPEGASUSPROMPTTYPE_UNKNOWN"
+ "T@\"FLOWSchemaFLOWLocationAccessPermissionPromptContext\",&,N,V_locationAccessPermissionPromptContext"
+ "T@\"FLOWSchemaFLOWLocationAccessPermissionPromptEnded\",&,N,V_ended"
+ "T@\"FLOWSchemaFLOWLocationAccessPermissionPromptFailed\",&,N,V_failed"
+ "T@\"FLOWSchemaFLOWLocationAccessPermissionPromptStarted\",&,N,V_startedOrChanged"
+ "T@\"MHSchemaMHVoiceProfileICloudSyncFinished\",&,N,V_voiceProfileICloudSyncFinished"
+ "T@\"NSString\",C,N,V_enrollmentId"
+ "T@\"NSString\",C,N,V_voiceProfileSyncFailureReason"
+ "TB,N,V_hasEnrollmentId"
+ "TB,N,V_hasLocationAccessPermissionPromptContext"
+ "TB,N,V_hasVoiceProfileICloudSyncFinished"
+ "TB,N,V_hasVoiceProfileSyncFailureReason"
+ "TB,N,V_isPreciseLocationResult"
+ "TB,N,V_isVoiceProfileSyncSuccess"
+ "Ti,N,V_locationAccessPermission"
+ "Ti,N,V_pegasusPromptType"
+ "Ti,N,V_permissionStatusResult"
+ "_enrollmentId"
+ "_hasEnrollmentId"
+ "_hasLocationAccessPermissionPromptContext"
+ "_hasVoiceProfileICloudSyncFinished"
+ "_hasVoiceProfileSyncFailureReason"
+ "_isPreciseLocationResult"
+ "_isVoiceProfileSyncSuccess"
+ "_locationAccessPermission"
+ "_locationAccessPermissionPromptContext"
+ "_pegasusPromptType"
+ "_permissionStatusResult"
+ "_voiceProfileICloudSyncFinished"
+ "_voiceProfileSyncFailureReason"
+ "com.apple.aiml.siri.flow.FLOWClientEvent.FLOWLocationAccessPermissionPromptContext"
+ "com.apple.aiml.siri.mh.MHClientEvent.MHVoiceProfileICloudSyncFinished"
+ "deleteEnrollmentId"
+ "deleteIsPreciseLocationResult"
+ "deleteIsVoiceProfileSyncSuccess"
+ "deleteLocationAccessPermission"
+ "deleteLocationAccessPermissionPromptContext"
+ "deletePegasusPromptType"
+ "deletePermissionStatusResult"
+ "deleteVoiceProfileICloudSyncFinished"
+ "deleteVoiceProfileSyncFailureReason"
+ "enrollmentId"
+ "hasEnrollmentId"
+ "hasIsPreciseLocationResult"
+ "hasIsVoiceProfileSyncSuccess"
+ "hasLocationAccessPermission"
+ "hasLocationAccessPermissionPromptContext"
+ "hasPegasusPromptType"
+ "hasPermissionStatusResult"
+ "hasVoiceProfileICloudSyncFinished"
+ "hasVoiceProfileSyncFailureReason"
+ "isPreciseLocationResult"
+ "isVoiceProfileSyncSuccess"
+ "locationAccessPermission"
+ "locationAccessPermissionPromptContext"
+ "pegasusPromptType"
+ "permissionStatusResult"
+ "setEnrollmentId:"
+ "setHasEnrollmentId:"
+ "setHasIsPreciseLocationResult:"
+ "setHasIsVoiceProfileSyncSuccess:"
+ "setHasLocationAccessPermission:"
+ "setHasLocationAccessPermissionPromptContext:"
+ "setHasPegasusPromptType:"
+ "setHasPermissionStatusResult:"
+ "setHasVoiceProfileICloudSyncFinished:"
+ "setHasVoiceProfileSyncFailureReason:"
+ "setIsPreciseLocationResult:"
+ "setIsVoiceProfileSyncSuccess:"
+ "setLocationAccessPermission:"
+ "setLocationAccessPermissionPromptContext:"
+ "setPegasusPromptType:"
+ "setPermissionStatusResult:"
+ "setVoiceProfileICloudSyncFinished:"
+ "setVoiceProfileSyncFailureReason:"
+ "voiceProfileICloudSyncFinished"
+ "voiceProfileSyncFailureReason"
+ "{?=\"assistantEnabled\"b1\"dictationEnabled\"b1\"hardwareButtonEnabled\"b1\"heySiriEnabled\"b1\"assistantOnLockscreen\"b1\"raiseToSpeakEnabled\"b1\"spokenNotificationsEnabled\"b1\"hasHomekitHome\"b1\"shortcutsAvailable\"b1\"dataSharingOptInStatus\"b1\"typeToSiriEnabled\"b1\"isPreciseLocationEnabled\"b1\"voiceFeedback\"b1\"isAdaptiveVolumeEnabled\"b1\"isRemoteDarwinHeySiriEnabled\"b1\"isAutoPunctuationEnabled\"b1\"isHSHangupEnabled\"b1\"isSiriInCallEnabled\"b1\"hsHangupEnablementState\"b1\"siriInCallEnablementState\"b1\"isAlwaysShowSiriCaptionsEnabled\"b1\"isAlwaysShowSpeechEnabled\"b1\"isShowAppsBehindSiriEnabled\"b1\"siriSpeechRate\"b1\"isVoiceOverEnabled\"b1\"isShowAppsBehindSiriEnabledOnCarPlay\"b1\"isSiriCapableDigitalCarKeyAvailable\"b1\"isAlwaysListenForHeySiriEnabled\"b1\"siriPauseTimeState\"b1\"isMteUploadEnabled\"b1\"isServerUserDataSyncEnabled\"b1\"locationAccessPermission\"b1}"
+ "{?=\"isAssistantEnabled\"b1\"listenFor\"b1\"numSiriShortcutsEnabled\"b1\"isPreciseLocationEnabled\"b1\"locationAccessPermission\"b1}"
+ "{?=\"isVoiceProfileSyncSuccess\"b1\"locale\"b1}"
+ "{?=\"permissionStatusResult\"b1\"isPreciseLocationResult\"b1}"
+ "{?=\"pommesConfidenceScore\"b1\"isFromResponseCache\"b1\"pegasusPromptType\"b1}"
- "\x0f\x0f\x0f\r"
- "{?=\"assistantEnabled\"b1\"dictationEnabled\"b1\"hardwareButtonEnabled\"b1\"heySiriEnabled\"b1\"assistantOnLockscreen\"b1\"raiseToSpeakEnabled\"b1\"spokenNotificationsEnabled\"b1\"hasHomekitHome\"b1\"shortcutsAvailable\"b1\"dataSharingOptInStatus\"b1\"typeToSiriEnabled\"b1\"isPreciseLocationEnabled\"b1\"voiceFeedback\"b1\"isAdaptiveVolumeEnabled\"b1\"isRemoteDarwinHeySiriEnabled\"b1\"isAutoPunctuationEnabled\"b1\"isHSHangupEnabled\"b1\"isSiriInCallEnabled\"b1\"hsHangupEnablementState\"b1\"siriInCallEnablementState\"b1\"isAlwaysShowSiriCaptionsEnabled\"b1\"isAlwaysShowSpeechEnabled\"b1\"isShowAppsBehindSiriEnabled\"b1\"siriSpeechRate\"b1\"isVoiceOverEnabled\"b1\"isShowAppsBehindSiriEnabledOnCarPlay\"b1\"isSiriCapableDigitalCarKeyAvailable\"b1\"isAlwaysListenForHeySiriEnabled\"b1\"siriPauseTimeState\"b1\"isMteUploadEnabled\"b1\"isServerUserDataSyncEnabled\"b1}"
- "{?=\"isAssistantEnabled\"b1\"listenFor\"b1\"numSiriShortcutsEnabled\"b1\"isPreciseLocationEnabled\"b1}"
- "{?=\"pommesConfidenceScore\"b1\"isFromResponseCache\"b1}"

```
