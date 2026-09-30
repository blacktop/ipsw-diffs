## DataDetectorsUI

> `/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI`

```diff

-599.2.0.0.0
-  __TEXT.__text: 0x537a0
-  __TEXT.__auth_stubs: 0xed0
+599.3.0.0.0
+  __TEXT.__text: 0x56094
+  __TEXT.__auth_stubs: 0xe60
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0x1748
-  __TEXT.__objc_methlist: 0x4d28
+  __TEXT.__objc_methlist: 0x4cf0
   __TEXT.__const: 0x280
-  __TEXT.__oslogstring: 0x2198
-  __TEXT.__gcc_except_tab: 0xd98
-  __TEXT.__cstring: 0x5c85
+  __TEXT.__oslogstring: 0x21b7
+  __TEXT.__gcc_except_tab: 0xd70
+  __TEXT.__cstring: 0x5aec
   __TEXT.__ustring: 0x4aa
   __TEXT.__constg_swiftt: 0x110
   __TEXT.__swift5_typeref: 0x4a

   __TEXT.__swift5_fieldmd: 0x54
   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1490
-  __TEXT.__objc_classname: 0xc1e
-  __TEXT.__objc_methname: 0xbdeb
-  __TEXT.__objc_methtype: 0x36f8
-  __TEXT.__objc_stubs: 0xae40
-  __DATA_CONST.__got: 0xa80
+  __TEXT.__unwind_info: 0x1570
+  __TEXT.__objc_classname: 0xd5f
+  __TEXT.__objc_methname: 0xc976
+  __TEXT.__objc_methtype: 0x3807
+  __TEXT.__objc_stubs: 0xad00
+  __DATA_CONST.__got: 0xa78
   __DATA_CONST.__const: 0xea0
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3390
+  __DATA_CONST.__objc_selrefs: 0x3350
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x1638
-  __AUTH_CONST.__auth_got: 0x780
+  __AUTH_CONST.__auth_got: 0x748
   __AUTH_CONST.__const: 0x308
   __AUTH_CONST.__cfstring: 0x6740
-  __AUTH_CONST.__objc_const: 0x7ab0
+  __AUTH_CONST.__objc_const: 0x7a90
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0xde0
   __AUTH_CONST.__objc_doubleobj: 0x2f0

   __AUTH.__objc_data: 0x1068
   __AUTH.__data: 0x1a0
   __DATA.__objc_ivar: 0x4a0
-  __DATA.__data: 0xaa8
+  __DATA.__data: 0xaac
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__bss: 0x158

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3DE06DC3-590B-30F4-A138-F0506CB8FF28
-  Functions: 1876
-  Symbols:   7198
-  CStrings:  4347
+  UUID: 18DE5F71-F900-38BB-99A5-7DA545CF1B3D
+  Functions: 1908
+  Symbols:   7315
+  CStrings:  4331
 
Symbols:
+ -[DDAction interceptAnalyticsReporterActionType]
+ -[DDAction interceptAnalyticsReporter]
+ -[DDAction setInterceptAnalyticsReporter:]
+ -[DDCallAction interceptAnalyticsReporterActionType]
+ -[DDDataDetectorInterceptReporter dealloc]
+ -[DDDataDetectorInterceptReporter initForContact:savedContact:shownOptions:]
+ -[DDDataDetectorInterceptReporter logForActionType:]
+ -[DDDataDetectorInterceptReporter logForActionType:].cold.1
+ -[DDDataDetectorInterceptReporter logForActionType:].cold.2
+ -[DDOpenURLAction interceptAnalyticsReporterActionType]
+ -[DDSupportFlowAction interceptAnalyticsReporterActionType]
+ -[DDTextMessageAction interceptAnalyticsReporterActionType]
+ GCC_except_table10
+ GCC_except_table102
+ GCC_except_table140
+ GCC_except_table90
+ _OBJC_IVAR_$_DDAction._interceptAnalyticsReporter
+ _OBJC_IVAR_$_DDDataDetectorInterceptReporter._logged
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___52-[DDDataDetectorInterceptReporter logForActionType:]_block_invoke
+ ___52-[DDDataDetectorInterceptReporter logForActionType:]_block_invoke_2
+ ___76-[DDDataDetectorInterceptReporter initForContact:savedContact:shownOptions:]_block_invoke
+ _objc_msgSend$init
+ _objc_msgSend$initForContact:savedContact:shownOptions:
+ _objc_msgSend$interceptAnalyticsReporter
+ _objc_msgSend$interceptAnalyticsReporterActionType
+ _objc_msgSend$logForActionType:
+ _objc_msgSend$setInterceptAnalyticsReporter:
- -[DDAction analyticsReporter]
- -[DDAction setAnalyticsReporter:]
- -[DDDataDetectorInterceptReporter eventRepresentation]
- -[DDDataDetectorInterceptReporter firstShownOption]
- -[DDDataDetectorInterceptReporter init]
- -[DDDataDetectorInterceptReporter logForAction:]
- -[DDDataDetectorInterceptReporter log]
- -[DDDataDetectorInterceptReporter log].cold.1
- -[DDDataDetectorInterceptReporter secondShownOption]
- -[DDDataDetectorInterceptReporter selectedOption]
- -[DDDataDetectorInterceptReporter setFirstShownOption:]
- -[DDDataDetectorInterceptReporter setSecondShownOption:]
- -[DDDataDetectorInterceptReporter setSelectedOption:]
- -[DDDataDetectorInterceptReporter setShownOptions:]
- -[DDDataDetectorInterceptReporter stringForOption:]
- -[DDPersonAction dealloc]
- GCC_except_table101
- GCC_except_table138
- GCC_except_table89
- _OBJC_IVAR_$_DDAction._analyticsReporter
- _OBJC_IVAR_$_DDPersonAction._analyticsReporter
- ___38-[DDDataDetectorInterceptReporter log]_block_invoke
- ___38-[DDDataDetectorInterceptReporter log]_block_invoke_2
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$analyticsReporter
- _objc_msgSend$eventRepresentation
- _objc_msgSend$firstShownOption
- _objc_msgSend$log
- _objc_msgSend$logForAction:
- _objc_msgSend$secondShownOption
- _objc_msgSend$selectedOption
- _objc_msgSend$setAnalyticsReporter:
- _objc_msgSend$setAppleSupport:
- _objc_msgSend$setContact:
- _objc_msgSend$setFirstShownOption:
- _objc_msgSend$setSavedContact:
- _objc_msgSend$setSecondShownOption:
- _objc_msgSend$setSelectedOption:
- _objc_msgSend$setShownOptions:
- _objc_msgSend$stringForOption:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "/Library/Caches/com.apple.xbs/399A43A8-D26B-4776-B179-AA84C3C17786/TemporaryDirectory.TGzkQw/Sources/MobileDataDetectorsUI/Actions/DDActionController.m"
+ "/Library/Caches/com.apple.xbs/399A43A8-D26B-4776-B179-AA84C3C17786/TemporaryDirectory.TGzkQw/Sources/MobileDataDetectorsUI/Actions/DDAddressActions.m"
+ "/Library/Caches/com.apple.xbs/399A43A8-D26B-4776-B179-AA84C3C17786/TemporaryDirectory.TGzkQw/Sources/MobileDataDetectorsUI/Actions/DDCallAction.m"
+ "/Library/Caches/com.apple.xbs/399A43A8-D26B-4776-B179-AA84C3C17786/TemporaryDirectory.TGzkQw/Sources/MobileDataDetectorsUI/Actions/DDFlightAction.m"
+ "/Library/Caches/com.apple.xbs/399A43A8-D26B-4776-B179-AA84C3C17786/TemporaryDirectory.TGzkQw/Sources/MobileDataDetectorsUI/DDPreviewActions/DDParsecCollectionViewController.m"
+ "@32@0:8B16B20@24"
+ "T@\"DDDataDetectorInterceptReporter\",&,N,V_interceptAnalyticsReporter"
+ "_interceptAnalyticsReporter"
+ "_logged"
+ "initForContact:savedContact:shownOptions:"
+ "interceptAnalyticsReporter"
+ "interceptAnalyticsReporterActionType"
+ "log intercept action: %@ -> %@"
+ "logForActionType:"
+ "setInterceptAnalyticsReporter:"
- "/Library/Caches/com.apple.xbs/Sources/MobileDataDetectorsUI/Actions/DDActionController.m"
- "/Library/Caches/com.apple.xbs/Sources/MobileDataDetectorsUI/Actions/DDAddressActions.m"
- "/Library/Caches/com.apple.xbs/Sources/MobileDataDetectorsUI/Actions/DDCallAction.m"
- "/Library/Caches/com.apple.xbs/Sources/MobileDataDetectorsUI/Actions/DDFlightAction.m"
- "/Library/Caches/com.apple.xbs/Sources/MobileDataDetectorsUI/DDPreviewActions/DDParsecCollectionViewController.m"
- "T@\"DDDataDetectorInterceptReporter\",&,N,V_analyticsReporter"
- "Tq,N,V_firstShownOption"
- "Tq,N,V_secondShownOption"
- "Tq,N,V_selectedOption"
- "_analyticsReporter"
- "analyticsReporter"
- "eventRepresentation"
- "firstShownOption"
- "log"
- "logForAction:"
- "secondShownOption"
- "selectedOption"
- "setAnalyticsReporter:"
- "setFirstShownOption:"
- "setSecondShownOption:"
- "setSelectedOption:"
- "setShownOptions:"
- "stringForOption:"

```
