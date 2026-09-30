## GameControllerSettings

> `/System/Library/PrivateFrameworks/GameControllerSettings.framework/Versions/A/GameControllerSettings`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0xb31c
+12.4.12.0.0
+  __TEXT.__text: 0xb450
   __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__objc_methlist: 0xe28
+  __TEXT.__objc_methlist: 0x1264
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0xaab
   __TEXT.__oslogstring: 0xd7
-  __TEXT.__unwind_info: 0x308
+  __TEXT.__unwind_info: 0x320
   __TEXT.__objc_classname: 0x231
-  __TEXT.__objc_methname: 0x225b
+  __TEXT.__objc_methname: 0x223c
   __TEXT.__objc_methtype: 0x659
   __TEXT.__objc_stubs: 0x1160
-  __DATA_CONST.__got: 0x28
+  __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3318
-  __DATA_CONST.__objc_selrefs: 0x6e8
+  __DATA_CONST.__objc_selrefs: 0x778
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__objc_const: 0x808
-  __AUTH_CONST.__cfstring: 0x1100
-  __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__auth_got: 0xe0
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__cfstring: 0x1100
+  __AUTH_CONST.__objc_const: 0x3378
   __AUTH.__objc_data: 0x500
   __DATA.__objc_ivar: 0x148
   __DATA.__data: 0x4e8

   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/Versions/A/GameControllerFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 31EFD4D2-3E89-3828-92CC-9BED9995D544
-  Functions: 284
-  Symbols:   872
+  UUID: F9E5E09C-8906-30E0-AB2A-434BF98EA858
+  Functions: 291
+  Symbols:   884
   CStrings:  783
 
Symbols:
+ -[GCSCopilotFusedControllersCollection _unitTest_fusePilotController:withCopilot:].cold.1
+ -[GCSCopilotFusedControllersCollection _unitTest_fusePilotController:withCopilot:].cold.2
+ -[GCSCopilotFusedControllersCollection _unitTest_unfuseCopilotFusedController:].cold.1
+ -[GCSMouseProfilesCollection observeValueForKeyPath:ofObject:change:context:].cold.1
+ -[GCSMouseProfilesCollection observeValueForKeyPath:ofObject:change:context:].cold.2
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSDate_$_GCSJSONSerializable
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSDictionary_$_GameControllerSettings
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDate_$_GCSJSONSerializable
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_GameControllerSettings
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_GCS
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSUUID_$_GCSJSONSerializable
+ __OBJC_$_PROP_LIST_NSArray_$_GCSJSONObject
+ __OBJC_$_PROP_LIST_NSDate_$_GCSJSONSerializable
+ __OBJC_$_PROP_LIST_NSNull_$_GCSJSONObject
+ __OBJC_$_PROP_LIST_NSNumber_$_GCSJSONObject
+ __OBJC_$_PROP_LIST_NSUUID_$_GCSJSONSerializable
+ __OBJC_CATEGORY_PROTOCOLS_$_NSArray_$_GCSJSONObject
+ __OBJC_CATEGORY_PROTOCOLS_$_NSDate_$_GCSJSONSerializable
+ __OBJC_CATEGORY_PROTOCOLS_$_NSNull_$_GCSJSONObject
+ __OBJC_CATEGORY_PROTOCOLS_$_NSNumber_$_GCSJSONObject
+ __OBJC_CATEGORY_PROTOCOLS_$_NSUUID_$_GCSJSONSerializable
+ __OBJC_CLASS_PROTOCOLS_$_NSString(GCS|GCSJSONObject)
+ gcs_isInternalBuild.cold.1
+ getGCSLogger.cold.1
- __OBJC_$_CLASS_METHODS_NSDate(GCSJSONSerializable)
- __OBJC_$_CLASS_METHODS_NSDictionary(GameControllerSettings|GCSJSONObject)
- __OBJC_$_INSTANCE_METHODS_NSDate(GCSJSONSerializable)
- __OBJC_$_INSTANCE_METHODS_NSDictionary(GameControllerSettings|GCSJSONObject)
- __OBJC_$_INSTANCE_METHODS_NSString(GCS|GCSJSONObject)
- __OBJC_$_INSTANCE_METHODS_NSUUID(GCSJSONSerializable)
- __OBJC_CLASS_PROTOCOLS_$_NSArray(GCSJSONObject)
- __OBJC_CLASS_PROTOCOLS_$_NSDate(GCSJSONSerializable)
- __OBJC_CLASS_PROTOCOLS_$_NSNull(GCSJSONObject)
- __OBJC_CLASS_PROTOCOLS_$_NSNumber(GCSJSONObject)
- __OBJC_CLASS_PROTOCOLS_$_NSString(GCSJSONObject)
- __OBJC_CLASS_PROTOCOLS_$_NSUUID(GCSJSONSerializable)
Functions:
~ -[NSUUID(GCSJSONSerializable) initWithJSONObject:] : 132 -> 136
~ -[GCSGamesCollection initWithSettingsStore:userDefaults:] : 416 -> 412
~ -[GCSGamesCollection updateGames:] : 908 -> 892
~ -[GCSGamesCollection dealloc] : 196 -> 192
~ _gcs_isInternalBuild : 68 -> 56
~ _getGCSLogger : 84 -> 68
~ -[GCSDirectionPadMapping isCustomized] : 132 -> 128
~ -[GCSCopilotFusedControllersCollection initWithSettingsStore:userDefaults:] : 292 -> 288
~ -[GCSCopilotFusedControllersCollection dealloc] : 196 -> 192
~ -[GCSCopilotFusedControllersCollection _unitTest_fusePilotController:withCopilot:] : 492 -> 388
~ -[GCSCopilotFusedControllersCollection _unitTest_unfuseCopilotFusedController:] : 240 -> 188
~ -[GCSController initWithName:persistentIdentifier:productCategoryKey:hidden:shareButton:buttons:dpads:logoSfSymbolsName:supportsHaptics:supportsLight:baseProfile:miscellaneous:] : 508 -> 504
~ -[GCSProfile initWithUUID:name:persistentControllerIdentifier:gameBundleIdentifier:baseProfile:customizable:sfSymbolsName:elementMappings:hapticFeedbackOverride:hapticStrength:doublePressShareGesture:longPressShareGesture:lightbarOverride:lightbarCustomColorEnabled:lightbarColor:] : 492 -> 472
~ -[GCSControllersCollection initWithSettingsStore:userDefaults:] : 292 -> 288
~ -[GCSControllersCollection dealloc] : 196 -> 192
~ -[NSDate(GCSJSONSerializable) initWithJSONObject:] : 228 -> 232
~ -[GCSProfilesCollection initWithSettingsStore:userDefaults:] : 416 -> 412
~ -[GCSProfilesCollection dealloc] : 196 -> 192
~ -[GCSTombstonesCollection initWithSettingsStore:userDefaults:] : 312 -> 308
~ -[GCSTombstonesCollection dealloc] : 196 -> 192
~ -[GCSMouseProfilesCollection observeValueForKeyPath:ofObject:change:context:] : 616 -> 512

```
