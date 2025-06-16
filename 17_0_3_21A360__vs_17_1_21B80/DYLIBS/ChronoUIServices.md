## ChronoUIServices

> `/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices`

```diff

-401.1.107.0.0
-  __TEXT.__text: 0x1f604
+401.12.100.0.0
+  __TEXT.__text: 0x1f6f8
   __TEXT.__auth_stubs: 0xa20
-  __TEXT.__objc_methlist: 0x1998
+  __TEXT.__objc_methlist: 0x19b0
   __TEXT.__const: 0x54c
-  __TEXT.__gcc_except_tab: 0x2a6c
-  __TEXT.__cstring: 0x142e
-  __TEXT.__oslogstring: 0x1503
+  __TEXT.__gcc_except_tab: 0x2a78
+  __TEXT.__cstring: 0x147e
+  __TEXT.__oslogstring: 0x14ff
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__swift5_typeref: 0x1f2
   __TEXT.__swift5_fieldmd: 0x240

   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0x24
-  __TEXT.__unwind_info: 0x142c
-  __TEXT.__objc_classname: 0x6f2
-  __TEXT.__objc_methname: 0x5055
-  __TEXT.__objc_methtype: 0xba8
-  __TEXT.__objc_stubs: 0x3880
-  __DATA_CONST.__got: 0x100
+  __TEXT.__unwind_info: 0x1434
+  __TEXT.__objc_classname: 0x6f1
+  __TEXT.__objc_methname: 0x5187
+  __TEXT.__objc_methtype: 0xbbb
+  __TEXT.__objc_stubs: 0x3940
+  __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0x8e8
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4420
-  __DATA_CONST.__objc_selrefs: 0x1228
+  __DATA_CONST.__objc_const: 0x4450
+  __DATA_CONST.__objc_selrefs: 0x1260
+  __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__objc_const: 0xce8
-  __AUTH_CONST.__cfstring: 0x1360
+  __AUTH_CONST.__cfstring: 0x13a0
   __AUTH_CONST.__const: 0x638
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x520
   __AUTH.__objc_data: 0x5a0
   __AUTH.__data: 0x140
   __DATA.__objc_classrefs: 0x2d0
   __DATA.__objc_superrefs: 0xd8
-  __DATA.__objc_ivar: 0x1a8
+  __DATA.__objc_ivar: 0x1ac
   __DATA.__data: 0x5b8
-  __DATA.__bss: 0x510
+  __DATA.__bss: 0x520
   __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__data: 0x138
-  __DATA_DIRTY.__bss: 0x120
+  __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 291DBC2B-25DA-3A4E-A5B2-73685794797C
-  Functions: 1056
-  Symbols:   2971
-  CStrings:  1491
+  UUID: 4B501432-369B-3DD7-ADC3-0A9C65C0162D
+  Functions: 1060
+  Symbols:   2991
+  CStrings:  1505
 
Symbols:
+ -[CHUISPreferences observeValueForKeyPath:ofObject:change:context:]
+ -[CHUISPreferences userWantsWidgetDataWhenPasscodeLocked]
+ -[CHUISWidgetHostViewController extensionsDidChangeForExtensionProvider:]
+ -[CHUISWidgetHostViewController initWithWidget:metrics:widgetConfigurationIdentifier:extensionProvider:sceneWorkspace:screenshotManager:preferences:keybag:]
+ -[CHUISWidgetHostViewController initWithWidget:metrics:widgetConfigurationIdentifier:extensionProvider:sceneWorkspace:screenshotManager:preferences:keybag:].cold.1
+ _CHUISSharedExtensionProvider.__instance
+ _CHUISSharedExtensionProvider.__once
+ _NSKeyValueChangeKindKey
+ _NSKeyValueChangeNewKey
+ _OBJC_CLASS_$_CHSWidgetExtensionProvider
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_IVAR_$_CHUISPreferences._userWantsWidgetDataWhenPasscodeLocked
+ _OBJC_IVAR_$_CHUISWidgetHostViewController._extensionProvider
+ _OUTLINED_FUNCTION_10
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CHSWidgetExtensionProviderObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CHSWidgetExtensionProviderObserver
+ __OBJC_$_PROTOCOL_REFS_CHSWidgetExtensionProviderObserver
+ __OBJC_LABEL_PROTOCOL_$_CHSWidgetExtensionProviderObserver
+ __OBJC_PROTOCOL_$_CHSWidgetExtensionProviderObserver
+ ___156-[CHUISWidgetHostViewController initWithWidget:metrics:widgetConfigurationIdentifier:extensionProvider:sceneWorkspace:screenshotManager:preferences:keybag:]_block_invoke
+ ___73-[CHUISWidgetHostViewController extensionsDidChangeForExtensionProvider:]_block_invoke
+ ___73-[CHUISWidgetHostViewController extensionsDidChangeForExtensionProvider:]_block_invoke.cold.1
+ ___CHUISSharedExtensionProvider_block_invoke
+ __unnamed_array_storage
+ __unnamed_array_storage.28
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$initWithWidget:metrics:widgetConfigurationIdentifier:extensionProvider:sceneWorkspace:screenshotManager:preferences:keybag:
+ _objc_msgSend$intValue
+ _objc_msgSend$registerDefaults:
+ _objc_msgSend$registerObserver:
+ _objc_msgSend$setUserWantsWidgetDataWhenPasscodeLocked:
+ _objc_msgSend$unregisterObserver:
+ _objc_msgSend$userWantsWidgetDataWhenPasscodeLocked
+ _objc_msgSend$widgetDescriptorForWidget:
- -[CHUISWidgetHostViewController descriptorsDidChangeForDescriptorProvider:]
- -[CHUISWidgetHostViewController initWithWidget:metrics:widgetConfigurationIdentifier:descriptorProvider:sceneWorkspace:screenshotManager:preferences:keybag:]
- -[CHUISWidgetHostViewController initWithWidget:metrics:widgetConfigurationIdentifier:descriptorProvider:sceneWorkspace:screenshotManager:preferences:keybag:].cold.1
- GCC_except_table142
- _CHUISSharedDescriptorProvider.__instance
- _CHUISSharedDescriptorProvider.__once
- _OBJC_CLASS_$_CHSWidgetDescriptorProvider
- _OBJC_IVAR_$_CHUISWidgetHostViewController._descriptorProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CHSWidgetDescriptorProviderObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_CHSWidgetDescriptorProviderObserver
- __OBJC_$_PROTOCOL_REFS_CHSWidgetDescriptorProviderObserver
- __OBJC_LABEL_PROTOCOL_$_CHSWidgetDescriptorProviderObserver
- __OBJC_PROTOCOL_$_CHSWidgetDescriptorProviderObserver
- ___157-[CHUISWidgetHostViewController initWithWidget:metrics:widgetConfigurationIdentifier:descriptorProvider:sceneWorkspace:screenshotManager:preferences:keybag:]_block_invoke
- ___75-[CHUISWidgetHostViewController descriptorsDidChangeForDescriptorProvider:]_block_invoke
- ___CHUISSharedDescriptorProvider_block_invoke
- _objc_msgSend$descriptorForPersonality:
- _objc_msgSend$descriptors
- _objc_msgSend$initWithWidget:metrics:widgetConfigurationIdentifier:descriptorProvider:sceneWorkspace:screenshotManager:preferences:keybag:
CStrings:
+ "@\"CHSWidgetExtensionProvider\""
+ "CHSWidgetExtensionProviderObserver"
+ "TB,R,N,V_userWantsWidgetDataWhenPasscodeLocked"
+ "[%p-%{public}@] Descriptors did change"
+ "[%p-%{public}@] No descriptor found for widget: %{public}@"
+ "[%p-%{public}@] No snapshot image found or couldn't be opened (data protection)."
+ "_extensionProvider"
+ "_userWantsWidgetDataWhenPasscodeLocked"
+ "addObserver:forKeyPath:options:context:"
+ "extensionsDidChangeForExtensionProvider:"
+ "initWithWidget:metrics:widgetConfigurationIdentifier:extensionProvider:sceneWorkspace:screenshotManager:preferences:keybag:"
+ "intValue"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "registerDefaults:"
+ "registerObserver:"
+ "setUserWantsWidgetDataWhenPasscodeLocked:"
+ "showComplicationDataWhenPasscodeLocked"
+ "unregisterObserver:"
+ "userWantsWidgetDataWhenPasscodeLocked"
+ "v24@0:8@\"CHSWidgetExtensionProvider\"16"
+ "v48@0:8@16@24@32^v40"
+ "widgetDescriptorForWidget:"
- "@\"CHSWidgetDescriptorProvider\""
- "CHSWidgetDescriptorProviderObserver"
- "[%p-%{public}@] Descriptors did change (%lu available)"
- "[%p-%{public}@] No descriptor found for widget: %{public}@ (%lu descriptors available)"
- "[%p-%{public}@] No snapshot image found."
- "_descriptorProvider"
- "descriptorForPersonality:"
- "descriptors"
- "descriptorsDidChangeForDescriptorProvider:"
- "initWithWidget:metrics:widgetConfigurationIdentifier:descriptorProvider:sceneWorkspace:screenshotManager:preferences:keybag:"
- "v24@0:8@\"CHSWidgetDescriptorProvider\"16"

```
