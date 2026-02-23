## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

-525.475.13.1.0
-  __TEXT.__text: 0x2afcfc
+525.475.16.0.0
+  __TEXT.__text: 0x2b0768
   __TEXT.__auth_stubs: 0x20e0
-  __TEXT.__objc_stubs: 0x1b940
-  __TEXT.__objc_methlist: 0xbcdc
+  __TEXT.__objc_stubs: 0x1b9e0
+  __TEXT.__objc_methlist: 0xbd14
   __TEXT.__const: 0x61b0
-  __TEXT.__cstring: 0xab53
-  __TEXT.__objc_classname: 0x2883
+  __TEXT.__cstring: 0xaae5
+  __TEXT.__objc_classname: 0x286a
   __TEXT.__gcc_except_tab: 0x3e18
-  __TEXT.__objc_methname: 0x26235
-  __TEXT.__objc_methtype: 0x7646
-  __TEXT.__oslogstring: 0x25078
+  __TEXT.__objc_methname: 0x26315
+  __TEXT.__objc_methtype: 0x7652
+  __TEXT.__oslogstring: 0x252a7
   __TEXT.__dlopen_cstrs: 0x15f
-  __TEXT.__swift5_typeref: 0x2ccb
-  __TEXT.__swift5_fieldmd: 0x1324
-  __TEXT.__constg_swiftt: 0x1d10
-  __TEXT.__swift5_reflstr: 0xfb0
+  __TEXT.__swift5_typeref: 0x2ce5
+  __TEXT.__swift5_fieldmd: 0x132c
+  __TEXT.__constg_swiftt: 0x1cec
+  __TEXT.__swift5_reflstr: 0x1001
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_assocty: 0x270
-  __TEXT.__swift5_capture: 0x1954
+  __TEXT.__swift5_capture: 0x193c
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_proto: 0x2e4
-  __TEXT.__swift5_types: 0x1b4
-  __TEXT.__swift_as_entry: 0x414
-  __TEXT.__swift_as_ret: 0x508
-  __TEXT.__unwind_info: 0x6410
-  __TEXT.__eh_frame: 0xc410
+  __TEXT.__swift5_types: 0x1b0
+  __TEXT.__swift_as_entry: 0x420
+  __TEXT.__swift_as_ret: 0x520
+  __TEXT.__unwind_info: 0x6080
+  __TEXT.__eh_frame: 0xc678
   __DATA_CONST.__auth_got: 0x1080
-  __DATA_CONST.__got: 0x19b8
-  __DATA_CONST.__auth_ptr: 0x610
-  __DATA_CONST.__const: 0x12170
+  __DATA_CONST.__got: 0x19c0
+  __DATA_CONST.__auth_ptr: 0x608
+  __DATA_CONST.__const: 0x121a0
   __DATA_CONST.__cfstring: 0x7f20
-  __DATA_CONST.__objc_classlist: 0x7d8
+  __DATA_CONST.__objc_classlist: 0x7d0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__linkguard: 0x3e
-  __DATA.__objc_const: 0x28d80
-  __DATA.__objc_selrefs: 0x8038
+  __DATA.__objc_const: 0x28ce0
+  __DATA.__objc_selrefs: 0x8060
   __DATA.__objc_ivar: 0xacc
-  __DATA.__objc_data: 0x6110
-  __DATA.__data: 0x4640
+  __DATA.__objc_data: 0x6080
+  __DATA.__data: 0x4658
   __DATA.__bss: 0x56b0
-  __DATA.__common: 0x140
+  __DATA.__common: 0x138
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F3FF3F44-8797-304D-8B3D-B7F5870B2C40
-  Functions: 8261
-  Symbols:   1507
-  CStrings:  11656
+  UUID: 8B05EC8D-854C-3483-9F51-2B9DC7EB185C
+  Functions: 8275
+  Symbols:   1508
+  CStrings:  11662
 
