## SyncedDefaultsDaemon

> `/System/Library/PrivateFrameworks/SyncedDefaultsDaemon.framework/SyncedDefaultsDaemon`

```diff

-2260.12.0.0.0
-  __TEXT.__text: 0x37708
+2300.109.0.0.0
+  __TEXT.__text: 0x375d4
   __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_methlist: 0x1724
+  __TEXT.__objc_methlist: 0x173c
   __TEXT.__const: 0x126
-  __TEXT.__gcc_except_tab: 0x1138
+  __TEXT.__gcc_except_tab: 0x1108
   __TEXT.__cstring: 0x2169
-  __TEXT.__oslogstring: 0x6c7f
+  __TEXT.__oslogstring: 0x6c20
   __TEXT.__dlopen_cstrs: 0xb5
   __TEXT.__swift5_typeref: 0x5
-  __TEXT.__unwind_info: 0xc38
+  __TEXT.__unwind_info: 0xbf0
   __TEXT.__objc_classname: 0x1f6
-  __TEXT.__objc_methname: 0x5dd5
+  __TEXT.__objc_methname: 0x5e19
   __TEXT.__objc_methtype: 0xd3b
-  __TEXT.__objc_stubs: 0x4fe0
-  __DATA_CONST.__got: 0x450
-  __DATA_CONST.__const: 0xd48
+  __TEXT.__objc_stubs: 0x5020
+  __DATA_CONST.__got: 0x458
+  __DATA_CONST.__const: 0xd28
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1730
+  __DATA_CONST.__objc_selrefs: 0x1740
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x1f8
   __AUTH_CONST.__auth_got: 0x588
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x21e0
-  __AUTH_CONST.__objc_const: 0x1908
+  __AUTH_CONST.__objc_const: 0x1918
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x348

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 240CEAB1-53B0-3616-81F3-2AEB06A89C0C
-  Functions: 1135
-  Symbols:   3736
-  CStrings:  2183
+  UUID: 430EE0AD-740B-39BD-B94B-C9A08E74CAEF
+  Functions: 1137
+  Symbols:   3725
+  CStrings:  2185
 
Symbols:
+ -[SYDDaemonToClientConnection entitlements]
+ -[SYDDaemonToClientConnection relatedApplicationsForStoreIdentifier:]
+ GCC_except_table52
+ GCC_except_table72
+ GCC_except_table99
+ _OBJC_CLASS_$_SYDEntitlements
+ ___64-[SYDDaemonToClientConnection syncManagerDidChangeNotification:]_block_invoke.139
+ ___71-[SYDDaemonToClientConnection daemonToClientConnectionDidChangeValues:]_block_invoke.153
+ ___74-[SYDDaemonToClientConnection processAccountChangesWithCompletionHandler:]_block_invoke.137
+ ___79-[SYDDaemonToClientConnection saveChangeToken:forStoreWithConfiguration:reply:]_block_invoke.128
+ ___79-[SYDDaemonToClientConnection saveChangeToken:forStoreWithConfiguration:reply:]_block_invoke.128.cold.1
+ ___93-[SYDDaemonToClientConnection registerForChangeNotificationsForStoreWithConfiguration:reply:]_block_invoke.119
+ ___97-[SYDDaemonToClientConnection notifyAccountDidChangeFromAccountID:toAccountID:completionHandler:]_block_invoke.151.cold.1
+ ___97-[SYDDaemonToClientConnection notifyAccountDidChangeFromAccountID:toAccountID:completionHandler:]_block_invoke.151.cold.2
+ ___97-[SYDDaemonToClientConnection notifyAccountDidChangeFromAccountID:toAccountID:completionHandler:]_block_invoke.152
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SyncedDefaultsDaemon
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SyncedDefaultsDaemon
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SyncedDefaultsDaemon
+ _objc_msgSend$additionalStoreIdentifiers
+ _objc_msgSend$initWithAuditToken:
+ _objc_msgSend$initWithBundleRecord:
+ _objc_msgSend$relatedApplicationsForStoreIdentifier:
+ _objc_msgSend$storeIdentifiers
+ _saveChangeToken:forStoreWithConfiguration:reply:.onceToken.127
- GCC_except_table50
- GCC_except_table68
- GCC_except_table9
- ___64-[SYDDaemonToClientConnection syncManagerDidChangeNotification:]_block_invoke.138
- ___71-[SYDDaemonToClientConnection daemonToClientConnectionDidChangeValues:]_block_invoke.152
- ___74-[SYDDaemonToClientConnection processAccountChangesWithCompletionHandler:]_block_invoke.136
- ___79-[SYDDaemonToClientConnection saveChangeToken:forStoreWithConfiguration:reply:]_block_invoke.127
- ___79-[SYDDaemonToClientConnection saveChangeToken:forStoreWithConfiguration:reply:]_block_invoke.127.cold.1
- ___93-[SYDDaemonToClientConnection registerForChangeNotificationsForStoreWithConfiguration:reply:]_block_invoke.118
- ___97-[SYDDaemonToClientConnection notifyAccountDidChangeFromAccountID:toAccountID:completionHandler:]_block_invoke.150
- ___97-[SYDDaemonToClientConnection notifyAccountDidChangeFromAccountID:toAccountID:completionHandler:]_block_invoke.150.cold.1
- ___97-[SYDDaemonToClientConnection notifyAccountDidChangeFromAccountID:toAccountID:completionHandler:]_block_invoke.150.cold.2
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_SyncedDefaultsDaemon
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_SyncedDefaultsDaemon
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_SyncedDefaultsDaemon
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_SyncedDefaultsDaemon
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_SyncedDefaultsDaemon
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_SyncedDefaultsDaemon
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_SyncedDefaultsDaemon
- _objc_msgSend$objectForKey:ofClass:
- _objc_msgSend$objectForKey:ofClass:valuesOfClass:
- _objc_msgSend$setNeedsToReloadAccount:
- _saveChangeToken:forStoreWithConfiguration:reply:.onceToken.126
CStrings:
+ "Bundle %@ has Ubiquity disabled and is entitled to store identifiers: %@"
+ "Found registered store %@, but no application identifier from %@"
+ "T@\"SYDEntitlements\",R,C,N"
+ "Unable to find key-value to post notification for %@"
+ "additionalStoreIdentifiers"
+ "initWithAuditToken:"
+ "initWithBundleRecord:"
+ "relatedApplicationsForStoreIdentifier:"
+ "storeIdentifiers"
- "Bundle %@ has Ubiquity disabled and is entitled to defaultStoreIdentifier=%@ additionalStoreIdentifiers=%@"
- "Found registered store in %@, but no application identifier from %@"
- "Unable to find key to post notification for %@"
- "Will tell sync engine to reload the account for sync manager %@"
- "objectForKey:ofClass:"
- "objectForKey:ofClass:valuesOfClass:"
- "setNeedsToReloadAccount:"

```
