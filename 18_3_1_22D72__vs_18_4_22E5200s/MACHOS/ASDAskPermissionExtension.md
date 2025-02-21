## ASDAskPermissionExtension

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDAskPermissionExtension.appex/ASDAskPermissionExtension`

```diff

-11.2.30.0.0
-  __TEXT.__text: 0x5ac
-  __TEXT.__auth_stubs: 0x130
-  __TEXT.__objc_stubs: 0x220
+11.4.17.2.1
+  __TEXT.__text: 0x908
+  __TEXT.__auth_stubs: 0x170
+  __TEXT.__objc_stubs: 0x280
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x18
-  __TEXT.__oslogstring: 0x177
+  __TEXT.__const: 0x28
+  __TEXT.__oslogstring: 0x2a3
   __TEXT.__cstring: 0x41
   __TEXT.__objc_classname: 0x1e
-  __TEXT.__objc_methname: 0x152
+  __TEXT.__objc_methname: 0x1a0
   __TEXT.__objc_methtype: 0x17
-  __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x68
+  __TEXT.__unwind_info: 0x60
+  __DATA_CONST.__auth_got: 0xc0
+  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__const: 0x50
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x98
+  __DATA.__objc_selrefs: 0xb0
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
   - /System/Library/PrivateFrameworks/AskPermission.framework/AskPermission
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 4
-  Symbols:   36
-  CStrings:  33
+  Symbols:   41
+  CStrings:  37
 
Symbols:
+ _MCFeatureAppInstallationAllowed
+ _OBJC_CLASS_$_MCProfileConnection
+ _objc_opt_class
+ _objc_release_x24
+ _objc_retain
+ _objc_retain_x22
- __NSConcreteGlobalBlock
CStrings:
+ "[%{public}@] AskPermission updated request for unhandled product type '%{public}@'"
+ "[%{public}@] Download failed. Error: %{public}@"
+ "[%{public}@] Download queue request complete with result: %{BOOL}d"
+ "[%{public}@] Download queue request returned error: %{public}@"
+ "[%{public}@] Download succeeded. Response items: %{public}@"
+ "[%{public}@] Failing family purchase request due to permission setting(s)."
+ "[%{public}@] Processing purchase. Purchase: %{public}@"
+ "[%{public}@] Request to check download queue received. appInstallsAllowed: %{BOOL}d autoDownloadsAllowed: %{BOOL}d"
+ "[%{public}@] Request updated. appInstallsAllowed: %{BOOL}d autoDownloadsAllowed: %{BOOL}d result: %{public}@"
+ "effectiveBoolValueForSetting:"
+ "isAutomaticAppDownloadsAllowed"
+ "sharedConnection"
- "AskPermission updated request for unhandled product type '%{public}@'"
- "Download failed. Error: %{public}@"
- "Download queue request complete with result: %{BOOL}d"
- "Download queue request returned error: %{public}@"
- "Download succeeded. Response items: %{public}@"
- "Processing purchase. Purchase: %{public}@"
- "Request to check download queue received"
- "Request updated. Result: %{public}@"

```
