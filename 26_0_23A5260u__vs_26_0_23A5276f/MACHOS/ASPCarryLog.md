## ASPCarryLog

> `/usr/libexec/ASPCarryLog`

```diff

-653.0.0.0.1
-  __TEXT.__text: 0x47e28
+653.0.4.0.0
+  __TEXT.__text: 0x47ed4
   __TEXT.__auth_stubs: 0xc10
   __TEXT.__objc_stubs: 0x30a0
   __TEXT.__objc_methlist: 0x14e8
   __TEXT.__gcc_except_tab: 0x58c
-  __TEXT.__cstring: 0x427e1
+  __TEXT.__cstring: 0x4283b
   __TEXT.__const: 0x270
   __TEXT.__objc_methname: 0x3325
   __TEXT.__oslogstring: 0x12b8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/local/lib/libNVMeCTL.dylib
-  UUID: 1F2BF7D7-7153-304B-AEB4-8BE32C5E715D
+  UUID: 10D81B95-AC39-3837-9A30-59F29AAAFCC3
   Functions: 611
   Symbols:   267
-  CStrings:  12621
+  CStrings:  12624
 
Functions:
~ sub_10002de64 : 49500 -> 49680
~ sub_10003b224 -> sub_10003b2d8 : 880 -> 872
CStrings:
+ "Band:%4d  Flow:%s [%d]  Flags:%1u%c%c%c%c%c%c%c  "
+ "Flags: Bits/Cell (1/3/4), r: retrace, C: GCcan, M: GCmust, S: Special, R: GCrd, E: erased, I: toInvalidate\n"
+ "currentThrottlingCommonLevel"
+ "nandWritesIn16KBAlignedMode"
+ "paddingFor16KBAlinged"
+ "throttlingmWEstimateLatencyHisto"
- "Band:%4d  Flow:%s [%d]  Flags:%c%c%c%c%c%c%c%c  "
- "Flags: Bits/Cell (1 or 3), r: retrace, C: GCcan, M: GCmust, S: Special, R: GCrd, E: erased, I: toInvalidate\n"
- "selfThrottlingEnabled"

```
