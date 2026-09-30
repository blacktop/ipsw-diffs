## ManifestStorageService

> `/System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/XPCServices/ManifestStorageService.xpc/Contents/MacOS/ManifestStorageService`

```diff

-1329.80.16.0.0
-  __TEXT.__text: 0x2cc4
-  __TEXT.__auth_stubs: 0x2b0
+1487.101.2.0.0
+  __TEXT.__text: 0x371c
+  __TEXT.__auth_stubs: 0x270
   __TEXT.__objc_stubs: 0x880
-  __TEXT.__objc_methlist: 0x234
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x1094
-  __TEXT.__objc_methname: 0xb03
+  __TEXT.__objc_methlist: 0x384
+  __TEXT.__const: 0xa0
+  __TEXT.__cstring: 0x89c
+  __TEXT.__oslogstring: 0x57a
+  __TEXT.__objc_methname: 0xadd
   __TEXT.__objc_classname: 0xb9
   __TEXT.__objc_methtype: 0x2bc
-  __TEXT.__oslogstring: 0x17
-  __TEXT.__gcc_except_tab: 0xb4
+  __TEXT.__gcc_except_tab: 0x124
   __TEXT.__unwind_info: 0x120
-  __DATA_CONST.__auth_got: 0x168
+  __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x160
-  __DATA_CONST.__cfstring: 0x1020
+  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__cfstring: 0xcc0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x2b8
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x7c8
-  __DATA.__objc_selrefs: 0x2b0
+  __DATA.__objc_const: 0x568
+  __DATA.__objc_selrefs: 0x350
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x120
-  __DATA.__bss: 0x43
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/Versions/A/SoftwareUpdateCoreSupport
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 214E8BA2-59B5-37B2-882B-02ED5EDBEA8C
-  Functions: 68
-  Symbols:   89
-  CStrings:  457
+  UUID: B999B47A-6C6A-315B-8271-E2056D022F6C
+  Functions: 62
+  Symbols:   82
+  CStrings:  418
 
Symbols:
+ _OBJC_CLASS_$_SUCore
+ __MAClientLog
- _NSLog
- _OBJC_CLASS_$_NSFileHandle
- __MobileAssetLog
- __os_log_debug_impl
- __os_log_error_impl
- _logDebug
- _logError
- _logInfo
- _objc_alloc
CStrings:
+ "%{public}@:<<<<<<<<<<\n%{public}@%{public}@:>>>>>>>>>>"
+ "20:53:34"
+ "Asset type (%{public}@) or specifier (%{public}@) missing"
+ "Asset type is unsupported: %{public}@"
+ "Authenticated plist: %{public}@"
+ "Auto"
+ "AutoSet"
+ "AutoStager"
+ "Brain"
+ "Client connected: %{public}@"
+ "Client disconnected: %{public}@"
+ "Commit %{public}s -> %{public}s failed: %d %{public}s"
+ "Commit %{public}s -> %{public}s succeeded"
+ "Commit failed: %{public}@"
+ "Connection interrupted: %{public}@"
+ "DEFAULT"
+ "ERROR: Invalid string passed to %{public}s"
+ "Failed to create containing directory: %{public}@"
+ "Failed to deserialize info plist: %{public}@"
+ "Failed to flash manifest: %d (%{public}s)"
+ "Ignoring ENOENT for %{public}@"
+ "Invalid selector: %{public}@"
+ "Invalidating manifest for %{public}@:%{public}@"
+ "KeyManager"
+ "Manifest"
+ "Mar 10 2025"
+ "Missing asset type (%{public}@) or specifier (%{public}@)"
+ "Plist trust evaluation failed: %d (%{public}s)"
+ "PushNotification"
+ "Rejecting incoming XPC connection: %{public}@"
+ "Remove failed: %{public}@"
+ "Removing %{public}@"
+ "SSO"
+ "SecureMA"
+ "Selector missing type or specifier: %{public}@"
+ "Staged manifest does not exist: %{public}@"
+ "Starting with MobileAsset-%{public}s (built %{public}s %{public}s)"
+ "Store failed: %{public}@"
+ "UTF8String"
+ "V2"
+ "Wrote manifest to %{public}@"
+ "com.apple.MobileAsset"
+ "objectForKey:"
+ "sharedCore"
+ "useDomain:"
- "\n"
- "%@"
- "%@:<<<<<<<<<<\n%@%@:>>>>>>>>>>"
- "%{public}s: %{public}@"
- "-[MAManifestStorageService _authenticatePlist:manifest:result:]"
- "-[MAManifestStorageService _flashManifest:]"
- "-[MAManifestStorageService _logBase64Data:description:]"
- "-[MAManifestStorageService _parseSelector:assetType:specifier:]"
- "-[MAManifestStorageService _writeManifest:destination:error:]"
- "-[MAManifestStorageService commitStagedManifestsForSelectors:]"
- "-[MAManifestStorageService commitStagedManifestsForSelectors:completion:]_block_invoke"
- "-[MAManifestStorageService invalidateManifestForAssetType:specifier:]"
- "-[MAManifestStorageService invalidateManifestForAssetType:specifier:completion:]_block_invoke"
- "-[MAManifestStorageService storeManifest:infoPlist:stage:]"
- "-[MAManifestStorageService storeManifest:infoPlist:stage:completion:]_block_invoke"
- "-[MAManifestStorageServiceDelegate listener:shouldAcceptNewConnection:]"
- "-[MAManifestStorageServiceDelegate listener:shouldAcceptNewConnection:]_block_invoke"
- "-[MASecureMobileAssetTypes _loadTypes]"
- "15:56:57"
- "Asset type (%@) or specifier (%@) missing"
- "Asset type is unsupported: %@"
- "Authenticated plist: %@"
- "Client connected: %@"
- "Client disconnected: %@"
- "Commit %s -> %s failed: %d %s"
- "Commit %s -> %s succeeded"
- "Commit failed: %@"
- "Connection interrupted: %@"
- "Debug"
- "Dec 16 2024"
- "ERROR: Invalid string passed to %s"
- "Error"
- "Failed to create containing directory: %@"
- "Failed to deserialize info plist: %@"
- "Failed to flash manifest: %d (%s)"
- "Ignoring ENOENT for %@"
- "Invalid selector: %@"
- "Invalidating manifest for %@:%@"
- "Missing asset type (%@) or specifier (%@)"
- "Notice"
- "Plist trust evaluation failed: %d (%s)"
- "Rejecting incoming XPC connection: %@"
- "Remove failed: %@"
- "Removing %@"
- "Selector missing type or specifier: %@"
- "Staged manifest does not exist: %@"
- "Starting with MobileAsset-%s (built %s %s)"
- "Store failed: %@"
- "Unable to allocate log message"
- "Wrote manifest to %@"
- "_plist_trust_callback"
- "com.apple.mobileassetd"
- "dataUsingEncoding:"
- "fileHandleWithStandardOutput"
- "initWithFormat:arguments:"
- "main"
- "writeData:"

```
