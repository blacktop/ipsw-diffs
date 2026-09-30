## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-631.80.9.0.0
-  __TEXT.__text: 0x8b43c
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__objc_stubs: 0x8180
-  __TEXT.__objc_methlist: 0x4278
-  __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x122a7
-  __TEXT.__objc_classname: 0x7f8
-  __TEXT.__objc_methname: 0xda7f
-  __TEXT.__oslogstring: 0x9d8e
-  __TEXT.__objc_methtype: 0x1d4a
-  __TEXT.__gcc_except_tab: 0x25c0
+699.100.10.0.0
+  __TEXT.__text: 0x8c6a8
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__objc_stubs: 0x8340
+  __TEXT.__objc_methlist: 0x4d84
+  __TEXT.__const: 0x1c0
+  __TEXT.__cstring: 0x124d1
+  __TEXT.__objc_methname: 0xdd9d
+  __TEXT.__objc_classname: 0x80d
+  __TEXT.__objc_methtype: 0x1d72
+  __TEXT.__oslogstring: 0x9ddd
+  __TEXT.__gcc_except_tab: 0x2608
   __TEXT.__ustring: 0x26a
-  __TEXT.__unwind_info: 0x1f88
-  __DATA_CONST.__auth_got: 0x608
-  __DATA_CONST.__got: 0x2d0
+  __TEXT.__unwind_info: 0x1fe0
+  __DATA_CONST.__auth_got: 0x600
+  __DATA_CONST.__got: 0x2d8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2360
-  __DATA_CONST.__cfstring: 0x6d80
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__const: 0x23b8
+  __DATA_CONST.__cfstring: 0x6f00
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0xc0
-  __DATA.__objc_const: 0xb6b0
-  __DATA.__objc_selrefs: 0x2800
-  __DATA.__objc_ivar: 0x3e0
-  __DATA.__objc_data: 0x1180
+  __DATA.__objc_const: 0xa6f0
+  __DATA.__objc_selrefs: 0x2910
+  __DATA.__objc_ivar: 0x3fc
+  __DATA.__objc_data: 0x11d0
   __DATA.__data: 0x5f0
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x170

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 585F9F3A-5AA8-3327-8BA9-3CB30AC5F5A6
-  Functions: 2754
+  UUID: 86C16913-D2DD-3340-B567-C32E80FD3358
+  Functions: 2785
   Symbols:   295
-  CStrings:  5177
+  CStrings:  5236
 
Symbols:
+ __kCFBundleShortVersionStringKey
- _strcmp
CStrings:
+ "%s: Call to %@ SPI returned retryable error %@; retrying in %d seconds (%lu/%lu tries)"
+ "%s: Unexpectedly found existing power assertion for background scheduled update: %@"
+ "-[IXSCoordinatedAppInstall _onQueue_gizmoInstallForInstallOptions:appAssetAtPath:]"
+ "-[IXSCoordinatedAppInstall _shouldRetryInstallAttemptBasedOnPreviousResult:returnedError:targetInstallURL:retriesAttempted:totalRetries:]"
+ "-[IXSCoordinatedAppInstall scheduledAppUpdateReadyToExecuteAndRunBlockWhenComplete:]"
+ "02:57:54"
+ "@40@0:8@16Q24Q32"
+ "B52@0:8B16@20@28Q36Q44"
+ "Failed to stage background update."
+ "IXAppCoordinationStateReadyForStaging"
+ "IXAppCoordinationStateStagingPending"
+ "IXDefaultAppMetadata"
+ "Mar  8 2025"
+ "NSAccentColorName"
+ "T@\"IXApplicationIdentity\",R,N,V_identity"
+ "T@\"NSDictionary\",C,N,V_uiLaunchScreen"
+ "T@\"NSString\",&,N,V_stagedUpdateIdentifier"
+ "T@\"NSString\",C,N,V_accentColorName"
+ "T@\"NSString\",C,N,V_bundleShortVersionString"
+ "TQ,R,N,V_appType"
+ "TQ,R,N,V_offloadAnswer"
+ "UILaunchScreen"
+ "_accentColorName"
+ "_appType"
+ "_bundleShortVersionString"
+ "_isStagedUpdate"
+ "_offloadAnswer"
+ "_onQueue_gizmoInstallForInstallOptions:appAssetAtPath:"
+ "_shouldRetryInstallAttemptBasedOnPreviousResult:returnedError:targetInstallURL:retriesAttempted:totalRetries:"
+ "_stagedUpdateIdentifier"
+ "_uiLaunchScreen"
+ "accentColorName"
+ "appType"
+ "bundleShortVersionString"
+ "initWithAppIdentity:appType:offloadAnswer:"
+ "install"
+ "offloadAnswer"
+ "setAccentColorName:"
+ "setBundleShortVersionString:"
+ "setStagedUpdateIdentifier:"
+ "setUiLaunchScreen:"
+ "stage update"
+ "stagedUpdateIdentifier"
+ "trackingStagedUpdateIdentifier"
+ "uiLaunchScreen"
+ "\xf0a"
- "%s: Call to install SPI returned retryable error %@; retrying in %d seconds (%lu/%lu tries)"
- "02:39:54"
- "Dec 14 2024"
- "PPBundleMetadata"
- "\xf0Q"

```