Symbols:
+ _AKURLBagKeyPasskeyCleanupDisabled
CStrings:
+ "@\"NSDate\"24@0:8@\"ACAccount\"16"
+ "@\"NSNumber\"24@0:8@\"ACAccount\"16"
+ "Cannot cleanup stale passkeys - missing primary account"
+ "Cannot delete stale passkeys - eligibility check failed"
+ "Continue to SRP for server driven interactive auth with context (%@) for client (%@)"
+ "Detected stale passkeys. Cleaning up before enrollment..."
+ "Detected stale passkeys: server has no passkey but device has passkey(s)"
+ "Failed to delete stale passkeys"
+ "Failed to delete stale passkeys - error %@"
+ "Failed to obtain full UI capability for server driven interactive auth with error (%@)"
+ "Failed to perform server driven interactive auth for context (%@) with error (%@)"
+ "Federated auth: Routing to server driven interactive auth."
+ "Forced passkey creation requested"
+ "Obtaining full UI capability before attempting server driven interactive auth with context (%@) for client (%@)"
+ "Passkey eligibility check succeeded"
+ "Passwordless auth: Routing to server driven interactive auth."
+ "Performing eligibility checks for stale passkey deletion..."
+ "Performing eligibility checks for unenroll..."
+ "Recently attempted passkey deletion. Skipping for now."
+ "Server driven interactive auth failed, handling failure..."
+ "Shared iPad auth: routing to native interactive UI to prompt for passcode."
+ "Skipped IDMS account update as requested by context (appProvidedContext=%ld, altDSID=%{mask.hash}@)"
+ "Skipping IDMS account update and token persistence as requested by context (appProvidedContext=%ld, altDSID=%{mask.hash}@)"
+ "Skipping service token provisioning and persistence - context configured to skip account updates (shouldUpdatePersistentServiceTokens=%@, _shouldSkipAccountUpdates=%@, appProvidedContext=%ld, altDSID=%{mask.hash}@)"
+ "Stale passkey deletion failed - Device is in locked state."
+ "Successfully performed server driven interactive auth for context (%@)"
+ "Unable to determine client passkey count - assuming no passkeys"
+ "_continueWithServerDrivenInteractiveAuth:completion:"
+ "_isServerDrivenInteractiveAuthForContext:"
+ "akd.AppleIDPasskeyServerConfiguration"
+ "canDeleteStalePasskeysWithCompletionHandler:"
+ "canUnenrollPasskeyWithCompletionHandler:"
+ "configurationValueForKey:completion:"
+ "forceEnrollmentIgnoringServerState"
+ "hasStalePasskeys"
+ "initWithAccount:passkeyAuthenticationController:"
+ "passkeyDeletionAttemptDateForAccount:"
+ "prepareForUIWithContext:client:completion:"
+ "setForceEnrollmentIgnoringServerState:"
+ "setPasskeyDeletionAttemptDate:forAccount:"
+ "setPasskeyRegistrationAttemptDate:forAccount:"
+ "setupPasskeyWithContext:completion:"
+ "urlBag"
- "%@: Attempting to perform passwordless auth with context (%@) for client (%@)"
- "%@: Failed to obtain full UI capability for passwordless auth with error (%@)"
- "%@: Failed to perform passwordless auth for context (%@) with error (%@)"
- "%@: Obtaining full UI capability before attempting passwordless auth with context (%@) for client (%@)"
- "%@: Successfully performed passwordless auth for context (%@)"
- "@72@0:8@16@24@32@40@48@56@64"
- "AKAppleIDPasskeyHealthCheckService"
- "AltDSID not found for account %@."
- "AppleIDPasskeyHealthCheckService missing instance."
- "Authmode %@ supports passwordless auth + server UI. Time for SRP."
- "Client is asking for passwordless auth with auth mode %@ and just a username... lets see how this goes"
- "Failed to unenroll passkey with error - %@"
- "Keychain has an AppleID passkey. Unenroll not required."
- "Keychain has no AppleID passkey"
- "No passkeyCount saved. Skipping unenroll"
- "Passkey XPC activity registration complete. State: %ld."
- "Passkey cleanup not required - No passkeys found in iCloud keychain"
- "Passkey eligibility check failed - Primary account not found"
- "Passkey eligibility check failed - missing primary account."
- "Performing eligibility checks before unenrolling..."
- "Registering for passkey XPC activity: %s..."
- "T@\"AKAppleIDPasskeyHealthCheckService\",N,R"
- "XPC activity failed to set passkey activity state: %ld."
- "_performPasswordlessAuth:completion:"
- "canDeleteAllPasskeys()"
- "canUnenrollPasskeyWithForced:completionHandler:"
- "com.apple.ak.passkey.healthcheck"
- "com.apple.authkit.passkey-unenroll"
- "fetchUICapableContext:client:completion:"
- "initWithAccount:accountManager:featureManager:configuration:device:cdpFactory:authenticationController:"
- "isPasskeyCleanupDisabled"
- "isPasskeyEligible()"
- "passkeysDeletionAttemptDateForAccount:"
- "pdpEligible"
- "setPasskeyRegistrationAttemptDateForAccount:forAccount:"
- "setPasskeysDeletionAttemptDate:forAccount:"
- "setupPasskeyWithContext:forced:completion:"
- "v36@0:8@\"AKAppleIDPasskeySetupContext\"16B24@?<v@?B@\"NSError\">28"

```
