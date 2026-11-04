## uarpassetmanagerd

> `/usr/libexec/uarpassetmanagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1587.40.33.0.0
-  __TEXT.__text: 0x2ed88
+1587.60.11.0.0
+  __TEXT.__text: 0x2f5fc
   __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_stubs: 0x2960
-  __TEXT.__objc_methlist: 0x14dc
-  __TEXT.__cstring: 0x3129
-  __TEXT.__oslogstring: 0x19b8
-  __TEXT.__objc_methname: 0x3094
+  __TEXT.__objc_stubs: 0x29a0
+  __TEXT.__objc_methlist: 0x14fc
+  __TEXT.__cstring: 0x326f
+  __TEXT.__oslogstring: 0x1a2e
+  __TEXT.__objc_methname: 0x30eb
   __TEXT.__objc_classname: 0x341
   __TEXT.__objc_methtype: 0x897
   __TEXT.__gcc_except_tab: 0x11c
-  __TEXT.__unwind_info: 0x7b0
-  __DATA_CONST.__const: 0x2cc0
-  __DATA_CONST.__cfstring: 0x3020
+  __TEXT.__unwind_info: 0x7c0
+  __DATA_CONST.__const: 0x2ce0
+  __DATA_CONST.__cfstring: 0x30a0
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x1b0
   __DATA.__objc_const: 0x30c0
-  __DATA.__objc_selrefs: 0xc68
+  __DATA.__objc_selrefs: 0xc80
   __DATA.__objc_ivar: 0x1a0
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x480

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 508
-  Symbols:   1726
-  CStrings:  1256
+  Functions: 512
+  Symbols:   1736
+  CStrings:  1269
 
Symbols:
+ -[AUDeveloperSettingsDatabase copyAccessoryGroupForAccessory:]
+ -[AUDeveloperSettingsDatabase isValidPallasAudience:]
+ -[AUDeveloperSettingsDatabase updateAccessory:pallasAudience:]
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceInstance-343ad870c4aff45691c6db3618621440.o
+ ___kCFBooleanTrue
+ ___os_log_helper_16_2_3_8_32_8_66_8_66
+ _kAUSettingsLocationPallasAirPodsDeveloperSeed
+ _kAUSettingsLocationPallasAirPodsPublicSeed
+ _kPallasAirPodsDeveloperSeedAudienceUUID
+ _kPallasAirPodsPublicSeedAudienceUUID
+ _objc_msgSend$copyAccessoryGroupForAccessory:
+ _objc_msgSend$isValidPallasAudience:
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceInstance-56f11a94e2f69fa8bfc6c9236f548e4d.o
- ___kCFBooleanFalse
CStrings:
+ "%s: Ignoring unsupported pallas audience %lu"
+ "%s: Updating pallas audience = %{public}@ for accessoryName = %{public}@"
+ "-[AUDeveloperSettingsDatabase copyAccessoryGroupForAccessory:]"
+ "-[AUDeveloperSettingsDatabase updateAccessory:pallasAudience:]"
+ "174c5baa-4dbf-4bae-9b71-55637b17dad2"
+ "8d1900d3-8b34-4707-893e-a6151c04ee05"
+ "AIRPODS_DEVELOPER_SEED_AUDIENCE"
+ "AIRPODS_PUBLIC_SEED_AUDIENCE"
+ "AirPods Developer Seed Audience"
+ "AirPods Public Seed Audience"
+ "RaveCSeed"
+ "copyAccessoryGroupForAccessory:"
+ "isValidPallasAudience:"
+ "updateAccessory:pallasAudience:"
- "RaveB"
```
