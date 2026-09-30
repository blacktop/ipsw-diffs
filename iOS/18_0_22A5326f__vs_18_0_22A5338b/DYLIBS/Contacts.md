## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3656.0.0.0.0
-  __TEXT.__text: 0x18bdd4
-  __TEXT.__auth_stubs: 0x3070
-  __TEXT.__objc_methlist: 0x165e0
+3657.1.0.0.0
+  __TEXT.__text: 0x18c84c
+  __TEXT.__auth_stubs: 0x30a0
+  __TEXT.__objc_methlist: 0x16648
   __TEXT.__const: 0x1268
-  __TEXT.__gcc_except_tab: 0x30e4
+  __TEXT.__gcc_except_tab: 0x3114
   __TEXT.__cstring: 0xc292
-  __TEXT.__oslogstring: 0x8c3a
+  __TEXT.__oslogstring: 0x8d0a
   __TEXT.__dlopen_cstrs: 0x394
   __TEXT.__ustring: 0x12
   __TEXT.__constg_swiftt: 0xc4c
-  __TEXT.__swift5_typeref: 0xb83
+  __TEXT.__swift5_typeref: 0xb5b
   __TEXT.__swift5_reflstr: 0x65b
   __TEXT.__swift5_fieldmd: 0x6ec
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__swift5_proto: 0x90
   __TEXT.__swift5_types: 0x8c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_capture: 0x448
-  __TEXT.__unwind_info: 0x6e10
-  __TEXT.__eh_frame: 0x1f10
+  __TEXT.__swift5_capture: 0x444
+  __TEXT.__unwind_info: 0x6e38
+  __TEXT.__eh_frame: 0x1f68
   __TEXT.__objc_classname: 0x3a64
-  __TEXT.__objc_methname: 0x26980
-  __TEXT.__objc_methtype: 0x4881
-  __TEXT.__objc_stubs: 0x1b980
+  __TEXT.__objc_methname: 0x26a18
+  __TEXT.__objc_methtype: 0x48a4
+  __TEXT.__objc_stubs: 0x1b9a0
   __DATA_CONST.__got: 0x19e8
-  __DATA_CONST.__const: 0x5ba8
+  __DATA_CONST.__const: 0x5bd0
   __DATA_CONST.__objc_classlist: 0xee8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x86b0
+  __DATA_CONST.__objc_selrefs: 0x86c0
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x898
   __DATA_CONST.__objc_arraydata: 0x258
-  __AUTH_CONST.__auth_got: 0x1848
+  __AUTH_CONST.__auth_got: 0x1860
   __AUTH_CONST.__auth_ptr: 0x3e0
-  __AUTH_CONST.__const: 0x5e70
-  __AUTH_CONST.__cfstring: 0xd040
-  __AUTH_CONST.__objc_const: 0x29908
+  __AUTH_CONST.__const: 0x5e90
+  __AUTH_CONST.__cfstring: 0xd060
+  __AUTH_CONST.__objc_const: 0x29978
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH.__objc_data: 0x4dd0
   __AUTH.__data: 0x590
-  __DATA.__objc_ivar: 0x1044
+  __DATA.__objc_ivar: 0x1048
   __DATA.__data: 0x2640
-  __DATA.__bss: 0x21a0
+  __DATA.__bss: 0x21b0
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x51e0
   __DATA_DIRTY.__data: 0x28

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10855
-  Symbols:   11825
-  CStrings:  9969
+  Functions: 10871
+  Symbols:   11844
+  CStrings:  9978
 
Symbols:
+ _ABDropAllLimitedAccessRows
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
- _ABDropAllLimitedAccesRows
CStrings:
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "Creating new sync session for %!{(MISSING)public}@"
+ "Joining existing sync session for %!{(MISSING)public}@"
+ "Performing sync session for %!{(MISSING)public}@"
+ "Sync session completed successfully for %!{(MISSING)public}@ (%!{(MISSING)public}@)"
+ "Sync session failed for %!{(MISSING)public}@ (%!{(MISSING)public}@) with error: %!{(MISSING)public}@"
+ "Sync session requested for %!{(MISSING)public}@ (%!{(MISSING)public}@)"
+ "T@\"<CNScheduler>\",R,N,V_workQueue"
+ "T@\"NSObject<OS_dispatch_semaphore>\",R,N,V_workSemaphore"
+ "Timeout waiting to perform sync session for %!{(MISSING)public}@"
+ "_workSemaphore"
+ "com.apple.contacts.provider.moderator"
+ "dropAllLimitedAccessRows"
+ "dropAllLimitedAccessRows failed: %!@(MISSING)"
+ "dropAllLimitedAccessRowsAndSyncNotify"
+ "dropAllLimitedAccessRowsAndSyncNotify failed: %!@(MISSING)"
+ "dropAllLimitedAccessRowsAndSyncNotifyWithReply:"
+ "dropAllLimitedAccessRowsWithReply:"
+ "enableExtensionFor:bundleIdentifier:showPrompt:shouldSynchronize:completionHandler:"
+ "parameter ‘providerHost’ must be nonnull"
+ "resultWithFuture:timeout:"
+ "synchronizeProviderDomainUsingSession:bundleIdentifier:providerHost:"
+ "v48@0:8@\"NSString\"16@\"NSString\"24B32B36@?<v@?@\"NSError\">40"
+ "workSemaphore"
- "Creating new sync session using %!{(MISSING)public}@"
- "Joining existing sync session"
- "Sync requested for %!{(MISSING)public}@ (%!{(MISSING)public}@)"
- "Sync session (%!{(MISSING)public}@) for %!{(MISSING)public}@ completed successfully"
- "Sync session (%!{(MISSING)public}@) for %!{(MISSING)public}@ failed with error: %!{(MISSING)public}@"
- "T@\"_TtC8Contacts28CNContactProviderSupportHost\",R,N,V_host"
- "_host"
- "dropAllLimitedAccesRows"
- "dropAllLimitedAccesRows failed: %!@(MISSING)"
- "dropAllLimitedAccesRowsWithReply:"
- "enableExtensionFor:bundleIdentifier:showPrompt:shouldSynchronize:moderator:completionHandler:"
- "host"
- "initWithHost:"
- "synchronizeProviderDomainUsingSession:bundleIdentifier:"
- "v56@0:8@\"NSString\"16@\"NSString\"24B32B36@\"CNContactProviderSupportModerator\"40@?<v@?@\"NSError\">48"

```
