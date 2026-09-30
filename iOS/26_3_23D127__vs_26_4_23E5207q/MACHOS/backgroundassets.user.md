## backgroundassets.user

> `/usr/libexec/backgroundassets.user`

```diff

-227.60.2.0.0
-  __TEXT.__text: 0x4b980
-  __TEXT.__auth_stubs: 0x1490
-  __TEXT.__objc_stubs: 0x7560
+227.100.15.0.0
+  __TEXT.__text: 0x4e9d8
+  __TEXT.__auth_stubs: 0x1460
+  __TEXT.__objc_stubs: 0x75c0
   __TEXT.__objc_methlist: 0x33d4
-  __TEXT.__const: 0x13e4
-  __TEXT.__objc_classname: 0x721
-  __TEXT.__objc_methtype: 0x193b
+  __TEXT.__const: 0x1364
+  __TEXT.__objc_classname: 0x7b3
+  __TEXT.__objc_methtype: 0x1983
   __TEXT.__oslogstring: 0x5ee8
-  __TEXT.__cstring: 0x4202
-  __TEXT.__objc_methname: 0x976f
-  __TEXT.__gcc_except_tab: 0x1508
+  __TEXT.__cstring: 0x3f62
+  __TEXT.__objc_methname: 0x990e
+  __TEXT.__gcc_except_tab: 0x1520
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0x2fc
-  __TEXT.__swift5_typeref: 0x3f7
+  __TEXT.__swift5_typeref: 0x3f3
   __TEXT.__swift5_reflstr: 0x39a
   __TEXT.__swift5_fieldmd: 0x3a8
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__swift5_assocty: 0xd8
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x1258
-  __TEXT.__eh_frame: 0x360
-  __DATA_CONST.__auth_got: 0xa58
-  __DATA_CONST.__got: 0x4e8
+  __TEXT.__unwind_info: 0x12c8
+  __TEXT.__eh_frame: 0x330
+  __DATA_CONST.__auth_got: 0xa40
+  __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__auth_ptr: 0x2f0
   __DATA_CONST.__const: 0x1a40
   __DATA_CONST.__cfstring: 0x2400

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x55e8
-  __DATA.__objc_selrefs: 0x2100
+  __DATA.__objc_selrefs: 0x2108
   __DATA.__objc_ivar: 0x3ac
   __DATA.__objc_data: 0x10d0
-  __DATA.__data: 0xf28
+  __DATA.__data: 0xf20
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1e00
   __DATA.__common: 0x18

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 286BA235-DE9A-3F58-9209-71A21DD348BA
-  Functions: 1749
-  Symbols:   600
-  CStrings:  2873
+  UUID: 72757912-24C5-30DC-9A6E-713F3E96F545
+  Functions: 1752
+  Symbols:   597
+  CStrings:  2864
 
Symbols:
+ _$s29ManagedBackgroundAssetsHelper0D0C18manifestDataSource18forAppWithBundleIDSo011MBAManifestfG0VSS_tKFTj
+ _$s29ManagedBackgroundAssetsHelper0D0C23appStoreManifestRequest18forAppWithBundleID10Foundation10URLRequestVSS_tKFTj
+ _$s29ManagedBackgroundAssetsHelper0D0C26pathToManifestInLocalCache18forAppWithBundleID6System8FilePathVSgSS_tKFTj
+ _$s29ManagedBackgroundAssetsHelper0D0C6helperACyKFZ
+ _$s29ManagedBackgroundAssetsHelper0D0CMn
+ _$sSD23ManagedBackgroundAssetsSSRszAA15UserInfoCodable_pSgRs_rlE4jsonSDySSACGSgyp_tcfC
+ _$ss22KeyedDecodingContainerV23ManagedBackgroundAssetsE14decodeUserInfo6forKeySDySSAC0hI7Codable_pSgGx_tKF
+ _$ss22KeyedEncodingContainerV23ManagedBackgroundAssetsE6encode8userInfo6forKeyySDySSAC04UserI7Codable_pSgG_xtKF
+ _swift_bridgeObjectRelease_n
- _$s10Foundation4DataVSEAAMc
- _$s29ManagedBackgroundAssetsHelper0D0C5ProxyC15manifestRequest011forAppStoreI12WithBundleID10Foundation10URLRequestVSS_tKF
- _$s29ManagedBackgroundAssetsHelper0D0C5ProxyC18manifestDataSource18forAppWithBundleIDSo011MBAManifestgH0VSS_tKF
- _$s29ManagedBackgroundAssetsHelper0D0C5ProxyC4path40toManifestInLocalCacheForAppWithBundleID6System8FilePathVSgSS_tKF
- _$s29ManagedBackgroundAssetsHelper0D0C5ProxyCMn
- _$s29ManagedBackgroundAssetsHelper0D0C8newProxyAC0F0CyKFZ
- _$ss22KeyedDecodingContainerV23ManagedBackgroundAssetsE14decodeUserInfo6forKeySDySSAC0hI7Codable_pGx_tKF
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "App Store manifest request for app with bundle ID: %{public}s"
+ "Local-cache manifest contents for app with bundle ID: %{public}s"
+ "Local-cache manifest for app with bundle ID: %{public}s"
+ "No development-override URL is set."
+ "The App Review manifest contents couldn’t be retrieved for the application with the bundle identifier “%{public}@”."
+ "The App Review manifest contents couldn’t be retrieved for the application with the bundle identifier “%{public}@”: %{public}@"
+ "The application with the identifier “%{public}@” is ineligible for development overrides."
+ "The custom information is invalid."
+ "The local-cache manifest contents couldn’t be retrieved for the application with the bundle identifier “%{public}@”."
+ "The local-cache manifest contents couldn’t be retrieved for the application with the bundle identifier “%{public}@”: %{public}@"
+ "The manifest data source “%{public}s” is unknown."
+ "appStoreManifestRequestForApplicationWithBundleIdentifier:error:"
+ "isUPPValidated"
+ "localCacheManifestContentsForApplicationWithBundleIdentifier:error:"
- "Contents of manifest in local cache for app with bundle ID: %{public}s"
- "Development overrides aren’t permitted for the application with the identifier “%{public}@”."
- "Manifest data from local cache for app with bundle ID: %{public}s"
- "Manifest in local cache for app with bundle ID: %{public}s"
- "Manifest request for App Store app with bundle ID: %{public}s"
- "No development override is set."
- "The App Review manifest data couldn’t be retrieved for the application with the bundle identifier “%{public}@”."
- "The App Review manifest data couldn’t be retrieved for the application with the bundle identifier “%{public}@”: %{public}@"
- "The custom information “"
- "The local-cache manifest data couldn’t be retrieved for the application with the bundle identifier “%{public}@”."
- "The local-cache manifest data couldn’t be retrieved for the application with the bundle identifier “%{public}@”: %{public}@"
- "manifestDataFromLocalCacheForApplicationWithBundleIdentifier:error:"
- "manifestRequestForAppStoreApplicationWithBundleIdentifier:error:"

```
