## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-950.0.1.0.2
-  __TEXT.__text: 0xaeb48
+950.0.18.0.0
+  __TEXT.__text: 0xaecb4
   __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_methlist: 0xab2c
+  __TEXT.__objc_methlist: 0xab6c
   __TEXT.__const: 0x318
-  __TEXT.__cstring: 0x206fd
+  __TEXT.__cstring: 0x208e6
   __TEXT.__gcc_except_tab: 0x1014
   __TEXT.__oslogstring: 0xd81
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x3158
-  __TEXT.__objc_classname: 0xeed
-  __TEXT.__objc_methname: 0x1898c
+  __TEXT.__unwind_info: 0x3160
+  __TEXT.__objc_classname: 0xeec
+  __TEXT.__objc_methname: 0x18a9f
   __TEXT.__objc_methtype: 0x344d
-  __TEXT.__objc_stubs: 0x14060
-  __DATA_CONST.__got: 0xd70
-  __DATA_CONST.__const: 0x2900
+  __TEXT.__objc_stubs: 0x140c0
+  __DATA_CONST.__got: 0xd90
+  __DATA_CONST.__const: 0x28d8
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b70
+  __DATA_CONST.__objc_selrefs: 0x5ba0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x760
   __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x128a0
-  __AUTH_CONST.__objc_const: 0x15698
+  __AUTH_CONST.__cfstring: 0x12980
+  __AUTH_CONST.__objc_const: 0x156e8
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0xfc8
-  __DATA.__objc_ivar: 0x944
+  __DATA.__objc_ivar: 0x948
   __DATA.__data: 0xe98
   __DATA.__bss: 0xe8
   __DATA_DIRTY.__objc_data: 0x1658

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0A647743-89DB-360A-9769-F896185EA532
-  Functions: 4448
-  Symbols:   14762
-  CStrings:  10009
+  UUID: D552A3A4-55B6-320D-97B5-AF1D6E0AA951
+  Functions: 4453
+  Symbols:   14779
+  CStrings:  10033
 
