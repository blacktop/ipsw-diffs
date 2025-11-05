## SystemPolicy

> `/System/Library/PrivateFrameworks/SystemPolicy.framework/Versions/A/SystemPolicy`

```diff

-620.81.1.0.0
-  __TEXT.__text: 0x17c5c
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_methlist: 0x13b8
+620.100.82.0.0
+  __TEXT.__text: 0x183c8
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_methlist: 0x1770
   __TEXT.__const: 0xb4
-  __TEXT.__cstring: 0x15ff
+  __TEXT.__cstring: 0x168a
   __TEXT.__gcc_except_tab: 0x1cc
-  __TEXT.__oslogstring: 0x126a
-  __TEXT.__unwind_info: 0x708
-  __TEXT.__objc_classname: 0x2b5
-  __TEXT.__objc_methname: 0x3ad7
-  __TEXT.__objc_methtype: 0xb48
+  __TEXT.__oslogstring: 0x12ba
+  __TEXT.__unwind_info: 0x738
+  __TEXT.__objc_classname: 0x2c0
+  __TEXT.__objc_methname: 0x3bb8
+  __TEXT.__objc_methtype: 0xb82
   __TEXT.__objc_stubs: 0x2280
   __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0x150
-  __DATA_CONST.__objc_classlist: 0xf8
+  __DATA_CONST.__const: 0x130
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe00
+  __DATA_CONST.__objc_selrefs: 0xe38
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__objc_arraydata: 0x478
-  __AUTH_CONST.__auth_got: 0x410
+  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_arraydata: 0x490
+  __AUTH_CONST.__auth_got: 0x418
   __AUTH_CONST.__const: 0x860
-  __AUTH_CONST.__cfstring: 0x21a0
-  __AUTH_CONST.__objc_const: 0x3808
-  __AUTH_CONST.__objc_arrayobj: 0x180
+  __AUTH_CONST.__cfstring: 0x2200
+  __AUTH_CONST.__objc_const: 0x3320
+  __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0x26c
+  __AUTH.__objc_data: 0xa00
+  __DATA.__objc_ivar: 0x280
   __DATA.__data: 0x248
   __DATA.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24144DD3-FFF1-364A-8359-05A83237BE1C
-  Functions: 710
-  Symbols:   1738
-  CStrings:  1504
+  UUID: 6B187CF0-EAB8-3688-8E84-FEF38421C739
+  Functions: 733
+  Symbols:   1771
+  CStrings:  1524
 
Symbols:
+ +[AppWrapper checkAppWrapperWithURL:withProcessURL:]
+ +[AppWrapper checkAppWrapperWithURL:withProcessURL:].cold.1
+ +[AppWrapper checkAppWrapperWithURL:withProcessURL:].cold.2
+ +[MIS currentDeviceID].cold.1
+ +[SPFilePolicy getAllowedPaths].cold.1
+ +[SPLog exec].cold.1
+ +[SPLog generic].cold.1
+ +[SPLog kext].cold.1
+ +[SPLog measurements].cold.1
+ +[SPLog sampling].cold.1
+ +[SPLog signposts].cold.1
+ +[SPLog verboseLoggingEnabled].cold.1
+ -[PolicyScanTarget createdTime]
+ -[PolicyScanTarget isBackingDMGNotarized]
+ -[PolicyScanTarget isBadAppWrapper]
+ -[PolicyScanTarget setIsBadAppWrapper:]
+ -[SPMetrics .cxx_destruct]
+ -[SPMetrics dealloc]
+ -[SPMetrics init]
+ -[SPMetrics reportEvent:andData:]
+ GCC_except_table14
+ OBJC_IVAR_$_PolicyScanTarget._createdTime
+ OBJC_IVAR_$_PolicyScanTarget._isBackingDMGNotarizationChecked
+ OBJC_IVAR_$_PolicyScanTarget._isBackingDMGNotarized
+ OBJC_IVAR_$_PolicyScanTarget._isBadAppWrapper
+ OBJC_IVAR_$_SPMetrics._connection
+ OBJC_IVAR_$_SPMetrics._interface
+ _NSURLCreationDateKey
+ _OBJC_CLASS_$_SPMetrics
+ _OBJC_METACLASS_$_SPMetrics
+ __OBJC_$_INSTANCE_METHODS_SPMetrics
+ __OBJC_$_INSTANCE_VARIABLES_SPMetrics
+ __OBJC_CLASS_RO_$_SPMetrics
+ __OBJC_METACLASS_RO_$_SPMetrics
+ ___33-[SPMetrics reportEvent:andData:]_block_invoke
+ __block_literal_global.74
+ __block_literal_global.99
+ __kCFURLDiskImageBackingURLKey
+ _isCodeRefNotarized
+ _isTerminalLikePath
+ _objc_msgSend$reportEvent:withData:withReply:
+ _os_variant_allows_internal_security_policies
+ globalBundleSuffixes.cold.1
+ isCodeRefNotarized.cold.1
- +[AppWrapper checkAppWrapperSymlink:]
- +[AppWrapper checkAppWrapperSymlink:].cold.1
- -[PolicyScanTarget hasBadAppWrapperSymlink]
- -[PolicyScanTarget isNotarized].cold.1
- GCC_except_table13
- OBJC_IVAR_$_PolicyScanTarget._hasBadAppWrapperSymlink
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- __block_literal_global.72
- _objc_msgSend$checkAppWrapperSymlink:
CStrings:
+ "/System/AppleInternal/Library/Frameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity"
+ "Alacritty.app"
+ "Process path doesn't match Wrappedbundle symlink: %@, %@"
+ "SPMetrics"
+ "T@\"NSDate\",R,N,V_createdTime"
+ "TB,N,V_isBadAppWrapper"
+ "TB,R,N,V_isBackingDMGNotarized"
+ "Terminal.app"
+ "WrappedBundle symlink points outside of the bundle: %@, %@"
+ "_createdTime"
+ "_isBackingDMGNotarizationChecked"
+ "_isBackingDMGNotarized"
+ "_isBadAppWrapper"
+ "checkAppWrapperWithURL:withProcessURL:"
+ "createdTime"
+ "iTerm2.app"
+ "isBackingDMGNotarized"
+ "isBadAppWrapper"
+ "reportEvent:andData:"
+ "reportEvent:withData:withReply:"
+ "setIsBadAppWrapper:"
+ "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?B@\"NSError\">32"
- "App wrapper has bad symlink: %@, %@"
- "TB,R,N,V_hasBadAppWrapperSymlink"
- "_hasBadAppWrapperSymlink"
- "checkAppWrapperSymlink:"
- "hasBadAppWrapperSymlink"

```
