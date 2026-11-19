## gamepolicyd

> `/usr/libexec/gamepolicyd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__info_plist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-4.0.8.0.0
-  __TEXT.__text: 0x6d584
-  __TEXT.__auth_stubs: 0x27c0
+4.1.2.0.0
+  __TEXT.__text: 0x6e4e8
+  __TEXT.__auth_stubs: 0x27d0
   __TEXT.__objc_stubs: 0x1320
-  __TEXT.__objc_methlist: 0xc00
-  __TEXT.__const: 0x2010
+  __TEXT.__objc_methlist: 0xc18
+  __TEXT.__const: 0x2020
   __TEXT.__cstring: 0x15c8
-  __TEXT.__objc_methname: 0x2e3d
-  __TEXT.__oslogstring: 0x1e6b
+  __TEXT.__objc_methname: 0x2e8d
+  __TEXT.__oslogstring: 0x1efb
   __TEXT.__objc_classname: 0x92c
-  __TEXT.__objc_methtype: 0xa43
+  __TEXT.__objc_methtype: 0xa93
   __TEXT.__gcc_except_tab: 0x58
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x2028
-  __TEXT.__swift5_typeref: 0x10ba
+  __TEXT.__constg_swiftt: 0x2040
+  __TEXT.__swift5_typeref: 0x10c4
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x1660
-  __TEXT.__swift5_fieldmd: 0x1190
+  __TEXT.__swift5_reflstr: 0x1680
+  __TEXT.__swift5_fieldmd: 0x119c
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_proto: 0xe4
   __TEXT.__swift5_types: 0xd0

   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0xc
   __TEXT.__info_plist: 0x4d6
-  __TEXT.__unwind_info: 0x1398
-  __TEXT.__eh_frame: 0x7f0
+  __TEXT.__unwind_info: 0x13c8
+  __TEXT.__eh_frame: 0x848
   __DATA_CONST.__const: 0x26f0
   __DATA_CONST.__cfstring: 0x100
   __DATA_CONST.__objc_classlist: 0x100

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__auth_got: 0x13f0
-  __DATA_CONST.__got: 0x4f8
+  __DATA_CONST.__auth_got: 0x13f8
+  __DATA_CONST.__got: 0x4f0
   __DATA_CONST.__auth_ptr: 0x478
-  __DATA.__objc_const: 0x34e0
-  __DATA.__objc_selrefs: 0x7e8
+  __DATA.__objc_const: 0x3510
+  __DATA.__objc_selrefs: 0x7f0
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0xba0
-  __DATA.__data: 0x3810
+  __DATA.__data: 0x3830
   __DATA.__bss: 0x15e0
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1517
+  Functions: 1525
   Symbols:   881
-  CStrings:  864
+  CStrings:  870
 
Symbols:
+ _$ss10__CocoaSetV8containsySbyXlF
- _OBJC_CLASS_$_GPGameCenterMediator
CStrings:
+ "Daemon forwarding gameDidBecomeForeground bundleID=%{public}s uid=%{public}u"
+ "No user agent to forward gameDidBecomeForeground for %{public}s"
+ "gameDidBecomeForegroundWithBundleID:auditToken:"
+ "notifiedForegroundGames"
+ "setCLPCTrialID:error:"
+ "v32@0:8@\"NSString\"16@\"NSValue\"24"
+ "v32@0:8@16@24"
- "gameDidBecomeForeground:auditToken:"
```
