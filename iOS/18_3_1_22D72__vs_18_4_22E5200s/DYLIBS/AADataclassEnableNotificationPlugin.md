## AADataclassEnableNotificationPlugin

> `/System/Library/Accounts/Notification/AADataclassEnableNotificationPlugin.bundle/AADataclassEnableNotificationPlugin`

```diff

-1007.230.0.0.0
-  __TEXT.__text: 0x4594
+1007.456.0.0.0
+  __TEXT.__text: 0x5198
   __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_methlist: 0x2f8
+  __TEXT.__objc_methlist: 0x494
   __TEXT.__const: 0x38
+  __TEXT.__oslogstring: 0xa4a
   __TEXT.__cstring: 0x581
-  __TEXT.__oslogstring: 0x683
-  __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__unwind_info: 0x160
+  __TEXT.__gcc_except_tab: 0xa8
+  __TEXT.__unwind_info: 0x1b0
   __TEXT.__objc_classname: 0xca
-  __TEXT.__objc_methname: 0xf5a
+  __TEXT.__objc_methname: 0xfd0
   __TEXT.__objc_methtype: 0x2b0
-  __TEXT.__objc_stubs: 0xcc0
-  __DATA_CONST.__got: 0x230
+  __TEXT.__objc_stubs: 0xd00
+  __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d8
+  __DATA_CONST.__objc_selrefs: 0x4c0
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x1c0
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x5a0
-  __AUTH_CONST.__objc_const: 0xce8
-  __AUTH.__objc_data: 0x190
+  __AUTH_CONST.__objc_const: 0xa10
+  __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x120
-  __DATA.__bss: 0x60
-  __DATA_DIRTY.__objc_data: 0x50
+  __DATA.__bss: 0x30
+  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 89
-  Symbols:   140
-  CStrings:  299
+  Functions: 120
+  Symbols:   141
+  CStrings:  317
 
Symbols:
+ _ACAccountTypeIdentifierIMAPMail
CStrings:
+ "Enabling dataclasses: %@"
+ "Enabling mail dataclass"
+ "Failed to enable mail dataclass for account %@ with error %@"
+ "Processing Apple Account change for account: %@"
+ "Processing IMAP Mail Account change for account: %@"
+ "Stop processing Apple Account change: Account wasn't modified"
+ "Stop processing Apple Account change: No new dataclasses to enable"
+ "Stop processing Apple Account change: No newly provisioned dataclasses"
+ "Stop processing Apple Account change: Provisioned dataclasses weren't modified"
+ "Stop processing IMAP Mail Account change: Account wasn't added"
+ "Stop processing IMAP Mail Account change: Cannot auto enable mail dataclass"
+ "Stop processing IMAP Mail Account change: Mail dataclass already enabled"
+ "Stop processing IMAP Mail Account change: Mail dataclass not provisioned"
+ "Stop processing IMAP Mail Account change: No parent account"
+ "Stop processing IMAP Mail Account change: Parent account is not an Apple Account"
+ "Successfully enabled dataclasses for account %@"
+ "Successfully enabled mail dataclass for account %@"
+ "_processAppleAccount:didChangeWithType:inStore:oldAccount:"
+ "_processIMAPMailAccount:didChangeWithType:inStore:oldAccount:"
+ "parentAccount"
- "Successfully enabled datclasses for account %@"
- "compare:options:"

```
