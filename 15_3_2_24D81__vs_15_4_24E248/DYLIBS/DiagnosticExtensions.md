## DiagnosticExtensions

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/Versions/A/DiagnosticExtensions`

```diff

-130.0.0.0.0
-  __TEXT.__text: 0x2619c
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_methlist: 0xe98
-  __TEXT.__const: 0x70
+131.0.0.0.0
+  __TEXT.__text: 0x264e0
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_methlist: 0x10a4
+  __TEXT.__const: 0x60
   __TEXT.__cstring: 0x116f
   __TEXT.__oslogstring: 0x286f
   __TEXT.__gcc_except_tab: 0x9a0

   __TEXT.__objc_methname: 0x310a
   __TEXT.__objc_methtype: 0x591
   __TEXT.__objc_stubs: 0x2500
-  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__got: 0x240
   __DATA_CONST.__const: 0x6f0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc18
+  __DATA_CONST.__objc_selrefs: 0xcc8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH_CONST.__auth_got: 0x3e8
   __AUTH_CONST.__const: 0xa50
   __AUTH_CONST.__cfstring: 0x10a0
-  __AUTH_CONST.__objc_const: 0x2990
+  __AUTH_CONST.__objc_const: 0x25e8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x500

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 08451EC7-38A5-3900-A7FB-58859B9774CF
+  UUID: BC783D04-C127-35E8-8C37-033A91EEE845
   Functions: 443
   Symbols:   1532
   CStrings:  1137
