## HelpData

> `/System/Library/PrivateFrameworks/HelpData.framework/Versions/A/HelpData`

```diff

 236.0.0.0.0
-  __TEXT.__text: 0x1e970
+  __TEXT.__text: 0x1ea18
   __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x1d40
+  __TEXT.__objc_methlist: 0x1fcc
   __TEXT.__cstring: 0x357c
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x3fc
+  __TEXT.__gcc_except_tab: 0x3e0
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__oslogstring: 0x250
-  __TEXT.__unwind_info: 0x6e8
+  __TEXT.__unwind_info: 0x710
   __TEXT.__objc_classname: 0x31d
   __TEXT.__objc_methname: 0x5691
   __TEXT.__objc_methtype: 0xc12

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16c0
+  __DATA_CONST.__objc_selrefs: 0x1788
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0x730
   __AUTH_CONST.__cfstring: 0x3560
-  __AUTH_CONST.__objc_const: 0x4a00
+  __AUTH_CONST.__objc_const: 0x4578
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x960

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 233C2C2C-9B0F-3DE4-8D08-4C419D54B039
-  Functions: 729
-  Symbols:   2332
+  UUID: E63C6B3C-E27A-363C-9EA9-731E04F2804A
+  Functions: 747
+  Symbols:   2353
   CStrings:  2164
 
Symbols:
+ +[DDMAssetURLProtocol sharedManager].cold.1
+ +[DDMAssetURLProtocolCoordinator sharedCoordinator].cold.1
+ +[DDMConfig sharedConfig].cold.1
+ +[DDMContext sharedContext].cold.1
+ +[DDMObject log].cold.1
+ +[DDMObjectManager sharedObjectManager].cold.1
+ +[HPDFeatureFlags allowLandingView].cold.1
+ +[HPDFeatureFlags allowTipsSharing].cold.1
+ +[HPDHelpBook allowedClasses].cold.1
+ +[HPDSearchManager sharedSearchManager].cold.1
+ -[DDMContext isInternalBuild].cold.1
+ -[DDMObject _makeTreeFromArray:withDescription:topLevelItemIDs:].cold.1
+ -[DDMObject _makeTreeFromArray:withDescription:topLevelItemIDs:].cold.2
+ -[DDMObject _makeTreeFromArray:withDescription:topLevelItemIDs:].cold.3
+ -[HPDHelpBook absolutePathForApplicationWithBundleIdentifier:].cold.1
+ -[NSFileManager(HPDAdditions) hpd_UserHelpCacheContainerURL].cold.1
+ -[NSString(HPDHelpBookAdditions) addSSLAsNecessary].cold.1
+ HPDDefaultLog.cold.1
+ HPDLog.cold.1
+ _OUTLINED_FUNCTION_2
+ _allowedClasses.cold.1

```
