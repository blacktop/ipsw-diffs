## nanoregistryd

> `/usr/libexec/nanoregistryd`

```diff

-989.19.0.0.0
-  __TEXT.__text: 0xfd530
+989.20.0.0.0
+  __TEXT.__text: 0xfd788
   __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_stubs: 0x10ce0
-  __TEXT.__objc_methlist: 0xd6e4
+  __TEXT.__objc_stubs: 0x10d00
+  __TEXT.__objc_methlist: 0xd704
   __TEXT.__const: 0x678
   __TEXT.__gcc_except_tab: 0x2638
-  __TEXT.__objc_methname: 0x1bcaf
-  __TEXT.__cstring: 0xd71b
-  __TEXT.__oslogstring: 0x149ba
+  __TEXT.__objc_methname: 0x1bd23
+  __TEXT.__cstring: 0xd79c
+  __TEXT.__oslogstring: 0x14a14
   __TEXT.__objc_classname: 0x21a5
   __TEXT.__objc_methtype: 0x492e
   __TEXT.__dlopen_cstrs: 0xef
   __TEXT.__ustring: 0x4ac
-  __TEXT.__unwind_info: 0x39e8
+  __TEXT.__unwind_info: 0x39e0
   __DATA_CONST.__auth_got: 0x860
   __DATA_CONST.__got: 0xc78
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__objc_arraydata: 0x470
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x19810
-  __DATA.__objc_selrefs: 0x5d20
-  __DATA.__objc_ivar: 0x1170
+  __DATA.__objc_const: 0x19840
+  __DATA.__objc_selrefs: 0x5d30
+  __DATA.__objc_ivar: 0x1174
   __DATA.__objc_data: 0x4c90
   __DATA.__data: 0x19d8
   __DATA.__bss: 0x4a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 5692
+  Functions: 5694
   Symbols:   689
-  CStrings:  8589
+  CStrings:  8597
 
CStrings:
+ "%s Calling cancelDiscovery on %@"
+ "%s _pairingInProgress = %{BOOL}d"
+ "%s bluetooth identifier: %@, isAltAccount: %{BOOL}d"
+ "-[NetworkRelayAgent abortCurrentPairing]_block_invoke"
+ "-[NetworkRelayAgent migrationPairWithCandidateWithBluetoothIdentifier:isAltAccountPairing:completion:]"
+ "-[NetworkRelayAgent stopScanningForMigrationCandidates]"
+ "23"
+ "NanoRegistry-989.20"
+ "TB,R,N,V_isAltAccountPairing"
+ "_isAltAccountPairing"
+ "isAltAccountPairing"
+ "migrationPairWithCandidateWithBluetoothIdentifier:isAltAccountPairing:completion:"
+ "stopNetworkRelayWatchScan"
- "%s bluetooth identifier: %@"
- "-[NetworkRelayAgent migrationPairWithCandidateWithBluetoothIdentifier:completion:]"
- "137"
- "NanoRegistry-989.19"
- "migrationPairWithCandidateWithBluetoothIdentifier:completion:"

```
