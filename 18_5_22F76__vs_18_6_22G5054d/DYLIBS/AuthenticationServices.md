## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-621.2.5.10.10
-  __TEXT.__text: 0x89a1c
-  __TEXT.__auth_stubs: 0x1b20
+621.3.6.10.1
+  __TEXT.__text: 0x89dbc
+  __TEXT.__auth_stubs: 0x1b30
   __TEXT.__objc_methlist: 0x6dc0
-  __TEXT.__const: 0x5094
-  __TEXT.__gcc_except_tab: 0x1138
-  __TEXT.__cstring: 0x6156
-  __TEXT.__oslogstring: 0x2438
+  __TEXT.__const: 0x5124
+  __TEXT.__gcc_except_tab: 0x113c
+  __TEXT.__cstring: 0x61b6
+  __TEXT.__oslogstring: 0x2568
   __TEXT.__dlopen_cstrs: 0x2a8
   __TEXT.__ustring: 0x751e
   __TEXT.__constg_swiftt: 0x978

   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift5_mpenum: 0x48
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x2b40
+  __TEXT.__unwind_info: 0x2b50
   __TEXT.__eh_frame: 0x1200
   __TEXT.__objc_classname: 0x1e3f
-  __TEXT.__objc_methname: 0x1478f
+  __TEXT.__objc_methname: 0x147c9
   __TEXT.__objc_methtype: 0x3cda
-  __TEXT.__objc_stubs: 0xcf60
+  __TEXT.__objc_stubs: 0xcf80
   __DATA_CONST.__got: 0xcb0
   __DATA_CONST.__const: 0x1a28
   __DATA_CONST.__objc_classlist: 0x458

   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x330
   __DATA_CONST.__objc_arraydata: 0x140
-  __AUTH_CONST.__auth_got: 0xda8
+  __AUTH_CONST.__auth_got: 0xdb0
   __AUTH_CONST.__const: 0x2f10
-  __AUTH_CONST.__cfstring: 0x4280
+  __AUTH_CONST.__cfstring: 0x42e0
   __AUTH_CONST.__objc_const: 0xd5c0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0xc0

   __AUTH.__objc_data: 0x2a10
   __AUTH.__data: 0x8a8
   __DATA.__objc_ivar: 0x6d4
-  __DATA.__data: 0x1fe8
+  __DATA.__data: 0x1f50
   __DATA.__bss: 0x5410
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x190

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D91E4D0B-738F-31AD-B58D-133DABF5FABB
-  Functions: 3868
-  Symbols:   9645
-  CStrings:  4751
+  UUID: 97E78FE9-AB7A-37CD-947F-C98572A87E68
+  Functions: 3871
+  Symbols:   9653
+  CStrings:  4762
 
Symbols:
+ +[_ASWebsiteNameProvider fetchWebsiteNameForDomain:completionHandler:].cold.2
+ GCC_except_table48
+ GCC_except_table50
+ GCC_except_table58
+ GCC_except_table59
+ ___58-[_ASPasswordManagerIconController performMaintenanceWork]_block_invoke
+ ___68-[_ASPasswordManagerIconController prepareForApplicationTermination]_block_invoke
+ ___68-[_ASPasswordManagerIconController prepareForApplicationTermination]_block_invoke.28
+ ___73-[_ASAgentPeriodicMaintenanceActivity _runActivityWithCompletionHandler:]_block_invoke_3
+ ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke.33
+ ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke.34
+ ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke_2.35
+ ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke_2.35.cold.1
+ ___block_literal_global.144
+ ___block_literal_global.146
+ ___block_literal_global.276
+ _dispatch_group_wait
+ _objc_msgSend$performExpiringActivityWithReason:usingBlock:
+ _objc_msgSend$processInfo
+ _objc_msgSend$savePendingProviderChangesWithCompletion:
+ _objc_msgSend$setSourceApplicationSecondaryIdentifierForRequiringPrivacyProxyFailingClosed:
- GCC_except_table44
- GCC_except_table45
- GCC_except_table52
- ___73-[_ASAgentPeriodicMaintenanceActivity _runActivityWithCompletionHandler:]_block_invoke.5
- ___73-[_ASAgentPeriodicMaintenanceActivity _runActivityWithCompletionHandler:]_block_invoke.cold.1
- ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke.25
- ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke.26
- ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke_2.27
- ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke_2.27.cold.1
- ___block_literal_global.139
- ___block_literal_global.141
- ___block_literal_global.271
- _objc_msgSend$_verifyGroupsInSync
- _objc_msgSend$savePendingProviderChangesBeforeTermination
- _objc_msgSend$setRequirePrivateRelayForAllNetworkTraffic:
CStrings:
+ "Background activity for performMaintenanceWork expired"
+ "Background activity for savePendingProviderChangesBeforeTermination expired"
+ "Fetch for %{sensitive}@ intentionally failed due to absence of underlying platform support."
+ "Perform maintenance work"
+ "Save pending changes before termination"
+ "Saved pending changes to database"
+ "Starting maintenance work with background task assertion"
+ "Starting to save pending changes with background task assertion"
+ "com.apple.Passwords.PRIconFetching"
+ "performExpiringActivityWithReason:usingBlock:"
+ "savePendingProviderChangesWithCompletion:"
+ "setSourceApplicationSecondaryIdentifierForRequiringPrivacyProxyFailingClosed:"
- "Periodic maintenance activity is attempting to run group sync verification"
- "_verifyGroupsInSync"
- "savePendingProviderChangesBeforeTermination"
- "setRequirePrivateRelayForAllNetworkTraffic:"

```
