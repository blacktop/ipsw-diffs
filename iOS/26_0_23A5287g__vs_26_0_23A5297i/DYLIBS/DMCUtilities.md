## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities`

```diff

-48.0.0.0.0
-  __TEXT.__text: 0x347bc
+49.0.0.0.0
+  __TEXT.__text: 0x34ae8
   __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_methlist: 0x2d9c
+  __TEXT.__objc_methlist: 0x2db4
   __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x77c
-  __TEXT.__cstring: 0x3718
-  __TEXT.__oslogstring: 0x51ca
+  __TEXT.__gcc_except_tab: 0x7b8
+  __TEXT.__cstring: 0x3737
+  __TEXT.__oslogstring: 0x520d
   __TEXT.__dlopen_cstrs: 0x165
-  __TEXT.__unwind_info: 0xde8
+  __TEXT.__unwind_info: 0xe00
   __TEXT.__objc_classname: 0x4b7
-  __TEXT.__objc_methname: 0x99cf
+  __TEXT.__objc_methname: 0x9a25
   __TEXT.__objc_methtype: 0x1335
-  __TEXT.__objc_stubs: 0x6220
+  __TEXT.__objc_stubs: 0x6240
   __DATA_CONST.__got: 0x690
-  __DATA_CONST.__const: 0x1168
+  __DATA_CONST.__const: 0x11e8
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2540
+  __DATA_CONST.__objc_selrefs: 0x2550
   __DATA_CONST.__objc_superrefs: 0xc8
   __AUTH_CONST.__auth_got: 0x778
   __AUTH_CONST.__const: 0xd20
-  __AUTH_CONST.__cfstring: 0x4080
+  __AUTH_CONST.__cfstring: 0x40a0
   __AUTH_CONST.__objc_const: 0x4350
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH.__objc_data: 0xf00

   __DATA.__data: 0x300
   __DATA.__bss: 0x968
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__bss: 0xa8
+  __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6D2FBF8F-CFA7-3AD2-B559-B40E3B81D216
-  Functions: 1382
-  Symbols:   5063
-  CStrings:  3248
+  UUID: 1E1FDEBA-EDC7-3798-9725-39F01B16F43E
+  Functions: 1386
+  Symbols:   5077
+  CStrings:  3254
 
Symbols:
+ +[DMCFeatureOverrides bootstrapTokenOverrideWithDefaultValue:]
+ +[DMCFeatureOverrides nagMigrationGracePeriod]
+ -[DMCNetworkMonitor waitForNetworkWithCompletionHandler:timeout:]
+ _DMCDefaultsKeyNagMigrationGracePeriod
+ ___65-[DMCNetworkMonitor waitForNetworkWithCompletionHandler:timeout:]_block_invoke
+ ___65-[DMCNetworkMonitor waitForNetworkWithCompletionHandler:timeout:]_block_invoke.5
+ ___65-[DMCNetworkMonitor waitForNetworkWithCompletionHandler:timeout:]_block_invoke_2
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32bs40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ _objc_msgSend$waitForNetworkWithCompletionHandler:timeout:
- +[DMCFeatureOverrides bootstrapTokenOverride]
- ___57-[DMCNetworkMonitor waitForNetworkWithCompletionHandler:]_block_invoke
CStrings:
+ "DMCNagMigrationGracePeriod"
+ "DMCNetworkMonitor: Timedout waiting for network after %.1f seconds"
+ "RTS"
+ "bootstrapTokenOverrideWithDefaultValue:"
+ "nagMigrationGracePeriod"
+ "waitForNetworkWithCompletionHandler:timeout:"
- "bootstrapTokenOverride"

```
