## ArchiveService

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService`

```diff

-1827.3.2.0.0
-  __TEXT.__text: 0x2a728
-  __TEXT.__auth_stubs: 0x1460
-  __TEXT.__objc_stubs: 0x1c60
-  __TEXT.__objc_methlist: 0x7e4
-  __TEXT.__gcc_except_tab: 0x41b0
-  __TEXT.__const: 0x5b8
-  __TEXT.__objc_methname: 0x2573
-  __TEXT.__cstring: 0x1063
-  __TEXT.__objc_classname: 0x130
-  __TEXT.__objc_methtype: 0xe1c
-  __TEXT.__oslogstring: 0x1198
-  __TEXT.__unwind_info: 0x1108
-  __DATA_CONST.__auth_got: 0xa40
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xec0
-  __DATA_CONST.__cfstring: 0x920
-  __DATA_CONST.__objc_classlist: 0x28
+1827.4.3.2.0
+  __TEXT.__text: 0x31950
+  __TEXT.__auth_stubs: 0x19d0
+  __TEXT.__objc_stubs: 0x1ee0
+  __TEXT.__objc_methlist: 0x85c
+  __TEXT.__gcc_except_tab: 0x46e0
+  __TEXT.__const: 0x902
+  __TEXT.__objc_methname: 0x2892
+  __TEXT.__cstring: 0x23e2
+  __TEXT.__objc_classname: 0x152
+  __TEXT.__objc_methtype: 0xf9f
+  __TEXT.__oslogstring: 0x1486
+  __TEXT.__swift5_typeref: 0xc0
+  __TEXT.__swift5_reflstr: 0x95
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__constg_swiftt: 0x158
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_fieldmd: 0xb8
+  __TEXT.__swift5_proto: 0x14
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__unwind_info: 0x12f0
+  __TEXT.__eh_frame: 0xe8
+  __DATA_CONST.__auth_got: 0xcf8
+  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__auth_ptr: 0xf8
+  __DATA_CONST.__const: 0x1190
+  __DATA_CONST.__cfstring: 0x9c0
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x9a8
-  __DATA.__objc_selrefs: 0x880
+  __DATA.__objc_const: 0xa30
+  __DATA.__objc_selrefs: 0x928
   __DATA.__objc_ivar: 0x40
-  __DATA.__objc_data: 0x190
-  __DATA.__data: 0x338
-  __DATA.__bss: 0x520
+  __DATA.__objc_data: 0x270
+  __DATA.__data: 0x408
+  __DATA.__bss: 0x7e0
   __DATA.__common: 0xc
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/APFS.framework/APFS

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1ED52A7A-E9B5-3AEE-8E5F-46B567982BBF
-  Functions: 611
-  Symbols:   579
-  CStrings:  805
+  - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: BD09978B-821B-3600-9F62-C86699ECD4A1
+  Functions: 721
+  Symbols:   653
+  CStrings:  896
 
