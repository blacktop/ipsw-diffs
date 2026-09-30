## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-623.1.13.10.3
-  __TEXT.__text: 0x12858c
+623.1.14.10.6
+  __TEXT.__text: 0x128834
   __TEXT.__auth_stubs: 0x2720
-  __TEXT.__objc_methlist: 0x7ca4
+  __TEXT.__objc_methlist: 0x7cbc
   __TEXT.__const: 0x11b14
-  __TEXT.__gcc_except_tab: 0x13bc
+  __TEXT.__gcc_except_tab: 0x13c8
   __TEXT.__cstring: 0xc976
   __TEXT.__oslogstring: 0x3305
   __TEXT.__dlopen_cstrs: 0x308

   __TEXT.__swift_as_entry: 0x198
   __TEXT.__swift_as_ret: 0x218
   __TEXT.__swift5_mpenum: 0xb0
-  __TEXT.__unwind_info: 0x5028
+  __TEXT.__unwind_info: 0x5038
   __TEXT.__eh_frame: 0x52d4
   __TEXT.__objc_classname: 0x20ae
-  __TEXT.__objc_methname: 0x1726f
+  __TEXT.__objc_methname: 0x172e7
   __TEXT.__objc_methtype: 0x42c9
-  __TEXT.__objc_stubs: 0xd300
+  __TEXT.__objc_stubs: 0xd320
   __DATA_CONST.__got: 0xf70
   __DATA_CONST.__const: 0x19a8
   __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b80
+  __DATA_CONST.__objc_selrefs: 0x4b90
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x170
   __AUTH_CONST.__auth_got: 0x13a8
   __AUTH_CONST.__const: 0x7b10
   __AUTH_CONST.__cfstring: 0x4600
-  __AUTH_CONST.__objc_const: 0xf9d0
+  __AUTH_CONST.__objc_const: 0xfa00
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH.__objc_data: 0x3770
   __AUTH.__data: 0x14a0
-  __DATA.__objc_ivar: 0x6fc
+  __DATA.__objc_ivar: 0x700
   __DATA.__data: 0x31b0
   __DATA.__bss: 0xf330
   __DATA.__common: 0x88

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C4EFECFD-01A7-38BD-AB40-B41A560F12A7
-  Functions: 7161
-  Symbols:   11150
-  CStrings:  5612
+  UUID: 841D838D-FFC6-38F8-9807-17CD4EACFBC6
+  Functions: 7164
+  Symbols:   11156
+  CStrings:  5616
 
Symbols:
+ -[ASCredentialSharingGroupsNotificationManager savedAccountStore]
+ -[ASCredentialSharingGroupsNotificationManager setSavedAccountStore:]
+ _OBJC_IVAR_$_ASCredentialSharingGroupsNotificationManager._lazySavedAccountStore
+ _OBJC_IVAR_$_ASCredentialSharingGroupsNotificationManager._savedAccountStoreLock
+ _objc_msgSend$savedAccountStore
- _OBJC_IVAR_$_ASCredentialSharingGroupsNotificationManager._savedAccountStore
Functions:
~ -[ASCredentialSharingGroupsNotificationManager init] : 124 -> 132
~ -[ASCredentialSharingGroupsNotificationManager initWithSavedAccountStore:] : 168 -> 96
+ -[ASCredentialSharingGroupsNotificationManager savedAccountStore]
~ -[ASCredentialSharingGroupsNotificationManager notifyUserAboutSharedSavedAccountsInRecentlyDeleted:] : 444 -> 476
~ ___100-[ASCredentialSharingGroupsNotificationManager notifyUserAboutSharedSavedAccountsInRecentlyDeleted:]_block_invoke_2 : 320 -> 332
~ ___83-[ASCredentialSharingGroupsNotificationManager leaveGroupWithID:completionHandler:]_block_invoke : 472 -> 492
~ ___83-[ASCredentialSharingGroupsNotificationManager leaveGroupWithID:completionHandler:]_block_invoke_2 : 40 -> 132
~ ___84-[ASCredentialSharingGroupsNotificationManager deleteGroupWithID:completionHandler:]_block_invoke : 472 -> 492
~ ___84-[ASCredentialSharingGroupsNotificationManager deleteGroupWithID:completionHandler:]_block_invoke_2 : 40 -> 132
~ -[ASCredentialSharingGroupsNotificationManager fetchNumberOfPasswordAndPasskeySavedAccountsWithCompletion:] : 192 -> 208
~ ___107-[ASCredentialSharingGroupsNotificationManager fetchNumberOfPasswordAndPasskeySavedAccountsWithCompletion:]_block_invoke : 136 -> 156
~ -[ASCredentialSharingGroupsNotificationManager _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupID:] : 100 -> 128
+ -[ASCredentialSharingGroupsNotificationManager setSavedAccountStore:]
+ sub_1b22d9864
CStrings:
+ "T@\"WBSSavedAccountStore\",&,N,V_lazySavedAccountStore"
+ "_lazySavedAccountStore"
+ "_savedAccountStoreLock"
+ "setSavedAccountStore:"
- "_savedAccountStore"

```
