## libSecureMAHelper.dylib

> `/usr/lib/libSecureMAHelper.dylib`

```diff

-1487.122.1.0.0
-  __TEXT.__text: 0x10050
-  __TEXT.__auth_stubs: 0x9d0
+1788.0.0.0.4
+  __TEXT.__text: 0xfe14
+  __TEXT.__auth_stubs: 0x9a0
   __TEXT.__objc_methlist: 0x614
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x213d
-  __TEXT.__oslogstring: 0x1cb6
+  __TEXT.__cstring: 0x2220
+  __TEXT.__oslogstring: 0x1bc6
   __TEXT.__gcc_except_tab: 0x758
-  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__unwind_info: 0x2d0
   __TEXT.__objc_classname: 0xca
   __TEXT.__objc_methname: 0x11b1
   __TEXT.__objc_methtype: 0x3f3
   __TEXT.__objc_stubs: 0x1360
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x370
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__const: 0x3a8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x4f8
+  __AUTH_CONST.__auth_got: 0x4e0
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x2540
+  __AUTH_CONST.__cfstring: 0x2680
   __AUTH_CONST.__objc_const: 0x620
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 22A32092-B801-303E-A2FA-1C4DADD50FA3
-  Functions: 168
-  Symbols:   878
-  CStrings:  1026
+  UUID: 5F187017-3F07-3933-B9DB-42D823E96405
+  Functions: 167
+  Symbols:   882
+  CStrings:  1041
 
Symbols:
+ ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1187
+ ___MABrainUtilityScheduleDeviceUnlockAction_block_invoke.398
+ ___block_literal_global.1182
+ ___block_literal_global.1318
+ ___block_literal_global.1575
+ ___block_literal_global.1789
+ ___block_literal_global.408
+ ___kCFBooleanFalse
+ _kMobileAssetPreferencesAnalyticsSendImmediate
+ _kMobileAssetPreferencesAutoAssetSuspendResumeTimeoutCancelOverride
+ _kMobileAssetPreferencesAutoAssetSuspendResumeTimeoutEvictOverride
+ _kMobileAssetPreferencesAutoHealthReportSetNames
+ _kMobileAssetPreferencesAutoStartupHealthReport
+ _kMobileAssetPreferencesFakeDeviceRecoveryMode
+ _kMobileAssetPreferencesReclaimStatOnlyForAssetTypes
- _MABrainUtilityBootSessionUUID
- __NSGetMachExecuteHeader
- ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1160
- ___MABrainUtilityScheduleDeviceUnlockAction_block_invoke.393
- ___block_literal_global.1155
- ___block_literal_global.1270
- ___block_literal_global.1539
- ___block_literal_global.1753
- ___block_literal_global.403
- _malloc_type_malloc
- _sysctlbyname
Functions:
~ _MABrainUtilityGetImageUUID : 284 -> 280
- _MABrainUtilityBootSessionUUID
~ _syncPreferences : 368 -> 288
~ +[SecureMobileAssetBundle getSigningServerURL:] : 448 -> 496
~ -[SecureMobileAssetBundle _personalize:error:] : 9276 -> 9296
~ -[SecureMobileAssetBundle attach:error:] : 1984 -> 2080
~ -[SecureMobileAssetBundle beginAccess_nowait:error:] : 3276 -> 3280
CStrings:
+ "AnalyticsSendImmediate"
+ "Asset type+specifier is unsupported in Exclaves"
+ "AutoAssetSuspendResumeTimeoutCancelOverride"
+ "AutoAssetSuspendResumeTimeoutEvictOverride"
+ "AutoHealthReportSets"
+ "AutoStartupHealthReport"
+ "FakeDeviceRecoveryMode"
+ "OSInternal"
+ "ReclaimStatOnlyForAssetTypes"
+ "[SMA] Overridden signing server is '%@'"
+ "[SMA] signing server override was set but was invalid"
+ "autodiskmount"
+ "write-protected"
- "Asset type+sepcifier is unsupported in Exclaves"
- "[MAB] Boot session UUID has an invalid length (%zu)"
- "[MAB] Could not allocate buffer to copy boot session UUID"
- "[MAB] Could not copy boot session UUID: %d (%s)"
- "[MAB] Could not look up boot session UUID: %d (%s)"
- "[MA_PREFS] {%{public}@} [%{public}@] Synchronized preferences for %{public}@"
- "[SMA] Using overridden value for signing server"
- "kern.bootsessionuuid"

```
