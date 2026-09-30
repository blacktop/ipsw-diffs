## HearingWidgetExtension

> `/Applications/HearingApp.app/PlugIns/HearingWidgetExtension.appex/HearingWidgetExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`

```diff

-536.0.0.0.0
-  __TEXT.__text: 0x15014
-  __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_stubs: 0x360
+539.1.0.0.0
+  __TEXT.__text: 0x15540
+  __TEXT.__auth_stubs: 0x11a0
+  __TEXT.__objc_stubs: 0x3a0
   __TEXT.__objc_methlist: 0x60c
-  __TEXT.__const: 0x1318
-  __TEXT.__constg_swiftt: 0x3e0
-  __TEXT.__swift5_typeref: 0x2dba
-  __TEXT.__swift5_reflstr: 0x236
-  __TEXT.__swift5_fieldmd: 0x220
+  __TEXT.__const: 0x1328
+  __TEXT.__constg_swiftt: 0x3e8
+  __TEXT.__swift5_typeref: 0x2ed6
+  __TEXT.__swift5_reflstr: 0x23e
+  __TEXT.__swift5_fieldmd: 0x22c
   __TEXT.__swift5_proto: 0xa0
   __TEXT.__swift5_types: 0x34
   __TEXT.__objc_classname: 0x7d
-  __TEXT.__objc_methname: 0xb4e
+  __TEXT.__objc_methname: 0xb6f
   __TEXT.__objc_methtype: 0x2a7
   __TEXT.__swift5_assocty: 0x1a0
   __TEXT.__cstring: 0x403
-  __TEXT.__swift5_capture: 0x140
-  __TEXT.__oslogstring: 0x34a
+  __TEXT.__swift5_capture: 0xf8
+  __TEXT.__oslogstring: 0x39a
   __TEXT.__swift_as_entry: 0x20
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__unwind_info: 0x4d8
   __TEXT.__eh_frame: 0x20c
-  __DATA_CONST.__const: 0x9bb
+  __DATA_CONST.__const: 0x91b
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0x8c8
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__auth_ptr: 0x590
+  __DATA_CONST.__auth_got: 0x8d8
+  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__auth_ptr: 0x598
   __DATA.__objc_const: 0x908
-  __DATA.__objc_selrefs: 0x460
-  __DATA.__objc_data: 0x130
-  __DATA.__data: 0x930
+  __DATA.__objc_selrefs: 0x470
+  __DATA.__objc_data: 0x138
+  __DATA.__data: 0x940
   __DATA.__bss: 0x1478
   __DATA.__common: 0xa0
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 416
-  Symbols:   156
-  CStrings:  260
+  Functions: 410
+  Symbols:   159
+  CStrings:  262
 
Symbols:
+ _OBJC_CLASS_$_HUHearingAidSettings
+ _objc_release_x22
+ _objc_retain_x23
+ _objc_retain_x28
- _objc_retain_x21
CStrings:
+ "HearingWidget: MuteVolumeIntent — hearing aid not reachable"
+ "HearingWidget: MuteVolumeIntent — toggling microphone mute to %{bool}d"
+ "HearingWidget: fast path — device '%s' already loaded"
+ "HearingWidget: makeEntry — device '%s' hasConnection=%{bool}d reachable=%{bool}d"
+ "T@\"AXHearingAidMode\",R,&"
+ "T@\"NSNumber\",R"
+ "hearingAidMicrophoneMuted"
+ "setHearingAidMicrophoneMuted:"
- "HearingWidget: MuteVolumeIntent — muting all volumes"
- "HearingWidget: MuteVolumeIntent — no device available"
- "HearingWidget: buildAndResolve — device '%s' hasConnection=%{bool}d reachable=%{bool}d"
- "T@\"AXHearingAidMode\",R,&,N"
- "T@\"NSNumber\",R,N"
- "T@\"NSString\",R,&,N"
```
