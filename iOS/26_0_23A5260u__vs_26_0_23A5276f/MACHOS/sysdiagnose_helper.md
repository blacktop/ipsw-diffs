## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-1512.0.0.0.0
-  __TEXT.__text: 0x37e98
+1522.0.0.0.2
+  __TEXT.__text: 0x37f58
   __TEXT.__auth_stubs: 0xbd0
   __TEXT.__objc_stubs: 0x13e0
   __TEXT.__objc_methlist: 0x55c
   __TEXT.__const: 0x3f8
   __TEXT.__gcc_except_tab: 0x7c4
   __TEXT.__oslogstring: 0x20c2
-  __TEXT.__cstring: 0x2e60d
+  __TEXT.__cstring: 0x2e667
   __TEXT.__objc_classname: 0xc4
   __TEXT.__objc_methtype: 0x29b
-  __TEXT.__objc_methname: 0x1448
+  __TEXT.__objc_methname: 0x1444
   __TEXT.__unwind_info: 0x520
   __DATA_CONST.__auth_got: 0x5f8
   __DATA_CONST.__got: 0x198

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
-  UUID: 89E11AA5-5E2F-3716-BF0C-CF8087C68621
+  UUID: 833AF6CD-49F2-3453-A732-52B2C1EF45F2
   Functions: 314
   Symbols:   251
-  CStrings:  4235
+  CStrings:  4238
 
Functions:
~ sub_100005010 : 336 -> 356
~ sub_100028734 -> sub_100028748 : 49500 -> 49680
~ sub_10003618c -> sub_100036254 : 880 -> 872
CStrings:
+ "Band:%4d  Flow:%s [%d]  Flags:%1u%c%c%c%c%c%c%c  "
+ "Flags: Bits/Cell (1/3/4), r: retrace, C: GCcan, M: GCmust, S: Special, R: GCrd, E: erased, I: toInvalidate\n"
+ "currentThrottlingCommonLevel"
+ "intelligencePlatformTaskWithDir:withTimeout:"
+ "nandWritesIn16KBAlignedMode"
+ "paddingFor16KBAlinged"
+ "throttlingmWEstimateLatencyHisto"
- "Band:%4d  Flow:%s [%d]  Flags:%c%c%c%c%c%c%c%c  "
- "Flags: Bits/Cell (1 or 3), r: retrace, C: GCcan, M: GCmust, S: Special, R: GCrd, E: erased, I: toInvalidate\n"
- "intelligencePlatformTaskWithTimeout:withTimeout:"
- "selfThrottlingEnabled"

```
