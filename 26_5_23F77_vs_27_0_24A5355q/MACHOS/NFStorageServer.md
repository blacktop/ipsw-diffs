## NFStorageServer

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFStorageServer.xpc/NFStorageServer`

```diff

-365.3.1.0.0
-  __TEXT.__text: 0xd68
-  __TEXT.__auth_stubs: 0x150
-  __TEXT.__objc_stubs: 0x2c0
-  __TEXT.__objc_methlist: 0x19c
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x154
-  __TEXT.__oslogstring: 0x5c
-  __TEXT.__objc_classname: 0x59
-  __TEXT.__objc_methname: 0x3a9
-  __TEXT.__objc_methtype: 0x156
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0xb0
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__cfstring: 0x1e0
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x18
+370.33.1.0.0
+  __TEXT.__text: 0x1ef0
+  __TEXT.__auth_stubs: 0x270
+  __TEXT.__objc_stubs: 0x540
+  __TEXT.__objc_methlist: 0x2f4
+  __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x337
+  __TEXT.__oslogstring: 0x7d
+  __TEXT.__objc_methname: 0x62f
+  __TEXT.__objc_classname: 0x10e
+  __TEXT.__objc_methtype: 0x20d
+  __TEXT.__unwind_info: 0xd0
+  __DATA_CONST.__cfstring: 0x2e0
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA.__objc_const: 0x398
-  __DATA.__objc_selrefs: 0x168
-  __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x120
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0x90
+  __DATA.__objc_const: 0x6f8
+  __DATA.__objc_selrefs: 0x218
+  __DATA.__objc_ivar: 0x10
+  __DATA.__objc_data: 0x230
+  __DATA.__data: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libnfshared.dylib
   - /usr/lib/libnfstorage.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 70AA685B-4D92-3F53-B6D1-622E84DB0F53
-  Functions: 7
-  Symbols:   39
-  CStrings:  110
+  UUID: 79565556-B915-3616-8280-F1F101BCBF1E
+  Functions: 27
+  Symbols:   60
+  CStrings:  170
 
Symbols:
+ _OBJC_CLASS_$_NFStorageControllerDeveloperPresentment
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSUUID
+ _objc_alloc
+ _objc_autorelease
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSendSuper2
+ _objc_opt_respondsToSelector
+ _objc_release
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_storeStrong
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
CStrings:
+ ""
+ "%s:%i Invalid params: %@"
+ "%{public}s:%i Invalid params: %@"
+ "-[NFStorageServerDeveloperPresentmentEndpoint deleteWithParams:error:]"
+ "-[NFStorageServerDeveloperPresentmentEndpoint fetchWithParams:error:]"
+ "-[NFStorageServerDeveloperPresentmentEndpoint updateWithParams:error:]"
+ "-[NFStorageServerDeveloperPresentmentReceiptEndpoint updateWithParams:error:]"
+ ".cxx_destruct"
+ "@\"NFStorageControllerApplet\""
+ "@\"NFStorageControllerDeveloperPresentment\""
+ "@\"NFStorageControllerESEExpress\""
+ "@\"NSObject\"24@0:8^@16"
+ "@\"NSObject\"32@0:8@\"NSObject\"16^@24"
+ "@24@0:8^@16"
+ "@32@0:8@16^@24"
+ "@40@0:8@16^@24^@32"
+ "Delete"
+ "DeveloperPresentment"
+ "DeveloperPresentmentReceipt"
+ "Invalid Parameter"
+ "NFStorageServerAppletsEndpoint"
+ "NFStorageServerDeveloperPresentmentEndpoint"
+ "NFStorageServerDeveloperPresentmentReceiptEndpoint"
+ "NFStorageServerEndpoint"
+ "NFStorageServerExpressEndpoint"
+ "Operation Not Supported"
+ "Params"
+ "UUIDString"
+ "Unknown Config"
+ "Unknown Model"
+ "_controller"
+ "_validateBundleIDAndTeamIDParameters:outBundleID:outTeamID:"
+ "_validateReportIdParameter:outError:"
+ "boolValue"
+ "bundleID"
+ "deleteAllReportReceipts"
+ "deleteAllReports"
+ "deleteAllWithError:"
+ "deleteReportWithId:"
+ "deleteWithParams:error:"
+ "doubleValue"
+ "fetchReportWithId:error:"
+ "fetchReportsWithError:"
+ "fetchWithParams:error:"
+ "getLastReportReceiptForBundleID:teamID:outSentTimestamp:outIsOnDenyList:"
+ "init"
+ "initWithUUIDString:"
+ "isOnDenyList"
+ "lastSentTimestamp"
+ "numberWithBool:"
+ "numberWithDouble:"
+ "objectForKey:"
+ "presentmentData"
+ "reportID"
+ "reportReadyToSend"
+ "savePresentmentWithBundleID:teamID:timestampDay:presentmentData:savedToReport:reportReadyToSend:"
+ "stringWithUTF8String:"
+ "teamID"
+ "timestampDay"
+ "unsignedLongLongValue"
+ "updatePresentmentReportReceiptWithBundleID:teamID:sentTimestamp:isOnDenyList:"
+ "updateWithParams:error:"
+ "v16@0:8"
- "Config"
- "Invalid parameter"
- "Unknown config"
- "Unknown model"
- "Unknown operation"
- "delete:withCompletion:"
- "fetch:withCompletion:"
- "update:params:withCompletion:"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"

```
