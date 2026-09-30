## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2333.7.0.1.0
-  __TEXT.__text: 0x9ed4c
-  __TEXT.__auth_stubs: 0x1d00
-  __TEXT.__objc_methlist: 0x3e9c
-  __TEXT.__const: 0x360
-  __TEXT.__cstring: 0x781e
-  __TEXT.__oslogstring: 0x9bd8
-  __TEXT.__gcc_except_tab: 0x3fcc
-  __TEXT.__unwind_info: 0x2150
+2333.22.12.1.0
+  __TEXT.__text: 0xa02ac
+  __TEXT.__auth_stubs: 0x1d60
+  __TEXT.__objc_methlist: 0x3ecc
+  __TEXT.__const: 0x378
+  __TEXT.__cstring: 0x7889
+  __TEXT.__oslogstring: 0x9cd6
+  __TEXT.__gcc_except_tab: 0x407c
+  __TEXT.__dlopen_cstrs: 0x4a
+  __TEXT.__unwind_info: 0x21a8
   __TEXT.__objc_classname: 0x48e
-  __TEXT.__objc_methname: 0xd184
+  __TEXT.__objc_methname: 0xd25d
   __TEXT.__objc_methtype: 0x223e
-  __TEXT.__objc_stubs: 0xabc0
-  __DATA_CONST.__got: 0x910
-  __DATA_CONST.__const: 0x3958
+  __TEXT.__objc_stubs: 0xacc0
+  __DATA_CONST.__got: 0x918
+  __DATA_CONST.__const: 0x3970
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x31d0
+  __DATA_CONST.__objc_selrefs: 0x3210
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x448
-  __AUTH_CONST.__auth_got: 0xe98
+  __AUTH_CONST.__auth_got: 0xec8
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0xf28
-  __AUTH_CONST.__cfstring: 0x67c0
+  __AUTH_CONST.__cfstring: 0x6800
   __AUTH_CONST.__objc_const: 0x54e0
   __AUTH_CONST.__objc_arrayobj: 0x330
   __AUTH_CONST.__objc_intobj: 0x168

   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x3fc
   __DATA.__data: 0x7a0
-  __DATA.__bss: 0x189
+  __DATA.__bss: 0x1a1
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__data: 0x220

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex
   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpotlightEmbedding.framework/SpotlightEmbedding
   - /System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge
   - /System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 2626
-  Symbols:   3547
-  CStrings:  4551
+  Functions: 2643
+  Symbols:   3571
+  CStrings:  4571
 
Symbols:
+ _OBJC_CLASS_$_APApplication
+ _SIUpdateKnownBundles
+ __sl_dlopen
+ _abort_report_np
+ _dlerror
+ _dlsym
+ _objc_getClass
CStrings:
+ "### fixupBundles %@ - %@"
+ "### fixupBundles found %@ - %@"
+ "(qid=%ld, bid=%s, AP) Filtering out hidden app %s"
+ "(qid=%ld, bid=%s, SP) Filtering out hidden app %s"
+ "(qid=%ld, bid=%s, context) Filtering out disabled bundle %s"
+ "2333.22.12.1"
+ "@_kMDItemBundleID=*"
+ "SDAppUninstallMonitor"
+ "SPFastHiddenAppsGetNoBuild"
+ "Unable to find class %s"
+ "Using disabledBundleIDs for (%ld, %s)"
+ "addHiddenAppFiltersToQueryContext:"
+ "applicationsExcludedFromUninstall"
+ "bundlefixup"
+ "filterOutHiddenApps"
+ "fixupBundlesWithGroup:"
+ "hiddenApplications"
+ "issueBundleFixup:completionHandler:"
+ "setFilterOutHiddenApps:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/Search.framework/Search"
+ "updateKnownBundles:group:"
- "2333.7.0.1"

```
