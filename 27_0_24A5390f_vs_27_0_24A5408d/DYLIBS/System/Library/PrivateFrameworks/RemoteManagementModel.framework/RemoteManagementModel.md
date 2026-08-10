## RemoteManagementModel

> `/System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-624.0.10.0.0
-  __TEXT.__text: 0x56ef4
+624.2.3.0.0
+  __TEXT.__text: 0x56f9c
   __TEXT.__objc_methlist: 0x8394
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x4b85
+  __TEXT.__cstring: 0x4b75
   __TEXT.__oslogstring: 0x5dc
-  __TEXT.__unwind_info: 0x1488
+  __TEXT.__unwind_info: 0x1480
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x880
-  __DATA_CONST.__objc_classlist: 0x540
+  __DATA_CONST.__const: 0x878
+  __DATA_CONST.__objc_classlist: 0x538
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2298
+  __DATA_CONST.__objc_selrefs: 0x22b8
   __DATA_CONST.__objc_superrefs: 0x430
-  __DATA_CONST.__objc_arraydata: 0x32f0
-  __DATA_CONST.__got: 0x610
+  __DATA_CONST.__objc_arraydata: 0x3220
+  __DATA_CONST.__got: 0x608
   __AUTH_CONST.__const: 0xa80
   __AUTH_CONST.__cfstring: 0x7540
-  __AUTH_CONST.__objc_const: 0xf068
-  __AUTH_CONST.__objc_arrayobj: 0x4fb0
-  __AUTH_CONST.__objc_intobj: 0x2a60
+  __AUTH_CONST.__objc_const: 0xf008
+  __AUTH_CONST.__objc_arrayobj: 0x4e00
+  __AUTH_CONST.__objc_intobj: 0x29d0
   __AUTH_CONST.__auth_got: 0x1f0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x8a4
+  __DATA.__objc_ivar: 0x8a8
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x1b0
-  __DATA_DIRTY.__objc_data: 0x33e0
+  __DATA_DIRTY.__objc_data: 0x3390
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2729
-  Symbols:   5907
-  CStrings:  999
+  Functions: 2730
+  Symbols:   5903
+  CStrings:  998
 
Symbols:
+ -[RMModelConfigurationSchemaDynamicSetting defaultValue]
+ -[RMModelConfigurationSchemaDynamicSetting initWithDynamicSetting:keyPath:valueType:invertBoolean:defaultValue:managedSettingScope:supportedOSOverride:parentSchema:]
+ -[RMModelPayloadBase loadArrayFromDictionary:usingKey:forKeyPath:transform:isRequired:defaultValue:error:]
+ -[RMModelPayloadBase loadData:withType:]
+ -[RMModelPayloadBase serializeData:withType:]
+ _OBJC_IVAR_$_RMModelConfigurationSchemaDynamicSetting._defaultValue
+ _objc_msgSend$defaultValue
+ _objc_msgSend$initWithDynamicSetting:keyPath:valueType:invertBoolean:defaultValue:managedSettingScope:supportedOSOverride:parentSchema:
- +[RMModelStatusManagementPushToken statusItemType]
- +[RMModelStatusManagementPushToken supportedOS]
- -[RMModelConfigurationSchemaDynamicSetting initWithDynamicSetting:keyPath:valueType:invertBoolean:managedSettingScope:supportedOSOverride:parentSchema:]
- -[RMModelStatusManagementPushToken isArrayValue]
- _OBJC_CLASS_$_RMModelStatusManagementPushToken
- _OBJC_METACLASS_$_RMModelStatusManagementPushToken
- _RMModelStatusItemManagementPushToken
- __OBJC_$_CLASS_METHODS_RMModelStatusManagementPushToken
- __OBJC_$_INSTANCE_METHODS_RMModelStatusManagementPushToken
- __OBJC_CLASS_RO_$_RMModelStatusManagementPushToken
- __OBJC_METACLASS_RO_$_RMModelStatusManagementPushToken
- _objc_msgSend$initWithDynamicSetting:keyPath:valueType:invertBoolean:managedSettingScope:supportedOSOverride:parentSchema:
CStrings:
+ "default"
- "a"
- "management.push-token"
```
