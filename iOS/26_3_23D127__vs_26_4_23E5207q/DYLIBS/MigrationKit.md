## MigrationKit

> `/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit`

```diff

-829.80.170.0.0
-  __TEXT.__text: 0x5ba1cc
-  __TEXT.__auth_stubs: 0x5d30
-  __TEXT.__objc_methlist: 0x6afc
-  __TEXT.__const: 0x2ea08
-  __TEXT.__oslogstring: 0xdd6c
-  __TEXT.__gcc_except_tab: 0x1424
-  __TEXT.__cstring: 0x202a1
-  __TEXT.__constg_swiftt: 0xd804
-  __TEXT.__swift5_typeref: 0xab5d
+1224.100.67.0.0
+  __TEXT.__text: 0x6ddfa4
+  __TEXT.__auth_stubs: 0x5d40
+  __TEXT.__objc_methlist: 0x6b9c
+  __TEXT.__const: 0x2eaa8
+  __TEXT.__oslogstring: 0xe5ec
+  __TEXT.__gcc_except_tab: 0x1494
+  __TEXT.__cstring: 0x1b0a1
+  __TEXT.__constg_swiftt: 0xd88c
+  __TEXT.__swift5_typeref: 0xaacd
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_reflstr: 0xb082
-  __TEXT.__swift5_fieldmd: 0xc4b0
+  __TEXT.__swift5_reflstr: 0xb0f2
+  __TEXT.__swift5_fieldmd: 0xc4ec
   __TEXT.__swift5_assocty: 0x1f10
-  __TEXT.__swift5_proto: 0x2090
+  __TEXT.__swift5_proto: 0x209c
   __TEXT.__swift5_types: 0xba8
-  __TEXT.__swift_as_entry: 0xff0
-  __TEXT.__swift_as_ret: 0x1328
-  __TEXT.__swift5_capture: 0x28a0
+  __TEXT.__swift_as_entry: 0x1018
+  __TEXT.__swift_as_ret: 0x135c
+  __TEXT.__swift5_capture: 0x2890
   __TEXT.__swift5_protos: 0x13c
   __TEXT.__swift5_mpenum: 0xd0
-  __TEXT.__unwind_info: 0x140c0
-  __TEXT.__eh_frame: 0x36834
-  __TEXT.__objc_classname: 0xd99
-  __TEXT.__objc_methname: 0x102ca
-  __TEXT.__objc_methtype: 0x37e4
-  __TEXT.__objc_stubs: 0x9780
-  __DATA_CONST.__got: 0x1a20
-  __DATA_CONST.__const: 0x9e0
-  __DATA_CONST.__objc_classlist: 0xb38
+  __TEXT.__unwind_info: 0x144d0
+  __TEXT.__eh_frame: 0x3820c
+  __TEXT.__objc_classname: 0x3cc1
+  __TEXT.__objc_methname: 0x13266
+  __TEXT.__objc_methtype: 0x43ee
+  __TEXT.__objc_stubs: 0xf5a0
+  __DATA_CONST.__got: 0x1a68
+  __DATA_CONST.__const: 0xa10
+  __DATA_CONST.__objc_classlist: 0xb40
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4970
+  __DATA_CONST.__objc_selrefs: 0x4a00
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x308
   __DATA_CONST.__objc_arraydata: 0x488
-  __AUTH_CONST.__auth_got: 0x2eb0
-  __AUTH_CONST.__const: 0x14df8
-  __AUTH_CONST.__cfstring: 0x5180
-  __AUTH_CONST.__objc_const: 0x197e8
+  __AUTH_CONST.__auth_got: 0x2eb8
+  __AUTH_CONST.__const: 0x14cf0
+  __AUTH_CONST.__cfstring: 0x5920
+  __AUTH_CONST.__objc_const: 0x19950
   __AUTH_CONST.__objc_intobj: 0xcc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x210
-  __AUTH.__objc_data: 0x7360
-  __AUTH.__data: 0x14ad8
+  __AUTH.__objc_data: 0x73b8
+  __AUTH.__data: 0x14b50
   __DATA.__objc_ivar: 0x790
-  __DATA.__data: 0xc6b8
-  __DATA.__bss: 0x39410
-  __DATA.__common: 0x1470
+  __DATA.__data: 0xc738
+  __DATA.__bss: 0x395c0
+  __DATA.__common: 0x14a8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftSystem.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A14F2132-61CE-3D81-BBB7-A5F0F5A4D0C9
-  Functions: 21393
-  Symbols:   13942
-  CStrings:  9645
+  UUID: E37AC75D-BD2F-3384-B731-244B35BF41B5
+  Functions: 21394
+  Symbols:   14977
+  CStrings:  9737
 
Symbols:
+ +[MKUSBRoleSwap configureNCM]
+ +[MKUSBRoleSwap destroyHPMLibInterface:]
+ +[MKUSBRoleSwap disableDeviceModeAndNCM]
+ +[MKUSBRoleSwap enableDeviceModeAndNCM]
+ +[MKUSBRoleSwap getCurrentUSBDataRole]
+ +[MKUSBRoleSwap getDeviceAddressFromHPMService:]
+ +[MKUSBRoleSwap getHPMLibInterface:]
+ +[MKUSBRoleSwap isUSBConnected]
+ +[MKUSBRoleSwap restorePreviousUSBConfiguration]
+ +[MKUSBRoleSwap setUSBDeviceModeAndNCM:error:]
+ _CFGetTypeID
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryGetChildIterator
+ _IOServiceGetMatchingServices
+ _NSLog
+ _OBJC_CLASS_$_CWFActivity
+ _OBJC_CLASS_$_MKUSBRoleSwap
+ _OBJC_METACLASS_$_MKUSBRoleSwap
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_CLASS_METHODS_MKUSBRoleSwap
+ __OBJC_CLASS_RO_$_MKUSBRoleSwap
+ __OBJC_METACLASS_RO_$_MKUSBRoleSwap
+ __PROTOCOLS__TtC12MigrationKit27AppPlaceholderPromotionInfo.31
+ __ZL13_hpmInterface
+ __ZL14_deviceAddress
+ __ZL14_usbController
+ __ZL16_didConfigureNCM
+ __ZL19_didPerformRoleSwap
+ __ZL20_previousDescription
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB9foe210106ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9foe210106EPKvm
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB9foe210106ERKS6_S9_
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SD_SH_SF_Lb1EEENS5_ISD_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SD_SH_SF_Lb1EEENS5_ISD_EEE13__move_assignERSM_NS_17integral_constantIbLb1EEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SD_SH_SF_Lb1EEENS5_ISD_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS9_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SD_SH_SF_Lb1EEENS5_ISD_EEE21__construct_node_hashIRKSD_JEEENS_10unique_ptrINS_11__hash_nodeIS9_PvEENS_22__hash_node_destructorINS5_IST_EEEEEEmOT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SD_SH_SF_Lb1EEENS5_ISD_EEE25__emplace_unique_key_argsIS7_JRKSD_EEENSB_INS_15__hash_iteratorIPNS_11__hash_nodeIS9_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SD_SH_SF_Lb1EEENS5_ISD_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SD_SH_SF_Lb1EEENS5_ISD_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S8_EENS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SD_SH_SF_Lb1EEENS5_ISD_EEED2Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe210106ILi0EEEPKc
+ __ZNSt3__113unordered_mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigNS_4hashIS6_EENS_8equal_toIS6_EENS4_INS_4pairIKS6_S7_EEEEED1B9foe210106Ev
+ __ZNSt3__117__call_once_proxyB9foe210106INS_5tupleIJOZN12migrationkit9signature14get_identifierEPKhmE3$_0EEEEEvPv
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B9foe210106EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B9foe210106EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B9foe210106EPKcm
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE3sigEEPvEEEEEclB9foe210106EPSC_
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ ___swift_assign_boxed_opaque_existential_1
+ ___swift_get_extra_inhabitant_index.118Tm
+ ___swift_get_extra_inhabitant_index.197Tm
+ ___swift_get_extra_inhabitant_index.48Tm
+ ___swift_store_extra_inhabitant_index.119Tm
+ ___swift_store_extra_inhabitant_index.198Tm
+ ___swift_store_extra_inhabitant_index.49Tm
+ _block_copy_helper.26
+ _block_copy_helper.44
+ _block_copy_helper.80
+ _block_descriptor.28
+ _block_descriptor.46
+ _block_descriptor.82
+ _block_destroy_helper.27
+ _block_destroy_helper.45
+ _block_destroy_helper.81
+ _get_type_metadata 15Synchronization6AtomicVySbG noncopyable.2
+ _kCFAllocatorSystemDefault
+ _objc_exception_rethrow
+ _objc_msgSend$BSSID
+ _objc_msgSend$CGImage
+ _objc_msgSend$CGRectValue
+ _objc_msgSend$SSID
+ _objc_msgSend$URL
+ _objc_msgSend$URLWithSize:
+ _objc_msgSend$UUIDWithString:
+ _objc_msgSend$__systemImageNamedSwift:
+ _objc_msgSend$absoluteDate
+ _objc_msgSend$accountIdentifier
+ _objc_msgSend$accountNumberSuffix
+ _objc_msgSend$accountWithIdentifier:error:
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$actionType
+ _objc_msgSend$actionWithTitle:style:handler:
+ _objc_msgSend$activateConstraints:
+ _objc_msgSend$activateWithCompletion:
+ _objc_msgSend$activityType
+ _objc_msgSend$activityWithType:reason:
+ _objc_msgSend$addAction:
+ _objc_msgSend$addAction:forControlEvents:
+ _objc_msgSend$addAttachment:
+ _objc_msgSend$addButton:
+ _objc_msgSend$addEntry:
+ _objc_msgSend$addGestureRecognizer:
+ _objc_msgSend$addInput:
+ _objc_msgSend$addObserver:
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$addOutput:
+ _objc_msgSend$addRecurrenceRule:
+ _objc_msgSend$addResourceWithType:fileURL:options:
+ _objc_msgSend$addSublayer:
+ _objc_msgSend$addSubview:
+ _objc_msgSend$addTarget:action:forControlEvents:
+ _objc_msgSend$addWithClient:
+ _objc_msgSend$alarms
+ _objc_msgSend$alertControllerWithTitle:message:preferredStyle:
+ _objc_msgSend$allHeaderFields
+ _objc_msgSend$appLibraryCollectionForProviderDomain:
+ _objc_msgSend$appTags
+ _objc_msgSend$applicationExtensionRecords
+ _objc_msgSend$applyPackage:
+ _objc_msgSend$assetId
+ _objc_msgSend$assetLocalIdentifier
+ _objc_msgSend$assetProperty:
+ _objc_msgSend$assetResourcesForAsset:
+ _objc_msgSend$associateWithParameters:reply:
+ _objc_msgSend$attachProgressCallBack:
+ _objc_msgSend$attendees
+ _objc_msgSend$attestKey:clientDataHash:completionHandler:
+ _objc_msgSend$audioBalance
+ _objc_msgSend$audioDescription
+ _objc_msgSend$autoRotateScreen
+ _objc_msgSend$availability
+ _objc_msgSend$backgroundColor
+ _objc_msgSend$backgroundColorVideoOverride
+ _objc_msgSend$backgroundOpacity
+ _objc_msgSend$backgroundOpacityVideoOverride
+ _objc_msgSend$bagSubProfile
+ _objc_msgSend$bagSubProfileVersion
+ _objc_msgSend$batchedEventsMatchingPredicate:batchSize:error:handler:
+ _objc_msgSend$becomeFirstResponder
+ _objc_msgSend$beginActivity:error:
+ _objc_msgSend$birthday
+ _objc_msgSend$blueYellowFilter
+ _objc_msgSend$bluetoothUUID
+ _objc_msgSend$boldButton
+ _objc_msgSend$boldText
+ _objc_msgSend$bottomAnchor
+ _objc_msgSend$bounds
+ _objc_msgSend$bundleContainerURL
+ _objc_msgSend$bundleName
+ _objc_msgSend$burstIdentifier
+ _objc_msgSend$buttonTray
+ _objc_msgSend$buttonWithType:
+ _objc_msgSend$buyParameters
+ _objc_msgSend$calendarForEntityType:eventStore:
+ _objc_msgSend$calendarIdentifier
+ _objc_msgSend$calendarWithIdentifier:
+ _objc_msgSend$calendarsForEntityType:
+ _objc_msgSend$callStatus
+ _objc_msgSend$callsWithPredicate:limit:offset:batchSize:
+ _objc_msgSend$canEvaluatePolicy:error:
+ _objc_msgSend$cancelDiscovery
+ _objc_msgSend$cancelsPurchaseBatch
+ _objc_msgSend$capabilities
+ _objc_msgSend$captionStyleName
+ _objc_msgSend$captionStyles
+ _objc_msgSend$cardholder
+ _objc_msgSend$cbUUID
+ _objc_msgSend$cellForRowAtIndexPath:
+ _objc_msgSend$centerXAnchor
+ _objc_msgSend$centerYAnchor
+ _objc_msgSend$channel
+ _objc_msgSend$city
+ _objc_msgSend$cleanBluetooth
+ _objc_msgSend$clearColor
+ _objc_msgSend$closeAndReturnError:
+ _objc_msgSend$color
+ _objc_msgSend$colorString
+ _objc_msgSend$colorVideoOverride
+ _objc_msgSend$complete
+ _objc_msgSend$configureNCM
+ _objc_msgSend$confirmSelectionWithSelections:disabledBundleIDs:
+ _objc_msgSend$connectWithCode:
+ _objc_msgSend$connectedInterfaceName
+ _objc_msgSend$constraintEqualToAnchor:
+ _objc_msgSend$constraintEqualToAnchor:constant:
+ _objc_msgSend$constraintEqualToConstant:
+ _objc_msgSend$contactRelations
+ _objc_msgSend$containersMatchingPredicate:error:
+ _objc_msgSend$contentView
+ _objc_msgSend$contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:
+ _objc_msgSend$coordinate
+ _objc_msgSend$copyItemAtPath:toPath:error:
+ _objc_msgSend$copySharedDeviceManager
+ _objc_msgSend$country
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$createSymbolicLinkAtURL:withDestinationURL:error:
+ _objc_msgSend$creationDate
+ _objc_msgSend$creationRequestForAssetFromScreenshotImage:
+ _objc_msgSend$creationRequestForAssetWithOptions:
+ _objc_msgSend$creationRequestForAssetWithUUID:options:
+ _objc_msgSend$currentDeviceCapabilities
+ _objc_msgSend$currentEstimates
+ _objc_msgSend$currentKnownNetworkProfile
+ _objc_msgSend$cvv
+ _objc_msgSend$darkMode
+ _objc_msgSend$dataImportPromisesWithError:
+ _objc_msgSend$dataTaskPromiseWithRequest:
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$dates
+ _objc_msgSend$day
+ _objc_msgSend$dayOfTheWeek
+ _objc_msgSend$dayOfWeek:weekNumber:
+ _objc_msgSend$daysOfTheMonth
+ _objc_msgSend$daysOfTheWeek
+ _objc_msgSend$daysOfTheYear
+ _objc_msgSend$debugDescription
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$defaultDeviceWithMediaType:
+ _objc_msgSend$defaultSessionConfiguration
+ _objc_msgSend$defaultWorkspace
+ _objc_msgSend$departmentName
+ _objc_msgSend$dequeueReusableCellWithIdentifier:forIndexPath:
+ _objc_msgSend$deselectRowAtIndexPath:animated:
+ _objc_msgSend$destroyHPMLibInterface:
+ _objc_msgSend$directionalLayoutMargins
+ _objc_msgSend$disableDevice:
+ _objc_msgSend$disableDeviceModeAndNCM
+ _objc_msgSend$disassociateWithReason:
+ _objc_msgSend$dismissViewControllerAnimated:completion:
+ _objc_msgSend$distributorID
+ _objc_msgSend$distributorInfo
+ _objc_msgSend$distributorType
+ _objc_msgSend$documentsURL
+ _objc_msgSend$domainIdentifier
+ _objc_msgSend$emailAddresses
+ _objc_msgSend$enableDeviceModeAndNCM
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$endActivity:
+ _objc_msgSend$endDate
+ _objc_msgSend$endEditing:
+ _objc_msgSend$enhanced
+ _objc_msgSend$entries
+ _objc_msgSend$entriesForContact:
+ _objc_msgSend$enumerateContactsWithFetchRequest:error:usingBlock:
+ _objc_msgSend$enumerateCoordinatorsWithError:usingBlock:
+ _objc_msgSend$enumeratorWithOptions:
+ _objc_msgSend$estimatedLibrarySizeForOsMigration
+ _objc_msgSend$evaluatePolicy:localizedReason:reply:
+ _objc_msgSend$evaluateWithObject:
+ _objc_msgSend$eventIDWithType:interfaceName:
+ _objc_msgSend$eventIdentifier
+ _objc_msgSend$eventWithEventStore:
+ _objc_msgSend$eventWithIdentifier:
+ _objc_msgSend$expectedTimeRemaining
+ _objc_msgSend$expiration
+ _objc_msgSend$export
+ _objc_msgSend$exportAlarms
+ _objc_msgSend$exportWiFiNetworks
+ _objc_msgSend$exportableCardEntry:completion:
+ _objc_msgSend$exportableManifestWithCompletion:
+ _objc_msgSend$extensionPointRecord
+ _objc_msgSend$extent
+ _objc_msgSend$externalID
+ _objc_msgSend$familyName
+ _objc_msgSend$fetchAppContentListWithCompletionHandler:
+ _objc_msgSend$fetchAssetCollectionsContainingAsset:withType:options:
+ _objc_msgSend$fetchAssetCollectionsWithLocalIdentifiers:options:
+ _objc_msgSend$fetchAssetsForOsMigrationWithOptions:
+ _objc_msgSend$fetchHomeScreenWallpaperForOrientation:completion:
+ _objc_msgSend$fetchLockScreenWallpaperForOrientation:completion:
+ _objc_msgSend$fetchRecordingMetadataWithUUID:completionBlock:
+ _objc_msgSend$fetchURLForItem:completionHandler:
+ _objc_msgSend$fileHandleForReading
+ _objc_msgSend$fileHandleForWriting
+ _objc_msgSend$fileHandleForWritingToURL:error:
+ _objc_msgSend$fileName
+ _objc_msgSend$fileSize
+ _objc_msgSend$fileURL
+ _objc_msgSend$filterWithName:
+ _objc_msgSend$firstDayOfTheWeek
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$firstViewController:
+ _objc_msgSend$flashForAlerts
+ _objc_msgSend$flowWithOptions:
+ _objc_msgSend$fontName
+ _objc_msgSend$fpan
+ _objc_msgSend$fractionCompleted
+ _objc_msgSend$frame
+ _objc_msgSend$frequency
+ _objc_msgSend$generateAssertion:clientDataHash:completionHandler:
+ _objc_msgSend$generateKeyWithCompletionHandler:
+ _objc_msgSend$generatePackage
+ _objc_msgSend$getCurrentUSBDataRole
+ _objc_msgSend$getDeviceAddressFromHPMService:
+ _objc_msgSend$getHPMLibInterface:
+ _objc_msgSend$getHasDataImportPromises:error:
+ _objc_msgSend$getLocalFileUrl
+ _objc_msgSend$getPostProcessingShouldBegin:error:
+ _objc_msgSend$givenName
+ _objc_msgSend$grayscaleFilter
+ _objc_msgSend$greenRedFilter
+ _objc_msgSend$hasAttachment
+ _objc_msgSend$hasBytesAvailable
+ _objc_msgSend$headerView
+ _objc_msgSend$heightAnchor
+ _objc_msgSend$hiddenState
+ _objc_msgSend$hidesBusyIndicator
+ _objc_msgSend$homeDirectoryForCurrentUser
+ _objc_msgSend$imageByApplyingTransform:
+ _objc_msgSend$imageData
+ _objc_msgSend$imageForDescriptor:
+ _objc_msgSend$imageNamed:
+ _objc_msgSend$importFileWithURL:withMeta:completionHandler:
+ _objc_msgSend$importWiFiNetworks:error:
+ _objc_msgSend$importWithMKAlarm:completionHandler:
+ _objc_msgSend$initRecurrenceWithFrequency:interval:daysOfTheWeek:daysOfTheMonth:monthsOfTheYear:weeksOfTheYear:daysOfTheYear:setPositions:end:
+ _objc_msgSend$initWithAbsoluteDate:
+ _objc_msgSend$initWithActivityIndicatorStyle:
+ _objc_msgSend$initWithArrangedSubviews:
+ _objc_msgSend$initWithBarButtonSystemItem:target:action:
+ _objc_msgSend$initWithBool:
+ _objc_msgSend$initWithBundleID:
+ _objc_msgSend$initWithBundleID:selfPairingName:peerDeviceName:storageClass:lifetime:pairingClient:
+ _objc_msgSend$initWithCGImage:
+ _objc_msgSend$initWithCIImage:scale:orientation:
+ _objc_msgSend$initWithClientIdentifier:bag:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithConfiguration:
+ _objc_msgSend$initWithContact:propertyKey:labeledValueIdentifier:actionType:bundleIdentifier:store:
+ _objc_msgSend$initWithContentsOfFile:
+ _objc_msgSend$initWithCustomView:
+ _objc_msgSend$initWithDelegate:queue:
+ _objc_msgSend$initWithDevice:error:
+ _objc_msgSend$initWithDevice:previewLayer:
+ _objc_msgSend$initWithDeviceIdentifier:delegate:queue:
+ _objc_msgSend$initWithDiscoveryResult:serviceType:serviceSpecificInfo:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithEndDate:
+ _objc_msgSend$initWithExplanation:
+ _objc_msgSend$initWithFilepath:
+ _objc_msgSend$initWithFloat:
+ _objc_msgSend$initWithFrame:
+ _objc_msgSend$initWithFrame:style:
+ _objc_msgSend$initWithIdentifier:pairingCriteria:metadata:queue:
+ _objc_msgSend$initWithImage:
+ _objc_msgSend$initWithInt:
+ _objc_msgSend$initWithKey:ascending:
+ _objc_msgSend$initWithKeysToFetch:
+ _objc_msgSend$initWithLabel:value:
+ _objc_msgSend$initWithLatitude:longitude:
+ _objc_msgSend$initWithMachServiceName:forClients:delegate:
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$initWithName:
+ _objc_msgSend$initWithNavigationBarClass:toolbarClass:
+ _objc_msgSend$initWithNibName:bundle:
+ _objc_msgSend$initWithOccurrenceCount:
+ _objc_msgSend$initWithPairingConfiguration:usingPairingDelegate:usingPairingPassphrase:
+ _objc_msgSend$initWithPattern:options:error:
+ _objc_msgSend$initWithPredicate:context:allowLaunch:
+ _objc_msgSend$initWithProtocolType:servicePort:
+ _objc_msgSend$initWithReason:containerTypes:
+ _objc_msgSend$initWithRelativeOffset:
+ _objc_msgSend$initWithRootViewController:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$initWithServiceType:securityConfiguration:connectionMode:
+ _objc_msgSend$initWithSession:
+ _objc_msgSend$initWithSize:scale:
+ _objc_msgSend$initWithStringValue:
+ _objc_msgSend$initWithSupportedPairSetupMethods:pairingCachingEnabled:
+ _objc_msgSend$initWithTarget:action:
+ _objc_msgSend$initWithTitle:detailText:icon:contentLayout:
+ _objc_msgSend$initWithTitle:detailText:symbolName:contentLayout:
+ _objc_msgSend$initWithTokenService:
+ _objc_msgSend$initWithTokenService:bag:
+ _objc_msgSend$initWithURL:
+ _objc_msgSend$initWithUrlString:username:userIdentifier:service:
+ _objc_msgSend$installType
+ _objc_msgSend$interfaceName
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$interval
+ _objc_msgSend$ipv6LinkLocalAddress
+ _objc_msgSend$is2GHz
+ _objc_msgSend$is5GHz
+ _objc_msgSend$is6GHz
+ _objc_msgSend$isAllDay
+ _objc_msgSend$isBeta
+ _objc_msgSend$isCloudPhotoLibraryEnabled
+ _objc_msgSend$isComplete
+ _objc_msgSend$isEnumeratingDirectoryPostOrder
+ _objc_msgSend$isFavorite
+ _objc_msgSend$isFeatureAvailable
+ _objc_msgSend$isFeatureEnabled
+ _objc_msgSend$isFeatureSupported
+ _objc_msgSend$isHidden
+ _objc_msgSend$isImmutable
+ _objc_msgSend$isInCloud
+ _objc_msgSend$isLaunchProhibited
+ _objc_msgSend$isLocallyAvailable
+ _objc_msgSend$isOpen
+ _objc_msgSend$isPlaceholder
+ _objc_msgSend$isProximitySetupToNewDeviceAllowed
+ _objc_msgSend$isSubscribed
+ _objc_msgSend$isTrashed
+ _objc_msgSend$isUSBConnected
+ _objc_msgSend$isVideoRotationAngleSupported:
+ _objc_msgSend$isoCountryCode
+ _objc_msgSend$items
+ _objc_msgSend$jobTitle
+ _objc_msgSend$lastModifiedDate
+ _objc_msgSend$layer
+ _objc_msgSend$layoutIfNeeded
+ _objc_msgSend$leadingAnchor
+ _objc_msgSend$linkButton
+ _objc_msgSend$listOfMonitoredApps
+ _objc_msgSend$liveCaptions
+ _objc_msgSend$liveTranscribe
+ _objc_msgSend$localInterfaceIndex
+ _objc_msgSend$localRelativePath
+ _objc_msgSend$localURL
+ _objc_msgSend$localizedName
+ _objc_msgSend$localizedOrganization
+ _objc_msgSend$localizedShortName
+ _objc_msgSend$localizedTitle
+ _objc_msgSend$location
+ _objc_msgSend$mainICloudDriveDomainID
+ _objc_msgSend$managementDomain
+ _objc_msgSend$mediaSubtypes
+ _objc_msgSend$metadataForBundleContainerURL:error:
+ _objc_msgSend$middleName
+ _objc_msgSend$migrationDidComplete:zoomEnabled:
+ _objc_msgSend$migrationDidReset
+ _objc_msgSend$mk_setMigrationUserAgent
+ _objc_msgSend$modificationDate
+ _objc_msgSend$monoAudio
+ _objc_msgSend$month
+ _objc_msgSend$monthsOfTheYear
+ _objc_msgSend$namePrefix
+ _objc_msgSend$nameSuffix
+ _objc_msgSend$navigationController
+ _objc_msgSend$navigationItem
+ _objc_msgSend$newDeviceIdentifierWithBluetoothUUID:
+ _objc_msgSend$nextObject
+ _objc_msgSend$nickname
+ _objc_msgSend$note
+ _objc_msgSend$notes
+ _objc_msgSend$notificationOccurred:
+ _objc_msgSend$occurrenceCount
+ _objc_msgSend$occurrenceDate
+ _objc_msgSend$openSensitiveURL:withOptions:
+ _objc_msgSend$openURL:configuration:error:
+ _objc_msgSend$openURL:options:completionHandler:
+ _objc_msgSend$options
+ _objc_msgSend$organizationName
+ _objc_msgSend$organizer
+ _objc_msgSend$outputImage
+ _objc_msgSend$parentAccount
+ _objc_msgSend$participantRole
+ _objc_msgSend$participantStatus
+ _objc_msgSend$participantType
+ _objc_msgSend$passwordForKnownNetworkProfile:error:
+ _objc_msgSend$pauseBackgroundActivity
+ _objc_msgSend$paymentDetails
+ _objc_msgSend$peerSupportedSelectionsWithCompletionHandler:
+ _objc_msgSend$performScanWithParameters:reply:
+ _objc_msgSend$phoneNumbers
+ _objc_msgSend$phoneticFamilyName
+ _objc_msgSend$phoneticGivenName
+ _objc_msgSend$phoneticMiddleName
+ _objc_msgSend$phoneticOrganizationName
+ _objc_msgSend$pixelHeight
+ _objc_msgSend$pixelWidth
+ _objc_msgSend$placeholderForCreatedAssetCollection
+ _objc_msgSend$popToViewController:animated:
+ _objc_msgSend$postalAddresses
+ _objc_msgSend$postalCode
+ _objc_msgSend$powerButtonEndsCall
+ _objc_msgSend$predicateForContactsInContainerWithIdentifier:
+ _objc_msgSend$predicateForContactsMatchingExternalUUIDs:
+ _objc_msgSend$predicateForMasterEventsInCalendar:
+ _objc_msgSend$predicateMatchingBundleIdentifier:
+ _objc_msgSend$preferCaptionsSDH
+ _objc_msgSend$preferredFontForTextStyle:
+ _objc_msgSend$preflightSelectionWithSelections:completionHandler:
+ _objc_msgSend$prepare
+ _objc_msgSend$presentViewController:animated:completion:
+ _objc_msgSend$presentationController
+ _objc_msgSend$previousFamilyName
+ _objc_msgSend$prioritizeCoordinatorForAppWithIdentity:completion:
+ _objc_msgSend$privateFileURL
+ _objc_msgSend$processExists
+ _objc_msgSend$processWithData:completionHandler:
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$providerDisplayName
+ _objc_msgSend$providerDomainForURL:error:
+ _objc_msgSend$providerDomainWithID:cachePolicy:error:
+ _objc_msgSend$pushViewController:animated:
+ _objc_msgSend$queryMetaDataSync
+ _objc_msgSend$rangeAtIndex:
+ _objc_msgSend$read
+ _objc_msgSend$readDataToEndOfFile
+ _objc_msgSend$recurrenceEnd
+ _objc_msgSend$recurrenceRules
+ _objc_msgSend$redGreenFilter
+ _objc_msgSend$refreshContainersWithOptions:forApplicationIdentity:error:
+ _objc_msgSend$registerClass:forCellReuseIdentifier:
+ _objc_msgSend$registerDevice:properties:operationalproperties:queue:completionBlock:
+ _objc_msgSend$registerFilesystemBarrierAtURL:error:
+ _objc_msgSend$relativeOffset
+ _objc_msgSend$reloadData
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$remoteParticipantHandles
+ _objc_msgSend$removeFromSuperview
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$removeWithCancelled:
+ _objc_msgSend$requestWithComponents:
+ _objc_msgSend$resetLockScreenWallpapersToImageAtURL:completion:
+ _objc_msgSend$resetLockScreenWallpapersToImageAtURL:homeScreenWallpaper:completion:
+ _objc_msgSend$resignFirstResponder
+ _objc_msgSend$restorePreviousUSBConfiguration
+ _objc_msgSend$results
+ _objc_msgSend$resume
+ _objc_msgSend$resumeBackgroundActivity
+ _objc_msgSend$rootURLForProviderDomainID:cachePolicy:error:
+ _objc_msgSend$runWithClient:scheme:
+ _objc_msgSend$sanitizedPKPassArchive
+ _objc_msgSend$save
+ _objc_msgSend$saveCalendar:commit:error:
+ _objc_msgSend$saveEvent:span:commit:error:
+ _objc_msgSend$scale
+ _objc_msgSend$scanForPeripheralsWithServices:options:completion:
+ _objc_msgSend$screen
+ _objc_msgSend$screenReader
+ _objc_msgSend$screenReaderSpeechRate
+ _objc_msgSend$secondarySystemBackgroundColor
+ _objc_msgSend$sendNotificationWithData:completionHandler:
+ _objc_msgSend$sendWithData:completionHandler:
+ _objc_msgSend$service
+ _objc_msgSend$servicePort
+ _objc_msgSend$serviceProvider
+ _objc_msgSend$sessionWithConfiguration:
+ _objc_msgSend$setAccountID:
+ _objc_msgSend$setAllDay:
+ _objc_msgSend$setAllowRefreshDuringPostProcessing:
+ _objc_msgSend$setAllowedLinkSubtypes:
+ _objc_msgSend$setAllowedLinkTypes:
+ _objc_msgSend$setAllowsCellularAccess:
+ _objc_msgSend$setAllowsExpensiveAccess:
+ _objc_msgSend$setAlpha:
+ _objc_msgSend$setAppExtensionPlaceholderPromises:error:
+ _objc_msgSend$setAttributes:ofItemAtPath:error:
+ _objc_msgSend$setAudioBalance:
+ _objc_msgSend$setAudioDescription:
+ _objc_msgSend$setAuthenticationType:
+ _objc_msgSend$setAutoRotateScreen:
+ _objc_msgSend$setAutocapitalizationType:
+ _objc_msgSend$setAutocorrectionType:
+ _objc_msgSend$setAvailability:
+ _objc_msgSend$setAxis:
+ _objc_msgSend$setBackgroundColor:
+ _objc_msgSend$setBackgroundColorVideoOverride:
+ _objc_msgSend$setBackgroundOpacity:
+ _objc_msgSend$setBackgroundOpacityVideoOverride:
+ _objc_msgSend$setBirthday:
+ _objc_msgSend$setBlueYellowFilter:
+ _objc_msgSend$setBluetoothRole:
+ _objc_msgSend$setBoldText:
+ _objc_msgSend$setBundleVersion:
+ _objc_msgSend$setCanUseLocalCacheServer:
+ _objc_msgSend$setCancelsTouchesInView:
+ _objc_msgSend$setCandidateDiscoveredHandler:
+ _objc_msgSend$setCandidateLostHandler:
+ _objc_msgSend$setCaptionStyleName:
+ _objc_msgSend$setCaptionStyles:
+ _objc_msgSend$setCaptionText:
+ _objc_msgSend$setCity:
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setColor:
+ _objc_msgSend$setColorString:
+ _objc_msgSend$setColorVideoOverride:
+ _objc_msgSend$setCompletionHandler:
+ _objc_msgSend$setConnectionMode:
+ _objc_msgSend$setContactRelations:
+ _objc_msgSend$setContentMode:
+ _objc_msgSend$setCornerRadius:
+ _objc_msgSend$setCountry:
+ _objc_msgSend$setCreationDate:
+ _objc_msgSend$setDarkMode:
+ _objc_msgSend$setDataImportPromises:error:
+ _objc_msgSend$setDataSource:
+ _objc_msgSend$setDatapathConfiguration:
+ _objc_msgSend$setDates:
+ _objc_msgSend$setDepartmentName:
+ _objc_msgSend$setDeviceType:
+ _objc_msgSend$setDiscretionary:
+ _objc_msgSend$setDistribution:
+ _objc_msgSend$setDistributorID:
+ _objc_msgSend$setDistributorInfo:
+ _objc_msgSend$setDomain:
+ _objc_msgSend$setEmailAddresses:
+ _objc_msgSend$setEndDate:
+ _objc_msgSend$setEndTimeZone:
+ _objc_msgSend$setEventHandler:eventID:
+ _objc_msgSend$setExAppExtensionAttributes:
+ _objc_msgSend$setExternalUUID:
+ _objc_msgSend$setFamilyName:
+ _objc_msgSend$setFilter:
+ _objc_msgSend$setFlashForAlerts:
+ _objc_msgSend$setFont:
+ _objc_msgSend$setFontName:
+ _objc_msgSend$setFormatOptions:
+ _objc_msgSend$setFrame:
+ _objc_msgSend$setGivenName:
+ _objc_msgSend$setGrayscaleFilter:
+ _objc_msgSend$setGreenRedFilter:
+ _objc_msgSend$setHidesBackButton:animated:
+ _objc_msgSend$setImageData:
+ _objc_msgSend$setIncludeAllBurstAssets:
+ _objc_msgSend$setIncludeAssetSourceTypes:
+ _objc_msgSend$setIncludeHiddenAssets:
+ _objc_msgSend$setIncludesApproximationPhrase:
+ _objc_msgSend$setIncludesTimeRemainingPhrase:
+ _objc_msgSend$setInterface:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setIsExternalPairing:
+ _objc_msgSend$setJobTitle:
+ _objc_msgSend$setKeyboardType:
+ _objc_msgSend$setLastModifiedDate:
+ _objc_msgSend$setLayoutMargins:
+ _objc_msgSend$setLayoutMarginsRelativeArrangement:
+ _objc_msgSend$setLeftBarButtonItem:
+ _objc_msgSend$setLiveCaptions:
+ _objc_msgSend$setLiveTranscribe:
+ _objc_msgSend$setLocalizedDistributorName:
+ _objc_msgSend$setLocation:
+ _objc_msgSend$setMarketplaceDomain:
+ _objc_msgSend$setMarketplaceItemID:
+ _objc_msgSend$setMasksToBounds:
+ _objc_msgSend$setMaximumTerminationResistance:
+ _objc_msgSend$setMetadataObjectTypes:
+ _objc_msgSend$setMetadataObjectsDelegate:queue:
+ _objc_msgSend$setMiddleName:
+ _objc_msgSend$setModalPresentationStyle:
+ _objc_msgSend$setModificationDate:
+ _objc_msgSend$setMonoAudio:
+ _objc_msgSend$setNamePrefix:
+ _objc_msgSend$setNameSuffix:
+ _objc_msgSend$setNickname:
+ _objc_msgSend$setNote:
+ _objc_msgSend$setNotes:
+ _objc_msgSend$setNumberOfLines:
+ _objc_msgSend$setObserver:
+ _objc_msgSend$setOrganizationName:
+ _objc_msgSend$setOutOfBandKey:
+ _objc_msgSend$setPairingDelegate:
+ _objc_msgSend$setPairingMetadata:
+ _objc_msgSend$setPairingMethod:
+ _objc_msgSend$setPairingTransport:
+ _objc_msgSend$setParentPlaceholder:
+ _objc_msgSend$setPercentComplete:
+ _objc_msgSend$setPhoneNumbers:
+ _objc_msgSend$setPhoneticFamilyName:
+ _objc_msgSend$setPhoneticGivenName:
+ _objc_msgSend$setPhoneticMiddleName:
+ _objc_msgSend$setPhoneticOrganizationName:
+ _objc_msgSend$setPlaceholderAttributes:error:
+ _objc_msgSend$setPositions
+ _objc_msgSend$setPostalAddresses:
+ _objc_msgSend$setPostalCode:
+ _objc_msgSend$setPowerButtonEndsCall:
+ _objc_msgSend$setPreferCaptionsSDH:
+ _objc_msgSend$setPreferredMaxLayoutWidth:
+ _objc_msgSend$setPreviousFamilyName:
+ _objc_msgSend$setProgressText:
+ _objc_msgSend$setProtocolHandler:
+ _objc_msgSend$setPsm:
+ _objc_msgSend$setRedGreenFilter:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setReportType:
+ _objc_msgSend$setRequestEncoding:
+ _objc_msgSend$setResetHandler:
+ _objc_msgSend$setReturnKeyType:
+ _objc_msgSend$setRightBarButtonItem:
+ _objc_msgSend$setSSID:
+ _objc_msgSend$setScanResult:
+ _objc_msgSend$setScreenReader:
+ _objc_msgSend$setSelectionStyle:
+ _objc_msgSend$setServiceSpecificInfo:
+ _objc_msgSend$setSession:
+ _objc_msgSend$setShouldCreateScreenshot:
+ _objc_msgSend$setShouldMoveFile:
+ _objc_msgSend$setSocialProfiles:
+ _objc_msgSend$setSoftwareVersionExternalIdentifier:
+ _objc_msgSend$setSortDescriptors:
+ _objc_msgSend$setSource:
+ _objc_msgSend$setSpeakSelection:
+ _objc_msgSend$setStartDate:
+ _objc_msgSend$setStartTimeZone:
+ _objc_msgSend$setStatus:
+ _objc_msgSend$setStreet:
+ _objc_msgSend$setTableView:
+ _objc_msgSend$setText:
+ _objc_msgSend$setTextAlignment:
+ _objc_msgSend$setTextColor:
+ _objc_msgSend$setTextEdgeStyle:
+ _objc_msgSend$setTextEdgeStyleVideoOverride:
+ _objc_msgSend$setTextHighlightColor:
+ _objc_msgSend$setTextHighlightOpacity:
+ _objc_msgSend$setTextHighlightOpacityVideoOverride:
+ _objc_msgSend$setTextOpacity:
+ _objc_msgSend$setTextOpacityVideoOverride:
+ _objc_msgSend$setTextSize:
+ _objc_msgSend$setTimeoutIntervalForResource:
+ _objc_msgSend$setTintColor:
+ _objc_msgSend$setTitle:forState:
+ _objc_msgSend$setTranslatesAutoresizingMaskIntoConstraints:
+ _objc_msgSend$setURL:
+ _objc_msgSend$setUSBDeviceModeAndNCM:error:
+ _objc_msgSend$setUniqueId:
+ _objc_msgSend$setUnitsStyle:
+ _objc_msgSend$setUrlAddresses:
+ _objc_msgSend$setUserInteractionEnabled:
+ _objc_msgSend$setVideoGravity:
+ _objc_msgSend$setVideoRotationAngle:
+ _objc_msgSend$setViewControllers:
+ _objc_msgSend$setVoiceControl:
+ _objc_msgSend$setWorkingQueue:
+ _objc_msgSend$setZeroFormattingBehavior:
+ _objc_msgSend$setZoom:
+ _objc_msgSend$sharedApplication
+ _objc_msgSend$sharedConnection
+ _objc_msgSend$sharedRegistry
+ _objc_msgSend$sharedService
+ _objc_msgSend$sharedSession
+ _objc_msgSend$shortVersionString
+ _objc_msgSend$showsBusyIndicator
+ _objc_msgSend$shutdown
+ _objc_msgSend$skipDescendants
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$socialProfiles
+ _objc_msgSend$sourceType
+ _objc_msgSend$sources
+ _objc_msgSend$speakSelection
+ _objc_msgSend$startAdvertisingForUsecase:withOptions:
+ _objc_msgSend$startAnimating
+ _objc_msgSend$startCatalogDownload:options:completionWithError:
+ _objc_msgSend$startDate
+ _objc_msgSend$startDiscoveryWithCompletion:
+ _objc_msgSend$startDownload:completionWithError:
+ _objc_msgSend$startMonitoringEvent:error:
+ _objc_msgSend$startObserving
+ _objc_msgSend$startRunning
+ _objc_msgSend$status
+ _objc_msgSend$statusCode
+ _objc_msgSend$stopAdvertising
+ _objc_msgSend$stopMonitoringAllEvents
+ _objc_msgSend$stopObserving
+ _objc_msgSend$stopRunning
+ _objc_msgSend$stopScan
+ _objc_msgSend$streamError
+ _objc_msgSend$street
+ _objc_msgSend$stringByReplacingCharactersInRange:withString:
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$stringFromByteCount:
+ _objc_msgSend$stringFromByteCount:countStyle:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$stringFromInteger:
+ _objc_msgSend$stringFromTimeInterval:
+ _objc_msgSend$subject
+ _objc_msgSend$subviews
+ _objc_msgSend$supportedFeatures
+ _objc_msgSend$supportedSelectionsWithCompletionHandler:
+ _objc_msgSend$supportsDataExport
+ _objc_msgSend$synchronizeAndReturnError:
+ _objc_msgSend$systemBackgroundColor
+ _objc_msgSend$systemBlueColor
+ _objc_msgSend$systemFontOfSize:
+ _objc_msgSend$systemGray4Color
+ _objc_msgSend$systemGray5Color
+ _objc_msgSend$systemGrayColor
+ _objc_msgSend$systemOrangeColor
+ _objc_msgSend$systemRedColor
+ _objc_msgSend$tableView
+ _objc_msgSend$text
+ _objc_msgSend$textEdgeStyle
+ _objc_msgSend$textEdgeStyleVideoOverride
+ _objc_msgSend$textHighlightColor
+ _objc_msgSend$textHighlightOpacity
+ _objc_msgSend$textHighlightOpacityVideoOverride
+ _objc_msgSend$textOpacity
+ _objc_msgSend$textOpacityVideoOverride
+ _objc_msgSend$textSize
+ _objc_msgSend$threadID
+ _objc_msgSend$timeZone
+ _objc_msgSend$topAnchor
+ _objc_msgSend$topViewController
+ _objc_msgSend$totalExpected
+ _objc_msgSend$totalWritten
+ _objc_msgSend$trailingAnchor
+ _objc_msgSend$transferSize
+ _objc_msgSend$ttyType
+ _objc_msgSend$typeForInstallMachinery
+ _objc_msgSend$underlyingErrors
+ _objc_msgSend$unifiedContactWithIdentifier:keysToFetch:error:
+ _objc_msgSend$unifiedContactsMatchingPredicate:keysToFetch:error:
+ _objc_msgSend$uniqueId
+ _objc_msgSend$unregisterDevice:
+ _objc_msgSend$unsignedCharValue
+ _objc_msgSend$updateContact:
+ _objc_msgSend$urlAddresses
+ _objc_msgSend$userInfo
+ _objc_msgSend$valueWithCompletion:
+ _objc_msgSend$vibrationType
+ _objc_msgSend$videoRotationAngleForHorizonLevelPreview
+ _objc_msgSend$view
+ _objc_msgSend$viewControllers
+ _objc_msgSend$visibleCells
+ _objc_msgSend$visibleTopLevelAccounts
+ _objc_msgSend$voiceControl
+ _objc_msgSend$webpageURL
+ _objc_msgSend$weekNumber
+ _objc_msgSend$weeksOfTheYear
+ _objc_msgSend$widthAnchor
+ _objc_msgSend$window
+ _objc_msgSend$workingQueue
+ _objc_msgSend$year
+ _objc_msgSend$zoom
+ _objc_terminate
+ _objectdestroy.16Tm
+ _objectdestroy.190Tm
+ _objectdestroy.222Tm
+ _objectdestroy.231Tm
+ _objectdestroy.2Tm
+ _objectdestroy.44Tm
+ _objectdestroy.5Tm
+ _symbolic ScTy_____Sg_____GSg 12MigrationKit10NCMNetworkC s5NeverO
+ _symbolic _____ 12MigrationKit18OSMigrationFeatureV0aD8FlagsKey33_EC1AE9331AF005723FC8720EB763F84ALLV
+ _symbolic _____Sg 12MigrationKit10NCMNetworkC
+ _symbolic _____Sg 12MigrationKit15ExporterContextV
+ _symbolic _____Sg 12MigrationKit17AppMatchOverridesV0cD8OverrideV
+ _symbolic _____Sg 12MigrationKit7AppInfoV
+ _symbolic _____SgIeAgHr_ 12MigrationKit10NCMNetworkC
+ _symbolic _____Sg_ABt 10Foundation12URLQueryItemV
+ _symbolic _____y______G 12MigrationKit18OSMigrationPayloadC5FieldV s6UInt16V
+ _symbolic _____y___________pGSg s6ResultOsRi_zRi0_zrlE 12MigrationKit13AppPropertiesV s5ErrorP
+ _symbolic _____y___________pGSg s6ResultOsRi_zRi0_zrlE 12MigrationKit17HashedFileContentO s5ErrorP
+ _type_layout_string 12MigrationKit18OSMigrationFeatureV0aD8FlagsKey33_EC1AE9331AF005723FC8720EB763F84ALLV
- __PROTOCOLS__TtC12MigrationKit27AppPlaceholderPromotionInfo.30
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne200100ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8ne200100EPKvm
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne200100ERKS6_S9_
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_S9_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S9_SE_SC_Lb1EEENS5_IS9_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_S9_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S9_SE_SC_Lb1EEENS5_IS9_EEE13__move_assignERSJ_NS_17integral_constantIbLb1EEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_S9_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S9_SE_SC_Lb1EEENS5_IS9_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS9_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_S9_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S9_SE_SC_Lb1EEENS5_IS9_EEE21__construct_node_hashIRKNS_4pairIKS7_S8_EEJEEENS_10unique_ptrINS_11__hash_nodeIS9_PvEENS_22__hash_node_destructorINS5_IST_EEEEEEmOT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_S9_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S9_SE_SC_Lb1EEENS5_IS9_EEE25__emplace_unique_key_argsIS7_JRKNS_4pairIKS7_S8_EEEEENSL_INS_15__hash_iteratorIPNS_11__hash_nodeIS9_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_S9_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S9_SE_SC_Lb1EEENS5_IS9_EEE5clearEv
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_S9_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S9_SE_SC_Lb1EEENS5_IS9_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigEENS_22__unordered_map_hasherIS7_S9_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_S9_SE_SC_Lb1EEENS5_IS9_EEED2Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
- __ZNSt3__113unordered_mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE3sigNS_4hashIS6_EENS_8equal_toIS6_EENS4_INS_4pairIKS6_S7_EEEEED1B8ne200100Ev
- __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12migrationkit9signature14get_identifierEPKhmE3$_0EEEEEvPv
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8ne200100EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8ne200100EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8ne200100EPKcm
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE3sigEEPvEEEEEclB8ne200100EPSC_
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- ___swift_destroy_boxed_opaque_existential_2
- ___swift_destroy_boxed_opaque_existential_2Tm
- ___swift_get_extra_inhabitant_index.116Tm
- ___swift_get_extra_inhabitant_index.188Tm
- ___swift_get_extra_inhabitant_index.46Tm
- ___swift_mutable_project_boxed_opaque_existential_0
- ___swift_project_boxed_opaque_existential_2
- ___swift_store_extra_inhabitant_index.117Tm
- ___swift_store_extra_inhabitant_index.189Tm
- ___swift_store_extra_inhabitant_index.47Tm
- _block_copy_helper.188
- _block_copy_helper.29
- _block_copy_helper.30
- _block_copy_helper.37
- _block_copy_helper.4
- _block_copy_helper.45
- _block_copy_helper.8
- _block_descriptor.10
- _block_descriptor.190
- _block_descriptor.31
- _block_descriptor.32
- _block_descriptor.39
- _block_descriptor.47
- _block_descriptor.6
- _block_destroy_helper.189
- _block_destroy_helper.30
- _block_destroy_helper.31
- _block_destroy_helper.38
- _block_destroy_helper.46
- _block_destroy_helper.5
- _block_destroy_helper.9
- _get_type_metadata 15Synchronization6AtomicVySbG.2
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_release_x2
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objectdestroy.13Tm
- _objectdestroy.176Tm
- _objectdestroy.208Tm
- _objectdestroy.217Tm
- _objectdestroy.28Tm
- _objectdestroy.43Tm
- _objectdestroy.4Tm
- _objectdestroy.9Tm
- _symbolic Say_____G 12MigrationKit13AppIdentifierV
- _symbolic _____ 12MigrationKit18OSMigrationFeatureV0aD8FlagsKey33_79A53E23D90415892BECB0D5472FC0AFLLV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit13AppIdentifierV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit24OSMigrationAppIdentifierV
- _symbolic _____y__________ySay_____GG_G s16AsyncMapSequenceV8IteratorV 6IMCore12ImportExportO010AttachmentgD0C 0A18AlgorithmsInternal0a4SyncC0V AG0H0V
- _symbolic _____y__________ySay_____GG_G s16AsyncMapSequenceV8IteratorV 6IMCore12ImportExportO011ParticipantgD0C 0A18AlgorithmsInternal0a4SyncC0V AG0H0V
- _symbolic _____y__________ySay_____GG_G s16AsyncMapSequenceV8IteratorV 6IMCore12ImportExportO012ConversationgD0C 0A18AlgorithmsInternal0a4SyncC0V AG0H0V
- _symbolic _____y__________ySay_____GG_G s16AsyncMapSequenceV8IteratorV 6IMCore12ImportExportO07MessagegD0C 0A18AlgorithmsInternal0a4SyncC0V AG0H0V
- _symbolic _____y_____ySaySSGG_____y_____y___________pGG_G s16AsyncMapSequenceV8IteratorV 0A18AlgorithmsInternal0a4SyncC0V 12MigrationKit0A13BoundedStreamC s6ResultOsRi_zRi0_zrlE AH24OSMigrationCalendarEventV s5ErrorP
- _symbolic _____y_____ySaySSGG_____y_____y_____ySay_____y___________pGGSgGAByALGGG_G s16AsyncMapSequenceV8IteratorV 0A18AlgorithmsInternal0a4SyncC0V AE0a6JoinedC0V s0a7CompactbC0V 12MigrationKit0A13BoundedStreamC s6ResultOsRi_zRi0_zrlE AL15EventAttachmentV s5ErrorP
- _type_layout_string 12MigrationKit18OSMigrationFeatureV0aD8FlagsKey33_79A53E23D90415892BECB0D5472FC0AFLLV
CStrings:
+ "  Capability check result: canSupportNCM=%{bool}d"
+ "  USB capabilities (Android → iOS): ncmHostSupport=%{bool}d, ncmDeviceSupport=%{bool}d, drSwapSupport=%{bool}d"
+ "  USB capabilities (client → server): ncmHostSupport=%{bool}d, ncmDeviceSupport=%{bool}d, drSwapSupport=%{bool}d"
+ "  USB capabilities (iOS → Android): ncmHostSupport=%{bool}d, ncmDeviceSupport=%{bool}d, drSwapSupport=%{bool}d"
+ "  USB capabilities (server → client): ncmHostSupport=%{bool}d, ncmDeviceSupport=%{bool}d, drSwapSupport=%{bool}d"
+ "  interface: %s, type: %s, name: %s"
+ " migration failure"
+ "Address"
+ "AppleHPMARM"
+ "AppleUSBNCMControl"
+ "AppleUSBNCMData"
+ "Bulk importing networks from Android"
+ "Can not truncate last component"
+ "Capability determined: canSupportNCM=%{bool}d"
+ "Client initialization: USB connection check: %s"
+ "DataRole"
+ "Device"
+ "Discovering NCM interface..."
+ "Failed to disable USB device mode and restore configuration"
+ "Failed to enable USB device mode and NCM"
+ "Failed to enable USB device mode and NCM configuration"
+ "Failed to enable USB device mode and configure NCM"
+ "Forcing USB device mode and configuring NCM"
+ "Host"
+ "IOPortTransportStateUSB2"
+ "IOService"
+ "If enabled, skips ASC mapping. To export, mapping details must be provided in app Info.plist. For import, this implicitly trusts the bundleID from `targetPlatformIdentifiers` exported by Android."
+ "If enabled, the implicit data classes can be individually selected/deselected for debugging purposes."
+ "MKUSBRoleSwap"
+ "MigrationKit/APIClientPool.swift"
+ "MigrationKit/OSMigrationFeature.swift"
+ "NCM"
+ "NCM activated successfully as fallback"
+ "NCM activation completed successfully"
+ "NCM activation failed"
+ "NCM activation failed or no USB connection - continuing without NCM"
+ "NCM interface discovery failed"
+ "NCM interface is not up - cannot activate as current network"
+ "NCM is supported; USB connection check: %s"
+ "NCM was not started"
+ "NO"
+ "No USB connection detected - skipping NCM setup"
+ "None"
+ "Q20@0:8I16"
+ "Received"
+ "Received an \"empty\" first multipart part, indicating 0 actual parts"
+ "Received medium closure request"
+ "Received wireless medium negotiation response: infraSta=%{bool}d, wifiAware=%{bool}d"
+ "Request contained an empty file content identifier"
+ "Server initialization: USB connection check: %s"
+ "Starting NCM bringUp in parallel with device info exchange"
+ "Successfully disabled USB device mode and restored configuration"
+ "Successfully enabled NCM as current network."
+ "Successfully enabled USB device mode and NCM"
+ "Tearing down NCM network"
+ "USB re-enumeration wait completed"
+ "Waiting for USB re-enumeration to complete..."
+ "Wireless failed - attempting NCM as fallback"
+ "Wireless medium negotiation successful"
+ "YES"
+ "[MKUSBRoleSwap] Added AppleUSBNCMControl at interface index %d"
+ "[MKUSBRoleSwap] Added AppleUSBNCMData at interface index %d"
+ "[MKUSBRoleSwap] Adding NCM interfaces"
+ "[MKUSBRoleSwap] Already in device mode, just configuring NCM"
+ "[MKUSBRoleSwap] Brief delay between ForceUSBDeviceMode and NCM configuration"
+ "[MKUSBRoleSwap] Brief delay between forceMode and ForceUSBDeviceMode"
+ "[MKUSBRoleSwap] Calling ForceUSBDeviceMode to switch to device mode"
+ "[MKUSBRoleSwap] Calling forceMode(device=0x%llx, enable=0) to replug USB port"
+ "[MKUSBRoleSwap] Calling forceMode(device=0x%llx, enable=1) to unplug USB port"
+ "[MKUSBRoleSwap] Cleaning up HPM interface (no role swap was performed)"
+ "[MKUSBRoleSwap] Cleanup completed with some errors - check logs above"
+ "[MKUSBRoleSwap] Cleanup: didPerformRoleSwap=%s, didConfigureNCM=%s"
+ "[MKUSBRoleSwap] Configuring NCM interfaces"
+ "[MKUSBRoleSwap] Currently in host mode, performing full PD role switch sequence"
+ "[MKUSBRoleSwap] DataRole property not found in IOPortTransportStateUSB2 service"
+ "[MKUSBRoleSwap] Failed to append AppleUSBNCMControl: %d"
+ "[MKUSBRoleSwap] Failed to append AppleUSBNCMData: %d"
+ "[MKUSBRoleSwap] Failed to configure NCM"
+ "[MKUSBRoleSwap] Failed to create NCM description"
+ "[MKUSBRoleSwap] Failed to create matching dictionary for IOPortTransportStateUSB2"
+ "[MKUSBRoleSwap] Failed to get HPM interface: 0x%x"
+ "[MKUSBRoleSwap] Failed to get child iterator for AppleHPMARM: 0x%x"
+ "[MKUSBRoleSwap] Failed to restore USB description: 0x%x"
+ "[MKUSBRoleSwap] Failed to restore previous USB configuration"
+ "[MKUSBRoleSwap] Failed to save previous USB description"
+ "[MKUSBRoleSwap] Failed to trigger bus re-enumeration: 0x%x"
+ "[MKUSBRoleSwap] ForceMode(enable=0) failed: 0x%x"
+ "[MKUSBRoleSwap] ForceMode(enable=1) failed: 0x%x"
+ "[MKUSBRoleSwap] ForceUSBDeviceMode(enable=0) failed: 0x%x"
+ "[MKUSBRoleSwap] ForceUSBDeviceMode(enable=1) failed: 0x%x"
+ "[MKUSBRoleSwap] Found device Address: 0x%llx"
+ "[MKUSBRoleSwap] IOServiceGetMatchingServices failed with error: 0x%x"
+ "[MKUSBRoleSwap] IOServiceGetMatchingServices failed: 0x%x"
+ "[MKUSBRoleSwap] IOUSBDeviceControllerCreate failed: 0x%x"
+ "[MKUSBRoleSwap] IOUSBDeviceControllerGoOffAndOnBus failed: 0x%x"
+ "[MKUSBRoleSwap] IOUSBDeviceControllerSetDescription failed: 0x%x"
+ "[MKUSBRoleSwap] IOUSBDeviceDescriptionAppendConfiguration failed: %d"
+ "[MKUSBRoleSwap] No IOPortTransportStateUSB2 service found"
+ "[MKUSBRoleSwap] No previous USB configuration to restore"
+ "[MKUSBRoleSwap] QueryInterface failed with result: 0x%x"
+ "[MKUSBRoleSwap] Reconfiguring USB for NCM"
+ "[MKUSBRoleSwap] Released AppleHPMLib interface"
+ "[MKUSBRoleSwap] Restoring previous USB configuration"
+ "[MKUSBRoleSwap] Saved previous USB description"
+ "[MKUSBRoleSwap] Successfully configured NCM"
+ "[MKUSBRoleSwap] Successfully configured USB for NCM"
+ "[MKUSBRoleSwap] Successfully disabled ForceUSBDeviceMode (enable=0)"
+ "[MKUSBRoleSwap] Successfully disabled USB device mode and restored USB configuration"
+ "[MKUSBRoleSwap] Successfully enabled USB device mode and NCM"
+ "[MKUSBRoleSwap] Successfully obtained AppleHPMLib interface"
+ "[MKUSBRoleSwap] Successfully restored previous USB configuration"
+ "[MKUSBRoleSwap] USB connection check: DataRole=%d (%s), Connected=%s"
+ "_locked"
+ "activityWithType:reason:"
+ "arrow.forward.circle"
+ "beginActivity:error:"
+ "bringUp()"
+ "capability"
+ "com.apple.MigrationKit.MKUSBRoleSwap"
+ "configureNCM"
+ "destroyHPMLibInterface:"
+ "deviceUsesAPLDidChange:usesAPL:"
+ "disableDeviceModeAndNCM"
+ "enableDevAppMappingForAppDataTesting"
+ "enableDeviceModeAndNCM"
+ "enableImplicitDataclassSelection"
+ "endActivity:"
+ "getCurrentUSBDataRole"
+ "getDeviceAddressFromHPMService:"
+ "getHPMLibInterface:"
+ "i24@0:8^^^{AppleHPMLibInterfaceStructV3}16"
+ "isUSBConnected"
+ "ncmNetwork"
+ "ncmTask"
+ "pairingRequestEndedForPublisher:bySubscriber:reason:"
+ "publisher:getKeysBlobForMulticastSession:"
+ "restorePreviousUSBConfiguration"
+ "setAlpha:"
+ "setUSBDeviceModeAndNCM:error:"
+ "sleepForTimeInterval:"
+ "successfully imported voice memo. file=%@, savedRecordingURI=%@, size=%llu"
+ "v32@0:8@\"WiFiAwarePublisher\"16@\"NSData\"24"
+ "v40@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublishServiceSpecificInfo\"24q32"
+ "📤 Sending capability request to server:"
+ "📤 Sending capability response to client:"
+ "📥 Received capability request from client:"
+ "📥 Received capability response from server:"
- "Cannnot truncate last component"
- "Client migration failure"
- "Failed to send medium closure request"
- "Failed to tear down network"
- "Interface name is null"
- "MigrationKit/FeatureFlags.swift"
- "Network not found for interface "
- "Recieved"
- "Recieved an \"empty\" first multipart part, indicating 0 actual parts"
- "Request contained an empty file content identifer"
- "Requesting medium closure on %s"
- "Saved Wi-Fi Networks"
- "Server migration failure"
- "arrow.right.circle"
- "enabled ncm."
- "not enabled ncm."
- "removeNetwork(forInterfaceName:)"
- "sucessfully imported voice memo. file=%@, savedRecordingURI=%@, size=%llu"
- "supportedDestinations"
- "unknown interface"
- "will enable ncm."

```
