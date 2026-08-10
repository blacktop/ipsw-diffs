## migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-1426.0.0.0.0
-  __TEXT.__text: 0x18838
-  __TEXT.__auth_stubs: 0x1000
+1428.0.3.0.0
+  __TEXT.__text: 0x18cac
+  __TEXT.__auth_stubs: 0x1060
   __TEXT.__objc_stubs: 0x3e0
   __TEXT.__objc_methlist: 0x38c
   __TEXT.__cstring: 0x34c
   __TEXT.__swift5_entry: 0x8
   __TEXT.__oslogstring: 0x704
-  __TEXT.__const: 0x5da
+  __TEXT.__const: 0x5ea
   __TEXT.__constg_swiftt: 0x1c0
-  __TEXT.__swift5_typeref: 0x44f
+  __TEXT.__swift5_typeref: 0x457
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x107
-  __TEXT.__swift5_fieldmd: 0x148
+  __TEXT.__swift5_reflstr: 0x129
+  __TEXT.__swift5_fieldmd: 0x154
   __TEXT.__swift5_types: 0x10
   __TEXT.__objc_classname: 0xb0
-  __TEXT.__objc_methtype: 0x43a
-  __TEXT.__objc_methname: 0x94b
+  __TEXT.__objc_methtype: 0x46a
+  __TEXT.__objc_methname: 0x93d
   __TEXT.__swift5_capture: 0x3c8
   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0x90

   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__auth_got: 0x808
-  __DATA_CONST.__got: 0x390
-  __DATA_CONST.__auth_ptr: 0x188
-  __DATA.__objc_const: 0x600
+  __DATA_CONST.__auth_got: 0x838
+  __DATA_CONST.__got: 0x3a0
+  __DATA_CONST.__auth_ptr: 0x190
+  __DATA.__objc_const: 0x620
   __DATA.__objc_selrefs: 0x240
   __DATA.__objc_data: 0xc8
-  __DATA.__data: 0x490
+  __DATA.__data: 0x4a0
   __DATA.__bss: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 414
-  Symbols:   434
-  CStrings:  209
+  Symbols:   443
+  CStrings:  210
 
Symbols:
+ _$s12MigrationKit17OriginatingUIFlowO5setupyA2CmFWC
+ _$s12MigrationKit17OriginatingUIFlowO7unknownyA2CmFWC
+ _$s12MigrationKit17OriginatingUIFlowO8rawValueACSgSi_tcfC
+ _$s12MigrationKit17OriginatingUIFlowOMa
+ _$s12MigrationKit17OriginatingUIFlowOMn
+ _$s12MigrationKit6ClientC17originatingUIFlowAA011OriginatingE0OvsTj
+ _$s12MigrationKit6SchemeO2eeoiySbAC_ACtFZ
+ _$s12MigrationKit6ServerC17originatingUIFlowAA011OriginatingE0OvsTj
+ _swift_retain_x24
Functions:
~ sub_100004204 : 288 -> 308
~ sub_100004658 -> sub_10000466c : 120 -> 128
~ sub_100004b60 -> sub_100004b7c : 2088 -> 2096
~ sub_10000bfac -> sub_10000bfd0 : 404 -> 552
~ sub_10000c3f4 -> sub_10000c4ac : 636 -> 872
~ sub_10000c670 -> sub_10000c814 : 404 -> 576
~ sub_10000cab8 -> sub_10000cd08 : 636 -> 1172
~ sub_100016364 -> sub_1000167cc : 660 -> 672
CStrings:
+ "_originatingUIFlow"
+ "runWithClient:scheme:originatingUIFlow:"
+ "v32@0:8@\"<_TtP12MigrationKit9XPCClient_>\"16C24C28"
+ "v32@0:8@16C24C28"
- "runWithClient:scheme:"
- "v28@0:8@\"<_TtP12MigrationKit9XPCClient_>\"16C24"
- "v28@0:8@16C24"
```
