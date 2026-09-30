## WelcomeKitCore

> `/System/Library/PrivateFrameworks/WelcomeKitCore.framework/WelcomeKitCore`

```diff

-128.120.2.0.0
-  __TEXT.__text: 0x36728
+701.0.0.0.0
+  __TEXT.__text: 0x3673c
   __TEXT.__auth_stubs: 0xd80
   __TEXT.__objc_methlist: 0x336c
   __TEXT.__const: 0x238

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: C118A962-B56E-3F80-99E5-CD9A1FEC67B8
+  UUID: C2D1B031-987E-330A-8D59-24BFD8E031FC
   Functions: 1181
   Symbols:   4623
   CStrings:  3616
Symbols:
+ -[WLMessagesMigrator _senderHandleIDFromReceivedGroupMessageHandleIDs:]
+ -[WLRemoteDeviceDataSource _maximumRetryableTaskDurationForLongServerOperations]
+ _objc_msgSend$_maximumRetryableTaskDurationForLongServerOperations
+ _objc_msgSend$_senderHandleIDFromReceivedGroupMessageHandleIDs:
- -[WLMessagesMigrator _senderHandleIDFromReceviedGroupMessageHandleIDs:]
- -[WLRemoteDeviceDataSource _maximumRetriableTaskDurationForLongServerOperations]
- _objc_msgSend$_maximumRetriableTaskDurationForLongServerOperations
- _objc_msgSend$_senderHandleIDFromReceviedGroupMessageHandleIDs:
Functions:
~ -[WLMigrator _importDataWithContext:failureDetailsBlock:] : 1852 -> 1872
CStrings:
+ "_maximumRetryableTaskDurationForLongServerOperations"
+ "_senderHandleIDFromReceivedGroupMessageHandleIDs:"
- "_maximumRetriableTaskDurationForLongServerOperations"
- "_senderHandleIDFromReceviedGroupMessageHandleIDs:"

```
