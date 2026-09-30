## ManagedSettingsAgent

> `/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent`

```diff

-242.4.6.0.0
-  __TEXT.__text: 0x5c2a0
-  __TEXT.__auth_stubs: 0x1aa0
+242.4.8.0.0
+  __TEXT.__text: 0x5d304
+  __TEXT.__auth_stubs: 0x1af0
   __TEXT.__objc_stubs: 0x20
   __TEXT.__objc_methlist: 0x598
   __TEXT.__const: 0x144c
   __TEXT.__objc_classname: 0x121
-  __TEXT.__objc_methname: 0xf00
+  __TEXT.__objc_methname: 0xee5
   __TEXT.__objc_methtype: 0x194
   __TEXT.__cstring: 0x18c5
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xcc0
-  __TEXT.__swift5_typeref: 0xf7f
+  __TEXT.__constg_swiftt: 0xcc8
+  __TEXT.__swift5_typeref: 0xf8d
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x77d
   __TEXT.__swift5_fieldmd: 0x738
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_proto: 0x108
   __TEXT.__swift5_types: 0x80
-  __TEXT.__oslogstring: 0x2352
+  __TEXT.__oslogstring: 0x23e2
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_capture: 0x34c
-  __TEXT.__unwind_info: 0xb00
+  __TEXT.__unwind_info: 0xb18
   __TEXT.__eh_frame: 0x1838
-  __DATA_CONST.__auth_got: 0xd58
-  __DATA_CONST.__got: 0x428
-  __DATA_CONST.__auth_ptr: 0x3f8
+  __DATA_CONST.__auth_got: 0xd80
+  __DATA_CONST.__got: 0x458
+  __DATA_CONST.__auth_ptr: 0x3a8
   __DATA_CONST.__const: 0x1908
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA.__objc_const: 0x16f0
-  __DATA.__objc_selrefs: 0x3b0
+  __DATA.__objc_selrefs: 0x3a8
   __DATA.__objc_data: 0x2c8
-  __DATA.__data: 0x18d0
+  __DATA.__data: 0x18e8
   __DATA.__bss: 0x1990
   __DATA.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 948
-  Symbols:   663
-  CStrings:  454
+  Functions: 951
+  Symbols:   671
+  CStrings:  455
 
Symbols:
+ _$s15ManagedSettings010WebContentB0V12FilterPolicyOSQAAMc
+ _$s15ManagedSettings010WebContentB0V15blockedByFilterAA15SettingMetadataVyAC0G6PolicyOGvgZ
+ _$s15ManagedSettings06SafariB0V19denyHistoryClearingAA15SettingMetadataVySbGvgZ
+ _$s15ManagedSettings06SafariB0V19denyPrivateBrowsingAA15SettingMetadataVySbGvgZ
+ _$s15ManagedSettings11PersistenceC013readEffectiveB04fromSDySSSo8NSObjectCG10Foundation3URLV_tKFZ
+ _$s15ManagedSettings11PersistenceC07readRawB04fromSDySSSo8NSObjectCG10Foundation3URLV_tKFZ
+ _$s15ManagedSettings11PersistenceC08writeRawB0_2toySDySSSo8NSObjectCG_10Foundation3URLVtKFZ
+ _$s15ManagedSettings11PersistenceC09readLocalB04fromSDySSSo8NSObjectCG10Foundation3URLV_tKFZ
+ _$s15ManagedSettings11PersistenceC7rawData4from10Foundation0E0VSgAF3URLV_tKFZ
+ _objc_release_x9
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _$s15ManagedSettings11PersistenceC4data4from10Foundation4DataVSgAF3URLV_tKFZ
- _$s15ManagedSettings11PersistenceC4read4fromSDySSSo8NSObjectCG10Foundation3URLV_tKFZ
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initializeBufferWithCopyOfBuffer
CStrings:
+ "Failed to read effective settings from %{public}s: %{public}s"
+ "Failed to read local settings from %{public}s: %{public}s"
+ "Skipping effective settings from %{public}s because the file does not exist"
+ "Skipping local settings from %{public}s because the file does not exist"
- "Failed to read settings from %{public}s: %{public}s"
- "Skipping settings from %{public}s because the file does not exist"
- "copyItemAtURL:toURL:error:"

```
