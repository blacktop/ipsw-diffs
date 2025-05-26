## imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

-1262.400.41.2.3
-  __TEXT.__text: 0x6bf60
-  __TEXT.__auth_stubs: 0x1660
-  __TEXT.__objc_stubs: 0x76a0
-  __TEXT.__objc_methlist: 0x2838
+1262.500.151.2.4
+  __TEXT.__text: 0x6cdb0
+  __TEXT.__auth_stubs: 0x1680
+  __TEXT.__objc_stubs: 0x7720
+  __TEXT.__objc_methlist: 0x2868
   __TEXT.__const: 0xdd4
-  __TEXT.__gcc_except_tab: 0x6b40
-  __TEXT.__cstring: 0x2f41
-  __TEXT.__oslogstring: 0x6b90
-  __TEXT.__objc_methname: 0xe968
+  __TEXT.__gcc_except_tab: 0x6aec
+  __TEXT.__cstring: 0x32c1
+  __TEXT.__oslogstring: 0x6cc7
+  __TEXT.__objc_methname: 0xeb02
   __TEXT.__objc_classname: 0x911
-  __TEXT.__objc_methtype: 0x337c
+  __TEXT.__objc_methtype: 0x343f
   __TEXT.__swift5_typeref: 0x2f3
   __TEXT.__swift5_fieldmd: 0x184
   __TEXT.__constg_swiftt: 0x364

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2768
-  __TEXT.__eh_frame: 0x46c
-  __DATA_CONST.__auth_got: 0xb40
-  __DATA_CONST.__got: 0x590
-  __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x19b0
+  __TEXT.__unwind_info: 0x2730
+  __TEXT.__eh_frame: 0x41c
+  __DATA_CONST.__auth_got: 0xb50
+  __DATA_CONST.__got: 0x598
+  __DATA_CONST.__auth_ptr: 0x58
+  __DATA_CONST.__const: 0x19e8
   __DATA_CONST.__cfstring: 0x17c0
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0xc0
+  __DATA_CONST.__objc_classrefs: 0x498
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x6c48
-  __DATA.__objc_selrefs: 0x2e18
-  __DATA.__objc_protorefs: 0xc0
-  __DATA.__objc_classrefs: 0x4a0
-  __DATA.__objc_superrefs: 0x20
+  __DATA.__objc_const: 0x6cc8
+  __DATA.__objc_selrefs: 0x2e60
   __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0x980
   __DATA.__data: 0x1738
   __DATA.__bss: 0xd20
-  __DATA.__common: 0xa8
+  __DATA.__common: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1377
-  Symbols:   600
-  CStrings:  3048
+  Functions: 1386
+  Symbols:   599
+  CStrings:  3088
 
Symbols:
+ _CSIndexErrorDomain
+ _IMDMessageRecordCalculateTotalCounts
- _IMDCoreSpotlightReindexMessages
- _OBJC_CLASS_$_IMDLegacyDTController
- _objc_retain_x10
CStrings:
+ "21:03:09"
+ "Attempting to cancel sync"
+ "ChatRequestHandler"
+ "Checking if server prevents onboarding ramp for mic"
+ "Checking if user satisfies size cohort conditions"
+ "Error getting client state (attempt %ld/%d): %@"
+ "Failed to inspect client state %d times - giving up"
+ "Fatal error"
+ "Feb 19 2024"
+ "IMDCKLocalDBStatsKey is nil, re-fetching record totals for size criteria check"
+ "Insufficient space allocated to copy string contents"
+ "Negative value is not representable"
+ "No message found for message guid: %@"
+ "No message guid found for message: %@"
+ "No session for account: %s -- can't close session."
+ "Not enough bits to represent the passed value"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/Integers.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"<ParentalControlsProtocol>\",?,R,N"
+ "T@\"IMMessageContext\",?,&,N"
+ "T@\"NSString\",?,R,C"
+ "TB,?,R,N,GisSetupComplete"
+ "TQ,?,R,N"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_checkSpotlightClientStateForReindexIfNeededWithAttempts:"
+ "_clientCapabilitiesSupportAccounts:"
+ "cancelSync:"
+ "closeSessionChatID:identifier:didDeleteConversation:style:"
+ "closeSessionChatID:identifier:didDeleteConversation:style:account:"
+ "getValueFromDomain:forKey:"
+ "invalid Collection: less than 'count' elements in collection"
+ "markAsSpamForIDs:style:onServices:chatID:queryID:autoReport:isJunkReportedToCarrier:reportReason:"
+ "markChatAsSpamWithGUID:chatIdentifiers:style:services:isAutoReport:isJunkReportedToCarrier:reportReason:reply:"
+ "retryGroupPhotoUpload:toChatID:identifier:style:account:isPhotoRefresh:"
+ "satisfiesSizeCohortConditionsWithReply:"
+ "satisfiesSizeCohortConditionsWithStats:"
+ "serverPreventsOnboardingRamp"
+ "serverPreventsOnboardingWithReply:"
+ "setSyncCancelled:"
+ "syncState"
+ "syncType"
+ "v24@0:8@?<v@?BQ>16"
+ "v48@0:8@\"NSString\"16@\"NSString\"24B32C36@\"NSString\"40"
+ "v48@0:8@16@24B32C36@40"
+ "v68@0:8@\"NSString\"16@\"NSArray\"24C32@\"NSArray\"36B44B48Q52@?<v@?Q>60"
+ "v68@0:8@16@24C32@36B44B48Q52@?60"
- "20:55:41"
- "20:55:43"
- "Initiating reindex for %ld GUIDs"
- "Jan  8 2024"
- "Reindex request complete for %ld GUIDs"
- "T@\"<ParentalControlsProtocol>\",R,N"
- "T@\"IMMessageContext\",&,N"
- "TB,R,N,GisSetupComplete"
- "TQ,R,N"
- "_needsPartialReindexingDueToCoreSpotlightRequest"
- "closeSessionChatID:identifier:style:"
- "closeSessionChatID:identifier:style:account:"
- "closeSessionChatID:identifier:style:account:messageContext:"
- "deferredReindexingGUIDs"
- "markAsSpamForIDs:style:onServices:chatID:queryID:autoReport:isJunkReportedToCarrier:"
- "markDeferredReindexingCompletedForGUIDs:"

```
