## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1450.600.53.2.3
-  __TEXT.__text: 0xc4590
-  __TEXT.__auth_stubs: 0x1c40
-  __TEXT.__objc_stubs: 0xd300
-  __TEXT.__objc_methlist: 0x29c4
+1450.600.61.2.7
+  __TEXT.__text: 0xc4fe8
+  __TEXT.__auth_stubs: 0x1c50
+  __TEXT.__objc_stubs: 0xd3e0
+  __TEXT.__objc_methlist: 0x29dc
   __TEXT.__const: 0xe58
-  __TEXT.__gcc_except_tab: 0xa0a4
-  __TEXT.__cstring: 0x329d
-  __TEXT.__oslogstring: 0x1744b
+  __TEXT.__gcc_except_tab: 0xa168
+  __TEXT.__cstring: 0x337d
+  __TEXT.__oslogstring: 0x1765b
   __TEXT.__objc_classname: 0x61c
-  __TEXT.__objc_methname: 0x12854
+  __TEXT.__objc_methname: 0x12924
   __TEXT.__objc_methtype: 0x2c79
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x67e

   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2338
+  __TEXT.__unwind_info: 0x2350
   __TEXT.__eh_frame: 0x988
-  __DATA_CONST.__auth_got: 0xe30
-  __DATA_CONST.__got: 0x10d8
+  __DATA_CONST.__auth_got: 0xe38
+  __DATA_CONST.__got: 0x10f0
   __DATA_CONST.__auth_ptr: 0x1d8
   __DATA_CONST.__const: 0x3a88
-  __DATA_CONST.__cfstring: 0x3860
+  __DATA_CONST.__cfstring: 0x3900
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x2e08
-  __DATA.__objc_selrefs: 0x3ac8
+  __DATA.__objc_selrefs: 0x3b00
   __DATA.__objc_ivar: 0x1c8
   __DATA.__objc_data: 0x9c0
   __DATA.__data: 0xa60

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 80A9FB57-6C21-32C6-911A-07E61936D1BE
-  Functions: 1671
-  Symbols:   893
-  CStrings:  5124
+  UUID: D0802B17-7D69-398E-BD86-F3BF01AA030F
+  Functions: 1674
+  Symbols:   897
+  CStrings:  5149
 
Symbols:
+ _IMFileTransferFilenameKey
+ _IMFileTransferGroupPhotoName
+ _IMFileTransferUnsafeGroupPhotoName
+ _IMServerBagValueForKnownSender
CStrings:
+ " => failed to remove unsafe group photo file (%@) error: %@"
+ " => failed to rename safe group photo from %@ to %@, error: %@"
+ "Dropping command %@ from %@ via server bag"
+ "Dropping generic notification %@ from %@ via server bag"
+ "Dropping group message command %@ from %@ via server bag"
+ "Dropping push error %d from %@ via server bag"
+ "IMDNotificationsController-force-notify"
+ "MessagePushHandler-unsupported-push-commands"
+ "MessageServiceSession-unsupported-generic-notifications"
+ "MessageServiceSession-unsupported-group-messages"
+ "MessageServiceSession-unsupported-push-errors"
+ "Rejecting group photo because BlastDoor safe render replacement did not occur. transferGuid: %@"
+ "Rejecting group photo because filename was not replaced with safe name. filename: %@, transferGuid: %@"
+ "URLByAppendingPathComponent:"
+ "_moveToSafePathWith:downloadedGroupPhotoURL:"
+ "_shouldRejectGroupPhotoFileTransfer:"
+ "replacedWithBlastDoorVersionDuringFinalize"
+ "setFilename:"
+ "setMmcsInfo:"
+ "setReplacedWithBlastDoorVersionDuringFinalize:"

```
