## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3846.300.21.0.0
-  __TEXT.__text: 0x214c68
-  __TEXT.__objc_methlist: 0x1bfd8
+3846.300.54.0.0
+  __TEXT.__text: 0x214358
+  __TEXT.__objc_methlist: 0x1bf18
   __TEXT.__const: 0x4c60
-  __TEXT.__gcc_except_tab: 0x3ca0
-  __TEXT.__cstring: 0xcce9
-  __TEXT.__dlopen_cstrs: 0xa28
-  __TEXT.__oslogstring: 0xf9ba
+  __TEXT.__gcc_except_tab: 0x3c3c
+  __TEXT.__cstring: 0xcc69
+  __TEXT.__dlopen_cstrs: 0x97e
+  __TEXT.__oslogstring: 0xf90a
   __TEXT.__ustring: 0x12
   __TEXT.__constg_swiftt: 0x16d4
   __TEXT.__swift5_typeref: 0x1b0f

   __TEXT.__swift_as_entry: 0xb8
   __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift_as_cont: 0x158
-  __TEXT.__unwind_info: 0xbb38
+  __TEXT.__unwind_info: 0xbb00
   __TEXT.__eh_frame: 0x4000
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6780
-  __DATA_CONST.__objc_classlist: 0x11c0
+  __DATA_CONST.__const: 0x6730
+  __DATA_CONST.__objc_classlist: 0x11b0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9e48
+  __DATA_CONST.__objc_selrefs: 0x9dc0
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0xa28
+  __DATA_CONST.__objc_superrefs: 0xa20
   __DATA_CONST.__objc_arraydata: 0x268
-  __DATA_CONST.__got: 0x1dc0
+  __DATA_CONST.__got: 0x1dc8
   __AUTH_CONST.__const: 0x92b8
-  __AUTH_CONST.__cfstring: 0xe040
-  __AUTH_CONST.__objc_const: 0x2de88
+  __AUTH_CONST.__cfstring: 0xdfe0
+  __AUTH_CONST.__objc_const: 0x2dce8
   __AUTH_CONST.__objc_intobj: 0x5e8
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1de8
-  __AUTH.__objc_data: 0x5ea0
+  __AUTH_CONST.__auth_got: 0x1df0
+  __AUTH.__objc_data: 0x5e00
   __AUTH.__data: 0x860
-  __DATA.__objc_ivar: 0x1350
-  __DATA.__data: 0x3ab8
+  __DATA.__objc_ivar: 0x1348
+  __DATA.__data: 0x3ac8
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x6368
   __DATA_DIRTY.__data: 0x58
-  __DATA_DIRTY.__bss: 0x1158
+  __DATA_DIRTY.__bss: 0x1148
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ClassKit.framework/ClassKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14275
-  Symbols:   20232
-  CStrings:  3464
+  Functions: 14261
+  Symbols:   20205
+  CStrings:  3460
 
