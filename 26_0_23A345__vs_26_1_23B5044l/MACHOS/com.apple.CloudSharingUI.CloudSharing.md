## com.apple.CloudSharingUI.CloudSharing

> `/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing`

```diff

-215.0.0.0.0
-  __TEXT.__text: 0xc5614
-  __TEXT.__auth_stubs: 0x2460
+215.1.3.1.0
+  __TEXT.__text: 0xbe978
+  __TEXT.__auth_stubs: 0x2420
   __TEXT.__objc_stubs: 0x1ac0
   __TEXT.__objc_methlist: 0x1654
-  __TEXT.__const: 0xa3c4
+  __TEXT.__const: 0xa074
   __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__cstring: 0x7555
-  __TEXT.__objc_methname: 0x4d22
-  __TEXT.__oslogstring: 0x2f09
+  __TEXT.__cstring: 0x77a5
+  __TEXT.__objc_methname: 0x4d01
+  __TEXT.__oslogstring: 0x2fe9
   __TEXT.__objc_classname: 0x351
   __TEXT.__objc_methtype: 0x1944
-  __TEXT.__swift5_typeref: 0xc14c
-  __TEXT.__swift5_fieldmd: 0x1dd8
-  __TEXT.__constg_swiftt: 0x1a54
-  __TEXT.__swift5_reflstr: 0x2484
-  __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_assocty: 0x918
-  __TEXT.__swift5_capture: 0x1314
-  __TEXT.__swift5_protos: 0x20
-  __TEXT.__swift5_proto: 0x2d8
-  __TEXT.__swift5_types: 0x1a8
+  __TEXT.__swift5_typeref: 0x9e42
+  __TEXT.__swift5_fieldmd: 0x1e2c
+  __TEXT.__constg_swiftt: 0x1a7c
+  __TEXT.__swift5_reflstr: 0x25d1
+  __TEXT.__swift5_builtin: 0x12c
+  __TEXT.__swift5_assocty: 0x900
+  __TEXT.__swift5_capture: 0x12bc
+  __TEXT.__swift5_protos: 0x24
+  __TEXT.__swift5_proto: 0x2cc
+  __TEXT.__swift5_types: 0x1ac
   __TEXT.__swift_as_entry: 0x188
   __TEXT.__swift_as_ret: 0x1c0
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2a98
-  __TEXT.__eh_frame: 0x5360
-  __DATA_CONST.__auth_got: 0x1240
-  __DATA_CONST.__got: 0xc88
-  __DATA_CONST.__auth_ptr: 0xee0
-  __DATA_CONST.__const: 0x5300
+  __TEXT.__unwind_info: 0x2a08
+  __TEXT.__eh_frame: 0x52c8
+  __DATA_CONST.__auth_got: 0x1220
+  __DATA_CONST.__got: 0xc48
+  __DATA_CONST.__auth_ptr: 0xed0
+  __DATA_CONST.__const: 0x4fe0
   __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x3820
-  __DATA.__objc_selrefs: 0x14a8
+  __DATA.__objc_const: 0x3800
+  __DATA.__objc_selrefs: 0x1498
   __DATA.__objc_ivar: 0x74
   __DATA.__objc_data: 0xee0
-  __DATA.__data: 0x49f8
-  __DATA.__bss: 0x6be0
+  __DATA.__data: 0x4888
+  __DATA.__bss: 0x6970
   __DATA.__common: 0x78
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/CloudSharingUI.framework/CloudSharingUI
   - /System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete
   - /System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/ContactsAutocompleteUI
-  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F03B3A50-6AF0-3139-8367-8BA6B41A9D63
-  Functions: 3783
-  Symbols:   384
-  CStrings:  1772
+  UUID: C320BE8A-890E-3FA6-8FB8-183D0AA3EF3E
+  Functions: 3682
+  Symbols:   387
+  CStrings:  1787
 
Symbols:
+ _AnalyticsSendEventLazy
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_getTupleTypeMetadata2
- _OBJC_CLASS_$_CKUserIdentity
- _OBJC_CLASS_$_NSUserDefaults
CStrings:
+ "%s: couldn't determine UTI"
+ ", will do nothing."
+ "@\"NSDictionary\"8@?0"
+ "Analytics event is: %s, will be built and sent: %{bool}d"
+ "Analytics event: %s sent lazily"
+ "Analytics payload: %s"
+ "No CKRequester for rowViewModel.id "
+ "SPIAnalyticsEvent sharePermission is none but no error"
+ "SPIAnalyticsEvent sharingMode is none but no error"
+ "SPIAnalyticsEvent unknown CSUICurrentUserCKShareStatus"
+ "SPIAnalyticsEvent unknown CSUIShareItemStatus"
+ "SPIAnalyticsEvent unknown sharing status but no error"
+ "SPIAnalyticsEvent unknown user share status but no error"
+ "Unexpected error denying requester for share"
+ "com.apple.CloudSharing.AddParticipantsToShareNoOptions"
+ "com.apple.CloudSharing.AddParticipantsToShareWithOptions"
+ "com.apple.CloudSharing.AddToShareByShareURL"
+ "com.apple.CloudSharing.ApproveAccessRequest"
+ "com.apple.CloudSharing.CloudKitAddToSharing"
+ "com.apple.CloudSharing.DenyAccessRequest"
+ "com.apple.CloudSharing.FSItemStartSharing"
+ "com.apple.CloudSharing.FSItemStatusQuery"
+ "com.apple.CloudSharing.GetMetadataFromShare"
+ "com.apple.CloudSharing.MailContent"
+ "com.apple.CloudSharing.RemoveFromShare"
+ "com.apple.CloudSharing.RemoveFromShareByShareURL"
+ "com.apple.CloudSharing.RemoveFromShareForFileURL"
+ "com.apple.CloudSharing.UserStatusQuery"
+ "com.apple.CloudSharing.updateShare"
+ "com.apple.documentsapp"
+ "com.apple.finder"
+ "com.apple.groups-folder"
+ "com.apple.keynote"
+ "com.apple.mobilesms"
+ "com.apple.numbers"
+ "errorCallingFunction"
+ "iOS appIcon: icon: %@"
+ "initWithType:"
+ "standardPayload(url:share:_:_:uti:)"
- "Anyone can ask to be added to the share as a participant"
- "Anyone with link can ask for access"
- "CloudSharingUI"
- "CloudSharingUIGelatoEnabled"
- "Gelato"
- "No one can ask to be added to the share"
- "No one can request access"
- "ShareAccessRequests"
- "ShareAccessRequestsEnabled"
- "Shared folder: %@"
- "Show Shared Folder"
- "WHO CAN REQUEST ACCESS"
- "_shouldShowSendLink"
- "boolForKey:"
- "fetchContactsForRequesters: Unexpected error: %@"
- "fetchContactsForRequesters: finished"
- "fetchContactsForRequesters: new contacts fetched: %ld for %ld requesters"
- "fetchContactsForRequesters: started"
- "fetchContactsForRequesters: unifiedContacts(matching:...) took: %f, total contacts found: %ld"
- "header text identifying owner of the share (never 'Me')"
- "header text naming top-level shared folder while examining a subitem"
- "header text when we can't determine the share owner string"
- "objectForKey:"
- "standardUserDefaults"

```
