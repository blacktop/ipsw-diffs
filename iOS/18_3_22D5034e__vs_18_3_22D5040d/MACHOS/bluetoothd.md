## bluetoothd

> `/usr/sbin/bluetoothd`

```diff

-183.5.2.1.1
-  __TEXT.__text: 0x794f38
+183.7.2.0.0
+  __TEXT.__text: 0x796ba8
   __TEXT.__auth_stubs: 0x45e0
   __TEXT.__objc_stubs: 0x127e0
   __TEXT.__init_offsets: 0x54
   __TEXT.__objc_methlist: 0x55a4
   __TEXT.__const: 0xa1fc
-  __TEXT.__gcc_except_tab: 0x5f2a0
-  __TEXT.__cstring: 0x9b94a
+  __TEXT.__gcc_except_tab: 0x5f338
+  __TEXT.__cstring: 0x9bbb6
   __TEXT.__objc_classname: 0x7c4
   __TEXT.__objc_methname: 0x15548
   __TEXT.__objc_methtype: 0x44a8
-  __TEXT.__oslogstring: 0x9ec64
+  __TEXT.__oslogstring: 0x9f15b
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x1e818
+  __TEXT.__unwind_info: 0x1e898
   __DATA_CONST.__auth_got: 0x2308
   __DATA_CONST.__got: 0xcc8
   __DATA_CONST.__auth_ptr: 0x168
-  __DATA_CONST.__const: 0x2a850
-  __DATA_CONST.__cfstring: 0x1eca0
+  __DATA_CONST.__const: 0x2a9c8
+  __DATA_CONST.__cfstring: 0x1ecc0
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb0

   __DATA.__objc_data: 0x1450
   __DATA.__data: 0x43c8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1871a
+  __DATA.__bss: 0x1880a
   __DATA.__common: 0x5af8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 28290
+  Functions: 28318
   Symbols:   1540
-  CStrings:  34597
+  CStrings:  34632
 
CStrings:
+ "23:59:28"
+ "BT_AbortSleepWithContext com.apple.BTStack.AbortSleep.%s returned %d systemState %d"
+ "BT_CancelAbortSleep apple.BTStack.AbortSleep.%s returned %d"
+ "Dec 17 2024"
+ "HCI_ACI_PACKET_TYPE"
+ "LeBroadcaster::updateAdvertisement System about to go to sleep, but in the middle of reconfig"
+ "LeBroadcaster::updateAdvertisement System about to go to sleep, will try again later"
+ "LeObserver::addUniqueMatchRulesToDictionary ignoring type %d(%s) fSystemWillSleep:%d requiresWA:%d"
+ "LeObserver::currentMatchRulesIncludeTypes checking %s type %d(%s) hasAppleType:%d"
+ "LeObserver::updateScanState System about to go to sleep, but in the middle of reconfig"
+ "LeObserver::updateScanState System about to go to sleep, but we have rules that need to be removed"
+ "LeObserver::updateScanState System about to go to sleep, will try again later"
+ "OI_HCIIfc_DataReceived asserting wake force for %s"
+ "OI_HCIIfc_SetDataReceivedAssertionRequired %c"
+ "OI_HCI_ACL_DATA_PACKET"
+ "OI_HCI_ACL_DATA_WITH_TS_PACKET"
+ "OI_HCI_COMMAND_PACKET"
+ "OI_HCI_EVENT_PACKET"
+ "OI_HCI_SCO_DATA_PACKET"
+ "OI_HCI_SCO_HDR_DATA_PACKET"
+ "OI_HCI_UNKNOWN_TYPE"
+ "Overriding requiresWillSleepWorkaround=%c"
+ "Scan state change:  %{public}s(%d) --> %{public}s(%d)"
+ "SystemSettings::advStateStable:%c"
+ "SystemSettings::scanStateStable:%c"
+ "WillSleep"
+ "com.apple.BTStack.AbortSleep.%s"
+ "com.apple.BTStack.SleepAbort.IOPMAssertion"
+ "kIOMessageCanSystemSleep"
+ "kIOMessageSystemHasPoweredOn"
+ "kIOMessageSystemWillSleep"
+ "powerManagementEventSystemSleep msgType:%x(%s)"
+ "powerManagementMessage %s fPendingSleepAck:%c fPendingSleepAllow:%c fPendingSleepAckMessageArgument:%p"
+ "requiresWillSleepWorkaround"
+ "requiresWillSleepWorkaround %c chipset %d"
+ "respondToSleepIfPossible canRespond:%d fLeScanStateStable:%d fLeAdvStateStable:%d canDefer:%c"
+ "respondToSleepIfPossible cannot respond allow:%c Sleep:%fsec LeAdvStable:%c LeScanStable:%c canDefer:%c"
+ "respondToSleepIfPossible responding allow:%c willSleep:%fsec canDefer:%c"
+ "updateAdvertisement not doing anything dataChanged:%c validSessions:%c state:%d(%s)"
- "20:46:56"
- "Dec  9 2024"
- "powerManagementMessage %x"
- "updateAdvertisement not doing anything"

```