Symbols:
+ -[CNContactsAPIServiceAuthorizationCheck requireClientsAllowedToUseSPI]
+ -[CNContactsAPIServiceAuthorizationCheck setRequireClientsAllowedToUseSPI:]
+ -[CNNicknameProvider contactWithImageSafeForSharing:]
+ -[CNSharedProfileStateOracle contactIdentifier]
+ -[CNSharedProfileStateOracle setContactIdentifier:]
+ -[CNiOSContactFetcher _matchInfos:forPeople:]
+ -[_CNContactsAPIServiceAuthorizationChecker isConnectionAllowedToUseSPI]
+ -[_CNContactsAPIServiceAuthorizationChecker requireClientsAllowedToUseSPI]
+ -[_CNContactsAPIServiceAuthorizationChecker setRequireClientsAllowedToUseSPI:]
+ _CGImageSourceCreateThumbnailAtIndex
+ _CNImageUtilsCreateImageFromData
+ _CNImageUtilsIsImageDataAcceptableForSharedAvatar
+ _CNImageUtilsSharedAvatarDataFromImageData
+ _OBJC_IVAR_$_CNContactsAPIServiceAuthorizationCheck._requireClientsAllowedToUseSPI
+ _OBJC_IVAR_$_CNSharedProfileStateOracle._contactIdentifier
+ _OBJC_IVAR_$__CNContactsAPIServiceAuthorizationChecker._requireClientsAllowedToUseSPI
+ ___initializeThumbnailProperties
+ ___thumbnailProperties
+ ___thumbnailPropertiesOnce
+ _descriptionForActionType:.cn_once_object_76
+ _descriptionForActionType:.cn_once_token_76
+ _descriptionForUpdateState:.cn_once_object_77
+ _descriptionForUpdateState:.cn_once_token_77
+ _kCGImageSourceCreateThumbnailFromImageAlways
+ _kCGImageSourceCreateThumbnailWithTransform
+ _pthread_once
+ _sharableImageWhenResizeFails
- +[CNFakeSensitiveNicknameProvider makeIfEnabled]
- -[CNFakeSensitiveIMNicknameProvider .cxx_destruct]
- -[CNFakeSensitiveIMNicknameProvider allNicknamesForContact:]
- -[CNFakeSensitiveIMNicknameProvider cn_anyHandleForContact:]
- -[CNFakeSensitiveIMNicknameProvider contactsByRecordID]
- -[CNFakeSensitiveIMNicknameProvider forwardingTargetForSelector:]
- -[CNFakeSensitiveIMNicknameProvider identifiers]
- -[CNFakeSensitiveIMNicknameProvider realProvider]
- -[CNFakeSensitiveIMNicknameProvider setContactsByRecordID:]
- -[CNFakeSensitiveIMNicknameProvider setIdentifiers:]
- -[CNFakeSensitiveIMNicknameProvider setRealProvider:]
- -[CNFakeSensitiveNicknameProvider .cxx_destruct]
- -[CNFakeSensitiveNicknameProvider cn_makeSensitivityAnalysis]
- -[CNFakeSensitiveNicknameProvider cn_stablePosterArchiveDataForContact:]
- -[CNFakeSensitiveNicknameProvider fakeIMProvider]
- -[CNFakeSensitiveNicknameProvider initWithIdentifiers:]
- -[CNFakeSensitiveNicknameProvider realProvider]
- -[CNFakeSensitiveNicknameProvider setFakeIMProvider:]
- -[CNFakeSensitiveNicknameProvider setRealProvider:]
- -[CNFakeSensitiveNicknameProvider sharedWallpaperForNickname:]
- -[CNFakeSensitiveNicknameProvider sharedWatchWallpaperImageDataForNickname:]
- -[CNSharedProfileStateOracle cn_isFakeSensitiveDebugContact]
- _CGImageSourceGetType
- _CNImageUtilsIsImageDataInHEICFormat
- _CNImageUtilsIsImageDataOfFormatInUTIs
- _CNImageUtilsJPEGDataFromImageData
- _CNImageUtilsUTIFormatForImageData
- _OBJC_CLASS_$_CNFakeSensitiveIMNicknameProvider
- _OBJC_CLASS_$_CNFakeSensitiveNicknameProvider
- _OBJC_IVAR_$_CNFakeSensitiveIMNicknameProvider._contactsByRecordID
- _OBJC_IVAR_$_CNFakeSensitiveIMNicknameProvider._identifiers
- _OBJC_IVAR_$_CNFakeSensitiveIMNicknameProvider._realProvider
- _OBJC_IVAR_$_CNFakeSensitiveNicknameProvider._fakeIMProvider
- _OBJC_IVAR_$_CNFakeSensitiveNicknameProvider._realProvider
- _OBJC_METACLASS_$_CNFakeSensitiveIMNicknameProvider
- _OBJC_METACLASS_$_CNFakeSensitiveNicknameProvider
- _UTTypeHEIC
- __OBJC_$_CLASS_METHODS_CNFakeSensitiveNicknameProvider
- __OBJC_$_INSTANCE_METHODS_CNFakeSensitiveIMNicknameProvider
- __OBJC_$_INSTANCE_METHODS_CNFakeSensitiveNicknameProvider
- __OBJC_$_INSTANCE_VARIABLES_CNFakeSensitiveIMNicknameProvider
- __OBJC_$_INSTANCE_VARIABLES_CNFakeSensitiveNicknameProvider
- __OBJC_$_PROP_LIST_CNFakeSensitiveIMNicknameProvider
- __OBJC_$_PROP_LIST_CNFakeSensitiveNicknameProvider
- __OBJC_CLASS_RO_$_CNFakeSensitiveIMNicknameProvider
- __OBJC_CLASS_RO_$_CNFakeSensitiveNicknameProvider
- __OBJC_METACLASS_RO_$_CNFakeSensitiveIMNicknameProvider
- __OBJC_METACLASS_RO_$_CNFakeSensitiveNicknameProvider
- ___CNImageUtilsIsImageDataOfFormatInUTIs_block_invoke
- ___block_descriptor_40_e18_B16?0"NSString"8l
- _descriptionForActionType:.cn_once_object_78
- _descriptionForActionType:.cn_once_token_78
- _descriptionForUpdateState:.cn_once_object_79
- _descriptionForUpdateState:.cn_once_token_79
CStrings:
+ "Could not make the image acceptable for sharing, dropping image data to avoid BlastDoor rejection"
+ "Could not make the personal nickname image acceptable for sharing, dropping it to avoid BlastDoor rejection"
+ "Could not make the scaled image acceptable for sharing, dropping image data to avoid BlastDoor rejection"
+ "Resizing failed for an image BlastDoor would reject, dropping image data"
+ "This process is using a %@ predicate, which has not been optimized for Limited Access."
+ "not allowed to use SPI"
- "CNFakeSensitiveNicknameProviderContentType"
- "CNFakeSensitiveNicknameProviderEnabled"
- "CNFakeSensitiveNicknameProviderIdentifiers"
- "CNFakeSensitivePosterArchive."
- "FakeSensitive debug: ignoring shared-profile action %@ (with nicknames) for %{public}@ to preserve the faked poster"
- "FakeSensitive debug: ignoring shared-profile action %@ for %{public}@ to preserve the faked poster"
- "HEIC to JPEG conversion failed, dropping image data to avoid BlastDoor rejection"
- "Post-scale HEIC to JPEG conversion failed, dropping image data to avoid BlastDoor rejection"
- "Scaling failed for HEIC input, dropping image data to avoid BlastDoor rejection"
- "This process is using a %@ predicate, which has not been optimized for Limited Access. Please file a radar against Contacts | New Bugs if you see performance issues."
```
