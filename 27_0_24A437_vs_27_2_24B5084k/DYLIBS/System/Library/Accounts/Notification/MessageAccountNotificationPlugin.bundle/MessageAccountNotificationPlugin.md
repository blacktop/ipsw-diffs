## MessageAccountNotificationPlugin

> `/System/Library/Accounts/Notification/MessageAccountNotificationPlugin.bundle/MessageAccountNotificationPlugin`

```diff

-3901.100.1.2.14
+3901.200.34.0.0
   __TEXT.__text: 0x19ec
   __TEXT.__objc_methlist: 0x234
   __TEXT.__const: 0x30

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
   - /System/Library/PrivateFrameworks/Email.framework/Email
+  - /System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon
   - /System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation
   - /System/Library/PrivateFrameworks/MailServices.framework/MailServices
   - /System/Library/PrivateFrameworks/Message.framework/MailServices/IMAP.framework/IMAP
Symbols:
+ _OBJC_CLASS_$_EDAccountAuthentication
- _OBJC_CLASS_$_EMAccountAuthentication
```
