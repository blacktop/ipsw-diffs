## ManagedSettingsAgent

> `/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent`

```diff

-267.102.1.0.0
-  __TEXT.__text: 0x64204
-  __TEXT.__auth_stubs: 0x1b80
+267.120.4.0.0
+  __TEXT.__text: 0x6d944
+  __TEXT.__auth_stubs: 0x1c00
   __TEXT.__objc_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x610
-  __TEXT.__const: 0x1aac
+  __TEXT.__objc_methlist: 0x620
+  __TEXT.__const: 0x1b5c
   __TEXT.__objc_classname: 0x6cc
-  __TEXT.__objc_methtype: 0xb42
-  __TEXT.__objc_methname: 0x1917
+  __TEXT.__objc_methtype: 0xba2
+  __TEXT.__objc_methname: 0x1985
   __TEXT.__cstring: 0x785
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xd14
-  __TEXT.__swift5_typeref: 0xff5
+  __TEXT.__constg_swiftt: 0xd70
+  __TEXT.__swift5_typeref: 0x1031
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0xa05
-  __TEXT.__swift5_fieldmd: 0x89c
+  __TEXT.__swift5_reflstr: 0xa35
+  __TEXT.__swift5_fieldmd: 0x8c4
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_capture: 0x3b0
-  __TEXT.__oslogstring: 0x27a2
-  __TEXT.__swift5_proto: 0x114
+  __TEXT.__oslogstring: 0x2af2
+  __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0x80
-  __TEXT.__swift5_protos: 0x30
-  __TEXT.__unwind_info: 0xac0
-  __TEXT.__eh_frame: 0x1524
-  __DATA_CONST.__auth_got: 0xdc8
-  __DATA_CONST.__got: 0x488
+  __TEXT.__swift5_protos: 0x34
+  __TEXT.__unwind_info: 0xb68
+  __TEXT.__eh_frame: 0x194c
+  __DATA_CONST.__auth_got: 0xe08
+  __DATA_CONST.__got: 0x490
   __DATA_CONST.__auth_ptr: 0x3d8
-  __DATA_CONST.__const: 0x1b80
+  __DATA_CONST.__const: 0x1c20
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA.__objc_const: 0x1a18
-  __DATA.__objc_selrefs: 0x420
+  __DATA.__objc_const: 0x1a60
+  __DATA.__objc_selrefs: 0x428
   __DATA.__objc_data: 0x310
-  __DATA.__data: 0x19a8
+  __DATA.__data: 0x1a00
   __DATA.__bss: 0x1a90
   __DATA.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 07176CDA-D09D-3744-B89E-FC4BB2F7208D
-  Functions: 996
-  Symbols:   683
-  CStrings:  503
+  UUID: CEAEF7FC-4494-3666-9885-F8D00A383E2E
+  Functions: 1024
+  Symbols:   692
+  CStrings:  521
 
Symbols:
+ _$s15ManagedSettings0abB0V16tokenEncodingKeyAA15SettingMetadataVy10Foundation4DataVGvgZ
+ _$s15ManagedSettings11ApplicationV5tokenAcA5TokenVyACG_tcfC
+ _$s15ManagedSettings16ActivityCategoryV5tokenAcA5TokenVyACG_tcfC
+ _$s15ManagedSettings5TokenV16persistableValueSo8NSObjectCSgyF
+ _$s15ManagedSettings5TokenV5value4fromACyxGSgSo8NSObjectCSg_tFZ
+ _$s15ManagedSettings5TokenVyxGs23CustomStringConvertibleAAMc
+ _$s15ManagedSettings9WebDomainV5tokenAcA5TokenVyACG_tcfC
+ _$sSo18NSNotificationNamea15ManagedSettingsE23tokenEncodingKeyChangedABvgZ
+ __swift_stdlib_bridgeErrorToNSError
CStrings:
+ "Failed to initialize application token with persisted value: %{public}@"
+ "Failed to initialize category token with persisted value: %{public}@"
+ "Failed to persist refreshed application token: %{public}s"
+ "Failed to persist refreshed category token: %{public}s"
+ "Failed to refresh dictionary key %{public}s for %{public}s: %{public}s"
+ "Failed to refresh set element %{public}s for %{public}s: %{public}s"
+ "Failed to refresh setting %{public}s value %{public}@ for %{public}s: %{public}s"
+ "Failed to refresh tokens for record: %s, storeName: %s. Error: %{public}@"
+ "Refreshing all store tokens..."
+ "Refreshing application tokens..."
+ "Refreshing category tokens..."
+ "Refreshing tokens..."
+ "Refreshing web domain tokens..."
+ "pendingRefreshTokens"
+ "refresh tokens received from process %{public}d"
+ "refreshCategoryTokens:applicationTokens:webDomainTokens:replyHandler:"
+ "tokenEncodingNotifier"
+ "v48@0:8@\"NSArray\"16@\"NSArray\"24@\"NSArray\"32@?<v@?@\"NSArray\"@\"NSArray\"@\"NSArray\"@\"NSError\">40"

```
