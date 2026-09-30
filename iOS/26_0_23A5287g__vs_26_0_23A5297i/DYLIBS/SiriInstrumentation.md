## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`

```diff

-3500.100.1.0.0
-  __TEXT.__text: 0x9fc994
+3500.105.1.0.0
+  __TEXT.__text: 0xa09c0c
   __TEXT.__auth_stubs: 0x1090
-  __TEXT.__objc_methlist: 0xd0fe4
-  __TEXT.__const: 0x11ab4
-  __TEXT.__cstring: 0x78a95
-  __TEXT.__constg_swiftt: 0x6320
-  __TEXT.__swift5_typeref: 0x1894
-  __TEXT.__swift5_builtin: 0x396c
+  __TEXT.__objc_methlist: 0xd225c
+  __TEXT.__const: 0x11c64
+  __TEXT.__cstring: 0x790c6
+  __TEXT.__constg_swiftt: 0x63c0
+  __TEXT.__swift5_typeref: 0x18b2
+  __TEXT.__swift5_builtin: 0x39d0
   __TEXT.__swift5_reflstr: 0x212
   __TEXT.__swift5_assocty: 0x120
-  __TEXT.__swift5_proto: 0xec4
-  __TEXT.__swift5_types: 0xbcc
+  __TEXT.__swift5_proto: 0xedc
+  __TEXT.__swift5_types: 0xbe0
   __TEXT.__swift5_fieldmd: 0x3e8
   __TEXT.__oslogstring: 0x95
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x29d00
+  __TEXT.__unwind_info: 0x2a0a0
   __TEXT.__eh_frame: 0x23a8
-  __TEXT.__objc_classname: 0x1584f
-  __TEXT.__objc_methname: 0x120976
-  __TEXT.__objc_methtype: 0x28015
-  __TEXT.__objc_stubs: 0x68ec0
-  __DATA_CONST.__got: 0x4c90
-  __DATA_CONST.__const: 0x349c0
-  __DATA_CONST.__objc_classlist: 0x4b70
+  __TEXT.__objc_classname: 0x159a8
+  __TEXT.__objc_methname: 0x121560
+  __TEXT.__objc_methtype: 0x282eb
+  __TEXT.__objc_stubs: 0x693e0
+  __DATA_CONST.__got: 0x4ce8
+  __DATA_CONST.__const: 0x34ce0
+  __DATA_CONST.__objc_classlist: 0x4bc8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x36478
+  __DATA_CONST.__objc_selrefs: 0x366e8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x7518
+  __DATA_CONST.__objc_superrefs: 0x75d0
   __AUTH_CONST.__auth_got: 0x850
-  __AUTH_CONST.__const: 0x21198
-  __AUTH_CONST.__cfstring: 0x68e00
-  __AUTH_CONST.__objc_const: 0x11b2b0
+  __AUTH_CONST.__const: 0x212d8
+  __AUTH_CONST.__cfstring: 0x69480
+  __AUTH_CONST.__objc_const: 0x11cb30
   __AUTH_CONST.__objc_intobj: 0xb70
-  __AUTH.__objc_data: 0x11558
-  __DATA.__objc_ivar: 0xe15c
-  __DATA.__data: 0x1ff0
-  __DATA.__bss: 0x18800
+  __AUTH.__objc_data: 0x118c8
+  __DATA.__objc_ivar: 0xe2ac
+  __DATA.__data: 0x2020
+  __DATA.__bss: 0x18a80
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x1df58
   __DATA_DIRTY.__data: 0x590

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: DDC863BF-95D5-3E88-9D74-EE468C215FE4
-  Functions: 75643
-  Symbols:   188249
-  CStrings:  77494
+  UUID: AB89A993-91EF-3EF8-8140-C6DBB3292274
+  Functions: 76059
+  Symbols:   189244
+  CStrings:  77757
 
Symbols:
+ +[ASVSchemaASVClientEvent(Component) joinability]
+ +[ASVSchemaASVClientEvent(InnerEventContainer) getInnerTypeStringByTag:]
+ -[ASVSchemaASVClientEvent .cxx_destruct]
+ -[ASVSchemaASVClientEvent asvOutputVolumeQueried]
+ -[ASVSchemaASVClientEvent asvUserIntentDetected]
+ -[ASVSchemaASVClientEvent deleteAsvOutputVolumeQueried]
+ -[ASVSchemaASVClientEvent deleteAsvUserIntentDetected]
+ -[ASVSchemaASVClientEvent deleteEventMetadata]
+ -[ASVSchemaASVClientEvent dictionaryRepresentation]
+ -[ASVSchemaASVClientEvent eventMetadata]
+ -[ASVSchemaASVClientEvent hasAsvOutputVolumeQueried]
+ -[ASVSchemaASVClientEvent hasAsvUserIntentDetected]
+ -[ASVSchemaASVClientEvent hasEventMetadata]
+ -[ASVSchemaASVClientEvent hash]
+ -[ASVSchemaASVClientEvent initWithDictionary:]
+ -[ASVSchemaASVClientEvent initWithJSON:]
+ -[ASVSchemaASVClientEvent isEqual:]
+ -[ASVSchemaASVClientEvent jsonData]
+ -[ASVSchemaASVClientEvent qualifiedMessageName]
+ -[ASVSchemaASVClientEvent readFrom:]
+ -[ASVSchemaASVClientEvent setAsvOutputVolumeQueried:]
+ -[ASVSchemaASVClientEvent setAsvUserIntentDetected:]
+ -[ASVSchemaASVClientEvent setEventMetadata:]
+ -[ASVSchemaASVClientEvent setHasAsvOutputVolumeQueried:]
+ -[ASVSchemaASVClientEvent setHasAsvUserIntentDetected:]
+ -[ASVSchemaASVClientEvent setHasEventMetadata:]
+ -[ASVSchemaASVClientEvent whichEvent_Type]
+ -[ASVSchemaASVClientEvent writeTo:]
+ -[ASVSchemaASVClientEvent(Component) componentName]
+ -[ASVSchemaASVClientEvent(Component) getComponentId]
+ -[ASVSchemaASVClientEvent(InnerEventContainer) innerEvent]
+ -[ASVSchemaASVClientEvent(InnerEventContainer) whichInnerEventType]
+ -[ASVSchemaASVClientEvent(InstrumentationAdditions) getAnyEventType]
+ -[ASVSchemaASVClientEvent(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ASVSchemaASVClientEvent(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASVSchemaASVClientEventMetadata .cxx_destruct]
+ -[ASVSchemaASVClientEventMetadata asvId]
+ -[ASVSchemaASVClientEventMetadata deleteAsvId]
+ -[ASVSchemaASVClientEventMetadata dictionaryRepresentation]
+ -[ASVSchemaASVClientEventMetadata hasAsvId]
+ -[ASVSchemaASVClientEventMetadata hash]
+ -[ASVSchemaASVClientEventMetadata initWithDictionary:]
+ -[ASVSchemaASVClientEventMetadata initWithJSON:]
+ -[ASVSchemaASVClientEventMetadata isEqual:]
+ -[ASVSchemaASVClientEventMetadata jsonData]
+ -[ASVSchemaASVClientEventMetadata readFrom:]
+ -[ASVSchemaASVClientEventMetadata setAsvId:]
+ -[ASVSchemaASVClientEventMetadata setHasAsvId:]
+ -[ASVSchemaASVClientEventMetadata writeTo:]
+ -[ASVSchemaASVClientEventMetadata(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ASVSchemaASVClientEventMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASVSchemaASVOutputVolumeQueried backgroundNoiseActivityLevel]
+ -[ASVSchemaASVOutputVolumeQueried backgroundNoiseLevel]
+ -[ASVSchemaASVOutputVolumeQueried deleteBackgroundNoiseActivityLevel]
+ -[ASVSchemaASVOutputVolumeQueried deleteBackgroundNoiseLevel]
+ -[ASVSchemaASVOutputVolumeQueried deleteInvocationType]
+ -[ASVSchemaASVOutputVolumeQueried deleteIsMediaPlaybackOn]
+ -[ASVSchemaASVOutputVolumeQueried deleteIsPermanentOffsetEnabled]
+ -[ASVSchemaASVOutputVolumeQueried deleteMusicLoudnessLevel]
+ -[ASVSchemaASVOutputVolumeQueried deleteOutputVolume]
+ -[ASVSchemaASVOutputVolumeQueried deletePermanentOffsetFactor]
+ -[ASVSchemaASVOutputVolumeQueried deleteSpeakerDistance]
+ -[ASVSchemaASVOutputVolumeQueried deleteSpeakerSpeechLevel]
+ -[ASVSchemaASVOutputVolumeQueried dictionaryRepresentation]
+ -[ASVSchemaASVOutputVolumeQueried hasBackgroundNoiseActivityLevel]
+ -[ASVSchemaASVOutputVolumeQueried hasBackgroundNoiseLevel]
+ -[ASVSchemaASVOutputVolumeQueried hasInvocationType]
+ -[ASVSchemaASVOutputVolumeQueried hasIsMediaPlaybackOn]
+ -[ASVSchemaASVOutputVolumeQueried hasIsPermanentOffsetEnabled]
+ -[ASVSchemaASVOutputVolumeQueried hasMusicLoudnessLevel]
+ -[ASVSchemaASVOutputVolumeQueried hasOutputVolume]
+ -[ASVSchemaASVOutputVolumeQueried hasPermanentOffsetFactor]
+ -[ASVSchemaASVOutputVolumeQueried hasSpeakerDistance]
+ -[ASVSchemaASVOutputVolumeQueried hasSpeakerSpeechLevel]
+ -[ASVSchemaASVOutputVolumeQueried hash]
+ -[ASVSchemaASVOutputVolumeQueried initWithDictionary:]
+ -[ASVSchemaASVOutputVolumeQueried initWithJSON:]
+ -[ASVSchemaASVOutputVolumeQueried invocationType]
+ -[ASVSchemaASVOutputVolumeQueried isEqual:]
+ -[ASVSchemaASVOutputVolumeQueried isMediaPlaybackOn]
+ -[ASVSchemaASVOutputVolumeQueried isPermanentOffsetEnabled]
+ -[ASVSchemaASVOutputVolumeQueried jsonData]
+ -[ASVSchemaASVOutputVolumeQueried musicLoudnessLevel]
+ -[ASVSchemaASVOutputVolumeQueried outputVolume]
+ -[ASVSchemaASVOutputVolumeQueried permanentOffsetFactor]
+ -[ASVSchemaASVOutputVolumeQueried readFrom:]
+ -[ASVSchemaASVOutputVolumeQueried setBackgroundNoiseActivityLevel:]
+ -[ASVSchemaASVOutputVolumeQueried setBackgroundNoiseLevel:]
+ -[ASVSchemaASVOutputVolumeQueried setHasBackgroundNoiseActivityLevel:]
+ -[ASVSchemaASVOutputVolumeQueried setHasBackgroundNoiseLevel:]
+ -[ASVSchemaASVOutputVolumeQueried setHasInvocationType:]
+ -[ASVSchemaASVOutputVolumeQueried setHasIsMediaPlaybackOn:]
+ -[ASVSchemaASVOutputVolumeQueried setHasIsPermanentOffsetEnabled:]
+ -[ASVSchemaASVOutputVolumeQueried setHasMusicLoudnessLevel:]
+ -[ASVSchemaASVOutputVolumeQueried setHasOutputVolume:]
+ -[ASVSchemaASVOutputVolumeQueried setHasPermanentOffsetFactor:]
+ -[ASVSchemaASVOutputVolumeQueried setHasSpeakerDistance:]
+ -[ASVSchemaASVOutputVolumeQueried setHasSpeakerSpeechLevel:]
+ -[ASVSchemaASVOutputVolumeQueried setInvocationType:]
+ -[ASVSchemaASVOutputVolumeQueried setIsMediaPlaybackOn:]
+ -[ASVSchemaASVOutputVolumeQueried setIsPermanentOffsetEnabled:]
+ -[ASVSchemaASVOutputVolumeQueried setMusicLoudnessLevel:]
+ -[ASVSchemaASVOutputVolumeQueried setOutputVolume:]
+ -[ASVSchemaASVOutputVolumeQueried setPermanentOffsetFactor:]
+ -[ASVSchemaASVOutputVolumeQueried setSpeakerDistance:]
+ -[ASVSchemaASVOutputVolumeQueried setSpeakerSpeechLevel:]
+ -[ASVSchemaASVOutputVolumeQueried speakerDistance]
+ -[ASVSchemaASVOutputVolumeQueried speakerSpeechLevel]
+ -[ASVSchemaASVOutputVolumeQueried writeTo:]
+ -[ASVSchemaASVOutputVolumeQueried(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASVSchemaASVUserIntentDetected deleteIsPermanentOffsetEnabled]
+ -[ASVSchemaASVUserIntentDetected deletePermanentOffsetFactor]
+ -[ASVSchemaASVUserIntentDetected deleteUserIntentType]
+ -[ASVSchemaASVUserIntentDetected deleteUserIntentVolume]
+ -[ASVSchemaASVUserIntentDetected dictionaryRepresentation]
+ -[ASVSchemaASVUserIntentDetected hasIsPermanentOffsetEnabled]
+ -[ASVSchemaASVUserIntentDetected hasPermanentOffsetFactor]
+ -[ASVSchemaASVUserIntentDetected hasUserIntentType]
+ -[ASVSchemaASVUserIntentDetected hasUserIntentVolume]
+ -[ASVSchemaASVUserIntentDetected hash]
+ -[ASVSchemaASVUserIntentDetected initWithDictionary:]
+ -[ASVSchemaASVUserIntentDetected initWithJSON:]
+ -[ASVSchemaASVUserIntentDetected isEqual:]
+ -[ASVSchemaASVUserIntentDetected isPermanentOffsetEnabled]
+ -[ASVSchemaASVUserIntentDetected jsonData]
+ -[ASVSchemaASVUserIntentDetected permanentOffsetFactor]
+ -[ASVSchemaASVUserIntentDetected readFrom:]
+ -[ASVSchemaASVUserIntentDetected setHasIsPermanentOffsetEnabled:]
+ -[ASVSchemaASVUserIntentDetected setHasPermanentOffsetFactor:]
+ -[ASVSchemaASVUserIntentDetected setHasUserIntentType:]
+ -[ASVSchemaASVUserIntentDetected setHasUserIntentVolume:]
+ -[ASVSchemaASVUserIntentDetected setIsPermanentOffsetEnabled:]
+ -[ASVSchemaASVUserIntentDetected setPermanentOffsetFactor:]
+ -[ASVSchemaASVUserIntentDetected setUserIntentType:]
+ -[ASVSchemaASVUserIntentDetected setUserIntentVolume:]
+ -[ASVSchemaASVUserIntentDetected userIntentType]
+ -[ASVSchemaASVUserIntentDetected userIntentVolume]
+ -[ASVSchemaASVUserIntentDetected writeTo:]
+ -[ASVSchemaASVUserIntentDetected(SensitiveConditions) suppressMessageUnderConditions]
+ -[GATSchemaGATClientEvent deleteResponseMetadataCaptured]
+ -[GATSchemaGATClientEvent hasResponseMetadataCaptured]
+ -[GATSchemaGATClientEvent responseMetadataCaptured]
+ -[GATSchemaGATClientEvent setHasResponseMetadataCaptured:]
+ -[GATSchemaGATClientEvent setResponseMetadataCaptured:]
+ -[GATSchemaGATCreateSessionEventFailed .cxx_destruct]
+ -[GATSchemaGATCreateSessionEventFailed deleteError]
+ -[GATSchemaGATCreateSessionEventFailed deleteUnderlyingError]
+ -[GATSchemaGATCreateSessionEventFailed error]
+ -[GATSchemaGATCreateSessionEventFailed hasError]
+ -[GATSchemaGATCreateSessionEventFailed hasUnderlyingError]
+ -[GATSchemaGATCreateSessionEventFailed setError:]
+ -[GATSchemaGATCreateSessionEventFailed setHasError:]
+ -[GATSchemaGATCreateSessionEventFailed setHasUnderlyingError:]
+ -[GATSchemaGATCreateSessionEventFailed setUnderlyingError:]
+ -[GATSchemaGATCreateSessionEventFailed underlyingError]
+ -[GATSchemaGATCreateSessionEventFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[GATSchemaGATError .cxx_destruct]
+ -[GATSchemaGATError code]
+ -[GATSchemaGATError deleteCode]
+ -[GATSchemaGATError deleteDomain]
+ -[GATSchemaGATError dictionaryRepresentation]
+ -[GATSchemaGATError domain]
+ -[GATSchemaGATError hasCode]
+ -[GATSchemaGATError hasDomain]
+ -[GATSchemaGATError hash]
+ -[GATSchemaGATError initWithDictionary:]
+ -[GATSchemaGATError initWithJSON:]
+ -[GATSchemaGATError isEqual:]
+ -[GATSchemaGATError jsonData]
+ -[GATSchemaGATError readFrom:]
+ -[GATSchemaGATError setCode:]
+ -[GATSchemaGATError setDomain:]
+ -[GATSchemaGATError setHasCode:]
+ -[GATSchemaGATError setHasDomain:]
+ -[GATSchemaGATError writeTo:]
+ -[GATSchemaGATError(SensitiveConditions) suppressMessageUnderConditions]
+ -[GATSchemaGATFileMetadata deleteSizeInKB]
+ -[GATSchemaGATFileMetadata dictionaryRepresentation]
+ -[GATSchemaGATFileMetadata hasSizeInKB]
+ -[GATSchemaGATFileMetadata hash]
+ -[GATSchemaGATFileMetadata initWithDictionary:]
+ -[GATSchemaGATFileMetadata initWithJSON:]
+ -[GATSchemaGATFileMetadata isEqual:]
+ -[GATSchemaGATFileMetadata jsonData]
+ -[GATSchemaGATFileMetadata readFrom:]
+ -[GATSchemaGATFileMetadata setHasSizeInKB:]
+ -[GATSchemaGATFileMetadata setSizeInKB:]
+ -[GATSchemaGATFileMetadata sizeInKB]
+ -[GATSchemaGATFileMetadata writeTo:]
+ -[GATSchemaGATFileMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[GATSchemaGATGenerativeRequestEventFailed .cxx_destruct]
+ -[GATSchemaGATGenerativeRequestEventFailed deleteError]
+ -[GATSchemaGATGenerativeRequestEventFailed deleteUnderlyingError]
+ -[GATSchemaGATGenerativeRequestEventFailed error]
+ -[GATSchemaGATGenerativeRequestEventFailed hasError]
+ -[GATSchemaGATGenerativeRequestEventFailed hasUnderlyingError]
+ -[GATSchemaGATGenerativeRequestEventFailed setError:]
+ -[GATSchemaGATGenerativeRequestEventFailed setHasError:]
+ -[GATSchemaGATGenerativeRequestEventFailed setHasUnderlyingError:]
+ -[GATSchemaGATGenerativeRequestEventFailed setUnderlyingError:]
+ -[GATSchemaGATGenerativeRequestEventFailed underlyingError]
+ -[GATSchemaGATGenerativeRequestEventFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[GATSchemaGATImageMetadata deleteSizeInKB]
+ -[GATSchemaGATImageMetadata dictionaryRepresentation]
+ -[GATSchemaGATImageMetadata hasSizeInKB]
+ -[GATSchemaGATImageMetadata hash]
+ -[GATSchemaGATImageMetadata initWithDictionary:]
+ -[GATSchemaGATImageMetadata initWithJSON:]
+ -[GATSchemaGATImageMetadata isEqual:]
+ -[GATSchemaGATImageMetadata jsonData]
+ -[GATSchemaGATImageMetadata readFrom:]
+ -[GATSchemaGATImageMetadata setHasSizeInKB:]
+ -[GATSchemaGATImageMetadata setSizeInKB:]
+ -[GATSchemaGATImageMetadata sizeInKB]
+ -[GATSchemaGATImageMetadata writeTo:]
+ -[GATSchemaGATImageMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[GATSchemaGATImageResizingEventFailed .cxx_destruct]
+ -[GATSchemaGATImageResizingEventFailed deleteError]
+ -[GATSchemaGATImageResizingEventFailed error]
+ -[GATSchemaGATImageResizingEventFailed hasError]
+ -[GATSchemaGATImageResizingEventFailed setError:]
+ -[GATSchemaGATImageResizingEventFailed setHasError:]
+ -[GATSchemaGATImageResizingEventFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[GATSchemaGATLoadScreenContentEventEnded .cxx_destruct]
+ -[GATSchemaGATLoadScreenContentEventEnded deleteUnderlyingError]
+ -[GATSchemaGATLoadScreenContentEventEnded hasUnderlyingError]
+ -[GATSchemaGATLoadScreenContentEventEnded setHasUnderlyingError:]
+ -[GATSchemaGATLoadScreenContentEventEnded setUnderlyingError:]
+ -[GATSchemaGATLoadScreenContentEventEnded underlyingError]
+ -[GATSchemaGATLoadScreenContentEventEnded(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[GATSchemaGATLoadScreenContentEventFailed .cxx_destruct]
+ -[GATSchemaGATLoadScreenContentEventFailed deleteError]
+ -[GATSchemaGATLoadScreenContentEventFailed deleteUnderlyingError]
+ -[GATSchemaGATLoadScreenContentEventFailed error]
+ -[GATSchemaGATLoadScreenContentEventFailed hasError]
+ -[GATSchemaGATLoadScreenContentEventFailed hasUnderlyingError]
+ -[GATSchemaGATLoadScreenContentEventFailed setError:]
+ -[GATSchemaGATLoadScreenContentEventFailed setHasError:]
+ -[GATSchemaGATLoadScreenContentEventFailed setHasUnderlyingError:]
+ -[GATSchemaGATLoadScreenContentEventFailed setUnderlyingError:]
+ -[GATSchemaGATLoadScreenContentEventFailed underlyingError]
+ -[GATSchemaGATLoadScreenContentEventFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[GATSchemaGATPnRMetrics deleteFileCount]
+ -[GATSchemaGATPnRMetrics deleteImageCount]
+ -[GATSchemaGATPnRMetrics fileCount]
+ -[GATSchemaGATPnRMetrics hasFileCount]
+ -[GATSchemaGATPnRMetrics hasImageCount]
+ -[GATSchemaGATPnRMetrics imageCount]
+ -[GATSchemaGATPnRMetrics setFileCount:]
+ -[GATSchemaGATPnRMetrics setHasFileCount:]
+ -[GATSchemaGATPnRMetrics setHasImageCount:]
+ -[GATSchemaGATPnRMetrics setImageCount:]
+ -[GATSchemaGATRegisterMediaEventFailed .cxx_destruct]
+ -[GATSchemaGATRegisterMediaEventFailed deleteError]
+ -[GATSchemaGATRegisterMediaEventFailed deleteUnderlyingError]
+ -[GATSchemaGATRegisterMediaEventFailed error]
+ -[GATSchemaGATRegisterMediaEventFailed hasError]
+ -[GATSchemaGATRegisterMediaEventFailed hasUnderlyingError]
+ -[GATSchemaGATRegisterMediaEventFailed setError:]
+ -[GATSchemaGATRegisterMediaEventFailed setHasError:]
+ -[GATSchemaGATRegisterMediaEventFailed setHasUnderlyingError:]
+ -[GATSchemaGATRegisterMediaEventFailed setUnderlyingError:]
+ -[GATSchemaGATRegisterMediaEventFailed underlyingError]
+ -[GATSchemaGATRegisterMediaEventFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[GATSchemaGATRequestFailed .cxx_destruct]
+ -[GATSchemaGATRequestFailed deleteError]
+ -[GATSchemaGATRequestFailed deleteUnderlyingError]
+ -[GATSchemaGATRequestFailed error]
+ -[GATSchemaGATRequestFailed hasError]
+ -[GATSchemaGATRequestFailed hasUnderlyingError]
+ -[GATSchemaGATRequestFailed setError:]
+ -[GATSchemaGATRequestFailed setHasError:]
+ -[GATSchemaGATRequestFailed setHasUnderlyingError:]
+ -[GATSchemaGATRequestFailed setUnderlyingError:]
+ -[GATSchemaGATRequestFailed underlyingError]
+ -[GATSchemaGATRequestFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[GATSchemaGATRequestStarted deleteIsConfirmationPromptSettingEnabled]
+ -[GATSchemaGATRequestStarted hasIsConfirmationPromptSettingEnabled]
+ -[GATSchemaGATRequestStarted isConfirmationPromptSettingEnabled]
+ -[GATSchemaGATRequestStarted setHasIsConfirmationPromptSettingEnabled:]
+ -[GATSchemaGATRequestStarted setIsConfirmationPromptSettingEnabled:]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured .cxx_destruct]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured addResponseSegments:]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured clearResponseSegments]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured deleteResponseSegments]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured dictionaryRepresentation]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured hash]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured initWithDictionary:]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured initWithJSON:]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured isEqual:]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured jsonData]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured readFrom:]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured responseSegmentsAtIndex:]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured responseSegmentsCount]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured responseSegments]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured setResponseSegments:]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured writeTo:]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[GATSchemaGATRichFormatResponseMetadataCaptured(SensitiveConditions) suppressMessageUnderConditions]
+ -[GATSchemaGATRichFormatResponseSegment .cxx_destruct]
+ -[GATSchemaGATRichFormatResponseSegment deleteFile]
+ -[GATSchemaGATRichFormatResponseSegment deleteImage]
+ -[GATSchemaGATRichFormatResponseSegment deleteMediaType]
+ -[GATSchemaGATRichFormatResponseSegment deleteMimeType]
+ -[GATSchemaGATRichFormatResponseSegment deleteText]
+ -[GATSchemaGATRichFormatResponseSegment dictionaryRepresentation]
+ -[GATSchemaGATRichFormatResponseSegment file]
+ -[GATSchemaGATRichFormatResponseSegment hasFile]
+ -[GATSchemaGATRichFormatResponseSegment hasImage]
+ -[GATSchemaGATRichFormatResponseSegment hasMediaType]
+ -[GATSchemaGATRichFormatResponseSegment hasMimeType]
+ -[GATSchemaGATRichFormatResponseSegment hasText]
+ -[GATSchemaGATRichFormatResponseSegment hash]
+ -[GATSchemaGATRichFormatResponseSegment image]
+ -[GATSchemaGATRichFormatResponseSegment initWithDictionary:]
+ -[GATSchemaGATRichFormatResponseSegment initWithJSON:]
+ -[GATSchemaGATRichFormatResponseSegment isEqual:]
+ -[GATSchemaGATRichFormatResponseSegment jsonData]
+ -[GATSchemaGATRichFormatResponseSegment mediaType]
+ -[GATSchemaGATRichFormatResponseSegment mimeType]
+ -[GATSchemaGATRichFormatResponseSegment readFrom:]
+ -[GATSchemaGATRichFormatResponseSegment setFile:]
+ -[GATSchemaGATRichFormatResponseSegment setHasFile:]
+ -[GATSchemaGATRichFormatResponseSegment setHasImage:]
+ -[GATSchemaGATRichFormatResponseSegment setHasMediaType:]
+ -[GATSchemaGATRichFormatResponseSegment setHasMimeType:]
+ -[GATSchemaGATRichFormatResponseSegment setHasText:]
+ -[GATSchemaGATRichFormatResponseSegment setImage:]
+ -[GATSchemaGATRichFormatResponseSegment setMediaType:]
+ -[GATSchemaGATRichFormatResponseSegment setMimeType:]
+ -[GATSchemaGATRichFormatResponseSegment setText:]
+ -[GATSchemaGATRichFormatResponseSegment text]
+ -[GATSchemaGATRichFormatResponseSegment whichPayload]
+ -[GATSchemaGATRichFormatResponseSegment writeTo:]
+ -[GATSchemaGATRichFormatResponseSegment(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[GATSchemaGATRichFormatResponseSegment(SensitiveConditions) suppressMessageUnderConditions]
+ -[GATSchemaGATTextMetadata characterCount]
+ -[GATSchemaGATTextMetadata deleteCharacterCount]
+ -[GATSchemaGATTextMetadata dictionaryRepresentation]
+ -[GATSchemaGATTextMetadata hasCharacterCount]
+ -[GATSchemaGATTextMetadata hash]
+ -[GATSchemaGATTextMetadata initWithDictionary:]
+ -[GATSchemaGATTextMetadata initWithJSON:]
+ -[GATSchemaGATTextMetadata isEqual:]
+ -[GATSchemaGATTextMetadata jsonData]
+ -[GATSchemaGATTextMetadata readFrom:]
+ -[GATSchemaGATTextMetadata setCharacterCount:]
+ -[GATSchemaGATTextMetadata setHasCharacterCount:]
+ -[GATSchemaGATTextMetadata writeTo:]
+ -[GATSchemaGATTextMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 .cxx_destruct]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 deleteIsLlmGeneratedAnswer]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 deleteQnaId]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 dictionaryRepresentation]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 hasIsLlmGeneratedAnswer]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 hasQnaId]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 hash]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 initWithDictionary:]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 initWithJSON:]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 isEqual:]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 isLlmGeneratedAnswer]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 jsonData]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 qnaId]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 readFrom:]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 setHasIsLlmGeneratedAnswer:]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 setHasQnaId:]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 setIsLlmGeneratedAnswer:]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 setQnaId:]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1 writeTo:]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[PEGASUSSchemaPEGASUSRequestEndedTier1 deleteDeviceExpertExecutionTier1]
+ -[PEGASUSSchemaPEGASUSRequestEndedTier1 deviceExpertExecutionTier1]
+ -[PEGASUSSchemaPEGASUSRequestEndedTier1 hasDeviceExpertExecutionTier1]
+ -[PEGASUSSchemaPEGASUSRequestEndedTier1 setDeviceExpertExecutionTier1:]
+ -[PEGASUSSchemaPEGASUSRequestEndedTier1 setHasDeviceExpertExecutionTier1:]
+ -[TTSSchemaTTSSpeechStarted deleteThermalLevel]
+ -[TTSSchemaTTSSpeechStarted hasThermalLevel]
+ -[TTSSchemaTTSSpeechStarted setHasThermalLevel:]
+ -[TTSSchemaTTSSpeechStarted setThermalLevel:]
+ -[TTSSchemaTTSSpeechStarted thermalLevel]
+ -[TTSSchemaTTSSynthesisStarted deleteThermalLevel]
+ -[TTSSchemaTTSSynthesisStarted hasThermalLevel]
+ -[TTSSchemaTTSSynthesisStarted setHasThermalLevel:]
+ -[TTSSchemaTTSSynthesisStarted setThermalLevel:]
+ -[TTSSchemaTTSSynthesisStarted thermalLevel]
+ OBJC_IVAR_$_ASVSchemaASVClientEvent._asvOutputVolumeQueried
+ OBJC_IVAR_$_ASVSchemaASVClientEvent._asvUserIntentDetected
+ OBJC_IVAR_$_ASVSchemaASVClientEvent._eventMetadata
+ OBJC_IVAR_$_ASVSchemaASVClientEventMetadata._asvId
+ OBJC_IVAR_$_ASVSchemaASVOutputVolumeQueried._backgroundNoiseActivityLevel
+ OBJC_IVAR_$_ASVSchemaASVOutputVolumeQueried._backgroundNoiseLevel
+ OBJC_IVAR_$_ASVSchemaASVOutputVolumeQueried._has
+ OBJC_IVAR_$_ASVSchemaASVOutputVolumeQueried._invocationType
+ OBJC_IVAR_$_ASVSchemaASVOutputVolumeQueried._isMediaPlaybackOn
+ OBJC_IVAR_$_ASVSchemaASVOutputVolumeQueried._isPermanentOffsetEnabled
+ OBJC_IVAR_$_ASVSchemaASVOutputVolumeQueried._musicLoudnessLevel
+ OBJC_IVAR_$_ASVSchemaASVOutputVolumeQueried._outputVolume
+ OBJC_IVAR_$_ASVSchemaASVOutputVolumeQueried._permanentOffsetFactor
+ OBJC_IVAR_$_ASVSchemaASVOutputVolumeQueried._speakerDistance
+ OBJC_IVAR_$_ASVSchemaASVOutputVolumeQueried._speakerSpeechLevel
+ OBJC_IVAR_$_ASVSchemaASVUserIntentDetected._has
+ OBJC_IVAR_$_ASVSchemaASVUserIntentDetected._isPermanentOffsetEnabled
+ OBJC_IVAR_$_ASVSchemaASVUserIntentDetected._permanentOffsetFactor
+ OBJC_IVAR_$_ASVSchemaASVUserIntentDetected._userIntentType
+ OBJC_IVAR_$_ASVSchemaASVUserIntentDetected._userIntentVolume
+ OBJC_IVAR_$_GATSchemaGATClientEvent._responseMetadataCaptured
+ OBJC_IVAR_$_GATSchemaGATCreateSessionEventFailed._error
+ OBJC_IVAR_$_GATSchemaGATCreateSessionEventFailed._underlyingError
+ OBJC_IVAR_$_GATSchemaGATError._code
+ OBJC_IVAR_$_GATSchemaGATError._domain
+ OBJC_IVAR_$_GATSchemaGATError._has
+ OBJC_IVAR_$_GATSchemaGATFileMetadata._has
+ OBJC_IVAR_$_GATSchemaGATFileMetadata._sizeInKB
+ OBJC_IVAR_$_GATSchemaGATGenerativeRequestEventFailed._error
+ OBJC_IVAR_$_GATSchemaGATGenerativeRequestEventFailed._underlyingError
+ OBJC_IVAR_$_GATSchemaGATImageMetadata._has
+ OBJC_IVAR_$_GATSchemaGATImageMetadata._sizeInKB
+ OBJC_IVAR_$_GATSchemaGATImageResizingEventFailed._error
+ OBJC_IVAR_$_GATSchemaGATLoadScreenContentEventEnded._underlyingError
+ OBJC_IVAR_$_GATSchemaGATLoadScreenContentEventFailed._error
+ OBJC_IVAR_$_GATSchemaGATLoadScreenContentEventFailed._underlyingError
+ OBJC_IVAR_$_GATSchemaGATPnRMetrics._fileCount
+ OBJC_IVAR_$_GATSchemaGATPnRMetrics._imageCount
+ OBJC_IVAR_$_GATSchemaGATRegisterMediaEventFailed._error
+ OBJC_IVAR_$_GATSchemaGATRegisterMediaEventFailed._underlyingError
+ OBJC_IVAR_$_GATSchemaGATRequestFailed._error
+ OBJC_IVAR_$_GATSchemaGATRequestFailed._underlyingError
+ OBJC_IVAR_$_GATSchemaGATRequestStarted._isConfirmationPromptSettingEnabled
+ OBJC_IVAR_$_GATSchemaGATRichFormatResponseMetadataCaptured._responseSegments
+ OBJC_IVAR_$_GATSchemaGATRichFormatResponseSegment._file
+ OBJC_IVAR_$_GATSchemaGATRichFormatResponseSegment._has
+ OBJC_IVAR_$_GATSchemaGATRichFormatResponseSegment._image
+ OBJC_IVAR_$_GATSchemaGATRichFormatResponseSegment._mediaType
+ OBJC_IVAR_$_GATSchemaGATRichFormatResponseSegment._mimeType
+ OBJC_IVAR_$_GATSchemaGATRichFormatResponseSegment._text
+ OBJC_IVAR_$_GATSchemaGATTextMetadata._characterCount
+ OBJC_IVAR_$_GATSchemaGATTextMetadata._has
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1._has
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1._isLlmGeneratedAnswer
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1._qnaId
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSRequestEndedTier1._deviceExpertExecutionTier1
+ OBJC_IVAR_$_TTSSchemaTTSSpeechStarted._thermalLevel
+ OBJC_IVAR_$_TTSSchemaTTSSynthesisStarted._thermalLevel
+ _ASVSchemaASVClientEventMetadataReadFrom
+ _ASVSchemaASVClientEventReadFrom
+ _ASVSchemaASVOutputVolumeQueriedReadFrom
+ _ASVSchemaASVUserIntentDetectedReadFrom
+ _GATSchemaGATErrorReadFrom
+ _GATSchemaGATFileMetadataReadFrom
+ _GATSchemaGATImageMetadataReadFrom
+ _GATSchemaGATRichFormatResponseMetadataCapturedReadFrom
+ _GATSchemaGATRichFormatResponseSegmentReadFrom
+ _GATSchemaGATTextMetadataReadFrom
+ _OBJC_CLASS_$_ASVSchemaASVClientEvent
+ _OBJC_CLASS_$_ASVSchemaASVClientEventMetadata
+ _OBJC_CLASS_$_ASVSchemaASVOutputVolumeQueried
+ _OBJC_CLASS_$_ASVSchemaASVUserIntentDetected
+ _OBJC_CLASS_$_GATSchemaGATError
+ _OBJC_CLASS_$_GATSchemaGATFileMetadata
+ _OBJC_CLASS_$_GATSchemaGATImageMetadata
+ _OBJC_CLASS_$_GATSchemaGATRichFormatResponseMetadataCaptured
+ _OBJC_CLASS_$_GATSchemaGATRichFormatResponseSegment
+ _OBJC_CLASS_$_GATSchemaGATTextMetadata
+ _OBJC_CLASS_$_PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1
+ _OBJC_IVAR_$_ASVSchemaASVClientEvent._hasAsvOutputVolumeQueried
+ _OBJC_IVAR_$_ASVSchemaASVClientEvent._hasAsvUserIntentDetected
+ _OBJC_IVAR_$_ASVSchemaASVClientEvent._hasEventMetadata
+ _OBJC_IVAR_$_ASVSchemaASVClientEvent._whichEvent_Type
+ _OBJC_IVAR_$_ASVSchemaASVClientEventMetadata._hasAsvId
+ _OBJC_IVAR_$_GATSchemaGATClientEvent._hasResponseMetadataCaptured
+ _OBJC_IVAR_$_GATSchemaGATCreateSessionEventFailed._hasError
+ _OBJC_IVAR_$_GATSchemaGATCreateSessionEventFailed._hasUnderlyingError
+ _OBJC_IVAR_$_GATSchemaGATError._hasDomain
+ _OBJC_IVAR_$_GATSchemaGATGenerativeRequestEventFailed._hasError
+ _OBJC_IVAR_$_GATSchemaGATGenerativeRequestEventFailed._hasUnderlyingError
+ _OBJC_IVAR_$_GATSchemaGATImageResizingEventFailed._hasError
+ _OBJC_IVAR_$_GATSchemaGATLoadScreenContentEventEnded._hasUnderlyingError
+ _OBJC_IVAR_$_GATSchemaGATLoadScreenContentEventFailed._hasError
+ _OBJC_IVAR_$_GATSchemaGATLoadScreenContentEventFailed._hasUnderlyingError
+ _OBJC_IVAR_$_GATSchemaGATRegisterMediaEventFailed._hasError
+ _OBJC_IVAR_$_GATSchemaGATRegisterMediaEventFailed._hasUnderlyingError
+ _OBJC_IVAR_$_GATSchemaGATRequestFailed._hasError
+ _OBJC_IVAR_$_GATSchemaGATRequestFailed._hasUnderlyingError
+ _OBJC_IVAR_$_GATSchemaGATRichFormatResponseSegment._hasFile
+ _OBJC_IVAR_$_GATSchemaGATRichFormatResponseSegment._hasImage
+ _OBJC_IVAR_$_GATSchemaGATRichFormatResponseSegment._hasMimeType
+ _OBJC_IVAR_$_GATSchemaGATRichFormatResponseSegment._hasText
+ _OBJC_IVAR_$_GATSchemaGATRichFormatResponseSegment._whichPayload
+ _OBJC_IVAR_$_PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1._hasQnaId
+ _OBJC_IVAR_$_PEGASUSSchemaPEGASUSRequestEndedTier1._hasDeviceExpertExecutionTier1
+ _OBJC_METACLASS_$_ASVSchemaASVClientEvent
+ _OBJC_METACLASS_$_ASVSchemaASVClientEventMetadata
+ _OBJC_METACLASS_$_ASVSchemaASVOutputVolumeQueried
+ _OBJC_METACLASS_$_ASVSchemaASVUserIntentDetected
+ _OBJC_METACLASS_$_GATSchemaGATError
+ _OBJC_METACLASS_$_GATSchemaGATFileMetadata
+ _OBJC_METACLASS_$_GATSchemaGATImageMetadata
+ _OBJC_METACLASS_$_GATSchemaGATRichFormatResponseMetadataCaptured
+ _OBJC_METACLASS_$_GATSchemaGATRichFormatResponseSegment
+ _OBJC_METACLASS_$_GATSchemaGATTextMetadata
+ _OBJC_METACLASS_$_PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1
+ _PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1ReadFrom
+ __OBJC_$_CLASS_METHODS_ASVSchemaASVClientEvent(InstrumentationAdditions|SensitiveConditions|Component|InnerEventContainer)
+ __OBJC_$_INSTANCE_METHODS_ASVSchemaASVClientEvent(InstrumentationAdditions|SensitiveConditions|Component|InnerEventContainer)
+ __OBJC_$_INSTANCE_METHODS_ASVSchemaASVClientEventMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASVSchemaASVOutputVolumeQueried(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASVSchemaASVUserIntentDetected(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_GATSchemaGATError(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_GATSchemaGATFileMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_GATSchemaGATImageMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_GATSchemaGATRichFormatResponseMetadataCaptured(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_GATSchemaGATRichFormatResponseSegment(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_GATSchemaGATTextMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_VARIABLES_ASVSchemaASVClientEvent
+ __OBJC_$_INSTANCE_VARIABLES_ASVSchemaASVClientEventMetadata
+ __OBJC_$_INSTANCE_VARIABLES_ASVSchemaASVOutputVolumeQueried
+ __OBJC_$_INSTANCE_VARIABLES_ASVSchemaASVUserIntentDetected
+ __OBJC_$_INSTANCE_VARIABLES_GATSchemaGATError
+ __OBJC_$_INSTANCE_VARIABLES_GATSchemaGATFileMetadata
+ __OBJC_$_INSTANCE_VARIABLES_GATSchemaGATImageMetadata
+ __OBJC_$_INSTANCE_VARIABLES_GATSchemaGATRichFormatResponseMetadataCaptured
+ __OBJC_$_INSTANCE_VARIABLES_GATSchemaGATRichFormatResponseSegment
+ __OBJC_$_INSTANCE_VARIABLES_GATSchemaGATTextMetadata
+ __OBJC_$_INSTANCE_VARIABLES_PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1
+ __OBJC_$_PROP_LIST_ASVSchemaASVClientEventMetadata
+ __OBJC_$_PROP_LIST_ASVSchemaASVOutputVolumeQueried
+ __OBJC_$_PROP_LIST_ASVSchemaASVUserIntentDetected
+ __OBJC_$_PROP_LIST_GATSchemaGATError
+ __OBJC_$_PROP_LIST_GATSchemaGATFileMetadata
+ __OBJC_$_PROP_LIST_GATSchemaGATImageMetadata
+ __OBJC_$_PROP_LIST_GATSchemaGATRichFormatResponseMetadataCaptured
+ __OBJC_$_PROP_LIST_GATSchemaGATRichFormatResponseSegment
+ __OBJC_$_PROP_LIST_GATSchemaGATTextMetadata
+ __OBJC_$_PROP_LIST_PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1
+ __OBJC_CLASS_PROTOCOLS_$_ASVSchemaASVClientEvent(InstrumentationAdditions|SensitiveConditions|Component|InnerEventContainer)
+ __OBJC_CLASS_RO_$_ASVSchemaASVClientEvent
+ __OBJC_CLASS_RO_$_ASVSchemaASVClientEventMetadata
+ __OBJC_CLASS_RO_$_ASVSchemaASVOutputVolumeQueried
+ __OBJC_CLASS_RO_$_ASVSchemaASVUserIntentDetected
+ __OBJC_CLASS_RO_$_GATSchemaGATError
+ __OBJC_CLASS_RO_$_GATSchemaGATFileMetadata
+ __OBJC_CLASS_RO_$_GATSchemaGATImageMetadata
+ __OBJC_CLASS_RO_$_GATSchemaGATRichFormatResponseMetadataCaptured
+ __OBJC_CLASS_RO_$_GATSchemaGATRichFormatResponseSegment
+ __OBJC_CLASS_RO_$_GATSchemaGATTextMetadata
+ __OBJC_CLASS_RO_$_PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1
+ __OBJC_METACLASS_RO_$_ASVSchemaASVClientEvent
+ __OBJC_METACLASS_RO_$_ASVSchemaASVClientEventMetadata
+ __OBJC_METACLASS_RO_$_ASVSchemaASVOutputVolumeQueried
+ __OBJC_METACLASS_RO_$_ASVSchemaASVUserIntentDetected
+ __OBJC_METACLASS_RO_$_GATSchemaGATError
+ __OBJC_METACLASS_RO_$_GATSchemaGATFileMetadata
+ __OBJC_METACLASS_RO_$_GATSchemaGATImageMetadata
+ __OBJC_METACLASS_RO_$_GATSchemaGATRichFormatResponseMetadataCaptured
+ __OBJC_METACLASS_RO_$_GATSchemaGATRichFormatResponseSegment
+ __OBJC_METACLASS_RO_$_GATSchemaGATTextMetadata
+ __OBJC_METACLASS_RO_$_PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1
+ _objc_msgSend$addResponseSegments:
+ _objc_msgSend$asvId
+ _objc_msgSend$asvOutputVolumeQueried
+ _objc_msgSend$asvUserIntentDetected
+ _objc_msgSend$clearResponseSegments
+ _objc_msgSend$deleteAsvId
+ _objc_msgSend$deleteAsvOutputVolumeQueried
+ _objc_msgSend$deleteAsvUserIntentDetected
+ _objc_msgSend$deleteDeviceExpertExecutionTier1
+ _objc_msgSend$deleteImage
+ _objc_msgSend$deleteIsLlmGeneratedAnswer
+ _objc_msgSend$deleteQnaId
+ _objc_msgSend$deleteResponseMetadataCaptured
+ _objc_msgSend$deviceExpertExecutionTier1
+ _objc_msgSend$fileCount
+ _objc_msgSend$image
+ _objc_msgSend$isConfirmationPromptSettingEnabled
+ _objc_msgSend$isLlmGeneratedAnswer
+ _objc_msgSend$mimeType
+ _objc_msgSend$outputVolume
+ _objc_msgSend$qnaId
+ _objc_msgSend$responseMetadataCaptured
+ _objc_msgSend$responseSegments
+ _objc_msgSend$setAsvId:
+ _objc_msgSend$setAsvOutputVolumeQueried:
+ _objc_msgSend$setAsvUserIntentDetected:
+ _objc_msgSend$setDeviceExpertExecutionTier1:
+ _objc_msgSend$setFileCount:
+ _objc_msgSend$setImage:
+ _objc_msgSend$setIsConfirmationPromptSettingEnabled:
+ _objc_msgSend$setIsLlmGeneratedAnswer:
+ _objc_msgSend$setMimeType:
+ _objc_msgSend$setOutputVolume:
+ _objc_msgSend$setQnaId:
+ _objc_msgSend$setResponseMetadataCaptured:
+ _objc_msgSend$setResponseSegments:
+ _objc_msgSend$setSizeInKB:
+ _objc_msgSend$setThermalLevel:
+ _objc_msgSend$sizeInKB
+ _objc_msgSend$thermalLevel
+ _objc_msgSend$whichPayload
+ _qname_ASVSchemaASVClientEvent_WhichEvent_Type_None
+ _qname_ASVSchemaASVClientEvent_WhichEvent_Type_asvOutputVolumeQueried
+ _qname_ASVSchemaASVClientEvent_WhichEvent_Type_asvUserIntentDetected
+ _qname_GATSchemaGATClientEvent_WhichEvent_Type_responseMetadataCaptured
+ _symbolic _____ So26ASVSchemaASVInvocationTypeV
+ _symbolic _____ So26ASVSchemaASVUserIntentTypeV
+ _symbolic _____ So28GATSchemaGATGeneralMediaTypeV
+ _symbolic _____ So31ASVSchemaASVSpeakerDistanceTypeV
+ _symbolic _____ So40ASVSchemaASVBackgroundNoiseActivityLevelV
CStrings:
+ "@\"ASVSchemaASVClientEventMetadata\""
+ "@\"ASVSchemaASVOutputVolumeQueried\""
+ "@\"ASVSchemaASVUserIntentDetected\""
+ "@\"GATSchemaGATError\""
+ "@\"GATSchemaGATFileMetadata\""
+ "@\"GATSchemaGATImageMetadata\""
+ "@\"GATSchemaGATRichFormatResponseMetadataCaptured\""
+ "@\"GATSchemaGATTextMetadata\""
+ "@\"PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1\""
+ "ASVBACKGROUNDNOISEACTIVITYLEVEL_HIGH"
+ "ASVBACKGROUNDNOISEACTIVITYLEVEL_LOW"
+ "ASVBACKGROUNDNOISEACTIVITYLEVEL_UNKNOWN"
+ "ASVINVOCATIONTYPE_BUTTON_PRESS"
+ "ASVINVOCATIONTYPE_UNKNOWN"
+ "ASVINVOCATIONTYPE_VOICE_TRIGGER"
+ "ASVSPEAKERDISTANCETYPE_ESTIMATION_INCOMPLETE"
+ "ASVSPEAKERDISTANCETYPE_FAR"
+ "ASVSPEAKERDISTANCETYPE_MID"
+ "ASVSPEAKERDISTANCETYPE_NEAR"
+ "ASVSPEAKERDISTANCETYPE_UNKNOWN"
+ "ASVSchemaASVClientEvent"
+ "ASVSchemaASVClientEventMetadata"
+ "ASVSchemaASVOutputVolumeQueried"
+ "ASVSchemaASVUserIntentDetected"
+ "ASVUSERINTENTTYPE_DECREASE_SIRI_VOLUME"
+ "ASVUSERINTENTTYPE_DEFAULT"
+ "ASVUSERINTENTTYPE_INCREASE_SIRI_VOLUME"
+ "ASVUSERINTENTTYPE_SET_VOLUME"
+ "ASVUSERINTENTTYPE_UNKNOWN"
+ "ASV_CLIENT_EVENT"
+ "COMPONENTNAME_ASV"
+ "GATGENERALMEDIATYPE_CODEBLOCK"
+ "GATGENERALMEDIATYPE_FILE"
+ "GATGENERALMEDIATYPE_IMAGE"
+ "GATGENERALMEDIATYPE_TEXT"
+ "GATGENERALMEDIATYPE_UNKNOWN"
+ "GATSchemaGATError"
+ "GATSchemaGATFileMetadata"
+ "GATSchemaGATImageMetadata"
+ "GATSchemaGATRichFormatResponseMetadataCaptured"
+ "GATSchemaGATRichFormatResponseSegment"
+ "GATSchemaGATTextMetadata"
+ "PEGASUSPRODUCTAREA_DEVICE_EXPERT"
+ "PEGASUSPROVIDER_DEVICE_EXPERT"
+ "PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1"
+ "T@\"ASVSchemaASVClientEventMetadata\",&,N,V_eventMetadata"
+ "T@\"ASVSchemaASVOutputVolumeQueried\",&,N,V_asvOutputVolumeQueried"
+ "T@\"ASVSchemaASVUserIntentDetected\",&,N,V_asvUserIntentDetected"
+ "T@\"GATSchemaGATError\",&,N,V_error"
+ "T@\"GATSchemaGATError\",&,N,V_underlyingError"
+ "T@\"GATSchemaGATFileMetadata\",&,N,V_file"
+ "T@\"GATSchemaGATImageMetadata\",&,N,V_image"
+ "T@\"GATSchemaGATRichFormatResponseMetadataCaptured\",&,N,V_responseMetadataCaptured"
+ "T@\"GATSchemaGATTextMetadata\",&,N,V_text"
+ "T@\"NSArray\",C,N,V_responseSegments"
+ "T@\"NSString\",C,N,V_mimeType"
+ "T@\"NSString\",C,N,V_qnaId"
+ "T@\"PEGASUSSchemaPEGASUSDeviceExpertExecutionTier1\",&,N,V_deviceExpertExecutionTier1"
+ "T@\"SISchemaUUID\",&,N,V_asvId"
+ "TB,N,V_hasAsvId"
+ "TB,N,V_hasAsvOutputVolumeQueried"
+ "TB,N,V_hasAsvUserIntentDetected"
+ "TB,N,V_hasDeviceExpertExecutionTier1"
+ "TB,N,V_hasImage"
+ "TB,N,V_hasMimeType"
+ "TB,N,V_hasQnaId"
+ "TB,N,V_hasResponseMetadataCaptured"
+ "TB,N,V_isConfirmationPromptSettingEnabled"
+ "TB,N,V_isLlmGeneratedAnswer"
+ "TQ,N,V_sizeInKB"
+ "TQ,R,N,V_whichPayload"
+ "TTSSYNTHESISSOURCE_PCC_STREAMING"
+ "TTSSYNTHESISSOURCE_PEGASUS_STREAMING"
+ "Tf,N,V_outputVolume"
+ "Ti,N,V_fileCount"
+ "Ti,N,V_imageCount"
+ "Ti,N,V_thermalLevel"
+ "VOICENAME_ENUSWORKOUTA"
+ "VOICENAME_ENUSWORKOUTB"
+ "VOICENAME_ENUSWORKOUTC"
+ "VOICENAME_ENUSWORKOUTD"
+ "VOICENAME_PTPTA"
+ "VOICENAME_PTPTB"
+ "_asvId"
+ "_asvOutputVolumeQueried"
+ "_asvUserIntentDetected"
+ "_deviceExpertExecutionTier1"
+ "_fileCount"
+ "_hasAsvId"
+ "_hasAsvOutputVolumeQueried"
+ "_hasAsvUserIntentDetected"
+ "_hasDeviceExpertExecutionTier1"
+ "_hasImage"
+ "_hasMimeType"
+ "_hasQnaId"
+ "_hasResponseMetadataCaptured"
+ "_image"
+ "_isConfirmationPromptSettingEnabled"
+ "_isLlmGeneratedAnswer"
+ "_mimeType"
+ "_outputVolume"
+ "_qnaId"
+ "_responseMetadataCaptured"
+ "_responseSegments"
+ "_sizeInKB"
+ "_thermalLevel"
+ "_whichPayload"
+ "addResponseSegments:"
+ "asvId"
+ "asvOutputVolumeQueried"
+ "asvUserIntentDetected"
+ "clearResponseSegments"
+ "com.apple.aiml.siri.asv.ASVClientEvent"
+ "com.apple.aiml.siri.asv.ASVClientEvent.ASVOutputVolumeQueried"
+ "com.apple.aiml.siri.asv.ASVClientEvent.ASVUserIntentDetected"
+ "com.apple.aiml.siri.gat.GATClientEvent.GATRichFormatResponseMetadataCaptured"
+ "deleteAsvId"
+ "deleteAsvOutputVolumeQueried"
+ "deleteAsvUserIntentDetected"
+ "deleteDeviceExpertExecutionTier1"
+ "deleteFileCount"
+ "deleteImage"
+ "deleteIsConfirmationPromptSettingEnabled"
+ "deleteIsLlmGeneratedAnswer"
+ "deleteMimeType"
+ "deleteOutputVolume"
+ "deleteQnaId"
+ "deleteResponseMetadataCaptured"
+ "deleteResponseSegments"
+ "deleteSizeInKB"
+ "deleteThermalLevel"
+ "deviceExpertExecutionTier1"
+ "fileCount"
+ "hasAsvId"
+ "hasAsvOutputVolumeQueried"
+ "hasAsvUserIntentDetected"
+ "hasDeviceExpertExecutionTier1"
+ "hasFileCount"
+ "hasImage"
+ "hasIsConfirmationPromptSettingEnabled"
+ "hasIsLlmGeneratedAnswer"
+ "hasMimeType"
+ "hasOutputVolume"
+ "hasQnaId"
+ "hasResponseMetadataCaptured"
+ "hasSizeInKB"
+ "hasThermalLevel"
+ "image"
+ "isConfirmationPromptSettingEnabled"
+ "isLlmGeneratedAnswer"
+ "mimeType"
+ "outputVolume"
+ "pegasusRequestEndedTier1.deviceExpertExecutionTier1.isLlmGeneratedAnswer"
+ "pegasusRequestEndedTier1.deviceExpertExecutionTier1.qnaId"
+ "qnaId"
+ "responseMetadataCaptured"
+ "responseSegments"
+ "responseSegmentsAtIndex:"
+ "responseSegmentsCount"
+ "setAsvId:"
+ "setAsvOutputVolumeQueried:"
+ "setAsvUserIntentDetected:"
+ "setDeviceExpertExecutionTier1:"
+ "setFileCount:"
+ "setHasAsvId:"
+ "setHasAsvOutputVolumeQueried:"
+ "setHasAsvUserIntentDetected:"
+ "setHasDeviceExpertExecutionTier1:"
+ "setHasFileCount:"
+ "setHasImage:"
+ "setHasIsConfirmationPromptSettingEnabled:"
+ "setHasIsLlmGeneratedAnswer:"
+ "setHasMimeType:"
+ "setHasOutputVolume:"
+ "setHasQnaId:"
+ "setHasResponseMetadataCaptured:"
+ "setHasSizeInKB:"
+ "setHasThermalLevel:"
+ "setImage:"
+ "setIsConfirmationPromptSettingEnabled:"
+ "setIsLlmGeneratedAnswer:"
+ "setMimeType:"
+ "setOutputVolume:"
+ "setQnaId:"
+ "setResponseMetadataCaptured:"
+ "setResponseSegments:"
+ "setSizeInKB:"
+ "setThermalLevel:"
+ "sizeInKB"
+ "thermalLevel"
+ "whichPayload"
+ "{?=\"appIntentName\"b1\"isConfirmationPromptSettingEnabled\"b1}"
+ "{?=\"audioOutputRoute\"b1\"customerPerceivedLatencyInSecond\"b1\"synthesisSource\"b1\"synthesisEffect\"b1\"volume\"b1\"thermalState\"b1\"assetSelectionLatencyInSecond\"b1\"audioQueueLatencyInSecond\"b1\"isWarmStart\"b1\"llmStylePrompt\"b1\"thermalLevel\"b1}"
+ "{?=\"characterCount\"b1}"
+ "{?=\"isLlmGeneratedAnswer\"b1}"
+ "{?=\"mediaType\"b1}"
+ "{?=\"outputVolume\"b1\"speakerDistance\"b1\"speakerSpeechLevel\"b1\"musicLoudnessLevel\"b1\"backgroundNoiseLevel\"b1\"backgroundNoiseActivityLevel\"b1\"isMediaPlaybackOn\"b1\"invocationType\"b1\"isPermanentOffsetEnabled\"b1\"permanentOffsetFactor\"b1}"
+ "{?=\"sizeInKB\"b1}"
+ "{?=\"startSiriSessionDurationInSeconds\"b1\"generativeRequestDurationInSeconds\"b1\"loadScreenContentDurationInSeconds\"b1\"imageResizingDurationInSeconds\"b1\"registerMediaDurationInSeconds\"b1\"loadScreenContentRateKBsPerSecond\"b1\"registerMediaRateKBsPerSecond\"b1\"generativeResultCharactersCount\"b1\"imageResizingRateKBsPerSecond\"b1\"imageCount\"b1\"fileCount\"b1}"
+ "{?=\"synthesisSource\"b1\"synthesisEffect\"b1\"thermalState\"b1\"thermalLevel\"b1}"
- "{?=\"appIntentName\"b1}"
- "{?=\"audioOutputRoute\"b1\"customerPerceivedLatencyInSecond\"b1\"synthesisSource\"b1\"synthesisEffect\"b1\"volume\"b1\"thermalState\"b1\"assetSelectionLatencyInSecond\"b1\"audioQueueLatencyInSecond\"b1\"isWarmStart\"b1\"llmStylePrompt\"b1}"
- "{?=\"startSiriSessionDurationInSeconds\"b1\"generativeRequestDurationInSeconds\"b1\"loadScreenContentDurationInSeconds\"b1\"imageResizingDurationInSeconds\"b1\"registerMediaDurationInSeconds\"b1\"loadScreenContentRateKBsPerSecond\"b1\"registerMediaRateKBsPerSecond\"b1\"generativeResultCharactersCount\"b1\"imageResizingRateKBsPerSecond\"b1}"
- "{?=\"synthesisSource\"b1\"synthesisEffect\"b1\"thermalState\"b1}"

```
