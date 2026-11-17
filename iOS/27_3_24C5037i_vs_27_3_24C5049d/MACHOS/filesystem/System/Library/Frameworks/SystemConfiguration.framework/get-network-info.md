## get-network-info

> `/System/Library/Frameworks/SystemConfiguration.framework/get-network-info`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-1453.60.5.0.0
-  __TEXT.__text: 0x14c4c
-  __TEXT.__auth_stubs: 0x11d0
-  __TEXT.__objc_stubs: 0x1a0
+1453.60.7.0.0
+  __TEXT.__text: 0x160e4
+  __TEXT.__auth_stubs: 0x12f0
+  __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x688
+  __TEXT.__const: 0x6a2
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x33f
+  __TEXT.__swift5_typeref: 0x353
   __TEXT.__constg_swiftt: 0x168
-  __TEXT.__swift5_reflstr: 0x2c2
+  __TEXT.__swift5_reflstr: 0x2b2
   __TEXT.__swift5_fieldmd: 0x1bc
-  __TEXT.__cstring: 0x1af3
+  __TEXT.__cstring: 0x1e13
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x18
   __TEXT.__objc_classname: 0xef
-  __TEXT.__objc_methname: 0x446
+  __TEXT.__objc_methname: 0x426
   __TEXT.__objc_methtype: 0xb4
   __TEXT.__swift5_capture: 0x128
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x3b8
-  __TEXT.__eh_frame: 0x250
-  __DATA_CONST.__const: 0xc78
+  __TEXT.__unwind_info: 0x3e8
+  __TEXT.__eh_frame: 0x2b0
+  __DATA_CONST.__const: 0xcb8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__auth_got: 0x8f0
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__auth_ptr: 0x278
+  __DATA_CONST.__auth_got: 0x980
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__auth_ptr: 0x280
   __DATA.__objc_const: 0x460
-  __DATA.__objc_selrefs: 0x108
+  __DATA.__objc_selrefs: 0xf8
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x840
+  __DATA.__data: 0x850
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 222
-  Symbols:   448
-  CStrings:  238
+  Functions: 231
+  Symbols:   466
+  CStrings:  255
 
Symbols:
+ _$s6Darwin5errnos5Int32Vvs
+ _$s6Darwin7S_IFLNKs6UInt16Vvg
+ _$s6Darwin7S_IWGRPs6UInt16Vvg
+ _$sSS5index5afterSS5IndexVAD_tF
+ _$sSSySJSS5IndexVcig
+ _$sSy10FoundationE8containsySbqd__SyRd__lF
+ _$ss18_DictionaryStorageC4copy8originalAByxq_Gs05__RawaB0C_tFZ
+ _$ss18_DictionaryStorageC6resize8original8capacity4moveAByxq_Gs05__RawaB0C_SiSbtFZ
+ _$ss18_DictionaryStorageC8allocate8capacityAByxq_GSi_tFZ
+ _$ss18_DictionaryStorageCMn
+ _$ss4Int8VN
+ _$ss53KEY_TYPE_OF_DICTIONARY_VIOLATES_HASHABLE_REQUIREMENTSys5NeverOypXpF
+ __swiftEmptyDictionarySingleton
+ _closedir
+ _confstr
+ _dup
+ _fdopendir
+ _fstatat
+ _fstatfs
+ _mkdtemp
+ _objc_release_x26
+ _objc_retain_x26
+ _objc_retain_x27
+ _readdir
+ _readlinkat
+ _swift_release_x1
+ _swift_retain_n
+ _swift_retain_x25
+ _swift_retain_x27
- _$s10Foundation25NSFastEnumerationIteratorV4nextypSgyF
- _$s10Foundation25NSFastEnumerationIteratorVMa
- _$sSo12NSEnumeratorC10FoundationE12makeIteratorAC017NSFastEnumerationD0VyF
- _$ss11_SetStorageC8allocate8capacityAByxGSi_tFZ
- _$ss6UInt64VN
- _NSFileSize
- _OBJC_CLASS_$_NSByteCountFormatter
- _lstat
- _objc_release_x27
- _swift_release_x12
- _swift_release_x9
CStrings:
+ "' failed revalidation"
+ "' is not a safe single-owner directory"
+ "' whose identity changed"
+ "' with unexpected owner or link count"
+ "' with unexpected owner or writable mode"
+ "': exceeds remaining snapshot budget"
+ "/"
+ "/var/run/racoon/"
+ "Reached the network snapshot byte budget; skipping remaining items"
+ "confstr(_CS_DARWIN_USER_TEMP_DIR) failed: "
+ "copyTree fdopendir '"
+ "copyTree fstatat '"
+ "copyTree openat destination '"
+ "copyTree openat source '"
+ "copyTree openat source file '"
+ "copyTree readdir '"
+ "copyTree refusing source directory '"
+ "copyTree refusing source file '"
+ "copyTree skipping '"
+ "copyTree source directory '"
+ "couldn't create a private directory for packet captures"
+ "couldn't read the private packet-capture directory"
+ "failed creating private capture directory: "
+ "failed to stat directory '"
+ "get-network-info-pcap.XXXXXX"
+ "openOutputFiles"
+ "refusing group- or world-writable output directory '"
+ "refusing to read untracked output file '"
+ "removeItemAtPath:error:"
- " snapshot droptappcap"
- " snapshot sysdiagpcap"
- "': would exceed 4MB limit (current: "
- "Network snapshots collection complete: "
- "copyTree lstat '"
- "copyTree openat '"
- "createdOutputPaths"
- "enumeratorAtPath:"
- "failed reading output file '"
- "refusing world-writable output directory '"
- "setCountStyle:"
- "stringFromByteCount:"
```
