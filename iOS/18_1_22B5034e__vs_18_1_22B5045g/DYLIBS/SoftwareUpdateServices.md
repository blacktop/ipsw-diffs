## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-868.0.0.0.0
-  __TEXT.__text: 0xaaf68
+868.40.5.0.0
+  __TEXT.__text: 0xac7bc
   __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x91e8
-  __TEXT.__cstring: 0x1e0c1
+  __TEXT.__objc_methlist: 0x9308
+  __TEXT.__cstring: 0x1e421
   __TEXT.__const: 0x2a0
-  __TEXT.__gcc_except_tab: 0xf78
+  __TEXT.__gcc_except_tab: 0x1064
   __TEXT.__oslogstring: 0xd48
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x2fe8
-  __TEXT.__objc_classname: 0xece
-  __TEXT.__objc_methname: 0x17c0a
-  __TEXT.__objc_methtype: 0x34a8
-  __TEXT.__objc_stubs: 0x13520
-  __DATA_CONST.__got: 0xd50
-  __DATA_CONST.__const: 0x2910
-  __DATA_CONST.__objc_classlist: 0x3c8
-  __DATA_CONST.__objc_catlist: 0x38
+  __TEXT.__unwind_info: 0x3088
+  __TEXT.__objc_classname: 0xee5
+  __TEXT.__objc_methname: 0x17d3e
+  __TEXT.__objc_methtype: 0x34d2
+  __TEXT.__objc_stubs: 0x13640
+  __DATA_CONST.__got: 0xd58
+  __DATA_CONST.__const: 0x2948
+  __DATA_CONST.__objc_classlist: 0x3d0
+  __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5658
+  __DATA_CONST.__objc_selrefs: 0x56a8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x310
-  __DATA_CONST.__objc_arraydata: 0xb8
+  __DATA_CONST.__objc_superrefs: 0x318
+  __DATA_CONST.__objc_arraydata: 0xd8
   __AUTH_CONST.__auth_got: 0x7a0
-  __AUTH_CONST.__const: 0x800
-  __AUTH_CONST.__cfstring: 0x11da0
-  __AUTH_CONST.__objc_const: 0x17e40
+  __AUTH_CONST.__const: 0x7e0
+  __AUTH_CONST.__cfstring: 0x120a0
+  __AUTH_CONST.__objc_const: 0x17ee0
   __AUTH_CONST.__objc_intobj: 0x258
-  __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x1018
-  __DATA.__objc_ivar: 0x918
+  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__objc_arrayobj: 0x120
+  __AUTH.__objc_data: 0x1068
+  __DATA.__objc_ivar: 0x928
   __DATA.__data: 0xef8
   __DATA.__bss: 0x108
   __DATA_DIRTY.__objc_data: 0x15b8

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libReverseProxyDevice.dylib

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4278
-  Symbols:   5349
-  CStrings:  7360
+  Functions: 4311
+  Symbols:   5384
+  CStrings:  7403
 
Symbols:
+ _OBJC_CLASS_$_SUCellularFeeAlertItem
+ _OBJC_METACLASS_$_SUCellularFeeAlertItem
+ _kSUNotifyUserKey
CStrings:
+ "Current network: %!@(MISSING)"
+ "@40@0:8@?16@24@32"
+ "download did fail"
+ "[ANOMALY] Download faild but the download object is nil"
+ "_handleExistingDownload:targetUpdate:"
+ "download policy doesn't allow downloading over cellular"
+ "download did finish"
+ "Download %!@(MISSING) to start. Error: %!@(MISSING)"
+ "Download policy doesn't allow downloading over cellular; try again later..."
+ "[%!@(MISSING)] User declined to use cellular."
+ "-[SUDDMManager downloadDidFail:withError:]"
+ "overrideCarrierDownloadPolicyProperties"
+ "download failed"
+ "download failed to start"
+ "No network connection; try again later..."
+ "_copyDictPreferenceForKey:"
+ "safeStringForKey:"
+ "SUOverrideCarrierDownloadPolicyProperties"
+ "_updateName"
+ "_getOverriddenProperties"
+ "Schedule to retry downloading on %!@(MISSING) for reason: %!@(MISSING)"
+ "download did finish: %!@(MISSING), install policy: %!@(MISSING)"
+ "No target update; not handling the download"
+ "Current download is what is encforced"
+ "B44@0:8B16B20B24@28^@36"
+ "isArmed"
+ "_downloadScheduler"
+ "_cachedDictValueForKey:"
+ "setTimeStyle:"
+ "_scheduleDownloadRetryForReason:"
+ "initWithHandler:updateName:dueDate:"
+ "_dueDate"
+ "Override carrier download policy properties. Don't set via sus_tool; use defaults write instead"
+ "_downloadInvalidatedWithUpdates:"
+ "-[SUDDMManager downloadDidStart:]"
+ "device is considered cellular capable because networkMonitorOverride (%!d(MISSING)) exists"
+ "SUNotifyUser"
+ "SUCellularFeeAlertItem"
+ "-[SUDDMManager _scheduleDownloadRetryForReason:]"
+ "download did start: %!@(MISSING)"
+ "currently no network connection"
+ "Cancel scheduled download retry for reason: %!@(MISSING)"
+ "MANAGED_UPDATE"
+ "_cancelScheduledDownloadRetryForReason:"
+ "download did fail: %!@(MISSING), error: %!@(MISSING)"
+ "download did start"
+ "CELLULAR_DOWNLOAD_ACCEPT_DEFINITE_FEES_FOR_MANAGED_UPDATE"
+ "-[SUDDMManager _cancelScheduledDownloadRetryForReason:]"
+ "com.apple.sus.ddm.download"
+ "download was killed"
+ "com.apple.springboard"
+ "[PREFERENCES] Override properties with %!@(MISSING)"
+ "CONTINUE"
+ "killDownload:userRequested:keepDocAssets:forUpdates:error:"
+ "-[SUDDMManager downloadDidFinish:withInstallPolicy:]"
+ "[ANOMALY] shouldn't have any previously scheduled activity!"
+ "\n"
+ "_keys"
+ "-[SUDDMManager _handleExistingDownload:targetUpdate:]"
+ "Download already exists: %!l(MISSING)d"
+ "No download"
+ "[%!@(MISSING)] User accepted to use cellular."
- "Overdue. Promoting download and allowing countdown alert"
- "updateDownloadOptions finished (result: %!d(MISSING) ; error: %!@(MISSING))"
- "The current download is what we want."
- "Triggerring installation"
- "Download started with result %!d(MISSING). Error: %!@(MISSING)"
- "-[SUDDMManager postDownloadEventWithDownload:withInstallPolicy:]_block_invoke"
- "_handleExistingDownload:"
- "Download failed to start  :_( (see error above)"
- "Cannnot handle existing download for a null update"
- "-[SUDDMManager _handleExistingDownload:]"
- "\t"
- "sendDownloadInvalidatedForNewDescriptors:"
- "Previous download invalidated/destroyed for new update."
- "postDownloadEventWithDownload:withInstallPolicy:"
- "-[SUDDMManager _handleExistingDownload:]_block_invoke"
- "enforcedInstallDate is: %!@(MISSING)"
- "Not past enforced install date. We'll wait for timer to fire"
- "isInstallOverdue"
- "No need to do anything: current declaration: %!@(MISSING), current update to download: %!@(MISSING)"

```
