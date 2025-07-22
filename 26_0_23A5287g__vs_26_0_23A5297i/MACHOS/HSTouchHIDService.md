## HSTouchHIDService

> `/System/Library/HIDPlugins/ServicePlugins/HSTouchHIDService.plugin/HSTouchHIDService`

```diff

-9100.23.0.0.0
-  __TEXT.__text: 0xc5160
+9100.25.0.0.0
+  __TEXT.__text: 0xc6394
   __TEXT.__auth_stubs: 0x1950
-  __TEXT.__objc_stubs: 0x6080
-  __TEXT.__init_offsets: 0x1218
-  __TEXT.__objc_methlist: 0x4940
-  __TEXT.__const: 0x3ede
-  __TEXT.__gcc_except_tab: 0xd4d4
-  __TEXT.__cstring: 0x9ffb
-  __TEXT.__oslogstring: 0x3653
-  __TEXT.__objc_methname: 0x6d13
+  __TEXT.__objc_stubs: 0x61c0
+  __TEXT.__init_offsets: 0x1260
+  __TEXT.__objc_methlist: 0x49e8
+  __TEXT.__const: 0x3f1e
+  __TEXT.__gcc_except_tab: 0xd684
+  __TEXT.__cstring: 0xa181
+  __TEXT.__oslogstring: 0x3704
+  __TEXT.__objc_methname: 0x6e7a
   __TEXT.__objc_classname: 0xb7d
-  __TEXT.__objc_methtype: 0x53f2
-  __TEXT.__unwind_info: 0x4260
+  __TEXT.__objc_methtype: 0x5400
+  __TEXT.__unwind_info: 0x42a0
   __DATA_CONST.__auth_got: 0xcb8
   __DATA_CONST.__got: 0x270
   __DATA_CONST.__const: 0x1b40
-  __DATA_CONST.__cfstring: 0x6c60
+  __DATA_CONST.__cfstring: 0x6de0
   __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x298
-  __DATA_CONST.__objc_intobj: 0x5a0
+  __DATA_CONST.__objc_intobj: 0x600
   __DATA_CONST.__objc_doubleobj: 0xc0
-  __DATA_CONST.__objc_arraydata: 0x558
+  __DATA_CONST.__objc_arraydata: 0x518
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_floatobj: 0x20
-  __DATA_CONST.__objc_dictobj: 0x258
-  __DATA.__objc_const: 0x8830
-  __DATA.__objc_selrefs: 0x1d10
-  __DATA.__objc_ivar: 0x5a8
+  __DATA_CONST.__objc_dictobj: 0x230
+  __DATA.__objc_const: 0x8920
+  __DATA.__objc_selrefs: 0x1d60
+  __DATA.__objc_ivar: 0x5bc
   __DATA.__objc_data: 0x2300
-  __DATA.__data: 0x15d0
+  __DATA.__data: 0x1610
   __DATA.__bss: 0xc0
   __DATA.__common: 0x890
   - /AppleInternal/Library/Frameworks/HIDSensingInternalSupport.framework/HIDSensingInternalSupport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2FF6E253-DF7A-3F07-A47A-D8EA5549E877
-  Functions: 4658
-  Symbols:   25848
-  CStrings:  4443
+  UUID: 8CB183F3-B8F4-3038-8D72-C7229E6E2DA8
+  Functions: 4692
+  Symbols:   26062
+  CStrings:  4490
 
Symbols:
+ -[MouseSettings buttonDivision]
+ -[MouseSettings buttonMode]
+ -[MouseSettings decodeFromMap:].cold.3
+ -[MouseSettings decodeFromMap:].cold.4
+ -[MouseSettings setButtonDivision:]
+ -[MouseSettings setButtonMode:]
+ -[PointerSettings remapUserFacingValue:forKey:]
+ -[TrackpadFirmwareManager activated]
+ -[TrackpadFirmwareManager activeSettings]
+ -[TrackpadFirmwareManager configuredMouse]
+ -[TrackpadFirmwareManager handleActivateEvent:]
+ -[TrackpadFirmwareManager handlePointerSettings:]
+ -[TrackpadFirmwareManager setActivated:]
+ -[TrackpadFirmwareManager setActiveSettings:]
+ -[TrackpadFirmwareManager setConfiguredMouse:]
+ -[TrackpadFirmwareManager setMouseButtonMode:buttonDivision:]
+ GCC_except_table105
+ GCC_except_table164
+ OBJC_IVAR_$_MouseSettings._buttonDivision
+ OBJC_IVAR_$_MouseSettings._buttonMode
+ OBJC_IVAR_$_TrackpadFirmwareManager._activated
+ OBJC_IVAR_$_TrackpadFirmwareManager._activeSettings
+ OBJC_IVAR_$_TrackpadFirmwareManager._configuredMouse
+ __ZGVN6HSUtil8CoderKey7LiteralIJLc115ELc101ELc108ELc102ELc46ELc98ELc117ELc116ELc116ELc111ELc110ELc68ELc105ELc118ELc105ELc115ELc105ELc111ELc110EEE3KeyE
+ __ZGVN6HSUtil8CoderKey7LiteralIJLc115ELc101ELc108ELc102ELc46ELc98ELc117ELc116ELc116ELc111ELc110ELc77ELc111ELc100ELc101EEE3KeyE
+ __ZGVN6HSUtil8CoderKey7LiteralIJLc98ELc117ELc116ELc116ELc111ELc110ELc68ELc105ELc118ELc105ELc115ELc105ELc111ELc110EEE3KeyE
+ __ZGVN6HSUtil8CoderKey7LiteralIJLc98ELc117ELc116ELc116ELc111ELc110ELc77ELc111ELc100ELc101EEE3KeyE
+ __ZN6HSUtil8CoderKey7LiteralIJLc115ELc101ELc108ELc102ELc46ELc98ELc117ELc116ELc116ELc111ELc110ELc68ELc105ELc118ELc105ELc115ELc105ELc111ELc110EEE3KeyE
+ __ZN6HSUtil8CoderKey7LiteralIJLc115ELc101ELc108ELc102ELc46ELc98ELc117ELc116ELc116ELc111ELc110ELc68ELc105ELc118ELc105ELc115ELc105ELc111ELc110EEE4_StrE
+ __ZN6HSUtil8CoderKey7LiteralIJLc115ELc101ELc108ELc102ELc46ELc98ELc117ELc116ELc116ELc111ELc110ELc77ELc111ELc100ELc101EEE3KeyE
+ __ZN6HSUtil8CoderKey7LiteralIJLc115ELc101ELc108ELc102ELc46ELc98ELc117ELc116ELc116ELc111ELc110ELc77ELc111ELc100ELc101EEE4_StrE
+ __ZN6HSUtil8CoderKey7LiteralIJLc98ELc117ELc116ELc116ELc111ELc110ELc68ELc105ELc118ELc105ELc115ELc105ELc111ELc110EEE3KeyE
+ __ZN6HSUtil8CoderKey7LiteralIJLc98ELc117ELc116ELc116ELc111ELc110ELc68ELc105ELc118ELc105ELc115ELc105ELc111ELc110EEE4_StrE
+ __ZN6HSUtil8CoderKey7LiteralIJLc98ELc117ELc116ELc116ELc111ELc110ELc77ELc111ELc100ELc101EEE3KeyE
+ __ZN6HSUtil8CoderKey7LiteralIJLc98ELc117ELc116ELc116ELc111ELc110ELc77ELc111ELc100ELc101EEE4_StrE
+ __cxx_global_var_init.219
+ __cxx_global_var_init.220
+ __cxx_global_var_init.221
+ __cxx_global_var_init.222
+ __cxx_global_var_init.223
+ __cxx_global_var_init.224
+ __cxx_global_var_init.225
+ __cxx_global_var_init.226
+ __cxx_global_var_init.228
+ __cxx_global_var_init.229
+ __cxx_global_var_init.230
+ __cxx_global_var_init.231
+ __cxx_global_var_init.233
+ __cxx_global_var_init.234
+ __cxx_global_var_init.235
+ __cxx_global_var_init.236
+ __cxx_global_var_init.237
+ __cxx_global_var_init.238
+ __cxx_global_var_init.240
+ __cxx_global_var_init.241
+ __cxx_global_var_init.242
+ __cxx_global_var_init.243
+ __cxx_global_var_init.244
+ __cxx_global_var_init.246
+ __cxx_global_var_init.556
+ __cxx_global_var_init.557
+ __cxx_global_var_init.558
+ __cxx_global_var_init.559
+ __cxx_global_var_init.560
+ __cxx_global_var_init.561
+ __cxx_global_var_init.562
+ __cxx_global_var_init.563
+ _objc_msgSend$activeSettings
+ _objc_msgSend$buttonDivision
+ _objc_msgSend$buttonMode
+ _objc_msgSend$configuredMouse
+ _objc_msgSend$remapUserFacingValue:forKey:
+ _objc_msgSend$setActiveSettings:
+ _objc_msgSend$setButtonDivision:
+ _objc_msgSend$setButtonMode:
+ _objc_msgSend$setConfiguredMouse:
+ _objc_msgSend$setMouseButtonMode:buttonDivision:
- GCC_except_table152
- __cxx_global_var_init.177
- __cxx_global_var_init.178
- __cxx_global_var_init.179
- __cxx_global_var_init.181
- __cxx_global_var_init.182
- __cxx_global_var_init.184
- __cxx_global_var_init.185
- __cxx_global_var_init.186
- __cxx_global_var_init.187
- __cxx_global_var_init.188
- __cxx_global_var_init.189
- __cxx_global_var_init.190
- __cxx_global_var_init.191
- __cxx_global_var_init.192
- __cxx_global_var_init.193
- __cxx_global_var_init.194
- __cxx_global_var_init.195
- __cxx_global_var_init.196
- __cxx_global_var_init.198
- __cxx_global_var_init.199
- __cxx_global_var_init.200
- __cxx_global_var_init.201
- __cxx_global_var_init.202
- __cxx_global_var_init.203
- __cxx_global_var_init.204
- __cxx_global_var_init.524
- __cxx_global_var_init.525
- __cxx_global_var_init.526
- __cxx_global_var_init.527
CStrings:
+ "-[PointerSettings updatePreferenceKey:to:]"
+ "9100.25"
+ "Activated"
+ "ActiveSettings"
+ "ButtonDivision"
+ "ButtonMode"
+ "ConfiguredMouse"
+ "HIDMouseScrollAcceleration"
+ "HIDTrackpadScrollAcceleration"
+ "IOReturn HSTPipeline::FirmwareUtil::SetReport(MTDeviceRef _Nonnull, const T &) [T = HSTPipeline::FirmwareInterface::FeatureReport::MouseButtonConfig]"
+ "MouseButtonDivision"
+ "MouseButtonMode"
+ "OneButton"
+ "Successfully updated mouse button config: mode=%u division=%u (deviceID 0x%llX)"
+ "T@\"PointerSettings\",&,N,V_activeSettings"
+ "TB,N,V_configuredMouse"
+ "TC,N,V_buttonDivision"
+ "TC,N,V_buttonMode"
+ "TwoButton"
+ "TwoButtonSwapped"
+ "[HID] [MT] %s%s%s Invalid value(%{public}@) of %{public}@ was provided for preference %{public}@"
+ "_activeSettings"
+ "_buttonDivision"
+ "_buttonMode"
+ "_configuredMouse"
+ "activeSettings"
+ "buttonDivision"
+ "buttonMode"
+ "configuredMouse"
+ "i24@0:8C16C20"
+ "remapUserFacingValue:forKey:"
+ "setActiveSettings:"
+ "setButtonDivision:"
+ "setButtonMode:"
+ "setConfiguredMouse:"
+ "setMouseButtonMode:buttonDivision:"
- "9100.23"

```
