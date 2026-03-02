## proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

-300.40.45.0.0
-  __TEXT.__text: 0x2a4d5c
-  __TEXT.__auth_stubs: 0x34a0
-  __TEXT.__objc_stubs: 0x42a0
+300.40.46.0.0
+  __TEXT.__text: 0x2a2fa4
+  __TEXT.__auth_stubs: 0x3480
+  __TEXT.__objc_stubs: 0x4280
   __TEXT.__objc_methlist: 0x2974
-  __TEXT.__objc_classname: 0x2317
-  __TEXT.__objc_methname: 0xdfed
-  __TEXT.__const: 0x29150
-  __TEXT.__objc_methtype: 0x3612
-  __TEXT.__cstring: 0x86ad
-  __TEXT.__swift5_typeref: 0x10b62
-  __TEXT.__constg_swiftt: 0xe928
+  __TEXT.__objc_classname: 0x2367
+  __TEXT.__objc_methname: 0xdf6d
+  __TEXT.__const: 0x29270
+  __TEXT.__objc_methtype: 0x3602
+  __TEXT.__cstring: 0x868d
+  __TEXT.__swift5_typeref: 0x10cfc
+  __TEXT.__constg_swiftt: 0xea04
   __TEXT.__swift5_reflstr: 0xa2a3
-  __TEXT.__swift5_fieldmd: 0xa64c
+  __TEXT.__swift5_fieldmd: 0xa6f0
   __TEXT.__swift5_builtin: 0x5dc
   __TEXT.__swift5_assocty: 0xf78
-  __TEXT.__oslogstring: 0x8296
-  __TEXT.__swift5_capture: 0x33f4
-  __TEXT.__swift5_proto: 0x1f64
-  __TEXT.__swift5_types: 0xa7c
-  __TEXT.__swift_as_entry: 0x148
-  __TEXT.__swift_as_ret: 0x154
-  __TEXT.__swift5_protos: 0x128
+  __TEXT.__oslogstring: 0x8266
+  __TEXT.__swift5_capture: 0x3394
+  __TEXT.__swift5_proto: 0x1f68
+  __TEXT.__swift5_types: 0xa8c
+  __TEXT.__swift_as_entry: 0x120
+  __TEXT.__swift_as_ret: 0x120
+  __TEXT.__swift5_protos: 0x12c
   __TEXT.__swift5_mpenum: 0x140
-  __TEXT.__unwind_info: 0x7a38
-  __TEXT.__eh_frame: 0x84f8
-  __DATA_CONST.__auth_got: 0x1a58
-  __DATA_CONST.__got: 0xf10
-  __DATA_CONST.__auth_ptr: 0x1b50
-  __DATA_CONST.__const: 0x17e10
+  __TEXT.__unwind_info: 0x79d8
+  __TEXT.__eh_frame: 0x7ed8
+  __DATA_CONST.__auth_got: 0x1a48
+  __DATA_CONST.__got: 0xf00
+  __DATA_CONST.__auth_ptr: 0x1b68
+  __DATA_CONST.__const: 0x17f00
   __DATA_CONST.__cfstring: 0x480
-  __DATA_CONST.__objc_classlist: 0x460
+  __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x180
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x17dc0
-  __DATA.__objc_selrefs: 0x1de8
+  __DATA.__objc_const: 0x17d68
+  __DATA.__objc_selrefs: 0x1de0
   __DATA.__objc_ivar: 0x54
-  __DATA.__objc_data: 0x37b0
-  __DATA.__data: 0x199d0
-  __DATA.__bss: 0x3ac50
-  __DATA.__common: 0x850
+  __DATA.__objc_data: 0x3800
+  __DATA.__data: 0x19b98
+  __DATA.__bss: 0x3abd0
+  __DATA.__common: 0x858
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 348AE286-55DF-3C9F-BFCB-27797CE4D3EA
-  Functions: 11616
-  Symbols:   1629
-  CStrings:  4319
+  UUID: A7C7A172-7A6C-3958-92C6-5E175162B97F
+  Functions: 11628
+  Symbols:   1625
+  CStrings:  4314
 
Symbols:
- _$s14ProductKitCore7HomePodV6AssetsCMa
- _$sScG22awaitAllRemainingTasks9isolationyScA_pSgYi_tYaF
- _$sScG22awaitAllRemainingTasks9isolationyScA_pSgYi_tYaFTu
- _OBJC_CLASS_$_NSBundle
CStrings:
+ "### Download completed with error: %@"
+ "### Failed to fetch '%s' assets for %s with timeout '%f': %@"
+ "### No cached bundle found - fetching just-in-time"
+ "%s: %s, type=%s"
+ "%s: %s, type=%s, timeout=%f"
+ "Could not find deviceImage '"
+ "Download completed!"
+ "Found '%s' bundle for speed '%s'"
+ "_TtC17proximitycontrold24SharingAssetBundleSource"
+ "_TtC17proximitycontrold27ProductKitAssetBundleSource"
+ "assets(for:type:)"
+ "bundles"
+ "fetchAssets(for:type:timeout:)"
+ "fetchAssetsTask(for:type:timeout:)"
+ "✔ Caching '%s' assets for %s with timeout '%f'"
- "### Failed to prewarm '%s' assets: %@"
- "### Failed to retrieve asset bundle for %s: %@"
- "### Failed to retrieve assets for %s: %@"
- "### No DeviceHistory for device?"
- "### No SessionHistory for session?"
- "%s: handoffEvent=%s"
- "%s: identifier=%s"
- "%s: identifier=%s, type%s, timeout=%f"
- "%s: message=%s, session=%s"
- "@@@ Download complete! error=%@"
- "Could not find device image '"
- "Could not resolve deviceImage"
- "_TtC17proximitycontrold19SharingAssetManager"
- "assets(for:type:timeout:)"
- "bundleCache"
- "handle(serializedObject:)"
- "handleHandoffEvent(_:timestamp:distance:)"
- "handoffAssetsCache"
- "imageNamed:inBundle:withConfiguration:"
- "start()"

```
