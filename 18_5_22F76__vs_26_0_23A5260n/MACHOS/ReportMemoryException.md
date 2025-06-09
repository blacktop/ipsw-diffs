## ReportMemoryException

> `/usr/libexec/ReportMemoryException`

```diff

-281.100.5.0.0
-  __TEXT.__text: 0x8070
+301.0.0.0.0
+  __TEXT.__text: 0x80dc
   __TEXT.__auth_stubs: 0x6b0
   __TEXT.__objc_stubs: 0xe00
   __TEXT.__objc_methlist: 0x14

   __TEXT.__const: 0xd8
   __TEXT.__objc_classname: 0xe
   __TEXT.__objc_methtype: 0x31
-  __TEXT.__oslogstring: 0x195a
+  __TEXT.__oslogstring: 0x19b7
   __TEXT.__gcc_except_tab: 0x94
   __TEXT.__objc_methname: 0x9b9
   __TEXT.__unwind_info: 0x130

   __DATA.__objc_selrefs: 0x380
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x58
-  __DATA.__crash_info: 0x40
+  __DATA.__crash_info: 0x148
   __DATA.__common: 0x8
   __DATA.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 873E5E8D-B12E-3F84-B7C0-B9C2CA4FEF92
+  UUID: 8B91D864-ACFE-38D1-9934-7D85CE314428
   Functions: 48
   Symbols:   159
-  CStrings:  380
+  CStrings:  381
 
Functions:
~ sub_100003780 : 1884 -> 1876
~ sub_100005b4c -> sub_100005b44 : 1120 -> 1240
~ sub_100008540 -> sub_1000085b0 : 60 -> 56
CStrings:
+ "Analysis of %{public}@ [%d] timed out. (%lu: RMEMemgraphFailedReasonHitLogGenerationTimeout)"

```
