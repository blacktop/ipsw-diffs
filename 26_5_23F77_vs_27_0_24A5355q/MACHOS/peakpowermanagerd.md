## peakpowermanagerd

> `/usr/libexec/peakpowermanagerd`

```diff

-1035.100.47.0.0
-  __TEXT.__text: 0x104b0
-  __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_stubs: 0x2140
-  __TEXT.__objc_methlist: 0x10ac
-  __TEXT.__objc_methname: 0x2a53
-  __TEXT.__cstring: 0x7fa
-  __TEXT.__objc_classname: 0x5c
+1177.0.0.502.4
+  __TEXT.__text: 0x10914
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_stubs: 0x2240
+  __TEXT.__objc_methlist: 0x10d4
+  __TEXT.__objc_methname: 0x2ac9
+  __TEXT.__cstring: 0x8a2
+  __TEXT.__objc_classname: 0x50
   __TEXT.__objc_methtype: 0x2e7
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__oslogstring: 0x9e0
-  __TEXT.__unwind_info: 0x360
-  __DATA_CONST.__auth_got: 0x348
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__oslogstring: 0xa83
+  __TEXT.__unwind_info: 0x2e0
   __DATA_CONST.__const: 0xd8
-  __DATA_CONST.__cfstring: 0xa80
+  __DATA_CONST.__cfstring: 0xaa0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__got: 0xa8
   __DATA.__objc_const: 0x13f0
-  __DATA.__objc_selrefs: 0xbb8
+  __DATA.__objc_selrefs: 0xbf8
   __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x60

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7CEBDA60-017A-3173-BE25-D95F280FAA81
-  Functions: 447
-  Symbols:   134
-  CStrings:  763
+  UUID: 13A88DD5-26EF-330E-B39E-2C712140972A
+  Functions: 458
+  Symbols:   140
+  CStrings:  779
 
Symbols:
+ _IOIteratorNext
+ _IOServiceGetMatchingServices
+ _OBJC_CLASS_$_NSMutableArray
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x23
+ _objc_release_x27
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x23
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x25
- _objc_retain_x26
CStrings:
+ "%s <Error> IOConnectCallStructMethod fail to call IOUserClient setBatteryParams,  ioReturnResult = 0x%08x"
+ "%s <Error> IOServiceGetMatchingServices returned 0x%08x"
+ "%s <Warning> valueCF null"
+ "-[BatteryModelDataHandler getIntValuesForKeyFromBatteryPackData:]"
+ "-[BatteryModelDataHandler getNumberOfBatteryPacks]"
+ "AppleSmartBatteryPack"
+ "BatteryPackCount"
+ "Incorrect Number of Battery Packs of 0\n"
+ "Number of Chem IDs %lu does not match number of battery packs %d \n"
+ "addObject:"
+ "array"
+ "copy"
+ "count"
+ "getBatteryChemIDs"
+ "getIntValuesForKeyFromBatteryPackData:"
+ "getNumberOfBatteryPacks"
+ "intValue"
- "%s <Error> IOConnectCallStructMethod fail to call IOUserClient setBatteryParams,  ioReturnResult = %d"
- "%s <Warning> batteryData null"

```
