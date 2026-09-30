## ProactiveContextClient

> `/System/Library/PrivateFrameworks/ProactiveContextClient.framework/ProactiveContextClient`

```diff

-588.12.0.0.0
-  __TEXT.__text: 0x2b2ac
+610.0.11.0.0
+  __TEXT.__text: 0x2a4f4
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x29d4
-  __TEXT.__const: 0x420
-  __TEXT.__gcc_except_tab: 0x1180
-  __TEXT.__cstring: 0x2121
-  __TEXT.__oslogstring: 0x3fcf
+  __TEXT.__objc_methlist: 0x2a20
+  __TEXT.__const: 0x430
+  __TEXT.__gcc_except_tab: 0x10a0
+  __TEXT.__cstring: 0x20f2
+  __TEXT.__oslogstring: 0x3ca4
   __TEXT.__dlopen_cstrs: 0x9f
-  __TEXT.__unwind_info: 0xe80
-  __TEXT.__objc_classname: 0x999
-  __TEXT.__objc_methname: 0x60ed
-  __TEXT.__objc_methtype: 0x1666
-  __TEXT.__objc_stubs: 0x4b60
-  __DATA_CONST.__got: 0x498
-  __DATA_CONST.__const: 0x1430
-  __DATA_CONST.__objc_classlist: 0x238
+  __TEXT.__unwind_info: 0xe20
+  __TEXT.__objc_classname: 0x985
+  __TEXT.__objc_methname: 0x6151
+  __TEXT.__objc_methtype: 0x16da
+  __TEXT.__objc_stubs: 0x4c00
+  __DATA_CONST.__got: 0x4a0
+  __DATA_CONST.__const: 0x13d8
+  __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16e0
+  __DATA_CONST.__objc_selrefs: 0x1740
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x140
   __AUTH_CONST.__auth_got: 0x368
-  __AUTH_CONST.__const: 0xae0
-  __AUTH_CONST.__cfstring: 0x1ce0
-  __AUTH_CONST.__objc_const: 0x9d28
-  __AUTH_CONST.__objc_intobj: 0x2a0
-  __DATA.__objc_ivar: 0x304
-  __DATA.__data: 0x840
-  __DATA.__bss: 0x258
-  __DATA_DIRTY.__objc_data: 0x1630
+  __AUTH_CONST.__const: 0xb40
+  __AUTH_CONST.__cfstring: 0x1cc0
+  __AUTH_CONST.__objc_const: 0x9cd8
+  __AUTH_CONST.__objc_intobj: 0x288
+  __DATA.__objc_ivar: 0x300
+  __DATA.__data: 0x8a0
+  __DATA.__bss: 0x2a8
+  __DATA_DIRTY.__objc_data: 0x15e0
   __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/EventKit.framework/EventKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppPredictionFoundation.framework/AppPredictionFoundation
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1347966F-D2FF-329F-A930-28EEC4D320A8
-  Functions: 1203
-  Symbols:   4665
-  CStrings:  2087
+  UUID: A35EE952-9F3E-34B0-B775-08513DB4B463
+  Functions: 1202
+  Symbols:   4663
+  CStrings:  2096
 
Symbols:
+ -[ATXMiloProvider .cxx_destruct]
+ -[ATXMiloProvider _isInferredModeEventEligibleForHistoricalLabelDonations:]
+ -[ATXMiloProvider _isInferredModeEventEligibleForMicrolocationLabelDonation:]
+ -[ATXMiloProvider _isUserFocusComputedModeEventEligibleForHistoricalLabelDonations:]
+ -[ATXMiloProvider _isUserFocusComputedModeEventEligibleForMicrolocationLabelDonation:]
+ -[ATXMiloProvider _schedulerForStreamName:]
+ -[ATXMiloProvider _subscribeToModeChanges]
+ -[ATXMiloProvider _subscribeToStreamWithPublisher:scheduler:sink:]
+ -[ATXMiloProvider _subscribeToStreamWithPublisher:scheduler:sink:].cold.1
+ -[ATXMiloProvider _subscribeToStreamWithPublisher:scheduler:sink:].cold.2
+ -[ATXMiloProvider _triggerHistoricalLabelDonationAtModeEndWithStoreEvent:]
+ -[ATXMiloProvider _triggerMicroLocationHistoricalLabelDonationWithStartDate:endDate:]
+ -[ATXMiloProvider _triggerMicroLocationHistoricalLabelDonationWithStartDate:endDate:].cold.1
+ -[ATXMiloProvider _triggerMicrolocationLabelingAtModeStartWithStoreEvent:]
+ -[ATXMiloProvider _triggerPredictionRequest]
+ -[ATXMiloProvider _triggerPredictionRequest].cold.1
+ -[ATXMiloProvider _truthLabelForMode:]
+ -[ATXMiloProvider _userDidEnterModeOrModeWasPredicted]
+ -[ATXMiloProvider _userDidExitModeOrModeWasNoLongerPredicted]
+ -[ATXMiloProvider _userDidExitModeOrModeWasNoLongerPredicted].cold.1
+ -[ATXMiloProvider connection]
+ -[ATXMiloProvider dealloc]
+ -[ATXMiloProvider initWithInferredModeStream:]
+ -[ATXMiloProvider requestPrediction]
+ -[ATXMiloProvider setConnection:]
+ -[ATXModeCalendarFeaturizer initWithLocationManager:andMiloProvider:]
+ -[ATXModeHeuristicClassifier initWithConfiguredModeService:locationManager:miloProvider:]
+ -[ATXModeMicrolocationFeaturizer _provideFeaturesWithCurrentULMap:]
+ -[ATXModeMicrolocationFeaturizer _provideFeaturesWithCurrentULMap:].cold.1
+ -[ATXModeMicrolocationFeaturizer connectionDidUpdatePredictionContext:]
+ -[ATXModeMicrolocationFeaturizer initWithMiloProvider:]
+ -[ATXModeMicrolocationFeaturizer initWithMiloProvider:].cold.1
+ GCC_except_table20
+ GCC_except_table27
+ _OBJC_CLASS_$_ATXMiloProvider
+ _OBJC_CLASS_$_ULLabel
+ _OBJC_CLASS_$_ULUpdateConfiguration
+ _OBJC_IVAR_$_ATXMiloProvider._coalescingTimerForHistoricalLabelDonations
+ _OBJC_IVAR_$_ATXMiloProvider._coalescingTimerForLabelDonation
+ _OBJC_IVAR_$_ATXMiloProvider._coalescingTimerForPrediction
+ _OBJC_IVAR_$_ATXMiloProvider._connection
+ _OBJC_IVAR_$_ATXMiloProvider._inferredModeScheduler
+ _OBJC_IVAR_$_ATXMiloProvider._inferredModeStream
+ _OBJC_IVAR_$_ATXMiloProvider._inferredModeStreamSink
+ _OBJC_IVAR_$_ATXMiloProvider._queue
+ _OBJC_IVAR_$_ATXMiloProvider._timeBuffer
+ _OBJC_IVAR_$_ATXMiloProvider._userComputedModeScheduler
+ _OBJC_IVAR_$_ATXMiloProvider._userComputedModeStreamSink
+ _OBJC_IVAR_$_ATXMiloProvider._userFocusComputedModeStream
+ _OBJC_IVAR_$_ATXModeCalendarFeaturizer._miloProvider
+ _OBJC_IVAR_$_ATXModeClassifier._miloProvider
+ _OBJC_IVAR_$_ATXModeMicrolocationFeaturizer._connection
+ _OBJC_METACLASS_$_ATXMiloProvider
+ __OBJC_$_INSTANCE_METHODS_ATXMiloProvider
+ __OBJC_$_INSTANCE_VARIABLES_ATXMiloProvider
+ __OBJC_$_PROP_LIST_ATXMiloProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ULConnectionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ULConnectionDelegate
+ __OBJC_$_PROTOCOL_REFS_ULConnectionDelegate
+ __OBJC_CLASS_RO_$_ATXMiloProvider
+ __OBJC_LABEL_PROTOCOL_$_ULConnectionDelegate
+ __OBJC_METACLASS_RO_$_ATXMiloProvider
+ __OBJC_PROTOCOL_$_ULConnectionDelegate
+ ___46-[ATXMiloProvider initWithInferredModeStream:]_block_invoke
+ ___46-[ATXMiloProvider initWithInferredModeStream:]_block_invoke_2
+ ___46-[ATXMiloProvider initWithInferredModeStream:]_block_invoke_3
+ ___66-[ATXMiloProvider _subscribeToStreamWithPublisher:scheduler:sink:]_block_invoke
+ ___66-[ATXMiloProvider _subscribeToStreamWithPublisher:scheduler:sink:]_block_invoke.22
+ ___66-[ATXMiloProvider _subscribeToStreamWithPublisher:scheduler:sink:]_block_invoke.22.cold.1
+ ___66-[ATXMiloProvider _subscribeToStreamWithPublisher:scheduler:sink:]_block_invoke.cold.1
+ ___71-[ATXModeMicrolocationFeaturizer connectionDidUpdatePredictionContext:]_block_invoke
+ ___ATXDispatchAsyncWithStrongSelf_block_invoke
+ _____atxlog_handle_client_donations_block_invoke
+ _____atxlog_handle_document_predictor_block_invoke
+ _____atxlog_handle_menu_items_block_invoke
+ _____atxlog_handle_ml_inference_block_invoke
+ _____atxlog_handle_screen_entities_block_invoke
+ ___atxlog_handle_client_donations
+ ___atxlog_handle_client_donations.cold.1
+ ___atxlog_handle_client_donations.log
+ ___atxlog_handle_client_donations.onceToken
+ ___atxlog_handle_document_predictor
+ ___atxlog_handle_document_predictor.cold.1
+ ___atxlog_handle_document_predictor.log
+ ___atxlog_handle_document_predictor.onceToken
+ ___atxlog_handle_menu_items
+ ___atxlog_handle_menu_items.cold.1
+ ___atxlog_handle_menu_items.log
+ ___atxlog_handle_menu_items.onceToken
+ ___atxlog_handle_ml_inference
+ ___atxlog_handle_ml_inference.cold.1
+ ___atxlog_handle_ml_inference.log
+ ___atxlog_handle_ml_inference.onceToken
+ ___atxlog_handle_screen_entities
+ ___atxlog_handle_screen_entities.cold.1
+ ___atxlog_handle_screen_entities.log
+ ___atxlog_handle_screen_entities.onceToken
+ ___block_descriptor_40_e40_v16?0"ATXModeMicrolocationFeaturizer"8l
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_literal_global.128
+ ___block_literal_global.131
+ ___block_literal_global.134
+ ___block_literal_global.137
+ ___block_literal_global.140
+ _hasMotionActivity._pasOnceToken7
+ _objc_msgSend$_isInferredModeEventEligibleForMicrolocationLabelDonation:
+ _objc_msgSend$_isUserFocusComputedModeEventEligibleForMicrolocationLabelDonation:
+ _objc_msgSend$_provideFeaturesWithCurrentULMap:
+ _objc_msgSend$_triggerPredictionRequest
+ _objc_msgSend$addLabel:
+ _objc_msgSend$addLabel:betweenStartDate:andEndDate:
+ _objc_msgSend$connect
+ _objc_msgSend$connection
+ _objc_msgSend$createServiceIdentifierForToken:
+ _objc_msgSend$currentMap
+ _objc_msgSend$disconnect
+ _objc_msgSend$initWithConfiguredModeService:locationManager:miloProvider:
+ _objc_msgSend$initWithDelegate:serviceIdentifier:
+ _objc_msgSend$initWithIsLowLatency:
+ _objc_msgSend$initWithLocationManager:andMiloProvider:
+ _objc_msgSend$initWithMiloProvider:
+ _objc_msgSend$initWithName:
+ _objc_msgSend$isEqualToTuple2:
+ _objc_msgSend$isMapValid
+ _objc_msgSend$isPredictionValid
+ _objc_msgSend$labels
+ _objc_msgSend$mapItems
+ _objc_msgSend$numberOfLabelsInSameSpaceForMapItem:
+ _objc_msgSend$predictionContext
+ _objc_msgSend$requestPrediction
+ _objc_msgSend$serviceState
+ _objc_msgSend$setConnection:
+ _objc_msgSend$startUpdatingWithConfiguration:
+ _objc_msgSend$uniqueIdentifier
- -[ATXMicrolocationLocalization .cxx_destruct]
- -[ATXMicrolocationLocalization _triggerMicroLocationLocalization]
- -[ATXMicrolocationLocalization init]
- -[ATXMicrolocationLocalization initiateLocalization]
- -[ATXMicrolocationRecordingTrigger .cxx_destruct]
- -[ATXMicrolocationRecordingTrigger _donateTruthLabelForTriggerUUID:truthLabel:]
- -[ATXMicrolocationRecordingTrigger _isInferredModeEventEligibleForHistoricalLabelDonations:]
- -[ATXMicrolocationRecordingTrigger _isInferredModeEventEligibleForMicrolocationRecording:]
- -[ATXMicrolocationRecordingTrigger _isUserFocusComputedModeEventEligibleForHistoricalLabelDonations:]
- -[ATXMicrolocationRecordingTrigger _isUserFocusComputedModeEventEligibleForMicrolocationRecording:]
- -[ATXMicrolocationRecordingTrigger _schedulerForStreamName:]
- -[ATXMicrolocationRecordingTrigger _subscribeToModeChanges]
- -[ATXMicrolocationRecordingTrigger _subscribeToStreamWithPublisher:scheduler:sink:]
- -[ATXMicrolocationRecordingTrigger _subscribeToStreamWithPublisher:scheduler:sink:].cold.1
- -[ATXMicrolocationRecordingTrigger _subscribeToStreamWithPublisher:scheduler:sink:].cold.2
- -[ATXMicrolocationRecordingTrigger _triggerHistoricalLabelDonationAtModeEndWithStoreEvent:]
- -[ATXMicrolocationRecordingTrigger _triggerMicroLocationHistoricalLabelDonationWithStartDate:endDate:]
- -[ATXMicrolocationRecordingTrigger _triggerMicroLocationRecordingScan]
- -[ATXMicrolocationRecordingTrigger _triggerMicroLocationRecordingScan].cold.1
- -[ATXMicrolocationRecordingTrigger _triggerMicrolocationRecordingAtModeStartWithStoreEvent:]
- -[ATXMicrolocationRecordingTrigger _truthLabelForMode:]
- -[ATXMicrolocationRecordingTrigger _userDidEnterModeOrModeWasPredicted]
- -[ATXMicrolocationRecordingTrigger _userDidExitModeOrModeWasNoLongerPredicted]
- -[ATXMicrolocationRecordingTrigger _userDidExitModeOrModeWasNoLongerPredicted].cold.1
- -[ATXMicrolocationRecordingTrigger dealloc]
- -[ATXMicrolocationRecordingTrigger initWithInferredModeStream:]
- -[ATXModeHeuristicClassifier initWithConfiguredModeService:locationManager:]
- -[ATXModeMicrolocationFeaturizer _processLocalizationEvent:]
- -[ATXModeMicrolocationFeaturizer _provideFeaturesWithLocalizationEvent:]
- -[ATXModeMicrolocationFeaturizer _provideFeaturesWithLocalizationEvent:].cold.1
- GCC_except_table26
- _OBJC_CLASS_$_ATXMicrolocationLocalization
- _OBJC_CLASS_$_ATXMicrolocationRecordingTrigger
- _OBJC_IVAR_$_ATXMicrolocationLocalization._coalescingTimer
- _OBJC_IVAR_$_ATXMicrolocationLocalization._queue
- _OBJC_IVAR_$_ATXMicrolocationRecordingTrigger._coalescingTimerForHistoricalLabelDonations
- _OBJC_IVAR_$_ATXMicrolocationRecordingTrigger._coalescingTimerForRecordingScans
- _OBJC_IVAR_$_ATXMicrolocationRecordingTrigger._inferredModeScheduler
- _OBJC_IVAR_$_ATXMicrolocationRecordingTrigger._inferredModeStream
- _OBJC_IVAR_$_ATXMicrolocationRecordingTrigger._inferredModeStreamSink
- _OBJC_IVAR_$_ATXMicrolocationRecordingTrigger._queue
- _OBJC_IVAR_$_ATXMicrolocationRecordingTrigger._timeBuffer
- _OBJC_IVAR_$_ATXMicrolocationRecordingTrigger._userComputedModeScheduler
- _OBJC_IVAR_$_ATXMicrolocationRecordingTrigger._userComputedModeStreamSink
- _OBJC_IVAR_$_ATXMicrolocationRecordingTrigger._userFocusComputedModeStream
- _OBJC_IVAR_$_ATXModeCalendarFeaturizer._microlocationLocalization
- _OBJC_IVAR_$_ATXModeClassifier._microlocationRecordingTrigger
- _OBJC_IVAR_$_ATXModeMicrolocationFeaturizer._scheduler
- _OBJC_IVAR_$_ATXModeMicrolocationFeaturizer._sink
- _OBJC_METACLASS_$_ATXMicrolocationLocalization
- _OBJC_METACLASS_$_ATXMicrolocationRecordingTrigger
- _OUTLINED_FUNCTION_5
- __OBJC_$_INSTANCE_METHODS_ATXMicrolocationLocalization
- __OBJC_$_INSTANCE_METHODS_ATXMicrolocationRecordingTrigger
- __OBJC_$_INSTANCE_VARIABLES_ATXMicrolocationLocalization
- __OBJC_$_INSTANCE_VARIABLES_ATXMicrolocationRecordingTrigger
- __OBJC_CLASS_RO_$_ATXMicrolocationLocalization
- __OBJC_CLASS_RO_$_ATXMicrolocationRecordingTrigger
- __OBJC_METACLASS_RO_$_ATXMicrolocationLocalization
- __OBJC_METACLASS_RO_$_ATXMicrolocationRecordingTrigger
- ___102-[ATXMicrolocationRecordingTrigger _triggerMicroLocationHistoricalLabelDonationWithStartDate:endDate:]_block_invoke
- ___102-[ATXMicrolocationRecordingTrigger _triggerMicroLocationHistoricalLabelDonationWithStartDate:endDate:]_block_invoke.cold.1
- ___36-[ATXMicrolocationLocalization init]_block_invoke
- ___48-[ATXModeMicrolocationFeaturizer beginListening]_block_invoke
- ___48-[ATXModeMicrolocationFeaturizer beginListening]_block_invoke.36
- ___48-[ATXModeMicrolocationFeaturizer beginListening]_block_invoke_2
- ___48-[ATXModeMicrolocationFeaturizer beginListening]_block_invoke_2.cold.1
- ___49-[ATXModeMicrolocationFeaturizer provideFeatures]_block_invoke
- ___49-[ATXModeMicrolocationFeaturizer provideFeatures]_block_invoke.25
- ___49-[ATXModeMicrolocationFeaturizer provideFeatures]_block_invoke_2
- ___49-[ATXModeMicrolocationFeaturizer provideFeatures]_block_invoke_2.cold.1
- ___63-[ATXMicrolocationRecordingTrigger initWithInferredModeStream:]_block_invoke
- ___63-[ATXMicrolocationRecordingTrigger initWithInferredModeStream:]_block_invoke_2
- ___70-[ATXMicrolocationRecordingTrigger _triggerMicroLocationRecordingScan]_block_invoke
- ___70-[ATXMicrolocationRecordingTrigger _triggerMicroLocationRecordingScan]_block_invoke.cold.1
- ___79-[ATXMicrolocationRecordingTrigger _donateTruthLabelForTriggerUUID:truthLabel:]_block_invoke
- ___79-[ATXMicrolocationRecordingTrigger _donateTruthLabelForTriggerUUID:truthLabel:]_block_invoke.cold.1
- ___83-[ATXMicrolocationRecordingTrigger _subscribeToStreamWithPublisher:scheduler:sink:]_block_invoke
- ___83-[ATXMicrolocationRecordingTrigger _subscribeToStreamWithPublisher:scheduler:sink:]_block_invoke.22
- ___83-[ATXMicrolocationRecordingTrigger _subscribeToStreamWithPublisher:scheduler:sink:]_block_invoke.22.cold.1
- ___83-[ATXMicrolocationRecordingTrigger _subscribeToStreamWithPublisher:scheduler:sink:]_block_invoke.cold.1
- ___block_descriptor_48_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_48_e8_32s_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_48_e8_32w_e22_v16?0"BMStoreEvent"8lw32l8
- ___block_descriptor_64_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
- _hasMotionActivity._pasOnceToken6
- _objc_msgSend$Localization
- _objc_msgSend$MicroLocation
- _objc_msgSend$_donateTruthLabelForTriggerUUID:truthLabel:
- _objc_msgSend$_isInferredModeEventEligibleForMicrolocationRecording:
- _objc_msgSend$_isUserFocusComputedModeEventEligibleForMicrolocationRecording:
- _objc_msgSend$_processLocalizationEvent:
- _objc_msgSend$_provideFeaturesWithLocalizationEvent:
- _objc_msgSend$_triggerMicroLocationLocalization
- _objc_msgSend$_triggerMicroLocationRecordingScan
- _objc_msgSend$_triggerMicrolocationRecordingAtModeStartWithStoreEvent:
- _objc_msgSend$absoluteTimeStamp
- _objc_msgSend$clientBundleID
- _objc_msgSend$donateMicroLocationTruthTagWithTagUUID:correspondingToTriggerUUID:handler:
- _objc_msgSend$donateMicroLocationTruthTagWithTagUUID:forRecordingEventsBetweenDate:andDate:handler:
- _objc_msgSend$getRecordingTriggerUUIDAndRequestMicroLocationRecordingScanWithAdditionalInformation:shouldForceRecording:handler:
- _objc_msgSend$initWithConfiguredModeService:locationManager:
- _objc_msgSend$initiateLocalization
- _objc_msgSend$label
- _objc_msgSend$localizedDescription
- _objc_msgSend$maxProbability
- _objc_msgSend$maxProbabilityLabel
- _objc_msgSend$probability
- _objc_msgSend$probabilityVector
- _objc_msgSend$requestCurrentMicroLocationWithAdditionalInformation:
CStrings:
+ "!"
+ "@\"ATXMiloProvider\""
+ "@\"ULConnection\""
+ "ATXMiloProvider"
+ "ATXMiloProvider.Modes.%@.%@"
+ "ATXMiloProvider: sink is nil"
+ "ATXMiloProviderTimeBufferKey"
+ "ATXModeMicrolocationFeaturizer.m"
+ "T@\"ULConnection\",&,N,V_connection"
+ "ULConnectionDelegate"
+ "[%@][%@] Connection unavilable, Unable to label scans between dates"
+ "[%@][%@] Device is predicted (at %{private}f) to be at a work microlocation"
+ "[%@][%@] Device was predicted (at %{private}f) to not be at a work microlocation"
+ "[%@][%@] Got invalid MiLo prediction, return empty feature set"
+ "[%@][%@] Initiating prediction scan in %f seconds"
+ "[%@][%@] Invalid microlocation map"
+ "[%@][%@] MiLo prediction received, uniqueIdentifier: %@, isPredictionValid: %@, isMapValid: %@"
+ "[%@][%@] Milo service state suspended"
+ "[%@][%@] Probability that this device is not at work microlocation [labled:%@]: %{private}f"
+ "[%@][%@] Starting Microlocation Labeling"
+ "[%@][%@] Triggering prediction request now"
+ "[%@][%@] ULConnection unavilable"
+ "[%@][%@] Warning: Prediction scan was unexpectedly delayed by more than %f seconds"
+ "[%@][%@] analyzing predicted Microlocation for this device"
+ "_coalescingTimerForLabelDonation"
+ "_coalescingTimerForPrediction"
+ "_connection"
+ "_isInferredModeEventEligibleForMicrolocationLabelDonation:"
+ "_isUserFocusComputedModeEventEligibleForMicrolocationLabelDonation:"
+ "_miloProvider"
+ "_provideFeaturesWithCurrentULMap:"
+ "_triggerMicrolocationLabelingAtModeStartWithStoreEvent:"
+ "_triggerPredictionRequest"
+ "addLabel:"
+ "addLabel:betweenStartDate:andEndDate:"
+ "client_donations"
+ "com.apple.ULConnectionDelgetae.queue"
+ "com.apple.proactive.ProactiveContextClient"
+ "com.apple.proactive.ProactiveContextClient.ATXMiloProvider.queue"
+ "connect"
+ "connection"
+ "connection:didEnableMicrolocationAtCurrentLocationWithError:"
+ "connection:didFailWithError:"
+ "connection:didUpdatePrediction:"
+ "connection:didUpdateServiceStatus:"
+ "connectionDidUpdateMap:"
+ "connectionDidUpdatePredictionContext:"
+ "createServiceIdentifierForToken:"
+ "currentMap"
+ "disconnect"
+ "documentPredictor"
+ "inference"
+ "initWithConfiguredModeService:locationManager:miloProvider:"
+ "initWithDelegate:serviceIdentifier:"
+ "initWithIsLowLatency:"
+ "initWithLocationManager:andMiloProvider:"
+ "initWithMiloProvider:"
+ "initWithName:"
+ "isEqualToTuple2:"
+ "isMapValid"
+ "isPredictionValid"
+ "labels"
+ "mapItems"
+ "menuItems"
+ "miloProvider must not be nil."
+ "numberOfLabelsInSameSpaceForMapItem:"
+ "predictionContext"
+ "requestPrediction"
+ "screenEntities"
+ "serviceState"
+ "setConnection:"
+ "startUpdatingWithConfiguration:"
+ "uniqueIdentifier"
+ "v16@?0@\"ATXModeMicrolocationFeaturizer\"8"
+ "v24@0:8@\"ULConnection\"16"
+ "v32@0:8@\"ULConnection\"16@\"NSError\"24"
+ "v32@0:8@\"ULConnection\"16@\"ULPrediction\"24"
+ "v32@0:8@\"ULConnection\"16@\"ULServiceStatus\"24"
- "00000000-0000-0000-0000-000000000000"
- "@\"ATXMicrolocationLocalization\""
- "@\"ATXMicrolocationRecordingTrigger\""
- "ATXMicrolocationLocalization"
- "ATXMicrolocationRecordingTrigger"
- "ATXMicrolocationRecordingTrigger.Modes.%@.%@"
- "ATXMicrolocationRecordingTrigger: sink is nil"
- "ATXMicrolocationRecordingTriggerTimeBufferKey"
- "FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF"
- "FocusModes.Microlocation"
- "Localization"
- "MicroLocation"
- "[%@][%@]  Error encountered while requesting MiLo recording scan: %{public}s"
- "[%@][%@]  Successfully requested MiLo recording scan"
- "[%@][%@] Device is predicted to be at a work microlocation"
- "[%@][%@] Device was predicted to not be at a work microlocation"
- "[%@][%@] Donating truth label: %@ for triggerId: %@"
- "[%@][%@] Error encountered while donating historical labels: %{public}s"
- "[%@][%@] Error encountered while requesting MiLo recording scan: %{public}s"
- "[%@][%@] Error fetching last event: %@"
- "[%@][%@] Fetching predicted Microlocation for this device"
- "[%@][%@] Generated triggerId: %@"
- "[%@][%@] Initiating localization scan in %f seconds"
- "[%@][%@] Nil BMMicroLocationRestrictedLocalizationEvent"
- "[%@][%@] Probability that this device is at a work microlocation: %{private}f"
- "[%@][%@] Probability that this device is at an unknown microlocation: %{private}f"
- "[%@][%@] Probability that this device is outside of a work microlocation: %{private}f"
- "[%@][%@] Received new MicroLocation Localization event: %@"
- "[%@][%@] Starting Microlocation recording scan"
- "[%@][%@] Successfully donated MiLo label %@ for triggerId: %@"
- "[%@][%@] Successfully donated historical labels"
- "[%@][%@] Successfully fetched last event from BMMicroLocationRestrictedLocalizationStream"
- "[%@][%@] TriggerId was unexpectedly nil"
- "[%@][%@] Triggering localization scan now"
- "[%@][%@] Warning: Localization scan was unexpectedly delayed by more than %f seconds"
- "[%@][%@] listening to MicroLocation Localization events: %@"
- "[%@][%@] registering for real time events from the BiomeMicroLocationRestrictedLocalizationEventStream"
- "[%@][%@] successfully finished listening to MicroLocation Localization events"
- "_coalescingTimer"
- "_coalescingTimerForRecordingScans"
- "_donateTruthLabelForTriggerUUID:truthLabel:"
- "_isInferredModeEventEligibleForMicrolocationRecording:"
- "_isUserFocusComputedModeEventEligibleForMicrolocationRecording:"
- "_microlocationLocalization"
- "_microlocationRecordingTrigger"
- "_processLocalizationEvent:"
- "_provideFeaturesWithLocalizationEvent:"
- "_triggerMicroLocationLocalization"
- "_triggerMicroLocationRecordingScan"
- "_triggerMicrolocationRecordingAtModeStartWithStoreEvent:"
- "absoluteTimeStamp"
- "clientBundleID"
- "com.apple.BiomeMicroLocationRestrictedLocalizationEvent.queue"
- "com.apple.proactive.ProactiveContextClient.ATXMicrolocationLocalization.queue"
- "com.apple.proactive.ProactiveContextClient.ATXMicrolocationRecordingTrigger.queue"
- "donateMicroLocationTruthTagWithTagUUID:correspondingToTriggerUUID:handler:"
- "donateMicroLocationTruthTagWithTagUUID:forRecordingEventsBetweenDate:andDate:handler:"
- "focus-mode"
- "getRecordingTriggerUUIDAndRequestMicroLocationRecordingScanWithAdditionalInformation:shouldForceRecording:handler:"
- "initWithConfiguredModeService:locationManager:"
- "initiateLocalization"
- "label"
- "localizedDescription"
- "maxProbability"
- "maxProbabilityLabel"
- "probability"
- "probabilityVector"
- "requestCurrentMicroLocationWithAdditionalInformation:"

```
