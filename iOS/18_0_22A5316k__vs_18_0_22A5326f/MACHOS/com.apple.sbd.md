## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

-638.0.5.0.0
-  __TEXT.__text: 0x6688c
+638.0.9.0.0
+  __TEXT.__text: 0x66b84
   __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_stubs: 0x7700
+  __TEXT.__objc_stubs: 0x76e0
   __TEXT.__objc_methlist: 0x36dc
   __TEXT.__const: 0xd20
-  __TEXT.__gcc_except_tab: 0x20b0
+  __TEXT.__gcc_except_tab: 0x20b8
   __TEXT.__cstring: 0x52a0
-  __TEXT.__objc_methname: 0x89f1
+  __TEXT.__objc_methname: 0x89f7
   __TEXT.__objc_classname: 0x7d8
   __TEXT.__objc_methtype: 0x1281
-  __TEXT.__oslogstring: 0x9abf
+  __TEXT.__oslogstring: 0x9ae4
   __TEXT.__info_plist: 0x66e
-  __TEXT.__unwind_info: 0x1188
+  __TEXT.__unwind_info: 0x1190
   __DATA_CONST.__auth_got: 0x9c8
   __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__auth_ptr: 0x18

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
+  - /System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/AppleIDAuthSupport
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1909
+  Functions: 1915
   Symbols:   449
-  CStrings:  3467
+  CStrings:  3468
 
CStrings:
+ "authKitAccountWithAltDSID:error:"
+ "failed to look up authKitAccount: %!@(MISSING)"
- "authKitAccountWithAltDSID:"

```
