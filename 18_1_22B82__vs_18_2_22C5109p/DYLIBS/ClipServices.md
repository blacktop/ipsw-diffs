## ClipServices

> `/System/Library/PrivateFrameworks/ClipServices.framework/ClipServices`

```diff

-1021.3.0.0.0
-  __TEXT.__text: 0x37994
+1023.2.0.0.0
+  __TEXT.__text: 0x38f88
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x28f4
+  __TEXT.__objc_methlist: 0x298c
   __TEXT.__gcc_except_tab: 0xbe0
   __TEXT.__const: 0x110
-  __TEXT.__oslogstring: 0x4471
-  __TEXT.__cstring: 0x3c60
+  __TEXT.__cstring: 0x3da1
+  __TEXT.__oslogstring: 0x4578
   __TEXT.__dlopen_cstrs: 0x2e4
-  __TEXT.__unwind_info: 0x1008
-  __TEXT.__objc_classname: 0x51a
-  __TEXT.__objc_methname: 0x9c09
-  __TEXT.__objc_methtype: 0x13ec
-  __TEXT.__objc_stubs: 0x6d80
+  __TEXT.__unwind_info: 0x1050
+  __TEXT.__objc_classname: 0x52c
+  __TEXT.__objc_methname: 0x9f2c
+  __TEXT.__objc_methtype: 0x145c
+  __TEXT.__objc_stubs: 0x6f20
   __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__const: 0x1818
-  __DATA_CONST.__objc_classlist: 0x140
+  __DATA_CONST.__const: 0x18d0
+  __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2150
+  __DATA_CONST.__objc_selrefs: 0x21e0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x4b8
-  __AUTH_CONST.__const: 0x5e0
-  __AUTH_CONST.__cfstring: 0x3240
-  __AUTH_CONST.__objc_const: 0x5e60
+  __AUTH_CONST.__const: 0x620
+  __AUTH_CONST.__cfstring: 0x32e0
+  __AUTH_CONST.__objc_const: 0x5f90
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0x370
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x374
   __DATA.__data: 0x730
   __DATA.__bss: 0x130
   __DATA_DIRTY.__objc_data: 0xc80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1409
-  Symbols:   1862
-  CStrings:  2564
+  Functions: 1440
+  Symbols:   1895
+  CStrings:  2602
 
Symbols:
+ _OBJC_CLASS_$_CPSWebClipService
+ _OBJC_METACLASS_$_CPSWebClipService
CStrings:
+ "\x01!\x15\x14"
+ "%!@(MISSING)-%!@(MISSING)-%!@(MISSING)-%!@(MISSING)-%!@(MISSING)"
+ "%!@(MISSING): \n  uuid = %!@(MISSING),\n  webClipType = %!l(MISSING)d,\n  title = %!@(MISSING),\n  bundleVersion = %!l(MISSING)u,\n  bundleIdentifier = %!@(MISSING),\n  scenelessBackgroundLaunch = %!d(MISSING),\n  applicationBundleIdentifier = %!@(MISSING),\n  trustedClientBundleIdentifiers = %!@(MISSING),\n  pageURL = %!@(MISSING),\n  registeredURL = %!@(MISSING),\n  registeredURLHash = %!@(MISSING),\n  appClipUserActivity = %!@(MISSING),\n  path = %!@(MISSING),\n  iconImagePath = %!@(MISSING),\n  localizedSubtitle = %!@(MISSING),\n  fullAppName = %!@(MISSING),\n  fullAppCaption = %!@(MISSING),\n  fullAppStoreURL = %!@(MISSING),\n  applicationInstalled = %!d(MISSING),\n  dictionaryRepresentation = %!@(MISSING)"
+ "@\"NSSet\""
+ "@\"NSString\"16@?0@\"CPSWebClip\"8"
+ "@\"NSURL\"16@?0@\"NSString\"8"
+ "@\"NSUUID\"16@?0@\"NSString\"8"
+ "@16@?0@\"CPSWebClip\"8"
+ "ApplicationManifest"
+ "CPSWebClipService"
+ "DictionaryRepresentationIdentifier"
+ "DictionaryRepresentationManifest"
+ "T@\"NSSet\",R,N,V_trustedClientBundleIdentifiers"
+ "T@\"NSUUID\",R,N"
+ "TrustedClientBundleIdentifiers"
+ "_enumerateAndMapClipsWithBlock:"
+ "_trustedClientBundleIdentifiers"
+ "dictionaryWithContentsOfFile:"
+ "fetchWebClipsURLForClientBundleID:completion:"
+ "fetchWebClipsURLStringForClientBundleID: Cannot connect to daemon with error: %!{(MISSING)public}@"
+ "fetchWebClipsURLStringForClientBundleID:completion:"
+ "fetchWebClipsURLStringForClientBundleID:completionHandler:"
+ "fetchWebClipsURLStringForClientBundleID:reply:"
+ "fetchWebClipsUUIDForClientBundleID:completion:"
+ "fetchWebClipsUUIDStringForClientBundleID: Cannot connect to daemon with error: %!{(MISSING)public}@"
+ "fetchWebClipsUUIDStringForClientBundleID:completion:"
+ "fetchWebClipsUUIDStringForClientBundleID:completionHandler:"
+ "fetchWebClipsUUIDStringForClientBundleID:reply:"
+ "getWebClipDictionaryWithIdentifier: Cannot connect to daemon with error: %!{(MISSING)public}@"
+ "getWebClipDictionaryWithIdentifier:completion:"
+ "getWebClipDictionaryWithIdentifier:completionHandler:"
+ "getWebClipDictionaryWithIdentifier:reply:"
+ "initWithString:"
+ "initWithUUIDString:"
+ "substringWithRange:"
+ "trustedClientBundleIdentifiers"
+ "uuid"
+ "v24@?0@\"NSError\"8@\"NSArray\"16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\"@\"NSArray\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\"@\"NSDictionary\">24"
- "\x01!\x14\x14"
- "%!@(MISSING): \n  webClipType = %!l(MISSING)d,\n  title = %!@(MISSING),\n  bundleVersion = %!l(MISSING)u,\n  bundleIdentifier = %!@(MISSING),\n  scenelessBackgroundLaunch = %!d(MISSING),\n  applicationBundleIdentifier = %!@(MISSING),\n  pageURL = %!@(MISSING),\n  registeredURL = %!@(MISSING),\n  registeredURLHash = %!@(MISSING),\n  appClipUserActivity = %!@(MISSING),\n  path = %!@(MISSING),\n  iconImagePath = %!@(MISSING),\n  localizedSubtitle = %!@(MISSING),\n  fullAppName = %!@(MISSING),\n  fullAppCaption = %!@(MISSING),\n  fullAppStoreURL = %!@(MISSING),\n  applicationInstalled = %!d(MISSING),\n  dictionaryRepresentation = %!@(MISSING)"

```
