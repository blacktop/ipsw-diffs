## SiriAnalyticsToolKitSupport

> `/System/Library/PrivateFrameworks/SiriAnalyticsToolKitSupport.framework/SiriAnalyticsToolKitSupport`

```diff

-2.2.0.0.0
-  __TEXT.__text: 0x0
-  __TEXT.__const: 0x52
+2.3.1.0.0
+  __TEXT.__text: 0x14fd8
+  __TEXT.__objc_methlist: 0x4ec
+  __TEXT.__const: 0x3e8
+  __TEXT.__cstring: 0x733
+  __TEXT.__constg_swiftt: 0x144
+  __TEXT.__swift5_typeref: 0x163
+  __TEXT.__swift5_reflstr: 0x12e
+  __TEXT.__swift5_fieldmd: 0x130
+  __TEXT.__swift5_proto: 0x14
+  __TEXT.__swift5_types: 0x10
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__oslogstring: 0x2ac
+  __TEXT.__swift_as_entry: 0x4
+  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__swift_as_cont: 0x4
+  __TEXT.__unwind_info: 0x248
+  __TEXT.__eh_frame: 0xa8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x78
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_selrefs: 0x460
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__got: 0x3b0
+  __AUTH_CONST.__const: 0x1d8
+  __AUTH_CONST.__cfstring: 0x1e0
+  __AUTH_CONST.__objc_const: 0x778
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x638
+  __DATA.__objc_ivar: 0x58
+  __DATA.__data: 0x30
+  __DATA.__bss: 0x200
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__data: 0x240
+  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__common: 0x58
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
+  - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
+  - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 240D11D3-D823-3D34-8B81-5E994D419118
-  Functions: 0
-  Symbols:   33
-  CStrings:  0
+  UUID: ADDE86CD-0BD7-3894-AB52-60C2370D6DAA
+  Functions: 233
+  Symbols:   560
+  CStrings:  86
 
Symbols:
+ -[FFTSchemaFFTWrapper .cxx_destruct]
+ -[FFTSchemaFFTWrapper addErrors:]
+ -[FFTSchemaFFTWrapper addSkippedMessages:]
+ -[FFTSchemaFFTWrapper addTaggedMessages:]
+ -[FFTSchemaFFTWrapper clearErrors]
+ -[FFTSchemaFFTWrapper clearSkippedMessages]
+ -[FFTSchemaFFTWrapper clearTaggedMessages]
+ -[FFTSchemaFFTWrapper deleteErrors]
+ -[FFTSchemaFFTWrapper deleteFftId]
+ -[FFTSchemaFFTWrapper deleteNumTools]
+ -[FFTSchemaFFTWrapper deleteNumTypedValues]
+ -[FFTSchemaFFTWrapper deleteSkippedMessages]
+ -[FFTSchemaFFTWrapper deleteTaggedMessages]
+ -[FFTSchemaFFTWrapper dictionaryRepresentation]
+ -[FFTSchemaFFTWrapper errorsAtIndex:]
+ -[FFTSchemaFFTWrapper errorsCount]
+ -[FFTSchemaFFTWrapper errors]
+ -[FFTSchemaFFTWrapper fftId]
+ -[FFTSchemaFFTWrapper hasFftId]
+ -[FFTSchemaFFTWrapper hasNumTools]
+ -[FFTSchemaFFTWrapper hasNumTypedValues]
+ -[FFTSchemaFFTWrapper hash]
+ -[FFTSchemaFFTWrapper initWithDictionary:]
+ -[FFTSchemaFFTWrapper initWithJSON:]
+ -[FFTSchemaFFTWrapper isEqual:]
+ -[FFTSchemaFFTWrapper jsonData]
+ -[FFTSchemaFFTWrapper numTools]
+ -[FFTSchemaFFTWrapper numTypedValues]
+ -[FFTSchemaFFTWrapper qualifiedMessageName]
+ -[FFTSchemaFFTWrapper readFrom:]
+ -[FFTSchemaFFTWrapper setErrors:]
+ -[FFTSchemaFFTWrapper setFftId:]
+ -[FFTSchemaFFTWrapper setHasFftId:]
+ -[FFTSchemaFFTWrapper setHasNumTools:]
+ -[FFTSchemaFFTWrapper setHasNumTypedValues:]
+ -[FFTSchemaFFTWrapper setNumTools:]
+ -[FFTSchemaFFTWrapper setNumTypedValues:]
+ -[FFTSchemaFFTWrapper setSkippedMessages:]
+ -[FFTSchemaFFTWrapper setTaggedMessages:]
+ -[FFTSchemaFFTWrapper skippedMessagesAtIndex:]
+ -[FFTSchemaFFTWrapper skippedMessagesCount]
+ -[FFTSchemaFFTWrapper skippedMessages]
+ -[FFTSchemaFFTWrapper taggedMessagesAtIndex:]
+ -[FFTSchemaFFTWrapper taggedMessagesCount]
+ -[FFTSchemaFFTWrapper taggedMessages]
+ -[FFTSchemaFFTWrapper writeTo:]
+ -[FFTSchemaFFTWrapper(InstrumentationAdditions) getAnyEventType]
+ -[FFTSchemaFFTWrapper(InstrumentationAdditions) getTypeId]
+ -[FFTSchemaFFTWrapper(InstrumentationAdditions) getVersion]
+ -[FFTSchemaFFTWrapper(InstrumentationAdditions) isProvisional]
+ -[FFTSchemaRegistrationData .cxx_destruct]
+ -[FFTSchemaRegistrationData classifiedString]
+ -[FFTSchemaRegistrationData deleteClassifiedString]
+ -[FFTSchemaRegistrationData deleteEntityName]
+ -[FFTSchemaRegistrationData deletePropertyName]
+ -[FFTSchemaRegistrationData deleteTagMetadata]
+ -[FFTSchemaRegistrationData deleteToolId]
+ -[FFTSchemaRegistrationData dictionaryRepresentation]
+ -[FFTSchemaRegistrationData entityName]
+ -[FFTSchemaRegistrationData hasClassifiedString]
+ -[FFTSchemaRegistrationData hasEntityName]
+ -[FFTSchemaRegistrationData hasPropertyName]
+ -[FFTSchemaRegistrationData hasTagMetadata]
+ -[FFTSchemaRegistrationData hasToolId]
+ -[FFTSchemaRegistrationData hash]
+ -[FFTSchemaRegistrationData initWithDictionary:]
+ -[FFTSchemaRegistrationData initWithJSON:]
+ -[FFTSchemaRegistrationData isEqual:]
+ -[FFTSchemaRegistrationData jsonData]
+ -[FFTSchemaRegistrationData propertyName]
+ -[FFTSchemaRegistrationData readFrom:]
+ -[FFTSchemaRegistrationData setClassifiedString:]
+ -[FFTSchemaRegistrationData setEntityName:]
+ -[FFTSchemaRegistrationData setHasClassifiedString:]
+ -[FFTSchemaRegistrationData setHasEntityName:]
+ -[FFTSchemaRegistrationData setHasPropertyName:]
+ -[FFTSchemaRegistrationData setHasTagMetadata:]
+ -[FFTSchemaRegistrationData setHasToolId:]
+ -[FFTSchemaRegistrationData setPropertyName:]
+ -[FFTSchemaRegistrationData setTagMetadata:]
+ -[FFTSchemaRegistrationData setToolId:]
+ -[FFTSchemaRegistrationData tagMetadata]
+ -[FFTSchemaRegistrationData toolId]
+ -[FFTSchemaRegistrationData writeTo:]
+ -[FFTSchemaRegistrationError .cxx_destruct]
+ -[FFTSchemaRegistrationError deleteErrorMessage]
+ -[FFTSchemaRegistrationError deleteRegistration]
+ -[FFTSchemaRegistrationError dictionaryRepresentation]
+ -[FFTSchemaRegistrationError errorMessage]
+ -[FFTSchemaRegistrationError hasErrorMessage]
+ -[FFTSchemaRegistrationError hasRegistration]
+ -[FFTSchemaRegistrationError hash]
+ -[FFTSchemaRegistrationError initWithDictionary:]
+ -[FFTSchemaRegistrationError initWithJSON:]
+ -[FFTSchemaRegistrationError isEqual:]
+ -[FFTSchemaRegistrationError jsonData]
+ -[FFTSchemaRegistrationError readFrom:]
+ -[FFTSchemaRegistrationError registration]
+ -[FFTSchemaRegistrationError setErrorMessage:]
+ -[FFTSchemaRegistrationError setHasErrorMessage:]
+ -[FFTSchemaRegistrationError setHasRegistration:]
+ -[FFTSchemaRegistrationError setRegistration:]
+ -[FFTSchemaRegistrationError writeTo:]
+ <redacted>
+ OBJC_IVAR_$_FFTSchemaFFTWrapper._errors
+ OBJC_IVAR_$_FFTSchemaFFTWrapper._fftId
+ OBJC_IVAR_$_FFTSchemaFFTWrapper._has
+ OBJC_IVAR_$_FFTSchemaFFTWrapper._numTools
+ OBJC_IVAR_$_FFTSchemaFFTWrapper._numTypedValues
+ OBJC_IVAR_$_FFTSchemaFFTWrapper._skippedMessages
+ OBJC_IVAR_$_FFTSchemaFFTWrapper._taggedMessages
+ OBJC_IVAR_$_FFTSchemaRegistrationData._classifiedString
+ OBJC_IVAR_$_FFTSchemaRegistrationData._entityName
+ OBJC_IVAR_$_FFTSchemaRegistrationData._propertyName
+ OBJC_IVAR_$_FFTSchemaRegistrationData._tagMetadata
+ OBJC_IVAR_$_FFTSchemaRegistrationData._toolId
+ OBJC_IVAR_$_FFTSchemaRegistrationError._errorMessage
+ OBJC_IVAR_$_FFTSchemaRegistrationError._registration
+ _FFTSchemaFFTWrapperReadFrom
+ _FFTSchemaRegistrationDataReadFrom
+ _FFTSchemaRegistrationErrorReadFrom
+ _LRSchemaLRDataClassificationMetadataReadFrom
+ _OBJC_CLASS_$_AssistantSiriAnalytics
+ _OBJC_CLASS_$_FFTSchemaFFTWrapper
+ _OBJC_CLASS_$_FFTSchemaRegistrationData
+ _OBJC_CLASS_$_FFTSchemaRegistrationError
+ _OBJC_CLASS_$_LRSchemaLRDataClassificationMetadata
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDateComponentsFormatter
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSDateIntervalFormatter
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSPersonNameComponentsFormatter
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_SISchemaInstrumentationMessage
+ _OBJC_CLASS_$_SISchemaTopLevelUnionType
+ _OBJC_CLASS_$_SISchemaUUID
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_FFTSchemaFFTWrapper._hasFftId
+ _OBJC_IVAR_$_FFTSchemaRegistrationData._hasClassifiedString
+ _OBJC_IVAR_$_FFTSchemaRegistrationData._hasEntityName
+ _OBJC_IVAR_$_FFTSchemaRegistrationData._hasPropertyName
+ _OBJC_IVAR_$_FFTSchemaRegistrationData._hasTagMetadata
+ _OBJC_IVAR_$_FFTSchemaRegistrationData._hasToolId
+ _OBJC_IVAR_$_FFTSchemaRegistrationError._hasErrorMessage
+ _OBJC_IVAR_$_FFTSchemaRegistrationError._hasRegistration
+ _OBJC_METACLASS_$_FFTSchemaFFTWrapper
+ _OBJC_METACLASS_$_FFTSchemaRegistrationData
+ _OBJC_METACLASS_$_FFTSchemaRegistrationError
+ _OBJC_METACLASS_$_NSObject
+ _OBJC_METACLASS_$_SISchemaInstrumentationMessage
+ _OBJC_METACLASS_$_SISchemaTopLevelUnionType
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _PBDataWriterWriteInt32Field
+ _PBDataWriterWriteStringField
+ _PBDataWriterWriteSubmessage
+ _PBReaderPlaceMark
+ _PBReaderReadString
+ _PBReaderRecallMark
+ _PBReaderSkipValueWithTag
+ _SISchemaUUIDReadFrom
+ __DATA__TtC27SiriAnalyticsToolKitSupport12Hillclimbing
+ __IVARS__TtC27SiriAnalyticsToolKitSupport12Hillclimbing
+ __METACLASS_DATA__TtC27SiriAnalyticsToolKitSupport12Hillclimbing
+ __OBJC_$_INSTANCE_METHODS_FFTSchemaFFTWrapper(InstrumentationAdditions)
+ __OBJC_$_INSTANCE_METHODS_FFTSchemaRegistrationData
+ __OBJC_$_INSTANCE_METHODS_FFTSchemaRegistrationError
+ __OBJC_$_INSTANCE_VARIABLES_FFTSchemaFFTWrapper
+ __OBJC_$_INSTANCE_VARIABLES_FFTSchemaRegistrationData
+ __OBJC_$_INSTANCE_VARIABLES_FFTSchemaRegistrationError
+ __OBJC_$_PROP_LIST_FFTSchemaFFTWrapper
+ __OBJC_$_PROP_LIST_FFTSchemaRegistrationData
+ __OBJC_$_PROP_LIST_FFTSchemaRegistrationError
+ __OBJC_CLASS_RO_$_FFTSchemaFFTWrapper
+ __OBJC_CLASS_RO_$_FFTSchemaRegistrationData
+ __OBJC_CLASS_RO_$_FFTSchemaRegistrationError
+ __OBJC_METACLASS_RO_$_FFTSchemaFFTWrapper
+ __OBJC_METACLASS_RO_$_FFTSchemaRegistrationData
+ __OBJC_METACLASS_RO_$_FFTSchemaRegistrationError
+ ___CFConstantStringClassReference
+ ___chkstk_darwin
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_allocate_value_buffer
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_memcpy1_1
+ ___swift_memcpy72_8
+ ___swift_memcpy73_8
+ ___swift_noop_void_return
+ ___swift_project_value_buffer
+ __objc_empty_cache
+ __os_log_impl
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ __swift_implicitisolationactor_to_executor_cast
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ _associated conformance 27SiriAnalyticsToolKitSupport15ExtractionErrorV0G4KindOSHAASQ
+ _get_enum_tag_for_layout_string 27SiriAnalyticsToolKitSupport26TypedValueExtractionResultO
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_alloc
+ _objc_allocWithZone
+ _objc_alloc_init
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$_setError
+ _objc_msgSend$addErrors:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addSkippedMessages:
+ _objc_msgSend$addTaggedMessages:
+ _objc_msgSend$areasOfInterest
+ _objc_msgSend$array
+ _objc_msgSend$classifiedString
+ _objc_msgSend$clearErrors
+ _objc_msgSend$clearSkippedMessages
+ _objc_msgSend$clearTaggedMessages
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$data
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$deleteGeneral
+ _objc_msgSend$deleteSensor
+ _objc_msgSend$deleteTool
+ _objc_msgSend$description
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$emitMessage:
+ _objc_msgSend$entityName
+ _objc_msgSend$errorMessage
+ _objc_msgSend$errors
+ _objc_msgSend$fftId
+ _objc_msgSend$filename
+ _objc_msgSend$general
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$hash
+ _objc_msgSend$init
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithNSUUID:
+ _objc_msgSend$intValue
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$isValidJSONObject:
+ _objc_msgSend$length
+ _objc_msgSend$name
+ _objc_msgSend$nameComponents
+ _objc_msgSend$null
+ _objc_msgSend$numTools
+ _objc_msgSend$numTypedValues
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$personHandle
+ _objc_msgSend$position
+ _objc_msgSend$propertyName
+ _objc_msgSend$registration
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$setClassifiedString:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setDateStyle:
+ _objc_msgSend$setEntityName:
+ _objc_msgSend$setErrorMessage:
+ _objc_msgSend$setErrors:
+ _objc_msgSend$setFftId:
+ _objc_msgSend$setGeneral:
+ _objc_msgSend$setKind:
+ _objc_msgSend$setNumTools:
+ _objc_msgSend$setNumTypedValues:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setPropertyName:
+ _objc_msgSend$setRegistration:
+ _objc_msgSend$setSensor:
+ _objc_msgSend$setSkippedMessages:
+ _objc_msgSend$setStyle:
+ _objc_msgSend$setTagMetadata:
+ _objc_msgSend$setTaggedMessages:
+ _objc_msgSend$setTimeStyle:
+ _objc_msgSend$setTool:
+ _objc_msgSend$setToolId:
+ _objc_msgSend$setUnitsStyle:
+ _objc_msgSend$sharedStream
+ _objc_msgSend$skippedMessages
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$stringFromDateComponents:
+ _objc_msgSend$stringFromDateInterval:
+ _objc_msgSend$stringFromPersonNameComponents:
+ _objc_msgSend$tagMetadata
+ _objc_msgSend$taggedMessages
+ _objc_msgSend$toolId
+ _objc_msgSend$type
+ _objc_msgSend$value
+ _objc_msgSend$whichProvenance_Type
+ _objc_msgSend$willProduceDictionaryRepresentation:
+ _objc_msgSendSuper2
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_opt_self
+ _objc_release
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x27
+ _objc_retain_x8
+ _objc_setProperty_nonatomic_copy
+ _objc_storeStrong
+ _os_log_type_enabled
+ _swift_allocBox
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_endAccess
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_projectBox
+ _swift_release
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x8
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _symbolic SS
+ _symbolic SS3key______5valuet 7ToolKit10TypedValueO
+ _symbolic SSSg
+ _symbolic SS_So36LRSchemaLRDataClassificationMetadataCt
+ _symbolic SaySo25FFTSchemaRegistrationDataCG
+ _symbolic SaySo26FFTSchemaRegistrationErrorCG
+ _symbolic Say_____G 27SiriAnalyticsToolKitSupport26TypedValueExtractionResultO
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 27SiriAnalyticsToolKitSupport12HillclimbingC
+ _symbolic _____ 27SiriAnalyticsToolKitSupport15ExtractionErrorV
+ _symbolic _____ 27SiriAnalyticsToolKitSupport15ExtractionErrorV0G4KindO
+ _symbolic _____ 27SiriAnalyticsToolKitSupport26TypedValueExtractionResultO
+ _symbolic _____ s5Int32V
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySS_So36LRSchemaLRDataClassificationMetadataCtG s23_ContiguousArrayStorageC
+ _symbolic _____ySo6NSUnitCG 10Foundation11MeasurementV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 27SiriAnalyticsToolKitSupport15ExtractionErrorV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 27SiriAnalyticsToolKitSupport26TypedValueExtractionResultO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____yyXlG s23_ContiguousArrayStorageC
+ _type_layout_string 27SiriAnalyticsToolKitSupport15ExtractionErrorV
+ _type_layout_string 27SiriAnalyticsToolKitSupport26TypedValueExtractionResultO
CStrings:
+ "Emitting hillclimbing data with uuid %{private}s"
+ "Extracted %{public}ld values, %{sensitive}s"
+ "Failed to create hillclimbing wrapper"
+ "Failed to emit hillclimbing error"
+ "Failed to emit hillclimbing message data"
+ "Failed to extract values from "
+ "Failed to format dateComponents "
+ "Failed to format dateInterval "
+ "Failed to save tag"
+ "Needed a type hint"
+ "No entity name from "
+ "No value for INPersonHandle"
+ "Nothing interesting from person "
+ "Nothing interesting from placemark "
+ "Skipping empty hillclimbing data"
+ "Unhandled context: %s"
+ "Unknown PrimitiveValue: TypedValueExtractor.Type"
+ "Unknown context: %s"
+ "appInFocusBundleId"
+ "attributedString"
+ "bluetoothDeviceType"
+ "classifiedString"
+ "classifying %{sensitive}s with %{sensitive}@"
+ "com.apple.MobileAddressBook#ContactEntity"
+ "com.apple.MobileAddressBook#ContactLabeledValueEntity"
+ "com.apple.MobileSMS#ConversationEntity"
+ "com.apple.aiml.instr.location"
+ "com.apple.aiml.instr.onScreen"
+ "com.apple.aiml.platform.fft.FFTWrapper"
+ "com.apple.aiml.platform.fft.ProvisionalFFTWrapper"
+ "com.apple.mobilecal#EventEntity"
+ "com.apple.mobilesafari#TabEntity"
+ "com.apple.mobilesafari#WindowEntity"
+ "com.apple.mobiletimer#TimerEntity"
+ "com.apple.omniSearch.SearchToolExtension.SearchTool"
+ "com.apple.shortcuts"
+ "com.apple.siri#ReadableMessageAppEntity"
+ "com.apple.siri.SiriNotificationsAppIntentsExtension#ReadableNotificationEntity"
+ "com.apple.siri.analytics"
+ "entityName"
+ "errorMessage"
+ "errors"
+ "fftId"
+ "i"
+ "intelligenceCommand"
+ "introductionNames"
+ "nowPlayingMediaItem"
+ "nowPlayingPlaybackState"
+ "numTools"
+ "numTypedValues"
+ "onScreenContentAppEntity"
+ "onScreenContentDocumentImage"
+ "onScreenContentEmailAddress"
+ "onScreenContentPhoneNumber"
+ "onScreenContentPostalAddress"
+ "onScreenContentUriLink"
+ "onScreenDateTime"
+ "propertyName"
+ "recentTranscript"
+ "registration"
+ "semanticLocation"
+ "siriRequestContext"
+ "skippedMessages"
+ "tagMetadata"
+ "taggedMessages"
+ "toolId"
+ "→Skipping %{sensitive}s"
+ "⛰️Emitted hillclimbing event with id:%{private}s"
+ "❌ Hit an error extracting %{sensitive}s and %{sensitive}s %{sensitive}s: %{sensitive}@"
+ "❌Failed to save tag"
+ "🟢 Pulling %{public}ld from %{sensitive}s"

```
