## SiriMailInternal

> `/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal`

```diff

-3401.8.1.0.0
-  __TEXT.__text: 0xe06dc
-  __TEXT.__auth_stubs: 0x3f00
+3401.13.1.0.0
+  __TEXT.__text: 0xe1f84
+  __TEXT.__auth_stubs: 0x3f90
   __TEXT.__const: 0x5f60
   __TEXT.__cstring: 0x2384
   __TEXT.__constg_swiftt: 0x2180
-  __TEXT.__swift5_typeref: 0x35ae
+  __TEXT.__swift5_typeref: 0x35ca
   __TEXT.__swift5_fieldmd: 0x19ec
-  __TEXT.__oslogstring: 0x6267
+  __TEXT.__oslogstring: 0x63b7
   __TEXT.__swift5_types: 0x194
   __TEXT.__swift5_proto: 0x288
   __TEXT.__swift5_reflstr: 0x1923

   __TEXT.__swift5_mpenum: 0x6c
   __TEXT.__swift5_capture: 0x5a0
   __TEXT.__unwind_info: 0x2c90
-  __TEXT.__eh_frame: 0x5f60
+  __TEXT.__eh_frame: 0x5f38
   __TEXT.__objc_classname: 0xb8
-  __TEXT.__objc_methname: 0x9fa
+  __TEXT.__objc_methname: 0x98c
   __TEXT.__objc_methtype: 0x1d1
-  __DATA_CONST.__got: 0x1100
-  __DATA_CONST.__const: 0x158
+  __DATA_CONST.__got: 0x1148
+  __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d8
+  __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_protorefs: 0x60
-  __AUTH_CONST.__auth_got: 0x1f80
-  __AUTH_CONST.__auth_ptr: 0x1748
-  __AUTH_CONST.__const: 0x2388
+  __AUTH_CONST.__auth_got: 0x1fc8
+  __AUTH_CONST.__auth_ptr: 0x1790
+  __AUTH_CONST.__const: 0x2358
   __AUTH_CONST.__objc_const: 0x2618
   __AUTH.__objc_data: 0x750
   __AUTH.__data: 0x2e88
-  __DATA.__data: 0x2680
+  __DATA.__data: 0x26b0
   __DATA.__bss: 0x51d0
-  __DATA.__common: 0x220
+  __DATA.__common: 0x228
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes
   - /System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology
   - /System/Library/PrivateFrameworks/SiriReferenceResolution.framework/SiriReferenceResolution
+  - /System/Library/PrivateFrameworks/SiriReferenceResolutionDataModel.framework/SiriReferenceResolutionDataModel
   - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities
   - /System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4242
-  Symbols:   2246
-  CStrings:  813
+  Functions: 4244
+  Symbols:   2241
+  CStrings:  818
 
Symbols:
+ _swift_getEnumCaseMultiPayload
- _swift_continuation_throwingResume
- _objc_retain_x2
- _swift_continuation_throwingResumeWithError
- _swift_continuation_await
- _swift_continuation_init
- _OBJC_CLASS_$_LNApplicationConnection
CStrings:
+ "ReferenceResolution# No matches found"
+ "ReferenceResolution# Received a failure: %!s(MISSING) -> nil"
+ "FetchMailMessages"
+ "#GetMail returning some new emails"
+ "ReferenceResolution# Found plural ambiguous entities"
+ "#GetMail found %!l(MISSING)d unread emails, returning those"
+ "#GetMail filtering for implicit unread since there are unreads but the user did not specify"
+ "#ReferenceResolution calling SRR for resolving onscreen Mail app entity"
+ "#ViewEntities Failed to resolve view entities: %!s(MISSING)"
+ "ReferenceResolution# Received unknown result type %!s(MISSING)"
+ "ReferenceResolution# Found %!l(MISSING)d candidates. Using the first one"
+ "ReferenceResolution# Found a candidate %!s(MISSING)"
+ "#GetMail user is referring to something onscreen that we couldn't resolve, returning empty array"
+ "#GetMail didn't find any new emails, returning nothing"
+ "ReferenceResolution# Found ambiguous entities"
- "GetMail didn't find any new emails, returning nothing"
- "instanceIdentifier"
- "#ViewEntities Requires LNFeatureFlags.isViewActionAnnotationEnabled to be enabled: please enable the feature flag to use view entities"
- "GetMail filtering for implicit unread since there are unreads but the user did not specify"
- "GetMail returning some new emails"
- "GetMail user is referring to something onscreen that we couldn't resolve, returning empty array"
- "#ViewEntities Found %!l(MISSING)d MailMessageEntity(s) in the view onscreen"
- "fetchEntitiesFromActiveApplicationsWithInteractionIDs:bundleIdentifiers:completionHandler:"
- "GetMail found %!l(MISSING)d unread emails, returning those"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"

```
