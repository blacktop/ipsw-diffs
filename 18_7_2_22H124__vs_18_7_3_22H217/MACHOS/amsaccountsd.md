## amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

-8.6.8.0.0
-  __TEXT.__text: 0x189768
+8.6.8.1.0
+  __TEXT.__text: 0x18a30c
   __TEXT.__auth_stubs: 0x2a90
-  __TEXT.__objc_stubs: 0x98c0
-  __TEXT.__objc_methlist: 0x522c
-  __TEXT.__const: 0x13c80
-  __TEXT.__objc_classname: 0xe29
-  __TEXT.__objc_methname: 0xe619
-  __TEXT.__oslogstring: 0xa4fe
-  __TEXT.__objc_methtype: 0x400d
-  __TEXT.__cstring: 0x90ff
+  __TEXT.__objc_stubs: 0x9980
+  __TEXT.__objc_methlist: 0x5304
+  __TEXT.__const: 0x13c90
+  __TEXT.__objc_classname: 0xe69
+  __TEXT.__objc_methname: 0xe791
+  __TEXT.__oslogstring: 0xa6ae
+  __TEXT.__objc_methtype: 0x4078
+  __TEXT.__cstring: 0x918f
   __TEXT.__gcc_except_tab: 0xe98
   __TEXT.__dlopen_cstrs: 0x34d
   __TEXT.__swift5_typeref: 0x3da9
   __TEXT.__constg_swiftt: 0x3540
-  __TEXT.__swift5_reflstr: 0x2c50
+  __TEXT.__swift5_reflstr: 0x2c70
   __TEXT.__swift5_fieldmd: 0x4b48
   __TEXT.__swift5_capture: 0x63c
   __TEXT.__swift5_builtin: 0xa0

   __TEXT.__swift_as_ret: 0x270
   __TEXT.__swift5_protos: 0x7c
   __TEXT.__swift5_mpenum: 0x68
-  __TEXT.__unwind_info: 0x6960
-  __TEXT.__eh_frame: 0xb688
+  __TEXT.__unwind_info: 0x6608
+  __TEXT.__eh_frame: 0xb668
   __DATA_CONST.__auth_got: 0x1558
   __DATA_CONST.__got: 0xd00
-  __DATA_CONST.__auth_ptr: 0xcc0
-  __DATA_CONST.__const: 0xce90
-  __DATA_CONST.__cfstring: 0x4120
-  __DATA_CONST.__objc_classlist: 0x2e0
+  __DATA_CONST.__auth_ptr: 0xbc0
+  __DATA_CONST.__const: 0xceb0
+  __DATA_CONST.__cfstring: 0x41a0
+  __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x240
+  __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x190
+  __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0x9d78
-  __DATA.__objc_selrefs: 0x3770
-  __DATA.__objc_ivar: 0x338
-  __DATA.__objc_data: 0x1d78
-  __DATA.__data: 0x7068
-  __DATA.__bss: 0x21438
+  __DATA.__objc_const: 0x9f50
+  __DATA.__objc_selrefs: 0x37b8
+  __DATA.__objc_ivar: 0x344
+  __DATA.__objc_data: 0x1dc8
+  __DATA.__data: 0x70d8
+  __DATA.__bss: 0x21448
   __DATA.__common: 0x160
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 937597AF-AC32-3D59-AD2D-53A5DC971201
-  Functions: 10002
+  UUID: 9588DB49-B9AF-336F-AAF0-BE2862C24860
+  Functions: 10017
   Symbols:   1360
-  CStrings:  4992
+  CStrings:  5028
 
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
+ "AMSDSafariDataUpdateService"
+ "AMSSafariDataUpdate Error"
+ "AMSSafariDataUpdateServiceInterface"
+ "Invalid URL for publish"
+ "Pending update expired"
+ "T@\"AMSDSafariDataUpdateService\",R,N"
+ "T@\"NSDate\",&,N,V_pendingTimestamp"
+ "T@\"NSString\",&,N,V_pendingURL"
+ "_pendingTimestamp"
+ "_pendingURL"
+ "com.apple.AMS.SafariDataUpdate"
+ "com.apple.amsaccountsd.SafariDataUpdate"
+ "fetchPendingSafariDataUpdate:"
+ "getSafariDataUpdateServiceProxyWithReplyHandler:"
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
