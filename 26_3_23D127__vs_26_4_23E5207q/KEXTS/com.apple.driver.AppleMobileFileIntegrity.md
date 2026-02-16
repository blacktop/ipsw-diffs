## com.apple.driver.AppleMobileFileIntegrity

> `com.apple.driver.AppleMobileFileIntegrity`

```diff

-1045.80.8.0.0
-  __TEXT.__cstring: 0xc347
-  __TEXT.__const: 0x1570
+1045.100.75.0.0
+  __TEXT.__cstring: 0xb90a
+  __TEXT.__const: 0x1538
   __TEXT.__os_log: 0x32d
-  __TEXT_EXEC.__text: 0x28c08
+  __TEXT_EXEC.__text: 0x281bc
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x74a
+  __DATA.__data: 0x56a
   __DATA.__common: 0xb0
   __DATA.__bss: 0x81
-  __DATA_CONST.__auth_got: 0x7f8
+  __DATA_CONST.__auth_got: 0x808
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x40d0
+  __DATA_CONST.__const: 0x40b8
   __DATA_CONST.__kalloc_type: 0xf80
   __DATA_CONST.__kalloc_var: 0x1400
   __DATA_CONST.__assert: 0xf0
-  UUID: FE87B43D-C464-3225-B1D5-A9F989D2E214
-  Functions: 894
+  UUID: 6728C3B2-458C-3AED-8D3D-2573AB4C5CC1
+  Functions: 898
   Symbols:   0
-  CStrings:  1233
+  CStrings:  1170
 
CStrings:
+ "(data && dataLength && dataLength <= kACMControlMaxDataLength) || (!data && !dataLength)"
+ "(data && dataLength && dataLength <= kACMEnvironmentVariableMaxDataLength) || (!data && !dataLength)"
+ "(keybagUuid && keybagUuidLength == UUID_LEN) || (!keybagUuid && !keybagUuidLength)"
+ "*"
+ "/Library/Caches/com.apple.xbs/1D43EACD-F3C7-46AB-AD58-2F164BD3EB02/TemporaryDirectory.9X72Ti/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
+ "/Library/Caches/com.apple.xbs/1D43EACD-F3C7-46AB-AD58-2F164BD3EB02/TemporaryDirectory.9X72Ti/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
+ "/Library/Caches/com.apple.xbs/1D43EACD-F3C7-46AB-AD58-2F164BD3EB02/TemporaryDirectory.9X72Ti/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
+ "22:47:44"
+ "CoreEntitlements: subset | %.*s: 0x%04X\n"
+ "Feb  4 2026"
+ "S24@?0r^{_CEKeyValuePair={_CEElement={?=*Q}{?=Q{?=*Q}}}{_CEValueTypePair=I{_CEElement={?=*Q}{?=Q{?=*Q}}}}}8^{_CEIterateArgs=Q^vB}16"
+ "S24@?0r^{_CEValueTypePair=I{_CEElement={?=*Q}{?=Q{?=*Q}}}}8^{_CEIterateArgs=Q^vB}16"
+ "UTIL_OPTIONAL_BUFFER(outBuffer,outSize)"
+ "cmd = (acm_command_t *)acm_malloc_data(cmdSize)"
+ "com.apple.contactsd"
+ "os_add_overflow(sizeof(acm_command_t), dataSize, &cmdSize) == 0 "
+ "v16@?0r^{_OSEntitlementsReadOnly=^{OSEntitlements}{_CEContext={_CEContextInfo=CI}{_CEElement={?=*Q}{?=Q{?=*Q}}}^{_CEElementIndex}Q{CEQueryContext={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}B}B}^{_CEContext}*{?=^{__SC_GenericBlob}}{?=BB}}8"
- "\"AMFI: unable to update legacy context: %u\" @%s:%d"
- "( ((outSize != nullptr && *outSize > 0) && outBuffer != nullptr) || ((outSize == nullptr || *outSize == 0) && outBuffer == nullptr) )"
- "(data && dataLength && dataLength <= 128) || (!data && !dataLength)"
- "(data && dataLength && dataLength <= 4096) || (!data && !dataLength)"
- "(keybagUuid && keybagUuidLength == 16) || (!keybagUuid && !keybagUuidLength)"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
- "20:48:39"
- "CoreEntitlements: %.*s | validate: 0x%04X\n"
- "CoreEntitlements: duplicate key | %.*s\n"
- "Jan 26 2026"
- "S24@?0r^{_CEKeyValuePair={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}{_CEValueTypePair=I{der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}}}8^{_CEIterateArgs=^vQQBS}16"
- "S24@?0r^{_CEValueTypePair=I{der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}}8^{_CEIterateArgs=^vQQBS}16"
- "__os_warn_unused(__builtin_add_overflow((sizeof(acm_command_t)), (dataSize), (&cmdSize))) == 0 "
- "cmd = (acm_command_t *)({ size_t sizeVal = (cmdSize); void *ptr = acm_mem_alloc_data(sizeVal); acm_mem_alloc_info(\"<data>\", ptr, sizeVal, \"/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c\", 22, __func__); ptr; })"
- "com.apple.AppleAccountUI.CustodianInviteMessageExtension"
- "com.apple.AppleAccountUI.LegacyContactMessageExtention"
- "com.apple.Bridge.GreenfieldThumbnailExtension"
- "com.apple.CoreSVG.thumbnail"
- "com.apple.CoreSpotlight.TestImporter"
- "com.apple.CoreSpotlight.TextImporter"
- "com.apple.DriverKit-AppleBCMWLAN"
- "com.apple.FTLivePhotoService"
- "com.apple.GenerativePlaygroundApp.MessagesExtension"
- "com.apple.ImageIO.imageimporter"
- "com.apple.MADownloadServiceBuiltin"
- "com.apple.MobileSMS.MessagesTranscriptExtension"
- "com.apple.Music.MusicCoreSpotlightExtension"
- "com.apple.OfficeImport.OfficeSpotlightImporter"
- "com.apple.PDFKit.PDFImporter"
- "com.apple.PassKit.PassKitSpotlightIndexExtension"
- "com.apple.PassKit.PassKitThumbnailExtension"
- "com.apple.PassKitWrapperXPCServiceUI"
- "com.apple.Passbook.QuicklookPreviewExtension"
- "com.apple.Photos.CPLDiagnose"
- "com.apple.TelephonyUtilities.PhoneIntentHandler"
- "com.apple.UserEventAgent"
- "com.apple.UserNotificationsServer.UserNotificationsThumbnailProvider"
- "com.apple.VoiceMemos.SpotlightIndexExtension"
- "com.apple.WebKit.WebContent.EnhancedSecurity"
- "com.apple.WorkflowKit.ShortcutsIntents"
- "com.apple.accountsd"
- "com.apple.announced"
- "com.apple.avconferenced"
- "com.apple.backupd"
- "com.apple.captiveagent"
- "com.apple.contacts.ContactsCoreSpotlightExtension"
- "com.apple.eapolclient"
- "com.apple.iBooks.iBooksSpotlightExtension"
- "com.apple.kml.CarKeyAppIntents"
- "com.apple.mediaplaybackd"
- "com.apple.mobileassetd"
- "com.apple.mobilenotes.SpotlightIndexExtension"
- "com.apple.mobilephone.SpotlightIndexExtension"
- "com.apple.news.NewsArticleQuickLook"
- "com.apple.podcasts.SpotlightIndexExtension"
- "com.apple.polarisd"
- "com.apple.reminders.spotlightindexextension"
- "com.apple.sbd"
- "com.apple.securepairingd"
- "com.apple.security.cryptexd"
- "com.apple.siri.SiriGeo.SiriGeoAppIntentExtension"
- "com.apple.siri.SiriNotificationsAppIntentsExtension"
- "com.apple.siri.SiriPhoneAppIntentsExtension"
- "com.apple.siri.SiriSecureSettingsMigrationExtension"
- "com.apple.siri.SiriVideoAppIntents"
- "com.apple.siri.messages.SiriMessagesAppIntentsExtension"
- "com.apple.splashboardd"
- "com.apple.spotlightknowledged.updater"
- "com.apple.thermalmonitord"
- "com.apple.tips.TipsSpotlightIndexExtension"
- "com.apple.tv.TVCoreSpotlightExtension"
- "com.apple.webapp"
- "com.apple.wifi.manager"
- "com.apple.xpc.launchd"
- "der_vm_container_from_context"
- "der_vm_iterate_nocopy"
- "run-invalid-allow"
- "v16@?0r^{_OSEntitlementsReadOnly=^{OSEntitlements}{_CEContext={_CEContextInfo=CI}{CEQueryContext={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}B}}^{_CEContext}*{?=^{__SC_GenericBlob}}{?=BB}}8"

```
