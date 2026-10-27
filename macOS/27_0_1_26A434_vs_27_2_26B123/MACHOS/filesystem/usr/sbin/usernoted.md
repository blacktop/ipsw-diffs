## usernoted

> `/usr/sbin/usernoted`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-1674.0.7.0.400
-  __TEXT.__text: 0x162660
-  __TEXT.__auth_stubs: 0x3400
+1674.1.28.402.0
+  __TEXT.__text: 0x1659d0
+  __TEXT.__auth_stubs: 0x3430
   __TEXT.__objc_stubs: 0x31e0
   __TEXT.__objc_methlist: 0x6e0
-  __TEXT.__const: 0xa5b4
+  __TEXT.__const: 0xa5f4
   __TEXT.__cstring: 0x4c6c
-  __TEXT.__oslogstring: 0x61ae
+  __TEXT.__oslogstring: 0x644e
   __TEXT.__objc_methtype: 0xc4f
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x3254
-  __TEXT.__swift5_typeref: 0x35a4
+  __TEXT.__constg_swiftt: 0x324c
+  __TEXT.__swift5_typeref: 0x35de
   __TEXT.__swift5_builtin: 0x1a4
-  __TEXT.__swift5_reflstr: 0x3018
+  __TEXT.__swift5_reflstr: 0x3008
   __TEXT.__swift5_assocty: 0xa18
-  __TEXT.__swift5_capture: 0x3884
-  __TEXT.__swift5_fieldmd: 0x37fc
+  __TEXT.__swift5_capture: 0x3d20
+  __TEXT.__swift5_fieldmd: 0x3814
   __TEXT.__swift5_proto: 0x7d0
   __TEXT.__swift5_types: 0x35c
-  __TEXT.__objc_classname: 0xa54
-  __TEXT.__objc_methname: 0x439f
+  __TEXT.__objc_classname: 0xa44
+  __TEXT.__objc_methname: 0x4332
   __TEXT.__swift5_protos: 0x58
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__info_plist: 0xfd
-  __TEXT.__unwind_info: 0x5440
-  __TEXT.__eh_frame: 0x27e4
-  __DATA_CONST.__const: 0xe670
+  __TEXT.__unwind_info: 0x5478
+  __TEXT.__eh_frame: 0x2804
+  __DATA_CONST.__const: 0xf1d8
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__auth_got: 0x1a08
-  __DATA_CONST.__got: 0x918
+  __DATA_CONST.__auth_got: 0x1a20
+  __DATA_CONST.__got: 0x910
   __DATA_CONST.__auth_ptr: 0xca0
-  __DATA.__objc_const: 0x3388
+  __DATA.__objc_const: 0x3348
   __DATA.__objc_selrefs: 0xea8
   __DATA.__objc_data: 0x870
-  __DATA.__data: 0x6fa0
-  __DATA.__common: 0x400
+  __DATA.__data: 0x6fc8
+  __DATA.__common: 0x418
   __DATA.__bss: 0xe588
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8900
-  Symbols:   1289
-  CStrings:  1698
+  Functions: 9000
+  Symbols:   1291
+  CStrings:  1703
 
Symbols:
+ _$s10Foundation4DateV2geoiySbAC_ACtFZ
+ _$s10Foundation4DateV2leoiySbAC_ACtFZ
+ _$ss18_DictionaryStorageC4copy8originalAByxq_Gs05__RawaB0C_tFZ
+ _sqlite3_wal_checkpoint_v2
- _$s10Foundation4DateVSLAAMc
- _$sSL2geoiySbx_xtFZTj
CStrings:
+ "Application %{public}s set dock badge count to %ld"
+ "Asking UserNotifications client %{public}s:pid=%d about presenting notification"
+ "Delivering %{public}s to %{public}s without presentation, just updating existing record."
+ "Delivering %{public}s to %{public}s without presentation."
+ "Delivering %{public}s to %{public}s: askBeforePresenting: %{bool,public}d, effectiveStyle: %{public}s, hasSound: %{bool,public}d, shouldPresent: %{bool,public}d"
+ "Presentation reply %{public}s: %{public}s"
+ "Sending request for permission for %{public}s with path %{public}s, authorizations: %{public}s, criticalOnly: %{bool,public}d"
+ "Unable to truncate wal: %{public}d"
+ "UserNotifications app setBadgeNumber to %s for %{public}s"
+ "actually deliver %{public}s: deliveredChanged: %{bool,public}d, alertsChanged: %{bool,public}d, shouldPresent: %{bool,public}d, askBeforePresenting: %{bool,public}d"
+ "set Dock badge: %ld for %{public}s"
- "Asking UserNotifications client %{public}s:pid: %d about presenting notification"
- "Delivering %{public}s to %{public}s: updatedExisting: %{bool,public}d"
- "Presentation reply %{public}s %{public}s"
- "Sending request for permission for %{public}s with path %{public}s"
- "_sortedApplicationIdentifiers"
- "_vacuumTimer"
```
