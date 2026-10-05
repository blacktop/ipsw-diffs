## RemoteManagementAccountNotificationPlugin

> `/System/Library/Accounts/Notification/RemoteManagementAccountNotificationPlugin.bundle/RemoteManagementAccountNotificationPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-624.40.13.0.0
-  __TEXT.__text: 0x2238
+624.40.15.0.0
+  __TEXT.__text: 0x2268
   __TEXT.__auth_stubs: 0x200
   __TEXT.__objc_stubs: 0x6c0
   __TEXT.__objc_methlist: 0x474
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x309
+  __TEXT.__cstring: 0x32e
   __TEXT.__objc_classname: 0x2d5
   __TEXT.__objc_methname: 0xa25
   __TEXT.__objc_methtype: 0x2d8
   __TEXT.__oslogstring: 0x158
   __TEXT.__unwind_info: 0x168
-  __DATA_CONST.__const: 0x1b0
-  __DATA_CONST.__cfstring: 0x1c0
+  __DATA_CONST.__const: 0x1b8
+  __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28

   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/DataAccess.framework/DataAccess
   - /System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DALDAP.framework/DALDAP
+  - /System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/DAEAS.framework/DAEAS
   - /System/Library/PrivateFrameworks/Message.framework/MailServices/IMAP.framework/IMAP
   - /System/Library/PrivateFrameworks/Message.framework/MailServices/POP.framework/POP
   - /System/Library/PrivateFrameworks/Message.framework/Message

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 80
-  Symbols:   114
-  CStrings:  183
+  Symbols:   115
+  CStrings:  184
 
Symbols:
+ _AccountPropertyRemoteManagementExchangeProtocolType
Functions:
~ sub_1848 -> sub_18c0 : 668 -> 716
CStrings:
+ "RemoteManagementExchangeProtocolType"
```
