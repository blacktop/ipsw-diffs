## ClockKit

> `/System/Library/Frameworks/ClockKit.framework/ClockKit`

```diff

-2398.53.19.0.0
-  __TEXT.__text: 0x6b35c
-  __TEXT.__auth_stubs: 0xf30
+2398.92.0.0.0
+  __TEXT.__text: 0x6b250
+  __TEXT.__auth_stubs: 0xf20
   __TEXT.__objc_methlist: 0x8e64
   __TEXT.__const: 0xa2a
   __TEXT.__cstring: 0x3fb2

   __TEXT.__dlopen_cstrs: 0x21c
   __TEXT.__ustring: 0x84
   __TEXT.__constg_swiftt: 0x14c
-  __TEXT.__swift5_typeref: 0x143
+  __TEXT.__swift5_typeref: 0x135
   __TEXT.__swift5_reflstr: 0x95
   __TEXT.__swift5_fieldmd: 0xf0
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x24cc
-  __TEXT.__eh_frame: 0x148
+  __TEXT.__unwind_info: 0x2494
+  __TEXT.__eh_frame: 0x118
   __TEXT.__objc_classname: 0x1e27
-  __TEXT.__objc_methname: 0xedec
+  __TEXT.__objc_methname: 0xee00
   __TEXT.__objc_methtype: 0x1a1b
   __TEXT.__objc_stubs: 0x8ce0
   __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0x1a48
+  __DATA_CONST.__const: 0x1a58
   __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xc370
   __DATA_CONST.__objc_selrefs: 0x3280
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x500
+  __DATA_CONST.__objc_superrefs: 0x498
   __DATA_CONST.__objc_arraydata: 0x4a0
   __AUTH_CONST.__cfstring: 0x4d60
   __AUTH_CONST.__objc_const: 0x5b68
-  __AUTH_CONST.__const: 0x1090
+  __AUTH_CONST.__const: 0x1088
   __AUTH_CONST.__objc_intobj: 0x9c0
   __AUTH_CONST.__objc_doubleobj: 0x230
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__auth_got: 0x7a8
+  __AUTH_CONST.__auth_got: 0x7a0
   __AUTH.__objc_data: 0x3788
   __AUTH.__data: 0x28
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x500
-  __DATA.__objc_superrefs: 0x498
   __DATA.__objc_ivar: 0xa9c
-  __DATA.__data: 0x780
+  __DATA.__data: 0x778
   __DATA.__bss: 0xb30
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3752
-  Symbols:   11641
-  CStrings:  3752
+  - /usr/lib/swift/libswiftsimd.dylib
+  Functions: 3749
+  Symbols:   11643
+  CStrings:  3753
 
Symbols:
+ ___42-[CLKComplicationServer _createConnection]_block_invoke.91
+ ___42-[CLKComplicationServer _createConnection]_block_invoke.91.cold.1
+ ___63-[CLKComplicationServer getComplicationDescriptorsWithHandler:]_block_invoke.150
+ ___73-[CLKComplicationServer getWidgetMigrationConfigurationFrom:withHandler:]_block_invoke.157
+ ___73-[CLKComplicationServer getWidgetMigrationConfigurationFrom:withHandler:]_block_invoke.157.cold.1
+ ___73-[CLKComplicationServer getWidgetMigrationConfigurationFrom:withHandler:]_block_invoke.157.cold.2
+ ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.140
+ ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.140.cold.1
+ ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.140.cold.2
+ ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.140.cold.3
+ ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.144
+ ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.144.cold.1
+ ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.144.cold.2
+ ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.144.cold.3
+ ____FinalizedEntriesFilteredByDateAndCount_block_invoke.220
+ ___block_literal_global.55
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_ClockKit
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_ClockKit
- ___42-[CLKComplicationServer _createConnection]_block_invoke.90
- ___42-[CLKComplicationServer _createConnection]_block_invoke.90.cold.1
- ___63-[CLKComplicationServer getComplicationDescriptorsWithHandler:]_block_invoke.149
- ___73-[CLKComplicationServer getWidgetMigrationConfigurationFrom:withHandler:]_block_invoke.156
- ___73-[CLKComplicationServer getWidgetMigrationConfigurationFrom:withHandler:]_block_invoke.156.cold.1
- ___73-[CLKComplicationServer getWidgetMigrationConfigurationFrom:withHandler:]_block_invoke.156.cold.2
- ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.139
- ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.139.cold.1
- ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.139.cold.2
- ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.139.cold.3
- ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.143
- ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.143.cold.1
- ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.143.cold.2
- ___81-[CLKComplicationServer getLocalizableSampleTemplateForComplication:withHandler:]_block_invoke.143.cold.3
- ____FinalizedEntriesFilteredByDateAndCount_block_invoke.219
- _swift_initStaticObject
- _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
CStrings:
+ "T@\"<CLKComplicationWidgetMigrator>\",?,R,N"
+ "T@\"NSString\",?,R,C"
- "T@\"<CLKComplicationWidgetMigrator>\",R,N"

```
