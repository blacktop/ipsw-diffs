## libtzupdate.dylib

> `/usr/lib/libtzupdate.dylib`

```diff

 88.0.0.0.0
-  __TEXT.__text: 0x2f00
+  __TEXT.__text: 0x3124
   __TEXT.__auth_stubs: 0x330
   __TEXT.__objc_methlist: 0x418
   __TEXT.__const: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 945286EF-0AF3-393D-AC9D-B6D39C6A070D
+  UUID: 8C65DD79-E4A1-332A-BB25-1BFD3B9D0373
   Functions: 88
   Symbols:   429
   CStrings:  369
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x22
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x24
- _objc_retain_x8
Functions:
~ +[TZDeviceInfoHelper icuVersion] : 200 -> 204
~ +[TZDeviceInfoHelper zoneinfoVersion] : 168 -> 176
~ +[TZFileSystemInterface sharedInstance] : 68 -> 84
~ -[TZFileSystemInterface systemICUSchemaVersionURL] : 196 -> 212
~ -[TZFileSystemInterface cacheTZLatestDestination] : 100 -> 108
~ -[TZFileSystemInterface systemVersionInfo] : 88 -> 100
~ -[TZFileSystemInterface latestVersionInfo] : 180 -> 192
~ -[TZFileSystemInterface currentVersionInfo] : 448 -> 480
~ -[TZFileSystemInterface lastInstalledVersionInfo] : 156 -> 168
~ -[TZFileSystemInterface systemICUTZSchemaVersion] : 292 -> 316
~ -[TZFileSystemInterface obtainDestinationOfLinkAtURL:] : 312 -> 324
~ +[TZUtilities stringWithContentsOfFileAtURL:error:] : 264 -> 276
~ +[TZUtilities fileExistsAndIsSymbolicLinkAtURL:] : 360 -> 368
~ +[TZVersionInfo versionInfoFromContainerDirectory:] : 532 -> 560
~ +[TZVersionInfo versionInfoFromDefaultSystem] : 232 -> 244
~ -[TZVersionInfo _initWithVersionInfoDictionary:isPartial:] : 388 -> 408
~ -[TZVersionInfo versionString] : 276 -> 308
~ +[TZVersionInfo _verifyVersionInfoDictionary:] : 1708 -> 1756
~ +[TZVersionInfo _tzDataVersionFromZoneinfoDirectory:withError:] : 348 -> 364
~ -[TZVersionInfo compare:] : 116 -> 124
~ -[TZVersionInfo description] : 164 -> 180
~ -[TZVersionInfo isBlank] : 304 -> 336
~ +[TZDLogging canLogMessageAtLevel:] : 80 -> 84
~ +[TZUpdate sharedInstance] : 68 -> 84
~ -[TZUpdate init] : 104 -> 108
~ -[TZUpdate createNewXPCConnection] : 136 -> 140
~ -[TZUpdate isUpdateWaitingWithCompletion:] : 404 -> 400
~ ___42-[TZUpdate isUpdateWaitingWithCompletion:]_block_invoke : 168 -> 172
~ ___42-[TZUpdate isUpdateWaitingWithCompletion:]_block_invoke_2 : 160 -> 164
~ -[TZUpdate purgeAllAssetsWithCompletion:] : 404 -> 400
~ ___41-[TZUpdate purgeAllAssetsWithCompletion:]_block_invoke : 172 -> 176
~ ___41-[TZUpdate purgeAllAssetsWithCompletion:]_block_invoke_2 : 184 -> 188
~ -[TZUpdate affectedZones] : 244 -> 272
~ -[TZUpdate currentTZDataVersion] : 100 -> 112
~ -[TZUpdate alertForAllZones] : 112 -> 124
~ -[TZUpdate updateTZDataVersion] : 124 -> 136
~ -[TZUpdate isUpdateWaiting] : 248 -> 284
~ +[TZPreferencesController sharedPreferencesController] : 160 -> 176
~ -[TZPreferencesController init] : 184 -> 192

```