Functions:
~ -[DEArchive initWithURL:] : 516 -> 536
~ -[DEArchive addFile:withPathName:] : 156 -> 152
~ -[DEArchive addFile:withPathName:progressHandler:] : 2856 -> 2780
~ -[DEArchive closeArchive] : 100 -> 92
~ -[DEArchive archiverForUrl:] : 984 -> 980
~ +[DELoggingPreferences installLoggingProfile:sessionIdentifier:extensionIdentifier:error:] : 1020 -> 1008
~ +[DELoggingPreferences removeLoggingProfileForSessionIdentifier:extensionIdentifier:error:] : 1332 -> 1360
~ +[DELoggingPreferences loggingPayloadForURL:error:] : 452 -> 436
~ +[DELoggingPreferences combinedLoggingPayloadForURLs:error:] : 1544 -> 1572
~ +[DELoggingPreferences _subsystemPayloadForURL:error:] : 764 -> 768
~ +[DELoggingPreferences numberOfManagedLoggingPreferences] : 168 -> 180
~ +[DELoggingPreferences managedLoggingProfilesDirectory] : 420 -> 432
~ +[DELoggingPreferences managedLoggingProfilesDirectoryForSessionIdentifier:createIfNeeded:error:] : 668 -> 700
~ +[DEExtensionTracker checkIn] : 268 -> 276
~ ___29+[DEExtensionTracker checkIn]_block_invoke : 312 -> 320
~ +[DEExtensionTracker shouldSetupWithIdentifier:session:expirationDate:] : 604 -> 632
~ ___71+[DEExtensionTracker shouldSetupWithIdentifier:session:expirationDate:]_block_invoke : 576 -> 572
~ +[DEExtensionTracker shouldTeardownWithIdentifier:session:] : 524 -> 544
~ ___59+[DEExtensionTracker shouldTeardownWithIdentifier:session:]_block_invoke : 700 -> 692
~ +[DEExtensionTracker saveCurrentLoggingExtensionsWithDictionary:] : 392 -> 400
~ +[DEExtensionTracker hasInactiveLoggingSession:] : 492 -> 488
~ +[DEExtensionTracker sharedSerialQueue] : 148 -> 144
~ ___39+[DEExtensionTracker sharedSerialQueue]_block_invoke : 80 -> 88
~ +[DEExtensionTracker _updateExtensionExpirationDateWithIdentifier:expirationDate:] : 772 -> 780
~ +[DEExtensionTracker _updateXPCActivityDate] : 1960 -> 1976
~ ___44+[DEExtensionTracker _updateXPCActivityDate]_block_invoke : 252 -> 240
~ +[DEExtensionTracker xpcActivityTimeInterval] : 28 -> 32
~ +[DEExtensionTracker scheduleXPCActivity] : 908 -> 900
~ ___41+[DEExtensionTracker scheduleXPCActivity]_block_invoke : 484 -> 468
~ +[DEExtensionTracker extensionTrackerCleanup] : 276 -> 284
~ ___45+[DEExtensionTracker extensionTrackerCleanup]_block_invoke : 1272 -> 1300
~ __45+[DEExtensionTracker extensionTrackerCleanup]_block_invoke.34 : 1972 -> 1968
~ __45+[DEExtensionTracker extensionTrackerCleanup]_block_invoke.35 : 364 -> 348
~ +[DEExtensionTracker updateRetainCountWithIdentifier:session:offsetBy:] : 848 -> 864
~ _Log : 140 -> 136
~ ___Log_block_invoke : 80 -> 88
~ +[DEArchiver directorySizeOf:] : 888 -> 828
~ +[DEArchiver archiveDirectoryAt:deleteOriginal:] : 164 -> 156
~ +[DEArchiver archiveDirectoryAt:deleteOriginal:progressHandler:] : 3468 -> 3412
~ +[DEArchiver archiveFile:deleteOriginal:] : 164 -> 156
~ +[DEArchiver archiveFile:deleteOriginal:progressHandler:] : 1468 -> 1404
~ +[DEExtensionHostContext _extensionAuxiliaryVendorProtocol] : 148 -> 144
~ ___59+[DEExtensionHostContext _extensionAuxiliaryVendorProtocol]_block_invoke : 476 -> 484
~ +[DEExtensionHostContext _extensionAuxiliaryHostProtocol] : 148 -> 144
~ ___57+[DEExtensionHostContext _extensionAuxiliaryHostProtocol]_block_invoke : 88 -> 96
~ -[DEExtensionHostContext hasEntitlement] : 380 -> 368
~ ___52-[DEExtensionHostContext attachmentListWithHandler:]_block_invoke : 328 -> 336
~ -[DEExtensionHostContext annotatedAttachmentsForParameters:withHandler:] : 888 -> 920
~ ___72-[DEExtensionHostContext annotatedAttachmentsForParameters:withHandler:]_block_invoke : 352 -> 360
~ -[DEExtensionHostContext attachmentsForParameters:withProgressHandler:withHandler:] : 1272 -> 1304
~ ___83-[DEExtensionHostContext attachmentsForParameters:withProgressHandler:withHandler:]_block_invoke : 352 -> 360
~ __83-[DEExtensionHostContext attachmentsForParameters:withProgressHandler:withHandler:]_block_invoke.137 : 140 -> 148
~ ___57-[DEExtensionHostContext setupForParameters:withHandler:]_block_invoke : 328 -> 336
~ ___60-[DEExtensionHostContext teardownForParameters:withHandler:]_block_invoke : 328 -> 336
~ -[DEExtensionHostContext isExtensionEnhancedLoggingStateOnWithHandler:] : 252 -> 244
~ ___71-[DEExtensionHostContext isExtensionEnhancedLoggingStateOnWithHandler:]_block_invoke : 328 -> 336
~ -[DEExtensionHostContext collectionDidUpdateWithProgress:] : 168 -> 176
~ +[DEAnnotation annotateURL:displayName:description:iconType:additionalInfo:error:] : 1328 -> 1280
~ +[DEAnnotation readExtendedAttributeInURL:forKey:error:] : 2464 -> 2436
~ +[DEAnnotation writeExtendedAttributeInURL:forKey:value:] : 904 -> 928
~ +[DEAnnotation errorWithMessage:] : 280 -> 284
~ -[DEExtension initWithNSExtension:] : 948 -> 980
~ ___35-[DEExtension initWithNSExtension:]_block_invoke : 292 -> 284
~ _Log : 140 -> 136
~ __35-[DEExtension initWithNSExtension:]_block_invoke.68 : 360 -> 368
~ -[DEExtension isLoggingEnabled] : 2176 -> 2128
~ -[DEExtension endUsingExtension] : 252 -> 260
~ ___32-[DEExtension endUsingExtension]_block_invoke : 1512 -> 1672
~ -[DEExtension createExtensionHostContextCompletion:] : 372 -> 388
~ ___52-[DEExtension createExtensionHostContextCompletion:]_block_invoke : 2440 -> 2660
~ __52-[DEExtension createExtensionHostContextCompletion:]_block_invoke.78 : 232 -> 224
~ -[DEExtension serialQueue] : 300 -> 336
~ -[DEExtension performWithHostContext:] : 452 -> 484
~ ___38-[DEExtension performWithHostContext:]_block_invoke : 1836 -> 1936
~ __38-[DEExtension performWithHostContext:]_block_invoke.83 : 120 -> 136
~ __38-[DEExtension performWithHostContext:]_block_invoke.86 : 284 -> 308
~ ___38-[DEExtension performWithHostContext:]_block_invoke_2 : 1516 -> 1564
~ __38-[DEExtension performWithHostContext:]_block_invoke.87 : 120 -> 136
~ __38-[DEExtension performWithHostContext:]_block_invoke.88 : 120 -> 136
~ -[DEExtension attachmentListWithHandler:] : 256 -> 272
~ ___41-[DEExtension attachmentListWithHandler:]_block_invoke : 316 -> 308
~ ___41-[DEExtension attachmentListWithHandler:]_block_invoke_2 : 120 -> 112
~ -[DEExtension annotatedAttachmentsForParameters:andHandler:] : 328 -> 352
~ ___60-[DEExtension annotatedAttachmentsForParameters:andHandler:]_block_invoke : 328 -> 320
~ ___60-[DEExtension annotatedAttachmentsForParameters:andHandler:]_block_invoke_2 : 120 -> 112
~ -[DEExtension attachmentsForParameters:withProgressHandler:andHandler:] : 600 -> 648
~ ___71-[DEExtension attachmentsForParameters:withProgressHandler:andHandler:]_block_invoke_2 : 292 -> 280
~ -[DEExtension setupWithParameters:session:] : 228 -> 240
~ -[DEExtension setupWithParameters:session:expirationDate:] : 964 -> 980
~ ___58-[DEExtension setupWithParameters:session:expirationDate:]_block_invoke : 120 -> 112
~ ___58-[DEExtension setupWithParameters:session:expirationDate:]_block_invoke_2 : 164 -> 160
~ -[DEExtension teardownWithParameters:session:] : 940 -> 964
~ ___46-[DEExtension teardownWithParameters:session:]_block_invoke_2 : 184 -> 180
~ -[DEExtension checkAndTeardown] : 656 -> 660
~ ___31-[DEExtension checkAndTeardown]_block_invoke : 324 -> 340
~ ___31-[DEExtension checkAndTeardown]_block_invoke_2 : 696 -> 700
~ __31-[DEExtension checkAndTeardown]_block_invoke.104 : 244 -> 260
~ __31-[DEExtension checkAndTeardown]_block_invoke_2.105 : 328 -> 308
~ -[DEExtension requiresDataClassBAccessToRun] : 440 -> 448
~ ___44-[DEExtension requiresDataClassBAccessToRun]_block_invoke : 224 -> 228
~ -[DEExtension accessBundleWithSynchronousHandler:] : 2076 -> 2120
~ ___50-[DEExtension accessBundleWithSynchronousHandler:]_block_invoke : 396 -> 404
~ -[DEExtension _localizedTextFromLocalizedStringKey:fallbackFileContentsKey:localization:] : 524 -> 508
~ -[DEExtension _fileContentsFromPlistWithKey:localization:] : 648 -> 668
~ ___58-[DEExtension _fileContentsFromPlistWithKey:localization:]_block_invoke : 1016 -> 996
~ -[DEExtension _localizedStringFromPlistWithKey:localization:] : 648 -> 668
~ ___61-[DEExtension _localizedStringFromPlistWithKey:localization:]_block_invoke : 536 -> 528
~ -[DEExtension installLoggingProfileWithSessionID:] : 1128 -> 1108
~ -[DEExtension removeLoggingProfileWithSessionID:] : 800 -> 784
~ -[DEExtension loggingProfileURLsFromExtension] : 2168 -> 2132
~ -[DEExtension setAllowUserAttachmentSelection:] : 48 -> 40
~ -[DEExtension setIsFetchingExtensionHostContext:] : 40 -> 36
~ -[DEExtension setAdoptsExtensionTrackerFlow:] : 40 -> 36
~ ___Log_block_invoke : 80 -> 88
~ -[DEArchiveReader initWithURL:] : 564 -> 556
~ -[DEArchiveReader listContainedPaths] : 260 -> 240
~ -[DEArchiveReader closeArchive] : 88 -> 80
~ -[DEAnnotatedGroup initWithDisplayName:localizedDescription:iconType:additionalInfo:attachmentItems:] : 412 -> 408
~ -[DEAnnotatedGroup description] : 236 -> 260
~ -[DEAnnotatedGroup debugDescription] : 348 -> 396
~ -[DEAnnotatedGroup encodeWithCoder:] : 500 -> 540
~ -[DEAnnotatedGroup initWithCoder:] : 396 -> 444
~ -[DEAttachmentItem initWithPath:] : 192 -> 208
~ -[DEAttachmentItem initWithPathURL:] : 152 -> 160
~ -[DEAttachmentItem initWithPathURL:shouldCheckURLAttributes:] : 1908 -> 1848
~ -[DEAttachmentItem _generateSandboxExtensionTokenForPID:] : 2060 -> 2040
~ -[DEAttachmentItem initWithPath:withDisplayName:modificationDate:andFilesize:] : 384 -> 388
~ -[DEAttachmentItem initWithCoder:] : 540 -> 612
~ -[DEAttachmentItem attachToDestinationDir:] : 696 -> 724
~ -[DEAttachmentItem detach] : 112 -> 120
~ -[DEAttachmentItem description] : 112 -> 120
~ -[DEAttachmentItem sandboxExtensionHandleWithErrorOut:] : 288 -> 312
~ -[DEAttachmentItemSandboxExtensionHandle initWithSandboxExtensionToken:itemURL:errorOut:] : 1508 -> 1524
~ -[DEAttachmentItemSandboxExtensionHandle setDidInit:] : 48 -> 40
~ +[DEDaemonHelper generateSandboxExtensionWithDestinationDir:pingTarget:] : 1088 -> 1056
~ _Log : 140 -> 136
~ ___Log_block_invoke : 80 -> 88
~ -[DELogMover initWithServiceName:] : 248 -> 256
~ -[DELogMover sendRequestReturningBooleanResponse:withSuccessKey:] : 1264 -> 1204
~ ___65-[DELogMover sendRequestReturningBooleanResponse:withSuccessKey:]_block_invoke : 396 -> 376
~ +[DELogMover moveSystemLogsWithExtensions:] : 320 -> 328
~ ___43+[DELogMover moveSystemLogsWithExtensions:]_block_invoke : 424 -> 404
~ +[DEExtensionManager sharedInstance] : 148 -> 144
~ ___36+[DEExtensionManager sharedInstance]_block_invoke : 212 -> 236
~ -[DEExtensionManager extensionForIdentifier:] : 588 -> 572
~ -[DEExtensionManager init] : 172 -> 168
~ -[DEExtensionManager loadExtensions] : 552 -> 560
~ ___36-[DEExtensionManager loadExtensions]_block_invoke : 916 -> 884
~ -[DEExtensionManager extensionsWithFilter:] : 480 -> 512
~ -[DEExtensionManager setExtendedLoaded:] : 48 -> 40
~ -[DEExtensionProvider init] : 196 -> 192
~ -[DEExtensionProvider beginRequestWithExtensionContext:] : 764 -> 768
~ -[DEExtensionProvider attachmentsForParameters:] : 120 -> 128
~ -[DEExtensionProvider setupWithParameters:] : 296 -> 288
~ -[DEExtensionProvider teardownWithParameters:] : 296 -> 288
~ -[DEExtensionProvider isExtensionEnhancedLoggingStateOnWithHandler:] : 336 -> 324
~ -[DEExtensionProvider filesInDir:matchingPattern:excludingPattern:] : 2200 -> 2204
~ -[DEExtensionProvider _getHostname] : 148 -> 144
~ ___35-[DEExtensionProvider _getHostname]_block_invoke : 264 -> 248
~ -[DEExtensionProvider setCanGenerateNewAttachment:] : 48 -> 40
~ -[DEExtensionProvider setAllowUserAttachmentSelection:] : 48 -> 40
~ -[DEExtensionProvider setIsEnhancedLoggingStateOn:] : 48 -> 40
~ _DEUtilsValidateConnection : 688 -> 656
~ _Log : 140 -> 136
~ _DEUtilsValidateDestination : 696 -> 660
~ ___Log_block_invoke : 80 -> 88
~ +[DELogging fwHandle] : 148 -> 144
~ ___21+[DELogging fwHandle]_block_invoke : 80 -> 88
~ -[DECollectionProgress initWithPercentComplete:] : 112 -> 120
~ -[DECollectionProgress initWithCoder:] : 348 -> 364
~ +[DEAttachmentGroup createWithName:rootURL:] : 908 -> 924
~ +[DEAttachmentGroup createWithName:rootURL:attachmentItems:] : 384 -> 408
~ -[DEAttachmentGroup initWithCoder:] : 304 -> 328
~ -[DEAttachmentGroup attachToDestinationDir:] : 2004 -> 2044
~ _pgrep : 760 -> 676
~ _signal_USR2 : 72 -> 64
~ -[NSString(DEURLPathEscaping) escape] : 144 -> 140
~ ___37-[NSString(DEURLPathEscaping) escape]_block_invoke : 80 -> 88
~ +[DEUtils getFileSystemItemSize:] : 824 -> 816
~ _Log : 140 -> 136
~ +[DEUtils getDirectorySize:] : 1956 -> 1952
~ ___28+[DEUtils getDirectorySize:]_block_invoke : 300 -> 292
~ +[DEUtils tarGzForDirectoryUrl:validatesUrl:] : 668 -> 656
~ +[DEUtils dirForTarGz:] : 320 -> 296
~ +[DEUtils isValidDirectory:] : 804 -> 780
~ +[DEUtils copyAllFilesFromDir:toDir:keepSourceDir:] : 1996 -> 1976
~ +[DEUtils copyItem:toDestinationDir:zipped:] : 1432 -> 1440
~ +[DEUtils moveItem:toDestinationDir:] : 716 -> 720
~ +[DEUtils copyFile:toDir:] : 160 -> 164
~ +[DEUtils copyAndReturn:toDir:withNewFileName:] : 972 -> 1000
~ +[DEUtils copyAndReturn:toDir:] : 980 -> 1008
~ +[DEUtils copyAllFilesFromDir:toDir:] : 160 -> 156
~ +[DEUtils pathComponentsInURL:removingBaseURLComponents:keepingFirstComponent:] : 776 -> 840
~ +[DEUtils urlByRemovingComponentsBefore:source:keepComponent:] : 384 -> 400
~ +[DEUtils enumeratorForAllItems:] : 368 -> 396
~ ___33+[DEUtils enumeratorForAllItems:]_block_invoke : 300 -> 292
~ +[DEUtils findAllItems:includeDirs:] : 964 -> 928
~ +[DEUtils lsDir:sorted:] : 912 -> 916
~ ___24+[DEUtils lsDir:sorted:]_block_invoke : 720 -> 692
~ +[DEUtils userLibraryDirectoryForApp:] : 548 -> 524
~ +[DEUtils applicationSupportDirectoryForApp:] : 648 -> 628
~ +[DEUtils createUserOwnedDirectoryAtUrl:] : 600 -> 616
~ +[DEUtils copyPath:toDestinationDir:zipped:] : 2260 -> 2308
~ +[DEUtils uniqueDateString] : 188 -> 196
~ +[DEUtils removeFile:] : 768 -> 788
~ +[DEUtils findEntriesInDirectory:createdAfter:matchingPattern:] : 1196 -> 1188
~ +[DEUtils processErrorResponse:] : 1220 -> 1224
~ +[DEUtils uniqueTemporaryDirectory] : 564 -> 580
~ -[NSURL(DESandboxExtension) generateSandboxExtensionForProcess:] : 1460 -> 1436
~ -[NSURL(DESandboxExtension) accessWithSandboxExtension:inBlock:] : 1456 -> 1448
~ ___Log_block_invoke : 80 -> 88
~ +[DEExtensionContext _extensionAuxiliaryVendorProtocol] : 148 -> 144
~ ___55+[DEExtensionContext _extensionAuxiliaryVendorProtocol]_block_invoke : 88 -> 96
~ +[DEExtensionContext _extensionAuxiliaryHostProtocol] : 148 -> 144
~ ___53+[DEExtensionContext _extensionAuxiliaryHostProtocol]_block_invoke : 88 -> 96
~ -[DEExtensionContext hasEntitlement] : 148 -> 152
~ -[DEExtensionContext attachmentListWithHandler:] : 212 -> 228
~ -[DEExtensionContext attachmentsForParameters:withHandler:] : 1068 -> 1064
~ ___59-[DEExtensionContext attachmentsForParameters:withHandler:]_block_invoke : 196 -> 212
~ ___59-[DEExtensionContext attachmentsForParameters:withHandler:]_block_invoke_2 : 328 -> 336
~ -[DEExtensionContext annotatedAttachmentsForParameters:withHandler:] : 708 -> 688
~ -[DEExtensionContext setupWithParameters:withHandler:] : 188 -> 196
~ -[DEExtensionContext teardownWithParameters:withHandler:] : 188 -> 196
~ -[DEExtensionContext isExtensionEnhancedLoggingStateOnWithHandler:] : 152 -> 160

```
