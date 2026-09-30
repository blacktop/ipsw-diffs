## CarPlayHalogen

> `/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen`

```diff

-950.7.1.0.0
-  __TEXT.__text: 0x72dc sha256:109bcbd1b13574aac1ad90af6b33afbb54ab38f8afe60d6786e217d5cfb3c1d4
-  __TEXT.__auth_stubs: 0x570 sha256:03eae0a69ce85d6e09fb007807d036f6b44829ba42e1786ecd86584a13768692
-  __TEXT.__const: 0x88 sha256:0efe12049bad053d6ff0e1e438dee9fae94314408693f2dba85a3dd946c21b4f
-  __TEXT.__cstring: 0x1361 sha256:73bf0207a686258d6c7b3c1db023fa6d183a05415d684148e9edef09b20eeb51
-  __TEXT.__oslogstring: 0x52 sha256:da9cab94a636ad57d11f28428ea8a9e8d0e9f44b4a919031ba0399030b389569
-  __TEXT.__unwind_info: 0x1a8 sha256:ce8eb228ec939c4b420268ebfa55b6eea0d6b63db1b67847079f435089bf0576
-  __DATA_CONST.__auth_got: 0x2b8 sha256:456be6a9b899807b3732656049644322c2c8025ec0c03020ca31f700da1d7bbd
-  __DATA_CONST.__got: 0x118 sha256:1655678a2784b647022dd768394b4868a10ec795ff4820c788999f23247fee67
-  __DATA_CONST.__const: 0x2d0 sha256:3c51686268e26140d224619fb154205571b03e7f238f06ed5ac57d7f1ece524d
-  __DATA_CONST.__cfstring: 0x60 sha256:258fd83fcb9296f3f788099cfa01739e90fb2c3535945f58470fb3b99b1b3150
-  __DATA.__data: 0xe0 sha256:2699a6a444398245881e7d6c67466de8513c68204832484250a0db3c388fa98d
-  __DATA.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
+980.58.1.11.1
+  __TEXT.__text: 0x7210 sha256:7fa2a5cb99f817e01ac7bebb49a091dec1bbde39439a5026fe4d65bee17534f3
+  __TEXT.__auth_stubs: 0x5b0 sha256:7b055b277403838c102df7cd4c167bea92fe68d166e32f551e25e0631d4492e9
+  __TEXT.__const: 0x90 sha256:32a8fc2b729494d6b14878bd8d9f6f7a73adeb85bc74c8c8ac3d4715a836ed0b
+  __TEXT.__cstring: 0x1235 sha256:22b90187ea34a3c61d63b2ca3b25449cf8c22e8546a9566f98873e1624a92fa7
+  __TEXT.__oslogstring: 0x93 sha256:1e034f8de245a2c28ab79cf2097b64437751e2deb191c0758308dbae1d18f12a
+  __TEXT.__unwind_info: 0x1a0 sha256:59f5652c731b57e006c50152427ea8e79a034c35cb093f93b3e64671fc34c3df
+  __DATA_CONST.__const: 0x2d0 sha256:fb96bbd17a2528868513fb3477983c8ef8896be48bc6f5506ffe9e21d2eeb176
+  __DATA_CONST.__cfstring: 0x60 sha256:a5cf8f01e9741854ea422bd02b7270bbe0ef7e8549c1a4df59e278cc3af8c8c5
+  __DATA_CONST.__auth_got: 0x2d8 sha256:c14db2ffeda92ddcf1928449341c732cc2c0f60272edfc5177686f36be5f8ab2
+  __DATA_CONST.__got: 0x118 sha256:c125c17ef11e64c15ab2f75f7629bb4a7fc183c4351282d41f9d4f85a863b2a4
+  __DATA.__data: 0xe0 sha256:3d6f5f21f07b9414db48154e9f6430696a0f0da525579964b12285fb70696ca8
   __DATA.__bss: 0x8c sha256:24045c10c12a89f4c11e3b88ea34558fcdf926a8c1008cd08cc33bc71407c774
+  __DATA.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: 8B7EBD42-136B-3978-9A26-F9436D3EED92
+  UUID: B7F1B2C7-D229-3785-8204-9D695C0933A2
   Functions: 153
-  Symbols:   129
-  CStrings:  112
+  Symbols:   131
+  CStrings:  109
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _os_log_type_enabled
- _FigSignalErrorAtGM
- _kAPEndpointStreamCarPlayAudioControl_SpeechEvent
- _kAPEndpointStreamCarPlayAudioControl_SpeechEventKey_Event
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "APHALCarAudioStream.c"
+ "CarPlayHALPluginFactory %s: CarPlayEndpointManagerCarPlay = [%p]"
+ "Unknown config change action"
+ "kAudioHardwareIllegalOperationError"
- "%s signalled err=%d at <>:%d"
- "%s, isUnplugged=%d\n"
- "Boolean carDevice_HasProperty(FigHALAudioObjectRef, const AudioObjectPropertyAddress *)"
- "Boolean carDevice_IsPropertySettable(FigHALAudioObjectRef, const AudioObjectPropertyAddress *)"
- "UInt32 carDevice_GetPropertyDataSize(FigHALAudioObjectRef, const AudioObjectPropertyAddress *, UInt32, const void *)"
- "carDevice_GetPropertyDataSize"
- "carDevice_HasProperty"
- "carDevice_IsPropertySettable"

```
