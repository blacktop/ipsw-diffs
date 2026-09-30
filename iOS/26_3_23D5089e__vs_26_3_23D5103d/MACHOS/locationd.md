## locationd

> `/usr/libexec/locationd`

```diff

-3068.0.7.2.0
-  __TEXT.__text: 0x1bfaac8
+3068.0.10.0.0
+  __TEXT.__text: 0x1bfdf54
   __TEXT.__auth_stubs: 0x6940
   __TEXT.__objc_stubs: 0x47d60
   __TEXT.__init_offsets: 0xa80
   __TEXT.__objc_methlist: 0x33798
-  __TEXT.__const: 0x160de1
-  __TEXT.__cstring: 0x1f6104
-  __TEXT.__gcc_except_tab: 0xdadec
-  __TEXT.__objc_methname: 0x69200
-  __TEXT.__oslogstring: 0x290076
+  __TEXT.__const: 0x160f11
+  __TEXT.__cstring: 0x1f62f4
+  __TEXT.__gcc_except_tab: 0xdadb0
+  __TEXT.__objc_methname: 0x69204
+  __TEXT.__oslogstring: 0x290366
   __TEXT.__objc_classname: 0x83b4
   __TEXT.__objc_methtype: 0x38527
   __TEXT.__constg_swiftt: 0x624

   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_proto: 0x50
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x72520
+  __TEXT.__unwind_info: 0x725e8
   __TEXT.__eh_frame: 0xcc0
   __DATA_CONST.__auth_got: 0x34c0
   __DATA_CONST.__got: 0x2fb0
   __DATA_CONST.__auth_ptr: 0x5b0
-  __DATA_CONST.__const: 0xbf188
+  __DATA_CONST.__const: 0xbf478
   __DATA_CONST.__cfstring: 0x457a0
   __DATA_CONST.__objc_classlist: 0x15f0
   __DATA_CONST.__objc_catlist: 0xd8

   __DATA.__objc_ivar: 0x3ed0
   __DATA.__objc_data: 0xe2b8
   __DATA.__data: 0x61d58
-  __DATA.__common: 0x21e18
+  __DATA.__common: 0x21e38
   __DATA.__bss: 0x118b8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 89D451DC-E8E9-354D-9622-9A874A27F866
-  Functions: 106676
+  UUID: 0AB957CB-47C8-37C3-87C0-D9BBFCD73D2F
+  Functions: 106741
   Symbols:   3357
-  CStrings:  95854
+  CStrings:  95868
 
CStrings:
+ "#fusion,CLLCFusionCarPlayFlags unexpectedly returned nullptr"
+ "#fusion,mct,%{public}.3f,Override likelyOutOfAVisit to true,likelyDistanceMovedSinceInsideAVisit_m,%{public}.1f"
+ "#fusion,mct_now,%{public}.3f,moving motion state override to low confidence Walk,InVisit,%{public}d,IsLikelyOutOfAVisit,%{public}d,hasRecentPersonalizedWiFiFix,%{public}d,timeSinceLastNonCellLocationFix_s,%{public}.3f"
+ "#fusion,now_mct,%{public}.3f,before processing buffer data transition fusion state to running mode"
+ "-[CLAuthorizationDatabase registerClient:allowUninstalled:]"
+ "/AppleInternal/Library/BuildRoots/4~CGMVugAgppB-b21TXLS5EGztwhpeLQV5IocWrgQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CGMVugAgppB-b21TXLS5EGztwhpeLQV5IocWrgQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
+ "/AppleInternal/Library/BuildRoots/4~CGMVugAgppB-b21TXLS5EGztwhpeLQV5IocWrgQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CGMVugAgppB-b21TXLS5EGztwhpeLQV5IocWrgQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/4~CGMVugAgppB-b21TXLS5EGztwhpeLQV5IocWrgQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "20:27:40"
+ "20:34:19"
+ "::CLP::LogEntry::PrivateData::MobileAssetNotification_NotificationType_IsValid(value)"
+ "CLP.LogEntry.PrivateData.MobileAssetNotification"
+ "CLP.LogEntry.PrivateData.MobileAssetNotification.KeyValueList"
+ "CLP.LogEntry.PrivateData.MobileAssetNotification.KeyValuePair"
+ "CLP.LogEntry.PrivateData.MobileAssetNotification.NotificationData"
+ "CLP.LogEntry.Raven.TunnelBridgeState"
+ "Jan  6 2026"
+ "Jan  6 2026 20:30:40"
+ "registerClient:allowUninstalled:"
+ "void CLLCFusionCarPlayConditions::updateConditions()"
+ "void CLLCFusionCarPlayFlags::readCarPlayLCFusionDefaultsWriteSetting()"
+ "{\"msg%{public}.0s\":\"#Warning Not using location because interval has not elapsed\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"long\":%{public, location:Encrypted_longitude}.*P, \"timestamp\":\"%{public}0.2f\", \"source\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"Not reporting metric for re-evaluation of Geo reported unconfirmed time zone\"}"
+ "{\"msg%{public}.0s\":\"we've previously confirmed our Location timezone\"}"
+ "{\"msg%{public}.0s\":\"we've previously confirmed our LocationBorder timezone\"}"
- "#fusion,mct_now,%{public}.3f,moving motion state override to low confidence Walk,InVisit,%{public}d,IsLikelyOutOfAVisit,%{public}d,WiFiServiceStatesAssociated,%{public}d"
- "-[CLAuthorizationDatabase registerClient:fromAuthSync:]"
- "/AppleInternal/Library/BuildRoots/4~CEEfugCev5rwp7n2DRam0g4zKPUm-iKekplXcDE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
- "/AppleInternal/Library/BuildRoots/4~CEEfugCev5rwp7n2DRam0g4zKPUm-iKekplXcDE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
- "/AppleInternal/Library/BuildRoots/4~CEEfugCev5rwp7n2DRam0g4zKPUm-iKekplXcDE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "/AppleInternal/Library/BuildRoots/4~CEEfugCev5rwp7n2DRam0g4zKPUm-iKekplXcDE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/4~CEEfugCev5rwp7n2DRam0g4zKPUm-iKekplXcDE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "20:59:27"
- "21:06:27"
- "Dec  8 2025"
- "Dec  8 2025 21:02:36"
- "registerClient:fromAuthSync:"
- "{\"msg%{public}.0s\":\"we've previously confirmed our timezone\"}"

```
