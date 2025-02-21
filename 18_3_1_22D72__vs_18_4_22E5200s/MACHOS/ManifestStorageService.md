## ManifestStorageService

> `/System/Library/PrivateFrameworks/MobileAsset.framework/XPCServices/ManifestStorageService.xpc/ManifestStorageService`

```diff

-1329.82.1.0.0
-  __TEXT.__text: 0x27f4
-  __TEXT.__auth_stubs: 0x3f0
+1487.100.54.502.2
+  __TEXT.__text: 0x3128
+  __TEXT.__auth_stubs: 0x3b0
   __TEXT.__objc_stubs: 0x880
-  __TEXT.__objc_methlist: 0x234
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x10f4
-  __TEXT.__objc_methname: 0xb03
+  __TEXT.__objc_methlist: 0x384
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0x8a5
+  __TEXT.__oslogstring: 0x57a
+  __TEXT.__objc_methname: 0xadd
   __TEXT.__objc_classname: 0xb9
   __TEXT.__objc_methtype: 0x2bc
-  __TEXT.__oslogstring: 0x17
-  __TEXT.__gcc_except_tab: 0xb4
-  __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__auth_got: 0x208
+  __TEXT.__gcc_except_tab: 0x124
+  __TEXT.__unwind_info: 0x110
+  __DATA_CONST.__auth_got: 0x1e8
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x140
-  __DATA_CONST.__cfstring: 0x1020
+  __DATA_CONST.__const: 0x100
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
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 62
-  Symbols:   109
-  CStrings:  331
+  Functions: 56
+  Symbols:   102
+  CStrings:  318
 
Symbols:
+ _OBJC_CLASS_$_SUCore
+ __MAClientLog
+ _objc_release_x9
- _NSLog
- _OBJC_CLASS_$_NSFileHandle
- __MobileAssetLog
- __os_log_debug_impl
- __os_log_error_impl
- _logDebug
- _logError
- _logInfo
- _objc_alloc
- _objc_release
CStrings:
+ "%{public}@:<<<<<<<<<<\n%{public}@%{public}@:>>>>>>>>>>"
+ "23:50:16"
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
+ "Feb 17 2025"
+ "Ignoring ENOENT for %{public}@"
+ "Invalid selector: %{public}@"
+ "Invalidating manifest for %{public}@:%{public}@"
+ "KeyManager"
+ "Manifest"
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
- "-[MAManifestStorageServiceDelegate listener:shouldAcceptNewConnection:]_block_invoke_2"
- "-[MASecureMobileAssetTypes _loadTypes]"
- "03:22:04"
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
- "ERROR: Invalid string passed to %s"
- "Error"
- "Failed to create containing directory: %@"
- "Failed to deserialize info plist: %@"
- "Failed to flash manifest: %d (%s)"
- "Ignoring ENOENT for %@"
- "Invalid selector: %@"
- "Invalidating manifest for %@:%@"
- "Jan 16 2025"
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
