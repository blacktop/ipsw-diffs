## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-548.0.15.0.0
-  __TEXT.__text: 0x63498
+548.0.17.0.0
+  __TEXT.__text: 0x63654
   __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x85d4
+  __TEXT.__objc_methlist: 0x85dc
   __TEXT.__const: 0x230
   __TEXT.__gcc_except_tab: 0xd9c
   __TEXT.__cstring: 0x509e
-  __TEXT.__oslogstring: 0x6f20
+  __TEXT.__oslogstring: 0x6f8f
   __TEXT.__unwind_info: 0x1720
   __TEXT.__objc_classname: 0xd3a
   __TEXT.__objc_methname: 0xf857
   __TEXT.__objc_methtype: 0x2a08
-  __TEXT.__objc_stubs: 0x99c0
+  __TEXT.__objc_stubs: 0x99e0
   __DATA_CONST.__got: 0x570
   __DATA_CONST.__const: 0x1800
   __DATA_CONST.__objc_classlist: 0x380

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F7DB17DD-CE3E-326C-88AB-6D31D8623475
-  Functions: 2801
-  Symbols:   9080
-  CStrings:  5661
+  UUID: 2EA4A7A3-C504-3B24-8564-2A1089C7F918
+  Functions: 2802
+  Symbols:   9083
+  CStrings:  5665
 
Symbols:
+ -[TVRCXPCClient reset]
+ GCC_except_table18
+ GCC_except_table49
+ _objc_msgSend$deviceUpdatedState:
- GCC_except_table17
- GCC_except_table48
Functions:
~ -[TVRCDevice _deviceUpdatedState:] : 3480 -> 3492
~ -[TVRCXPCClient addEventObserver:forDeviceWithIdentifier:] : 176 -> 284
~ -[TVRCXPCClient removeEventObserver:forDeviceWithIdentifier:] : 120 -> 236
+ -[TVRCXPCClient reset]
~ -[TVRCXPCClient suggestedDevices:] : 148 -> 152
~ ___48-[TVRCXPCClient _broadcastStateUpdateToDevices:]_block_invoke : 516 -> 596
CStrings:
+ "%s - device:<%p> state: %{public}@ "
+ "Added observer: %@"
+ "Broadcasting to eventObservers: %@"
+ "Removed observer: %@"
+ "Resetting TVRCXPCClient"
- "%s - state: %{public}@ "

```
