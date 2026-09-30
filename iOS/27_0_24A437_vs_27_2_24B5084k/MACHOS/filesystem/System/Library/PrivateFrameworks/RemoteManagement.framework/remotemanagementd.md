## remotemanagementd

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-624.2.3.0.0
-  __TEXT.__text: 0x89790
+624.40.12.0.0
+  __TEXT.__text: 0x8b1e0
   __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_stubs: 0xc3a0
-  __TEXT.__objc_methlist: 0x4a28
+  __TEXT.__objc_stubs: 0xc500
+  __TEXT.__objc_methlist: 0x4b00
   __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0x3fe8
-  __TEXT.__cstring: 0x3044
+  __TEXT.__gcc_except_tab: 0x408c
+  __TEXT.__cstring: 0x3150
   __TEXT.__objc_classname: 0x1032
-  __TEXT.__objc_methname: 0xf15e
-  __TEXT.__objc_methtype: 0x265e
-  __TEXT.__oslogstring: 0xc31b
+  __TEXT.__objc_methname: 0xf419
+  __TEXT.__objc_methtype: 0x269e
+  __TEXT.__oslogstring: 0xc65f
   __TEXT.__ustring: 0x2ec
-  __TEXT.__unwind_info: 0x2c98
-  __DATA_CONST.__const: 0x2760
-  __DATA_CONST.__cfstring: 0x3480
+  __TEXT.__unwind_info: 0x2d18
+  __DATA_CONST.__const: 0x27a0
+  __DATA_CONST.__cfstring: 0x34e0
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x108

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x150
   __DATA_CONST.__auth_got: 0x448
-  __DATA_CONST.__got: 0x9e8
-  __DATA.__objc_const: 0x86a8
-  __DATA.__objc_selrefs: 0x3538
-  __DATA.__objc_ivar: 0x2ac
+  __DATA_CONST.__got: 0x9f8
+  __DATA.__objc_const: 0x8740
+  __DATA.__objc_selrefs: 0x35a8
+  __DATA.__objc_ivar: 0x2b8
   __DATA.__objc_data: 0x1db0
   __DATA.__data: 0xc68
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2566
-  Symbols:   433
-  CStrings:  3885
+  Functions: 2595
+  Symbols:   435
+  CStrings:  3928
 
