## tvremoted

> `/usr/libexec/tvremoted`

```diff

-548.0.10.0.0
-  __TEXT.__text: 0xf8d8
+548.0.15.0.0
+  __TEXT.__text: 0xfd3c
   __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_stubs: 0x2420
-  __TEXT.__objc_methlist: 0xee0
+  __TEXT.__objc_stubs: 0x2480
+  __TEXT.__objc_methlist: 0xef0
   __TEXT.__const: 0xd2
-  __TEXT.__oslogstring: 0x21a7
+  __TEXT.__oslogstring: 0x2416
   __TEXT.__cstring: 0x81b
   __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__objc_methname: 0x3179
+  __TEXT.__objc_methname: 0x31cc
   __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methtype: 0xe5d
-  __TEXT.__unwind_info: 0x328
+  __TEXT.__objc_methtype: 0xe81
+  __TEXT.__unwind_info: 0x338
   __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x638

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0xe78
-  __DATA.__objc_selrefs: 0xc50
+  __DATA.__objc_selrefs: 0xc60
   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x360

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 9A09AFD6-50A6-3ACE-AF62-27A8C894B6D7
-  Functions: 306
-  Symbols:   2321
-  CStrings:  921
+  UUID: 48AD3F38-BA31-30DE-A2FE-94FDD9D578CA
+  Functions: 311
+  Symbols:   2349
+  CStrings:  932
 
Symbols:
+ -[TVRDClientProcessConnection updateDeviceIdentifier:to:]
+ -[TVRDServer _updateClientConnectionsForDevice:oldIdentifier:]
+ -[TVRDServer device:didUpdateNameFrom:]
+ -[TVRDServer device:didUpdateNameFrom:].cold.1
+ GCC_except_table92
+ _OUTLINED_FUNCTION_4
+ __76-[TVRDServer clientConnection:requestsSendingTouchEvent:toDeviceIdentifier:]_block_invoke.cold.1
+ __77-[TVRDServer clientConnection:requestsSendingButtonEvent:toDeviceIdentifier:]_block_invoke.cold.1
+ _objc_msgSend$_updateClientConnectionsForDevice:oldIdentifier:
+ _objc_msgSend$deviceBeganConnecting:
+ _objc_msgSend$updateDeviceIdentifier:to:
- -[TVRDServer deviceNameChanged:]
- -[TVRDServer deviceNameChanged:].cold.1
- GCC_except_table91
CStrings:
+ "BeganTextEditing - broadcasting to %{public}@, that device updated keyboard state: %{public}@"
+ "Cached devices: %@ _deviceIdentifiers: %@"
+ "Device %{public}@ is connecting, informing clients again..."
+ "DidUpdateAttributes - broadcasting to %{public}@, that device updated keyboard state: %{public}@"
+ "DidUpdateText - broadcasting to %{public}@, that device updated keyboard state: %{public}@"
+ "EndedTextEditing - broadcasting to %{public}@, that device updated keyboard state: %{public}@"
+ "No cached device found with identifier: %{public}@. All cached devices - %{public}@"
+ "No interested clients for device: %{public}@ connection identifiers: %{public}@"
+ "Updating all client connections' deviceIdentifiers from: %{public}@ to %{public}@"
+ "[TVRDServer] lost interest in %{public}@"
+ "_updateClientConnectionsForDevice:oldIdentifier:"
+ "device:didUpdateNameFrom:"
+ "updateDeviceIdentifier:to:"
+ "v32@0:8@\"TVRXDevice\"16@\"NSString\"24"
- "Broadcasting to %{public}@, that device updated keyboard state: %{public}@"
- "No cached device found with identifier %@. All cached devices - %@"
- "deviceNameChanged:"

```