Symbols:
+ _AAExtractArchiveOutputStreamSetQuarantine
+ _AEAAuthDataCreateWithContext
+ _AEAAuthDataDestroy
+ _AEAAuthDataGetEntry
+ _AEAAuthDataGetEntryCount
+ _CFBooleanGetTypeID
+ _CFPreferencesCopyValue
+ _CFStringAppendCString
+ _NSFileGroupOwnerAccountID
+ _NSFileOwnerAccountID
+ _NSFilePosixPermissions
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_NSTextCheckingResult
+ _OBJC_CLASS_$_OS_os_log
+ _SecCertificateCopyKey
+ _SecCertificateCreateWithData
+ _SecCopyErrorMessageString
+ _SecKeyCopyExternalRepresentation
+ _SecPolicyCreateBasicX509
+ _SecTrustCreateWithCertificates
+ _SecTrustEvaluateWithError
+ _SecTrustSetVerifyDate
+ __Z14NoFollowPrefixv
+ __Z17SMBDomainIDPrefixv
+ __Z17USBDomainIDPrefixv
+ __Z19FilesFeatureEnabledPKc
+ __Z26NoFollowPrefixWithoutSlashv
+ __Z42UseFPv2EnumerationForExternalOrSMBDomainIDRK7TString
+ __ZN10TCFURLInfo15AreOnSameVolumeERKNSt3__110shared_ptrIKS_EES5_
+ __ZN10TCFURLInfo19GetVolumeIdentifierEPK7__CFURL
+ __ZN7TString6AppendEPKc
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __os_feature_enabled_impl
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_stdlib_reportUnimplementedInitializer
+ _kCFPreferencesAnyApplication
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _kCFURLVolumeIdentifierKey
+ _lchown
+ _malloc_size
+ _objc_allocWithZone
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocPartialClassInstance
+ _swift_dynamicCastObjCClass
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_isaMask
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRelease
+ _swift_willThrow
- _NSTemporaryDirectory
- _mkdtemp
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
- _objc_retain_x9
- _realpath$DARWIN_EXTSN
CStrings:
+ "\n?-----BEGIN CERTIFICATE-----\n([^-]+)\n-----END CERTIFICATE-----\n?"
+ " for certificate chain "
+ "/.nofollow"
+ "/.nofollow/"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3371: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "/AppleInternal/Library/BuildRoots/4~CHouugChnNzN38ZddrlHC4qh6QqD8sIFOvTYHfI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "@\"NSProgress\"68@0:8@\"NSArray\"16@\"NSString\"24Q32Q40@\"NSSecurityScopedURLWrapper\"48B56@?<v@?@\"NSSecurityScopedURLWrapper\"@\"NSString\"@\"NSError\">60"
+ "@\"NSProgress\"72@0:8@\"FPSandboxingURLWrapper\"16@\"NSArray\"24Q32@\"NSSecurityScopedURLWrapper\"40Q48B56B60@?<v@?@\"NSSecurityScopedURLWrapper\"@\"NSError\">64"
+ "@24@0:8^@16"
+ "@40@0:8@16B24B28^@32"
+ "@40@0:8^v16@24^@32"
+ "@68@0:8@16@24Q32Q40@48B56@?60"
+ "@68@0:8Q16@24@32Q40B48@?52@?60"
+ "@72@0:8@16@24Q32@40Q48B56B60@?64"
+ "AAExtractArchiveOutputStreamSetQuarantine failed"
+ "AEAAuthInfo.init found %{public}i entries in auth data"
+ "Apple Archive type %lu isn't on allow list: %@"
+ "ArchiveContent"
+ "ArchiveService.AEAAuthInfo"
+ "Auth data not set or could not be read."
+ "B48@0:8^^{AEAContext_impl}16^{?=^{AAByteStream_impl}^{AAByteStream_impl}^{AAByteStream_impl}^{AEAContext_impl}}24@32^@40"
+ "B52@0:8@16B24^^{AEAContext_impl}28^{?=^{AAByteStream_impl}^{AAByteStream_impl}^{AAByteStream_impl}^{AEAContext_impl}}36^@44"
+ "B56@0:8@16@24^@32Q40^@48"
+ "B84@0:8i16@20@28B36@40Q48@56@64B72^@76"
+ "Could not get SecCertificates from data for key '"
+ "Could not get SecCertificates from data for key '%{public}s'"
+ "Could not obtain file coordination for %{public}@: %@"
+ "Couldn't get nofollow url for %{public}@"
+ "DOCFeature.override.DocumentManager."
+ "DSEnumeration_SMB_FPv2"
+ "DSEnumeration_USB_FPv2"
+ "DocumentManager"
+ "Expected a single top-level item but found %lu: %@"
+ "Failed getting protected group container %{public}@"
+ "Failed getting public key: %@"
+ "Failed removing placeholder %{public}@: %@"
+ "Failed to create a String from Data passed in"
+ "Failed to create extraction dir in secure container"
+ "Failed to create regular expression from pattern '%{public}s'"
+ "Failed to create sandbox directory"
+ "Failed to create sandbox directory. %s"
+ "Failed to create sandbox parent directory. %@"
+ "Failed to create temporary directory: %@"
+ "Failed to enumerate sandbox parent directory: %@"
+ "Failed to get key_length and data_size from __AEAAuthDataGetEntry - status is: "
+ "Failed to get key_length and data_size from __AEAAuthDataGetEntry - status is: %{public}i"
+ "Failed to move %{public}@ into place at %{public}@:  %@"
+ "Failed to perform coordination with intents %{public}@ with error: %@"
+ "Failed to remove orphaned item %{public}@: %@"
+ "Failed to replace %{public}@ at %{public}@  %@"
+ "Failed to set public key: (%d)"
+ "Failed to set trust verify date on certificate chain "
+ "Failure from __AEAAuthDataGetEntry - Got non-zero status "
+ "Failure from __AEAAuthDataGetEntry - Got non-zero status %{public}i for key '%{public}s'"
+ "File coordination timed out for %{public}@, skipping deletion"
+ "Found zero certificates in string."
+ "Invalid auth data: %@"
+ "No data found for auth data entry %{public}s"
+ "No data found for auth data entry '"
+ "Path does not begin with a '/' : %{public}@"
+ "Performing cross-volume move of %{public}@ to %{public}@"
+ "Removed orphaned item: %{public}@"
+ "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,R"
+ "Trusting certificate chain %{public}s"
+ "Unknown failure from SecTrustCreateWithCertificates"
+ "Unknown failure from SecTrustEvaluateWithError for certificate chain "
+ "We do not trust the certificate chain "
+ "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@0:8"
+ "_TtC14ArchiveService11AEAAuthInfo"
+ "_cleanupOrphanedItemsIn:"
+ "_openAEADecryptionStreamForXcodeAEAWithContext:combinedStreamState:url:error:"
+ "_openAEADecryptionStreamWithPassphrases:addToKeychain:aeaContext:combinedStreamState:error:"
+ "_protectedAppGroupContainer"
+ "_replacePlaceholder:withItem:resultingItem:options:error:"
+ "_setUpSecureExtractionDirectory:"
+ "_temporaryURLAppropriateForURL:calledFromCLI:calledFromLegacyAPI:error:"
+ "_unarchiveFromArchiveFD:url:passphrases:addToKeychain:destinationURL:formats:progress:readItemGroup:isAppleArchive:error:"
+ "appleArchiveSigningPublicKey"
+ "archiveItemsWithURLWrappers:passphrase:options:compressionFormat:destinationFolderURLWrapper:usePlaceholder:completionHandler:"
+ "arrayByAddingObject:"
+ "authInfoInternal"
+ "bytes"
+ "cancel"
+ "com.apple.ias.signature.certificate-chain"
+ "containerURLForSecurityApplicationGroupIdentifier:"
+ "dealloc"
+ "group.com.apple.desktopservices.ArchiveService.AppGroupContainer"
+ "init()"
+ "initWithAuthData:trustVerifyDate:error:"
+ "initWithFilePresenter:"
+ "initWithPattern:options:error:"
+ "insertObject:atIndex:"
+ "isWritableFileAtPath:"
+ "matchesInString:options:range:"
+ "moveItemAtURL:toURL:error:"
+ "numberOfRanges"
+ "numberWithUnsignedInt:"
+ "performActionOfKind:onResourcesWithURLWrappers:clientDestinationFolderURLWrapper:options:calledFromLegacyAPI:actionHandler:completionHandler:"
+ "rangeAtIndex:"
+ "unarchiveItemWithURLWrapper:passphrases:options:destinationFolderURLWrapper:acceptedFormats:exportsStreamingReceiver:usePlaceholder:completionHandler:"
+ "writingIntentWithURL:options:"
- "@\"NSProgress\"64@0:8@\"NSArray\"16@\"NSString\"24B32Q36@\"NSSecurityScopedURLWrapper\"44B52@?<v@?@\"NSSecurityScopedURLWrapper\"@\"NSString\"@\"NSError\">56"
- "@\"NSProgress\"68@0:8@\"FPSandboxingURLWrapper\"16@\"NSArray\"24B32@\"NSSecurityScopedURLWrapper\"36Q44B52B56@?<v@?@\"NSSecurityScopedURLWrapper\"@\"NSError\">60"
- "@36@0:8@16B24^@28"
- "@60@0:8Q16@24@32B40@?44@?52"
- "@64@0:8@16@24B32Q36@44B52@?56"
- "@68@0:8@16@24B32@36Q44B52B56@?60"
- "Apple Archive format not allowed: %@"
- "Archiving__XXXXXX"
- "B80@0:8i16@20@28B36@40Q48@56@64^@72"
- "Couldn't copy temporary directory name"
- "Couldn't copy temporary directory name: %@"
- "Couldn't create temporary directory"
- "Couldn't create temporary directory: %@"
- "Couldn't fetch realpath for %{public}@"
- "Couldn't get temporary directory"
- "Failed to create temporary dir: %@"
- "Failed to perform coordinated read with intents %{public}@ with error: %@"
- "__temporaryURLAppropriateForURL:calledFromLegacyAPI:error:"
- "_temporaryURLAppropriateForURL:calledFromLegacyAPI:error:"
- "_unarchiveFromArchiveFD:url:passphrases:addToKeychain:destinationURL:formats:progress:readItemGroup:error:"
- "archiveItemsWithURLWrappers:passphrase:addToKeychain:compressionFormat:destinationFolderURLWrapper:usePlaceholder:completionHandler:"
- "hasDirectoryPath"
- "performActionOfKind:onResourcesWithURLWrappers:clientDestinationFolderURLWrapper:calledFromLegacyAPI:actionHandler:completionHandler:"
- "unarchiveItemWithURLWrapper:passphrases:addToKeychain:destinationFolderURLWrapper:acceptedFormats:exportsStreamingReceiver:usePlaceholder:completionHandler:"

```
