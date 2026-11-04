## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-655.1.14.1.0
-  __TEXT.__text: 0x1011f4
-  __TEXT.__objc_methlist: 0xa4c0
-  __TEXT.__const: 0x3618
+655.2.7.0.0
+  __TEXT.__text: 0x105358
+  __TEXT.__objc_methlist: 0xa4f0
+  __TEXT.__const: 0x3668
   __TEXT.__cstring: 0xaa2c
-  __TEXT.__oslogstring: 0xc82a
-  __TEXT.__gcc_except_tab: 0x1bb0
-  __TEXT.__constg_swiftt: 0xe30
-  __TEXT.__swift5_typeref: 0x175e
+  __TEXT.__oslogstring: 0xccba
+  __TEXT.__gcc_except_tab: 0x1bf4
+  __TEXT.__constg_swiftt: 0xe68
+  __TEXT.__swift5_typeref: 0x17e6
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x7fe
-  __TEXT.__swift5_fieldmd: 0xa44
+  __TEXT.__swift5_reflstr: 0x85e
+  __TEXT.__swift5_fieldmd: 0xa84
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_proto: 0x214
-  __TEXT.__swift5_types: 0xfc
-  __TEXT.__swift5_capture: 0xc28
+  __TEXT.__swift5_types: 0x100
+  __TEXT.__swift5_capture: 0xc4c
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift_as_entry: 0x198
-  __TEXT.__swift_as_ret: 0x1d4
-  __TEXT.__swift_as_cont: 0x284
+  __TEXT.__swift_as_entry: 0x19c
+  __TEXT.__swift_as_ret: 0x1dc
+  __TEXT.__swift_as_cont: 0x288
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x5658
-  __TEXT.__eh_frame: 0x4aac
+  __TEXT.__unwind_info: 0x56e0
+  __TEXT.__eh_frame: 0x4d04
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5548
+  __DATA_CONST.__objc_selrefs: 0x5570
   __DATA_CONST.__objc_protorefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x260
-  __DATA_CONST.__got: 0xf00
-  __AUTH_CONST.__const: 0x39c0
+  __DATA_CONST.__got: 0xf20
+  __AUTH_CONST.__const: 0x3ac8
   __AUTH_CONST.__cfstring: 0x9aa0
-  __AUTH_CONST.__objc_const: 0x13660
+  __AUTH_CONST.__objc_const: 0x136d0
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x1410
+  __AUTH_CONST.__auth_got: 0x1418
   __AUTH.__objc_data: 0x32b8
   __AUTH.__data: 0x508
-  __DATA.__objc_ivar: 0x7e4
-  __DATA.__data: 0x2360
+  __DATA.__objc_ivar: 0x7f0
+  __DATA.__data: 0x2370
   __DATA.__common: 0xe8
   __DATA_DIRTY.__objc_data: 0x1f40
   __DATA_DIRTY.__data: 0x2c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6155
-  Symbols:   6907
-  CStrings:  2310
+  Functions: 6189
+  Symbols:   6925
+  CStrings:  2324
 
Symbols:
+ -[STConversation _applyManagingGuardianAppleIDs:generation:]
+ -[STConversation _managingGuardiansMayHaveChanged]
+ -[STConversation _nextManagingGuardiansFetchGeneration]
+ -[STConversation familyNotifyToken]
+ GCC_except_table52
+ GCC_except_table57
+ GCC_except_table71
+ GCC_except_table72
+ _FAFamilyUpdateNotification
+ _OBJC_IVAR_$_STConversation._appliedManagingGuardiansFetchGeneration
+ _OBJC_IVAR_$_STConversation._familyNotifyToken
+ _OBJC_IVAR_$_STConversation._managingGuardiansFetchGeneration
+ ___50-[STConversation _managingGuardiansMayHaveChanged]_block_invoke
+ ___73-[STConversation _stConversationCommonInitSetupObservationOfStateChanges]_block_invoke_3
+ ___block_descriptor_48_e8_32s_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___swift_closure_destructor.20Tm
+ ___swift_memcpy48_8
+ _symbolic SSSo9STAppInfoCSgIeggo_
+ _symbolic So10CTCategoryCSg
+ _symbolic So17STAppDataMigratorC
+ _symbolic So8NSStringCSo9STAppInfoCSgIeyBya_
+ _symbolic _____ So17STAppDataMigratorC14ScreenTimeCoreE12MigratingApp33_4577F3EA85A9A211B1933E19220B9859LLV
+ _symbolic _____ySo14STAppExceptionCG s11_SetStorageC
+ _type_layout_string So17STAppDataMigratorC14ScreenTimeCoreE12MigratingApp33_4577F3EA85A9A211B1933E19220B9859LLV
- GCC_except_table40
- GCC_except_table50
- GCC_except_table66
- ___block_descriptor_40_e8_32s_e29_v24?0"NSArray"8"NSError"16ls32l8
- ___swift_closure_destructor.19Tm
- _swift_retain_x28
CStrings:
+ "Added %{public}s to always allowed apps for app data migration"
+ "Added app exception for %{public}s for app data migration"
+ "Could not get groupEntryContent for webDomain %{private}s, error: %{public}@"
+ "Failed to add %{public}s to always allowed apps for app data migration: %{public}s"
+ "Failed to add app exception for %{public}s for app data migration: %{public}s"
+ "Failed to fetch managing guardian Apple IDs again. Error: %{public}@"
+ "Ignored managing guardian Apple IDs, a newer reply was applied"
+ "Managing guardian Apple IDs changed to: %{private}@"
+ "No always-allow change needed for app data migration to %{public}s"
+ "No app exception change needed for app data migration to %{public}s"
+ "No app exception change needed for app data migration to %{public}s as it already has one"
+ "No applicator, defaulting content to webDomain %{private}s"
+ "Not adding app exception for app data migration to %{public}s as it has no installed app record with a rating, distributor, and Adam ID"
+ "Not adding app exception for app data migration to %{public}s as its rating %{public}llu doesn't match an approved rating for the source"
+ "migrateAppData(fromBundleIdentifier:toBundleIdentifier:persistenceController:categoryProvider:fetchAppInfo:completionHandler:)"
- "migrateAppData(fromBundleIdentifier:toBundleIdentifier:persistenceController:categoryProvider:completionHandler:)"
```
