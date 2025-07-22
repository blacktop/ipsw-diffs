## ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

-588.0.0.0.0
-  __TEXT.__text: 0x252130
-  __TEXT.__auth_stubs: 0x2da0
-  __TEXT.__objc_stubs: 0x11520
-  __TEXT.__objc_methlist: 0x9f50
-  __TEXT.__const: 0x5ab8
+591.100.0.0.0
+  __TEXT.__text: 0x2549ec
+  __TEXT.__auth_stubs: 0x2db0
+  __TEXT.__objc_stubs: 0x11580
+  __TEXT.__objc_methlist: 0x9fd8
+  __TEXT.__const: 0x5ad8
   __TEXT.__gcc_except_tab: 0x217c
-  __TEXT.__cstring: 0xe3dc
-  __TEXT.__oslogstring: 0x1c47b
-  __TEXT.__objc_methname: 0x1c058
-  __TEXT.__objc_classname: 0x2017
-  __TEXT.__objc_methtype: 0x54ef
-  __TEXT.__constg_swiftt: 0x313c
-  __TEXT.__swift5_typeref: 0x2e18
+  __TEXT.__cstring: 0xe44c
+  __TEXT.__oslogstring: 0x1c83b
+  __TEXT.__objc_methname: 0x1c118
+  __TEXT.__objc_classname: 0x2037
+  __TEXT.__objc_methtype: 0x5514
+  __TEXT.__constg_swiftt: 0x31a4
+  __TEXT.__swift5_typeref: 0x2f24
   __TEXT.__swift5_builtin: 0x1a4
-  __TEXT.__swift5_reflstr: 0x23b4
-  __TEXT.__swift5_fieldmd: 0x1710
-  __TEXT.__swift5_capture: 0x2c84
+  __TEXT.__swift5_reflstr: 0x2404
+  __TEXT.__swift5_fieldmd: 0x1740
+  __TEXT.__swift5_capture: 0x2cd0
   __TEXT.__swift5_assocty: 0x338
   __TEXT.__swift5_proto: 0x310
   __TEXT.__swift5_types: 0x1b8

   __TEXT.__swift_as_ret: 0x438
   __TEXT.__swift5_protos: 0x90
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x74c0
-  __TEXT.__eh_frame: 0xfdf0
-  __DATA_CONST.__auth_got: 0x16e0
-  __DATA_CONST.__got: 0x16a8
-  __DATA_CONST.__auth_ptr: 0x790
-  __DATA_CONST.__const: 0xb2e0
+  __TEXT.__unwind_info: 0x7530
+  __TEXT.__eh_frame: 0xfe68
+  __DATA_CONST.__auth_got: 0x16e8
+  __DATA_CONST.__got: 0x16b8
+  __DATA_CONST.__auth_ptr: 0x798
+  __DATA_CONST.__const: 0xb420
   __DATA_CONST.__cfstring: 0x4ae0
   __DATA_CONST.__objc_classlist: 0x678
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x568
+  __DATA_CONST.__objc_protolist: 0x580
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x188
+  __DATA_CONST.__objc_protorefs: 0x198
   __DATA_CONST.__objc_superrefs: 0x3a0
   __DATA_CONST.__objc_intobj: 0x390
   __DATA_CONST.__objc_doubleobj: 0x80
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x1ee28
-  __DATA.__objc_selrefs: 0x57a0
+  __DATA.__objc_const: 0x1f090
+  __DATA.__objc_selrefs: 0x57d0
   __DATA.__objc_ivar: 0x804
-  __DATA.__objc_data: 0x4938
-  __DATA.__data: 0x7be0
+  __DATA.__objc_data: 0x49c0
+  __DATA.__data: 0x7cb0
   __DATA.__bss: 0x4f30
   __DATA.__common: 0x130
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FAF802E9-BA84-3EFB-BAFB-0D0FE557A348
-  Functions: 7756
-  Symbols:   1601
-  CStrings:  8662
+  UUID: 0D457C9E-9BA7-39C4-9D34-DCE59F84BA3E
+  Functions: 7804
+  Symbols:   1605
+  CStrings:  8694
 
Symbols:
+ _$s10Foundation12NotificationV19_bridgeToObjectiveCSo14NSNotificationCyF
+ _$s15Synchronization5MutexVMn
+ _NSManagedObjectContextDidSaveNotification
+ _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "Context updated notification"
+ "Creating fetched results controller"
+ "Creating managed context"
+ "Error obtaining update delegate:%@"
+ "Exceptions list updated. Notifying %ld connections)"
+ "Failed to create app exceptions fetch context"
+ "Failed to create app exceptions fetch controller"
+ "Failed to fetch exceptions. Error:%@"
+ "Failed to fetch family circle for local user. Error: %{public}@"
+ "Failed to fetch user with error: %{public}@"
+ "Fetch controller did change content"
+ "Fetch succeeded. Fetched %ld exceptions"
+ "Fetching app exceptions"
+ "Fetching managing guardian Apple IDs for the local user."
+ "Local user is not managed. Returning an empty array of managing Apple IDs."
+ "Observing context save notifications"
+ "PersistenceController has not loaded stores with error: %{public}@"
+ "STAppExceptionsUpdateMonitoring"
+ "User is a managed child: %{BOOL}u or User has Web Content Filter enabled: %{BOOL}u and has passcode set: %{BOOL}u. Should enable denyHistoryClearing and denyPrivateBrowsing: %{public}d"
+ "activeConnections"
+ "appExceptionsDidUpdate"
+ "appleIDAliases"
+ "connection invalidated)"
+ "contextDidSave:"
+ "exceptionsListUpdateDelegate"
+ "familyOrgSettings"
+ "fetchAllAppExceptions. UserId: %@"
+ "fetchContext"
+ "fetchController"
+ "managingGuardianAppleIDsForLocalUserWithCompletionHandler:"
+ "mergeChangesFromContextDidSaveNotification:"
+ "remoteObjectProxyWithErrorHandler:"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "User is a managed child: %{public}d. User has Web Content Filter enabled and passcode set: %{public}d. Should enable denyHistoryClearing and denyPrivateBrowsing: %{public}d"

```
