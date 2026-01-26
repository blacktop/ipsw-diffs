## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-488.37.0.0.0
-  __TEXT.__text: 0xffb70
+488.39.0.0.0
+  __TEXT.__text: 0x101fb8
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x17d9c
-  __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x5e8
-  __TEXT.__oslogstring: 0x36eb
-  __TEXT.__cstring: 0x784d
+  __TEXT.__objc_methlist: 0x17df4
+  __TEXT.__const: 0x168
+  __TEXT.__gcc_except_tab: 0x608
+  __TEXT.__oslogstring: 0x385c
+  __TEXT.__cstring: 0x78c7
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x3968
+  __TEXT.__unwind_info: 0x3980
   __TEXT.__objc_classname: 0x404b
-  __TEXT.__objc_methname: 0x1e325
-  __TEXT.__objc_methtype: 0x47fd
-  __TEXT.__objc_stubs: 0x13f20
-  __DATA_CONST.__got: 0xe70
+  __TEXT.__objc_methname: 0x1e3e3
+  __TEXT.__objc_methtype: 0x4800
+  __TEXT.__objc_stubs: 0x13fc0
+  __DATA_CONST.__got: 0xe80
   __DATA_CONST.__const: 0x2598
   __DATA_CONST.__objc_classlist: 0xd48
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x6e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7500
+  __DATA_CONST.__objc_selrefs: 0x7528
   __DATA_CONST.__objc_protorefs: 0x680
   __DATA_CONST.__objc_superrefs: 0x890
-  __DATA_CONST.__objc_arraydata: 0xb138
+  __DATA_CONST.__objc_arraydata: 0xb268
   __AUTH_CONST.__auth_got: 0x358
-  __AUTH_CONST.__const: 0x9c0
-  __AUTH_CONST.__cfstring: 0xd620
-  __AUTH_CONST.__objc_const: 0x51930
+  __AUTH_CONST.__const: 0xa40
+  __AUTH_CONST.__cfstring: 0xd660
+  __AUTH_CONST.__objc_const: 0x519b0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x678
-  __AUTH_CONST.__objc_dictobj: 0x5fc8
+  __AUTH_CONST.__objc_dictobj: 0x6090
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x2940
-  __DATA.__objc_ivar: 0x630
+  __DATA.__objc_ivar: 0x638
   __DATA.__data: 0x52a0
-  __DATA.__bss: 0x360
+  __DATA.__bss: 0x3a0
   __DATA_DIRTY.__objc_data: 0x5b90
   __DATA_DIRTY.__bss: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 70A58DE2-C5F6-3A64-A214-8D656B6722D9
-  Functions: 7412
-  Symbols:   24882
-  CStrings:  9620
+  UUID: C0E71F6C-BBFF-387E-B631-3390A4F43F0C
+  Functions: 7428
+  Symbols:   24935
+  CStrings:  9636
 
