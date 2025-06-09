## AAGKAuthenticationPlugin

> `/System/Library/Accounts/Authentication/AAGKAuthenticationPlugin.bundle/AAGKAuthenticationPlugin`

```diff

-1007.477.0.0.0
-  __TEXT.__text: 0xb59c
+1025.0.0.0.0
+  __TEXT.__text: 0xb5a0
   __TEXT.__auth_stubs: 0x590
   __TEXT.__objc_stubs: 0x1860
   __TEXT.__objc_methlist: 0x4bc

   __TEXT.__gcc_except_tab: 0x448
   __TEXT.__cstring: 0x9e8
   __TEXT.__objc_methname: 0x1a45
-  __TEXT.__oslogstring: 0x1a4c
+  __TEXT.__oslogstring: 0x1a6f
   __TEXT.__objc_classname: 0x7e
   __TEXT.__objc_methtype: 0x645
   __TEXT.__unwind_info: 0x2e8

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 84BB8AEA-02BB-3607-AE9B-748BC2B8AD81
+  UUID: 1DCAA67C-1805-3DE0-92FF-B70123C76719
   Functions: 210
   Symbols:   185
   CStrings:  589
Functions:
~ sub_9ad8 : 3872 -> 3876
CStrings:
+ "AAGKAuthenticationPlugin: Looking for iCloud account with DSID %{mask}@ for raw password update."
+ "Did not receive the required parameters. Apple ID: %@ DSID: %{mask}@ playerID: %@ token: %{sensitive}@"
+ "GKAuth:telling authkit account is in use using DSID:%{mask}@"
+ "GKAuth:telling authkit account is in use using altDSID:%{mask}@"
- "AAGKAuthenticationPlugin: Looking for iCloud account with DSID %@ for raw password update."
- "Did not receive the required parameters. Apple ID: %@ DSID: %@ playerID: %@ token: %@"
- "GKAuth:telling authkit account is in use using DSID:%@"
- "GKAuth:telling authkit account is in use using altDSID:%@"

```
