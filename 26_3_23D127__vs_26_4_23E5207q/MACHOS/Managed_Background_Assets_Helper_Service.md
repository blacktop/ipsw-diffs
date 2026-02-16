## Managed Background Assets Helper Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/XPCServices/Managed Background Assets Helper Service.xpc/Managed Background Assets Helper Service`

```diff

-1.2.1.0.0
-  __TEXT.__text: 0x9804
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_stubs: 0x40
+1.4.9.0.0
+  __TEXT.__text: 0x73e0
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__objc_stubs: 0x220
   __TEXT.__objc_methlist: 0x124
-  __TEXT.__const: 0x376
+  __TEXT.__const: 0x428
   __TEXT.__gcc_except_tab: 0x10
-  __TEXT.__objc_classname: 0x37
-  __TEXT.__objc_methname: 0x3c4
-  __TEXT.__objc_methtype: 0xe0
-  __TEXT.__cstring: 0x682
+  __TEXT.__objc_classname: 0x7d
+  __TEXT.__objc_methtype: 0x102
+  __TEXT.__cstring: 0x39c
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__constg_swiftt: 0x21c
-  __TEXT.__swift5_typeref: 0x220
+  __TEXT.__constg_swiftt: 0x234
+  __TEXT.__swift5_typeref: 0x306
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x168
-  __TEXT.__swift5_fieldmd: 0x150
-  __TEXT.__swift5_types: 0x1c
-  __TEXT.__swift5_proto: 0xc
-  __TEXT.__oslogstring: 0x4f7
-  __TEXT.__swift5_types2: 0x8
+  __TEXT.__swift5_reflstr: 0x176
+  __TEXT.__swift5_fieldmd: 0x198
+  __TEXT.__swift5_proto: 0x20
+  __TEXT.__swift5_types: 0x18
+  __TEXT.__objc_methname: 0x3ee
+  __TEXT.__oslogstring: 0x4e3
+  __TEXT.__swift5_types2: 0xc
+  __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_capture: 0xb4
-  __TEXT.__swift_as_entry: 0x14
-  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__swift_as_entry: 0x4
+  __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2a8
-  __TEXT.__eh_frame: 0x3f0
-  __DATA_CONST.__auth_got: 0x6a0
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__auth_ptr: 0x118
-  __DATA_CONST.__const: 0x460
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__unwind_info: 0x210
+  __TEXT.__eh_frame: 0x1e8
+  __DATA_CONST.__auth_got: 0x5a0
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__auth_ptr: 0x178
+  __DATA_CONST.__const: 0x480
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0x320
+  __DATA.__objc_const: 0x2b0
   __DATA.__objc_selrefs: 0x128
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x548
-  __DATA.__bss: 0x190
-  __DATA.__common: 0x8
+  __DATA.__data: 0x4a0
+  __DATA.__bss: 0x390
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/LightweightCodeRequirements.framework/LightweightCodeRequirements
   - /System/Library/PrivateFrameworks/ManagedBackgroundAssetsHelper.framework/ManagedBackgroundAssetsHelper
+  - /System/Library/PrivateFrameworks/ManagedBackgroundAssetsXPC.framework/ManagedBackgroundAssetsXPC
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A3766E41-48CD-3D78-BF50-B957612EAB45
-  Functions: 164
-  Symbols:   152
-  CStrings:  126
+  UUID: 16E85A24-B05B-3CCB-AA82-94E80416EC61
+  Functions: 139
+  Symbols:   140
+  CStrings:  110
 
Symbols:
+ _objc_retain_x24
+ _objc_retain_x25
+ _swift_allocateGenericClassMetadata
+ _swift_bridgeObjectRelease_n
+ _swift_checkMetadataState
+ _swift_getGenericMetadata
+ _swift_initClassMetadata2
- _OBJC_CLASS_$_OS_dispatch_queue
- _SecTaskCopySigningIdentifier
- _SecTaskCreateWithAuditToken
- __Block_copy
- __Block_release
- _dispatch_sync
- _objc_claimAutoreleasedReturnValue
- _objc_release_x28
- _objc_retain_x23
- _objc_retain_x26
- _objc_retain_x3
- _objc_retain_x8
- _objc_retain_x9
- _swift_deallocObject
- _swift_getErrorValue
- _swift_isEscapingClosureAtFileLocation
- _swift_task_create
- _swift_task_isCurrentExecutor
- _swift_task_reportUnexpectedExecutor
CStrings:
+ "A lightweight code requirement couldn’t be created: %{public}@"
+ "Acquiring the transaction “%{public}s” at +0x%llX…"
+ "Entering the activity “%{public}s”…"
+ "Leaving the activity “%{public}s”…"
+ "Relinquishing a transaction acquired at +0x%llX after %{public}s…"
+ "Relinquishing a transaction…"
+ "Relinquishing the transaction “%{public}s” as acquired at +0x%llX after %{public}s…"
+ "Relinquishing the transaction “%{public}s”…"
+ "The Helper Service was launched as root, which isn’t supported. Switching to mobile…"
+ "The current timestamp couldn’t be retrieved: %{public}@"
+ "activity"
+ "referenceCount"
+ "value"
- "%{public}@"
- "A message couldn’t be decoded: %{public}@"
- "A security task couldn’t be created."
- "A session was canceled: %{public}@"
- "Activating the listener…"
- "Creating a listener…"
- "Fatal error"
- "Handing off responsibility for replying synchronously to “%{public}s” to the queue “%{public}@”…"
- "Helper Service Activation"
- "HelperServiceSync"
- "Imbalance in transaction accounting!"
- "ManagedBackgroundAssetsHelperService/HelperService.swift"
- "ManagedBackgroundAssetsHelperService/Transaction.swift"
- "Rejecting a session request…"
- "The app record for the bundle ID “"
- "The helper service was launched as root, which isn’t supported. Switching to mobile…"
- "The message “%{public}s” was received."
- "The peer lacks a signing ID."
- "The signing ID couldn’t be copied: "
- "The signing ID couldn’t be copied: %{public}@"
- "XPC Request Handler"
- "[TXN%.*hX] 🐏 Acquiring transaction (%s)"
- "[TXN%.*hX] 🐏 Releasing transaction (%s) (%s)"
- "_TtCV36ManagedBackgroundAssetsHelperService11TransactionP33_5FBBF6D2B35B8693B996FCF36CC421A719SendableTransaction"
- "logActivity"
- "rawTransaction"
- "” couldn’t be looked up: "

```
