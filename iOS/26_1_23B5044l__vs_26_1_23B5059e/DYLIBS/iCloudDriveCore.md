## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4257.40.32.502.1
-  __TEXT.__text: 0x31012c
+4257.40.57.0.1
+  __TEXT.__text: 0x311514
   __TEXT.__auth_stubs: 0x1b40
-  __TEXT.__objc_methlist: 0x1a18c
+  __TEXT.__objc_methlist: 0x1a24c
   __TEXT.__const: 0x500
-  __TEXT.__cstring: 0x7d4f9
-  __TEXT.__oslogstring: 0x3c0f3
-  __TEXT.__gcc_except_tab: 0x1a464
+  __TEXT.__cstring: 0x7d6ac
+  __TEXT.__oslogstring: 0x3c1d5
+  __TEXT.__gcc_except_tab: 0x1a568
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0x9f50
-  __TEXT.__objc_classname: 0x2acb
-  __TEXT.__objc_methname: 0x444b0
-  __TEXT.__objc_methtype: 0x900f
-  __TEXT.__objc_stubs: 0x2f0c0
-  __DATA_CONST.__got: 0x1720
-  __DATA_CONST.__const: 0x95c8
+  __TEXT.__unwind_info: 0x9fb0
+  __TEXT.__objc_classname: 0x2acc
+  __TEXT.__objc_methname: 0x446a2
+  __TEXT.__objc_methtype: 0x905f
+  __TEXT.__objc_stubs: 0x2f160
+  __DATA_CONST.__got: 0x1718
+  __DATA_CONST.__const: 0x95f0
   __DATA_CONST.__objc_classlist: 0xa60
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe6a0
+  __DATA_CONST.__objc_selrefs: 0xe6f8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x920
-  __DATA_CONST.__objc_arraydata: 0xe40
+  __DATA_CONST.__objc_arraydata: 0xe58
   __AUTH_CONST.__auth_got: 0xdb0
-  __AUTH_CONST.__const: 0x2b60
-  __AUTH_CONST.__cfstring: 0x22960
-  __AUTH_CONST.__objc_const: 0x3d220
-  __AUTH_CONST.__objc_intobj: 0xba0
-  __AUTH_CONST.__objc_arrayobj: 0x1f8
+  __AUTH_CONST.__const: 0x2b80
+  __AUTH_CONST.__cfstring: 0x22a20
+  __AUTH_CONST.__objc_const: 0x3d2b8
+  __AUTH_CONST.__objc_intobj: 0xbb8
+  __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH.__objc_data: 0x28a0
+  __AUTH.__objc_data: 0x2788
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1fa4
+  __DATA.__objc_ivar: 0x1fac
   __DATA.__data: 0x2740
   __DATA.__bss: 0x208
-  __DATA_DIRTY.__objc_data: 0x3f20
+  __DATA_DIRTY.__objc_data: 0x4038
   __DATA_DIRTY.__data: 0xd0
-  __DATA_DIRTY.__bss: 0x3f8
+  __DATA_DIRTY.__bss: 0x408
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E66D3460-3419-33B8-A91A-2353426B8254
-  Functions: 13580
-  Symbols:   44215
-  CStrings:  23274
+  UUID: F650AD1B-A0CC-39AB-93AF-8EAB9B85663B
+  Functions: 13600
+  Symbols:   44272
+  CStrings:  23303
 
