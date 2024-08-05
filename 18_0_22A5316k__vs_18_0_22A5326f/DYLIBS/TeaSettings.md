## TeaSettings

> `/System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings`

```diff

-1048.0.0.0.0
+1056.0.0.0.0
   __TEXT.__text: 0x17830
   __TEXT.__auth_stubs: 0xa40
   __TEXT.__objc_methlist: 0x14

   __TEXT.__eh_frame: 0x1d0
   __TEXT.__objc_methname: 0x17c
   __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb0

   __AUTH_CONST.__auth_ptr: 0x210
   __AUTH_CONST.__const: 0x1850
   __AUTH_CONST.__objc_const: 0x1198
-  __AUTH.__data: 0x558
   __DATA.__data: 0x3b8
   __DATA.__bss: 0x900
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0xb20
+  __DATA_DIRTY.__data: 0x1078
   __DATA_DIRTY.__bss: 0x400
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 990
-  Symbols:   211
-  CStrings:  67
+  Symbols:   219
+  CStrings:  62
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "N,V_hasInnerType"
+ "T@\"NSString\",R,N,V_publicIPPrefix"
+ "T@\"NSString\",R,N,V_pushType"
+ "T@\"NSString\",R,N,V_qID"
+ "T@\"NSString\",R,N,V_queryRaw"
+ "T@\"NSString\",R,N,V_question"
+ "T@\"NSString\",R,N,V_radioBand"
+ "T@\"NSString\",R,N,V_radioType"
+ "T@\"NSString\",R,N,V_ratType"
+ "T@\"NSString\",R,N,V_rawMessage"
+ "T@\"NSString\",R,N,V_reasonCodes"
+ "T@\"NSString\",R,N,V_recipients"
+ "T@\"NSString\",R,N,V_recognizedText"
+ "T@\"NSString\",R,N,V_recordID"
+ "T@\"NSString\",R,N,V_recordingRequestID"
+ "T@\"NSString\",R,N,V_referrerBundleID"
+ "T@\"NSString\",R,N,V_referrerURL"
+ "T@\"NSString\",R,N,V_replacementContext"
+ "T@\"NSString\",R,N,V_requestId"
+ "T@\"NSString\",R,N,V_requestIdentifier"
+ "T@\"NSString\",R,N,V_requesterDSID"
+ "T@\"NSString\",R,N,V_resourceURL"
+ "T@\"NSString\",R,N,V_responderDSID"
+ "T@\"NSString\",R,N,V_responsibleApp"
+ "T@\"NSString\",R,N,V_resultID"
+ "T@\"NSString\",R,N,V_resultIdentifier"
+ "T@\"NSString\",R,N,V_roomUniqueIdentifier"
+ "T@\"NSString\",R,N,V_safariProfileID"
+ "T@\"NSString\",R,N,V_searchResultTitle"
+ "T@\"NSString\",R,N,V_searchSessionUUID"
+ "T@\"NSString\",R,N,V_searchTerms"
+ "T@\"NSString\",R,N,V_securityMethod"
+ "T@\"NSString\",R,N,V_semanticModeIdentifier"
+ "T@\"NSString\",R,N,V_senderId"
+ "T@\"NSString\",R,N,V_serverReleaseVersion"
+ "T@\"NSString\",R,N,V_serviceGroupName"
+ "T@\"NSString\",R,N,V_serviceGroupUniqueIdentifier"
+ "T@\"NSString\",R,N,V_serviceUniqueIdentifier"
+ "T@\"NSString\",R,N,V_shareSessionIdentifier"
+ "T@\"NSString\",R,N,V_sharingEventUID"
+ "T@\"NSString\",R,N,V_signal"
+ "T@\"NSString\",R,N,V_siriInputLocale"
+ "T@\"NSString\",R,N,V_siriLocale"
+ "T@\"NSString\",R,N,V_siriResponseId"
+ "T@\"NSString\",R,N,V_sirikitIntentItemId"
+ "T@\"NSString\",R,N,V_slotValue"
+ "T@\"NSString\",R,N,V_soundDetectionType"
+ "T@\"NSString\",R,N,V_soundName"
+ "TB,N,V_hasInsectsAssetCount"
+ "TB,N,V_hasInsectsAssetProcessedCount"
+ "TB,N,V_hasInsectsAssetSuccessesCount"
+ "TB,N,V_hasInstalled"
+ "TB,N,V_hasInstdBA"
+ "TB,N,V_hasInstdBC"
+ "TB,N,V_hasInt64Value"
+ "TB,N,V_hasIntValue"
+ "TB,N,V_hasInt_value"
+ "TB,N,V_hasIntendedRequestCount"
+ "TB,N,V_hasIntendedRequestRatio"
+ "TB,N,V_hasInteractionContactScore"
+ "TB,N,V_hasInvocationTypeID"
+ "ixStoreVersion"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_nanoSynchronizeQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_callQueue"
- "T@\"NSString\",&,N,V_callIdentifier"
- "T@\"NSString\",&,N,V_currentCallUUID"
- "T@\"NSString\",&,N,V_serviceUpdateType"
- "T@\"NSUUID\",&,N,V_testUuid"
- "T@\"RTTConversation\",&,N,V_conversation"
- "T@\"TUCall\",&,N,V_call"
- "TB,N,V_isTranscription"
- "Tasks"
- "_verifyPairingForSession:holdForPIN:completion:"
- "_visiblePingUUIDs"
- "_workerService"
- "_xpcConnectionsCompletion"
- "_xpcConnector"
- "_xpcConnectorDelegate"
- "addData:withFilename:"
- "addIncomingSFSession:forIdentifier:"
- "addRawRecordToQueueFromModel:"
- "addReferenceForModel:referenceKey:"
- "addToStore"
- "additionalStateInfo"
- "adoptFiles:withCompletion:"
- "adoptFilesCompletions"
- "allExtensionIdentifiers"
- "allPlatforms"
- "allUploadsComplete"
- "allVerificationTasksComplete"
- "allowsCellularUpload"
- "archiveItemsInDirectory:"
- "asynchronousDataFromURL:completionBlock:"
- "asynchronousDataFromURL:key:completionBlock:"
- "attachCompletionHandlerForDEDExtensionIdentifier:handler:"
- "attachCompletionHandlerForOngoingOperation:handler:"
- "attachmentGroupModel"
- "basePayloadForCommand:"
- "beginListeningForNotification"
- "beginUploadWithRequest:fromFileURL:error:"
- "blockingSharingSessionForDevice:fromInbound:"
- "bluetoothSessionSemaphore"
- "bodyDataForParameters:encoding:error:"
- "bugSession"
- "bugSessionConfig"
- "bugSessionIdentifier"
- "bugSessionStartTimeout"
- "bytesUploadedFromAllFiles"
- "cachedImageFromKey:"
- "cancelDiagnosticExtension:"
- "cancelDiagnosticExtensionWithDEDExtensionIdentifier:"
- "cancelDiagnosticExtensionWithIdentifier:"
- "cancelDiagnosticExtensionWithIdentifier:invocationNumber:"
- "cancelPromise:withSuccess:error:"
- "checkReadinessForSFDevice:session:"
- "cleanUpIfNeededWithDefaults:"
- "cleanupFinishedUploads:"
- "clearNotification"
- "cloudKitModel"
- "cloudkitContainer"
- "cloudkitData"
- "cloudkitUseDevelopmentEnvironment"
- "collectedGroupsWithSessionIdentifier:matchingExtensions:"
- "compactMapOnFeedbackUploadsWithUserDefaults:block:"
- "compiledEntityID"
- "compressOnAttach"
- "compressionProgress:total:"
- "currentCallUUID"
- "s"

```
