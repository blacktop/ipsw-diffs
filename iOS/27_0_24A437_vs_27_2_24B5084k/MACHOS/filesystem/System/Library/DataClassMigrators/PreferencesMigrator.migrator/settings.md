## settings

> `/System/Library/DataClassMigrators/PreferencesMigrator.migrator/settings`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-2027.0.10.401.0
-  __TEXT.__text: 0x16888
-  __TEXT.__auth_stubs: 0xd30
+2027.1.4.0.0
+  __TEXT.__text: 0x19ce4
+  __TEXT.__auth_stubs: 0xe60
   __TEXT.__objc_stubs: 0x60
-  __TEXT.__const: 0x1f70
+  __TEXT.__const: 0x21e0
   __TEXT.__objc_classname: 0x9
-  __TEXT.__swift5_typeref: 0x65c
-  __TEXT.__constg_swiftt: 0x3ec
-  __TEXT.__swift5_reflstr: 0x569
-  __TEXT.__swift5_fieldmd: 0x448
-  __TEXT.__cstring: 0x1524
-  __TEXT.__swift5_proto: 0x1d0
-  __TEXT.__swift5_types: 0x70
-  __TEXT.__swift_as_entry: 0x44
-  __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__swift_as_cont: 0x4c
+  __TEXT.__swift5_typeref: 0x6e2
+  __TEXT.__constg_swiftt: 0x438
+  __TEXT.__swift5_reflstr: 0x589
+  __TEXT.__swift5_fieldmd: 0x480
+  __TEXT.__cstring: 0x15a4
+  __TEXT.__swift5_proto: 0x1f4
+  __TEXT.__swift5_types: 0x78
+  __TEXT.__swift_as_entry: 0x4c
+  __TEXT.__swift_as_ret: 0x44
+  __TEXT.__swift_as_cont: 0x58
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__objc_methtype: 0x15
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_methname: 0x6f
-  __TEXT.__unwind_info: 0x880
-  __TEXT.__eh_frame: 0x94c
-  __DATA_CONST.__const: 0xb30
+  __TEXT.__unwind_info: 0x960
+  __TEXT.__eh_frame: 0xb44
+  __DATA_CONST.__const: 0xbc0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x6a0
-  __DATA_CONST.__got: 0x2a0
-  __DATA_CONST.__auth_ptr: 0x328
+  __DATA_CONST.__auth_got: 0x738
+  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__auth_ptr: 0x348
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x18
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0xb40
+  __DATA.__data: 0xc48
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 529
-  Symbols:   409
-  CStrings:  110
+  Functions: 576
+  Symbols:   433
+  CStrings:  111
 
Symbols:
+ _$s10Foundation11JSONEncoderC16OutputFormattingV10sortedKeysAEvgZ
+ _$s10Foundation11JSONEncoderC16OutputFormattingV13prettyPrintedAEvgZ
+ _$s10Foundation11JSONEncoderC16OutputFormattingVMa
+ _$s10Foundation11JSONEncoderC16OutputFormattingVMn
+ _$s10Foundation11JSONEncoderC16OutputFormattingVs10SetAlgebraAAMc
+ _$s10Foundation11JSONEncoderC16outputFormattingAC06OutputD0VvsTj
+ _$s10Foundation13__DataStorageC6_bytesSvSgvg
+ _$s10Foundation13__DataStorageC7_lengthSivg
+ _$s10Foundation13__DataStorageC7_offsetSivg
+ _$s10Foundation4DataV13_copyContents12initializingAC8IteratorV_SitSrys5UInt8VG_tF
+ _$s10Foundation4DataV8IteratorVMa
+ _$s10Foundation4DataVN
+ _$s12SettingsHost0A16SearchResultItemV16uniqueIdentifierSSvg
+ _$sSS18_fromUTF8RepairingySS6result_Sb11repairsMadetSRys5UInt8VGFZ
+ _$sSo11CSUserQueryC12SettingsHostE08allItemsB02inABSaySSG_tFZ
+ _$ss10SetAlgebraPyxqd__ncSTRd__7ElementQyd__ACRtzlufCTj
+ _$ss15ContiguousArrayV28_allocateBufferUninitialized15minimumCapacitys01_abD0VyxGSi_tFZ
+ _$ss19_HasContiguousBytesMp
+ _$ss19_HasContiguousBytesP010withUnsafeC0yqd__qd__SWKXEKlFTj
+ _$ss19_HasContiguousBytesP09_providesbC6NoCopySbvgTj
+ _$ss22_minimumMergeRunLengthyS2iF
+ _$ss5UInt8VMn
+ _memcpy
+ _swift_dynamicCast
CStrings:
+ "Dump the entire search index of a given Settings application as a stable, sorted JSON array (for diffing two builds)."
```
