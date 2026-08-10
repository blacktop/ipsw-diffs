## profiled

> `/usr/libexec/profiled`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__oslogstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2483.0.5.0.0
-  __TEXT.__text: 0xc88d8
+2483.2.6.0.0
+  __TEXT.__text: 0xc8fac
   __TEXT.__auth_stubs: 0x2910
-  __TEXT.__objc_stubs: 0x133e0
-  __TEXT.__objc_methlist: 0x625c
+  __TEXT.__objc_stubs: 0x13480
+  __TEXT.__objc_methlist: 0x6284
   __TEXT.__const: 0x137e
-  __TEXT.__gcc_except_tab: 0x1200
+  __TEXT.__gcc_except_tab: 0x1210
   __TEXT.__oslogstring: 0xfeb0
-  __TEXT.__cstring: 0xa8ba
-  __TEXT.__objc_methname: 0x16b43
+  __TEXT.__cstring: 0xa8ea
+  __TEXT.__objc_methname: 0x16c13
   __TEXT.__objc_classname: 0xbfe
-  __TEXT.__objc_methtype: 0x23f2
+  __TEXT.__objc_methtype: 0x2412
   __TEXT.__constg_swiftt: 0xe94
   __TEXT.__swift5_typeref: 0x804
   __TEXT.__swift5_reflstr: 0xee6

   __TEXT.__swift5_types: 0xb8
   __TEXT.__swift5_protos: 0x74
   __TEXT.__swift5_capture: 0x80
-  __TEXT.__unwind_info: 0x1b60
+  __TEXT.__unwind_info: 0x1b70
   __TEXT.__eh_frame: 0x190
-  __DATA_CONST.__const: 0x3020
-  __DATA_CONST.__cfstring: 0x86e0
+  __DATA_CONST.__const: 0x3048
+  __DATA_CONST.__cfstring: 0x86c0
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__auth_got: 0x1498
-  __DATA_CONST.__got: 0x2120
+  __DATA_CONST.__got: 0x2118
   __DATA_CONST.__auth_ptr: 0x300
-  __DATA.__objc_const: 0x70a8
-  __DATA.__objc_selrefs: 0x54b0
+  __DATA.__objc_const: 0x70b0
+  __DATA.__objc_selrefs: 0x54d8
   __DATA.__objc_ivar: 0x204
   __DATA.__objc_data: 0x1ea8
   __DATA.__data: 0x8f8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2735
-  Symbols:   1798
-  CStrings:  5758
+  Functions: 2741
+  Symbols:   1797
+  CStrings:  5764
 
Symbols:
- _MCFeatureDelayedSoftwareUpdatesForced
CStrings:
+ "-[MCProfileServiceServer areAppRatingsLockedDownOnlyByScreenTimeWithCompletion:]_block_invoke"
+ "ERROR_PROFILE_NONUNIQUE_IDENTIFIER_P_ID"
+ "Failed to apply restrictions. Error: %{public}s"
+ "_migrateValueRestrictions:withAppID:forKey:keysToRestrictions:currentValueUserSettings:"
+ "areAppRatingsLockedDownOnlyByScreenTime"
+ "areAppRatingsLockedDownOnlyByScreenTimeWithCompletion:"
+ "boolFeaturesWithPayloadRestictionKeyAlias"
+ "boolPayloadRestrictionKeysForFeature:"
+ "memberQueueCombinedProfileRestrictions"
+ "v24@0:8@?<v@?@\"NSNumber\"@\"NSError\">16"
- "ERROR_PROFILE_NONUNIQUE_UUID_P_ID"
- "Failed to apply restricitons. Error: %{public}s"
- "_migrateValueRestrictions:withAppID:forKey:keysToRestricitons:currentValueUserSettings:"
- "restriction_forceDelayedSoftwareUpdates"
```