Symbols:
+ -[SUDownloader isReadyForDownload:ignoreExistingDownload:error:]
+ -[SUManagerCore reportStartedFromPersistedState]
+ -[SUManagerCore setReportStartedFromPersistedState:]
+ -[SUManagerCore(Analytics) _describeAndReportEvent:policy:primaryDescriptor:alternateDescriptor:additionalMetrics:]
+ -[SUManagerCore(Analytics) _reportOTAEvent:withStatus:policy:descriptor:additionalMetrics:error:]
+ -[SUManagerCore(Analytics) _reportOTAEvent:withStatus:policy:primaryDescriptor:alternateDescriptor:additionalMetrics:error:]
+ -[SUManagerCore(Analytics) _reportRollbackEvent:withInfo:buildVersion:]
+ -[SUManagerCore(Analytics) donateSUErrorToBiome:]
+ -[SUManagerCore(Analytics) donateSuccessToBiomeFor:]
+ -[SUManagerCore(Analytics) eventRecordingServiceURL:]
+ -[SUManagerCore(Analytics) reportOTAAbandonedEventWithError:]
+ -[SUManagerCore(Analytics) reportOTAAbandonedEventWithError:additionalMetrics:]
+ -[SUManagerCore(Analytics) reportOTAAbandonedEvent]
+ -[SUManagerCore(Analytics) reportOTAAutoTriggeredEvent]
+ -[SUManagerCore(Analytics) reportOTAAvailableEvent:]
+ -[SUManagerCore(Analytics) reportOTADownloadedEvent:]
+ -[SUManagerCore(Analytics) reportOTAInstalledEvent]
+ -[SUManagerCore(Analytics) reportOTAStartedDownloadingEvent:]
+ -[SUManagerCore(Analytics) reportOTASucceededEvent]
+ -[SUManagerCore(Analytics) reportPostponedEvent:withStatus:]
+ -[SUManagerCore(Analytics) reportPostponedEvent:withStatus:withAdditionalMetrics:]
+ -[SUManagerCore(Analytics) reportRSRRollbackSuggestedEventWithDescriptor:rollbackSuggestionInfo:]
+ -[SUManagerCore(Analytics) reportRSRRollbackSuggestedEventWithRollbackDescriptor:rollbackSuggestionInfo:]
+ -[SUManagerCore(Analytics) reportSimulatedOTAAutoTriggeredEvent]
+ -[SUManagerCore(Analytics) reporterFlushEvent]
+ -[SUManagerCore(Analytics) rollbackSuggestionReasonFromSUReason:]
+ -[SUManagerCore(Analytics) setRollbackValue:forKey:count:event:]
+ -[SUPreferences inboxUpdaterdInitiatedScan]
+ -[SUScanOptions collectDocumentation]
+ -[SUScanOptions setCollectDocumentation:]
+ -[SUScanOptions(SUS) clientIsInboxUpdaterd]
+ GCC_except_table73
+ GCC_except_table78
+ GCC_except_table86
+ _OBJC_IVAR_$_SUScanOptions._collectDocumentation
+ _SUCorePolicyDDMStatusInstallStateValueKeyDownloading
+ _SUCorePolicyDDMStatusInstallStateValueKeyInstalling
+ _SUCorePolicyDDMStatusInstallStateValueKeyNone
+ _SUCorePolicyDDMStatusInstallStateValueKeyPrepared
+ ___49-[SUManagerCore(Analytics) donateSUErrorToBiome:]_block_invoke
+ ___52-[SUManagerCore(Analytics) donateSuccessToBiomeFor:]_block_invoke
+ ___86-[SUManagerCore updatesDownloadableWithOptions:alternateDownloadOptions:replyHandler:]_block_invoke.490
+ ___block_descriptor_72_e8_32s40s48s56s64s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.393
+ ___block_literal_global.401
+ ___block_literal_global.429
+ ___block_literal_global.460
+ ___block_literal_global.507
+ ___block_literal_global.532
+ ___block_literal_global.537
+ ___block_literal_global.564
+ ___block_literal_global.611
+ _kSUCoreDDMSoftwareUpdateStatusDidChangeNotificationValueTargetLocalDateTime
+ _objc_msgSend$clientIsInboxUpdaterd
+ _objc_msgSend$collectDocumentation
+ _objc_msgSend$inboxUpdaterdInitiatedScan
+ _objc_msgSend$isReadyForDownload:ignoreExistingDownload:error:
+ _objc_msgSend$reportStartedFromPersistedState
+ _objc_msgSend$setCollectDocumentation:
- -[SUDownloader isReadyForDownload:error:]
- -[SUManagerCore _describeAndReportEvent:policy:primaryDescriptor:alternateDescriptor:additionalMetrics:]
- -[SUManagerCore _reportOTAEvent:withStatus:policy:descriptor:additionalMetrics:error:]
- -[SUManagerCore _reportOTAEvent:withStatus:policy:primaryDescriptor:alternateDescriptor:additionalMetrics:error:]
- -[SUManagerCore _reportRollbackEvent:withInfo:buildVersion:]
- -[SUManagerCore donateSUErrorToBiome:]
- -[SUManagerCore donateSuccessToBiomeFor:]
- -[SUManagerCore eventRecordingServiceURL:]
- -[SUManagerCore reportOTAAbandonedEventWithError:]
- -[SUManagerCore reportOTAAbandonedEventWithError:additionalMetrics:]
- -[SUManagerCore reportOTAAbandonedEvent]
- -[SUManagerCore reportOTAAutoTriggeredEvent]
- -[SUManagerCore reportOTAAvailableEvent:]
- -[SUManagerCore reportOTADownloadedEvent:]
- -[SUManagerCore reportOTAInstalledEvent]
- -[SUManagerCore reportOTAStartedDownloadingEvent:]
- -[SUManagerCore reportOTASucceededEvent]
- -[SUManagerCore reportPostponedEvent:withStatus:]
- -[SUManagerCore reportPostponedEvent:withStatus:withAdditionalMetrics:]
- -[SUManagerCore reportRSRRollbackSuggestedEventWithDescriptor:rollbackSuggestionInfo:]
- -[SUManagerCore reportRSRRollbackSuggestedEventWithRollbackDescriptor:rollbackSuggestionInfo:]
- -[SUManagerCore reportSimulatedOTAAutoTriggeredEvent]
- -[SUManagerCore reporterFlushEvent]
- -[SUManagerCore rollbackSuggestionReasonFromSUReason:]
- -[SUManagerCore setRollbackValue:forKey:count:event:]
- GCC_except_table72
- _SUCorePolicyDDMStatusKeyTargetLocalDateTime
- ___38-[SUManagerCore donateSUErrorToBiome:]_block_invoke
- ___41-[SUManagerCore donateSuccessToBiomeFor:]_block_invoke
- ___52-[SUDownloader startDownloadWithOptions:withResult:]_block_invoke_10
- ___86-[SUManagerCore updatesDownloadableWithOptions:alternateDownloadOptions:replyHandler:]_block_invoke.496
- ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s72l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s80l8s64l8s72l8
- ___block_literal_global.405
- ___block_literal_global.413
- ___block_literal_global.419
- ___block_literal_global.441
- ___block_literal_global.472
- ___block_literal_global.519
- ___block_literal_global.544
- ___block_literal_global.549
- ___block_literal_global.558
- ___block_literal_global.654
- _objc_msgSend$isReadyForDownload:error:
- _objc_msgSend$reportCoreAnalyticsOTAStartedDownloadingEvent:
- _objc_msgSend$reportOTAStartedDownloadingEvent:
CStrings:
+ "\n            ClientName: %@\n            Identifier: %@\n            Forced: %@\n            ScanType: %d\n            CollectDoc: %@\n            Types: %@\n            Requested PMV: %@\n            Requested Build: %@\n            SessionID: %@\n            MDM use delay: %@\n            MDM show RSR: %@\n            =============== MDM: %@ \n            ===================\n            Ignore NoUpdateFound response: %@\n"
+ "%s: Overriding result to YES by SUInboxUpdaterdInitiatedScan"
+ "%s: client is inboxupdaterd; disable splombo and psus for this scan"
+ "-[SUManagerCore(Analytics) reportPostponedEvent:withStatus:withAdditionalMetrics:]"
+ "-[SUScanOptions(SUS) clientIsInboxUpdaterd]"
+ "Active download policy class: %@"
+ "SUCollectDocumentation"
+ "SUInboxUpdaterdInitiatedScan"
+ "Skip loading documentation (directed by options)"
+ "TB,N,V_collectDocumentation"
+ "TB,N,V_reportStartedFromPersistedState"
+ "[SUState] removed the testing state file: %d (%@)"
+ "[makeRoom] result = %d, error = %@"
+ "_collectDocumentation"
+ "clientIsInboxUpdaterd"
+ "collectDocumentation"
+ "com.apple.inboxupdaterd"
+ "if set to true, scans will be initiated with inboxupdaterd"
+ "inboxUpdaterdInitiatedScan"
+ "isReadyForDownload:ignoreExistingDownload:error:"
+ "received profile change notification"
+ "reportStartedFromPersistedState"
+ "setCollectDocumentation:"
+ "setReportStartedFromPersistedState:"
- "\n            ClientName: %@\n            Identifier: %@\n            Forced: %@\n            ScanType: %d\n            Types: %@\n            Requested PMV: %@\n            Requested Build: %@\n            SessionID: %@\n            MDM use delay: %@\n            MDM show RSR: %@\n            =============== MDM: %@ \n            ===================\n            Ignore NoUpdateFound response: %@\n"
- "-[SUManagerCore reportPostponedEvent:withStatus:withAdditionalMetrics:]"
- "isReadyForDownload:error:"
- "none"
- "prepared"
- "recived profile change notification"

```
