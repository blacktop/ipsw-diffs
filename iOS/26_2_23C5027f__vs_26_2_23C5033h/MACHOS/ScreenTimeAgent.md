## ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

-605.2.3.0.0
-  __TEXT.__text: 0x11f5c4
-  __TEXT.__auth_stubs: 0x2250
+605.2.5.0.0
+  __TEXT.__text: 0x120730
+  __TEXT.__auth_stubs: 0x2260
   __TEXT.__objc_stubs: 0x116a0
-  __TEXT.__objc_methlist: 0xa068
-  __TEXT.__const: 0x4a80
+  __TEXT.__objc_methlist: 0xa088
+  __TEXT.__const: 0x4a90
   __TEXT.__gcc_except_tab: 0x2278
-  __TEXT.__cstring: 0xd61e
-  __TEXT.__oslogstring: 0x13920
-  __TEXT.__objc_methname: 0x1bbe6
+  __TEXT.__cstring: 0xd69e
+  __TEXT.__oslogstring: 0x13a90
+  __TEXT.__objc_methname: 0x1bd11
   __TEXT.__objc_classname: 0x1fa7
-  __TEXT.__objc_methtype: 0x552e
-  __TEXT.__constg_swiftt: 0x3030
-  __TEXT.__swift5_typeref: 0x2756
+  __TEXT.__objc_methtype: 0x5586
+  __TEXT.__constg_swiftt: 0x3050
+  __TEXT.__swift5_typeref: 0x278c
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0x1fc9
-  __TEXT.__swift5_fieldmd: 0x1474
+  __TEXT.__swift5_reflstr: 0x1fd9
+  __TEXT.__swift5_fieldmd: 0x1490
   __TEXT.__swift5_assocty: 0x248
-  __TEXT.__swift5_proto: 0x24c
+  __TEXT.__swift5_proto: 0x250
   __TEXT.__swift5_types: 0x178
   __TEXT.__swift5_capture: 0x21c4
   __TEXT.__swift_as_entry: 0x264
   __TEXT.__swift_as_ret: 0x198
-  __TEXT.__swift5_protos: 0x98
+  __TEXT.__swift5_protos: 0x9c
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x4200
+  __TEXT.__unwind_info: 0x4228
   __TEXT.__eh_frame: 0x4ea8
-  __DATA_CONST.__auth_got: 0x1138
-  __DATA_CONST.__got: 0x12d0
+  __DATA_CONST.__auth_got: 0x1140
+  __DATA_CONST.__got: 0x12d8
   __DATA_CONST.__auth_ptr: 0x668
-  __DATA_CONST.__const: 0x9980
+  __DATA_CONST.__const: 0x99b8
   __DATA_CONST.__cfstring: 0x4c20
   __DATA_CONST.__objc_classlist: 0x678
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x1e108
-  __DATA.__objc_selrefs: 0x5628
+  __DATA.__objc_const: 0x1e198
+  __DATA.__objc_selrefs: 0x5658
   __DATA.__objc_ivar: 0x800
-  __DATA.__objc_data: 0x4a80
-  __DATA.__data: 0x7110
+  __DATA.__objc_data: 0x4a88
+  __DATA.__data: 0x7138
   __DATA.__bss: 0x3730
   __DATA.__common: 0xa0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/AskTo.framework/AskTo

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C2B16D5A-B182-38C1-89BC-4D02B6E26490
-  Functions: 5970
-  Symbols:   1299
-  CStrings:  7990
+  UUID: D16FBB28-D63C-3057-82D5-6D7387B94F5F
+  Functions: 5984
+  Symbols:   1301
+  CStrings:  8008
 
Symbols:
+ _$sSa11descriptionSSvg
+ _OBJC_CLASS_$_ASDAppStoreService
CStrings:
+ "Applying regulatory restrictions: Web Content Filter forced to Limit Adult Websites"
+ "Applying user settings Web Content Filter"
+ "Deleting web content filter stores in container '%s': %s"
+ "Error checking if web content filter is forced: %{public}@ ; assuming forced"
+ "Failed to inform AppStore on exception deletion. Error: %@"
+ "Informed AppStore on exception deletion. Success:%{bool}d"
+ "WebContentFilterStore:Regulatory"
+ "appStoreService"
+ "applicationsDidUpdateMetadata:"
+ "applyWebContentFilterForFamilyMemberType:"
+ "com.apple.screentime.regulatory"
+ "containerNamesForDeletion: %{public}s"
+ "currentContainerName: %{public}s"
+ "defaultService"
+ "initWithUnsignedLongLong:"
+ "isCommunicationSafetyForcedToEnabledForFamilyMemberType:error:"
+ "isWebContentFilterForcedToLimitAdultWebsitesForFamilyMemberType:error:"
+ "revokeAppConsentForAccountID:itemID:account:completionBlock:"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"
- "Deleting web content filter stores in other container: %s"
- "applyWebContentFilter"
- "currentContainerName: %{public}s, otherContainerName: %{public}s"
- "isCommunicationSafetyForcedToEnabledAndReturnError:"

```
