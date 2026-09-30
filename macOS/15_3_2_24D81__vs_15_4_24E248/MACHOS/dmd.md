## dmd

> `/usr/libexec/dmd`

```diff

-221.2.7.0.0
-  __TEXT.__text: 0x64478
+221.4.7.0.0
+  __TEXT.__text: 0x65840
   __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_stubs: 0x97e0
-  __TEXT.__objc_methlist: 0x5878
-  __TEXT.__const: 0x138
-  __TEXT.__objc_classname: 0x1ae8
-  __TEXT.__objc_methname: 0xc1c1
-  __TEXT.__objc_methtype: 0x167d
-  __TEXT.__cstring: 0x4228
-  __TEXT.__oslogstring: 0x6944
-  __TEXT.__gcc_except_tab: 0x930
+  __TEXT.__objc_stubs: 0x9880
+  __TEXT.__objc_methlist: 0x6174
+  __TEXT.__const: 0x140
+  __TEXT.__objc_classname: 0x1b21
+  __TEXT.__objc_methname: 0xc39e
+  __TEXT.__objc_methtype: 0x16f9
+  __TEXT.__cstring: 0x427d
+  __TEXT.__oslogstring: 0x69e8
+  __TEXT.__gcc_except_tab: 0xc94
   __TEXT.__ustring: 0x498
-  __TEXT.__unwind_info: 0x16f8
+  __TEXT.__unwind_info: 0x1870
   __DATA_CONST.__auth_got: 0x4d0
-  __DATA_CONST.__got: 0xed8
+  __DATA_CONST.__got: 0xef0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1848
-  __DATA_CONST.__cfstring: 0x4740
-  __DATA_CONST.__objc_classlist: 0x620
+  __DATA_CONST.__const: 0x1888
+  __DATA_CONST.__cfstring: 0x4780
+  __DATA_CONST.__objc_classlist: 0x630
   __DATA_CONST.__objc_catlist: 0x168
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x2c0
-  __DATA_CONST.__objc_arraydata: 0x560
-  __DATA_CONST.__objc_arrayobj: 0x918
+  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_arraydata: 0x570
+  __DATA_CONST.__objc_arrayobj: 0x948
   __DATA_CONST.__objc_intobj: 0x2d0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x140
-  __DATA.__objc_const: 0x1b3b8
-  __DATA.__objc_selrefs: 0x2b10
+  __DATA.__objc_const: 0x1a610
+  __DATA.__objc_selrefs: 0x2be8
   __DATA.__objc_ivar: 0x374
-  __DATA.__objc_data: 0x3d40
+  __DATA.__objc_data: 0x3de0
   __DATA.__data: 0xba8
   __DATA.__bss: 0x2e8
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /System/Library/PrivateFrameworks/login.framework/Versions/A/login
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 92B01AAB-6588-397B-A20C-E10BA85FE512
-  Functions: 2173
-  Symbols:   691
-  CStrings:  3830
+  UUID: B2A9692C-954B-3785-8753-A971F2B4C195
+  Functions: 2294
+  Symbols:   694
+  CStrings:  3852
 
Symbols:
+ _OBJC_CLASS_$_DMFFetchAppInfoRequest
+ _OBJC_CLASS_$_DMFFetchAppInfoResultObject
+ _OBJC_CLASS_$_DMFUpdateAppAttributesRequest
CStrings:
+ "Clearing app policy caches"
+ "Clearing category policy caches"
+ "Clearing website policy caches"
+ "DMDFetchAppInfoOperation"
+ "DMDUpdateAppAttributesOperation"
+ "Error fetching budget statuses: %{public}@"
+ "Failed to load persistent store. Error: %{public}@"
+ "Recalculating effective policies for types %{public}@"
+ "Requested website %{sensitive}@ has policy %{public}@, associated categories:%{public}@ associated sites:%{sensitive}@ equivalent bundle identifiers:%{sensitive}@"
+ "Start updating app attributes for request: %{public}@"
+ "T@\"NSMutableDictionary\",&,N,V_effectivePolicyCache"
+ "_effectivePoliciesForTypes:"
+ "_effectivePolicyForType:"
+ "_startUpdateAppAttributesForRequest:metadata:"
+ "addAttributes:forApp:"
+ "allEffectivePolicyTypes"
+ "allManagementInformation"
+ "checkStatusOfBudgets:completionHandler:"
+ "com.apple.dmd.operation.fetch-app-info"
+ "com.apple.dmd.operation.update-app-attributes"
+ "filterForExpiredBudgetIdentifiers:shouldBeSynchronous:replyHandler:"
+ "ignoreNilConfiguration"
+ "setEffectivePolicyCache:"
+ "setVPNUUIDString:cellularSliceUUIDString:contentFilterUUIDString:DNSProxyUUIDString:relayUUIDString:associatedDomains:enableDirectDownloads:allowUserToHide:allowUserToLock:configuration:ignoreNilConfiguration:options:sourceIdentifier:forBundleIdentifier:"
+ "v124@0:8@16@24@32@40@48@56@64@72@80@88B96Q100@108@116"
+ "v36@0:8@\"NSArray\"16B24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "v36@0:8@16B24@?28"
- "Error recalculating effectivePolicy for type %{public}@: %{public}@"
- "Error recalculating effectivePolicy for types %{public}@: %{public}@"
- "Requested website %{public}@ has policy %{public}@, associated categories:%{public}@ associated sites:%{public}@ equivalent bundle identifiers:%{public}@"
- "T@\"NSCache\",R,N,V_effectivePolicyCache"
- "_effectivePoliciesForTypes:outError:"
- "_effectivePolicyForType:outError:"
- "_recalculateEffectivePolicyForType:outError:"

```
