## MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3901.200.34.0.0
-  __TEXT.__text: 0x60c4a4
+3901.200.41.0.0
+  __TEXT.__text: 0x60c53c
   __TEXT.__auth_stubs: 0x8290
-  __TEXT.__objc_stubs: 0x46900
-  __TEXT.__objc_methlist: 0x26c2c
-  __TEXT.__gcc_except_tab: 0x56180
-  __TEXT.__objc_methname: 0x699c7
-  __TEXT.__cstring: 0x197c4
+  __TEXT.__objc_stubs: 0x46880
+  __TEXT.__objc_methlist: 0x26c0c
+  __TEXT.__gcc_except_tab: 0x561e0
+  __TEXT.__objc_methname: 0x69a27
+  __TEXT.__cstring: 0x19784
   __TEXT.__objc_classname: 0x639a
   __TEXT.__objc_methtype: 0x12838
   __TEXT.__const: 0x163b0
-  __TEXT.__oslogstring: 0x1ac92
+  __TEXT.__oslogstring: 0x1ac62
   __TEXT.__ustring: 0xace
   __TEXT.__dlopen_cstrs: 0x2cc
   __TEXT.__constg_swiftt: 0x4f38

   __TEXT.__swift_as_cont: 0xaec
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift5_protos: 0x54
-  __TEXT.__unwind_info: 0x23e20
+  __TEXT.__unwind_info: 0x23e28
   __TEXT.__eh_frame: 0x5a74
-  __DATA_CONST.__const: 0x267c8
+  __DATA_CONST.__const: 0x26788
   __DATA_CONST.__cfstring: 0xe940
   __DATA_CONST.__objc_classlist: 0xea8
-  __DATA_CONST.__objc_catlist: 0xf0
+  __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0xbc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x290

   __DATA_CONST.__objc_doubleobj: 0x290
   __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__auth_got: 0x4158
-  __DATA_CONST.__got: 0x4278
+  __DATA_CONST.__got: 0x4238
   __DATA_CONST.__auth_ptr: 0x2068
-  __DATA.__objc_const: 0x37968
-  __DATA.__objc_selrefs: 0x15b20
-  __DATA.__objc_ivar: 0x1fdc
+  __DATA.__objc_const: 0x37988
+  __DATA.__objc_selrefs: 0x15b00
+  __DATA.__objc_ivar: 0x1fe8
   __DATA.__objc_data: 0xc470
   __DATA.__data: 0x109c0
   __DATA.__common: 0x958

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 26906
-  Symbols:   5046
-  CStrings:  22359
+  Symbols:   5038
+  CStrings:  22357
 
Symbols:
- _MFMessageCcContainsAccountAddress
- _MFMessageConversationIsMuted
- _MFMessageConversationIsVIP
- _MFMessageHasAttachments
- _MFMessageSenderIsVIP
- _MFMessageToContainsAccountAddress
- _MFMessageToOrCcContainsAccountAddress
- _MessageIsJournaled
CStrings:
+ "<%@: %p> Deferring load more messages - mailbox object ids not resolved yet"
+ "<%@: %p> Updated resolved mailbox object ids: %{public}@, complete: %i, mailboxes: %{public}@"
+ "Deferring selectDefaultMailbox until maild returns the mailbox list"
+ "TB,N,V_resolvedMailboxObjectIDsAreComplete"
+ "_cachedAccountDisplayName"
+ "_didRetryMailboxObjectIDsAfterLoadFailure"
+ "_pendingMailboxCacheWarmRefresh"
+ "_resolvedMailboxObjectIDsAreComplete"
+ "_selectDefaultMailboxWhenMailboxesAreAvailable"
+ "_updateResolvedMailboxObjectIDsRetryingWhenCacheWarms:"
+ "accountIfAvailable"
+ "accountWithURL:"
+ "availableMailboxTypeResolver"
+ "isMailboxCacheWarm"
+ "mailboxesFuture"
+ "resolvedMailboxObjectIDsAreComplete"
+ "setBucketBarPeekingEnabled:"
+ "setResolvedMailboxObjectIDsAreComplete:"
+ "v16@?0@\"NSOrderedSet\"8"
- "#Warning Unsupported criterion during server-side searchability determination (failing transformation) : %@"
- "#Warning unexpected criterion during server-side searchability determination (assuming YES) : %@"
- "<%@: %p> Updated resolved mailbox object ids: %{public}@, mailboxes: %{public}@"
- "@\"MFMessageCriterion\"16@?0@\"MFMessageCriterion\"8"
- "@\"MFMessageCriterion\"16@?0@\"NSString\"8"
- "TB,N,V_wasWindowSceneWide"
- "_wasWindowSceneWide"
- "allVIPEmailAddressesCriterion"
- "components:fromDate:"
- "criteria"
- "criterionByApplyingTransform:"
- "expression"
- "initWithType:qualifier:expression:"
- "mailServerSideCriterion"
- "mf_shouldUseDesktopClassNavigationBarForTraitCollection:windowScene:"
- "mui_isWide"
- "myEmailAddressesCriterionWithType:"
- "notCriterionWithCriterion:"
- "orCompoundCriterionWithCriteria:"
- "setWasWindowSceneWide:"
- "wasWindowSceneWide"
```
