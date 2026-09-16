## AMSAccountNotificationPlugin

> `/System/Library/Accounts/Notification/AMSAccountNotificationPlugin.bundle/AMSAccountNotificationPlugin`

```diff

-10.0.60.2.4
-  __TEXT.__text: 0x11318
-  __TEXT.__objc_methlist: 0x64c
+10.1.11.2.1
+  __TEXT.__text: 0x11f6c
+  __TEXT.__objc_methlist: 0x65c
   __TEXT.__const: 0x232
-  __TEXT.__cstring: 0xac5
+  __TEXT.__cstring: 0xae5
   __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__oslogstring: 0x2d88
+  __TEXT.__oslogstring: 0x30ce
   __TEXT.__dlopen_cstrs: 0x106
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0xbe

   __TEXT.__swift_as_entry: 0x20
   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x38
-  __TEXT.__unwind_info: 0x420
+  __TEXT.__unwind_info: 0x438
   __TEXT.__eh_frame: 0x468
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4c0
+  __DATA_CONST.__const: 0x530
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9c8
+  __DATA_CONST.__objc_selrefs: 0xa08
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__got: 0x1b8
-  __AUTH_CONST.__const: 0x1a8
-  __AUTH_CONST.__cfstring: 0x860
+  __DATA_CONST.__got: 0x1c8
+  __AUTH_CONST.__const: 0x1c8
+  __AUTH_CONST.__cfstring: 0x840
   __AUTH_CONST.__objc_const: 0x568
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 226
-  Symbols:   200
-  CStrings:  246
+  Functions: 231
+  Symbols:   202
+  CStrings:  254
 
Symbols:
+ _ACErrorDomain
+ _AMSPrivateEntitlementName
CStrings:
+ "%{public}@Failed to fetch simple profiles for sponsor. Leaving profileIdentifiers unchanged. sponsor = %{public}@ error = %{public}@"
+ "%{public}@Failed to save sponsor with recomputed profileIdentifiers. The cache stays stale until the next sponsor save. sponsor = %{public}@ error = %{public}@"
+ "%{public}@No simple profile is selected while the sponsor is active. Marking sponsor selected. sponsor = %{public}@"
+ "%{public}@Recomputed sponsor profileIdentifiers. sponsor = %{public}@ | count = %lu"
+ "%{public}@Sponsor has no identifier. Skipping profileIdentifiers cache update. sponsor = %{public}@"
+ "%{public}@Sponsor no longer exists. Skipping profileIdentifiers cache update. sponsor = %{public}@"
+ "%{public}@Sponsor profileIdentifiers already up to date. Skipping save. sponsor = %{public}@"
+ "%{public}@The account was already active and so were %lu other account(s). Reconciled to a single active account. account = %{public}@"
+ "@\"NSString\"16@?0@\"ACAccount\"8"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
- "%{public}@Error staging deselected simple profile: %{public}@. error = %{public}@"
- "com.apple.private.applemediaservices"
```
