## powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2043.1.1.0.0
-  __TEXT.__text: 0x6cf08
-  __TEXT.__auth_stubs: 0x1da0
-  __TEXT.__objc_stubs: 0x4480
-  __TEXT.__objc_methlist: 0x1dbc
-  __TEXT.__const: 0x360
-  __TEXT.__cstring: 0x7ae8
-  __TEXT.__objc_methname: 0x5c5c
-  __TEXT.__oslogstring: 0xbdb5
+2043.40.52.0.2
+  __TEXT.__text: 0x6d92c
+  __TEXT.__auth_stubs: 0x1dd0
+  __TEXT.__objc_stubs: 0x4520
+  __TEXT.__objc_methlist: 0x1e0c
+  __TEXT.__const: 0x340
+  __TEXT.__cstring: 0x7b33
+  __TEXT.__objc_methname: 0x5d53
+  __TEXT.__oslogstring: 0xbf88
   __TEXT.__objc_classname: 0x2a8
-  __TEXT.__objc_methtype: 0x7b1
-  __TEXT.__gcc_except_tab: 0x3d4
+  __TEXT.__objc_methtype: 0x7b5
+  __TEXT.__gcc_except_tab: 0x3e4
   __TEXT.__dlopen_cstrs: 0x152
-  __TEXT.__unwind_info: 0x1fd8
-  __DATA_CONST.__const: 0x25d0
-  __DATA_CONST.__cfstring: 0x6ba0
+  __TEXT.__unwind_info: 0x2010
+  __DATA_CONST.__const: 0x2590
+  __DATA_CONST.__cfstring: 0x6c00
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0xf0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arrayobj: 0x348
-  __DATA_CONST.__auth_got: 0xee0
-  __DATA_CONST.__got: 0x380
+  __DATA_CONST.__auth_got: 0xef8
+  __DATA_CONST.__got: 0x390
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x3648
-  __DATA.__objc_selrefs: 0x16c0
-  __DATA.__objc_ivar: 0x2b8
+  __DATA.__objc_const: 0x36b0
+  __DATA.__objc_selrefs: 0x16e8
+  __DATA.__objc_ivar: 0x2c0
   __DATA.__objc_data: 0x6e0
   __DATA.__data: 0x8fc
   __DATA.__bss: 0xf30

   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/Versions/A/CoreDuetContext
   - /System/Library/PrivateFrameworks/LockdownMode.framework/Versions/A/LockdownMode
   - /System/Library/PrivateFrameworks/LowPowerMode.framework/Versions/A/LowPowerMode
+  - /System/Library/PrivateFrameworks/MobileActivationMacOS.framework/Versions/A/MobileActivationMacOS
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/Versions/A/OSAnalytics
   - /System/Library/PrivateFrameworks/OSIntelligence.framework/Versions/A/OSIntelligence

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libsystemstats.dylib
-  Functions: 2332
-  Symbols:   593
-  CStrings:  3698
+  Functions: 2350
+  Symbols:   598
+  CStrings:  3718
 
Symbols:
+ _MAEGetActivationStateMacOSWithOptions
+ _MAEGetUCRTActivationLockStateMacOSWithError
+ __CFPreferencesSetMultipleWithContainer
+ _kMAActivationStateActivated
+ _kMAUCRTUnavailable
+ _objc_setProperty_nonatomic
- __CFPreferencesSetValueWithContainer
CStrings:
+ "%@: collecting (connState=%u ncrs=%@ connChanged=%d ncrChanged=%d)"
+ "@24@0:8^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@QI^{?}}16"
+ "DataCollectOnNotChargingReasonChange"
+ "Failed to get UCRT activation lock state: %@\n"
+ "Failed to get activation state: %@\n"
+ "Failed to initialize new pack data (packId=%u status=0x%x)"
+ "Failed to retrieve feature flags (packId=%u status=0x%x)"
+ "Failed to write to CFPreferences (status=0x%x)"
+ "FeatureFlags"
+ "IONVRAM-SYNCNOW-PROPERTY"
+ "Not initializing due to auth not passing (packId=%u failedAuthServiceFlags=%llx)"
+ "Retrieved feature flags (packId=%u flags=0x%llx status=0x%x)"
+ "Setting DOFU requires a customer UCRT: %@\n"
+ "Setting DOFU requires an activated device: %@\n"
+ "T@\"NSMutableDictionary\",&,N,V_lastNotChargingReasons"
+ "TB,N,V_collectOnNCRChange"
+ "_collectOnNCRChange"
+ "_lastNotChargingReasons"
+ "collectOnNCRChange"
+ "i32@0:8@\"NSDictionary\"16^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@QI^{?}}24"
+ "i32@0:8@16^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@QI^{?}}24"
+ "i32@0:8^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@QI^{?}}16^@24"
+ "lastNotChargingReasons"
+ "serviceStateFusionGetFromPacks:"
+ "setCollectOnNCRChange:"
+ "setLastNotChargingReasons:"
- "@24@0:8^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@I^{?}}16"
- "Connected state changed to %u"
- "Failed to initialize new pack data (packId=%u)"
- "i32@0:8@\"NSDictionary\"16^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@I^{?}}24"
- "i32@0:8@16^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@I^{?}}24"
- "i32@0:8^{?=IIb1b1b1b1b1iiiiiiQiiiiiiQIiiQiii@@@qi@@I^{?}}16^@24"
```
