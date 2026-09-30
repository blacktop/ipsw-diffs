## amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

-9.2.21.0.0
-  __TEXT.__text: 0x2189bc
+9.2.23.2.2
+  __TEXT.__text: 0x21b240
   __TEXT.__auth_stubs: 0x3cf0
-  __TEXT.__objc_stubs: 0x9b00
-  __TEXT.__objc_methlist: 0x5644
-  __TEXT.__const: 0x1d4b4
-  __TEXT.__objc_classname: 0xf0d
-  __TEXT.__objc_methname: 0xeec0
-  __TEXT.__oslogstring: 0xda41
-  __TEXT.__objc_methtype: 0x43f4
-  __TEXT.__cstring: 0xb1a7
+  __TEXT.__objc_stubs: 0x9c40
+  __TEXT.__objc_methlist: 0x5714
+  __TEXT.__const: 0x1d484
+  __TEXT.__objc_classname: 0xf4d
+  __TEXT.__objc_methname: 0xf0ab
+  __TEXT.__oslogstring: 0xdc31
+  __TEXT.__objc_methtype: 0x445f
+  __TEXT.__cstring: 0xb227
   __TEXT.__gcc_except_tab: 0xe30
   __TEXT.__dlopen_cstrs: 0x34d
   __TEXT.__swift5_typeref: 0x6cc8
-  __TEXT.__swift5_fieldmd: 0x645c
   __TEXT.__constg_swiftt: 0x52d4
-  __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_reflstr: 0x471c
+  __TEXT.__swift5_fieldmd: 0x645c
+  __TEXT.__swift5_capture: 0xa28
+  __TEXT.__swift5_builtin: 0x118
+  __TEXT.__swift5_mpenum: 0x78
   __TEXT.__swift5_assocty: 0x8f8
-  __TEXT.__swift5_protos: 0xa8
   __TEXT.__swift5_proto: 0x16d8
   __TEXT.__swift5_types: 0x67c
   __TEXT.__swift_as_entry: 0x204
-  __TEXT.__swift5_mpenum: 0x78
-  __TEXT.__swift5_capture: 0xa28
   __TEXT.__swift_as_ret: 0x2b0
+  __TEXT.__swift5_protos: 0xa8
   __TEXT.__swift5_types2: 0x8
-  __TEXT.__unwind_info: 0x8678
-  __TEXT.__eh_frame: 0xf894
+  __TEXT.__unwind_info: 0x8720
+  __TEXT.__eh_frame: 0xf8e4
   __DATA_CONST.__auth_got: 0x1e88
   __DATA_CONST.__got: 0x1228
-  __DATA_CONST.__auth_ptr: 0xcb8
-  __DATA_CONST.__const: 0x121d8
-  __DATA_CONST.__cfstring: 0x4000
-  __DATA_CONST.__objc_classlist: 0x358
+  __DATA_CONST.__auth_ptr: 0xcc0
+  __DATA_CONST.__const: 0x121f8
+  __DATA_CONST.__cfstring: 0x4080
+  __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x278
+  __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x198
+  __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__linkguard: 0x2c
-  __DATA.__objc_const: 0xb160
-  __DATA.__objc_selrefs: 0x3900
-  __DATA.__objc_ivar: 0x350
-  __DATA.__objc_data: 0x2420
-  __DATA.__data: 0xa230
-  __DATA.__bss: 0x2d420
+  __DATA.__objc_const: 0xb338
+  __DATA.__objc_selrefs: 0x3968
+  __DATA.__objc_ivar: 0x35c
+  __DATA.__objc_data: 0x2470
+  __DATA.__data: 0xa280
+  __DATA.__bss: 0x2d430
   __DATA.__common: 0x190
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6C483660-4357-3350-99B2-4DC5BA1FEB17
-  Functions: 13290
+  UUID: 1C0A714F-ADCB-346D-B7A4-C717C3329FEE
+  Functions: 13325
   Symbols:   1870
-  CStrings:  5477
+  CStrings:  5518
 
CStrings:
+ "%{public}@: Fetching pending Safari Data Update"
+ "%{public}@: Invalid URL for publish"
+ "%{public}@: No pending update available"
+ "%{public}@: Pending update expired (age: %.1fs)"
+ "%{public}@: Published notification successfully"
+ "%{public}@: Publishing Safari Data Update: %{public}@"
+ "%{public}@: Returning pending update: %{public}@"
+ "%{public}@: Safari Data Update service initialized"
+ "%{public}@: Stored pending update, posting notification"
+ "%{public}@: [%{public}@] Unable to sync account data, error: %{public}@"
+ "AMSDSafariDataUpdateService"
+ "AMSSafariDataUpdate Error"
+ "AMSSafariDataUpdateServiceInterface"
+ "Invalid URL for publish"
+ "Pending update expired"
+ "T@\"AMSDSafariDataUpdateService\",R,N"
+ "T@\"NSDate\",&,N,V_pendingTimestamp"
+ "T@\"NSString\",&,N,V_pendingURL"
+ "_daemonOSUpgradeTasks:lastMigratedBuildVersion:"
+ "_pendingTimestamp"
+ "_pendingURL"
+ "com.apple.AMS.SafariDataUpdate"
+ "com.apple.amsaccountsd.SafariDataUpdate"
+ "currentBuildVersion"
+ "fetchPendingSafariDataUpdate:"
+ "getSafariDataUpdateServiceProxyWithReplyHandler:"
+ "initWithDSID:altDSID:"
+ "lastMigratedBuildVersion"
+ "pendingTimestamp"
+ "pendingURL"
+ "postNotificationName:object:userInfo:options:"
+ "publishSafariDataUpdate:completion:"
+ "setPendingTimestamp:"
+ "setPendingURL:"
+ "timeIntervalSinceNow"
+ "v24@0:8@?<v@?@\"<AMSSafariDataUpdateServiceInterface>\"@\"NSError\">16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"

```
