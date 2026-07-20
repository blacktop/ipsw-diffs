## HybridSearchRuntime

> `/System/Library/PrivateFrameworks/HybridSearchRuntime.framework/Versions/A/HybridSearchRuntime`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_types2`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-59.0.1.0.0
-  __TEXT.__text: 0x267294
-  __TEXT.__objc_methlist: 0x6b4
-  __TEXT.__const: 0xbec0
-  __TEXT.__constg_swiftt: 0x38d8
-  __TEXT.__swift5_typeref: 0x5c02
+62.1.0.0.0
+  __TEXT.__text: 0x284f7c
+  __TEXT.__objc_methlist: 0x6cc
+  __TEXT.__const: 0xbeb0
+  __TEXT.__constg_swiftt: 0x3908
+  __TEXT.__swift5_typeref: 0x5c66
   __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_reflstr: 0x2070
-  __TEXT.__swift5_fieldmd: 0x2b20
+  __TEXT.__swift5_reflstr: 0x2060
+  __TEXT.__swift5_fieldmd: 0x2b2c
   __TEXT.__swift5_assocty: 0xba0
-  __TEXT.__cstring: 0xe991
-  __TEXT.__swift5_capture: 0x3dd0
-  __TEXT.__oslogstring: 0x6eed
+  __TEXT.__cstring: 0xed11
+  __TEXT.__swift5_capture: 0x3e08
+  __TEXT.__oslogstring: 0x6ffd
   __TEXT.__swift5_mpenum: 0x40
   __TEXT.__swift5_proto: 0x5ec
-  __TEXT.__swift5_types: 0x454
-  __TEXT.__swift_as_entry: 0xe90
-  __TEXT.__swift_as_ret: 0x1478
-  __TEXT.__swift_as_cont: 0x2cdc
+  __TEXT.__swift5_types: 0x458
+  __TEXT.__swift_as_entry: 0xeac
+  __TEXT.__swift_as_ret: 0x1494
+  __TEXT.__swift_as_cont: 0x2d1c
   __TEXT.__swift5_protos: 0x7c
   __TEXT.__swift5_types2: 0x8
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__unwind_info: 0x9d60
-  __TEXT.__eh_frame: 0x1f138
+  __TEXT.__unwind_info: 0x9a00
+  __TEXT.__eh_frame: 0x20314
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x208
-  __DATA_CONST.__objc_classlist: 0xe8
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1458
+  __DATA_CONST.__objc_selrefs: 0x1480
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__got: 0x1ce8
+  __DATA_CONST.__got: 0x17c0
   __AUTH_CONST.__const: 0xd770
   __AUTH_CONST.__cfstring: 0x1a0
-  __AUTH_CONST.__objc_const: 0x2628
+  __AUTH_CONST.__objc_const: 0x2708
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x29c0
+  __AUTH_CONST.__auth_got: 0x2a28
   __AUTH.__objc_data: 0x1a0
-  __AUTH.__data: 0x1a38
-  __DATA.__data: 0x2920
+  __AUTH.__data: 0x1ae0
+  __DATA.__data: 0x2940
   __DATA.__bss: 0x5f20
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x2f0
-  __DATA_DIRTY.__data: 0x36b0
+  __DATA_DIRTY.__data: 0x36c0
   __DATA_DIRTY.__bss: 0x2900
   __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12273
-  Symbols:   323
-  CStrings:  954
+  Functions: 12874
+  Symbols:   325
+  CStrings:  973
 
Symbols:
+ _OBJC_CLASS_$_CCMailAddressForm
+ _swift_stdlib_random
CStrings:
+ " (id INT64 PRIMARY KEY, version UINT16);"
+ " AS entity_type,\n       n.payload AS payload,\n       n."
+ " AS provenance_vid"
+ ". Underlying error: "
+ "176308566_add_writing_assistant_profile_domain_identifier"
+ "ALTER TABLE Documents_general ADD draftMail_isJunk BOOL;"
+ "ALTER TABLE Documents_general ADD draftMail_isTrash BOOL;"
+ "ALTER TABLE Documents_general ADD mailAttachment_isJunk BOOL;"
+ "ALTER TABLE Documents_general ADD mailAttachment_isTrash BOOL;"
+ "ALTER TABLE Documents_general ADD remoteWritingAssistantProfile_domainIdentifier STRING;"
+ "ALTER TABLE Documents_general ADD writingAssistantProfile_domainIdentifier STRING;"
+ "CALL show_tables() WHERE name='_hybridindex_metadata' RETURN name;"
+ "CREATE (n:_hybridindex_metadata {id: 0, version: $version});"
+ "Failed to seed generation version, rolling back: %{public}@"
+ "Generation version missing from the index (e.g. read-only open); falling back to the UserDefaults value"
+ "IndexingServer.generationVersion"
+ "MATCH (n:_hybridindex_metadata {id: 0}) RETURN n.version;"
+ "Seeded generation version %{public}hu"
+ "_hybridindex_metadata"
+ "generationVersion"
+ "generationVersion: unexpected value "
+ "perform(text:checkSafety:safetyThreshold:embeddingModelProperties:contextLength:allowTruncation:sendAnalyticsEvent:)"
+ "readGenerationVersion: %{public}hu"
+ "readGenerationVersion: no version row present"
+ "readGenerationVersion: table is missing; no version seeded yet"
+ "readGenerationVersion: unexpected value %{public}s"
- " AS entity_type,\n       n.payload AS payload"
- "Bumped generation version to %{public}hu"
- "FTSRetokenizeTask"
- "HybridIndex incremental FTS retokenize succeeded."
- "Start HybridIndex incremental FTS retokenize."
- "com.apple.GenerativeSearch.PeriodicTasks.FTSRetokenizeTask"
- "perform(text:checkSafety:safetyThreshold:safetyBlockingDisabled:embeddingModelProperties:contextLength:allowTruncation:sendAnalyticsEvent:)"
```
