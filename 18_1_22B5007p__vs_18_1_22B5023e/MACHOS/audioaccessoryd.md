## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-20.47.3.0.0
-  __TEXT.__text: 0x197cac
+21.3.1.1.1
+  __TEXT.__text: 0x197774
   __TEXT.__auth_stubs: 0x2760
-  __TEXT.__objc_stubs: 0xdac0
-  __TEXT.__objc_methlist: 0x58b8
+  __TEXT.__objc_stubs: 0xdae0
+  __TEXT.__objc_methlist: 0x58f0
   __TEXT.__const: 0x3760
-  __TEXT.__gcc_except_tab: 0x33dc
-  __TEXT.__cstring: 0x28a03
-  __TEXT.__objc_methname: 0x13e14
+  __TEXT.__gcc_except_tab: 0x33e4
+  __TEXT.__cstring: 0x28a43
+  __TEXT.__objc_methname: 0x13eb9
   __TEXT.__objc_classname: 0x64f
-  __TEXT.__objc_methtype: 0x233b
+  __TEXT.__objc_methtype: 0x2337
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__oslogstring: 0x830a
   __TEXT.__constg_swiftt: 0x1584
   __TEXT.__swift5_typeref: 0x186e
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0x128b
-  __TEXT.__swift5_fieldmd: 0x127c
+  __TEXT.__swift5_reflstr: 0x129b
+  __TEXT.__swift5_fieldmd: 0x1288
   __TEXT.__swift5_assocty: 0x198
   __TEXT.__swift5_proto: 0x338
   __TEXT.__swift5_types: 0xe8

   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__info_plist: 0x599
-  __TEXT.__unwind_info: 0x3678
+  __TEXT.__unwind_info: 0x3680
   __TEXT.__eh_frame: 0x1ea0
   __DATA_CONST.__auth_got: 0x13c0
-  __DATA_CONST.__got: 0xac8
-  __DATA_CONST.__auth_ptr: 0x630
-  __DATA_CONST.__const: 0xa2a8
+  __DATA_CONST.__got: 0xab8
+  __DATA_CONST.__auth_ptr: 0x6c0
+  __DATA_CONST.__const: 0xa2e8
   __DATA_CONST.__cfstring: 0x67a0
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_dictobj: 0x4b0
   __DATA_CONST.__objc_intobj: 0x180
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x106d8
-  __DATA.__objc_selrefs: 0x44d8
+  __DATA.__objc_const: 0x10708
+  __DATA.__objc_selrefs: 0x44f0
   __DATA.__objc_ivar: 0xc68
   __DATA.__objc_data: 0x1bf0
-  __DATA.__data: 0x3028
+  __DATA.__data: 0x3038
   __DATA.__bss: 0x6680
-  __DATA.__common: 0x250
+  __DATA.__common: 0x258
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5562
-  Symbols:   1113
-  CStrings:  8395
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 5567
+  Symbols:   1119
+  CStrings:  8399
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _AVAudioSessionCategoryPlayback
- _AVAudioSessionModeDefault
CStrings:
+ "\x01\x16"
+ "-[AADeviceManagerDaemon _accessoryDeviceUpdateCloudRecord:config:]"
+ "-[AADeviceManagerDaemon _sendConfigOverAAController:device:completion:]"
+ "-[AADeviceManagerDaemon _sendConfigOverAAController:device:completion:]_block_invoke"
+ "-[AADeviceManagerDaemon _sendConfigOverCBController:device:completion:]_block_invoke"
+ "-[BTSmartRoutingDaemon _sendAudioCategory:withAudioCategory:]"
+ "3rd Party ringtone shall not hijack non-watch tipi device"
+ "B28@0:8@16I24"
+ "Rejected, Remote Category %!d(MISSING) > Local Category %!d(MISSING), audio streaming state %!d(MISSING)"
+ "Rejected, Remote Category %!d(MISSING) >= Local Category %!d(MISSING)"
+ "SR disabled: Other tipi device is watch; do not disconnect either device"
+ "Saved AADeviceRecord to cloud with error %!@(MISSING), record: %!@(MISSING)"
+ "Skip creating SR Wx device since headset doesn't support SR"
+ "TC,N,V_hideEarDetectionCapability"
+ "Triangle recovery: wxAddress %!@(MISSING)"
+ "[Hijackv2] Allow hijack=%!s(MISSING), Local audio category=%!u(MISSING), Remote audio category=%!u(MISSING), wx stream state=%!s(MISSING), Deny reason=%!@(MISSING)"
+ "_accessoryDeviceUpdateCloudRecord:config:"
+ "_hideEarDetectionCapability"
+ "_sendAudioCategory:withAudioCategory:"
+ "_sendCloudConfigsToDevice:"
+ "_sendConfigOverAAController:device:completion:"
+ "_sendConfigOverCBController:device:completion:"
+ "_supportsPhoneWatchTipi:"
+ "_supportsSR:andProductID:"
+ "ckTokenBaseURL"
+ "hiED"
+ "hideEarDetectionCapability"
+ "needsUpdateToDeviceCloudRecord"
+ "setHideEarDetectionCapability:"
- "\x01\x17"
- "-[AADeviceManagerDaemon _accessoryDeviceUpdateRecord:config:]"
- "-[AADeviceManagerDaemon _activateHeadGestureAudioSession]"
- "-[AADeviceManagerDaemon _deactivateHeadGestureAudioSession]"
- "-[AADeviceManagerDaemon _sendDeviceConfig:identifier:completion:]_block_invoke"
- "-[AADeviceManagerDaemon _sendDeviceConfig:identifier:completion:]_block_invoke_2"
- "-[BTSmartRoutingDaemon _sendAudioCategory:withAudioCatoegory:]"
- "@\"AVAudioSession\""
- "CBDeviceSetting sent: %!@(MISSING)"
- "Deactivating HeadGesture Audio Session"
- "HeadGesture: AudioFeedback setcategory %!@(MISSING) with error %!@(MISSING)"
- "Rejected, Remote Category %!d(MISSING) > Local Category %!d(MISSING),  audio streaming state %!d(MISSING)"
- "Saving AADeviceRecord for cloud sync %!@(MISSING)"
- "Saving AADeviceRecord returned with error %!@(MISSING), record: %!@(MISSING)"
- "Sending CBDeviceSetting: %!@(MISSING)"
- "Traingle recovery: wxAddress %!@(MISSING)"
- "[Hijackv2] Allow hijack=%!s(MISSING), Local audio category=%!u(MISSING), Remote audio cateogry=%!u(MISSING), wx stream state=%!s(MISSING), Deny reason=%!@(MISSING)"
- "_accessoryDeviceUpdateRecord:config:"
- "_activateHeadGestureAudioSession"
- "_auxAVAudioSession"
- "_deactivateHeadGestureAudioSession"
- "_sendAudioCategory:withAudioCatoegory:"
- "auxiliarySession"
- "needsUpdateToDeviceRecord"
- "setCategory:mode:options:error:"

```
