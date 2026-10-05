## linkd

> `/usr/libexec/linkd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-301.1.10.2.101
-  __TEXT.__text: 0xbf100
+301.1.15.0.0
+  __TEXT.__text: 0xbebc8
   __TEXT.__auth_stubs: 0x2a50
   __TEXT.__objc_stubs: 0x27a0
   __TEXT.__objc_methlist: 0xe0c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x5c76
-  __TEXT.__swift5_typeref: 0x2d9a
-  __TEXT.__swift5_fieldmd: 0x16d0
+  __TEXT.__const: 0x5c3c
   __TEXT.__constg_swiftt: 0x1d60
-  __TEXT.__objc_classname: 0x91e
-  __TEXT.__objc_methname: 0x3fbd
-  __TEXT.__objc_methtype: 0x1887
-  __TEXT.__swift5_reflstr: 0x12d7
+  __TEXT.__swift5_typeref: 0x2d9a
   __TEXT.__swift5_builtin: 0x1b8
+  __TEXT.__swift5_reflstr: 0x1325
+  __TEXT.__swift5_fieldmd: 0x16e8
   __TEXT.__swift5_assocty: 0x2a0
-  __TEXT.__swift5_protos: 0x68
   __TEXT.__swift5_proto: 0x34c
   __TEXT.__swift5_types: 0x1cc
-  __TEXT.__swift5_capture: 0x3148
-  __TEXT.__oslogstring: 0x4e23
-  __TEXT.__cstring: 0x1c15
-  __TEXT.__swift_as_entry: 0x590
-  __TEXT.__swift_as_ret: 0x55c
-  __TEXT.__swift_as_cont: 0x754
+  __TEXT.__objc_classname: 0x90c
+  __TEXT.__objc_methname: 0x3fcd
+  __TEXT.__objc_methtype: 0x188b
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x44a8
-  __TEXT.__eh_frame: 0xa330
-  __DATA_CONST.__const: 0xa070
+  __TEXT.__cstring: 0x1c80
+  __TEXT.__oslogstring: 0x4ef6
+  __TEXT.__swift5_capture: 0x2f30
+  __TEXT.__swift5_protos: 0x68
+  __TEXT.__swift_as_entry: 0x594
+  __TEXT.__swift_as_ret: 0x560
+  __TEXT.__swift_as_cont: 0x758
+  __TEXT.__unwind_info: 0x44c0
+  __TEXT.__eh_frame: 0xa378
+  __DATA_CONST.__const: 0x9b20
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__auth_got: 0x1530
   __DATA_CONST.__got: 0xa78
-  __DATA_CONST.__auth_ptr: 0x13d8
+  __DATA_CONST.__auth_ptr: 0x1420
   __DATA.__objc_const: 0x22a8
   __DATA.__objc_selrefs: 0xe30
   __DATA.__objc_data: 0x8e8
-  __DATA.__data: 0x3b58
+  __DATA.__data: 0x3b90
   __DATA.__common: 0x320
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5602
-  Symbols:   1198
-  CStrings:  1232
+  Functions: 5593
+  Symbols:   1199
+  CStrings:  1235
 
Symbols:
+ _$s15AppIntentsIndex08MetadataC0V020processedBundlesWithA9ShortcutsSaySSGyKF
+ _$s15AppIntentsIndex08MetadataC0V23appShortcutsUnprocessed3forSbSS_tKF
- _$s15AppIntentsIndex08MetadataC0V21appShortcutsProcessedySbSSKF
CStrings:
+ "AppShortcuts for %{public}s does not need processing, unblocking"
+ "Emitting adoption summary: indexedBundles=%ld appShortcutBundles=%ld thirdPartyIndexedBundles=%ld thirdPartyAppShortcutBundles=%ld"
+ "EntitlementAudit: %{public}s (pid %{public}d) lacks both %{public}s and %{public}s, would be REJECTED (enforcement off)"
+ "thirdPartyAppShortcutBundleCount"
+ "thirdPartyIndexedBundleCount"
- "AppShortcuts for %{public}s appear processed, unblocking"
- "Emitting adoption summary: indexedBundles=%ld appShortcutBundles=%ld"
```
