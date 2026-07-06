## peakpowermanagerd

> `/usr/libexec/peakpowermanagerd`

```diff

-  __TEXT.__text: 0x106b8
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_stubs: 0x2160
-  __TEXT.__objc_methlist: 0x10d4
-  __TEXT.__objc_methname: 0x2a6a
-  __TEXT.__cstring: 0x84a
+  __TEXT.__text: 0x10cc0
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_stubs: 0x2280
+  __TEXT.__objc_methlist: 0x10f4
+  __TEXT.__objc_methname: 0x2b40
+  __TEXT.__cstring: 0x8cd
   __TEXT.__objc_classname: 0x50
-  __TEXT.__objc_methtype: 0x315
+  __TEXT.__objc_methtype: 0x332
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__const: 0x48
-  __TEXT.__oslogstring: 0xa34
+  __TEXT.__const: 0x58
+  __TEXT.__oslogstring: 0xabf
   __TEXT.__unwind_info: 0x2d0
   __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__cfstring: 0xa60
+  __DATA_CONST.__cfstring: 0xac0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__auth_got: 0x2e0
-  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__auth_got: 0x300
+  __DATA_CONST.__got: 0xa0
   __DATA.__objc_const: 0x13f0
-  __DATA.__objc_selrefs: 0xbd0
+  __DATA.__objc_selrefs: 0xc20
   __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x60

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 447
-  Symbols:   120
-  CStrings:  767
+  Functions: 451
+  Symbols:   125
+  CStrings:  790
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _CFDataGetTypeID
+ _CFNumberGetTypeID
+ _IORegistryEntryFromPath
+ _IOServiceNameMatching
+ _OBJC_CLASS_$_NSArray
CStrings:
+ "%@/%x.rcmodel"
+ "%s <Error> AppleSmartBatteryPack service null"
+ "%s <Error> BankCount property null"
+ "%s <Error> baseURL nil, error is %@"
+ "%s <Info> resolved battery model via casing fallback: %@ (target type \"%@\")"
+ "-[BatteryModelDataHandler getNumberOfBatteryBanks]"
+ "@36@0:8@16I24@28"
+ "AppleSmartBatteryPack"
+ "B24@0:8^I16"
+ "BankCount"
+ "Failed to read hw.targettype"
+ "IODeviceTree:/arm-io/ppm"
+ "Incorrect Number of Battery Banks of 0\n"
+ "Number of Chem IDs %lu does not match number of battery packs %d banks %d \n"
+ "PPM/BatteryModels"
+ "UTF8String"
+ "arrayWithObjects:count:"
+ "cpms-use-lpem-data"
+ "getNumberOfBatteryBanks"
+ "getPPMDebugDict:forbatteryPackIndex:"
+ "lowercaseString"
+ "path"
+ "ppm"
+ "readCPMSUseLPEMData:"
+ "resolveModelURLForDeviceType:chemID:inParentDirectory:"
+ "stringByAppendingString:"
+ "substringFromIndex:"
+ "substringToIndex:"
+ "uppercaseString"
- "%s <Error> workingDirURL nil"
- "%s workingDirURL resource: %@ \n"
- "Failed to malloc."
- "Failed to read size (%d)."
- "Failed to read value (%d)."
- "Number of Chem IDs %lu does not match number of battery packs %d \n"
- "PPM/BatteryModels/%@/%x.rcmodel"
- "fileSystemRepresentation"
- "getPPMDebugDict:forBatteryIndex:"

```
