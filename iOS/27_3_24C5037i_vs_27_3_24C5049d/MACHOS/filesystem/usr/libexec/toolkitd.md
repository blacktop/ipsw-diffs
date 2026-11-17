## toolkitd

> `/usr/libexec/toolkitd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-5203.0.1.0.0
-  __TEXT.__text: 0x9c510
-  __TEXT.__auth_stubs: 0x2e80
-  __TEXT.__objc_stubs: 0x1a60
+5206.0.3.0.0
+  __TEXT.__text: 0x9ca68
+  __TEXT.__auth_stubs: 0x2eb0
+  __TEXT.__objc_stubs: 0x1a40
   __TEXT.__objc_methlist: 0x13c
-  __TEXT.__const: 0x47ac
+  __TEXT.__const: 0x478c
   __TEXT.__objc_classname: 0x17d
-  __TEXT.__objc_methname: 0x1338
+  __TEXT.__objc_methname: 0x1328
   __TEXT.__objc_methtype: 0x1fe
-  __TEXT.__constg_swiftt: 0xd38
+  __TEXT.__constg_swiftt: 0xd44
   __TEXT.__swift5_typeref: 0x1815
-  __TEXT.__swift5_reflstr: 0x10a4
-  __TEXT.__swift5_fieldmd: 0x10d8
+  __TEXT.__swift5_reflstr: 0x10b4
+  __TEXT.__swift5_fieldmd: 0x10e4
   __TEXT.__cstring: 0x223d
-  __TEXT.__oslogstring: 0x194c
+  __TEXT.__oslogstring: 0x19fc
   __TEXT.__swift5_capture: 0xd44
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_assocty: 0x330
   __TEXT.__swift5_proto: 0x1c4
   __TEXT.__swift5_types: 0x148
-  __TEXT.__swift_as_entry: 0x1dc
+  __TEXT.__swift_as_entry: 0x1d8
   __TEXT.__swift_as_cont: 0x414
-  __TEXT.__swift_as_ret: 0x228
+  __TEXT.__swift_as_ret: 0x224
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_mpenum: 0xc8
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__unwind_info: 0x2430
-  __TEXT.__eh_frame: 0x5ff8
-  __DATA_CONST.__const: 0x4350
+  __TEXT.__unwind_info: 0x2438
+  __TEXT.__eh_frame: 0x5f70
+  __DATA_CONST.__const: 0x42d0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__auth_got: 0x1748
+  __DATA_CONST.__auth_got: 0x1760
   __DATA_CONST.__got: 0xc30
   __DATA_CONST.__auth_ptr: 0x768
   __DATA.__objc_const: 0x780
-  __DATA.__objc_selrefs: 0x728
+  __DATA.__objc_selrefs: 0x720
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x1ce0
+  __DATA.__data: 0x1d78
   __DATA.__common: 0x2b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2998
-  Symbols:   1287
+  Functions: 2991
+  Symbols:   1290
   CStrings:  599
 
Symbols:
+ _$s11WorkflowKit04ToolB14IndexingPolicyC31shouldPreserveExistingFlowTools08existingiC5Count09generatedicL024removedContainersIsEmpty21hasIncompleteMetadataSbSi_SiS2btFZ
+ _$s7ToolKit0A8DatabaseC8AccessorC09localFlowA5CountSiyKF
+ _$sSo25LNActionParameterMetadataC11WorkflowKitE40dynamicOptionsProviderRestrictionContext14toolIdentifier12parameterKey5query06bundleL004ToolE00iJ0OSgSS_SSSo07LNQueryC0CSgSStF
CStrings:
+ "Preserving %ld existing FlowTool(s): this pass regenerated only %ld. Skipping destructive FlowTool replacement so a later reindex can regenerate once indexing is complete."
- "dynamicOptionsSupport"
```
