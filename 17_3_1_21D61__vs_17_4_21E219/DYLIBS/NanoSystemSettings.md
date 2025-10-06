## NanoSystemSettings

> `/System/Library/PrivateFrameworks/NanoSystemSettings.framework/NanoSystemSettings`

```diff

   __TEXT.__oslogstring: 0x5dd
   __TEXT.__unwind_info: 0xc84
   __TEXT.__objc_classname: 0x651
-  __TEXT.__objc_methname: 0x4801
+  __TEXT.__objc_methname: 0x4815
   __TEXT.__objc_methtype: 0x96b
   __TEXT.__objc_stubs: 0x2680
   __DATA_CONST.__got: 0xa0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4fc0
   __DATA_CONST.__objc_selrefs: 0x1328
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x140
+  __DATA_CONST.__objc_superrefs: 0x1e8
   __AUTH_CONST.__cfstring: 0x1f60
   __AUTH_CONST.__objc_const: 0x15a8
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__auth_got: 0x268
   __AUTH.__objc_data: 0x1310
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x140
-  __DATA.__objc_superrefs: 0x1e8
   __DATA.__objc_ivar: 0x30c
   __DATA.__data: 0x244
   __DATA.__bss: 0x50

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 18B2BC9F-12B6-3E66-9FA6-4493A7FDA0C6
+  UUID: 8C81CC9E-98A0-3AEA-A8B7-C55A6C3B2AFE
   Functions: 1412
   Symbols:   4164
-  CStrings:  1650
+  CStrings:  1651
 
Symbols:
+ ___24-[NSSManager connection]_block_invoke.140
+ ___27-[NSSManager getAboutInfo:]_block_invoke.241
+ ___27-[NSSManager getAboutInfo:]_block_invoke.243
+ ___27-[NSSManager getAboutInfo:]_block_invoke_2.242
+ ___27-[NSSManager getUsageData:]_block_invoke.201
+ ___27-[NSSManager getUsageData:]_block_invoke.204
+ ___27-[NSSManager getUsageData:]_block_invoke_2.202
+ ___28-[NSSManager getWatchFaces:]_block_invoke.292
+ ___28-[NSSManager getWatchFaces:]_block_invoke.294
+ ___28-[NSSManager getWatchFaces:]_block_invoke.296
+ ___28-[NSSManager getWatchFaces:]_block_invoke_2.293
+ ___29-[NSSManager getLocalesInfo:]_block_invoke.284
+ ___29-[NSSManager getLocalesInfo:]_block_invoke.287
+ ___29-[NSSManager getLocalesInfo:]_block_invoke_2.285
+ ___30-[NSSManager getProfilesInfo:]_block_invoke.255
+ ___30-[NSSManager getProfilesInfo:]_block_invoke.257
+ ___30-[NSSManager getProfilesInfo:]_block_invoke_2.256
+ ___32-[NSSManager getLegalDocuments:]_block_invoke.280
+ ___32-[NSSManager getLegalDocuments:]_block_invoke.283
+ ___32-[NSSManager getLegalDocuments:]_block_invoke_2.281
+ ___40-[NSSManager fetchBetaEnrollmentStatus:]_block_invoke.301
+ ___40-[NSSManager fetchBetaEnrollmentStatus:]_block_invoke.303
+ ___40-[NSSManager fetchBetaEnrollmentStatus:]_block_invoke.305
+ ___40-[NSSManager fetchBetaEnrollmentStatus:]_block_invoke_2.302
+ ___46-[NSSManager getDiagnosticLogsInfoByCateogry:]_block_invoke.235
+ ___46-[NSSManager getDiagnosticLogsInfoByCateogry:]_block_invoke.237
+ ___46-[NSSManager getDiagnosticLogsInfoByCateogry:]_block_invoke_2.236
+ ___47-[NSSManager installProfile:completionHandler:]_block_invoke.267
+ ___47-[NSSManager installProfile:completionHandler:]_block_invoke.269
+ ___47-[NSSManager installProfile:completionHandler:]_block_invoke.271
+ ___47-[NSSManager installProfile:completionHandler:]_block_invoke_2.268
+ ___47-[NSSManager installProfile:completionHandler:]_block_invoke_2.270
+ ___49-[NSSManager deleteDiagnosticLogFile:withResult:]_block_invoke.238
+ ___49-[NSSManager deleteDiagnosticLogFile:withResult:]_block_invoke.240
+ ___49-[NSSManager deleteDiagnosticLogFile:withResult:]_block_invoke_2.239
+ ___51-[NSSManager enableAirplaneMode:completionHandler:]_block_invoke.144
+ ___51-[NSSManager enableAirplaneMode:completionHandler:]_block_invoke.147
+ ___51-[NSSManager enableAirplaneMode:completionHandler:]_block_invoke.156
+ ___51-[NSSManager enableAirplaneMode:completionHandler:]_block_invoke_2.146
+ ___51-[NSSManager enableAirplaneMode:completionHandler:]_block_invoke_2.148
+ ___51-[NSSManager setSafetyXpcInterruptionHandlerBlock:]_block_invoke.141
+ ___55-[NSSManager purgeUsageBundleWithId:completionHandler:]_block_invoke.213
+ ___55-[NSSManager purgeUsageBundleWithId:completionHandler:]_block_invoke.215
+ ___55-[NSSManager purgeUsageBundleWithId:completionHandler:]_block_invoke.217
+ ___55-[NSSManager purgeUsageBundleWithId:completionHandler:]_block_invoke_2.214
+ ___55-[NSSManager purgeUsageBundleWithId:completionHandler:]_block_invoke_2.216
+ ___56-[NSSManager cancelDiagnosticLogTranfer:withCompletion:]_block_invoke.226
+ ___56-[NSSManager cancelDiagnosticLogTranfer:withCompletion:]_block_invoke.228
+ ___56-[NSSManager cancelDiagnosticLogTranfer:withCompletion:]_block_invoke_2.227
+ ___56-[NSSManager getDiagnosticLogFileFromGizmo:withResults:]_block_invoke.218
+ ___56-[NSSManager getDiagnosticLogFileFromGizmo:withResults:]_block_invoke.220
+ ___56-[NSSManager getDiagnosticLogFileFromGizmo:withResults:]_block_invoke_2.219
+ ___60-[NSSManager removeProfileWithIdentifier:completionHandler:]_block_invoke.275
+ ___60-[NSSManager removeProfileWithIdentifier:completionHandler:]_block_invoke.277
+ ___60-[NSSManager removeProfileWithIdentifier:completionHandler:]_block_invoke.279
+ ___60-[NSSManager removeProfileWithIdentifier:completionHandler:]_block_invoke_2.276
+ ___60-[NSSManager removeProfileWithIdentifier:completionHandler:]_block_invoke_2.278
+ ___60-[NSSManager setAirplaneModeSettings:withCompletionHandler:]_block_invoke.199
+ ___60-[NSSManager setAirplaneModeSettings:withCompletionHandler:]_block_invoke_2.200
+ ___62-[NSSManager getAccountsInfoForAccountType:completionHandler:]_block_invoke.249
+ ___62-[NSSManager getAccountsInfoForAccountType:completionHandler:]_block_invoke.251
+ ___62-[NSSManager getAccountsInfoForAccountType:completionHandler:]_block_invoke_2.250
+ ___62-[NSSManager obliterateGizmoPreservingeSIM:completionHandler:]_block_invoke.244
+ ___62-[NSSManager obliterateGizmoPreservingeSIM:completionHandler:]_block_invoke.246
+ ___62-[NSSManager obliterateGizmoPreservingeSIM:completionHandler:]_block_invoke.248
+ ___62-[NSSManager obliterateGizmoPreservingeSIM:completionHandler:]_block_invoke_2.245
+ ___62-[NSSManager obliterateGizmoPreservingeSIM:completionHandler:]_block_invoke_2.247
+ ___64-[NSSManager retrieveAirplaneModeSettingsWithCompletionHandler:]_block_invoke.190
+ ___64-[NSSManager retrieveAirplaneModeSettingsWithCompletionHandler:]_block_invoke_2.191
+ ___65-[NSSManager retrieveDiagnosticLogTransferProgress:withProgress:]_block_invoke.222
+ ___65-[NSSManager retrieveDiagnosticLogTransferProgress:withProgress:]_block_invoke.224
+ ___65-[NSSManager retrieveDiagnosticLogTransferProgress:withProgress:]_block_invoke_2.223
+ ___74-[NSSManager _updateBetaEnrollmentStatus:requiresUnenroll:withCompletion:]_block_invoke.312
+ ___74-[NSSManager _updateBetaEnrollmentStatus:requiresUnenroll:withCompletion:]_block_invoke.314
+ ___74-[NSSManager _updateBetaEnrollmentStatus:requiresUnenroll:withCompletion:]_block_invoke.316
+ ___74-[NSSManager _updateBetaEnrollmentStatus:requiresUnenroll:withCompletion:]_block_invoke_2.313
+ ___75-[NSSManager recordSoftwareUpdateSpaceFailure:osBeingUpdatedTo:completion:]_block_invoke.288
+ ___75-[NSSManager recordSoftwareUpdateSpaceFailure:osBeingUpdatedTo:completion:]_block_invoke.291
+ ___75-[NSSManager recordSoftwareUpdateSpaceFailure:osBeingUpdatedTo:completion:]_block_invoke_2.289
+ ___78-[NSSManager setWatchFaceIdentifier:forFocusModeIdentifier:completionHandler:]_block_invoke.297
+ ___78-[NSSManager setWatchFaceIdentifier:forFocusModeIdentifier:completionHandler:]_block_invoke.300
+ ___78-[NSSManager setWatchFaceIdentifier:forFocusModeIdentifier:completionHandler:]_block_invoke_2.298
+ ___88-[NSSManager getFullProfileInfoWithIdentifier:includeManagedPayloads:completionHandler:]_block_invoke.261
+ ___88-[NSSManager getFullProfileInfoWithIdentifier:includeManagedPayloads:completionHandler:]_block_invoke.263
+ ___88-[NSSManager getFullProfileInfoWithIdentifier:includeManagedPayloads:completionHandler:]_block_invoke_2.262
+ ___block_literal_global.143
- ___24-[NSSManager connection]_block_invoke.138
- ___27-[NSSManager getAboutInfo:]_block_invoke.240
- ___27-[NSSManager getAboutInfo:]_block_invoke.242
- ___27-[NSSManager getAboutInfo:]_block_invoke_2.241
- ___27-[NSSManager getUsageData:]_block_invoke.200
- ___27-[NSSManager getUsageData:]_block_invoke.203
- ___27-[NSSManager getUsageData:]_block_invoke_2.201
- ___28-[NSSManager getWatchFaces:]_block_invoke.291
- ___28-[NSSManager getWatchFaces:]_block_invoke.293
- ___28-[NSSManager getWatchFaces:]_block_invoke.295
- ___28-[NSSManager getWatchFaces:]_block_invoke_2.292
- ___29-[NSSManager getLocalesInfo:]_block_invoke.283
- ___29-[NSSManager getLocalesInfo:]_block_invoke.285
- ___29-[NSSManager getLocalesInfo:]_block_invoke_2.284
- ___30-[NSSManager getProfilesInfo:]_block_invoke.254
- ___30-[NSSManager getProfilesInfo:]_block_invoke.256
- ___30-[NSSManager getProfilesInfo:]_block_invoke_2.255
- ___32-[NSSManager getLegalDocuments:]_block_invoke.279
- ___32-[NSSManager getLegalDocuments:]_block_invoke.281
- ___32-[NSSManager getLegalDocuments:]_block_invoke_2.280
- ___40-[NSSManager fetchBetaEnrollmentStatus:]_block_invoke.300
- ___40-[NSSManager fetchBetaEnrollmentStatus:]_block_invoke.302
- ___40-[NSSManager fetchBetaEnrollmentStatus:]_block_invoke.304
- ___40-[NSSManager fetchBetaEnrollmentStatus:]_block_invoke_2.301
- ___46-[NSSManager getDiagnosticLogsInfoByCateogry:]_block_invoke.234
- ___46-[NSSManager getDiagnosticLogsInfoByCateogry:]_block_invoke.236
- ___46-[NSSManager getDiagnosticLogsInfoByCateogry:]_block_invoke_2.235
- ___47-[NSSManager installProfile:completionHandler:]_block_invoke.266
- ___47-[NSSManager installProfile:completionHandler:]_block_invoke.268
- ___47-[NSSManager installProfile:completionHandler:]_block_invoke.270
- ___47-[NSSManager installProfile:completionHandler:]_block_invoke_2.267
- ___47-[NSSManager installProfile:completionHandler:]_block_invoke_2.269
- ___49-[NSSManager deleteDiagnosticLogFile:withResult:]_block_invoke.237
- ___49-[NSSManager deleteDiagnosticLogFile:withResult:]_block_invoke.239
- ___49-[NSSManager deleteDiagnosticLogFile:withResult:]_block_invoke_2.238
- ___51-[NSSManager enableAirplaneMode:completionHandler:]_block_invoke.143
- ___51-[NSSManager enableAirplaneMode:completionHandler:]_block_invoke.146
- ___51-[NSSManager enableAirplaneMode:completionHandler:]_block_invoke.155
- ___51-[NSSManager enableAirplaneMode:completionHandler:]_block_invoke_2.145
- ___51-[NSSManager enableAirplaneMode:completionHandler:]_block_invoke_2.147
- ___51-[NSSManager setSafetyXpcInterruptionHandlerBlock:]_block_invoke.140
- ___55-[NSSManager purgeUsageBundleWithId:completionHandler:]_block_invoke.212
- ___55-[NSSManager purgeUsageBundleWithId:completionHandler:]_block_invoke.214
- ___55-[NSSManager purgeUsageBundleWithId:completionHandler:]_block_invoke.216
- ___55-[NSSManager purgeUsageBundleWithId:completionHandler:]_block_invoke_2.213
- ___55-[NSSManager purgeUsageBundleWithId:completionHandler:]_block_invoke_2.215
- ___56-[NSSManager cancelDiagnosticLogTranfer:withCompletion:]_block_invoke.225
- ___56-[NSSManager cancelDiagnosticLogTranfer:withCompletion:]_block_invoke.227
- ___56-[NSSManager cancelDiagnosticLogTranfer:withCompletion:]_block_invoke_2.226
- ___56-[NSSManager getDiagnosticLogFileFromGizmo:withResults:]_block_invoke.217
- ___56-[NSSManager getDiagnosticLogFileFromGizmo:withResults:]_block_invoke.219
- ___56-[NSSManager getDiagnosticLogFileFromGizmo:withResults:]_block_invoke_2.218
- ___60-[NSSManager removeProfileWithIdentifier:completionHandler:]_block_invoke.274
- ___60-[NSSManager removeProfileWithIdentifier:completionHandler:]_block_invoke.276
- ___60-[NSSManager removeProfileWithIdentifier:completionHandler:]_block_invoke.278
- ___60-[NSSManager removeProfileWithIdentifier:completionHandler:]_block_invoke_2.275
- ___60-[NSSManager removeProfileWithIdentifier:completionHandler:]_block_invoke_2.277
- ___60-[NSSManager setAirplaneModeSettings:withCompletionHandler:]_block_invoke.198
- ___60-[NSSManager setAirplaneModeSettings:withCompletionHandler:]_block_invoke_2.199
- ___62-[NSSManager getAccountsInfoForAccountType:completionHandler:]_block_invoke.248
- ___62-[NSSManager getAccountsInfoForAccountType:completionHandler:]_block_invoke.250
- ___62-[NSSManager getAccountsInfoForAccountType:completionHandler:]_block_invoke_2.249
- ___62-[NSSManager obliterateGizmoPreservingeSIM:completionHandler:]_block_invoke.243
- ___62-[NSSManager obliterateGizmoPreservingeSIM:completionHandler:]_block_invoke.245
- ___62-[NSSManager obliterateGizmoPreservingeSIM:completionHandler:]_block_invoke.247
- ___62-[NSSManager obliterateGizmoPreservingeSIM:completionHandler:]_block_invoke_2.244
- ___62-[NSSManager obliterateGizmoPreservingeSIM:completionHandler:]_block_invoke_2.246
- ___64-[NSSManager retrieveAirplaneModeSettingsWithCompletionHandler:]_block_invoke.189
- ___64-[NSSManager retrieveAirplaneModeSettingsWithCompletionHandler:]_block_invoke_2.190
- ___65-[NSSManager retrieveDiagnosticLogTransferProgress:withProgress:]_block_invoke.221
- ___65-[NSSManager retrieveDiagnosticLogTransferProgress:withProgress:]_block_invoke.223
- ___65-[NSSManager retrieveDiagnosticLogTransferProgress:withProgress:]_block_invoke_2.222
- ___74-[NSSManager _updateBetaEnrollmentStatus:requiresUnenroll:withCompletion:]_block_invoke.311
- ___74-[NSSManager _updateBetaEnrollmentStatus:requiresUnenroll:withCompletion:]_block_invoke.313
- ___74-[NSSManager _updateBetaEnrollmentStatus:requiresUnenroll:withCompletion:]_block_invoke.315
- ___74-[NSSManager _updateBetaEnrollmentStatus:requiresUnenroll:withCompletion:]_block_invoke_2.312
- ___75-[NSSManager recordSoftwareUpdateSpaceFailure:osBeingUpdatedTo:completion:]_block_invoke.287
- ___75-[NSSManager recordSoftwareUpdateSpaceFailure:osBeingUpdatedTo:completion:]_block_invoke.289
- ___75-[NSSManager recordSoftwareUpdateSpaceFailure:osBeingUpdatedTo:completion:]_block_invoke_2.288
- ___78-[NSSManager setWatchFaceIdentifier:forFocusModeIdentifier:completionHandler:]_block_invoke.296
- ___78-[NSSManager setWatchFaceIdentifier:forFocusModeIdentifier:completionHandler:]_block_invoke.298
- ___78-[NSSManager setWatchFaceIdentifier:forFocusModeIdentifier:completionHandler:]_block_invoke_2.297
- ___88-[NSSManager getFullProfileInfoWithIdentifier:includeManagedPayloads:completionHandler:]_block_invoke.260
- ___88-[NSSManager getFullProfileInfoWithIdentifier:includeManagedPayloads:completionHandler:]_block_invoke.262
- ___88-[NSSManager getFullProfileInfoWithIdentifier:includeManagedPayloads:completionHandler:]_block_invoke_2.261
- ___block_literal_global.142
CStrings:
+ "T@\"NSString\",?,R,C"

```