Symbols:
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) _errorsChainIfNecessaryForAppTelemetryIdentifier:error:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) _errorsChainIfNecessaryForAppTelemetryIdentifier:error:].cold.1
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) _newTelemetryEventWithIdentifier:error:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) _newTelemetryEventWithIdentifier:zoneWithMangledID:enhancedDrivePrivacyEnabled:error:errorDescription:itemIDString:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newTelemetryEventWithIdentifier:zoneWithMangledID:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newTelemetryEventWithIdentifier:zoneWithMangledID:enhancedDrivePrivacyEnabled:]
+ +[AppTelemetryTimeSeriesEvent(BRCAdditions) newTelemetryEventWithIdentifier:zoneWithMangledID:enhancedDrivePrivacyEnabled:fromError:errorDescription:itemIDString:]
+ +[BRCGlobalProgress _syncUpSizeWithVersionSize:]
+ +[BRCGlobalProgress _transferSizeWithVersionSize:]
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) errorsChain]
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) hasErrorsChain]
+ -[AppTelemetryInvestigation(AppTelemetryDriveTelemetryExtension) setErrorsChain:]
+ -[BRCContainerScheduler _pushTopicForIdentifier:]
+ -[BRCGlobalProgress queue]
+ -[BRCGlobalProgress resumeGroup]
+ -[BRCUserDefaults telemetryEventIdentifiersToReportErrorsChain]
+ -[BRCUserDefaults telemetryEventIdentifiersToReportErrorsChain].cold.1
+ -[BRCUserNotificationRequestAccessApprovedRequestID iconAppIdentifier]
+ -[BRCUserNotificationRequestAccessRequestID iconAppIdentifier]
+ -[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]
+ -[NSError(BRCAdditions) _getErrorsChainWithErrorsCount:]
+ -[NSError(BRCAdditions) brc_getErrorsChainJSONStringWithErrorsCount:error:]
+ -[NSError(BRCAdditions) brc_getErrorsChainJSONStringWithErrorsCount:error:].cold.1
+ -[NSError(BRCAdditions) brc_isNetworkUnreachableDueToCellularError]
+ GCC_except_table118
+ GCC_except_table140
+ GCC_except_table161
+ GCC_except_table163
+ GCC_except_table166
+ GCC_except_table574
+ OBJC_IVAR_$_AppTelemetryInvestigation._errorsChain
+ _BRiCloudIconUTI
+ _NSMultipleUnderlyingErrorsKey
+ _OBJC_IVAR_$_BRCGlobalProgress._resumeGroup
+ ___102-[BRCUserNotificationRequestAccessRequestID _approveRequester:share:sessionContext:completionHandler:]_block_invoke.83
+ ___102-[BRCUserNotificationRequestAccessRequestID _approveRequester:share:sessionContext:completionHandler:]_block_invoke.83.cold.1
+ ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.162
+ ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.162.cold.1
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.106
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.106.cold.1
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.108
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.110
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.115
+ ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.115.cold.1
+ ___125-[BRCXPCRegularIPCsClient(FPFSAdditions) uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.193
+ ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.195
+ ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.196
+ ___63-[BRCUserDefaults telemetryEventIdentifiersToReportErrorsChain]_block_invoke
+ ___72-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]_block_invoke.191
+ ___73-[BRCXPCRegularIPCsClient(FPFSAdditions) getCKRecordIDsForFPItems:reply:]_block_invoke.195
+ ___77-[BRCXPCRegularIPCsClient(FPFSAdditions) copyShareIDForItemIdentifier:reply:]_block_invoke.156
+ ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke
+ ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke.144
+ ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke.145
+ ___84-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke.145.cold.1
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.178
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.184
+ ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.152
+ ___88-[BRCUserNotificationRequestAccessRequestID _saveShareOperationForShare:sessionContext:]_block_invoke.75
+ ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) checkIfItemIsShareableWithItemIdentifier:reply:]_block_invoke.158
+ ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) startOperation:toWaitForFPFSMigrationWithReply:]_block_invoke.165
+ ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getCreatorNameComponentsForItemIdentifier:reply:]_block_invoke.159
+ ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.185
+ ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.186
+ ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.150
+ ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.150.cold.1
+ ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]_block_invoke.151
+ ___95-[BRCXPCRegularIPCsClient(FPFSAdditions) launchItemCountMismatchChecksForItemIdentifier:reply:]_block_invoke.154
+ ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getClientSaltingVerificationKeysAtItemIdentifier:reply:]_block_invoke.170
+ ___block_descriptor_56_e8_32s40s48s_e23_B16?0"BRCAppLibrary"8ls32l8s40l8s48l8
+ ___block_literal_global.113
+ ___block_literal_global.164
+ ___block_literal_global.198
+ ___block_literal_global.2422
+ ___block_literal_global.2446
+ ___block_literal_global.2462
+ ___block_literal_global.247
+ ___block_literal_global.2543
+ ___block_literal_global.2884
+ ___block_literal_global.87
+ ___block_literal_global.96
+ ___block_literal_global.98
+ _objc_msgSend$_errorsChainIfNecessaryForAppTelemetryIdentifier:error:
+ _objc_msgSend$_getErrorsChainWithErrorsCount:
+ _objc_msgSend$_newTelemetryEventWithIdentifier:error:
+ _objc_msgSend$_newTelemetryEventWithIdentifier:zoneWithMangledID:enhancedDrivePrivacyEnabled:error:errorDescription:itemIDString:
+ _objc_msgSend$_pushTopicForIdentifier:
+ _objc_msgSend$_syncUpSizeWithVersionSize:
+ _objc_msgSend$_transferSizeWithVersionSize:
+ _objc_msgSend$brc_errorNetworkUnreachableDueToCellularOverICDDisabled
+ _objc_msgSend$brc_getErrorsChainJSONStringWithErrorsCount:error:
+ _objc_msgSend$brc_isNetworkUnreachableDueToCellularError
+ _objc_msgSend$iconAppIdentifier
+ _objc_msgSend$iconForApplicationIdentifier:
+ _objc_msgSend$iconWithUTI:
+ _objc_msgSend$newTelemetryEventWithIdentifier:zoneWithMangledID:
+ _objc_msgSend$newTelemetryEventWithIdentifier:zoneWithMangledID:enhancedDrivePrivacyEnabled:
+ _objc_msgSend$newTelemetryEventWithIdentifier:zoneWithMangledID:enhancedDrivePrivacyEnabled:fromError:errorDescription:itemIDString:
+ _objc_msgSend$setErrorsChain:
+ _objc_msgSend$telemetryEventIdentifiersToReportErrorsChain
+ _telemetryEventIdentifiersToReportErrorsChain.defaultSet
+ _telemetryEventIdentifiersToReportErrorsChain.onceToken
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) _newTelemetryEventInZoneWithMangledID:enhancedDrivePrivacyEnabled:error:errorDescription:itemIDString:]
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) _newTelemetryEventWithError:]
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) newTelemetryEventInZoneWithMangledID:]
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) newTelemetryEventInZoneWithMangledID:enhancedDrivePrivacyEnabled:]
- +[AppTelemetryTimeSeriesEvent(BRCAdditions) newTelemetryEventInZoneWithMangledID:enhancedDrivePrivacyEnabled:fromError:errorDescription:itemIDString:]
- -[CKRecord(BRCSharingAdditions) brc_iconTypeNameForUserNotification]
- -[NSError(BRCAdditions) brc_isNetworkUnreachableDueToCellularConstraintError]
- GCC_except_table129
- GCC_except_table156
- GCC_except_table162
- GCC_except_table572
- _OBJC_CLASS_$_ISIcon
- _OBJC_CLASS_$_ISImageDescriptor
- ___102-[BRCUserNotificationRequestAccessRequestID _approveRequester:share:sessionContext:completionHandler:]_block_invoke.80
- ___102-[BRCUserNotificationRequestAccessRequestID _approveRequester:share:sessionContext:completionHandler:]_block_invoke.80.cold.1
- ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.160
- ___104-[BRCXPCRegularIPCsClient(FPFSAdditions) validateConnectionDomainWithDomainIdentifier:databaseID:reply:]_block_invoke.160.cold.1
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.103
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.103.cold.1
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.105
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.107
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.112
- ___118-[BRCUserNotificationRequestAccessRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.112.cold.1
- ___125-[BRCXPCRegularIPCsClient(FPFSAdditions) uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:options:reply:]_block_invoke.191
- ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.191
- ___126-[BRCUserNotificationRequestAccessApprovedRequestID performOnActionWithNotificationResponse:sessionContext:completionHandler:]_block_invoke.192
- ___57-[BRCNotificationManager hasWatcherMatchingGlobalItemID:]_block_invoke
- ___72-[BRCXPCRegularIPCsClient(FPFSAdditions) waitForStabilizationWithReply:]_block_invoke.189
- ___73-[BRCXPCRegularIPCsClient(FPFSAdditions) getCKRecordIDsForFPItems:reply:]_block_invoke.193
- ___77-[BRCXPCRegularIPCsClient(FPFSAdditions) copyShareIDForItemIdentifier:reply:]_block_invoke.154
- ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.176
- ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerSaltingKeysAtItemIdentifier:reply:]_block_invoke.182
- ___85-[BRCXPCRegularIPCsClient(FPFSAdditions) refreshSharingStateForItemIdentifier:reply:]_block_invoke.150
- ___88-[BRCUserNotificationRequestAccessRequestID _saveShareOperationForShare:sessionContext:]_block_invoke.72
- ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) checkIfItemIsShareableWithItemIdentifier:reply:]_block_invoke.156
- ___89-[BRCXPCRegularIPCsClient(FPFSAdditions) startOperation:toWaitForFPFSMigrationWithReply:]_block_invoke.163
- ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getCreatorNameComponentsForItemIdentifier:reply:]_block_invoke.157
- ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.183
- ___90-[BRCXPCRegularIPCsClient(FPFSAdditions) getServerContentSignatureAtItemIdentifier:reply:]_block_invoke.184
- ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.144
- ___91-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:forURL:reply:]_block_invoke.144.cold.1
- ___92-[BRCXPCRegularIPCsClient(FPFSAdditions) cloneLatestContentRevisionForItemIdentifier:reply:]_block_invoke.149
- ___95-[BRCXPCRegularIPCsClient(FPFSAdditions) launchItemCountMismatchChecksForItemIdentifier:reply:]_block_invoke.152
- ___97-[BRCXPCRegularIPCsClient(FPFSAdditions) getClientSaltingVerificationKeysAtItemIdentifier:reply:]_block_invoke.168
- ___block_literal_global.162
- ___block_literal_global.194
- ___block_literal_global.2431
- ___block_literal_global.2447
- ___block_literal_global.2532
- ___block_literal_global.2873
- ___block_literal_global.84
- ___block_literal_global.93
- ___block_literal_global.95
- ___block_literal_global.99
- _kISImageDescriptorNotification
- _objc_msgSend$_newTelemetryEventInZoneWithMangledID:enhancedDrivePrivacyEnabled:error:errorDescription:itemIDString:
- _objc_msgSend$_newTelemetryEventWithError:
- _objc_msgSend$brc_iconTypeNameForUserNotification
- _objc_msgSend$brc_isNetworkUnreachableDueToCellularConstraintError
- _objc_msgSend$iconType
- _objc_msgSend$iconWithData:
- _objc_msgSend$imageDescriptorNamed:
- _objc_msgSend$initWithType:
- _objc_msgSend$newTelemetryEventInZoneWithMangledID:
- _objc_msgSend$newTelemetryEventInZoneWithMangledID:enhancedDrivePrivacyEnabled:
- _objc_msgSend$newTelemetryEventInZoneWithMangledID:enhancedDrivePrivacyEnabled:fromError:errorDescription:itemIDString:
- _objc_msgSend$prepareImageForDescriptor:
- _objc_msgSend$setIconType:
CStrings:
+ "+[AppTelemetryTimeSeriesEvent(BRCAdditions) _errorsChainIfNecessaryForAppTelemetryIdentifier:error:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) calculateSignatureForItemIdentifier:reply:]_block_invoke"
+ "-[NSError(BRCAdditions) brc_getErrorsChainJSONStringWithErrorsCount:error:]"
+ "@24@0:8^i16"
+ "@32@0:8^i16^@24"
+ "@56@0:8i16@20B28@32@40@48"
+ "@60@0:8i16@20@28@36@44@52"
+ "D"
+ "T@\"NSObject<OS_dispatch_group>\",R,N,V_resumeGroup"
+ "UE"
+ "UES"
+ "[CRIT] Assertion failed: [error.userInfo[@kBRCErrorForErrorsChainKey] isKindOfClass:[NSError class]]%@"
+ "[CRIT] Assertion failed: errorsCount != nil%@"
+ "[DEBUG] Finished resolving postpone upload errors for cellular disabled with %@%@"
+ "[DEBUG] Rescheduling uploads due to unlimited updates toggle%@"
+ "[ERROR] failed to convert dictionary to json.\n%@\n%@%@"
+ "_errorsChain"
+ "_errorsChainIfNecessaryForAppTelemetryIdentifier:error:"
+ "_getErrorsChainWithErrorsCount:"
+ "_newTelemetryEventWithIdentifier:error:"
+ "_newTelemetryEventWithIdentifier:zoneWithMangledID:enhancedDrivePrivacyEnabled:error:errorDescription:itemIDString:"
+ "_pushTopicForIdentifier:"
+ "_resumeGroup"
+ "_syncUpSizeWithVersionSize:"
+ "_transferSizeWithVersionSize:"
+ "brc-error-for-errors-chain"
+ "brc_errorNetworkUnreachableDueToCellularOverICDDisabled"
+ "brc_getErrorsChainJSONStringWithErrorsCount:error:"
+ "brc_isNetworkUnreachableDueToCellularError"
+ "calculateSignatureForItemIdentifier:reply:"
+ "errorsChain"
+ "hasErrorsChain"
+ "iconAppIdentifier"
+ "iconForApplicationIdentifier:"
+ "iconWithUTI:"
+ "newTelemetryEventWithIdentifier:zoneWithMangledID:"
+ "newTelemetryEventWithIdentifier:zoneWithMangledID:enhancedDrivePrivacyEnabled:"
+ "newTelemetryEventWithIdentifier:zoneWithMangledID:enhancedDrivePrivacyEnabled:fromError:errorDescription:itemIDString:"
+ "resumeGroup"
+ "setErrorsChain:"
+ "telemetry.event-identifiers-to-report-errors-chain"
+ "telemetryEventIdentifiersToReportErrorsChain"
- "[DEBUG] Finished resolving postpone upload errors with %@%@"
- "[DEBUG] Rescheduling uploads due to unlimited updats toggle%@"
- "_newTelemetryEventInZoneWithMangledID:enhancedDrivePrivacyEnabled:error:errorDescription:itemIDString:"
- "_newTelemetryEventWithError:"
- "brc_iconTypeNameForUserNotification"
- "brc_isNetworkUnreachableDueToCellularConstraintError"
- "com.apple.groups-folder"
- "iconWithData:"
- "imageDescriptorNamed:"
- "initWithType:"
- "newTelemetryEventInZoneWithMangledID:"
- "newTelemetryEventInZoneWithMangledID:enhancedDrivePrivacyEnabled:"
- "newTelemetryEventInZoneWithMangledID:enhancedDrivePrivacyEnabled:fromError:errorDescription:itemIDString:"
- "prepareImageForDescriptor:"

```
