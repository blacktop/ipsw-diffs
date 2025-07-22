## SignpostSupport

> `/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport`

```diff

-172.0.0.0.0
-  __TEXT.__text: 0x48a08
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x61bc
+173.0.0.0.0
+  __TEXT.__text: 0x48f54
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_methlist: 0x622c
   __TEXT.__const: 0x228
-  __TEXT.__cstring: 0x16d0f
+  __TEXT.__cstring: 0x16da9
   __TEXT.__oslogstring: 0xe6a
   __TEXT.__gcc_except_tab: 0x28c
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0x1190
-  __TEXT.__objc_classname: 0xd28
-  __TEXT.__objc_methname: 0xea77
-  __TEXT.__objc_methtype: 0x1136
-  __TEXT.__objc_stubs: 0x87e0
-  __DATA_CONST.__got: 0x2f0
-  __DATA_CONST.__const: 0xb50
+  __TEXT.__unwind_info: 0x11c0
+  __TEXT.__objc_classname: 0xd2a
+  __TEXT.__objc_methname: 0xea97
+  __TEXT.__objc_methtype: 0x118e
+  __TEXT.__objc_stubs: 0x88e0
+  __DATA_CONST.__got: 0x300
+  __DATA_CONST.__const: 0xb78
   __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2950
+  __DATA_CONST.__objc_selrefs: 0x2990
   __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__objc_arraydata: 0x5058
-  __AUTH_CONST.__auth_got: 0x2c8
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0xae0
-  __AUTH_CONST.__cfstring: 0x18360
-  __AUTH_CONST.__objc_const: 0xd870
+  __AUTH_CONST.__cfstring: 0x183c0
+  __AUTH_CONST.__objc_const: 0xd800
   __AUTH_CONST.__objc_arrayobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH.__objc_data: 0x168
-  __DATA.__objc_ivar: 0x8fc
+  __DATA.__objc_ivar: 0x8ec
   __DATA.__data: 0xb48
   __DATA.__bss: 0x3a0
   __DATA_DIRTY.__objc_data: 0x1ba8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5B4FB291-DA87-3AD0-B793-63C38BE8C9E0
-  Functions: 2296
-  Symbols:   7652
-  CStrings:  8976
+  UUID: 10EE479D-CD99-35CC-AF7A-422FB929DF8B
+  Functions: 2306
+  Symbols:   7683
+  CStrings:  8985
 
Symbols:
+ -[SSCAMetalLayerOnGlassDrawableInterval drawableID]
+ -[SSInFlightCAMetalDrawableInterval initWithOnGlassSignpostInterval:namedArgDict:]
+ -[SignpostSupportValueStats _percentile:]
+ -[SignpostSupportValueStats _sortValuesIfNeeded]
+ -[SignpostSupportValueStats addValue:]
+ -[SignpostSupportValueStats addValues:]
+ -[SignpostSupportValueStats addValues:count:]
+ -[SignpostSupportValueStats dealloc]
+ -[SignpostSupportValueStats initWithCapacity:unitsLabel:]
+ -[SignpostSupportValueStats setSupportsDynamicPercentiles:]
+ -[SignpostSupportValueStats variance]
+ _NSInternalInconsistencyException
+ _OBJC_CLASS_$_NSException
+ _OBJC_IVAR_$_SSCAMetalLayerOnGlassDrawableInterval._drawableID
+ _OBJC_IVAR_$_SignpostSupportValueStats._capacity
+ _OBJC_IVAR_$_SignpostSupportValueStats._isSorted
+ _OBJC_IVAR_$_SignpostSupportValueStats._stats
+ _OBJC_IVAR_$_SignpostSupportValueStats._values
+ ___62+[SignpostAnimationInterval frameStatisticsForFrameLifetimes:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e42_v32?0"SignpostSupportValueStats"8Q16^B24ls32l8s40l8
+ ___block_literal_global.1011
+ ___block_literal_global.1020
+ ___block_literal_global.831
+ ___block_literal_global.944
+ ___block_literal_global.946
+ ___block_literal_global.948
+ ___block_literal_global.950
+ ___block_literal_global.952
+ ___block_literal_global.954
+ ___block_literal_global.956
+ _compareDoubles
+ _malloc_type_malloc
+ _malloc_type_realloc
+ _memcpy
+ _objc_msgSend$_percentile:
+ _objc_msgSend$_sortValuesIfNeeded
+ _objc_msgSend$addValue:
+ _objc_msgSend$addValues:
+ _objc_msgSend$addValues:count:
+ _objc_msgSend$initWithCapacity:unitsLabel:
+ _objc_msgSend$initWithOnGlassSignpostInterval:namedArgDict:
+ _objc_msgSend$raise:format:
+ _objc_msgSend$setSupportsDynamicPercentiles:
+ _objc_msgSend$supportsDynamicPercentiles
+ _objc_msgSend$variance
+ _qsort
- -[SSInFlightCAMetalDrawableInterval initWithOnGlassSignpostInterval:]
- -[SignpostSupportValueStats sortedValues]
- _OBJC_IVAR_$_SignpostSupportValueStats._max
- _OBJC_IVAR_$_SignpostSupportValueStats._min
- _OBJC_IVAR_$_SignpostSupportValueStats._p50
- _OBJC_IVAR_$_SignpostSupportValueStats._p90
- _OBJC_IVAR_$_SignpostSupportValueStats._p95
- _OBJC_IVAR_$_SignpostSupportValueStats._p99
- _OBJC_IVAR_$_SignpostSupportValueStats._sortedValues
- _OBJC_IVAR_$_SignpostSupportValueStats._stddev
- _OBJC_IVAR_$_SignpostSupportValueStats._sum
- ___block_literal_global.1007
- ___block_literal_global.1013
- ___block_literal_global.827
- ___block_literal_global.937
- ___block_literal_global.939
- ___block_literal_global.941
- ___block_literal_global.943
- ___block_literal_global.945
- ___block_literal_global.947
- ___block_literal_global.949
- __valueForPercentile
- _objc_msgSend$initWithOnGlassSignpostInterval:
- _objc_msgSend$sortedArrayUsingSelector:
- _objc_msgSend$sortedValues
CStrings:
+ "Adding values to frozen value statistics"
+ "Enabling supporting dynamic percentiles is not supported."
+ "T@\"NSNumber\",R,N,V_drawableID"
+ "^d"
+ "_capacity"
+ "_drawableID"
+ "_isSorted"
+ "_percentile:"
+ "_sortValuesIfNeeded"
+ "_values"
+ "addValue:"
+ "addValues:"
+ "addValues:count:"
+ "d24@0:8d16"
+ "drawableID"
+ "drawable_id"
+ "initWithCapacity:unitsLabel:"
+ "initWithOnGlassSignpostInterval:namedArgDict:"
+ "raise:format:"
+ "setSupportsDynamicPercentiles:"
+ "v32@0:8r^d16Q24"
+ "v32@?0@\"SignpostSupportValueStats\"8Q16^B24"
+ "variance"
+ "{?=\"sum\"d\"min\"d\"max\"d\"variance\"d\"p50\"d\"p90\"d\"p95\"d\"p99\"d}"
+ "\xc1"
- "T@\"NSArray\",R,N,V_sortedValues"
- "Td,R,N,V_max"
- "Td,R,N,V_min"
- "Td,R,N,V_p50"
- "Td,R,N,V_p90"
- "Td,R,N,V_p95"
- "Td,R,N,V_p99"
- "Td,R,N,V_stddev"
- "Td,R,N,V_sum"
- "_p50"
- "_p90"
- "_p95"
- "_p99"
- "_sortedValues"
- "_sum"
- "initWithOnGlassSignpostInterval:"
- "sortedArrayUsingSelector:"
- "sortedValues"
- "\x92"

```
