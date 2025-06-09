## accountsd

> `/System/Library/Frameworks/Accounts.framework/accountsd`

```diff

-999.4.0.0.0
+1014.0.0.0.0
   __TEXT.__text: 0x4ec
   __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_stubs: 0x300

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
+  - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 13BC7929-9140-31FA-9D0A-53627117FDFB
+  UUID: BDE0E4D1-36CF-3A1A-8780-B5E8EA9F4978
   Functions: 4
   Symbols:   41
   CStrings:  40

```
