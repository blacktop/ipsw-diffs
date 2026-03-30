## migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

-1224.102.3.0.0
-  __TEXT.__text: 0x16bc4
+1224.120.85.502.1
+  __TEXT.__text: 0x16c10
   __TEXT.__auth_stubs: 0xce0
   __TEXT.__objc_stubs: 0x2c0
   __TEXT.__objc_methlist: 0x37c

   __TEXT.__swift5_entry: 0x8
   __TEXT.__oslogstring: 0x5b4
   __TEXT.__objc_classname: 0xb0
-  __TEXT.__objc_methname: 0x6f9
-  __TEXT.__objc_methtype: 0x3ca
-  __TEXT.__const: 0x82a
+  __TEXT.__objc_methname: 0x6db
+  __TEXT.__objc_methtype: 0x39a
+  __TEXT.__const: 0x83a
   __TEXT.__constg_swiftt: 0x2d0
-  __TEXT.__swift5_typeref: 0x3e1
+  __TEXT.__swift5_typeref: 0x405
   __TEXT.__swift5_reflstr: 0x101
   __TEXT.__swift5_fieldmd: 0x1c0
   __TEXT.__swift5_assocty: 0x80

   __TEXT.__eh_frame: 0x1440
   __DATA_CONST.__auth_got: 0x678
   __DATA_CONST.__got: 0x2f8
-  __DATA_CONST.__auth_ptr: 0x1f8
+  __DATA_CONST.__auth_ptr: 0x200
   __DATA_CONST.__const: 0x978
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 93E96392-C1C5-3341-9FCD-8AAA94290DF8
+  UUID: 2AE9D322-078E-3987-90D6-1D2BD2662E60
   Functions: 455
-  Symbols:   383
+  Symbols:   384
   CStrings:  188
 
Symbols:
+ _$s12MigrationKit10EstimationV11bytesOnDisks6UInt64Vvg
+ _$s12MigrationKit10EstimationV12bytesInClouds6UInt64Vvg
+ _$s12MigrationKit10EstimationVMn
+ _$s12MigrationKit14TransferResultV9XPCHelperC6resultAeC_tcfc
+ _$s12MigrationKit14TransferResultV9XPCHelperCMa
+ _$s12MigrationKit14TransferResultVMa
+ _$s12MigrationKit6ClientC5StateO11transferredyAeA14TransferResultV_tcAEmFWC
+ _$s12MigrationKit6ServerC5StateO11transferredyAeA14TransferResultV_tcAEmFWC
+ _$s12MigrationKit6ServerC5StateO9estimatedyAeA9SelectionO_AA10EstimationVtcAEmFWC
- _$s12MigrationKit10EstimationV5bytess6UInt64Vvg
- _$s12MigrationKit10EstimationV9selectionAA9SelectionOvg
- _$s12MigrationKit15MigratorContextV9XPCHelperC7contextAeC_tcfc
- _$s12MigrationKit15MigratorContextV9XPCHelperCMa
- _$s12MigrationKit15MigratorContextVMa
- _$s12MigrationKit6ClientC5StateO11transferredyAeA15MigratorContextV_tcAEmFWC
- _$s12MigrationKit6ServerC5StateO11transferredyAeA15MigratorContextV_tcAEmFWC
- _$s12MigrationKit6ServerC5StateO9estimatedyAeA10EstimationV_tcAEmFWC
Functions:
~ sub_100012a88 : 2720 -> 2796
CStrings:
+ "didEstimateWithSelection:bytesOnDisk:bytesInCloud:items:"
+ "didTransferWithResult:"
+ "v24@0:8@\"MKTransferResult\"16"
+ "v44@0:8C16Q20Q28Q36"
- "didEstimateWithSelection:bytes:items:"
- "didTransferWithContext:"
- "v24@0:8@\"MKMigratorContext\"16"
- "v36@0:8C16Q20Q28"

```
