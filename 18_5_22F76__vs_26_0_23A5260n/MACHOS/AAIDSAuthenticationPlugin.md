## AAIDSAuthenticationPlugin

> `/System/Library/Accounts/Authentication/AAIDSAuthenticationPlugin.bundle/AAIDSAuthenticationPlugin`

```diff

-1007.477.0.0.0
-  __TEXT.__text: 0x7c84
+1025.0.0.0.0
+  __TEXT.__text: 0x7c90
   __TEXT.__auth_stubs: 0x5a0
   __TEXT.__objc_stubs: 0x13a0
   __TEXT.__objc_methlist: 0x38c

   __TEXT.__gcc_except_tab: 0x1f8
   __TEXT.__cstring: 0x5f6
   __TEXT.__objc_methname: 0x14db
-  __TEXT.__oslogstring: 0x14a7
+  __TEXT.__oslogstring: 0x14b8
   __TEXT.__objc_classname: 0x64
   __TEXT.__objc_methtype: 0x58d
   __TEXT.__unwind_info: 0x210

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 43A9270B-C059-319F-ABEC-0D88D200B97A
+  UUID: DD6EEE1A-059F-36E2-9057-9D9583435DF9
   Functions: 141
   Symbols:   178
   CStrings:  413
Functions:
~ sub_71d0 : 2488 -> 2500
CStrings:
+ "AAIDSAuthenticationPlugin: Looking for iCloud account with DSID %{mask}@ for raw password update."
+ "Setting credential (%@) on account with identifier (%@). [receiptTime: %f, token: %{sensitive}@]"
- "AAIDSAuthenticationPlugin: Looking for iCloud account with DSID %@ for raw password update."
- "Setting credential (%@) on account with identifier (%@). [receiptTime: %f, token: %@]"

```
