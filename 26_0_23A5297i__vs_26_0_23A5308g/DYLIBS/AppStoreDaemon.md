## AppStoreDaemon

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon`

```diff

-12.0.60.1.1
-  __TEXT.__text: 0x82570
+12.0.66.0.0
+  __TEXT.__text: 0x826d4
   __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0xab64
+  __TEXT.__objc_methlist: 0xabc4
   __TEXT.__const: 0x2d0
   __TEXT.__dlopen_cstrs: 0xb1
-  __TEXT.__cstring: 0x52e7
+  __TEXT.__cstring: 0x532b
   __TEXT.__constg_swiftt: 0x54
   __TEXT.__swift5_typeref: 0x26
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_fieldmd: 0x28
-  __TEXT.__oslogstring: 0x478a
+  __TEXT.__oslogstring: 0x4720
   __TEXT.__gcc_except_tab: 0x1044
-  __TEXT.__unwind_info: 0x2710
+  __TEXT.__unwind_info: 0x2718
   __TEXT.__objc_classname: 0x18ac
-  __TEXT.__objc_methname: 0x142ac
+  __TEXT.__objc_methname: 0x143eb
   __TEXT.__objc_methtype: 0x348f
-  __TEXT.__objc_stubs: 0x8680
+  __TEXT.__objc_stubs: 0x86a0
   __DATA_CONST.__got: 0x620
   __DATA_CONST.__const: 0x2768
   __DATA_CONST.__objc_classlist: 0x5d8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x43a0
+  __DATA_CONST.__objc_selrefs: 0x43d8
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_got: 0x600
   __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__cfstring: 0x6780
-  __AUTH_CONST.__objc_const: 0x15638
+  __AUTH_CONST.__cfstring: 0x67e0
+  __AUTH_CONST.__objc_const: 0x156f8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1720
-  __DATA.__objc_ivar: 0xd1c
+  __DATA.__objc_ivar: 0xd2c
   __DATA.__data: 0x18f8
   __DATA.__bss: 0x310
   __DATA_DIRTY.__objc_ivar: 0x19c

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 24E2FB8D-C1CF-3B15-9A2E-F4ACBB794AB1
-  Functions: 4322
-  Symbols:   13186
-  CStrings:  6317
+  UUID: 0CA17B61-833A-3C1A-9C0F-6F5A19CC1E32
+  Functions: 4331
+  Symbols:   13209
+  CStrings:  6336
 
Symbols:
+ -[ASDPurchase performanceMetricsOverlay]
+ -[ASDPurchase setPerformanceMetricsOverlay:]
+ -[ASDPurchaseHistoryQuery genreID]
+ -[ASDPurchaseHistoryQuery properties]
+ -[ASDPurchaseHistoryQuery setGenreID:]
+ -[ASDPurchaseHistoryQuery setProperties:]
+ -[ASDPurchaseHistoryQuery setSupportsCurrentDevice:]
+ -[ASDPurchaseHistoryQuery supportsCurrentDevice]
+ _OBJC_IVAR_$_ASDPurchase._performanceMetricsOverlay
+ _OBJC_IVAR_$_ASDPurchaseHistoryQuery._genreID
+ _OBJC_IVAR_$_ASDPurchaseHistoryQuery._properties
+ _OBJC_IVAR_$_ASDPurchaseHistoryQuery._supportsCurrentDevice
+ ___39-[ASDApp updateCodedPropertiesFromApp:]_block_invoke
+ _objc_msgSend$longValue
+ _objc_msgSend$supportsCurrentDevice
- _objc_msgSend$updateCodedPropertiesFromApp:
CStrings:
+ "T@\"NSDictionary\",C,N,V_performanceMetricsOverlay"
+ "T@\"NSNumber\",&,V_genreID"
+ "TQ,V_properties"
+ "Tq,V_supportsCurrentDevice"
+ "_performanceMetricsOverlay"
+ "_properties"
+ "_supportsCurrentDevice"
+ "genreID = %ld"
+ "longValue"
+ "performanceMetricsOverlay"
+ "properties"
+ "setPerformanceMetricsOverlay:"
+ "setProperties:"
+ "setSupportsCurrentDevice:"
+ "supportsCurrentDevice"
+ "supportsCurrentDevice = %ld"
- "[%{public}@]: Forcing progress to complete after receiving update that had no remote progress: %{public}@"

```
