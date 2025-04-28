## searchpartyd

> `/usr/libexec/searchpartyd`

```diff

-396.35.2.11.22
-  __TEXT.__text: 0x13783e0
+396.35.2.11.28
+  __TEXT.__text: 0x1374b40
   __TEXT.__auth_stubs: 0x7530
   __TEXT.__objc_stubs: 0x40
-  __TEXT.__objc_methlist: 0x3e54
+  __TEXT.__objc_methlist: 0x3e3c
   __TEXT.__const: 0x727b0
-  __TEXT.__oslogstring: 0x44add
+  __TEXT.__oslogstring: 0x4486d
   __TEXT.__objc_classname: 0x626
-  __TEXT.__objc_methname: 0xeb9e
+  __TEXT.__objc_methname: 0xeb81
   __TEXT.__objc_methtype: 0x4b83
-  __TEXT.__cstring: 0x3b72d
+  __TEXT.__cstring: 0x3b70d
   __TEXT.__swift5_typeref: 0x22416
   __TEXT.__swift5_fieldmd: 0x211e0
-  __TEXT.__constg_swiftt: 0x1e2ac
+  __TEXT.__constg_swiftt: 0x1e29c
   __TEXT.__swift5_builtin: 0x924
   __TEXT.__swift5_reflstr: 0x1eddf
   __TEXT.__swift5_assocty: 0x2770
   __TEXT.__swift5_protos: 0x2dc
   __TEXT.__swift5_proto: 0x57a8
   __TEXT.__swift5_types: 0x1ca0
-  __TEXT.__swift_as_entry: 0x2458
-  __TEXT.__swift5_capture: 0x1b33c
-  __TEXT.__swift_as_ret: 0x48f4
+  __TEXT.__swift_as_entry: 0x2454
+  __TEXT.__swift5_capture: 0x1b310
+  __TEXT.__swift_as_ret: 0x48e8
   __TEXT.__swift5_mpenum: 0x68c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x39680
-  __TEXT.__eh_frame: 0xab040
+  __TEXT.__unwind_info: 0x39648
+  __TEXT.__eh_frame: 0xaaf48
   __DATA_CONST.__auth_got: 0x3aa0
   __DATA_CONST.__got: 0x3078
-  __DATA_CONST.__auth_ptr: 0x4838
-  __DATA_CONST.__const: 0x73d40
+  __DATA_CONST.__auth_ptr: 0x5098
+  __DATA_CONST.__const: 0x73cb0
   __DATA_CONST.__objc_classlist: 0x7c0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x388

   __DATA_CONST.__objc_protorefs: 0x1d0
   __DATA_CONST.__linkguard: 0x15
   __DATA.__objc_const: 0x19410
-  __DATA.__objc_selrefs: 0x3478
+  __DATA.__objc_selrefs: 0x3470
   __DATA.__objc_data: 0x3b20
-  __DATA.__data: 0x3f828
+  __DATA.__data: 0x3f838
   __DATA.__bss: 0xa79d0
   __DATA.__common: 0x2628
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 57944
+  Functions: 57924
   Symbols:   3901
-  CStrings:  12971
+  CStrings:  12961
 
CStrings:
+ "Untracked peripheral canSendDataTo!: <CBPeripheral>"
+ "Untracked peripheral didConnect!: <CBPeripheral>"
+ "Untracked peripheral didDisconnectPeripheral!: <CBPeripheral>"
+ "Untracked peripheral didFailToConnect!: <CBPeripheral>"
+ "Untracked peripheral didReceive!: <CBPeripheral>"
+ "Untracked peripheral didSendBytes!: <CBPeripheral>"
+ "[%@] Removing <CBPeripheral> from cache"
+ "[%@] Removing <CBPeripheral> from peripheralCache"
+ "[%@] centralManager didConnect: <CBPeripheral>"
+ "[%@] centralManager didDisconnectPeripheral: <CBPeripheral>"
+ "[%@] centralManager didDiscover: <CBPeripheral> %s"
+ "centralManager canSendDataTo <CBPeripheral>"
+ "centralManager connectionEventDidOccur: %ld for peripheral: <CBPeripheral>"
+ "centralManager didFailToConnect: <CBPeripheral>"
+ "centralManager didReceive %s from <CBPeripheral>"
+ "centralManager didSendBytes %@ to <CBPeripheral> with error"
+ "centralManager didUpdateFindMyPeripherals: <CBPeripheral>"
- "            #Durian: TagCommandManager: didFetch batteryStatus error: %{public}@ for device: %{private,mask.hash}s."
- "            Unable to init BatteryLevel from CLFindMyAccessoryBatteryStatus %lu for beacon %{private,mask.hash}s."
- "        #Durian: TagCommandManager: didFetch batteryStatus: [%lu] for device: %{private,mask.hash}s."
- "#Durian: TagCommandManager: fetch battery state for: %{private,mask.hash}s."
- "#Durian: TagCommandManager: skip fetch battery state for beacon: %{private,mask.hash}s - already fetching."
- "#Durian: TagCommandManager: skip fetch battery state for beacon: %{private,mask.hash}s of unsupported type %{public}s."
- "#Durian: TagCommandManager: skip fetch battery state for non-owned device: %{private,mask.hash}s."
- "#Durian: TagCommandManager: skip fetch battery state for: %{private,mask.hash}s."
- "Error from didFetchBattery: %{public}@."
- "Untracked peripheral canSendDataTo!: %@"
- "Untracked peripheral didConnect!: %@"
- "Untracked peripheral didDisconnectPeripheral!: %@"
- "Untracked peripheral didFailToConnect!: %@"
- "Untracked peripheral didReceive!: %@"
- "Untracked peripheral didSendBytes!: %@"
- "[%@] Removing %@ from cache"
- "[%@] Removing %@ from peripheralCache"
- "[%@] centralManager didDiscover: %@ %s"
- "centralManager canSendDataTo %@"
- "centralManager connectionEventDidOccur: %ld for peripheral: %@"
- "centralManager didFailToConnect: %@"
- "centralManager didReceive %s from %@"
- "centralManager didSendBytes %@ to %@ with error"
- "centralManager didUpdateFindMyPeripherals: %s"
- "didFetchBattery"
- "fetchBatteryStatusForDevice:"

```
