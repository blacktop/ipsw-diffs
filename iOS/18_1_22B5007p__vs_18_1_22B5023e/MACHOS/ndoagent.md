## ndoagent

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent`

```diff

-423.0.0.0.0
-  __TEXT.__text: 0x10c20
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_stubs: 0x2220
-  __TEXT.__objc_methlist: 0xa00
-  __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x13c7
-  __TEXT.__oslogstring: 0x1e63
-  __TEXT.__objc_classname: 0x204
-  __TEXT.__objc_methname: 0x2497
-  __TEXT.__objc_methtype: 0x7d5
+425.2.0.0.0
+  __TEXT.__text: 0x10d90
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_stubs: 0x22a0
+  __TEXT.__objc_methlist: 0xa28
+  __TEXT.__const: 0xe8
+  __TEXT.__cstring: 0x140b
+  __TEXT.__oslogstring: 0x1e14
+  __TEXT.__objc_classname: 0x218
+  __TEXT.__objc_methname: 0x2520
+  __TEXT.__objc_methtype: 0x7fe
   __TEXT.__gcc_except_tab: 0x3fc
-  __TEXT.__unwind_info: 0x410
-  __DATA_CONST.__auth_got: 0x2c0
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x910
-  __DATA_CONST.__cfstring: 0x940
-  __DATA_CONST.__objc_classlist: 0x90
+  __TEXT.__unwind_info: 0x418
+  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__const: 0x8e8
+  __DATA_CONST.__cfstring: 0x9e0
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x4638
-  __DATA.__objc_selrefs: 0x980
-  __DATA.__objc_ivar: 0x6c
-  __DATA.__objc_data: 0x5a0
+  __DATA.__objc_const: 0x4738
+  __DATA.__objc_selrefs: 0x9a0
+  __DATA.__objc_ivar: 0x74
+  __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x240
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 318
-  Symbols:   155
-  CStrings:  787
+  Functions: 316
+  Symbols:   157
+  CStrings:  800
 
Symbols:
+ _NRDevicePropertyIsActive
+ _NRPairedDeviceRegistryDeviceDidUnpairDarwinNotification
+ _OBJC_CLASS_$_NDOTypeChecking
- _objc_alloc_init
CStrings:
+ "\x02"
+ "%!s(MISSING): mapping watch serial:%!@(MISSING) to:%!@(MISSING)"
+ "-[NDOPairedDevicesMonitor updatePairedWatchesFollowUp]"
+ "@\"<NDONanoRegistry>\""
+ "B16@?0@\"<NDONanoDevice>\"8"
+ "DBG-ADD:%!@(MISSING)"
+ "DBG-MAP:%!@(MISSING)"
+ "NDODeviceProvider"
+ "PairedWatchesSerialNumbersMap"
+ "Ti,V_unpairNotifyToken"
+ "_nanoRegistry"
+ "_unpairNotifyToken"
+ "_updatePairedBTDevicesFollowUp"
+ "com.apple.nanoregistry.devicedidunpair"
+ "com.apple.nanoregistry.watchdidbecomeactive"
+ "entered stream for device pairing"
+ "initWithNanoRegistry:"
+ "isNotEmptyString:"
+ "setUnpairNotifyToken:"
+ "sharedProvider"
+ "unpairNotifyToken"
+ "updatePairedWatchesFollowUp"
+ "v24@0:8@\"NSArray\"16"
- "%!s(MISSING) -> internal overriden pairedWatches: %!@(MISSING)"
- "%!s(MISSING) -> pairedDevices pairedWatchesSerialNumbers overrideDict: %!@(MISSING)"
- "-[NDODevicesManager pairedWatches]_block_invoke"
- "-[NDOPairedDevicesMonitor updatePariedWatchesFollowUp]"
- "B16@?0@\"NRDevice\"8"
- "_updatePariedBTDevicesFollowUp"
- "entered stream for watch device pairing"
- "sharedManager"
- "updatePariedWatchesFollowUp"
- "v32@?0@\"NRDevice\"8Q16^B24"

```
