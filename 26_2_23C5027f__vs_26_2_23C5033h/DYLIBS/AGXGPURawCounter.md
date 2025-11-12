## AGXGPURawCounter

> `/System/Library/PrivateFrameworks/AGXGPURawCounter.framework/AGXGPURawCounter`

```diff

-341.11.0.0.0
-  __TEXT.__text: 0xeae4
-  __TEXT.__auth_stubs: 0x4d0
+342.2.0.0.0
+  __TEXT.__text: 0xecd0
+  __TEXT.__auth_stubs: 0x4c0
   __TEXT.__const: 0x1d4
-  __TEXT.__gcc_except_tab: 0x5f8
-  __TEXT.__cstring: 0x3e55
-  __TEXT.__oslogstring: 0x1fa9
+  __TEXT.__gcc_except_tab: 0x618
+  __TEXT.__cstring: 0x3f95
+  __TEXT.__oslogstring: 0x20ac
   __TEXT.__unwind_info: 0x258
   __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x131
-  __TEXT.__objc_stubs: 0x200
+  __TEXT.__objc_methname: 0x14d
+  __TEXT.__objc_stubs: 0x220
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x420
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x80
+  __DATA_CONST.__objc_selrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x278
+  __AUTH_CONST.__auth_got: 0x270
   __AUTH_CONST.__const: 0x760
-  __AUTH_CONST.__cfstring: 0x8c0
+  __AUTH_CONST.__cfstring: 0x920
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __DATA.__data: 0x1f3

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 00FA5D25-4235-3BC6-8F2B-4C9F9627251D
-  Functions: 146
-  Symbols:   478
-  CStrings:  431
+  UUID: 803A434A-8F93-335D-AEF4-B509672E21D7
+  Functions: 147
+  Symbols:   480
+  CStrings:  440
 
Symbols:
+ GCC_except_table106
+ GCC_except_table134
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table97
+ __Z28createInternalCoreConfigDictj
+ ___block_literal_global.153
+ _objc_msgSend$numberWithUnsignedLongLong:
- GCC_except_table105
- GCC_except_table133
- GCC_except_table79
- GCC_except_table81
- GCC_except_table91
- ___block_literal_global.149
- _objc_release_x26
Functions:
~ __ZN20AGXGPURawCounterImpl20populateFeaturesDictEP19NSMutableDictionary : 264 -> 360
~ __ZN20AGXGPURawCounterImpl4initEj : 14464 -> 14628
+ __Z28createInternalCoreConfigDictj
CStrings:
+ "AGXGRC:%s:%d:%s: *** \"((cfContTimeOffset = (CFNumberRef)IORegistryEntryCreateCFProperty(_acceleratorPort, CFSTR(\"ContTimeOffset\"), NULL, 0)) != NULL) && CFNumberGetValue(cfContTimeOffset, kCFNumberSInt64Type, (void*)(&_samplingState.contTimeOffset))\"\n"
+ "AGXGRC:AGXGRC:%s:%d:%s: *** \"((cfContTimeOffset = (CFNumberRef)IORegistryEntryCreateCFProperty(_acceleratorPort, CFSTR(\"ContTimeOffset\"), NULL, 0)) != NULL) && CFNumberGetValue(cfContTimeOffset, kCFNumberSInt64Type, (void*)(&_samplingState.contTimeOffset))\"\n"
+ "ConstantAGX_AbsTimeOffset"
+ "ConstantAGX_ContTimeOffset"
+ "ContTimeOffset"
+ "numberWithUnsignedLongLong:"

```
