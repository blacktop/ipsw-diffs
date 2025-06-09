## GameControllerSettings

> `/System/Library/PrivateFrameworks/GameControllerSettings.framework/GameControllerSettings`

```diff

-12.5.2.0.0
-  __TEXT.__text: 0xa4e4
+13.0.28.0.0
+  __TEXT.__text: 0xb2dc
   __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_methlist: 0x1264
+  __TEXT.__objc_methlist: 0x143c
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0xaab
-  __TEXT.__oslogstring: 0xd7
-  __TEXT.__unwind_info: 0x340
-  __TEXT.__objc_classname: 0x231
-  __TEXT.__objc_methname: 0x223c
-  __TEXT.__objc_methtype: 0x659
-  __TEXT.__objc_stubs: 0x1160
-  __DATA_CONST.__got: 0x100
+  __TEXT.__cstring: 0xb2c
+  __TEXT.__oslogstring: 0x109
+  __TEXT.__unwind_info: 0x388
+  __TEXT.__objc_classname: 0x28e
+  __TEXT.__objc_methname: 0x23d2
+  __TEXT.__objc_methtype: 0x6d2
+  __TEXT.__objc_stubs: 0x1180
+  __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0x70
-  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x778
+  __DATA_CONST.__objc_selrefs: 0x7b0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0x90
   __AUTH_CONST.__auth_got: 0x1b8
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x1100
-  __AUTH_CONST.__objc_const: 0x3378
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x148
-  __DATA.__data: 0x4e8
+  __AUTH_CONST.__cfstring: 0x11c0
+  __AUTH_CONST.__objc_const: 0x37f8
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x164
+  __DATA.__data: 0x548
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x280
+  __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1B7BFA28-4EBB-34A8-A02A-6A65E8A74E7D
-  Functions: 291
-  Symbols:   1200
-  CStrings:  783
+  UUID: D5128E07-BBD9-3C96-87EF-5642D4BE440F
+  Functions: 317
+  Symbols:   1290
+  CStrings:  814
 
Symbols:
+ +[GCSTouchControlsGameConfig(NSSecureCoding) archivalClasses]
+ +[GCSTouchControlsGameConfig(NSSecureCoding) supportsSecureCoding]
+ -[GCSSettingsStore hasPairedSpatialController]
+ -[GCSSettingsStore setHasPairedSpatialController:]
+ -[GCSSettingsStore touchControlsGameConfigs]
+ -[GCSTouchControlsGameConfig .cxx_destruct]
+ -[GCSTouchControlsGameConfig bundleIdentifier]
+ -[GCSTouchControlsGameConfig description]
+ -[GCSTouchControlsGameConfig id]
+ -[GCSTouchControlsGameConfig initWithBundleIdentifier:touchControlsData:]
+ -[GCSTouchControlsGameConfig modifiedDate]
+ -[GCSTouchControlsGameConfig touchControlsData]
+ -[GCSTouchControlsGameConfig(GCSJSONSerializable) initWithJSONObject:]
+ -[GCSTouchControlsGameConfig(GCSJSONSerializable) jsonObject]
+ -[GCSTouchControlsGameConfig(NSSecureCoding) encodeWithCoder:]
+ -[GCSTouchControlsGameConfig(NSSecureCoding) initWithCoder:]
+ -[GCSTouchControlsGameConfigsCollection .cxx_destruct]
+ -[GCSTouchControlsGameConfigsCollection configWithBundleIdentifier:]
+ -[GCSTouchControlsGameConfigsCollection dealloc]
+ -[GCSTouchControlsGameConfigsCollection initWithSettingsStore:userDefaults:]
+ -[GCSTouchControlsGameConfigsCollection observeValueForKeyPath:ofObject:change:context:]
+ -[GCSTouchControlsGameConfigsCollection setValues:]
+ -[GCSTouchControlsGameConfigsCollection settingsStore]
+ -[GCSTouchControlsGameConfigsCollection storeVersionIsCompatible]
+ -[GCSTouchControlsGameConfigsCollection updateTouchControlsGameConfigsCollection:]
+ -[GCSTouchControlsGameConfigsCollection values]
+ _OBJC_CLASS_$_GCSTouchControlsGameConfig
+ _OBJC_CLASS_$_GCSTouchControlsGameConfigsCollection
+ _OBJC_IVAR_$_GCSSettingsStore._touchControlsGameConfigs
+ _OBJC_IVAR_$_GCSTouchControlsGameConfig._bundleIdentifier
+ _OBJC_IVAR_$_GCSTouchControlsGameConfig._modifiedDate
+ _OBJC_IVAR_$_GCSTouchControlsGameConfig._touchControlsData
+ _OBJC_IVAR_$_GCSTouchControlsGameConfigsCollection._settingsStore
+ _OBJC_IVAR_$_GCSTouchControlsGameConfigsCollection._userDefaults
+ _OBJC_IVAR_$_GCSTouchControlsGameConfigsCollection._values
+ _OBJC_METACLASS_$_GCSTouchControlsGameConfig
+ _OBJC_METACLASS_$_GCSTouchControlsGameConfigsCollection
+ __OBJC_$_CLASS_METHODS_GCSTouchControlsGameConfig(NSSecureCoding|GCSJSONSerializable)
+ __OBJC_$_INSTANCE_METHODS_GCSTouchControlsGameConfig(NSSecureCoding|GCSJSONSerializable)
+ __OBJC_$_INSTANCE_METHODS_GCSTouchControlsGameConfigsCollection
+ __OBJC_$_INSTANCE_VARIABLES_GCSTouchControlsGameConfig
+ __OBJC_$_INSTANCE_VARIABLES_GCSTouchControlsGameConfigsCollection
+ __OBJC_$_PROP_LIST_GCSTouchControlsGameConfigs
+ __OBJC_$_PROP_LIST_GCSTouchControlsGameConfigsCollection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCSTouchControlsGameConfigs
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCSTouchControlsGameConfigs
+ __OBJC_CLASS_PROTOCOLS_$_GCSTouchControlsGameConfig(NSSecureCoding|GCSJSONSerializable)
+ __OBJC_CLASS_PROTOCOLS_$_GCSTouchControlsGameConfigsCollection
+ __OBJC_CLASS_RO_$_GCSTouchControlsGameConfig
+ __OBJC_CLASS_RO_$_GCSTouchControlsGameConfigsCollection
+ __OBJC_LABEL_PROTOCOL_$_GCSTouchControlsGameConfigs
+ __OBJC_METACLASS_RO_$_GCSTouchControlsGameConfig
+ __OBJC_METACLASS_RO_$_GCSTouchControlsGameConfigsCollection
+ __OBJC_PROTOCOL_$_GCSTouchControlsGameConfigs
+ _objc_msgSend$updateTouchControlsGameConfigsCollection:
CStrings:
+ "13.0.14"
+ "<GCSTouchControlsGameConfig %@>"
+ "@\"<GCSTouchControlsGameConfigs>\""
+ "@\"<GCSTouchControlsGameConfigs>\"16@0:8"
+ "@\"GCSTouchControlsGameConfig\"24@0:8@\"NSString\"16"
+ "GCSTouchControlsGameConfig"
+ "GCSTouchControlsGameConfigs"
+ "GCSTouchControlsGameConfigsCollection"
+ "GCSTouchControlsGameConfigsCollection.values = %@"
+ "T@\"<GCSTouchControlsGameConfigs>\",R,N"
+ "T@\"<GCSTouchControlsGameConfigs>\",R,N,V_touchControlsGameConfigs"
+ "T@\"NSDictionary\",R,C,N,V_touchControlsData"
+ "_touchControlsData"
+ "_touchControlsGameConfigs"
+ "configWithBundleIdentifier:"
+ "hasPairedSpatialController"
+ "initWithBundleIdentifier:touchControlsData:"
+ "setHasPairedSpatialController:"
+ "touchControlsData"
+ "touchControlsGameConfigs"
+ "updateTouchControlsGameConfigsCollection:"

```
