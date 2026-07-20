## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

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
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`

```diff

-2700.27.0.0.0
-  __TEXT.__text: 0x54708
-  __TEXT.__objc_methlist: 0x467c
+2700.30.0.0.0
+  __TEXT.__text: 0x549e4
+  __TEXT.__objc_methlist: 0x46c4
   __TEXT.__const: 0x908
-  __TEXT.__cstring: 0xa0e3
+  __TEXT.__cstring: 0xa143
   __TEXT.__gcc_except_tab: 0x1330
   __TEXT.__constg_swiftt: 0x3b8
   __TEXT.__swift5_typeref: 0x25a

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f70
+  __DATA_CONST.__objc_selrefs: 0x1f98
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__got: 0x538
   __AUTH_CONST.__const: 0x6d0
-  __AUTH_CONST.__cfstring: 0x3580
-  __AUTH_CONST.__objc_const: 0x7fa0
+  __AUTH_CONST.__cfstring: 0x35c0
+  __AUTH_CONST.__objc_const: 0x8060
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0xc20
-  __AUTH.__objc_data: 0x1088
-  __AUTH.__data: 0x258
-  __DATA.__objc_ivar: 0x70c
-  __DATA.__data: 0xc40
+  __AUTH.__objc_data: 0x98
+  __AUTH.__data: 0x90
+  __DATA.__objc_ivar: 0x71c
+  __DATA.__data: 0xc08
   __DATA.__bss: 0x2f0
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x2a8
-  __DATA_DIRTY.__data: 0x70
+  __DATA_DIRTY.__objc_data: 0x1298
+  __DATA_DIRTY.__data: 0x270
   __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2294
-  Symbols:   3946
-  CStrings:  1508
+  Functions: 2300
+  Symbols:   3958
+  CStrings:  1511
 
Symbols:
+ -[DAAppAsset distributorBundleID]
+ -[DAAppAsset initWithBundleID:adamID:appName:developerName:iconData:distributorBundleID:]
+ -[DADevice preUpgradeDiscoveryConfiguration]
+ -[DADevice setPreUpgradeDiscoveryConfiguration:]
+ -[DADeviceRegistry initWithManufacturerID:modelID:friendlyName:image2xData:image3xData:videoURL:companionAppBundleID:companionAppIsOptional:supportedFeatures:manufacturerURL:supportedModes:]
+ -[DADeviceRegistry manufacturerURL]
+ -[DADeviceRegistryInfo manufacturerURL]
+ -[DADeviceRegistryInfo setManufacturerURL:]
+ _OBJC_IVAR_$_DAAppAsset._distributorBundleID
+ _OBJC_IVAR_$_DADevice._preUpgradeDiscoveryConfiguration
+ _OBJC_IVAR_$_DADeviceRegistry._manufacturerURL
+ _OBJC_IVAR_$_DADeviceRegistryInfo._manufacturerURL
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
