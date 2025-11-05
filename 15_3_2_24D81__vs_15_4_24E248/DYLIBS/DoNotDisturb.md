## DoNotDisturb

> `/System/Library/PrivateFrameworks/DoNotDisturb.framework/Versions/A/DoNotDisturb`

```diff

-433.4.2.0.0
-  __TEXT.__text: 0x4c8b8
+433.5.22.0.0
+  __TEXT.__text: 0x4c51c
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x3f04
-  __TEXT.__const: 0x25a
+  __TEXT.__objc_methlist: 0x465c
+  __TEXT.__const: 0x262
   __TEXT.__cstring: 0x3647
   __TEXT.__gcc_except_tab: 0x1644
-  __TEXT.__oslogstring: 0x53ba
-  __TEXT.__unwind_info: 0x1580
+  __TEXT.__oslogstring: 0x53bb
+  __TEXT.__unwind_info: 0x15d0
   __TEXT.__objc_classname: 0xf4b
   __TEXT.__objc_methname: 0x8e07
   __TEXT.__objc_methtype: 0x1e7a

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1978
+  __DATA_CONST.__objc_selrefs: 0x1a00
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0x1280
   __AUTH_CONST.__cfstring: 0x37a0
-  __AUTH_CONST.__objc_const: 0xd870
+  __AUTH_CONST.__objc_const: 0xcbe0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1c20
   __DATA.__objc_ivar: 0x3dc

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 6781E38B-9B97-3F33-9E70-F6A60E051DCA
-  Functions: 1680
-  Symbols:   4293
+  UUID: 656C4DFA-92B9-3D68-9EA3-2B1F7E3CEB66
+  Functions: 1699
+  Symbols:   4315
   CStrings:  2850
 
Symbols:
+ +[DNDAppConfigurationService serviceForClientIdentifier:].cold.1
+ +[DNDAppInfoService serviceForClientIdentifier:].cold.1
+ +[DNDAuxiliaryStateService serviceForClientIdentifier:].cold.1
+ +[DNDAvailabilityService serviceForClientIdentifier:].cold.1
+ +[DNDEventBehaviorResolutionService serviceForClientIdentifier:].cold.1
+ +[DNDGlobalConfigurationService serviceForClientIdentifier:].cold.1
+ +[DNDHearingTestService serviceForClientIdentifier:].cold.1
+ +[DNDMeDeviceService serviceForClientIdentifier:].cold.1
+ +[DNDModeAssertionLifetime _secureCodingLifetimeClasses].cold.1
+ +[DNDModeAssertionService serviceForClientIdentifier:].cold.1
+ +[DNDModeConfigurationService serviceForClientIdentifier:].cold.1
+ +[DNDModeSelectionService serviceForClientIdentifier:].cold.1
+ +[DNDSettingsService serviceForClientIdentifier:].cold.1
+ +[DNDStateService serviceForClientIdentifier:].cold.1
+ +[NSBundle(DoNotDisturb) dnd_doNotDisturbLocalizationBundle].cold.1
+ +[NSBundle(DoNotDisturb) dnd_locationBundle].cold.1
+ DNDRegisterLogging.cold.1
+ DNDRemoteAppConfigurationServiceServerInterface.cold.1
+ DNDRemoteAvailabilityServiceServerInterface.cold.1
+ DNDRemoteMonitorServerInterface.cold.1
+ DNDRemoteServiceServerInterface.cold.1
+ __26+[DNDDevice currentDevice]_block_invoke.cold.1
CStrings:
+ "[%{public}@] Got current state, state=%{private}@"
- "[%{public}@] Got current state, state=%{public}@"

```
