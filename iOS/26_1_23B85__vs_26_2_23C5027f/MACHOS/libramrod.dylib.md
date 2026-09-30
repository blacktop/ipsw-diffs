## libramrod.dylib

> `/usr/lib/libramrod.dylib`

```diff

-3476.40.39.0.0
-  __TEXT.__text: 0xdbdc4
-  __TEXT.__auth_stubs: 0x28b0
+3476.60.7.0.1
+  __TEXT.__text: 0xdcba0
+  __TEXT.__auth_stubs: 0x28e0
   __TEXT.__objc_methlist: 0x1164
-  __TEXT.__cstring: 0x28513
-  __TEXT.__const: 0x94950
+  __TEXT.__cstring: 0x28982
+  __TEXT.__const: 0x94948
   __TEXT.__gcc_except_tab: 0xbc4
-  __TEXT.__oslogstring: 0xab1
-  __TEXT.__unwind_info: 0x1d00
+  __TEXT.__oslogstring: 0xab4
+  __TEXT.__unwind_info: 0x1d28
   __TEXT.__eh_frame: 0x3c0
   __TEXT.__objc_classname: 0x195
   __TEXT.__objc_methname: 0x2940
   __TEXT.__objc_methtype: 0xb65
   __TEXT.__objc_stubs: 0x2880
-  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x1f80
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xca8
-  __AUTH_CONST.__auth_got: 0x1470
-  __AUTH_CONST.__const: 0x1fe0
-  __AUTH_CONST.__cfstring: 0xb740
+  __AUTH_CONST.__auth_got: 0x1488
+  __AUTH_CONST.__const: 0x2020
+  __AUTH_CONST.__cfstring: 0xb9e0
   __AUTH_CONST.__objc_const: 0x1aa0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x5a0

   __DATA.__objc_superrefs: 0x80
   __DATA.__objc_ivar: 0x134
   __DATA.__data: 0x2198
-  __DATA.__bss: 0x850
+  __DATA.__bss: 0x868
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib
-  UUID: 09E4E974-F18D-3054-B0BB-F06E9BDAFA93
-  Functions: 2632
-  Symbols:   1814
-  CStrings:  7375
+  UUID: C28C8D73-51A7-3369-8F8E-EDE1DCC43386
+  Functions: 2659
+  Symbols:   1819
+  CStrings:  7434
 
Symbols:
+ _AMAuthInstallCreate
+ _AMAuthInstallSupportGetValueForKeyWithFormat
+ _AMAuthInstallUpdaterSetInfoWithUARPCallbacks
+ _kAMAuthInstallErrorDomain
+ _ramrod_update_copy_deviceinfo_with_payload
CStrings:
+ "%@ has no tags provided by the host"
+ "%s/applelogo@2340~iphone.tga"
+ "%s: Failed to allocate requestsDict"
+ "%s: Failed to allocate space for keys/values\n"
+ "%s: Failed to allocate tagsDict"
+ "%s: Tethred preflight payload didn't include BuildIdentity"
+ "%s: buildIdentityTags is NULL"
+ "%s: buildIdentityTags not CFArray"
+ "%s: ctx is NULL"
+ "%s: ctx->func_execCmd is NULL"
+ "%s: ctx->updaterRef is NULL"
+ "%s: error is NULL"
+ "%s: failed to allocate dictionary for queryPersonalizationInfo input"
+ "%s: failed to execute %@"
+ "%s: out dictionary from updater is null or malformed for %@"
+ "%s: requestedEntries is NULL"
+ "BuildIdentityTags"
+ "DeviceInfoRequests"
+ "DeviceInfoTags"
+ "Failed to set personalization info for %s"
+ "FirmwareData"
+ "Host asked for preflight personalization for this updater"
+ "Manifest.%@"
+ "No data was provided from the host for tag %@"
+ "No tethered preflight payload provided"
+ "Starting %s...\n"
+ "Supports DeviceRestoreInfo, but not setting ForceRepersonalization.\n"
+ "TetheredPreflightPayload"
+ "_ramrod_copy_build_identity_callback"
+ "_ramrod_copy_files_from_bundle_callback"
+ "_ramrod_query_personalization_info_callback"
+ "amai is NULL"
+ "buildIdentityTags is NULL"
+ "com.apple.RestoreRemoteServices.restoreservice"
+ "queryPersonalizationInfo"
+ "ramrod"
+ "ramrod_update_copy_deviceinfo_with_payload"
+ "responseDict is NULL"
- "Supports DeviceRestoreInfo, setting ForceRepersonalization and skipping preflightTickets query for tethered restore."

```
