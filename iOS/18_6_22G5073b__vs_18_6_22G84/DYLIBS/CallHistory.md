## CallHistory

> `/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory`

```diff

-55.700.1.0.0
-  __TEXT.__text: 0x3a1e8
+55.700.11.0.0
+  __TEXT.__text: 0x3a374
   __TEXT.__auth_stubs: 0x760
   __TEXT.__objc_methlist: 0x36bc
-  __TEXT.__cstring: 0x2500
+  __TEXT.__cstring: 0x2501
   __TEXT.__const: 0x358
-  __TEXT.__oslogstring: 0x4dd9
+  __TEXT.__oslogstring: 0x4e5f
   __TEXT.__gcc_except_tab: 0x6f4
   __TEXT.__dlopen_cstrs: 0xf9
   __TEXT.__unwind_info: 0xee0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1708D2A9-C538-3EA0-9242-CCB19C3F46CB
+  UUID: 5A2543A7-3A49-3C72-A713-1416C46B610B
   Functions: 1346
-  Symbols:   5105
-  CStrings:  2907
+  Symbols:   5111
+  CStrings:  2910
 
Symbols:
+ +[DBManager migrateDataStoreAtLocation:withGetDestinationModel:isEncrypted:].cold.7
+ -[CallDBManagerClient willMoveCallsFromTempDatabase].cold.5
+ -[CallDBManagerClient willMoveCallsFromTempDatabase].cold.6
CStrings:
+ "55.700.11"
+ "55.700.11~13"
+ "Failed to get DBManager instance with modelURL: %{public}@"
+ "Failed to get moc"
+ "Failed to get the destination model URL with version %ld"
- "55.700.1"
- "55.700.1~437"

```
