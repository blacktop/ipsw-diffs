## NanoResourceGrabber

> `/System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber`

```diff

-113.0.0.0.0
-  __TEXT.__text: 0x4440
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0x36c
-  __TEXT.__const: 0x40
-  __TEXT.__oslogstring: 0x796
-  __TEXT.__cstring: 0x43e
-  __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__unwind_info: 0x1c8
-  __TEXT.__objc_classname: 0x5c
-  __TEXT.__objc_methname: 0xcf7
-  __TEXT.__objc_methtype: 0x2d2
-  __TEXT.__objc_stubs: 0x9c0
-  __DATA_CONST.__got: 0xf0
+116.0.0.0.0
+  __TEXT.__text: 0x437c
+  __TEXT.__objc_methlist: 0x374
+  __TEXT.__const: 0x48
+  __TEXT.__oslogstring: 0x85e
+  __TEXT.__cstring: 0x440
+  __TEXT.__gcc_except_tab: 0xb8
+  __TEXT.__unwind_info: 0x1c0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x298
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a0
+  __DATA_CONST.__objc_selrefs: 0x3f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1c8
+  __DATA_CONST.__got: 0x100
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x360
   __AUTH_CONST.__objc_const: 0x3d0
   __AUTH_CONST.__objc_intobj: 0x348
-  __AUTH.__objc_data: 0xf0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x30
+  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1FF12D90-D44B-3533-9BEB-97D7C2883BBB
-  Functions: 113
-  Symbols:   470
-  CStrings:  283
+  UUID: 7FDC67DE-A6C2-3DEE-B7EE-44AC5157068E
+  Functions: 116
+  Symbols:   494
+  CStrings:  110
 
Symbols:
+ +[NanoResourceGrabber iconDataForVariant:proxy:screenScale:]
+ +[NanoResourceGrabber iconDataForVariant:proxy:screenScale:].cold.1
+ +[NanoResourceGrabber iconDataForVariant:proxy:screenScale:].cold.2
+ _CGAffineTransformMakeScale
+ _OBJC_CLASS_$_ISIcon
+ _OBJC_CLASS_$_ISImageDescriptor
+ ___54-[NanoResourceGrabber getAppViewListImage:completion:]_block_invoke.79
+ ___54-[NanoResourceGrabber getAppViewListImage:completion:]_block_invoke.79.cold.1
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$CGImageForDescriptor:
+ _objc_msgSend$_sizeForVariant:
+ _objc_msgSend$appState
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$initWithCGImage:scale:orientation:
+ _objc_msgSend$initWithResourceProxy:
+ _objc_msgSend$initWithSize:scale:
+ _objc_msgSend$isInstalled
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$prepareImageForDescriptor:
+ _objc_release_x28
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- ___54-[NanoResourceGrabber getAppViewListImage:completion:]_block_invoke.77
- ___54-[NanoResourceGrabber getAppViewListImage:completion:]_block_invoke.77.cold.1
CStrings:
+ "%@: missing proxy or app not installed %@ %{BOOL}u"
+ "icon for %@ variant %@ (%@) scale %f (%f) found, descriptor %@, cgImage %@, iconImage %@, iconScale %f, length = %@"
+ "icon for %@ variant %@ not found"
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8q16"
- "@28@0:8@16i24"
- "@28@0:8i16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@36@0:8i16@20@28"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8[32C]16"
- "Checksum"
- "NRGError"
- "NRGResourceCache"
- "NSObject"
- "NanoResourceGrabber"
- "NanoResourceGrabberIDSXPC"
- "Q16@0:8"
- "T#,R"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_iconCacheQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",&,N,V_nrgdConnection"
- "TB,V_connectionMayBeValid"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_connectionMayBeValid"
- "_getCachedIconForBundleID:iconVariant:"
- "_getPhoneIconForBundleID:iconVariant:timeout:block:"
- "_getPhoneLocalIconForBundleID:iconVariant:block:"
- "_getRemoteIconForBundleIDBypassingCache:iconVariant:block:timeout:"
- "_iconCacheQueue"
- "_iconVariant:fromURL:"
- "_nrgdConnection"
- "_queue"
- "_setCachedIcon:forIconVariant:inBundleID:"
- "_sizeForVariant:"
- "activePairedDeviceSelectorBlock"
- "addObject:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayWithObjects:count:"
- "autorelease"
- "boolValue"
- "bytes"
- "cacheDirPathForAppBundleID:withPairedDeviceStorePath:"
- "cacheDirPathForPairedDevice"
- "cacheDirPathForPairedDeviceStorePath:"
- "cachePathForIconVariant:inBundleID:withPairedDeviceStorePath:"
- "checksum:"
- "checksumData"
- "checksumDataToChecksum:"
- "class"
- "conformsToProtocol:"
- "connectToService"
- "connectionMayBeValid"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "createCachePathIfNecessaryWithPairedDeviceStorePath:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "currentHandler"
- "dataWithBytes:length:"
- "dataWithContentsOfFile:"
- "dataWithContentsOfFile:options:error:"
- "dealloc"
- "debugDescription"
- "defaultManager"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithCode:"
- "errorWithDomain:code:userInfo:"
- "fetchWatchAppBundleURLWithinCompanionAppWithWatchAppIdentifier:completion:"
- "fileExistsAtPath:"
- "fileURLWithPath:isDirectory:"
- "firstObject"
- "getAllDevicesWithArchivedAltAccountDevicesMatching:"
- "getAppViewListImage:completion:"
- "getBytes:length:"
- "getCachedIconForBundleID:iconVariant:outIconImage:queue:updateBlock:timeout:"
- "getCachedIconForBundleID:iconVariant:outIconImage:updateBlock:"
- "getIconForBundleID:iconVariant:block:timeout:"
- "getIconForBundleID:iconVariant:queue:block:timeout:"
- "handleFailureInFunction:file:lineNumber:description:"
- "hash"
- "iconCacheDirPathForAppBundleID:withPairedDeviceStorePath:"
- "iconCacheQueue"
- "iconForIconVariant:inBundleID:withPairedDeviceStorePath:"
- "imageWithCGImage:scale:orientation:"
- "imageWithData:"
- "imageWithData:scale:"
- "init"
- "initWithMachServiceName:options:"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidate"
- "invalidateBundleID:withPairedDeviceStorePath:"
- "invalidatePairedDevice:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "liIconVariants"
- "mainScreen"
- "matchesChecksum:"
- "matchesChecksumData:"
- "nrgIconVariants"
- "nrgdConnection"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "queue"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeItemAtPath:error:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "scale"
- "self"
- "setConnectionMayBeValid:"
- "setIcon:forIconVariant:inBundleID:withPairedDeviceStorePath:"
- "setIconCacheQueue:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setNrgdConnection:"
- "setQueue:"
- "setRemoteObjectInterface:"
- "setResourceValue:forKey:error:"
- "sharedDeviceConnection"
- "sharedInstance"
- "stringByAppendingPathComponent:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "unarchivedObjectOfClass:fromData:error:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8[32C]16"
- "v32@0:8@16@24"
- "v36@0:8@16i24@28"
- "v36@0:8@16i24@?28"
- "v40@0:8{CGSize=dd}16@?32"
- "v44@0:8@\"NSString\"16i24d28@?<v@?@\"NSData\">36"
- "v44@0:8@16i24@28@36"
- "v44@0:8@16i24@?28d36"
- "v44@0:8@16i24^@28@?36"
- "v44@0:8@16i24d28@?36"
- "v48@0:8{CGSize=dd}16d32@?40"
- "v48@0:8{CGSize=dd}16d32@?<v@?@\"NSData\"@\"NSError\">40"
- "v52@0:8@16i24@28@?36d44"
- "v60@0:8@16i24^@28@36@?44d52"
- "valueForProperty:"
- "waitForAltAccountPairingStorePathPairingID:"
- "writeToFile:options:error:"
- "xpcGetAppViewListImage:scale:reply:"
- "xpcGetIconForBundleID:iconVariant:withTimeout:reply:"
- "zone"
- "{CGSize=dd}20@0:8i16"

```
