## ClipServices

> `/System/Library/PrivateFrameworks/ClipServices.framework/ClipServices`

```diff

-1025.6.0.0.0
-  __TEXT.__text: 0x39ce8
+1031.8.0.0.0
+  __TEXT.__text: 0x3a74c
   __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_methlist: 0x319c
-  __TEXT.__gcc_except_tab: 0xc98
+  __TEXT.__objc_methlist: 0x321c
+  __TEXT.__gcc_except_tab: 0xd60
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x3e00
-  __TEXT.__oslogstring: 0x478e
+  __TEXT.__cstring: 0x3eb2
+  __TEXT.__oslogstring: 0x4774
   __TEXT.__dlopen_cstrs: 0x2e4
-  __TEXT.__unwind_info: 0x10c0
+  __TEXT.__unwind_info: 0x10e0
   __TEXT.__objc_classname: 0x52c
-  __TEXT.__objc_methname: 0xa028
+  __TEXT.__objc_methname: 0xa158
   __TEXT.__objc_methtype: 0x145c
-  __TEXT.__objc_stubs: 0x7000
+  __TEXT.__objc_stubs: 0x71c0
   __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__const: 0x1970
+  __DATA_CONST.__const: 0x19c8
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2478
+  __DATA_CONST.__objc_selrefs: 0x24e8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x4c0
   __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x3300
-  __AUTH_CONST.__objc_const: 0x5090
+  __AUTH_CONST.__cfstring: 0x3400
+  __AUTH_CONST.__objc_const: 0x5120
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x374
+  __DATA.__objc_ivar: 0x37c
   __DATA.__data: 0x730
   __DATA.__bss: 0x130
   __DATA_DIRTY.__objc_data: 0xc80

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 78DDD2B7-79BD-3EBF-81DF-BCD14628ECD4
-  Functions: 1469
-  Symbols:   5236
-  CStrings:  3011
+  UUID: E01D202C-EBA3-3061-A30B-53C01EEA7694
+  Functions: 1482
+  Symbols:   5274
+  CStrings:  3044
 
Symbols:
+ -[CPSClipMetadata setSupportsArcade:]
+ -[CPSClipMetadata supportsArcade]
+ -[CPSWebClip setSupportsArcade:]
+ -[CPSWebClip supportsArcade]
+ -[NSString(ClipServicesExtras) cps_looksLikeStoreItemIdentifier]
+ -[NSURL(ClipServicesExtras) cps_embeddedBundleIdentifierInDefaultLink]
+ -[NSURL(ClipServicesExtras) cps_embeddedBundleIdentifierInDemoLink]
+ -[NSURL(ClipServicesExtras) cps_embeddedItemID]
+ -[NSURL(ClipServicesExtras) cps_isDemoLink]
+ -[NSURL(ClipServicesExtras) cps_sanitizedURL]
+ _CPSClipMetadataKeySupportsArcade
+ _CPSSimulateArcadeAppClipForTesting
+ _OBJC_IVAR_$_CPSClipMetadata._supportsArcade
+ _OBJC_IVAR_$_CPSWebClip._supportsArcade
+ ___45-[NSURL(ClipServicesExtras) cps_sanitizedURL]_block_invoke
+ ___47-[NSURL(ClipServicesExtras) cps_embeddedItemID]_block_invoke
+ ___block_descriptor_40_e8_32r_e25_v32?0"NSString"8Q16^B24lr32l8
+ ___block_descriptor_48_e8_32s40s_e37_v24?0"CPSClipMetadata"8"NSError"16ls32l8s40l8
+ ___block_literal_global.289
+ _objc_msgSend$containsString:
+ _objc_msgSend$cps_embeddedBundleIdentifierInDefaultLink
+ _objc_msgSend$cps_embeddedBundleIdentifierInDemoLink
+ _objc_msgSend$cps_embeddedItemID
+ _objc_msgSend$cps_isDemoLink
+ _objc_msgSend$cps_looksLikeStoreItemIdentifier
+ _objc_msgSend$cps_sanitizedURL
+ _objc_msgSend$pathComponents
+ _objc_msgSend$setHost:
+ _objc_msgSend$setPath:
+ _objc_msgSend$setScheme:
+ _objc_msgSend$setSupportsArcade:
+ _objc_msgSend$string
+ _objc_msgSend$supportsArcade
- ___block_literal_global.286
CStrings:
+ "\n  clipName = %@,\n  abrClipCaption = %@,\n  storeClipCaption = %@, \n  clipCaption = %@,\n  clipBundleID = %@,\n  clipHeroImageURL = %@,\n  clipOpenButtonTitle = %@,\n  clipURL = %@,\n  clipIpaURL = %@,\n  clipRequestURL = %@,\n  clipMinimumOSVersion = %@,\n  fullAppName = %@,\n  fullAppShortName = %@,\n  fullAppCaption = %@,\n  fullAppContentRating = %@,\n  fullAppBundleID = %@,\n  fullAppStoreURL = %@,\n  fullAppIconURL = %@, \n  isPoweredBy = %@, \n  supportsArcade = %@, \n  provider = %@, \n  webClipID = %@, \n  clipURLHash = %@, \n  clipVersionIdentifier = %llu \n  clipRequestsLocationConfirmationPermission = %@ \n  clipRequestsNotificationPermission = %@ \n  expirationDate = %@ \n  bundleDisplayName = %@ \n  thinnedSize = %@ \n"
+ "%@: \n  uuid = %@,\n  webClipType = %ld,\n  title = %@,\n  bundleVersion = %lu,\n  bundleIdentifier = %@,\n  scenelessBackgroundLaunch = %d,\n  applicationBundleIdentifier = %@,\n  trustedClientBundleIdentifiers = %@,\n  pageURL = %@,\n  registeredURL = %@,\n  registeredURLHash = %@,\n  appClipUserActivity = %@,\n  path = %@,\n  iconImagePath = %@,\n  localizedSubtitle = %@,\n  supportsArcade = %@,\n  fullAppName = %@,\n  fullAppCaption = %@,\n  fullAppStoreURL = %@,\n  applicationInstalled = %d,\n  dictionaryRepresentation = %@"
+ "/%@"
+ "/%@/%@"
+ "CPSSimulateArcadeAppClip"
+ "SupportsArcade"
+ "TB,N,V_supportsArcade"
+ "Updating a demo app clip on physical invocation."
+ "_supportsArcade"
+ "app-clip-bundle-id"
+ "apps.apple.com"
+ "containsString:"
+ "cps_embeddedBundleIdentifierInDefaultLink"
+ "cps_embeddedBundleIdentifierInDemoLink"
+ "cps_embeddedItemID"
+ "cps_isDemoLink"
+ "cps_looksLikeStoreItemIdentifier"
+ "cps_sanitizedURL"
+ "demo"
+ "pathComponents"
+ "setHost:"
+ "setPath:"
+ "setScheme:"
+ "setSupportsArcade:"
+ "string"
+ "supportsArcade"
+ "v32@?0@\"NSString\"8Q16^B24"
- "\n  clipName = %@,\n  abrClipCaption = %@,\n  storeClipCaption = %@, \n  clipCaption = %@,\n  clipBundleID = %@,\n  clipHeroImageURL = %@,\n  clipOpenButtonTitle = %@,\n  clipURL = %@,\n  clipIpaURL = %@,\n  clipRequestURL = %@,\n  clipMinimumOSVersion = %@,\n  fullAppName = %@,\n  fullAppShortName = %@,\n  fullAppCaption = %@,\n  fullAppContentRating = %@,\n  fullAppBundleID = %@,\n  fullAppStoreURL = %@,\n  fullAppIconURL = %@, \n  isPoweredBy = %@, \n  provider = %@, \n  webClipID = %@, \n  clipURLHash = %@, \n  clipVersionIdentifier = %llu \n  clipRequestsLocationConfirmationPermission = %@ \n  clipRequestsNotificationPermission = %@ \n  expirationDate = %@ \n  bundleDisplayName = %@ \n  thinnedSize = %@ \n"
- "%@: \n  uuid = %@,\n  webClipType = %ld,\n  title = %@,\n  bundleVersion = %lu,\n  bundleIdentifier = %@,\n  scenelessBackgroundLaunch = %d,\n  applicationBundleIdentifier = %@,\n  trustedClientBundleIdentifiers = %@,\n  pageURL = %@,\n  registeredURL = %@,\n  registeredURLHash = %@,\n  appClipUserActivity = %@,\n  path = %@,\n  iconImagePath = %@,\n  localizedSubtitle = %@,\n  fullAppName = %@,\n  fullAppCaption = %@,\n  fullAppStoreURL = %@,\n  applicationInstalled = %d,\n  dictionaryRepresentation = %@"
- "%{public}@ (%p): Not launched thorugh NFC, full app fast path not eligible"

```
