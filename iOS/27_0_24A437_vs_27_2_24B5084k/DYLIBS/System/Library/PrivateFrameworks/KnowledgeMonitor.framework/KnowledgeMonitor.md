## KnowledgeMonitor

> `/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor`

```diff

-477.0.1.0.0
-  __TEXT.__text: 0x2d6e0
-  __TEXT.__objc_methlist: 0x3264
-  __TEXT.__const: 0x250
-  __TEXT.__gcc_except_tab: 0x7e4
-  __TEXT.__cstring: 0x3111
-  __TEXT.__oslogstring: 0x28d2
-  __TEXT.__unwind_info: 0xfb8
+480.0.0.0.0
+  __TEXT.__text: 0x2f85c
+  __TEXT.__objc_methlist: 0x3394
+  __TEXT.__const: 0x240
+  __TEXT.__gcc_except_tab: 0x894
+  __TEXT.__cstring: 0x3a10
+  __TEXT.__oslogstring: 0x2c2f
+  __TEXT.__unwind_info: 0x1058
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9e0
-  __DATA_CONST.__objc_classlist: 0x180
+  __DATA_CONST.__const: 0xa80
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24b0
-  __DATA_CONST.__objc_superrefs: 0x158
-  __DATA_CONST.__objc_arraydata: 0x100
-  __DATA_CONST.__got: 0x648
+  __DATA_CONST.__objc_selrefs: 0x2578
+  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_arraydata: 0x328
+  __DATA_CONST.__got: 0x6b0
   __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__cfstring: 0x1fe0
-  __AUTH_CONST.__objc_const: 0x50d0
-  __AUTH_CONST.__objc_arrayobj: 0x1c8
+  __AUTH_CONST.__cfstring: 0x2860
+  __AUTH_CONST.__objc_const: 0x53c0
+  __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x38c
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x3b8
   __DATA.__data: 0x548
   __DATA_DIRTY.__objc_data: 0xf00
   __DATA_DIRTY.__bss: 0xb0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1249
-  Symbols:   3160
-  CStrings:  584
+  Functions: 1293
+  Symbols:   3253
+  CStrings:  663
 
Symbols:
+ -[DKApplicationState rawApplication]
+ -[DKApplicationState setRawApplication:]
+ -[_DKApplicationMonitor updateFocalApplication:rawFocalApplication:timestamp:displayType:transitionReason:transaction:]
+ -[_DKApplicationMonitorBase updateBiomeAppInFocusWithStopEventAtTimestamp:reason:transitionReason:]
+ -[_DKExtensionInfo .cxx_destruct]
+ -[_DKExtensionInfo bundleIdentifier]
+ -[_DKExtensionInfo extensionHostID]
+ -[_DKExtensionInfo initWithBundleIdentifier:parentBundleIdentifier:extensionHostID:]
+ -[_DKExtensionInfo parentBundleIdentifier]
+ -[_DKExtensionInfo setBundleIdentifier:]
+ -[_DKExtensionInfo setExtensionHostID:]
+ -[_DKExtensionInfo setParentBundleIdentifier:]
+ -[_DKExtensionUsageMonitor .cxx_destruct]
+ -[_DKExtensionUsageMonitor addProcess:forIdentity:]
+ -[_DKExtensionUsageMonitor dealloc]
+ -[_DKExtensionUsageMonitor extensionInfoForID:]
+ -[_DKExtensionUsageMonitor init]
+ -[_DKExtensionUsageMonitor processMonitor:didUpdateState:forProcess:]
+ -[_DKExtensionUsageMonitor processUpdateHandlerForEpoch:]
+ -[_DKExtensionUsageMonitor removeProcessForIdentity:]
+ -[_DKExtensionUsageMonitor sendBiomeEvent:type:timestamp:]
+ -[_DKExtensionUsageMonitor setSource:]
+ -[_DKExtensionUsageMonitor source]
+ -[_DKExtensionUsageMonitor start]
+ -[_DKExtensionUsageMonitor stop]
+ -[_DKNowPlayingMonitor saveBMEventWithCurrent:outputDevices:artistStoreIdentifier:albumStoreIdentifier:strictMediaType:contentType:excludeFromSuggestions:]
+ GCC_except_table16
+ GCC_except_table44
+ GCC_except_table51
+ GCC_except_table57
+ GCC_except_table62
+ _MRNowPlayingInfoContentTypeBook
+ _MRNowPlayingInfoContentTypeGeneric
+ _MRNowPlayingInfoContentTypeHomeMedia
+ _MRNowPlayingInfoContentTypeMovie
+ _MRNowPlayingInfoContentTypeMusic
+ _MRNowPlayingInfoContentTypePodcast
+ _MRNowPlayingInfoContentTypeRadio
+ _MRNowPlayingInfoContentTypeTVShow
+ _MRNowPlayingInfoMediaTypeAudio
+ _MRNowPlayingInfoMediaTypeVideo
+ _OBJC_CLASS_$_BMAppExtensionUsage
+ _OBJC_CLASS_$__DKExtensionInfo
+ _OBJC_CLASS_$__DKExtensionUsageMonitor
+ _OBJC_IVAR_$_DKApplicationState._rawApplication
+ _OBJC_IVAR_$__DKExtensionInfo._bundleIdentifier
+ _OBJC_IVAR_$__DKExtensionInfo._extensionHostID
+ _OBJC_IVAR_$__DKExtensionInfo._parentBundleIdentifier
+ _OBJC_IVAR_$__DKExtensionUsageMonitor._activeExtensions
+ _OBJC_IVAR_$__DKExtensionUsageMonitor._epoch
+ _OBJC_IVAR_$__DKExtensionUsageMonitor._everVisibleIdentities
+ _OBJC_IVAR_$__DKExtensionUsageMonitor._nonEligibleExtensionsIdentifiers
+ _OBJC_IVAR_$__DKExtensionUsageMonitor._processMonitor
+ _OBJC_IVAR_$__DKExtensionUsageMonitor._source
+ _OBJC_IVAR_$__DKExtensionUsageMonitor._thirdPartyExtensions
+ _OBJC_METACLASS_$__DKExtensionInfo
+ _OBJC_METACLASS_$__DKExtensionUsageMonitor
+ __OBJC_$_INSTANCE_METHODS__DKExtensionInfo
+ __OBJC_$_INSTANCE_METHODS__DKExtensionUsageMonitor
+ __OBJC_$_INSTANCE_VARIABLES__DKExtensionInfo
+ __OBJC_$_INSTANCE_VARIABLES__DKExtensionUsageMonitor
+ __OBJC_$_PROP_LIST__DKExtensionInfo
+ __OBJC_$_PROP_LIST__DKExtensionUsageMonitor
+ __OBJC_CLASS_RO_$__DKExtensionInfo
+ __OBJC_CLASS_RO_$__DKExtensionUsageMonitor
+ __OBJC_METACLASS_RO_$__DKExtensionInfo
+ __OBJC_METACLASS_RO_$__DKExtensionUsageMonitor
+ ___32-[_DKExtensionUsageMonitor stop]_block_invoke
+ ___33-[_DKExtensionUsageMonitor start]_block_invoke
+ ___33-[_DKExtensionUsageMonitor start]_block_invoke_2
+ ___33-[_DKExtensionUsageMonitor start]_block_invoke_3
+ ___57-[_DKExtensionUsageMonitor processUpdateHandlerForEpoch:]_block_invoke
+ ___57-[_DKExtensionUsageMonitor processUpdateHandlerForEpoch:]_block_invoke_2
+ ___block_descriptor_112_e8_32s40s48s56s64r72r80r88r96r104r_e29_v24?0^{__CFDictionary=}8^v16lr64l8s32l8s40l8r72l8r80l8r88l8r96l8r104l8s48l8s56l8
+ ___block_descriptor_120_e8_32s40s48s56r64r72r80r88r96r104r112r_e5_v8?0lr56l8s32l8r64l8r72l8s40l8r80l8r88l8r96l8r104l8r112l8s48l8
+ ___block_descriptor_40_e8_32s_e35_v24?0"NSString"8"NSDictionary"16ls32l8
+ ___block_descriptor_48_e8_32w_e74_v32?0"RBSProcessMonitor"8"RBSProcessHandle"16"RBSProcessStateUpdate"24lw32l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e40_v16?0"<RBSProcessMonitorConfiguring>"8ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8r48l8s40l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32r40r48r56r64r72r_e42_v16?0"_DKApplicationMonitorGuardedData"8lr32l8r40l8r48l8r56l8r64l8r72l8
+ _kMRMediaRemoteNowPlayingInfoContentType
+ _kMRMediaRemoteNowPlayingInfoStrictMediaType
+ _objc_msgSend$ExtensionUsage
+ _objc_msgSend$addProcess:forIdentity:
+ _objc_msgSend$allValues
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$exitEvent
+ _objc_msgSend$extensionInfoForID:
+ _objc_msgSend$extensionPointRecord
+ _objc_msgSend$iTunesMetadata
+ _objc_msgSend$initWithBundleIdentifier:parentBundleIdentifier:extensionHostID:
+ _objc_msgSend$initWithLaunchReason:type:starting:absoluteTimestamp:bundleID:parentBundleID:extensionHostID:shortVersionString:exactVersionString:dyldPlatform:isNativeArchitecture:displayType:transitionReason:
+ _objc_msgSend$initWithStarting:absoluteTimestamp:bundleID:parentBundleID:extensionHostID:
+ _objc_msgSend$localNonWakingRegistrationWithIdentifier:contextualPredicate:clientIdentifier:callback:
+ _objc_msgSend$parentBundleIdentifier
+ _objc_msgSend$predicateMatchingExtensionPoint:
+ _objc_msgSend$processUpdateHandlerForEpoch:
+ _objc_msgSend$rawApplication
+ _objc_msgSend$removeProcessForIdentity:
+ _objc_msgSend$saveBMEventWithCurrent:outputDevices:artistStoreIdentifier:albumStoreIdentifier:strictMediaType:contentType:excludeFromSuggestions:
+ _objc_msgSend$sendBiomeEvent:type:timestamp:
+ _objc_msgSend$setEndowmentNamespaces:
+ _objc_msgSend$setEvents:
+ _objc_msgSend$setValues:
+ _objc_msgSend$storeItemIdentifier
+ _objc_msgSend$updateBiomeAppInFocusWithStopEventAtTimestamp:reason:transitionReason:
+ _objc_msgSend$updateFocalApplication:rawFocalApplication:timestamp:displayType:transitionReason:transaction:
- -[_DKApplicationMonitor updateFocalApplication:timestamp:displayType:transitionReason:transaction:]
- -[_DKNowPlayingMonitor saveBMEventWithCurrent:outputDevices:artistStoreIdentifier:albumStoreIdentifier:excludeFromSuggestions:]
- GCC_except_table42
- GCC_except_table49
- GCC_except_table55
- GCC_except_table60
- _OBJC_CLASS_$_NSTimer
- ___block_descriptor_104_e8_32s40s48s56r64r72r80r88r96r_e5_v8?0lr56l8s32l8r64l8r72l8s40l8r80l8r88l8r96l8s48l8
- ___block_descriptor_40_e8_32s_e18_B16?0"NSString"8ls32l8
- ___block_descriptor_40_e8_32w_e17_v16?0"NSTimer"8lw32l8
- ___block_descriptor_72_e8_32r40r48r56r64r_e42_v16?0"_DKApplicationMonitorGuardedData"8lr32l8r40l8r48l8r56l8r64l8
- ___block_descriptor_96_e8_32s40s48s56s64r72r80r88r_e29_v24?0^{__CFDictionary=}8^v16lr64l8s32l8s40l8r72l8r80l8r88l8s48l8s56l8
- _objc_msgSend$localNonWakingRegistrationWithIdentifier:contextualPredicate:callback:
- _objc_msgSend$saveBMEventWithCurrent:outputDevices:artistStoreIdentifier:albumStoreIdentifier:excludeFromSuggestions:
- _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
- _objc_msgSend$updateFocalApplication:timestamp:displayType:transitionReason:transaction:
CStrings:
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBacklightMonitor.m:200"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNowPlayingMonitor.m:502"
+ "App extension has no LaunchServices record for its containingBundleRecord: %@ error: %@"
+ "App extension has no LaunchServices record: %@ error: %@"
+ "BMAppInFocus started %@ (transitionReason: %@)"
+ "BMAppInFocus stopped %@ (transitionReason: %@)"
+ "BMMediaNowPlayingMediaSubtype: Unrecognized value for contentType: %{public}@"
+ "BMMediaNowPlayingMediaType: Unrecognized value for strictMediaType: %{public}@"
+ "Caching app extension where the containingBundleRecord ID is nil: %@"
+ "Caching app extension where the containingBundleRecord is not eligible: %@"
+ "Extension usage monitor deallocated while still started"
+ "Extension usage monitor stopped while starting. Discarding process monitor"
+ "Found valid third-party extension: %@ (parent: %@, store ID: %lld)"
+ "Last alive date %{public}@ predates boot %{public}@; ignoring it"
+ "Sending %@ event for bundleID: %@ extensionHostID: %@ parentBundleID: %@"
+ "Starting extension usage monitor"
+ "com.apple.AppSSO.idp-extension"
+ "com.apple.AudioUnit"
+ "com.apple.AudioUnit-UI"
+ "com.apple.ManagedSettings.shield-action-service"
+ "com.apple.ManagedSettingsUI.shield-configuration-service"
+ "com.apple.Safari.content-blocker"
+ "com.apple.Safari.web-extension"
+ "com.apple.accessory-setup-extension"
+ "com.apple.accessory-transport-extension"
+ "com.apple.app-migration"
+ "com.apple.appintents-extension"
+ "com.apple.authentication-services-account-authentication-modification-ui"
+ "com.apple.authentication-services-credential-provider-ui"
+ "com.apple.background-asset-downloader-extension"
+ "com.apple.broadcast-services-setupui"
+ "com.apple.broadcast-services-upload"
+ "com.apple.calendar.virtualconference"
+ "com.apple.callkit.call-directory"
+ "com.apple.classkit.context-provider"
+ "com.apple.contact.provider.extension"
+ "com.apple.coreduet.background.extension.usage"
+ "com.apple.crash-reporter.extension"
+ "com.apple.ctk-tokens"
+ "com.apple.deviceactivity.monitor-extension"
+ "com.apple.deviceactivityui.report-extension"
+ "com.apple.fileprovider-actionsui"
+ "com.apple.fileprovider-nonui"
+ "com.apple.fileprovider-ui"
+ "com.apple.financekit.background-delivery"
+ "com.apple.identity-document-services.document-provider-ui"
+ "com.apple.identitylookup.classification-ui"
+ "com.apple.identitylookup.message-filter"
+ "com.apple.intents-service"
+ "com.apple.intents-ui-service"
+ "com.apple.keyboard-service"
+ "com.apple.live-lookup"
+ "com.apple.location.push.service"
+ "com.apple.matter.support.extension.device-setup"
+ "com.apple.message-payload-provider"
+ "com.apple.networkextension.app-proxy"
+ "com.apple.networkextension.app-push"
+ "com.apple.networkextension.dns-proxy"
+ "com.apple.networkextension.filter-control"
+ "com.apple.networkextension.filter-data"
+ "com.apple.networkextension.hotspot-authentication"
+ "com.apple.networkextension.hotspot-evaluation"
+ "com.apple.networkextension.packet-tunnel"
+ "com.apple.networkextension.url-filter-control"
+ "com.apple.photo-editing"
+ "com.apple.photos.background-upload"
+ "com.apple.printing.discovery"
+ "com.apple.public.translation-ui-provider"
+ "com.apple.quicklook.preview"
+ "com.apple.quicklook.thumbnail"
+ "com.apple.securecapture"
+ "com.apple.services"
+ "com.apple.share-services"
+ "com.apple.spotlight.import"
+ "com.apple.spotlight.index"
+ "com.apple.ui-services"
+ "com.apple.usernotifications.content-extension"
+ "com.apple.usernotifications.service"
+ "com.apple.widgetkit-extension"
+ "contentType"
+ "deviceactivitylevelmonitor"
+ "end"
+ "start"
+ "strictMediaType"
+ "system:"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBacklightMonitor.m:193"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNowPlayingMonitor.m:494"
- "B16@?0@\"NSString\"8"
- "BMAppInFocus started %@"
- "BMAppInFocus stopped %@"
- "v16@?0@\"NSTimer\"8"
```
