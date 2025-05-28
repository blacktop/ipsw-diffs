## CallHistorySyncHelper

> `/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper`

```diff

-1222.200.21.2.1
-  __TEXT.__text: 0x21bdc
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0x4600
-  __TEXT.__objc_methlist: 0x15a0
+1222.300.51.0.0
+  __TEXT.__text: 0x221a8
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_stubs: 0x4680
+  __TEXT.__objc_methlist: 0x15f0
   __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x2fc
+  __TEXT.__gcc_except_tab: 0x2f4
   __TEXT.__cstring: 0xf9f
-  __TEXT.__objc_methname: 0x5475
-  __TEXT.__oslogstring: 0x35f3
-  __TEXT.__objc_classname: 0x2b2
-  __TEXT.__objc_methtype: 0x12c9
+  __TEXT.__objc_methname: 0x5575
+  __TEXT.__oslogstring: 0x3717
+  __TEXT.__objc_classname: 0x28e
+  __TEXT.__objc_methtype: 0x12b8
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x6b8
-  __DATA_CONST.__auth_got: 0x3f8
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0xa48
+  __TEXT.__unwind_info: 0x6c4
+  __DATA_CONST.__auth_got: 0x410
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__const: 0xa28
   __DATA_CONST.__cfstring: 0xfa0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x47d8
-  __DATA.__objc_selrefs: 0x1518
+  __DATA.__objc_const: 0x4778
+  __DATA.__objc_selrefs: 0x1548
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x2b8
   __DATA.__objc_superrefs: 0xa0
-  __DATA.__objc_ivar: 0x1bc
+  __DATA.__objc_ivar: 0x1b8
   __DATA.__objc_data: 0x690
-  __DATA.__data: 0x4e0
+  __DATA.__data: 0x420
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 651
-  Symbols:   249
-  CStrings:  1649
+  Functions: 658
+  Symbols:   254
+  CStrings:  1658
 
Symbols:
+ _NSKeyValueChangeKindKey
+ _OBJC_CLASS_$_NSXPCConnection
+ _kCallDBManagerDataStoreType
+ _objc_sync_enter
+ _objc_sync_exit
+ _sel_isEqual
- _OBJC_CLASS_$_CHDeviceObserver
CStrings:
+ "\x03\x19"
+ "Data store changed to permanent; activating data store maintenance."
+ "Data store changed to permanent; activating iCloud."
+ "Data store changed to temporary; deactivating data store maintenance."
+ "Data store changed to temporary; deactivating iCloud."
+ "Device has not been unlocked since boot; rejecting access to %@ from connection %@"
+ "Prune operation failed with error %@"
+ "Pruned %ld calls from the data store."
+ "Q24@0:8@16"
+ "Received a key-value observing notification for key path (%@), object (%@)."
+ "T@\"CallHistoryDBClientHandle\",R,N,V_database"
+ "T@\"CallHistoryDBPrivacyPruner\",R,V_dbPrivacyPruner"
+ "T@\"NSXPCListener\",R,N,V_listener"
+ "activateDataStoreMaintenance"
+ "addObserver:forKeyPath:options:context:"
+ "canAccessListenerInterfaceSelector:"
+ "currentConnection"
+ "dbPrivacyPruner"
+ "deactivateDataStoreMaintenance"
+ "listener"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "pruneCallsWithPredicate:"
+ "removeObserver:forKeyPath:context:"
+ "updateDataStoreMaintenance"
+ "v48@0:8@16@24@32^v40"
- "\x06\x17"
- "@\"CHDeviceObserver\""
- "CHDelegate"
- "CHDeviceObserverDelegate"
- "Could not delete calls; operation failed with error %@"
- "Deleted %ld calls from the data store."
- "Device has not been unlocked since boot; rejecting connection %@"
- "Goodbye from client pid=%d"
- "T@\"CHDeviceObserver\",R,N,V_deviceObserver"
- "_deviceObserver"
- "deviceObserver"
- "didChangeBootLockEnabledForDeviceObserver:"
- "handleClientDisconnect:"
- "isBootLockEnabled"
- "setInvalidationHandler:"
- "v24@0:8@\"CHDeviceObserver\"16"

```