Symbols:
+ +[CAFAccessoryTypes isUltraOnlyType:]
+ +[CAFAccessoryTypes isUltraOnlyType:].cold.1
+ +[CAFCharacteristicTypes isUltraOnlyType:]
+ +[CAFCharacteristicTypes isUltraOnlyType:].cold.1
+ +[CAFControlTypes isUltraOnlyType:]
+ +[CAFControlTypes isUltraOnlyType:].cold.1
+ +[CAFRegistrations forCarPlay]
+ +[CAFServiceTypes isUltraOnlyType:]
+ +[CAFServiceTypes isUltraOnlyType:].cold.1
+ -[CAFCarConfiguration initWithName:identifier:ultraEnabled:rightHandDrive:pluginCount:sessionAnalytics:pluginNameDictionary:]
+ -[CAFCarConfiguration ultraEnabled]
+ -[CAFCarManagerConfiguration forCarPlay]
+ -[CAFCarManagerConfiguration setForCarPlay:]
+ _OBJC_IVAR_$_CAFCarConfiguration._ultraEnabled
+ _OBJC_IVAR_$_CAFCarManagerConfiguration._forCarPlay
+ ___35+[CAFControlTypes isUltraOnlyType:]_block_invoke
+ ___35+[CAFServiceTypes isUltraOnlyType:]_block_invoke
+ ___37+[CAFAccessoryTypes isUltraOnlyType:]_block_invoke
+ ___42+[CAFCharacteristicTypes isUltraOnlyType:]_block_invoke
+ ___56-[CAFCarManager shouldAllocAccessoryType:serviceConfig:]_block_invoke.118
+ ___block_literal_global.1765
+ ___block_literal_global.248
+ ___block_literal_global.273
+ ___block_literal_global.854
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ _isUltraOnlyType:._isUltraOnlyType
+ _isUltraOnlyType:.onceToken
+ _objc_msgSend$forCarPlay
+ _objc_msgSend$hasGaugeClusterScreen
+ _objc_msgSend$initWithName:identifier:ultraEnabled:rightHandDrive:pluginCount:sessionAnalytics:pluginNameDictionary:
+ _objc_msgSend$isUltraOnlyType:
+ _objc_msgSend$setForCarPlay:
+ _objc_msgSend$ultraEnabled
- -[CAFCarConfiguration initWithName:identifier:rightHandDrive:pluginCount:sessionAnalytics:pluginNameDictionary:]
- ___56-[CAFCarManager shouldAllocAccessoryType:serviceConfig:]_block_invoke.117
- _objc_msgSend$initWithName:identifier:rightHandDrive:pluginCount:sessionAnalytics:pluginNameDictionary:
CStrings:
+ "%{public}@ %s old:(locale=%@ measurementSystem=%@ tempUnit=%@) new:(locale=%@ measurementSystem=%@ tempUnit=%@) measurementSystemChanged=%@ tempUnitChanged=%@"
+ "-[CAFDimensionManager currentLocaleChanged]"
+ "<%@ %p(%p): name=%@ uniqueIdentifier=%@ ultraEnabled=%@ %@ isConfigured=%@ recievedAllValues=%@>"
+ "<%@: %p delegate=%p name=%@ uniqueIdentifier=%@ ultraEnabled=%@ pluginCount=%lu/%lu>"
+ "@64@0:8@16@24B32B36Q40@48@56"
+ "CAFCarConfigurationUltraEnabledKey"
+ "T@\"CAFASCTree\",&,N"
+ "T@\"CAFASCTree\",&,N,V_forCarPlay"
+ "TB,R,N,V_ultraEnabled"
+ "_forCarPlay"
+ "_ultraEnabled"
+ "forCarPlay"
+ "hasGaugeClusterScreen"
+ "initWithName:identifier:ultraEnabled:rightHandDrive:pluginCount:sessionAnalytics:pluginNameDictionary:"
+ "isUltraOnlyType:"
+ "setForCarPlay:"
+ "should not allocate accessory %{public}@ (shouldAlloc=%{public}@ disabledASC=%{public}@ ultraOnly=%{public}@)"
+ "should not allocate characteristic %{public}@.%{public}@.%{public}@ (shouldAlloc=%{public}@  disabledASC=%{public}@ ultraOnly=%{public}@ forCarPlay=%{public}@)"
+ "should not allocate control %{public}@.%{public}@.%{public}@ (shouldAlloc=%{public}@  disabledASC=%{public}@ ultraOnly=%{public}@ forCarPlay=%{public}@)"
+ "should not allocate service %{public}@.%{public}@ (shouldAlloc=%{public}@  disabledASC=%{public}@ ultraOnly=%{public}@ forCarPlay=%{public}@)"
+ "ultraEnabled"
- "<%@ %p(%p): name=%@ uniqueIdentifier=%@ %@ isConfigured=%@ recievedAllValues=%@>"
- "<%@: %p delegate=%p name=%@ uniqueIdentifier=%@ pluginCount=%lu/%lu>"
- "@60@0:8@16@24B32Q36@44@52"
- "initWithName:identifier:rightHandDrive:pluginCount:sessionAnalytics:pluginNameDictionary:"
- "should not allocate accessory %{public}@ (shouldAlloc=%{public}@ disabled=%{public}@)"
- "should not allocate characteristic %{public}@.%{public}@.%{public}@"
- "should not allocate control %{public}@.%{public}@.%{public}@ (shouldAlloc=%{public}@ disabled=%{public}@)"
- "should not allocate service %{public}@.%{public}@ (shouldAlloc=%{public}@ disabled=%{public}@)"

```
