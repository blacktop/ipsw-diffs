## IOAnalytics

> `/System/Library/HIDPlugins/SessionFilters/IOAnalytics.plugin/IOAnalytics`

```diff

-1043.120.6.0.0
-  __TEXT.__text: 0x15864
+1110.0.0.0.1
+  __TEXT.__text: 0x15c40
   __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_stubs: 0xec0
-  __TEXT.__objc_methlist: 0xebc
-  __TEXT.__const: 0x70
-  __TEXT.__objc_methname: 0x12a7
+  __TEXT.__objc_stubs: 0xee0
+  __TEXT.__objc_methlist: 0xec4
+  __TEXT.__const: 0x78
+  __TEXT.__objc_methname: 0x12ca
   __TEXT.__cstring: 0x1c77
-  __TEXT.__oslogstring: 0x13ec
+  __TEXT.__oslogstring: 0x149d
   __TEXT.__objc_classname: 0x13f
-  __TEXT.__objc_methtype: 0x4dc
+  __TEXT.__objc_methtype: 0x4ef
   __TEXT.__gcc_except_tab: 0xec
   __TEXT.__ustring: 0xa
   __TEXT.__unwind_info: 0x430

   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0x1b00
-  __DATA.__objc_selrefs: 0x578
+  __DATA.__objc_selrefs: 0x580
   __DATA.__objc_ivar: 0x168
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x178

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 111DB645-2591-3245-9620-A210320D64BB
-  Functions: 518
-  Symbols:   3890
-  CStrings:  1191
+  UUID: C3DC2DF9-A4BE-30E7-B78F-3614751C98A6
+  Functions: 525
+  Symbols:   3921
+  CStrings:  1197
 
Symbols:
+ -[ApplePCIeAnalytics _iteratePCITree:findSlot:findTBID:]
+ -[ApplePCIeAnalytics _iteratePCITree:findSlot:findTBID:].cold.1
+ -[ApplePCIeAnalytics _iteratePCITree:findSlot:findTBID:].cold.2
+ -[ApplePCIeAnalytics _iteratePCITree:findSlot:findTBID:].cold.3
+ -[ApplePCIeAnalytics _iteratePCITree:findSlot:findTBID:].cold.4
+ _objc_msgSend$_iteratePCITree:findSlot:findTBID:
CStrings:
+ "%s is not a type of IOPCIDevice"
+ "B36@0:8I16^@20^@28"
+ "Got %d instead of next IOPCIDevice parent. Next device: %s"
+ "Got %d instead of next IOPCIDevice. Current parent: %s"
+ "Got %d instead of parent of %s"
+ "IOPCIHostBridge"
+ "_iteratePCITree:findSlot:findTBID:"
- "IOPCI2PCIBridge"

```
