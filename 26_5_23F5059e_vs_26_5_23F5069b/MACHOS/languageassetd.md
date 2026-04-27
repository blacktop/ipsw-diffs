## languageassetd

> `/usr/libexec/languageassetd`

```diff

-64.3.2.0.0
-  __TEXT.__text: 0x3da4
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_stubs: 0xc40
-  __TEXT.__objc_methlist: 0x248
-  __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x71b
-  __TEXT.__objc_methname: 0xa6a
-  __TEXT.__oslogstring: 0x83
+64.3.3.0.0
+  __TEXT.__text: 0x4cac
+  __TEXT.__auth_stubs: 0x4d0
+  __TEXT.__objc_stubs: 0xc60
+  __TEXT.__objc_methlist: 0x250
+  __TEXT.__oslogstring: 0x548
+  __TEXT.__const: 0x40
+  __TEXT.__cstring: 0x5a9
+  __TEXT.__objc_methname: 0xa93
   __TEXT.__objc_classname: 0x2e
-  __TEXT.__objc_methtype: 0x12f
-  __TEXT.__unwind_info: 0x138
-  __DATA_CONST.__auth_got: 0x238
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__objc_methtype: 0x14a
+  __TEXT.__unwind_info: 0x148
+  __DATA_CONST.__auth_got: 0x270
+  __DATA_CONST.__got: 0xc8
   __DATA_CONST.__const: 0x358
-  __DATA_CONST.__cfstring: 0x860
+  __DATA_CONST.__cfstring: 0x760
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x230
-  __DATA.__objc_selrefs: 0x340
-  __DATA.__objc_ivar: 0x20
+  __DATA.__objc_const: 0x250
+  __DATA.__objc_selrefs: 0x348
+  __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0xa0
   __DATA.__bss: 0x30
   __DATA.__common: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1346C748-FC65-3F04-BEA9-F3C549718F08
-  Functions: 69
-  Symbols:   104
-  CStrings:  282
+  UUID: B7BB1E1B-2992-3EB3-A3CB-DB4B8CA4A39C
+  Functions: 85
+  Symbols:   110
+  CStrings:  292
 
Symbols:
+ _MAIsCancelDownloadResultFailure
+ _NSStringFromClass
+ _NSStringFromSelector
+ __os_log_error_impl
+ _objc_opt_class
+ _objc_release_x23
+ _objc_release_x26
+ _xpc_release
- __os_log_default
- _objc_release_x21
CStrings:
+ "-[%{public}@ %{public}@]"
+ "@\"NSObject<OS_xpc_object>\""
+ "AssetType:%{public}@: download completed: asset \"%{public}@\", result=%ld"
+ "AssetType:%{public}@: start downloading asset \"%{public}@\""
+ "Cancel previous downloads assetType=[%{public}@] - result: %ld"
+ "Cancelling previous downloads for assetType=[%{public}@] - enter"
+ "Cancelling previous downloads for assetType=[%{public}@] - exit"
+ "Local asset: %{public}@"
+ "NO"
+ "Query metadata sync result for assetType=[%{public}@], version=%ld => %ld"
+ "Query metadata sync start for assetType=[%{public}@], version=%ld"
+ "Remote asset: %{public}@"
+ "YES"
+ "_xpcListener"
+ "alreadyInstalledAssetsWithPrimaryLanguages:assetFlagArray:assetInfo:"
+ "cancelCatalogDownload: failed (result %ld) for assetType=[%{public}@]; skipping new download"
+ "cancelCatalogDownload:then:"
+ "downloadLanguageAssets: eventString=[%{public}@]"
+ "initiateActualDownload:"
+ "languageassetd started"
+ "localAssetsWithAssetFlagArray:assetInfo:"
+ "purgeLocalAssetsWithType: %{public}@, mobileAssetVersionV2: %{public}@"
+ "purgeLocalFontAssets"
+ "setNeedsRedownload: %{public}@"
+ "startCatalogDownload completed: assetType=[%{public}@] result=%ld"
+ "startCatalogDownload marked assetType=[%{public}@] for redownloading."
+ "startCatalogDownload purging local font assets assetType=[%{public}@]."
+ "startCatalogDownload: enter assetType=[%{public}@]"
+ "startCatalogDownload: exit assetType=[%{public}@]"
- "AssetType:%@: download completed: asset \"%@\", result=%ld"
- "AssetType:%@: start downloading asset \"%@\""
- "Local asset: %@"
- "Remote asset: %@"
- "alreadyInstalledAssetsWithPrimaryLanguages:results:assetInfo:"
- "checkFontAssetsSanityWithLanguageAssetInfo:"
- "downloadLanguageAssets: eventString=[%@]"
- "initWithCapacity:"
- "localAssetsWithType:assetInfo:"
- "startCatalogDownload completed: assetType=[%@] result=%ld"
- "startCatalogDownload: assetType=[%@]"

```
