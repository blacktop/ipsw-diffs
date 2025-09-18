## Coordination

> `/System/Library/PrivateFrameworks/Coordination.framework/Coordination`

```diff

-196.11.1.0.0
-  __TEXT.__text: 0x2c4ec
+196.21.1.0.0
+  __TEXT.__text: 0x2c9e4
   __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x21f4
+  __TEXT.__objc_methlist: 0x222c
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x92c
-  __TEXT.__cstring: 0x1201
-  __TEXT.__oslogstring: 0x283b
-  __TEXT.__unwind_info: 0xcb0
-  __TEXT.__objc_classname: 0x8ac
-  __TEXT.__objc_methname: 0x50bc
+  __TEXT.__cstring: 0x1257
+  __TEXT.__oslogstring: 0x28f7
+  __TEXT.__unwind_info: 0xcc8
+  __TEXT.__objc_classname: 0x8b7
+  __TEXT.__objc_methname: 0x5160
   __TEXT.__objc_methtype: 0xf88
-  __TEXT.__objc_stubs: 0x3b20
+  __TEXT.__objc_stubs: 0x3be0
   __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0xfa0
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __DATA_CONST.__const: 0xfb8
+  __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4198
-  __DATA_CONST.__objc_selrefs: 0x11f0
-  __AUTH_CONST.__cfstring: 0x1440
-  __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__objc_const: 0x1508
+  __DATA_CONST.__objc_const: 0x41e0
+  __DATA_CONST.__objc_selrefs: 0x1230
+  __AUTH_CONST.__cfstring: 0x14a0
+  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__objc_const: 0x1550
   __AUTH_CONST.__auth_got: 0x2d0
-  __AUTH.__objc_data: 0xe60
+  __AUTH.__objc_data: 0xeb0
   __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0x288
+  __DATA.__objc_classrefs: 0x2a0
   __DATA.__objc_superrefs: 0x158
   __DATA.__objc_ivar: 0x2a8
   __DATA.__data: 0x900
-  __DATA.__bss: 0x80
+  __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__bss: 0x48
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 435F2417-50EF-389A-B3B1-27462A8AAE54
-  Functions: 1090
-  Symbols:   3794
-  CStrings:  1670
+  UUID: 83EC626F-B1C4-3395-A1BA-AAAFF85D23BA
+  Functions: 1096
+  Symbols:   3827
+  CStrings:  1692
 
Symbols:
+ +[CODefaults coordinationBundleID]
+ +[CODefaults userDefaultsForIdentifer:]
+ +[COFeatureStatus isFastFoldEnabled]
+ +[COFeatureStatus isIPDiscoveryDiffingEnabled]
+ _COCoordinationServiceDefaultsFastFoldEnabled
+ _COCoordinationServiceDefaultsIPDiffingEnabled
+ _OBJC_CLASS_$_CODefaults
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_METACLASS_$_CODefaults
+ __OBJC_$_CLASS_METHODS_CODefaults
+ __OBJC_CLASS_RO_$_CODefaults
+ __OBJC_METACLASS_RO_$_CODefaults
+ ___36+[COFeatureStatus isFastFoldEnabled]_block_invoke
+ ___46+[COFeatureStatus isIPDiscoveryDiffingEnabled]_block_invoke
+ ___block_literal_global.11
+ _isFastFoldEnabled.enabled
+ _isFastFoldEnabled.onceToken
+ _isIPDiscoveryDiffingEnabled.enabled
+ _isIPDiscoveryDiffingEnabled.onceToken
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$coordinationBundleID
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$mainBundle
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$userDefaultsForIdentifer:
CStrings:
+ "CODefaults"
+ "Fast fold feature status = %d. FF = %d"
+ "Fast fold feature status = %d. FF = %d, defaults = %d"
+ "FeatureStatus"
+ "IP Diffing feature status = %d. FF = %d"
+ "IP Diffing feature status = %d. FF = %d, defaults = %d"
+ "bundleIdentifier"
+ "com.apple.coordinated"
+ "coordinationBundleID"
+ "fastFold"
+ "fast_fold"
+ "initWithSuiteName:"
+ "ipDiffing"
+ "ip_discovery_diffing"
+ "isFastFoldEnabled"
+ "isIPDiscoveryDiffingEnabled"
+ "mainBundle"
+ "standardUserDefaults"
+ "userDefaultsForIdentifer:"

```
