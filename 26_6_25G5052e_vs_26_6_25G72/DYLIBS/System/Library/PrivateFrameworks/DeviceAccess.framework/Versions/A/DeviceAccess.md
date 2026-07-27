## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/Versions/A/DeviceAccess`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__TEXT.__objc_classname`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-326.7.0.0.0
-  __TEXT.__text: 0x5aecc
+326.9.0.0.0
+  __TEXT.__text: 0x5b1f8
   __TEXT.__auth_stubs: 0x1490
-  __TEXT.__objc_methlist: 0x45ec
+  __TEXT.__objc_methlist: 0x4634
   __TEXT.__const: 0x900
-  __TEXT.__cstring: 0x9e93
+  __TEXT.__cstring: 0x9ef3
   __TEXT.__gcc_except_tab: 0x1330
   __TEXT.__constg_swiftt: 0x3b8
   __TEXT.__swift5_typeref: 0x264

   __TEXT.__unwind_info: 0x1580
   __TEXT.__eh_frame: 0x5c0
   __TEXT.__objc_classname: 0x6b4
-  __TEXT.__objc_methname: 0x8a84
-  __TEXT.__objc_methtype: 0xc26
-  __TEXT.__objc_stubs: 0x4ac0
+  __TEXT.__objc_methname: 0x8c44
+  __TEXT.__objc_methtype: 0xc36
+  __TEXT.__objc_stubs: 0x4b00
   __DATA_CONST.__got: 0x508
   __DATA_CONST.__const: 0x320
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f50
+  __DATA_CONST.__objc_selrefs: 0x1f78
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x180
   __AUTH_CONST.__auth_got: 0xa58
   __AUTH_CONST.__const: 0x13a0
-  __AUTH_CONST.__cfstring: 0x3520
-  __AUTH_CONST.__objc_const: 0x7e28
+  __AUTH_CONST.__cfstring: 0x3560
+  __AUTH_CONST.__objc_const: 0x7ee8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0xb60
   __AUTH.__data: 0x250
-  __DATA.__objc_ivar: 0x6fc
+  __DATA.__objc_ivar: 0x70c
   __DATA.__data: 0xc48
   __DATA.__bss: 0x2e0
   __DATA.__common: 0x8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2333
-  Symbols:   3966
-  CStrings:  3258
+  Functions: 2339
+  Symbols:   3978
+  CStrings:  3272
 
Symbols:
+ -[DAAppAsset distributorBundleID]
+ -[DAAppAsset initWithBundleID:adamID:appName:developerName:iconData:distributorBundleID:]
+ -[DADevice preUpgradeDiscoveryConfiguration]
+ -[DADevice setPreUpgradeDiscoveryConfiguration:]
+ -[DADeviceRegistry initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoURL:companionAppBundleID:companionAppIsOptional:manufacturerURL:supportedModes:]
+ -[DADeviceRegistry manufacturerURL]
+ -[DADeviceRegistryInfo manufacturerURL]
+ -[DADeviceRegistryInfo setManufacturerURL:]
+ OBJC_IVAR_$_DAAppAsset._distributorBundleID
+ OBJC_IVAR_$_DADevice._preUpgradeDiscoveryConfiguration
+ OBJC_IVAR_$_DADeviceRegistry._manufacturerURL
+ OBJC_IVAR_$_DADeviceRegistryInfo._manufacturerURL
+ _objc_msgSend$initWithBundleID:adamID:appName:developerName:iconData:distributorBundleID:
+ _objc_msgSend$initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoURL:companionAppBundleID:companionAppIsOptional:manufacturerURL:supportedModes:
+ _objc_msgSend$manufacturerURL
+ _objc_msgSend$setManufacturerURL:
- -[DAAppAsset initWithBundleID:adamID:appName:developerName:iconData:]
- -[DADeviceRegistry initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoURL:companionAppBundleID:companionAppIsOptional:supportedModes:]
- _objc_msgSend$initWithBundleID:adamID:appName:developerName:iconData:
- _objc_msgSend$initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoURL:companionAppBundleID:companionAppIsOptional:supportedModes:
CStrings:
+ "<%@: %p; friendlyName=%@; image2x=%@; image3x=%@; videoURL=%@; companionAppBundleID=%@; companionAppIsOptional=%@; manufacturerURL=%@; supportedMode=%@>"
+ "<%@: %p; manufacturerID=%@; modelID=%@; friendlyName=%@; image2x=%@; image3x=%@; videoURL=%@; companionAppBundleID=%@; companionAppIsOptional=%@; manufacturerURL=%@; supportedMode=%@>"
+ "<DAAppAsset bundleID=%@ adamID=%@ appName=%@ developerName=%@ distributor=%@ iconSize=%lu cached=%@>"
+ "@64@0:8@16@24@32@40@48@56"
+ "@92@0:8@16@24@32@40@48@56@64B72@76@84"
+ "T@\"DADiscoveryConfiguration\",C,N,V_preUpgradeDiscoveryConfiguration"
+ "T@\"NSString\",C,N,V_manufacturerURL"
+ "T@\"NSString\",R,C,N,V_distributorBundleID"
+ "T@\"NSString\",R,C,N,V_manufacturerURL"
+ "_distributorBundleID"
+ "_manufacturerURL"
+ "_preUpgradeDiscoveryConfiguration"
+ "distributorBundleID"
+ "drMU"
+ "dsBd"
+ "initWithBundleID:adamID:appName:developerName:iconData:distributorBundleID:"
+ "initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoURL:companionAppBundleID:companionAppIsOptional:manufacturerURL:supportedModes:"
+ "manufacturerURL"
+ "preUpgradeDiscoveryConfiguration"
+ "setManufacturerURL:"
+ "setPreUpgradeDiscoveryConfiguration:"
- "<%@: %p; friendlyName=%@; image2x=%@; image3x=%@; videoURL=%@; companionAppBundleID=%@; companionAppIsOptional=%@; supportedMode=%@>"
- "<%@: %p; manufacturerID=%@; modelID=%@; friendlyName=%@; image2x=%@; image3x=%@; videoURL=%@; companionAppBundleID=%@; companionAppIsOptional=%@ upportedMode=%@>"
- "<DAAppAsset bundleID=%@ adamID=%@ appName=%@ developerName=%@  iconSize=%lu cached=%@>"
- "@56@0:8@16@24@32@40@48"
- "@84@0:8@16@24@32@40@48@56@64B72@76"
- "initWithBundleID:adamID:appName:developerName:iconData:"
- "initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoURL:companionAppBundleID:companionAppIsOptional:supportedModes:"
```
