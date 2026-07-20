## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/Versions/A/DeviceAccess`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`

```diff

-2700.27.0.0.0
-  __TEXT.__text: 0x586ac
-  __TEXT.__objc_methlist: 0x467c
+2700.30.0.0.0
+  __TEXT.__text: 0x589c4
+  __TEXT.__objc_methlist: 0x46c4
   __TEXT.__const: 0x908
-  __TEXT.__cstring: 0x9fc3
+  __TEXT.__cstring: 0xa013
   __TEXT.__gcc_except_tab: 0x132c
   __TEXT.__constg_swiftt: 0x3b8
   __TEXT.__swift5_typeref: 0x25a

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f58
+  __DATA_CONST.__objc_selrefs: 0x1f80
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__got: 0x510
   __AUTH_CONST.__const: 0x13a0
-  __AUTH_CONST.__cfstring: 0x3520
-  __AUTH_CONST.__objc_const: 0x7fa0
+  __AUTH_CONST.__cfstring: 0x3560
+  __AUTH_CONST.__objc_const: 0x8060
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__auth_got: 0xa78
-  __AUTH.__objc_data: 0x1088
-  __AUTH.__data: 0x258
-  __DATA.__objc_ivar: 0x70c
-  __DATA.__data: 0xc40
+  __AUTH.__objc_data: 0x98
+  __AUTH.__data: 0x90
+  __DATA.__objc_ivar: 0x71c
+  __DATA.__data: 0xc08
   __DATA.__bss: 0x2e0
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x2a8
-  __DATA_DIRTY.__data: 0x70
+  __DATA_DIRTY.__objc_data: 0x1298
+  __DATA_DIRTY.__data: 0x270
   __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2331
-  Symbols:   3995
-  CStrings:  1502
+  Functions: 2337
+  Symbols:   4007
+  CStrings:  1505
 
Symbols:
+ -[DAAppAsset distributorBundleID]
+ -[DAAppAsset initWithBundleID:adamID:appName:developerName:iconData:distributorBundleID:]
+ -[DADevice preUpgradeDiscoveryConfiguration]
+ -[DADevice setPreUpgradeDiscoveryConfiguration:]
+ -[DADeviceRegistry initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoURL:companionAppBundleID:companionAppIsOptional:supportedFeatures:manufacturerURL:supportedModes:]
+ -[DADeviceRegistry manufacturerURL]
+ -[DADeviceRegistryInfo manufacturerURL]
+ -[DADeviceRegistryInfo setManufacturerURL:]
+ OBJC_IVAR_$_DAAppAsset._distributorBundleID
+ OBJC_IVAR_$_DADevice._preUpgradeDiscoveryConfiguration
+ OBJC_IVAR_$_DADeviceRegistry._manufacturerURL
+ OBJC_IVAR_$_DADeviceRegistryInfo._manufacturerURL
+ _objc_msgSend$initWithBundleID:adamID:appName:developerName:iconData:distributorBundleID:
+ _objc_msgSend$initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoURL:companionAppBundleID:companionAppIsOptional:supportedFeatures:manufacturerURL:supportedModes:
+ _objc_msgSend$manufacturerURL
+ _objc_msgSend$setManufacturerURL:
- -[DAAppAsset initWithBundleID:adamID:appName:developerName:iconData:]
- -[DADeviceRegistry initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoURL:companionAppBundleID:companionAppIsOptional:supportedFeatures:supportedModes:]
- _objc_msgSend$initWithBundleID:adamID:appName:developerName:iconData:
- _objc_msgSend$initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoURL:companionAppBundleID:companionAppIsOptional:supportedFeatures:supportedModes:
CStrings:
+ "<%@: %p; friendlyName=%@; image2x=%@; image3x=%@; videoURL=%@; companionAppBundleID=%@; companionAppIsOptional=%@; manufacturerURL=%@; supportedFeatures=%@ supportedMode=%@>"
+ "<%@: %p; manufacturerID=%@; modelID=%@; friendlyName=%@; image2x=%@; image3x=%@; videoURL=%@; companionAppBundleID=%@; companionAppIsOptional=%@; manufacturerURL=%@; supportedFeatures=%@; supportedMode=%@>"
+ "<DAAppAsset bundleID=%@ adamID=%@ appName=%@ developerName=%@ distributor=%@ iconSize=%lu cached=%@>"
+ "distributorBundleID"
+ "drMU"
+ "dsBd"
- "<%@: %p; friendlyName=%@; image2x=%@; image3x=%@; videoURL=%@; companionAppBundleID=%@; companionAppIsOptional=%@; supportedFeatures=%@ supportedMode=%@>"
- "<%@: %p; manufacturerID=%@; modelID=%@; friendlyName=%@; image2x=%@; image3x=%@; videoURL=%@; companionAppBundleID=%@; companionAppIsOptional=%@; supportedFeatures=%@; supportedMode=%@>"
- "<DAAppAsset bundleID=%@ adamID=%@ appName=%@ developerName=%@  iconSize=%lu cached=%@>"
```
