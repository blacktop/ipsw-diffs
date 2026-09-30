## companiond

> `/usr/libexec/companiond`

```diff

-  __TEXT.__text: 0x894b4
-  __TEXT.__auth_stubs: 0x2d60
-  __TEXT.__objc_stubs: 0x4260
-  __TEXT.__objc_methlist: 0x2ba8
-  __TEXT.__objc_methname: 0x60b5
-  __TEXT.__swift5_typeref: 0xc86
-  __TEXT.__swift5_fieldmd: 0x86c
-  __TEXT.__objc_classname: 0xb67
-  __TEXT.__objc_methtype: 0x15b7
-  __TEXT.__const: 0x20b6
-  __TEXT.__constg_swiftt: 0x8b8
-  __TEXT.__swift5_reflstr: 0x894
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__cstring: 0x2625
-  __TEXT.__swift5_capture: 0x784
+  __TEXT.__text: 0x8bffc
+  __TEXT.__auth_stubs: 0x2d80
+  __TEXT.__objc_stubs: 0x43a0
+  __TEXT.__objc_methlist: 0x2b60
+  __TEXT.__objc_methname: 0x6115
+  __TEXT.__swift5_typeref: 0xc9f
+  __TEXT.__swift5_fieldmd: 0x820
+  __TEXT.__objc_classname: 0xb48
+  __TEXT.__objc_methtype: 0x1588
+  __TEXT.__const: 0x2096
+  __TEXT.__constg_swiftt: 0x7ec
+  __TEXT.__swift5_reflstr: 0x832
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__cstring: 0x2669
+  __TEXT.__swift5_capture: 0x754
   __TEXT.__swift5_assocty: 0x150
   __TEXT.__swift5_proto: 0x118
-  __TEXT.__swift5_types: 0x8c
-  __TEXT.__swift_as_entry: 0x1a8
-  __TEXT.__swift_as_ret: 0x1c0
-  __TEXT.__swift_as_cont: 0x390
-  __TEXT.__oslogstring: 0x404b
+  __TEXT.__swift5_types: 0x84
+  __TEXT.__swift_as_entry: 0x1b0
+  __TEXT.__swift_as_ret: 0x1d0
+  __TEXT.__swift_as_cont: 0x3a8
+  __TEXT.__oslogstring: 0x417e
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x1a84
+  __TEXT.__gcc_except_tab: 0x1ab0
   __TEXT.__ustring: 0x40
-  __TEXT.__unwind_info: 0x2520
-  __TEXT.__eh_frame: 0x4cb0
-  __DATA_CONST.__const: 0x25d0
+  __TEXT.__unwind_info: 0x2558
+  __TEXT.__eh_frame: 0x4ed0
+  __DATA_CONST.__const: 0x2560
   __DATA_CONST.__cfstring: 0x1ba0
-  __DATA_CONST.__objc_classlist: 0x248
+  __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x16c0
-  __DATA_CONST.__got: 0xd10
-  __DATA_CONST.__auth_ptr: 0x560
-  __DATA.__objc_const: 0x7640
-  __DATA.__objc_selrefs: 0x14f0
-  __DATA.__objc_ivar: 0x40c
-  __DATA.__objc_data: 0x1a30
-  __DATA.__data: 0x1e70
+  __DATA_CONST.__auth_got: 0x16d0
+  __DATA_CONST.__got: 0xd08
+  __DATA_CONST.__auth_ptr: 0x558
+  __DATA.__objc_const: 0x7548
+  __DATA.__objc_selrefs: 0x1530
+  __DATA.__objc_ivar: 0x410
+  __DATA.__objc_data: 0x18e0
+  __DATA.__data: 0x1e20
   __DATA.__bss: 0x2380
   __DATA.__common: 0xe8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   - @rpath/AppleConnectClient.framework/AppleConnectClient
-  Functions: 2312
-  Symbols:   1273
-  CStrings:  2232
+  Functions: 2295
+  Symbols:   1274
+  CStrings:  2242
 
Sections:
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_doubleobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
Symbols:
+ _$s17CompanionServices32CPSRequesterUseCaseConfigurationV18requiresSharedHomeSbvg
+ _$s17CompanionServices32CPSRequesterUseCaseConfigurationV19requiresSameAccountSbvg
+ _$s17CompanionServices32CPSRequesterUseCaseConfigurationV6TargetO9accountIDSSSgvg
+ _$s17CompanionServices32CPSRequesterUseCaseConfigurationV7targetsSayAC6TargetOGSgvs
- _$sSo17OS_dispatch_queueC8DispatchE4mainABvgZ
- _OBJC_CLASS_$_OS_dispatch_queue
- _swift_bridgeObjectRetain_n
CStrings:
+ "@\"CBDiscovery\""
+ "Bluetooth scanner older setup device lost: %@"
+ "Bluetooth scanner setup device found: %@"
+ "Bluetooth scanner setup device lost. Invalidating."
+ "Bluetooth scanner start failed: %@"
+ "No account store"
+ "No primary account"
+ "No setup ID in advertisement. Not starting Bluetooth scanner."
+ "Starting Bluetooth scanner. setupID=0x%04x"
+ "[%s] bluetooth scanner device found: ignored, not sharedHome, %@"
+ "_bluetoothScannerFoundDevice:"
+ "_bluetoothScannerLostDevice:"
+ "_setupID"
+ "_setupIDForDevice:"
+ "_startBluetoothScanner"
+ "_stopBluetoothScanner"
+ "aa_primaryAppleAccountWithCompletion:"
+ "addDiscoveryType:"
+ "discoveredDevices"
+ "nearbyActionExtraData"
+ "numberWithUnsignedShort:"
+ "setUseCase:"
+ "unsignedShortValue"
+ "v24@?0@\"ACAccount\"8@\"NSError\"16"
- "@\"OS_dispatch_queue\""
- "@\"_TtC10companiond11CDCSKClient\""
- "@28@0:8@16i24"
- "Setup not needed handler called. Invalidating."
- "T@\"OS_dispatch_queue\",N,&,VdispatchQueue"
- "T@?,N,C"
- "_TtC10companiond11CDCSKClient"
- "_cskClient"
- "_startCSKClient"
- "bluetoothDevice"
- "companiond.CDCSKClient"
- "initWithBluetoothDevice:discoveryType:"
- "invalidateDone"
- "setSetupNotNeededHandler:"
- "setupNotNeededHandler"

```
