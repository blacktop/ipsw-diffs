## IMCore

> `/System/Library/PrivateFrameworks/IMCore.framework/IMCore`

```diff

-1262.600.61.2.9
-  __TEXT.__text: 0x195664
-  __TEXT.__auth_stubs: 0x23f0
-  __TEXT.__objc_methlist: 0x11bcc
+1262.700.71.2.1
+  __TEXT.__text: 0x1961c8
+  __TEXT.__auth_stubs: 0x2400
+  __TEXT.__objc_methlist: 0x11c54
   __TEXT.__const: 0x15d0
-  __TEXT.__gcc_except_tab: 0xde6c
-  __TEXT.__cstring: 0x10887
-  __TEXT.__oslogstring: 0x1ae13
+  __TEXT.__gcc_except_tab: 0xdedc
+  __TEXT.__cstring: 0x108b7
+  __TEXT.__oslogstring: 0x1b00c
   __TEXT.__dlopen_cstrs: 0x184
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x7c9

   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0x60
-  __TEXT.__unwind_info: 0x7bd4
-  __TEXT.__eh_frame: 0x810
-  __TEXT.__objc_classname: 0x2145
-  __TEXT.__objc_methname: 0x37e2c
-  __TEXT.__objc_methtype: 0x5f38
-  __TEXT.__objc_stubs: 0x214c0
-  __DATA_CONST.__got: 0xf40
-  __DATA_CONST.__const: 0x4928
-  __DATA_CONST.__objc_classlist: 0x670
+  __TEXT.__unwind_info: 0x7bfc
+  __TEXT.__eh_frame: 0x808
+  __TEXT.__objc_classname: 0x216a
+  __TEXT.__objc_methname: 0x380b6
+  __TEXT.__objc_methtype: 0x5f72
+  __TEXT.__objc_stubs: 0x21660
+  __DATA_CONST.__got: 0xf48
+  __DATA_CONST.__const: 0x4930
+  __DATA_CONST.__objc_classlist: 0x678
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x3b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x19a60
-  __DATA_CONST.__objc_selrefs: 0xb990
+  __DATA_CONST.__objc_const: 0x19b38
+  __DATA_CONST.__objc_selrefs: 0xba00
   __DATA_CONST.__objc_protorefs: 0x168
-  __DATA_CONST.__objc_classrefs: 0xb48
+  __DATA_CONST.__objc_classrefs: 0xb58
   __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__cfstring: 0xb2c0
-  __AUTH_CONST.__const: 0x3f98
+  __AUTH_CONST.__cfstring: 0xb2e0
+  __AUTH_CONST.__const: 0x3fb8
   __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH_CONST.__objc_const: 0x4cf8
+  __AUTH_CONST.__objc_const: 0x4d40
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH_CONST.__auth_got: 0x1208
-  __AUTH.__objc_data: 0x2610
+  __AUTH_CONST.__auth_got: 0x1210
+  __AUTH.__objc_data: 0x2660
   __AUTH.__data: 0x100
-  __DATA.__objc_ivar: 0x1008
-  __DATA.__data: 0x2d58
+  __DATA.__objc_ivar: 0x100c
+  __DATA.__data: 0x2d68
   __DATA.__bss: 0x2ae0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1e78

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 74416117-EDEB-33E2-8549-49C4EF6C9D7A
-  Functions: 8264
-  Symbols:   2112
-  CStrings:  14822
+  UUID: 0B45BB6F-B5BE-382D-9C50-92E72F950C2C
+  Functions: 8280
+  Symbols:   2120
+  CStrings:  14849
 
Symbols:
+ _IMChatPropertyRequestedDowngradeExpirationDate
+ _IMChatServiceSwitchRequestedNotification
+ _IMIsInternationalFilteringAccount
+ _IMResetInternationalFilterEligibilityState
+ _OBJC_CLASS_$_IMUnknownInternationalSenderChatItem
+ _OBJC_CLASS_$_IMUnknownSenderHelper
+ _OBJC_METACLASS_$_IMUnknownInternationalSenderChatItem
+ __IMAllowSMSDowngradeRequests
CStrings:
+ "Chat %@ is ending holds on updates for all keys"
+ "Chat %@ will end holding chat item updates for reason: %{public}@"
+ "Chat %@ will hold chat item updates for reason: %{public}@"
+ "Chat has unknown international participant, inserting status item for unknown international number."
+ "Chat is downgraded by other user, overriding IDS: allAddressesiMessageCapable(%@), chat: %@"
+ "IMUnknownInternationalSenderChatItem"
+ "Not showing unknown international status item because chat has known participants."
+ "Not showing unknown international status item. chat.isFiltered=%@ and hasUnknownInternationalParticipant=%@"
+ "Personal nickname found"
+ "Personal nickname found after fetch"
+ "Previous downgrade request to SMS expired on %@, clearing"
+ "Processing %lu chat items for deletion"
+ "Recently Deleted | Will move %lu messageGUIDs to recently deleted"
+ "Request to delete entire chatItem for message (guid: %@). Adding messageGUID for deletion."
+ "TB,N,V_serviceSwitchRequested"
+ "__kIMChatServiceSwitchRequestedNotification"
+ "_hasValidSMSDowngradeRequest"
+ "_processChatItemsForUnknownInternationalSender:"
+ "_serviceSwitchRequested"
+ "accountCountryIsCandidateForInternationalFiltering:"
+ "accountRegionIsCandidateForInternationalFiltering:"
+ "activeAccountsAreEligibleForInternationalFiltering"
+ "originalUnformattedID"
+ "receiverIsCandidateForInternationalFiltering:"
+ "regionID"
+ "requestedDowngradeExpirationDate"
+ "serviceSwitchRequestReceivedForChatWithIdentifier:"
+ "serviceSwitchRequested"
+ "setRequestedDowngradeExpirationDate:"
+ "setServiceSwitchRequested:"
+ "shouldShowInternationalSenderWarningForHandleID:"
+ "simulateDowngradeRequestFromID:fromService:toService:expirationDate:"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSDate\"40"
- "Chat %{public}@ is ending holds on updates for all keys"
- "Chat %{public}@ will end holding chat item updates for reason: %{public}@"
- "Chat %{public}@ will hold chat item updates for reason: %{public}@"
- "Delete chat items: %@"
- "Personal nickname found after fetch: %@"
- "Personal nickname found: %@"
- "Request to delete all chatItems for message (guid: %@). Adding message to delete."

```
