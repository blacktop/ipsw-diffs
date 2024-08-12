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
   __AUTH_CONST.__auth_got: 0x520
-  __AUTH_CONST.__auth_ptr: 0x210
+  __AUTH_CONST.__auth_ptr: 0x200
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
-  CStrings:  77
+  Symbols:   219
+  CStrings:  47
 
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
+ "_preferredFontForSubheadingText"
+ "hostedNotesAppearanceCoordinator:shouldHideWithModal:"
+ "hostedNotesAppearanceCoordinatorModeButtonHidingModalTypes:"
+ "hostedNotesAppearanceCoordinatorModeButtonHidingPopoverTypes:"
+ "hostedNotesAppearanceCoordinatorSafeAreaViewController:"
+ "htmlAccountForObject:"
+ "htmlAttributesForAttachment:legacyContentID:tagName:"
+ "htmlDestinationFolder"
+ "htmlManagedObjectContext"
+ "htmlObjectAttributesForAttachmentWithContentID:"
+ "htmlSourceObjects"
+ "htmlStoreCoordinator"
+ "htmlStringByFixingDashedListsInHTMLString:"
+ "htmlStringFromAttributedString:attachmentConversionHandler:"
+ "htmlStringToLoad"
+ "htmlStringWithAttachmentConversionHandler:"
+ "htmlStringWithAttachments:"
+ "htmlStringWithHTMLAttachments"
+ "icReplaceTextStorage:"
+ "ic_CGImage"
+ "ic_HTMLInsertionPoint"
+ "ic_JPEGData"
+ "ic_JPEGDataWithOrientation:"
+ "ic_PDFData"
+ "ic_PNGData"
+ "ic_PNGDataWithOrientation:"
+ "ic_UIImageFromCIImage:"
+ "ic_acceptedParticipants"
+ "ic_actionWithAttributedTitle:handler:"
+ "ic_actionWithImage:handler:"
+ "ic_actionWithTitle:handler:"
+ "ic_actionWithTitle:imageName:attributes:handler:"
+ "ic_actionWithTitle:imageName:handler:"
+ "ic_actionWithTitle:subtitle:imageName:attributes:handler:"
+ "ic_actionWithTitle:subtitle:imageName:handler:"
+ "ic_addAnchorsToFillSuperview"
+ "ic_addAnchorsToFillSuperviewLayoutMargins"
+ "ic_addAnchorsToFillSuperviewWithHorizontalPadding:"
+ "ic_addAnchorsToFillSuperviewWithHorizontalPadding:verticalPadding:usesSafeAreaLayoutGuide:"
+ "ic_addAnchorsToFillSuperviewWithHorizontalPadding:verticalPadding:usesSafeAreaLayoutGuideHorizontally:usesSafeAreaLayoutGuideVertically:"
+ "ic_preferredFontForSubheadingTextWithContentSizeCategory:"
+ "ic_preferredFontForSubheadingTextWithContentSizeCategory:isForPrint:"
+ "ic_preferredFontForTextStyle:adjustedForDefaultSize:"
+ "ic_preferredFontForTextStyle:adjustedForDefaultSize:maxSize:"
+ "ic_preferredFontForTextStyle:maxContentSizeCategory:"
+ "ic_preferredFontForTitleText"
+ "intTitleLabel"
- "_processAttachments:withSessionIdentifier:extension:rootDir:"
- "_processAttachments:withSessionIdentifier:extension:shouldAddClassBDataProtection:rootDir:"
- "_queueItem"
- "_queuePayload"
- "_radarAttachmentName"
- "_recentlyFinishedSessions"
- "_remoteSideDelegate"
- "_remoteTransport"
- "_requiresClassBDataAccess"
- "_requiresDataClassBAccessToRun"
- "_reviewActionLabel"
- "_rfc1123DateFormatter"
- "_run_queue"
- "_runtime"
- "_sandboxEnvironment"
- "_saveDevice:"
- "_seedingDeviceToken"
- "_seedingEnvironment"
- "_seedingHost"
- "_seedingSubmissionID"
- "_seedingSubmissionType"
- "_sendActionLabel"
- "_senderPid"
- "_serverErrorFromTask:"
- "_sessionDidStartBlocks"
- "_sessionExistsCompletion"
- "_sessionStartBlocks"
- "_sessionStateCompletionBlock"
- "_sfDevice"
- "_statusCompletionBlock"
- "_streamOperationQueue"
- "_successfulUploads"
- "_syncCompletionBlock"
- "_terminateExtensionWithIdentifier:info:"
- "_timberLorryUUID"
- "_totalBytesExpectedToSend"
- "_totalUploadSize"
- "_uploadItems"
- "_uploadProgressCounter"
- "_uploadStartTime"
- "_uploadedBytes"
- "_useSharing"
- "_userInitiatedOpQueue"
- "_userNotificationShouldPlaySound"
- "_verificationTasks"
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
- "rkerTransportType"
- "talFileSize"
- "trySessionWithFoundDevice:fromInbound:"
- "unscheduleOperationsOnAvailability"
- "updateControllerWithDevice:andStatus:"
- "updateELSSnapshotStatus:"
- "updatePongAdvertisement"
- "updatePromise:withAttachmentGroup:status:success:error:"
- "updatePromise:withFilename:size:extensionID:status:success:error:"
- "updatePromise:withFilename:size:status:success:error:"

```
