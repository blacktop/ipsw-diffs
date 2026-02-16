## DeviceDiscoveryUICore

> `/System/Library/PrivateFrameworks/DeviceDiscoveryUICore.framework/DeviceDiscoveryUICore`

```diff

-2094.40.71.0.0
-  __TEXT.__text: 0x3d9b8
-  __TEXT.__auth_stubs: 0x1970
-  __TEXT.__objc_methlist: 0x15ac
+2094.50.11.2.1
+  __TEXT.__text: 0x41678
+  __TEXT.__auth_stubs: 0x1920
+  __TEXT.__objc_methlist: 0x15c4
   __TEXT.__const: 0x2bd0
-  __TEXT.__cstring: 0x2037
+  __TEXT.__cstring: 0x1767
   __TEXT.__oslogstring: 0x3050
-  __TEXT.__gcc_except_tab: 0x284
+  __TEXT.__gcc_except_tab: 0x278
   __TEXT.__swift5_typeref: 0xd1c
   __TEXT.__constg_swiftt: 0xb44
   __TEXT.__swift5_fieldmd: 0x8c0

   __TEXT.__swift5_assocty: 0xb8
   __TEXT.__swift5_proto: 0x234
   __TEXT.__swift5_types: 0xd8
-  __TEXT.__swift5_capture: 0x208
+  __TEXT.__swift5_capture: 0x218
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x78
   __TEXT.__swift5_acfuncs: 0x28
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x11e0
-  __TEXT.__eh_frame: 0x1b08
-  __TEXT.__objc_classname: 0x3fc
-  __TEXT.__objc_methname: 0x4115
-  __TEXT.__objc_methtype: 0xe02
-  __TEXT.__objc_stubs: 0x2600
-  __DATA_CONST.__got: 0x520
+  __TEXT.__unwind_info: 0x12f0
+  __TEXT.__eh_frame: 0x1ae8
+  __TEXT.__objc_classname: 0x83a
+  __TEXT.__objc_methname: 0x44d5
+  __TEXT.__objc_methtype: 0x1122
+  __TEXT.__objc_stubs: 0x3240
+  __DATA_CONST.__got: 0x530
   __DATA_CONST.__const: 0x990
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1028
+  __DATA_CONST.__objc_selrefs: 0x1030
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0xcc8
-  __AUTH_CONST.__const: 0x18e8
+  __AUTH_CONST.__auth_got: 0xca0
+  __AUTH_CONST.__const: 0x1910
   __AUTH_CONST.__cfstring: 0x12a0
-  __AUTH_CONST.__objc_const: 0x2de8
+  __AUTH_CONST.__objc_const: 0x2e18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0xc20
-  __AUTH.__data: 0x898
-  __DATA.__objc_ivar: 0x140
-  __DATA.__data: 0x1210
+  __AUTH.__data: 0x890
+  __DATA.__objc_ivar: 0x144
+  __DATA.__data: 0x1230
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x42b0
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x1c8
-  __DATA_DIRTY.__data: 0x188
+  __DATA_DIRTY.__data: 0x180
   __DATA_DIRTY.__bss: 0x2b0
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 52E4052D-2987-3300-AB36-03D978F32843
-  Functions: 1488
-  Symbols:   2486
-  CStrings:  1502
+  UUID: 8C89B2C1-EE02-3B53-B67E-171239219D84
+  Functions: 1490
+  Symbols:   2605
+  CStrings:  1496
 
Symbols:
+ -[_DDUIRemoteDisplaySessionHandler canEnterSessionWithDevice:]
+ -[_DDUIRemoteDisplaySessionHandler isContinuityCaptureUserPreferenceEnabledOrSkippedForDevice:]
+ -[_DDUIRemoteDisplaySessionHandler shouldAutoAcceptCCConfirmationForRemoteDevice:]
+ -[_DDUIRemoteDisplaySessionHandler shouldByPassConfirmationForRemoteDevice:]
+ -[_DDUIiOSPresentedNotification remoteDevice]
+ -[_DDUIiOSPresentedNotification setRemoteDevice:]
+ _OBJC_IVAR_$__DDUIiOSPresentedNotification._remoteDevice
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _block_copy_helper.29
+ _block_copy_helper.38
+ _block_copy_helper.67
+ _block_copy_helper.81
+ _block_copy_helper.84
+ _block_descriptor.31
+ _block_descriptor.40
+ _block_descriptor.69
+ _block_descriptor.83
+ _block_descriptor.86
+ _block_destroy_helper.30
+ _block_destroy_helper.39
+ _block_destroy_helper.68
+ _block_destroy_helper.82
+ _block_destroy_helper.85
+ _objc_msgSend$_crossPlatformUnifiedMeContactWithKeysToFetch:error:
+ _objc_msgSend$aa_primaryAppleAccount
+ _objc_msgSend$activate:
+ _objc_msgSend$addContact:toContainerWithIdentifier:
+ _objc_msgSend$addObserver:
+ _objc_msgSend$canEnterSessionWithDevice:
+ _objc_msgSend$configureParameters:
+ _objc_msgSend$contactID
+ _objc_msgSend$contactWithDisplayName:handleStrings:
+ _objc_msgSend$contactsWithData:error:
+ _objc_msgSend$createScene:
+ _objc_msgSend$dataForKey:
+ _objc_msgSend$dataWithContacts:options:error:
+ _objc_msgSend$debugDescription
+ _objc_msgSend$defaultStore
+ _objc_msgSend$description
+ _objc_msgSend$displayPhoneNumber
+ _objc_msgSend$emailAddresses
+ _objc_msgSend$exchangeQUICPublicKeyFor:publicKey:completion:
+ _objc_msgSend$executeSaveRequest:error:
+ _objc_msgSend$familyName
+ _objc_msgSend$firstName
+ _objc_msgSend$formattedStringValue
+ _objc_msgSend$getIdentitiesWithFlags:completion:
+ _objc_msgSend$getPhoneNumber:error:
+ _objc_msgSend$getUserDefaultVoiceSubscriptionContext:
+ _objc_msgSend$givenName
+ _objc_msgSend$identityForAngelJobLabel:
+ _objc_msgSend$idsDeviceID
+ _objc_msgSend$imageData
+ _objc_msgSend$info
+ _objc_msgSend$init
+ _objc_msgSend$initWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithInfo:responder:
+ _objc_msgSend$initWithInfo:timeout:forResponseOnQueue:withHandler:
+ _objc_msgSend$initWithLabel:value:
+ _objc_msgSend$initWithMachServiceName:
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$initWithSettings:
+ _objc_msgSend$initWithStringValue:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$isContinuityCaptureUserPreferenceEnabledOrSkippedForDevice:
+ _objc_msgSend$isLikePhoneNumber:
+ _objc_msgSend$lastName
+ _objc_msgSend$mainConfiguration
+ _objc_msgSend$nameOrderForContact:
+ _objc_msgSend$nicknameForCurrentUserWithCompletionHandler:
+ _objc_msgSend$objectForSetting:
+ _objc_msgSend$otherSettings
+ _objc_msgSend$phoneNumbers
+ _objc_msgSend$phoneticFamilyName
+ _objc_msgSend$phoneticGivenName
+ _objc_msgSend$phoneticMiddleName
+ _objc_msgSend$posterArchiveData
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$resume
+ _objc_msgSend$sceneWithIdentifier:
+ _objc_msgSend$setAddressingGrammars:
+ _objc_msgSend$setClientIdentity:
+ _objc_msgSend$setContactType:
+ _objc_msgSend$setDisplayConfiguration:
+ _objc_msgSend$setEmailAddresses:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setFamilyName:
+ _objc_msgSend$setForeground:
+ _objc_msgSend$setGivenName:
+ _objc_msgSend$setIncludePhotos:
+ _objc_msgSend$setIncludeWallpaper:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setMiddleName:
+ _objc_msgSend$setNamePrefix:
+ _objc_msgSend$setNameSuffix:
+ _objc_msgSend$setObject:forSetting:
+ _objc_msgSend$setPhoneNumbers:
+ _objc_msgSend$setPhoneticFamilyName:
+ _objc_msgSend$setPhoneticGivenName:
+ _objc_msgSend$setPhoneticMiddleName:
+ _objc_msgSend$setRemoteDevice:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setSharedPhotoDisplayPreference:
+ _objc_msgSend$setSpecification:
+ _objc_msgSend$setThumbnailImageData:
+ _objc_msgSend$setTransactionAuthor:
+ _objc_msgSend$setWallpaper:
+ _objc_msgSend$setWatchWallpaperImageData:
+ _objc_msgSend$shouldAutoAcceptCCConfirmationForRemoteDevice:
+ _objc_msgSend$shouldByPassConfirmationForRemoteDevice:
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$stringFromContact:
+ _objc_msgSend$stringValue
+ _objc_msgSend$thumbnailImageData
+ _objc_msgSend$updateSettingsWithBlock:
+ _objc_msgSend$userDidRespondWithAccepted:
+ _objc_msgSend$userFullName
+ _objc_msgSend$username
+ _objc_msgSend$value
+ _objc_msgSend$wallpaper
+ _objc_msgSend$watchWallpaperImageData
+ _objectdestroy.24Tm
+ _objectdestroy.32Tm
- -[_DDUIRemoteDisplaySessionHandler canEnterSession]
- -[_DDUIRemoteDisplaySessionHandler isContinuityCaptureUserPreferenceEnabled]
- -[_DDUIRemoteDisplaySessionHandler shouldAutoAcceptCCConfirmation]
- -[_DDUIRemoteDisplaySessionHandler shouldByPassConfirmationForRemoteDeviceID:]
- _block_copy_helper.28
- _block_copy_helper.37
- _block_copy_helper.66
- _block_copy_helper.80
- _block_copy_helper.83
- _block_descriptor.30
- _block_descriptor.39
- _block_descriptor.68
- _block_descriptor.82
- _block_descriptor.85
- _block_destroy_helper.29
- _block_destroy_helper.38
- _block_destroy_helper.67
- _block_destroy_helper.81
- _block_destroy_helper.84
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$canEnterSession
- _objc_msgSend$isContinuityCaptureUserPreferenceEnabled
- _objc_msgSend$shouldAutoAcceptCCConfirmation
- _objc_msgSend$shouldByPassConfirmationForRemoteDeviceID:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objectdestroy.23Tm
- _objectdestroy.31Tm
CStrings:
+ "@\"<DDUIDevice>\""
+ "T@\"<DDUIDevice>\",&,N,V_remoteDevice"
+ "_remoteDevice"
+ "canEnterSessionWithDevice:"
+ "isContinuityCaptureUserPreferenceEnabledOrSkippedForDevice:"
+ "setRemoteDevice:"
+ "shouldAutoAcceptCCConfirmationForRemoteDevice:"
+ "shouldByPassConfirmationForRemoteDevice:"
- "canEnterSession"
- "isContinuityCaptureUserPreferenceEnabled"
- "shouldAutoAcceptCCConfirmation"
- "shouldByPassConfirmationForRemoteDeviceID:"

```
