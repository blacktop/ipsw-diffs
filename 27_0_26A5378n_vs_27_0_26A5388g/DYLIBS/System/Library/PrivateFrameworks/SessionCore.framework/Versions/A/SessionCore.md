## SessionCore

> `/System/Library/PrivateFrameworks/SessionCore.framework/Versions/A/SessionCore`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-310.0.0.0.0
-  __TEXT.__text: 0x14c314
+311.0.0.0.0
+  __TEXT.__text: 0x14f578
   __TEXT.__objc_methlist: 0xd44
-  __TEXT.__const: 0x5402
-  __TEXT.__swift5_typeref: 0x2cf7
+  __TEXT.__const: 0x5412
+  __TEXT.__swift5_typeref: 0x2d1b
   __TEXT.__swift5_fieldmd: 0x2c64
   __TEXT.__constg_swiftt: 0x4574
   __TEXT.__swift5_reflstr: 0x2c77
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__cstring: 0x35b2
-  __TEXT.__oslogstring: 0x75f4
+  __TEXT.__oslogstring: 0x7834
   __TEXT.__swift5_capture: 0x1490
   __TEXT.__swift5_protos: 0xc8
   __TEXT.__swift5_proto: 0x35c

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0x2428
+  __TEXT.__unwind_info: 0x2438
   __TEXT.__eh_frame: 0x3658
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__auth_got: 0x1bd8
   __AUTH.__objc_data: 0x740
   __AUTH.__data: 0x2e8
-  __DATA.__data: 0x18c0
+  __DATA.__data: 0x1790
   __DATA.__common: 0x68
-  __DATA.__bss: 0x2380
+  __DATA.__bss: 0x2080
   __DATA_DIRTY.__objc_data: 0x1988
-  __DATA_DIRTY.__data: 0x6f40
-  __DATA_DIRTY.__bss: 0xb80
+  __DATA_DIRTY.__data: 0x7070
+  __DATA_DIRTY.__bss: 0xe80
   __DATA_DIRTY.__common: 0x269
   - /System/Library/Frameworks/ActivityKit.framework/Versions/A/ActivityKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3485
-  Symbols:   1802
-  CStrings:  828
+  Functions: 3491
+  Symbols:   1804
+  CStrings:  835
 
Symbols:
+ _symbolic SS3key______5valuet 11SessionCore24ActivityParticipantEventV
+ _symbolic _____ySS_____G s18_DictionaryStorageC 11SessionCore24ActivityParticipantEventV
CStrings:
+ "Activity request blocked by alert scene target without user consent: %{private}s"
+ "Activity request blocked by content source without user consent: %{private}s"
+ "Activity request blocked by scene target without user consent: %{private}s"
+ "Alert scene target does not have user consent to request activities %{public}s"
+ "Alert scene target does not include NSSupportsLiveActivities key in its Info.plist %{public}s"
+ "Alert scene target has too many activities"
+ "Alert scene target is restricted: %{private}s"
+ "Ending activity %{public}s because authorization was revoked for %{public}s"
+ "Scene target does not have user consent to request activities %{public}s"
+ "Scene target does not include NSSupportsLiveActivities key in its Info.plist %{public}s"
+ "Scene target has too many activities"
- "Ending activity because authorization was revoked: %{public}s"
- "No scene target has user consent to request activities"
- "Target does not have user consent to request activities %{public}s"
- "User consent granted by scene target %{public}s"
```
