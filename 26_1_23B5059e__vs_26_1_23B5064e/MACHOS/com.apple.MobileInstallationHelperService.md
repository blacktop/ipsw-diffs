## com.apple.MobileInstallationHelperService

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/XPCServices/com.apple.MobileInstallationHelperService.xpc/com.apple.MobileInstallationHelperService`

```diff

-1513.40.11.502.1
-  __TEXT.__text: 0x15078
+1513.40.14.0.0
+  __TEXT.__text: 0x150cc
   __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_stubs: 0x1f40
+  __TEXT.__objc_stubs: 0x1f20
   __TEXT.__objc_methlist: 0x8e4
   __TEXT.__const: 0xc0
   __TEXT.__objc_classname: 0x17e
-  __TEXT.__objc_methname: 0x2a74
+  __TEXT.__objc_methname: 0x2a5d
   __TEXT.__objc_methtype: 0x8e9
-  __TEXT.__cstring: 0x5c79
+  __TEXT.__cstring: 0x5d18
   __TEXT.__gcc_except_tab: 0x7bc
   __TEXT.__oslogstring: 0x277
   __TEXT.__unwind_info: 0x3f8

   __DATA_CONST.__got: 0x200
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x5a0
-  __DATA_CONST.__cfstring: 0x3320
+  __DATA_CONST.__cfstring: 0x3360
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA.__objc_const: 0x10a0
-  __DATA.__objc_selrefs: 0x968
+  __DATA.__objc_selrefs: 0x960
   __DATA.__objc_ivar: 0x50
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x180

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 04CB0D82-56D5-3AA9-B0E6-115A5002B306
-  Functions: 296
-  Symbols:   403
-  CStrings:  1407
+  UUID: 3EDE4942-1230-3C98-B9C0-EE46A7ECCFD2
+  Functions: 297
+  Symbols:   404
+  CStrings:  1410
 
Symbols:
+ _MICreateCFBundleEnforcingInfoPlistSize
Functions:
~ _MICreateCFBundle : 752 -> 16
+ _MICreateCFBundleEnforcingInfoPlistSize
~ _MILoadInfoPlistWithError : 224 -> 228
~ _MILoadRawInfoPlist : 252 -> 256
CStrings:
+ "01:21:07"
+ "Expected Info.plist file at %@ but found something that was not a file (found mode 0%o)."
+ "MICreateCFBundleEnforcingInfoPlistSize"
+ "Oct  6 2025"
+ "The Info.plist at %@ is too large. Found %lld bytes on disk, but maximum allowed size is %lld bytes."
+ "lstat of %@ failed"
- "20:41:33"
- "Expected Info.plist file at %@ but found something that was not a file."
- "MICreateCFBundle"
- "Sep 29 2025"
- "itemIsFileAtURL:error:"

```
