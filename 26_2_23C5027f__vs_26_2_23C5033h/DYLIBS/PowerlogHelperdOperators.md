## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

-2964.60.10.0.0
-  __TEXT.__text: 0x1bfc50
+2964.60.14.0.0
+  __TEXT.__text: 0x1bfd18
   __TEXT.__auth_stubs: 0x1b90
-  __TEXT.__objc_methlist: 0xeb40
+  __TEXT.__objc_methlist: 0xeb50
   __TEXT.__const: 0x6a8
   __TEXT.__cstring: 0x2320f
   __TEXT.__oslogstring: 0x12926

   __TEXT.__ustring: 0x10
   __TEXT.__unwind_info: 0x3700
   __TEXT.__objc_classname: 0xc17
-  __TEXT.__objc_methname: 0x316ca
+  __TEXT.__objc_methname: 0x316e9
   __TEXT.__objc_methtype: 0x27d0
   __TEXT.__objc_stubs: 0x1ec20
   __DATA_CONST.__got: 0xea8

   __DATA_CONST.__objc_nlclslist: 0x108
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9918
+  __DATA_CONST.__objc_selrefs: 0x9920
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x14b48
   __AUTH_CONST.__auth_got: 0xde0
   __AUTH_CONST.__const: 0x1880
   __AUTH_CONST.__cfstring: 0x31160
-  __AUTH_CONST.__objc_const: 0x12998
+  __AUTH_CONST.__objc_const: 0x129a0
   __AUTH_CONST.__objc_intobj: 0x27d8
   __AUTH_CONST.__objc_dictobj: 0x34a8
   __AUTH_CONST.__objc_doubleobj: 0xb90

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4CDFE21F-7B5C-35CA-9B4B-AC29D5ED5292
+  UUID: 13E7A73A-89C2-3167-921E-5FAA118F8E96
   Functions: 7832
   Symbols:   26519
-  CStrings:  22294
+  CStrings:  22295
 
Functions:
~ -[PLPowerMetricMonitorService _pidIsValid:] : 240 -> 260
~ +[PLUtilities compressWithSourceStream:withDestination:withLevel:] : 504 -> 524
~ +[PLUtilities decompressWithSourceStream:withDestinationStream:] : 536 -> 556
~ +[PLUtilities binaryPathForPid:] : 196 -> 216
~ +[PLUtilities fullProcessNameForPid:] : 200 -> 220
~ -[PLProcessMonitorAgent updateProcessMonitorCache] : 964 -> 984
~ -[PLProcessMonitorAgent getProcessName:] : 180 -> 200
~ +[PLWifiAgent entryEventBackwardDefinitionCumulativeBasic] : 18468 -> 18488
~ -[PLXPCAgent initOperatorDependancies] : 14044 -> 14064
~ +[PLBatteryAgent entryEventBackwardDefinitionBattery] : 7784 -> 7804
CStrings:
+ "applicationsDidUpdateMetadata:"

```
