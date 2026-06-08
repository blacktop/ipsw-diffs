## nanoappregistryd

> `/System/Library/PrivateFrameworks/NanoAppRegistry.framework/Support/nanoappregistryd`

```diff

-71.0.4.0.0
-  __TEXT.__text: 0xbba4
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x21e0
+71.0.5.0.0
+  __TEXT.__text: 0xb3a8
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__objc_stubs: 0x2200
   __TEXT.__objc_methlist: 0x12a0
-  __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__cstring: 0x5db
-  __TEXT.__objc_methname: 0x2a0e
-  __TEXT.__oslogstring: 0x93b
-  __TEXT.__objc_classname: 0x23e
+  __TEXT.__const: 0x40
+  __TEXT.__gcc_except_tab: 0x54
+  __TEXT.__cstring: 0x5d7
+  __TEXT.__oslogstring: 0x986
+  __TEXT.__objc_methname: 0x2a0b
+  __TEXT.__objc_classname: 0x224
   __TEXT.__objc_methtype: 0xbc0
-  __TEXT.__unwind_info: 0x410
-  __DATA_CONST.__auth_got: 0x2f8
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x2a0
+  __TEXT.__unwind_info: 0x370
+  __DATA_CONST.__const: 0x278
   __DATA_CONST.__cfstring: 0x560
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__auth_got: 0x320
+  __DATA_CONST.__got: 0x140
   __DATA.__objc_const: 0x34e8
-  __DATA.__objc_selrefs: 0xbd8
+  __DATA.__objc_selrefs: 0xbe0
   __DATA.__objc_ivar: 0xec
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x540

   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/NanoAppRegistry.framework/NanoAppRegistry
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/PairedSync.framework/PairedSync
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C715AD77-64FC-3D59-B304-30BB62D6AE0A
-  Functions: 343
-  Symbols:   144
-  CStrings:  786
+  UUID: 1446373D-CB00-3D33-9578-96E99B3083C5
+  Functions: 339
+  Symbols:   149
+  CStrings:  787
 
Symbols:
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_PDRDarwinNotifications
+ _OBJC_CLASS_$_PDRRegistry
+ __os_log_fault_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x8
- _NRPairedDeviceRegistryDeviceDidPairDarwinNotification
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x27
CStrings:
+ "No pairingStorePath for paired device %{public}@ with pairingID %{public}@"
+ "deviceDidPair"
+ "getActivePairedDevice"
+ "pairingStorePath"
- "stringWithUTF8String:"
- "v24@?0@\"NSString\"8@\"NSUUID\"16"
- "waitForPairingStorePathPairingID:"

```
