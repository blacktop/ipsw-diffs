## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1576.500.201.2.4
-  __TEXT.__text: 0x18da38
+1576.600.4.0.0
+  __TEXT.__text: 0x18ea54
   __TEXT.__auth_stubs: 0x24f0
-  __TEXT.__objc_methlist: 0x1a5b8
-  __TEXT.__cstring: 0x135f6
+  __TEXT.__objc_methlist: 0x1a670
+  __TEXT.__cstring: 0x13686
   __TEXT.__const: 0x2148
-  __TEXT.__oslogstring: 0x12d87
+  __TEXT.__oslogstring: 0x12fa7
   __TEXT.__gcc_except_tab: 0x197c
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x8df

   __TEXT.__swift_as_ret: 0xa8
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6818
+  __TEXT.__unwind_info: 0x6858
   __TEXT.__eh_frame: 0x19f0
   __TEXT.__objc_classname: 0x2a00
-  __TEXT.__objc_methname: 0x3d6cf
+  __TEXT.__objc_methname: 0x3d8bb
   __TEXT.__objc_methtype: 0x80c6
-  __TEXT.__objc_stubs: 0x218a0
-  __DATA_CONST.__got: 0xe90
-  __DATA_CONST.__const: 0x3718
+  __TEXT.__objc_stubs: 0x21960
+  __DATA_CONST.__got: 0xe98
+  __DATA_CONST.__const: 0x3720
   __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x418
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb100
+  __DATA_CONST.__objc_selrefs: 0xb138
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x6b0
   __DATA_CONST.__objc_arraydata: 0xa00
   __AUTH_CONST.__auth_got: 0x1288
   __AUTH_CONST.__const: 0x3898
-  __AUTH_CONST.__cfstring: 0x11e40
-  __AUTH_CONST.__objc_const: 0x296c0
+  __AUTH_CONST.__cfstring: 0x11ea0
+  __AUTH_CONST.__objc_const: 0x29730
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x40

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6DE5A119-BB48-3373-BBC1-FF572FE61684
-  Functions: 10462
-  Symbols:   30547
-  CStrings:  16674
+  UUID: 415E400B-74C6-396D-A38E-CC1FD28D8DE2
+  Functions: 10479
+  Symbols:   30587
+  CStrings:  16699
 
Symbols:
+ +[TUUserConfiguration faceTimeHideNotifications]
+ +[TUUserConfiguration isSilenceUnknownCallersEnabledForFaceTime]
+ +[TUUserConfiguration migrateLegacyCallFiltering]
+ +[TUUserConfiguration refreshFaceTimeHideNotifications]
+ +[TUUserConfiguration setFaceTimeHideNotifications:]
+ +[TUUserConfiguration setFaceTimeNewCallersFilterMode:]
+ +[TUUserConfiguration shouldHideFaceTimeNotificationsByDefault]
+ -[TUConfigurationProvider faceTimeHideNotifications]
+ -[TUConfigurationProvider isFaceTimeHideNotificationsAvailable]
+ -[TUConfigurationProvider setFaceTimeHideNotifications:]
+ -[TUFeatureFlags ftCallFilteringHideNotificationsEnabled]
+ -[TUFeatureFlags incomingCallNotificationForwardingEnabled]
+ -[TUUserConfiguration faceTimeHideNotifications]
+ -[TUUserConfiguration setFaceTimeHideNotifications:]
+ _TUFaceTimeHideNotificationsKey
+ _TUIsInternationalHandle
+ _TUIsInternationalHandle.cold.1
+ _TUIsInternationalHandle.cold.2
+ _TUIsInternationalRecentCall
+ __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.684
+ __OBJC_$_PROP_LIST_TUFeatureFlags.688
+ ___block_literal_global.139
+ ___block_literal_global.141
+ ___block_literal_global.143
+ ___block_literal_global.177
+ ___block_literal_global.214
+ ___block_literal_global.273
+ ___block_literal_global.363
+ ___block_literal_global.391
+ ___block_literal_global.396
+ ___block_literal_global.401
+ _kCHServiceProviderFaceTime
+ _objc_msgSend$faceTimeHideNotifications
+ _objc_msgSend$ftCallFilteringHideNotificationsEnabled
+ _objc_msgSend$isFaceTimeHideNotificationsAvailable
+ _objc_msgSend$migrateLegacyCallFiltering
+ _objc_msgSend$refreshFaceTimeHideNotifications
+ _objc_msgSend$setFaceTimeHideNotifications:
+ _objc_msgSend$shouldHideFaceTimeNotificationsByDefault
- +[TUUserConfiguration migrateLegaceCallFiltering]
- __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.678
- __OBJC_$_PROP_LIST_TUFeatureFlags.682
- ___block_literal_global.133
- ___block_literal_global.135
- ___block_literal_global.171
- ___block_literal_global.196
- ___block_literal_global.267
- ___block_literal_global.357
- ___block_literal_global.385
- ___block_literal_global.390
- ___block_literal_global.395
- _objc_msgSend$migrateLegaceCallFiltering
CStrings:
+ "%@ facetimeHideNotifications not available, ignoring set request"
+ "%@ setFaceTimeHideNotifications called, set to %d"
+ "%@ shouldHideFaceTimeNotificationsByDefault: silenceEnabled=%d, filterMode=%lu, deviceShouldMitigateSpam=%d -> %d"
+ "FaceTimeHideNotifications"
+ "LocalCountryCodeDebugOverride"
+ "RemoteCountryCodeDebugOverride"
+ "TB,N,SsetFaceTimeHideNotifications:"
+ "TB,R,N,GisFaceTimeHideNotificationsAvailable"
+ "TUIsInternationalHandle called with either nil localCountryCode or nil remoteCountryCode, treating as domestic"
+ "TUIsInternationalHandle called with localCountryCode: '%@' and remoteCountryCode '%@'"
+ "TUIsInternationalHandle resolved localCountryCode: '%@'"
+ "TUIsInternationalHandle resolved resolvedRemoteCountryCode: '%@'"
+ "faceTimeHideNotifications"
+ "faceTimeHideNotificationsAvailable"
+ "ftCallFilteringHideNotifications"
+ "ftCallFilteringHideNotificationsEnabled"
+ "incomingCallNotificationForwarding"
+ "incomingCallNotificationForwardingEnabled"
+ "isFaceTimeHideNotificationsAvailable"
+ "migrateLegacyCallFiltering"
+ "refreshFaceTimeHideNotifications"
+ "setFaceTimeHideNotifications:"
+ "shouldHideFaceTimeNotificationsByDefault"
- "migrateLegaceCallFiltering"

```
