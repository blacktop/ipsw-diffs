## WelcomeKit

> `/System/Library/PrivateFrameworks/WelcomeKit.framework/WelcomeKit`

```diff

-1224.122.6.0.0
-  __TEXT.__text: 0x7be4
-  __TEXT.__auth_stubs: 0x440
+1410.0.0.0.0
+  __TEXT.__text: 0x73fc
   __TEXT.__objc_methlist: 0x1044
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x11c8
+  __TEXT.__cstring: 0x11dc
   __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__unwind_info: 0x380
-  __TEXT.__objc_classname: 0x1ef
-  __TEXT.__objc_methname: 0x26bd
-  __TEXT.__objc_methtype: 0x721
-  __TEXT.__objc_stubs: 0x12a0
-  __DATA_CONST.__got: 0x108
+  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x398
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x108
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0x15a0
   __AUTH_CONST.__objc_const: 0x2010
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x5f0
   __DATA.__objc_ivar: 0x178
   __DATA.__data: 0x240

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 15E9E4CB-40D7-3551-A0EA-EC467ECDB70F
+  UUID: 0B941D72-224B-3CCF-9CDB-93F27AF39045
   Functions: 330
-  Symbols:   1228
-  CStrings:  948
+  Symbols:   1230
+  CStrings:  356
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x2
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x6
+ _objc_retain_x8
- _objc_release_x10
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
- _objc_retain_x28
Functions:
~ -[WLDeviceAuthentication initWithCoder:] : 116 -> 112
~ -[WLPayload dictionary] : 1188 -> 1124
~ -[WLPayload setMessages:] : 64 -> 12
~ -[WLPayload setPhotos:] : 64 -> 12
~ -[WLPayload setVideos:] : 64 -> 12
~ -[WLPayload setContacts:] : 64 -> 12
~ -[WLPayload setCalendars:] : 64 -> 12
~ -[WLPayload setBookmarks:] : 64 -> 12
~ -[WLPayload setAccounts:] : 64 -> 12
~ -[WLPayload setFiles:] : 64 -> 12
~ -[WLPayload setAccessibilitySettings:] : 64 -> 12
~ -[WLPayload setDisplaySettings:] : 64 -> 12
~ +[WLTelemetry sharedInstance] : 84 -> 68
~ -[WLTelemetry send:payload:] : 196 -> 204
~ ___28-[WLTelemetry send:payload:]_block_invoke : 56 -> 8
~ -[WLTelemetry wifiDidFail] : 156 -> 152
~ -[WLTelemetry deviceDidFailWithTimeout] : 156 -> 152
~ -[WLTelemetry deviceDidFailWithAuthenticationError] : 156 -> 152
~ -[WLTelemetry migratorDidFinish:] : 148 -> 144
~ -[WLTelemetry _telemetryDictionaryForPreparatoryDataDidComplete:contentType:duration:android:model:version:] : 368 -> 376
~ -[WLTelemetry preparatoryDataDidComplete:contentType:duration:android:model:version:] : 364 -> 396
~ -[WLTelemetry _telemetryDictionaryForContentTypeDidComplete:downloadByteCount:importRecordCount:importFailedRecordCount:downloadDuration:importDuration:android:model:version:] : 544 -> 536
~ -[WLTelemetry contentTypeDidComplete:downloadByteCount:importRecordCount:importFailedRecordCount:downloadDuration:importDuration:android:model:version:] : 324 -> 352
~ -[WLTelemetry importDidFailSilentlyForContentType:] : 180 -> 184
~ ___51-[WLTelemetry importDidFailSilentlyForContentType:]_block_invoke : 136 -> 132
~ -[WLTelemetry didResolveTimeEstimate:forDownloadTask:threshold:actualTime:] : 216 -> 220
~ ___75-[WLTelemetry didResolveTimeEstimate:forDownloadTask:threshold:actualTime:]_block_invoke : 264 -> 252
~ ___52-[WLTelemetry userDidChooseToInstallMigratableApps:]_block_invoke : 188 -> 180
~ ___59-[WLTelemetry didLookupAppsWithMatchedApps:mismatchedApps:]_block_invoke : 236 -> 224
~ ___48-[WLTelemetry photoLibraryDidFailWithExtension:]_block_invoke : 136 -> 132
~ ___29-[WLTelemetry didLoadQRCode:]_block_invoke : 188 -> 180
~ ___64-[WLTelemetry didLoadAndroidStore:selected:canceled:inAttempts:]_block_invoke : 296 -> 280
~ -[WLContext initWithCoder:] : 1084 -> 1016
~ -[WLContext encodeWithCoder:] : 436 -> 428
~ -[WLContext isEnabled] : 388 -> 384
~ -[WLContext setApplication:] : 64 -> 12
~ -[WLContext setAccount:] : 64 -> 12
~ -[WLContext setMessage:] : 64 -> 12
~ -[WLContext setContact:] : 64 -> 12
~ -[WLContext setCallHistory:] : 64 -> 12
~ -[WLContext setCalendar:] : 64 -> 12
~ -[WLContext setBookmark:] : 64 -> 12
~ -[WLContext setFile:] : 64 -> 12
~ -[WLContext setImage:] : 64 -> 12
~ -[WLContext setVideo:] : 64 -> 12
~ -[WLContext setVoiceMemo:] : 64 -> 12
~ -[WLContext setAlbum:] : 64 -> 12
~ -[WLContext setContainer:] : 64 -> 12
~ -[WLContext setAccessibilitySetting:] : 64 -> 12
~ -[WLContext setDisplaySetting:] : 64 -> 12
~ -[WLContext setPlaceholder:] : 64 -> 12
~ -[WLContext setSim:] : 64 -> 12
~ -[WLDaemonConnection daemonWithErrorHandler:] : 116 -> 108
~ -[WLDaemonConnection invalidateDaemonConnection] : 68 -> 64
~ +[WLDaemonController sharedInstance] : 84 -> 68
~ ___58-[WLDaemonController getLocalImportOptionsWithCompletion:]_block_invoke : 276 -> 268
~ ___58-[WLDaemonController getLocalImportOptionsWithCompletion:]_block_invoke_2 : 160 -> 156
~ -[WLDaemonController importLocalContent] : 164 -> 156
~ -[WLDaemonController setStashDataLocally:] : 180 -> 172
~ -[WLDaemonController setConnection:] : 64 -> 12
~ _WLDaemonExportedInterface : 284 -> 268
~ _WLDataMigrationDelegateInterface : 1044 -> 976
~ -[WLImportContext initWithCoder:] : 260 -> 248
~ -[WLImportContext encodeWithCoder:] : 240 -> 228
~ +[WLLogController sharedLogger] : 84 -> 68
~ __loggingUserDefaultsChangedNotificationHandler : 88 -> 84
~ _WLLoggingEnabled : 68 -> 64
~ __WLLog : 124 -> 120
~ -[WLDataMigrationController startMigrationUsingRetryPolicies:] : 300 -> 296
~ ___62-[WLDataMigrationController startMigrationUsingRetryPolicies:]_block_invoke_2 : 244 -> 240
~ -[WLDataMigrationController deleteMessages] : 136 -> 132
~ -[WLDataMigrationController lookupAppDataContainer:] : 160 -> 156
~ -[WLDataMigrationController testAMSPurchase] : 136 -> 132
~ -[WLDataMigrationControllerSurrogate initWithDelegate:forceDownloadError:] : 84 -> 88
~ -[WLDataMigrationControllerSurrogate startMigrationUsingRetryPolicies:] : 200 -> 196
~ -[WLDataMigrationControllerSurrogate _startMigrationUsingRetryPolicies:] : 896 -> 856
~ -[WLMigrationKitController run:] : 280 -> 276
~ -[WLMigrationKitController cancel] : 76 -> 72
~ -[WLSourceDevice initWithCoder:] : 1004 -> 940
~ -[WLSourceDevice encodeWithCoder:] : 556 -> 548
~ __didDiscoverCandidate : 256 -> 252
~ __sourceDevicesDidChange : 256 -> 252
~ ___71-[WLSourceDevicesController startWiFiAndDeviceDiscoveryWithCompletion:]_block_invoke_2 : 220 -> 232
~ -[WLSourceDevicesController attemptDirectConnectionToAddress:] : 160 -> 156
~ -[WLSourceDevicesControllerSurrogate initWithDelegate:] : 112 -> 116
~ -[WLSourceDevicesControllerSurrogate startWiFiAndDeviceDiscoveryWithCompletion:] : 192 -> 200
~ ___80-[WLSourceDevicesControllerSurrogate startWiFiAndDeviceDiscoveryWithCompletion:]_block_invoke : 276 -> 248
~ -[WLSourceDevicesControllerSurrogate scheduleSurrogateDeviceDiscovery] : 148 -> 152
~ -[WLSourceDevicesControllerSurrogate stopDeviceDiscoveryWithCompletion:] : 192 -> 200
~ ___72-[WLSourceDevicesControllerSurrogate stopDeviceDiscoveryWithCompletion:]_block_invoke : 128 -> 136
~ -[WLSourceDevicesControllerSurrogate stopWiFiAndDeviceDiscoveryWithCompletion:] : 192 -> 200
~ ___79-[WLSourceDevicesControllerSurrogate stopWiFiAndDeviceDiscoveryWithCompletion:]_block_invoke : 124 -> 132
~ -[NSDictionary(_BOOL) wl_boolForKey:] : 100 -> 96
~ -[NSDictionary(Float) wl_floatForKey:] : 132 -> 128
~ +[NSString(UUID) wl_uniqueIdentifier] : 92 -> 84
~ -[NSString(UUID) wl_stringByAppendingRelativePath:] : 180 -> 164
~ _WLLocalizedString : 120 -> 116
~ ___WLLocalizedString_block_invoke : 96 -> 92
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<WLDataMigrationDelegate>\""
- "@\"<WLDataMigratorProtocol>\""
- "@\"<WLSourceDevicesDelegate>\""
- "@\"NSLock\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"WLDaemonConnection\""
- "@\"WLFeaturePayload\""
- "@\"WLImportContext\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@64@0:8@16@24d32@40@48@56"
- "@88@0:8@16Q24Q32Q40Q48Q56@64@72@80"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "Float"
- "JSONObjectWithData:options:error:"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "S"
- "S16@0:8"
- "T#,R"
- "T@\"<WLDataMigrationDelegate>\",R,W,N,V_delegate"
- "T@\"<WLDataMigrationDelegate>\",W,N,V_delegate"
- "T@\"<WLSourceDevicesDelegate>\",W,N,V_delegate"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_androidAPILevel"
- "T@\"NSString\",C,N,V_androidBrand"
- "T@\"NSString\",C,N,V_androidLocale"
- "T@\"NSString\",C,N,V_androidModel"
- "T@\"NSString\",C,N,V_androidOSVersion"
- "T@\"NSString\",C,N,V_androidVersion"
- "T@\"NSString\",C,N,V_androidVersionCode"
- "T@\"NSString\",C,N,V_api"
- "T@\"NSString\",C,N,V_apiLevel"
- "T@\"NSString\",C,N,V_brand"
- "T@\"NSString\",C,N,V_clientVersion"
- "T@\"NSString\",C,N,V_hardwareBrand"
- "T@\"NSString\",C,N,V_hardwareDesign"
- "T@\"NSString\",C,N,V_hardwareMaker"
- "T@\"NSString\",C,N,V_hardwareModel"
- "T@\"NSString\",C,N,V_hardwareProduct"
- "T@\"NSString\",C,N,V_ipAddress"
- "T@\"NSString\",C,N,V_locale"
- "T@\"NSString\",C,N,V_model"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_osAPIVersion"
- "T@\"NSString\",C,N,V_osVersion"
- "T@\"NSString\",C,N,V_persistentIdentifier"
- "T@\"NSString\",C,N,V_state"
- "T@\"NSString\",C,N,V_version"
- "T@\"NSString\",C,N,V_versionCode"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_sessionUUID"
- "T@\"WLDaemonConnection\",&,N,V_connection"
- "T@\"WLFeaturePayload\",&,N,V_accessibilitySettings"
- "T@\"WLFeaturePayload\",&,N,V_accounts"
- "T@\"WLFeaturePayload\",&,N,V_bookmarks"
- "T@\"WLFeaturePayload\",&,N,V_calendars"
- "T@\"WLFeaturePayload\",&,N,V_contacts"
- "T@\"WLFeaturePayload\",&,N,V_displaySettings"
- "T@\"WLFeaturePayload\",&,N,V_files"
- "T@\"WLFeaturePayload\",&,N,V_messages"
- "T@\"WLFeaturePayload\",&,N,V_photos"
- "T@\"WLFeaturePayload\",&,N,V_videos"
- "T@\"WLFeaturePayload\",R,N,V_callHistory"
- "T@\"WLFeaturePayload\",R,N,V_voiceMemos"
- "T@\"WLImportContext\",&,N,V_accessibilitySetting"
- "T@\"WLImportContext\",&,N,V_account"
- "T@\"WLImportContext\",&,N,V_album"
- "T@\"WLImportContext\",&,N,V_application"
- "T@\"WLImportContext\",&,N,V_bookmark"
- "T@\"WLImportContext\",&,N,V_calendar"
- "T@\"WLImportContext\",&,N,V_callHistory"
- "T@\"WLImportContext\",&,N,V_contact"
- "T@\"WLImportContext\",&,N,V_container"
- "T@\"WLImportContext\",&,N,V_displaySetting"
- "T@\"WLImportContext\",&,N,V_file"
- "T@\"WLImportContext\",&,N,V_image"
- "T@\"WLImportContext\",&,N,V_message"
- "T@\"WLImportContext\",&,N,V_placeholder"
- "T@\"WLImportContext\",&,N,V_sim"
- "T@\"WLImportContext\",&,N,V_video"
- "T@\"WLImportContext\",&,N,V_voiceMemo"
- "T@?,C,N,V_interruptionHandler"
- "TB,N,V_canAddAccessibility"
- "TB,N,V_canAddDisplay"
- "TB,N,V_canAddFiles"
- "TB,N,V_enableAccessibilityDisplayInversion"
- "TB,N,V_enableDisplayDarkMode"
- "TB,N,V_enableDisplayZoom"
- "TB,N,V_enabled"
- "TB,N,V_isEnabled"
- "TB,N,V_isLocal"
- "TB,N,V_isSelectingDataTypeInHandshake"
- "TB,N,V_supportsFileLength"
- "TB,N,V_useMigrationKit"
- "TB,R"
- "TQ,N,V_count"
- "TQ,N,V_data"
- "TQ,N,V_dataSize"
- "TQ,N,V_elapsedTime"
- "TQ,N,V_importCount"
- "TQ,N,V_importErrorCount"
- "TQ,N,V_size"
- "TQ,R"
- "TS,N,V_httpPort"
- "TS,N,V_socketPort"
- "Td,N,V_accessibilityFontScale"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "WLContext"
- "WLDaemonConnection"
- "WLDaemonController"
- "WLDaemonProtocol"
- "WLDataMigrationController"
- "WLDataMigrationControllerSurrogate"
- "WLDataMigrationDelegate"
- "WLDataMigratorProtocol"
- "WLDeviceAuthentication"
- "WLFeaturePayload"
- "WLImportContext"
- "WLInternal"
- "WLInternalSettings"
- "WLLogController"
- "WLMigrationKitController"
- "WLPayload"
- "WLPreferences"
- "WLSourceDevice"
- "WLSourceDevicesController"
- "WLSourceDevicesControllerSurrogate"
- "WLTelemetry"
- "WLUtilities"
- "^{_NSZone=}16@0:8"
- "_BOOL"
- "_accessibilityFontScale"
- "_accessibilitySetting"
- "_accessibilitySettings"
- "_account"
- "_accounts"
- "_album"
- "_androidAPILevel"
- "_androidBrand"
- "_androidLocale"
- "_androidModel"
- "_androidOSVersion"
- "_androidVersion"
- "_androidVersionCode"
- "_api"
- "_application"
- "_bookmark"
- "_bookmarks"
- "_calendar"
- "_calendars"
- "_callHistory"
- "_canAddFiles"
- "_connection"
- "_contact"
- "_contacts"
- "_container"
- "_count"
- "_daemonConn"
- "_daemonLock"
- "_data"
- "_dataSize"
- "_delegate"
- "_deviceDiscoverySession"
- "_displaySetting"
- "_displaySettings"
- "_elapsedTime"
- "_enableAccessibilityDisplayInversion"
- "_enableDisplayDarkMode"
- "_enableDisplayZoom"
- "_enabled"
- "_file"
- "_files"
- "_forceDownloadError"
- "_hardwareProduct"
- "_image"
- "_importCount"
- "_importErrorCount"
- "_interruptionHandler"
- "_isEnabled"
- "_loggingEnabled"
- "_message"
- "_messages"
- "_migrator"
- "_photos"
- "_placeholder"
- "_reloadLogPreferences"
- "_serialQueue"
- "_sim"
- "_size"
- "_startMigrationUsingRetryPolicies:"
- "_state"
- "_telemetryDictionaryForContentTypeDidComplete:downloadByteCount:importRecordCount:importFailedRecordCount:downloadDuration:importDuration:android:model:version:"
- "_telemetryDictionaryForPreparatoryDataDidComplete:contentType:duration:android:model:version:"
- "_video"
- "_videos"
- "_voiceMemo"
- "_voiceMemos"
- "_wifiStarted"
- "accessibilityFontScale"
- "accessibilitySetting"
- "accessibilitySettings"
- "androidAPILevel"
- "androidBrand"
- "androidLocale"
- "androidModel"
- "androidVersion"
- "androidVersionCode"
- "api"
- "apiLevel"
- "arrayByAddingObjectsFromArray:"
- "arrayWithObjects:count:"
- "attemptDirectConnectionToAddress:"
- "autorelease"
- "boolForKey:"
- "boolValue"
- "brand"
- "bundleForClass:"
- "c24@0:8@16"
- "callHistory"
- "canAddAccessibility"
- "canAddDisplay"
- "canAddFiles"
- "cancel"
- "class"
- "clientVersion"
- "conformsToProtocol:"
- "connection"
- "contentTypeDidComplete:downloadByteCount:importRecordCount:importFailedRecordCount:downloadDuration:importDuration:android:model:version:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "d24@0:8@16"
- "daemon:didChangeState:withContext:"
- "daemon:didCreateCode:"
- "daemon:didImportWithContext:"
- "daemon:didReceiveClient:brand:model:name:"
- "daemon:didUpdateProgress:remainingTime:completedOperationCount:totalOperationCount:"
- "daemonConnection"
- "daemonDidAuthenticateClient:"
- "daemonDidGetInterrupted"
- "daemonDidRejectClient:"
- "daemonWillImport:"
- "daemonWithErrorHandler:"
- "dataMigrator:didFailWithError:"
- "dataMigrator:didUpdateMigrationState:"
- "dataMigrator:didUpdateProgressPercentage:"
- "dataMigrator:didUpdateRemainingDownloadTime:"
- "dataMigratorDidBecomeRestartable:"
- "dataMigratorDidFinish:withImportErrors:context:"
- "dataMigratorDidGetInterrupted"
- "dataSize"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "delegate"
- "deleteMessages"
- "description"
- "deviceDidFailWithAuthenticationError"
- "deviceDidFailWithTimeout"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "didLoadAndroidStore:selected:canceled:inAttempts:"
- "didLoadQRCode:"
- "didLookupAppsWithMatchedApps:mismatchedApps:"
- "didResolveTimeEstimate:forDownloadTask:threshold:actualTime:"
- "displaySetting"
- "displaySettings"
- "elapsedTime"
- "enableAccessibilityDisplayInversion"
- "enableDisplayDarkMode"
- "enableDisplayZoom"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "floatValue"
- "getLocalImportOptions:"
- "getLocalImportOptionsWithCompletion:"
- "hardwareBrand"
- "hardwareDesign"
- "hardwareMaker"
- "hardwareModel"
- "hardwareProduct"
- "hash"
- "httpPort"
- "importCount"
- "importDidFailSilentlyForContentType:"
- "importErrorCount"
- "importLocalContent"
- "init"
- "initWithCoder:"
- "initWithData:encoding:"
- "initWithDelegate:"
- "initWithDelegate:forceDownloadError:"
- "initWithJSONDictionary:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "interruptionHandler"
- "invalidate"
- "invalidateDaemonConnection"
- "ipAddress"
- "isEnabled"
- "isEqual:"
- "isInternal"
- "isKindOfClass:"
- "isLocal"
- "isMemberOfClass:"
- "isProxy"
- "isSelectingDataTypeInHandshake"
- "locale"
- "localizedStringForKey:value:table:"
- "lock"
- "logMessageFromAddress:withLevel:format:args:"
- "lookupAppDataContainer:"
- "migratorDidFinish:"
- "model"
- "name"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "osAPIVersion"
- "osVersion"
- "pathComponents"
- "pathWithComponents:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistentIdentifier"
- "photoLibraryDidFailWithExtension:"
- "preparatoryDataDidComplete:contentType:duration:android:model:version:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeForKey:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "run:"
- "scheduleSurrogateDeviceDiscovery"
- "self"
- "send:payload:"
- "sessionUUID"
- "setAccessibilityFontScale:"
- "setAccessibilitySetting:"
- "setAccessibilitySettings:"
- "setAccount:"
- "setAccounts:"
- "setAlbum:"
- "setAndroidAPILevel:"
- "setAndroidBrand:"
- "setAndroidLocale:"
- "setAndroidModel:"
- "setAndroidOSVersion:"
- "setAndroidVersion:"
- "setAndroidVersionCode:"
- "setApi:"
- "setApiLevel:"
- "setApplication:"
- "setBookmark:"
- "setBookmarks:"
- "setBool:forKey:"
- "setBrand:"
- "setCalendar:"
- "setCalendars:"
- "setCallHistory:"
- "setCanAddAccessibility:"
- "setCanAddDisplay:"
- "setCanAddFiles:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClientVersion:"
- "setConnection:"
- "setContact:"
- "setContacts:"
- "setContainer:"
- "setCount:"
- "setData:"
- "setDataSize:"
- "setDelegate:"
- "setDisplaySetting:"
- "setDisplaySettings:"
- "setElapsedTime:"
- "setEnableAccessibilityDisplayInversion:"
- "setEnableDisplayDarkMode:"
- "setEnableDisplayZoom:"
- "setEnabled:"
- "setFile:"
- "setFiles:"
- "setHardwareBrand:"
- "setHardwareDesign:"
- "setHardwareMaker:"
- "setHardwareModel:"
- "setHardwareProduct:"
- "setHttpPort:"
- "setImage:"
- "setImportCount:"
- "setImportErrorCount:"
- "setInterface:forSelector:argumentIndex:ofReply:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIpAddress:"
- "setIsEnabled:"
- "setIsLocal:"
- "setIsSelectingDataTypeInHandshake:"
- "setLocale:"
- "setMessage:"
- "setMessages:"
- "setModel:"
- "setName:"
- "setObject:forKey:"
- "setOsAPIVersion:"
- "setOsVersion:"
- "setPersistentIdentifier:"
- "setPhotos:"
- "setPlaceholder:"
- "setRemoteObjectInterface:"
- "setSim:"
- "setSize:"
- "setSocketPort:"
- "setStashDataLocally:"
- "setState:"
- "setString:forKey:"
- "setSupportsFileLength:"
- "setUseMigrationKit:"
- "setVersion:"
- "setVersionCode:"
- "setVideo:"
- "setVideos:"
- "setVoiceMemo:"
- "setWithObjects:"
- "settingsWithData:"
- "sharedInstance"
- "sharedLogger"
- "socketPort"
- "sourceDeviceController:didDiscoverCandidate:"
- "sourceDeviceController:didDiscoverDevice:"
- "sourceDeviceWithReply:"
- "startMigrationUsingRetryPolicies:"
- "startMigrationUsingRetryPolicies:delegate:useMigrationKit:replyBlock:"
- "startWiFiAndDeviceDiscovery:"
- "startWiFiAndDeviceDiscoveryWithCompletion:"
- "stopDeviceDiscovery:"
- "stopDeviceDiscoveryWithCompletion:"
- "stopWiFiAndDeviceDiscovery:"
- "stopWiFiAndDeviceDiscoveryWithCompletion:"
- "stringForKey:"
- "stringWithFormat:"
- "superclass"
- "supportsFileLength"
- "supportsSecureCoding"
- "testAMSPurchase"
- "unlock"
- "unsignedLongLongValue"
- "useMigrationKit"
- "userDidChooseToInstallMigratableApps:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8S16"
- "v24@0:8@\"<WLDataMigratorProtocol>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSString\">16"
- "v24@0:8@?<v@?@\"WLSourceDevice\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSString\"@\"NSString\"@\"NSString\"q@\"NSError\">16"
- "v24@0:8@?<v@?BB@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v28@0:8@\"<WLDataMigratorProtocol>\"16f24"
- "v28@0:8@16f24"
- "v28@0:8B16@20"
- "v32@0:8@\"<WLDataMigratorProtocol>\"16@\"NSError\"24"
- "v32@0:8@\"<WLDataMigratorProtocol>\"16@\"NSString\"24"
- "v32@0:8@\"<WLDataMigratorProtocol>\"16@\"WLContext\"24"
- "v32@0:8@\"<WLDataMigratorProtocol>\"16Q24"
- "v32@0:8@\"<WLDataMigratorProtocol>\"16d24"
- "v32@0:8@16@24"
- "v32@0:8@16Q24"
- "v32@0:8@16d24"
- "v32@0:8Q16Q24"
- "v36@0:8@\"<WLDataMigratorProtocol>\"16B24@\"WLContext\"28"
- "v36@0:8@16B24@28"
- "v40@0:8@\"<WLDataMigratorProtocol>\"16q24@\"WLContext\"32"
- "v40@0:8@16B24B28Q32"
- "v40@0:8@16q24@32"
- "v40@0:8B16@\"<WLDataMigrationDelegate>\"20B28@?<v@?@\"<WLDataMigratorProtocol>\"@\"NSError\">32"
- "v40@0:8B16@20B28@?32"
- "v48@0:8Q16@24Q32Q40"
- "v48@0:8^v16Q24@32*40"
- "v52@0:8@\"<WLDataMigratorProtocol>\"16f24Q28Q36Q44"
- "v52@0:8@16f24Q28Q36Q44"
- "v56@0:8@\"<WLDataMigratorProtocol>\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48"
- "v56@0:8@16@24@32@40@48"
- "v64@0:8@16@24d32@40@48@56"
- "v88@0:8@16Q24Q32Q40Q48Q56@64@72@80"
- "version"
- "versionCode"
- "voiceMemo"
- "voiceMemos"
- "wifiAndDeviceDiscoveryDidGetInterrupted"
- "wifiDidFail"
- "wl_boolForKey:"
- "wl_floatForKey:"
- "wl_stringByAppendingRelativePath:"
- "wl_uniqueIdentifier"
- "zone"

```
