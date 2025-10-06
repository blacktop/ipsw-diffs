## ClipServices

> `/System/Library/PrivateFrameworks/ClipServices.framework/ClipServices`

```diff

-1011.9.0.0.0
-  __TEXT.__text: 0x3783c
+1015.1.0.0.0
+  __TEXT.__text: 0x377fc
   __TEXT.__auth_stubs: 0x940
   __TEXT.__objc_methlist: 0x28f8
   __TEXT.__gcc_except_tab: 0x938

   __TEXT.__dlopen_cstrs: 0x2e4
   __TEXT.__unwind_info: 0xfec
   __TEXT.__objc_classname: 0x51a
-  __TEXT.__objc_methname: 0x9cbc
+  __TEXT.__objc_methname: 0x9cd2
   __TEXT.__objc_methtype: 0x13ec
   __TEXT.__objc_stubs: 0x6d80
   __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x17f0
+  __DATA_CONST.__const: 0x1818
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4ae0
   __DATA_CONST.__objc_selrefs: 0x2150
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x3b0
+  __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__objc_const: 0x1380
   __AUTH_CONST.__cfstring: 0x3240

   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x4b8
   __AUTH.__objc_data: 0x640
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x3b0
-  __DATA.__objc_superrefs: 0x118
   __DATA.__objc_ivar: 0x370
   __DATA.__data: 0x730
   __DATA.__bss: 0x130

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 930A85AC-FE99-3F50-8D70-5D5B6436CDF8
+  UUID: DA81B7B8-2F21-374A-B021-6D533F02C967
   Functions: 1435
-  Symbols:   5074
-  CStrings:  2965
+  Symbols:   5075
+  CStrings:  2966
 
Symbols:
+ ___44-[CPSDaemonConnection registerSessionProxy:]_block_invoke.127
+ ___44-[CPSDaemonConnection registerSessionProxy:]_block_invoke.127.cold.1
+ ___46-[CPSDaemonConnection unregisterSessionProxy:]_block_invoke.131
+ ___46-[CPSDaemonConnection unregisterSessionProxy:]_block_invoke.131.cold.1
+ ___51-[CPSDaemonConnection isClipURL:completionHandler:]_block_invoke.134
+ ___57-[CPSDaemonConnection openClipWithURL:completionHandler:]_block_invoke.139
+ ___57-[CPSDaemonConnection openClipWithURL:completionHandler:]_block_invoke.139.cold.1
+ ___60-[CPSDaemonConnection installClipWithURL:completionHandler:]_block_invoke.140
+ ___60-[CPSDaemonConnection prewarmClipWithURL:completionHandler:]_block_invoke.137
+ ___60-[CPSDaemonConnection prewarmClipWithURL:completionHandler:]_block_invoke.137.cold.1
+ ___62-[CPSDaemonConnection uninstallClipWithURL:completionHandler:]_block_invoke.141
+ ___64-[CPSDaemonConnection openClipWithURL:launchOptions:completion:]_block_invoke.148
+ ___64-[CPSDaemonConnection openClipWithURL:launchOptions:completion:]_block_invoke.148.cold.1
+ ___66-[CPSDaemonConnection fetchClipMetadataWithURL:completionHandler:]_block_invoke.143
+ ___69-[CPSDaemonConnection cancelPrewarmingClipWithURL:completionHandler:]_block_invoke.138
+ ___69-[CPSDaemonConnection cancelPrewarmingClipWithURL:completionHandler:]_block_invoke.138.cold.1
+ ___69-[CPSDaemonConnection uninstallClipsWithBundleIDs:completionHandler:]_block_invoke.142
+ ___72-[CPSDaemonConnection getUserNotificationConsentForBundleID:completion:]_block_invoke.149
+ ___72-[CPSDaemonConnection getUserNotificationConsentForBundleID:completion:]_block_invoke.149.cold.1
+ ___75-[CPSDaemonConnection fetchClipMetadataAndImagesWithURL:completionHandler:]_block_invoke.136
+ ___75-[CPSDaemonConnection fetchClipMetadataAndImagesWithURL:completionHandler:]_block_invoke.136.cold.1
+ ___76-[CPSDaemonConnection notifyWebClipActivationWithBundleID:referrerBundleID:]_block_invoke.153
+ ___76-[CPSDaemonConnection notifyWebClipActivationWithBundleID:referrerBundleID:]_block_invoke.153.cold.1
+ ___76-[CPSDaemonConnection stopStallingCurrentInstallationWithCompletionHandler:]_block_invoke.147
+ ___81-[CPSDaemonConnection openClipWithInvocationUIIfNeededWithURL:completionHandler:]_block_invoke.146
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.126
+ ___block_literal_global.130
+ ___block_literal_global.133
+ ___block_literal_global.152
+ ___block_literal_global.155
+ ___block_literal_global.157
+ ___block_literal_global.159
+ ___block_literal_global.161
- ___44-[CPSDaemonConnection registerSessionProxy:]_block_invoke.126
- ___44-[CPSDaemonConnection registerSessionProxy:]_block_invoke.126.cold.1
- ___46-[CPSDaemonConnection unregisterSessionProxy:]_block_invoke.130
- ___46-[CPSDaemonConnection unregisterSessionProxy:]_block_invoke.130.cold.1
- ___51-[CPSDaemonConnection isClipURL:completionHandler:]_block_invoke.133
- ___57-[CPSDaemonConnection openClipWithURL:completionHandler:]_block_invoke.138
- ___57-[CPSDaemonConnection openClipWithURL:completionHandler:]_block_invoke.138.cold.1
- ___60-[CPSDaemonConnection installClipWithURL:completionHandler:]_block_invoke.139
- ___60-[CPSDaemonConnection prewarmClipWithURL:completionHandler:]_block_invoke.136
- ___60-[CPSDaemonConnection prewarmClipWithURL:completionHandler:]_block_invoke.136.cold.1
- ___62-[CPSDaemonConnection uninstallClipWithURL:completionHandler:]_block_invoke.140
- ___64-[CPSDaemonConnection openClipWithURL:launchOptions:completion:]_block_invoke.147
- ___64-[CPSDaemonConnection openClipWithURL:launchOptions:completion:]_block_invoke.147.cold.1
- ___66-[CPSDaemonConnection fetchClipMetadataWithURL:completionHandler:]_block_invoke.142
- ___69-[CPSDaemonConnection cancelPrewarmingClipWithURL:completionHandler:]_block_invoke.137
- ___69-[CPSDaemonConnection cancelPrewarmingClipWithURL:completionHandler:]_block_invoke.137.cold.1
- ___69-[CPSDaemonConnection uninstallClipsWithBundleIDs:completionHandler:]_block_invoke.141
- ___72-[CPSDaemonConnection getUserNotificationConsentForBundleID:completion:]_block_invoke.148
- ___72-[CPSDaemonConnection getUserNotificationConsentForBundleID:completion:]_block_invoke.148.cold.1
- ___75-[CPSDaemonConnection fetchClipMetadataAndImagesWithURL:completionHandler:]_block_invoke.135
- ___75-[CPSDaemonConnection fetchClipMetadataAndImagesWithURL:completionHandler:]_block_invoke.135.cold.1
- ___76-[CPSDaemonConnection notifyWebClipActivationWithBundleID:referrerBundleID:]_block_invoke.152
- ___76-[CPSDaemonConnection notifyWebClipActivationWithBundleID:referrerBundleID:]_block_invoke.152.cold.1
- ___76-[CPSDaemonConnection stopStallingCurrentInstallationWithCompletionHandler:]_block_invoke.146
- ___81-[CPSDaemonConnection openClipWithInvocationUIIfNeededWithURL:completionHandler:]_block_invoke.145
- ___block_literal_global.124
- ___block_literal_global.129
- ___block_literal_global.132
- ___block_literal_global.151
- ___block_literal_global.154
- ___block_literal_global.156
- ___block_literal_global.158
- ___block_literal_global.160
CStrings:
+ "T@\"NSString\",?,R,C"

```
