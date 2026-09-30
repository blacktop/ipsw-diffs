## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

-1301.79.0.0.0
-  __TEXT.__text: 0x41930
+1301.81.0.0.0
+  __TEXT.__text: 0x43bf0
   __TEXT.__auth_stubs: 0x1160
   __TEXT.__const: 0x500
   __TEXT.__gcc_except_tab: 0x268
-  __TEXT.__oslogstring: 0x7566
-  __TEXT.__cstring: 0x8a81
-  __TEXT.__unwind_info: 0x608
+  __TEXT.__oslogstring: 0x7654
+  __TEXT.__cstring: 0x8c1c
+  __TEXT.__unwind_info: 0x618
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x107
   __TEXT.__objc_stubs: 0x180
   __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__const: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x60
   __AUTH_CONST.__auth_got: 0x8c0
-  __AUTH_CONST.__const: 0x1088
+  __AUTH_CONST.__const: 0x10a8
   __AUTH_CONST.__cfstring: 0xa40
   __DATA.__data: 0x1
   __DATA.__common: 0x3c

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1F0011E8-AEDA-337C-8AB4-960F0F33814B
-  Functions: 503
-  Symbols:   1080
-  CStrings:  1357
+  UUID: E9591C51-C825-3FED-A0D9-884720BC05A8
+  Functions: 509
+  Symbols:   1089
+  CStrings:  1375
 
Symbols:
+ GCC_except_table361
+ GCC_except_table375
+ GCC_except_table377
+ GCC_except_table378
+ GCC_except_table439
+ GCC_except_table504
+ __ZN16CCProfileMonitor20getOwnersFromProfileEPK14__CFDictionary
+ __ZN16CCProfileMonitor21getOwnersFromCCConfigEPK14__CFDictionaryP7__CFSet
+ __ZN16CCProfileMonitor26isProfileInstalledForOwnerEPK10__CFString
+ __ZN16CCProfileMonitor28getOwnersFromPipesAndStreamsEPK14__CFDictionaryP7__CFSet
+ ____ZN12CCXPCService21handleIncomingMessageEP17_xpc_connection_sPv_block_invoke.20
+ ___block_descriptor_tmp.1780
+ ___block_descriptor_tmp.1844
+ ___block_descriptor_tmp.1937
+ ___block_descriptor_tmp.21
+ ___block_descriptor_tmp.2196
+ ___block_descriptor_tmp.2315
+ ___block_descriptor_tmp.26.2123
+ ___block_descriptor_tmp.30
+ ___block_literal_global.1258
+ ___block_literal_global.1842
+ ___block_literal_global.2152
+ ___block_literal_global.23
+ _isMultipleProfilesSupported
- GCC_except_table357
- GCC_except_table367
- GCC_except_table368
- GCC_except_table370
- GCC_except_table434
- GCC_except_table498
- ___block_descriptor_tmp.1721
- ___block_descriptor_tmp.1785
- ___block_descriptor_tmp.1878
- ___block_descriptor_tmp.2139
- ___block_descriptor_tmp.22
- ___block_descriptor_tmp.2258
- ___block_descriptor_tmp.26.2056
- ___block_literal_global.1257
- ___block_literal_global.1783
- ___block_literal_global.2095
CStrings:
+ "%s:%06u Configuration type is not dictionary\n"
+ "%s:%06u invalid configuration\n"
+ "%s:%06u keycount : %ld\n"
+ "%s:%06u unable to create set\n"
+ "%s:%d Owner:%s skipping profileLoaded"
+ "CCProfileMonitor::getOwnersFromCCConfig"
+ "CCProfileMonitor::getOwnersFromPipesAndStreams"
+ "CCProfileMonitor::profileCallback getting owners from profile failed"
+ "getOwnersFromCCConfig"
+ "getOwnersFromPipesAndStreams"
+ "getOwnersFromProfile"
+ "profileLoaded"

```
