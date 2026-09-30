## AMSAccountNotificationPlugin

> `/System/Library/Accounts/Notification/AMSAccountNotificationPlugin.bundle/AMSAccountNotificationPlugin`

```diff

-9.1.20.2.1
-  __TEXT.__text: 0xeaa0
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x5ac
+9.2.16.0.0
+  __TEXT.__text: 0xffa4
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_methlist: 0x5dc
   __TEXT.__const: 0x228
-  __TEXT.__cstring: 0xa95
+  __TEXT.__cstring: 0xad5
   __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__oslogstring: 0x25da
+  __TEXT.__oslogstring: 0x28ed
   __TEXT.__dlopen_cstrs: 0x1a6
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0xbe

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x20
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x380
+  __TEXT.__unwind_info: 0x388
   __TEXT.__eh_frame: 0x3d0
   __TEXT.__objc_classname: 0x5f
-  __TEXT.__objc_methname: 0x1dc2
+  __TEXT.__objc_methname: 0x1f07
   __TEXT.__objc_methtype: 0x2f6
-  __TEXT.__objc_stubs: 0x1e20
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x468
+  __TEXT.__objc_stubs: 0x1fa0
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0x470
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8c8
+  __DATA_CONST.__objc_selrefs: 0x930
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x428
+  __AUTH_CONST.__auth_got: 0x420
   __AUTH_CONST.__const: 0x208
-  __AUTH_CONST.__cfstring: 0x7a0
+  __AUTH_CONST.__cfstring: 0x820
   __AUTH_CONST.__objc_const: 0x568
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 30A4730A-EB89-3E51-B3AC-3B7F6DDD4F47
-  Functions: 212
-  Symbols:   194
-  CStrings:  618
+  UUID: 71EB7843-08FE-38FA-8033-8B7B6D6C3F53
+  Functions: 216
+  Symbols:   195
+  CStrings:  652
 
Symbols:
+ _AMSBagKeyAuthenticateSimpleProfileURL
+ ___kCFBooleanFalse
- _objc_retain_x28
CStrings:
+ "%@: %@ "
+ "%@: [%@] %@ "
+ "%{public}@: [%{public}@] Activating Selected Account. account = %{public}@"
+ "%{public}@: [%{public}@] Activating Sponsor Account. account = %{public}@"
+ "%{public}@: [%{public}@] Error activating %{public}@. error = %{public}@"
+ "%{public}@: [%{public}@] Removing authentication state for account = %{public}@"
+ "%{public}@: [%{public}@] Sponsor Account already active. account = %{public}@"
+ "%{public}@Deselected account: %{public}@."
+ "%{public}@Deselecting account: %{public}@."
+ "%{public}@Error deselecting account: %{public}@. error = %{public}@"
+ "%{public}@Finished processing."
+ "%{public}@Handling %{public}@. account = %{public}@ | changeType = %{public}@ | caller = %{public}@"
+ "%{public}@Marked account as not selected, updating: %{public}@."
+ "%{public}@The account was added already active. account = %{public}@."
+ "%{public}@The account was added already selected. account = %{public}@"
+ "%{public}@The account was deselected. account = %{public}@"
+ "%{public}@The account was selected. account = %{public}@"
+ "%{public}@The account was set to active. account = %{public}@"
+ "%{public}@The account was set to inactive. account = %{public}@"
+ "_deselectAllAccountsExcept:inStore:"
+ "_removeAuthenticationStateForAccount:store:"
+ "_updateActiveStateForSelected:inStore:"
+ "ams_activeiCloudAccount"
+ "ams_iTunesAccounts"
+ "ams_isSelectedProfile"
+ "ams_isSimpleProfile"
+ "ams_simpleProfileAccounts"
+ "arrayByAddingObjectsFromArray:"
+ "authenticateSimpleProfile"
+ "isEqualToNumber:"
+ "isSelectedProfile"
+ "isiCloudAccountBackingOf:"
+ "parentAccount"
+ "reload"
- "%{public}@: [%{public}@] Finished processing account:willChange."
- "%{public}@: [%{public}@] Handling account:willChange. account = %{public}@ | changeType = %{public}@ | caller = %{public}@"
- "%{public}@: [%{public}@] The account was added with its active flag set to YES."
- "%{public}@: [%{public}@] The account was set to active."

```
