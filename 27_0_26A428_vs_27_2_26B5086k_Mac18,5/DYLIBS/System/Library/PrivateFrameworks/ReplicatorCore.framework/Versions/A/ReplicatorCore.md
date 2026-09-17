## ReplicatorCore

> `/System/Library/PrivateFrameworks/ReplicatorCore.framework/Versions/A/ReplicatorCore`

```diff

-176.0.0.0.0
-  __TEXT.__text: 0x78464
+176.2.2.0.0
+  __TEXT.__text: 0x7a6c8
   __TEXT.__objc_methlist: 0x660
-  __TEXT.__const: 0xf58
-  __TEXT.__constg_swiftt: 0xdb8
-  __TEXT.__swift5_typeref: 0xeb1
-  __TEXT.__swift5_reflstr: 0x6cd
-  __TEXT.__swift5_fieldmd: 0x730
+  __TEXT.__const: 0x1258
+  __TEXT.__constg_swiftt: 0xf48
+  __TEXT.__swift5_typeref: 0xfe9
+  __TEXT.__swift5_reflstr: 0x753
+  __TEXT.__swift5_fieldmd: 0x7dc
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__oslogstring: 0x2486
-  __TEXT.__cstring: 0x9e6
+  __TEXT.__oslogstring: 0x25f6
+  __TEXT.__cstring: 0xa06
   __TEXT.__swift5_capture: 0x338
-  __TEXT.__swift5_protos: 0x2c
-  __TEXT.__swift5_proto: 0x68
-  __TEXT.__swift5_types: 0x68
-  __TEXT.__unwind_info: 0xef8
-  __TEXT.__eh_frame: 0x1f38
+  __TEXT.__swift5_protos: 0x38
+  __TEXT.__swift5_proto: 0x88
+  __TEXT.__swift5_types: 0x78
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__unwind_info: 0xfa8
+  __TEXT.__eh_frame: 0x1f08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x68
-  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__const: 0x78
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x368
+  __DATA_CONST.__objc_selrefs: 0x378
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1028
-  __AUTH_CONST.__objc_const: 0x1bf0
-  __AUTH_CONST.__auth_got: 0x1748
+  __AUTH_CONST.__const: 0x1170
+  __AUTH_CONST.__objc_const: 0x1da0
+  __AUTH_CONST.__auth_got: 0x1760
   __AUTH.__objc_data: 0x168
-  __AUTH.__data: 0x1b0
-  __DATA.__data: 0x7c0
+  __AUTH.__data: 0x360
+  __DATA.__data: 0x800
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x768
-  __DATA_DIRTY.__data: 0x13c8
+  __DATA_DIRTY.__data: 0x13b8
   __DATA_DIRTY.__bss: 0x380
   __DATA_DIRTY.__common: 0xa8
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 912
-  Symbols:   624
-  CStrings:  227
+  Functions: 1007
+  Symbols:   656
+  CStrings:  234
 
Symbols:
+ _OBJC_CLASS_$_BSBuildVersion
+ __DATA__TtC14ReplicatorCore18SystemDataMigrator
+ __DATA__TtC14ReplicatorCore38SystemDataMigratorBuildVersionProvider
+ __IVARS__TtC14ReplicatorCore18SystemDataMigrator
+ __IVARS__TtC14ReplicatorCore38SystemDataMigratorBuildVersionProvider
+ __METACLASS_DATA__TtC14ReplicatorCore18SystemDataMigrator
+ __METACLASS_DATA__TtC14ReplicatorCore38SystemDataMigratorBuildVersionProvider
+ ___swift_memcpy8_8
+ _associated conformance 14ReplicatorCore18SystemDataMigratorC16MigrationReasonsVs10SetAlgebraAASQ
+ _associated conformance 14ReplicatorCore18SystemDataMigratorC16MigrationReasonsVs10SetAlgebraAAs25ExpressibleByArrayLiteral
+ _associated conformance 14ReplicatorCore18SystemDataMigratorC16MigrationReasonsVs9OptionSetAASY
+ _associated conformance 14ReplicatorCore18SystemDataMigratorC16MigrationReasonsVs9OptionSetAAs0I7Algebra
+ _free
+ _objc_msgSend$init
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$stringRepresentation
+ _swift_coroFrameAlloc
+ _symbolic $s14ReplicatorCore25SystemDataMigratorStoringP
+ _symbolic $s14ReplicatorCore28SystemDataMigratorPerformingP
+ _symbolic $s14ReplicatorCore39SystemDataMigratorBuildVersionProvidingP
+ _symbolic $sSY
+ _symbolic $ss10SetAlgebraP
+ _symbolic $ss25ExpressibleByArrayLiteralP
+ _symbolic $ss9OptionSetP
+ _symbolic _____ 14ReplicatorCore18SystemDataMigratorC
+ _symbolic _____ 14ReplicatorCore18SystemDataMigratorC16MigrationReasonsV
+ _symbolic _____ 14ReplicatorCore23SystemDataMigratorStoreV
+ _symbolic _____ 14ReplicatorCore27SystemDataMigratorPerformerV
+ _symbolic _____ 14ReplicatorCore38SystemDataMigratorBuildVersionProviderC
+ _symbolic ______p 14ReplicatorCore25SystemDataMigratorStoringP
+ _symbolic ______p 14ReplicatorCore28SystemDataMigratorPerformingP
+ _symbolic ______p 14ReplicatorCore39SystemDataMigratorBuildVersionProvidingP
+ _type_layout_string 14ReplicatorCore18SystemDataMigratorC16MigrationReasonsV
- _objc_msgSend$bundleID
- _symbolic _____ 14ReplicatorCore18SystemDataMigratorV
CStrings:
+ "Blocking on system data migration"
+ "Cached %{public}s and current %{public}s build versions do not match"
+ "Current build version is unknown"
+ "Last known build version is unknown"
+ "Stored and current build versions match %{public}s; bypassing migration check"
+ "Updating current build version from %{public}s to %{public}s"
+ "lastKnownBuildVersion"
```
