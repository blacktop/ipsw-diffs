## BridgeCommons

> `/System/Library/PrivateFrameworks/BridgeCommons.framework/BridgeCommons`

```diff

-1310.13.0.0.0
-  __TEXT.__text: 0x1ad4
-  __TEXT.__auth_stubs: 0x2c0
+1350.1.0.0.0
+  __TEXT.__text: 0x196c
   __TEXT.__objc_methlist: 0x29c
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__cstring: 0x281
+  __TEXT.__gcc_except_tab: 0x3c
+  __TEXT.__cstring: 0x284
   __TEXT.__oslogstring: 0x1e2
   __TEXT.__dlopen_cstrs: 0x9f
-  __TEXT.__unwind_info: 0xf0
-  __TEXT.__objc_classname: 0x65
-  __TEXT.__objc_methname: 0x84b
-  __TEXT.__objc_methtype: 0x182
-  __TEXT.__objc_stubs: 0x780
-  __DATA_CONST.__got: 0xb8
+  __TEXT.__unwind_info: 0xf8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xf8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_selrefs: 0x2f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x170
+  __DATA_CONST.__got: 0xb8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x360
   __AUTH_CONST.__objc_const: 0x418
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 00889B1E-CB1B-3A09-BDCB-6A48949CA194
+  UUID: 7D965E9C-EBBE-3E99-B122-1DF63BFAC450
   Functions: 35
-  Symbols:   263
-  CStrings:  209
+  Symbols:   264
+  CStrings:  75
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x25
Functions:
~ -[BCUserGuide getUserGuideViewWithTitle:] : 828 -> 744
~ _BCViewContollerForModallyPresentingTheUrl : 308 -> 304
~ +[BCCAReporter incrementDiscoverSuccessType:] : 224 -> 212
~ +[BCPluginLoader _validatedBundleAtURL:] : 864 -> 812
~ +[BCPluginLoader loadPluginBundlesAtURL:] : 484 -> 472
~ +[BCDiscoverPluginManager _discoverPluginDirectoryURL] : 240 -> 224
~ +[BCDiscoverPluginManager discoverPluginBundles] : 176 -> 160
~ ___48+[BCDiscoverPluginManager discoverPluginBundles]_block_invoke : 124 -> 116
~ -[BCDiscoverPluginManager _buildDiscoverPlugins] : 300 -> 296
~ ___48-[BCDiscoverPluginManager _buildDiscoverPlugins]_block_invoke : 500 -> 440
~ -[BCDiscoverPluginManager sortedPluginsBySectionForInput:] : 200 -> 192
~ -[BCDiscoverPluginManager discoverPlugins] : 120 -> 108
~ _BCDiscoverPluginDescriptionWithSymbol : 504 -> 476
~ ___41+[BCPluginLoader loadPluginBundlesAtURL:]_block_invoke.cold.1 : 136 -> 92
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSMutableAttributedString\"16@0:8"
- "@\"NSString\"16@0:8"
- "@\"UIImage\"16@0:8"
- "@\"UIViewController\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "BCCAReporter"
- "BCDiscoverPluginManager"
- "BCDiscoverPluginProtocol"
- "BCPluginLoader"
- "BCUserGuide"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSArray\",C,N,V_discoverPlugins"
- "T@\"NSSet\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "T{os_unfair_lock_s=I},R,N,V_discoverPluginsLock"
- "URLByAppendingPathComponent:"
- "URLWithString:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_buildDiscoverPlugins"
- "_discoverPluginDirectoryURL"
- "_discoverPlugins"
- "_discoverPluginsLock"
- "_validatedBundleAtURL:"
- "activePairedDeviceSelectorBlock"
- "addObject:"
- "analyticsEventType"
- "appendAttributedString:"
- "arrayWithObjects:"
- "attributedStringWithAttachment:"
- "autorelease"
- "badgeImageForDiscoverPlugin"
- "boolValue"
- "bundleWithURL:"
- "capHeight"
- "class"
- "configurationWithTextStyle:scale:"
- "conformsToProtocol:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "debugDescription"
- "defaultManager"
- "description"
- "descriptionForDiscoverPlugin"
- "descriptionForDiscoverSuccessType:"
- "descriptionImage"
- "detailViewControllerToLaunch"
- "dictionaryWithObjects:forKeys:count:"
- "discoverPluginBundles"
- "discoverPlugins"
- "discoverPluginsLock"
- "discoverRouteDescription"
- "displayIndexForPluginInSection"
- "displaySectionForPlugin"
- "enumerateObjectsUsingBlock:"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "firstObject"
- "getAllDevicesWithArchivedAltAccountDevicesMatching:"
- "getResourceValue:forKey:error:"
- "getUserGuideViewWithTitle:"
- "hasSuffix:"
- "hash"
- "helpViewControllerWithTitle:identifier:version:"
- "image"
- "imageWithTintColor:renderingMode:"
- "incrementDiscoverSuccessType:"
- "init"
- "initWithCapacity:"
- "initWithData:ofType:"
- "initWithRootViewController:"
- "initWithString:"
- "initWithURL:"
- "isAvailableInCurrentConfiguration"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastPathComponent"
- "loadAndReturnError:"
- "loadPluginBundlesAtURL:"
- "objectAtIndex:"
- "onUserTappedPlugin"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "preferredFontForTextStyle:"
- "principalClass"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "routeType"
- "self"
- "sendEvent:with:"
- "setBounds:"
- "setDiscoverPlugins:"
- "setImage:"
- "setModalPresentationStyle:"
- "setPreferredControlTintColor:"
- "setRouteType:"
- "setShowTopicViewOnLoad:"
- "sharedInstance"
- "size"
- "sortedArrayUsingComparator:"
- "sortedPluginsBySectionForInput:"
- "superclass"
- "systemGrayColor"
- "systemImageNamed:withConfiguration:"
- "titleForDiscoverPlugin"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8Q16"
- "valueForProperty:"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
