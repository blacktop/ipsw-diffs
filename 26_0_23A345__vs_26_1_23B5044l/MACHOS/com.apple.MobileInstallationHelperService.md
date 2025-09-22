## com.apple.MobileInstallationHelperService

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/XPCServices/com.apple.MobileInstallationHelperService.xpc/com.apple.MobileInstallationHelperService`

```diff

-1513.2.1.0.0
-  __TEXT.__text: 0x14764
+1513.40.8.0.0
+  __TEXT.__text: 0x15078
   __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_stubs: 0x1f20
-  __TEXT.__objc_methlist: 0x8c4
-  __TEXT.__const: 0xb8
+  __TEXT.__objc_stubs: 0x1f40
+  __TEXT.__objc_methlist: 0x8e4
+  __TEXT.__const: 0xc0
   __TEXT.__objc_classname: 0x17e
-  __TEXT.__objc_methname: 0x2a13
-  __TEXT.__objc_methtype: 0x894
-  __TEXT.__cstring: 0x59e9
+  __TEXT.__objc_methname: 0x2a74
+  __TEXT.__objc_methtype: 0x8e9
+  __TEXT.__cstring: 0x5c79
   __TEXT.__gcc_except_tab: 0x7bc
   __TEXT.__oslogstring: 0x277
-  __TEXT.__unwind_info: 0x3e8
+  __TEXT.__unwind_info: 0x3f8
   __DATA_CONST.__auth_got: 0x628
   __DATA_CONST.__got: 0x200
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x578
-  __DATA_CONST.__cfstring: 0x3220
+  __DATA_CONST.__const: 0x5a0
+  __DATA_CONST.__cfstring: 0x3320
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0xd8
-  __DATA.__objc_const: 0x1078
-  __DATA.__objc_selrefs: 0x958
+  __DATA.__objc_const: 0x10a0
+  __DATA.__objc_selrefs: 0x968
   __DATA.__objc_ivar: 0x50
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x180

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B3A5D37B-8BCD-38B4-BC19-412D05F5AF90
-  Functions: 292
+  UUID: D8F1E5B2-8E48-3B58-AD49-76C1F1BBF6A3
+  Functions: 296
   Symbols:   403
-  CStrings:  1385
+  CStrings:  1407
 
CStrings:
+ "-[MobileInstallationHelperService _onQueue_cloneItemAtURL:toURL:onBehalfOf:completion:]"
+ "-[MobileInstallationHelperService cloneItemAtURL:toURL:onBehalfOf:completion:]"
+ "23:13:46"
+ "Failed to clone item from %@ to %@ because the source doesn't exist."
+ "Failed to clone item from %@ to %@ because the staging location could not be created."
+ "Failed to clone item from %@ to %@ because the staging location could not be resolved."
+ "Failed to lchown %@ : %s"
+ "Failed to remove staging directory at %@: %@"
+ "Failed to rename clone from staged path at %@ to caller's destination at %@"
+ "Parameter validation failed, srcURL %@ parameter was not a valid url"
+ "Sep 16 2025"
+ "_onQueue_cloneItemAtURL:toURL:onBehalfOf:completion:"
+ "cloneItemAtURL:toURL:onBehalfOf:completion:"
+ "copyfile of %@ to %@ failed: %s"
+ "v72@0:8@\"NSURL\"16@\"NSURL\"24{?=[8I]}32@?<v@?@\"NSError\">64"
+ "v72@0:8@16@24{?=[8I]}32@?64"
- "20:53:45"
- "Aug 25 2025"

```
