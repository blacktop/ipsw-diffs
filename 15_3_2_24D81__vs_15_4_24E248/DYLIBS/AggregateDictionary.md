## AggregateDictionary

> `/System/Library/PrivateFrameworks/AggregateDictionary.framework/Versions/A/AggregateDictionary`

```diff

 437.0.0.0.0
-  __TEXT.__text: 0x418
+  __TEXT.__text: 0x440
   __TEXT.__auth_stubs: 0x60
   __TEXT.__objc_methlist: 0x34
   __TEXT.__const: 0x10

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 81976928-DABD-365F-9DAC-DCF70A84C96E
-  Functions: 19
-  Symbols:   38
+  UUID: 5F62D5B1-41F7-3F77-851B-73327F8F5F55
+  Functions: 21
+  Symbols:   50
   CStrings:  9
 
Symbols:
+ ADClientAddValueForScalarKey.cold.1
+ ADClientBatchKeys.cold.1
+ ADClientCheckpoint.cold.1
+ ADClientClearDistributionKey.cold.1
+ ADClientClearScalarKey.cold.1
+ ADClientCommit.cold.1
+ ADClientIsEnabled.cold.1
+ ADClientPushValueForDistributionKey.cold.1
+ ADClientSetValueForDistributionKey.cold.1
+ ADClientSetValueForScalarKey.cold.1
+ ADClientSignificantTimeChanged.cold.1
+ ADPushTimeIntervalForDistributionKeySinceStartTime.cold.1
Functions:
~ _ADClientPushValueForDistributionKey : 40 -> 44
~ _ADClientAddValueForScalarKey : 40 -> 44
~ _ADClientClearScalarKey : 40 -> 44
~ _ADClientSetValueForScalarKey : 40 -> 44
~ _ADClientIsEnabled : 64 -> 52
~ _ADClientCommit : 64 -> 52
~ _ADClientCheckpoint : 64 -> 52
~ _ADClientSignificantTimeChanged : 40 -> 44
~ _ADClientClearDistributionKey : 40 -> 44
~ _ADClientSetValueForDistributionKey : 40 -> 44
~ _ADClientBatchKeys : 40 -> 44
~ _ADPushTimeIntervalForDistributionKeySinceStartTime : 176 -> 160

```
