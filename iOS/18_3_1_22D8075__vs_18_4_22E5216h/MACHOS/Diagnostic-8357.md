## Diagnostic-8357

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8357.appex/Diagnostic-8357`

```diff

-820.82.2.0.0
-  __TEXT.__text: 0x1050
-  __TEXT.__auth_stubs: 0x200
-  __TEXT.__objc_stubs: 0x700
-  __TEXT.__objc_methlist: 0x118
-  __TEXT.__cstring: 0xb6
-  __TEXT.__objc_classname: 0x5a
-  __TEXT.__objc_methname: 0x6b9
-  __TEXT.__objc_methtype: 0x142
+820.100.56.0.0
+  __TEXT.__text: 0x158c
+  __TEXT.__auth_stubs: 0x210
+  __TEXT.__objc_stubs: 0x920
+  __TEXT.__objc_methlist: 0x274
+  __TEXT.__cstring: 0x11d
+  __TEXT.__objc_classname: 0x58
+  __TEXT.__objc_methname: 0x819
+  __TEXT.__objc_methtype: 0x152
   __TEXT.__const: 0x8
-  __TEXT.__gcc_except_tab: 0x44
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x110
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__cfstring: 0x1a0
+  __TEXT.__gcc_except_tab: 0x4c
+  __TEXT.__unwind_info: 0xd8
+  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__const: 0x170
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x5e0
-  __DATA.__objc_selrefs: 0x1e0
-  __DATA.__objc_ivar: 0x14
+  __DATA_CONST.__objc_intobj: 0x78
+  __DATA.__objc_const: 0x3d0
+  __DATA.__objc_selrefs: 0x318
+  __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 26
-  Symbols:   62
-  CStrings:  144
+  Functions: 33
+  Symbols:   66
+  CStrings:  167
 
Symbols:
+ _BMDiagnosticsPanicPatternTypeColumn
+ _BiomeLibrary
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSNull
+ _objc_unsafeClaimAutoreleasedReturnValue
- _objc_retain_x21
CStrings:
+ "%@"
+ "@\"NSMutableSet\""
+ "B16@?0@\"BMStoreEvent\"8"
+ "Diagnostics"
+ "DiagnosticsPanicEventCollection"
+ "Panic"
+ "T@\"NSMutableSet\",&,N,V_logLineReferences"
+ "_logLineReferences"
+ "addObjectsFromArray:"
+ "captureTime"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "eventBody"
+ "filterWithIsIncluded:"
+ "gatherBiomeRecords"
+ "hasCaptureTime"
+ "hasPatternType"
+ "incidentID"
+ "logLineReferences"
+ "null"
+ "numberWithUnsignedInt:"
+ "patternType"
+ "publisherWithUseCase:"
+ "setLogLineReferences:"
+ "sinkWithCompletion:receiveInput:"
+ "v16@?0@\"BMStoreEvent\"8"
+ "v16@?0@\"BPSCompletion\"8"
- "\x02"
- " "
- "componentsJoinedByString:"

```
