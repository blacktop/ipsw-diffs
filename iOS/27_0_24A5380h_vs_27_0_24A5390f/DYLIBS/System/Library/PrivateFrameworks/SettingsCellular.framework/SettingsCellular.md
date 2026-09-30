## SettingsCellular

> `/System/Library/PrivateFrameworks/SettingsCellular.framework/SettingsCellular`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA_DIRTY.__objc_data`

```diff

-746.0.0.0.0
-  __TEXT.__text: 0xa5d8
-  __TEXT.__objc_methlist: 0xe34
+750.0.0.0.0
+  __TEXT.__text: 0xa700
+  __TEXT.__objc_methlist: 0xeac
   __TEXT.__const: 0xa8
   __TEXT.__dlopen_cstrs: 0xba
-  __TEXT.__cstring: 0x74c
+  __TEXT.__cstring: 0x76f
   __TEXT.__oslogstring: 0x9eb
   __TEXT.__gcc_except_tab: 0x1c0
-  __TEXT.__unwind_info: 0x320
+  __TEXT.__unwind_info: 0x328
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x210
-  __DATA_CONST.__objc_classlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbb0
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_selrefs: 0xbc0
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x210
-  __AUTH_CONST.__const: 0x100
+  __DATA_CONST.__got: 0x220
+  __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x640
-  __AUTH_CONST.__objc_const: 0x1410
+  __AUTH_CONST.__objc_const: 0x1638
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0x308
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x68
+  __DATA.__data: 0x368
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_ivar: 0x34
   __DATA_DIRTY.__objc_data: 0x3c0
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 244
-  Symbols:   856
-  CStrings:  147
+  Functions: 250
+  Symbols:   886
+  CStrings:  149
 
Symbols:
+ +[SettingsCellularFeatureFlagManager sharedManager]
+ -[SettingsCellularFeatureFlagManager .cxx_destruct]
+ -[SettingsCellularFeatureFlagManager init]
+ -[SettingsCellularFeatureFlagManager isEnabled:]
+ -[SettingsCellularLiveFeatureFlagProvider isEnabled:]
+ _OBJC_CLASS_$_SettingsCellularFeatureFlagManager
+ _OBJC_CLASS_$_SettingsCellularLiveFeatureFlagProvider
+ _OBJC_IVAR_$_SettingsCellularFeatureFlagManager._liveProvider
+ _OBJC_METACLASS_$_SettingsCellularFeatureFlagManager
+ _OBJC_METACLASS_$_SettingsCellularLiveFeatureFlagProvider
+ __OBJC_$_CLASS_METHODS_SettingsCellularFeatureFlagManager
+ __OBJC_$_INSTANCE_METHODS_SettingsCellularFeatureFlagManager
+ __OBJC_$_INSTANCE_METHODS_SettingsCellularLiveFeatureFlagProvider
+ __OBJC_$_INSTANCE_VARIABLES_SettingsCellularFeatureFlagManager
+ __OBJC_$_PROP_LIST_SettingsCellularFeatureFlagManager
+ __OBJC_$_PROP_LIST_SettingsCellularLiveFeatureFlagProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SettingsCellularFeatureFlagProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SettingsCellularFeatureFlagProviding
+ __OBJC_$_PROTOCOL_REFS_SettingsCellularFeatureFlagProviding
+ __OBJC_CLASS_PROTOCOLS_$_SettingsCellularFeatureFlagManager
+ __OBJC_CLASS_PROTOCOLS_$_SettingsCellularLiveFeatureFlagProvider
+ __OBJC_CLASS_RO_$_SettingsCellularFeatureFlagManager
+ __OBJC_CLASS_RO_$_SettingsCellularLiveFeatureFlagProvider
+ __OBJC_LABEL_PROTOCOL_$_SettingsCellularFeatureFlagProviding
+ __OBJC_METACLASS_RO_$_SettingsCellularFeatureFlagManager
+ __OBJC_METACLASS_RO_$_SettingsCellularLiveFeatureFlagProvider
+ __OBJC_PROTOCOL_$_SettingsCellularFeatureFlagProviding
+ ___51+[SettingsCellularFeatureFlagManager sharedManager]_block_invoke
+ __os_feature_enabled_impl
+ _objc_msgSend$isEnabled:
CStrings:
+ "CarrierAppInSettings"
+ "CoreTelephony"
```
