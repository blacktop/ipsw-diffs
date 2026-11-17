## FamilyControlsAgent

> `/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_data`

```diff

-1248.0.0.0.0
-  __TEXT.__text: 0x57eb0
-  __TEXT.__auth_stubs: 0x2250
-  __TEXT.__objc_stubs: 0x16e0
-  __TEXT.__objc_methlist: 0x7ac
-  __TEXT.__const: 0x1cf8
-  __TEXT.__oslogstring: 0x355b
-  __TEXT.__cstring: 0x9d6
+1250.2.1.0.0
+  __TEXT.__text: 0x5c794
+  __TEXT.__auth_stubs: 0x2300
+  __TEXT.__objc_stubs: 0x17a0
+  __TEXT.__objc_methlist: 0x7c4
+  __TEXT.__const: 0x1e60
+  __TEXT.__oslogstring: 0x38cb
+  __TEXT.__cstring: 0x9f6
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xc54
-  __TEXT.__swift5_typeref: 0x119c
+  __TEXT.__constg_swiftt: 0xccc
+  __TEXT.__swift5_typeref: 0x126e
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_reflstr: 0x502
-  __TEXT.__swift5_fieldmd: 0x644
+  __TEXT.__swift5_fieldmd: 0x674
   __TEXT.__swift5_assocty: 0x150
-  __TEXT.__swift5_proto: 0xf8
+  __TEXT.__swift5_proto: 0x104
   __TEXT.__swift5_types: 0x6c
   __TEXT.__objc_classname: 0x46c
-  __TEXT.__objc_methname: 0x231d
-  __TEXT.__swift5_capture: 0xb20
-  __TEXT.__objc_methtype: 0x1073
-  __TEXT.__swift5_protos: 0x50
+  __TEXT.__objc_methname: 0x23f5
+  __TEXT.__swift5_capture: 0xb80
+  __TEXT.__objc_methtype: 0x10c3
+  __TEXT.__swift5_protos: 0x5c
+  __TEXT.__swift_as_entry: 0x3c
+  __TEXT.__swift_as_ret: 0x38
+  __TEXT.__swift_as_cont: 0x44
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift_as_entry: 0x2c
-  __TEXT.__swift_as_ret: 0x24
-  __TEXT.__swift_as_cont: 0x14
-  __TEXT.__unwind_info: 0xf08
-  __TEXT.__eh_frame: 0x9f8
-  __DATA_CONST.__const: 0x2540
+  __TEXT.__unwind_info: 0x1000
+  __TEXT.__eh_frame: 0xd50
+  __DATA_CONST.__const: 0x2678
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__auth_got: 0x1130
-  __DATA_CONST.__got: 0x6f0
-  __DATA_CONST.__auth_ptr: 0x568
-  __DATA.__objc_const: 0x28c0
-  __DATA.__objc_selrefs: 0x898
+  __DATA_CONST.__auth_got: 0x1188
+  __DATA_CONST.__got: 0x700
+  __DATA_CONST.__auth_ptr: 0x588
+  __DATA.__objc_const: 0x28c8
+  __DATA.__objc_selrefs: 0x8d0
   __DATA.__objc_data: 0x730
-  __DATA.__data: 0x1210
+  __DATA.__data: 0x1220
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1169
-  Symbols:   904
-  CStrings:  742
+  Functions: 1214
+  Symbols:   919
+  CStrings:  762
 
Symbols:
+ _$s15ManagedSettings0aB9InterfaceC14migrateAppData4from2to17completionHandlerySS_SSys5Error_pSgctFTj
+ _$s15ManagedSettings0aB9InterfaceC6sharedACvgZ
+ _$s15ManagedSettings0aB9InterfaceCMa
+ _$s15ManagedSettings0aB9InterfaceCMn
+ _$sScA15unownedExecutorScevgTj
+ _$sScC12continuation8functionScCyxq_GSccyxq_G_SStcfC
+ _$sScC6resume8throwingyq_n_tF
+ _$sScC6resume9returningyxn_tF
+ _$ss5ErrorWS
+ _OBJC_CLASS_$_USAppDataMigrator
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_deletedAsyncMethodErrorTu
CStrings:
+ "Failed to find the installed application %{public}s: %{public}s"
+ "Failed to migrate Family Controls data from %{public}s to %{public}s: %{public}s"
+ "Failed to migrate ManagedSettings data from %{public}s to %{public}s: %{public}s"
+ "Failed to migrate UsageTracking data from %{public}s to %{public}s: %{public}s"
+ "Failed to revoke child authorization for %{public}s after migrating its data: %{public}s"
+ "Migrating app data from %{public}s to %{public}s"
+ "Not migrating authorization from %{public}s because it isn't authorized"
+ "Not migrating authorization to %{public}s because it already has its own"
+ "Not migrating authorization to %{public}s because it doesn't have a Family Controls entitlement"
+ "Skipping app data migration because %{public}s isn't authorized"
+ "The installed application %{public}s has no team identifier"
+ "boolValue"
+ "entitlements"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "migrateAppData(from:to:)"
+ "migrateAppDataFromBundleIdentifier:toBundleIdentifier:completionHandler:"
+ "migrateAppDataFromBundleIdentifier:toBundleIdentifier:replyHandler:"
+ "objectForKey:ofClass:"
+ "teamIdentifier"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
```
