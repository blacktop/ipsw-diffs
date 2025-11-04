## AppStoreComponentsDaemonKit

> `/System/Library/PrivateFrameworks/AppStoreComponentsDaemonKit.framework/AppStoreComponentsDaemonKit`

```diff

-8.1.9.2.1
-  __TEXT.__text: 0x10bc5c
-  __TEXT.__auth_stubs: 0x3b00
-  __TEXT.__objc_methlist: 0x4658
-  __TEXT.__const: 0x6af0
-  __TEXT.__cstring: 0x965c
-  __TEXT.__oslogstring: 0x1c74
+8.2.6.0.0
+  __TEXT.__text: 0x10c098
+  __TEXT.__auth_stubs: 0x3b20
+  __TEXT.__objc_methlist: 0x46b8
+  __TEXT.__const: 0x6b00
+  __TEXT.__cstring: 0x968c
+  __TEXT.__oslogstring: 0x1ced
   __TEXT.__gcc_except_tab: 0x58
   __TEXT.__dlopen_cstrs: 0x8e
   __TEXT.__constg_swiftt: 0x1a1c
   __TEXT.__swift5_typeref: 0x3379
+  __TEXT.__swift5_fieldmd: 0x1658
   __TEXT.__swift5_builtin: 0x1f4
   __TEXT.__swift5_reflstr: 0x11d6
-  __TEXT.__swift5_fieldmd: 0x1658
   __TEXT.__swift5_assocty: 0x6c8
+  __TEXT.__swift5_capture: 0x17b8
   __TEXT.__swift5_proto: 0x418
   __TEXT.__swift5_types: 0x224
-  __TEXT.__swift5_capture: 0x17b8
   __TEXT.__swift_as_entry: 0x1e4
   __TEXT.__swift_as_ret: 0x284
   __TEXT.__swift5_mpenum: 0x24
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__unwind_info: 0x3870
+  __TEXT.__unwind_info: 0x3878
   __TEXT.__eh_frame: 0x7fec
-  __TEXT.__objc_classname: 0x83b
-  __TEXT.__objc_methname: 0x7bd1
-  __TEXT.__objc_methtype: 0x1244
-  __TEXT.__objc_stubs: 0x3900
+  __TEXT.__objc_classname: 0x83e
+  __TEXT.__objc_methname: 0x7cbb
+  __TEXT.__objc_methtype: 0x1276
+  __TEXT.__objc_stubs: 0x3920
   __DATA_CONST.__got: 0xd10
-  __DATA_CONST.__const: 0x798
+  __DATA_CONST.__const: 0x7a8
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e20
+  __DATA_CONST.__objc_selrefs: 0x1e50
   __DATA_CONST.__objc_protorefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x1e8
-  __AUTH_CONST.__auth_got: 0x1d90
+  __AUTH_CONST.__auth_got: 0x1da0
   __AUTH_CONST.__const: 0x58d8
-  __AUTH_CONST.__cfstring: 0x3500
-  __AUTH_CONST.__objc_const: 0x9e98
+  __AUTH_CONST.__cfstring: 0x3560
+  __AUTH_CONST.__objc_const: 0x9ed8
   __AUTH.__objc_data: 0x1700
   __AUTH.__data: 0x3b8
-  __DATA.__objc_ivar: 0x374
+  __DATA.__objc_ivar: 0x378
   __DATA.__data: 0x20f0
   __DATA.__bss: 0x5330
   __DATA.__common: 0x68

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DF182D89-FC1C-385D-9AF9-A892F77D2CD7
-  Functions: 4477
-  Symbols:   6006
-  CStrings:  3321
+  UUID: B7E2E2A4-3616-3484-ACDB-227709D7355F
+  Functions: 4484
+  Symbols:   6028
+  CStrings:  3339
 
Symbols:
+ -[ASCJSClientObject _checkEligibilityDomain:withContextDictionary:]
+ -[ASCJSClientObject _checkEligibilityDomain:withContextDictionary:].cold.1
+ -[ASCJSClientObject _checkEligibilityDomain:withContextDictionary:].cold.2
+ -[ASCJSClientObject contextForEligibilityDomain:]
+ -[ASCJSClientObject hasEligibilityDomain:]
+ -[ASCLockupProductDetails setWebBrowserFlowType:]
+ -[ASCLockupProductDetails webBrowserFlowType]
+ -[ASCLockupRequest(AppDistributionInstall) lockupRequestWithSourceAppBundleId:]
+ _ASCLockupWebBrowserFlowTypePurchaseAndOpen
+ _ASCLockupWebBrowserFlowTypeSelectionOnly
+ _OBJC_IVAR_$_ASCLockupProductDetails._webBrowserFlowType
+ __CFXPCCreateCFObjectFromXPCObject
+ _objc_msgSend$_checkEligibilityDomain:withContextDictionary:
+ _os_eligibility_domain_for_name
CStrings:
+ "@\"NSDictionary\"24@0:8@\"NSString\"16"
+ "B32@0:8@16^@24"
+ "Error fetching eligibility for domain: %{public}@, error: %{public}d"
+ "T@\"NSString\",&,N,V_webBrowserFlowType"
+ "Tried to query eligibility but domain %@ is invalid"
+ "_checkEligibilityDomain:withContextDictionary:"
+ "_webBrowserFlowType"
+ "appBundleId[referrer]"
+ "contextForEligibilityDomain:"
+ "hasEligibilityDomain:"
+ "lockupRequestWithSourceAppBundleId:"
+ "purchaseAndOpen"
+ "seed"
+ "selectionOnly"
+ "setWebBrowserFlowType:"
+ "webBrowserFlowType"
- "production"

```
