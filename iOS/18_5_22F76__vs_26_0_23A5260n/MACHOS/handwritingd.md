## handwritingd

> `/usr/libexec/handwritingd`

```diff

-521.7.100.0.0
-  __TEXT.__text: 0x151d4
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_stubs: 0x3160
-  __TEXT.__objc_methlist: 0xc88
+544.0.0.0.0
+  __TEXT.__text: 0x13e6c
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__objc_stubs: 0x2ba0
+  __TEXT.__objc_methlist: 0xd08
   __TEXT.__dlopen_cstrs: 0x4f
-  __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x1ecc
-  __TEXT.__cstring: 0x134d
-  __TEXT.__objc_methname: 0x393c
-  __TEXT.__objc_classname: 0x274
-  __TEXT.__objc_methtype: 0x9e2
-  __TEXT.__oslogstring: 0x1b2c
-  __TEXT.__unwind_info: 0x7b0
-  __DATA_CONST.__auth_got: 0x3f8
-  __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0x768
-  __DATA_CONST.__cfstring: 0xf00
-  __DATA_CONST.__objc_classlist: 0x70
+  __TEXT.__const: 0x80
+  __TEXT.__gcc_except_tab: 0x1960
+  __TEXT.__cstring: 0x126b
+  __TEXT.__objc_methname: 0x33eb
+  __TEXT.__objc_classname: 0x29f
+  __TEXT.__objc_methtype: 0xa73
+  __TEXT.__oslogstring: 0x1608
+  __TEXT.__unwind_info: 0x7a8
+  __DATA_CONST.__auth_got: 0x3c8
+  __DATA_CONST.__got: 0x308
+  __DATA_CONST.__const: 0x6b0
+  __DATA_CONST.__cfstring: 0xf40
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_doubleobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x118
-  __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x1570
-  __DATA.__objc_selrefs: 0xe38
-  __DATA.__objc_ivar: 0xf0
-  __DATA.__objc_data: 0x460
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA.__objc_const: 0x15f8
+  __DATA.__objc_selrefs: 0xcd8
+  __DATA.__objc_ivar: 0xec
+  __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x360
   __DATA.__bss: 0x80
-  __DATA.__common: 0x78
+  __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1AC89565-E283-316F-BFC6-3DE48B1E5B49
-  Functions: 275
-  Symbols:   246
-  CStrings:  1063
+  UUID: 90738F85-BA94-3BAB-9519-2A2E6768A5F6
+  Functions: 280
+  Symbols:   230
+  CStrings:  989
 
Symbols:
+ _OBJC_CLASS_$_CHDocumentLayoutAnalyzer
+ _OBJC_CLASS_$_CHSynthesisRequestConcreteHandler
+ _objc_retain_x10
- _CGRectGetMaxX
- _CGRectGetMaxY
- _CGRectGetWidth
- _CHPostProcessingStepOptionAdjustColumns
- _OBJC_CLASS_$_CHFastPathCharacterPersonalizerInterface
- _OBJC_CLASS_$_CHMultiScriptTextSynthesizer
- _OBJC_CLASS_$_CHPersonalizedSynthesisModelStatus
- _OBJC_CLASS_$_CHStrokeClassificationModel
- _OBJC_CLASS_$_CHSynthesisContractViolation
- _OBJC_CLASS_$_CHSynthesisModelHashes
- _OBJC_CLASS_$_CHSynthesisResult
- _OBJC_CLASS_$_CHSynthesisStyleInventory
- _OBJC_CLASS_$_CHTextSynthesizer
- _OBJC_CLASS_$_CHTokenizedMathResult
- _OBJC_CLASS_$_NSMutableString
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _objc_retain_x28
CStrings:
+ "@\"CHDocumentLayoutAnalyzer\""
+ "@\"CHRemoteDocumentLayoutAnalysisRequestHandler\""
+ "@\"CHSynthesisRequestConcreteHandler\""
+ "@56@0:8@16@24@32@40^@48"
+ "@60@0:8@16@24@32B40@44^@52"
+ "A valid queue is required to run document layout analysis"
+ "CHRemoteDocumentLayoutAnalysisRequestHandler"
+ "CHRemoteRequestHandlers: handleSynthesisStringChunkingRequest content %{sensitive}@ length %d"
+ "CHRemoteRequestHandlers: handleSynthesisStringChunkingRequest is not supported with synthesis_expansion=off"
+ "CHRemoteSynthesisRequestHandler: character inventory is frozen. Ignoring clear inventory request"
+ "Currently active document layout analysis requests: %li"
+ "Did not evict document layout analyzer. activeRequestCount=%lu, hasIdleLifetimeElapsed=%i"
+ "Document layout analyzer for eviction with idle lifetime=%1.2f"
+ "Document layout analyzer is already fully checked in."
+ "DocumentLayoutAnalysis"
+ "Evicted document layout analyzer"
+ "Loaded document layout analyzer"
+ "Remote document layout analysis cannot handle empty input drawings"
+ "Remote document layout analyzer cannot process an empty request"
+ "Style inventory debug view unsupported"
+ "Submit a new valid document layout analysis request"
+ "Submit valid drawings with one or more strokes for document layout analysis"
+ "Synthesizer contract violation found, result %{sensitive}@, expected %{sensitive}@ score %f"
+ "The document layout analysis request is invalid"
+ "The listener must be resumed to handle chunking string requests"
+ "The listener must be resumed to handle document layout analysis requests"
+ "_buildMultiLingualResultForRequest:recognitionLocales:recognizersByLocale:statisticsByLocale:outPrincipalLineResult:"
+ "_checkInDocumentLayoutAnalyzer"
+ "_checkOutDocumentLayoutAnalyzer"
+ "_computeTextRecognitionResultsForRequest:recognizer:recognizerCachingKey:isTopLocale:writingStatistics:outPrincipalPoints:"
+ "_concreteHandler"
+ "_documentLayoutAnalysisRequestHandler"
+ "_documentLayoutAnalyzer"
+ "_isValidRemoteDocumentLayoutAnalysisRequest:bundleIdentifier:error:"
+ "_stageEvictionOfDocumentLayoutAnalyzerWithTargetIdleLifetime:"
+ "addToHolderPersonalizedCharacterWithId:"
+ "analyzeDrawing:strokeIdentifiers:contextStrokeIdentifiers:options:shouldCancel:"
+ "b"
+ "clearInventory"
+ "contextStrokeIdentifiers"
+ "createPersonalizationCandidatesForAll:"
+ "enumeratePersonalizedCandidatesWithBlock:"
+ "evictInventory"
+ "handleDocumentLayoutAnalysisRequest:withReply:"
+ "handleInventoryRequest:reply:"
+ "handleSynthesisRequest:reply:"
+ "handleSynthesisStringChunkingRequest:withReply:"
+ "handleSynthesisStringChunkingRequest:withReply:bundleIdentifier:"
+ "hasPersonalizationAvailable"
+ "hasStyleInventory"
+ "initWithServerQueue:recognitionHandler:"
+ "initWithStyleComputeBlock:"
+ "inventoryContainsSampleMatchingRequest:"
+ "inventoryStatus"
+ "isReadyForCharacterInventorySynthesis"
+ "isValidRemoteSynthesisRequest:bundleIdentifier:error:"
+ "lastInventoryCharacterStyleTimeStamp"
+ "resultByAppendingInventoryContents"
+ "retrieveActivationMatrixForDrawing:recognitionEngineCachingKey:outStrokeIndexMapping:outStrokeEndings:outPrincipalPoints:"
+ "shouldFreezeCharacterInventory"
+ "textRecognitionResultForDrawing:options:writingStatistics:principalPoints:shouldCancel:"
+ "unsafeCheckInStyleInventory"
+ "unsafeCheckOutStyleInventory"
+ "unsafeCheckOutTextSynthesizer"
+ "unsafeCleanupFastPathCharacters"
+ "unsafeClearStyleInventory"
+ "unsafeEvictStyleInventory"
+ "unsafeEvictTextSynthesizer"
+ "unsafeSynthesisChunkingRequest:"
+ "updateInventoryStylePredictionsWithCompletion:"
+ "v16@?0@\"CHSynthesisStyleInventoryStatus\"8"
+ "v32@0:8@\"CHRemoteDocumentLayoutAnalysisRequest\"16@?<v@?@\"CHDocumentLayoutAnalysisTileResult\"@\"NSError\">24"
+ "v32@0:8@\"CHRemoteRecognitionRequest\"16@?<v@?@\"CHTokenizedResult\"@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"CHRemoteSynthesisStringChunkingRequest\"16@?<v@?@\"CHTextSynthesizerChunkedData\"@\"NSError\">24"
+ "v32@?0@\"CHTokenizedResult\"8@\"NSArray\"16@\"NSError\"24"
+ "v32@?0Q8@\"CHDrawing\"16@\"NSString\"24"
- "%@\n"
- "@\"<CHSynthesizingText><CHSynthesizingTextInternal>\""
- "@\"CHFastPathCharacterPersonalizerInterface\""
- "@\"CHStrokeClassificationModel\""
- "@\"CHSynthesisResult\"48@?0@\"NSString\"8Q16Q24@?<v@?@\"CHSynthesisResult\"@\"NSError\">32@?<@\"NSArray\"@?@\"NSArray\">40"
- "@\"CHSynthesisStyleInventory\""
- "@32@0:8@16^B24"
- "@48@0:8@16@24@32@40"
- "@52@0:8@16@24@32B40@44"
- "A valid queue is required to run style inventory requests"
- "A valid queue is required to run synthesis"
- "Batch samples size (%lu) is larger than the batch size (%lu)"
- "CHRemoteSynthesisRequestHandler: Synthesise content %{sensitive}@ with style %{sensitive}@ with initial drawing %@"
- "CHRemoteSynthesisRequestHandler: fast Path synthesis found sufficient digit coverage from the inventory to trigger the character inventory preparation : %@"
- "CHRemoteSynthesisRequestTypeGeneration: style prediction from the textSynthesizer is nil for input style sample with content %{sensitive}@"
- "Computing style prediction for %lu samples out of %lu samples without style prediction."
- "Diffusion model (Latin) is not ready. The model hash could not be validated"
- "Diffusion model hash has changed (old: %@, new: %@). The inventory samples embedding need to be recomputed."
- "Evicted style inventory"
- "Evicted synthesizer"
- "Fast path character builder created"
- "Invalid synthesis request priority specified"
- "Invalid synthesis request type specified"
- "Invalid tokenized result type provided: %@"
- "Inventory data ingestion: (embedding prediction) sample with unsupported script. This sample will be removed: %{sensitive}@"
- "Inventory data ingestion: Script prediction for tokenized text results is non-supported script for string: %{sensitive}@"
- "Inventory request can't have both removedStrokeIdentifiers and tokenizedResult non-nil"
- "Loaded style inventory"
- "Loaded synthesizer"
- "Not possible to create a fast path character builder, inventory is null."
- "Number of segment stroke indexes not equal to segment contents length"
- "Only fast path queries should end up on non-synchronized synthesis queues"
- "Remote request handled on synchronized synthesis queue=%@"
- "Sample [%lu] \"%{sensitive}@\" numStrokes=%lu"
- "Sending message to save the style inventory if needed"
- "Skipping style inventory lookup"
- "Style inventory has not been checked out"
- "Style inventory is nil "
- "Synthesizer contract violation found, result %{sensitive}@, expected %{sensitive}@ score %f totalViolations %d"
- "Synthesizer contract violations found, total %d"
- "Synthesizer contract violations not found"
- "Text synthesizer has not been checked out"
- "TextRecognition"
- "The diffusion model hash for Latin should be non-nil"
- "Updating style prediction for %lu samples, removing %lu unsupported samples"
- "_backgroundPrioritySynthesisProcessingQueue"
- "_buildMultiLingualResultForRequest:recognitionLocales:recognizersByLocale:statisticsByLocale:"
- "_computeTextRecognitionResultsForRequest:recognizer:recognizerCachingKey:isTopLocale:writingStatistics:"
- "_fastPathCharacterPersonalizer"
- "_highPrioritySynthesisProcessingQueue"
- "_isReadyForCharacterInventorySynthesis"
- "_isValidRemoteSynthesisRequest:bundleIdentifier:error:"
- "_queueForRequest:outIsSynchronizedSynthesisQueue:"
- "_scriptClassifier"
- "_shouldFreezeCharacterInventory"
- "_styleInventory"
- "_synthesisProcessingWorkloop"
- "_textSynthesizer"
- "_updateStylePredictionsSingleBatch:"
- "addSamplesIfNeededWithTokenizedMathResult:drawing:strokeIdentifiers:"
- "addSamplesIfNeededWithTokenizedTextResult:drawing:script:strokeIdentifiers:"
- "appendDrawing:"
- "appendFormat:"
- "arrayByAddingObjectsFromArray:"
- "bounds"
- "canPredictStyleForTranscription:"
- "checkSegmentsAndDrawingConsistencyForSynthesisResult:bundleIdentifier:withReply:"
- "clear"
- "com.apple.handwritingd.BackgroundPriorityRecognitionProcessingQueue"
- "com.apple.handwritingd.HighPrioritySynthesisProcessingQueue"
- "com.apple.handwritingd.ongoingSynthesisCheck"
- "com.apple.handwritingd.synthesisProcessingWorkloop"
- "containsSampleWithStrokeIdentifiers:"
- "countCodepoints"
- "diffusionModelHash"
- "diffusionModelHashes"
- "drawingTransformedWithTranslation:scaleFactor:"
- "enumerateObjectsUsingBlock:"
- "enumerateStyleSamplesUsingBlock:"
- "extended_latin"
- "fastPathCharacterStylesWithVariations"
- "getLastCharacterStyleTimestamp"
- "hasAllDigits"
- "hasIdleLifetimeElapsed:"
- "hasStyleInventoryIdleLifetimeElapsed:"
- "initWithContent:drawing:"
- "initWithLocationRange:comment:kind:"
- "initWithServerQueue:lowPriorityQueue:highPriorityQueue:recognitionHandler:"
- "initWithStyleInventory:"
- "initWithStyleInventory:characterSet:"
- "isFastPath"
- "isPersonalizedSynthesisAvailableForLatin"
- "lastSavedDate"
- "latin"
- "localesForScriptClassification:selectedScriptCodepoints:"
- "minimumNumberOfSamplesWithStylePrediction"
- "modelHashesWithLatinHash:"
- "modelWithModelName:"
- "needsStylePredictionUpdateForScript:"
- "objectAtIndex:"
- "predictedScriptsForDrawing:maxNumberOfLocales:"
- "q24@0:8q16"
- "q24@?0@\"CHSynthesisStyleSample\"8@\"CHSynthesisStyleSample\"16"
- "qwertyuioplikjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
- "refineDrawing:transcription:options:shouldCancel:error:"
- "removeObjectsInArray:"
- "removeSamplesContainingStrokeIdentifiers:"
- "removedStrokeIdentifiers"
- "replaceDrawing:originalTranscription:replacementTranscription:options:shouldCancel:error:"
- "reset"
- "retrieveActivationMatrixForDrawing:recognitionEngineCachingKey:outStrokeIndexMapping:outStrokeEndings:"
- "runPersonalizationWithBlock:resynthesizeAll:"
- "samplesWithoutStylePrediction"
- "saveIfNeeded"
- "script_classification.bundle"
- "script_classification_sunglow"
- "segmentContents"
- "segmentStrokeIndexes"
- "setContractViolations:"
- "setStylePredictions:"
- "setSynthesizeCharacterInventoryBehavior:"
- "shouldResetInventory"
- "skipStyleInventoryLookup"
- "sortedArrayUsingComparator:"
- "sortedArrayUsingSelector:"
- "statusWithInventory:"
- "stitchStyleSamples:"
- "styleContents"
- "styleDrawings"
- "stylePredictionResultForTranscriptions:drawings:shouldCancel:"
- "styleSampleOptionsForRequest:script:"
- "styleSamplesForInputSample:prompt:script:samplingAlgorithm:"
- "styleSamplesForInputSample:prompt:script:samplingAlgorithm:maxNumOfSamples:"
- "styleScriptForSynthesizerSupportedStyle:"
- "supportedCharactersForPersonalizedSynthesis"
- "synthesisModelHashes"
- "synthesizeDrawingForString:options:shouldCancel:error:"
- "textRecognitionResultForDrawing:options:writingStatistics:shouldCancel:"
- "throttledSaveStyleInventoryIfNeeded"
- "timeIntervalSinceNow"
- "tokenizedResult"
- "transcription"
- "updateStyleEmbedding:script:"
- "updateStylePredictionsWithSamplesToUpdate:toRemove:"
- "updateSynthesisModelHashLatin:"
- "v24@0:8q16"
- "v24@?0@\"CHSynthesisStyleSample\"8^B16"
- "v24@?0@\"CHTokenizedResult\"8@\"NSError\"16"
- "v28@?0@\"CHDrawing\"8B16d20"
- "v32@0:8@\"CHRemoteRecognitionRequest\"16@?<v@?@\"CHTokenizedResult\"@\"NSError\">24"
- "v32@?0@\"CHSynthesisStyleSample\"8Q16^B24"
- "validateSegments"

```
