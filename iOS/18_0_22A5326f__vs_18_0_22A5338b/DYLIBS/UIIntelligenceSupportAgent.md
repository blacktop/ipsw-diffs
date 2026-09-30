## UIIntelligenceSupportAgent

> `/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent`

```diff

-8079.0.0.0.0
-  __TEXT.__text: 0x37b54
-  __TEXT.__auth_stubs: 0x16e0
-  __TEXT.__const: 0x15e8
-  __TEXT.__constg_swiftt: 0x59c
-  __TEXT.__swift5_typeref: 0xac7
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x677
-  __TEXT.__swift5_fieldmd: 0x720
-  __TEXT.__swift5_types: 0x80
-  __TEXT.__cstring: 0xf57
-  __TEXT.__oslogstring: 0x628
-  __TEXT.__swift5_capture: 0x110
+8081.0.0.0.0
+  __TEXT.__text: 0x3db1c
+  __TEXT.__auth_stubs: 0x17c0
+  __TEXT.__const: 0x1828
+  __TEXT.__constg_swiftt: 0x688
+  __TEXT.__swift5_typeref: 0xc13
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_reflstr: 0x837
+  __TEXT.__swift5_fieldmd: 0x848
+  __TEXT.__swift5_assocty: 0x90
+  __TEXT.__swift5_proto: 0x148
+  __TEXT.__swift5_types: 0x94
+  __TEXT.__cstring: 0x1117
+  __TEXT.__oslogstring: 0x713
+  __TEXT.__swift5_capture: 0x1ac
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_proto: 0x130
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__unwind_info: 0x948
-  __TEXT.__eh_frame: 0xb90
+  __TEXT.__unwind_info: 0xad8
+  __TEXT.__eh_frame: 0xec0
   __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methname: 0x23b
+  __TEXT.__objc_methname: 0x372
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x360
+  __DATA_CONST.__got: 0x3a8
   __DATA_CONST.__const: 0xd8
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x70
+  __DATA_CONST.__objc_selrefs: 0xc0
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0xb70
-  __AUTH_CONST.__auth_ptr: 0x3d0
-  __AUTH_CONST.__const: 0xc68
-  __AUTH_CONST.__objc_const: 0xec0
-  __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0xc0
-  __DATA.__data: 0x5f8
-  __DATA.__bss: 0x2110
+  __AUTH_CONST.__auth_got: 0xbe0
+  __AUTH_CONST.__auth_ptr: 0x468
+  __AUTH_CONST.__const: 0xfd0
+  __AUTH_CONST.__objc_const: 0x1108
+  __AUTH.__objc_data: 0xa0
+  __AUTH.__data: 0x240
+  __DATA.__data: 0x678
+  __DATA.__bss: 0x2410
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x910
+  __DATA_DIRTY.__data: 0x940
   __DATA_DIRTY.__bss: 0x400
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 869
-  Symbols:   201
-  CStrings:  190
+  Functions: 981
+  Symbols:   229
+  CStrings:  214
 
Symbols:
+ _DMFEffectivePolicyTypeApplication
+ _OBJC_CLASS_$_DMFEffectivePolicy
+ _OBJC_CLASS_$_DMFPolicyMonitor
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$_NSThread
+ _dispatch_sync
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x28
+ _swift_dynamicCastObjCClass
+ _swift_getObjCClassFromMetadata
+ _swift_isEscapingClosureAtFileLocation
+ _swift_stdlib_isStackAllocationSafe
CStrings:
+ "ManagementPolicy"
+ "PrewarmManagementPolicy"
+ "_TtC26UIIntelligenceSupportAgent24ManagementPolicyProvider"
+ "_TtCC26UIIntelligenceSupportAgent16FragmentCollatorP33_6BE94AAF2C91BC919D389B27AF47AB7925FragmentResolutionContext"
+ "bundleIdentifier"
+ "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
+ "collection prohibited due to management policy: %!{(MISSING)public}s"
+ "com.apple.springboard"
+ "containingBundleRecord"
+ "dropWindowsMissingOcclusionInfo"
+ "getDeviceManagementPolicyWithCompletionHandler:"
+ "init"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "isMainThread"
+ "localizedDescription"
+ "management policy fetch timed out"
+ "managementPolicyProvider"
+ "policyForIdentifier:excludableIdentifiers:"
+ "policyStatusMap"
+ "requestPoliciesForTypes:withError:"
+ "unable to perform fast policy fetch: %!{(MISSING)public}s; underlying error: %!{(MISSING)public}s"
+ "unable to prewarm management policy provider using \"%!{(MISSING)public}s\": %!{(MISSING)public}s; underlying error: %!{(MISSING)public}s"
+ "v16@?0q8"
+ "windowVisibleShapeMap"
+ "windowZOrderMap"
- "dropping window with missing occlusion info: %!{(MISSING)public}s"

```
