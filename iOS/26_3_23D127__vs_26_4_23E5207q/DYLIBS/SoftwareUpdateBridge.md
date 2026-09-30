## SoftwareUpdateBridge

> `/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/SoftwareUpdateBridge`

```diff

-367.40.5.0.0
-  __TEXT.__text: 0x72dc
-  __TEXT.__auth_stubs: 0x630
+367.100.6.0.0
+  __TEXT.__text: 0x7ba8
+  __TEXT.__auth_stubs: 0x610
   __TEXT.__objc_methlist: 0x858
   __TEXT.__const: 0xd8
-  __TEXT.__gcc_except_tab: 0x54
+  __TEXT.__gcc_except_tab: 0x60
   __TEXT.__cstring: 0x1168
   __TEXT.__oslogstring: 0xbe5
-  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__unwind_info: 0x2c0
   __TEXT.__objc_classname: 0x69
   __TEXT.__objc_methname: 0x1dff
   __TEXT.__objc_methtype: 0x20f

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x6e0
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__auth_got: 0x318
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0xec0
   __AUTH_CONST.__objc_const: 0xf98

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FDFDA9D1-5144-3514-9482-525F6267B811
+  UUID: 1A9E5EFE-3B88-359F-AF79-27D13D65E317
   Functions: 215
-  Symbols:   928
+  Symbols:   926
   CStrings:  733
 
Symbols:
+ _objc_release_x27
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_release_x26
- _objc_release_x28
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[SUBManager initWithDelegate:] : 180 -> 184
~ -[SUBManager setDelegate:] : 152 -> 160
~ -[SUBManager delegate] : 240 -> 236
~ -[SUBManager _serverConnection] : 240 -> 236
~ ___31-[SUBManager _serverConnection]_block_invoke : 468 -> 480
~ -[SUBManager _forwardScanResult:] : 248 -> 260
~ -[SUBManager _forwardDownloadProgress:] : 564 -> 600
~ -[SUBManager _forwardInstallResult:] : 296 -> 308
~ -[SUBManager _forwardInstallationCanProceed:] : 272 -> 280
~ -[SUBManager _forwardInstallationWillProceed:] : 236 -> 244
~ -[SUBManager _forwardUserDidAcceptTermsAndConditionsChanged:] : 100 -> 104
~ -[SUBManager _forwardUserInstallRequestTypeChanged:] : 184 -> 192
~ -[SUBManager _forwardInstallationAwaitingUserInteraction:] : 388 -> 396
~ ___27-[SUBManager managerState:]_block_invoke : 528 -> 544
~ -[SUBManager scanForUpdates] : 136 -> 140
~ -[SUBManager startDownload:] : 172 -> 176
~ -[SUBManager installUpdate:] : 172 -> 176
~ -[SUBManager userDidAcceptTermsAndConditionsForUpdate:] : 184 -> 188
~ ___34-[SUBManager getCloudDescriptors:]_block_invoke : 264 -> 280
~ -[SUBManager removeCloudDescriptor:] : 172 -> 176
~ -[SUBManager userDidAcceptTermsAndConditionsForUpdate:completion:] : 228 -> 224
~ ___66-[SUBManager userDidAcceptTermsAndConditionsForUpdate:completion:]_block_invoke : 364 -> 368
~ ___66-[SUBManager userDidAcceptTermsAndConditionsForUpdate:completion:]_block_invoke_2 : 432 -> 444
~ -[SUBManager purgeUpdate:completion:] : 280 -> 276
~ ___37-[SUBManager purgeUpdate:completion:]_block_invoke : 156 -> 160
~ -[SUBManager setUserInstallRequestTypeForUpdate:userInstallRequestType:completion:] : 424 -> 408
~ ___83-[SUBManager setUserInstallRequestTypeForUpdate:userInstallRequestType:completion:]_block_invoke : 448 -> 460
~ ___83-[SUBManager setUserInstallRequestTypeForUpdate:userInstallRequestType:completion:]_block_invoke_2 : 648 -> 660
~ -[SUBManager adoptSimulationFileOfName:] : 692 -> 700
~ -[SUBManager performMigration] : 136 -> 140
~ -[SUBManager supportsInstallTonightWithCompletion:] : 368 -> 380
~ ___51-[SUBManager supportsInstallTonightWithCompletion:]_block_invoke : 512 -> 528
~ ___31-[SUBManager sendTermsRequest:]_block_invoke : 432 -> 444
~ -[SUBManager setServerConnection:] : 12 -> 64
~ -[SUBManager setQueue:] : 12 -> 64
~ +[SUBDownload downloadWithDescriptor:andProgress:] : 160 -> 156
~ -[SUBDownload initWithCoder:] : 188 -> 196
~ -[SUBDownload encodeWithCoder:] : 108 -> 116
~ -[SUBDownload copy] : 116 -> 124
~ -[SUBDownload setDescriptor:] : 12 -> 64
~ -[SUBDownload setProgress:] : 12 -> 64
~ _SUBIPCEncodeObject : 272 -> 276
~ _SUBIPCDecodeObjectForKey : 212 -> 220
~ _SUBIPCDecodeObjectsForKey : 408 -> 412
~ _SUBIPCDictionaryToXPC : 216 -> 220
~ ___SUBIPCDictionaryToXPC_block_invoke : 308 -> 304
~ _SUBIPCXPCToDictionary : 220 -> 224
~ ___SUBIPCXPCToDictionary_block_invoke : 300 -> 320
~ -[SUBDocumentation currentPhoneLanguage] : 356 -> 364
~ -[SUBDocumentation preferredPhoneLanguages] : 264 -> 268
~ -[SUBDocumentation initWithDocumentationBundleURL:] : 128 -> 120
~ -[SUBDocumentation initWithMAAsset:] : 344 -> 348
~ -[SUBDocumentation initWithCoder:] : 424 -> 452
~ -[SUBDocumentation encodeWithCoder:] : 208 -> 216
~ -[SUBDocumentation humanReadableUpdateName] : 56 -> 64
~ -[SUBDocumentation releaseNotesSummary] : 200 -> 208
~ -[SUBDocumentation releaseNotes] : 200 -> 208
~ -[SUBDocumentation licenseAgreement] : 200 -> 208
~ -[SUBDocumentation _resourceFromBundle:forKey:] : 312 -> 316
~ -[SUBDocumentation _loadBundleResources] : 1496 -> 1532
~ -[SUBDocumentation isEqual:] : 164 -> 172
~ -[SUBDocumentation summary] : 324 -> 348
~ -[SUBDocumentation setReleaseNotesSummary:] : 12 -> 64
~ -[SUBDocumentation setReleaseNotes:] : 12 -> 64
~ -[SUBDocumentation setLicenseAgreement:] : 12 -> 64
~ -[SUBDocumentation setHumanReadableUpdateName:] : 12 -> 64
~ -[SUBDocumentation setPreferencesIcon:] : 12 -> 64
~ -[SUBDocumentation setDocumentationBundleURL:] : 12 -> 64
~ -[SUBDocumentation setSuCoreParsedDocumentation:] : 12 -> 64
~ -[SUBDocumentation setPhoneLanguage:] : 12 -> 64
~ _SUBError : 76 -> 80
~ _SUBErrorUserInfoV : 304 -> 300
~ _SUBErrorUserInfo : 64 -> 68
~ _SUBActiveNRDevice : 368 -> 376
~ ___SUBIsRunningInStoreDemoMode_block_invoke_2 : 300 -> 304
~ _copySUBSimulationFileName : 68 -> 84
~ -[SUBDescriptor initWithCoder:] : 1032 -> 1088
~ -[SUBDescriptor encodeWithCoder:] : 528 -> 536
~ -[SUBDescriptor copy] : 116 -> 124
~ -[SUBDescriptor stringsMatch:second:] : 112 -> 108
~ -[SUBDescriptor isEqual:] : 760 -> 772
~ -[SUBDescriptor hash] : 92 -> 96
~ -[SUBDescriptor description] : 616 -> 648
~ -[SUBDescriptor compare:] : 184 -> 192
~ -[SUBDescriptor humanReadableUpdateName] : 200 -> 216
~ -[SUBDescriptor setDocumentation:] : 12 -> 64
~ -[SUBDescriptor setProductVersion:] : 12 -> 64
~ -[SUBDescriptor setProductBuildVersion:] : 12 -> 64
~ -[SUBDescriptor setDocumentationID:] : 12 -> 64
~ -[SUBDescriptor setMarketingVersion:] : 12 -> 64
~ -[SUBDescriptor setPublisher:] : 12 -> 64
~ -[SUBDescriptor setProductSystemName:] : 12 -> 64
~ -[SUBDescriptor setDenialReasons:] : 12 -> 64
~ -[SUBDescriptor setDateOfLastSentInstallNotification:] : 12 -> 64
~ -[SUBDescriptor setDateOfLastScheduleOfAutoUpdateNotification:] : 12 -> 64
~ -[SUBDescriptor setDateOfLastScheduleOfAutoUpdate:] : 12 -> 64
~ -[SUBDescriptor setManifest:] : 12 -> 64
~ -[SUBDescriptor setUpdatePowerPolicy:] : 12 -> 64
~ -[SUBDescriptor setCoreDescriptor:] : 12 -> 64
~ -[SUBDescriptor setOsName:] : 12 -> 64
~ -[SUBDescriptor setAutoSUStartTime:] : 12 -> 64
~ -[SUBDescriptor setAutoSUEndTime:] : 12 -> 64
~ -[SUBProgress initWithCoder:] : 256 -> 264
~ -[SUBProgress encodeWithCoder:] : 172 -> 180
~ -[SUBProgress copy] : 116 -> 124
~ -[SUBProgress setPhase:] : 12 -> 64
~ -[SUBProgress setTaskID:] : 12 -> 64
CStrings:
+ "79C6122C-332F-481C-B7DE-7E80973B07BF"
- "79C6122C-6767-4098-9B1E-30DE4D6D0180"

```
