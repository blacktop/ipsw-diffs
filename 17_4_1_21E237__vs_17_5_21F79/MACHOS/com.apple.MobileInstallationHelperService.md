## com.apple.MobileInstallationHelperService

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/XPCServices/com.apple.MobileInstallationHelperService.xpc/com.apple.MobileInstallationHelperService`

```diff

-1270.102.7.0.0
-  __TEXT.__text: 0x12808
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_stubs: 0x1940
+1270.120.9.0.0
+  __TEXT.__text: 0x12a90
+  __TEXT.__auth_stubs: 0xed0
+  __TEXT.__objc_stubs: 0x1960
   __TEXT.__objc_methlist: 0x5b0
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x6d4
-  __TEXT.__cstring: 0x557c
+  __TEXT.__cstring: 0x55dd
   __TEXT.__objc_methname: 0x22e5
   __TEXT.__objc_classname: 0x129
   __TEXT.__objc_methtype: 0x6d0
   __TEXT.__oslogstring: 0x277
-  __TEXT.__unwind_info: 0x3a0
-  __DATA_CONST.__auth_got: 0x770
+  __TEXT.__unwind_info: 0x3a4
+  __DATA_CONST.__auth_got: 0x778
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x3d8
-  __DATA_CONST.__cfstring: 0x2f40
+  __DATA_CONST.__cfstring: 0x2f60
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9076F404-76A0-359D-BEFE-7A51085A3A55
-  Functions: 259
-  Symbols:   401
-  CStrings:  1290
+  UUID: 3A84D249-41B4-36F4-9B4E-3943944665B9
+  Functions: 262
+  Symbols:   404
+  CStrings:  1293
 
Symbols:
+ _MILoadInfoPlistWithError
+ _MILoadRawInfoPlist
+ __CFBundleCopyInfoPlistURL
CStrings:
+ "06:24:25"
+ "Apr 13 2024"
+ "CFBundleGetInfoDictionary failed for bundle at %@"
+ "Error when introspecting %@"
+ "Expected Info.plist file at %@ but found something that was not a file."
+ "Failed to create CFBundle for %@"
+ "Failed to get Info.plist URL from %@; falling back to assumed path"
+ "MILoadInfoPlistWithError"
+ "_CreateCFBundle"
- "00:25:55"
- "CFBundleGetInfoDictionary failed for bundle %@"
- "Error when introspecting %@ : %@"
- "Expected Info.plist file at %@ but found something else: %@"
- "Failed to create CFBundle from URL %@"
- "MILoadInfoPlist"
- "Mar  9 2024"

```
