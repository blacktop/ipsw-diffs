## FeedbackCore

> `/System/Library/PrivateFrameworks/FeedbackCore.framework/Versions/A/FeedbackCore`

```diff

-139.9.0.0.0
-  __TEXT.__text: 0xf411c
-  __TEXT.__auth_stubs: 0x19c0
-  __TEXT.__objc_methlist: 0x64ac
-  __TEXT.__const: 0xe24
-  __TEXT.__cstring: 0x884c
-  __TEXT.__oslogstring: 0x85b2
-  __TEXT.__gcc_except_tab: 0x173c
+150.8.1.0.0
+  __TEXT.__text: 0xf45cc
+  __TEXT.__auth_stubs: 0x1990
+  __TEXT.__objc_methlist: 0x6cdc
+  __TEXT.__const: 0xe14
+  __TEXT.__cstring: 0x83ec
+  __TEXT.__oslogstring: 0x85f2
+  __TEXT.__gcc_except_tab: 0x1734
   __TEXT.__ustring: 0xdc
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__constg_swiftt: 0x58c
-  __TEXT.__swift5_typeref: 0x11e2
+  __TEXT.__constg_swiftt: 0x5e4
+  __TEXT.__swift5_typeref: 0x11ee
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x2a4
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_capture: 0x8a0
   __TEXT.__swift5_proto: 0x70
-  __TEXT.__swift5_types: 0x50
-  __TEXT.__swift5_fieldmd: 0x330
-  __TEXT.__unwind_info: 0x3168
-  __TEXT.__eh_frame: 0x13c0
+  __TEXT.__swift5_types: 0x58
+  __TEXT.__swift5_fieldmd: 0x350
+  __TEXT.__unwind_info: 0x31a0
+  __TEXT.__eh_frame: 0x1388
   __TEXT.__objc_classname: 0xa10
-  __TEXT.__objc_methname: 0x11f6c
+  __TEXT.__objc_methname: 0x1204d
   __TEXT.__objc_methtype: 0x18e6
-  __TEXT.__objc_stubs: 0xd9e0
-  __DATA_CONST.__got: 0xb80
-  __DATA_CONST.__const: 0xef0
-  __DATA_CONST.__objc_classlist: 0x310
+  __TEXT.__objc_stubs: 0xda60
+  __DATA_CONST.__got: 0xba0
+  __DATA_CONST.__const: 0xf58
+  __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a48
+  __DATA_CONST.__objc_selrefs: 0x4ba8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x4c8
-  __AUTH_CONST.__auth_got: 0xcf0
+  __AUTH_CONST.__auth_got: 0xcd8
   __AUTH_CONST.__const: 0x54b8
-  __AUTH_CONST.__cfstring: 0x8240
-  __AUTH_CONST.__objc_const: 0xea50
+  __AUTH_CONST.__cfstring: 0x8280
+  __AUTH_CONST.__objc_const: 0xdd18
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x468
-  __AUTH.__objc_data: 0x22d8
-  __AUTH.__data: 0x2b8
+  __AUTH.__objc_data: 0x2438
+  __AUTH.__data: 0x300
   __DATA.__objc_ivar: 0x414
-  __DATA.__data: 0x1428
+  __DATA.__data: 0x1398
   __DATA.__bss: 0x12a0
-  __DATA.__common: 0x140
+  __DATA.__common: 0x120
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/Versions/A/AppleIDSSOAuthentication
   - /System/Library/PrivateFrameworks/AppleSystemInfo.framework/Versions/A/AppleSystemInfo
+  - /System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
   - /System/Library/PrivateFrameworks/AuthKitUI.framework/Versions/A/AuthKitUI
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/Versions/A/DiagnosticExtensions

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 2CADFC6F-D64E-3344-B9D1-BA2D6A2FDFC7
-  Functions: 4559
-  Symbols:   7644
-  CStrings:  6707
+  UUID: 8C9E2247-2AD6-332A-9705-718C74384C42
+  Functions: 4602
+  Symbols:   7724
+  CStrings:  6699
 
Symbols:
+ +[FBKAnswer answerTypeFromString:].cold.1
+ +[FBKAppScanMacOS _allAppURLs].cold.2
+ +[FBKAppScanMacOS denyListedApps].cold.1
+ +[FBKBugForm bugFormRoleFromString:].cold.1
+ +[FBKBugForm bugFormTypeFromString:].cold.1
+ +[FBKBugFormStub sortDescriptor].cold.1
+ +[FBKConstants helpBookName].cold.1
+ +[FBKDeviceManager supportedPlatforms].cold.1
+ +[FBKEnhancedLoggingPersistence sharedInstance].cold.1
+ +[FBKFeedbackFollowup followupTypeFromString:].cold.1
+ +[FBKFeedbackFollowupResponse followupResponseTypeFromString:].cold.1
+ +[FBKFileCollector diskAccessQueue].cold.1
+ +[FBKFileManager humansCanReadFile:].cold.1
+ +[FBKLaunchAction hostBundleIdentifier].cold.1
+ +[FBKLicenseAgreement hasAgreedToCurrentLicenseAgreement].cold.1
+ +[FBKLog appHandle].cold.1
+ +[FBKLog appleConnect].cold.1
+ +[FBKLog attachHandle].cold.1
+ +[FBKLog clientHandle].cold.1
+ +[FBKLog data].cold.1
+ +[FBKLog ded].cold.1
+ +[FBKLog ffu].cold.1
+ +[FBKLog model].cold.1
+ +[FBKLog net].cold.1
+ +[FBKLog reachability].cold.1
+ +[FBKLog sp2].cold.1
+ +[FBKLog upload].cold.1
+ +[FBKRequestsLog sharedInstance].cold.1
+ +[FBKSharedConstants isEnhancedLoggingEnabled].cold.1
+ +[FBKSharedConstants listsFormsFetchedByTat].cold.1
+ +[FBKTimeIntervals log].cold.1
+ +[FBKTimeIntervals sharedInstance].cold.1
+ +[NSString(FBKUtils) whitespaceSet].cold.1
+ -[FBKAnnouncement fullHTMLContent].cold.1
+ -[FBKBugForm(Survey) fullAnnouncementHTML].cold.1
+ -[FBKBugForm(Survey) surveyAnnouncementHTML].cold.1
+ -[FBKContentItem formattedCreationDate].cold.1
+ -[FBKContentItem mailboxSortDateFormatter].cold.1
+ -[FBKContentItem mailboxSortDateFormatter].cold.2
+ -[FBKDeviceManager thisDevice].cold.1
+ -[FBKFileCollector _fileProcessingQueue].cold.1
+ -[FBKInstalledApp isInstalledIn:].cold.1
+ -[FBKInstalledApp isInstalledIn:].cold.2
+ -[FBKInstalledApp isInstalledIn:].cold.3
+ -[FBKParticipant fullName].cold.1
+ -[FBKQuestionGroup diffableHashWithContext:]
+ -[FBKRequestRecord attributedStringAttributes].cold.1
+ -[FBKUser fullName].cold.1
+ -[NSString(FBKFile) isImageFile].cold.1
+ FBKIsAppleConnectAvailable.cold.1
+ GCC_except_table432
+ GCC_except_table437
+ GCC_except_table441
+ GCC_except_table450
+ Log.cold.1
+ _NSApp
+ _NSAppearanceNameDarkAqua
+ _OBJC_CLASS_$_AFPreferences
+ _OBJC_CLASS_$_NSColorSpace
+ _OBJC_CLASS_$__TtC12FeedbackCore16FBKOSEligibility
+ _OBJC_CLASS_$__TtC12FeedbackCore8FBKColor
+ _OBJC_METACLASS_$__TtC12FeedbackCore16FBKOSEligibility
+ _OBJC_METACLASS_$__TtC12FeedbackCore8FBKColor
+ __49-[FBKHTTPClient jsonForURLRequest:success:error:]_block_invoke.130
+ __61-[FBKHTTPClient dataForURLRequest:successWithResponse:error:]_block_invoke.106
+ __61-[FBKHTTPClient dataForURLRequest:successWithResponse:error:]_block_invoke.113
+ __CLASS_METHODS__TtC12FeedbackCore8FBKColor
+ __DATA__TtC12FeedbackCore16FBKOSEligibility
+ __DATA__TtC12FeedbackCore8FBKColor
+ __INSTANCE_METHODS__TtC12FeedbackCore16FBKOSEligibility
+ __INSTANCE_METHODS__TtC12FeedbackCore8FBKColor
+ __METACLASS_DATA__TtC12FeedbackCore16FBKOSEligibility
+ __METACLASS_DATA__TtC12FeedbackCore8FBKColor
+ __OBJC_CLASS_PROTOCOLS_$_FBKQuestionGroup
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ __block_literal_global.151
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_FeedbackCore
+ _isLanguageRTL
+ _objc_msgSend$diffableHashWithContext:
+ _objc_msgSend$languageCode
+ _objc_msgSend$sharedPreferences
+ _objc_msgSend$userInterfaceLayoutDirection
+ _swift_setDeallocating
+ _symbolic _____ 12FeedbackCore16FBKOSEligibilityC
+ _symbolic _____ 12FeedbackCore8FBKColorC
+ formatterReader.cold.1
- GCC_except_table431
- GCC_except_table436
- GCC_except_table439
- GCC_except_table449
- GCC_except_table63
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_20
- __49-[FBKHTTPClient jsonForURLRequest:success:error:]_block_invoke.126
- __61-[FBKHTTPClient dataForURLRequest:successWithResponse:error:]_block_invoke.102
- __61-[FBKHTTPClient dataForURLRequest:successWithResponse:error:]_block_invoke.109
- ___swift_destroy_boxed_opaque_existential_1
- __block_literal_global.133
CStrings:
+ "%@ "
+ "-[FBKLoginManager loginAsUnauthenticatedUserWithCompletion:]"
+ ":%@"
+ "Failed to get RGB components from color"
+ "Using Siri Language: [%{public}@]"
+ "[%{public}s while in state [%{public}s]"
+ "_TtC12FeedbackCore16FBKOSEligibility"
+ "_TtC12FeedbackCore8FBKColor"
+ "colorUsingColorSpace:"
+ "darkerColorFor:amount:"
+ "deviceRGBColorSpace"
+ "effectiveAppearance"
+ "getRed:green:blue:alpha:"
+ "languageCode"
+ "lighterColorFor:amount:"
+ "prominentInfoQuestionTextColor"
+ "sharedPreferences"
+ "userInterfaceLayoutDirection"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Error reading extended attributes."
- "Insufficient space allocated to copy string contents"
- "Must take zero or more splits"
- "Negative value is not representable"
- "Range requires lowerBound <= upperBound"
- "Swift/Array.swift"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/Range.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "dd-snapshot-needs-change"
- "invalid Collection: less than 'count' elements in collection"

```
