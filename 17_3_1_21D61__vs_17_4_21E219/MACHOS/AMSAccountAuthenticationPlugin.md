## AMSAccountAuthenticationPlugin

> `/System/Library/Accounts/Authentication/AMSAccountAuthenticationPlugin.bundle/AMSAccountAuthenticationPlugin`

```diff

-7.3.4.0.0
-  __TEXT.__text: 0x8dd4
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_stubs: 0x1fc0
-  __TEXT.__objc_methlist: 0x404
+7.4.38.2.4
+  __TEXT.__text: 0x869c
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_stubs: 0x1e80
+  __TEXT.__objc_methlist: 0x39c
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0xb49
-  __TEXT.__objc_classname: 0xe9
-  __TEXT.__objc_methname: 0x21ba
-  __TEXT.__objc_methtype: 0x884
-  __TEXT.__oslogstring: 0x17cb
+  __TEXT.__cstring: 0xa56
+  __TEXT.__objc_classname: 0xd0
+  __TEXT.__objc_methname: 0x20ce
+  __TEXT.__objc_methtype: 0x876
+  __TEXT.__oslogstring: 0x16e4
   __TEXT.__gcc_except_tab: 0x10
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x1b4
-  __DATA_CONST.__auth_got: 0x228
+  __TEXT.__unwind_info: 0x198
+  __DATA_CONST.__auth_got: 0x230
   __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x518
-  __DATA_CONST.__cfstring: 0xa80
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__const: 0x4e8
+  __DATA_CONST.__cfstring: 0x980
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xf00
-  __DATA.__objc_selrefs: 0x868
-  __DATA.__objc_classrefs: 0x140
-  __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0x30
-  __DATA.__objc_data: 0x190
+  __DATA_CONST.__objc_classrefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA.__objc_const: 0xe00
+  __DATA.__objc_selrefs: 0x818
+  __DATA.__objc_ivar: 0x28
+  __DATA.__objc_data: 0x140
   __DATA.__data: 0x180
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 109
-  Symbols:   146
-  CStrings:  600
+  Functions: 100
+  Symbols:   142
+  CStrings:  576
 
Symbols:
+ _OBJC_CLASS_$_AMSDeviceAccountPrivacyAcknowledgementTask
+ _objc_retainAutoreleaseReturnValue
- _AMSBagKeySubscriptionBundleGDPRURL
- _OBJC_CLASS_$_AMSAcknowledgePrivacyTask
- _OBJC_CLASS_$_AMSDeviceAccountGDPRTask
- _OBJC_CLASS_$_AMSEngagementRequest
- _OBJC_CLASS_$_AMSSystemEngagementTask
- _OBJC_METACLASS_$_AMSDeviceAccountGDPRTask
CStrings:
+ "%{public}@: [%{public}@] Account save failed with error %{public}@"
+ "T@\"NSString\",?,R,C"
+ "isDirty"
+ "performPrivacyAcknowledgement"
+ "promiseWithSuccess"
- "%{public}@: [%{public}@] Failed to determine bundle owner status"
- "%{public}@: [%{public}@] Presenting engagement to get GDPR consent"
- "%{public}@: [%{public}@] Requesting gdpr presentation for id: %{public}@"
- "%{public}@: [%{public}@] Skipping subscription bundle acknowledgement - already acknowledged"
- "@28@0:8@16B24"
- "AMSDeviceAccountGDPRTask"
- "B16@?0^@8"
- "Missing bundle owner status"
- "Missing dynamic ui gdpr route"
- "_presentEngagementRequest:"
- "_presentGDPREngagementRequestForAccount:bundleOwnerStatus:"
- "_verifyGDPRStatusForAccount:"
- "absoluteURL"
- "acknowledgementNeededForPrivacyIdentifier:account:"
- "auth-plugin"
- "bundleOwner"
- "com.apple.onboarding.deviceholder"
- "com.apple.onboarding.subscriptionbundle"
- "context"
- "dynamic-ui-bundle-gdpr-url"
- "finishWithSuccess"
- "initWithRequest:"
- "performBinaryTaskWithBlock:"
- "performGDPRUpdate"
- "present"
- "setClientData:"
- "setURL:"
- "v24@?0@\"AMSEngagementResult\"8@\"NSError\"16"
- "valueWithError:"

```
