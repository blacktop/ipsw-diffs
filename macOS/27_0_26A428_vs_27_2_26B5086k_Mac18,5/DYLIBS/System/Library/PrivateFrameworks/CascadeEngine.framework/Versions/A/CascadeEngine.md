## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/Versions/A/CascadeEngine`

```diff

-250.0.0.3.0
-  __TEXT.__text: 0x66d98
-  __TEXT.__objc_methlist: 0x1ef4
-  __TEXT.__const: 0x1268
+255.0.2.0.0
+  __TEXT.__text: 0x67f88
+  __TEXT.__objc_methlist: 0x1f2c
+  __TEXT.__const: 0x1280
   __TEXT.__gcc_except_tab: 0x6f4
-  __TEXT.__cstring: 0x2ba4
+  __TEXT.__cstring: 0x2acf
   __TEXT.__ustring: 0x84
-  __TEXT.__oslogstring: 0x6b49
+  __TEXT.__oslogstring: 0x6cff
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__swift5_typeref: 0xde0
+  __TEXT.__swift5_typeref: 0xe32
   __TEXT.__swift5_reflstr: 0x31e
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__constg_swiftt: 0x5c0

   __TEXT.__swift_as_entry: 0x98
   __TEXT.__swift_as_ret: 0x98
   __TEXT.__swift_as_cont: 0xdc
-  __TEXT.__unwind_info: 0x1ae8
-  __TEXT.__eh_frame: 0x17a8
+  __TEXT.__unwind_info: 0x1b20
+  __TEXT.__eh_frame: 0x1840
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__got: 0x680
   __AUTH_CONST.__const: 0x35d8
-  __AUTH_CONST.__cfstring: 0x1a20
-  __AUTH_CONST.__objc_const: 0x5148
+  __AUTH_CONST.__cfstring: 0x19e0
+  __AUTH_CONST.__objc_const: 0x5168
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xd20
+  __AUTH_CONST.__auth_got: 0xd38
   __AUTH.__objc_data: 0x648
-  __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x2c4
-  __DATA.__data: 0xe08
+  __AUTH.__data: 0x58
+  __DATA.__objc_ivar: 0x2c8
+  __DATA.__data: 0xe20
   __DATA_DIRTY.__objc_data: 0xb00
   __DATA_DIRTY.__data: 0x4b0
   __DATA_DIRTY.__bss: 0x430

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2356
-  Symbols:   2875
-  CStrings:  831
+  Functions: 2386
+  Symbols:   2885
+  CStrings:  834
 
Symbols:
+ +[CCSyncManager isCloudKitFeatureFlagEnabled]
+ +[CCSyncManager isCloudKitSyncEnabledByTrial]
+ -[CCRapportManager _isFileTransferSessionPossible:]
+ -[CCSyncManager sharedCloudKitSyncEngine]
+ GCC_except_table45
+ OBJC_IVAR_$_CCSyncManager._cloudKitSyncEngineLock
+ _OUTLINED_FUNCTION_202
+ __OBJC_$_CLASS_METHODS_CCSyncManager
+ _objc_msgSend$_isFileTransferSessionPossible:
+ _objc_msgSend$createCloudKitSyncEngineWithSyncStateStorage:
+ _objc_msgSend$currentPlatformHasCloudKitEnabledSets
+ _objc_msgSend$isCloudKitFeatureFlagEnabled
+ _objc_msgSend$isCloudKitSyncEnabledByTrial
+ _objc_msgSend$sharedCloudKitSyncEngine
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _symbolic So8NSObjectC3key______5valuet 13CascadeEngine10TimedCacheC5Entry33_900D586F8B467B403EE930617B3CC2C0LLC
+ _symbolic _____ySnySiGG s23_ContiguousArrayStorageC
+ _symbolic _____ySo8NSObjectC3key______5valuetG s23_ContiguousArrayStorageC 13CascadeEngine10TimedCacheC5Entry33_900D586F8B467B403EE930617B3CC2C0LLC
- +[CCSyncManager isCloudKitSyncEnabled]
- __OBJC_$_CLASS_METHODS_CCSyncManager(CascadeEngine)
- _objc_msgSend$closeWithError:
- _objc_msgSend$errorFlags
- _objc_msgSend$isCloudKitSyncEnabled
- _objc_msgSend$setValue:forKey:
- _objc_msgSend$syncStateStorage
- _objc_msgSend$valueForKey:
CStrings:
+ "Cascade/CascadeCloudkitSync disabled; skipping CloudKit sync engine"
+ "CloudKit sync disabled by Trial"
+ "CloudKit sync disabled by Trial; skipping CloudKit sync engine"
+ "Evicting least-recently-accessed evictable entry to honor countLimit %s: %{public}@"
+ "Failed to evaluate CloudKit-enabled sets for eager init: %@, creating sync engine"
+ "No CloudKit-enabled sets for this platform; skipping CloudKit sync engine"
+ "TimedCache deinit: releasing %ld cached entry(s)"
+ "WALTruncator skipping %s — write in flight"
- "Client not initiating RPFileTransferSession because WiFi is off"
- "Evicting least-recently-accessed entry to honor countLimit %s: %{public}@"
- "Server not fullfilling RPFileTransferSession because WiFi is off"
- "TimedCache deinit: evicting all entries"
- "_cloudKitSyncEngine"
```
