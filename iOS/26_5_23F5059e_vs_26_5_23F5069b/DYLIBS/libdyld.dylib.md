## libdyld.dylib

> `/usr/lib/system/libdyld.dylib`

```diff

-1377.3.0.0.0
-  __TEXT.__text: 0x2bfe8
+1378.0.0.0.0
+  __TEXT.__text: 0x2c100
   __TEXT.__auth_stubs: 0x660
   __TEXT.__const: 0x600
-  __TEXT.__cstring: 0x4a06
+  __TEXT.__cstring: 0x4ab9
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x1708
   __DATA_CONST.__helper: 0x8

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: E13B6FC0-9898-330D-A282-536A71036287
+  UUID: 4BAB3E37-F84A-3A6C-8E40-E82A54E6BFC3
   Functions: 1101
   Symbols:   3062
-  CStrings:  548
+  CStrings:  550
 
Symbols:
+ __ZNK6mach_o13ChainedFixups13validLinkeditEybNSt3__14spanIKNS_13MappedSegmentELm18446744073709551615EEE
+ __ZNK6mach_o13ChainedFixups5validEyNSt3__14spanIKNS_13MappedSegmentELm18446744073709551615EEEbb
- __ZNK6mach_o13ChainedFixups13validLinkeditEyNSt3__14spanIKNS_13MappedSegmentELm18446744073709551615EEE
- __ZNK6mach_o13ChainedFixups5validEyNSt3__14spanIKNS_13MappedSegmentELm18446744073709551615EEEb
Functions:
~ __ZNK6mach_o13ChainedFixups13validLinkeditEyNSt3__14spanIKNS_13MappedSegmentELm18446744073709551615EEE -> __ZNK6mach_o13ChainedFixups13validLinkeditEybNSt3__14spanIKNS_13MappedSegmentELm18446744073709551615EEE : 1180 -> 1428
~ __ZNK6mach_o13ChainedFixups5validEyNSt3__14spanIKNS_13MappedSegmentELm18446744073709551615EEEb -> __ZNK6mach_o13ChainedFixups5validEyNSt3__14spanIKNS_13MappedSegmentELm18446744073709551615EEEbb : 96 -> 112
~ __ZNK6mach_o5Image13validLinkeditERKNS_6PolicyE : 840 -> 856
CStrings:
+ "chained fixups, in segment #%d page_start[%d]=0x%04X multi-start chains not supported in 64-bit archs"
+ "chained fixups, pointer_format=%d in segment #%d does not match pointer size"

```
