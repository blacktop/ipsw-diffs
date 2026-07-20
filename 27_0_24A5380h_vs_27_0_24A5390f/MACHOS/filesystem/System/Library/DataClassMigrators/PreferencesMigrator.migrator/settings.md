## settings

> `/System/Library/DataClassMigrators/PreferencesMigrator.migrator/settings`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_entry`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-2027.0.3.100.0
-  __TEXT.__text: 0x154d8
-  __TEXT.__auth_stubs: 0xcf0
+2027.0.6.101.0
+  __TEXT.__text: 0x17524
+  __TEXT.__auth_stubs: 0xd30
   __TEXT.__objc_stubs: 0x60
-  __TEXT.__const: 0x1d20
+  __TEXT.__const: 0x1f70
   __TEXT.__objc_classname: 0x9
-  __TEXT.__swift5_typeref: 0x604
-  __TEXT.__constg_swiftt: 0x3a0
-  __TEXT.__swift5_reflstr: 0x499
-  __TEXT.__swift5_fieldmd: 0x3d4
-  __TEXT.__cstring: 0x1344
-  __TEXT.__swift5_proto: 0x1ac
-  __TEXT.__swift5_types: 0x68
-  __TEXT.__swift_as_entry: 0x3c
-  __TEXT.__swift_as_ret: 0x34
-  __TEXT.__swift_as_cont: 0x48
+  __TEXT.__swift5_typeref: 0x65c
+  __TEXT.__constg_swiftt: 0x3ec
+  __TEXT.__swift5_reflstr: 0x569
+  __TEXT.__swift5_fieldmd: 0x448
+  __TEXT.__cstring: 0x1524
+  __TEXT.__swift5_proto: 0x1d0
+  __TEXT.__swift5_types: 0x70
+  __TEXT.__swift_as_entry: 0x44
+  __TEXT.__swift_as_ret: 0x3c
+  __TEXT.__swift_as_cont: 0x4c
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__objc_methtype: 0x15
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_methname: 0x6f
-  __TEXT.__unwind_info: 0x6a0
-  __TEXT.__eh_frame: 0x864
-  __DATA_CONST.__const: 0xaa0
+  __TEXT.__unwind_info: 0x728
+  __TEXT.__eh_frame: 0x94c
+  __DATA_CONST.__const: 0xb30
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x680
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__auth_ptr: 0x318
+  __DATA_CONST.__auth_got: 0x6a0
+  __DATA_CONST.__got: 0x2a0
+  __DATA_CONST.__auth_ptr: 0x328
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x18
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0xa60
-  __DATA.__bss: 0x3580
+  __DATA.__data: 0xb40
+  __DATA.__bss: 0x3a00
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal
   - /System/Library/PrivateFrameworks/SettingsHost.framework/SettingsHost
+  - /System/Library/PrivateFrameworks/SettingsServices.framework/SettingsServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 489
-  Symbols:   403
-  CStrings:  107
+  Functions: 529
+  Symbols:   409
+  CStrings:  110
 
Symbols:
+ _$s16SettingsServices0A19SearchIndexerClientC14requestReindex3forySayAC0G13DomainRequestVG_tYaKFZ
+ _$s16SettingsServices0A19SearchIndexerClientC14requestReindex3forySayAC0G13DomainRequestVG_tYaKFZTu
+ _$s16SettingsServices0A19SearchIndexerClientC20ReindexDomainRequestV20openIntentIdentifier08appValueK0017attributionBundleK004hostoK0AESS_S3StcfC
+ _$s16SettingsServices0A19SearchIndexerClientC20ReindexDomainRequestVMa
+ _$s16SettingsServices0A19SearchIndexerClientC20ReindexDomainRequestVMn
+ _$s16SettingsServices0A19SearchIndexerClientCMa
CStrings:
+ "No value provided for `-attribution-bundle-identifiers`."
+ "Request a reindex of a specific `OpenIntent`/target domain via the `SettingsSearchIndexerClient` API in `SettingsServices`."
+ "Unlike `reindex`, which performs the indexing operation directly via `SettingsHost`, this command calls into `SettingsServices` to *request* that the host Settings application reindex the specified domain(s). One request is issued per provided attribution bundle identifier."
```
