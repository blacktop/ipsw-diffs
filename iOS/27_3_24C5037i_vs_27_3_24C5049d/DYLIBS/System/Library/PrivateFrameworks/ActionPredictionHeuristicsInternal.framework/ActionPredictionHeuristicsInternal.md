## ActionPredictionHeuristicsInternal

> `/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal`

```diff

-678.2.1.0.3
-  __TEXT.__text: 0x3ccb4
-  __TEXT.__objc_methlist: 0x2a74
+678.2.6.0.2
+  __TEXT.__text: 0x3d248
+  __TEXT.__objc_methlist: 0x2a7c
   __TEXT.__const: 0x338
-  __TEXT.__cstring: 0x322a
+  __TEXT.__cstring: 0x3280
   __TEXT.__gcc_except_tab: 0xe54
-  __TEXT.__oslogstring: 0x726a
+  __TEXT.__oslogstring: 0x730d
   __TEXT.__dlopen_cstrs: 0x1a0
-  __TEXT.__unwind_info: 0x1398
+  __TEXT.__unwind_info: 0x13c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f18
+  __DATA_CONST.__objc_selrefs: 0x1f28
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x130
-  __DATA_CONST.__got: 0x908
+  __DATA_CONST.__got: 0x920
   __AUTH_CONST.__const: 0x9c0
-  __AUTH_CONST.__cfstring: 0x3580
-  __AUTH_CONST.__objc_const: 0x9b68
+  __AUTH_CONST.__cfstring: 0x35a0
+  __AUTH_CONST.__objc_const: 0x9be8
   __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x300
+  __DATA.__objc_ivar: 0x310
   __DATA.__data: 0x340
   __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__data: 0x40

   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient
   - /System/Library/PrivateFrameworks/AppPredictionFoundation.framework/AppPredictionFoundation
+  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CallHistory.framework/CallHistory

   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1221
-  Symbols:   2501
-  CStrings:  964
+  Functions: 1229
+  Symbols:   2510
+  CStrings:  969
 
Symbols:
+ -[ATXHeuristicResultCache _expireAllAndNotifyAppEligibilityChanged]
+ GCC_except_table75
+ _APHiddenAppsChangedNotificationCStr
+ _APLockedAppsChangedNotificationCStr
+ _ATXHeuristicSiriExcludedBundleIds
+ _OBJC_CLASS_$_ATXAppProtectionInfo
+ _OBJC_IVAR_$_ATXHeuristicResultCache._cachedSiriExcludedBundleIds
+ _OBJC_IVAR_$_ATXHeuristicResultCache._hiddenAppsRefreshToken
+ _OBJC_IVAR_$_ATXHeuristicResultCache._lockedAppsRefreshToken
+ _OBJC_IVAR_$_ATXHeuristicResultCache._tccRefreshToken
- GCC_except_table67
CStrings:
+ "Bundle ID %@ is not learnable: locked or hidden."
+ "Expiring all heuristics after Darwin notification '%s'"
+ "Expiring all heuristics after kTCCServiceSiriAccess change"
+ "com.apple.duetexpertd.heuristic.app-eligibility-changed"
+ "com.apple.tcc.access.changed"
```
