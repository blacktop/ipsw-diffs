## CoreUARP

> `/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP`

```diff

-1338.0.21.0.2
-  __TEXT.__text: 0x8b154
-  __TEXT.__auth_stubs: 0xa20
-  __TEXT.__objc_methlist: 0x8b34
+1338.0.37.0.0
+  __TEXT.__text: 0x8a6dc
+  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__objc_methlist: 0x8b3c
   __TEXT.__const: 0x220
-  __TEXT.__cstring: 0x7c29
-  __TEXT.__oslogstring: 0x656f
-  __TEXT.__gcc_except_tab: 0x8b4
-  __TEXT.__dlopen_cstrs: 0x10e
+  __TEXT.__cstring: 0x7b1a
+  __TEXT.__oslogstring: 0x646a
+  __TEXT.__gcc_except_tab: 0x88c
+  __TEXT.__dlopen_cstrs: 0xa4
   __TEXT.__unwind_info: 0x2588
   __TEXT.__objc_classname: 0x18d0
-  __TEXT.__objc_methname: 0xe0af
+  __TEXT.__objc_methname: 0xe0ca
   __TEXT.__objc_methtype: 0x3f03
-  __TEXT.__objc_stubs: 0x9800
+  __TEXT.__objc_stubs: 0x97c0
   __DATA_CONST.__got: 0x758
-  __DATA_CONST.__const: 0x2098
+  __DATA_CONST.__const: 0x2080
   __DATA_CONST.__objc_classlist: 0x688
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3148
+  __DATA_CONST.__objc_selrefs: 0x3150
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x678
-  __AUTH_CONST.__auth_got: 0x520
+  __AUTH_CONST.__auth_got: 0x510
   __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x7360
-  __AUTH_CONST.__objc_const: 0x11a88
+  __AUTH_CONST.__cfstring: 0x7180
+  __AUTH_CONST.__objc_const: 0x11a68
   __AUTH_CONST.__objc_intobj: 0xca8
   __AUTH.__objc_data: 0x2080
-  __DATA.__objc_ivar: 0xbc4
+  __DATA.__objc_ivar: 0xbc0
   __DATA.__data: 0x40d
-  __DATA.__bss: 0x1a5b
+  __DATA.__bss: 0x1a4b
   __DATA_DIRTY.__objc_data: 0x20d0
   __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 792D0C57-DD30-3A6B-B26A-21DA10BB425D
-  Functions: 3906
-  Symbols:   12415
-  CStrings:  5849
+  UUID: 86628419-2F1E-364F-993E-0296A04751FB
+  Functions: 3900
+  Symbols:   12392
+  CStrings:  5811
 
Symbols:
+ -[UARPUploaderEndpoint solicitLogsDynamicAssetForEndpoint:]
+ -[UARPUploaderEndpoint solicitLogsDynamicAssetForTTR]
+ GCC_except_table34
+ _objc_msgSend$solicitLogsDynamicAssetForEndpoint:
+ _objc_msgSend$solicitLogsDynamicAssetForTTR
- -[UARPDynamicAssetCrashLogEvent decomposeUARP].cold.2
- -[UARPDynamicAssetCrashLogEvent decomposeUARP].cold.3
- -[UARPDynamicAssetCrashLogEvent expandCRSHPayloads]
- -[UARPDynamicAssetCrashLogEvent expandCRSHPayloads].cold.1
- -[UARPDynamicAssetCrashLogEvent expandCRSHPayloads].cold.2
- -[UARPDynamicAssetCrashLogEvent processCrashInstance].cold.1
- -[UARPDynamicAssetCrashLogEvent processCrashInstance].cold.2
- _OBJC_IVAR_$_UARPDynamicAssetCrashLogEvent._processedCrashLogs
- _RTBuddyCrashlogDecoderLibraryCore.frameworkLibrary
- ___RTBuddyCrashlogDecoderLibraryCore_block_invoke
- ___getRTBuddyCrashlogDecodeSymbolLoc_block_invoke
- _audit_stringRTBuddyCrashlogDecoder
- _dlerror
- _dlsym
- _getRTBuddyCrashlogDecodeSymbolLoc.ptr
- _objc_msgSend$expandCRSHPayloads
- _objc_msgSend$expandCrshData:withAppleModelNumber:
- _objc_msgSend$findMatchingCMAP
- _objc_msgSend$sendSpeedTracer
CStrings:
+ "Failed to process CRSH Payloads."
+ "solicitLogsDynamicAssetForEndpoint:"
+ "solicitLogsDynamicAssetForTTR"
- "1.0"
- "Could not produce output JSON for Crash Instance: %@"
- "Failed to expand CRSH Payloads."
- "Failed to find matching CMAP. Saving for Later Processing."
- "RTBuddyCrashlogDecode"
- "RTKitBuddy unable to decode Crash Log"
- "Successfully expanded CRSH Dynamic Asset: %@"
- "US"
- "Unable to expand CRSH Data for: %@"
- "Unable to expand Crash Payloads"
- "_processedCrashLogs"
- "accessory_crashreporter_key"
- "accessory_fusing"
- "accessory_machine_config"
- "accessory_os_train"
- "accessory_os_version"
- "accessory_release_type"
- "audio"
- "case"
- "expandCRSHPayloads"
- "role"
- "side"
- "softlink:o:path:/System/Library/PrivateFrameworks/RTBuddyCrashlogDecoder.framework/RTBuddyCrashlogDecoder"
- "usage_since_last_crash"
- "usage_since_last_crash_in_ear"
- "usage_since_last_crash_user_facing"

```
