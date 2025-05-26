## ClarityFoundation

> `/System/Library/PrivateFrameworks/ClarityFoundation.framework/ClarityFoundation`

```diff

-3089.1.0.0.0
-  __TEXT.__text: 0x3f84
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_methlist: 0x67c
+3093.2.4.0.2
+  __TEXT.__text: 0x498c
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__objc_methlist: 0x6b4
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x66f
-  __TEXT.__oslogstring: 0x1c4
-  __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__dlopen_cstrs: 0xb7
-  __TEXT.__unwind_info: 0x220
-  __TEXT.__objc_classname: 0xf1
-  __TEXT.__objc_methname: 0xfed
+  __TEXT.__gcc_except_tab: 0x50
+  __TEXT.__cstring: 0x6d7
+  __TEXT.__oslogstring: 0x2b7
+  __TEXT.__dlopen_cstrs: 0xfa
+  __TEXT.__unwind_info: 0x248
+  __TEXT.__objc_classname: 0x1bd
+  __TEXT.__objc_methname: 0x1155
   __TEXT.__objc_methtype: 0x175
-  __TEXT.__objc_stubs: 0x6e0
+  __TEXT.__objc_stubs: 0x8e0
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x148
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__const: 0x188
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x848
-  __DATA_CONST.__objc_selrefs: 0x408
+  __DATA_CONST.__objc_const: 0xb20
+  __DATA_CONST.__objc_selrefs: 0x480
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__cfstring: 0x8c0
+  __AUTH_CONST.__cfstring: 0x8e0
+  __AUTH_CONST.__objc_const: 0x630
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__objc_const: 0x5a0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1d8
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_classrefs: 0xb0
-  __DATA.__objc_superrefs: 0x48
+  __AUTH_CONST.__auth_got: 0x1f8
+  __AUTH.__objc_data: 0x410
+  __DATA.__objc_classrefs: 0xb8
+  __DATA.__objc_superrefs: 0x50
   __DATA.__objc_ivar: 0x14
   __DATA.__data: 0xd0
-  __DATA.__bss: 0x90
+  __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 150
-  Symbols:   598
-  CStrings:  308
+  Functions: 160
+  Symbols:   672
+  CStrings:  339
 
Symbols:
+ +[CLFCameraSettings_GeneratedCode allPreferenceSelectorsAsStrings]
+ +[CLFCameraSettings_GeneratedCode domainName]
+ +[CLFCameraSettings_GeneratedCode sharedInstance]
+ +[CLFMessagesSettings_GeneratedCode allPreferenceSelectorsAsStrings]
+ +[CLFMessagesSettings_GeneratedCode domainName]
+ +[CLFMessagesSettings_GeneratedCode sharedInstance]
+ +[CLFMusicSettings_GeneratedCode allPreferenceSelectorsAsStrings]
+ +[CLFMusicSettings_GeneratedCode domainName]
+ +[CLFMusicSettings_GeneratedCode sharedInstance]
+ +[CLFPhoneFaceTimeSettings_GeneratedCode allPreferenceSelectorsAsStrings]
+ +[CLFPhoneFaceTimeSettings_GeneratedCode domainName]
+ +[CLFPhoneFaceTimeSettings_GeneratedCode sharedInstance]
+ +[CLFPhotosSettings_GeneratedCode allPreferenceSelectorsAsStrings]
+ +[CLFPhotosSettings_GeneratedCode domainName]
+ +[CLFPhotosSettings_GeneratedCode sharedInstance]
+ +[CLFSettings_GeneratedCode allPreferenceSelectorsAsStrings]
+ +[CLFSettings_GeneratedCode domainName]
+ +[CLFSettings_GeneratedCode sharedInstance]
+ -[CLFCameraSettings_GeneratedCode allowPhotoCapture]
+ -[CLFCameraSettings_GeneratedCode allowSelfieCapture]
+ -[CLFCameraSettings_GeneratedCode allowSelfieVideoCapture]
+ -[CLFCameraSettings_GeneratedCode allowVideoCapture]
+ -[CLFCameraSettings_GeneratedCode init]
+ -[CLFCameraSettings_GeneratedCode setAllowPhotoCapture:]
+ -[CLFCameraSettings_GeneratedCode setAllowSelfieCapture:]
+ -[CLFCameraSettings_GeneratedCode setAllowSelfieVideoCapture:]
+ -[CLFCameraSettings_GeneratedCode setAllowVideoCapture:]
+ -[CLFMessagesSettings_GeneratedCode conversationDetailsEnabled]
+ -[CLFMessagesSettings_GeneratedCode emojiKeyboardEnabled]
+ -[CLFMessagesSettings_GeneratedCode incomingCommunicationLimit]
+ -[CLFMessagesSettings_GeneratedCode init]
+ -[CLFMessagesSettings_GeneratedCode setConversationDetailsEnabled:]
+ -[CLFMessagesSettings_GeneratedCode setEmojiKeyboardEnabled:]
+ -[CLFMessagesSettings_GeneratedCode setIncomingCommunicationLimit:]
+ -[CLFMessagesSettings_GeneratedCode setSoftwareKeyboardEnabled:]
+ -[CLFMessagesSettings_GeneratedCode setTapToSpeakEnabled:]
+ -[CLFMessagesSettings_GeneratedCode setVideoRecordingEnabled:]
+ -[CLFMessagesSettings_GeneratedCode softwareKeyboardEnabled]
+ -[CLFMessagesSettings_GeneratedCode tapToSpeakEnabled]
+ -[CLFMessagesSettings_GeneratedCode videoRecordingEnabled]
+ -[CLFMusicSettings_GeneratedCode init]
+ -[CLFMusicSettings_GeneratedCode selectedPlaylists]
+ -[CLFMusicSettings_GeneratedCode setSelectedPlaylists:]
+ -[CLFPhoneFaceTimeSettings_GeneratedCode dialerKeypadEnabled]
+ -[CLFPhoneFaceTimeSettings_GeneratedCode inCallKeypadEnabled]
+ -[CLFPhoneFaceTimeSettings_GeneratedCode incomingCommunicationLimit]
+ -[CLFPhoneFaceTimeSettings_GeneratedCode init]
+ -[CLFPhoneFaceTimeSettings_GeneratedCode muteEnabled]
+ -[CLFPhoneFaceTimeSettings_GeneratedCode recentsEnabled]
+ -[CLFPhoneFaceTimeSettings_GeneratedCode setDialerKeypadEnabled:]
+ -[CLFPhoneFaceTimeSettings_GeneratedCode setInCallKeypadEnabled:]
+ -[CLFPhoneFaceTimeSettings_GeneratedCode setIncomingCommunicationLimit:]
+ -[CLFPhoneFaceTimeSettings_GeneratedCode setMuteEnabled:]
+ -[CLFPhoneFaceTimeSettings_GeneratedCode setRecentsEnabled:]
+ -[CLFPhoneFaceTimeSettings_GeneratedCode setSpeakerOptionEnabled:]
+ -[CLFPhoneFaceTimeSettings_GeneratedCode speakerOptionEnabled]
+ -[CLFPhotosSettings(Migration) _migrateSelectedSharedAlbumNamesIfNecessary]
+ -[CLFPhotosSettings(Migration) _saveSelectedSharedAlbumCloudIdentifiersForNames:]
+ -[CLFPhotosSettings(Migration) selectedSharedAlbumCloudIdentifiers]
+ -[CLFPhotosSettings_GeneratedCode includeSharedAlbums]
+ -[CLFPhotosSettings_GeneratedCode init]
+ -[CLFPhotosSettings_GeneratedCode selectedSharedAlbumCloudIdentifiers]
+ -[CLFPhotosSettings_GeneratedCode setIncludeSharedAlbums:]
+ -[CLFPhotosSettings_GeneratedCode setSelectedSharedAlbumCloudIdentifiers:]
+ -[CLFSettings_GeneratedCode adminPasscodeRecoveryAppleID]
+ -[CLFSettings_GeneratedCode allowSiri]
+ -[CLFSettings_GeneratedCode applicationBundleIdentifiers]
+ -[CLFSettings_GeneratedCode batteryMonitoringEnabled]
+ -[CLFSettings_GeneratedCode didCompleteSetup]
+ -[CLFSettings_GeneratedCode emergencyKeypadEnabled]
+ -[CLFSettings_GeneratedCode init]
+ -[CLFSettings_GeneratedCode listLayout]
+ -[CLFSettings_GeneratedCode lockScreenClockEnabled]
+ -[CLFSettings_GeneratedCode notificationsEnabled]
+ -[CLFSettings_GeneratedCode overrideNonClarityApplicationBundleIdentifiers]
+ -[CLFSettings_GeneratedCode setAdminPasscodeRecoveryAppleID:]
+ -[CLFSettings_GeneratedCode setAllowSiri:]
+ -[CLFSettings_GeneratedCode setApplicationBundleIdentifiers:]
+ -[CLFSettings_GeneratedCode setBatteryMonitoringEnabled:]
+ -[CLFSettings_GeneratedCode setDidCompleteSetup:]
+ -[CLFSettings_GeneratedCode setEmergencyKeypadEnabled:]
+ -[CLFSettings_GeneratedCode setListLayout:]
+ -[CLFSettings_GeneratedCode setLockScreenClockEnabled:]
+ -[CLFSettings_GeneratedCode setNotificationsEnabled:]
+ -[CLFSettings_GeneratedCode setOverrideNonClarityApplicationBundleIdentifiers:]
+ -[CLFSettings_GeneratedCode setShouldShowTripleClickInstructions:]
+ -[CLFSettings_GeneratedCode setVolumeButtonsEnabled:]
+ -[CLFSettings_GeneratedCode shouldShowTripleClickInstructions]
+ -[CLFSettings_GeneratedCode volumeButtonsEnabled]
+ _OBJC_CLASS_$_CLFCameraSettings_GeneratedCode
+ _OBJC_CLASS_$_CLFMessagesSettings_GeneratedCode
+ _OBJC_CLASS_$_CLFMusicSettings_GeneratedCode
+ _OBJC_CLASS_$_CLFPhoneFaceTimeSettings_GeneratedCode
+ _OBJC_CLASS_$_CLFPhotosSettings_GeneratedCode
+ _OBJC_CLASS_$_CLFSettings_GeneratedCode
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_METACLASS_$_CLFCameraSettings_GeneratedCode
+ _OBJC_METACLASS_$_CLFMessagesSettings_GeneratedCode
+ _OBJC_METACLASS_$_CLFMusicSettings_GeneratedCode
+ _OBJC_METACLASS_$_CLFPhoneFaceTimeSettings_GeneratedCode
+ _OBJC_METACLASS_$_CLFPhotosSettings_GeneratedCode
+ _OBJC_METACLASS_$_CLFSettings_GeneratedCode
+ _PhotosLibrary
+ _PhotosLibraryCore.frameworkLibrary
+ __OBJC_$_CLASS_METHODS_CLFCameraSettings_GeneratedCode
+ __OBJC_$_CLASS_METHODS_CLFMessagesSettings_GeneratedCode
+ __OBJC_$_CLASS_METHODS_CLFMusicSettings_GeneratedCode
+ __OBJC_$_CLASS_METHODS_CLFPhoneFaceTimeSettings_GeneratedCode
+ __OBJC_$_CLASS_METHODS_CLFPhotosSettings_GeneratedCode
+ __OBJC_$_CLASS_METHODS_CLFSettings_GeneratedCode
+ __OBJC_$_CLASS_PROP_LIST_CLFCameraSettings_GeneratedCode
+ __OBJC_$_CLASS_PROP_LIST_CLFMessagesSettings_GeneratedCode
+ __OBJC_$_CLASS_PROP_LIST_CLFMusicSettings_GeneratedCode
+ __OBJC_$_CLASS_PROP_LIST_CLFPhoneFaceTimeSettings_GeneratedCode
+ __OBJC_$_CLASS_PROP_LIST_CLFPhotosSettings_GeneratedCode
+ __OBJC_$_CLASS_PROP_LIST_CLFSettings_GeneratedCode
+ __OBJC_$_INSTANCE_METHODS_CLFCameraSettings_GeneratedCode
+ __OBJC_$_INSTANCE_METHODS_CLFMessagesSettings_GeneratedCode
+ __OBJC_$_INSTANCE_METHODS_CLFMusicSettings_GeneratedCode
+ __OBJC_$_INSTANCE_METHODS_CLFPhoneFaceTimeSettings_GeneratedCode
+ __OBJC_$_INSTANCE_METHODS_CLFPhotosSettings(Migration)
+ __OBJC_$_INSTANCE_METHODS_CLFPhotosSettings_GeneratedCode
+ __OBJC_$_INSTANCE_METHODS_CLFSettings_GeneratedCode
+ __OBJC_$_PROP_LIST_CLFCameraSettings_GeneratedCode
+ __OBJC_$_PROP_LIST_CLFMessagesSettings_GeneratedCode
+ __OBJC_$_PROP_LIST_CLFMusicSettings_GeneratedCode
+ __OBJC_$_PROP_LIST_CLFPhoneFaceTimeSettings_GeneratedCode
+ __OBJC_$_PROP_LIST_CLFPhotosSettings_GeneratedCode
+ __OBJC_$_PROP_LIST_CLFSettings_GeneratedCode
+ __OBJC_CLASS_RO_$_CLFCameraSettings_GeneratedCode
+ __OBJC_CLASS_RO_$_CLFMessagesSettings_GeneratedCode
+ __OBJC_CLASS_RO_$_CLFMusicSettings_GeneratedCode
+ __OBJC_CLASS_RO_$_CLFPhoneFaceTimeSettings_GeneratedCode
+ __OBJC_CLASS_RO_$_CLFPhotosSettings_GeneratedCode
+ __OBJC_CLASS_RO_$_CLFSettings_GeneratedCode
+ __OBJC_METACLASS_RO_$_CLFCameraSettings_GeneratedCode
+ __OBJC_METACLASS_RO_$_CLFMessagesSettings_GeneratedCode
+ __OBJC_METACLASS_RO_$_CLFMusicSettings_GeneratedCode
+ __OBJC_METACLASS_RO_$_CLFPhoneFaceTimeSettings_GeneratedCode
+ __OBJC_METACLASS_RO_$_CLFPhotosSettings_GeneratedCode
+ __OBJC_METACLASS_RO_$_CLFSettings_GeneratedCode
+ ___43+[CLFSettings_GeneratedCode sharedInstance]_block_invoke
+ ___48+[CLFMusicSettings_GeneratedCode sharedInstance]_block_invoke
+ ___49+[CLFCameraSettings_GeneratedCode sharedInstance]_block_invoke
+ ___49+[CLFPhotosSettings_GeneratedCode sharedInstance]_block_invoke
+ ___51+[CLFMessagesSettings_GeneratedCode sharedInstance]_block_invoke
+ ___56+[CLFPhoneFaceTimeSettings_GeneratedCode sharedInstance]_block_invoke
+ ___81-[CLFPhotosSettings(Migration) _saveSelectedSharedAlbumCloudIdentifiersForNames:]_block_invoke
+ ___PhotosLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32s_e34_v32?0"PHAssetCollection"8Q16^B24ls32l8
+ ___getPHAssetCollectionClass_block_invoke
+ ___getPHAssetCollectionClass_block_invoke.cold.1
+ ___getPHPhotoLibraryClass_block_invoke
+ ___getPHPhotoLibraryClass_block_invoke.cold.1
+ _audit_stringPhotos
+ _getPHAssetCollectionClass.softClass
+ _getPHPhotoLibraryClass.softClass
+ _objc_msgSend$_migrateSelectedSharedAlbumNamesIfNecessary
+ _objc_msgSend$_saveSelectedSharedAlbumCloudIdentifiersForNames:
+ _objc_msgSend$addObject:
+ _objc_msgSend$array
+ _objc_msgSend$cloudIdentifier
+ _objc_msgSend$cloudIdentifierMappingsForLocalIdentifiers:
+ _objc_msgSend$count
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$error
+ _objc_msgSend$fetchAssetCollectionsWithType:subtype:options:
+ _objc_msgSend$length
+ _objc_msgSend$localIdentifier
+ _objc_msgSend$localizedTitle
+ _objc_msgSend$setSelectedSharedAlbumCloudIdentifiers:
+ _objc_msgSend$sharedPhotoLibrary
+ _objc_msgSend$stringValue
+ _objc_release_x27
+ _objc_retain_x1
+ _objc_retain_x20
+ _objc_retain_x24
- +[CLFCameraSettings allPreferenceSelectorsAsStrings]
- +[CLFCameraSettings domainName]
- +[CLFCameraSettings sharedInstance]
- +[CLFMessagesSettings allPreferenceSelectorsAsStrings]
- +[CLFMessagesSettings domainName]
- +[CLFMessagesSettings sharedInstance]
- +[CLFMusicSettings allPreferenceSelectorsAsStrings]
- +[CLFMusicSettings domainName]
- +[CLFMusicSettings sharedInstance]
- +[CLFPhoneFaceTimeSettings allPreferenceSelectorsAsStrings]
- +[CLFPhoneFaceTimeSettings domainName]
- +[CLFPhoneFaceTimeSettings sharedInstance]
- +[CLFPhotosSettings allPreferenceSelectorsAsStrings]
- +[CLFPhotosSettings domainName]
- +[CLFPhotosSettings sharedInstance]
- +[CLFSettings allPreferenceSelectorsAsStrings]
- +[CLFSettings domainName]
- +[CLFSettings sharedInstance]
- -[CLFCameraSettings allowPhotoCapture]
- -[CLFCameraSettings allowSelfieCapture]
- -[CLFCameraSettings allowSelfieVideoCapture]
- -[CLFCameraSettings allowVideoCapture]
- -[CLFCameraSettings init]
- -[CLFCameraSettings setAllowPhotoCapture:]
- -[CLFCameraSettings setAllowSelfieCapture:]
- -[CLFCameraSettings setAllowSelfieVideoCapture:]
- -[CLFCameraSettings setAllowVideoCapture:]
- -[CLFMessagesSettings conversationDetailsEnabled]
- -[CLFMessagesSettings emojiKeyboardEnabled]
- -[CLFMessagesSettings incomingCommunicationLimit]
- -[CLFMessagesSettings init]
- -[CLFMessagesSettings setConversationDetailsEnabled:]
- -[CLFMessagesSettings setEmojiKeyboardEnabled:]
- -[CLFMessagesSettings setIncomingCommunicationLimit:]
- -[CLFMessagesSettings setSoftwareKeyboardEnabled:]
- -[CLFMessagesSettings setTapToSpeakEnabled:]
- -[CLFMessagesSettings setVideoRecordingEnabled:]
- -[CLFMessagesSettings softwareKeyboardEnabled]
- -[CLFMessagesSettings tapToSpeakEnabled]
- -[CLFMessagesSettings videoRecordingEnabled]
- -[CLFMusicSettings init]
- -[CLFMusicSettings selectedPlaylists]
- -[CLFMusicSettings setSelectedPlaylists:]
- -[CLFPhoneFaceTimeSettings dialerKeypadEnabled]
- -[CLFPhoneFaceTimeSettings inCallKeypadEnabled]
- -[CLFPhoneFaceTimeSettings incomingCommunicationLimit]
- -[CLFPhoneFaceTimeSettings init]
- -[CLFPhoneFaceTimeSettings muteEnabled]
- -[CLFPhoneFaceTimeSettings recentsEnabled]
- -[CLFPhoneFaceTimeSettings setDialerKeypadEnabled:]
- -[CLFPhoneFaceTimeSettings setInCallKeypadEnabled:]
- -[CLFPhoneFaceTimeSettings setIncomingCommunicationLimit:]
- -[CLFPhoneFaceTimeSettings setMuteEnabled:]
- -[CLFPhoneFaceTimeSettings setRecentsEnabled:]
- -[CLFPhoneFaceTimeSettings setSpeakerOptionEnabled:]
- -[CLFPhoneFaceTimeSettings speakerOptionEnabled]
- -[CLFPhotosSettings includeSharedAlbums]
- -[CLFPhotosSettings init]
- -[CLFPhotosSettings selectedSharedAlbums]
- -[CLFPhotosSettings setIncludeSharedAlbums:]
- -[CLFPhotosSettings setSelectedSharedAlbums:]
- -[CLFSettings adminPasscodeRecoveryAppleID]
- -[CLFSettings allowSiri]
- -[CLFSettings applicationBundleIdentifiers]
- -[CLFSettings batteryMonitoringEnabled]
- -[CLFSettings didCompleteSetup]
- -[CLFSettings emergencyKeypadEnabled]
- -[CLFSettings init]
- -[CLFSettings listLayout]
- -[CLFSettings lockScreenClockEnabled]
- -[CLFSettings notificationsEnabled]
- -[CLFSettings overrideNonClarityApplicationBundleIdentifiers]
- -[CLFSettings setAdminPasscodeRecoveryAppleID:]
- -[CLFSettings setAllowSiri:]
- -[CLFSettings setApplicationBundleIdentifiers:]
- -[CLFSettings setBatteryMonitoringEnabled:]
- -[CLFSettings setDidCompleteSetup:]
- -[CLFSettings setEmergencyKeypadEnabled:]
- -[CLFSettings setListLayout:]
- -[CLFSettings setLockScreenClockEnabled:]
- -[CLFSettings setNotificationsEnabled:]
- -[CLFSettings setOverrideNonClarityApplicationBundleIdentifiers:]
- -[CLFSettings setShouldShowTripleClickInstructions:]
- -[CLFSettings setVolumeButtonsEnabled:]
- -[CLFSettings shouldShowTripleClickInstructions]
- -[CLFSettings volumeButtonsEnabled]
- __OBJC_$_CLASS_METHODS_CLFCameraSettings
- __OBJC_$_CLASS_METHODS_CLFMessagesSettings(Staging)
- __OBJC_$_CLASS_METHODS_CLFMusicSettings
- __OBJC_$_CLASS_METHODS_CLFPhoneFaceTimeSettings
- __OBJC_$_CLASS_METHODS_CLFPhotosSettings
- __OBJC_$_CLASS_METHODS_CLFSettings
- __OBJC_$_CLASS_PROP_LIST_CLFCameraSettings
- __OBJC_$_CLASS_PROP_LIST_CLFMessagesSettings
- __OBJC_$_CLASS_PROP_LIST_CLFMusicSettings
- __OBJC_$_CLASS_PROP_LIST_CLFPhoneFaceTimeSettings
- __OBJC_$_CLASS_PROP_LIST_CLFPhotosSettings
- __OBJC_$_CLASS_PROP_LIST_CLFSettings
- __OBJC_$_INSTANCE_METHODS_CLFCameraSettings
- __OBJC_$_INSTANCE_METHODS_CLFMusicSettings
- __OBJC_$_INSTANCE_METHODS_CLFPhoneFaceTimeSettings
- __OBJC_$_INSTANCE_METHODS_CLFPhotosSettings
- __OBJC_$_INSTANCE_METHODS_CLFSettings
- __OBJC_$_PROP_LIST_CLFCameraSettings
- __OBJC_$_PROP_LIST_CLFMusicSettings
- __OBJC_$_PROP_LIST_CLFPhoneFaceTimeSettings
- __OBJC_$_PROP_LIST_CLFPhotosSettings
- __OBJC_$_PROP_LIST_CLFSettings
- ___29+[CLFSettings sharedInstance]_block_invoke
- ___34+[CLFMusicSettings sharedInstance]_block_invoke
- ___35+[CLFCameraSettings sharedInstance]_block_invoke
- ___35+[CLFPhotosSettings sharedInstance]_block_invoke
- ___37+[CLFMessagesSettings sharedInstance]_block_invoke
- ___42+[CLFPhoneFaceTimeSettings sharedInstance]_block_invoke
CStrings:
+ "CLFCameraSettings_GeneratedCode"
+ "CLFMessagesSettings_GeneratedCode"
+ "CLFMusicSettings_GeneratedCode"
+ "CLFPhoneFaceTimeSettings_GeneratedCode"
+ "CLFPhotosSettings_GeneratedCode"
+ "CLFSettings_GeneratedCode"
+ "Migrating %lu shared photo album name(s)."
+ "Migration"
+ "PHAssetCollection"
+ "PHPhotoLibrary"
+ "Removing empty shared photo album names."
+ "SelectedSharedAlbumCloudIdentifiers"
+ "Unable to get cloud identifier for shared album with local identifier: %{private}@, error: %@"
+ "Unable to get local identifier for shared album name: %{private}@"
+ "_migrateSelectedSharedAlbumNamesIfNecessary"
+ "_saveSelectedSharedAlbumCloudIdentifiersForNames:"
+ "addObject:"
+ "array"
+ "cloudIdentifier"
+ "cloudIdentifierMappingsForLocalIdentifiers:"
+ "count"
+ "enumerateObjectsUsingBlock:"
+ "error"
+ "fetchAssetCollectionsWithType:subtype:options:"
+ "length"
+ "localIdentifier"
+ "localizedTitle"
+ "selectedSharedAlbumCloudIdentifiers"
+ "setSelectedSharedAlbumCloudIdentifiers:"
+ "sharedPhotoLibrary"
+ "softlink:r:path:/System/Library/Frameworks/Photos.framework/Photos"
+ "stringValue"
+ "v32@?0@\"PHAssetCollection\"8Q16^B24"
- "selectedSharedAlbums"
- "setSelectedSharedAlbums:"

```
