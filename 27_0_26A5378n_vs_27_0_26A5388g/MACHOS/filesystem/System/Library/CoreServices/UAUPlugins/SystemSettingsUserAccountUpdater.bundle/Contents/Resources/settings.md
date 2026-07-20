## settings

> `/System/Library/CoreServices/UAUPlugins/SystemSettingsUserAccountUpdater.bundle/Contents/Resources/settings`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-2027.0.3.0.0
-  __TEXT.__text: 0x1813c
-  __TEXT.__auth_stubs: 0xd50
+2027.0.6.400.0
+  __TEXT.__text: 0x1a194
+  __TEXT.__auth_stubs: 0xd90
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x1f88
-  __TEXT.__cstring: 0x1474
+  __TEXT.__const: 0x21f0
+  __TEXT.__cstring: 0x1654
   __TEXT.__objc_classname: 0x9
   __TEXT.__objc_methtype: 0x35
-  __TEXT.__swift5_typeref: 0x69a
-  __TEXT.__constg_swiftt: 0x408
-  __TEXT.__swift5_reflstr: 0x4e9
-  __TEXT.__swift5_fieldmd: 0x464
-  __TEXT.__swift5_proto: 0x1d0
-  __TEXT.__swift5_types: 0x74
-  __TEXT.__swift_as_entry: 0x3c
-  __TEXT.__swift_as_ret: 0x34
-  __TEXT.__swift_as_cont: 0x48
+  __TEXT.__swift5_typeref: 0x6f2
+  __TEXT.__constg_swiftt: 0x454
+  __TEXT.__swift5_reflstr: 0x5b9
+  __TEXT.__swift5_fieldmd: 0x4d8
+  __TEXT.__swift5_proto: 0x1f4
+  __TEXT.__swift5_types: 0x7c
+  __TEXT.__swift_as_entry: 0x44
+  __TEXT.__swift_as_ret: 0x3c
+  __TEXT.__swift_as_cont: 0x4c
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_methname: 0x131
-  __TEXT.__unwind_info: 0x750
-  __TEXT.__eh_frame: 0x944
-  __DATA_CONST.__const: 0xb10
+  __TEXT.__unwind_info: 0x7d8
+  __TEXT.__eh_frame: 0xa2c
+  __DATA_CONST.__const: 0xba0
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x6b0
-  __DATA_CONST.__got: 0x2d8
-  __DATA_CONST.__auth_ptr: 0x330
+  __DATA_CONST.__auth_got: 0x6d0
+  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__auth_ptr: 0x340
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x50
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0xb80
-  __DATA.__bss: 0x3a00
+  __DATA.__data: 0xc60
+  __DATA.__bss: 0x3e80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight

   - /System/Library/Frameworks/TabularData.framework/Versions/A/TabularData
   - /System/Library/PrivateFrameworks/ArgumentParserInternal.framework/Versions/A/ArgumentParserInternal
   - /System/Library/PrivateFrameworks/SettingsHost.framework/Versions/A/SettingsHost
+  - /System/Library/PrivateFrameworks/SettingsServices.framework/Versions/A/SettingsServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 544
-  Symbols:   420
-  CStrings:  119
+  Functions: 584
+  Symbols:   426
+  CStrings:  122
 
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
