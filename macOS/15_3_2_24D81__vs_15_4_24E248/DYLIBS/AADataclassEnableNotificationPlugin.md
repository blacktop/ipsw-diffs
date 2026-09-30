## AADataclassEnableNotificationPlugin

> `/System/Library/Accounts/Notification/AADataclassEnableNotificationPlugin.bundle/Contents/MacOS/AADataclassEnableNotificationPlugin`

```diff

-1007.230.0.0.0
-  __TEXT.__text: 0x4fa4
+1007.460.0.0.0
+  __TEXT.__text: 0x5cd8
   __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_methlist: 0x304
+  __TEXT.__objc_methlist: 0x4a4
   __TEXT.__const: 0x38
+  __TEXT.__oslogstring: 0xaf7
   __TEXT.__cstring: 0x595
-  __TEXT.__oslogstring: 0x730
-  __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__unwind_info: 0x180
+  __TEXT.__gcc_except_tab: 0xa8
+  __TEXT.__unwind_info: 0x1d0
   __TEXT.__objc_classname: 0xca
-  __TEXT.__objc_methname: 0xf91
+  __TEXT.__objc_methname: 0x1007
   __TEXT.__objc_methtype: 0x2b0
-  __TEXT.__objc_stubs: 0xd00
-  __DATA_CONST.__got: 0x1f8
+  __TEXT.__objc_stubs: 0xd40
+  __DATA_CONST.__got: 0x200
   __DATA_CONST.__const: 0x30
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e8
+  __DATA_CONST.__objc_selrefs: 0x4d0
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x118
   __AUTH_CONST.__const: 0x1f0
   __AUTH_CONST.__cfstring: 0x580
-  __AUTH_CONST.__objc_const: 0xce8
+  __AUTH_CONST.__objc_const: 0xa10
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x120

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DF83A2B7-8D74-3B69-9477-7B332C01B1DE
-  Functions: 104
-  Symbols:   112
-  CStrings:  347
+  UUID: 10510CD3-56C2-3403-8865-F799DE738A04
+  Functions: 134
+  Symbols:   113
+  CStrings:  365
 
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
