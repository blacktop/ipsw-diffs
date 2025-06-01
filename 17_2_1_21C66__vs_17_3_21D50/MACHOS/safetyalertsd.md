## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-43.0.27.0.0
-  __TEXT.__text: 0x6c738
+45.0.2.0.0
+  __TEXT.__text: 0x6ca7c
   __TEXT.__auth_stubs: 0xc10
   __TEXT.__objc_stubs: 0x1c80
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x2c0
-  __TEXT.__const: 0x3ec9
-  __TEXT.__gcc_except_tab: 0x2f70
-  __TEXT.__oslogstring: 0x19773
-  __TEXT.__cstring: 0x3639
+  __TEXT.__const: 0x3eb9
+  __TEXT.__gcc_except_tab: 0x2fac
+  __TEXT.__oslogstring: 0x19919
+  __TEXT.__cstring: 0x3681
   __TEXT.__objc_methname: 0x2332
   __TEXT.__objc_classname: 0x173
   __TEXT.__objc_methtype: 0x103f
-  __TEXT.__unwind_info: 0x1d58
+  __TEXT.__unwind_info: 0x1d68
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x618
   __DATA_CONST.__got: 0x2b8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x3f60
-  __DATA_CONST.__cfstring: 0x3ac0
+  __DATA_CONST.__cfstring: 0x3ae0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x370
   __DATA.__common: 0x10
-  __DATA.__bss: 0x320
+  __DATA.__bss: 0x338
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 209DDD26-775B-3E7F-A530-CB6F56F8E3C0
-  Functions: 1695
+  UUID: D818E107-AE1D-317E-A999-9739DF615D4A
+  Functions: 1696
   Symbols:   331
-  CStrings:  2761
+  CStrings:  2770
 
CStrings:
+ "efficacyManifestFileName"
+ "efficacy_manifest.txt"
+ "efficacy_manifest_v2.txt"
+ "{\"msg%{public}.0s\":\"#assetConfig,log\", \"pullpc\":%{private}d, \"appc\":%{private}d, \"efficacyParticipationPercentage\":%{private}d, \"wowControls\":%{private}d, \"pullCname\":%{private, location:escape_only}s, \"efficacyManifestFileName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#assetConfig,readRollingMetricAsset\", \"efficacyManifestFileName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#eff,#warning,downloadManifest,empty manifest file name\"}"
+ "{\"msg%{public}.0s\":\"#eff,collectingEfficacyMetric,not valid\"}"
+ "{\"msg%{public}.0s\":\"#eff,eraseManifests\"}"
+ "{\"msg%{public}.0s\":\"#eff,eraseManifests,empty file name\"}"
- "{\"msg%{public}.0s\":\"#assetConfig,log\", \"pullpc\":%{private}d, \"appc\":%{private}d, \"efficacyParticipationPercentage\":%{private}d, \"wowControls\":%{private}d, \"pullCname\":%{private, location:escape_only}s}"

```
