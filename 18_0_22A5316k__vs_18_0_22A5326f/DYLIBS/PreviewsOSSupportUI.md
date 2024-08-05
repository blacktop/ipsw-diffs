## PreviewsOSSupportUI

> `/System/Library/PrivateFrameworks/PreviewsOSSupportUI.framework/PreviewsOSSupportUI`

```diff

-22.0.69.0.0
-  __TEXT.__text: 0x1f57c
-  __TEXT.__auth_stubs: 0xd40
+22.0.72.0.0
+  __TEXT.__text: 0x1f4a8
+  __TEXT.__auth_stubs: 0xd20
   __TEXT.__objc_methlist: 0x21c
   __TEXT.__const: 0x1ea8
   __TEXT.__cstring: 0xd20
   __TEXT.__oslogstring: 0x190
-  __TEXT.__swift5_typeref: 0x869
+  __TEXT.__swift5_typeref: 0x868
   __TEXT.__constg_swiftt: 0x648
   __TEXT.__swift5_reflstr: 0x498
   __TEXT.__swift5_fieldmd: 0x75c

   __TEXT.__swift5_proto: 0x1c4
   __TEXT.__swift5_types: 0xac
   __TEXT.__unwind_info: 0x9f8
-  __TEXT.__eh_frame: 0x6b8
+  __TEXT.__eh_frame: 0x680
   __TEXT.__objc_classname: 0x121
   __TEXT.__objc_methname: 0x91c
   __TEXT.__objc_methtype: 0x27d
   __TEXT.__objc_stubs: 0x280
-  __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0xc0
+  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_selrefs: 0x268
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x6a8
+  __AUTH_CONST.__auth_got: 0x698
   __AUTH_CONST.__auth_ptr: 0x2b0
   __AUTH_CONST.__const: 0x1b40
   __AUTH_CONST.__cfstring: 0x80

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 983
-  Symbols:   224
-  CStrings:  0
+  Symbols:   230
+  CStrings:  196
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _swift_continuation_await
- _swift_continuation_init
CStrings:
+ "VPixelBufferCustomMemoryLayoutCallbacksKey"
+ "_ACAccountCredentialsDidChangeNotification"
+ "_ACAccountDataclassAvailability"
+ "_ACAccountDataclassBackup"
+ "_ACAccountDataclassBookmarks"
+ "_ACAccountDataclassCKCodeService"
+ "_ACAccountDataclassCKDatabaseService"
+ "_ACAccountDataclassCKDeviceService"
+ "_ACAccountDataclassCKMetricsService"
+ "_ACAccountDataclassCKShareService"
+ "_ACAccountDataclassCalendars"
+ "_ACAccountDataclassCloudPhotos"
+ "_ACAccountDataclassContacts"
+ "_ACAccountDataclassContactsSearch"
+ "_ACAccountDataclassContent"
+ "_ACAccountDataclassDeviceLocator"
+ "_ACAccountDataclassFitnessPlus"
+ "_ACAccountDataclassFreeform"
+ "_ACAccountDataclassHealth"
+ "_ACAccountDataclassHome"
+ "_ACAccountDataclassKeyValue"
+ "_ACAccountDataclassKeychainSync"
+ "_ACAccountDataclassMail"
+ "_ACAccountDataclassMediaStream"
+ "_ACAccountDataclassMessages"
+ "_ACAccountDataclassMoments"
+ "_ACAccountDataclassNetworkVPN"
+ "_ACAccountDataclassNews"
+ "_ACAccountDataclassNotes"
+ "_ACAccountDataclassPhoneFaceTime"
+ "_ACAccountDataclassPhotos"
+ "_ACAccountDataclassProtectedCloudStorage"
+ "_ACAccountDataclassReminders"
+ "_ACAccountDataclassServerDocuments"
+ "_ACAccountDataclassSettings"
+ "_ACAccountDataclassShareLocation"
+ "_ACAccountDataclassSharedStreams"
+ "_ACAccountDataclassShoebox"
+ "_ACAccountDataclassSiri"
+ "_ACAccountDataclassStocks"
+ "_ACAccountDataclassUbiquity"
+ "_ACAccountIdentifierKey"
+ "_ACAccountPropertyFirstName"
+ "_ACAccountPropertyFullName"
+ "_ACAccountStoreDidChangeNotification"
+ "_ACAccountTypeIdentifierKey"
+ "_ACDAccountStoreDidChangeNotification"
+ "_ACKeepPasswordsAround"
+ "_ACMonitoredAccountStoreDidChangeNotification"
+ "_ACRemoteDeviceCommandAddAccount"
+ "_ACRemoteDeviceCommandDeleteAccount"
+ "_ACRemoteDeviceCommandDeleteAllAccounts"
+ "_ACRemoteDeviceCommandFetchAccounts"
+ "_ACRemoteDeviceCommandInvalidateFetchedAccountsCache"
+ "_ACRemoteDeviceCommandShowCredentialPrompt"
+ "_ACRemoteDeviceCommandUpdateAccount"
+ "_ACRemoteDeviceCommandUpdateAccountCredential"
+ "_ACRemoteDeviceOptionAccountQueryIgnoreCache"
+ "_ACRemoteDeviceOptionAskForReply"
+ "_ACRemoteDeviceOptionPreloadedPropertiesArray"
+ "_ACRemoteDeviceOptionTargetDeviceBTUUID"
+ "_ACShouldSuppressPromptsKey"
+ "_kACAccountIdentifier"
+ "_kACAllowedSSLCertificatesKey"
+ "_kACDShouldNotCoalesceRequests"
+ "_kACDShouldNotUseParentAccount"
+ "_kACDiscoverPropertiesShouldSaveKey"
+ "_kACIDServiceCommandAccountDeleted"
+ "_kACIDServiceCommandNewAccount"
+ "_kACIDServiceCommandPromptUser"
+ "_kACRenewCredentialsAppleIDServiceTypeKey"
+ "_kACRenewCredentialsProxiedAppBundleIDKey"
+ "_kACRenewCredentialsReasonStringKey"
+ "_kACRenewCredentialsServicesKey"
+ "_kACRenewCredentialsShouldAvoidUIKey"
+ "_kACRenewCredentialsShouldForceKey"
+ "_kACRenewCredentialsShouldPromptBeforeRenewKey"
+ "_kACVerifyCredentialsShouldSaveKey"
+ "_kAccountAuthenticationTypeNone"
+ "_kAccountAuthenticationTypeParent"
+ "_kAccountDataclassAvailability"
+ "_kAccountDataclassBackToMyMacDeprecated"
+ "_kAccountDataclassBackup"
+ "_kAccountDataclassBookmarks"
+ "_kAccountDataclassCKDatabaseService"
+ "_kAccountDataclassCKDeviceService"
+ "_kAccountDataclassCKShareService"
+ "_kAccountDataclassCalendars"
+ "_kAccountDataclassCloudDesktop"
+ "_kAccountDataclassCloudPhotos"
+ "_kAccountDataclassContacts"
+ "_kAccountDataclassContactsSearch"
+ "_kAccountDataclassContent"
+ "_kAccountDataclassCoreRoutine"
+ "_kAccountDataclassDeviceLocator"
+ "_kAccountDataclassHealth"
+ "_kAccountDataclassHome"
+ "_kAccountDataclassKeyValue"
+ "_kAccountDataclassKeychainSync"
+ "_kAccountDataclassMail"
+ "_kAccountDataclassMediaStream"
+ "_kAccountDataclassMessages"
+ "_kAccountDataclassNetworkVPN"
+ "_kAccountDataclassNews"
+ "_kAccountDataclassNotes"
+ "_kAccountDataclassNotifications"
+ "_kAccountDataclassPhotos"
+ "_kAccountDataclassReminders"
+ "_kAccountDataclassServerDocumentsDeprecated"
+ "_kAccountDataclassShareLocation"
+ "_kAccountDataclassShareMenu"
+ "_kAccountDataclassSharedStreams"
+ "_kAccountDataclassShoebox"
+ "_kAccountDataclassSiri"
+ "_kAccountDataclassSmartDefaults"
+ "_kAccountDataclassStocks"
+ "_kAccountDataclassUbiquity"
+ "_kCVImageBufferAlphaChannelIsOpaque"
+ "_kCVImageBufferAlphaChannelModeKey"
+ "_kCVImageBufferAlphaChannelMode_PremultipliedAlpha"
+ "_kCVImageBufferAlphaChannelMode_StraightAlpha"
+ "_kCVImageBufferAmbientViewingEnvironmentKey"
+ "_kCVImageBufferBlankieTransportIdentifierKey"
+ "_kCVImageBufferChromaLocationBottomFieldKey"
+ "_kCVImageBufferChromaLocationTopFieldKey"
+ "_kCVImageBufferChromaLocation_Bottom"
+ "_kCVImageBufferChromaLocation_BottomLeft"
+ "_kCVImageBufferChromaLocation_Center"
+ "_kCVImageBufferChromaLocation_DV420"
+ "_kCVImageBufferChromaLocation_Left"
+ "_kCVImageBufferChromaLocation_Top"
+ "_kCVImageBufferChromaLocation_TopLeft"
+ "_kCVImageBufferChromaSubsamplingKey"
+ "_kCVImageBufferChromaSubsampling_420"
+ "_kCVImageBufferChromaSubsampling_422"
+ "_kCVImageBufferContentLightLevelInfoKey"
+ "_kCVImageBufferDolbyCompatibilityIDKey"
+ "_kCVImageBufferDolbyVisionRPUDataKey"
+ "_kCVImageBufferHDR10PlusDataKey"
+ "_kCVImageBufferHDRImageStatisticsInfoFilteredKey"
+ "_kCVImageBufferHDRImageStatisticsInfoRawKey"
+ "_kCVImageBufferHDRImageStatisticsInfoTransferFunctionKey"
+ "_kCVImageBufferHDRImageStatisticsInfo_AnchorPQKey"
+ "_kCVImageBufferHDRImageStatisticsInfo_AnchorPowerKey"
+ "_kCVImageBufferHDRImageStatisticsInfo_AverageOffsetKey"
+ "_kCVImageBufferHDRImageStatisticsInfo_DolbyMetadataVersionKey"
+ "_kCVImageBufferHDRImageStatisticsInfo_MaximumKey"
+ "_kCVImageBufferHDRImageStatisticsInfo_MaximumOffsetKey"
+ "_kCVImageBufferHDRImageStatisticsInfo_MinimumKey"
+ "_kCVImageBufferHDRImageStatisticsInfo_MinimumOffsetKey"
+ "_kCVImageBufferHorizontalDisparityAdjustmentKey"
+ "_kCVImageBufferLogTransferFunctionKey"
+ "_kCVImageBufferLogTransferFunction_AppleLog"
+ "_kCVImageBufferMasteringDisplayColorVolumeKey"
+ "_kCVImageBufferRegionOfInterestKey"
+ "_kCVImageBufferSceneIlluminationKey"
+ "_kCVImageBufferSceneReferredExtendedLinearKey"
+ "_kCVPixelBufferBytesPerRowAlignmentKey"
+ "_kCVPixelBufferCGBitmapContextCompatibilityKey"
+ "_kCVPixelBufferCGImageCompatibilityKey"
+ "_kCVPixelBufferCacheModeKey"
+ "_kCVPixelBufferCompressedDataRegionAlignmentKey"
+ "_kCVPixelBufferCompressedTileHeaderGroupBytesPerRowAlignmentKey"
+ "_kCVPixelBufferExactBytesPerRowKey"
+ "_kCVPixelBufferExtendedPixelsBottomKey"
+ "_kCVPixelBufferExtendedPixelsFilledKey"
+ "_kCVPixelBufferExtendedPixelsLeftKey"
+ "_kCVPixelBufferExtendedPixelsRightKey"
+ "_kCVPixelBufferExtendedPixelsTopKey"
+ "_kCVPixelBufferFixedPointInvalidValueKey"
+ "_kCVPixelBufferFixedPointOffsetKey"
+ "_kCVPixelBufferHeightKey"
+ "_kCVPixelBufferIOSurfaceCoreAnimationCompatibilityHTPCOKKey"
+ "_kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey"
+ "_kCVPixelBufferIOSurfacePropertiesKey"
+ "_kCVPixelBufferMemoryAllocatorKey"
+ "_kCVPixelBufferMetalCompatibilityKey"
+ "_kCVPixelBufferNumberOfSlicesKey"
+ "_kCVPixelBufferOpenGLCompatibilityKey"
+ "_kCVPixelBufferOpenGLESCompatibilityKey"
+ "_kCVPixelBufferOpenGLESTextureCacheCompatibilityKey"
+ "_kCVPixelBufferPixelFormatDescriptionKey"
+ "_kCVPixelBufferPixelFormatTypeKey"
+ "_kCVPixelBufferPlaneAlignmentKey"
+ "_kCVPixelBufferPoolAllocationThresholdKey"
+ "_kCVPixelBufferPoolMinimumBufferCountKey"
+ "_kCVPixelBufferPoolNameKey"
+ "_kCVPixelBufferPoolRequireIOSurfaceWithoutWiringAssertionYetKey"
+ "_kCVPixelBufferPreferRealTimeCacheModeIfEveryoneDoesKey"
+ "_kCVPixelBufferQDCompatibilityKey"
+ "_kCVPixelBufferRotationKey"
+ "_kCVPixelBufferWidthKey"
+ "ferFunction_UseGamma"
+ "o_AverageKey"
+ "serializeSecCertificates"
+ "tChanged"

```
