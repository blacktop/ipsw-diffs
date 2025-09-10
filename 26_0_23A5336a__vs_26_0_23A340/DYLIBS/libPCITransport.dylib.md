## libPCITransport.dylib

> `/usr/lib/libPCITransport.dylib`

```diff

 1054.0.0.0.0
-  __TEXT.__text: 0x1c134
+  __TEXT.__text: 0x1c274
   __TEXT.__auth_stubs: 0xd90
-  __TEXT.__gcc_except_tab: 0x1dcc
+  __TEXT.__gcc_except_tab: 0x1ddc
   __TEXT.__const: 0xbe5
-  __TEXT.__cstring: 0x2385
-  __TEXT.__oslogstring: 0x1088
+  __TEXT.__cstring: 0x240e
+  __TEXT.__oslogstring: 0x10a9
   __TEXT.__unwind_info: 0xd38
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x8d0
+  __DATA_CONST.__const: 0x8e0
   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__const: 0xc68
   __AUTH_CONST.__cfstring: 0x260

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 731CA3CB-EA5D-38A7-AAE2-F121DCAB60C1
+  UUID: A6AA8F53-68E7-355C-BCBB-160A71988E0B
   Functions: 640
   Symbols:   1928
-  CStrings:  473
+  CStrings:  478
 
Symbols:
+ ____ZN3pci5event8Listener4initEv_block_invoke.23
+ ___block_descriptor_tmp.27
+ ___block_descriptor_tmp.31
+ ___block_descriptor_tmp.83
+ ___block_descriptor_tmp.90
+ ___block_descriptor_tmp.95
- ____ZN3pci5event8Listener4initEv_block_invoke.22
- ___block_descriptor_tmp.26
- ___block_descriptor_tmp.81
- ___block_descriptor_tmp.88
- ___block_descriptor_tmp.91
Functions:
~ ____ZN3pci9transport2th9readAsyncEv_block_invoke : 1084 -> 1216
~ ____ZN3pci9transport6kernel12probeVariantEv_block_invoke : 268 -> 276
~ __ZN3pci9transport6kernel13errorAsStringENSt3__14pairINS1_7variantEjEE : 44 -> 64
~ __ZN3pci9transport6kernel6createEv : 376 -> 380
~ __ZN3pci5event8Listener6notifyENSt3__14pairINS_9transport6kernel7variantEjEEPvS8_ : 1480 -> 1528
~ __ZN3pci5event23getPDPMessageTypeStringENSt3__14pairINS_9transport6kernel7variantEjEE : 136 -> 152
~ __ZN3pci5event11PDPListener5startEv : 484 -> 576
CStrings:
+ "%s: unsupported PCI variant: daleipc\n"
+ "AirshipDaleBasebandControl"
+ "pci error (unsupported variant: daleipc): "
+ "unsupported PCI variant: daleipc"
+ "unsupported variant: daleipc"

```
