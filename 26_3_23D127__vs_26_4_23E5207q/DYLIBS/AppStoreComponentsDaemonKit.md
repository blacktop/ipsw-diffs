## AppStoreComponentsDaemonKit

> `/System/Library/PrivateFrameworks/AppStoreComponentsDaemonKit.framework/AppStoreComponentsDaemonKit`

```diff

-8.3.1.0.0
-  __TEXT.__text: 0x10cc90
-  __TEXT.__auth_stubs: 0x3b20
-  __TEXT.__objc_methlist: 0x47a0
-  __TEXT.__const: 0x6bb0
-  __TEXT.__cstring: 0x973c
-  __TEXT.__oslogstring: 0x1ced
+8.4.11.0.0
+  __TEXT.__text: 0x113758
+  __TEXT.__auth_stubs: 0x3a90
+  __TEXT.__objc_methlist: 0x4780
+  __TEXT.__const: 0x6c00
+  __TEXT.__cstring: 0x6cbc
+  __TEXT.__oslogstring: 0x1cbc
   __TEXT.__gcc_except_tab: 0x58
   __TEXT.__dlopen_cstrs: 0x8e
   __TEXT.__constg_swiftt: 0x1a1c
-  __TEXT.__swift5_typeref: 0x3379
+  __TEXT.__swift5_typeref: 0x3349
   __TEXT.__swift5_fieldmd: 0x1658
   __TEXT.__swift5_builtin: 0x1f4
   __TEXT.__swift5_reflstr: 0x11d6
   __TEXT.__swift5_assocty: 0x6c8
   __TEXT.__swift5_capture: 0x17b8
-  __TEXT.__swift5_proto: 0x41c
+  __TEXT.__swift5_proto: 0x420
   __TEXT.__swift5_types: 0x224
-  __TEXT.__swift_as_entry: 0x1e4
-  __TEXT.__swift_as_ret: 0x284
+  __TEXT.__swift_as_entry: 0x1e8
+  __TEXT.__swift_as_ret: 0x288
   __TEXT.__swift5_mpenum: 0x24
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__unwind_info: 0x38b0
-  __TEXT.__eh_frame: 0x8064
-  __TEXT.__objc_classname: 0x86c
-  __TEXT.__objc_methname: 0x7dd8
-  __TEXT.__objc_methtype: 0x1276
-  __TEXT.__objc_stubs: 0x3980
+  __TEXT.__unwind_info: 0x3838
+  __TEXT.__eh_frame: 0x8074
+  __TEXT.__objc_classname: 0x1826
+  __TEXT.__objc_methname: 0x90b1
+  __TEXT.__objc_methtype: 0x1eb3
+  __TEXT.__objc_stubs: 0x5580
   __DATA_CONST.__got: 0xd18
-  __DATA_CONST.__const: 0x7a8
-  __DATA_CONST.__objc_classlist: 0x338
+  __DATA_CONST.__const: 0x7c8
+  __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e98
+  __DATA_CONST.__objc_selrefs: 0x1ec8
   __DATA_CONST.__objc_protorefs: 0x140
-  __DATA_CONST.__objc_superrefs: 0x1f0
-  __AUTH_CONST.__auth_got: 0x1da0
+  __DATA_CONST.__objc_superrefs: 0x1e8
+  __AUTH_CONST.__auth_got: 0x1d58
   __AUTH_CONST.__const: 0x58e8
-  __AUTH_CONST.__cfstring: 0x35e0
-  __AUTH_CONST.__objc_const: 0xa070
-  __AUTH.__objc_data: 0x1750
-  __AUTH.__data: 0x3b8
-  __DATA.__objc_ivar: 0x380
-  __DATA.__data: 0x20f0
-  __DATA.__bss: 0x5330
+  __AUTH_CONST.__cfstring: 0x3680
+  __AUTH_CONST.__objc_const: 0xa078
+  __AUTH.__objc_data: 0xc70
+  __AUTH.__data: 0x3b0
+  __DATA.__objc_ivar: 0x390
+  __DATA.__data: 0x1a40
+  __DATA.__bss: 0x53b0
   __DATA.__common: 0x68
-  __DATA_DIRTY.__objc_data: 0x1220
-  __DATA_DIRTY.__data: 0x1d18
+  __DATA_DIRTY.__objc_data: 0x1cb0
+  __DATA_DIRTY.__data: 0x2350
   __DATA_DIRTY.__bss: 0x15e0
   __DATA_DIRTY.__common: 0x110
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 63ED3B21-A253-37B6-B9CE-9620D93E1741
-  Functions: 4501
-  Symbols:   6075
-  CStrings:  3362
+  UUID: 9A912608-57BF-32DF-862B-1BE7C6CAB48E
+  Functions: 4495
+  Symbols:   6290
+  CStrings:  3336
 
Symbols:
+ +[ASCEligibility isFreeform:]
+ +[ASCIconTextOfferMetadata supportsSecureCoding]
+ +[ASCOfferMetadata offerMetadataWithTitle:subtitle:imageName:]
+ +[ASCOfferMetadata resumeMetadata:]
+ -[ASCAppOffer initWithID:titles:subtitles:flags:ageRating:metrics:baseBuyParams:metricsBuyParams:metricsOverlay:additionalHeaders:preflightPackageURL:bundleID:itemName:vendorName:capabilities:]
+ -[ASCAppOffer metricsOverlay]
+ -[ASCIconTextOfferMetadata .cxx_destruct]
+ -[ASCIconTextOfferMetadata animationName]
+ -[ASCIconTextOfferMetadata baseImageName]
+ -[ASCIconTextOfferMetadata description]
+ -[ASCIconTextOfferMetadata encodeWithCoder:]
+ -[ASCIconTextOfferMetadata hash]
+ -[ASCIconTextOfferMetadata imageNameForSize:]
+ -[ASCIconTextOfferMetadata initWithCoder:]
+ -[ASCIconTextOfferMetadata initWithCoder:].cold.1
+ -[ASCIconTextOfferMetadata initWithCoder:].cold.2
+ -[ASCIconTextOfferMetadata initWithTitle:subtitle:imageName:animationName:]
+ -[ASCIconTextOfferMetadata isEqual:]
+ -[ASCIconTextOfferMetadata isIconOnly]
+ -[ASCIconTextOfferMetadata isTextAndIcon]
+ -[ASCIconTextOfferMetadata isTextOnly]
+ -[ASCIconTextOfferMetadata subtitle]
+ -[ASCIconTextOfferMetadata title]
+ -[ASCOfferMetadata isIconOnly]
+ -[ASCOfferMetadata isTextAndIcon]
+ -[ASCOfferMetadata isTextOnly]
+ _ASCLockupContextSpringboard
+ _OBJC_CLASS_$_ASCIconTextOfferMetadata
+ _OBJC_IVAR_$_ASCAppOffer._metricsOverlay
+ _OBJC_IVAR_$_ASCIconTextOfferMetadata._animationName
+ _OBJC_IVAR_$_ASCIconTextOfferMetadata._baseImageName
+ _OBJC_IVAR_$_ASCIconTextOfferMetadata._subtitle
+ _OBJC_IVAR_$_ASCIconTextOfferMetadata._title
+ _OBJC_IVAR_$_ASCOfferMetadata._icon
+ _OBJC_IVAR_$_ASCOfferMetadata._iconAndText
+ _OBJC_IVAR_$_ASCOfferMetadata._text
+ _OBJC_METACLASS_$_ASCIconTextOfferMetadata
+ __OBJC_$_CLASS_METHODS_ASCIconTextOfferMetadata
+ __OBJC_$_INSTANCE_METHODS_ASCIconTextOfferMetadata
+ __OBJC_$_INSTANCE_VARIABLES_ASCIconTextOfferMetadata
+ __OBJC_$_INSTANCE_VARIABLES_ASCOfferMetadata
+ __OBJC_$_PROP_LIST_ASCIconTextOfferMetadata
+ __OBJC_CLASS_RO_$_ASCIconTextOfferMetadata
+ __OBJC_METACLASS_RO_$_ASCIconTextOfferMetadata
+ _block_copy_helper.15
+ _block_descriptor.17
+ _block_destroy_helper.16
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$_setQueue:
+ _objc_msgSend$actionWithTitle:
+ _objc_msgSend$actionWithTitle:identifier:
+ _objc_msgSend$activate
+ _objc_msgSend$adamId
+ _objc_msgSend$addButtonAction:
+ _objc_msgSend$addObserver:
+ _objc_msgSend$addSubsystem:category:
+ _objc_msgSend$additionalQueryParams
+ _objc_msgSend$ams_DSID
+ _objc_msgSend$ams_accountID
+ _objc_msgSend$ams_configurationWithProcessInfo:bag:
+ _objc_msgSend$ams_cookiesForURL:
+ _objc_msgSend$ams_firstName
+ _objc_msgSend$ams_isManagedAppleID
+ _objc_msgSend$ams_lastName
+ _objc_msgSend$ams_setDSID:
+ _objc_msgSend$ams_setFirstName:
+ _objc_msgSend$ams_setLastName:
+ _objc_msgSend$ams_setManagedAppleID:
+ _objc_msgSend$ams_sharedAccountStoreForClient:
+ _objc_msgSend$appClipMetadata
+ _objc_msgSend$applicationIsInstalled:
+ _objc_msgSend$applicationState
+ _objc_msgSend$asc_frameworkBundle
+ _objc_msgSend$attributes
+ _objc_msgSend$auditToken
+ _objc_msgSend$bagForProfile:profileVersion:processInfo:
+ _objc_msgSend$beginDate
+ _objc_msgSend$bootstrapDidBeginWithTag:
+ _objc_msgSend$bootstrapDidEndWithTag:
+ _objc_msgSend$bundleURL
+ _objc_msgSend$cancellationHandler
+ _objc_msgSend$code
+ _objc_msgSend$correspondingApplicationRecord
+ _objc_msgSend$currentConnection
+ _objc_msgSend$currentProcess
+ _objc_msgSend$debugPackageURL
+ _objc_msgSend$deeplinkMetadata
+ _objc_msgSend$defaultManager
+ _objc_msgSend$description
+ _objc_msgSend$disableShutdownTimer
+ _objc_msgSend$domain
+ _objc_msgSend$doubleValue
+ _objc_msgSend$enableWebInspector
+ _objc_msgSend$enumeratorWithOptions:
+ _objc_msgSend$expirationDate
+ _objc_msgSend$expiresDate
+ _objc_msgSend$fetchIsFitnessAvailableForDeviceWithCompletion:
+ _objc_msgSend$fetchMediaToken
+ _objc_msgSend$generateEventFieldsForKeys:
+ _objc_msgSend$getAllIAPsForActiveAccountWithResultHandler:
+ _objc_msgSend$handleURL:
+ _objc_msgSend$iTunesMetadata
+ _objc_msgSend$identifierForKey:
+ _objc_msgSend$identifierStoreWithAccount:bagNamespace:bag:
+ _objc_msgSend$indeterminateProgressMetadata
+ _objc_msgSend$init
+ _objc_msgSend$initWithAccountStore:
+ _objc_msgSend$initWithArtwork:mediaPlatform:
+ _objc_msgSend$initWithBool:
+ _objc_msgSend$initWithClientIdentifier:bag:
+ _objc_msgSend$initWithDeviceCornerRadiusFactor:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$initWithID:titles:subtitles:flags:ageRating:metrics:baseBuyParams:metricsBuyParams:metricsOverlay:additionalHeaders:preflightPackageURL:bundleID:itemName:vendorName:capabilities:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$initWithMachServiceName:
+ _objc_msgSend$initWithName:identifier:
+ _objc_msgSend$initWithRequest:
+ _objc_msgSend$initWithServiceDomain:delegate:
+ _objc_msgSend$initWithStoreItemIdentifier:error:
+ _objc_msgSend$initWithStoreMetadata:
+ _objc_msgSend$initWithTitle:message:
+ _objc_msgSend$initWithTitle:subtitle:imageName:animationName:
+ _objc_msgSend$initWithType:clientIdentifier:clientVersion:bag:
+ _objc_msgSend$initWithURL:bag:
+ _objc_msgSend$initWithURLTemplate:width:height:decoration:preferredCrop:preferredFormat:
+ _objc_msgSend$initWithUnsignedLongLong:
+ _objc_msgSend$initWithVideoURL:preview:
+ _objc_msgSend$initWithVideos:mediaPlatform:
+ _objc_msgSend$installApp:onPairedDevice:withCompletionHandler:
+ _objc_msgSend$installApp:withCompletionHandler:
+ _objc_msgSend$invalidate
+ _objc_msgSend$invalidateMediaToken
+ _objc_msgSend$isCapableOfAction:capabilities:
+ _objc_msgSend$isInstalled
+ _objc_msgSend$isInstalledFromDistributorOrWeb
+ _objc_msgSend$isLaunchProhibited
+ _objc_msgSend$isOperatingSystemAtLeastVersion:
+ _objc_msgSend$isPausable
+ _objc_msgSend$isPlaceholder
+ _objc_msgSend$itemID
+ _objc_msgSend$jsCallDidBeginWithTag:
+ _objc_msgSend$jsCallDidEndWithTag:
+ _objc_msgSend$jsStackBootstrapDidBeginWithTag:
+ _objc_msgSend$jsStackBootstrapDidEndWithTag:
+ _objc_msgSend$keyWithName:crossDeviceSync:
+ _objc_msgSend$launchCorrelationKeyWithTag:withString:
+ _objc_msgSend$launchMessagesExtensionForApp:withResultHandler:
+ _objc_msgSend$localizedName
+ _objc_msgSend$lockupRequestWithCountryCodeOverride:
+ _objc_msgSend$lockupWithSignpostTags:
+ _objc_msgSend$metricsActivityByMergingFields:uniquingFieldsWithBlock:
+ _objc_msgSend$metricsOverlay
+ _objc_msgSend$nextObject
+ _objc_msgSend$numberValue
+ _objc_msgSend$offer:didChangeState:withMetadata:flags:
+ _objc_msgSend$offer:didChangeStatusText:
+ _objc_msgSend$offerContextByAddingFlags:
+ _objc_msgSend$offerMetadataWithTitle:subtitle:imageName:
+ _objc_msgSend$openApplication:withOptions:completion:
+ _objc_msgSend$openSensitiveURL:
+ _objc_msgSend$openSensitiveURL:frontBoardOptions:
+ _objc_msgSend$operatingSystemVersion
+ _objc_msgSend$optionsWithDictionary:
+ _objc_msgSend$pairingID
+ _objc_msgSend$path
+ _objc_msgSend$pause
+ _objc_msgSend$perform
+ _objc_msgSend$performAuthentication
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$predicateByAddingTag:
+ _objc_msgSend$preferInternalJS
+ _objc_msgSend$present
+ _objc_msgSend$processLogArchiveWithPath:startDate:endDate:errorOut:
+ _objc_msgSend$progress
+ _objc_msgSend$progressMetadataWithValue:cancellable:
+ _objc_msgSend$promiseWithTimeout:
+ _objc_msgSend$redownloadMetadata
+ _objc_msgSend$redownloadParams
+ _objc_msgSend$refreshIAPsForActiveAccountWithCompletionHandler:
+ _objc_msgSend$requestDidBeginWithTag:
+ _objc_msgSend$requestDidEndWithTag:
+ _objc_msgSend$requiredFieldNames
+ _objc_msgSend$responseDictionary
+ _objc_msgSend$resultWithCompletion:
+ _objc_msgSend$resume
+ _objc_msgSend$resumeMetadata:
+ _objc_msgSend$rootViewModelParseDidBeginWithTag:
+ _objc_msgSend$rootViewModelParseDidEndWithTag:
+ _objc_msgSend$selectedActionIdentifier
+ _objc_msgSend$serverTimeFromDate:
+ _objc_msgSend$serviceWithDefaultShellEndpoint
+ _objc_msgSend$setAccount:
+ _objc_msgSend$setAccountMediaType:
+ _objc_msgSend$setAdditionalHeaders:
+ _objc_msgSend$setAdditionalPlatforms:
+ _objc_msgSend$setAdditionalQueryParams:
+ _objc_msgSend$setAnonymous:
+ _objc_msgSend$setAppCapabilities:
+ _objc_msgSend$setAppDistributionCountryCodeOverride:
+ _objc_msgSend$setBeginEventProcessingBlock:
+ _objc_msgSend$setBundleID:
+ _objc_msgSend$setBundleIdentifiers:
+ _objc_msgSend$setBuyParameters:
+ _objc_msgSend$setCalendar:
+ _objc_msgSend$setClientID:
+ _objc_msgSend$setClientInfo:
+ _objc_msgSend$setCreatesJobs:
+ _objc_msgSend$setDateStyle:
+ _objc_msgSend$setDefaultMediaTypeForCurrentProcess:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setDeviceRebootProcessingBlock:
+ _objc_msgSend$setDialogObserver:
+ _objc_msgSend$setDoesRelativeDateFormatting:
+ _objc_msgSend$setEmitEventProcessingBlock:
+ _objc_msgSend$setEndEventProcessingBlock:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setExtensionsToEnable:
+ _objc_msgSend$setFilter:
+ _objc_msgSend$setFlushDelayEnabled:
+ _objc_msgSend$setForceWatchInstall:
+ _objc_msgSend$setFormatterBehavior:
+ _objc_msgSend$setFormattingContext:
+ _objc_msgSend$setIncludeAccountMatchStatus:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setIsActiveITunesAccountRequired:
+ _objc_msgSend$setIsDSIDLess:
+ _objc_msgSend$setIsRedownload:
+ _objc_msgSend$setIsUpdate:
+ _objc_msgSend$setItemID:
+ _objc_msgSend$setItemIdentifiers:
+ _objc_msgSend$setItemName:
+ _objc_msgSend$setJsVersion:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$setLocalizedDateFormatFromTemplate:
+ _objc_msgSend$setMetricsOverlay:
+ _objc_msgSend$setMinimumFractionDigits:
+ _objc_msgSend$setNumberStyle:
+ _objc_msgSend$setOverlaysLoadTimeout:
+ _objc_msgSend$setOverlaysRateLimitRequestsPerSecond:
+ _objc_msgSend$setOverlaysRateLimitTimeWindow:
+ _objc_msgSend$setPreflightURLString:
+ _objc_msgSend$setRedownloadParams:
+ _objc_msgSend$setStorefrontLocaleID:
+ _objc_msgSend$setSubsystemCategoryFilter:
+ _objc_msgSend$setTimeStyle:
+ _objc_msgSend$setTopic:
+ _objc_msgSend$setUserInitiated:
+ _objc_msgSend$setUsername:
+ _objc_msgSend$setVendorName:
+ _objc_msgSend$sharedManager
+ _objc_msgSend$shrinkFootprintWhenIdle
+ _objc_msgSend$signpostId
+ _objc_msgSend$storeItemIdentifier
+ _objc_msgSend$stringFromByteCount:countStyle:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$stringFromNumber:
+ _objc_msgSend$supportsSecureCoding
+ _objc_msgSend$temporaryDirectory
+ _objc_msgSend$textMetadataWithTitle:subtitle:
+ _objc_msgSend$toDictionary
+ _objc_msgSend$tokenString
+ _objc_msgSend$type
+ _objc_msgSend$underlyingErrors
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$userHasPairedGameController
+ _objc_msgSend$userInfo
+ _objc_msgSend$username
+ _objc_msgSend$valueForEntitlement:
+ _objc_msgSend$valueWithNewObjectInContext:
+ _objc_msgSend$valueWithNullInContext:
+ _objc_msgSend$valueWithObject:inContext:
+ _objc_msgSend$versionIdentifier
+ _objc_msgSend$virtualMachine
+ _objectdestroy.19Tm
+ _objectdestroy.32Tm
+ _symbolic _____Sg s11AnyHashableV
- +[ASCIconOfferMetadata supportsSecureCoding]
- +[ASCOfferMetadata iconMetadataWithImageName:animationName:]
- +[ASCTextOfferMetadata supportsSecureCoding]
- -[ASCAppOffer initWithID:titles:subtitles:flags:ageRating:metrics:baseBuyParams:metricsBuyParams:additionalHeaders:preflightPackageURL:bundleID:itemName:vendorName:capabilities:]
- -[ASCIconOfferMetadata .cxx_destruct]
- -[ASCIconOfferMetadata animationName]
- -[ASCIconOfferMetadata baseImageName]
- -[ASCIconOfferMetadata description]
- -[ASCIconOfferMetadata encodeWithCoder:]
- -[ASCIconOfferMetadata hash]
- -[ASCIconOfferMetadata imageNameForSize:]
- -[ASCIconOfferMetadata initWithBaseImageName:animationName:]
- -[ASCIconOfferMetadata initWithCoder:]
- -[ASCIconOfferMetadata initWithCoder:].cold.1
- -[ASCIconOfferMetadata initWithCoder:].cold.2
- -[ASCIconOfferMetadata isEqual:]
- -[ASCIconOfferMetadata isIcon]
- -[ASCTextOfferMetadata .cxx_destruct]
- -[ASCTextOfferMetadata description]
- -[ASCTextOfferMetadata encodeWithCoder:]
- -[ASCTextOfferMetadata hash]
- -[ASCTextOfferMetadata initWithCoder:]
- -[ASCTextOfferMetadata initWithCoder:].cold.1
- -[ASCTextOfferMetadata initWithTitle:subtitle:]
- -[ASCTextOfferMetadata isEqual:]
- -[ASCTextOfferMetadata isText]
- -[ASCTextOfferMetadata subtitle]
- -[ASCTextOfferMetadata title]
- _OBJC_CLASS_$_ASCIconOfferMetadata
- _OBJC_CLASS_$_ASCTextOfferMetadata
- _OBJC_IVAR_$_ASCIconOfferMetadata._animationName
- _OBJC_IVAR_$_ASCIconOfferMetadata._baseImageName
- _OBJC_IVAR_$_ASCTextOfferMetadata._subtitle
- _OBJC_IVAR_$_ASCTextOfferMetadata._title
- _OBJC_METACLASS_$_ASCIconOfferMetadata
- _OBJC_METACLASS_$_ASCTextOfferMetadata
- __OBJC_$_CLASS_METHODS_ASCIconOfferMetadata
- __OBJC_$_CLASS_METHODS_ASCTextOfferMetadata
- __OBJC_$_INSTANCE_METHODS_ASCIconOfferMetadata
- __OBJC_$_INSTANCE_METHODS_ASCTextOfferMetadata
- __OBJC_$_INSTANCE_VARIABLES_ASCIconOfferMetadata
- __OBJC_$_INSTANCE_VARIABLES_ASCTextOfferMetadata
- __OBJC_$_PROP_LIST_ASCIconOfferMetadata
- __OBJC_$_PROP_LIST_ASCTextOfferMetadata
- __OBJC_CLASS_RO_$_ASCIconOfferMetadata
- __OBJC_CLASS_RO_$_ASCTextOfferMetadata
- __OBJC_METACLASS_RO_$_ASCIconOfferMetadata
- __OBJC_METACLASS_RO_$_ASCTextOfferMetadata
- ___118-[ASCWorkspace(ASCAppLaunchTrampolineWorkspace) openApplicationWithBundleIdentifier:payloadURL:universalLinkRequired:]_block_invoke.cold.2
- ___118-[ASCWorkspace(ASCAppLaunchTrampolineWorkspace) openApplicationWithBundleIdentifier:payloadURL:universalLinkRequired:]_block_invoke.cold.3
- ___118-[ASCWorkspace(ASCAppLaunchTrampolineWorkspace) openApplicationWithBundleIdentifier:payloadURL:universalLinkRequired:]_block_invoke.cold.4
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCompression_$_AppStoreComponentsDaemonKit
- _block_copy_helper.13
- _block_copy_helper.21
- _block_descriptor.15
- _block_descriptor.23
- _block_destroy_helper.14
- _block_destroy_helper.22
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$iconMetadataWithImageName:animationName:
- _objc_msgSend$initWithBaseImageName:animationName:
- _objc_msgSend$initWithID:titles:subtitles:flags:ageRating:metrics:baseBuyParams:metricsBuyParams:additionalHeaders:preflightPackageURL:bundleID:itemName:vendorName:capabilities:
- _objc_msgSend$initWithTitle:subtitle:
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _symbolic Sb8inserted______17memberAfterInsertt 8AppState0A5OfferV5FlagsV
- _symbolic _____y______yptG s23_ContiguousArrayStorageC s11AnyHashableV
CStrings:
+ "@136@0:8@16@24@32q40@48@56@64@72@80@88@96@104@112@120@128"
+ "ASCIconTextOfferMetadata"
+ "Could not decode ASCIconTextOfferMetadata because baseImageName and title were missing"
+ "OfferButton.Title.Resume"
+ "T@\"NSDictionary\",R,C,N,V_metricsOverlay"
+ "TB,R,N,GisIconOnly,V_icon"
+ "TB,R,N,GisTextAndIcon,V_iconAndText"
+ "TB,R,N,GisTextOnly,V_text"
+ "_iconAndText"
+ "_metricsOverlay"
+ "_text"
+ "com.apple.AppSubscriptionsDemo"
+ "com.apple.UnifiedMessagingKitSampleApp"
+ "com.apple.freeform"
+ "iconAndText"
+ "initWithID:titles:subtitles:flags:ageRating:metrics:baseBuyParams:metricsBuyParams:metricsOverlay:additionalHeaders:preflightPackageURL:bundleID:itemName:vendorName:capabilities:"
+ "initWithTitle:subtitle:imageName:animationName:"
+ "isFreeform:"
+ "isIconOnly"
+ "isTextAndIcon"
+ "isTextOnly"
+ "metricsOverlay"
+ "offerMetadataWithTitle:subtitle:imageName:"
+ "resumeMetadata:"
+ "seed"
+ "setMetricsOverlay:"
+ "springboard"
- "@128@0:8@16@24@32q40@48@56@64@72@80@88@96@104@112@120"
- "ASCIconOfferMetadata"
- "ASCTextOfferMetadata"
- "Could not decode ASCIconOfferMetadata because baseImageName was missing"
- "Could not decode ASCTextOfferMetadata because title was missing"
- "TB,R,N,GisIcon"
- "TB,R,N,GisText"
- "iconMetadataWithImageName:animationName:"
- "initWithBaseImageName:animationName:"
- "initWithID:titles:subtitles:flags:ageRating:metrics:baseBuyParams:metricsBuyParams:additionalHeaders:preflightPackageURL:bundleID:itemName:vendorName:capabilities:"
- "initWithTitle:subtitle:"
- "production"

```
