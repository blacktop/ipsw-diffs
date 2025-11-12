## SafariFoundation

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation`

```diff

-623.1.12.10.4
-  __TEXT.__text: 0x2aa1c
+623.1.13.10.3
+  __TEXT.__text: 0x2aa40
   __TEXT.__auth_stubs: 0xa90
   __TEXT.__objc_methlist: 0x1fec
   __TEXT.__cstring: 0x2c3c

   __TEXT.__unwind_info: 0x1078
   __TEXT.__eh_frame: 0x518
   __TEXT.__objc_classname: 0x4b1
-  __TEXT.__objc_methname: 0x7e95
+  __TEXT.__objc_methname: 0x7ea0
   __TEXT.__objc_methtype: 0xbf9
   __TEXT.__objc_stubs: 0x4c60
   __DATA_CONST.__got: 0x4d8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E672A337-B9BC-30DF-8559-ADC1BB5F5479
+  UUID: 371101FC-D7DC-325A-9EEF-69CD3DAE4F96
   Functions: 1067
   Symbols:   3610
   CStrings:  1841
Symbols:
+ _objc_msgSend$getPasskeysForRunningAssertionWithApplicationIdentifier:webPageURL:withCompletionHandler:
- _objc_msgSend$getPasskeysForRunningAssertionWithApplicationIdentifier:withCompletionHandler:
Functions:
~ -[SFAppAutoFillOneTimeCodeProvider _consumeOneTimeCode:] : 336 -> 356
~ -[SFAppAutoFillPasskeyProvider getAvailablePasskeysForApplicationIdentifier:completionHandler:] : 168 -> 172
~ ___170+[SFSafariCredentialStore getCredentialsForAppWithAppID:frameIdentifier:externallyVerifiedAndApprovedSharedWebCredentialDomains:websiteURL:testOptions:completionHandler:]_block_invoke.6 : 544 -> 556
CStrings:
+ "getPasskeysForRunningAssertionWithApplicationIdentifier:webPageURL:withCompletionHandler:"
- "getPasskeysForRunningAssertionWithApplicationIdentifier:withCompletionHandler:"

```
