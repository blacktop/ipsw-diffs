## WelcomeKit

> `/System/Library/PrivateFrameworks/WelcomeKit.framework/WelcomeKit`

```diff

-829.80.170.0.0
-  __TEXT.__text: 0x73c0
-  __TEXT.__auth_stubs: 0x470
+1224.100.67.0.0
+  __TEXT.__text: 0x7be4
+  __TEXT.__auth_stubs: 0x440
   __TEXT.__objc_methlist: 0x1044
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x11c8
   __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__unwind_info: 0x380
   __TEXT.__objc_classname: 0x1ef
   __TEXT.__objc_methname: 0x26bd
   __TEXT.__objc_methtype: 0x721

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x248
+  __AUTH_CONST.__auth_got: 0x230
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0x15a0
   __AUTH_CONST.__objc_const: 0x2010

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CB6A6E09-C450-3D80-BE0C-5B67CA7E612C
+  UUID: A1A74A1F-D1C2-3E72-A117-CD6DF17715B5
   Functions: 330
-  Symbols:   1231
+  Symbols:   1228
   CStrings:  948
 
Symbols:
+ _objc_release_x28
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_release_x2
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x24
- _objc_retain_x3
- _objc_retain_x6
- _objc_retain_x8
Functions:
~ -[WLDeviceAuthentication initWithCoder:] : 112 -> 116
~ -[WLPayload dictionary] : 1124 -> 1188
~ -[WLPayload setMessages:] : 12 -> 64
~ -[WLPayload setPhotos:] : 12 -> 64
~ -[WLPayload setVideos:] : 12 -> 64
~ -[WLPayload setContacts:] : 12 -> 64
~ -[WLPayload setCalendars:] : 12 -> 64
~ -[WLPayload setBookmarks:] : 12 -> 64
~ -[WLPayload setAccounts:] : 12 -> 64
~ -[WLPayload setFiles:] : 12 -> 64
~ -[WLPayload setAccessibilitySettings:] : 12 -> 64
~ -[WLPayload setDisplaySettings:] : 12 -> 64
~ +[WLTelemetry sharedInstance] : 68 -> 84
~ -[WLTelemetry send:payload:] : 204 -> 196
~ ___28-[WLTelemetry send:payload:]_block_invoke : 8 -> 56
~ -[WLTelemetry wifiDidFail] : 152 -> 156
~ -[WLTelemetry deviceDidFailWithTimeout] : 152 -> 156
~ -[WLTelemetry deviceDidFailWithAuthenticationError] : 152 -> 156
~ -[WLTelemetry migratorDidFinish:] : 144 -> 148
~ -[WLTelemetry _telemetryDictionaryForPreparatoryDataDidComplete:contentType:duration:android:model:version:] : 376 -> 368
~ -[WLTelemetry preparatoryDataDidComplete:contentType:duration:android:model:version:] : 396 -> 364
~ -[WLTelemetry _telemetryDictionaryForContentTypeDidComplete:downloadByteCount:importRecordCount:importFailedRecordCount:downloadDuration:importDuration:android:model:version:] : 536 -> 544
~ -[WLTelemetry contentTypeDidComplete:downloadByteCount:importRecordCount:importFailedRecordCount:downloadDuration:importDuration:android:model:version:] : 352 -> 324
~ -[WLTelemetry importDidFailSilentlyForContentType:] : 184 -> 180
~ ___51-[WLTelemetry importDidFailSilentlyForContentType:]_block_invoke : 132 -> 136
~ -[WLTelemetry didResolveTimeEstimate:forDownloadTask:threshold:actualTime:] : 220 -> 216
~ ___75-[WLTelemetry didResolveTimeEstimate:forDownloadTask:threshold:actualTime:]_block_invoke : 252 -> 264
~ ___52-[WLTelemetry userDidChooseToInstallMigratableApps:]_block_invoke : 180 -> 188
~ ___59-[WLTelemetry didLookupAppsWithMatchedApps:mismatchedApps:]_block_invoke : 224 -> 236
~ ___48-[WLTelemetry photoLibraryDidFailWithExtension:]_block_invoke : 132 -> 136
~ ___29-[WLTelemetry didLoadQRCode:]_block_invoke : 180 -> 188
~ ___64-[WLTelemetry didLoadAndroidStore:selected:canceled:inAttempts:]_block_invoke : 280 -> 296
~ -[WLContext initWithCoder:] : 1016 -> 1084
~ -[WLContext encodeWithCoder:] : 428 -> 436
~ -[WLContext isEnabled] : 392 -> 388
~ -[WLContext setApplication:] : 12 -> 64
~ -[WLContext setAccount:] : 12 -> 64
~ -[WLContext setMessage:] : 12 -> 64
~ -[WLContext setContact:] : 12 -> 64
~ -[WLContext setCallHistory:] : 12 -> 64
~ -[WLContext setCalendar:] : 12 -> 64
~ -[WLContext setBookmark:] : 12 -> 64
~ -[WLContext setFile:] : 12 -> 64
~ -[WLContext setImage:] : 12 -> 64
~ -[WLContext setVideo:] : 12 -> 64
~ -[WLContext setVoiceMemo:] : 12 -> 64
~ -[WLContext setAlbum:] : 12 -> 64
~ -[WLContext setContainer:] : 12 -> 64
~ -[WLContext setAccessibilitySetting:] : 12 -> 64
~ -[WLContext setDisplaySetting:] : 12 -> 64
~ -[WLContext setPlaceholder:] : 12 -> 64
~ -[WLContext setSim:] : 12 -> 64
~ -[WLDaemonConnection daemonWithErrorHandler:] : 108 -> 116
~ -[WLDaemonConnection invalidateDaemonConnection] : 64 -> 68
~ +[WLDaemonController sharedInstance] : 68 -> 84
~ ___58-[WLDaemonController getLocalImportOptionsWithCompletion:]_block_invoke : 268 -> 276
~ ___58-[WLDaemonController getLocalImportOptionsWithCompletion:]_block_invoke_2 : 156 -> 160
~ -[WLDaemonController importLocalContent] : 156 -> 164
~ -[WLDaemonController setStashDataLocally:] : 172 -> 180
~ -[WLDaemonController setConnection:] : 12 -> 64
~ _WLDaemonExportedInterface : 268 -> 284
~ _WLDataMigrationDelegateInterface : 976 -> 1044
~ -[WLImportContext initWithCoder:] : 248 -> 260
~ -[WLImportContext encodeWithCoder:] : 228 -> 240
~ +[WLLogController sharedLogger] : 68 -> 84
~ __loggingUserDefaultsChangedNotificationHandler : 84 -> 88
~ _WLLoggingEnabled : 64 -> 68
~ __WLLog : 120 -> 124
~ -[WLDataMigrationController startMigrationUsingRetryPolicies:] : 296 -> 300
~ ___62-[WLDataMigrationController startMigrationUsingRetryPolicies:]_block_invoke_2 : 236 -> 244
~ -[WLDataMigrationController deleteMessages] : 132 -> 136
~ -[WLDataMigrationController lookupAppDataContainer:] : 156 -> 160
~ -[WLDataMigrationController testAMSPurchase] : 132 -> 136
~ -[WLDataMigrationControllerSurrogate startMigrationUsingRetryPolicies:] : 196 -> 200
~ -[WLDataMigrationControllerSurrogate _startMigrationUsingRetryPolicies:] : 840 -> 896
~ -[WLMigrationKitController run:] : 276 -> 280
~ -[WLMigrationKitController cancel] : 72 -> 76
~ -[WLSourceDevice initWithCoder:] : 940 -> 1004
~ -[WLSourceDevice encodeWithCoder:] : 548 -> 556
~ __didDiscoverCandidate : 252 -> 256
~ __sourceDevicesDidChange : 252 -> 256
~ ___71-[WLSourceDevicesController startWiFiAndDeviceDiscoveryWithCompletion:]_block_invoke_2 : 232 -> 220
~ -[WLSourceDevicesController attemptDirectConnectionToAddress:] : 156 -> 160
~ -[WLSourceDevicesControllerSurrogate startWiFiAndDeviceDiscoveryWithCompletion:] : 196 -> 192
~ ___80-[WLSourceDevicesControllerSurrogate startWiFiAndDeviceDiscoveryWithCompletion:]_block_invoke : 244 -> 276
~ ___70-[WLSourceDevicesControllerSurrogate scheduleSurrogateDeviceDiscovery]_block_invoke : 144 -> 148
~ -[WLSourceDevicesControllerSurrogate stopDeviceDiscoveryWithCompletion:] : 196 -> 192
~ -[WLSourceDevicesControllerSurrogate stopWiFiAndDeviceDiscoveryWithCompletion:] : 196 -> 192
~ -[NSDictionary(_BOOL) wl_boolForKey:] : 96 -> 100
~ -[NSDictionary(Float) wl_floatForKey:] : 128 -> 132
~ +[NSString(UUID) wl_uniqueIdentifier] : 84 -> 92
~ -[NSString(UUID) wl_stringByAppendingRelativePath:] : 164 -> 180
~ _WLLocalizedString : 116 -> 120
~ ___WLLocalizedString_block_invoke : 92 -> 96

```
