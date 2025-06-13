## AppleProxServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter`

```diff

-31.6.0.0.0
-  __TEXT.__text: 0x3e44
+31.7.0.0.0
+  __TEXT.__text: 0x4170
   __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_stubs: 0x660
-  __TEXT.__objc_methlist: 0x4d8
-  __TEXT.__gcc_except_tab: 0x3e4
+  __TEXT.__objc_stubs: 0x6e0
+  __TEXT.__objc_methlist: 0x528
+  __TEXT.__gcc_except_tab: 0x454
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x555
-  __TEXT.__objc_methname: 0xd77
-  __TEXT.__oslogstring: 0x4eb
-  __TEXT.__objc_classname: 0x91
-  __TEXT.__objc_methtype: 0x47e
-  __TEXT.__unwind_info: 0x1b0
+  __TEXT.__cstring: 0x5fa
+  __TEXT.__objc_methname: 0xf5f
+  __TEXT.__oslogstring: 0x52a
+  __TEXT.__objc_classname: 0x92
+  __TEXT.__objc_methtype: 0x4b0
+  __TEXT.__unwind_info: 0x1bc
   __DATA_CONST.__auth_got: 0x1e8
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0xa60
+  __DATA_CONST.__cfstring: 0xb40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0xba8
-  __DATA.__objc_selrefs: 0x378
-  __DATA.__objc_classrefs: 0x30
-  __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_const: 0xc38
+  __DATA.__objc_selrefs: 0x3c8
+  __DATA.__objc_ivar: 0x70
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   __DATA.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7D1112BC-F4B8-388F-9DC8-64B0E765B3D3
-  Functions: 116
-  Symbols:   84
-  CStrings:  471
+  UUID: CAD5D0DF-9715-3826-B6C0-9CA516C51C1F
+  Functions: 123
+  Symbols:   86
+  CStrings:  508
 
Symbols:
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSISO8601DateFormatter
CStrings:
+ "5\x11"
+ "@\"NSDate\""
+ "C"
+ "C16@0:8"
+ "Current reading received - avg: %lld microamps over %u samples"
+ "SupplyCurrentReading"
+ "T@\"NSDate\",&,N,V_lastSupplyCurrentReadingDate"
+ "T@\"NSString\",?,R,C"
+ "TC,N,V_lastSupplyCurrentNumSamples"
+ "Tq,N,V_lastSupplyCurrentReadingMicroAmps"
+ "_lastSupplyCurrentNumSamples"
+ "_lastSupplyCurrentReadingDate"
+ "_lastSupplyCurrentReadingMicroAmps"
+ "average_current_ua"
+ "date"
+ "handleCurrentReport:"
+ "lastSupplyCurrentNumSamples"
+ "lastSupplyCurrentReadingDate"
+ "lastSupplyCurrentReadingMicroAmps"
+ "num_current_samples"
+ "numberWithLongLong:"
+ "setLastSupplyCurrentNumSamples:"
+ "setLastSupplyCurrentReadingDate:"
+ "setLastSupplyCurrentReadingMicroAmps:"
+ "stringFromDate:"
+ "supplyCurrent"
+ "v20@0:8C16"
+ "v24@0:8r^{?=CqC}16"
- "5"

```
