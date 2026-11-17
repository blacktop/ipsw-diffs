## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

-7027.2.13.0.0
-  __TEXT.__text: 0x4454a8
-  __TEXT.__objc_methlist: 0x334bc
-  __TEXT.__cstring: 0x398b2
+7027.2.519.2.2
+  __TEXT.__text: 0x445cdc
+  __TEXT.__objc_methlist: 0x334d4
+  __TEXT.__cstring: 0x398d2
   __TEXT.__const: 0xd9b9c
   __TEXT.__oslogstring: 0xe153
-  __TEXT.__gcc_except_tab: 0x4264
+  __TEXT.__gcc_except_tab: 0x4270
   __TEXT.__dlopen_cstrs: 0x644
   __TEXT.__ustring: 0x1d0
   __TEXT.__constg_swiftt: 0x6afc

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x10120
+  __DATA_CONST.__const: 0x10128
   __DATA_CONST.__objc_classlist: 0x1d50
   __DATA_CONST.__objc_catlist: 0x1b8
   __DATA_CONST.__objc_protolist: 0x868
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x126a8
+  __DATA_CONST.__objc_selrefs: 0x126c0
   __DATA_CONST.__objc_protorefs: 0x658
   __DATA_CONST.__objc_superrefs: 0x18c8
   __DATA_CONST.__objc_arraydata: 0x69d8
   __DATA_CONST.__got: 0x1f98
-  __AUTH_CONST.__const: 0x17529
-  __AUTH_CONST.__cfstring: 0x34b00
+  __AUTH_CONST.__const: 0x17509
+  __AUTH_CONST.__cfstring: 0x34b20
   __AUTH_CONST.__objc_const: 0x57140
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x4a58

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 32458
-  Symbols:   37433
-  CStrings:  9152
+  Functions: 32456
+  Symbols:   37435
+  CStrings:  9153
 
Symbols:
+ +[HKChartableCodedQuantity _valueFromCodedQuantity:inUnit:unitNameResolver:error:]
+ +[HKChartableCodedQuantity chartableCodedQuantityWithCodings:originalCodedQuantity:originalRangeLowCodedQuantity:originalRangeHighCodedQuantity:unitNameResolver:error:]
+ -[HKCodedValue chartableCodedQuantitySetWithDate:unitNameResolver:error:]
+ -[HKCodedValue chartableCodedQuantityWithUnitNameResolver:error:]
+ ___73-[HKCodedValue chartableCodedQuantitySetWithDate:unitNameResolver:error:]_block_invoke
+ ___block_descriptor_48_e8_32s40r_e22_16?0"HKCodedValue"8ls32l8r40l8
+ _kHKPairedWatchOverride
- +[HKChartableCodedQuantity _valueFromCodedQuantity:inUnit:error:]
- +[HKChartableCodedQuantity converter]
- ___37+[HKChartableCodedQuantity converter]_block_invoke
- ___56-[HKCodedValue chartableCodedQuantitySetWithDate:error:]_block_invoke
- ___block_descriptor_40_e8_32r_e22_16?0"HKCodedValue"8lr32l8
CStrings:
+ "kHKPairedWatchOverride"
```
