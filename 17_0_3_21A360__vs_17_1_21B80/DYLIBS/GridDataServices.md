## GridDataServices

> `/System/Library/PrivateFrameworks/GridDataServices.framework/GridDataServices`

```diff

-57.0.0.0.0
-  __TEXT.__text: 0x775c
+60.0.0.0.0
+  __TEXT.__text: 0x7830
   __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x5b0
+  __TEXT.__objc_methlist: 0x5c0
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x7f5
+  __TEXT.__cstring: 0x817
   __TEXT.__oslogstring: 0x816
   __TEXT.__gcc_except_tab: 0x180
-  __TEXT.__unwind_info: 0x204
+  __TEXT.__unwind_info: 0x208
   __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methname: 0x14fa
+  __TEXT.__objc_methname: 0x1546
   __TEXT.__objc_methtype: 0x317
-  __TEXT.__objc_stubs: 0x1140
+  __TEXT.__objc_stubs: 0x11a0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x1e8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xda8
-  __DATA_CONST.__objc_selrefs: 0x5e8
-  __DATA_CONST.__objc_arraydata: 0x98
+  __DATA_CONST.__objc_selrefs: 0x600
+  __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__objc_const: 0x2d0
-  __AUTH_CONST.__cfstring: 0xc60
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__objc_dictobj: 0x140
+  __AUTH_CONST.__cfstring: 0xca0
+  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x238
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0xf8
+  __DATA.__objc_classrefs: 0x100
   __DATA.__objc_superrefs: 0x30
   __DATA.__objc_ivar: 0x70
   __DATA.__data: 0x120

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 59BC543D-F93C-323E-B356-DD1FDFA0331B
-  Functions: 168
-  Symbols:   750
-  CStrings:  595
+  UUID: 02FBC4CE-4F8F-3C4B-BCAF-C255C2BD7D0A
+  Functions: 170
+  Symbols:   761
+  CStrings:  602
 
Symbols:
+ +[_GDSServerConnection fetchEstimatedCountryCode]
+ GCC_except_table10
+ GCC_except_table24
+ GCC_except_table28
+ GCC_except_table31
+ GCC_except_table34
+ _OBJC_CLASS_$_RDEstimate
+ ___44+[_GDSServerConnection queryItemsMetaParams]_block_invoke
+ ___45+[_GDSServerConnection fetchConfigWithError:]_block_invoke.146
+ ___45+[_GDSServerConnection fetchConfigWithError:]_block_invoke.146.cold.1
+ ___55-[_GDSServerConnection fetchBalancingAuthorityPolygons]_block_invoke.193
+ ___57-[_GDSServerConnection fetchMarginalEmissionForecastFor:]_block_invoke.203
+ ___65-[_GDSServerConnection fetchCarbonIntensityHistoryForBA:from:to:]_block_invoke.236
+ ___block_literal_global.110
+ ___block_literal_global.205
+ ___block_literal_global.238
+ __unnamed_array_storage.115
+ __unnamed_array_storage.210
+ __unnamed_array_storage.211
+ __unnamed_array_storage.235
+ __unnamed_array_storage.243
+ __unnamed_array_storage.244
+ _objc_msgSend$currentEstimates
+ _objc_msgSend$fetchEstimatedCountryCode
+ _objc_msgSend$lastKnownEstimates
+ _objc_msgSend$objectAtIndexedSubscript:
- GCC_except_table22
- GCC_except_table26
- GCC_except_table29
- GCC_except_table32
- GCC_except_table8
- ___45+[_GDSServerConnection fetchConfigWithError:]_block_invoke.134
- ___45+[_GDSServerConnection fetchConfigWithError:]_block_invoke.134.cold.1
- ___55-[_GDSServerConnection fetchBalancingAuthorityPolygons]_block_invoke.184
- ___57-[_GDSServerConnection fetchMarginalEmissionForecastFor:]_block_invoke.193
- ___65-[_GDSServerConnection fetchCarbonIntensityHistoryForBA:from:to:]_block_invoke.226
- ___block_literal_global.187
- ___block_literal_global.228
- __unnamed_array_storage.192
- __unnamed_array_storage.225
- __unnamed_array_storage.233
- __unnamed_array_storage.234
- _objc_msgSend$currentLocale
CStrings:
+ "ErrorFetchingDeviceCountryCode"
+ "US"
+ "currentEstimates"
+ "fetchEstimatedCountryCode"
+ "lastKnownEstimates"
+ "objectAtIndexedSubscript:"
- "currentLocale"

```
