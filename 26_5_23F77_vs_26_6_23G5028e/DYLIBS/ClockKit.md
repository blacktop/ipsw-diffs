## ClockKit

> `/System/Library/Frameworks/ClockKit.framework/ClockKit`

```diff

-2483.340.80.1.0
-  __TEXT.__text: 0x6ca20
+2483.340.84.0.0
+  __TEXT.__text: 0x6d3d0
   __TEXT.__auth_stubs: 0xc40
-  __TEXT.__objc_methlist: 0x94f4
-  __TEXT.__const: 0xb48
+  __TEXT.__objc_methlist: 0x958c
+  __TEXT.__const: 0xb78
   __TEXT.__cstring: 0x3f03
-  __TEXT.__oslogstring: 0x27de
-  __TEXT.__gcc_except_tab: 0x103c
+  __TEXT.__oslogstring: 0x2abe
+  __TEXT.__gcc_except_tab: 0x105c
   __TEXT.__dlopen_cstrs: 0x349
   __TEXT.__ustring: 0x80
   __TEXT.__constg_swiftt: 0xd0

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x2610
-  __TEXT.__objc_classname: 0x1e35
-  __TEXT.__objc_methname: 0xf7da
-  __TEXT.__objc_methtype: 0x1d79
-  __TEXT.__objc_stubs: 0x9260
+  __TEXT.__unwind_info: 0x2620
+  __TEXT.__objc_classname: 0x1e49
+  __TEXT.__objc_methname: 0xf8d4
+  __TEXT.__objc_methtype: 0x1e33
+  __TEXT.__objc_stubs: 0x92a0
   __DATA_CONST.__got: 0x700
   __DATA_CONST.__const: 0x1c98
   __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x80
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34b8
+  __DATA_CONST.__objc_selrefs: 0x3518
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x4a0
   __DATA_CONST.__objc_arraydata: 0x588
   __AUTH_CONST.__auth_got: 0x630
   __AUTH_CONST.__const: 0xfe8
   __AUTH_CONST.__cfstring: 0x53e0
-  __AUTH_CONST.__objc_const: 0xf818
+  __AUTH_CONST.__objc_const: 0xf8d8
   __AUTH_CONST.__objc_intobj: 0xc78
   __AUTH_CONST.__objc_doubleobj: 0x370
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x3660
   __DATA.__objc_ivar: 0xadc
-  __DATA.__data: 0x678
+  __DATA.__data: 0x6d8
   __DATA.__bss: 0xba0
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1532BE24-317B-321E-BC11-80DF52814747
-  Functions: 3843
-  Symbols:   12110
-  CStrings:  4535
+  UUID: 13D735FA-3B41-3F18-9E92-D8FDAFEB9EA8
+  Functions: 3846
+  Symbols:   12124
+  CStrings:  4564
 
Symbols:
+ -[CLKDevice _updatePDRDevice:]
+ -[CLKDevice registry:changed:properties:]
+ GCC_except_table13
+ GCC_except_table145
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PDRRegistryDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PDRRegistryDelegate
+ __OBJC_$_PROTOCOL_REFS_PDRRegistryDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CLKDevice
+ __OBJC_LABEL_PROTOCOL_$_PDRRegistryDelegate
+ __OBJC_PROTOCOL_$_PDRRegistryDelegate
+ ___41-[CLKDevice registry:changed:properties:]_block_invoke
+ ___block_literal_global.360
+ ___block_literal_global.45
+ ___block_literal_global.749
+ ___block_literal_global.792
+ ___block_literal_global.795
+ _objc_msgSend$_updatePDRDevice:
+ _objc_msgSend$addDelegate:
- GCC_except_table142
- GCC_except_table28
- ___block_literal_global.359
- ___block_literal_global.44
- ___block_literal_global.53
- ___block_literal_global.693
- ___block_literal_global.736
- ___block_literal_global.739
CStrings:
+ "PDR capability change fired for CLKDevice %p, pairingID=%@, current pdrDevice=%p"
+ "PDR capability change: _updatePDRDevice returned changed=%d, new pdrDevice=%p"
+ "PDR capability change: fetched fresh PDRDevice=%p"
+ "PDR delegate callback: CLKDevice=%p selfPairingID=%@ devicePairingID=%@ properties=%@"
+ "PDR delegate callback: _updatePDRDevice returned changed=%d, new pdrDevice=%p"
+ "PDR delegate callback: capabilities changed, sending CLKActiveDeviceChangedNotification"
+ "PDR delegate callback: processing on main, CLKDevice=%p currentPdrDevice=%p newPdrDevice=%p"
+ "PDR delegate callback: skipping, pairingID mismatch"
+ "PDRRegistryDelegate"
+ "Registered CLKDevice %p as PDRRegistryDelegate, pairingID=%@"
+ "Skipping +[PDRDarwinNotifications pairedDeviceDidChangeCapabilities] refresh CLKDevice: %@"
+ "_supportsCapabilityUncached: cap=0x%08x, pdrDevice=%p, result=%d"
+ "_updatePDRDevice:"
+ "addDelegate:"
+ "registry:added:"
+ "registry:changed:properties:"
+ "registry:compatibilityStateChanged:"
+ "registry:didActivate:"
+ "registry:didDeactivate:"
+ "registry:didPair:"
+ "registry:didSetup:"
+ "registry:didUnpair:"
+ "registry:removed:"
+ "registryChanged:"
+ "v24@0:8@\"PDRRegistry\"16"
+ "v32@0:8@\"PDRRegistry\"16@\"NSUUID\"24"
+ "v32@0:8@\"PDRRegistry\"16@\"PDRDevice\"24"
+ "v32@0:8@\"PDRRegistry\"16q24"
+ "v32@0:8@16q24"
+ "v40@0:8@\"PDRRegistry\"16@\"PDRDevice\"24@\"NSSet\"32"
- "Got +[PDRDarwinNotifications pairedDeviceDidChangeCapabilities] refresh CLKDevice: %@"

```
