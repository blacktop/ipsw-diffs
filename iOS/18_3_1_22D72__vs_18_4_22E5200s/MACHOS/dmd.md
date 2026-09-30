## dmd

> `/usr/libexec/dmd`

```diff

-221.2.7.0.0
-  __TEXT.__text: 0x82d3c
+221.4.4.1.0
+  __TEXT.__text: 0x84020
   __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_stubs: 0xe880
-  __TEXT.__objc_methlist: 0x6fec
+  __TEXT.__objc_stubs: 0xe940
+  __TEXT.__objc_methlist: 0x7b0c
   __TEXT.__const: 0x150
-  __TEXT.__objc_classname: 0x1e1b
-  __TEXT.__objc_methname: 0x116fe
-  __TEXT.__objc_methtype: 0x1d57
-  __TEXT.__cstring: 0x5300
-  __TEXT.__oslogstring: 0xadd6
-  __TEXT.__gcc_except_tab: 0xe78
-  __TEXT.__ustring: 0x810
+  __TEXT.__objc_classname: 0x1e54
+  __TEXT.__objc_methname: 0x11868
+  __TEXT.__objc_methtype: 0x1d8d
+  __TEXT.__cstring: 0x5349
+  __TEXT.__oslogstring: 0xae9b
+  __TEXT.__gcc_except_tab: 0x11d8
+  __TEXT.__ustring: 0x80a
   __TEXT.__dlopen_cstrs: 0xaf
-  __TEXT.__unwind_info: 0x1eb0
+  __TEXT.__unwind_info: 0x2048
   __DATA_CONST.__auth_got: 0x780
-  __DATA_CONST.__got: 0x12e8
-  __DATA_CONST.__const: 0x2708
-  __DATA_CONST.__cfstring: 0x5720
-  __DATA_CONST.__objc_classlist: 0x6e0
+  __DATA_CONST.__got: 0x1318
+  __DATA_CONST.__const: 0x2720
+  __DATA_CONST.__cfstring: 0x5760
+  __DATA_CONST.__objc_classlist: 0x6f0
   __DATA_CONST.__objc_catlist: 0x198
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x338
-  __DATA_CONST.__objc_arraydata: 0x4f0
-  __DATA_CONST.__objc_arrayobj: 0x918
+  __DATA_CONST.__objc_superrefs: 0x340
+  __DATA_CONST.__objc_arraydata: 0x500
+  __DATA_CONST.__objc_arrayobj: 0x948
   __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x1e3e8
-  __DATA.__objc_selrefs: 0x3fa0
+  __DATA.__objc_const: 0x1d1c0
+  __DATA.__objc_selrefs: 0x4170
   __DATA.__objc_ivar: 0x428
-  __DATA.__objc_data: 0x44c0
+  __DATA.__objc_data: 0x4560
   __DATA.__data: 0xc60
   __DATA.__bss: 0x4e8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 2959
-  Symbols:   906
-  CStrings:  4584
+  Functions: 3087
+  Symbols:   912
+  CStrings:  4601
 
Symbols:
+ _OBJC_CLASS_$_DMFFetchAppInfoRequest
+ _OBJC_CLASS_$_DMFFetchAppInfoResultObject
+ _OBJC_CLASS_$_DMFUpdateAppAttributesRequest
+ _OBJC_CLASS_$_MDMCloudConfiguration
+ _kMDMEnrollmentSSOAppStoreIDKey
+ _kMDMRequiredAppIDForMDMKey
CStrings:
+ "%@ (%@)"
+ "Clearing app policy caches"
+ "Clearing category policy caches"
+ "Clearing website policy caches"
+ "DMDFetchAppInfoOperation"
+ "DMDUpdateAppAttributesOperation"
+ "Failed to load persistent store. Error: %{public}@"
+ "Installing system app with bundle id: %{public}@"
+ "Managing app: %{public}@"
+ "Recalculating effective policies for types %{public}@"
+ "Request to manage app %{public}@ fast-tracked, supervised: %{public}@ internal: %{public}@"
+ "Start updating app attributes for request: %{public}@"
+ "T@\"NSDictionary\",&,N,V_effectivePolicyCache"
+ "_effectivePoliciesForTypes:"
+ "_effectivePolicyForType:"
+ "_getAllowedAppIDsFromDisk"
+ "_startUpdateAppAttributesForRequest:metadata:"
+ "addAttributes:forApp:"
+ "allEffectivePolicyTypes"
+ "allManagementInformation"
+ "com.apple.dmd.operation.fetch-app-info"
+ "com.apple.dmd.operation.update-app-attributes"
+ "ignoreNilConfiguration"
+ "setEffectivePolicyCache:"
+ "setVPNUUIDString:cellularSliceUUIDString:contentFilterUUIDString:DNSProxyUUIDString:relayUUIDString:associatedDomains:enableDirectDownloads:allowUserToHide:allowUserToLock:configuration:ignoreNilConfiguration:options:sourceIdentifier:forBundleIdentifier:"
+ "v124@0:8@16@24@32@40@48@56@64@72@80@88B96Q100@108@116"
- "Error recalculating effectivePolicy for type %{public}@: %{public}@"
- "Error recalculating effectivePolicy for types %{public}@: %{public}@"
- "Request to manage app fast-tracked, supervised: %{public}@ internal: %{public}@"
- "RequiredAppIDForMDM"
- "T@\"NSCache\",R,N,V_effectivePolicyCache"
- "_effectivePoliciesForTypes:outError:"
- "_effectivePolicyForType:outError:"
- "_getRequiredAppIDFromDisk"
- "_recalculateEffectivePolicyForType:outError:"

```
