## AMSAccountNotificationPlugin

> `/System/Library/Accounts/Notification/AMSAccountNotificationPlugin.bundle/AMSAccountNotificationPlugin`

```diff

-7.3.4.0.0
-  __TEXT.__text: 0xedc4
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_methlist: 0x4a4
+7.4.38.2.4
+  __TEXT.__text: 0xf218
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__objc_methlist: 0x4d4
   __TEXT.__const: 0x15c
-  __TEXT.__cstring: 0xa3d
-  __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__oslogstring: 0x259e
+  __TEXT.__cstring: 0xb0d
+  __TEXT.__gcc_except_tab: 0xa8
+  __TEXT.__oslogstring: 0x2662
   __TEXT.__dlopen_cstrs: 0x1a6
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0xa6

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x354
-  __TEXT.__eh_frame: 0x2a8
+  __TEXT.__unwind_info: 0x350
+  __TEXT.__eh_frame: 0x2d0
   __TEXT.__objc_classname: 0x93
-  __TEXT.__objc_methname: 0x1f4c
+  __TEXT.__objc_methname: 0x1fba
   __TEXT.__objc_methtype: 0x306
-  __TEXT.__objc_stubs: 0x1f00
-  __DATA_CONST.__got: 0x78
+  __TEXT.__objc_stubs: 0x1f40
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x4b8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x680
-  __DATA_CONST.__objc_selrefs: 0x878
+  __DATA_CONST.__objc_const: 0x6b0
+  __DATA_CONST.__objc_selrefs: 0x888
+  __DATA_CONST.__objc_classrefs: 0x148
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__cfstring: 0x740
+  __AUTH_CONST.__cfstring: 0x7a0
   __AUTH_CONST.__objc_const: 0x340
   __AUTH_CONST.__const: 0x1d0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x418
+  __AUTH_CONST.__auth_got: 0x428
   __AUTH.__objc_data: 0x250
   __AUTH.__data: 0x50
-  __DATA.__objc_classrefs: 0x148
-  __DATA.__objc_superrefs: 0x20
-  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x180
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 212
-  Symbols:   195
-  CStrings:  574
+  Functions: 217
+  Symbols:   198
+  CStrings:  583
 
Symbols:
+ _AMSAKOverrideEligibilityPlaceholderKey
+ _AMSSetLogKeyIfNeeded
+ _objc_retain_x27
CStrings:
+ "%{public}@ [%{public}@] Preventing attempted logout of local account. account = %{public}@"
+ "%{public}@: [%{public}@] Posting a com.apple.AppleMediaServices.eligibilityoverridechanged notification."
+ "Preventing an attempt to log out the local iTunes account."
+ "Starting engagement sync because the storefront changed"
+ "T@\"NSString\",?,R,C"
+ "The logout was cancelled"
+ "_postEligibilityOverrideNotificationIfNeededForAccount:oldAccount:"
+ "ams_isRegulatoryAccount"
+ "com.apple.AppleMediaServices.eligibilityoverridechanged"
+ "initWithCachePolicy:"
- "defaultTreatmentStore"

```
