## restoreserviced

> `/usr/libexec/restoreserviced`

```diff

-41.0.0.0.0
-  __TEXT.__text: 0x13950
-  __TEXT.__auth_stubs: 0xe20
+43.0.0.0.0
+  __TEXT.__text: 0x146f0
+  __TEXT.__auth_stubs: 0xea0
   __TEXT.__objc_stubs: 0x1760
   __TEXT.__objc_methlist: 0xcac
   __TEXT.__const: 0xb7c
-  __TEXT.__cstring: 0x74f7
-  __TEXT.__oslogstring: 0x34d
+  __TEXT.__cstring: 0x7977
+  __TEXT.__oslogstring: 0x374
   __TEXT.__gcc_except_tab: 0x218
   __TEXT.__objc_methname: 0x17c1
   __TEXT.__objc_classname: 0x10f
   __TEXT.__objc_methtype: 0x789
-  __TEXT.__unwind_info: 0x568
-  __DATA_CONST.__auth_got: 0x720
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0xc78
-  __DATA_CONST.__cfstring: 0x3760
+  __TEXT.__unwind_info: 0x588
+  __DATA_CONST.__auth_got: 0x760
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0xcb8
+  __DATA_CONST.__cfstring: 0x3a40
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x18

   __DATA.__objc_ivar: 0xe0
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x618
-  __DATA.__bss: 0xc8
+  __DATA.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 88C39322-8CAF-390B-BC7F-32BE0178D6D3
-  Functions: 501
-  Symbols:   285
-  CStrings:  1826
+  UUID: 0E24E14D-786F-31AA-AF0C-0DBCE5CCD360
+  Functions: 528
+  Symbols:   294
+  CStrings:  1890
 
Symbols:
+ _AMAuthInstallCreate
+ _AMAuthInstallSupportGetValueForKeyWithFormat
+ _AMAuthInstallUpdaterSetInfoWithUARPCallbacks
+ _AMSupportCreateErrorInternal
+ _AMSupportSafeRetain
+ _CFArrayGetTypeID
+ _CFDictionaryGetKeysAndValues
+ __CFXPCCreateCFObjectFromXPCObject
+ _kAMAuthInstallErrorDomain
+ _objc_retain_x24
+ _xpc_dictionary_get_value
- _objc_release_x26
- _objc_retain_x23
CStrings:
+ "%@ has no tags provided by the host"
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
+ "BuildIdentity"
+ "BuildIdentityTags"
+ "DeviceInfoRequests"
+ "DeviceInfoTags"
+ "Failed to set personalization info for %s"
+ "FirmwareData"
+ "Host asked for preflight personalization for this updater"
+ "Manifest.%@"
+ "No data was provided from the host for tag %@"
+ "No tethered preflight payload provided"
+ "Starting %s"
+ "Starting %s...\n"
+ "TetheredPreflightPayload"
+ "[dsri] payload received"
+ "_ramrod_copy_build_identity_callback"
+ "_ramrod_copy_files_from_bundle_callback"
+ "_ramrod_query_personalization_info_callback"
+ "amai is NULL"
+ "buildIdentityTags is NULL"
+ "get_ramrod_preflight_info"
+ "getdevicesidepreflightinfo"
+ "payload"
+ "queryPersonalizationInfo"
+ "ramrod"
+ "ramrod_update_copy_deviceinfo_with_payload"
+ "responseDict is NULL"
- "ramrod_update_copy_deviceinfo"

```
