## nanoregistryd

> `/usr/libexec/nanoregistryd`

```diff

-989.17.1.0.0
-  __TEXT.__text: 0xfc950
+989.19.0.0.0
+  __TEXT.__text: 0xfd530
   __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_stubs: 0x10c80
-  __TEXT.__objc_methlist: 0xd6ac
+  __TEXT.__objc_stubs: 0x10ce0
+  __TEXT.__objc_methlist: 0xd6e4
   __TEXT.__const: 0x678
-  __TEXT.__gcc_except_tab: 0x25d0
-  __TEXT.__objc_methname: 0x1bbef
-  __TEXT.__cstring: 0xd6fb
-  __TEXT.__oslogstring: 0x14780
+  __TEXT.__gcc_except_tab: 0x2638
+  __TEXT.__objc_methname: 0x1bcaf
+  __TEXT.__cstring: 0xd71b
+  __TEXT.__oslogstring: 0x149ba
   __TEXT.__objc_classname: 0x21a5
-  __TEXT.__objc_methtype: 0x490b
+  __TEXT.__objc_methtype: 0x492e
   __TEXT.__dlopen_cstrs: 0xef
   __TEXT.__ustring: 0x4ac
-  __TEXT.__unwind_info: 0x39c0
+  __TEXT.__unwind_info: 0x39e8
   __DATA_CONST.__auth_got: 0x860
-  __DATA_CONST.__got: 0xc70
+  __DATA_CONST.__got: 0xc78
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4b20
-  __DATA_CONST.__cfstring: 0xbae0
+  __DATA_CONST.__const: 0x4b50
+  __DATA_CONST.__cfstring: 0xbb20
   __DATA_CONST.__objc_classlist: 0x7a8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220

   __DATA_CONST.__objc_arraydata: 0x470
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x19808
-  __DATA.__objc_selrefs: 0x5d08
+  __DATA.__objc_const: 0x19810
+  __DATA.__objc_selrefs: 0x5d20
   __DATA.__objc_ivar: 0x1170
   __DATA.__objc_data: 0x4c90
   __DATA.__data: 0x19d8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 5689
-  Symbols:   688
-  CStrings:  8575
+  Functions: 5692
+  Symbols:   689
+  CStrings:  8589
 
Symbols:
+ _NRDevicePairingErrorOriginalCBUUIDKey
CStrings:
+ "137"
+ "Candidate discovered: %@ (bluetooth UUID %@)"
+ "Candidate lost: %@ (bluetooth UUID %@)"
+ "Duplicate candidate discovered with different bluetooth UUID:- previous %@ (%@), new %@ (%@)"
+ "Duplicate candidate discovered with identical bluetooth UUID:- previous %@, new %@"
+ "NanoRegistry-989.19"
+ "NetworkRelayPair: Ghost device UUID %@ matches paired NR device %@"
+ "Previously paired Bluetooth identifiers: %{public}@"
+ "Recently lost candidate %@ is not equal to the one in identifier/candidate map %@"
+ "Recently lost candidate %@ is not in identifier/candidate map"
+ "Removing lost candidate %@ from identifier/candidate map"
+ "[Push-New] requestAuthMethodForDevice on %{public}@ completed with error = %{public}@"
+ "[Push] requestAuthMethodForDevice on %{public}@ completed with error = %{public}@"
+ "_notifyDelegatesOfPreviouslyPairedBluetoothIdentifiers:"
+ "authMethod"
+ "com.apple.nanoregistry.networkrelaypairing-report"
+ "duration"
+ "networkRelayPairFoundPreviouslyPairedBluetoothIdentifiers:"
+ "reportNetworkRelayPairingResultWithAuthMethod:resultError:timeElapsed:"
+ "unpairDevice:queue:withCompletion:"
+ "v24@0:8@\"NSSet\"16"
+ "v40@0:8Q16@24d32"
- "6"
- "Candidate discovered: %@"
- "Candidate lost: %@"
- "NRDevicePairingErrorOriginalNRUUIDKey"
- "NanoRegistry-989.17.1"
- "Requested authentication method completed with error = %{public}@"
- "[Push] requestAuthMethodForDevice completed with error = %{public}@"
- "unpairDevice:withCompletion:"

```
