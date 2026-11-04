## AUSettings

> `/System/Library/PrivateFrameworks/AUSettings.framework/AUSettings`

```diff

-1587.40.33.0.0
-  __TEXT.__text: 0x5d70
-  __TEXT.__objc_methlist: 0x70c
+1587.60.11.0.0
+  __TEXT.__text: 0x6188
+  __TEXT.__objc_methlist: 0x72c
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0xe0f
-  __TEXT.__oslogstring: 0x1ec
+  __TEXT.__cstring: 0xf09
+  __TEXT.__oslogstring: 0x262
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x268
+  __TEXT.__unwind_info: 0x270
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x588
+  __DATA_CONST.__const: 0x5a8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x568
+  __DATA_CONST.__objc_selrefs: 0x580
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__got: 0xb8
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0xfa0
+  __AUTH_CONST.__cfstring: 0xfe0
   __AUTH_CONST.__objc_const: 0xdc8
+  __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8c

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 161
-  Symbols:   467
-  CStrings:  174
+  Functions: 166
+  Symbols:   474
+  CStrings:  183
 
Symbols:
+ -[AUDeveloperSettingsDatabase copyAccessoryGroupForAccessory:]
+ -[AUDeveloperSettingsDatabase isValidPallasAudience:]
+ -[AUDeveloperSettingsDatabase updateAccessory:pallasAudience:]
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OUTLINED_FUNCTION_3
+ ___kCFBooleanTrue
+ _kAUSettingsLocationPallasAirPodsDeveloperSeed
+ _kAUSettingsLocationPallasAirPodsPublicSeed
- ___kCFBooleanFalse
CStrings:
+ "%s: Ignoring unsupported pallas audience %lu"
+ "%s: Updating pallas audience = %{public}@ for accessoryName = %{public}@"
+ "-[AUDeveloperSettingsDatabase copyAccessoryGroupForAccessory:]"
+ "-[AUDeveloperSettingsDatabase updateAccessory:pallasAudience:]"
+ "AIRPODS_DEVELOPER_SEED_AUDIENCE"
+ "AIRPODS_PUBLIC_SEED_AUDIENCE"
+ "AirPods Developer Seed Audience"
+ "AirPods Public Seed Audience"
+ "Q"
```
