## BackBoard

> `/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard`

```diff

-3005.4.2.0.0
-  __TEXT.__text: 0x23034
+3005.4.3.5.0
+  __TEXT.__text: 0x2329c
   __TEXT.__auth_stubs: 0x1650
-  __TEXT.__objc_methlist: 0x1fd4
+  __TEXT.__objc_methlist: 0x200c
   __TEXT.__const: 0x2ba
   __TEXT.__gcc_except_tab: 0x608
-  __TEXT.__cstring: 0x2398
-  __TEXT.__oslogstring: 0x1be5
+  __TEXT.__cstring: 0x2378
+  __TEXT.__oslogstring: 0x1ca5
   __TEXT.__dlopen_cstrs: 0x2d9
   __TEXT.__constg_swiftt: 0x1fc
   __TEXT.__swift5_typeref: 0xb0

   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__unwind_info: 0xb88
+  __TEXT.__unwind_info: 0xb98
   __TEXT.__objc_classname: 0x46a
-  __TEXT.__objc_methname: 0x61ff
-  __TEXT.__objc_methtype: 0xa8b
-  __TEXT.__objc_stubs: 0x55c0
-  __DATA_CONST.__got: 0x630
+  __TEXT.__objc_methname: 0x62ce
+  __TEXT.__objc_methtype: 0xa88
+  __TEXT.__objc_stubs: 0x5620
+  __DATA_CONST.__got: 0x638
   __DATA_CONST.__const: 0x8f8
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a68
+  __DATA_CONST.__objc_selrefs: 0x1a80
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0xb38
-  __AUTH_CONST.__const: 0xd10
-  __AUTH_CONST.__cfstring: 0x1c20
-  __AUTH_CONST.__objc_const: 0x2b50
-  __AUTH_CONST.__objc_intobj: 0x1e0
+  __AUTH_CONST.__const: 0xd30
+  __AUTH_CONST.__cfstring: 0x1c00
+  __AUTH_CONST.__objc_const: 0x2be8
+  __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x220
-  __DATA.__objc_ivar: 0x138
+  __DATA.__objc_ivar: 0x13c
   __DATA.__data: 0x3b0
   __DATA.__bss: 0x280
   __DATA_DIRTY.__objc_data: 0xbb8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7B9C7E5C-F317-3C12-8EBE-0C6AA629A505
-  Functions: 959
-  Symbols:   3712
-  CStrings:  1810
+  UUID: 000FFD54-94AB-3637-8B85-BEBC315E9CFD
+  Functions: 965
+  Symbols:   3733
+  CStrings:  1816
 
Symbols:
+ -[AXBDisplayWakeManager _showAccessibilityHelpBannerForVoiceOver:switchControl:touchAccommodations:]
+ -[AXBDisplayWakeManager _showAccessibilityHelpBannerForVoiceOver:switchControl:touchAccommodations:].cold.1
+ -[AXBLiveCaptionsManager dealloc]
+ -[AXBLiveCaptionsManager init]
+ -[AXBLiveCaptionsManager isManagedConfigurationOverridingLiveCaptions]
+ -[AXBLiveCaptionsManager profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:]
+ -[AXBLiveCaptionsManager setIsManagedConfigurationOverridingLiveCaptions:]
+ GCC_except_table10
+ _MCFeatureAccessibilityLiveCaptionsAllowed
+ _OBJC_IVAR_$_AXBLiveCaptionsManager._isManagedConfigurationOverridingLiveCaptions
+ __OBJC_$_INSTANCE_VARIABLES_AXBLiveCaptionsManager
+ __OBJC_$_PROP_LIST_AXBLiveCaptionsManager
+ __OBJC_CLASS_PROTOCOLS_$_AXBLiveCaptionsManager
+ ___100-[AXBDisplayWakeManager _showAccessibilityHelpBannerForVoiceOver:switchControl:touchAccommodations:]_block_invoke
+ ___43+[AXBLiveCaptionsManager initializeMonitor]_block_invoke_4
+ _objc_msgSend$_showAccessibilityHelpBannerForVoiceOver:switchControl:touchAccommodations:
+ _objc_msgSend$isManagedConfigurationOverridingLiveCaptions
+ _objc_msgSend$setIsManagedConfigurationOverridingLiveCaptions:
+ _objc_msgSend$unregisterObserver:
- -[AXBDisplayWakeManager _showAccessibilityHelpBannerForVoiceOver:switchControl:zoom:touchAccommodations:]
- -[AXBDisplayWakeManager _showAccessibilityHelpBannerForVoiceOver:switchControl:zoom:touchAccommodations:].cold.1
- ___105-[AXBDisplayWakeManager _showAccessibilityHelpBannerForVoiceOver:switchControl:zoom:touchAccommodations:]_block_invoke
- _objc_msgSend$_showAccessibilityHelpBannerForVoiceOver:switchControl:zoom:touchAccommodations:
CStrings:
+ "Display wake: VoiceOver=%{BOOL}d, SwitchControl=%{BOOL}d, TouchAccommodations=%{BOOL}d"
+ "Managed Configuration is requesting Live Captions to be turned off"
+ "Managed configuration overriding Live Captions, disabling feature"
+ "Managed configuration settings changed, Live Captions allowed: %@"
+ "TB,N,V_isManagedConfigurationOverridingLiveCaptions"
+ "_isManagedConfigurationOverridingLiveCaptions"
+ "_showAccessibilityHelpBannerForVoiceOver:switchControl:touchAccommodations:"
+ "isManagedConfigurationOverridingLiveCaptions"
+ "setIsManagedConfigurationOverridingLiveCaptions:"
+ "unregisterObserver:"
+ "v28@0:8B16B20B24"
- "Display wake: VoiceOver=%{BOOL}d, SwitchControl=%{BOOL}d, Zoom=%{BOOL}d, TouchAccommodations=%{BOOL}d"
- "_showAccessibilityHelpBannerForVoiceOver:switchControl:zoom:touchAccommodations:"
- "v32@0:8B16B20B24B28"
- "zoom.banner.title"

```
