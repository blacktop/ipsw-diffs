## NFC

> `/System/Library/CoreAccessories/PlugIns/Transports/NFC.transport/NFC`

```diff

-1003.0.0.0.0
+1008.0.0.502.1
   __TEXT.__text: 0xa06c
   __TEXT.__auth_stubs: 0x790
   __TEXT.__objc_methlist: 0x230
-  __TEXT.__cstring: 0xb91
+  __TEXT.__cstring: 0xbe8
   __TEXT.__const: 0x1390
   __TEXT.__oslogstring: 0x17a2
   __TEXT.__gcc_except_tab: 0x1a8

   __TEXT.__objc_methtype: 0x394
   __TEXT.__objc_stubs: 0xde0
   __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x7e8
+  __DATA_CONST.__const: 0x828
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__auth_got: 0x3d8
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0xd40
+  __AUTH_CONST.__cfstring: 0xdc0
   __AUTH_CONST.__objc_const: 0x8b8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 126
-  Symbols:   558
-  CStrings:  375
+  Symbols:   566
+  CStrings:  0
 
Symbols:
+ _ACCUserDefaultsKey_DisableNFCAuthTimer
+ _ACCUserDefaultsKey_EnableIndonesiaInductiveTx
+ _ACCUserDefaultsKey_PretendNoNFCResponse
+ _ACCUserDefaultsKey_UARPActivityTimerS
+ _kCFACCUserDefaultsKey_DisableNFCAuthTimer
+ _kCFACCUserDefaultsKey_EnableIndonesiaInductiveTx
+ _kCFACCUserDefaultsKey_PretendNoNFCResponse
+ _kCFACCUserDefaultsKey_UARPActivityTimerS
CStrings:
- "BYPreferencesController"
- "C_CLASS_$_IOSurfaceDebugDescription"
- "MutableFieldInfo"
- "_AnalyticsIsEventUsed"
- "_AnalyticsRolloverEvents"
- "_AnalyticsSendEvent"
- "_AnalyticsSendEventLazy"
- "_AnalyticsSendExplodingEventLazy"
- "_AnalyticsSetCallbackForQueriedEventWithQueue"
- "_BYAssistantScreenShouldRunForPHSUpgrade"
- "_BYFlowSkipIdentifierFaceID"
- "_BYFlowSkipIdentifierPasscode"
- "_BYFlowSkipIdentifierSiri"
- "_BYSetupAssistantCreateAuthContext"
- "_BYSetupAssistantEnsureShortLivedTokenUpgrade"
- "_BYSetupAssistantPrepareLaunchSentinel"
- "_CSMapAddMapTable"
- "_CSMapGetHeader"
- "_CSMapInit"
- "_CSMapRemoveValue"
- "_CSMapSetValue"
- "_CSMapWriteToHeader"
- "_CSStoreAllocUnit"
- "_CSStoreAllocUnitWithData"
- "_CSStoreCreateMutable"
- "_CSStoreCreateMutableCopy"
- "_CSStoreFreeUnit"
- "_CSStoreGetGeneration"
- "_CSStoreGetHeader"
- "_CSStoreGetUnit"
- "_CSStringBindingCopyCFStrings"
- "_CSStringBindingFindStringAndBindings"
- "_CSStringBindingRemoveBindings"
- "_CSStringBindingSetBindings"
- "_CSStringBindingStoreAddTable"
- "_CSStringBindingStoreInit"
- "_OBJC_CLASS_$_AnalyticsConfigurationObserver"
- "_OBJC_CLASS_$_AnalyticsEventObserver"
- "_OBJC_CLASS_$_BFFSettingsManager"
- "_OBJC_CLASS_$_BYActionButtonStore"
- "_OBJC_CLASS_$_BYAnalyticsEvent"
- "_OBJC_CLASS_$_BYAnalyticsEventAppearance"
- "_OBJC_CLASS_$_BYAnalyticsEventAppleIDSignIn"
- "_OBJC_CLASS_$_BYAnalyticsEventRecommendedLocale"
- "_OBJC_CLASS_$_BYAnalyticsExpressRestore"
- "_OBJC_CLASS_$_BYAnalyticsLazyEvent"
- "_OBJC_CLASS_$_BYAnalyticsManager"
- "_OBJC_CLASS_$_BYAppleIDAccountsManager"
- "_OBJC_CLASS_$_BYAuthenticationContext"
- "_OBJC_CLASS_$_BYBackupMetadata"
- "_OBJC_CLASS_$_BYBuddyDaemonCloudSyncClient"
- "_OBJC_CLASS_$_BYBuddyDaemonGeneralClient"
- "_OBJC_CLASS_$_BYBuddyDaemonMigrationSourceClient"
- "_OBJC_CLASS_$_BYBuddyDaemonProximityAutomatedDeviceEnrollmentTargetClient"
- "_OBJC_CLASS_$_BYBuddyDaemonProximitySourceClient"
- "_OBJC_CLASS_$_BYBuddyDaemonProximityTargetClient"
- "_OBJC_CLASS_$_BYCapabilities"
- "_OBJC_CLASS_$_BYChronicle"
- "_OBJC_CLASS_$_BYChronicleEntry"
- "_OBJC_CLASS_$_BYDevice"
- "_OBJC_CLASS_$_BYDeviceConfiguration"
- "_OBJC_CLASS_$_BYDeviceMigrationManager"
- "_OBJC_CLASS_$_BYDeviceSetupSourceSession"
- "_OBJC_CLASS_$_BYExpressCloudSettings"
- "_OBJC_CLASS_$_BYFindMyManager"
- "_OBJC_CLASS_$_BYFlowSkipController"
- "_OBJC_CLASS_$_BYGreenController"
- "_OBJC_CLASS_$_BYLicenseAgreement"
- "_OBJC_CLASS_$_BYLocaleCountry"
- "_OBJC_CLASS_$_BYLocaleDataSource"
- "_OBJC_CLASS_$_BYLocationController"
- "_OBJC_CLASS_$_BYManagedAppleIDBootstrap"
- "_OBJC_CLASS_$_BYMigrationSourceController"
- "_OBJC_CLASS_$_BYMultitaskingGestures"
- "_OBJC_CLASS_$_BYNetworkMonitor"
- "_OBJC_CLASS_$_BYPaneFeatureAnalyticsManager"
- "_OBJC_CLASS_$_BYPowerLogAnalyticsManager"
- "_OBJC_CLASS_$_BYPowerLogEvent"
- "_OBJC_CLASS_$_BYPreferencesController"
- "_OBJC_CLASS_$_BYRunState"
- "_OBJC_CLASS_$_BYSeedProgramManager"
- "_OBJC_CLASS_$_BYSettingsManagerClient"
- "_OBJC_CLASS_$_BYSetupStateManager"
- "_OBJC_CLASS_$_BYSetupStateNotifier"
- "_OBJC_CLASS_$_BYSetupUserDisposition"
- "_OBJC_CLASS_$_BYSilentLoginUpgradeGuarantor"
- "_OBJC_CLASS_$_BYSiriUtilities"
- "_OBJC_CLASS_$_BYSourceDeviceMigration"
- "_OBJC_CLASS_$_BYTelephonyStateNotifier"
- "_OBJC_CLASS_$_BYWarranty"
- "_OBJC_CLASS_$_BYXPCActivity"
- "_OBJC_CLASS_$_BYXPCActivityRegistrar"
- "_OBJC_CLASS_$_BuddyFeatureFlags"
- "_OBJC_CLASS_$_DEAttachmentGroup"
- "_OBJC_CLASS_$_DECollectionProgress"
- "_OBJC_CLASS_$_DEExtensionHostContext"
- "_OBJC_CLASS_$_DEExtensionTracker"
- "_OBJC_CLASS_$_IOSurface"
- "_OBJC_CLASS_$_IOSurfaceMemoryPool"
- "_OBJC_CLASS_$_IOSurfaceRemotePerSurfaceGlobalState"
- "_OBJC_CLASS_$_IOSurfaceRemotePerSurfacePerClientState"
- "_OBJC_CLASS_$_IOSurfaceRemoteRemoteClient"
- "_OBJC_CLASS_$_IOSurfaceRemoteServer"
- "_OBJC_CLASS_$_IOSurfaceSharedEventListener"
- "_OBJC_CLASS_$_OSADateCounter"
- "_OBJC_CLASS_$_OSAExclaveContainer"
- "_OBJC_CLASS_$_OSAJetsamReport"
- "_OBJC_CLASS_$_OSALegacyXform"
- "_OBJC_CLASS_$_OSAOsLogPackParser"
- "_OBJC_CLASS_$_OSAParsedOsLogPart"
- "_OBJC_CLASS_$_OSASharedCacheEntry"
- "_OBJC_CLASS_$_OSASystemWatchdogCrashReport"
- "_OBJC_CLASS_$_VMUAnalyzerBase"
- "_OBJC_CLASS_$_VMUAnalyzerSummaryField"
- "_OBJC_CLASS_$_VMUBacktrace"
- "_OBJC_CLASS_$_VMUDebugTimer"
- "_OBJC_CLASS_$_VMUDirectedGraph"
- "_OBJC_CLASS_$_VMUDuplicatesAnalyzer"
- "_OBJC_CLASS_$_VMUHeapAndVMAggregator"
- "_OBJC_CLASS_$_VMULeaksAnalyzer"
- "_OBJC_CLASS_$_VMUMallocZoneAggregate"
- "_OBJC_CLASS_$_VMUOSTransactionsAnalyzer"
- "_OBJC_CLASS_$_VMUObjectIdentifier"
- "_OBJC_CLASS_$_VMUPeakFootprintAnalyzer"
- "_OBJC_CLASS_$_VMUProcInfo"
- "_OBJC_CLASS_$_VMUProcessDescription"
- "_OBJC_CLASS_$_VMURangeArray"
- "_OBJC_CLASS_$_VMUSampler"
- "_OBJC_CLASS_$_VMUStackLogReaderBase"
- "_OBJC_CLASS_$_VMUSwiftRuntimeInfo"
- "_OBJC_CLASS_$_VMUTaskMemoryCache"
- "_OBJC_CLASS_$_VMUTaskMemoryScanner"
- "_OBJC_CLASS_$_VMUTaskStackLogReader"
- "_OBJC_CLASS_$_VMUTaskThreadStates"
- "_OBJC_CLASS_$_VMUVMRegion"
- "_OBJC_CLASS_$_VMUVMRegionIdentifier"
- "_OBJC_CLASS_$_VMUWiredMemoryInfo"
- "_OBJC_IVAR_$_OSALog._filepath"
- "_OBJC_IVAR_$_OSALog._metaData"
- "_OBJC_IVAR_$_OSALog._stream"
- "_OBJC_IVAR_$_OSAReport._capture_time"
- "_OBJC_IVAR_$_OSAReport._logWritingOptions"
- "_OBJC_METACLASS_$_AnalyticsConfigurationObserver"
- "_OBJC_METACLASS_$_AnalyticsEventObserver"
- "_OBJC_METACLASS_$_BFFSettingsManager"
- "_OBJC_METACLASS_$_BYActionButtonStore"
- "_OBJC_METACLASS_$_BYAnalyticsEvent"
- "_OBJC_METACLASS_$_BYAnalyticsEventAppearance"
- "_OBJC_METACLASS_$_BYAnalyticsEventAppleIDSignIn"
- "_OBJC_METACLASS_$_BYAnalyticsEventRecommendedLocale"
- "_OBJC_METACLASS_$_BYAnalyticsExpressRestore"
- "_OBJC_METACLASS_$_BYAnalyticsLazyEvent"
- "_OBJC_METACLASS_$_BYAnalyticsManager"
- "_OBJC_METACLASS_$_BYAppleIDAccountsManager"
- "_OBJC_METACLASS_$_BYAuthenticationContext"
- "_OBJC_METACLASS_$_BYBackupMetadata"
- "_OBJC_METACLASS_$_BYBuddyDaemonCloudSyncClient"
- "_OBJC_METACLASS_$_BYBuddyDaemonGeneralClient"
- "_OBJC_METACLASS_$_BYBuddyDaemonMigrationSourceClient"
- "_OBJC_METACLASS_$_BYBuddyDaemonProximityAutomatedDeviceEnrollmentTargetClient"
- "_OBJC_METACLASS_$_BYBuddyDaemonProximitySourceClient"
- "_OBJC_METACLASS_$_BYBuddyDaemonProximityTargetClient"
- "_OBJC_METACLASS_$_BYCapabilities"
- "_OBJC_METACLASS_$_BYChronicle"
- "_OBJC_METACLASS_$_BYChronicleEntry"
- "_OBJC_METACLASS_$_BYDevice"
- "_OBJC_METACLASS_$_BYDeviceConfiguration"
- "_OBJC_METACLASS_$_BYDeviceMigrationManager"
- "_OBJC_METACLASS_$_BYDeviceSetupSourceSession"
- "_OBJC_METACLASS_$_BYExpressCloudSettings"
- "_OBJC_METACLASS_$_BYFindMyManager"
- "_OBJC_METACLASS_$_BYFlowSkipController"
- "_OBJC_METACLASS_$_BYGreenController"
- "_OBJC_METACLASS_$_BYLicenseAgreement"
- "_OBJC_METACLASS_$_BYLocaleCountry"
- "_OBJC_METACLASS_$_BYLocaleDataSource"
- "_OBJC_METACLASS_$_BYLocationController"
- "_OBJC_METACLASS_$_BYManagedAppleIDBootstrap"
- "_OBJC_METACLASS_$_BYMigrationSourceController"
- "_OBJC_METACLASS_$_BYMultitaskingGestures"
- "_OBJC_METACLASS_$_BYNetworkMonitor"
- "_OBJC_METACLASS_$_BYPaneFeatureAnalyticsManager"
- "_OBJC_METACLASS_$_BYPowerLogAnalyticsManager"
- "_OBJC_METACLASS_$_BYPowerLogEvent"
- "_OBJC_METACLASS_$_BYRunState"
- "_OBJC_METACLASS_$_BYSeedProgramManager"
- "_OBJC_METACLASS_$_BYSettingsManagerClient"
- "_OBJC_METACLASS_$_BYSetupStateManager"
- "_OBJC_METACLASS_$_BYSetupStateNotifier"
- "_OBJC_METACLASS_$_BYSetupUserDisposition"
- "_OBJC_METACLASS_$_BYSilentLoginUpgradeGuarantor"
- "_OBJC_METACLASS_$_BYSiriUtilities"
- "_OBJC_METACLASS_$_BYSourceDeviceMigration"
- "_OBJC_METACLASS_$_BYTelephonyStateNotifier"
- "_OBJC_METACLASS_$_BYWarranty"
- "_OBJC_METACLASS_$_BYXPCActivity"
- "_OBJC_METACLASS_$_BYXPCActivityRegistrar"
- "_OBJC_METACLASS_$_BuddyFeatureFlags"
- "_OBJC_METACLASS_$_DEAttachmentGroup"
- "_OBJC_METACLASS_$_DEExtensionTracker"
- "_OBJC_METACLASS_$_IOSurface"
- "_OBJC_METACLASS_$_IOSurfaceDebugDescription"
- "_OBJC_METACLASS_$_IOSurfaceMemoryPool"
- "_OBJC_METACLASS_$_IOSurfaceRemotePerSurfaceGlobalState"
- "_OBJC_METACLASS_$_IOSurfaceRemotePerSurfacePerClientState"
- "_OBJC_METACLASS_$_IOSurfaceRemoteRemoteClient"
- "_OBJC_METACLASS_$_IOSurfaceRemoteServer"
- "_OBJC_METACLASS_$_IOSurfaceSharedEventListener"
- "_OBJC_METACLASS_$_OSAExclaveContainer"
- "_OBJC_METACLASS_$_OSAJetsamReport"
- "_OBJC_METACLASS_$_OSAOsLogPackParser"
- "_OBJC_METACLASS_$_OSAParsedOsLogPart"
- "_OBJC_METACLASS_$_VMUAnalyzerBase"
- "_OBJC_METACLASS_$_VMUAnalyzerSummaryField"
- "_OBJC_METACLASS_$_VMUBacktrace"
- "_OBJC_METACLASS_$_VMUClassInfo"
- "_OBJC_METACLASS_$_VMUClassInfoMap"
- "_OBJC_METACLASS_$_VMUDebugTimer"
- "_OBJC_METACLASS_$_VMUDirectedGraph"
- "_OBJC_METACLASS_$_VMUDuplicatesAnalyzer"
- "_OBJC_METACLASS_$_VMUFieldInfo"
- "_OBJC_METACLASS_$_VMUHeapAndVMAggregator"
- "_OBJC_METACLASS_$_VMULeaksAnalyzer"
- "_OBJC_METACLASS_$_VMUMallocZoneAggregate"
- "_OBJC_METACLASS_$_VMUMutableClassInfo"
- "_OBJC_METACLASS_$_VMUMutableFieldInfo"
- "_OBJC_METACLASS_$_VMUOSTransactionsAnalyzer"
- "_OBJC_METACLASS_$_VMUObjectIdentifier"
- "_OBJC_METACLASS_$_VMUPeakFootprintAnalyzer"
- "_OBJC_METACLASS_$_VMUProcInfo"
- "_OBJC_METACLASS_$_VMUProcessDescription"
- "_OBJC_METACLASS_$_VMURangeArray"
- "_OBJC_METACLASS_$_VMUSampler"
- "_OBJC_METACLASS_$_VMUStackLogReaderBase"
- "_OBJC_METACLASS_$_VMUSwiftRuntimeInfo"
- "_OBJC_METACLASS_$_VMUTaskMemoryCache"
- "_OBJC_METACLASS_$_VMUTaskMemoryScanner"
- "_OBJC_METACLASS_$_VMUTaskStackLogReader"
- "_OBJC_METACLASS_$_VMUTaskThreadStates"
- "_OBJC_METACLASS_$_VMUVMRegion"
- "_OBJC_METACLASS_$_VMUVMRegionIdentifier"
- "_OBJC_METACLASS_$_VMUWiredMemoryInfo"
- "_OSADateFormat"
- "_OSAIsACDCDevice"
- "_OSAIsDebugEnabledForRSD"
- "_OSAIsRSDDevice"
- "_OSAIsRSDDisplay"
- "_OSAIsRSDHost"
- "_OSANSDateFormat"
- "_OSASafeOpenWriteOnly"
- "_OSASanitizePath"
- "_OSAStateMonitorEventSubmission"
- "_OSAStateMonitorEventSubmissionErrorDescriptionKey"
- "_OSAStateMonitorEventSubmissionErrorHTTPPostError"
- "_OSAStateMonitorEventSubmissionFoundLogs"
- "_OSAStateMonitorEventSubmissionFoundLogsLogsKey"
- "_OSAStateMonitorEventSubmissionHTTPPostStarted"
- "_OSAStateMonitorEventSubmissionHTTPPostStartedContentLength"
- "_OSAStateMonitorEventSubmissionHTTPPostStartedIncludedLogsKey"
- "_OSAStateMonitorEventSubmissionLogsAddedToArchive"
- "_OSAStateMonitorEventSubmissionLogsAddedToArchiveLogsKey"
- "_OSAnalyticsHelperServiceConnection"
- "_SimulateCrash"
- "_WriteCrashReportWithStackshot"
- "_WriteCrashReportWithStackshotWithPayload"
- "_WriteStackshotReport"
- "_WriteStackshotReportWithPID"
- "_WriteStackshotReport_async"
- "_WriteStackshotReport_stdc"
- "__CSArrayAppendValue"
- "__CSArrayCreate"
- "__CSArrayCreateWithCapacity"
- "__CSArrayDispose"
- "__CSArrayEnumerateAllValues"
- "__CSArrayGetCount"
- "__CSArrayGetValueAtIndex"
- "__CSArrayInsertValueAtIndex"
- "__CSArrayRemoveValueAtIndex"
- "__CSCopyStringForCharacters"
- "__CSGetConstStringForCharacters"
- "__CSGetStringForCFString"
- "__CSGetStringForCharacters"
- "__CSMapCopyDebugDescription"
- "__CSStoreAccessContextAccessForRead"
- "__CSStoreAccessContextAssertReading"
- "__CSStoreAccessContextAssertWriting"
- "__CSStoreAccessContextCreateSharedReadingContext"
- "__CSStoreAccessContextCreateWithLock"
- "__CSStoreAddTable"
- "__CSStoreCopyDebugDescriptionOfBytesInRange"
- "__CSStoreCopyDebugDescriptionOfUnit"
- "__CSStoreCopyMemoryStatistics"
- "__CSStoreCopyTableName"
- "__CSStoreCreateDataWithUnitNoCopy"
- "__CSStoreCreateWithURL"
- "__CSStoreCreateWithXPCRepresentation"
- "__CSStoreCreateXPCRepresentation"
- "__CSStoreEnumerateTables"
- "__CSStoreEnumerateUnits"
- "__CSStoreGarbageCollect"
- "__CSStoreGetArrayTable"
- "__CSStoreGetCatalogTable"
- "__CSStoreGetStringTable"
- "__CSStoreGetTableWithName"
- "__CSStoreGetXPCClass"
- "__CSStoreIsMutable"
- "__CSStoreSetExpectedAccessContext"
- "__CSStoreSetMutable"
- "__CSStoreValidate"
- "__CSStoreWriteToHeader"
- "__CSStoreWriteToURL"
- "__CSStoreWriteToUnit"
- "__CSStringBindingEnumerate"
- "__CSStringBindingEnumerateAllBindings"
- "__CSStringBindingGetBindings"
- "__CSStringCopyCFString"
- "__CSStringIsValid"
- "__CSStringMakeConst"
- "__CSStringRelease"
- "__CSStringRetain"
- "__CSVisualizerForegroundColorAttributeName"
- "__ZN8CSStore222AttributedStringWriter10beginFlagsEP8NSStringm"
- "__ZN8CSStore222AttributedStringWriter11missingFlagEmP8NSStringRKNSt3__18optionalIjEE"
- "__ZN8CSStore222AttributedStringWriter11stringArrayEP8NSStringPKjj"
- "__ZN8CSStore222AttributedStringWriter11stringArrayEP8NSStringj"
- "__ZN8CSStore222AttributedStringWriter13setVisualizerEP13_CSVisualizer"
- "__ZN8CSStore222AttributedStringWriter13withTextColorEjU13block_pointerFvvE"
- "__ZN8CSStore222AttributedStringWriter16attributedStringEP18NSAttributedString"
- "__ZN8CSStore222AttributedStringWriter17withWarningColorsEU13block_pointerFvvE"
- "__ZN8CSStore222AttributedStringWriter18beginBitfieldFlagsEP8NSString"
- "__ZN8CSStore222AttributedStringWriter18setInsertsNewlinesEb"
- "__ZN8CSStore222AttributedStringWriter19withReferenceToUnitEjjU13block_pointerFvvE"
- "__ZN8CSStore222AttributedStringWriter20setElidesEmptyValuesEb"
- "__ZN8CSStore222AttributedStringWriter20withAppliedAttributeEP8NSStringP11objc_objectU13block_pointerFvvE"
- "__ZN8CSStore222AttributedStringWriter26withTextAndBackgroundColorEjjU13block_pointerFvvE"
- "__ZN8CSStore222AttributedStringWriter4flagEmP8NSStringRKNSt3__18optionalIjEE"
- "__ZN8CSStore222AttributedStringWriter4linkEP5NSURLP8NSString"
- "__ZN8CSStore222AttributedStringWriter4linkEjjP8NSString"
- "__ZN8CSStore222AttributedStringWriter5arrayEP7NSArray"
- "__ZN8CSStore222AttributedStringWriter5arrayEP8NSStringP7NSArray"
- "__ZN8CSStore222AttributedStringWriter6formatEP8NSStringS2_z"
- "__ZN8CSStore222AttributedStringWriter6numberEP8NSStringP8NSNumber"
- "__ZN8CSStore222AttributedStringWriter6stringEP8NSString"
- "__ZN8CSStore222AttributedStringWriter6stringEP8NSStringS2_"
- "__ZN8CSStore222AttributedStringWriter6stringEP8NSStringj"
- "__ZN8CSStore222AttributedStringWriter8endFlagsEv"
- "__ZN8CSStore222AttributedStringWriter9SeparatorEcP8NSString"
- "__ZN8CSStore222AttributedStringWriter9childUnitEP8NSStringjj"
- "__ZN8CSStore222AttributedStringWriter9childUnitEjj"
- "__ZN8CSStore222AttributedStringWriter9separatorEcP8NSString"
- "__ZN8CSStore222AttributedStringWriter9timestampEP8NSStringd"
- "__ZN8CSStore222AttributedStringWriterC2EPK9__CSStoreP25NSMutableAttributedString"
- "__ZN8CSStore222AttributedStringWriterC2ERKS0_"
- "__ZN8CSStore222AttributedStringWriterD2Ev"
- "__ZNK8CSStore222AttributedStringWriter13getVisualizerEv"
- "_analytics_is_event_used"
- "_analytics_send_event"
- "_analytics_send_event_lazy"
- "_kOSALogOptionCreateTmpFile"
- "_kOSALogOptionDataVaultPath"
- "_kOSALogOptionDisplayName"
- "_kOSALogOptionFileOwner"
- "_kOSALogOptionMoveSourceFile"
- "_kOSALogOptionOverrideCountLimit"
- "_kOSALogOptionOverrideFileExtension"
- "_kOSALogOptionOverrideFilePrefix"
- "_kOSALogOptionOverridePath"
- "_kOSALogOptionPriority"
- "_kOSALogScanOptionIncludeProxiesKey"
- "_kPathOptionUntrusted"
- "_ns2xpc"
- "_rtcsc_send"
- "_xpc2ns"
- "entifierTouchID"
- "pAssistantHasCompletedInitialRun"

```