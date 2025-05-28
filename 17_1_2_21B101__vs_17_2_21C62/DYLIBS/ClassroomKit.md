## ClassroomKit

> `/System/Library/PrivateFrameworks/ClassroomKit.framework/ClassroomKit`

```diff

-101.1.0.0.0
-  __TEXT.__text: 0xae038
+103.7.0.0.0
+  __TEXT.__text: 0xaf808
   __TEXT.__auth_stubs: 0xf10
-  __TEXT.__objc_methlist: 0x10614
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x8760
-  __TEXT.__oslogstring: 0x3f0e
-  __TEXT.__gcc_except_tab: 0x6f8
+  __TEXT.__objc_methlist: 0x1083c
+  __TEXT.__const: 0x118
+  __TEXT.__cstring: 0x88de
+  __TEXT.__oslogstring: 0x4017
+  __TEXT.__gcc_except_tab: 0x708
   __TEXT.__ustring: 0x37e
   __TEXT.__dlopen_cstrs: 0x44
-  __TEXT.__unwind_info: 0x35f4
-  __TEXT.__objc_classname: 0x42de
-  __TEXT.__objc_methname: 0x22d1e
-  __TEXT.__objc_methtype: 0x5cb1
-  __TEXT.__objc_stubs: 0x15880
-  __DATA_CONST.__got: 0x518
-  __DATA_CONST.__const: 0x2820
-  __DATA_CONST.__objc_classlist: 0xed0
-  __DATA_CONST.__objc_catlist: 0xc0
-  __DATA_CONST.__objc_protolist: 0x440
+  __TEXT.__unwind_info: 0x365c
+  __TEXT.__objc_classname: 0x4392
+  __TEXT.__objc_methname: 0x23324
+  __TEXT.__objc_methtype: 0x5d20
+  __TEXT.__objc_stubs: 0x15ac0
+  __DATA_CONST.__got: 0x528
+  __DATA_CONST.__const: 0x2910
+  __DATA_CONST.__objc_classlist: 0xef0
+  __DATA_CONST.__objc_catlist: 0xd0
+  __DATA_CONST.__objc_protolist: 0x448
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1cfa8
-  __DATA_CONST.__objc_selrefs: 0x6978
+  __DATA_CONST.__objc_const: 0x1d6f8
+  __DATA_CONST.__objc_selrefs: 0x6a48
   __DATA_CONST.__objc_arraydata: 0x2a8
-  __AUTH_CONST.__cfstring: 0x8de0
-  __AUTH_CONST.__objc_const: 0xcd20
-  __AUTH_CONST.__const: 0x1740
+  __AUTH_CONST.__cfstring: 0x8f00
+  __AUTH_CONST.__objc_const: 0xcf50
+  __AUTH_CONST.__const: 0x17a0
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x798
-  __AUTH.__objc_data: 0x6ef0
+  __AUTH.__objc_data: 0x7030
   __DATA.__objc_protorefs: 0x68
-  __DATA.__objc_classrefs: 0xd70
-  __DATA.__objc_superrefs: 0xbd8
-  __DATA.__objc_ivar: 0x1278
-  __DATA.__data: 0x3308
+  __DATA.__objc_classrefs: 0xd88
+  __DATA.__objc_superrefs: 0xbf0
+  __DATA.__objc_ivar: 0x12a4
+  __DATA.__data: 0x3368
   __DATA.__bss: 0x1b8
   __DATA_DIRTY.__objc_data: 0x2530
-  __DATA_DIRTY.__bss: 0x5f0
+  __DATA_DIRTY.__bss: 0x600
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5855
-  Symbols:   21462
-  CStrings:  8333
+  Functions: 5905
+  Symbols:   21646
+  CStrings:  8415
 
Symbols:
+ +[CRKASMConcreteNameComponents annotatedStringFromNameComponents:configurationBlock:cleanupBlock:]
+ +[CRKASMConcreteNameComponents makeFamilyNameGivenNameWithComponents:]
+ +[CRKFetchEasyMAIDSignInEligibilityRequest allowlistedClassForResultObject]
+ +[CRKFetchEasyMAIDSignInEligibilityRequest supportsSecureCoding]
+ +[CRKFetchEasyMAIDSignInEligibilityResultObject supportsSecureCoding]
+ +[CRKRemoveSignInHistoryEntriesRequest allowlistedClassForResultObject]
+ +[CRKRemoveSignInHistoryEntriesRequest supportsSecureCoding]
+ -[CLSPerson(CRKReverseConformance) isAccountATOLocked]
+ -[CLSPerson(CRKReverseConformance) isAccountFailedPasswordLocked]
+ -[CRKASMConcreteNameComponents attributedFullName]
+ -[CRKASMConcreteUser isAccountATOLocked]
+ -[CRKASMConcreteUser isAccountLockedDueToFailedLoginAttempts]
+ -[CRKASMEasyMAIDSignInRosterProvider .cxx_destruct]
+ -[CRKASMEasyMAIDSignInRosterProvider configuration]
+ -[CRKASMEasyMAIDSignInRosterProvider fetchEligibilityForEasyMAIDSignInWithCompletion:]
+ -[CRKASMEasyMAIDSignInRosterProvider initWithRosterProviderGenerator:]
+ -[CRKASMEasyMAIDSignInRosterProvider instructorRosterProviderWithoutKeychain]
+ -[CRKASMEasyMAIDSignInRosterProvider providerGenerator]
+ -[CRKASMRosterProviderFactory makeEasyMAIDSignInRosterProvider]
+ -[CRKClassKitFacadeDecoratorBase makeQueryForLocationsAllowingEasyStudentSignInForPersonID:]
+ -[CRKConcreteClassKitFacade makeQueryForLocationsAllowingEasyStudentSignInForPersonID:]
+ -[CRKConcreteClassKitFacade makeQueryForLocationsAllowingEasyStudentSignInForPersonID:].cold.1
+ -[CRKConcreteClassKitRosterRequirements makeQueryForLocationsAllowingEasyStudentSignInForPersonID:]
+ -[CRKConcreteFeatureFlags isEasyMAIDPermissionCheckingEnabled]
+ -[CRKFetchEasyMAIDSignInEligibilityResultObject .cxx_destruct]
+ -[CRKFetchEasyMAIDSignInEligibilityResultObject eligibility]
+ -[CRKFetchEasyMAIDSignInEligibilityResultObject encodeWithCoder:]
+ -[CRKFetchEasyMAIDSignInEligibilityResultObject initWithCoder:]
+ -[CRKFetchEasyMAIDSignInEligibilityResultObject setEligibility:]
+ -[CRKFetchSignInHistoryResultObject historyVersion]
+ -[CRKFetchSignInHistoryResultObject isTruncated]
+ -[CRKFetchSignInHistoryResultObject limit]
+ -[CRKFetchSignInHistoryResultObject ownerAppleID]
+ -[CRKFetchSignInHistoryResultObject setHistoryVersion:]
+ -[CRKFetchSignInHistoryResultObject setIsTruncated:]
+ -[CRKFetchSignInHistoryResultObject setLimit:]
+ -[CRKFetchSignInHistoryResultObject setOwnerAppleID:]
+ -[CRKRemoveSignInHistoryEntriesRequest .cxx_destruct]
+ -[CRKRemoveSignInHistoryEntriesRequest encodeWithCoder:]
+ -[CRKRemoveSignInHistoryEntriesRequest identifiers]
+ -[CRKRemoveSignInHistoryEntriesRequest initWithCoder:]
+ -[CRKRemoveSignInHistoryEntriesRequest setIdentifiers:]
+ -[NSAttributedString(CRKAdditions) crk_familyNameRange]
+ _NSPersonNameComponentFamilyName
+ _NSPersonNameComponentKey
+ _OBJC_CLASS_$_AKURLBag
+ _OBJC_CLASS_$_CRKASMEasyMAIDSignInRosterProvider
+ _OBJC_CLASS_$_CRKFetchEasyMAIDSignInEligibilityRequest
+ _OBJC_CLASS_$_CRKFetchEasyMAIDSignInEligibilityResultObject
+ _OBJC_CLASS_$_CRKRemoveSignInHistoryEntriesRequest
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_IVAR_$_CRKASMConcreteNameComponents._attributedFullName
+ _OBJC_IVAR_$_CRKASMConcreteUser._accountATOLocked
+ _OBJC_IVAR_$_CRKASMConcreteUser._accountLockedDueToFailedLoginAttempts
+ _OBJC_IVAR_$_CRKASMEasyMAIDSignInRosterProvider._configuration
+ _OBJC_IVAR_$_CRKASMEasyMAIDSignInRosterProvider._instructorRosterProviderWithoutKeychain
+ _OBJC_IVAR_$_CRKASMEasyMAIDSignInRosterProvider._providerGenerator
+ _OBJC_IVAR_$_CRKFetchEasyMAIDSignInEligibilityResultObject._eligibility
+ _OBJC_IVAR_$_CRKFetchSignInHistoryResultObject._historyVersion
+ _OBJC_IVAR_$_CRKFetchSignInHistoryResultObject._isTruncated
+ _OBJC_IVAR_$_CRKFetchSignInHistoryResultObject._limit
+ _OBJC_IVAR_$_CRKFetchSignInHistoryResultObject._ownerAppleID
+ _OBJC_IVAR_$_CRKRemoveSignInHistoryEntriesRequest._identifiers
+ _OBJC_METACLASS_$_CRKASMEasyMAIDSignInRosterProvider
+ _OBJC_METACLASS_$_CRKFetchEasyMAIDSignInEligibilityRequest
+ _OBJC_METACLASS_$_CRKFetchEasyMAIDSignInEligibilityResultObject
+ _OBJC_METACLASS_$_CRKRemoveSignInHistoryEntriesRequest
+ __OBJC_$_CATEGORY_CLSPerson_$_CRKReverseConformance
+ __OBJC_$_CATEGORY_NSAttributedString_$_CRKAdditions
+ __OBJC_$_CLASS_METHODS_CRKFetchEasyMAIDSignInEligibilityRequest
+ __OBJC_$_CLASS_METHODS_CRKFetchEasyMAIDSignInEligibilityResultObject
+ __OBJC_$_CLASS_METHODS_CRKRemoveSignInHistoryEntriesRequest
+ __OBJC_$_INSTANCE_METHODS_CLSPerson(CRKReverseConformance)
+ __OBJC_$_INSTANCE_METHODS_CRKASMEasyMAIDSignInRosterProvider
+ __OBJC_$_INSTANCE_METHODS_CRKFetchEasyMAIDSignInEligibilityResultObject
+ __OBJC_$_INSTANCE_METHODS_CRKRemoveSignInHistoryEntriesRequest
+ __OBJC_$_INSTANCE_METHODS_NSAttributedString(CRKAdditions)
+ __OBJC_$_INSTANCE_VARIABLES_CRKASMEasyMAIDSignInRosterProvider
+ __OBJC_$_INSTANCE_VARIABLES_CRKFetchEasyMAIDSignInEligibilityResultObject
+ __OBJC_$_INSTANCE_VARIABLES_CRKRemoveSignInHistoryEntriesRequest
+ __OBJC_$_PROP_LIST_CRKASMEasyMAIDSignInRosterProvider
+ __OBJC_$_PROP_LIST_CRKClassKitPerson
+ __OBJC_$_PROP_LIST_CRKFetchEasyMAIDSignInEligibilityResultObject
+ __OBJC_$_PROP_LIST_CRKRemoveSignInHistoryEntriesRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRKClassKitPerson
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRKClassKitPerson
+ __OBJC_$_PROTOCOL_REFS_CRKClassKitPerson
+ __OBJC_CLASS_PROTOCOLS_$_CLSPerson(CRKReverseConformance)
+ __OBJC_CLASS_RO_$_CRKASMEasyMAIDSignInRosterProvider
+ __OBJC_CLASS_RO_$_CRKFetchEasyMAIDSignInEligibilityRequest
+ __OBJC_CLASS_RO_$_CRKFetchEasyMAIDSignInEligibilityResultObject
+ __OBJC_CLASS_RO_$_CRKRemoveSignInHistoryEntriesRequest
+ __OBJC_LABEL_PROTOCOL_$_CRKClassKitPerson
+ __OBJC_METACLASS_RO_$_CRKASMEasyMAIDSignInRosterProvider
+ __OBJC_METACLASS_RO_$_CRKFetchEasyMAIDSignInEligibilityRequest
+ __OBJC_METACLASS_RO_$_CRKFetchEasyMAIDSignInEligibilityResultObject
+ __OBJC_METACLASS_RO_$_CRKRemoveSignInHistoryEntriesRequest
+ __OBJC_PROTOCOL_$_CRKClassKitPerson
+ ___55-[NSAttributedString(CRKAdditions) crk_familyNameRange]_block_invoke
+ ___63-[CRKASMRosterProviderFactory makeEasyMAIDSignInRosterProvider]_block_invoke
+ ___70+[CRKASMConcreteNameComponents makeFamilyNameGivenNameWithComponents:]_block_invoke
+ ___70+[CRKASMConcreteNameComponents makeFamilyNameGivenNameWithComponents:]_block_invoke_2
+ ___86-[CRKASMEasyMAIDSignInRosterProvider fetchEligibilityForEasyMAIDSignInWithCompletion:]_block_invoke
+ ___86-[CRKASMEasyMAIDSignInRosterProvider fetchEligibilityForEasyMAIDSignInWithCompletion:]_block_invoke.39
+ ___86-[CRKASMEasyMAIDSignInRosterProvider fetchEligibilityForEasyMAIDSignInWithCompletion:]_block_invoke_2
+ ___86-[CRKASMEasyMAIDSignInRosterProvider fetchEligibilityForEasyMAIDSignInWithCompletion:]_block_invoke_2.40
+ ___86-[CRKASMEasyMAIDSignInRosterProvider fetchEligibilityForEasyMAIDSignInWithCompletion:]_block_invoke_3
+ ___block_descriptor_40_e8_32r_e27_v40?08{_NSRange=QQ}16^B32lr32l8
+ ___block_descriptor_40_e8_32s_e68_"<CRKASMRosterProviding>"16?0"CRKASMRosterProviderConfiguration"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e46_v24?0"<CRKClassKitCurrentUser>"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
+ _objc_msgSend$annotatedStringFromNameComponents:configurationBlock:cleanupBlock:
+ _objc_msgSend$annotatedStringFromPersonNameComponents:
+ _objc_msgSend$attributedFullName
+ _objc_msgSend$axmAccountStatus
+ _objc_msgSend$eligibility
+ _objc_msgSend$enumerateAttribute:inRange:options:usingBlock:
+ _objc_msgSend$historyVersion
+ _objc_msgSend$identifiers
+ _objc_msgSend$initWithRosterProviderGenerator:
+ _objc_msgSend$isAccountATOLocked
+ _objc_msgSend$isAccountFailedPasswordLocked
+ _objc_msgSend$isAccountLockedDueToFailedLoginAttempts
+ _objc_msgSend$isEasyMAIDPermissionCheckingEnabled
+ _objc_msgSend$isEasyStudentSignInDisabled
+ _objc_msgSend$isTruncated
+ _objc_msgSend$limit
+ _objc_msgSend$makeFamilyNameGivenNameWithComponents:
+ _objc_msgSend$makeQueryForLocationsAllowingEasyStudentSignInForPersonID:
+ _objc_msgSend$ownerAppleID
+ _objc_msgSend$providerGenerator
+ _objc_msgSend$sharedBag
- +[CRKASMConcreteNameComponents makeGivenNameFamilyInitialWithComponents:]
- +[NSLocale(CRKAdditions) crk_canShowGivenNameFamilyInitial]
- -[CRKASMConcreteNameComponents givenNameFamilyInitial]
- -[CRKASMRosterProviderFactory makeInstructorRosterProviderWithoutKeychain]
- _OBJC_IVAR_$_CRKASMConcreteNameComponents._givenNameFamilyInitial
- ___block_literal_global.15
- _objc_msgSend$_localizedShortNameForComponents:withStyle:options:
- _objc_msgSend$givenNameFamilyInitial
- _objc_msgSend$makeGivenNameFamilyInitialWithComponents:
CStrings:
+ "\x11!"
+ "<%@: %p { givenName = %@, phoneticGivenName = %@, familyName = %@, phoneticFamilyName = %@, fullName = %@, phoneticFullName = %@, monogram = %@, attributedFullName = %@ }>"
+ "<%@: %p { identifier = %@, appleID = %@, nameComponents = %@, isFederated = %@, isAccountLockedDueToFailedLoginAttempts = %@, isAccountATOLocked = %@ }>"
+ "@\"<CRKASMRosterProviding>\"16@?0@\"CRKASMRosterProviderConfiguration\"8"
+ "@\"<CRKClassKitQuery>\"24@0:8@\"NSString\"16"
+ "@\"NSAttributedString\""
+ "@\"NSAttributedString\"16@0:8"
+ "CRKASMEasyMAIDSignInRosterProvider"
+ "CRKClassKitPerson"
+ "CRKFetchEasyMAIDSignInEligibilityRequest"
+ "CRKFetchEasyMAIDSignInEligibilityResultObject"
+ "CRKRemoveSignInHistoryEntriesRequest"
+ "EasyMAIDPermissionChecking"
+ "EasyMAIDPermissionChecking feature flag is disabled in the Classroom domain. Allowing Easy MAID Sign In."
+ "Failed to create CLSQuery for organizations allowing Easy MAID Sign In for user with object ID: %{public}@"
+ "Found %lu locations allowing EasyMAID for %{public}@"
+ "T@\"<CRKASMRosterProviding>\",R,N,V_instructorRosterProviderWithoutKeychain"
+ "T@\"NSArray\",C,N,V_identifiers"
+ "T@\"NSAttributedString\",R,C,N"
+ "T@\"NSAttributedString\",R,C,N,V_attributedFullName"
+ "T@\"NSDictionary\",C,N,V_eligibility"
+ "T@\"NSString\",C,N,V_ownerAppleID"
+ "T@?,R,N,V_providerGenerator"
+ "TB,N,V_isTruncated"
+ "TB,R,N,GisAccountATOLocked"
+ "TB,R,N,GisAccountATOLocked,V_accountATOLocked"
+ "TB,R,N,GisAccountFailedPasswordLocked"
+ "TB,R,N,GisAccountLockedDueToFailedLoginAttempts"
+ "TB,R,N,GisAccountLockedDueToFailedLoginAttempts,V_accountLockedDueToFailedLoginAttempts"
+ "TB,R,N,GisEasyMAIDPermissionCheckingEnabled"
+ "TB,R,N,GisFederatedAccount"
+ "TQ,N,V_historyVersion"
+ "TQ,N,V_limit"
+ "_accountATOLocked"
+ "_accountLockedDueToFailedLoginAttempts"
+ "_attributedFullName"
+ "_eligibility"
+ "_historyVersion"
+ "_identifiers"
+ "_instructorRosterProviderWithoutKeychain"
+ "_isTruncated"
+ "_limit"
+ "_ownerAppleID"
+ "_providerGenerator"
+ "accountATOLocked"
+ "accountFailedPasswordLocked"
+ "accountLockedDueToFailedLoginAttempts"
+ "annotatedStringFromNameComponents:configurationBlock:cleanupBlock:"
+ "annotatedStringFromPersonNameComponents:"
+ "attributedFullName"
+ "axmAccountStatus"
+ "countOfLocationsAllowingEasyMAIDSignIn"
+ "crk_familyNameRange"
+ "easyMAIDPermissionCheckingEnabled"
+ "eligibility"
+ "enumerateAttribute:inRange:options:usingBlock:"
+ "federatedAccount"
+ "fetchEligibilityForEasyMAIDSignInWithCompletion:"
+ "givenName, phoneticGivenName, familyName, phoneticFamilyName, fullName, phoneticFullName, monogram, attributedFullName"
+ "historyVersion"
+ "identifiers"
+ "initWithRosterProviderGenerator:"
+ "instructorRosterProviderWithoutKeychain"
+ "isAccountATOLocked"
+ "isAccountFailedPasswordLocked"
+ "isAccountLockedDueToFailedLoginAttempts"
+ "isEasyMAIDPermissionCheckingEnabled"
+ "isEasyStudentSignInDisabled"
+ "isEasyStudentSignInDisabledByServer"
+ "isNonStudent"
+ "isPermissionCheckingEnabled"
+ "isTruncated"
+ "limit"
+ "makeEasyMAIDSignInRosterProvider"
+ "makeFamilyNameGivenNameWithComponents:"
+ "makeQueryForLocationsAllowingEasyStudentSignInForPersonID:"
+ "ownerAppleID"
+ "providerGenerator"
+ "setEligibility:"
+ "setHistoryVersion:"
+ "setIdentifiers:"
+ "setIsTruncated:"
+ "setLimit:"
+ "setOwnerAppleID:"
+ "sharedBag"
+ "v40@?0@8{_NSRange=QQ}16^B32"
+ "{_NSRange=QQ}16@0:8"
- "<%@: %p { givenName = %@, phoneticGivenName = %@, familyName = %@, phoneticFamilyName = %@, fullName = %@, phoneticFullName = %@, monogram = %@, givenNameFamilyInitial = %@ }>"
- "<%@: %p { identifier = %@, appleID = %@, nameComponents = %@, isFederated = %@}>"
- "T@\"NSString\",R,C,N,V_givenNameFamilyInitial"
- "_givenNameFamilyInitial"
- "_localizedShortNameForComponents:withStyle:options:"
- "crk_canShowGivenNameFamilyInitial"
- "el"
- "en"
- "givenName, phoneticGivenName, familyName, phoneticFamilyName, fullName, phoneticFullName, monogram, givenNameFamilyInitial"
- "givenNameFamilyInitial"
- "makeGivenNameFamilyInitialWithComponents:"
- "makeInstructorRosterProviderWithoutKeychain"

```