Symbols:
+ _OBJC_CLASS_$_RMThrottlingDebounceTimer
+ _OBJC_CLASS_$_RMXPCUtilities
CStrings:
+ "\f"
+ "(%K != nil) && ((%K == %d) || (%K == %d)) && (%K == YES) && (%K in %@)"
+ "(%K == %@) && ((%K == %d) || (%K == %d) || (%K == %d))"
+ "(%K == %@) && ((%K == %d) || (%K == %d) || (%K == %d)) && (%K == %@)"
+ "(%K == %@) && ((%K == %d) || (%K == %d) || (%K == %d)) && (%K in %@)"
+ "(%K == %@) && ((%K == %d) || (%K == %d)) && (%K == YES)"
+ "(%K == %@) && ((%K == %d) || (%K == %d)) && (%K == YES) && (%K in %@)"
+ "(%K == %@) && ((%K == %d) || (%K == %d)) && (%K == YES) && (%K in %@) && ((%K == NULL) || (%K == YES))"
+ "(%K == %@) && ((%K == %d) || (%K == %d)) && (%K IN %@)"
+ "(%K == %@) AND ((%K == %d) OR (%K == %d) OR ((%K != NULL) AND (%K.%K == YES)))"
+ "(%K == %@) AND ((%K == %d) OR (%K == %d)) AND (%K == %@)"
+ "@\"RMThrottlingDebounceTimer\""
+ "@36@0:8#16@24s32"
+ "ACME credential has invalid Subject value type"
+ "Already marked for deletion: %{public}@"
+ "Already proposed for deletion: %{public}@"
+ "B36@0:8@16s24^@28"
+ "B48@0:8@16@24@32@40"
+ "Deleted, never loaded: %{public}@"
+ "Loaded: %{public}@"
+ "Proposed for deletion: %{public}@"
+ "Proposed loaded: %{public}@"
+ "RMMigrationConfigurationUI2"
+ "Rejecting connection %{public}@ from non-platform binary"
+ "Restored to loaded: %{public}@"
+ "SCEP credential has invalid Subject value type"
+ "T@\"NSMutableSet\",&,N,V_pendingThrottledEventKeys"
+ "T@\"RMThrottlingDebounceTimer\",&,N,V_notificationThrottler"
+ "TB,R,N,V_hasSettingsEntitlement"
+ "Unable to find declarations of class %{public}@ with load state %d: %{public}@"
+ "Unable to save declaration changes for completed sync: %{public}@"
+ "_commitDeclarationChangesForCompletedSyncReturningError:"
+ "_declarationsOfClass:managementSource:loadState:"
+ "_hasSettingsEntitlement"
+ "_isValidSubject:"
+ "_loadPayload:loadedState:error:"
+ "_notificationThrottler"
+ "_pendingThrottledEventKeys"
+ "_publishStatusForEventKey:"
+ "_publishStatusForPendingEventKeys"
+ "com.apple.private.remotemanagement.settings"
+ "doesConnection:haveEntitlement:"
+ "hasSettingsEntitlement"
+ "isHashMismatchedWithExpectedHash:data:downloadURL:declaredSize:"
+ "isPlatformBinaryForConnection:"
+ "isSubclassOfClass:"
+ "loadPayloadAsProposed:error:"
+ "notificationThrottler"
+ "pendingThrottledEventKeys"
+ "proposed delete"
+ "proposed loaded"
+ "setNotificationThrottler:"
+ "setPendingThrottledEventKeys:"
+ "throttlingDebounceTimerWithThreshold:window:minimumInterval:maximumInterval:identifier:action:"
+ "⚫️ New: id='%{public}@' token='%{public}@'"
+ "🔴 Commit deleted: %{public}@"
+ "🔴 Commit marked for deletion: %{public}@"
+ "🔴 Deleted, never loaded: id='%{public}@' token='%{public}@'"
+ "🔵 Already marked for deletion: id='%{public}@' token='%{public}@'"
+ "🔵 Already proposed for deletion: id='%{public}@' token='%{public}@'"
+ "🟠 Proposed for deletion: id='%{public}@' token='%{public}@'"
+ "🟡 Proposed loaded: id='%{public}@' token='%{public}@'"
+ "🟢 Commit loaded: %{public}@"
+ "🟢 Restored to loaded: id='%{public}@' token='%{public}@'"
- "(%K != nil) && (%K == %d) && (%K == YES) && (%K in %@)"
- "(%K == %@) && (%K == %d) && (%K == YES)"
- "(%K == %@) && (%K == %d) && (%K == YES) && (%K in %@)"
- "(%K == %@) && (%K == %d) && (%K == YES) && (%K in %@) && ((%K == NULL) || (%K == YES))"
- "(%K == %@) && (%K == %d) && (%K IN %@)"
- "(%K == %@) && ((%K == %d) || (%K == %d))"
- "(%K == %@) && ((%K == %d) || (%K == %d)) && (%K == %@)"
- "(%K == %@) && ((%K == %d) || (%K == %d)) && (%K in %@)"
- "(%K == %@) AND (%K == %d) AND (%K == %@)"
- "(%K == %@) AND ((%K == %d) OR ((%K != NULL) AND (%K.%K == YES)))"
- "5@`"
- "AAACCOUNTS.com.apple.accountsd"
- "B48@0:8@16@24@32Q40"
- "Fetched partial object %{public}@: id='%{public}@' token='%{public}@'"
- "_doesConnection:haveEntitlement:"
- "_doesConnection:haveEntitlements:"
- "com.apple.purplebuddy"
- "isHashMismatchedWithExpectedHash:data:downloadURL:dataSize:"
- "🔴 Deleted: id='%{public}@' token='%{public}@'"
- "🟠 Marked for deletion: id='%{public}@' token='%{public}@'"
- "🟢 New: id='%{public}@' token='%{public}@'"
```
