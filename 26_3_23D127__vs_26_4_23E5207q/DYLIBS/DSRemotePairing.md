## DSRemotePairing

> `/System/Library/PrivateFrameworks/DSRemotePairing.framework/DSRemotePairing`

```diff

-595.0.2.0.0
-  __TEXT.__text: 0x2a3c
-  __TEXT.__auth_stubs: 0x5d0
+618.0.0.0.0
+  __TEXT.__text: 0x2af8
+  __TEXT.__auth_stubs: 0x590
   __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0xba
   __TEXT.__gcc_except_tab: 0x168
-  __TEXT.__cstring: 0x1a8
+  __TEXT.__cstring: 0x150
   __TEXT.__swift5_typeref: 0x62
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x110
-  __TEXT.__objc_classname: 0x43
+  __TEXT.__unwind_info: 0x120
+  __TEXT.__objc_classname: 0x75
   __TEXT.__objc_methname: 0x638
-  __TEXT.__objc_methtype: 0xe5
-  __TEXT.__objc_stubs: 0x4e0
+  __TEXT.__objc_methtype: 0xf8
+  __TEXT.__objc_stubs: 0x540
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x188
-  __AUTH_CONST.__auth_got: 0x2f8
+  __AUTH_CONST.__auth_got: 0x2d8
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x438

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7819F43A-266F-32B6-811F-B105BF688819
+  UUID: 03C5DB1B-E790-3435-BFEC-17A21473EF6D
   Functions: 71
   Symbols:   285
-  CStrings:  112
+  CStrings:  110
 
Symbols:
+ _objc_msgSend$init
+ _objc_msgSend$setModel:
+ _objc_msgSend$setRemotePairingFrameworkIdentifier:
+ _objc_retain_x22
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x4
Functions:
~ -[DSPairedComputer isEqual:] : 240 -> 252
~ -[DSRemotePairingWrapper removeAllPairedDevices] : 76 -> 84
~ -[DSRemotePairingWrapper removeSelectedDevices:onQueue:withCompletion:] : 144 -> 140
~ -[DSRemotePairingWrapper setRemotePairing:] : 12 -> 64
~ -[DSRemotePairingStore fetchPairedDevicesOnQueue:completion:] : 216 -> 208
~ ___61-[DSRemotePairingStore fetchPairedDevicesOnQueue:completion:]_block_invoke : 1972 -> 2096
~ ___61-[DSRemotePairingStore fetchPairedDevicesOnQueue:completion:]_block_invoke.2 : 96 -> 112
~ ___61-[DSRemotePairingStore fetchPairedDevicesOnQueue:completion:]_block_invoke_2 : 144 -> 156
~ ___61-[DSRemotePairingStore fetchPairedDevicesOnQueue:completion:]_block_invoke_3 : 112 -> 120
~ -[DSRemotePairingStore setRemotePairingSwift:] : 12 -> 64
~ -[DSRemotePairingStore setWorkQueue:] : 12 -> 64
~ sub_234c721e0 -> sub_238991324 : 1928 -> 1864
~ sub_234c729bc -> sub_238991ac0 : 104 -> 96
~ sub_234c72d04 -> sub_238991e00 : 52 -> 44
~ sub_234c72de8 -> sub_238991edc : 1932 -> 1876
~ sub_234c73574 -> sub_238992630 : 1460 -> 1456
~ _block_copy_helper : 16 -> 20

```
